"""
---
file: src/core/renderer.py
module: src.core.renderer
description: Renderizador visual de fórmulas LaTeX a QPixmap mediante Matplotlib OO Agg API.
type: core/renderer
version: 1.0.0
date: 2026-08-24
dependencies: []
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/palette_widget.py
exports:
  - MathRenderer: "Renderizador de tipografía matemática a imágenes QPixmap con transparencia"
test: pytest tests/test_editor_widget.py
constraints:
  - "Utilizar exclusivamente el backend Agg sin crear ventanas de Matplotlib que interfieran con Qt"
  - "Normalizar entornos de matriz pmatrix/bmatrix a sintaxis compatible con MathText"
keywords:
  - matplotlib-agg
  - mathtext
  - qpixmap
  - formula-renderer
  - latex-rendering
---

Matplotlib-backed High DPI Visual Math Renderer (Pure OO API)
Renders LaTeX math formulas into QPixmap safely without interfering with Qt's GUI event loop.
"""

from __future__ import annotations

import io
from dataclasses import dataclass

import matplotlib

matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from PySide6.QtGui import QImage, QPixmap


# 3. Configuración Operativa de Renderizado
@dataclass(frozen=True)
class RendererConfig:
    """Parámetros de configuración del motor de renderizado gráfico de Matplotlib.

    Attributes:
        default_fontsize: Tamaño de fuente base predeterminado.
        default_dpi: Densidad de puntos por pulgada para exportaciones rasterizadas.
        default_color: Color hexadecimal predeterminado del texto matemático.
        error_color: Color hexadecimal para mensajes de error.
    """

    default_fontsize: int = 18
    default_dpi: int = 180
    default_color: str = "#E2E2E9"
    error_color: str = "#E3327B"


RENDERER_CONFIG = RendererConfig()


class MathRenderer:
    """Renderizador vectorial de código LaTeX a `QPixmap`.

    Utiliza el motor gráfico OO Agg de Matplotlib para generar imágenes
    de alta calidad sin bloquear ni interferir con el bucle de eventos de PySide6.
    """

    @staticmethod
    def render_latex_to_pixmap(
        latex_str: str, fontsize: int = 18, color: str = "#E2E2E9", dpi: int = 180
    ) -> QPixmap:
        """Renderiza una cadena LaTeX matemática a un QPixmap con transparencia.

        Aplica normalización previa al texto para asegurar la compatibilidad
        con el motor MathText de Matplotlib (e.g. entornos de matrices).

        Args:
            latex_str: La fórmula en código LaTeX crudo.
            fontsize: Tamaño de la fuente base.
            color: Color del texto en formato hexadecimal.
            dpi: Resolución de la imagen generada.

        Returns:
            Una instancia de `QPixmap` conteniendo la imagen renderizada.
        """
        if not latex_str or latex_str.strip() == "":
            latex_str = r"\text{Selecciona o escribe una fórmula}"

        # Compatibilidad con Matplotlib mathtext
        latex_str = latex_str.replace(r"\begin{pmatrix}", r"\left( \begin{matrix}")
        latex_str = latex_str.replace(r"\end{pmatrix}", r"\end{matrix} \right)")
        latex_str = latex_str.replace(r"\begin{bmatrix}", r"\left[ \begin{matrix}")
        latex_str = latex_str.replace(r"\end{bmatrix}", r"\end{matrix} \right]")
        latex_str = latex_str.replace(r"\begin{vmatrix}", r"\left| \begin{matrix}")
        latex_str = latex_str.replace(r"\end{vmatrix}", r"\end{matrix} \right|")

        # Asegurarse de que los saltos de línea de las matrices se procesen bien
        latex_str = latex_str.replace(r"\\", r"\\ ")

        formatted_latex = f"${latex_str}$"

        try:
            fig = Figure(figsize=(4, 1.2), dpi=dpi)
            fig.patch.set_alpha(0.0)
            canvas = FigureCanvasAgg(fig)

            text_obj = fig.text(
                0.5,
                0.5,
                formatted_latex,
                fontsize=fontsize,
                color=color,
                ha="center",
                va="center",
            )

            canvas.draw()
            renderer = canvas.get_renderer()
            bbox = text_obj.get_window_extent(renderer)

            width_in = max((bbox.width + 30) / dpi, 1.5)
            height_in = max((bbox.height + 30) / dpi, 0.8)
            fig.set_size_inches(width_in, height_in)

            canvas.draw()

            buf = io.BytesIO()
            fig.savefig(
                buf,
                format="png",
                dpi=dpi,
                transparent=True,
                bbox_inches="tight",
                pad_inches=0.1,
            )

            buf.seek(0)
            qimg = QImage.fromData(buf.read())
            return QPixmap.fromImage(qimg)
        except Exception as e:  # noqa: BLE001
            return MathRenderer._render_error(str(e))

    @staticmethod
    def _render_error(error_msg: str) -> QPixmap:
        """Renderiza una imagen con un mensaje de error visual.

        Args:
            error_msg: Mensaje descriptivo del error a mostrar (actualmente ignorado en el visual final).

        Returns:
            Una instancia de `QPixmap` mostrando el texto de error en rojo.
        """
        try:
            fig = Figure(figsize=(4, 1), dpi=150)
            fig.patch.set_alpha(0.0)
            canvas = FigureCanvasAgg(fig)
            fig.text(
                0.5,
                0.5,
                "Sintaxis incompleta o inválida",
                fontsize=11,
                color="#FF7675",
                ha="center",
                va="center",
            )
            canvas.draw()
            buf = io.BytesIO()
            fig.savefig(
                buf, format="png", dpi=150, transparent=True, bbox_inches="tight"
            )
            buf.seek(0)
            qimg = QImage.fromData(buf.read())
            return QPixmap.fromImage(qimg)
        except Exception:  # noqa: BLE001
            return QPixmap()
