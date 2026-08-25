"""
---
file: src/ui/components/bracket_widget.py
module: src.ui.components.bracket_widget
description: Componente de dibujado vectorial de delimitadores y paréntesis adaptables en altura.
type: ui/component
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.syntax
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/editor_widget.py
exports:
  - BracketGraphicWidget: "Widget de dibujo vectorial para un glifo individual de delimitador adaptativo"
  - AdaptiveBracketWidget: "Contenedor compuesto que auto-ajusta el ancho y altura de delimitadores"
test: pytest tests/test_editor_widget.py
constraints:
  - "Preservar las proporciones de trazo vectorial sin deformación de curvas ante escalado vertical"
keywords:
  - bracket-widget
  - adaptive-brackets
  - vector-painter
  - qpainterpath
  - math-delimiters
---

Adaptive Bracket & Delimiter Widget Component for Interactive Formula Editor
Paints vector-drawn parenthesis, brackets, curly braces, and vertical bars that stretch vertically
to dynamically match the height of inner subformulas.
"""

from __future__ import annotations

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QFont, QFontMetrics, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import QHBoxLayout, QSizePolicy, QWidget

from src.core.syntax import COLOR_DELIMITER


class BracketGraphicWidget(QWidget):
    """Widget vectorial de bajo nivel que dibuja un glifo delimitador de altura variable.

    Renderiza delimitadores matemáticos como `(`, `)`, `[`, `]`, `{`, `}`, `|`
    escalando sus trazos proporcionales a la altura requerida sin deformación.
    """

    def __init__(self, delim: str, color: str = COLOR_DELIMITER, parent=None):
        super().__init__(parent)
        self.delim = delim
        self.color = color

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setMinimumWidth(8)
        self.setMaximumWidth(18)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

    def sizeHint(self) -> QSize:
        h = max(28, self.height())
        w = max(8, min(16, int(h * 0.22)))
        return QSize(w, h)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        h = float(self.height())
        w = float(self.width())
        p = 2.5  # padding

        # Determine stroke width scaled slightly by height
        pen_width = max(2.0, min(3.2, 1.8 + (h / 60.0)))
        pen = QPen(
            QColor(self.color), pen_width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin
        )
        painter.setPen(pen)

        if self.delim == "(":
            path = QPainterPath()
            path.moveTo(w - p, p)
            path.cubicTo(p, h * 0.25, p, h * 0.75, w - p, h - p)
            painter.drawPath(path)

        elif self.delim == ")":
            path = QPainterPath()
            path.moveTo(p, p)
            path.cubicTo(w - p, h * 0.25, w - p, h * 0.75, p, h - p)
            painter.drawPath(path)

        elif self.delim == "[":
            path = QPainterPath()
            path.moveTo(w - p, p)
            path.lineTo(p, p)
            path.lineTo(p, h - p)
            path.lineTo(w - p, h - p)
            painter.drawPath(path)

        elif self.delim == "]":
            path = QPainterPath()
            path.moveTo(p, p)
            path.lineTo(w - p, p)
            path.lineTo(w - p, h - p)
            path.lineTo(p, h - p)
            painter.drawPath(path)

        elif self.delim == "{":
            path = QPainterPath()
            path.moveTo(w - p, p)
            path.cubicTo(w * 0.4, p + h * 0.1, p + 1.5, h * 0.4, p, h * 0.5)
            path.cubicTo(p + 1.5, h * 0.6, w * 0.4, h - p - h * 0.1, w - p, h - p)
            painter.drawPath(path)

        elif self.delim == "}":
            path = QPainterPath()
            path.moveTo(p, p)
            path.cubicTo(w * 0.6, p + h * 0.1, w - p - 1.5, h * 0.4, w - p, h * 0.5)
            path.cubicTo(w - p - 1.5, h * 0.6, w * 0.6, h - p - h * 0.1, p, h - p)
            painter.drawPath(path)

        elif self.delim == "|":
            path = QPainterPath()
            path.moveTo(w / 2.0, p)
            path.lineTo(w / 2.0, h - p)
            painter.drawPath(path)

        else:
            painter.setFont(QFont("Segoe UI", 20, QFont.Bold))
            painter.drawText(self.rect(), Qt.AlignCenter, self.delim)


class AdaptiveBracketWidget(QWidget):
    """Contenedor de interfaz que envuelve un layout con delimitadores adaptables.

    Se asegura de actualizar dinámicamente el tamaño de los paréntesis laterales
    cuando el tamaño del contenido interno cambia.
    """

    def __init__(
        self,
        left_delim: str = "(",
        right_delim: str = ")",
        color: str = COLOR_DELIMITER,
        parent=None,
    ):
        super().__init__(parent)
        self.left_delim = left_delim
        self.right_delim = right_delim
        self.color = color

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(1, 0, 1, 0)
        self.main_layout.setSpacing(1)
        self.main_layout.setAlignment(Qt.AlignVCenter)

        self.left_bracket = BracketGraphicWidget(left_delim, color=color, parent=self)
        self.right_bracket = BracketGraphicWidget(right_delim, color=color, parent=self)

        self.body_container = QWidget(self)
        self.body_layout = QHBoxLayout(self.body_container)
        self.body_layout.setContentsMargins(1, 0, 1, 0)
        self.body_layout.setSpacing(1)
        self.body_layout.setAlignment(Qt.AlignVCenter)

        self.main_layout.addWidget(self.left_bracket)
        self.main_layout.addWidget(self.body_container)
        self.main_layout.addWidget(self.right_bracket)

        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Update bracket widths dynamically based on container height
        h = self.height()
        target_w = max(8, min(16, int(h * 0.22)))
        self.left_bracket.setFixedWidth(target_w)
        self.right_bracket.setFixedWidth(target_w)
        self.left_bracket.update()
        self.right_bracket.update()


class AdaptiveRootWidget(QWidget):
    """
    Adaptive Root widget wrapping an inner formula layout with a scalable vector root symbol and top line.
    """

    def __init__(self, color: str = COLOR_DELIMITER, parent=None):
        super().__init__(parent)
        self.color = color
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(14, 4, 2, 2)
        self.main_layout.setSpacing(1)
        self.main_layout.setAlignment(Qt.AlignVCenter)

        self.body_container = QWidget(self)
        self.body_layout = QHBoxLayout(self.body_container)
        self.body_layout.setContentsMargins(0, 0, 0, 0)
        self.body_layout.setSpacing(1)
        self.main_layout.addWidget(self.body_container)

        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        h = float(self.height())
        w = float(self.width())
        p = 2.0

        pen_width = max(2.0, min(3.2, 1.8 + (h / 60.0)))
        pen = QPen(
            QColor(self.color), pen_width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin
        )
        painter.setPen(pen)

        lm = 12.0

        path = QPainterPath()
        path.moveTo(p, h * 0.5)
        path.lineTo(lm * 0.4, h * 0.65)
        path.lineTo(lm * 0.8, h - p)
        path.lineTo(lm, p + 1)
        path.lineTo(w - p, p + 1)
        painter.drawPath(path)


class IntegralGraphicWidget(QWidget):
    """Widget gráfico que dibuja el glifo de la integral sin truncamiento superior ni inferior.

    Utiliza el rectángulo delimitador estricto (`tightBoundingRect`) para ubicar la línea
    base del texto con margen de seguridad (`pad_top` y `pad_bottom`), garantizando que
    los ganchos y curvas del símbolo de integral jamás se corten visualmente.
    """

    def __init__(
        self,
        symbol: str = "∫",
        font_size: int = 32,
        color: str = COLOR_DELIMITER,
        parent=None,
    ):
        super().__init__(parent)
        self.symbol = symbol
        self.font_size = font_size
        self.color = color
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self._recalc_metrics()

    def _recalc_metrics(self):
        self.font = QFont("Cambria Math", int(self.font_size * 1.35))
        fm = QFontMetrics(self.font)
        self.tight_br = fm.tightBoundingRect(self.symbol)
        self.pad_top = 4
        self.pad_bottom = 4
        self.pad_left = 2
        self.pad_right = 2
        self._w = max(18, self.tight_br.width() + self.pad_left + self.pad_right)
        self._h = max(38, self.tight_br.height() + self.pad_top + self.pad_bottom)
        self.setFixedSize(self._w, self._h)

    def sizeHint(self) -> QSize:
        return QSize(self._w, self._h)

    def set_font_size(self, font_size: int):
        self.font_size = font_size
        self._recalc_metrics()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)
        painter.setPen(QColor(self.color))
        painter.setFont(self.font)

        # Ubicación calculada para garantizar que los ganchos no se corten en la parte superior
        x = -self.tight_br.left() + self.pad_left
        y = -self.tight_br.top() + self.pad_top
        painter.drawText(x, y, self.symbol)
        painter.end()


class AdaptiveIntegralWidget(QWidget):
    """Contenedor de integral interactiva con límite visual y barrera de separación estricta.

    Mantiene al glifo en su propio `IntegralGraphicWidget` y establece una barrera vertical
    exacta de aproximadamente 6 píxeles a la derecha del último píxel del símbolo,
    impidiendo que las casillas editables de límites (`SlotBoxWidget`) se acerquen más.
    """

    def __init__(
        self,
        symbol: str = "∫",
        font_size: int = 32,
        color: str = COLOR_DELIMITER,
        parent=None,
    ):
        super().__init__(parent)
        self.symbol = symbol
        self.color = color
        self.font_size = font_size

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(
            6
        )  # Límite y separación estricta de 6px a la derecha del glifo
        self.main_layout.setAlignment(Qt.AlignVCenter)

        self.graphic = IntegralGraphicWidget(
            symbol=symbol, font_size=font_size, color=color, parent=self
        )
        self.main_layout.addWidget(self.graphic)

        self.body_container = QWidget(self)
        self.body_layout = QHBoxLayout(self.body_container)
        self.body_layout.setContentsMargins(0, 0, 0, 0)
        self.body_layout.setSpacing(2)
        self.body_layout.setAlignment(Qt.AlignVCenter)
        self.main_layout.addWidget(self.body_container)

        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
