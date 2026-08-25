"""
---
file: src/core/parser.py
module: src.core.parser
description: Parser inverso de código LaTeX a sintaxis del árbol AST (LaTeXParser).
type: core/parser
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
  - src.core.logger
  - src.data.symbols
relations:
  - docs/ARCHITECTURE.md
  - src/core/ast.py
  - src/ui/main_window.py
exports:
  - LaTeXParser: "Clase con métodos estáticos para parsear cadenas LaTeX a un árbol MathTree"
  - _LaTeXStreamParser: "Tokenizador y analizador sintáctico descendente basado en flujos de caracteres"
test: pytest tests/test_parser.py
constraints:
  - "Garantizar la preservación de casillas editables para comandos incompletos o vacíos"
  - "Evitar que tokens atómicos no delimitados devoren ávidamente exponentes subsecuentes"
keywords:
  - latex-parser
  - inverse-parser
  - recursive-descent
  - stream-tokenizer
  - ast-reconstruction
---
"""

from __future__ import annotations

import re

from src.core.ast import (
    BinomialNode,
    BracketNode,
    ContourIntegralNode,
    DefiniteIntegralNode,
    DerivativeNode,
    DoubleIntegralNode,
    FractionNode,
    IndefiniteIntegralNode,
    LimitNode,
    MathNode,
    MathTree,
    MatrixNode,
    ModularNode,
    NthRootNode,
    OperatorNode,
    PowerNode,
    ProductNode,
    Slot,
    SquareRootNode,
    StyleDecoratorNode,
    SubscriptNode,
    SubSupNode,
    SummationNode,
    SymbolNode,
    TextNode,
    TripleIntegralNode,
)
from src.core.logger import get_logger
from src.data.symbols import LATEX_TO_UNICODE

logger = get_logger()

OPERATOR_CMDS = {
    "\\sin",
    "\\cos",
    "\\tan",
    "\\csc",
    "\\sec",
    "\\cot",
    "\\sinh",
    "\\cosh",
    "\\tanh",
    "\\coth",
    "\\sech",
    "\\csch",
    "\\arcsin",
    "\\arccos",
    "\\arctan",
    "\\ln",
    "\\log",
    "\\exp",
    "\\det",
    "\\lim",
    "\\max",
    "\\min",
    "\\arg",
    "\\deg",
    "\\gcd",
    "\\dim",
    "\\ker",
    "\\hom",
    "\\inf",
    "\\sup",
}

STYLE_CMDS = sorted(
    [
        "mathbf",
        "mathrm",
        "mathit",
        "mathsf",
        "mathtt",
        "mathcal",
        "mathbb",
        "mathfrak",
        "textbf",
        "textit",
        "textrm",
        "textsf",
        "texttt",
        "text",
        "vec",
        "hat",
        "bar",
        "tilde",
        "ddot",
        "dot",
    ],
    key=len,
    reverse=True,
)
STYLE_PATTERN = r"\\(" + "|".join(STYLE_CMDS) + r")(?![a-zA-Z])"


class _LaTeXStreamParser:
    """Procesador interno de tokens (Lexer/Parser recursivo) de flujo único.

    Args:
        latex: Cadena de código fuente en formato LaTeX a procesar.
    """

    def __init__(self, latex: str) -> None:
        self.latex = latex
        self.length = len(latex)
        self.idx = 0

    def eof(self) -> bool:
        """Comprueba si el puntero de lectura ha llegado al final de la cadena.

        Returns:
            True si se alcanzó el fin del texto; False en caso contrario.
        """
        return self.idx >= self.length

    def peek(self) -> str:
        """Examina el siguiente carácter del flujo sin avanzar el puntero de lectura.

        Returns:
            El carácter actual bajo el cursor o una cadena vacía si eof() es True.
        """
        if self.eof():
            return ""
        return self.latex[self.idx]

    def skip_whitespace(self) -> None:
        """Avanza el puntero de lectura ignorando espacios en blanco y espaciadores TeX.

        Ignora espacios estándar (' ', '\t', '\n', '\r') y comandos de espaciado TeX
        como '\\,', '\\;', '\\!', '\\quad' y '\\qquad'.
        """
        while not self.eof():
            ch = self.latex[self.idx]
            if ch in " \t\n\r":
                self.idx += 1
            elif (
                self.latex[self.idx :].startswith(r"\,")
                or self.latex[self.idx :].startswith(r"\;")
                or self.latex[self.idx :].startswith(r"\!")
            ):
                self.idx += 2
            elif self.latex[self.idx :].startswith(r"\quad"):
                self.idx += 5
            elif self.latex[self.idx :].startswith(r"\qquad"):
                self.idx += 6
            else:
                break

    def parse_slot(self, stop_tokens: set[str] | None = None) -> Slot:
        """Parsea nodos y los agrupa en un `Slot` hasta el final o una parada.

        Args:
            stop_tokens: Conjunto de tokens que detienen el análisis (e.g. '\\right]').

        Returns:
            Una instancia de `Slot` con todos los nodos parseados adjuntos.
        """
        slot = Slot()
        while not self.eof():
            self.skip_whitespace()
            if self.eof():
                break

            ch = self.peek()
            if stop_tokens and any(
                self.latex[self.idx :].startswith(st) for st in stop_tokens
            ):
                break

            if ch == "}":
                break

            node = self.parse_next_node()
            if node is not None:
                node = self.check_sub_sup(node)
                slot.add_node(node)

        return slot

    def parse_arg_slot(self) -> Slot:
        """Parsea un argumento individual como un `Slot`.

        Se encarga de procesar bloques entre llaves `{...}` o, en su defecto,
        un solo token inmediato (e.g. en `x^2`, procesa el `2`).

        Returns:
            Una instancia de `Slot` con el argumento procesado.
        """
        self.skip_whitespace()
        if self.eof():
            return Slot()

        if self.peek() == "{":
            self.idx += 1  # consume '{'
            slot = self.parse_slot()
            if not self.eof() and self.peek() == "}":
                self.idx += 1  # consume '}'
            return slot
        else:
            node = self.parse_next_node()
            slot = Slot()
            if node is not None:
                slot.add_node(node)
            return slot

    def check_sub_sup(self, base_node: MathNode) -> MathNode:
        """Busca y adjunta subíndices (`_`) y superíndices (`^`) a un nodo base.

        Args:
            base_node: El nodo matemático central.

        Returns:
            El nodo original, o un nodo envolvente (`PowerNode`, `SubscriptNode`,
            `SubSupNode`) conteniendo la base y sus índices.
        """
        sub_slot = None
        sup_slot = None

        while not self.eof():
            self.skip_whitespace()
            if self.eof():
                break
            ch = self.peek()
            if ch == "_" and sub_slot is None:
                self.idx += 1
                sub_slot = self.parse_arg_slot()
            elif ch == "^" and sup_slot is None:
                self.idx += 1
                sup_slot = self.parse_arg_slot()
            else:
                break

        if sub_slot and sup_slot:
            subsup = SubSupNode()
            base_slot = Slot()
            base_slot.add_node(base_node)
            subsup.slots["base"] = base_slot
            subsup.slots["sub"] = sub_slot
            subsup.slots["sup"] = sup_slot
            return subsup
        elif sup_slot:
            pow_node = PowerNode()
            base_slot = Slot()
            base_slot.add_node(base_node)
            pow_node.slots["base"] = base_slot
            pow_node.slots["exp"] = sup_slot
            return pow_node
        elif sub_slot:
            sub_node = SubscriptNode()
            base_slot = Slot()
            base_slot.add_node(base_node)
            sub_node.slots["base"] = base_slot
            sub_node.slots["sub"] = sub_slot
            return sub_node

        return base_node

    def parse_next_node(self) -> MathNode | None:
        """Analiza y construye el siguiente nodo matemático del flujo de entrada.

        Identifica recursivamente grupos `{...}`, operadores `^`/`_`, comandos LaTeX,
        entornos matriciales, delimitadores `\\left`/`\\right`, operadores estilísticos
        y caracteres literales.

        Returns:
            Instancia de `MathNode` correspondiente o None si se alcanzó el fin del flujo.
        """
        self.skip_whitespace()
        if self.eof():
            return None

        ch = self.peek()

        # 1. Group in braces: { ... }
        if ch == "{":
            self.idx += 1
            slot = self.parse_slot()
            if not self.eof() and self.peek() == "}":
                self.idx += 1
            if len(slot.nodes) == 1:
                return slot.nodes[0]
            elif len(slot.nodes) == 0:
                return TextNode("")
            else:
                if all(isinstance(n, TextNode) for n in slot.nodes):
                    combined_text = "".join(getattr(n, "text", "") for n in slot.nodes)
                    return TextNode(combined_text)
                else:
                    bracket = BracketNode("{", "}")
                    bracket.slots["body"] = slot
                    return bracket

        # 2. Standalone ^ or _ (no preceding node)
        if ch in ("^", "_"):
            dummy_base = TextNode("")
            return self.check_sub_sup(dummy_base)

        # 3. LaTeX commands starting with \
        if ch == "\\":
            rest = self.latex[self.idx :]

            # Check \frac
            if rest.startswith(r"\frac"):
                self.idx += 5
                num_slot = self.parse_arg_slot()
                den_slot = self.parse_arg_slot()

                num_tex = num_slot.to_latex().strip()
                den_tex = den_slot.to_latex().strip()
                if num_tex.startswith(("d", r"\partial")) and den_tex.startswith(
                    ("d", r"\partial")
                ):
                    is_p = num_tex.startswith(r"\partial") or den_tex.startswith(
                        r"\partial"
                    )
                    deriv = DerivativeNode(is_partial=is_p)
                    f_str = re.sub(r"^(d|\\partial)\s*", "", num_tex).strip()
                    v_str = re.sub(r"^(d|\\partial)\s*", "", den_tex).strip()
                    f_slot = Slot()
                    f_slot.insert_text(f_str)
                    v_slot = Slot()
                    v_slot.insert_text(v_str)
                    deriv.slots["func"] = f_slot
                    deriv.slots["var"] = v_slot
                    return deriv

                frac = FractionNode()
                frac.slots["num"] = num_slot
                frac.slots["den"] = den_slot
                return frac

            # Check \binom
            if rest.startswith(r"\binom"):
                self.idx += 6
                n_slot = self.parse_arg_slot()
                k_slot = self.parse_arg_slot()
                binom = BinomialNode()
                binom.slots["n"] = n_slot
                binom.slots["k"] = k_slot
                return binom

            # Check \sqrt
            if rest.startswith(r"\sqrt"):
                self.idx += 5
                self.skip_whitespace()
                if not self.eof() and self.peek() == "[":
                    self.idx += 1
                    index_slot = self.parse_slot(stop_tokens={"]"})
                    if not self.eof() and self.peek() == "]":
                        self.idx += 1
                    rad_slot = self.parse_arg_slot()
                    nth = NthRootNode()
                    nth.slots["index"] = index_slot
                    nth.slots["radicand"] = rad_slot
                    return nth
                else:
                    rad_slot = self.parse_arg_slot()
                    sqrt = SquareRootNode()
                    sqrt.slots["radicand"] = rad_slot
                    return sqrt

            # Check \iiint, \iint, \oint, \int
            int_cmd = None
            if rest.startswith(r"\iiint"):
                int_cmd = r"\iiint"
            elif rest.startswith(r"\iint"):
                int_cmd = r"\iint"
            elif rest.startswith(r"\oint"):
                int_cmd = r"\oint"
            elif rest.startswith(r"\int"):
                int_cmd = r"\int"

            if int_cmd is not None:
                self.idx += len(int_cmd)
                sub_slot = None
                sup_slot = None

                while True:
                    self.skip_whitespace()
                    if self.peek() == "_":
                        self.idx += 1
                        sub_slot = self.parse_arg_slot()
                    elif self.peek() == "^":
                        self.idx += 1
                        sup_slot = self.parse_arg_slot()
                    else:
                        break

                body_slot = Slot()
                var_slot = Slot()

                default_var = (
                    "r"
                    if int_cmd == r"\oint"
                    else (
                        "A"
                        if int_cmd == r"\iint"
                        else ("V" if int_cmd == r"\iiint" else "x")
                    )
                )

                rem = self.latex[self.idx :]
                d_match = re.search(
                    r"(?:\\,|\\\s*)?(?:d|\\partial)\s*\{?([a-zA-Z0-9]+)\}?", rem
                )
                if d_match:
                    d_pos = self.idx + d_match.start()
                    var_name = d_match.group(1)
                    body_text = self.latex[self.idx : d_pos]
                    body_slot = _LaTeXStreamParser(body_text).parse_slot()
                    var_slot.insert_text(var_name)
                    self.idx = d_pos + len(d_match.group(0))
                else:
                    body_slot = self.parse_slot()
                    var_slot.insert_text(default_var)

                if int_cmd == r"\oint":
                    c_node = ContourIntegralNode()
                    c_node.slots["lower"] = sub_slot or Slot()
                    c_node.slots["upper"] = sup_slot or Slot()
                    c_node.slots["body"] = body_slot
                    c_node.slots["var"] = var_slot
                    return c_node
                elif int_cmd == r"\iint":
                    d_node = DoubleIntegralNode()
                    d_node.slots["lower"] = sub_slot or Slot()
                    d_node.slots["upper"] = sup_slot or Slot()
                    d_node.slots["body"] = body_slot
                    d_node.slots["var"] = var_slot
                    return d_node
                elif int_cmd == r"\iiint":
                    t_node = TripleIntegralNode()
                    t_node.slots["lower"] = sub_slot or Slot()
                    t_node.slots["upper"] = sup_slot or Slot()
                    t_node.slots["body"] = body_slot
                    t_node.slots["var"] = var_slot
                    return t_node
                elif sub_slot or sup_slot:
                    def_integ = DefiniteIntegralNode()
                    def_integ.slots["lower"] = sub_slot or Slot()
                    def_integ.slots["upper"] = sup_slot or Slot()
                    def_integ.slots["body"] = body_slot
                    def_integ.slots["var"] = var_slot
                    return def_integ
                else:
                    indef_integ = IndefiniteIntegralNode()
                    indef_integ.slots["body"] = body_slot
                    indef_integ.slots["var"] = var_slot
                    return indef_integ

            # Check \sum
            if rest.startswith(r"\sum"):
                self.idx += 4
                sub_slot = None
                sup_slot = None

                while True:
                    self.skip_whitespace()
                    if self.peek() == "_":
                        self.idx += 1
                        sub_slot = self.parse_arg_slot()
                    elif self.peek() == "^":
                        self.idx += 1
                        sup_slot = self.parse_arg_slot()
                    else:
                        break

                body_slot = (
                    self.parse_arg_slot()
                    if not self.eof() and self.peek() == "{"
                    else self.parse_slot()
                )
                summ = SummationNode()
                summ.slots["lower"] = sub_slot or Slot()
                summ.slots["upper"] = sup_slot or Slot()
                summ.slots["body"] = body_slot
                return summ

            # Check \lim
            if rest.startswith(r"\lim"):
                self.idx += 4
                self.skip_whitespace()
                var_slot = Slot()
                target_slot = Slot()

                if self.peek() == "_":
                    self.idx += 1
                    lim_arg = self.parse_arg_slot()
                    lim_tex = lim_arg.to_latex()
                    parts = re.split(r"\\to|\\rightarrow|->", lim_tex)
                    if len(parts) >= 2:
                        var_slot.insert_text(parts[0].strip())
                        target_slot.insert_text(parts[1].strip())
                    else:
                        var_slot.insert_text(lim_tex.strip())
                        target_slot.insert_text("0")
                else:
                    var_slot.insert_text("x")
                    target_slot.insert_text("0")

                body_slot = self.parse_slot()
                lim_node = LimitNode()
                lim_node.slots["var"] = var_slot
                lim_node.slots["target"] = target_slot
                lim_node.slots["body"] = body_slot
                return lim_node

            # Check \begin{matrix_type}
            if rest.startswith(r"\begin"):
                m_begin = re.match(r"\\begin\{([a-zA-Z]+)\}", rest)
                if m_begin:
                    m_type = m_begin.group(1)
                    end_str = f"\\end{{{m_type}}}"
                    end_pos = rest.find(end_str)
                    if end_pos != -1:
                        mat_body = rest[len(m_begin.group(0)) : end_pos]
                        self.idx += end_pos + len(end_str)

                        row_strs = [
                            r.strip()
                            for r in re.split(r"\\\\|\\cr", mat_body)
                            if r.strip()
                        ]
                        rows = len(row_strs) if row_strs else 1
                        cells_grid = []
                        for r_str in row_strs:
                            c_strs = [c.strip() for c in r_str.split("&")]
                            cells_grid.append(c_strs)

                        cols = max(len(r) for r in cells_grid) if cells_grid else 1
                        mat_node = MatrixNode(rows=rows, cols=cols, matrix_type=m_type)

                        for r_idx in range(rows):
                            for c_idx in range(cols):
                                cell_val = (
                                    cells_grid[r_idx][c_idx]
                                    if c_idx < len(cells_grid[r_idx])
                                    else ""
                                )
                                cell_slot = _LaTeXStreamParser(cell_val).parse_slot()
                                mat_node.slots[f"cell_{r_idx}_{c_idx}"] = cell_slot

                        return mat_node

            # Check \left
            if rest.startswith(r"\left"):
                self.idx += 5
                self.skip_whitespace()
                l_delim = "("
                if not self.eof():
                    if rest.startswith(r"\left\{"):
                        l_delim = "{"
                        self.idx += 2
                    elif rest.startswith(r"\left["):
                        l_delim = "["
                        self.idx += 1
                    elif rest.startswith(r"\left("):
                        l_delim = "("
                        self.idx += 1
                    elif rest.startswith(r"\left|"):
                        l_delim = "|"
                        self.idx += 1
                    else:
                        l_delim = self.peek()
                        self.idx += 1

                body_slot = self.parse_slot(stop_tokens={r"\right"})
                r_delim = ")"
                if self.latex[self.idx :].startswith(r"\right"):
                    self.idx += 6
                    self.skip_whitespace()
                    if not self.eof():
                        if self.latex[self.idx :].startswith(r"\}"):
                            r_delim = "}"
                            self.idx += 2
                        elif self.peek() in ")]|":
                            r_delim = self.peek()
                            self.idx += 1

                bracket_node = BracketNode(left_delim=l_delim, right_delim=r_delim)
                bracket_node.slots["body"] = body_slot
                return bracket_node

            # Check \operatorname
            if rest.startswith(r"\operatorname"):
                self.idx += 13  # len(r"\operatorname")
                self.skip_whitespace()
                op_name = ""
                if not self.eof() and self.peek() == "{":
                    self.idx += 1
                    name_slot = self.parse_slot()
                    if not self.eof() and self.peek() == "}":
                        self.idx += 1
                    op_name = "".join(
                        getattr(n, "text", getattr(n, "display", ""))
                        for n in name_slot.nodes
                    ).strip()
                else:
                    m_op = re.match(r"[a-zA-Z]+", self.latex[self.idx :])
                    if m_op:
                        op_name = m_op.group(0)
                        self.idx += len(op_name)
                return OperatorNode(f"\\operatorname{{{op_name}}}", op_name or "op")

            # Check \pmod
            if rest.startswith(r"\pmod"):
                self.idx += 5
                mod_slot = self.parse_arg_slot()
                mod_node = ModularNode()
                mod_node.slots["mod"] = mod_slot
                return mod_node

            # Check \prod
            if rest.startswith(r"\prod") and not rest.startswith(r"\propto"):
                self.idx += 5
                sub_slot = None
                sup_slot = None

                while True:
                    self.skip_whitespace()
                    if self.peek() == "_":
                        self.idx += 1
                        sub_slot = self.parse_arg_slot()
                    elif self.peek() == "^":
                        self.idx += 1
                        sup_slot = self.parse_arg_slot()
                    else:
                        break

                body_slot = (
                    self.parse_arg_slot()
                    if not self.eof() and self.peek() == "{"
                    else self.parse_slot()
                )
                prod_node = ProductNode()
                prod_node.slots["lower"] = sub_slot or Slot()
                prod_node.slots["upper"] = sup_slot or Slot()
                prod_node.slots["body"] = body_slot
                return prod_node

            # Check Style/Format Macros (Prioritizing by length via STYLE_PATTERN)
            m_style = re.match(STYLE_PATTERN, rest)
            if m_style:
                scmd = m_style.group(1)
                self.idx += len(m_style.group(0))
                arg_slot = self.parse_arg_slot()
                style_node = StyleDecoratorNode(scmd)
                style_node.slots["body"] = arg_slot
                return style_node

            m_cmd = re.match(r"\\[a-zA-Z]+", rest)
            if m_cmd:
                cmd = m_cmd.group(0)
                self.idx += len(cmd)

                if cmd in OPERATOR_CMDS:
                    display = LATEX_TO_UNICODE.get(cmd, cmd.lstrip("\\"))
                    if cmd == "\\sech":
                        return OperatorNode("\\operatorname{sech}", display)
                    if cmd == "\\csch":
                        return OperatorNode("\\operatorname{csch}", display)
                    return OperatorNode(cmd, display)
                elif cmd in LATEX_TO_UNICODE:
                    return SymbolNode(cmd, LATEX_TO_UNICODE[cmd])
                else:
                    return TextNode(cmd)
            else:
                esc_char = rest[1] if len(rest) > 1 else "\\"
                self.idx += 2
                return TextNode(esc_char)

        char = self.peek()
        self.idx += 1
        return TextNode(char)


class LaTeXParser:
    """Contenedor de métodos estáticos para procesar LaTeX y crear un MathTree."""

    @staticmethod
    def parse_to_tree(latex: str) -> MathTree:
        """Convierte una cadena LaTeX en una estructura interactiva de árbol AST.

        Parsea recursivamente la entrada, detectando errores y asegurando la
        consistencia matemática del árbol generado.

        Args:
            latex: La cadena de código fuente en formato LaTeX.

        Returns:
            Una instancia de `MathTree` lista para ser renderizada en la interfaz.

        Raises:
            Exception: Si falla el parser interno al procesar el código LaTeX.
        """
        logger.info(f"Iniciando parseo de LaTeX a AST: {latex}")
        try:
            tree = MathTree()
            tree.root_slot.clear()

            if not latex or not latex.strip():
                tree.active_slot = tree.root_slot
                return tree

            parser = _LaTeXStreamParser(latex)
            parsed_slot = parser.parse_slot()
            tree.root_slot = parsed_slot
            tree.active_slot = tree.root_slot
            tree.save_state()

            logger.info("Parseo de LaTeX a AST completado con éxito.")
            return tree
        except Exception as e:
            logger.error(
                f"[ERR_PARSER_002] Error interno durante el parseo de '{latex}': {e}"
            )
            raise
