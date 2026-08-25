"""
---
file: src/utils/qt_utils.py
module: src.utils.qt_utils
description: Funciones de utilidad y helpers para gestión recursiva de layouts en PySide6.
type: utils/helper
version: 1.0.0
date: 2026-08-24
dependencies: []
relations:
  - src/ui/components/palette_widget.py
exports:
  - clear_layout: "Limpia recursivamente todos los widgets y sub-layouts de un QLayout"
test: pytest tests/test_editor_widget.py
constraints:
  - "Utilizar deleteLater para asegurar la liberación adecuada de memoria en widgets Qt"
keywords:
  - clear-layout
  - qlayout
  - memory-management
  - qt-helpers
---

Qt/PySide6 utility functions.
"""

from __future__ import annotations

from PySide6.QtWidgets import QLayout


def clear_layout(layout: QLayout | None) -> None:
    """Limpia recursivamente todos los widgets y sub-layouts de un QLayout.

    Este método asegura la liberación adecuada de memoria al eliminar
    físicamente (mediante `deleteLater`) todos los hijos anidados de un contenedor.

    Args:
        layout: El layout padre a limpiar. Puede ser `None` (no hace nada).
    """
    if layout is None:
        return
    try:
        while layout.count():
            item = layout.takeAt(0)
            if item is None:
                continue
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            elif item.layout() is not None:
                clear_layout(item.layout())
    except RuntimeError:
        return
