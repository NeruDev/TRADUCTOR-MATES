"""
---
file: src/ui/components/constant_card.py
module: src.ui.components.constant_card
description: Componente de tarjeta visual para constantes matemáticas y físicas con selector contextual de precisión.
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
  - ConstantCardWidget: "Tarjeta interactiva para insertar constantes numéricas con precisión configurable"
test: pytest tests/test_editor_widget.py
constraints:
  - "Formatear números decimales sin pérdida de precisión ni artefactos en valores pequeños"
keywords:
  - constant-card
  - math-constants
  - precision-decimals
  - context-menu
  - card-widget
---

Interactive Visual Constant Card Component with Configurable Precision.
"""

from __future__ import annotations

from PySide6.QtCore import QPoint, QSize, Qt, Signal
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMenu,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QWidgetAction,
)

from src.ui.components.svg_cache import SVGMathCache
from src.ui.theme import get_theme_dict


class ConstantCardWidget(QFrame):
    """Tarjeta interactiva para insertar constantes con precisión ajustable.

    Args:
        name: Nombre descriptivo de la constante.
        symbol_latex: Símbolo matemático en código LaTeX.
        full_value: Valor numérico completo de alta precisión.
        current_theme: Nombre del tema activo ('dark' o 'light').
        parent: Widget contenedor padre opcional.

    Attributes:
        clicked_value: Señal emitida con el valor numérico al pulsar la tarjeta.
    """

    clicked_value = Signal(str)

    def __init__(
        self,
        name: str,
        symbol_latex: str,
        full_value: str,
        current_theme: str = "dark",
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.name = name
        self.symbol_latex = symbol_latex.strip("$")
        self.full_value = full_value
        self.decimals: int = 9
        self.current_theme = current_theme
        self.current_formatted_value: str = full_value

        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setToolTip("Clic derecho para ajustar decimales")

        self.setMinimumWidth(160)
        self.setMinimumHeight(130)

        t = get_theme_dict(current_theme)
        card_bg = t.get("bg_item_card", t["surface_variant"])
        card_hover = t.get("bg_item_card_hover", t["surface"])
        border_col = t.get("border_subtle", t["border"])

        self.setStyleSheet(f"""
            ConstantCardWidget {{
                background-color: {card_bg};
                border: 1px solid {border_col};
                border-radius: 8px;
            }}
            ConstantCardWidget:hover {{
                border-color: {t["primary"]};
                background-color: {card_hover};
            }}
        """)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(6, 6, 6, 6)
        self.main_layout.setSpacing(4)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # SVG Symbol
        self.lbl_art = QLabel()
        self.lbl_art.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_art.setScaledContents(False)
        self.lbl_art.setMinimumSize(QSize(100, 50))
        self.lbl_art.setStyleSheet("background: transparent; border: none;")

        math_fg = t.get("text_rendered_math", t["text_primary"])
        pixmap = SVGMathCache.get_instance().get_svg_icon(self.symbol_latex, math_fg)
        self.lbl_art.setPixmap(pixmap)

        # Name label
        self.lbl_name = QLabel(self.name)
        self.lbl_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_name.setWordWrap(True)
        self.lbl_name.setStyleSheet(
            f"font-size: 11px; font-weight: bold; color: {t['text_primary']}; "
            "background: transparent; border: none;"
        )

        # Value label
        self.lbl_value = QLabel()
        self.lbl_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_value.setStyleSheet(
            f"font-size: 10px; color: {t['text_secondary']}; "
            "background: transparent; border: none;"
        )
        self._update_value_label()

        self.main_layout.addWidget(self.lbl_art)
        self.main_layout.addWidget(self.lbl_name)
        self.main_layout.addWidget(self.lbl_value)

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)

    def _update_value_label(self) -> None:
        """Formatea el valor numérico truncado según la cantidad de decimales configurada."""
        parts = self.full_value.split(".")
        if len(parts) == 2 and self.decimals > 0:
            formatted_value = f"{parts[0]}.{parts[1][: self.decimals]}"
        elif self.decimals == 0:
            formatted_value = parts[0]
        else:
            formatted_value = self.full_value

        if len(self.full_value) > len(formatted_value):
            self.lbl_value.setText(f"{formatted_value}...")
        else:
            self.lbl_value.setText(formatted_value)

        self.current_formatted_value = formatted_value

    def _show_context_menu(self, pos: QPoint) -> None:
        """Despliega el menú contextual con control spinbox de decimales.

        Args:
            pos: Coordenadas relativas del clic del usuario.
        """
        menu = QMenu(self)
        t = get_theme_dict(self.current_theme)
        menu.setStyleSheet(f"""
            QMenu {{
                background-color: {t["surface"]};
                color: {t["text_primary"]};
                border: 1px solid {t["border"]};
                border-radius: 8px;
                padding: 4px;
            }}
            QLabel {{
                color: {t["text_primary"]};
                font-size: 12px;
            }}
        """)

        action = QWidgetAction(menu)
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(8, 4, 8, 4)

        lbl = QLabel("Decimales:")
        spin = QSpinBox()
        spin.setRange(0, 32)
        spin.setValue(self.decimals)
        spin.setStyleSheet(f"""
            QSpinBox {{
                background-color: {t["surface_variant"]};
                color: {t["text_primary"]};
                border: 1px solid {t["border"]};
                border-radius: 4px;
                padding: 2px;
                min-width: 50px;
            }}
        """)

        layout.addWidget(lbl)
        layout.addWidget(spin)

        def on_change(val: int) -> None:
            self.decimals = val
            self._update_value_label()

        spin.valueChanged.connect(on_change)

        action.setDefaultWidget(widget)
        menu.addAction(action)

        menu.exec_(self.mapToGlobal(pos))

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Emite el valor formateado al hacer clic izquierdo."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked_value.emit(self.current_formatted_value)
        super().mousePressEvent(event)
