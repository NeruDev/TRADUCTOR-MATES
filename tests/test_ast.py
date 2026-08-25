"""
---
file: tests/test_ast.py
module: tests.test_ast
description: Pruebas unitarias para manipulación y navegación del Árbol de Sintaxis Abstracta (AST).
type: test/unit
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
relations:
  - src/core/ast.py
exports: []
test: pytest tests/test_ast.py
constraints:
  - "Verificar inserción, anidamiento de casillas y exportación LaTeX en nodos hoja y plantillas"
keywords:
  - test-ast
  - math-tree
  - slot-navigation
  - template-nodes
---

Unit Tests for Math AST and Slot Navigation Engine.
"""

from __future__ import annotations

from src.core.ast import (
    DerivativeNode,
    FractionNode,
    MathTree,
    PowerNode,
    SquareRootNode,
    SubSupNode,
    SymbolNode,
)


def test_empty_tree_to_latex():
    tree = MathTree()
    assert tree.to_latex() == ""


def test_text_insertion():
    tree = MathTree()
    tree.insert_text("x + 5")
    assert tree.to_latex() == "x + 5"


def test_fraction_insertion():
    tree = MathTree()
    tree.insert_text("a = ")
    frac = FractionNode()
    tree.insert_node(frac)
    assert tree.active_slot == frac.slots["num"]
    tree.insert_text("1")
    tree.navigate_next_slot()
    assert tree.active_slot == frac.slots["den"]
    tree.insert_text("x")
    assert tree.to_latex() == r"a = \frac{ 1 }{ x }"


def test_nested_templates():
    tree = MathTree()
    frac = FractionNode()
    tree.insert_node(frac)
    sqrt = SquareRootNode()
    tree.insert_node(sqrt)
    sqrt.slots["radicand"].insert_text("y")
    tree.active_slot = frac.slots["den"]
    pow_node = PowerNode()
    tree.insert_node(pow_node)
    pow_node.slots["base"].insert_text("x")
    pow_node.slots["exp"].insert_text("2")
    assert tree.to_latex() == r"\frac{ \sqrt{ y } }{ { x }^{ 2 } }"


def test_symbol_node_rare_symbols():
    tree = MathTree()
    aleph = SymbolNode(r"\aleph", "ℵ")
    infty = SymbolNode(r"\infty", "∞")
    nabla = SymbolNode(r"\nabla", "∇")
    tree.insert_node(aleph)
    tree.insert_text(" = ")
    tree.insert_node(infty)
    tree.insert_text(" \\cdot ")
    tree.insert_node(nabla)
    assert tree.to_latex() == r"\aleph  = \infty  \cdot \nabla "


def test_derivative_and_subsup():
    tree = MathTree()
    deriv = DerivativeNode(is_partial=True)
    tree.insert_node(deriv)
    deriv.slots["var"].insert_text("x")
    deriv.slots["func"].insert_text("f(x)")

    tree.active_slot = tree.root_slot
    subsup = SubSupNode()
    tree.insert_node(subsup)
    subsup.slots["base"].insert_text("x")
    subsup.slots["sub"].insert_text("i")
    subsup.slots["sup"].insert_text("n")

    latex = tree.to_latex()
    assert r"\partial" in latex


def test_clear_all():
    tree = MathTree()
    tree.insert_text("123")
    tree.clear_all()
    assert tree.to_latex() == ""
    assert tree.active_slot == tree.root_slot
