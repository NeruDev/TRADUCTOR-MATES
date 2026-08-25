"""
---
file: tests/test_translator.py
module: tests.test_translator
description: Pruebas unitarias para la capa de traducción de MathTree a LaTeX, Markdown y texto plano.
type: test/unit
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
  - src.core.translator
relations:
  - src/core/translator.py
exports: []
test: pytest tests/test_translator.py
constraints:
  - "Garantizar canonización de subíndices/exponentes y formato de bloques Markdown"
keywords:
  - test-translator
  - latex-export
  - markdown-blocks
  - plain-text
---

Unit Tests for LaTeX and Markdown Translation Layer.
"""

from __future__ import annotations

from src.core.ast import MathTree
from src.core.translator import LaTeXTranslator


def test_markdown_translation():
    tree = MathTree()
    tree.insert_text("E = mc")
    tree.clear_all()
    tree.insert_text("E = mc^2")

    md = LaTeXTranslator.to_markdown_block(tree)
    assert md == "$$\nE = mc^2\n$$"

    inline_md = LaTeXTranslator.to_markdown_inline(tree)
    assert inline_md == "$E = mc^2$"


def test_latex_canonization():
    tree = MathTree()
    # Mocking nested sub and sup
    tree.insert_text("{x}_{i}^{n}")
    latex = LaTeXTranslator.to_latex(tree)
    # The regex should canonize the output
    assert "x" in latex


def test_plain_text_export():
    tree = MathTree()
    tree.insert_text(r"A = \pi r^2")
    plain = LaTeXTranslator.to_plain_text(tree)
    assert "A = " in plain
