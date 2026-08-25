"""
---
file: src/ui/components/editor_widget.py
module: src.ui.components.editor_widget
description: Editor visual e interactivo de casillas rellenables (Word / Wolfram Alpha Style).
type: ui/component
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
  - src.core.syntax
  - src.ui.theme
  - src.ui.components.bracket_widget
relations:
  - docs/ARCHITECTURE.md
  - src/ui/main_window.py
exports:
  - SlotBoxWidget: "Widget interactivo para casilla vacía o activa [ □ ]"
  - SlotContainerWidget: "Envolvente interactiva para casillas con nodos hijos"
  - MathCanvasWidget: "Lienzo de fondo con retícula sutil y foco visual"
  - MathEditorWidget: "Editor principal interactivo y bidimensional de fórmulas"
test: pytest tests/test_editor_widget.py
constraints:
  - "Garantizar la navegación fluida con teclado (Tab, flechas, retroceso) entre casillas anidadas"
  - "Desacoplar la construcción de widgets gráficos de la manipulación interna de nodos AST"
keywords:
  - editor-widget
  - visual-editor
  - slot-box
  - math-canvas
  - interactive-formula
  - keyboard-navigation
---

Interactive Structural Fill-in Slot Editor Widget (Word / Wolfram Alpha Style)
Renders math nodes recursively in a compact, cohesive typographic layout with relative positioning,
scaled typography matching rendered formulas, syntax highlighting, and vertically adaptive vector brackets.
"""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QKeyEvent, QPainter, QPen
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from src.core.ast import (
    BinomialNode,
    BracketNode,
    ContourIntegralNode,
    DefiniteIntegralNode,
    DerivativeNode,
    DoubleIntegralNode,
    FractionNode,
    IndefiniteIntegralNode,
    LimitNode,
    MathNode,
    MathTree,
    MatrixNode,
    ModularNode,
    NthRootNode,
    OperatorNode,
    PowerNode,
    ProductNode,
    Slot,
    SquareRootNode,
    StyleDecoratorNode,
    SubscriptNode,
    SubSupNode,
    SummationNode,
    SymbolNode,
    TextNode,
    TripleIntegralNode,
)
from src.core.syntax import (
    format_highlighted_html,
)
from src.ui.components.bracket_widget import (
    AdaptiveBracketWidget,
    AdaptiveIntegralWidget,
    AdaptiveRootWidget,
)
from src.ui.theme import COLOR_BORDER, COLOR_MIKU_CYAN, get_theme_dict


class SlotBoxWidget(QFrame):
    """Widget que representa visualmente una casilla vacía `[ □ ]`.

    Es un contenedor clicleable que indica visualmente dónde puede el usuario
    ingresar contenido. Adapta su tamaño tipográfico y paleta cromática Hatsune Miku.
    """

    clicked = Signal(object)

    def __init__(
        self,
        slot: Slot,
        is_active: bool = False,
        font_size: int = 24,
        theme: str = "dark",
        parent=None,
    ):
        super().__init__(parent)
        self.slot = slot
        self.is_active = is_active
        self.current_theme = theme
        t = get_theme_dict(theme)

        self.setCursor(Qt.PointingHandCursor)
        self.setFocusPolicy(Qt.NoFocus)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(3, 1, 3, 1)
        layout.setSpacing(0)

        symbol = "■" if is_active else "□"
        self.lbl = QLabel(symbol)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        symbol_color = (
            t.get("math_box_border", COLOR_MIKU_CYAN)
            if is_active
            else t.get("math_delim_color", "#828DA4")
        )
        box_font = max(1, int(font_size * 0.72))
        self.lbl.setStyleSheet(
            f"color: {symbol_color}; font-weight: bold; font-size: {box_font}px; margin: 0px; padding: 0px;"
        )
        layout.addWidget(self.lbl)

        self.setObjectName(f"SlotBox_{id(self)}")
        min_w = int(24 * (font_size / 24.0))
        max_w = int(44 * (font_size / 24.0))
        min_h = int(32 * (font_size / 24.0))
        max_h = int(44 * (font_size / 24.0))

        if is_active:
            border_color = t.get("math_box_border", COLOR_MIKU_CYAN)
            bg_color = t.get("math_box_bg_active", "rgba(57, 197, 187, 0.22)")
            self.setStyleSheet(f"""
                QFrame#{self.objectName()} {{
                    background-color: {bg_color};
                    border: 2px solid {border_color};
                    border-radius: 6px;
                    min-width: {min_w}px;
                    max-width: {max_w}px;
                    min-height: {min_h}px;
                    max-height: {max_h}px;
                }}
            """)
        else:
            border_color = t.get("math_delim_color", COLOR_BORDER)
            bg_color = t.get("math_box_bg_focus", "rgba(120, 120, 150, 0.08)")
            hover_border = t.get("math_box_border", COLOR_MIKU_CYAN)
            self.setStyleSheet(f"""
                QFrame#{self.objectName()} {{
                    background-color: {bg_color};
                    border: 1px solid {border_color};
                    border-radius: 6px;
                    min-width: {min_w}px;
                    max-width: {max_w}px;
                    min-height: {min_h}px;
                    max-height: {max_h}px;
                }}
                QFrame#{self.objectName()}:hover {{
                    border-color: {hover_border};
                    background-color: {t.get("math_box_bg_focus", "rgba(57, 197, 187, 0.12)")};
                }}
            """)

        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.slot)
            event.accept()


class SlotContainerWidget(QFrame):
    """Envolvente (wrapper) de visualización para casillas que ya poseen contenido.

    Muestra un leve resalte si es la casilla activa y asegura que sus hijos
    (nodos) estén empaquetados estrechamente (sin padding) para respetar
    el `kerning` tipográfico matemático.
    """

    clicked = Signal(object)

    def __init__(
        self, slot: Slot, is_active: bool = False, theme: str = "dark", parent=None
    ):
        super().__init__(parent)
        self.slot = slot
        self.is_active = is_active
        self.current_theme = theme
        t = get_theme_dict(theme)

        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName(f"SlotContainer_{id(self)}")

        if is_active:
            border_color = t.get("math_box_border", COLOR_MIKU_CYAN)
            bg_color = t.get("math_box_bg_focus", "rgba(57, 197, 187, 0.08)")
            self.setStyleSheet(f"""
                QFrame#{self.objectName()} {{
                    background-color: {bg_color};
                    border: 1.5px solid {border_color};
                    border-radius: 4px;
                    padding: 1px;
                }}
            """)
        else:
            hover_border = t.get("math_delim_color", "#828DA4")
            self.setStyleSheet(f"""
                QFrame#{self.objectName()} {{
                    background-color: transparent;
                    border: 1px dashed transparent;
                    border-radius: 3px;
                    padding: 0px;
                }}
                QFrame#{self.objectName()}:hover {{
                    border: 1px dashed {hover_border};
                }}
            """)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.slot)
            event.accept()


class MathCanvasWidget(QWidget):
    """Lienzo de dibujo de fondo con retícula cuadriculada temática."""

    def __init__(self, theme: str = "dark", parent=None):
        super().__init__(parent)
        self.current_theme = theme

    def paintEvent(self, event):
        painter = QPainter(self)
        t = get_theme_dict(self.current_theme)
        bg_color = t.get(
            "bg_canvas_editor", "#13141C" if self.current_theme == "dark" else "#FFFFFF"
        )
        painter.fillRect(self.rect(), QColor(bg_color))

        if self.current_theme == "dark":
            grid_color = QColor(57, 197, 187, 25)
        else:
            grid_color = QColor(100, 116, 139, 45)

        pen = QPen(grid_color)
        pen.setStyle(Qt.DotLine)
        pen.setWidth(1)
        painter.setPen(pen)

        grid_size = 20
        clip = event.rect()

        # Optimize rendering by only drawing within the exposed rect
        start_x = clip.left() - (clip.left() % grid_size)
        start_y = clip.top() - (clip.top() % grid_size)

        for x in range(start_x, clip.right() + grid_size, grid_size):
            painter.drawLine(x, clip.top(), x, clip.bottom())
        for y in range(start_y, clip.bottom() + grid_size, grid_size):
            painter.drawLine(clip.left(), y, clip.right(), y)

        super().paintEvent(event)


class MathEditorWidget(QFrame):
    """Editor principal de fórmulas matemáticas interactivo en 2D.

    Renderiza ecuaciones con estructura visual real, ajuste tipográfico fino,
    resaltado sintáctico semántico Hatsune Miku y delimitadores adaptables.
    """

    formula_changed = Signal()
    clear_requested = Signal()
    save_requested = Signal()

    def __init__(self, math_tree: MathTree, parent=None):
        super().__init__(parent)
        self.math_tree = math_tree
        self.current_theme = "dark"
        self.base_font_size = 32
        self.setProperty("class", "android-card")

        self.setFocusPolicy(Qt.StrongFocus)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(6)

        # Header Label & Instructions (Descriptive title)
        header_layout = QHBoxLayout()
        self.title = QLabel("Editor Visual de Fórmulas")
        self.info = QLabel(
            "Haz clic en cualquier casilla [ □ ] | Tecla Tab para avanzar"
        )

        header_layout.addWidget(self.title)
        header_layout.addStretch()
        header_layout.addWidget(self.info)
        main_layout.addLayout(header_layout)

        # Large Scrollable Math Canvas Area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.container_widget = MathCanvasWidget(theme=self.current_theme)
        self.container_layout = QHBoxLayout(self.container_widget)
        self.container_layout.setContentsMargins(10, 10, 10, 10)
        self.container_layout.setSpacing(1)
        self.container_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.scroll_area.setWidget(self.container_widget)
        main_layout.addWidget(self.scroll_area, stretch=1)

        # Bottom Action Bar: Limpiar and Guardar Fórmula
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(0, 4, 0, 0)
        bottom_layout.setSpacing(8)

        self.btn_clear = QPushButton("Limpiar")
        self.btn_clear.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_clear.clicked.connect(self.clear_requested.emit)

        self.btn_save = QPushButton("Guardar Fórmula")
        self.btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_save.clicked.connect(self.save_requested.emit)

        bottom_layout.addStretch()
        bottom_layout.addWidget(self.btn_clear)
        bottom_layout.addWidget(self.btn_save)
        main_layout.addLayout(bottom_layout)

        self._update_theme_ui()

        # Rebuild visual layout
        self.rebuild_editor()

    def _update_theme_ui(self):
        """Actualiza la apariencia visual del contenedor del editor según el tema."""
        t = get_theme_dict(self.current_theme)
        canvas_bg = t.get(
            "bg_canvas_editor", "#13141C" if self.current_theme == "dark" else "#FFFFFF"
        )
        border_subtle = t.get("border_subtle", t["border"])

        self.scroll_area.setStyleSheet(f"""
            QScrollArea {{
                border: 1px solid {border_subtle};
                border-radius: 12px;
                background-color: {canvas_bg};
            }}
        """)
        self.title.setStyleSheet(
            f"font-size: 14px; font-weight: bold; color: {t['text_primary']};"
        )
        self.info.setStyleSheet(f"font-size: 11px; color: {t['text_secondary']};")

        btn_clear_style = f"""
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
        btn_save_style = f"""
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
        self.btn_clear.setStyleSheet(btn_clear_style)
        self.btn_save.setStyleSheet(btn_save_style)

    def set_theme(self, theme: str) -> None:
        """Actualiza el tema cromático del editor y reconstruye la representación visual."""
        self.current_theme = theme
        self.container_widget.current_theme = theme
        self._update_theme_ui()
        self.rebuild_editor()

    def rebuild_editor(self):
        """Reconstruye de forma recursiva toda la jerarquía de widgets visuales."""
        while self.container_layout.count() > 0:
            item = self.container_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self._render_slot_into_layout(
            self.math_tree.root_slot,
            self.container_layout,
            font_size=self.base_font_size,
        )
        self.container_layout.addStretch()

    def _on_slot_clicked(self, slot: Slot):
        self.math_tree.set_active_slot(slot)
        self.rebuild_editor()
        self.setFocus()
        self.formula_changed.emit()

    def _render_slot_into_layout(
        self,
        slot: Slot,
        target_layout: QHBoxLayout,
        font_size: int = 32,
        depth: int = 0,
    ):
        """Renderiza una casilla en un layout horizontal ajustado con colores del tema activo."""
        is_active = slot.id == self.math_tree.active_slot.id

        if slot.is_empty():
            box = SlotBoxWidget(
                slot, is_active=is_active, font_size=font_size, theme=self.current_theme
            )
            box.clicked.connect(self._on_slot_clicked)
            target_layout.addWidget(box)
            return

        # Slot has contents -> wrap in container
        container = SlotContainerWidget(
            slot, is_active=is_active, theme=self.current_theme
        )
        container.clicked.connect(self._on_slot_clicked)
        cont_layout = QHBoxLayout(container)
        cont_layout.setContentsMargins(1, 0, 1, 0)
        cont_layout.setSpacing(0)
        cont_layout.setAlignment(Qt.AlignVCenter)

        # Render nodes inside slot
        for node in slot.nodes:
            self._render_node_into_layout(node, cont_layout, font_size, depth)

        target_layout.addWidget(container)

    def _render_node_into_layout(
        self,
        node: MathNode,
        target_layout: QHBoxLayout,
        font_size: int = 32,
        depth: int = 0,
    ):
        """Renderiza recursivamente un MathNode con jerarquía cromática y escalado tipográfico."""
        t = get_theme_dict(self.current_theme)

        if isinstance(node, TextNode):
            lbl = QLabel()
            lbl.setTextFormat(Qt.RichText)
            lbl.setText(format_highlighted_html(node.text, theme=self.current_theme))
            lbl.setStyleSheet(f"font-size: {font_size}px; margin: 0px; padding: 0px;")
            lbl.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(lbl)

        elif isinstance(node, (SymbolNode, OperatorNode)):
            lbl = QLabel()
            lbl.setTextFormat(Qt.RichText)
            display_text = getattr(node, "display", "")
            lbl.setText(format_highlighted_html(display_text, theme=self.current_theme))
            lbl.setStyleSheet(f"font-size: {font_size}px; margin: 0px; padding: 0px;")
            lbl.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(lbl)

        elif isinstance(node, FractionNode):
            frac_widget = QWidget()
            v_layout = QVBoxLayout(frac_widget)
            v_layout.setContentsMargins(1, 0, 1, 0)
            v_layout.setSpacing(0)
            v_layout.setAlignment(Qt.AlignVCenter)

            # Numerator layout
            num_h = QHBoxLayout()
            num_h.setContentsMargins(0, 0, 0, 0)
            num_h.setSpacing(0)
            num_h.setAlignment(Qt.AlignCenter)
            self._render_slot_into_layout(node.slots["num"], num_h, font_size, depth)
            v_layout.addLayout(num_h)

            # Fraction Bar Line (Delimiters / Structure color)
            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            delim_col = t.get("math_delim_color", "#828DA4")
            line.setStyleSheet(
                f"background-color: {delim_col}; max-height: 2px; min-height: 2px; border: none; margin: 1px 0px;"
            )
            v_layout.addWidget(line)

            # Denominator layout
            den_h = QHBoxLayout()
            den_h.setContentsMargins(0, 0, 0, 0)
            den_h.setSpacing(0)
            den_h.setAlignment(Qt.AlignCenter)
            self._render_slot_into_layout(node.slots["den"], den_h, font_size, depth)
            v_layout.addLayout(den_h)

            frac_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(frac_widget)

        elif isinstance(node, PowerNode):
            pow_widget = QWidget()
            h_layout = QHBoxLayout(pow_widget)
            h_layout.setContentsMargins(0, 0, 0, 0)
            h_layout.setSpacing(0)
            h_layout.setAlignment(Qt.AlignBottom)

            self._render_slot_into_layout(
                node.slots["base"], h_layout, font_size, depth
            )

            exp_font = max(10, int(font_size * 0.7))
            exp_box = QWidget()
            exp_v = QVBoxLayout(exp_box)
            y_offset = int(font_size * 0.6)
            exp_v.setContentsMargins(0, 0, 0, y_offset)
            exp_v.setSpacing(0)
            exp_h = QHBoxLayout()
            exp_h.setContentsMargins(0, 0, 0, 0)
            exp_h.setSpacing(0)
            self._render_slot_into_layout(node.slots["exp"], exp_h, exp_font, depth)
            exp_v.addLayout(exp_h)
            exp_v.addStretch()

            exp_box.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            h_layout.addWidget(exp_box)
            pow_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(pow_widget)

        elif isinstance(node, SubSupNode):
            subsup_widget = QWidget()
            h_layout = QHBoxLayout(subsup_widget)
            h_layout.setContentsMargins(0, 0, 0, 0)
            h_layout.setSpacing(0)
            h_layout.setAlignment(Qt.AlignVCenter)

            self._render_slot_into_layout(
                node.slots["base"], h_layout, font_size, depth
            )

            small_font = max(10, int(font_size * 0.7))

            # Stack the superscript on top of the subscript
            stack_box = QWidget()
            stack_v = QVBoxLayout(stack_box)
            stack_v.setContentsMargins(0, 0, 0, 0)
            stack_v.setSpacing(1)
            stack_v.setAlignment(Qt.AlignVCenter)

            # Superscript (top)
            sup_h = QHBoxLayout()
            sup_h.setContentsMargins(0, 0, 0, 0)
            sup_h.setSpacing(0)
            sup_h.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
            self._render_slot_into_layout(node.slots["sup"], sup_h, small_font, depth)
            stack_v.addLayout(sup_h)

            # Subscript (bottom)
            sub_h = QHBoxLayout()
            sub_h.setContentsMargins(0, 0, 0, 0)
            sub_h.setSpacing(0)
            sub_h.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            self._render_slot_into_layout(node.slots["sub"], sub_h, small_font, depth)
            stack_v.addLayout(sub_h)

            h_layout.addWidget(stack_box)
            target_layout.addWidget(subsup_widget)

        elif isinstance(node, SubscriptNode):
            sub_widget = QWidget()
            h_layout = QHBoxLayout(sub_widget)
            h_layout.setContentsMargins(0, 0, 0, 0)
            h_layout.setSpacing(0)
            h_layout.setAlignment(Qt.AlignTop)

            self._render_slot_into_layout(
                node.slots["base"], h_layout, font_size, depth
            )

            sub_font = max(10, int(font_size * 0.7))
            sub_box = QWidget()
            sub_v = QVBoxLayout(sub_box)
            y_offset = int(font_size * 0.4)
            sub_v.setContentsMargins(0, y_offset, 0, 0)
            sub_v.setSpacing(0)
            sub_h = QHBoxLayout()
            sub_h.setContentsMargins(0, 0, 0, 0)
            sub_h.setSpacing(0)
            self._render_slot_into_layout(node.slots["sub"], sub_h, sub_font, depth)
            sub_v.addLayout(sub_h)

            sub_box.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            h_layout.addWidget(sub_box)
            sub_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(sub_widget)

        elif isinstance(node, SquareRootNode):
            delim_col = t.get("math_delim_color", "#828DA4")
            sqrt_widget = AdaptiveRootWidget(color=delim_col)
            self._render_slot_into_layout(
                node.slots["radicand"], sqrt_widget.body_layout, font_size, depth
            )
            target_layout.addWidget(sqrt_widget)

        elif isinstance(node, NthRootNode):
            container = QWidget()
            h_layout = QHBoxLayout(container)
            h_layout.setContentsMargins(0, 0, 0, 0)
            h_layout.setSpacing(0)
            h_layout.setAlignment(Qt.AlignVCenter)

            idx_v = QVBoxLayout()
            idx_v.setContentsMargins(0, 0, -6, int(font_size * 0.5))
            idx_h = QHBoxLayout()
            idx_h.setContentsMargins(0, 0, 0, 0)
            idx_h.setSpacing(0)
            idx_font = max(10, int(font_size * 0.6))
            self._render_slot_into_layout(node.slots["index"], idx_h, idx_font, depth)
            idx_v.addLayout(idx_h)
            h_layout.addLayout(idx_v)

            delim_col = t.get("math_delim_color", "#828DA4")
            root_widget = AdaptiveRootWidget(color=delim_col)
            self._render_slot_into_layout(
                node.slots["radicand"], root_widget.body_layout, font_size, depth
            )
            h_layout.addWidget(root_widget)

            container.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(container)

        elif isinstance(
            node,
            (
                DefiniteIntegralNode,
                ContourIntegralNode,
                DoubleIntegralNode,
                TripleIntegralNode,
            ),
        ):
            cmd_col = t.get("math_cmd_color", "#C084FC")
            op_col = t.get("math_op_color", "#56D8CD")

            sym_char = "∫"
            if isinstance(node, ContourIntegralNode):
                sym_char = "∮"
            elif isinstance(node, DoubleIntegralNode):
                sym_char = "∬"
            elif isinstance(node, TripleIntegralNode):
                sym_char = "∭"

            adaptive_int = AdaptiveIntegralWidget(
                symbol=sym_char, font_size=font_size, color=cmd_col
            )

            # Left side: limits stack with dedicated column placed to the right of the integral graphic
            limits_widget = QWidget()
            sym_v = QVBoxLayout(limits_widget)
            sym_v.setContentsMargins(0, 0, 0, 0)
            sym_v.setSpacing(1)

            up_h = QHBoxLayout()
            up_h.setContentsMargins(0, 0, 0, 0)
            up_h.setSpacing(0)
            up_h.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
            lim_font = max(10, int(font_size * 0.65))
            self._render_slot_into_layout(node.slots["upper"], up_h, lim_font, depth)
            sym_v.addLayout(up_h)

            sym_v.addStretch()

            low_h = QHBoxLayout()
            low_h.setContentsMargins(0, 0, 0, 0)
            low_h.setSpacing(0)
            low_h.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            self._render_slot_into_layout(node.slots["lower"], low_h, lim_font, depth)
            sym_v.addLayout(low_h)

            # Insert limits_widget at index 1 (between the graphic at index 0 and body at index 2)
            # The layout spacing of 6px strictly maintains the 6px separation barrier from the graphic's right edge
            adaptive_int.main_layout.insertWidget(1, limits_widget)

            body_h = QHBoxLayout()
            body_h.setContentsMargins(1, 0, 0, 0)
            body_h.setSpacing(0)
            self._render_slot_into_layout(node.slots["body"], body_h, font_size, depth)
            adaptive_int.body_layout.addLayout(body_h)

            # Differential symbol 'd' in Operator Cyan
            d_lbl = QLabel("d")
            d_lbl.setStyleSheet(
                f"color: {op_col}; font-size: {font_size}px; font-weight: bold; margin-left: 2px; margin-right: 0px; padding: 0px;"
            )
            adaptive_int.body_layout.addWidget(d_lbl)

            var_h = QHBoxLayout()
            var_h.setContentsMargins(0, 0, 0, 0)
            var_h.setSpacing(0)
            self._render_slot_into_layout(node.slots["var"], var_h, font_size, depth)
            adaptive_int.body_layout.addLayout(var_h)

            target_layout.addWidget(adaptive_int)

        elif isinstance(node, IndefiniteIntegralNode):
            cmd_col = t.get("math_cmd_color", "#C084FC")
            op_col = t.get("math_op_color", "#56D8CD")
            adaptive_int = AdaptiveIntegralWidget(
                symbol="∫", font_size=font_size, color=cmd_col
            )

            body_h = QHBoxLayout()
            body_h.setContentsMargins(1, 0, 0, 0)
            body_h.setSpacing(0)
            self._render_slot_into_layout(node.slots["body"], body_h, font_size, depth)
            adaptive_int.body_layout.addLayout(body_h)

            d_lbl = QLabel("d")
            d_lbl.setStyleSheet(
                f"color: {op_col}; font-size: {font_size}px; font-weight: bold; margin-left: 2px; margin-right: 0px; padding: 0px;"
            )
            adaptive_int.body_layout.addWidget(d_lbl)

            var_h = QHBoxLayout()
            var_h.setContentsMargins(0, 0, 0, 0)
            var_h.setSpacing(0)
            self._render_slot_into_layout(node.slots["var"], var_h, font_size, depth)
            adaptive_int.body_layout.addLayout(var_h)

            target_layout.addWidget(adaptive_int)

        elif isinstance(node, SummationNode):
            sum_widget = QWidget()
            h_layout = QHBoxLayout(sum_widget)
            h_layout.setContentsMargins(1, 0, 1, 0)
            h_layout.setSpacing(1)
            h_layout.setAlignment(Qt.AlignVCenter)

            sym_v = QVBoxLayout()
            sym_v.setContentsMargins(0, 0, 0, 0)
            sym_v.setSpacing(0)
            sym_v.setAlignment(Qt.AlignCenter)

            up_h = QHBoxLayout()
            up_h.setContentsMargins(0, 0, 0, 0)
            up_h.setSpacing(0)
            up_h.setAlignment(Qt.AlignCenter)
            lim_font = max(10, int(font_size * 0.7))
            self._render_slot_into_layout(node.slots["upper"], up_h, lim_font, depth)
            sym_v.addLayout(up_h)

            cmd_col = t.get("math_cmd_color", "#C084FC")
            sym_lbl = QLabel("∑")
            sym_lbl.setAlignment(Qt.AlignCenter)
            sum_size = max(1, int(font_size * 1.58))
            sym_lbl.setStyleSheet(
                f"color: {cmd_col}; font-size: {sum_size}px; font-weight: bold; margin: 0px; padding: 0px;"
            )
            sym_v.addWidget(sym_lbl)

            low_h = QHBoxLayout()
            low_h.setContentsMargins(0, 0, 0, 0)
            low_h.setSpacing(0)
            low_h.setAlignment(Qt.AlignCenter)
            self._render_slot_into_layout(node.slots["lower"], low_h, lim_font, depth)
            sym_v.addLayout(low_h)

            h_layout.addLayout(sym_v)

            # Body Slot
            body_h = QHBoxLayout()
            body_h.setContentsMargins(1, 0, 0, 0)
            body_h.setSpacing(0)
            self._render_slot_into_layout(node.slots["body"], body_h, font_size, depth)
            h_layout.addLayout(body_h)

            sum_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(sum_widget)

        elif isinstance(node, LimitNode):
            lim_widget = QWidget()
            h_layout = QHBoxLayout(lim_widget)
            h_layout.setContentsMargins(1, 0, 1, 0)
            h_layout.setSpacing(1)
            h_layout.setAlignment(Qt.AlignVCenter)

            sym_v = QVBoxLayout()
            sym_v.setContentsMargins(0, 0, 0, 0)
            sym_v.setSpacing(0)

            cmd_col = t.get("math_cmd_color", "#C084FC")
            op_col = t.get("math_op_color", "#56D8CD")

            lim_lbl = QLabel("lim")
            lim_lbl.setAlignment(Qt.AlignCenter)
            lim_font = max(1, int(font_size * 0.83))
            lim_lbl.setStyleSheet(
                f"color: {cmd_col}; font-size: {lim_font}px; font-weight: bold; margin: 0px; padding: 0px;"
            )
            sym_v.addWidget(lim_lbl)

            sub_h = QHBoxLayout()
            sub_h.setContentsMargins(0, 0, 0, 0)
            sub_h.setSpacing(0)
            sub_h.setAlignment(Qt.AlignCenter)
            sub_font = max(10, int(font_size * 0.7))
            self._render_slot_into_layout(node.slots["var"], sub_h, sub_font, depth)

            arrow = QLabel("→")
            arrow_font = max(10, int(font_size * 0.66))
            arrow.setStyleSheet(
                f"color: {op_col}; font-size: {arrow_font}px; font-weight: bold; margin: 0px 1px;"
            )
            sub_h.addWidget(arrow)

            self._render_slot_into_layout(node.slots["target"], sub_h, sub_font, depth)
            sym_v.addLayout(sub_h)

            h_layout.addLayout(sym_v)

            body_h = QHBoxLayout()
            body_h.setContentsMargins(1, 0, 0, 0)
            body_h.setSpacing(0)
            self._render_slot_into_layout(node.slots["body"], body_h, font_size, depth)
            h_layout.addLayout(body_h)

            lim_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(lim_widget)

        elif isinstance(node, BracketNode):
            delim_col = t.get(
                f"rainbow_{(depth % 4) + 1}", t.get("math_delim_color", "#828DA4")
            )
            b_widget = AdaptiveBracketWidget(
                node.left_delim, node.right_delim, color=delim_col
            )
            self._render_slot_into_layout(
                node.slots["body"], b_widget.body_layout, font_size, depth + 1
            )
            target_layout.addWidget(b_widget)

        elif isinstance(node, MatrixNode):
            delim_col = t.get(
                f"rainbow_{(depth % 4) + 1}", t.get("math_delim_color", "#828DA4")
            )
            l_delim = "[" if "b" in node.matrix_type else "("
            r_delim = "]" if "b" in node.matrix_type else ")"
            mat_widget = AdaptiveBracketWidget(l_delim, r_delim, color=delim_col)

            grid = QGridLayout()
            grid.setContentsMargins(2, 2, 2, 2)
            grid.setSpacing(3)
            for r in range(node.rows):
                for c in range(node.cols):
                    cell_h = QHBoxLayout()
                    cell_h.setContentsMargins(0, 0, 0, 0)
                    cell_h.setSpacing(0)
                    self._render_slot_into_layout(
                        node.slots[f"cell_{r}_{c}"], cell_h, font_size, depth + 1
                    )
                    grid.addLayout(cell_h, r, c)

            grid_container = QWidget()
            grid_container.setLayout(grid)
            mat_widget.body_layout.addWidget(grid_container)

            target_layout.addWidget(mat_widget)

        elif isinstance(node, DerivativeNode):
            d_widget = QWidget()
            v_layout = QVBoxLayout(d_widget)
            v_layout.setContentsMargins(1, 0, 1, 0)
            v_layout.setSpacing(0)

            op_col = t.get("math_op_color", "#56D8CD")
            delim_col = t.get("math_delim_color", "#828DA4")

            # Top: d f
            top_h = QHBoxLayout()
            top_h.setContentsMargins(0, 0, 0, 0)
            top_h.setSpacing(0)
            top_h.setAlignment(Qt.AlignCenter)
            sym = "∂" if node.is_partial else "d"
            d_font = max(1, int(font_size * 0.83))
            lbl_t = QLabel(sym)
            lbl_t.setStyleSheet(
                f"color: {op_col}; font-size: {d_font}px; font-weight: bold; margin-right: 1px; padding: 0px;"
            )
            top_h.addWidget(lbl_t)
            self._render_slot_into_layout(node.slots["func"], top_h, font_size, depth)
            v_layout.addLayout(top_h)

            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            line.setStyleSheet(
                f"background-color: {delim_col}; max-height: 2px; min-height: 2px; border: none; margin: 1px 0px;"
            )
            v_layout.addWidget(line)

            # Bottom: d x
            bot_h = QHBoxLayout()
            bot_h.setContentsMargins(0, 0, 0, 0)
            bot_h.setSpacing(0)
            bot_h.setAlignment(Qt.AlignCenter)
            lbl_b = QLabel(sym)
            lbl_b.setStyleSheet(
                f"color: {op_col}; font-size: {d_font}px; font-weight: bold; margin-right: 1px; padding: 0px;"
            )
            bot_h.addWidget(lbl_b)
            self._render_slot_into_layout(node.slots["var"], bot_h, font_size, depth)
            v_layout.addLayout(bot_h)

            d_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(d_widget)

        elif isinstance(node, BinomialNode):
            delim_col = t.get("math_delim_color", "#828DA4")
            binom_widget = QWidget()
            v_layout = QVBoxLayout(binom_widget)
            v_layout.setContentsMargins(1, 0, 1, 0)
            v_layout.setSpacing(0)
            v_layout.setAlignment(Qt.AlignCenter)

            n_h = QHBoxLayout()
            n_h.setContentsMargins(0, 0, 0, 0)
            n_h.setSpacing(0)
            n_h.setAlignment(Qt.AlignCenter)
            self._render_slot_into_layout(node.slots["n"], n_h, font_size, depth)
            v_layout.addLayout(n_h)

            k_h = QHBoxLayout()
            k_h.setContentsMargins(0, 0, 0, 0)
            k_h.setSpacing(0)
            k_h.setAlignment(Qt.AlignCenter)
            self._render_slot_into_layout(node.slots["k"], k_h, font_size, depth)
            v_layout.addLayout(k_h)

            adaptive_binom = AdaptiveBracketWidget(
                left_delim="(",
                right_delim=")",
                color=delim_col,
            )
            adaptive_binom.body_layout.addWidget(binom_widget)
            target_layout.addWidget(adaptive_binom)

        elif isinstance(node, ModularNode):
            delim_col = t.get("math_delim_color", "#828DA4")
            cmd_col = t.get("math_cmd_color", "#C084FC")

            mod_widget = QWidget()
            h_layout = QHBoxLayout(mod_widget)
            h_layout.setContentsMargins(2, 0, 2, 0)
            h_layout.setSpacing(1)
            h_layout.setAlignment(Qt.AlignVCenter)

            l_par = QLabel("(")
            l_par.setStyleSheet(
                f"color: {delim_col}; font-size: {font_size}px; margin: 0px;"
            )
            h_layout.addWidget(l_par)

            mod_lbl = QLabel("mod ")
            mod_lbl.setStyleSheet(
                f"color: {cmd_col}; font-size: {font_size}px; font-weight: bold; margin: 0px;"
            )
            h_layout.addWidget(mod_lbl)

            self._render_slot_into_layout(node.slots["mod"], h_layout, font_size, depth)

            r_par = QLabel(")")
            r_par.setStyleSheet(
                f"color: {delim_col}; font-size: {font_size}px; margin: 0px;"
            )
            h_layout.addWidget(r_par)

            mod_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(mod_widget)

        elif isinstance(node, ProductNode):
            prod_widget = QWidget()
            h_layout = QHBoxLayout(prod_widget)
            h_layout.setContentsMargins(1, 0, 1, 0)
            h_layout.setSpacing(1)
            h_layout.setAlignment(Qt.AlignVCenter)

            sym_v = QVBoxLayout()
            sym_v.setContentsMargins(0, 0, 0, 0)
            sym_v.setSpacing(0)
            sym_v.setAlignment(Qt.AlignCenter)

            up_h = QHBoxLayout()
            up_h.setContentsMargins(0, 0, 0, 0)
            up_h.setSpacing(0)
            up_h.setAlignment(Qt.AlignCenter)
            lim_font = max(10, int(font_size * 0.7))
            self._render_slot_into_layout(node.slots["upper"], up_h, lim_font, depth)
            sym_v.addLayout(up_h)

            cmd_col = t.get("math_cmd_color", "#C084FC")
            sym_lbl = QLabel("∏")
            sym_lbl.setAlignment(Qt.AlignCenter)
            prod_size = max(1, int(font_size * 1.58))
            sym_lbl.setStyleSheet(
                f"color: {cmd_col}; font-size: {prod_size}px; font-weight: bold; margin: 0px; padding: 0px;"
            )
            sym_v.addWidget(sym_lbl)

            low_h = QHBoxLayout()
            low_h.setContentsMargins(0, 0, 0, 0)
            low_h.setSpacing(0)
            low_h.setAlignment(Qt.AlignCenter)
            self._render_slot_into_layout(node.slots["lower"], low_h, lim_font, depth)
            sym_v.addLayout(low_h)

            h_layout.addLayout(sym_v)

            # Body Slot
            body_h = QHBoxLayout()
            body_h.setContentsMargins(1, 0, 0, 0)
            body_h.setSpacing(0)
            self._render_slot_into_layout(node.slots["body"], body_h, font_size, depth)
            h_layout.addLayout(body_h)

            prod_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(prod_widget)

        elif isinstance(node, StyleDecoratorNode):
            if node.style_cmd in ("vec", "hat", "dot", "ddot", "bar", "tilde"):
                acc_widget = QWidget()
                v_layout = QVBoxLayout(acc_widget)
                v_layout.setContentsMargins(0, 0, 0, 0)
                v_layout.setSpacing(0)
                v_layout.setAlignment(Qt.AlignCenter)

                acc_map = {
                    "vec": "→",
                    "hat": "^",
                    "dot": "˙",
                    "ddot": "¨",
                    "bar": "¯",
                    "tilde": "~",
                }
                acc_sym = acc_map.get(node.style_cmd, "")
                op_col = t.get("math_op_color", "#56D8CD")
                acc_font = max(10, int(font_size * 0.55))
                acc_lbl = QLabel(acc_sym)
                acc_lbl.setStyleSheet(
                    f"color: {op_col}; font-size: {acc_font}px; font-weight: bold; margin: 0px; padding: 0px;"
                )
                acc_lbl.setAlignment(Qt.AlignCenter)
                v_layout.addWidget(acc_lbl)

                body_h = QHBoxLayout()
                body_h.setContentsMargins(0, 0, 0, 0)
                body_h.setSpacing(0)
                self._render_slot_into_layout(
                    node.slots["body"], body_h, font_size, depth
                )
                v_layout.addLayout(body_h)

                acc_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
                target_layout.addWidget(acc_widget)
            else:
                self._render_slot_into_layout(
                    node.slots["body"], target_layout, font_size, depth
                )

        else:
            # Generic fallback
            lbl = QLabel(node.to_display_text())
            lbl.setStyleSheet(
                f"color: {t.get('text_primary', '#E2E2E9')}; font-size: {font_size}px; margin: 0px;"
            )
            lbl.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            target_layout.addWidget(lbl)

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        text = event.text()

        if key == Qt.Key_Tab:
            if event.modifiers() & Qt.ShiftModifier:
                self.math_tree.navigate_prev_slot()
            else:
                self.math_tree.navigate_next_slot()
            self.rebuild_editor()
            self.formula_changed.emit()
            return

        elif key == Qt.Key_Backspace:
            self.math_tree.remove_last()
            self.rebuild_editor()
            self.formula_changed.emit()
            return

        elif key == Qt.Key_Delete:
            self.math_tree.remove_active_template()
            self.rebuild_editor()
            self.formula_changed.emit()
            return

        elif key in (Qt.Key_Left, Qt.Key_Right):
            if key == Qt.Key_Left:
                self.math_tree.navigate_prev_slot()
            else:
                self.math_tree.navigate_next_slot()
            self.rebuild_editor()
            self.formula_changed.emit()
            return

        elif text and text.isprintable():
            self.math_tree.insert_text(text)
            self.rebuild_editor()
            self.formula_changed.emit()
            return

        super().keyPressEvent(event)
