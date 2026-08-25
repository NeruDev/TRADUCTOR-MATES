r"""
---
file: src/core/syntax.py
module: src.core.syntax
description: Motor de análisis de sintaxis y resaltado semántico basado en la paleta de Hatsune Miku.
type: core/syntax
version: 1.0.0
date: 2026-08-24
dependencies: []
relations:
  - docs/ARCHITECTURE.md
  - src/ui/theme.py
  - src/ui/components/code_panel.py
exports:
  - get_token_color: "Devuelve el color hexadecimal según la categoría matemática del token y el tema"
  - format_highlighted_html: "Formatea texto plano a HTML con etiquetas span coloreadas adaptadas al tema"
  - LaTeXSyntaxHighlighter: "Resaltador PySide6 (QSyntaxHighlighter) con reglas adaptables al modo oscuro y claro"
test: pytest tests/test_syntax.py
constraints:
  - "Mantener la coherencia semántica cromática en ambos modos (Dark Studio y Light Canvas)"
  - "Utilizar negative lookbehind para evitar colorear caracteres dentro de comandos de control LaTeX"
keywords:
  - syntax-highlighter
  - token-colors
  - miku-theme
  - qsyntaxhighlighter
  - regex-rules
---

Syntax Analysis & Highlighting Engine for Mathematical Expressions and LaTeX
Implements the Hatsune Miku Harmonic Semantic Syntax Color Scheme:
- Variables / Unknowns ($x, y, z, \alpha, \theta$): Coral Pink (#FF7597) / Deep Magenta (#C2185B)
- Numbers / Constants ($0-9, \pi, e, \infty$): Soft Mint (#70D6A3) / Forest Mint (#0D8A72)
- Operators and Signs ($+, -, =, \pm, \times, \div$): Bright Miku Cyan (#56D8CD) / Ocean Cyan (#00838F)
- LaTeX Commands and Functions (`\\frac`, `\\sqrt`, $\\sin$, $\\lim$): Electric Lavender (#C084FC) / Imperial Purple (#6D28D9)
- Delimiters / Structure ($(), [], {}, |, /$, radicals): Steel Slate (#828DA4) / Neutral Slate (#475569)
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass
from typing import Any

from PySide6.QtGui import QColor, QFont, QSyntaxHighlighter, QTextCharFormat


# 3. Configuración Operativa de Sintaxis
@dataclass(frozen=True)
class SyntaxConfig:
    """Parámetros de configuración del motor léxico y analizador de sintaxis.

    Attributes:
        default_theme: Tema predeterminado ('dark' o 'light').
        enable_rainbow_brackets: Habilita el coloreado recursivo por niveles de delimitadores.
    """

    default_theme: str = "dark"
    enable_rainbow_brackets: bool = True


SYNTAX_CONFIG = SyntaxConfig()

# Hatsune Miku Semantic Color Palettes for Math Syntax Highlighting
SYNTAX_COLORS = {
    "dark": {
        "var": "#61AFEF",  # Azul (Variables - Estilo One Dark)
        "num": "#FF9EBB",  # Oro/Amarillo (Números)
        "op": "#C678DD",  # Rojo/Rosa (Operadores)
        "cmd": "#56B6C2",  # Púrpura (Comandos LaTeX)
        "delim": "#ABB2BF",  # Gris Base
        "default": "#ABB2BF",  # Gris Base
        "rainbow_1": "#98C379",  # Naranja
        "rainbow_2": "#4169E1",  # Azul Rey
        "rainbow_3": "#E5C07B",  # Verde Lima
        "rainbow_4": "#E3327B",  # Magenta Miku
    },
    "light": {
        "var": "#005CC5",  # Azul oscuro
        "num": "#D81B60",  # Oro oscuro
        "op": "#6F42C1",  # Rojo oscuro
        "cmd": "#00838F",  # Púrpura oscuro
        "delim": "#24292E",
        "default": "#24292E",
        "rainbow_1": "#50A14F",  # Naranja oscuro
        "rainbow_2": "#0033CC",  # Azul Rey oscuro
        "rainbow_3": "#B8860B",  # Verde oscuro
        "rainbow_4": "#C2185B",  # Magenta oscuro
    },
}

# Backward Compatible Constants (Defaulting to Dark Studio)
COLOR_NUMBER = SYNTAX_COLORS["dark"]["num"]
COLOR_OPERATOR = SYNTAX_COLORS["dark"]["op"]
COLOR_VARIABLE = SYNTAX_COLORS["dark"]["var"]
COLOR_DELIMITER = SYNTAX_COLORS["dark"]["delim"]
COLOR_LATEX_CMD = SYNTAX_COLORS["dark"]["cmd"]
COLOR_DEFAULT = SYNTAX_COLORS["dark"]["default"]

# Categorized Symbol Sets
VARIABLE_NAMES = {
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "X",
    "Y",
    "Z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "α",
    "β",
    "γ",
    "δ",
    "θ",
    "λ",
    "μ",
    "σ",
    "ω",
    "Δ",
    "Ω",
    "phi",
    "psi",
    "theta",
    "alpha",
    "beta",
    "gamma",
}

CONSTANT_NAMES = {"π", "pi", "e", "∞", "infty"}

OPERATOR_SYMBOLS = {
    "+",
    "-",
    "=",
    "*",
    "/",
    "±",
    "×",
    "÷",
    "≤",
    "≥",
    "≠",
    "≈",
    "≡",
    "∫",
    "∑",
    "∏",
    "∐",
    "√",
    "∂",
    "→",
    "←",
    "↔",
    "⇒",
    "⇔",
    "∣",
    "∤",
    "∠",
    "⟂",
    "∥",
    "d",
    "·",
    "∝",
    "†",
}

MATH_FUNCTIONS = {
    "sin",
    "cos",
    "tan",
    "cot",
    "sec",
    "csc",
    "sinh",
    "cosh",
    "tanh",
    "coth",
    "sech",
    "csch",
    "arcsin",
    "arccos",
    "arctan",
    "lim",
    "log",
    "ln",
    "det",
    "max",
    "min",
    "exp",
    "mcd",
    "mcm",
    "Adj",
    "gcd",
    "deg",
    "dim",
    "ker",
    "hom",
    "inf",
    "sup",
    "mod",
    "pmod",
}


def get_token_color(token: str, theme: str = "dark") -> str:
    """Obtiene el color hexadecimal de un token según su rol sintáctico y el tema activo.

    Categorías sintácticas (Esquema Hatsune Miku):
    - Variables / Incógnitas -> Rosa Coral / Magenta (#FF7597 en dark, #C2185B en light)
    - Números / Constantes -> Verde Menta / Bosque (#70D6A3 en dark, #0D8A72 en light)
    - Operadores y Signos -> Cian Miku (#56D8CD en dark, #00838F en light)
    - Comandos / Funciones -> Lavanda / Púrpura (#C084FC en dark, #6D28D9 en light)
    - Delimitadores / Estructura -> Gris Acero / Pizarra (#828DA4 en dark, #475569 en light)

    Args:
        token: La cadena de texto (símbolo, comando, número o variable) a evaluar.
        theme: Identificador del tema ('dark' o 'light').

    Returns:
        El color hexadecimal asociado al rol sintáctico del token.
    """
    pal = SYNTAX_COLORS.get(theme, SYNTAX_COLORS["dark"])
    token_str = token.strip()
    if not token_str:
        return pal["default"]

    # 1. Comandos LaTeX y funciones matemáticas -> Lavanda / Púrpura
    if token_str.startswith("\\") or token_str in MATH_FUNCTIONS:
        return pal["cmd"]

    # 2. Números y Constantes matemáticas -> Verde Menta
    if re.match(r"^\d+(\.\d+)?$", token_str) or token_str in CONSTANT_NAMES:
        return pal["num"]

    # 3. Operadores aritméticos y relacionales -> Cian Miku
    if token_str in OPERATOR_SYMBOLS:
        return pal["op"]

    # 4. Delimitadores y estructura -> Gris Acero / Pizarra
    if token_str in "()[]{}|/^_":
        return pal["delim"]

    # 5. Variables e incógnitas -> Rosa Coral / Magenta
    if token_str in VARIABLE_NAMES:
        return pal["var"]

    # Fallback para caracteres individuales
    if len(token_str) == 1:
        if token_str.isdigit():
            return pal["num"]
        if token_str.isalpha():
            return pal["var"]

    return pal["default"]


def format_highlighted_html(text: str, theme: str = "dark") -> str:
    """Convierte texto matemático plano a etiquetas HTML `span` con colores de sintaxis y rainbow delimiters.

    Args:
        text: Expresión matemática en texto plano a colorear.
        theme: Identificador del tema visual ('dark' o 'light').

    Returns:
        Cadena HTML con estilos en línea (`<span style="...">...</span>`).
    """
    if not text:
        return ""

    tokens = re.findall(r"\d+(?:\.\d+)?|\\[a-zA-Z]+|[a-zA-Z]|[^\s\w]", text)
    if not tokens:
        tokens = [text]

    spans = []
    pal = SYNTAX_COLORS.get(theme, SYNTAX_COLORS["dark"])

    depth = 0
    openers = {"(", "[", "{"}
    closers = {")", "]", "}"}

    for t in tokens:
        if t in openers:
            color = pal.get(f"rainbow_{(depth % 4) + 1}", pal["delim"])
            depth += 1
        elif t in closers:
            depth = max(0, depth - 1)
            color = pal.get(f"rainbow_{(depth % 4) + 1}", pal["delim"])
        else:
            color = get_token_color(t, theme)

        escaped = html.escape(t)
        font_style = (
            "font-style: italic;"
            if (t in VARIABLE_NAMES and len(t) == 1 and t.isalpha())
            else ""
        )
        spans.append(
            f'<span style="color: {color}; font-weight: bold; {font_style}">{escaped}</span>'
        )

    return "".join(spans)


class LaTeXSyntaxHighlighter(QSyntaxHighlighter):
    """Resaltador de sintaxis para componentes basados en QTextDocument.

    Extiende Qt para aplicar colores y jerarquías visuales mediante
    expresiones regulares y el uso de `QTextCharFormat` bajo el esquema Hatsune Miku.

    Args:
        parent: Objeto padre de Qt (ej. QTextDocument o QTextEdit).
        theme: Nombre del tema activo ('dark' o 'light').
    """

    def __init__(self, parent: Any = None, theme: str = "dark") -> None:
        super().__init__(parent)
        self.theme = theme
        self._rules: list[tuple[re.Pattern[str], QTextCharFormat]] = []
        self._setup_rules()

    def set_theme(self, theme: str) -> None:
        """Actualiza dinámicamente el tema de colores y re-evalúa el documento.

        Args:
            theme: Nombre del nuevo tema ('dark' o 'light').
        """
        self.theme = theme
        self._setup_rules()
        self.rehighlight()

    def _setup_rules(self) -> None:
        """Configura los formatos y expresiones regulares según el tema activo."""
        pal = SYNTAX_COLORS.get(self.theme, SYNTAX_COLORS["dark"])
        self._rules = []

        # 1. Comandos LaTeX (\frac, \sqrt, \int, \sin, etc.) -> Lavanda / Púrpura
        cmd_fmt = QTextCharFormat()
        cmd_fmt.setForeground(QColor(pal["cmd"]))
        cmd_fmt.setFontWeight(QFont.Bold)
        self._rules.append((re.compile(r"\\[a-zA-Z]+"), cmd_fmt))

        # 2. Operadores Aritméticos y Relacionales -> Cian Miku
        op_fmt = QTextCharFormat()
        op_fmt.setForeground(QColor(pal["op"]))
        op_fmt.setFontWeight(QFont.Bold)
        self._rules.append(
            (re.compile(r"[+\-=/=\*\^_\:\;<>\&∫∑∏∐√∂→←↔⇒⇔∣∤∠⟂∥±×÷≤≥≠≈≡·]"), op_fmt)
        )

        # 3. Números y Constantes numéricas -> Verde Menta
        num_fmt = QTextCharFormat()
        num_fmt.setForeground(QColor(pal["num"]))
        num_fmt.setFontWeight(QFont.Bold)
        self._rules.append((re.compile(r"\b\d+(\.\d+)?\b"), num_fmt))

        # 4. Variables individuales (que no forman parte de un comando \cmd) -> Rosa Coral / Magenta
        var_fmt = QTextCharFormat()
        var_fmt.setForeground(QColor(pal["var"]))
        var_fmt.setFontItalic(True)
        var_fmt.setFontWeight(QFont.Bold)
        self._rules.append((re.compile(r"(?<!\\)\b[a-zA-Z]\b"), var_fmt))

        # 5. Delimitadores y Estructura ({}, (), [], |) -> Gris Acero / Pizarra
        delim_fmt = QTextCharFormat()
        delim_fmt.setForeground(QColor(pal["delim"]))
        self._rules.append((re.compile(r"[\{\}\(\)\[\]\|]"), delim_fmt))

    def highlightBlock(self, text: str) -> None:
        """Aplica los formatos visuales definidos al bloque de texto en curso, con soporte Rainbow Delimiters.

        Args:
            text: Cadena de texto del párrafo o bloque actual a formatear.
        """
        for pattern, fmt in self._rules:
            for match in pattern.finditer(text):
                start, end = match.span()
                self.setFormat(start, end - start, fmt)

        pal = SYNTAX_COLORS.get(self.theme, SYNTAX_COLORS["dark"])
        depth = max(0, self.previousBlockState())

        openers = {"(", "[", "{"}
        closers = {")", "]", "}"}

        for i, char in enumerate(text):
            if char in openers:
                fmt = QTextCharFormat()
                fmt.setForeground(
                    QColor(pal.get(f"rainbow_{(depth % 4) + 1}", pal["delim"]))
                )
                fmt.setFontWeight(QFont.Bold)
                self.setFormat(i, 1, fmt)
                depth += 1
            elif char in closers:
                depth = max(0, depth - 1)
                fmt = QTextCharFormat()
                fmt.setForeground(
                    QColor(pal.get(f"rainbow_{(depth % 4) + 1}", pal["delim"]))
                )
                fmt.setFontWeight(QFont.Bold)
                self.setFormat(i, 1, fmt)

        self.setCurrentBlockState(depth)
