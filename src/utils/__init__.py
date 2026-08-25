"""
---
file: src/utils/__init__.py
module: src.utils
description: Paquete de utilidades generales, gestores de persistencia y helpers de Qt.
type: utils/package
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.utils.favorites_manager
  - src.utils.qt_utils
  - src.utils.recovery_manager
  - src.utils.user_formulas_manager
relations:
  - docs/ARCHITECTURE.md
  - main.py
exports: []
test: pytest tests/test_editor_widget.py
constraints:
  - "Mantener desacoplados los módulos de persistencia respecto a la lógica directa del AST"
keywords:
  - utils
  - favorites-manager
  - recovery-manager
  - user-formulas-manager
  - qt-utils
---

Utilities package providing crash recovery, user formula persistence, favorites management, and Qt helpers.
"""

from __future__ import annotations
