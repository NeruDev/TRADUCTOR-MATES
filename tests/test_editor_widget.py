"""
---
file: tests/test_editor_widget.py
module: tests.test_editor_widget
description: Pruebas unitarias y de integración gráfica para MathEditorWidget, casillas interactivas y brackets adaptables.
type: test/unit
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
  - src.ui.components.bracket_widget
  - src.ui.components.editor_widget
relations:
  - src/ui/components/editor_widget.py
  - src/ui/components/bracket_widget.py
exports: []
test: pytest tests/test_editor_widget.py
constraints:
  - "Ejecutar pruebas Qt utilizando fixture qapp para evitar inicializaciones duplicadas de QApplication"
keywords:
  - test-editor-widget
  - slot-box
  - adaptive-brackets
  - pyside6-testing
---

Unit tests for Math Editor Widget, Slot Box, and Adaptive Brackets.
"""

from __future__ import annotations

import pytest
from PySide6.QtWidgets import QApplication

from src.core.ast import (
    BracketNode,
    DefiniteIntegralNode,
    FractionNode,
    MathTree,
)
from src.ui.components.bracket_widget import AdaptiveBracketWidget, BracketGraphicWidget
from src.ui.components.editor_widget import (
    MathEditorWidget,
)


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app


def test_bracket_widgets(qapp):
    graphic = BracketGraphicWidget("(")
    assert graphic.minimumWidth() >= 6

    adaptive = AdaptiveBracketWidget("(", ")")
    assert adaptive.left_bracket.delim == "("
    assert adaptive.right_bracket.delim == ")"


def test_editor_widget_rebuild(qapp):
    tree = MathTree()

    # Insert Bracket Node with Fraction
    bracket = BracketNode("(", ")")
    frac = FractionNode()
    frac.slots["num"].insert_text("x")
    frac.slots["den"].insert_text("2")
    bracket.slots["body"].add_node(frac)
    tree.root_slot.add_node(bracket)

    editor = MathEditorWidget(tree)
    editor.rebuild_editor()
    assert editor.container_layout.count() > 0


def test_integral_rendering(qapp):
    tree = MathTree()
    integ = DefiniteIntegralNode()
    integ.slots["lower"].insert_text("-∞")
    integ.slots["upper"].insert_text("∞")
    integ.slots["body"].insert_text("e^{-x^2}")
    integ.slots["var"].insert_text("x")
    tree.root_slot.add_node(integ)

    editor = MathEditorWidget(tree)
    editor.rebuild_editor()
    assert editor.container_layout.count() > 0


def test_svg_cache_dynamic_scaling(qapp):
    from src.ui.components.svg_cache import SVGMathCache

    cache = SVGMathCache.get_instance()

    # Custom icon size
    pix_icon = cache.get_svg_icon(r"\int x dx", "#39C5BB", width=180, height=54)
    assert not pix_icon.isNull()
    assert pix_icon.width() == 180
    assert pix_icon.height() == 54

    # Dynamic preview scaling (125% default scale base_scale=0.15)
    pix_short = cache.get_dynamic_preview_pixmap("x", "#ffffff")
    assert not pix_short.isNull()
    assert pix_short.width() > 0

    # Test that default base_scale is 0.15 (125% of 0.12)
    pix_short_old = cache.get_dynamic_preview_pixmap("x", "#ffffff", base_scale=0.12)
    assert pix_short.width() > pix_short_old.width()

    # Long formulas vs short formulas
    pix_long = cache.get_dynamic_preview_pixmap(
        r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}", "#ffffff"
    )
    assert not pix_long.isNull()
    assert pix_long.width() > pix_short.width()

    # Vector norm formula: should adaptively dampen and fit in viewport with auto-fit
    vector_norm_latex = r"\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}"
    pix_norm = cache.get_dynamic_preview_pixmap(
        vector_norm_latex, "#ffffff", max_width=600, max_height=300, is_auto_fit=True
    )
    assert not pix_norm.isNull()
    assert pix_norm.width() <= 600


def test_preview_panel_export_png_and_svg(qapp, tmp_path):
    import os

    from PySide6.QtCore import QByteArray, QRectF
    from PySide6.QtGui import QColor, QImage, QPainter
    from PySide6.QtSvg import QSvgRenderer

    from src.ui.components.preview_panel import (
        MathPreviewPanel,
        ensure_svg_white_background,
    )
    from src.ui.components.svg_cache import SVGMathCache

    tree = MathTree()
    panel = MathPreviewPanel(tree)
    latex_str = r"\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}"
    panel.update_preview(latex_str)

    # 1. Test SVG generation with white background
    svg_code = SVGMathCache.get_instance().get_svg_string(latex_str, "#000000")
    assert svg_code.startswith("<svg")
    assert svg_code.endswith("</svg>")

    svg_with_bg = ensure_svg_white_background(svg_code)
    assert '<rect class="math-bg"' in svg_with_bg

    svg_file = tmp_path / "test_formula.svg"
    with open(svg_file, "w", encoding="utf-8") as f:
        f.write(svg_with_bg)

    verify_renderer = QSvgRenderer(str(svg_file))
    assert verify_renderer.isValid()

    # 2. Test PNG image rendering
    renderer = QSvgRenderer(QByteArray(svg_code.encode("utf-8")))
    assert renderer.isValid()

    vb = renderer.viewBoxF()
    w0 = vb.width() if vb.width() > 0 else 200.0
    h0 = vb.height() if vb.height() > 0 else 100.0

    scale = 0.35
    target_w = max(1, int(w0 * scale))
    target_h = max(1, int(h0 * scale))
    pad = 32

    image = QImage(target_w + pad * 2, target_h + pad * 2, QImage.Format.Format_ARGB32)
    image.fill(QColor("#FFFFFF"))
    painter = QPainter(image)
    renderer.render(
        painter, QRectF(float(pad), float(pad), float(target_w), float(target_h))
    )
    painter.end()

    png_file = tmp_path / "test_formula.png"
    assert image.save(str(png_file), "PNG")
    assert os.path.exists(png_file)
    assert os.path.getsize(png_file) > 100


def test_preview_panel_zoom_and_autofit(qapp):
    from src.ui.components.preview_panel import MathPreviewPanel

    tree = MathTree()
    panel = MathPreviewPanel(tree)
    panel.resize(600, 300)

    latex_str = r"\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}"
    panel.update_preview(latex_str)

    # 1. Initial state is auto-fit
    assert panel.is_auto_fit is True
    assert panel.zoom_factor == 1.0
    assert panel.lbl_zoom.text() == "Zoom"

    # 2. Test Zoom In
    panel._zoom_in()
    assert panel.is_auto_fit is False
    assert panel.zoom_factor > 1.0
    assert "%" in panel.lbl_zoom.text()

    # 3. Test Zoom Out
    panel._zoom_out()
    assert panel.is_auto_fit is False

    # 4. Test Reset
    panel._zoom_reset()
    assert panel.is_auto_fit is True
    assert panel.zoom_factor == 1.0
    assert panel.lbl_zoom.text() == "Zoom"


def test_main_window_lifecycle_and_theme_toggle(qapp):
    from src.ui.main_window import MainWindow

    window = MainWindow()
    assert window.current_theme == "dark"
    assert window.code_panel is not None
    assert window.editor_widget is not None
    assert window.preview_panel is not None
    assert window.palette_widget is not None

    # Toggle to Light mode
    window._on_theme_toggled()
    assert window.current_theme == "light"
    assert window.code_panel.current_theme == "light"
    assert window.editor_widget.current_theme == "light"
    assert window.palette_widget.current_theme == "light"
    assert window.preview_panel.current_theme == "light"

    # Toggle back to Dark mode
    window._on_theme_toggled()
    assert window.current_theme == "dark"
    assert window.code_panel.current_theme == "dark"
    assert window.editor_widget.current_theme == "dark"
    assert window.palette_widget.current_theme == "dark"
    assert window.preview_panel.current_theme == "dark"

    window.close()


def test_code_panel_font_size_selector(qapp):
    from src.core.ast import MathTree
    from src.ui.components.code_panel import CodeTranslationPanel
    from src.ui.theme import get_theme_qss

    qapp.setStyleSheet(get_theme_qss("dark"))

    tree = MathTree()
    panel = CodeTranslationPanel(tree)
    panel.show()
    qapp.processEvents()

    assert panel.current_font_size == 16
    assert panel.combo_font_size.currentText() == "16 pt"
    assert panel.latex_edit.font().pointSize() == 16
    assert panel.markdown_edit.font().pointSize() == 16
    assert panel.latex_edit.document().defaultFont().pointSize() == 16

    # Test selecting various font sizes dynamically
    for target_size in [10, 14, 20, 24, 32]:
        idx = panel.font_sizes.index(target_size)
        panel.combo_font_size.setCurrentIndex(idx)
        qapp.processEvents()
        assert panel.current_font_size == target_size
        assert panel.combo_font_size.currentText() == f"{target_size} pt"
        assert panel.latex_edit.font().pointSize() == target_size
        assert panel.markdown_edit.font().pointSize() == target_size
        assert panel.latex_edit.document().defaultFont().pointSize() == target_size

    # Test theme switching preserves font size
    panel.set_theme("light")
    qapp.processEvents()
    assert panel.current_font_size == 32
    assert panel.latex_edit.font().pointSize() == 32
    assert panel.markdown_edit.font().pointSize() == 32

    panel.close()


def test_editor_widget_scaled_boxes(qapp):
    from src.core.ast import MathTree
    from src.ui.components.editor_widget import MathEditorWidget

    tree = MathTree()
    editor = MathEditorWidget(tree)
    assert editor.base_font_size == 32


def test_palette_formulario_subtabs_and_catalog(qapp):
    from src.data.symbols import PRESET_FORMULAS
    from src.ui.components.palette_widget import MathPaletteWidget

    palette = MathPaletteWidget()
    assert palette.tabs.tabText(0) == "⭐ Favoritos"
    assert palette.tabs.tabText(1) == "🧩 Plantillas"
    assert palette.tabs.tabText(2) == "🔣 Símbolos"
    assert palette.tabs.tabText(3) == "♾️ Constantes"
    assert palette.tabs.tabText(4) == "📏 Unidades"
    assert palette.tabs.tabText(5) == "👤 Usuario"
    assert palette.tabs.tabText(6) == "📚 Formulario"

    assert palette.current_domain == "math"
    assert palette.btn_math.isChecked() is True
    assert palette.btn_phys.isChecked() is False

    # Switch to Physics
    palette._set_domain_and_level("physics", "BÁSICO")
    assert palette.current_domain == "physics"
    assert palette.btn_math.isChecked() is False
    assert palette.btn_phys.isChecked() is True

    # Switch back to Math
    palette._set_domain_and_level("math", "BÁSICO")
    assert palette.current_domain == "math"
    assert palette.btn_math.isChecked() is True

    # Verify formulas count and branches
    assert len(PRESET_FORMULAS) >= 50
    math_formulas = [f for f in PRESET_FORMULAS if f.get("domain") == "math"]
    phys_formulas = [f for f in PRESET_FORMULAS if f.get("domain") == "physics"]
    assert len(math_formulas) >= 25
    assert len(phys_formulas) >= 20


def test_fillable_integral_templates_and_greek_tab(qapp):
    from src.core.ast import ContourIntegralNode, DoubleIntegralNode, TripleIntegralNode
    from src.data.symbols import SYMBOLS, TEMPLATES
    from src.ui.components.palette_widget import MathPaletteWidget

    # Verify integral templates exist
    tmpl_ids = [t["id"] for t in TEMPLATES]
    assert "contour_integral" in tmpl_ids
    assert "double_integral" in tmpl_ids
    assert "triple_integral" in tmpl_ids

    c_tmpl = next(t for t in TEMPLATES if t["id"] == "contour_integral")
    d_tmpl = next(t for t in TEMPLATES if t["id"] == "double_integral")
    t_tmpl = next(t for t in TEMPLATES if t["id"] == "triple_integral")

    assert isinstance(c_tmpl["factory"](), ContourIntegralNode)
    assert isinstance(d_tmpl["factory"](), DoubleIntegralNode)
    assert isinstance(t_tmpl["factory"](), TripleIntegralNode)

    # Verify \oint, \iint, \iiint are NOT in SYMBOLS
    sym_latex = [s["latex"] for s in SYMBOLS]
    assert r"\oint" not in sym_latex
    assert r"\iint" not in sym_latex
    assert r"\iiint" not in sym_latex

    # Verify Symbols layout has categories
    palette = MathPaletteWidget()
    # Let the timers run or force build
    palette._build_symbols_grid()
    assert palette.sym_layout.count() >= 1


def test_integral_graphic_widget_and_6px_barrier(qapp):
    from src.core.ast import DefiniteIntegralNode, MathTree
    from src.ui.components.bracket_widget import (
        AdaptiveIntegralWidget,
        IntegralGraphicWidget,
    )
    from src.ui.components.editor_widget import MathEditorWidget

    # 1. Test graphic widget metric calculations
    for sym in ["∫", "∮", "∬", "∭"]:
        ig = IntegralGraphicWidget(symbol=sym, font_size=32)
        assert ig.width() >= 18
        assert ig.height() >= 38
        assert ig.pad_top == 4
        assert ig.pad_bottom == 4

    # 2. Test adaptive integral container layout & 6px barrier
    ai = AdaptiveIntegralWidget(symbol="∫", font_size=32)
    assert ai.main_layout.spacing() == 6
    assert ai.graphic is not None

    # 3. Test full editor rendering with definite & contour integral
    tree = MathTree()
    integ = DefiniteIntegralNode()
    integ.slots["lower"].insert_text("0")
    integ.slots["upper"].insert_text("1")
    integ.slots["body"].insert_text("x^2")
    integ.slots["var"].insert_text("x")
    tree.root_slot.add_node(integ)

    editor = MathEditorWidget(tree)
    assert editor is not None
    assert editor.container_layout.count() >= 1


def test_compendio_formulas_structure(qapp):
    """Verifica que el catálogo completo de fórmulas contenga todos los niveles y subsecciones requeridas."""
    from src.core.ast import MathTree
    from src.data.symbols import PRESET_CATEGORIES, PRESET_FORMULAS

    # 1. Verificar existencia de categorías fundamentales
    cat_ids = {c["id"] for c in PRESET_CATEGORIES}
    expected_cats = {
        "math_arithmetic",
        "math_algebra",
        "math_trigonometry",
        "math_geometry",
        "math_analytic_geom",
        "math_linear_algebra",
        "math_diff_calculus",
        "math_integral_calculus",
        "math_vector_calculus",
        "math_diff_equations",
        "math_numerical_methods",
        "math_statistics",
        "phys_kinematics_dynamics",
        "phys_energy_gravitation",
        "phys_oscillations",
        "phys_waves_acoustics",
        "phys_fluids",
        "phys_analytical_relativity",
        "phys_thermodynamics",
        "phys_electromagnetism",
        "phys_optics",
        "phys_modern",
    }
    assert expected_cats.issubset(cat_ids)

    # 2. Verificar fórmulas y consistencia de datos
    assert len(PRESET_FORMULAS) >= 150

    levels_found = set()

    for pf in PRESET_FORMULAS:
        assert pf["category"] in cat_ids
        assert pf["domain"] in {"math", "physics"}
        assert len(pf["title"]) > 0
        assert pf["level"] in {
            "NIVEL BÁSICO",
            "NIVEL INTERMEDIO",
            "NIVEL UNIVERSITARIO / AVANZADO",
        }

        levels_found.add(pf["level"])

        from src.core.parser import LaTeXParser

        # Verificar generación de AST
        if "variations" in pf:
            for var in pf.get("variations", []):
                tree = LaTeXParser.parse_to_tree(var["latex"])
                assert isinstance(tree, MathTree)
                assert tree.root_slot is not None

    assert "NIVEL BÁSICO" in levels_found
    assert "NIVEL INTERMEDIO" in levels_found
    assert "NIVEL UNIVERSITARIO / AVANZADO" in levels_found


def test_palette_formulario_sections_and_subsections(qapp):
    """Verifica la construcción de la interfaz con secciones, subsecciones e insignias en la paleta."""
    from src.ui.components.palette_widget import MathPaletteWidget

    palette = MathPaletteWidget()

    # 1. Probar dominio Matemáticas
    palette._set_domain_and_level("math", "BÁSICO")
    palette._build_examples_grid()
    assert palette.formulario_content_layout.count() > 0
    assert palette.btn_math.isChecked()
    assert not palette.btn_phys.isChecked()

    # 2. Probar dominio Física
    palette._set_domain_and_level("physics", "BÁSICO")
    palette._build_examples_grid()
    assert palette.formulario_content_layout.count() > 0
    assert not palette.btn_math.isChecked()
    assert palette.btn_phys.isChecked()


def test_editor_renders_modular_product_and_styles(qapp):
    """Verifica el renderizado interactivo de ModularNode, ProductNode y StyleDecoratorNode."""
    from src.core.ast import MathTree, ModularNode, ProductNode, StyleDecoratorNode
    from src.ui.components.editor_widget import MathEditorWidget

    tree = MathTree()

    # 1. Add ModularNode
    mod = ModularNode()
    mod.slots["mod"].insert_text("m")
    tree.root_slot.add_node(mod)

    # 2. Add ProductNode
    prod = ProductNode()
    prod.slots["lower"].insert_text("k=1")
    prod.slots["upper"].insert_text("n")
    prod.slots["body"].insert_text("x_k")
    tree.root_slot.add_node(prod)

    # 3. Add StyleDecoratorNode (vector)
    style = StyleDecoratorNode("vec")
    style.slots["body"].insert_text("v")
    tree.root_slot.add_node(style)

    editor = MathEditorWidget(tree)
    editor.rebuild_editor()
    assert editor.container_layout.count() > 0
