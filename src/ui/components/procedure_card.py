"""
---
file: src/ui/components/procedure_card.py
module: src.ui.components.procedure_card
description: Tarjeta interactiva con carrusel para agrupar fórmulas y variaciones de procedimientos.
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
  - ProcedureCardWidget: "Tarjeta interactiva que agrupa variaciones con carrusel"
test: pytest tests/test_editor_widget.py
constraints:
  - "Navegar circularmente por las variantes sin estados inconsistentes"
keywords:
  - procedure-card
  - formula-variations
  - carousel-widget
  - procedure-steps
---

Procedural Formula Card Component with Interactive Carousel Controls.
"""

from __future__ import annotations

from typing import Any

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from src.ui.components.svg_cache import SVGMathCache
from src.ui.theme import COLOR_MIKU_CYAN, get_theme_dict


class ProcedureCardWidget(QFrame):
    """Tarjeta interactiva que agrupa variaciones de fórmulas con carrusel.

    Args:
        group_data: Diccionario con el título del procedimiento y lista de variaciones.
        current_theme: Nombre del tema activo ('dark' o 'light').
        parent: Widget contenedor padre opcional.

    Attributes:
        latex_selected: Señal emitida con el código LaTeX al seleccionar la tarjeta.
    """

    latex_selected = Signal(str)

    def __init__(
        self,
        group_data: dict[str, Any],
        current_theme: str,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.group_data = group_data
        self.current_theme = current_theme
        self.variations = group_data.get("variations", [])
        self.current_index: int = 0

        # Styles
        t = get_theme_dict(self.current_theme)
        self.card_bg = t.get("bg_item_card", t["surface_variant"])
        self.card_hover = t.get("bg_item_card_hover", t["surface"])
        self.border_col = t.get("border_subtle", t["border"])
        self.math_fg = t.get("text_rendered_math", t["text_primary"])
        self.primary_col = t.get("primary", COLOR_MIKU_CYAN)

        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(76)
        self.setStyleSheet(f"""
            ProcedureCardWidget {{
                background-color: {self.card_bg};
                border: 1px solid {self.border_col};
                border-radius: 8px;
            }}
            ProcedureCardWidget:hover {{
                border-color: {self.primary_col};
                background-color: {self.card_hover};
            }}
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 8, 10, 8)
        main_layout.setSpacing(6)

        # Header: Title + Carousel controls
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)

        self.lbl_title = QLabel()
        self.lbl_title.setStyleSheet(
            f"font-size: 12px; font-weight: 700; color: {self.primary_col}; "
            "border: none; background: transparent;"
        )
        header_layout.addWidget(self.lbl_title)

        header_layout.addStretch()

        # Carousel controls (only if > 1 variation)
        self.carousel_widget = QWidget()
        car_layout = QHBoxLayout(self.carousel_widget)
        car_layout.setContentsMargins(0, 0, 0, 0)
        car_layout.setSpacing(4)

        btn_style = f"""
            QPushButton {{
                background-color: {t["surface"]};
                color: {t["text_primary"]};
                border: 1px solid {self.border_col};
                border-radius: 4px;
                padding: 2px 6px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                border-color: {self.primary_col};
                color: {self.primary_col};
            }}
        """

        self.btn_prev = QPushButton("<")
        self.btn_prev.setStyleSheet(btn_style)
        self.btn_prev.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_prev.clicked.connect(self._prev_variation)
        car_layout.addWidget(self.btn_prev)

        self.lbl_counter = QLabel("1/1")
        self.lbl_counter.setStyleSheet(
            f"font-size: 11px; font-weight: bold; color: {t['text_secondary']}; "
            "border: none; background: transparent;"
        )
        car_layout.addWidget(self.lbl_counter)

        self.btn_next = QPushButton(">")
        self.btn_next.setStyleSheet(btn_style)
        self.btn_next.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_next.clicked.connect(self._next_variation)
        car_layout.addWidget(self.btn_next)

        header_layout.addWidget(self.carousel_widget)
        main_layout.addLayout(header_layout)

        # Center/Bottom: Formula Name (Sub) + Rendered SVG Formula
        body_layout = QVBoxLayout()
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(4)

        self.lbl_var_name = QLabel()
        self.lbl_var_name.setStyleSheet(
            f"font-size: 11px; font-weight: 600; color: {t['text_primary']}; "
            "border: none; background: transparent;"
        )
        self.lbl_var_name.setWordWrap(True)
        body_layout.addWidget(self.lbl_var_name)

        self.lbl_icon = QLabel()
        self.lbl_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon.setStyleSheet("border: none; background: transparent;")
        body_layout.addWidget(self.lbl_icon)

        main_layout.addLayout(body_layout)

        if len(self.variations) <= 1:
            self.carousel_widget.hide()

        self._update_ui()

    def _update_ui(self) -> None:
        """Actualiza los textos, el contador y el icono SVG de la variante activa."""
        if not self.variations:
            return

        var = self.variations[self.current_index]

        self.lbl_title.setText(self.group_data["title"])
        self.lbl_var_name.setText(var["name"])
        self.setToolTip(var.get("description", var["name"]))

        self.lbl_counter.setText(f"{self.current_index + 1}/{len(self.variations)}")

        pixmap = SVGMathCache.get_instance().get_svg_icon(
            var["latex"], self.math_fg, width=220, height=52
        )
        self.lbl_icon.setPixmap(pixmap)

    def _prev_variation(self) -> None:
        """Retrocede a la variante anterior del carrusel."""
        if self.variations:
            self.current_index = (self.current_index - 1) % len(self.variations)
            self._update_ui()

    def _next_variation(self) -> None:
        """Avanza a la siguiente variante del carrusel."""
        if self.variations:
            self.current_index = (self.current_index + 1) % len(self.variations)
            self._update_ui()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Captura el clic para emitir la fórmula LaTeX seleccionada."""
        if event.button() == Qt.MouseButton.LeftButton and self.variations:
            latex_str = self.variations[self.current_index]["latex"]
            self.latex_selected.emit(latex_str)
        super().mousePressEvent(event)
