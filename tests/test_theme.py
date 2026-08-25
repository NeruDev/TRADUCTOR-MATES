"""
---
file: tests/test_theme.py
module: tests.test_theme
description: Pruebas unitarias para el generador de temas y hojas de estilo QSS Hatsune Miku.
type: test/unit
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.ui.theme
relations:
  - src/ui/theme.py
exports: []
test: pytest tests/test_theme.py
constraints:
  - "Validar tokens de diseño y generación de reglas QSS válidas para modo oscuro y claro"
keywords:
  - test-theme
  - qss-generator
  - dark-mode
  - light-mode
---

Unit tests for Hatsune Miku Theme Generator & Switching.
"""

from __future__ import annotations

from src.ui.theme import (
    COLOR_MIKU_CYAN,
    COLOR_MIKU_MAGENTA,
    get_theme_dict,
    get_theme_qss,
)


def test_miku_theme_palettes():
    dark = get_theme_dict("dark")
    light = get_theme_dict("light")

    assert dark["primary"] == COLOR_MIKU_CYAN
    assert dark["secondary"] == COLOR_MIKU_MAGENTA
    assert dark["bg"] == "#0F1017"
    assert dark["bg_canvas_editor"] == "#13141C"
    assert dark["bg_canvas_render"] == "#13141C"
    assert dark["text_rendered_math"] == "#F8FAFC"
    assert dark["math_var_color"] == "#61AFEF"
    assert dark["math_num_color"] == "#E5C07B"
    assert dark["math_op_color"] == "#C678DD"
    assert dark["math_cmd_color"] == "#56B6C2"
    assert dark["math_delim_color"] == "#ABB2BF"

    assert light["primary"] == COLOR_MIKU_CYAN
    assert light["secondary"] == COLOR_MIKU_MAGENTA
    assert light["bg"] == "#F1F5F9"
    assert light["bg_canvas_editor"] == "#FFFFFF"
    assert light["bg_canvas_render"] == "#F8FAFC"
    assert light["text_rendered_math"] == "#0F172A"
    assert light["math_var_color"] == "#005CC5"
    assert light["math_num_color"] == "#B8860B"
    assert light["math_op_color"] == "#6F42C1"
    assert light["math_cmd_color"] == "#00838F"
    assert light["math_delim_color"] == "#24292E"


def test_theme_qss_generation():
    dark_qss = get_theme_qss("dark")
    light_qss = get_theme_qss("light")

    assert "#0F1017" in dark_qss
    assert "#F1F5F9" in light_qss
    assert COLOR_MIKU_CYAN in dark_qss
    assert COLOR_MIKU_CYAN in light_qss
