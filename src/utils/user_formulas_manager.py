"""
---
file: src/utils/user_formulas_manager.py
module: src.utils.user_formulas_manager
description: Gestor de fórmulas, variaciones, ramas, categorías y subcategorías personalizadas creadas por el usuario.
type: utils/manager
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.logger
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/palette_widget.py
  - src/ui/components/save_formula_dialog.py
  - src/ui/components/edit_formula_dialog.py
exports:
  - UserFormulasManager: "Gestor de persistencia de fórmulas, categorías y variantes de usuario en JSON"
test: pytest tests/test_editor_widget.py
constraints:
  - "Mantener la integridad referencial de variantes, UUIDs y orden de categorías"
keywords:
  - user-formulas-manager
  - json-persistence
  - formula-variations
  - categories
  - subcategories
---

Manager for user-defined custom formulas and categories persistence.
"""

from __future__ import annotations

import json
import os
import uuid
from typing import Any

from src.core.logger import ERROR_CODES, get_logger


class UserFormulasManager:
    """Gestor de fórmulas personalizadas del usuario.

    Guarda y carga categorías, subcategorías, fórmulas y variantes
    en un archivo JSON local persistente.
    """

    def __init__(self) -> None:
        self.file_path: str = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "..", "data", "user_formulas_data.json"
            )
        )
        self.categories: list[dict[str, Any]] = self.load()

    def load(self) -> list[dict[str, Any]]:
        """Carga la estructura de categorías desde el archivo de datos JSON.

        Returns:
            Lista de diccionarios de categorías y subcategorías.
        """
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        return data
            except (OSError, json.JSONDecodeError) as e:
                logger = get_logger()
                logger.error(
                    f"{ERROR_CODES.get('IO_ERR', '[ERR_IO]')} Error al cargar fórmulas: {e!s}"
                )
        return []

    def save(self) -> None:
        """Guarda la estructura actual de categorías y fórmulas en el archivo JSON."""
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(self.categories, f, indent=4, ensure_ascii=False)
        except (OSError, TypeError) as e:
            logger = get_logger()
            logger.error(
                f"{ERROR_CODES.get('IO_ERR', '[ERR_IO]')} Error al guardar fórmulas: {e!s}"
            )

    def add_formula(
        self,
        category: str,
        subcategory: str,
        name: str,
        latex: str,
        description: str = "",
        variations: list[dict[str, str]] | None = None,
    ) -> None:
        """Añade una nueva fórmula al catálogo de usuario.

        Args:
            category: Nombre de la categoría contenedora.
            subcategory: Nombre de la subcategoría contenedora.
            name: Nombre principal de la ecuación.
            latex: Código LaTeX principal.
            description: Contexto o descripción opcional.
            variations: Lista opcional de variantes paso a paso.
        """
        cat_obj = next((c for c in self.categories if c["category"] == category), None)
        if not cat_obj:
            cat_obj = {"category": category, "subcategories": []}
            self.categories.append(cat_obj)

        subcat_obj = next(
            (s for s in cat_obj["subcategories"] if s["name"] == subcategory), None
        )
        if not subcat_obj:
            subcat_obj = {"name": subcategory, "formulas": []}
            cat_obj["subcategories"].append(subcat_obj)

        subcat_obj["formulas"].append(
            {
                "id": str(uuid.uuid4()),
                "name": name,
                "description": description,
                "latex": latex,
                "variations": variations or [{"name": name, "latex": latex}],
            }
        )
        self.save()

    def remove_formula(self, formula_id: str) -> None:
        """Elimina una fórmula buscando por su identificador único.

        Args:
            formula_id: UUID de la fórmula a remover.
        """
        for cat in self.categories:
            for subcat in cat["subcategories"]:
                original_len = len(subcat["formulas"])
                subcat["formulas"] = [
                    f for f in subcat["formulas"] if f["id"] != formula_id
                ]
                if len(subcat["formulas"]) < original_len:
                    if not subcat["formulas"]:
                        cat["subcategories"].remove(subcat)
                    if not cat["subcategories"]:
                        self.categories.remove(cat)
                    self.save()
                    return

    def update_formula(
        self,
        formula_id: str,
        new_category: str,
        new_subcategory: str,
        new_name: str,
        new_latex: str,
        new_description: str = "",
        new_variations: list[dict[str, str]] | None = None,
    ) -> bool:
        """Actualiza el nombre, descripción, latex, variaciones y ubicación de una fórmula.

        Args:
            formula_id: UUID de la fórmula existente.
            new_category: Nueva categoría destino.
            new_subcategory: Nueva subcategoría destino.
            new_name: Nuevo nombre principal.
            new_latex: Nuevo código LaTeX.
            new_description: Nueva descripción.
            new_variations: Lista actualizada de variantes.

        Returns:
            `True` si la fórmula fue encontrada y actualizada, `False` en caso contrario.
        """
        formula_found = None
        for cat in self.categories:
            for subcat in cat["subcategories"]:
                for formula in subcat["formulas"]:
                    if formula["id"] == formula_id:
                        formula_found = formula
                        break
                if formula_found:
                    break
            if formula_found:
                break

        if not formula_found:
            return False

        # Remover de la ubicación previa
        self.remove_formula(formula_id)

        # Añadir a la nueva ubicación preservando el ID
        cat_obj = next(
            (c for c in self.categories if c["category"] == new_category), None
        )
        if not cat_obj:
            cat_obj = {"category": new_category, "subcategories": []}
            self.categories.append(cat_obj)

        subcat_obj = next(
            (s for s in cat_obj["subcategories"] if s["name"] == new_subcategory), None
        )
        if not subcat_obj:
            subcat_obj = {"name": new_subcategory, "formulas": []}
            cat_obj["subcategories"].append(subcat_obj)

        subcat_obj["formulas"].append(
            {
                "id": formula_id,
                "name": new_name,
                "description": new_description,
                "latex": new_latex,
                "variations": new_variations
                or [{"name": new_name, "latex": new_latex}],
            }
        )
        self.save()
        return True

    def edit_category(self, old_name: str, new_name: str) -> None:
        """Renombra una categoría existente.

        Args:
            old_name: Nombre actual de la categoría.
            new_name: Nuevo nombre a asignar.
        """
        for cat in self.categories:
            if cat["category"] == old_name:
                cat["category"] = new_name
                self.save()
                break

    def remove_category(self, cat_name: str) -> None:
        """Elimina una categoría completa y todas sus subcategorías y fórmulas.

        Args:
            cat_name: Nombre de la categoría a eliminar.
        """
        self.categories = [c for c in self.categories if c["category"] != cat_name]
        self.save()

    def move_category(self, cat_name: str, direction: int) -> None:
        """Reordena la posición de una categoría en la lista visual.

        Args:
            cat_name: Nombre de la categoría a desplazar.
            direction: Desplazamiento relativo (+1 para abajo, -1 para arriba).
        """
        idx = next(
            (i for i, c in enumerate(self.categories) if c["category"] == cat_name), -1
        )
        if idx != -1 and 0 <= idx + direction < len(self.categories):
            self.categories[idx], self.categories[idx + direction] = (
                self.categories[idx + direction],
                self.categories[idx],
            )
            self.save()

    def edit_subcategory(self, cat_name: str, old_sub: str, new_sub: str) -> None:
        """Renombra una subcategoría dentro de una categoría dada.

        Args:
            cat_name: Nombre de la categoría contenedora.
            old_sub: Nombre actual de la subcategoría.
            new_sub: Nuevo nombre para la subcategoría.
        """
        for cat in self.categories:
            if cat["category"] == cat_name:
                for sub in cat["subcategories"]:
                    if sub["name"] == old_sub:
                        sub["name"] = new_sub
                        self.save()
                        return

    def remove_subcategory(self, cat_name: str, sub_name: str) -> None:
        """Elimina una subcategoría y todas sus fórmulas asociadas.

        Args:
            cat_name: Nombre de la categoría contenedora.
            sub_name: Nombre de la subcategoría a eliminar.
        """
        for cat in self.categories:
            if cat["category"] == cat_name:
                cat["subcategories"] = [
                    s for s in cat["subcategories"] if s["name"] != sub_name
                ]
                if not cat["subcategories"]:
                    self.categories.remove(cat)
                self.save()
                return

    def move_subcategory(self, cat_name: str, sub_name: str, direction: int) -> None:
        """Reordena la posición de una subcategoría dentro de su categoría.

        Args:
            cat_name: Nombre de la categoría contenedora.
            sub_name: Nombre de la subcategoría a mover.
            direction: Desplazamiento relativo (+1 para abajo, -1 para arriba).
        """
        for cat in self.categories:
            if cat["category"] == cat_name:
                subs = cat["subcategories"]
                idx = next((i for i, s in enumerate(subs) if s["name"] == sub_name), -1)
                if idx != -1 and 0 <= idx + direction < len(subs):
                    subs[idx], subs[idx + direction] = subs[idx + direction], subs[idx]
                    self.save()
                return
