"""
---
file: src/ui/components/help_dialog.py
module: src.ui.components.help_dialog
description: Ventana modal de ayuda y guía de usuario interactiva para Traductor Mates.
type: ui/dialog
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.ui.theme
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/action_bar.py
exports:
  - HelpDialog: "Ventana modal de guía de usuario con soporte de navegación HTML y temas"
test: pytest tests/test_editor_widget.py
constraints:
  - "Adaptar la paleta de colores del visor HTML dinámicamente al tema oscuro/claro"
keywords:
  - help-dialog
  - user-guide
  - manual
  - modal-dialog
  - qtextbrowser
---

Help & Documentation Dialog Window.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from src.ui.theme import COLOR_MIKU_CYAN, get_theme_dict, get_theme_qss


class HelpDialog(QDialog):
    """Cuadro de diálogo modal que contiene la guía interactiva completa del sistema.

    Proporciona un visor estructurado en formato Markdown con explicaciones
    exhaustivas sobre el editor, las ramas de matemáticas y física, el sistema
    de variantes de usuario, los catálogos y las herramientas de exportación.

    Args:
        parent: Widget padre que invoca el diálogo (típicamente MainWindow o MathActionBarWidget).
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Guía de Usuario y Documentación - Traductor Mates")
        self.resize(780, 580)
        self.setMinimumSize(600, 450)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)

        p = self.parent()
        self.current_theme = (
            p.current_theme if p and hasattr(p, "current_theme") else "dark"
        )
        self.setStyleSheet(get_theme_qss(self.current_theme))

        self._setup_ui()

    def _setup_ui(self) -> None:
        """Construye la interfaz gráfica y renderiza el contenido en Markdown."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        bg_frame = QFrame()
        bg_frame.setProperty("class", "android-card")
        layout = QVBoxLayout(bg_frame)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        main_layout.addWidget(bg_frame)

        t = get_theme_dict(self.current_theme)
        primary_col = t.get("primary", COLOR_MIKU_CYAN)

        # Cabecera
        header_layout = QHBoxLayout()
        title_lbl = QLabel("📖 Guía de Uso y Manual del Sistema")
        title_lbl.setProperty("class", "h2")
        title_lbl.setStyleSheet(
            f"font-weight: bold; font-size: 16px; color: {primary_col};"
        )
        header_layout.addWidget(title_lbl)
        header_layout.addStretch()
        layout.addLayout(header_layout)

        # Visor de texto enriquecido / Markdown
        self.browser = QTextBrowser()
        self.browser.setOpenExternalLinks(True)
        self.browser.setStyleSheet(f"""
            QTextBrowser {{
                background-color: {t.get("surface", "#1E1E1E")};
                color: {t.get("text_primary", "#E0E0E0")};
                border: 1px solid {t.get("border", "#333333")};
                border-radius: 8px;
                padding: 12px;
                font-size: 13px;
                line-height: 1.5;
            }}
        """)
        self.browser.setHtml(self._get_help_html())
        layout.addWidget(self.browser, stretch=1)

        # Botón de cierre
        btn_box = QHBoxLayout()
        btn_box.addStretch()
        btn_close = QPushButton("Entendido, cerrar")
        btn_close.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_close.setStyleSheet(f"""
            QPushButton {{
                background-color: {primary_col};
                color: #FFFFFF;
                border: none;
                border-radius: 6px;
                padding: 8px 18px;
                font-weight: bold;
                font-size: 12px;
            }}
            QPushButton:hover {{
                opacity: 0.9;
            }}
        """)
        btn_close.clicked.connect(self.accept)
        btn_box.addWidget(btn_close)
        layout.addLayout(btn_box)

    def _get_help_html(self) -> str:
        """Genera el contenido estructurado en HTML semántico para el visor.

        Returns:
            Cadena HTML con formato estilizado según el tema de la aplicación.
        """
        t = get_theme_dict(self.current_theme)
        cyan = t.get("primary", COLOR_MIKU_CYAN)
        surface_var = t.get("surface_variant", "#262636")
        border = t.get("border", "#333333")

        return f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Segoe UI', sans-serif; font-size: 13px; line-height: 1.6; }}
                h1, h2, h3 {{ color: {cyan}; margin-top: 14px; margin-bottom: 6px; }}
                h2 {{ font-size: 15px; border-bottom: 1px solid {border}; padding-bottom: 4px; }}
                h3 {{ font-size: 13px; color: #FFFFFF; }}
                p, li {{ color: {t.get("text_primary", "#E0E0E0")}; }}
                ul {{ margin-top: 4px; margin-bottom: 10px; padding-left: 20px; }}
                code {{ background-color: {surface_var}; color: {cyan}; padding: 2px 5px; border-radius: 4px; font-family: 'Consolas', monospace; font-size: 12px; }}
                .badge {{ background-color: {surface_var}; border: 1px solid {border}; border-radius: 4px; padding: 2px 6px; font-size: 11px; }}
                .note {{ background-color: {surface_var}; border-left: 4px solid {cyan}; padding: 8px 12px; margin: 10px 0; border-radius: 0 6px 6px 0; }}
            </style>
        </head>
        <body>
            <h2>📐 1. Estructura y Distribución de los 4 Paneles</h2>
            <p>Traductor Mates organiza su espacio de trabajo en cuatro cuadrantes principales mediante divisores ajustables (Splitters 50/50):</p>
            <ul>
                <li><b>Superior Izquierdo (Editor Interactivo):</b> Lienzo visual bidimensional con casillas editables para la construcción matemática en vivo.</li>
                <li><b>Inferior Izquierdo (Paleta & Compendios):</b> Acceso a plantillas, símbolos, compendio de fórmulas (Formulario) y fórmulas personalizadas (Usuario).</li>
                <li><b>Superior Derecho (Vista Previa KaTeX):</b> Renderizado de alta definición con zoom ajustable y exportación directa en PNG y SVG.</li>
                <li><b>Inferior Derecho (Traductor Multilenguaje):</b> Código fuente simultáneo en LaTeX, Python (SymPy), Wolfram Alpha y Markdown con botón de copiado rápido.</li>
            </ul>

            <h2>⌨️ 2. Editor Estructural y Navegación por Casillas</h2>
            <ul>
                <li><b>Casillas Rellenables (<code>[ □ ]</code>):</b> Haz clic sobre cualquier casilla vacía o llena para enfocarla y escribir en ella.</li>
                <li><b>Navegación Rápida:</b> Usa <code>Tab</code> para saltar a la siguiente casilla del árbol y <code>Shift + Tab</code> para retroceder.</li>
                <li><b>Inserción Inteligente sin Sobrescritura:</b> Al insertar una plantilla o símbolo desde la paleta, se inyecta directamente dentro de la casilla activa (subnodo del AST) sin alterar el resto de la ecuación.</li>
                <li><b>Recuperación de Sesión (Crash Recovery):</b> El sistema guarda periódicamente tu ecuación en curso. Si la app se cierra inesperadamente, recuperará tu progreso al arrancar.</li>
            </ul>

            <h2>📚 3. Formulario Clasificado y Carrusel de Variantes</h2>
            <ul>
                <li><b>Ramas de Estudio:</b> Selecciona entre <b>📐 Matemáticas</b> y <b>⚛️ Física</b> en el panel lateral.</li>
                <li><b>Niveles de Complejidad:</b> Alterna entre los niveles <b>Básico</b>, <b>Intermedio</b> y <b>Avanzado</b> identificados con indicadores circulares de color.</li>
                <li><b>Acordeones Desplegables:</b> Haz clic en cualquier categoría (<code>▼</code> / <code>▶</code>) para desplegar u ocultar sus fórmulas.</li>
                <li><b>Carrusel de Variantes (<code>&lt; 1/N &gt;</code>):</b> Las tarjetas que agrupan métodos o fórmulas asociadas (ej. formas canónicas, despejes o casos particulares) disponen de flechas para navegar entre sus variantes. Al hacer clic sobre la tarjeta se inserta la variante activa.</li>
                <li><b>Buscador Global en Tiempo Real:</b> Usa la barra superior de la paleta para filtrar instantáneamente cualquier fórmula por nombre, descripción o código LaTeX.</li>
            </ul>

            <h2>👤 4. Pestaña de Usuario y Fórmulas Personalizadas</h2>
            <ul>
                <li><b>Guardar una Fórmula:</b> Pulsa el botón <b>Guardar Fórmula</b> en la barra superior para registrar tu ecuación actual.</li>
                <li><b>Ventana de Guardado In-App:</b> Visualiza la fórmula renderizada y clasifícala por <b>Rama</b>, <b>Categoría</b>, <b>Descripción</b> (resaltada en color turquesa Miku), <b>Subcategoría</b> opcional y <b>Nombre</b>.</li>
                <li><b>Gestión de Variantes y Demostraciones:</b> En la ventana de <b>Editar Fórmula</b> (clic derecho sobre una tarjeta), puedes añadir múltiples variantes con <code>➕ Agregar Variante</code>, navegar con flechas <code>&lt; &gt;</code> y activar la casilla para personalizar el nombre de cada paso/variante.</li>
                <li><b>Menús Contextuales (Clic Derecho):</b>
                    <ul>
                        <li><b>En Fórmulas:</b> Editar fórmula/variantes, eliminar y marcar/desmarcar como Favorito (⭐).</li>
                        <li><b>En Categorías/Subcategorías:</b> Editar nombre, eliminar la sección completa, o moverla hacia arriba/abajo en el orden visual.</li>
                    </ul>
                </li>
            </ul>

            <h2>📏 5. Catálogo de Constantes y Unidades Físicas</h2>
            <ul>
                <li><b>Pestaña de Constantes:</b> Compendio de constantes físicas universales, gravitatorias, electromagnéticas y atómicas actualizadas a los estándares oficiales <b>CODATA 2022</b>.</li>
                <li><b>Pestaña de Unidades:</b> Tabla de magnitudes fundamentales del SI, magnitudes derivadas y unidades de ingeniería no-SI (eV, bar, cal, etc.).</li>
            </ul>

            <h2>💾 6. Exportación, Copiado y Diagnóstico</h2>
            <ul>
                <li><b>Exportar Imagen:</b> En la Vista Previa, despliega el botón de exportación para guardar tu fórmula en formato <b>PNG (rasterizado)</b> o <b>SVG (vectorial puro)</b>.</li>
                <li><b>Copiar Código:</b> En el panel de traducción, pulsa <code>📋 Copiar LaTeX</code> o <code>📝 Copiar Markdown</code> para llevar la ecuación lista a tus documentos o apuntes.</li>
                <li><b>Visor de Logs:</b> Accede a <code>📋 Logs</code> en la barra superior para inspeccionar en tiempo real el registro de eventos y trazas de diagnóstico de la sesión.</li>
            </ul>

            <div class="note">
                <b>💡 Consejo:</b> Puedes alternar entre el <b>☀️ Modo Claro</b> y el <b>🌙 Modo Oscuro</b> en cualquier momento desde la barra de acciones superior sin reiniciar la aplicación.
            </div>
        </body>
        </html>
        """
