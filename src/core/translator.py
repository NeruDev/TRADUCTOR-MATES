"""
---
file: src/core/translator.py
module: src.core.translator
description: Capa de traducción de objetos MathTree a LaTeX, bloques Markdown y texto plano.
type: core/translator
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
relations:
  - docs/ARCHITECTURE.md
  - src/core/ast.py
  - src/ui/components/code_panel.py
exports:
  - LaTeXTranslator: "Clase estática para conversión de MathTree a formatos LaTeX, Markdown y texto plano"
test: pytest tests/test_translator.py
constraints:
  - "Garantizar la canonización de potencias y subíndices en un solo nivel sintáctico"
  - "Mantener la idempotencia en las transformaciones MathTree -> LaTeX"
keywords:
  - translator
  - math-tree-to-latex
  - markdown-blocks
  - latex-canonization
  - plain-text
---

LaTeX, Markdown, and Text Translation Layer
Converts MathTree instances into raw LaTeX, Markdown blocks, and readable plain text.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from src.core.ast import MathTree


# 3. Configuración Operativa de Traducción
@dataclass(frozen=True)
class TranslatorConfig:
    """Parámetros de configuración del motor de traducción textual.

    Attributes:
        markdown_block_delimiter: Delimitador estándar para bloques de ecuación Markdown.
        markdown_inline_delimiter: Delimitador estándar para ecuaciones en línea.
    """

    markdown_block_delimiter: str = "$$"
    markdown_inline_delimiter: str = "$"


TRANSLATOR_CONFIG = TranslatorConfig()


class LaTeXTranslator:
    """Clase estática para conversión de objetos MathTree a formatos de texto."""

    @staticmethod
    def to_latex(tree: MathTree) -> str:
        """Exporta el árbol a código LaTeX crudo con canonización.

        Args:
            tree: Instancia de `MathTree` que representa la fórmula actual.

        Returns:
            El código LaTeX resultante.
        """
        latex = tree.to_latex()

        # Canonización de Potencias y Subíndices:
        # Se asegura que patrones como {base}_{sub}^{power} se generen en un solo nivel
        # Esta canonización limpia anidamientos inválidos de subíndices y exponentes
        def repl_subsup(m):
            base = m.group(1)
            sub = m.group(2)
            sup = m.group(3)
            return f"{base}_{{{sub}}}^{{{sup}}}"

        latex = re.sub(r"\{([^{}]+)\}_\{([^{}]+)\}\^\{([^{}]+)\}", repl_subsup, latex)

        return latex.strip()

    @staticmethod
    def to_markdown_block(tree: MathTree) -> str:
        """Genera un bloque de fórmula en Markdown.

        Args:
            tree: Instancia de `MathTree` a convertir.

        Returns:
            La ecuación encapsulada en bloque Markdown `$$ ... $$`.
        """
        latex = tree.to_latex()
        if not latex:
            latex = "% Ecuación vacía"
        return f"$$\n{latex}\n$$"

    @staticmethod
    def to_markdown_inline(tree: MathTree) -> str:
        """Genera una fórmula en línea para Markdown.

        Args:
            tree: Instancia de `MathTree` a convertir.

        Returns:
            La ecuación encapsulada en línea `$ ... $`.
        """
        latex = tree.to_latex()
        return f"${latex}$"

    @staticmethod
    def to_markdown_code_snippet(tree: MathTree) -> str:
        """Genera un bloque de código sintáctico Markdown.

        Args:
            tree: Instancia de `MathTree` a convertir.

        Returns:
            Bloque de código con la directiva de lenguaje `latex`.
        """
        latex = tree.to_latex()
        return f"```latex\n{latex}\n```"

    @staticmethod
    def to_plain_text(tree: MathTree) -> str:
        """Genera la representación en texto plano.

        Args:
            tree: Instancia de `MathTree` a convertir.

        Returns:
            El texto de visualización legible (Display Text).
        """
        return tree.to_display_text()
