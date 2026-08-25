"""
---
file: src/ui/__init__.py
module: src.ui
description: Paquete principal de la interfaz gráfica de usuario de Traductor Mates (PySide6 / Qt6, Tema Hatsune Miku).
type: ui/package
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.ui.main_window
  - src.ui.theme
  - src.ui.components
relations:
  - docs/ARCHITECTURE.md
  - main.py
exports: []
test: pytest tests/test_editor_widget.py
constraints:
  - "Garantizar la compatibilidad multiplataforma de componentes gráficos con PySide6"
keywords:
  - ui-package
  - pyside6
  - main-window
  - theme
  - components
---

User Interface Package for Traductor Mates.
"""

from __future__ import annotations
