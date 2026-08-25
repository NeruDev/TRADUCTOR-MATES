"""
---
file: src/ui/components/preview_panel.py
module: src.ui.components.preview_panel
description: Panel de visualización renderizada en alta resolución con SVGMathCache y zoom adaptativo dinámico.
type: ui/component
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
  - src.core.translator
  - src.ui.theme
  - src.ui.components.svg_cache
relations:
  - docs/ARCHITECTURE.md
  - src/ui/main_window.py
exports:
  - ensure_svg_white_background: "Asegura la capa de fondo blanco en el XML del SVG exportado"
  - MathPreviewPanel: "Panel de visualización síncrona del SVG con zoom adaptativo y exportación"
test: pytest tests/test_editor_widget.py
constraints:
  - "Garantizar la exportación nítida de PNG y SVG vectorial sin bordes cortados"
keywords:
  - preview-panel
  - svg-math-cache
  - dynamic-zoom
  - png-export
  - svg-export
---

Visual Math Formula Render Preview Panel
Displays high-resolution rendered math equations using SVGMathCache.
Supports exporting clean PNG images and lossless vector SVG files.
Adapts formula text color dynamically to Dark vs Light theme modes.
"""

from __future__ import annotations

from PySide6.QtCore import QByteArray, QRectF, Qt
from PySide6.QtGui import QAction, QColor, QImage, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMenu,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
)

from src.core.ast import MathTree
from src.core.logger import get_logger
from src.core.translator import LaTeXTranslator
from src.ui.components.svg_cache import SVGMathCache
from src.ui.theme import get_theme_dict


def ensure_svg_white_background(
    svg_string: str, bg_color: str = "#ffffff", fg_color: str = "#000000"
) -> str:
    """Modifica un XML de SVG para asegurar un fondo sólido color blanco y trazos de contraste.

    Extrae las coordenadas reales del viewBox para que el rectángulo de fondo
    cubra la totalidad del lienzo (incluyendo coordenadas negativas habituales
    en fórmulas de MathJax) y aísla la regla CSS para que el fondo no sea
    sobreescrito por el color de primer plano.

    Args:
        svg_string: El código fuente XML del SVG original.
        bg_color: Color hexadecimal del fondo sólido.
        fg_color: Color hexadecimal de los trazos matemáticos.

    Returns:
        El código SVG con fondo blanco sólido y trazos nítidos.
    """
    import re

    if not svg_string or "<svg" not in svg_string:
        return svg_string

    # 1. Asegurar namespace
    if "xmlns=" not in svg_string:
        svg_string = svg_string.replace(
            "<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1
        )

    # 2. Extraer dimensiones exactas del viewBox
    vb_match = re.search(r'viewBox="([^"]+)"', svg_string)
    if vb_match:
        parts = vb_match.group(1).split()
        if len(parts) == 4:
            x, y, w, h = parts
        else:
            x, y, w, h = "0", "0", "100%", "100%"
    else:
        x, y, w, h = "0", "0", "100%", "100%"

    # 3. Ajustar regla CSS para que no pinte el fondo con el color de trazo
    if "<style>" in svg_string:
        svg_string = re.sub(
            r"<style>.*?</style>",
            f"<style>svg g, svg path, svg text {{ fill: {fg_color} !important; stroke: {fg_color} !important; }} .math-bg {{ fill: {bg_color} !important; stroke: none !important; }}</style>",
            svg_string,
            flags=re.DOTALL,
        )

    # 4. Inyectar rect de fondo que cubre la totalidad del viewBox
    if 'class="math-bg"' not in svg_string:
        idx = svg_string.find(">") + 1
        bg_rect_str = f'<rect class="math-bg" x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg_color}" style="fill: {bg_color} !important; stroke: none !important;"/>'
        svg_string = svg_string[:idx] + bg_rect_str + svg_string[idx:]

    return svg_string


class MathPreviewPanel(QFrame):
    """Panel de previsualización gráfica de la ecuación en formato SVG.

    Muestra el resultado final usando el motor en JavaScript (MathJax) de
    forma síncrona con auto-ajuste de pantalla y controles interactivos de zoom.
    Además provee acciones contextuales de exportación.
    """

    def __init__(self, math_tree: MathTree, parent=None):
        super().__init__(parent)
        self.math_tree = math_tree
        self.setProperty("class", "android-card")
        self.current_theme: str = "dark"
        self.current_svg: str = ""
        self.current_latex: str = ""
        self.zoom_factor: float = 1.0
        self.is_auto_fit: bool = True

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(10)

        # Header
        header_layout = QHBoxLayout()
        header_layout.setSpacing(6)
        self.title_lbl = QLabel("Vista Previa Renderizada")
        self.title_lbl.setProperty("class", "section-header")

        self.btn_zoom_out = QPushButton("-")
        self.btn_zoom_out.setToolTip("Reducir zoom")
        self.btn_zoom_out.setCursor(Qt.PointingHandCursor)
        self.btn_zoom_out.clicked.connect(self._zoom_out)

        self.lbl_zoom = QLabel("Zoom")
        self.lbl_zoom.setToolTip("Nivel de zoom actual")
        self.lbl_zoom.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn_zoom_in = QPushButton("+")
        self.btn_zoom_in.setToolTip("Aumentar zoom (activa barras de desplazamiento)")
        self.btn_zoom_in.setCursor(Qt.PointingHandCursor)
        self.btn_zoom_in.clicked.connect(self._zoom_in)

        self.btn_zoom_reset = QPushButton("Restablecer")
        self.btn_zoom_reset.setToolTip(
            "Restablecer tamaño para ver la fórmula completa sin barras de desplazamiento"
        )
        self.btn_zoom_reset.setCursor(Qt.PointingHandCursor)
        self.btn_zoom_reset.clicked.connect(self._zoom_reset)

        # Export Dropdown Split Button (Single downward chevron)
        self.btn_export = QPushButton("Exportar ⌄")
        self.btn_export.setProperty("class", "action-btn")
        self.btn_export.setCursor(Qt.PointingHandCursor)

        self.export_menu = QMenu(self)
        action_png = QAction("Exportar como PNG (*.png)", self)
        action_png.triggered.connect(self._export_png)
        self.export_menu.addAction(action_png)

        action_svg = QAction("Exportar como SVG Vectorial (*.svg)", self)
        action_svg.triggered.connect(self._export_svg)
        self.export_menu.addAction(action_svg)

        self.btn_export.setMenu(self.export_menu)

        header_layout.addWidget(self.title_lbl)
        header_layout.addStretch()
        header_layout.addWidget(self.btn_zoom_out)
        header_layout.addWidget(self.lbl_zoom)
        header_layout.addWidget(self.btn_zoom_in)
        header_layout.addWidget(self.btn_zoom_reset)
        header_layout.addWidget(self.btn_export)
        layout.addLayout(header_layout)

        # Scroll Area for Preview Canvas
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setMinimumHeight(120)

        self.preview_lbl = QLabel()
        self.preview_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_lbl.setScaledContents(False)
        self.scroll_area.setWidget(self.preview_lbl)

        layout.addWidget(self.scroll_area)

        self._update_theme_ui()

    def _update_theme_ui(self):
        """Actualiza dinámicamente los estilos y colores según el tema activo."""
        t = get_theme_dict(self.current_theme)

        btn_zoom_out_style = f"""
            QPushButton {{
                background-color: {t["secondary"]};
                color: #FFFFFF;
                border: none;
                border-radius: 6px;
                padding: 4px 10px;
                font-size: 13px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {t["secondary_hover"]};
            }}
        """
        btn_zoom_in_style = f"""
            QPushButton {{
                background-color: {t["primary"]};
                color: #FFFFFF;
                border: none;
                border-radius: 6px;
                padding: 4px 10px;
                font-size: 13px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {t["primary_hover"]};
            }}
        """
        btn_reset_style = f"""
            QPushButton {{
                background-color: {t["primary"]};
                color: #FFFFFF;
                border: none;
                border-radius: 6px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: {t["primary_hover"]};
            }}
        """
        btn_export_style = f"""
            QPushButton {{
                background-color: {t["primary"]};
                color: #FFFFFF;
                border: none;
                border-radius: 6px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: {t["primary_hover"]};
            }}
            QPushButton::menu-indicator {{
                image: none;
                width: 0px;
            }}
        """
        self.btn_zoom_out.setStyleSheet(btn_zoom_out_style)
        self.btn_zoom_in.setStyleSheet(btn_zoom_in_style)
        self.btn_zoom_reset.setStyleSheet(btn_reset_style)
        self.btn_export.setStyleSheet(btn_export_style)
        self.lbl_zoom.setStyleSheet(
            f"font-size: 11px; font-weight: bold; color: {t['primary']}; min-width: 44px;"
        )

        self.export_menu.setStyleSheet(f"""
            QMenu {{
                background-color: {t["surface"]};
                color: {t["text_primary"]};
                border: 1px solid {t["border"]};
                border-radius: 8px;
                padding: 4px;
            }}
            QMenu::item {{
                padding: 6px 16px;
                border-radius: 4px;
                color: {t["text_primary"]};
            }}
            QMenu::item:selected {{
                background-color: {t["primary"]};
                color: #FFFFFF;
            }}
        """)

        canvas_bg = t.get("bg_canvas_render", t["surface_slot"])
        border_subtle = t.get("border_subtle", t["border"])
        self.scroll_area.setStyleSheet(f"""
            QScrollArea {{
                border: 1px solid {border_subtle};
                border-radius: 12px;
                background-color: {canvas_bg};
            }}
            QWidget {{
                background-color: {canvas_bg};
            }}
        """)
        self.preview_lbl.setStyleSheet(f"background-color: {canvas_bg}; border: none;")

    def set_theme(self, theme: str):
        """Actualiza el tema del panel y regenera el renderizado con el color de alto contraste."""
        self.current_theme = theme
        self._update_theme_ui()
        self.update_preview(self.current_latex)

    def _zoom_in(self):
        """Aumenta el factor de escala interactivo y habilita el desplazamiento libre."""
        self.is_auto_fit = False
        self.zoom_factor = min(4.0, round(self.zoom_factor * 1.25, 2))
        self.lbl_zoom.setText(f"{int(self.zoom_factor * 100)}%")
        self.update_preview(self.current_latex)

    def _zoom_out(self):
        """Reduce el factor de escala interactivo."""
        self.is_auto_fit = False
        self.zoom_factor = max(0.25, round(self.zoom_factor * 0.8, 2))
        self.lbl_zoom.setText(f"{int(self.zoom_factor * 100)}%")
        self.update_preview(self.current_latex)

    def _zoom_reset(self):
        """Restablece al modo de auto-ajuste para ver la fórmula completa sin barras de desplazamiento."""
        self.is_auto_fit = True
        self.zoom_factor = 1.0
        self.lbl_zoom.setText("Zoom")
        self.update_preview(self.current_latex)

    def resizeEvent(self, event):
        """Ajusta automáticamente la visualización al redimensionarse el panel si está en modo auto-fit."""
        super().resizeEvent(event)
        if self.is_auto_fit and self.current_latex:
            self.update_preview(self.current_latex)

    def update_preview(self, latex_str: str | None = None) -> None:
        """Actualiza la visualización renderizada de la fórmula en tiempo real.

        Args:
            latex_str: La fórmula matemática en sintaxis LaTeX a renderizar o None.
        """
        if latex_str is None:
            latex_str = LaTeXTranslator.to_latex(self.math_tree)

        self.current_latex = latex_str or ""
        if not latex_str or latex_str.strip() == "":
            self.preview_lbl.clear()
            self.current_svg = ""
            return

        t = get_theme_dict(self.current_theme)
        theme_fg = t.get("text_rendered_math", t["text_primary"])

        # Guardar string puro para previsualización
        self.current_svg = SVGMathCache.get_instance().get_svg_string(
            latex_str, theme_fg
        )

        # Obtener dimensiones disponibles en el viewport del scroll_area
        vp_width = (
            self.scroll_area.viewport().width()
            if self.scroll_area.viewport()
            else self.scroll_area.width()
        )
        vp_height = (
            self.scroll_area.viewport().height()
            if self.scroll_area.viewport()
            else self.scroll_area.height()
        )
        if vp_width <= 10:
            vp_width = max(200, self.width() - 40)
        if vp_height <= 10:
            vp_height = max(100, self.height() - 80)

        # Solicitar Pixmap al caché con auto-ajuste y zoom interactivo
        pixmap = SVGMathCache.get_instance().get_dynamic_preview_pixmap(
            latex_str,
            theme_fg,
            base_scale=0.15,
            min_scale=0.025,
            max_width=vp_width,
            max_height=vp_height,
            zoom_multiplier=self.zoom_factor,
            is_auto_fit=self.is_auto_fit,
        )
        self.preview_lbl.setPixmap(pixmap)

    def _export_png(self):
        options = QFileDialog.Option.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Fórmula como Imagen PNG",
            "formula.png",
            "Imágenes PNG (*.png)",
            options=options,
        )
        if not file_path:
            return

        latex_str = LaTeXTranslator.to_latex(self.math_tree)
        if not latex_str or not latex_str.strip():
            return

        # Para exportación gráfica se genera el SVG con trazos negros (#000000)
        svg_code = SVGMathCache.get_instance().get_svg_string(latex_str, "#000000")
        renderer = QSvgRenderer(QByteArray(svg_code.encode("utf-8")))

        if not renderer.isValid():
            get_logger().error(
                "[EXPORT_PNG] QSvgRenderer no pudo validar el SVG para exportar."
            )
            return

        vb = renderer.viewBoxF()
        w0 = vb.width() if vb.width() > 0 else float(renderer.defaultSize().width())
        h0 = vb.height() if vb.height() > 0 else float(renderer.defaultSize().height())
        if w0 <= 0:
            w0 = 200.0
        if h0 <= 0:
            h0 = 100.0

        # Escala HD de alta resolución (300 DPI equivalente)
        scale = 0.35
        target_w = max(1, int(w0 * scale))
        target_h = max(1, int(h0 * scale))
        padding = 32

        image = QImage(
            target_w + padding * 2, target_h + padding * 2, QImage.Format.Format_ARGB32
        )
        image.fill(QColor("#FFFFFF"))

        painter = QPainter(image)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        renderer.render(
            painter,
            QRectF(float(padding), float(padding), float(target_w), float(target_h)),
        )
        painter.end()

        saved = image.save(file_path, "PNG")
        if saved:
            get_logger().info(
                f"[EXPORT_PNG] Imagen guardada exitosamente en {file_path}"
            )
        else:
            get_logger().error(
                f"[EXPORT_PNG] Falló al escribir el archivo PNG en {file_path}"
            )

    def _export_svg(self):
        options = QFileDialog.Option.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Fórmula como SVG Vectorial",
            "formula.svg",
            "Gráficos Vectoriales SVG (*.svg)",
            options=options,
        )
        if not file_path:
            return

        latex_str = LaTeXTranslator.to_latex(self.math_tree)
        if not latex_str or not latex_str.strip():
            return

        # Para exportación vectorial se genera con trazos negros (#000000) y fondo blanco
        svg_code = SVGMathCache.get_instance().get_svg_string(latex_str, "#000000")
        svg_content = ensure_svg_white_background(svg_code)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(svg_content)
            get_logger().info(
                f"[EXPORT_SVG] Archivo SVG guardado exitosamente en {file_path}"
            )
        except OSError as e:
            get_logger().error(f"[EXPORT_SVG] Error al escribir archivo SVG: {e}")
