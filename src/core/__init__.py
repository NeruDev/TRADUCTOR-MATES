"""
---
file: src/core/__init__.py
module: src.core
description: Paquete principal del motor lógico y sintáctico de Traductor Mates (AST, Parser, Renderer, Syntax, Translator, Logger).
type: core/package
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
  - src.core.logger
  - src.core.parser
  - src.core.renderer
  - src.core.syntax
  - src.core.translator
relations:
  - docs/ARCHITECTURE.md
  - main.py
exports: []
test: pytest tests/test_ast.py tests/test_parser.py tests/test_translator.py
constraints:
  - "Mantener desacoplada la lógica del motor matemático respecto a la capa gráfica PySide6"
keywords:
  - core-engine
  - math-ast
  - parser
  - renderer
  - syntax
  - translator
  - logger
---

Core Engine Package for Math AST, Translation, Syntax Highlighting and Rendering.
"""
