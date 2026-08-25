"""
---
file: src/ui/components/action_bar.py
module: src.ui.components.action_bar
description: Barra de herramientas superior con controles globales (tema, visor de logs y guía de ayuda).
type: ui/component
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.logger
  - src.ui.theme
  - src.ui.components.help_dialog
  - src.ui.components.log_dialog
relations:
  - docs/ARCHITECTURE.md
  - src/ui/main_window.py
exports:
  - MathActionBarWidget: "Barra de herramientas superior y panel de control global"
test: pytest tests/test_editor_widget.py
constraints:
  - "Garantizar la actualización inmediata de la interfaz de botones ante cambios de tema"
keywords:
  - action-bar
  - theme-toggled
  - session-logs
  - help-dialog
  - toolbar
---

Top Action Bar & Controls Widget.
Includes theme toggle (Dark/Light Hatsune Miku), Session Logs viewer, and Help Dialog.
"""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)

from src.core.logger import get_logger
from src.ui.components.log_dialog import SessionLogDialog
from src.ui.theme import COLOR_MIKU_CYAN

logger = get_logger()


class MathActionBarWidget(QFrame):
    """Barra de herramientas superior y panel de acciones globales.

    Contiene los controles para alternar el tema, ver logs en vivo
    y abrir la ventana modal de documentación y ayuda del sistema.

    Args:
        parent: Widget contenedor padre opcional.

    Attributes:
        clear_requested: Señal de solicitud de limpieza total.
        save_requested: Señal de solicitud de guardado de fórmula.
        undo_requested: Señal de solicitud de deshacer cambios.
        redo_requested: Señal de solicitud de rehacer cambios.
        theme_toggled: Señal de alternancia de tema claro/oscuro.
    """

    clear_requested = Signal()
    save_requested = Signal()
    undo_requested = Signal()
    redo_requested = Signal()
    theme_toggled = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setProperty("class", "android-card-flat")
        self.current_theme: str = "dark"

        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 6, 12, 6)
        layout.setSpacing(10)

        # App Brand & Pill Badge
        title_box = QWidget()
        tb_layout = QHBoxLayout(title_box)
        tb_layout.setContentsMargins(0, 0, 0, 0)
        tb_layout.setSpacing(6)

        self.app_title = QLabel("Traductor Mates")
        self.app_title.setStyleSheet("font-weight: bold; font-size: 15px;")

        self.badge = QLabel("Miku Theme")
        self.badge.setStyleSheet(
            f"background: {COLOR_MIKU_CYAN}; color: #FFFFFF; font-size: 10px; font-weight: bold; "
            "border-radius: 8px; padding: 2px 6px;"
        )

        tb_layout.addWidget(self.app_title)
        tb_layout.addWidget(self.badge)
        layout.addWidget(title_box)

        layout.addStretch()

        # Theme Toggle Button (Light/Dark Mode with dynamic emoji)
        self.btn_theme = QPushButton("☀️ Modo Claro")
        self.btn_theme.setProperty("class", "theme-toggle-btn")
        self.btn_theme.setCursor(Qt.PointingHandCursor)
        self.btn_theme.clicked.connect(lambda: self.theme_toggled.emit())
        layout.addWidget(self.btn_theme)

        # Logs Button
        self.btn_logs = QPushButton("📋 Logs")
        self.btn_logs.setProperty("class", "action-btn-secondary")
        self.btn_logs.setCursor(Qt.PointingHandCursor)
        self.btn_logs.clicked.connect(self._show_logs_dialog)
        layout.addWidget(self.btn_logs)

        # Help Button
        self.btn_help = QPushButton("❓ Ayuda")
        self.btn_help.setProperty("class", "action-btn")
        self.btn_help.setCursor(Qt.PointingHandCursor)
        self.btn_help.clicked.connect(self._show_help_dialog)
        layout.addWidget(self.btn_help)

    def update_theme_ui(self, theme_name: str) -> None:
        """Actualiza el botón de alternar tema basándose en el modo actual.

        Args:
            theme_name: El modo actualmente activo ('dark' o 'light').
        """
        self.current_theme = theme_name
        if theme_name == "dark":
            self.btn_theme.setText("☀️ Modo Claro")
        else:
            self.btn_theme.setText("🌙 Modo Oscuro")

    def _show_logs_dialog(self) -> None:
        """Abre la ventana modal del visor de logs de sesión."""
        logger.info("El usuario abrió el visor de Logs de Sesión.")
        dialog = SessionLogDialog(self)
        dialog.exec_()

    def _show_help_dialog(self) -> None:
        """Abre la ventana modal con la guía de usuario y manual del sistema."""
        logger.info("El usuario abrió el diálogo de ayuda extendido.")
        from src.ui.components.help_dialog import HelpDialog

        dialog = HelpDialog(self)
        dialog.exec_()
