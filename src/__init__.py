"""
---
file: src/__init__.py
module: src
description: Paquete principal del código fuente de Traductor Mates.
type: core/package
version: 1.0.0
date: 2026-08-24
dependencies: []
relations:
  - main.py
  - docs/ARCHITECTURE.md
exports: []
test: pytest tests/test_editor_widget.py
constraints:
  - "Mantener importaciones diferidas para no penalizar el tiempo de arranque de la aplicación"
keywords:
  - src-package
  - traductor-mates
  - math-editor
---

Traductor Mates Application Package.
"""

from __future__ import annotations

__version__ = "1.0.0"
