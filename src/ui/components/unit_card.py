"""
---
file: src/ui/components/unit_card.py
module: src.ui.components.unit_card
description: Componente de tarjeta visual para unidades físicas del SI y magnitudes dimensionales.
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
  - UnitCardWidget: "Tarjeta interactiva para insertar unidades físicas y magnitudes dimensionales"
test: pytest tests/test_editor_widget.py
constraints:
  - "Visualizar correctamente las dimensiones y la abreviatura de cada unidad física"
keywords:
  - unit-card
  - physical-units
  - international-system
  - dimensions
  - engineering-units
---

Interactive Visual Physical Unit Card Component.
"""

from __future__ import annotations

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget

from src.ui.components.svg_cache import SVGMathCache
from src.ui.theme import get_theme_dict


class UnitCardWidget(QFrame):
    """Tarjeta interactiva para insertar unidades físicas.

    Args:
        magnitude: Magnitud física (e.g. Longitud, Fuerza).
        name: Nombre de la unidad (e.g. Metro, Newton).
        symbol_latex: Símbolo matemático en código LaTeX.
        base_latex: Expresión de desglose dimensional base.
        current_theme: Nombre del tema activo ('dark' o 'light').
        parent: Widget contenedor padre opcional.

    Attributes:
        clicked_unit: Señal emitida con el código LaTeX al pulsar la unidad.
    """

    clicked_unit = Signal(str)

    def __init__(
        self,
        magnitude: str,
        name: str,
        symbol_latex: str,
        base_latex: str,
        current_theme: str = "dark",
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.magnitude = magnitude
        self.name = name
        self.symbol_latex = symbol_latex.strip("$")
        self.base_latex = base_latex.strip("$")
        self.current_theme = current_theme

        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setToolTip("Clic para insertar unidad")

        self.setMinimumWidth(160)
        self.setMinimumHeight(130)

        t = get_theme_dict(current_theme)
        card_bg = t.get("bg_item_card", t["surface_variant"])
        card_hover = t.get("bg_item_card_hover", t["surface"])
        border_col = t.get("border_subtle", t["border"])

        self.setStyleSheet(f"""
            UnitCardWidget {{
                background-color: {card_bg};
                border: 1px solid {border_col};
                border-radius: 8px;
            }}
            UnitCardWidget:hover {{
                border-color: {t["primary"]};
                background-color: {card_hover};
            }}
        """)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(6, 6, 6, 6)
        self.main_layout.setSpacing(4)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # SVG Symbol and Base
        self.lbl_art = QLabel()
        self.lbl_art.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_art.setScaledContents(False)
        self.lbl_art.setMinimumSize(QSize(100, 50))
        self.lbl_art.setStyleSheet("background: transparent; border: none;")

        math_fg = t.get("text_rendered_math", t["text_primary"])

        if self.base_latex:
            display_latex = (
                f"{self.symbol_latex} \\, {self.base_latex}"
                if self.symbol_latex
                else self.base_latex
            )
        else:
            display_latex = self.symbol_latex

        pixmap = SVGMathCache.get_instance().get_svg_icon(display_latex, math_fg)
        self.lbl_art.setPixmap(pixmap)

        # Magnitude label
        self.lbl_mag = QLabel(self.magnitude)
        self.lbl_mag.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_mag.setWordWrap(True)
        self.lbl_mag.setStyleSheet(
            f"font-size: 11px; font-weight: bold; color: {t['text_primary']}; "
            "background: transparent; border: none;"
        )

        # Name label
        self.lbl_name = QLabel(self.name)
        self.lbl_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_name.setWordWrap(True)
        self.lbl_name.setStyleSheet(
            f"font-size: 10px; color: {t['text_secondary']}; "
            "background: transparent; border: none;"
        )

        self.main_layout.addWidget(self.lbl_mag)
        self.main_layout.addWidget(self.lbl_name)
        self.main_layout.addWidget(self.lbl_art)

        self.display_latex = display_latex

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Emite la unidad seleccionada al hacer clic."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked_unit.emit(self.display_latex)
        super().mousePressEvent(event)
