"""
---
file: tests/__init__.py
module: tests
description: Paquete raíz de la suite de pruebas unitarias de Traductor Mates.
type: test/suite
version: 1.0.0
date: 2026-08-24
dependencies: []
relations:
  - docs/ARCHITECTURE.md
exports: []
test: pytest tests/
constraints:
  - "Mantener aislamiento de las pruebas y evitar dependencias cruzadas con efectos secundarios"
keywords:
  - test-suite
  - pytest
  - unit-tests
---

Unit Test Suite Package.
"""

from __future__ import annotations
