"""
---
file: tests/test_parser.py
module: tests.test_parser
description: Pruebas unitarias para el analizador sintáctico inverso de LaTeX a AST (LaTeXParser).
type: test/unit
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
  - src.core.parser
  - src.core.translator
  - src.data.symbols
relations:
  - src/core/parser.py
  - src/core/ast.py
exports: []
test: pytest tests/test_parser.py
constraints:
  - "Validar que todos los presets y casos extremos de LaTeX construyan un árbol AST válido"
keywords:
  - test-parser
  - latex-to-ast
  - stream-parser
  - error-fallback
---

Unit Tests for Inverse LaTeX Parser (LaTeXParser).
"""

from __future__ import annotations

from src.core.ast import (
    DerivativeNode,
    FractionNode,
    IndefiniteIntegralNode,
    LimitNode,
    MatrixNode,
    NthRootNode,
    SquareRootNode,
)
from src.core.parser import LaTeXParser


def test_parse_indefinite_integral():
    latex = r"\int {6x} \, d{x}"
    tree = LaTeXParser.parse_to_tree(latex)
    assert len(tree.root_slot.nodes) == 1
    node = tree.root_slot.nodes[0]
    assert isinstance(node, IndefiniteIntegralNode)


def test_parse_matrix():
    latex = r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}"
    tree = LaTeXParser.parse_to_tree(latex)
    assert len(tree.root_slot.nodes) == 1
    node = tree.root_slot.nodes[0]
    assert isinstance(node, MatrixNode)
    assert node.rows == 2
    assert node.cols == 2


def test_parse_fraction_and_roots():
    frac_tree = LaTeXParser.parse_to_tree(r"\frac{a}{b}")
    assert isinstance(frac_tree.root_slot.nodes[0], FractionNode)

    sqrt_tree = LaTeXParser.parse_to_tree(r"\sqrt{x}")
    assert isinstance(sqrt_tree.root_slot.nodes[0], SquareRootNode)

    nth_tree = LaTeXParser.parse_to_tree(r"\sqrt[3]{x}")
    assert isinstance(nth_tree.root_slot.nodes[0], NthRootNode)


def test_parse_derivative_edge_case():
    # Test derivative parsing
    latex = r"\frac{d}{dx} f(x)"
    tree = LaTeXParser.parse_to_tree(latex)
    assert isinstance(tree.root_slot.nodes[0], DerivativeNode)
    assert tree.root_slot.nodes[0].is_partial is False


def test_parse_partial_derivative():
    latex = r"\frac{\partial}{\partial y} g(y)"
    tree = LaTeXParser.parse_to_tree(latex)
    assert isinstance(tree.root_slot.nodes[0], DerivativeNode)
    assert tree.root_slot.nodes[0].is_partial is True


def test_parse_limits():
    latex = r"\lim_{x \to \infty} \frac{1}{x}"
    tree = LaTeXParser.parse_to_tree(latex)
    assert isinstance(tree.root_slot.nodes[0], LimitNode)


def test_unclosed_braces_fallback():
    # Edge case: syntax error fallback
    latex = r"\frac{a"
    tree = LaTeXParser.parse_to_tree(latex)
    assert tree is not None


def test_all_presets_build_valid_tree():
    from src.core.parser import LaTeXParser
    from src.data.symbols import PRESET_FORMULAS

    assert len(PRESET_FORMULAS) >= 50
    for pf in PRESET_FORMULAS:
        if "variations" in pf:
            for var in pf.get("variations", []):
                tree = LaTeXParser.parse_to_tree(var["latex"])
                assert tree is not None
                assert tree.root_slot is not None


def test_parse_expected_value_with_brackets():
    from src.core.translator import LaTeXTranslator

    latex = r"\mathbb{E}[X] = \sum_{i} x_i P(X = x_i)"
    tree = LaTeXParser.parse_to_tree(latex)
    assert tree is not None
    out_latex = LaTeXTranslator.to_latex(tree)
    assert r"\mathbb{E}" in out_latex
    assert "sum" in out_latex
    assert "P(" in out_latex


def test_parse_bernoulli_with_text_cte():
    from src.core.translator import LaTeXTranslator

    latex = r"P + \frac{1}{2} \rho v^2 + \rho g h = \text{cte}"
    tree = LaTeXParser.parse_to_tree(latex)
    assert tree is not None
    out_latex = LaTeXTranslator.to_latex(tree)
    assert r"\text{cte}" in out_latex
    assert r"\rho" in out_latex


def test_parse_physics_vectors_and_decorators():
    from src.core.translator import LaTeXTranslator

    latex = r"\vec{v} + \hat{r} + \dot{x} + \ddot{x} + \mathbf{F}"
    tree = LaTeXParser.parse_to_tree(latex)
    assert tree is not None
    out_latex = LaTeXTranslator.to_latex(tree)
    assert r"\vec{v}" in out_latex
    assert r"\hat{r}" in out_latex
    assert r"\mathbf{F}" in out_latex


def test_parse_modular_and_operatorname():
    from src.core.ast import ModularNode, OperatorNode, SymbolNode

    # 1. Test \operatorname{mcd} and \operatorname{mcm}
    tree = LaTeXParser.parse_to_tree(
        r"\operatorname{mcd}(a, b) \cdot \operatorname{mcm}(a, b)"
    )
    op_nodes = [n for n in tree.root_slot.nodes if isinstance(n, OperatorNode)]
    assert len(op_nodes) == 2
    assert op_nodes[0].display == "mcd"
    assert op_nodes[1].display == "mcm"

    # 2. Test \pmod{m}
    tree_mod = LaTeXParser.parse_to_tree(r"a \equiv b \pmod{m} \iff m \mid (a - b)")
    mod_nodes = [n for n in tree_mod.root_slot.nodes if isinstance(n, ModularNode)]
    assert len(mod_nodes) == 1
    assert mod_nodes[0].slots["mod"].to_latex().strip() == "m"

    sym_nodes = [n for n in tree_mod.root_slot.nodes if isinstance(n, SymbolNode)]
    sym_latex = [s.latex_cmd for s in sym_nodes]
    assert r"\equiv" in sym_latex
    assert r"\iff" in sym_latex
    assert r"\mid" in sym_latex


def test_parse_hyperbolic_and_product():
    from src.core.ast import OperatorNode, ProductNode

    # 1. Test \sinh, \cosh, \tanh
    tree_hyp = LaTeXParser.parse_to_tree(r"\tanh(x) = \frac{\sinh(x)}{\cosh(x)}")
    op_names = [
        n.display for n in tree_hyp.root_slot.nodes if isinstance(n, OperatorNode)
    ]
    assert "tanh" in op_names

    # 2. Test \prod
    tree_prod = LaTeXParser.parse_to_tree(
        r"\prod_{p \mid n} \left(1 - \frac{1}{p}\right)"
    )
    prod_nodes = [n for n in tree_prod.root_slot.nodes if isinstance(n, ProductNode)]
    assert len(prod_nodes) == 1
    assert prod_nodes[0].slots["lower"].to_latex() is not None


def test_parse_definite_integral_laplace_limits():
    from src.core.ast import DefiniteIntegralNode

    latex = r"\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st} f(t) \, dt"
    tree = LaTeXParser.parse_to_tree(latex)
    assert tree is not None
    int_nodes = [n for n in tree.root_slot.nodes if isinstance(n, DefiniteIntegralNode)]
    assert len(int_nodes) == 1
    integ = int_nodes[0]
    assert integ.slots["lower"].to_latex().strip() == "0"
    assert integ.slots["upper"].to_latex().strip() == r"\infty"
