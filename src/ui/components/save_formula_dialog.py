"""
---
file: src/ui/components/save_formula_dialog.py
module: src.ui.components.save_formula_dialog
description: Cuadro de diálogo modal para guardar fórmulas de usuario en ramas, categorías y subcategorías personalizadas.
type: ui/dialog
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.data.symbols
  - src.ui.theme
  - src.ui.components.svg_cache
relations:
  - docs/ARCHITECTURE.md
  - src/ui/main_window.py
exports:
  - SaveFormulaDialog: "Diálogo modal para captura de metadatos y guardado de fórmulas de usuario"
test: pytest tests/test_editor_widget.py
constraints:
  - "Validar que la fórmula LaTeX no esté vacía antes de permitir el guardado"
keywords:
  - save-formula-dialog
  - user-formulas
  - custom-category
  - modal-dialog
---

Dialog window to save user-defined formulas with custom categories and descriptions.
"""

from __future__ import annotations

import re
from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QFrame,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

from src.data.symbols import PRESET_CATEGORIES
from src.ui.components.svg_cache import SVGMathCache
from src.ui.theme import get_theme_dict, get_theme_qss


class SaveFormulaDialog(QDialog):
    """Cuadro de diálogo modal para el registro y persistencia de fórmulas del usuario.

    Args:
        manager: Instancia de UserFormulasManager para persistencia.
        latex_str: Código LaTeX de la fórmula a guardar.
        parent: Widget contenedor padre opcional.
    """

    def __init__(
        self,
        manager: Any,
        latex_str: str,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.manager = manager
        self.latex_str = latex_str
        self.setWindowTitle("Guardar Fórmula")
        self.setMinimumWidth(350)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)

        # Apply Theme
        if parent and hasattr(parent, "current_theme"):
            self.setStyleSheet(get_theme_qss(parent.current_theme))

        self._setup_ui()

    def _setup_ui(self) -> None:
        """Construye los controles interactivos y el diseño visual del diálogo."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        bg_frame = QFrame()
        bg_frame.setProperty("class", "android-card")
        layout = QVBoxLayout(bg_frame)
        main_layout.addWidget(bg_frame)

        # Custom Title
        title_lbl = QLabel("Guardar Fórmula")
        title_lbl.setProperty("class", "h2")
        title_lbl.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(title_lbl)

        # 1. Rendered Latex instead of raw text
        self.render_widget = QLabel()
        self.render_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.render_widget.setMinimumHeight(60)
        self.render_widget.setStyleSheet("border: none; background: transparent;")

        p = self.parent()
        t = get_theme_dict(
            p.current_theme if p and hasattr(p, "current_theme") else "dark"
        )
        math_fg = t.get("text_rendered_math", t["text_primary"])

        pixmap = SVGMathCache.get_instance().get_svg_icon(
            self.latex_str, math_fg, width=320, height=60
        )
        self.render_widget.setPixmap(pixmap)
        layout.addWidget(self.render_widget)

        form = QFormLayout()

        # 1. Rama (Branch)
        self.branch_combo = QComboBox()
        self.branch_combo.addItems(["Matemáticas", "Física"])
        form.addRow("Rama:", self.branch_combo)

        # 2. Categoría
        self.cat_combo = QComboBox()
        self.cat_custom = QLineEdit()
        self.cat_custom.setPlaceholderText("Nueva categoría")
        self.cat_custom.setVisible(False)
        form.addRow("Categoría:", self.cat_combo)
        form.addRow("", self.cat_custom)

        # 3. Descripción
        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText(
            "Ej. Ecuación de onda para mecánica cuántica"
        )
        form.addRow("Descripción:", self.desc_input)

        # 4. Subcategoría (Opcional)
        self.subcat_checkbox = QCheckBox("Añadir subcategoría")
        form.addRow("", self.subcat_checkbox)

        self.subcat_combo = QComboBox()
        self.subcat_custom = QLineEdit()
        self.subcat_custom.setPlaceholderText("Nueva subcategoría")
        self.subcat_combo.setVisible(False)
        self.subcat_custom.setVisible(False)

        self.subcat_label = QLabel("Subcategoría:")
        self.subcat_label.setVisible(False)
        form.addRow(self.subcat_label, self.subcat_combo)
        form.addRow("", self.subcat_custom)

        # 5. Nombre
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Ej. Ecuación de Schrödinger")
        form.addRow("Nombre:", self.name_input)

        # Conexiones
        self.branch_combo.currentTextChanged.connect(self._update_cats)
        self.cat_combo.currentTextChanged.connect(self._update_subcats)
        self.subcat_combo.currentTextChanged.connect(self._update_subcat_visibility)
        self.subcat_checkbox.toggled.connect(self._toggle_subcat)

        self._update_cats(self.branch_combo.currentText())

        layout.addLayout(form)

        self.btns = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.btns.accepted.connect(self.accept)
        self.btns.rejected.connect(self.reject)
        layout.addWidget(self.btns)

    def _toggle_subcat(self, checked: bool) -> None:
        """Alterna la visibilidad de los controles de subcategoría."""
        self.subcat_label.setVisible(checked)
        self.subcat_combo.setVisible(checked)
        if checked:
            self._update_subcats(self.cat_combo.currentText())
        else:
            self.subcat_custom.setVisible(False)

    def _update_cats(self, branch: str) -> None:
        """Actualiza la lista de categorías disponibles según la rama seleccionada."""
        self.cat_combo.clear()

        domain_target = "math" if branch == "Matemáticas" else "physics"
        preset_cats = [
            re.sub(r"^\d+\.\s*", "", c["name"])
            for c in PRESET_CATEGORIES
            if c.get("domain") == domain_target
        ]

        user_cats = [c["category"] for c in self.manager.categories]

        all_cats: list[str] = []
        for c in preset_cats + user_cats:
            if c not in all_cats:
                all_cats.append(c)

        self.cat_combo.addItems(all_cats)
        self.cat_combo.addItem("Nueva categoría...")

    def _update_subcats(self, cat_name: str) -> None:
        """Actualiza la lista de subcategorías según la categoría seleccionada."""
        if cat_name == "Nueva categoría...":
            self.cat_custom.setVisible(True)
            if self.subcat_checkbox.isChecked():
                self.subcat_combo.clear()
                self.subcat_combo.addItem("Nueva categoría...")
            return

        self.cat_custom.setVisible(False)

        if not self.subcat_checkbox.isChecked():
            return

        self.subcat_combo.clear()

        cat_obj = next(
            (c for c in self.manager.categories if c["category"] == cat_name), None
        )
        if cat_obj:
            subcats = [s["name"] for s in cat_obj["subcategories"]]
            self.subcat_combo.addItems(subcats)

        self.subcat_combo.addItem("Nueva categoría...")

    def _update_subcat_visibility(self, subcat_name: str) -> None:
        """Gestiona la visibilidad del campo de subcategoría personalizada."""
        if not self.subcat_checkbox.isChecked():
            self.subcat_custom.setVisible(False)
            return

        if subcat_name == "Nueva categoría...":
            self.subcat_custom.setVisible(True)
        else:
            self.subcat_custom.setVisible(False)

    def get_data(self) -> dict[str, str]:
        """Extrae los campos completados por el usuario para su almacenamiento.

        Returns:
            Diccionario con nombre, descripción, categoría y subcategoría.
        """
        cat = self.cat_combo.currentText()
        if cat == "Nueva categoría...":
            cat = self.cat_custom.text().strip()

        if self.subcat_checkbox.isChecked():
            subcat = self.subcat_combo.currentText()
            if subcat == "Nueva categoría...":
                subcat = self.subcat_custom.text().strip()
        else:
            subcat = "General"

        return {
            "name": self.name_input.text().strip() or "Fórmula sin nombre",
            "description": self.desc_input.text().strip(),
            "category": cat or "General",
            "subcategory": subcat or "General",
        }
