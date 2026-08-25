"""
---
file: src/utils/favorites_manager.py
module: src.utils.favorites_manager
description: Gestor de símbolos y plantillas favoritas del usuario con almacenamiento persistente en JSON.
type: utils/manager
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.logger
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/palette_widget.py
exports:
  - FavoritesManager: "Gestor de persistencia de favoritos locales del usuario en JSON"
test: pytest tests/test_editor_widget.py
constraints:
  - "Manejar defensivamente errores de I/O y corrupción de JSON sin interrumpir la interfaz"
keywords:
  - favorites-manager
  - json-persistence
  - user-favorites
  - palette-favorites
---

Manager for user favorites persistence.
"""

from __future__ import annotations

import json
import os

from src.core.logger import ERROR_CODES, get_logger


class FavoritesManager:
    """Gestor de persistencia de símbolos y plantillas favoritas del usuario.

    Guarda un listado de IDs en un archivo JSON local en el directorio
    de usuario para mantener las preferencias entre ejecuciones.
    """

    def __init__(self) -> None:
        self.favorites_file: str = os.path.join(
            os.path.expanduser("~"), ".traductor_mates_favorites.json"
        )
        self.favorite_ids: list[str] = self.load()

    def load(self) -> list[str]:
        """Carga la lista de favoritos desde el archivo de configuración.

        Returns:
            Una lista de identificadores (IDs) de los elementos favoritos.
        """
        if os.path.exists(self.favorites_file):
            try:
                with open(self.favorites_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        return data
            except (OSError, json.JSONDecodeError) as e:
                logger = get_logger()
                logger.error(
                    f"{ERROR_CODES['IO_ERR']} Error al cargar favoritos desde {self.favorites_file}: {e!s}"
                )
        return []

    def save(self) -> None:
        """Guarda la lista actual de favoritos en el archivo JSON.

        Captura errores I/O y los registra mediante el sistema central de logging.
        """
        try:
            with open(self.favorites_file, "w", encoding="utf-8") as f:
                json.dump(self.favorite_ids, f)
        except (OSError, TypeError) as e:
            logger = get_logger()
            logger.error(
                f"{ERROR_CODES['IO_ERR']} Error al guardar favoritos en {self.favorites_file}: {e!s}"
            )

    def toggle(self, item_id: str) -> bool:
        """Añade o elimina un elemento de la lista de favoritos.

        Alterna el estado del `item_id`: si existe lo remueve, si no existe lo agrega.
        Posteriormente, invoca el auto-guardado en disco.

        Args:
            item_id: El identificador único del símbolo o plantilla.

        Returns:
            `True` si el elemento fue añadido; `False` si fue removido.
        """
        if item_id in self.favorite_ids:
            self.favorite_ids.remove(item_id)
            added = False
        else:
            self.favorite_ids.append(item_id)
            added = True
        self.save()
        return added

    def is_favorite(self, item_id: str) -> bool:
        """Verifica si un elemento se encuentra en favoritos.

        Args:
            item_id: El identificador a buscar.

        Returns:
            `True` si está en la lista de favoritos, `False` en caso contrario.
        """
        return item_id in self.favorite_ids
