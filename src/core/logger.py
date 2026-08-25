"""
---
file: src/core/logger.py
module: src.core.logger
description: Sistema centralizado de registro de eventos, diagnóstico y captura de errores de sesión.
type: core/logger
version: 1.0.0
date: 2026-08-24
dependencies: []
relations:
  - docs/ARCHITECTURE.md
  - main.py
exports:
  - SessionLogger: "Gestor Singleton para el logger central de la aplicación"
  - get_logger: "Función de acceso directo al logger de sesión global"
  - capture_error: "Decorador defensivo para registrar excepciones con traza completa y argumentos"
test: pytest tests/test_parser.py tests/test_editor_widget.py
constraints:
  - "Garantizar formato estructurado con timestamp y códigos de error normalizados"
  - "Evitar bloqueos I/O durante la captura y registro de excepciones"
keywords:
  - session-logger
  - diagnostics
  - capture-error
  - error-codes
  - logging
---

Centralized Logging & Diagnostics Module for Traductor Mates.
Manages session logs, standardized error codes, and exception trace capture.
"""

from __future__ import annotations

import functools
import logging
import traceback
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any


# 3. Configuración Operativa del Logger
@dataclass(frozen=True)
class LoggerConfig:
    """Parámetros de configuración del sistema de diagnóstico y logs.

    Attributes:
        log_file: Nombre del archivo de registro de sesión.
        date_format: Formato de fecha y hora para las entradas.
        log_format: Patrón de formateo para los mensajes.
    """

    log_file: str = "session.log"
    date_format: str = "%Y-%m-%d %H:%M:%S"
    log_format: str = (
        "[%(asctime)s] [%(levelname)s] %(message)s - (%(module)s:%(lineno)d)"
    )


LOGGER_CONFIG = LoggerConfig()
SESSION_LOG_FILE = LOGGER_CONFIG.log_file

# Códigos de error estándar del sistema
ERROR_CODES: dict[str, str] = {
    "COMM_ERR": "[ERR_COMM_001]",
    "PARSER_ERR": "[ERR_PARSER_002]",
    "AST_ERR": "[ERR_AST_003]",
    "UI_ERR": "[ERR_UI_004]",
    "EXPORT_ERR": "[ERR_EXPORT_005]",
    "THEME_ERR": "[ERR_THEME_006]",
    "CACHE_ERR": "[ERR_CACHE_007]",
    "IO_ERR": "[ERR_IO_008]",
    "JS_ERR": "[ERR_JS_009]",
    "SYSTEM_ERR": "[ERR_SYS_010]",
}


class SessionLogger:
    """Gestor Singleton para el logger de la aplicación."""

    _instance: logging.Logger | None = None

    @classmethod
    def get_logger(cls) -> logging.Logger:
        """Obtiene o inicializa la instancia global del logger.

        Returns:
            Instancia configurada de `logging.Logger`.
        """
        if cls._instance is None:
            logger = logging.getLogger("TraductorMates")
            logger.setLevel(logging.DEBUG)
            if logger.hasHandlers():
                logger.handlers.clear()
            file_handler = logging.FileHandler(
                SESSION_LOG_FILE, mode="w", encoding="utf-8"
            )
            file_handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(message)s - (%(module)s:%(lineno)d)",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            cls._instance = logger
            cls._instance.info("Sesión iniciada. Logger configurado.")
        return cls._instance


def get_logger() -> logging.Logger:
    """Función de conveniencia para acceder al logger global de la sesión.

    Returns:
        Instancia de `logging.Logger` configurada.
    """
    return SessionLogger.get_logger()


def capture_error(error_type: str = "UI_ERR") -> Callable:
    """Decorador para capturar excepciones con traza exacta y variables locales.

    Args:
        error_type: Clave del tipo de error según `ERROR_CODES`.

    Returns:
        Función decoradora envolvente.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as e:  # noqa: BLE001
                logger = get_logger()
                code = ERROR_CODES.get(error_type, "[ERR_UNKNOWN]")
                metadata = f"Args: {args[1:]} | Kwargs: {kwargs}"
                tb = traceback.format_exc()
                logger.error(
                    f"{code} Excepción en {func.__module__}.{func.__name__}: {e!s} | {metadata}\n{tb}"
                )
                # Don't re-raise, we want to fail gracefully in the UI

        return wrapper

    return decorator
