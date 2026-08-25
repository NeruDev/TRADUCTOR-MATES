"""
---
file: src/ui/components/log_dialog.py
module: src.ui.components.log_dialog
description: Cuadro de diálogo modal para la visualización en tiempo real de los logs de sesión.
type: ui/dialog
version: 1.0.0
date: 2026-08-24
dependencies: []
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/action_bar.py
  - src/core/logger.py
exports:
  - SessionLogDialog: "Cuadro de diálogo modal para leer e inspeccionar el archivo session.log"
test: pytest tests/test_editor_widget.py
constraints:
  - "Manejar la lectura segura y el scroll automático al final del historial de logs"
keywords:
  - log-dialog
  - session-logs
  - diagnostics
  - modal-dialog
  - log-viewer
---

Dialog window to view session logs.
"""

from __future__ import annotations

import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialog, QHBoxLayout, QPushButton, QTextEdit, QVBoxLayout


class SessionLogDialog(QDialog):
    """Cuadro de diálogo modal para la lectura del historial de sesión.

    Muestra el archivo `session.log` generado por `SessionLogger` en tiempo
    real, utilizando fuente monoespaciada para alinear los códigos de error.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Visor de Logs de Sesión")
        self.resize(800, 500)

        self.log_file_path = "session.log"

        layout = QVBoxLayout(self)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        # Use a monospaced font
        font = QFont("Consolas", 10)
        font.setStyleHint(QFont.Monospace)
        self.text_edit.setFont(font)

        # Enable word wrap
        self.text_edit.setLineWrapMode(QTextEdit.NoWrap)

        layout.addWidget(self.text_edit)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        self.btn_refresh = QPushButton("🔄 Actualizar")
        self.btn_refresh.setCursor(Qt.PointingHandCursor)
        self.btn_refresh.clicked.connect(self.load_logs)

        self.btn_close = QPushButton("Cerrar")
        self.btn_close.setCursor(Qt.PointingHandCursor)
        self.btn_close.clicked.connect(self.accept)

        btn_layout.addWidget(self.btn_refresh)
        btn_layout.addWidget(self.btn_close)

        layout.addLayout(btn_layout)

        self.load_logs()

    def load_logs(self) -> None:
        """Carga y muestra el contenido actual del archivo de registros.

        Realiza lectura segura del disco y desliza automáticamente
        la vista hacia el final (eventos más recientes).
        """
        if os.path.exists(self.log_file_path):
            try:
                with open(self.log_file_path, "r", encoding="utf-8") as f:
                    self.text_edit.setPlainText(f.read())
                    # Scroll to bottom
                    self.text_edit.verticalScrollBar().setValue(
                        self.text_edit.verticalScrollBar().maximum()
                    )
            except Exception as e:  # noqa: BLE001
                self.text_edit.setPlainText(f"Error al leer el archivo de logs: {e}")
        else:
            self.text_edit.setPlainText("El archivo session.log aún no existe.")
