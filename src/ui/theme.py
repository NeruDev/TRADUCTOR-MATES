"""
---
file: src/ui/theme.py
module: src.ui.theme
description: Sistema de diseño y temas dinámicos inspirados en Hatsune Miku (Modo Claro/Oscuro y QSS).
type: ui/theme
version: 1.0.0
date: 2026-08-24
dependencies: []
relations:
  - docs/ARCHITECTURE.md
  - src/ui/main_window.py
  - src/core/syntax.py
exports:
  - get_theme_dict: "Devuelve el diccionario de colores semánticos según el tema activo"
  - get_theme_qss: "Genera dinámicamente la hoja de estilos QSS completa para PySide6"
test: pytest tests/test_theme.py
constraints:
  - "Mantener la paridad de tokens semánticos en ambos temas (Dark Studio y Light Canvas)"
keywords:
  - hatsune-miku
  - miku-theme
  - qss-stylesheet
  - dark-mode
  - light-mode
  - theme-generator
---

Hatsune Miku Inspired Theme & Design System (Dark & Light Modes)
Provides dynamic QSS stylesheets, Hatsune Miku Cyan (#39C5BB) primary accents,
Magenta (#E3327B) secondary accents, dynamic splitters, and dark/light theme switching.
"""

from __future__ import annotations

# Hatsune Miku Signature Colors
COLOR_MIKU_CYAN = "#39C5BB"
COLOR_MIKU_CYAN_HOVER = "#4DD5CC"
COLOR_MIKU_MAGENTA = "#E3327B"
COLOR_MIKU_MAGENTA_HOVER = "#F0488F"

# Default Backward Compatible Constants (Dark Mode)
COLOR_BG = "#121218"
COLOR_SURFACE = "#1A1A24"
COLOR_SURFACE_VARIANT = "#242432"
COLOR_SURFACE_SLOT = "#181822"
COLOR_PRIMARY = COLOR_MIKU_CYAN
COLOR_PRIMARY_HOVER = COLOR_MIKU_CYAN_HOVER
COLOR_SECONDARY = COLOR_MIKU_MAGENTA
COLOR_ACCENT = "#FF7675"
COLOR_TEXT_PRIMARY = "#E2E2E9"
COLOR_TEXT_SECONDARY = "#9E9EB3"
COLOR_BORDER = "#2F2F42"
COLOR_ACTIVE_SLOT = COLOR_MIKU_CYAN

# Theme Palettes Dictionary
THEMES = {
    "dark": {
        "bg": "#0F1017",
        "surface": "#181924",
        "surface_variant": "#1E1F2D",
        "surface_slot": "#13141C",
        "bg_canvas_editor": "#13141C",
        "bg_canvas_render": "#13141C",
        "bg_subpanel": "#181924",
        "bg_item_card": "#1E1F2D",
        "bg_item_card_hover": "#252738",
        "primary": COLOR_MIKU_CYAN,
        "primary_hover": COLOR_MIKU_CYAN_HOVER,
        "secondary": COLOR_MIKU_MAGENTA,
        "secondary_hover": COLOR_MIKU_MAGENTA_HOVER,
        "text_primary": "#F8FAFC",
        "text_secondary": "#94A3B8",
        "text_rendered_math": "#F8FAFC",
        "border": "#2E3144",
        "border_subtle": "#2E3144",
        "border_grid_dots": "#2A2C3F",
        "active_slot": COLOR_MIKU_CYAN,
        "code_bg": "#0D0D14",
        "scroll_bg": "#12121B",
        # Math Semantic Syntax Tokens
        "math_var_color": "#61AFEF",  # Azul (Variables)
        "math_num_color": "#E5C07B",  # Oro/Amarillo (Números)
        "math_op_color": "#C678DD",  # Rojo/Rosa (Operadores)
        "math_cmd_color": "#56B6C2",  # Púrpura (Comandos)
        "math_delim_color": "#ABB2BF",  # Gris Base
        "rainbow_1": "#98C379",  # Naranja
        "rainbow_2": "#4169E1",  # Azul Rey
        "rainbow_3": "#E5C07B",  # Verde Lima
        "rainbow_4": "#E3327B",  # Magenta
        "math_box_border": "#39C5BB",
        "math_box_bg_focus": "rgba(57, 197, 187, 0.08)",
        "math_box_bg_active": "rgba(57, 197, 187, 0.22)",
    },
    "light": {
        "bg": "#F1F5F9",
        "surface": "#FFFFFF",
        "surface_variant": "#F1F5F9",
        "surface_slot": "#F8FAFC",
        "bg_canvas_editor": "#FFFFFF",
        "bg_canvas_render": "#F8FAFC",
        "bg_subpanel": "#F8FAFC",
        "bg_item_card": "#FFFFFF",
        "bg_item_card_hover": "#F1F5F9",
        "primary": COLOR_MIKU_CYAN,
        "primary_hover": "#2EA69E",
        "secondary": COLOR_MIKU_MAGENTA,
        "secondary_hover": "#C82567",
        "text_primary": "#0F172A",
        "text_secondary": "#64748B",
        "text_rendered_math": "#0F172A",
        "border": "#E2E8F0",
        "border_subtle": "#E2E8F0",
        "border_grid_dots": "#CBD5E1",
        "active_slot": COLOR_MIKU_CYAN,
        "code_bg": "#FFFFFF",
        "scroll_bg": "#F1F5F9",
        # Math Semantic Syntax Tokens
        "math_var_color": "#005CC5",
        "math_num_color": "#B8860B",
        "math_op_color": "#6F42C1",
        "math_cmd_color": "#00838F",
        "math_delim_color": "#24292E",
        "rainbow_1": "#50A14F",
        "rainbow_2": "#0033CC",
        "rainbow_3": "#B8860B",
        "rainbow_4": "#C2185B",
        "math_box_border": "#00A396",
        "math_box_bg_focus": "rgba(0, 163, 150, 0.10)",
        "math_box_bg_active": "rgba(0, 163, 150, 0.20)",
    },
}


def get_theme_dict(theme_name: str = "dark") -> dict:
    """Obtiene el diccionario de colores asociado a un tema.

    Args:
        theme_name: Identificador del tema (`'dark'` o `'light'`).

    Returns:
        Diccionario con las variables de color (bg, surface, primary, etc).
    """
    return THEMES.get(theme_name, THEMES["dark"])


def get_theme_qss(theme_name: str = "dark") -> str:
    """Genera dinámicamente la hoja de estilos QSS (Qt Style Sheet).

    Incorpora los colores de la paleta solicitada (Hatsune Miku oscuro/claro)
    y retorna la cascada completa para aplicarse a la aplicación.

    Args:
        theme_name: Identificador del tema (`'dark'` o `'light'`).

    Returns:
        Cadena de texto con la sintaxis QSS completa y compilada con las variables de color.
    """
    t = get_theme_dict(theme_name)

    return f"""
QMainWindow {{
    background-color: {t["bg"]};
    color: {t["text_primary"]};
}}

QWidget {{
    font-family: 'Segoe UI', 'Roboto', sans-serif;
    font-size: 13px;
    color: {t["text_primary"]};
}}

/* Cards & Containers */
QFrame.android-card {{
    background-color: {t["surface"]};
    border: 1px solid {t["border"]};
    border-radius: 16px;
    padding: 12px;
}}

QFrame.android-card-flat {{
    background-color: {t["surface_variant"]};
    border: 1px solid {t["border"]};
    border-radius: 12px;
}}

/* Section Titles */
QLabel.section-header {{
    font-size: 14px;
    font-weight: 600;
    color: {t["text_primary"]};
    letter-spacing: 0.5px;
}}

QLabel.section-subtitle {{
    font-size: 11px;
    color: {t["text_secondary"]};
}}

/* Android Material Chips / Tab Buttons */
QPushButton.chip-button {{
    background-color: {t["surface_variant"]};
    color: {t["text_secondary"]};
    border: 1px solid {t["border"]};
    border-radius: 16px;
    padding: 6px 14px;
    font-weight: 500;
}}

QPushButton.chip-button:hover {{
    background-color: {t["primary"]};
    color: #FFFFFF;
}}

QPushButton.chip-button:checked {{
    background-color: {t["primary"]};
    color: #FFFFFF;
    border: 1px solid {t["primary"]};
    font-weight: 600;
}}

/* Symbol & Template Palette Grid Buttons */
QPushButton.symbol-btn {{
    background-color: {t["surface_variant"]};
    color: {t["text_primary"]};
    border: 1px solid {t["border"]};
    border-radius: 10px;
    font-size: 14px;
    font-weight: bold;
    min-width: 44px;
    min-height: 44px;
}}

QPushButton.symbol-btn:hover {{
    background-color: {t["primary"]};
    color: #FFFFFF;
    border-color: {t["primary_hover"]};
}}

QPushButton.template-btn {{
    background-color: {t["surface_variant"]};
    color: {t["text_primary"]};
    border: 1px solid {t["border"]};
    border-radius: 12px;
    padding: 8px;
    text-align: center;
}}

QPushButton.template-btn:hover {{
    background-color: {t["surface_variant"]};
    border-color: {t["primary"]};
}}

/* Action Bar Buttons (Hatsune Miku Primary & Secondary) */
QPushButton.action-btn {{
    background-color: {t["primary"]};
    color: #FFFFFF;
    border: none;
    border-radius: 12px;
    padding: 8px 16px;
    font-weight: 600;
}}

QPushButton.action-btn:hover {{
    background-color: {t["primary_hover"]};
}}

QPushButton.action-btn-secondary {{
    background-color: {t["secondary"]};
    color: #FFFFFF;
    border: none;
    border-radius: 12px;
    padding: 8px 16px;
    font-weight: 600;
}}

QPushButton.action-btn-secondary:hover {{
    background-color: {t["secondary_hover"]};
}}

QPushButton.theme-toggle-btn {{
    background-color: {t["surface_variant"]};
    color: {t["primary"]};
    border: 1px solid {t["primary"]};
    border-radius: 12px;
    padding: 6px 14px;
    font-weight: 600;
}}

QPushButton.theme-toggle-btn:hover {{
    background-color: {t["primary"]};
    color: #FFFFFF;
    border-color: {t["primary_hover"]};
}}

/* Code Blocks & Text Areas */
QPlainTextEdit.code-block {{
    background-color: {t["code_bg"]};
    color: {t["text_primary"]};
    font-family: 'Cascadia Code', 'Consolas', 'Courier New', monospace;
    border: 1px solid {t["border"]};
    border-radius: 12px;
    padding: 10px;
    selection-background-color: {t["primary"]};
}}

/* Menus & Popups */
QMenu {{
    background-color: {t["surface"]};
    color: {t["text_primary"]};
    border: 1px solid {t["border"]};
    border-radius: 10px;
    padding: 6px;
}}

QMenu::item {{
    padding: 6px 16px;
    border-radius: 6px;
    color: {t["text_primary"]};
}}

QMenu::item:selected {{
    background-color: {t["primary"]};
    color: #FFFFFF;
}}

/* Tabs & TabBar */
QTabWidget::pane {{
    border: 1px solid {t["border"]};
    border-radius: 10px;
    background-color: {t["surface"]};
}}

QTabBar::tab {{
    background: {t["surface_variant"]};
    color: {t["text_secondary"]};
    border: 1px solid {t["border"]};
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    padding: 6px 14px;
    font-size: 12px;
    font-weight: 600;
    margin-right: 4px;
}}

QTabBar::tab:hover:!selected {{
    color: {t["secondary"]};
    border-color: {t["secondary"]};
    background: {t["bg_item_card_hover"]};
}}

QTabBar::tab:selected {{
    background: {t["primary"]};
    border: 1px solid {t["primary"]};
    color: #FFFFFF;
    font-weight: bold;
}}

/* Splitters & Resize Handles */
QSplitter::handle {{
    background-color: {t["border"]};
    border-radius: 2px;
}}

QSplitter::handle:horizontal {{
    width: 6px;
}}

QSplitter::handle:vertical {{
    height: 6px;
}}

QSplitter::handle:hover {{
    background-color: {t["primary"]};
}}

QSplitter::handle:pressed {{
    background-color: {t["primary_hover"]};
}}

/* Scrollbars */
QScrollBar:vertical {{
    background: transparent;
    width: 8px;
    margin: 0px;
}}

QScrollBar::handle:vertical {{
    background: {t["border"]};
    border-radius: 4px;
    min-height: 20px;
}}

QScrollBar::handle:vertical:hover {{
    background: {t["primary"]};
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0px;
}}

QScrollBar:horizontal {{
    background: transparent;
    height: 8px;
    margin: 0px;
}}

QScrollBar::handle:horizontal {{
    background: {t["border"]};
    border-radius: 4px;
    min-width: 20px;
}}

QScrollBar::handle:horizontal:hover {{
    background: {t["primary"]};
}}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    width: 0px;
}}

/* Toast Notifications (Hatsune Miku Magenta Accent) */
QLabel.toast-label {{
    background-color: {t["secondary"]};
    color: #FFFFFF;
    font-weight: bold;
    font-size: 12px;
    padding: 8px 16px;
    border-radius: 16px;
}}
"""


# Default backward compatible QSS
ANDROID_STYLE_QSS = get_theme_qss("dark")
