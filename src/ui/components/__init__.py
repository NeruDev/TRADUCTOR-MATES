"""
---
file: src/ui/components/__init__.py
module: src.ui.components
description: Paquete de componentes visuales modulares de interfaz de usuario para Traductor Mates.
type: ui/package
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.ui.components.action_bar
  - src.ui.components.bracket_widget
  - src.ui.components.code_panel
  - src.ui.components.constant_card
  - src.ui.components.edit_formula_dialog
  - src.ui.components.editor_widget
  - src.ui.components.help_dialog
  - src.ui.components.log_dialog
  - src.ui.components.palette_widget
  - src.ui.components.preview_panel
  - src.ui.components.procedure_card
  - src.ui.components.save_formula_dialog
  - src.ui.components.svg_cache
  - src.ui.components.template_card
  - src.ui.components.unit_card
relations:
  - docs/ARCHITECTURE.md
  - src/ui/main_window.py
exports: []
test: pytest tests/test_editor_widget.py
constraints:
  - "Mantener modularidad e independencia de estilos reutilizables en componentes UI"
keywords:
  - ui-components
  - action-bar
  - editor-widget
  - palette-widget
  - preview-panel
  - code-panel
---

UI Components Package for Modular Formula Editing, Palette Browsing, and Rendering.
"""

from __future__ import annotations
