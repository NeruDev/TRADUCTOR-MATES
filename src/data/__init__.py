"""
---
file: src/data/__init__.py
module: src.data
description: Paquete de datos estructurados para fórmulas, símbolos, constantes y unidades del sistema.
type: data/package
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.data.constants
  - src.data.symbols
  - src.data.units
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/palette_widget.py
exports: []
test: pytest tests/test_parser.py
constraints:
  - "Mantener la integridad de los catálogos y formatos LaTeX exportables"
keywords:
  - data-package
  - constants
  - symbols
  - units
  - formulas
---

Structured Data Package for Mathematical Formulas, Symbols, Constants and Units.
"""

from __future__ import annotations
