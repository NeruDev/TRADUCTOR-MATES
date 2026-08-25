"""
---
file: src/utils/recovery_manager.py
module: src.utils.recovery_manager
description: Gestor de auto-guardado en caliente para recuperación de fórmulas ante cierres inesperados.
type: utils/manager
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.logger
relations:
  - docs/ARCHITECTURE.md
  - src/ui/main_window.py
exports:
  - RecoveryManager: "Gestor para guardar, cargar y limpiar el estado de recuperación de la ecuación"
test: pytest tests/test_editor_widget.py
constraints:
  - "Garantizar la escritura atómica y la limpieza del archivo temporal al cerrar normalmente"
keywords:
  - recovery-manager
  - auto-save
  - crash-recovery
  - session-persistence
---

Crash recovery manager for auto-saving equation state.
"""

from __future__ import annotations

import os

from src.core.logger import ERROR_CODES, get_logger


class RecoveryManager:
    """Gestor de auto-guardado para recuperación de fórmulas (Crash Recovery).

    Escribe continuamente el estado de la ecuación en un archivo de texto oculto
    para prevenir pérdida de datos en caso de cierres abruptos o caídas de PySide6.
    """

    def __init__(self) -> None:
        self.recovery_file: str = os.path.join(
            os.path.expanduser("~"), ".traductor_mates_recovery.txt"
        )
        self.logger = get_logger()

    def save_state(self, latex_str: str) -> None:
        """Escribe la cadena de texto de la fórmula actual en disco.

        Args:
            latex_str: El código LaTeX representando el estado de la ecuación.
        """
        try:
            with open(self.recovery_file, "w", encoding="utf-8") as f:
                f.write(latex_str)
        except Exception as e:  # noqa: BLE001
            self.logger.error(
                f"{ERROR_CODES['IO_ERR']} Error al guardar recuperación: {e!s}"
            )

    def load_state(self) -> str | None:
        """Lee el estado previo de la ecuación desde el archivo temporal.

        Returns:
            La cadena LaTeX guardada, o `None` si no existe o está vacío.
        """
        if os.path.exists(self.recovery_file):
            try:
                with open(self.recovery_file, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    return content if content else None
            except Exception as e:  # noqa: BLE001
                self.logger.error(
                    f"{ERROR_CODES['IO_ERR']} Error al leer recuperación: {e!s}"
                )
        return None

    def clear_state(self) -> None:
        """Elimina el archivo temporal del disco.

        Debe invocarse durante un cierre seguro y normal de la aplicación.
        """
        if os.path.exists(self.recovery_file):
            try:
                os.remove(self.recovery_file)
            except Exception as e:  # noqa: BLE001
                self.logger.error(
                    f"{ERROR_CODES['IO_ERR']} Error al limpiar recuperación: {e!s}"
                )
