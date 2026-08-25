"""
---
file: src/ui/components/template_card.py
module: src.ui.components.template_card
description: Componente de tarjeta visual interactiva para opciones de plantillas matemáticas.
type: ui/component
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.ui.theme
  - src.ui.components.svg_cache
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/palette_widget.py
exports:
  - TemplateCardOption: "Tarjeta visual para opciones de plantillas estructuradas"
test: pytest tests/test_editor_widget.py
constraints:
  - "Renderizar iconos SVG con dimensiones compactas y feedback al pasar el ratón"
keywords:
  - template-card
  - template-option
  - svg-icon
  - card-widget
---

Word-style template option card displaying SVG Icon.
"""

from __future__ import annotations

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout

from src.ui.components.svg_cache import SVGMathCache
from src.ui.theme import get_theme_dict


class TemplateCardOption(QFrame):
    """Tarjeta interactiva para seleccionar una plantilla matemática.

    Consiste de una representación vectorial SVG extraída en tiempo real
    y un texto inferior con la descripción. Soporta clics como botón.
    """

    clicked = Signal()

    def __init__(
        self,
        latex: str,
        label_text: str,
        description: str = "",
        current_theme: str = "dark",
        parent=None,
    ):
        super().__init__(parent)
        self.latex = latex
        self.current_theme = current_theme

        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setToolTip(description or label_text)

        self.setMinimumWidth(140)
        self.setMinimumHeight(120)

        t = get_theme_dict(current_theme)
        card_bg = t.get("bg_item_card", t["surface_variant"])
        card_hover = t.get("bg_item_card_hover", t["surface"])
        border_col = t.get("border_subtle", t["border"])

        self.setStyleSheet(f"""
            TemplateCardOption {{
                background-color: {card_bg};
                border: 1px solid {border_col};
                border-radius: 8px;
            }}
            TemplateCardOption:hover {{
                border-color: {t["primary"]};
                background-color: {card_hover};
            }}
        """)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(6, 6, 6, 6)
        self.main_layout.setSpacing(2)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lbl_art = QLabel()
        self.lbl_art.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_art.setScaledContents(False)
        self.lbl_art.setMinimumSize(QSize(100, 60))
        self.lbl_art.setStyleSheet("background: transparent; border: none;")

        # Solicitar el gráfico síncrono a MathJax con el color de contraste del tema
        math_fg = t.get("text_rendered_math", t["text_primary"])
        pixmap = SVGMathCache.get_instance().get_svg_icon(self.latex, math_fg)

        # Asignar el gráfico a la interfaz
        self.lbl_art.setPixmap(pixmap)

        self.lbl_text = QLabel(label_text)
        self.lbl_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_text.setStyleSheet(
            f"font-size: 10px; color: {t['text_secondary']}; "
            "background: transparent; border: none;"
        )

        self.main_layout.addWidget(self.lbl_art)
        self.main_layout.addWidget(self.lbl_text)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)
