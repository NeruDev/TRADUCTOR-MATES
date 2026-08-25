"""
---
file: main.py
module: main
description: Punto de entrada principal ejecutable de la aplicación Traductor Mates con manejadores globales de excepciones.
type: app/entrypoint
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.logger
  - src.ui.main_window
relations:
  - docs/ARCHITECTURE.md
exports:
  - global_exception_handler: "Atrapa excepciones no controladas y las presenta en un diálogo crítico"
  - qt_message_handler: "Filtra advertencias cosméticas de renderizado SVG en la salida de consola"
  - main: "Inicializa la instancia de QApplication y muestra la ventana principal MainWindow"
test: pytest tests/test_editor_widget.py
constraints:
  - "Garantizar la captura de fallos críticos antes de la inicialización de la interfaz gráfica"
keywords:
  - main-entry-point
  - qapplication
  - global-exception-handler
  - qt-message-handler
  - main-window-launch
---

Main Application Entry Point for Traductor Mates.
Initializes PySide6 QApplication, configures global crash handling and displays the main window cleanly.
"""

from __future__ import annotations

import os
import sys
import traceback
from types import TracebackType
from typing import Any

# Ensure current workspace directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("QT_SVG_DEFAULT_OPTIONS", "2")

from PySide6.QtCore import QtMsgType, qInstallMessageHandler
from PySide6.QtSvg import QSvgRenderer, QtSvg
from PySide6.QtWidgets import QApplication, QMessageBox

from src.core.logger import get_logger
from src.ui.main_window import MainWindow


def global_exception_handler(
    exc_type: type[BaseException],
    exc_value: BaseException,
    exc_traceback: TracebackType | None,
) -> None:
    """Atrapa excepciones y muestra el error detallado de Python 3.11+ en una ventana emergente.

    Aprovechando las mejoras de reporte de errores de Python recientes, esta
    función captura la traza completa (con indicadores de columna) y la muestra
    directamente al usuario sin necesidad de consultar el log de sesión.

    Args:
        exc_type: Tipo o clase de la excepción generada.
        exc_value: Instancia de la excepción con el mensaje de error.
        exc_traceback: Objeto de traza de ejecución (traceback) o None.
    """
    logger = get_logger()
    logger.critical(
        f"[CRASH_FATAL] Excepción no controlada: {exc_value}",
        exc_info=(exc_type, exc_value, exc_traceback),
    )

    error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))

    app = QApplication.instance()
    if app:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Error Fatal de Ejecución")
        msg_box.setText(
            f"Ha ocurrido un error inesperado:\n{exc_type.__name__}: {exc_value}"
        )
        msg_box.setDetailedText(error_msg)

        font = msg_box.font()
        font.setFamily("Consolas")
        msg_box.setFont(font)

        msg_box.exec()

    sys.__excepthook__(exc_type, exc_value, exc_traceback)


def qt_message_handler(mode: QtMsgType, context: Any, message: str) -> None:
    """Filtra y suprime mensajes informativos/advertencias benignas del motor Qt.

    Args:
        mode: Nivel de severidad del mensaje de Qt (Debug, Warning, Critical, Fatal).
        context: Contexto de origen del mensaje Qt (archivo, línea, función).
        message: Cadena de texto del mensaje generado por Qt.
    """
    if (
        "nested svg element" in message
        or "Invalid path data" in message
        or "setPointSize" in message
        or "Too many nested nodes" in message
        or "QSvgHandler" in message
        or "QT_SVG_DEFAULT_OPTIONS" in message
    ):
        return
    sys.stderr.write(f"{message}\n")


sys.excepthook = global_exception_handler


def main() -> None:
    """Punto de entrada principal para lanzar Traductor Mates.

    Configura e inicializa el bucle de eventos de `QApplication` de PySide6,
    instala el manejador de mensajes de Qt, define el nombre de la app,
    instancia la ventana principal (`MainWindow`) y cede el control.
    """
    qInstallMessageHandler(qt_message_handler)
    QSvgRenderer.setDefaultOptions(QtSvg.Option.AssumeTrustedSource)

    app = QApplication(sys.argv)
    app.setApplicationName("Traductor Mates")
    app.setOrganizationName("Traductor Mates")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
