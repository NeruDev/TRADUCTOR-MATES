"""
---
file: src/ui/main_window.py
module: src.ui.main_window
description: Ventana principal de la aplicación con layout equilibrado en 4 cuadrantes (25% cada uno), splitters interactivos y gestión de temas.
type: ui/component
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
  - src.core.logger
  - src.core.parser
  - src.core.translator
  - src.data.symbols
  - src.ui.theme
  - src.ui.components.action_bar
  - src.ui.components.code_panel
  - src.ui.components.editor_widget
  - src.ui.components.palette_widget
  - src.ui.components.preview_panel
  - src.ui.components.save_formula_dialog
  - src.utils.recovery_manager
  - src.utils.user_formulas_manager
relations:
  - main.py
  - docs/ARCHITECTURE.md
exports:
  - MainWindow: "Ventana principal integradora de los 4 paneles de la aplicación en cuadrantes 2x2"
test: pytest tests/test_editor_widget.py
constraints:
  - "Mantener la proporción 25% equitativa entre los 4 paneles principales en showEvent"
  - "Garantizar la persistencia y limpieza segura de recuperación de sesión en closeEvent"
keywords:
  - main-window
  - quadrant-layout
  - qsplitter
  - theme-toggle
  - ast-sync
  - pyside6
---

Main Window for Traductor Mates Application.
Integrates the 4-panel interactive layout with 2 vertical splitters + 1 main horizontal splitter,
balanced 25% quadrant distribution, crash recovery, and Hatsune Miku Dark/Light theme switching.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent, QShowEvent
from PySide6.QtWidgets import QMainWindow, QSizePolicy, QSplitter, QVBoxLayout, QWidget

from src.core.ast import MathNode, MathTree
from src.core.logger import capture_error, get_logger
from src.core.parser import LaTeXParser
from src.core.translator import LaTeXTranslator
from src.ui.components.action_bar import MathActionBarWidget
from src.ui.components.code_panel import CodeTranslationPanel
from src.ui.components.editor_widget import MathEditorWidget
from src.ui.components.palette_widget import MathPaletteWidget
from src.ui.components.preview_panel import MathPreviewPanel
from src.ui.components.save_formula_dialog import SaveFormulaDialog
from src.ui.theme import get_theme_qss
from src.utils.recovery_manager import RecoveryManager
from src.utils.user_formulas_manager import UserFormulasManager

logger = get_logger()


class MainWindow(QMainWindow):
    """Ventana principal de la aplicación con disposición 2x2 en 4 cuadrantes balanceados.

    Coordina la interactividad entre la barra de herramientas superior, el editor
    matemático visual, la paleta de plantillas, la previsualización SVG y el panel
    de traducción con control tipográfico.
    """

    def __init__(self) -> None:
        super().__init__()
        self.current_theme: str = "dark"
        self.setWindowTitle("Traductor Mates - Editor & Traductor Matemático Visual")
        self.resize(1280, 800)
        self.setMinimumSize(900, 600)

        # Apply Global Theme Stylesheet
        self.setStyleSheet(get_theme_qss(self.current_theme))

        # Initialize AST Root
        self.math_tree = MathTree()
        self.user_formulas_manager = UserFormulasManager()

        # Central Widget & Root Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        root_layout = QVBoxLayout(central_widget)
        root_layout.setContentsMargins(12, 12, 12, 12)
        root_layout.setSpacing(8)

        # 1. Top Action Bar
        self.action_bar = MathActionBarWidget()
        self.action_bar.theme_toggled.connect(self._on_theme_toggled)
        root_layout.addWidget(self.action_bar)

        # 2. Main Horizontal Splitter (Left 2 Panels vs Right 2 Panels)
        self.main_splitter = QSplitter(Qt.Horizontal)
        self.main_splitter.setChildrenCollapsible(False)

        # Left Vertical Splitter (Top: Editor | Bottom: Palette)
        self.left_splitter = QSplitter(Qt.Vertical)
        self.left_splitter.setChildrenCollapsible(False)

        self.editor_widget = MathEditorWidget(self.math_tree)
        self.editor_widget.formula_changed.connect(self._on_formula_changed)
        self.editor_widget.clear_requested.connect(self._on_clear_requested)
        self.editor_widget.save_requested.connect(self._on_save_requested)
        self.editor_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.palette_widget = MathPaletteWidget()
        self.palette_widget.template_selected.connect(self._on_template_inserted)
        self.palette_widget.symbol_selected.connect(self._on_symbol_inserted)
        self.palette_widget.preset_selected.connect(self._on_preset_selected)
        self.palette_widget.latex_selected.connect(self._on_latex_selected)
        self.palette_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.left_splitter.addWidget(self.editor_widget)
        self.left_splitter.addWidget(self.palette_widget)
        self.left_splitter.setSizes([400, 400])
        self.left_splitter.setStretchFactor(0, 1)
        self.left_splitter.setStretchFactor(1, 1)

        self.main_splitter.addWidget(self.left_splitter)

        # Right Vertical Splitter (Top: Preview | Bottom: Code Translation)
        self.right_splitter = QSplitter(Qt.Vertical)
        self.right_splitter.setChildrenCollapsible(False)

        self.preview_panel = MathPreviewPanel(self.math_tree)
        self.preview_panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.code_panel = CodeTranslationPanel(self.math_tree)
        self.code_panel.latex_edited.connect(self._on_latex_edited)
        self.code_panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.right_splitter.addWidget(self.preview_panel)
        self.right_splitter.addWidget(self.code_panel)
        self.right_splitter.setSizes([400, 400])
        self.right_splitter.setStretchFactor(0, 1)
        self.right_splitter.setStretchFactor(1, 1)

        self.main_splitter.addWidget(self.right_splitter)

        # Set equal 50/50 horizontal distribution
        self.main_splitter.setSizes([600, 600])
        self.main_splitter.setStretchFactor(0, 1)
        self.main_splitter.setStretchFactor(1, 1)

        root_layout.addWidget(self.main_splitter, stretch=1)

        # 3. Crash Recovery Integration
        self.recovery_manager = RecoveryManager()
        recovered_latex = self.recovery_manager.load_state()
        if recovered_latex:
            try:
                self.math_tree = LaTeXParser.parse_to_tree(recovered_latex)
                self.editor_widget.math_tree = self.math_tree
                self.code_panel.math_tree = self.math_tree
                self.preview_panel.math_tree = self.math_tree
                self.editor_widget.rebuild_editor()
                self._on_formula_changed()
                logger.info(
                    f"Fórmula recuperada tras cierre inesperado: {recovered_latex}"
                )
            except Exception as e:  # noqa: BLE001
                logger.error(f"[ERR_PARSER_002] Fallo al recuperar fórmula: {e}")

        # 4. Populate User tab
        self.palette_widget.rebuild_user_tab(self.user_formulas_manager)

    def showEvent(self, event: QShowEvent) -> None:
        """Asegura la distribución equitativa (exactamente 25% por cuadrante) al mostrar la ventana."""
        super().showEvent(event)
        w = self.main_splitter.width()
        h = self.main_splitter.height()
        if w > 100:
            self.main_splitter.setSizes([w // 2, w // 2])
        if h > 100:
            self.left_splitter.setSizes([h // 2, h // 2])
            self.right_splitter.setSizes([h // 2, h // 2])

    def closeEvent(self, event: QCloseEvent) -> None:
        """Intercepta el evento de cierre de ventana para limpiar temporales.

        Al cerrarse de forma segura, elimina el estado de recuperación (crash recovery)
        ya que el usuario salió intencionadamente.

        Args:
            event: El evento de cierre de ventana enviado por Qt.
        """
        self.recovery_manager.clear_state()
        event.accept()

    def _on_theme_toggled(self) -> None:
        """Alterna dinámicamente entre el modo Oscuro y Claro.

        Aplica las nuevas hojas de estilo (QSS) globales y notifica a los
        paneles que requieren re-renderizado de sus componentes visuales.
        """
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        self.setStyleSheet(get_theme_qss(self.current_theme))
        self.action_bar.update_theme_ui(self.current_theme)
        self.code_panel.set_theme(self.current_theme)
        self.editor_widget.set_theme(self.current_theme)
        self.palette_widget.update_theme(self.current_theme)
        self.preview_panel.set_theme(self.current_theme)

    def _on_formula_changed(self) -> None:
        """Manejador global ejecutado cada vez que cambia el árbol de la ecuación.

        Sincroniza la previsualización de alta definición, el bloque de código y
        escribe el estado de la fórmula en el archivo de auto-guardado temporal.
        """
        self.code_panel.update_translation()
        latex = LaTeXTranslator.to_latex(self.math_tree)
        self.preview_panel.update_preview(latex)
        self.recovery_manager.save_state(latex)

    @capture_error("PARSER_ERR")
    def _on_latex_edited(self, text: str) -> None:
        """Reconstruye todo el estado de la aplicación a partir de un cambio manual.

        Se ejecuta tras una edición directa del usuario en el panel de texto LaTeX,
        reparseando la sintaxis y renderizando los visuales si no hay errores fatales.

        Args:
            text: La cadena de texto cruda escrita por el usuario.
        """
        try:
            new_tree = LaTeXParser.parse_to_tree(text)
            self.math_tree = new_tree
            self.editor_widget.math_tree = self.math_tree
            self.code_panel.math_tree = self.math_tree
            self.preview_panel.math_tree = self.math_tree
            self.editor_widget.rebuild_editor()
            self.preview_panel.update_preview(text)
        except Exception as e:  # noqa: BLE001
            logger.error(f"[ERR_PARSER_002] Fallo al parsear edición de usuario: {e}")

    @capture_error("UI_ERR")
    def _on_template_inserted(self, node: MathNode) -> None:
        """Inserta una plantilla o subárbol en la casilla activa.

        Args:
            node: Nodo de plantilla matemática o subárbol AST.
        """
        if isinstance(node, MathTree):
            self.math_tree.insert_nodes(node.root_slot.nodes)
        else:
            self.math_tree.insert_node(node)
        self.editor_widget.rebuild_editor()
        self._on_formula_changed()

    @capture_error("UI_ERR")
    def _on_symbol_inserted(self, node: MathNode) -> None:
        """Inserta un símbolo individual en la casilla activa.

        Args:
            node: Nodo de símbolo a insertar.
        """
        self.math_tree.insert_node(node)
        self.editor_widget.rebuild_editor()
        self._on_formula_changed()

    def _on_preset_selected(self, preset_idx: int) -> None:
        """Manejador legado para presets por índice (reemplazado por _on_latex_selected)."""

    @capture_error("PARSER_ERR")
    def _on_latex_selected(self, latex: str) -> None:
        """Carga una fórmula LaTeX completa desde el catálogo.

        Args:
            latex: Cadena en LaTeX de la fórmula seleccionada.
        """
        new_tree = LaTeXParser.parse_to_tree(latex)
        self.math_tree.insert_nodes(new_tree.root_slot.nodes)
        self.editor_widget.rebuild_editor()
        self._on_formula_changed()
        logger.info(f"Fórmula insertada desde paleta: {latex}")

    def _on_save_requested(self) -> None:
        """Abre el diálogo modal para guardar la fórmula actual en el catálogo."""
        latex = self.math_tree.to_latex()
        if not latex.strip():
            return

        dialog = SaveFormulaDialog(self.user_formulas_manager, latex, self)
        if dialog.exec_():
            data = dialog.get_data()
            self.user_formulas_manager.add_formula(
                data["category"],
                data["subcategory"],
                data["name"],
                latex,
                data.get("description", ""),
            )
            self.palette_widget.rebuild_user_tab(self.user_formulas_manager)

    def _on_clear_requested(self) -> None:
        """Limpia el árbol AST completo y resetea el editor y previsualizador."""
        logger.info("El usuario limpió el editor.")
        self.math_tree.clear_all()
        self.editor_widget.rebuild_editor()
        self._on_formula_changed()
