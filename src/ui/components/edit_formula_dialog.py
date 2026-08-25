"""
---
file: src/ui/components/edit_formula_dialog.py
module: src.ui.components.edit_formula_dialog
description: Cuadro de diálogo modal avanzado para editar fórmulas de usuario y gestionar variantes paso a paso.
type: ui/dialog
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.data.symbols
  - src.ui.theme
  - src.ui.components.svg_cache
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/palette_widget.py
exports:
  - EditFormulaDialog: "Diálogo modal para editar metadatos, ramas, categorías y variantes de fórmulas"
test: pytest tests/test_editor_widget.py
constraints:
  - "Mantener la sincronización de ramas/categorías y el aislamiento de datos temporales"
keywords:
  - edit-formula-dialog
  - modal-dialog
  - formula-variations
  - category-management
  - user-formulas
---

Dialog window to edit user-defined formulas and manage multi-step procedural variations.
"""

from __future__ import annotations

import copy
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
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from src.data.symbols import PRESET_CATEGORIES
from src.ui.components.svg_cache import SVGMathCache
from src.ui.theme import get_theme_dict, get_theme_qss


class EditFormulaDialog(QDialog):
    """Cuadro de diálogo modal para edición de fórmulas y gestión de variantes.

    Args:
        formula_name: Nombre principal de la fórmula.
        formula_latex: Expresión en código LaTeX.
        manager: Instancia de UserFormulasManager para persistencia.
        cat_name: Nombre de la categoría contenedora.
        subcat_name: Nombre de la subcategoría contenedora.
        formula_desc: Descripción o contexto de la ecuación.
        variations: Lista opcional de variantes agrupadas.
        parent: Widget contenedor padre.
    """

    def __init__(
        self,
        formula_name: str,
        formula_latex: str,
        manager: Any,
        cat_name: str,
        subcat_name: str,
        formula_desc: str = "",
        variations: list[dict[str, str]] | None = None,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle("Editar Fórmula")
        self.setMinimumWidth(440)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)

        # Apply Theme
        if parent and hasattr(parent, "current_theme"):
            self.setStyleSheet(get_theme_qss(parent.current_theme))

        self.formula_name = formula_name
        self.formula_latex = formula_latex
        self.formula_desc = formula_desc
        self.manager = manager
        self.cat_name = cat_name
        self.subcat_name = subcat_name

        # Inicializar lista de variantes
        if variations and len(variations) > 0:
            self.variations: list[dict[str, str]] = copy.deepcopy(variations)
        else:
            self.variations = [{"name": formula_name, "latex": formula_latex}]

        self.current_var_index: int = 0

        self._setup_ui()

    def _setup_ui(self) -> None:
        """Construye los controles y diseño del diálogo."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        bg_frame = QFrame()
        bg_frame.setProperty("class", "android-card")
        layout = QVBoxLayout(bg_frame)
        main_layout.addWidget(bg_frame)

        title_lbl = QLabel("Editar Fórmula")
        title_lbl.setProperty("class", "h2")
        title_lbl.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(title_lbl)

        p = self.parent()
        self.current_theme = (
            p.current_theme if p and hasattr(p, "current_theme") else "dark"
        )
        t = get_theme_dict(self.current_theme)

        # 1. Rendered Latex (para previsualizar la variante activa)
        self.render_widget = QLabel()
        self.render_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.render_widget.setMinimumHeight(60)
        self.render_widget.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(self.render_widget)

        form = QFormLayout()

        # Determinar rama inicial si pertenece a las preestablecidas
        initial_branch = "Matemáticas"
        for c in PRESET_CATEGORIES:
            cat_clean = re.sub(r"^\d+\.\s*", "", c["name"])
            if self.cat_name == c["name"] or self.cat_name == cat_clean:
                initial_branch = (
                    "Matemáticas" if c.get("domain") == "math" else "Física"
                )
                self.cat_name = cat_clean
                break

        # 1. Rama (Branch)
        self.branch_combo = QComboBox()
        self.branch_combo.addItems(["Matemáticas", "Física"])
        self.branch_combo.setCurrentText(initial_branch)
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
        self.desc_input.setText(self.formula_desc)
        self.desc_input.setPlaceholderText(
            "Ej. Ecuación de onda para mecánica cuántica"
        )
        form.addRow("Descripción:", self.desc_input)

        # 4. Subcategoría (Opcional)
        self.subcat_checkbox = QCheckBox("Añadir subcategoría")
        is_subcat = bool(self.subcat_name and self.subcat_name != "General")
        self.subcat_checkbox.setChecked(is_subcat)
        form.addRow("", self.subcat_checkbox)

        self.subcat_combo = QComboBox()
        self.subcat_custom = QLineEdit()
        self.subcat_custom.setPlaceholderText("Nueva subcategoría")
        self.subcat_combo.setVisible(is_subcat)
        self.subcat_custom.setVisible(False)

        self.subcat_label = QLabel("Subcategoría:")
        self.subcat_label.setVisible(is_subcat)
        form.addRow(self.subcat_label, self.subcat_combo)
        form.addRow("", self.subcat_custom)

        # 5. Nombre Principal
        self.name_input = QLineEdit()
        self.name_input.setText(self.formula_name)
        self.name_input.setPlaceholderText("Ej. Ecuación de Schrödinger")
        form.addRow("Nombre:", self.name_input)
        self.name_input.textChanged.connect(self._on_main_name_changed)

        layout.addLayout(form)

        # 6. Sección de Variantes de la fórmula
        var_frame = QFrame()
        var_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {t.get("surface", "#1E1E1E")};
                border: 1px solid {t.get("border", "#333333")};
                border-radius: 8px;
                padding: 6px;
                margin-top: 4px;
            }}
        """)
        var_layout = QVBoxLayout(var_frame)
        var_layout.setContentsMargins(6, 6, 6, 6)
        var_layout.setSpacing(6)

        # Barra superior de variantes (Controles de carrusel y agregar/eliminar)
        var_header = QHBoxLayout()
        var_header.setContentsMargins(0, 0, 0, 0)

        lbl_var_section = QLabel("Variantes:")
        lbl_var_section.setStyleSheet(
            f"font-weight: bold; color: {t.get('primary', '#00E5FF')}; border: none;"
        )
        var_header.addWidget(lbl_var_section)

        btn_style = f"""
            QPushButton {{
                background-color: {t.get("surface_variant", "#2A2A2A")};
                color: {t["text_primary"]};
                border: 1px solid {t["border"]};
                border-radius: 4px;
                padding: 3px 8px;
                font-weight: bold;
                font-size: 11px;
            }}
            QPushButton:hover {{
                border-color: {t.get("primary", "#00E5FF")};
                color: {t.get("primary", "#00E5FF")};
            }}
            QPushButton:disabled {{
                color: {t.get("text_secondary", "#666666")};
                border-color: transparent;
            }}
        """

        self.btn_prev_var = QPushButton("<")
        self.btn_prev_var.setStyleSheet(btn_style)
        self.btn_prev_var.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_prev_var.clicked.connect(self._prev_variant)
        var_header.addWidget(self.btn_prev_var)

        self.lbl_var_counter = QLabel("Variante 1 / 1")
        self.lbl_var_counter.setStyleSheet(
            f"font-size: 11px; font-weight: bold; color: {t['text_secondary']}; border: none;"
        )
        var_header.addWidget(self.lbl_var_counter)

        self.btn_next_var = QPushButton(">")
        self.btn_next_var.setStyleSheet(btn_style)
        self.btn_next_var.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_next_var.clicked.connect(self._next_variant)
        var_header.addWidget(self.btn_next_var)

        var_header.addStretch()

        self.btn_add_var = QPushButton("➕ Agregar Variante")
        self.btn_add_var.setStyleSheet(btn_style)
        self.btn_add_var.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_add_var.clicked.connect(self._add_variant)
        var_header.addWidget(self.btn_add_var)

        self.btn_del_var = QPushButton("🗑️ Eliminar")
        self.btn_del_var.setStyleSheet(btn_style)
        self.btn_del_var.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_del_var.clicked.connect(self._del_variant)
        var_header.addWidget(self.btn_del_var)

        var_layout.addLayout(var_header)

        # Campos de la variante activa
        var_form = QFormLayout()
        var_form.setContentsMargins(0, 4, 0, 0)

        self.custom_var_name_chk = QCheckBox("Personalizar nombre de esta variante")
        self.custom_var_name_chk.toggled.connect(self._on_custom_var_name_toggled)
        var_form.addRow("", self.custom_var_name_chk)

        self.var_name_label = QLabel("Nombre variante:")
        self.var_name_input = QLineEdit()
        self.var_name_input.setPlaceholderText("Ej. Forma simplificada / despeje")
        self.var_name_input.textChanged.connect(self._on_var_name_changed)
        var_form.addRow(self.var_name_label, self.var_name_input)

        self.latex_input = QLineEdit()
        self.latex_input.setPlaceholderText("Código LaTeX de esta variante")
        self.latex_input.textChanged.connect(self._on_latex_changed)
        var_form.addRow("LaTeX:", self.latex_input)

        var_layout.addLayout(var_form)
        layout.addWidget(var_frame)

        # Conexiones
        self.branch_combo.currentTextChanged.connect(self._update_cats)
        self.cat_combo.currentTextChanged.connect(self._update_subcats)
        self.subcat_combo.currentTextChanged.connect(self._update_subcat_visibility)
        self.subcat_checkbox.toggled.connect(self._toggle_subcat)

        self._update_cats(self.branch_combo.currentText())

        # Configurar categoría inicial
        if self.cat_name:
            idx = self.cat_combo.findText(self.cat_name)
            if idx >= 0:
                self.cat_combo.setCurrentIndex(idx)
            else:
                self.cat_combo.setCurrentText("Nueva categoría...")
                self.cat_custom.setText(self.cat_name)

        # Configurar subcategoría inicial
        if is_subcat:
            idx = self.subcat_combo.findText(self.subcat_name)
            if idx >= 0:
                self.subcat_combo.setCurrentIndex(idx)
            else:
                self.subcat_combo.setCurrentText("Nueva categoría...")
                self.subcat_custom.setText(self.subcat_name)

        # Cargar datos de la variante inicial
        self._load_variant_data()

        self.btns = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.btns.accepted.connect(self.accept)
        self.btns.rejected.connect(self.reject)
        layout.addWidget(self.btns)

    def _load_variant_data(self) -> None:
        """Carga y visualiza los datos de la variante activa actual."""
        if not self.variations:
            return

        self.current_var_index = max(
            0, min(self.current_var_index, len(self.variations) - 1)
        )
        var = self.variations[self.current_var_index]

        total = len(self.variations)
        self.lbl_var_counter.setText(f"Variante {self.current_var_index + 1} / {total}")
        self.btn_del_var.setEnabled(total > 1)
        self.btn_prev_var.setEnabled(total > 1)
        self.btn_next_var.setEnabled(total > 1)

        self.latex_input.blockSignals(True)
        self.latex_input.setText(var.get("latex", ""))
        self.latex_input.blockSignals(False)

        main_name = self.name_input.text().strip()
        var_name = var.get("name", "")

        has_custom_name = bool(var_name and var_name != main_name)

        self.custom_var_name_chk.blockSignals(True)
        self.custom_var_name_chk.setChecked(has_custom_name)
        self.custom_var_name_chk.blockSignals(False)

        self.var_name_input.blockSignals(True)
        self.var_name_input.setText(var_name if has_custom_name else "")
        self.var_name_input.setVisible(has_custom_name)
        self.var_name_label.setVisible(has_custom_name)
        self.var_name_input.blockSignals(False)

        self._update_preview(var.get("latex", ""))

    def _prev_variant(self) -> None:
        """Navega a la variante anterior."""
        if len(self.variations) > 1:
            self.current_var_index = (self.current_var_index - 1) % len(self.variations)
            self._load_variant_data()

    def _next_variant(self) -> None:
        """Navega a la variante siguiente."""
        if len(self.variations) > 1:
            self.current_var_index = (self.current_var_index + 1) % len(self.variations)
            self._load_variant_data()

    def _add_variant(self) -> None:
        """Añade una nueva variante al carrusel."""
        main_name = self.name_input.text().strip() or "Variante"
        new_var = {"name": main_name, "latex": ""}
        self.variations.append(new_var)
        self.current_var_index = len(self.variations) - 1
        self._load_variant_data()

    def _del_variant(self) -> None:
        """Elimina la variante activa actual."""
        if len(self.variations) > 1:
            self.variations.pop(self.current_var_index)
            self.current_var_index = max(0, self.current_var_index - 1)
            self._load_variant_data()

    def _on_custom_var_name_toggled(self, checked: bool) -> None:
        """Manejador de la casilla de nombre personalizado de variante."""
        self.var_name_label.setVisible(checked)
        self.var_name_input.setVisible(checked)
        if checked:
            custom_name = (
                self.var_name_input.text().strip() or self.name_input.text().strip()
            )
            self.variations[self.current_var_index]["name"] = custom_name
        else:
            self.variations[self.current_var_index]["name"] = (
                self.name_input.text().strip()
            )

    def _on_var_name_changed(self, text: str) -> None:
        """Manejador del cambio de texto en el nombre de la variante."""
        if self.custom_var_name_chk.isChecked():
            self.variations[self.current_var_index]["name"] = (
                text.strip() or self.name_input.text().strip()
            )

    def _on_latex_changed(self, text: str) -> None:
        """Manejador del cambio de código LaTeX de la variante activa."""
        self.variations[self.current_var_index]["latex"] = text
        self._update_preview(text)

    def _on_main_name_changed(self, text: str) -> None:
        """Manejador del cambio en el nombre principal de la fórmula."""
        if not self.custom_var_name_chk.isChecked():
            self.variations[self.current_var_index]["name"] = text.strip()

    def _update_preview(self, text: str) -> None:
        """Actualiza la previsualización gráfica de la fórmula en tiempo real."""
        t = get_theme_dict(self.current_theme)
        math_fg = t.get("text_rendered_math", t["text_primary"])
        pixmap = SVGMathCache.get_instance().get_svg_icon(
            text or " ", math_fg, width=320, height=60
        )
        self.render_widget.setPixmap(pixmap)

    def _toggle_subcat(self, checked: bool) -> None:
        """Alterna la visibilidad de los controles de subcategoría."""
        self.subcat_label.setVisible(checked)
        self.subcat_combo.setVisible(checked)
        if checked:
            self._update_subcats(self.cat_combo.currentText())
        else:
            self.subcat_custom.setVisible(False)

    def _update_cats(self, branch: str) -> None:
        """Actualiza las categorías desplegables según la rama seleccionada."""
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
        """Actualiza las subcategorías según la categoría seleccionada."""
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

    def get_data(self) -> dict[str, Any]:
        """Obtiene la estructura de datos completa con la fórmula y variantes.

        Returns:
            Diccionario estructurado con nombre, descripción, categoría, subcategoría y variantes.
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

        main_name = self.name_input.text().strip() or "Fórmula sin nombre"

        clean_variations: list[dict[str, str]] = []
        for v in self.variations:
            v_name = v.get("name", "").strip() or main_name
            v_latex = v.get("latex", "").strip()
            clean_variations.append({"name": v_name, "latex": v_latex})

        first_latex = clean_variations[0]["latex"] if clean_variations else ""

        return {
            "name": main_name,
            "description": self.desc_input.text().strip(),
            "latex": first_latex,
            "category": cat or "General",
            "subcategory": subcat or "General",
            "variations": clean_variations,
        }
