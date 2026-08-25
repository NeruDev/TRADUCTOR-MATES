"""
---
file: tests/test_syntax.py
module: tests.test_syntax
description: Pruebas unitarias para el motor de resaltado de sintaxis y clasificador léxico Hatsune Miku.
type: test/unit
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.syntax
relations:
  - src/core/syntax.py
exports: []
test: pytest tests/test_syntax.py
constraints:
  - "Validar correspondencia exacta de colores temáticos para variables, números, operadores y comandos"
keywords:
  - test-syntax
  - syntax-highlighter
  - miku-palette
  - token-classifier
---

Unit tests for Hatsune Miku Math Semantic Syntax Highlighting & Token Classifier Module.
"""

from __future__ import annotations

from src.core.syntax import (
    SYNTAX_COLORS,
    format_highlighted_html,
    get_token_color,
)


def test_miku_token_color_classification():
    # 1. Dark Mode Tests
    # Variables (Coral Pink #FF7597)
    assert get_token_color("x", "dark") == SYNTAX_COLORS["dark"]["var"]
    assert get_token_color("y", "dark") == SYNTAX_COLORS["dark"]["var"]
    assert get_token_color("theta", "dark") == SYNTAX_COLORS["dark"]["var"]

    # Numbers & Constants (Soft Mint #70D6A3)
    assert get_token_color("2", "dark") == SYNTAX_COLORS["dark"]["num"]
    assert get_token_color("3.14", "dark") == SYNTAX_COLORS["dark"]["num"]
    assert get_token_color("π", "dark") == SYNTAX_COLORS["dark"]["num"]
    assert get_token_color("∞", "dark") == SYNTAX_COLORS["dark"]["num"]

    # Operators (Bright Cyan #56D8CD)
    assert get_token_color("+", "dark") == SYNTAX_COLORS["dark"]["op"]
    assert get_token_color("-", "dark") == SYNTAX_COLORS["dark"]["op"]
    assert get_token_color("=", "dark") == SYNTAX_COLORS["dark"]["op"]
    assert get_token_color("±", "dark") == SYNTAX_COLORS["dark"]["op"]

    # Commands / Functions (Lavender #C084FC)
    assert get_token_color(r"\frac", "dark") == SYNTAX_COLORS["dark"]["cmd"]
    assert get_token_color(r"\sqrt", "dark") == SYNTAX_COLORS["dark"]["cmd"]
    assert get_token_color("lim", "dark") == SYNTAX_COLORS["dark"]["cmd"]

    # Delimiters (Steel Slate #828DA4)
    assert get_token_color("(", "dark") == SYNTAX_COLORS["dark"]["delim"]
    assert get_token_color(")", "dark") == SYNTAX_COLORS["dark"]["delim"]
    assert get_token_color("[", "dark") == SYNTAX_COLORS["dark"]["delim"]
    assert get_token_color("]", "dark") == SYNTAX_COLORS["dark"]["delim"]

    # 2. Light Mode Tests
    assert get_token_color("x", "light") == SYNTAX_COLORS["light"]["var"]
    assert get_token_color("2", "light") == SYNTAX_COLORS["light"]["num"]
    assert get_token_color("+", "light") == SYNTAX_COLORS["light"]["op"]
    assert get_token_color(r"\sqrt", "light") == SYNTAX_COLORS["light"]["cmd"]
    assert get_token_color("(", "light") == SYNTAX_COLORS["light"]["delim"]


def test_format_highlighted_html_miku_colors():
    html_dark = format_highlighted_html("-x2 = 0", theme="dark")
    assert SYNTAX_COLORS["dark"]["op"] in html_dark
    assert SYNTAX_COLORS["dark"]["var"] in html_dark
    assert SYNTAX_COLORS["dark"]["num"] in html_dark

    html_light = format_highlighted_html("-x2 = 0", theme="light")
    assert SYNTAX_COLORS["light"]["op"] in html_light
    assert SYNTAX_COLORS["light"]["var"] in html_light
    assert SYNTAX_COLORS["light"]["num"] in html_light
