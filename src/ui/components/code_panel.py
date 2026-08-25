"""
---
file: src/ui/components/code_panel.py
module: src.ui.components.code_panel
description: Panel de traducción a código LaTeX y Markdown con resaltado sintáctico, menú de fuentes y Toast.
type: ui/component
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
  - src.core.parser
  - src.core.syntax
  - src.core.translator
relations:
  - docs/ARCHITECTURE.md
  - src/ui/main_window.py
exports:
  - CodeTranslationPanel: "Panel de salida con pestañas para código LaTeX y bloques Markdown"
test: pytest tests/test_editor_widget.py
constraints:
  - "Aplicar debounce en la edición bidireccional de LaTeX para evitar re-renderizados costosos innecesarios"
keywords:
  - code-panel
  - latex-translation
  - markdown-export
  - syntax-highlighter
  - toast-notification
---

LaTeX Code Translation Panel with Markdown formatting & Android Toast Copy
Displays raw LaTeX output, Markdown code block, syntax highlighting, font size menu, and copy actions.
"""

from __future__ import annotations

import pyperclip
from PySide6.QtCore import Qt, QTimer, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from src.core.ast import MathTree
from src.core.syntax import LaTeXSyntaxHighlighter
from src.core.translator import LaTeXTranslator
from src.ui.theme import COLOR_MIKU_CYAN, get_theme_dict


class CodeTranslationPanel(QFrame):
    """Panel visualizador y editor bidireccional del código de la fórmula con control tipográfico.

    Integra pestañas interactivas con `QSyntaxHighlighter` para el código
    LaTeX crudo y bloque Markdown, además de selector de tamaño de fuente.
    """

    latex_edited = Signal(str)

    def __init__(self, math_tree: MathTree, parent=None):
        super().__init__(parent)
        self.math_tree = math_tree
        self.setProperty("class", "android-card")
        self._is_updating = False
        self.current_theme = "dark"
        self.current_font_size = 16

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(10)

        # Header with Title, Font Size Selector and Toast notification
        header_layout = QHBoxLayout()
        header_layout.setSpacing(6)
        title = QLabel("Traductor de Código Multilenguaje")
        title.setProperty("class", "section-header")

        # Font size dropdown (Word style: default 16 pt)
        self.size_container = QWidget()
        size_layout = QHBoxLayout(self.size_container)
        size_layout.setContentsMargins(0, 0, 0, 0)
        size_layout.setSpacing(4)

        self.lbl_font_size = QLabel("Tamaño:")

        self.combo_font_size = QComboBox()
        self.combo_font_size.setCursor(Qt.PointingHandCursor)
        self.font_sizes = [10, 11, 12, 13, 14, 16, 18, 20, 24, 28, 32]
        for s in self.font_sizes:
            self.combo_font_size.addItem(f"{s} pt", s)

        # Default to 16 pt (Word style)
        idx_16 = self.font_sizes.index(16) if 16 in self.font_sizes else 0
        self.combo_font_size.setCurrentIndex(idx_16)
        self.combo_font_size.currentIndexChanged.connect(self._on_font_size_changed)

        size_layout.addWidget(self.lbl_font_size)
        size_layout.addWidget(self.combo_font_size)

        self.toast = QLabel("¡Copiado al portapapeles! ✓")
        self.toast.setProperty("class", "toast-label")
        self.toast.hide()

        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(self.size_container)
        header_layout.addWidget(self.toast)
        layout.addLayout(header_layout)

        # Tabs for LaTeX Raw vs Markdown Block
        self.tabs = QTabWidget()

        # Tab 1: Raw LaTeX
        self.latex_edit = QPlainTextEdit()
        self.latex_edit.setReadOnly(False)  # Editable
        self.latex_highlighter = LaTeXSyntaxHighlighter(
            self.latex_edit.document(), theme=self.current_theme
        )
        self.tabs.addTab(self.latex_edit, r"LaTeX (\dots)")

        # Timer for Debounce
        self.parse_timer = QTimer(self)
        self.parse_timer.setSingleShot(True)
        self.parse_timer.setInterval(500)
        self.parse_timer.timeout.connect(self._on_parse_timeout)
        self.latex_edit.textChanged.connect(self._on_text_changed)

        # Tab 2: Markdown Code Block
        self.markdown_edit = QPlainTextEdit()
        self.markdown_edit.setReadOnly(True)
        self.markdown_highlighter = LaTeXSyntaxHighlighter(
            self.markdown_edit.document(), theme=self.current_theme
        )
        self.tabs.addTab(self.markdown_edit, r"Markdown ($$ \dots $$)")

        layout.addWidget(self.tabs)

        # Copy Action Bar
        btn_layout = QHBoxLayout()

        self.btn_copy_latex = QPushButton("Copiar LaTeX")
        self.btn_copy_latex.setProperty("class", "action-btn")
        self.btn_copy_latex.setCursor(Qt.PointingHandCursor)
        self.btn_copy_latex.clicked.connect(self._copy_latex)

        self.btn_copy_markdown = QPushButton("Copiar Markdown")
        self.btn_copy_markdown.setProperty("class", "action-btn-secondary")
        self.btn_copy_markdown.setCursor(Qt.PointingHandCursor)
        self.btn_copy_markdown.clicked.connect(self._copy_markdown)

        btn_layout.addWidget(self.btn_copy_latex)
        btn_layout.addWidget(self.btn_copy_markdown)
        btn_layout.addStretch()

        layout.addLayout(btn_layout)

        # Apply Styles and Font
        self._apply_font_size(self.current_font_size)
        self._update_tab_style()

        # Initialize content
        self.update_translation()

    def _apply_font_size(self, size: int) -> None:
        """Aplica el tamaño de fuente a los editores de texto de traducción.

        Args:
            size: Tamaño en puntos (pt) a aplicar a la tipografía monoespaciada.
        """
        self.current_font_size = size
        font = QFont("Cascadia Code", size)
        font.setStyleHint(QFont.Monospace)
        self.latex_edit.setFont(font)
        self.latex_edit.document().setDefaultFont(font)
        self.markdown_edit.setFont(font)
        self.markdown_edit.document().setDefaultFont(font)
        self._update_editor_style()

    def _update_editor_style(self) -> None:
        """Actualiza los estilos visuales y escala tipográfica de los editores."""
        t = get_theme_dict(self.current_theme)
        code_bg = t.get("code_bg", "#0D0D14")
        text_color = t.get("text_primary", "#F8FAFC")
        border_col = t.get("border", "#2E3144")
        accent = t.get("primary", COLOR_MIKU_CYAN)
        size = self.current_font_size

        editor_qss = f"""
            QPlainTextEdit {{
                background-color: {code_bg};
                color: {text_color};
                font-family: 'Cascadia Code', 'Consolas', 'Courier New', monospace;
                font-size: {size}pt;
                border: 1px solid {border_col};
                border-radius: 12px;
                padding: 10px;
                selection-background-color: {accent};
            }}
        """
        self.latex_edit.setStyleSheet(editor_qss)
        self.markdown_edit.setStyleSheet(editor_qss)

    def _on_font_size_changed(self, index: int = 0):
        """Manejador de evento para cambio de tipografía."""
        size = self.combo_font_size.currentData()
        try:
            size_int = int(size)
        except (TypeError, ValueError):
            size_int = 16
        if size_int <= 0:
            size_int = 16
        self._apply_font_size(size_int)

    def _update_tab_style(self) -> None:
        """Actualiza los estilos de las pestañas y selector según el tema activo."""
        t = get_theme_dict(self.current_theme)
        accent = t.get("math_box_border", COLOR_MIKU_CYAN)
        pane_bg = t.get("surface", "#101016")
        tab_bg = t.get("surface_variant", "#202030")
        tab_color = t.get("text_secondary", "#9E9EB3")
        border_col = t.get("border", "#32324A")
        combo_fg = t.get("text_primary", "#F8FAFC")

        self.tabs.setStyleSheet(f"""
            QTabWidget::pane {{
                border: 1px solid {border_col};
                border-radius: 10px;
                background-color: {pane_bg};
            }}
            QTabBar::tab {{
                background: {tab_bg};
                color: {tab_color};
                padding: 6px 14px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                margin-right: 4px;
            }}
            QTabBar::tab:selected {{
                background: {accent};
                color: #FFFFFF;
                font-weight: bold;
            }}
        """)

        self.lbl_font_size.setStyleSheet(
            f"font-size: 11px; font-weight: bold; color: {t['primary']};"
        )
        self.combo_font_size.setStyleSheet(f"""
            QComboBox {{
                background-color: {tab_bg};
                color: {combo_fg};
                border: 1px solid {t["primary"]};
                border-radius: 6px;
                padding: 3px 8px;
                font-size: 11px;
                font-weight: 600;
                min-width: 60px;
            }}
            QComboBox:hover {{
                border-color: {t["secondary"]};
            }}
            QComboBox QAbstractItemView {{
                background-color: {pane_bg};
                color: {combo_fg};
                selection-background-color: {t["primary"]};
                selection-color: #FFFFFF;
                border: 1px solid {t["primary"]};
                border-radius: 6px;
                padding: 4px;
            }}
        """)

        btn_latex_style = f"""
            QPushButton {{
                background-color: {t["primary"]};
                color: #FFFFFF;
                border: none;
                border-radius: 8px;
                padding: 6px 16px;
                font-size: 12px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: {t["primary_hover"]};
            }}
        """
        btn_markdown_style = f"""
            QPushButton {{
                background-color: {t["secondary"]};
                color: #FFFFFF;
                border: none;
                border-radius: 8px;
                padding: 6px 16px;
                font-size: 12px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: {t["secondary_hover"]};
            }}
        """
        self.btn_copy_latex.setStyleSheet(btn_latex_style)
        self.btn_copy_markdown.setStyleSheet(btn_markdown_style)

    def set_theme(self, theme: str) -> None:
        """Actualiza el resaltador de sintaxis y los estilos según el tema activo.

        Args:
            theme: Identificador del tema ('dark' o 'light').
        """
        self.current_theme = theme
        self._update_tab_style()
        self._update_editor_style()
        self.latex_highlighter.set_theme(theme)
        self.markdown_highlighter.set_theme(theme)

    def _on_text_changed(self) -> None:
        """Inicia el temporizador de retardo cuando el usuario introduce texto."""
        if not self._is_updating:
            self.parse_timer.start()

    def _on_parse_timeout(self) -> None:
        """Emite la señal de texto LaTeX editado tras la expiración del temporizador."""
        text = self.latex_edit.toPlainText().strip()
        if text and not text.startswith("%"):
            self.latex_edited.emit(text)

    def update_translation(self) -> None:
        """Actualiza el texto LaTeX y Markdown basándose en el estado de `MathTree`.

        Activa temporalmente un semáforo interno para evitar disparar
        cíclicamente las señales de edición por software.
        """
        self._is_updating = True
        latex_text = LaTeXTranslator.to_latex(self.math_tree)
        md_text = LaTeXTranslator.to_markdown_block(self.math_tree)

        self.latex_edit.setPlainText(latex_text if latex_text else "% (Fórmula vacía)")
        self.markdown_edit.setPlainText(md_text)
        self._is_updating = False

    def _copy_latex(self) -> None:
        """Copia el texto actual del editor LaTeX al portapapeles."""
        text = self.latex_edit.toPlainText()
        self._copy_to_clipboard(text, "LaTeX")

    def _copy_markdown(self) -> None:
        """Copia el texto actual del editor Markdown al portapapeles."""
        text = self.markdown_edit.toPlainText()
        self._copy_to_clipboard(text, "Markdown")

    def _copy_to_clipboard(self, text: str, label: str) -> None:
        """Copia texto al portapapeles del sistema y despliega notificación Toast.

        Args:
            text: Contenido textual a transferir al portapapeles.
            label: Etiqueta descriptiva del formato transferido ('LaTeX' o 'Markdown').
        """
        try:
            pyperclip.copy(text)
        except Exception:  # noqa: BLE001
            QApplication.clipboard().setText(text)

        self.toast.setText(f"¡Copiado {label}! ✓")
        self.toast.show()
        QTimer.singleShot(2200, self.toast.hide)
