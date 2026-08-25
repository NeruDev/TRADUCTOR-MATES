"""
---
file: src/ui/components/palette_widget.py
module: src.ui.components.palette_widget
description: Paleta de símbolos, plantillas y formulario interactivo con buscador integrado (QLineEdit).
type: ui/component
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
  - src.data.symbols
  - src.ui.theme
  - src.ui.components.procedure_card
  - src.ui.components.svg_cache
  - src.ui.components.template_card
  - src.utils.favorites_manager
  - src.utils.qt_utils
relations:
  - docs/ARCHITECTURE.md
  - src/ui/main_window.py
exports:
  - MathPaletteWidget: "Paleta central de símbolos, plantillas estructuradas y compendio de fórmulas"
test: pytest tests/test_editor_widget.py
constraints:
  - "Filtrar en tiempo real con buscador QLineEdit sin congelar la interfaz de usuario"
keywords:
  - palette-widget
  - symbol-palette
  - formula-compendium
  - search-filter
  - favorites
---

Symbol and Structured Template Palette Widget.
Provides flyout category buttons and dotted box cards.
"""

from __future__ import annotations

from collections.abc import Callable
from functools import partial
from typing import Any

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QAction, QColor, QIcon, QPainter, QPixmap
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenu,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from src.core.logger import get_logger
from src.data.constants import CONSTANTS
from src.data.symbols import (
    CATEGORIES,
    PRESET_CATEGORIES,
    PRESET_FORMULAS,
    SYMBOLS,
    TEMPLATES,
    _parse_preset,
)
from src.data.units import UNITS
from src.ui.components.constant_card import ConstantCardWidget
from src.ui.components.procedure_card import ProcedureCardWidget
from src.ui.components.template_card import TemplateCardOption
from src.ui.components.unit_card import UnitCardWidget
from src.ui.theme import COLOR_MIKU_CYAN, get_theme_dict
from src.utils.favorites_manager import FavoritesManager
from src.utils.qt_utils import clear_layout


class MathPaletteWidget(QFrame):
    """Paleta de inserción gráfica (Cinta de opciones / Ribbon)."""

    template_selected = Signal(object)
    symbol_selected = Signal(object)
    preset_selected = Signal(int)
    latex_selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "android-card")
        self.current_theme = "dark"

        self.fav_manager = FavoritesManager()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(12, 10, 12, 10)
        main_layout.setSpacing(8)

        # Header (Descriptive title)
        self.header_lbl = QLabel("Catálogo de Fórmulas y Símbolos")
        main_layout.addWidget(self.header_lbl)

        # Search Bar
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar fórmulas, símbolos, plantillas...")
        self.search_input.textChanged.connect(self._apply_search_filter)
        self.search_input.setClearButtonEnabled(True)
        main_layout.addWidget(self.search_input)

        # Bottom Panel: Tabs
        self.tabs = QTabWidget()
        self.tabs.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )

        # We will create tab_user later

        # Tab 1: Favorites
        self.tab_favorites = self._create_scroll_tab()
        fav_widget = QWidget()
        self.fav_layout = QVBoxLayout(fav_widget)
        self.fav_layout.setContentsMargins(8, 8, 8, 8)
        self.fav_grid = QGridLayout()
        self.fav_grid.setSpacing(8)
        self.fav_layout.addLayout(self.fav_grid)
        self.fav_layout.addStretch()
        self.tab_favorites.setWidget(fav_widget)
        self.tabs.addTab(self.tab_favorites, "⭐ Favoritos")

        # Tab: Plantillas
        self.tab_templates = self._create_scroll_tab()
        tpl_widget = QWidget()
        self.tpl_layout = QVBoxLayout(tpl_widget)
        self.tpl_layout.setContentsMargins(8, 8, 8, 8)
        self.tpl_layout.setSpacing(6)
        self.tpl_layout.addStretch()
        self.tab_templates.setWidget(tpl_widget)
        self.tabs.addTab(self.tab_templates, "🧩 Plantillas")

        # Tab: Símbolos
        self.tab_symbols = self._create_scroll_tab()
        sym_widget = QWidget()
        self.sym_layout = QVBoxLayout(sym_widget)
        self.sym_layout.setContentsMargins(8, 8, 8, 8)
        self.sym_layout.setSpacing(6)
        self.sym_layout.addStretch()
        self.tab_symbols.setWidget(sym_widget)
        self.tabs.addTab(self.tab_symbols, "🔣 Símbolos")

        # Tab: Constantes
        self.tab_constants = self._create_scroll_tab()
        const_widget = QWidget()
        self.const_layout = QVBoxLayout(const_widget)
        self.const_layout.setContentsMargins(8, 8, 8, 8)
        self.const_layout.setSpacing(6)
        self.const_layout.addStretch()
        self.tab_constants.setWidget(const_widget)
        self.tabs.addTab(self.tab_constants, "♾️ Constantes")

        # Tab: Unidades
        self.tab_units = self._create_scroll_tab()
        unit_widget = QWidget()
        self.unit_layout = QVBoxLayout(unit_widget)
        self.unit_layout.setContentsMargins(8, 8, 8, 8)
        self.unit_layout.setSpacing(6)
        self.unit_layout.addStretch()
        self.tab_units.setWidget(unit_widget)
        self.tabs.addTab(self.tab_units, "📏 Unidades")

        # Tabs 2,3,4: Niveles (Básico, Intermedio, Avanzado)
        self.current_domain = "math"
        self.current_level = "BÁSICO"
        self.level_layouts = {}

        # We also create tab_user right here since we skipped it earlier
        self.tab_user = self._create_scroll_tab()
        self.tabs.addTab(self.tab_user, "👤 Usuario")

        def _create_circle_icon(color_hex: str, size: int = 12) -> QIcon:
            pixmap = QPixmap(size, size)
            pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter(pixmap)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setBrush(QColor(color_hex))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(1, 1, size - 2, size - 2)
            painter.end()
            return QIcon(pixmap)

        levels = [
            ("BÁSICO", "Básico", "#4CAF50"),
            ("INTERMEDIO", "Intermedio", "#AB47BC"),
            ("UNIVERSITARIO / AVANZADO", "Avanzado", "#EF5350"),
        ]

        # Tab: Formulario
        tab_formulario = QWidget()
        form_layout = QHBoxLayout(tab_formulario)
        form_layout.setContentsMargins(4, 6, 4, 6)
        form_layout.setSpacing(6)

        # Sidebar
        subtab_container = QWidget()
        subtab_layout = QVBoxLayout(subtab_container)
        subtab_layout.setContentsMargins(0, 0, 0, 0)
        subtab_layout.setSpacing(6)

        self.btn_math = QPushButton("📐 Matemáticas")
        self.btn_math.setCheckable(True)
        self.btn_math.setChecked(True)
        self.btn_math.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_math.clicked.connect(
            lambda: self._set_domain_and_level("math", self.current_level)
        )

        self.math_levels_widget = QWidget()
        math_levels_layout = QVBoxLayout(self.math_levels_widget)
        math_levels_layout.setContentsMargins(16, 0, 0, 0)
        math_levels_layout.setSpacing(4)

        self.btn_phys = QPushButton("⚛️ Física")
        self.btn_phys.setCheckable(True)
        self.btn_phys.setChecked(False)
        self.btn_phys.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_phys.clicked.connect(
            lambda: self._set_domain_and_level("physics", self.current_level)
        )

        self.phys_levels_widget = QWidget()
        phys_levels_layout = QVBoxLayout(self.phys_levels_widget)
        phys_levels_layout.setContentsMargins(16, 0, 0, 0)
        phys_levels_layout.setSpacing(4)

        self.level_btns_math = []
        self.level_btns_phys = []

        for level_id, level_name, level_color in levels:
            btn_m = QPushButton(f" {level_name}")
            btn_m.setIcon(_create_circle_icon(level_color, 12))
            btn_m.setIconSize(QSize(10, 10))
            btn_m.setCheckable(True)
            btn_m.setCursor(Qt.CursorShape.PointingHandCursor)
            if level_id == "BÁSICO":
                btn_m.setChecked(True)
            btn_m.clicked.connect(
                lambda _, d="math", l=level_id: self._set_domain_and_level(d, l)
            )
            math_levels_layout.addWidget(btn_m)
            self.level_btns_math.append((level_id, btn_m))

            btn_p = QPushButton(f" {level_name}")
            btn_p.setIcon(_create_circle_icon(level_color, 12))
            btn_p.setIconSize(QSize(10, 10))
            btn_p.setCheckable(True)
            btn_p.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_p.clicked.connect(
                lambda _, d="physics", l=level_id: self._set_domain_and_level(d, l)
            )
            phys_levels_layout.addWidget(btn_p)
            self.level_btns_phys.append((level_id, btn_p))

        self.phys_levels_widget.setVisible(False)

        subtab_layout.addWidget(self.btn_math)
        subtab_layout.addWidget(self.math_levels_widget)
        subtab_layout.addWidget(self.btn_phys)
        subtab_layout.addWidget(self.phys_levels_widget)
        subtab_layout.addStretch()
        form_layout.addWidget(subtab_container)

        # Right side scroll
        self.formulario_scroll = self._create_scroll_tab()
        self.formulario_widget = QWidget()
        self.formulario_content_layout = QVBoxLayout(self.formulario_widget)
        self.formulario_content_layout.setContentsMargins(4, 4, 4, 4)
        self.formulario_content_layout.setSpacing(6)
        self.formulario_content_layout.addStretch()
        self.formulario_scroll.setWidget(self.formulario_widget)

        form_layout.addWidget(self.formulario_scroll, stretch=1)
        self.tabs.addTab(tab_formulario, "📚 Formulario")

        main_layout.addWidget(self.tabs)

        self._update_theme_ui()

        from PySide6.QtCore import QTimer

        QTimer.singleShot(0, self._load_favorites_grid)
        QTimer.singleShot(20, self._build_templates_grid)
        QTimer.singleShot(30, self._build_symbols_grid)
        QTimer.singleShot(40, self._build_constants_grid)
        QTimer.singleShot(50, self._build_units_grid)
        QTimer.singleShot(50, self._build_examples_grid)

        self.tabs.setCurrentIndex(0)

    def _set_domain_and_level(self, domain: str, level: str):
        self.current_domain = domain
        self.current_level = level

        self.btn_math.setChecked(domain == "math")
        self.btn_phys.setChecked(domain == "physics")

        self.math_levels_widget.setVisible(domain == "math")
        self.phys_levels_widget.setVisible(domain == "physics")

        for lvl_id, btn in self.level_btns_math:
            btn.setChecked(domain == "math" and lvl_id == level)

        for lvl_id, btn in self.level_btns_phys:
            btn.setChecked(domain == "physics" and lvl_id == level)

        self._update_subtab_style()
        self._build_examples_grid()
        if hasattr(self, "search_input"):
            self._apply_search_filter(self.search_input.text())

    def _update_subtab_style(self):
        t = get_theme_dict(self.current_theme)
        card_bg = t.get("surface_variant", "#202030")
        card_fg = t.get("text_secondary", "#9E9EB3")
        border_col = t.get("border", "#32324A")
        primary_col = t.get("primary", COLOR_MIKU_CYAN)

        subtab_css = f"""
            QPushButton {{
                background-color: {card_bg};
                color: {card_fg};
                border: 1px solid {border_col};
                border-radius: 8px;
                padding: 6px 10px;
                font-size: 11px;
                font-weight: bold;
                text-align: left;
            }}
            QPushButton:checked {{
                background-color: {primary_col};
                color: #FFFFFF;
                border: 1px solid {primary_col};
            }}
            QPushButton:hover:!checked {{
                background-color: {t.get("surface", "#2A2A3A")};
                border: 1px solid {primary_col};
            }}
        """
        self.btn_math.setStyleSheet(subtab_css)
        self.btn_phys.setStyleSheet(subtab_css)

        for _, btn in self.level_btns_math:
            btn.setStyleSheet(subtab_css)

        for _, btn in self.level_btns_phys:
            btn.setStyleSheet(subtab_css)

    def _create_scroll_tab(self) -> QScrollArea:
        area = QScrollArea()
        area.setWidgetResizable(True)
        area.setStyleSheet("background-color: transparent; border: none;")
        return area

    def _update_theme_ui(self):
        t = get_theme_dict(self.current_theme)
        self.header_lbl.setStyleSheet(
            f"font-size: 13px; font-weight: bold; color: {t['text_primary']};"
        )

        self.tabs.setStyleSheet(f"""
            QTabWidget::pane {{
                border: 1px solid {t["border"]};
                border-radius: 8px;
                background-color: {t["surface"]};
            }}
            QTabBar::tab {{
                background: {t["surface_variant"]};
                color: {t["text_secondary"]};
                border: 1px solid {t["border"]};
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                padding: 6px 14px;
                font-size: 12px;
                font-weight: 600;
                margin-right: 4px;
            }}
            QTabBar::tab:hover {{
                color: {t["primary"]};
                border-color: {t["primary"]};
                background: {t.get("bg_item_card_hover", t["surface"])};
            }}
            QTabBar::tab:selected {{
                background: {t["primary"]};
                border: 1px solid {t["primary"]};
                color: #FFFFFF;
                font-weight: bold;
            }}
        """)

        self.search_input.setStyleSheet(f"""
            QLineEdit {{
                background-color: {t["surface"]};
                color: {t["text_primary"]};
                border: 1px solid {t["border"]};
                border-radius: 8px;
                padding: 6px 12px;
                font-size: 13px;
            }}
            QLineEdit:focus {{
                border: 1px solid {t["primary"]};
            }}
        """)

        self._update_subtab_style()

        # Color specific tabs
        # Tab 2: Básico (Cyan)
        self.tabs.tabBar().setTabTextColor(
            3,
            Qt.GlobalColor.darkCyan
            if self.current_theme == "light"
            else Qt.GlobalColor.cyan,
        )
        # Tab 3: Intermedio (Lavender / Purple)
        self.tabs.tabBar().setTabTextColor(
            4,
            Qt.GlobalColor.darkMagenta
            if self.current_theme == "light"
            else Qt.GlobalColor.magenta,
        )
        # Tab 4: Avanzado (Magenta / Red)
        self.tabs.tabBar().setTabTextColor(
            5,
            Qt.GlobalColor.darkRed
            if self.current_theme == "light"
            else Qt.GlobalColor.red,
        )

    def update_theme(self, theme_name: str):
        self.current_theme = theme_name
        self._update_theme_ui()
        self._load_favorites_grid()
        self._build_templates_grid()
        self._build_symbols_grid()
        self._build_constants_grid()
        self._build_units_grid()
        self._build_examples_grid()
        if hasattr(self, "search_input"):
            self._apply_search_filter(self.search_input.text())

    def _toggle_favorite(self, item_id: str):
        self.fav_manager.toggle(item_id)
        self._load_favorites_grid()
        self._build_templates_grid()
        self._build_symbols_grid()
        if hasattr(self, "search_input"):
            self._apply_search_filter(self.search_input.text())

    def _show_context_menu(self, pos, btn, item_id: str, is_fav: bool):
        menu = QMenu(self)
        t = get_theme_dict(self.current_theme)
        menu.setStyleSheet(f"""
            QMenu {{
                background-color: {t["surface"]};
                color: {t["text_primary"]};
                border: 1px solid {t["border"]};
                border-radius: 8px;
                padding: 4px;
            }}
            QMenu::item {{
                padding: 6px 14px;
                border-radius: 4px;
                color: {t["text_primary"]};
            }}
            QMenu::item:selected {{
                background-color: {t["primary"]};
                color: #FFFFFF;
            }}
        """)
        action_text = "❌ Quitar de Favoritos" if is_fav else "⭐ Agregar a Favoritos"
        action = QAction(action_text, self)
        action.triggered.connect(lambda: self._toggle_favorite(item_id))
        menu.addAction(action)
        menu.exec_(btn.mapToGlobal(pos))

    def _show_user_formula_context_menu(
        self,
        pos,
        btn,
        formula: dict,
        manager,
        is_fav: bool,
        cat_name: str = "",
        subcat_name: str = "",
    ):
        menu = QMenu(self)
        t = get_theme_dict(self.current_theme)
        menu.setStyleSheet(f"""
            QMenu {{
                background-color: {t["surface"]};
                color: {t["text_primary"]};
                border: 1px solid {t["border"]};
                border-radius: 8px;
                padding: 4px;
            }}
            QMenu::item {{
                padding: 6px 14px;
                border-radius: 4px;
                color: {t["text_primary"]};
            }}
            QMenu::item:selected {{
                background-color: {t["primary"]};
                color: #FFFFFF;
            }}
        """)

        # Add to favorites
        action_fav_text = (
            "❌ Quitar de Favoritos" if is_fav else "⭐ Agregar a Favoritos"
        )
        action_fav = QAction(action_fav_text, self)
        action_fav.triggered.connect(lambda: self._toggle_favorite(formula["id"]))
        menu.addAction(action_fav)

        # Edit formula
        action_edit = QAction("✏️ Editar Fórmula", self)
        action_edit.triggered.connect(
            lambda: self._edit_user_formula(manager, formula, cat_name, subcat_name)
        )
        menu.addAction(action_edit)

        # Delete formula
        action_del = QAction("❌ Eliminar Fórmula", self)
        action_del.triggered.connect(
            lambda: self._delete_user_formula(manager, formula["id"])
        )
        menu.addAction(action_del)

        menu.exec_(btn.mapToGlobal(pos))

    def _edit_user_formula(
        self, manager, formula: dict, cat_name: str, subcat_name: str
    ):
        from src.ui.components.edit_formula_dialog import EditFormulaDialog

        dialog = EditFormulaDialog(
            formula["name"],
            formula["latex"],
            manager,
            cat_name,
            subcat_name,
            formula.get("description", ""),
            formula.get("variations", []),
            self,
        )
        if dialog.exec_():
            data = dialog.get_data()
            manager.update_formula(
                formula["id"],
                data["category"],
                data["subcategory"],
                data["name"],
                data["latex"],
                data.get("description", ""),
                data.get("variations", []),
            )
            self.rebuild_user_tab(manager)

    def _build_examples_grid(self):
        # Clear layout
        while self.formulario_content_layout.count() > 1:
            item = self.formulario_content_layout.takeAt(0)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        t = get_theme_dict(self.current_theme)
        card_hover = t.get("bg_item_card_hover", t["surface"])
        border_col = t.get("border_subtle", t["border"])
        primary_col = t.get("primary", COLOR_MIKU_CYAN)

        target_categories = [
            cat
            for cat in PRESET_CATEGORIES
            if cat.get("domain", "math") == self.current_domain
        ]

        for cat in target_categories:
            matching = [pf for pf in PRESET_FORMULAS if pf.get("category") == cat["id"]]
            if not matching:
                continue

            # Filter for current level
            pfs = []
            for pf in matching:
                lvl = pf.get("level", "BÁSICO")
                if "BÁSICO" in lvl.upper():
                    lvl_key = "BÁSICO"
                elif "INTERMEDIO" in lvl.upper():
                    lvl_key = "INTERMEDIO"
                else:
                    lvl_key = "UNIVERSITARIO / AVANZADO"

                if lvl_key == self.current_level:
                    pfs.append(pf)

            target_layout = self.formulario_content_layout

            btn_category = QPushButton(f"▶ {cat['name']}")
            btn_category.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_category.setStyleSheet(f"""
                QPushButton {{
                    font-size: 13px;
                    font-weight: 700;
                    color: {primary_col};
                    text-align: left;
                    border: 1px solid {border_col};
                    border-radius: 6px;
                    padding: 8px 10px;
                    margin-top: 8px;
                    margin-bottom: 2px;
                    background-color: {t["surface_variant"]};
                }}
                QPushButton:hover {{
                    color: {t["text_primary"]};
                    background-color: {card_hover};
                    border-color: {primary_col};
                }}
            """)
            target_layout.insertWidget(target_layout.count() - 1, btn_category)

            container = QWidget()
            container_layout = QVBoxLayout(container)
            container_layout.setContentsMargins(4, 4, 4, 10)
            container_layout.setSpacing(6)

            if not pfs:
                empty_lbl = QLabel("Aún no hay fórmulas en este nivel.")
                empty_lbl.setStyleSheet(
                    f"color: {t['text_secondary']}; font-style: italic; padding: 4px;"
                )
                container_layout.addWidget(empty_lbl)
            else:
                for pf in pfs:
                    card = ProcedureCardWidget(pf, self.current_theme)
                    card.latex_selected.connect(self.latex_selected.emit)
                    container_layout.addWidget(card)

            container.setVisible(False)
            target_layout.insertWidget(target_layout.count() - 1, container)

            btn_category.clicked.connect(
                lambda checked=False, c=container, b=btn_category, name=cat["name"]: (
                    c.setVisible(not c.isVisible()),
                    b.setText(f"▼ {name}" if c.isVisible() else f"▶ {name}"),
                )
            )

    def _build_templates_grid(self):
        # Clear layout (keep stretch)
        while self.tpl_layout.count() > 1:
            item = self.tpl_layout.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()

        t = get_theme_dict(self.current_theme)
        card_hover = t.get("bg_item_card_hover", t["surface"])
        border_col = t.get("border_subtle", t["border"])
        primary_col = t.get("primary", COLOR_MIKU_CYAN)

        for cat in CATEGORIES:
            cat_templates = [
                tpl for tpl in TEMPLATES if tpl.get("category") == cat["id"]
            ]
            if not cat_templates:
                continue

            btn_category = QPushButton(f"▶ {cat['name']}")
            btn_category.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_category.setStyleSheet(f"""
                QPushButton {{
                    font-size: 13px;
                    font-weight: 700;
                    color: {primary_col};
                    text-align: left;
                    border: 1px solid {border_col};
                    border-radius: 6px;
                    padding: 8px 10px;
                    margin-top: 4px;
                    margin-bottom: 2px;
                    background-color: {t["surface_variant"]};
                }}
                QPushButton:hover {{
                    color: {t["text_primary"]};
                    background-color: {card_hover};
                    border-color: {primary_col};
                }}
            """)
            self.tpl_layout.insertWidget(self.tpl_layout.count() - 1, btn_category)

            container = QWidget()
            container_layout = QGridLayout(container)
            container_layout.setContentsMargins(4, 4, 4, 10)
            container_layout.setSpacing(6)

            row, col = 0, 0
            for tpl in cat_templates:
                node = tpl["factory"]()
                for slot in node.slots.values():
                    slot.insert_text(r"\square")
                latex_repr = node.to_latex()

                card = TemplateCardOption(
                    latex=latex_repr,
                    label_text=str(tpl["name"]),
                    description=str(tpl["description"]),
                    current_theme=self.current_theme,
                )
                card.clicked.connect(partial(self._on_template_clicked, tpl["factory"]))
                card.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                is_fav = self.fav_manager.is_favorite(tpl["id"])
                card.customContextMenuRequested.connect(
                    partial(
                        self._show_context_menu,
                        btn=card,
                        item_id=tpl["id"],
                        is_fav=is_fav,
                    )
                )

                container_layout.addWidget(card, row, col)
                col += 1
                if col >= 3:
                    col = 0
                    row += 1

            container.setVisible(False)
            self.tpl_layout.insertWidget(self.tpl_layout.count() - 1, container)

            btn_category.clicked.connect(
                lambda checked=False, c=container, b=btn_category, name=cat["name"]: (
                    c.setVisible(not c.isVisible()),
                    b.setText(f"▼ {name}" if c.isVisible() else f"▶ {name}"),
                )
            )

    def _build_symbols_grid(self):
        while self.sym_layout.count() > 1:
            item = self.sym_layout.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()

        t = get_theme_dict(self.current_theme)
        card_hover = t.get("bg_item_card_hover", t["surface"])
        border_col = t.get("border_subtle", t["border"])
        primary_col = t.get("primary", COLOR_MIKU_CYAN)

        for cat in CATEGORIES:
            cat_symbols = [s for s in SYMBOLS if s.get("category") == cat["id"]]
            if not cat_symbols:
                continue

            btn_category = QPushButton(f"▶ {cat['name']}")
            btn_category.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_category.setStyleSheet(f"""
                QPushButton {{
                    font-size: 13px;
                    font-weight: 700;
                    color: {primary_col};
                    text-align: left;
                    border: 1px solid {border_col};
                    border-radius: 6px;
                    padding: 8px 10px;
                    margin-top: 4px;
                    margin-bottom: 2px;
                    background-color: {t["surface_variant"]};
                }}
                QPushButton:hover {{
                    color: {t["text_primary"]};
                    background-color: {card_hover};
                    border-color: {primary_col};
                }}
            """)
            self.sym_layout.insertWidget(self.sym_layout.count() - 1, btn_category)

            container = QWidget()
            container_layout = QGridLayout(container)
            container_layout.setContentsMargins(4, 4, 4, 10)
            container_layout.setSpacing(6)

            row, col = 0, 0
            for sym in cat_symbols:
                card = TemplateCardOption(
                    latex=sym["latex"],
                    label_text=sym["name"],
                    description=sym["name"],
                    current_theme=self.current_theme,
                )
                card.clicked.connect(partial(self._on_symbol_clicked, sym))
                card.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                is_fav = self.fav_manager.is_favorite(sym["latex"])
                card.customContextMenuRequested.connect(
                    partial(
                        self._show_context_menu,
                        btn=card,
                        item_id=sym["latex"],
                        is_fav=is_fav,
                    )
                )

                container_layout.addWidget(card, row, col)
                col += 1
                if col >= 3:
                    col = 0
                    row += 1

            container.setVisible(False)
            self.sym_layout.insertWidget(self.sym_layout.count() - 1, container)

            btn_category.clicked.connect(
                lambda checked=False, c=container, b=btn_category, name=cat["name"]: (
                    c.setVisible(not c.isVisible()),
                    b.setText(f"▼ {name}" if c.isVisible() else f"▶ {name}"),
                )
            )

    def _build_constants_grid(self):
        while self.const_layout.count() > 1:
            item = self.const_layout.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()

        t = get_theme_dict(self.current_theme)
        card_hover = t.get("bg_item_card_hover", t["surface"])
        border_col = t.get("border_subtle", t["border"])
        primary_col = t.get("primary", COLOR_MIKU_CYAN)

        for cat in CONSTANTS:
            btn_category = QPushButton(f"▶ {cat['name']}")
            btn_category.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_category.setStyleSheet(f"""
                QPushButton {{
                    font-size: 13px;
                    font-weight: 700;
                    color: {primary_col};
                    text-align: left;
                    border: 1px solid {border_col};
                    border-radius: 6px;
                    padding: 8px 10px;
                    margin-top: 4px;
                    margin-bottom: 2px;
                    background-color: {t["surface_variant"]};
                }}
                QPushButton:hover {{
                    color: {t["text_primary"]};
                    background-color: {card_hover};
                    border-color: {primary_col};
                }}
            """)
            self.const_layout.insertWidget(self.const_layout.count() - 1, btn_category)

            container = QWidget()
            container_layout = QGridLayout(container)
            container_layout.setContentsMargins(4, 4, 4, 10)
            container_layout.setSpacing(6)

            row, col = 0, 0
            for const_item in cat["constants"]:
                if "value" not in const_item:
                    continue
                card = ConstantCardWidget(
                    name=const_item["name"],
                    symbol_latex=const_item["symbol"],
                    full_value=const_item["value"],
                    current_theme=self.current_theme,
                )
                card.clicked_value.connect(
                    lambda val, symbol=const_item["symbol"]: self._on_symbol_clicked(
                        {"latex": val, "display": val, "name": symbol}
                    )
                )

                container_layout.addWidget(card, row, col)
                col += 1
                if col >= 3:
                    col = 0
                    row += 1

            container.setVisible(False)
            self.const_layout.insertWidget(self.const_layout.count() - 1, container)

            btn_category.clicked.connect(
                lambda checked=False, c=container, b=btn_category, name=cat["name"]: (
                    c.setVisible(not c.isVisible()),
                    b.setText(f"▼ {name}" if c.isVisible() else f"▶ {name}"),
                )
            )

    def _build_units_grid(self):
        while self.unit_layout.count() > 1:
            item = self.unit_layout.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()

        t = get_theme_dict(self.current_theme)
        card_hover = t.get("bg_item_card_hover", t["surface"])
        border_col = t.get("border_subtle", t["border"])
        primary_col = t.get("primary", COLOR_MIKU_CYAN)

        for cat in UNITS:
            btn_category = QPushButton(f"▶ {cat['name']}")
            btn_category.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_category.setStyleSheet(f"""
                QPushButton {{
                    font-size: 13px;
                    font-weight: 700;
                    color: {primary_col};
                    text-align: left;
                    border: 1px solid {border_col};
                    border-radius: 6px;
                    padding: 8px 10px;
                    margin-top: 4px;
                    margin-bottom: 2px;
                    background-color: {t["surface_variant"]};
                }}
                QPushButton:hover {{
                    color: {t["text_primary"]};
                    background-color: {card_hover};
                    border-color: {primary_col};
                }}
            """)
            self.unit_layout.insertWidget(self.unit_layout.count() - 1, btn_category)

            container = QWidget()
            container_layout = QGridLayout(container)
            container_layout.setContentsMargins(4, 4, 4, 10)
            container_layout.setSpacing(6)

            row, col = 0, 0
            for unit_item in cat["units"]:
                card = UnitCardWidget(
                    magnitude=unit_item["magnitude"],
                    name=unit_item["name"],
                    symbol_latex=unit_item["symbol"],
                    base_latex=unit_item["base"],
                    current_theme=self.current_theme,
                )
                card.clicked_unit.connect(
                    lambda val, symbol=unit_item["symbol"]: self._on_template_clicked(
                        lambda v=val: _parse_preset(v)
                    )
                )

                container_layout.addWidget(card, row, col)
                col += 1
                if col >= 3:
                    col = 0
                    row += 1

            container.setVisible(False)
            self.unit_layout.insertWidget(self.unit_layout.count() - 1, container)

            btn_category.clicked.connect(
                lambda checked=False, c=container, b=btn_category, name=cat["name"]: (
                    c.setVisible(not c.isVisible()),
                    b.setText(f"▼ {name}" if c.isVisible() else f"▶ {name}"),
                )
            )

    def _load_favorites_grid(self):
        try:
            clear_layout(self.fav_grid)
            col = 0
            row = 0
            max_cols = 3

            fav_templates = [
                t for t in TEMPLATES if self.fav_manager.is_favorite(t["id"])
            ]
            for tpl in fav_templates:
                node = tpl["factory"]()
                for slot in node.slots.values():
                    slot.insert_text(r"\square")

                latex_repr = node.to_latex()
                card = TemplateCardOption(
                    latex=latex_repr,
                    label_text=tpl["name"],
                    description=tpl["description"],
                    current_theme=self.current_theme,
                )
                card.clicked.connect(partial(self._on_template_clicked, tpl["factory"]))
                card.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                card.customContextMenuRequested.connect(
                    partial(
                        self._show_context_menu,
                        btn=card,
                        item_id=tpl["id"],
                        is_fav=True,
                    )
                )
                self.fav_grid.addWidget(card, row, col)
                col += 1
                if col >= max_cols:
                    col = 0
                    row += 1

            fav_symbols = [
                s for s in SYMBOLS if self.fav_manager.is_favorite(s["latex"])
            ]

            # User formulas in favorites
            if hasattr(self, "user_formulas_manager") and self.user_formulas_manager:
                for cat_obj in self.user_formulas_manager.categories:
                    for subcat in cat_obj["subcategories"]:
                        for form in subcat["formulas"]:
                            if self.fav_manager.is_favorite(form["id"]):
                                from src.ui.components.procedure_card import (
                                    ProcedureCardWidget,
                                )

                                card = ProcedureCardWidget(
                                    group_data={
                                        "title": form["name"],
                                        "variations": [
                                            {
                                                "latex": form["latex"],
                                                "name": "Principal",
                                            }
                                        ],
                                    },
                                    current_theme=self.current_theme,
                                )
                                card.latex_selected.connect(self.latex_selected.emit)
                                card.setContextMenuPolicy(
                                    Qt.ContextMenuPolicy.CustomContextMenu
                                )
                                card.customContextMenuRequested.connect(
                                    partial(
                                        self._show_context_menu,
                                        btn=card,
                                        item_id=form["id"],
                                        is_fav=True,
                                    )
                                )
                                self.fav_grid.addWidget(card, row, col)
                                col += 1
                                if col >= max_cols:
                                    col = 0
                                    row += 1

            for sym in fav_symbols:
                card = TemplateCardOption(
                    latex=sym["latex"],
                    label_text=sym["name"],
                    description=sym["name"],
                    current_theme=self.current_theme,
                )
                card.clicked.connect(partial(self._on_symbol_clicked, sym))
                card.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                card.customContextMenuRequested.connect(
                    partial(
                        self._show_context_menu,
                        btn=card,
                        item_id=sym["latex"],
                        is_fav=True,
                    )
                )
                self.fav_grid.addWidget(card, row, col)
                col += 1
                if col >= max_cols:
                    col = 0
                    row += 1
        except (OSError, RuntimeError) as e:
            get_logger().error(f"Error loading favorites: {e}")

    def _on_template_clicked(self, factory: Callable[[], Any]):
        try:
            self.template_selected.emit(factory())
        except Exception as e:  # noqa: BLE001
            get_logger().error(f"Error emitting template_selected: {e}")

    def _on_symbol_clicked(self, sym_data: dict[str, Any]):
        try:
            from src.core.ast import SymbolNode

            node = SymbolNode(
                sym_data["latex"], sym_data.get("display", sym_data.get("name", ""))
            )
            self.symbol_selected.emit(node)
        except Exception as e:  # noqa: BLE001
            get_logger().error(f"Error emitting symbol_selected: {e}")

    def _apply_search_filter(self, query: str):
        query = query.lower().strip()

        def _get_card_text(card) -> str:
            text = ""
            from src.ui.components.constant_card import ConstantCardWidget
            from src.ui.components.procedure_card import ProcedureCardWidget
            from src.ui.components.template_card import TemplateCardOption
            from src.ui.components.unit_card import UnitCardWidget

            if isinstance(card, TemplateCardOption):
                text = f"{card.latex} {card.lbl_text.text()} {card.toolTip()}"
            elif isinstance(card, ProcedureCardWidget):
                text = f"{card.group_data.get('title', '')} {card.group_data.get('description', '')}"
                for var in card.group_data.get("variations", []):
                    text += f" {var.get('name', '')} {var.get('latex', '')}"
            elif isinstance(card, ConstantCardWidget):
                text = f"{card.name} {card.symbol_latex} {card.full_value}"
            elif isinstance(card, UnitCardWidget):
                text = f"{card.magnitude} {card.name} {card.symbol_latex} {card.base_latex}"
            return text.lower()

        def filter_main_layout(main_layout):
            if not main_layout:
                return
            for i in range(main_layout.count()):
                item = main_layout.itemAt(i)
                if not item or not item.widget():
                    continue
                widget = item.widget()

                if (
                    isinstance(widget, QWidget)
                    and widget.layout()
                    and not isinstance(widget, QPushButton)
                ):
                    container_layout = widget.layout()
                    any_visible = False
                    for j in range(container_layout.count()):
                        card_item = container_layout.itemAt(j)
                        if card_item and card_item.widget():
                            card = card_item.widget()
                            card_text = _get_card_text(card)
                            if card_text:
                                match = query in card_text if query else True
                                card.setVisible(match)
                                if match:
                                    any_visible = True

                    if i > 0:
                        prev_item = main_layout.itemAt(i - 1)
                        if (
                            prev_item
                            and prev_item.widget()
                            and isinstance(prev_item.widget(), QPushButton)
                        ):
                            btn = prev_item.widget()
                            if query:
                                btn.setVisible(any_visible)
                                if any_visible:
                                    widget.setVisible(True)
                                    btn.setText(btn.text().replace("▶", "▼"))
                            else:
                                btn.setVisible(True)
                                widget.setVisible(False)
                                btn.setText(btn.text().replace("▼", "▶"))

        filter_main_layout(self.tpl_layout)
        filter_main_layout(self.sym_layout)
        filter_main_layout(self.const_layout)
        filter_main_layout(self.unit_layout)
        filter_main_layout(self.formulario_content_layout)

        for i in range(self.fav_grid.count()):
            item = self.fav_grid.itemAt(i)
            if item and item.widget():
                card = item.widget()
                card_text = _get_card_text(card)
                if card_text:
                    card.setVisible(query in card_text if query else True)
        # User tab search is handled without re-adding the tab

    def rebuild_user_tab(self, manager):
        self.user_formulas_manager = manager
        # Clear existing
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        t = get_theme_dict(self.current_theme)
        card_bg = t.get("bg_item_card", t["surface_variant"])
        card_hover = t.get("bg_item_card_hover", t["surface"])
        border_col = t.get("border_subtle", t["border"])

        if not manager.categories:
            empty_lbl = QLabel(
                "Aún no tienes fórmulas guardadas.\nCrea una nueva fórmula y guárdala para verla aquí."
            )
            empty_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            empty_lbl.setStyleSheet(
                f"color: {t['text_secondary']}; font-size: 14px; padding: 32px;"
            )
            layout.addWidget(empty_lbl)
        else:
            primary_col = t.get("primary", "#00E5FF")

            for cat_obj in manager.categories:
                # Botón de categoría desplegable (Accordion)
                btn_category = QPushButton(f"▼ {cat_obj['category']}")
                btn_category.setCursor(Qt.CursorShape.PointingHandCursor)
                btn_category.setStyleSheet(f"""
                    QPushButton {{
                        font-size: 13px;
                        font-weight: 700;
                        color: {primary_col};
                        text-align: left;
                        border: 1px solid {border_col};
                        border-radius: 6px;
                        padding: 8px 12px;
                        background-color: {card_bg};
                        margin-top: 8px;
                    }}
                    QPushButton:hover {{
                        background-color: {card_hover};
                        border: 1px solid {primary_col};
                    }}
                """)
                btn_category.setContextMenuPolicy(
                    Qt.ContextMenuPolicy.CustomContextMenu
                )
                btn_category.customContextMenuRequested.connect(
                    lambda pos, name=cat_obj["category"], b=btn_category: (
                        self._show_category_menu(b, pos, name)
                    )
                )
                layout.addWidget(btn_category)

                # Contenedor de la categoría
                cat_container = QWidget()
                cat_layout = QVBoxLayout(cat_container)
                cat_layout.setContentsMargins(0, 0, 0, 0)
                cat_layout.setSpacing(0)
                layout.addWidget(cat_container)

                # Funcionalidad de toggle
                btn_category.clicked.connect(
                    lambda checked=False, c=cat_container, b=btn_category, name=cat_obj["category"]: (
                        c.setVisible(not c.isVisible()),
                        b.setText(f"▼ {name}" if c.isVisible() else f"▶ {name}"),
                    )
                )

                for subcat in cat_obj["subcategories"]:
                    # Si no hay subcategoría (string vacío o "General" cuando está oculto), no mostramos el título
                    if (
                        subcat["name"]
                        and subcat["name"] != "General"
                        and subcat["name"] != "Sin subcategoría"
                    ):
                        subcat_label = QLabel(subcat["name"])
                        subcat_label.setProperty("class", "h3")
                        subcat_label.setContentsMargins(16, 8, 8, 4)
                        subcat_label.setContextMenuPolicy(
                            Qt.ContextMenuPolicy.CustomContextMenu
                        )
                        subcat_label.customContextMenuRequested.connect(
                            lambda pos, cat_n=cat_obj["category"], sub_n=subcat["name"], lbl=subcat_label: (
                                self._show_subcategory_menu(lbl, pos, cat_n, sub_n)
                            )
                        )
                        cat_layout.addWidget(subcat_label)

                    grid = QGridLayout()
                    grid.setSpacing(8)
                    grid.setContentsMargins(16, 4, 16, 12)

                    row, col = 0, 0
                    max_cols = 4

                    for formula in subcat["formulas"]:
                        from src.ui.components.procedure_card import ProcedureCardWidget

                        card_title = formula.get("description") or formula["name"]

                        # Obtener o construir lista de variantes
                        variations = formula.get("variations")
                        if not variations:
                            variations = [
                                {
                                    "name": formula["name"],
                                    "latex": formula["latex"],
                                    "description": formula.get(
                                        "description", formula["name"]
                                    ),
                                }
                            ]
                        else:
                            for v in variations:
                                if "description" not in v:
                                    v["description"] = formula.get(
                                        "description", v.get("name", formula["name"])
                                    )

                        card = ProcedureCardWidget(
                            group_data={"title": card_title, "variations": variations},
                            current_theme=self.current_theme,
                        )
                        card.latex_selected.connect(self.latex_selected.emit)

                        card.setContextMenuPolicy(
                            Qt.ContextMenuPolicy.CustomContextMenu
                        )
                        is_fav = self.fav_manager.is_favorite(formula["id"])
                        card.customContextMenuRequested.connect(
                            partial(
                                self._show_user_formula_context_menu,
                                btn=card,
                                formula=formula,
                                manager=manager,
                                is_fav=is_fav,
                                cat_name=cat_obj["category"],
                                subcat_name=subcat["name"],
                            )
                        )

                        grid.addWidget(card, row, col)
                        col += 1
                        if col >= max_cols:
                            col = 0
                            row += 1

                    cat_layout.addLayout(grid)

        layout.addStretch()
        self.tab_user.setWidget(widget)

    def _delete_user_formula(self, manager, formula_id: str):
        from PySide6.QtWidgets import QMessageBox

        from src.ui.theme import get_theme_qss

        msg = QMessageBox(self)
        msg.setWindowTitle("Confirmar Eliminación")
        msg.setText("¿Estás seguro de que deseas eliminar esta fórmula?")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        msg.setStyleSheet(get_theme_qss(self.current_theme))

        if msg.exec_() == QMessageBox.StandardButton.Yes:
            manager.remove_formula(formula_id)
            self.rebuild_user_tab(manager)

    def _show_category_menu(self, widget, pos, cat_name: str):
        menu = QMenu(self)
        t = get_theme_dict(self.current_theme)
        menu.setStyleSheet(f"""
            QMenu {{ background-color: {t["surface"]}; color: {t["text_primary"]}; border: 1px solid {t["border"]}; border-radius: 8px; padding: 4px; }}
            QMenu::item {{ padding: 6px 14px; border-radius: 4px; color: {t["text_primary"]}; }}
            QMenu::item:selected {{ background-color: {t["primary"]}; color: #FFFFFF; }}
        """)

        act_edit = QAction("✏️ Editar Categoría", self)
        act_edit.triggered.connect(lambda: self._edit_category(cat_name))
        menu.addAction(act_edit)

        act_up = QAction("⬆️ Mover Arriba", self)
        act_up.triggered.connect(lambda: self._move_category(cat_name, -1))
        menu.addAction(act_up)

        act_down = QAction("⬇️ Mover Abajo", self)
        act_down.triggered.connect(lambda: self._move_category(cat_name, 1))
        menu.addAction(act_down)

        act_del = QAction("❌ Eliminar Categoría", self)
        act_del.triggered.connect(lambda: self._delete_category(cat_name))
        menu.addAction(act_del)

        menu.exec_(widget.mapToGlobal(pos))

    def _show_subcategory_menu(self, widget, pos, cat_name: str, sub_name: str):
        menu = QMenu(self)
        t = get_theme_dict(self.current_theme)
        menu.setStyleSheet(f"""
            QMenu {{ background-color: {t["surface"]}; color: {t["text_primary"]}; border: 1px solid {t["border"]}; border-radius: 8px; padding: 4px; }}
            QMenu::item {{ padding: 6px 14px; border-radius: 4px; color: {t["text_primary"]}; }}
            QMenu::item:selected {{ background-color: {t["primary"]}; color: #FFFFFF; }}
        """)

        act_edit = QAction("✏️ Editar Subcategoría", self)
        act_edit.triggered.connect(lambda: self._edit_subcategory(cat_name, sub_name))
        menu.addAction(act_edit)

        act_up = QAction("⬆️ Mover Arriba", self)
        act_up.triggered.connect(lambda: self._move_subcategory(cat_name, sub_name, -1))
        menu.addAction(act_up)

        act_down = QAction("⬇️ Mover Abajo", self)
        act_down.triggered.connect(
            lambda: self._move_subcategory(cat_name, sub_name, 1)
        )
        menu.addAction(act_down)

        act_del = QAction("❌ Eliminar Subcategoría", self)
        act_del.triggered.connect(lambda: self._delete_subcategory(cat_name, sub_name))
        menu.addAction(act_del)

        menu.exec_(widget.mapToGlobal(pos))

    def _edit_category(self, cat_name: str):
        from PySide6.QtWidgets import QDialog, QInputDialog

        from src.ui.theme import get_theme_qss

        dialog = QInputDialog(self)
        dialog.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        dialog.setStyleSheet(get_theme_qss(self.current_theme))
        dialog.setWindowTitle("Editar Categoría")
        dialog.setLabelText("Nuevo nombre de categoría:")
        dialog.setTextValue(cat_name)
        if dialog.exec_() == QDialog.DialogCode.Accepted:
            new_name = dialog.textValue().strip()
            if new_name and new_name != cat_name:
                self.user_formulas_manager.edit_category(cat_name, new_name)
                self.rebuild_user_tab(self.user_formulas_manager)

    def _delete_category(self, cat_name: str):
        from PySide6.QtWidgets import QMessageBox

        from src.ui.theme import get_theme_qss

        msg = QMessageBox(self)
        msg.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        msg.setWindowTitle("Eliminar Categoría")
        msg.setText(
            f"¿Estás seguro de que deseas eliminar la categoría '{cat_name}' y TODAS sus fórmulas?"
        )
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        msg.setStyleSheet(get_theme_qss(self.current_theme))
        if msg.exec_() == QMessageBox.StandardButton.Yes:
            self.user_formulas_manager.remove_category(cat_name)
            self.rebuild_user_tab(self.user_formulas_manager)

    def _move_category(self, cat_name: str, offset: int):
        self.user_formulas_manager.move_category(cat_name, offset)
        self.rebuild_user_tab(self.user_formulas_manager)

    def _edit_subcategory(self, cat_name: str, sub_name: str):
        from PySide6.QtWidgets import QDialog, QInputDialog

        from src.ui.theme import get_theme_qss

        dialog = QInputDialog(self)
        dialog.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        dialog.setStyleSheet(get_theme_qss(self.current_theme))
        dialog.setWindowTitle("Editar Subcategoría")
        dialog.setLabelText("Nuevo nombre de subcategoría:")
        dialog.setTextValue(sub_name)
        if dialog.exec_() == QDialog.DialogCode.Accepted:
            new_name = dialog.textValue().strip()
            if new_name and new_name != sub_name:
                self.user_formulas_manager.edit_subcategory(
                    cat_name, sub_name, new_name
                )
                self.rebuild_user_tab(self.user_formulas_manager)

    def _delete_subcategory(self, cat_name: str, sub_name: str):
        from PySide6.QtWidgets import QMessageBox

        from src.ui.theme import get_theme_qss

        msg = QMessageBox(self)
        msg.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        msg.setWindowTitle("Eliminar Subcategoría")
        msg.setText(
            f"¿Estás seguro de que deseas eliminar la subcategoría '{sub_name}' y TODAS sus fórmulas?"
        )
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        msg.setStyleSheet(get_theme_qss(self.current_theme))
        if msg.exec_() == QMessageBox.StandardButton.Yes:
            self.user_formulas_manager.remove_subcategory(cat_name, sub_name)
            self.rebuild_user_tab(self.user_formulas_manager)

    def _move_subcategory(self, cat_name: str, sub_name: str, offset: int):
        self.user_formulas_manager.move_subcategory(cat_name, sub_name, offset)
        self.rebuild_user_tab(self.user_formulas_manager)
