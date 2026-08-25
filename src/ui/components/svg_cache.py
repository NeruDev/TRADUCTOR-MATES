"""
---
file: src/ui/components/svg_cache.py
module: src.ui.components.svg_cache
description: Motor de renderizado SVG y caché para fórmulas con zoom adaptativo dinámico.
type: ui/component
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.logger
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/preview_panel.py
  - src/ui/components/palette_widget.py
exports:
  - SVGMathCache: "Motor Singleton de renderizado vectorial SVG y caché de pixmaps"
test: pytest tests/test_editor_widget.py
constraints:
  - "Garantizar la thread-safety y el almacenamiento eficiente en caché de pixmaps SVG"
keywords:
  - svg-math-cache
  - dynamic-preview
  - svg-icons
  - miniracer-mathjax
---

SVG rendering engine and cache for math formulas with dynamic adaptive zooming.
"""

from __future__ import annotations

import os

os.environ.setdefault("QT_SVG_DEFAULT_OPTIONS", "2")

from PySide6.QtCore import QByteArray, QObject, QRectF, QSize, Qt
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer, QtSvg

from src.core.logger import ERROR_CODES, get_logger

# Configurar QtSvg para asumir fuentes seguras locales y deshabilitar límite de 32 nodos anidados
QSvgRenderer.setDefaultOptions(QtSvg.Option.AssumeTrustedSource)


class SVGMathCache(QObject):
    """Caché y motor síncrono de compilación LaTeX a SVG a través de MiniRacer.

    Actúa como Singleton para pre-cargar en memoria la biblioteca Node de MathJax.
    Mejora dramáticamente los tiempos de renderizado al no depender del
    loop de red ni de QWebEngineView para extraer los gráficos puros.
    """

    _instance: SVGMathCache | None = None

    @classmethod
    def get_instance(cls) -> SVGMathCache:
        """Recupera la única instancia del gestor de caché.

        Returns:
            La instancia inicializada globalmente de `SVGMathCache`.
        """
        if cls._instance is None:
            cls._instance = SVGMathCache()
        return cls._instance

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ctx = None

    def _ensure_v8_initialized(self):
        if self.ctx is not None:
            return

        from py_mini_racer import MiniRacer

        self.ctx = MiniRacer()

        base_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "assets")
        )
        js_path = os.path.join(base_dir, "mathjax_bundle.js")

        logger = get_logger()
        logger.debug(f"[SVGMathCache] base_dir absolute path: {base_dir}")
        logger.debug(f"[SVGMathCache] js_path absolute path: {js_path}")

        try:
            with open(js_path, "r", encoding="utf-8") as f:
                js_code = f.read()
            # Inyectar shims para globales básicos y módulos Node
            shims = """
            var window = this;
            var global = this;
            var document = { 
                createElement: function() { return {}; },
                getElementsByTagName: function() { return []; },
                documentElement: { style: {} }
            };
            var __dirname = '';
            var process = { env: {}, cwd: function() { return ''; } };
            var module = { exports: {} };
            var exports = module.exports;
            var _path = { resolve: function() { return ''; }, join: function() { return ''; }, dirname: function() { return ''; } };
            var _fs = { readFileSync: function() { return ''; }, existsSync: function() { return false; } };
            function require(m) {
                if (m === 'path') return _path;
                if (m === 'fs') return _fs;
                return {};
            }
            """
            self.ctx.eval(shims)
            self.ctx.eval(js_code)
            logger.debug(
                "[SVGMathCache] Motor JS síncrono (MiniRacer) cargado exitosamente."
            )
        except OSError as e:
            logger.error(
                f"{ERROR_CODES['CACHE_ERR']} Error al cargar mathjax_bundle.js: {e!s}"
            )
        except Exception as e:  # noqa: BLE001
            logger.error(
                f"{ERROR_CODES['CACHE_ERR']} Error al evaluar JS en MiniRacer: {e!s}"
            )

    def get_svg_string(self, latex: str, theme_color: str) -> str:
        """Compila una expresión LaTeX a código XML SVG mediante MathJax y MiniRacer.

        Args:
            latex: La fórmula matemática en sintaxis LaTeX.
            theme_color: Color hexadecimal a aplicar a los glifos matemáticos.

        Returns:
            Cadena de texto con el código XML del elemento SVG aislado y sanitizado.
        """
        self._ensure_v8_initialized()

        if not latex or not latex.strip():
            latex = r"\text{Selecciona o escribe una fórmula}"

        try:
            svg_string = self.ctx.call(
                "renderMathSync", latex, "transparent", theme_color
            )
        except Exception as e:  # noqa: BLE001
            get_logger().error(f"[SVGMathCache] Error evaluando renderMathSync: {e!s}")
            svg_string = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20"><text x="0" y="15" fill="{theme_color}" font-size="10">Error JS</text></svg>'

        if not isinstance(svg_string, str):
            svg_string = ""

        start = svg_string.find("<svg")
        end = svg_string.rfind("</svg>")
        if start != -1 and end != -1:
            svg_string = svg_string[start : end + 6]

        if "xmlns=" not in svg_string:
            svg_string = svg_string.replace(
                "<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1
            )

        svg_string = svg_string.replace("currentColor", theme_color)
        return svg_string

    def get_svg_icon(
        self, latex: str, theme_color: str, width: int = 140, height: int = 60
    ) -> QPixmap:
        """Renderiza una fórmula matemática a un QPixmap con tamaño acotado.

        Args:
            latex: La expresión en LaTeX a renderizar.
            theme_color: Color hexadecimal a aplicar a los trazos matemáticos.
            width: Ancho máximo en píxeles del lienzo generado.
            height: Alto máximo en píxeles del lienzo generado.

        Returns:
            Una instancia de QPixmap con el gráfico centrado y fondo transparente.
        """
        # 1. Solicitar string a V8
        svg_str = self.get_svg_string(latex, theme_color)

        logger = get_logger()
        logger.debug(
            f"[SVG PAYLOAD] LaTeX: '{latex[:15]}' | V8 Return: {svg_str[:100]}"
        )

        if "[object" in svg_str or "Promise" in svg_str:
            logger.error(
                f"[SVG FATAL] V8 devolvió una estructura asíncrona o inválida: {svg_str[:50]}"
            )
            return QPixmap(width, height)

        start = svg_str.find("<svg")
        end = svg_str.rfind("</svg>")
        if start != -1 and end != -1:
            svg_str = svg_str[start : end + 6]
        else:
            logger.error(f"[SVG FATAL] No se encontró etiqueta <svg>: {svg_str[:50]}")
            pix = QPixmap(width, height)
            pix.fill(Qt.GlobalColor.transparent)
            return pix

        # 2. Inyectar compatibilidad estricta para el parseo de QSvgRenderer
        if "xmlns=" not in svg_str:
            svg_str = svg_str.replace(
                "<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1
            )

        # 3. Forzar el color del tema
        svg_str = svg_str.replace("currentColor", theme_color)

        # 4. Renderizado nativo seguro
        byte_array = QByteArray(svg_str.encode("utf-8"))
        renderer = QSvgRenderer(byte_array)

        if not renderer.isValid():
            logger.error(
                "[SVG FATAL] QSvgRenderer rechazó el código XML/SVG sanitizado."
            )

        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.GlobalColor.transparent)

        original_size = renderer.defaultSize()
        if original_size.isEmpty():
            original_size = QSize(100, 50)

        target_size = original_size.scaled(
            pixmap.size(), Qt.AspectRatioMode.KeepAspectRatio
        )

        x = (pixmap.width() - target_size.width()) / 2.0
        y = (pixmap.height() - target_size.height()) / 2.0
        target_rect = QRectF(x, y, target_size.width(), target_size.height())

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        renderer.render(painter, target_rect)
        painter.end()

        return pixmap

    def get_dynamic_preview_pixmap(
        self,
        latex: str,
        theme_color: str,
        base_scale: float = 0.15,
        min_scale: float = 0.025,
        max_width: int | None = None,
        max_height: int | None = None,
        zoom_multiplier: float = 1.0,
        is_auto_fit: bool = True,
        padding: int = 16,
    ) -> QPixmap:
        """Renderiza una fórmula matemática con zoom adaptativo dinámico y auto-ajuste.

        Inicia con una escala prominente (125% estándar, base_scale = 0.15) para
        expresiones cortas y medianas, y reduce suavemente el factor de escala
        para fórmulas muy largas (como la norma vectorial o series extensas) para
        mantener una lectura balanceada sin desbordes. Además permite auto-ajustar
        la ecuación al ancho del viewport para evitar barras de desplazamiento en el inicio.

        Args:
            latex: La expresión en LaTeX a compilar y renderizar.
            theme_color: Color hexadecimal de los trazos matemáticos.
            base_scale: Factor de escala base para fórmulas estándar/cortas (125%).
            min_scale: Factor de escala mínimo para fórmulas muy extensas.
            max_width: Ancho máximo disponible en píxeles (viewport del scroll).
            max_height: Alto máximo disponible en píxeles (viewport del scroll).
            zoom_multiplier: Multiplicador manual de zoom para ampliación interactiva.
            is_auto_fit: Indica si se debe forzar el ajuste al tamaño del contenedor.
            padding: Margen interno de resguardo en píxeles alrededor de la ecuación.

        Returns:
            Una instancia de QPixmap de alta resolución con el renderizado dinámico.
        """
        svg_str = self.get_svg_string(latex, theme_color)
        logger = get_logger()

        if "[object" in svg_str or "Promise" in svg_str or not svg_str:
            logger.error(f"[SVG FATAL] V8 devolvió un SVG no válido: {svg_str[:50]}")
            pix = QPixmap(100, 50)
            pix.fill(Qt.GlobalColor.transparent)
            return pix

        start = svg_str.find("<svg")
        end = svg_str.rfind("</svg>")
        if start != -1 and end != -1:
            svg_str = svg_str[start : end + 6]
        else:
            pix = QPixmap(100, 50)
            pix.fill(Qt.GlobalColor.transparent)
            return pix

        if "xmlns=" not in svg_str:
            svg_str = svg_str.replace(
                "<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1
            )

        svg_str = svg_str.replace("currentColor", theme_color)

        byte_array = QByteArray(svg_str.encode("utf-8"))
        renderer = QSvgRenderer(byte_array)

        if not renderer.isValid():
            logger.error("[SVG FATAL] QSvgRenderer no pudo validar el SVG dinámico.")
            pix = QPixmap(100, 50)
            pix.fill(Qt.GlobalColor.transparent)
            return pix

        vb = renderer.viewBoxF()
        w0 = vb.width() if vb.width() > 0 else float(renderer.defaultSize().width())
        h0 = vb.height() if vb.height() > 0 else float(renderer.defaultSize().height())
        if w0 <= 0:
            w0 = 100.0
        if h0 <= 0:
            h0 = 50.0

        # 1. Curva de decaimiento adaptativa: estándar 125% para fórmulas cortas y medianas,
        # con amortiguación progresiva en fórmulas muy largas (ej. norma vectorial) para evitar desbordes.
        if w0 > 8500.0:
            w_factor = ((2600.0 / 8500.0) ** 0.38) * ((8500.0 / w0) ** 0.62)
        else:
            w_factor = (2600.0 / max(2600.0, w0)) ** 0.38

        h_factor = (1500.0 / max(1500.0, h0)) ** 0.28
        scale = max(min_scale, min(base_scale, base_scale * w_factor * h_factor))

        # 2. Si está en modo auto-fit, verificar y acotar para que quepa en el viewport
        if is_auto_fit:
            if max_width is not None and max_width > padding * 2:
                avail_w = max_width - padding * 2
                if w0 * scale > avail_w:
                    scale = max(min_scale, avail_w / w0)
            if max_height is not None and max_height > padding * 2:
                avail_h = max_height - padding * 2
                if h0 * scale > avail_h:
                    scale = max(min_scale, min(scale, avail_h / h0))

        # 3. Aplicar multiplicador de zoom manual
        final_scale = scale * zoom_multiplier

        target_w = max(1, int(w0 * final_scale))
        target_h = max(1, int(h0 * final_scale))

        pixmap = QPixmap(target_w + padding * 2, target_h + padding * 2)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        renderer.render(
            painter,
            QRectF(float(padding), float(padding), float(target_w), float(target_h)),
        )
        painter.end()

        return pixmap
