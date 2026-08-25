"""
---
file: src/data/symbols.py
module: src.data.symbols
description: Catálogo exhaustivo de plantillas, símbolos y compendio de fórmulas de matemáticas y física.
type: data/symbols
version: 1.0.0
date: 2026-08-24
dependencies:
  - src.core.ast
relations:
  - docs/ARCHITECTURE.md
  - src/core/parser.py
  - src/ui/components/palette_widget.py
exports:
  - CATEGORIES: "Categorías de navegación para la paleta estilo Android Chips"
  - TEMPLATES: "Catálogo de plantillas matemáticas interactivas con funciones factory"
  - SYMBOLS: "Catálogo de símbolos individuales con glifos y código LaTeX"
  - PRESET_CATEGORIES: "Ramas estructuradas de matemáticas y física para el formulario"
  - PRESET_FORMULAS: "Catálogo completo de fórmulas predefinidas por ramas y niveles"
test: pytest tests/test_parser.py
constraints:
  - "Garantizar que las expresiones LaTeX de plantillas contengan marcadores válidos de casillas"
keywords:
  - symbols
  - templates
  - preset-formulas
  - math-catalog
  - physics-compendium
---

Mathematical Template & Symbol Catalog
Organized into Android-style categories (Chips) for easy insertion into formula slots.
"""

from __future__ import annotations

from src.core.ast import (
    BinomialNode,
    BracketNode,
    ContourIntegralNode,
    DefiniteIntegralNode,
    DerivativeNode,
    DoubleIntegralNode,
    FractionNode,
    IndefiniteIntegralNode,
    LimitNode,
    MathTree,
    MatrixNode,
    ModularNode,
    NthRootNode,
    PowerNode,
    ProductNode,
    SquareRootNode,
    StyleDecoratorNode,
    SubscriptNode,
    SubSupNode,
    SummationNode,
    TripleIntegralNode,
)

# Categories for Android Chip Tab Bar
CATEGORIES = [
    {"id": "favorites", "name": "Favoritos", "icon": "star"},
    {"id": "basic", "name": "Básicos", "icon": "calculator"},
    {"id": "templates", "name": "Plantillas", "icon": "crop-free"},
    {"id": "physics", "name": "Física y Vectores", "icon": "atom"},
    {"id": "greek", "name": "Letras Griegas", "icon": "font-download"},
    {"id": "calculus", "name": "Cálculo y Funciones", "icon": "timeline"},
    {"id": "matrices", "name": "Matrices y Vectores", "icon": "grid-on"},
    {"id": "logic", "name": "Lógica y Conjuntos", "icon": "hub"},
    {"id": "delimiters", "name": "Delimitadores", "icon": "code"},
]

# Structured Templates (Creates slot-fillable node instances)
TEMPLATES = [
    {
        "id": "vector_arrow",
        "category": "physics",
        "name": "Vector (Flecha)",
        "display": "v⃗",
        "description": "Notación vectorial con flecha superior",
        "factory": lambda: StyleDecoratorNode("vec"),
    },
    {
        "id": "unit_vector",
        "category": "physics",
        "name": "Versor (Unitario)",
        "display": "r̂",
        "description": "Versor o vector unitario con circunflejo",
        "factory": lambda: StyleDecoratorNode("hat"),
    },
    {
        "id": "time_derivative",
        "category": "physics",
        "name": "Derivada Temporal (Punto)",
        "display": "ẋ",
        "description": "Derivada temporal de primer orden (notación de Newton)",
        "factory": lambda: StyleDecoratorNode("dot"),
    },
    {
        "id": "time_accel",
        "category": "physics",
        "name": "Aceleración (Dos Puntos)",
        "display": "ẍ",
        "description": "Derivada temporal de segundo orden",
        "factory": lambda: StyleDecoratorNode("ddot"),
    },
    {
        "id": "bold_vector",
        "category": "physics",
        "name": "Vector en Negrita",
        "display": "𝐯",
        "description": "Notación vectorial estándar en negrita",
        "factory": lambda: StyleDecoratorNode("mathbf"),
    },
    {
        "id": "fraction",
        "category": "templates",
        "name": "Fracción",
        "display": "x / y",
        "description": "Fracción con numerador y denominador rellenables",
        "factory": lambda: FractionNode(),
    },
    {
        "id": "power",
        "category": "templates",
        "name": "Potencia",
        "display": "xⁿ",
        "description": "Exponente o superíndice rellenable",
        "factory": lambda: PowerNode(),
    },
    {
        "id": "subscript",
        "category": "templates",
        "name": "Subíndice",
        "display": "xₙ",
        "description": "Subíndice rellenable",
        "factory": lambda: SubscriptNode(),
    },
    {
        "id": "subsup",
        "category": "templates",
        "name": "Sub + Super",
        "display": "xₙᵐ",
        "description": "Base con subíndice y superíndice",
        "factory": lambda: SubSupNode(),
    },
    {
        "id": "sqrt",
        "category": "templates",
        "name": "Raíz Cuadrada",
        "display": "√x",
        "description": "Raíz cuadrada con radicando rellenable",
        "factory": lambda: SquareRootNode(),
    },
    {
        "id": "nth_root",
        "category": "templates",
        "name": "Raíz Enésima",
        "display": "ⁿ√x",
        "description": "Raíz con índice y radicando",
        "factory": lambda: NthRootNode(),
    },
    {
        "id": "indef_integral",
        "category": "templates",
        "name": "Integral Indefinida",
        "display": "∫ f(x) dx",
        "description": "Integral simple sin límites",
        "factory": lambda: IndefiniteIntegralNode(),
    },
    {
        "id": "def_integral",
        "category": "templates",
        "name": "Integral Definida",
        "display": "∫ₐᵇ f(x) dx",
        "description": "Integral definida con límites inferior y superior",
        "factory": lambda: DefiniteIntegralNode(),
    },
    {
        "id": "contour_integral",
        "category": "physics",
        "name": "Integral de Circulación (∮)",
        "display": "∮ f(r) dr",
        "description": "Integral de contorno cerrado con límites o trayectoria",
        "factory": lambda: ContourIntegralNode(),
    },
    {
        "id": "double_integral",
        "category": "physics",
        "name": "Integral Doble (∬)",
        "display": "∬ f(x,y) dA",
        "description": "Integral doble de superficie con región o límites",
        "factory": lambda: DoubleIntegralNode(),
    },
    {
        "id": "triple_integral",
        "category": "physics",
        "name": "Integral Triple (∭)",
        "display": "∭ f(x,y,z) dV",
        "description": "Integral triple de volumen con región o límites",
        "factory": lambda: TripleIntegralNode(),
    },
    {
        "id": "summation",
        "category": "templates",
        "name": "Sumatoria",
        "display": "∑ₖ₌₁ⁿ",
        "description": "Sumatoria con límites",
        "factory": lambda: SummationNode(),
    },
    {
        "id": "limit",
        "category": "templates",
        "name": "Límite",
        "display": "lim (x→a)",
        "description": "Límite cuando variable tiende a valor",
        "factory": lambda: LimitNode(),
    },
    {
        "id": "derivative",
        "category": "templates",
        "name": "Derivada df/dx",
        "display": "df/dx",
        "description": "Derivada ordinaria",
        "factory": lambda: DerivativeNode(is_partial=False),
    },
    {
        "id": "partial_derivative",
        "category": "templates",
        "name": "Derivada Parcial",
        "display": "∂f/∂x",
        "description": "Derivada parcial",
        "factory": lambda: DerivativeNode(is_partial=True),
    },
    {
        "id": "matrix_2x2",
        "category": "matrices",
        "name": "Matriz 2x2",
        "display": "[2×2]",
        "description": "Matriz de 2 filas por 2 columnas",
        "factory": lambda: MatrixNode(2, 2, "pmatrix"),
    },
    {
        "id": "matrix_3x3",
        "category": "matrices",
        "name": "Matriz 3x3",
        "display": "[3×3]",
        "description": "Matriz de 3 filas por 3 columnas",
        "factory": lambda: MatrixNode(3, 3, "bmatrix"),
    },
    {
        "id": "bracket_parentheses",
        "category": "delimiters",
        "name": "Paréntesis",
        "display": "( □ )",
        "description": "Paréntesis adaptables",
        "factory": lambda: BracketNode("(", ")"),
    },
    {
        "id": "bracket_square",
        "category": "delimiters",
        "name": "Corchetes",
        "display": "[ □ ]",
        "description": "Corchetes adaptables",
        "factory": lambda: BracketNode("[", "]"),
    },
    {
        "id": "bracket_curly",
        "category": "delimiters",
        "name": "Llaves",
        "display": "{ □ }",
        "description": "Llaves adaptables",
        "factory": lambda: BracketNode("{", "}"),
    },
    {
        "id": "bracket_abs",
        "category": "delimiters",
        "name": "Valor Absoluto",
        "display": "| □ |",
        "description": "Barras de valor absoluto o norma",
        "factory": lambda: BracketNode("|", "|"),
    },
    {
        "id": "binomial",
        "category": "templates",
        "name": "Coeficiente Binomial",
        "display": "(n k)",
        "description": "Coeficiente binomial (n sobre k)",
        "factory": lambda: BinomialNode(),
    },
    {
        "id": "product",
        "category": "templates",
        "name": "Productoria",
        "display": "∏ₖ₌₁ⁿ",
        "description": "Productoria con límites inferior y superior",
        "factory": lambda: ProductNode(),
    },
    {
        "id": "modular",
        "category": "templates",
        "name": "Congruencia Modular",
        "display": "(mod m)",
        "description": "Plantilla de módulo interactivo pmod",
        "factory": lambda: ModularNode(),
    },
]

# Mathematical Symbols Dictionary
SYMBOLS = [
    # Basic & Operators
    {"category": "basic", "display": "+", "latex": "+", "name": "Suma"},
    {"category": "basic", "display": "-", "latex": "-", "name": "Resta"},
    {"category": "basic", "display": "×", "latex": r"\times", "name": "Multiplicación"},
    {"category": "basic", "display": "÷", "latex": r"\div", "name": "División"},
    {"category": "basic", "display": "±", "latex": r"\pm", "name": "Más menos"},
    {"category": "basic", "display": "∓", "latex": r"\mp", "name": "Menos más"},
    {"category": "basic", "display": "·", "latex": r"\cdot", "name": "Punto central"},
    {"category": "basic", "display": "=", "latex": "=", "name": "Igual"},
    {"category": "basic", "display": "≠", "latex": r"\neq", "name": "Diferente"},
    {"category": "basic", "display": "≈", "latex": r"\approx", "name": "Aproximado"},
    {"category": "basic", "display": "<", "latex": "<", "name": "Menor que"},
    {"category": "basic", "display": ">", "latex": ">", "name": "Mayor que"},
    {"category": "basic", "display": "≤", "latex": r"\le", "name": "Menor o igual"},
    {"category": "basic", "display": "≥", "latex": r"\ge", "name": "Mayor o igual"},
    {
        "category": "basic",
        "display": "≡",
        "latex": r"\equiv",
        "name": "Congruente / Idéntico",
    },
    {"category": "basic", "display": "∞", "latex": r"\infty", "name": "Infinito"},
    # Greek Letters
    {"category": "greek", "display": "α", "latex": r"\alpha", "name": "Alfa"},
    {"category": "greek", "display": "β", "latex": r"\beta", "name": "Beta"},
    {"category": "greek", "display": "γ", "latex": r"\gamma", "name": "Gamma"},
    {"category": "greek", "display": "δ", "latex": r"\delta", "name": "Delta"},
    {"category": "greek", "display": "ε", "latex": r"\epsilon", "name": "Epsilon"},
    {
        "category": "greek",
        "display": "ε",
        "latex": r"\varepsilon",
        "name": "Varepsilon",
    },
    {"category": "greek", "display": "ζ", "latex": r"\zeta", "name": "Zeta"},
    {"category": "greek", "display": "η", "latex": r"\eta", "name": "Eta"},
    {"category": "greek", "display": "θ", "latex": r"\theta", "name": "Theta"},
    {"category": "greek", "display": "ϑ", "latex": r"\vartheta", "name": "Vartheta"},
    {"category": "greek", "display": "ι", "latex": r"\iota", "name": "Iota"},
    {"category": "greek", "display": "κ", "latex": r"\kappa", "name": "Kappa"},
    {"category": "greek", "display": "ϰ", "latex": r"\varkappa", "name": "Varkappa"},
    {"category": "greek", "display": "λ", "latex": r"\lambda", "name": "Lambda"},
    {"category": "greek", "display": "μ", "latex": r"\mu", "name": "Mu"},
    {"category": "greek", "display": "ν", "latex": r"\nu", "name": "Nu"},
    {"category": "greek", "display": "ξ", "latex": r"\xi", "name": "Xi"},
    {"category": "greek", "display": "π", "latex": r"\pi", "name": "Pi"},
    {"category": "greek", "display": "ϖ", "latex": r"\varpi", "name": "Varpi"},
    {"category": "greek", "display": "ρ", "latex": r"\rho", "name": "Rho"},
    {"category": "greek", "display": "ϱ", "latex": r"\varrho", "name": "Varrho"},
    {"category": "greek", "display": "σ", "latex": r"\sigma", "name": "Sigma"},
    {"category": "greek", "display": "ς", "latex": r"\varsigma", "name": "Varsigma"},
    {"category": "greek", "display": "τ", "latex": r"\tau", "name": "Tau"},
    {"category": "greek", "display": "υ", "latex": r"\upsilon", "name": "Upsilon"},
    {"category": "greek", "display": "φ", "latex": r"\phi", "name": "Phi"},
    {"category": "greek", "display": "φ", "latex": r"\varphi", "name": "Varphi"},
    {"category": "greek", "display": "χ", "latex": r"\chi", "name": "Chi"},
    {"category": "greek", "display": "ψ", "latex": r"\psi", "name": "Psi"},
    {"category": "greek", "display": "ω", "latex": r"\omega", "name": "Omega"},
    {"category": "greek", "display": "Γ", "latex": r"\Gamma", "name": "Gamma Mayús"},
    {"category": "greek", "display": "Δ", "latex": r"\Delta", "name": "Delta Mayús"},
    {"category": "greek", "display": "Θ", "latex": r"\Theta", "name": "Theta Mayús"},
    {"category": "greek", "display": "Λ", "latex": r"\Lambda", "name": "Lambda Mayús"},
    {"category": "greek", "display": "Ξ", "latex": r"\Xi", "name": "Xi Mayús"},
    {"category": "greek", "display": "Π", "latex": r"\Pi", "name": "Pi Mayús"},
    {"category": "greek", "display": "Σ", "latex": r"\Sigma", "name": "Sigma Mayús"},
    {
        "category": "greek",
        "display": "Υ",
        "latex": r"\Upsilon",
        "name": "Upsilon Mayús",
    },
    {"category": "greek", "display": "Φ", "latex": r"\Phi", "name": "Phi Mayús"},
    {"category": "greek", "display": "Ψ", "latex": r"\Psi", "name": "Psi Mayús"},
    {"category": "greek", "display": "Ω", "latex": r"\Omega", "name": "Omega Mayús"},
    # Calculus & Functions & Physics
    {"category": "calculus", "display": "sin", "latex": r"\sin", "name": "Seno"},
    {"category": "calculus", "display": "cos", "latex": r"\cos", "name": "Coseno"},
    {"category": "calculus", "display": "tan", "latex": r"\tan", "name": "Tangente"},
    {"category": "calculus", "display": "csc", "latex": r"\csc", "name": "Cosecante"},
    {"category": "calculus", "display": "sec", "latex": r"\sec", "name": "Secante"},
    {"category": "calculus", "display": "cot", "latex": r"\cot", "name": "Cotangente"},
    {
        "category": "calculus",
        "display": "sinh",
        "latex": r"\sinh",
        "name": "Seno Hiperbólico",
    },
    {
        "category": "calculus",
        "display": "cosh",
        "latex": r"\cosh",
        "name": "Coseno Hiperbólico",
    },
    {
        "category": "calculus",
        "display": "tanh",
        "latex": r"\tanh",
        "name": "Tangente Hiperbólica",
    },
    {
        "category": "calculus",
        "display": "coth",
        "latex": r"\coth",
        "name": "Cotangente Hiperbólica",
    },
    {
        "category": "calculus",
        "display": "sech",
        "latex": r"\operatorname{sech}",
        "name": "Secante Hiperbólica",
    },
    {
        "category": "calculus",
        "display": "csch",
        "latex": r"\operatorname{csch}",
        "name": "Cosecante Hiperbólica",
    },
    {
        "category": "calculus",
        "display": "arcsin",
        "latex": r"\arcsin",
        "name": "Arco Seno",
    },
    {
        "category": "calculus",
        "display": "arccos",
        "latex": r"\arccos",
        "name": "Arco Coseno",
    },
    {
        "category": "calculus",
        "display": "arctan",
        "latex": r"\arctan",
        "name": "Arco Tangente",
    },
    {
        "category": "calculus",
        "display": "ln",
        "latex": r"\ln",
        "name": "Logaritmo Natural",
    },
    {"category": "calculus", "display": "log", "latex": r"\log", "name": "Logaritmo"},
    {"category": "calculus", "display": "exp", "latex": r"\exp", "name": "Exponencial"},
    {
        "category": "calculus",
        "display": "det",
        "latex": r"\det",
        "name": "Determinante",
    },
    {"category": "calculus", "display": "lim", "latex": r"\lim", "name": "Límite"},
    {"category": "calculus", "display": "max", "latex": r"\max", "name": "Máximo"},
    {"category": "calculus", "display": "min", "latex": r"\min", "name": "Mínimo"},
    {"category": "calculus", "display": "arg", "latex": r"\arg", "name": "Argumento"},
    {
        "category": "calculus",
        "display": "deg",
        "latex": r"\deg",
        "name": "Grado Polinomio",
    },
    {
        "category": "calculus",
        "display": "gcd",
        "latex": r"\gcd",
        "name": "Máximo Común Divisor (gcd)",
    },
    {"category": "calculus", "display": "dim", "latex": r"\dim", "name": "Dimensión"},
    {
        "category": "calculus",
        "display": "ker",
        "latex": r"\ker",
        "name": "Núcleo / Kernel",
    },
    {
        "category": "calculus",
        "display": "hom",
        "latex": r"\hom",
        "name": "Homomorfismo",
    },
    {"category": "calculus", "display": "inf", "latex": r"\inf", "name": "Ínfimo"},
    {"category": "calculus", "display": "sup", "latex": r"\sup", "name": "Supremo"},
    {"category": "calculus", "display": "∏", "latex": r"\prod", "name": "Productoria"},
    {"category": "calculus", "display": "∐", "latex": r"\coprod", "name": "Coproducto"},
    {
        "category": "calculus",
        "display": "∇",
        "latex": r"\nabla",
        "name": "Nabla / Gradiente",
    },
    {
        "category": "calculus",
        "display": "∂",
        "latex": r"\partial",
        "name": "Derivada parcial",
    },
    {
        "category": "calculus",
        "display": "ℏ",
        "latex": r"\hbar",
        "name": "Constante de Planck reducida",
    },
    {
        "category": "calculus",
        "display": "…",
        "latex": r"\dots",
        "name": "Puntos suspensivos (bajos)",
    },
    {
        "category": "calculus",
        "display": "⋯",
        "latex": r"\cdots",
        "name": "Puntos suspensivos (medios)",
    },
    {
        "category": "calculus",
        "display": "⋮",
        "latex": r"\vdots",
        "name": "Puntos suspensivos (verticales)",
    },
    {
        "category": "calculus",
        "display": "⋱",
        "latex": r"\ddots",
        "name": "Puntos suspensivos (diagonales)",
    },
    # Logic & Sets
    {"category": "logic", "display": "∈", "latex": r"\in", "name": "Pertenece"},
    {"category": "logic", "display": "∉", "latex": r"\notin", "name": "No pertenece"},
    {"category": "logic", "display": "⊂", "latex": r"\subset", "name": "Subconjunto"},
    {
        "category": "logic",
        "display": "⊆",
        "latex": r"\subseteq",
        "name": "Subconjunto o igual",
    },
    {"category": "logic", "display": "∪", "latex": r"\cup", "name": "Unión"},
    {"category": "logic", "display": "∩", "latex": r"\cap", "name": "Intersección"},
    {
        "category": "logic",
        "display": "∧",
        "latex": r"\land",
        "name": "Y lógico (Conjunción)",
    },
    {
        "category": "logic",
        "display": "∨",
        "latex": r"\lor",
        "name": "O lógico (Disyunción)",
    },
    {"category": "logic", "display": "⇒", "latex": r"\Rightarrow", "name": "Implica"},
    {
        "category": "logic",
        "display": "⇒",
        "latex": r"\implies",
        "name": "Implica (largo)",
    },
    {
        "category": "logic",
        "display": "⇔",
        "latex": r"\Leftrightarrow",
        "name": "Si y solo si",
    },
    {
        "category": "logic",
        "display": "⇔",
        "latex": r"\iff",
        "name": "Si y solo si (largo)",
    },
    {
        "category": "logic",
        "display": "∣",
        "latex": r"\mid",
        "name": "Divide a / Tal que",
    },
    {"category": "logic", "display": "∤", "latex": r"\nmid", "name": "No divide a"},
    {
        "category": "logic",
        "display": "→",
        "latex": r"\to",
        "name": "Tiende a / Flecha derecha",
    },
    {
        "category": "logic",
        "display": "→",
        "latex": r"\rightarrow",
        "name": "Flecha derecha",
    },
    {
        "category": "logic",
        "display": "←",
        "latex": r"\leftarrow",
        "name": "Flecha izquierda",
    },
    {
        "category": "logic",
        "display": "↔",
        "latex": r"\leftrightarrow",
        "name": "Flecha doble",
    },
    {"category": "logic", "display": "∀", "latex": r"\forall", "name": "Para todo"},
    {"category": "logic", "display": "∃", "latex": r"\exists", "name": "Existe"},
    {"category": "logic", "display": "ℝ", "latex": r"\mathbb{R}", "name": "Reales"},
    {"category": "logic", "display": "ℕ", "latex": r"\mathbb{N}", "name": "Naturales"},
    {"category": "logic", "display": "ℤ", "latex": r"\mathbb{Z}", "name": "Enteros"},
    {"category": "logic", "display": "ℂ", "latex": r"\mathbb{C}", "name": "Complejos"},
    # Physics & Vector Operators
    {
        "category": "physics",
        "display": "ℏ",
        "latex": r"\hbar",
        "name": "Constante de Planck reducida",
    },
    {
        "category": "physics",
        "display": "∇",
        "latex": r"\nabla",
        "name": "Nabla / Gradiente / Divergencia",
    },
    {
        "category": "physics",
        "display": "∂",
        "latex": r"\partial",
        "name": "Derivada Parcial",
    },
    {
        "category": "physics",
        "display": "∝",
        "latex": r"\propto",
        "name": "Proporcional a",
    },
    {"category": "physics", "display": "∠", "latex": r"\angle", "name": "Ángulo"},
    {
        "category": "physics",
        "display": "⟂",
        "latex": r"\perp",
        "name": "Perpendicular / Ortogonal",
    },
    {"category": "physics", "display": "∥", "latex": r"\parallel", "name": "Paralelo"},
    {
        "category": "physics",
        "display": "°",
        "latex": r"^\circ",
        "name": "Grado Sexagesimal",
    },
    {
        "category": "physics",
        "display": "Ω",
        "latex": r"\Omega",
        "name": "Ohmio / Resistencia",
    },
    {
        "category": "physics",
        "display": "†",
        "latex": r"\dagger",
        "name": "Operador Adjunto / Daga",
    },
    {
        "category": "physics",
        "display": "⊗",
        "latex": r"\otimes",
        "name": "Producto Tensorial / Kronecker",
    },
    {
        "category": "delimiters",
        "display": "⟨",
        "latex": r"\langle",
        "name": "Paréntesis Angular Izquierdo",
    },
    {
        "category": "delimiters",
        "display": "⟩",
        "latex": r"\rangle",
        "name": "Paréntesis Angular Derecho",
    },
]

LATEX_TO_UNICODE = {
    s["latex"]: s["display"] for s in SYMBOLS if s["latex"].startswith("\\")
}

# Preset Categories for Formulario (Mathematics & Physics Branches)
PRESET_CATEGORIES = [
    # Matemáticas
    {
        "id": "math_arithmetic",
        "domain": "math",
        "name": "1. Aritmética",
        "icon": "calculate",
    },
    {"id": "math_algebra", "domain": "math", "name": "2. Álgebra", "icon": "functions"},
    {
        "id": "math_trigonometry",
        "domain": "math",
        "name": "3. Trigonometría",
        "icon": "square-root-alt",
    },
    {
        "id": "math_geometry",
        "domain": "math",
        "name": "4. Geometría (Plana y del Espacio)",
        "icon": "shapes",
    },
    {
        "id": "math_analytic_geom",
        "domain": "math",
        "name": "5. Geometría Analítica",
        "icon": "show-chart",
    },
    {
        "id": "math_linear_algebra",
        "domain": "math",
        "name": "6. Álgebra Lineal",
        "icon": "grid-on",
    },
    {
        "id": "math_diff_calculus",
        "domain": "math",
        "name": "7. Cálculo Diferencial",
        "icon": "timeline",
    },
    {
        "id": "math_integral_calculus",
        "domain": "math",
        "name": "8. Cálculo Integral",
        "icon": "functions",
    },
    {
        "id": "math_vector_calculus",
        "domain": "math",
        "name": "9. Cálculo Vectorial y Multivariable",
        "icon": "grain",
    },
    {
        "id": "math_diff_equations",
        "domain": "math",
        "name": "10. Ecuaciones Diferenciales",
        "icon": "query-stats",
    },
    {
        "id": "math_numerical_methods",
        "domain": "math",
        "name": "11. Métodos Numéricos",
        "icon": "data-array",
    },
    {
        "id": "math_statistics",
        "domain": "math",
        "name": "12. Estadística y Probabilidad",
        "icon": "bar-chart",
    },
    # Física
    {
        "id": "phys_kinematics_dynamics",
        "domain": "physics",
        "name": "1. Cinemática y Dinámica Newtoniana",
        "icon": "speed",
    },
    {
        "id": "phys_energy_gravitation",
        "domain": "physics",
        "name": "2. Trabajo, Energía, Momento y Gravitación",
        "icon": "fitness-center",
    },
    {
        "id": "phys_oscillations",
        "domain": "physics",
        "name": "3. Movimiento Oscilatorio",
        "icon": "graphic-eq",
    },
    {
        "id": "phys_waves_acoustics",
        "domain": "physics",
        "name": "4. Ondas Mecánicas y Acústica",
        "icon": "waves",
    },
    {
        "id": "phys_fluids",
        "domain": "physics",
        "name": "5. Mecánica de Fluidos",
        "icon": "water-drop",
    },
    {
        "id": "phys_analytical_relativity",
        "domain": "physics",
        "name": "6. Mecánica Analítica y Relativista",
        "icon": "auto-awesome",
    },
    {
        "id": "phys_thermodynamics",
        "domain": "physics",
        "name": "7. Termodinámica Clásica y Estadística",
        "icon": "bolt",
    },
    {
        "id": "phys_electromagnetism",
        "domain": "physics",
        "name": "8. Electromagnetismo y Circuitos",
        "icon": "electric-bolt",
    },
    {
        "id": "phys_optics",
        "domain": "physics",
        "name": "9. Óptica y Fotónica",
        "icon": "wb-sunny",
    },
    {
        "id": "phys_modern",
        "domain": "physics",
        "name": "10. Física Cuántica y Moderna",
        "icon": "atom",
    },
]


def _parse_preset(latex_str: str) -> MathTree:
    """Convierte dinámicamente un string LaTeX a un árbol MathTree en tiempo real.

    Utiliza el motor de `LaTeXParser` internamente para hidratar las plantillas
    de fórmulas célebres predefinidas.

    Args:
        latex_str: La cadena cruda del código LaTeX preestablecido.

    Returns:
        Instancia de `MathTree` estructurada con la fórmula parseada.
    """
    from src.core.parser import LaTeXParser

    return LaTeXParser.parse_to_tree(latex_str)


# Preset Example Formulas Catalog (Compendio Completo de Aritmética, Álgebra, Trigonometría, Cálculo, Estadística y Física)
# Preset Example Formulas Catalog (Compendio Completo Agrupado por Procedimiento)
PRESET_FORMULAS = [
    {
        "id": "math_arithmetic_propiedades_de_la_adici_n_y_multiplicaci_n",
        "domain": "math",
        "category": "math_arithmetic",
        "level": "NIVEL BÁSICO",
        "title": "Propiedades de la Adición y Multiplicación",
        "variations": [
            {
                "name": "Clausura / Cerradura",
                "description": "La adición y multiplicación de números reales siempre produce un número real",
                "latex": r"""a + b \in \mathbb{R}, \quad a \cdot b \in \mathbb{R}""",
                "builder": lambda: _parse_preset(
                    r"""a + b \in \mathbb{R}, \quad a \cdot b \in \mathbb{R}"""
                ),
            },
            {
                "name": "Propiedad Conmutativa",
                "description": "El orden de los sumandos o de los factores no altera el resultado",
                "latex": r"""a + b = b + a, \quad a \cdot b = b \cdot a""",
                "builder": lambda: _parse_preset(
                    r"""a + b = b + a, \quad a \cdot b = b \cdot a"""
                ),
            },
            {
                "name": "Propiedad Asociativa",
                "description": "La agrupación de sumandos o factores no altera el resultado final",
                "latex": r"""(a + b) + c = a + (b + c), \quad (a \cdot b) \cdot c = a \cdot (b \cdot c)""",
                "builder": lambda: _parse_preset(
                    r"""(a + b) + c = a + (b + c), \quad (a \cdot b) \cdot c = a \cdot (b \cdot c)"""
                ),
            },
            {
                "name": "Elemento Neutro",
                "description": "Neutro aditivo (0) y neutro multiplicativo (1)",
                "latex": r"""a + 0 = a, \quad a \cdot 1 = a""",
                "builder": lambda: _parse_preset(r"""a + 0 = a, \quad a \cdot 1 = a"""),
            },
            {
                "name": "Elemento Inverso",
                "description": "Inverso aditivo (-a) e inverso multiplicativo (1/a con a ≠ 0)",
                "latex": r"""a + (-a) = 0, \quad a \cdot \left(\frac{1}{a}\right) = 1""",
                "builder": lambda: _parse_preset(
                    r"""a + (-a) = 0, \quad a \cdot \left(\frac{1}{a}\right) = 1"""
                ),
            },
            {
                "name": "Propiedad Distributiva",
                "description": "Distributividad de la multiplicación respecto a la adición",
                "latex": r"""a \cdot (b + c) = a \cdot b + a \cdot c""",
                "builder": lambda: _parse_preset(
                    r"""a \cdot (b + c) = a \cdot b + a \cdot c"""
                ),
            },
        ],
    },
    {
        "id": "math_arithmetic_operaciones_con_fracciones",
        "domain": "math",
        "category": "math_arithmetic",
        "level": "NIVEL BÁSICO",
        "title": "Operaciones con Fracciones",
        "variations": [
            {
                "name": "Suma/Resta (Mismo Denominador)",
                "description": "Operación directa sobre los numeradores manteniendo el denominador común",
                "latex": r"""\frac{a}{c} \pm \frac{b}{c} = \frac{a \pm b}{c}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{a}{c} \pm \frac{b}{c} = \frac{a \pm b}{c}"""
                ),
            },
            {
                "name": "Suma/Resta (Distinto Denominador)",
                "description": "Reducción a común denominador mediante producto cruzado",
                "latex": r"""\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}"""
                ),
            },
            {
                "name": "Multiplicación de Fracciones",
                "description": "Producto horizontal directo de numeradores y denominadores",
                "latex": r"""\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}"""
                ),
            },
            {
                "name": "División de Fracciones",
                "description": "Cociente de fracciones mediante multiplicación cruzada o extremo por extremo",
                "latex": r"""\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a \cdot d}{b \cdot c}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a \cdot d}{b \cdot c}"""
                ),
            },
        ],
    },
    {
        "id": "math_arithmetic_porcentajes_y_proporcionalidad",
        "domain": "math",
        "category": "math_arithmetic",
        "level": "NIVEL BÁSICO",
        "title": "Porcentajes y Proporcionalidad",
        "variations": [
            {
                "name": "Tanto por Ciento",
                "description": "Cálculo del valor porcentual P correspondiente al r% de una cantidad C",
                "latex": r"""P = \frac{C \cdot r}{100}""",
                "builder": lambda: _parse_preset(r"""P = \frac{C \cdot r}{100}"""),
            },
            {
                "name": "Regla de Tres Simple Directa",
                "description": "Determinación de la incógnita x en proporciones directas a/b = c/x",
                "latex": r"""x = \frac{b \cdot c}{a}""",
                "builder": lambda: _parse_preset(r"""x = \frac{b \cdot c}{a}"""),
            },
        ],
    },
    {
        "id": "math_arithmetic_teor_a_de_n_meros_b_sica",
        "domain": "math",
        "category": "math_arithmetic",
        "level": "NIVEL INTERMEDIO",
        "title": "Teoría de Números Básica",
        "variations": [
            {
                "name": "Algoritmo de la División (Euclides)",
                "description": "Dividendo igual a divisor por cociente más residuo acotado",
                "latex": r"""D = d \cdot q + r, \quad 0 \le r < d""",
                "builder": lambda: _parse_preset(
                    r"""D = d \cdot q + r, \quad 0 \le r < d"""
                ),
            },
            {
                "name": "Relación MCD y MCM",
                "description": "El producto del MCD y el MCM de dos números enteros es igual al valor absoluto de su producto",
                "latex": r"""\operatorname{mcd}(a, b) \cdot \operatorname{mcm}(a, b) = |a \cdot b|""",
                "builder": lambda: _parse_preset(
                    r"""\operatorname{mcd}(a, b) \cdot \operatorname{mcm}(a, b) = |a \cdot b|"""
                ),
            },
        ],
    },
    {
        "id": "math_arithmetic_progresiones_aritm_ticas_pa",
        "domain": "math",
        "category": "math_arithmetic",
        "level": "NIVEL INTERMEDIO",
        "title": "Progresiones Aritméticas (PA)",
        "variations": [
            {
                "name": "Término General (PA)",
                "description": "Enésimo término en función del primer término a₁ y la diferencia d",
                "latex": r"""a_n = a_1 + (n - 1)d""",
                "builder": lambda: _parse_preset(r"""a_n = a_1 + (n - 1)d"""),
            },
            {
                "name": "Suma de Términos (PA)",
                "description": "Suma de los primeros n términos de una progresión aritmética",
                "latex": r"""S_n = \frac{n}{2} (a_1 + a_n)""",
                "builder": lambda: _parse_preset(r"""S_n = \frac{n}{2} (a_1 + a_n)"""),
            },
        ],
    },
    {
        "id": "math_arithmetic_progresiones_geom_tricas_pg",
        "domain": "math",
        "category": "math_arithmetic",
        "level": "NIVEL INTERMEDIO",
        "title": "Progresiones Geométricas (PG)",
        "variations": [
            {
                "name": "Término General (PG)",
                "description": "Enésimo término en función del primer término a₁ y la razón r",
                "latex": r"""a_n = a_1 \cdot r^{n - 1}""",
                "builder": lambda: _parse_preset(r"""a_n = a_1 \cdot r^{n - 1}"""),
            },
            {
                "name": "Suma de n Términos (PG)",
                "description": "Suma finita de los n primeros términos con razón r ≠ 1",
                "latex": r"""S_n = \frac{a_1(1 - r^n)}{1 - r}""",
                "builder": lambda: _parse_preset(
                    r"""S_n = \frac{a_1(1 - r^n)}{1 - r}"""
                ),
            },
            {
                "name": "Suma Infinita (PG)",
                "description": "Suma infinita convergente de una serie geométrica con |r| < 1",
                "latex": r"""S_\infty = \frac{a_1}{1 - r}""",
                "builder": lambda: _parse_preset(r"""S_\infty = \frac{a_1}{1 - r}"""),
            },
        ],
    },
    {
        "id": "math_arithmetic_aritm_tica_modular",
        "domain": "math",
        "category": "math_arithmetic",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Aritmética Modular",
        "variations": [
            {
                "name": "Congruencia Lineal",
                "description": "Definición fundamental de congruencia de enteros módulo m",
                "latex": r"""a \equiv b \pmod{m} \iff m \mid (a - b)""",
                "builder": lambda: _parse_preset(
                    r"""a \equiv b \pmod{m} \iff m \mid (a - b)"""
                ),
            },
            {
                "name": "Pequeño Teorema de Fermat",
                "description": "Potencia de exponente p-1 congruente con 1 módulo p primo cuando mcd(a, p) = 1",
                "latex": r"""a^{p - 1} \equiv 1 \pmod{p}""",
                "builder": lambda: _parse_preset(r"""a^{p - 1} \equiv 1 \pmod{p}"""),
            },
            {
                "name": "Teorema de Euler-Fermat",
                "description": "Generalización del teorema de Fermat para cualquier entero m con función φ de Euler",
                "latex": r"""a^{\varphi(m)} \equiv 1 \pmod{m}""",
                "builder": lambda: _parse_preset(
                    r"""a^{\varphi(m)} \equiv 1 \pmod{m}"""
                ),
            },
            {
                "name": "Función φ de Euler",
                "description": "Fórmula del producto de Euler para contar enteros coprimos menores o iguales a n",
                "latex": r"""\varphi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)""",
                "builder": lambda: _parse_preset(
                    r"""\varphi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)"""
                ),
            },
        ],
    },
    {
        "id": "math_arithmetic_teorema_chino_del_resto",
        "domain": "math",
        "category": "math_arithmetic",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Teorema Chino del Resto",
        "variations": [
            {
                "name": "Teorema Chino del Resto",
                "description": "Solución única módulo M para un sistema de congruencias con módulos coprimos dos a dos",
                "latex": r"""x \equiv a_i \pmod{m_i}, \quad M = \prod_{i=1}^{k} m_i""",
                "builder": lambda: _parse_preset(
                    r"""x \equiv a_i \pmod{m_i}, \quad M = \prod_{i=1}^{k} m_i"""
                ),
            },
        ],
    },
    {
        "id": "math_algebra_leyes_de_exponentes_y_radicales",
        "domain": "math",
        "category": "math_algebra",
        "level": "NIVEL BÁSICO",
        "title": "Leyes de Exponentes y Radicales",
        "variations": [
            {
                "name": "Producto de Bases Iguales",
                "description": "Al multiplicar potencias de la misma base, se mantiene la base y se suman los exponentes",
                "latex": r"""x^a \cdot x^b = x^{a + b}""",
                "builder": lambda: _parse_preset(r"""x^a \cdot x^b = x^{a + b}"""),
            },
            {
                "name": "Cociente de Bases Iguales",
                "description": "Al dividir potencias de la misma base, se mantiene la base y se restan los exponentes",
                "latex": r"""\frac{x^a}{x^b} = x^{a - b}""",
                "builder": lambda: _parse_preset(r"""\frac{x^a}{x^b} = x^{a - b}"""),
            },
            {
                "name": "Potencia de una Potencia",
                "description": "La potencia de una base elevada a otro exponente multiplica ambos exponentes",
                "latex": r"""(x^a)^b = x^{a \cdot b}""",
                "builder": lambda: _parse_preset(r"""(x^a)^b = x^{a \cdot b}"""),
            },
            {
                "name": "Potencia de un Producto",
                "description": "El exponente exterior se distribuye a cada factor del producto",
                "latex": r"""(x \cdot y)^a = x^a \cdot y^a""",
                "builder": lambda: _parse_preset(r"""(x \cdot y)^a = x^a \cdot y^a"""),
            },
            {
                "name": "Exponente Negativo",
                "description": "Inversión multiplicativa de la base elevada al exponente positivo (x ≠ 0)",
                "latex": r"""x^{-a} = \frac{1}{x^a}""",
                "builder": lambda: _parse_preset(r"""x^{-a} = \frac{1}{x^a}"""),
            },
            {
                "name": "Exponente Fraccionario",
                "description": "Equivalencia entre exponente fraccionario y radicación de orden b",
                "latex": r"""x^{\frac{a}{b}} = \sqrt[b]{x^a}""",
                "builder": lambda: _parse_preset(
                    r"""x^{\frac{a}{b}} = \sqrt[b]{x^a}"""
                ),
            },
            {
                "name": "Raíz de un Producto",
                "description": "La raíz enésima de un producto es igual al producto de las raíces enésimas individuales",
                "latex": r"""\sqrt[n]{x \cdot y} = \sqrt[n]{x} \cdot \sqrt[n]{y}""",
                "builder": lambda: _parse_preset(
                    r"""\sqrt[n]{x \cdot y} = \sqrt[n]{x} \cdot \sqrt[n]{y}"""
                ),
            },
        ],
    },
    {
        "id": "math_algebra_productos_notables_y_factorizaci_n",
        "domain": "math",
        "category": "math_algebra",
        "level": "NIVEL BÁSICO",
        "title": "Productos Notables y Factorización",
        "variations": [
            {
                "name": "Binomio al Cuadrado",
                "description": "Cuadrado del primer término más/menos el doble producto más el cuadrado del segundo",
                "latex": r"""(a \pm b)^2 = a^2 \pm 2ab + b^2""",
                "builder": lambda: _parse_preset(
                    r"""(a \pm b)^2 = a^2 \pm 2ab + b^2"""
                ),
            },
            {
                "name": "Diferencia de Cuadrados",
                "description": "Factorización clásica de la diferencia de cuadrados en producto de suma por diferencia",
                "latex": r"""a^2 - b^2 = (a + b)(a - b)""",
                "builder": lambda: _parse_preset(r"""a^2 - b^2 = (a + b)(a - b)"""),
            },
            {
                "name": "Binomio al Cubo",
                "description": "Expansión algebraica del cubo de una suma o diferencia",
                "latex": r"""(a \pm b)^3 = a^3 \pm 3a^2b + 3ab^2 \pm b^3""",
                "builder": lambda: _parse_preset(
                    r"""(a \pm b)^3 = a^3 \pm 3a^2b + 3ab^2 \pm b^3"""
                ),
            },
            {
                "name": "Suma de Cubos",
                "description": "Factorización de la suma de dos cubos perfectos",
                "latex": r"""a^3 + b^3 = (a + b)(a^2 - ab + b^2)""",
                "builder": lambda: _parse_preset(
                    r"""a^3 + b^3 = (a + b)(a^2 - ab + b^2)"""
                ),
            },
            {
                "name": "Diferencia de Cubos",
                "description": "Factorización de la diferencia de dos cubos perfectos",
                "latex": r"""a^3 - b^3 = (a - b)(a^2 + ab + b^2)""",
                "builder": lambda: _parse_preset(
                    r"""a^3 - b^3 = (a - b)(a^2 + ab + b^2)"""
                ),
            },
            {
                "name": "Trinomio al Cuadrado",
                "description": "Expansión del cuadrado de un trinomio a + b + c",
                "latex": r"""(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + ac + bc)""",
                "builder": lambda: _parse_preset(
                    r"""(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + ac + bc)"""
                ),
            },
        ],
    },
    {
        "id": "math_algebra_ecuaciones_lineales",
        "domain": "math",
        "category": "math_algebra",
        "level": "NIVEL BÁSICO",
        "title": "Ecuaciones Lineales",
        "variations": [
            {
                "name": "Ecuación Lineal",
                "description": "Forma general y despeje de la incógnita para ax + b = 0 con a ≠ 0",
                "latex": r"""ax + b = 0 \implies x = -\frac{b}{a}""",
                "builder": lambda: _parse_preset(
                    r"""ax + b = 0 \implies x = -\frac{b}{a}"""
                ),
            },
        ],
    },
    {
        "id": "math_algebra_ecuaciones_cuadr_ticas",
        "domain": "math",
        "category": "math_algebra",
        "level": "NIVEL INTERMEDIO",
        "title": "Ecuaciones Cuadráticas",
        "variations": [
            {
                "name": "Fórmula Cuadrática",
                "description": "Solución general para ecuaciones de segundo grado ax² + bx + c = 0",
                "latex": r"""x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}""",
                "builder": lambda: _parse_preset(
                    r"""x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"""
                ),
            },
            {
                "name": "Discriminante Cuadrático (Δ)",
                "description": "Cálculo del discriminante para clasificar raíces reales o complejas",
                "latex": r"""\Delta = b^2 - 4ac""",
                "builder": lambda: _parse_preset(r"""\Delta = b^2 - 4ac"""),
            },
            {
                "name": "Relaciones de Cardano-Vieta",
                "description": "Suma y producto de las raíces de una ecuación polinómica de segundo grado",
                "latex": r"""x_1 + x_2 = -\frac{b}{a}, \quad x_1 \cdot x_2 = \frac{c}{a}""",
                "builder": lambda: _parse_preset(
                    r"""x_1 + x_2 = -\frac{b}{a}, \quad x_1 \cdot x_2 = \frac{c}{a}"""
                ),
            },
        ],
    },
    {
        "id": "math_algebra_logaritmos",
        "domain": "math",
        "category": "math_algebra",
        "level": "NIVEL INTERMEDIO",
        "title": "Logaritmos",
        "variations": [
            {
                "name": "Definición de Logaritmo",
                "description": "Equivalencia fundamental entre función logarítmica y función exponencial",
                "latex": r"""\log_b(x) = y \iff b^y = x""",
                "builder": lambda: _parse_preset(r"""\log_b(x) = y \iff b^y = x"""),
            },
            {
                "name": "Logaritmo de un Producto",
                "description": "El logaritmo de un producto es la suma de los logaritmos de sus factores",
                "latex": r"""\log_b(x \cdot y) = \log_b(x) + \log_b(y)""",
                "builder": lambda: _parse_preset(
                    r"""\log_b(x \cdot y) = \log_b(x) + \log_b(y)"""
                ),
            },
            {
                "name": "Logaritmo de un Cociente",
                "description": "El logaritmo de una fracción es la resta entre el logaritmo del numerador y denominador",
                "latex": r"""\log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)""",
                "builder": lambda: _parse_preset(
                    r"""\log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)"""
                ),
            },
            {
                "name": "Logaritmo de una Potencia",
                "description": "El exponente de la potencia se transforma en factor multiplicador del logaritmo",
                "latex": r"""\log_b(x^k) = k \cdot \log_b(x)""",
                "builder": lambda: _parse_preset(
                    r"""\log_b(x^k) = k \cdot \log_b(x)"""
                ),
            },
            {
                "name": "Cambio de Base Logarítmica",
                "description": "Conversión de logaritmo en base b a logaritmo en una nueva base c",
                "latex": r"""\log_b(x) = \frac{\log_c(x)}{\log_c(b)}""",
                "builder": lambda: _parse_preset(
                    r"""\log_b(x) = \frac{\log_c(x)}{\log_c(b)}"""
                ),
            },
        ],
    },
    {
        "id": "math_algebra_teorema_del_binomio_newton",
        "domain": "math",
        "category": "math_algebra",
        "level": "NIVEL INTERMEDIO",
        "title": "Teorema del Binomio (Newton)",
        "variations": [
            {
                "name": "Teorema del Binomio",
                "description": "Expansión polinómica de (a + b)ⁿ mediante sumatoria y coeficientes combinatorios",
                "latex": r"""(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k""",
                "builder": lambda: _parse_preset(
                    r"""(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k"""
                ),
            },
        ],
    },
    {
        "id": "math_algebra_n_meros_complejos",
        "domain": "math",
        "category": "math_algebra",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Números Complejos",
        "variations": [
            {
                "name": "Forma Binómica y Unidad Imaginaria",
                "description": "Representación rectangular z = a + bi en el plano complejo con i² = -1",
                "latex": r"""z = a + bi, \quad i^2 = -1""",
                "builder": lambda: _parse_preset(r"""z = a + bi, \quad i^2 = -1"""),
            },
            {
                "name": "Módulo y Argumento Complejo",
                "description": "Cálculo del módulo r y el argumento angular θ de un número complejo",
                "latex": r"""|z| = r = \sqrt{a^2 + b^2}, \quad \theta = \arctan\left(\frac{b}{a}\right)""",
                "builder": lambda: _parse_preset(
                    r"""|z| = r = \sqrt{a^2 + b^2}, \quad \theta = \arctan\left(\frac{b}{a}\right)"""
                ),
            },
            {
                "name": "Forma Polar y Exponencial (Euler)",
                "description": "Representación trigonométrica y exponencial compleja según la fórmula de Euler",
                "latex": r"""z = r(\cos(\theta) + i\sin(\theta)) = r e^{i\theta}""",
                "builder": lambda: _parse_preset(
                    r"""z = r(\cos(\theta) + i\sin(\theta)) = r e^{i\theta}"""
                ),
            },
            {
                "name": "Teorema de De Moivre",
                "description": "Potenciación de números complejos en forma trigonométrica",
                "latex": r"""[r(\cos(\theta) + i\sin(\theta))]^n = r^n (\cos(n\theta) + i\sin(n\theta))""",
                "builder": lambda: _parse_preset(
                    r"""[r(\cos(\theta) + i\sin(\theta))]^n = r^n (\cos(n\theta) + i\sin(n\theta))"""
                ),
            },
            {
                "name": "Raíces Enésimas de un Complejo",
                "description": "Fórmula para las n raíces complejas distribuidas en el plano de Argand",
                "latex": r"""z_k = \sqrt[n]{r} \, e^{i \frac{\theta + 2k\pi}{n}}, \quad k = 0, 1, \dots, n-1""",
                "builder": lambda: _parse_preset(
                    r"""z_k = \sqrt[n]{r} \, e^{i \frac{\theta + 2k\pi}{n}}, \quad k = 0, 1, \dots, n-1"""
                ),
            },
        ],
    },
    {
        "id": "math_trigonometry_razones_trigonom_tricas_en_el_tri_ngulo_rect_ngulo",
        "domain": "math",
        "category": "math_trigonometry",
        "level": "NIVEL BÁSICO",
        "title": "Razones Trigonométricas en el Triángulo Rectángulo",
        "variations": [
            {
                "name": "Razones Principales (Triángulo Rectángulo)",
                "description": "Definición de seno, coseno y tangente como cocientes de lados",
                "latex": r"""\sin(\theta) = \frac{\text{CO}}{H}, \quad \cos(\theta) = \frac{\text{CA}}{H}, \quad \tan(\theta) = \frac{\text{CO}}{\text{CA}}""",
                "builder": lambda: _parse_preset(
                    r"""\sin(\theta) = \frac{\text{CO}}{H}, \quad \cos(\theta) = \frac{\text{CA}}{H}, \quad \tan(\theta) = \frac{\text{CO}}{\text{CA}}"""
                ),
            },
            {
                "name": "Razones Recíprocas (Csc, Sec, Cot)",
                "description": "Definición de las razones trigonométricas recíprocas",
                "latex": r"""\csc(\theta) = \frac{1}{\sin(\theta)}, \quad \sec(\theta) = \frac{1}{\cos(\theta)}, \quad \cot(\theta) = \frac{1}{\tan(\theta)}""",
                "builder": lambda: _parse_preset(
                    r"""\csc(\theta) = \frac{1}{\sin(\theta)}, \quad \sec(\theta) = \frac{1}{\cos(\theta)}, \quad \cot(\theta) = \frac{1}{\tan(\theta)}"""
                ),
            },
        ],
    },
    {
        "id": "math_trigonometry_identidades_trigonom_tricas_fundamentales",
        "domain": "math",
        "category": "math_trigonometry",
        "level": "NIVEL BÁSICO",
        "title": "Identidades Trigonométricas Fundamentales",
        "variations": [
            {
                "name": "Identidades por Cociente",
                "description": "Tangente y cotangente expresadas en función de seno y coseno",
                "latex": r"""\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}, \quad \cot(\theta) = \frac{\cos(\theta)}{\sin(\theta)}""",
                "builder": lambda: _parse_preset(
                    r"""\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}, \quad \cot(\theta) = \frac{\cos(\theta)}{\sin(\theta)}"""
                ),
            },
            {
                "name": "Identidad Pitagórica Principal",
                "description": "Relación fundamental entre el seno y coseno al cuadrado",
                "latex": r"""\sin^2(\theta) + \cos^2(\theta) = 1""",
                "builder": lambda: _parse_preset(
                    r"""\sin^2(\theta) + \cos^2(\theta) = 1"""
                ),
            },
            {
                "name": "Identidades Pitagóricas Derivadas",
                "description": "Relaciones pitagóricas para secante y cosecante al cuadrado",
                "latex": r"""1 + \tan^2(\theta) = \sec^2(\theta), \quad 1 + \cot^2(\theta) = \csc^2(\theta)""",
                "builder": lambda: _parse_preset(
                    r"""1 + \tan^2(\theta) = \sec^2(\theta), \quad 1 + \cot^2(\theta) = \csc^2(\theta)"""
                ),
            },
        ],
    },
    {
        "id": "math_trigonometry_f_rmulas_de_suma_y_diferencia_de_ngulos",
        "domain": "math",
        "category": "math_trigonometry",
        "level": "NIVEL INTERMEDIO",
        "title": "Fórmulas de Suma y Diferencia de Ángulos",
        "variations": [
            {
                "name": "Seno de Suma y Diferencia",
                "description": "Expansión del seno de la suma o resta de dos ángulos",
                "latex": r"""\sin(\alpha \pm \beta) = \sin(\alpha)\cos(\beta) \pm \cos(\alpha)\sin(\beta)""",
                "builder": lambda: _parse_preset(
                    r"""\sin(\alpha \pm \beta) = \sin(\alpha)\cos(\beta) \pm \cos(\alpha)\sin(\beta)"""
                ),
            },
            {
                "name": "Coseno de Suma y Diferencia",
                "description": "Expansión del coseno de la suma o resta de dos ángulos",
                "latex": r"""\cos(\alpha \pm \beta) = \cos(\alpha)\cos(\beta) \mp \sin(\alpha)\sin(\beta)""",
                "builder": lambda: _parse_preset(
                    r"""\cos(\alpha \pm \beta) = \cos(\alpha)\cos(\beta) \mp \sin(\alpha)\sin(\beta)"""
                ),
            },
            {
                "name": "Tangente de Suma y Diferencia",
                "description": "Expansión de la tangente de la suma o resta de dos ángulos",
                "latex": r"""\tan(\alpha \pm \beta) = \frac{\tan(\alpha) \pm \tan(\beta)}{1 \mp \tan(\alpha)\tan(\beta)}""",
                "builder": lambda: _parse_preset(
                    r"""\tan(\alpha \pm \beta) = \frac{\tan(\alpha) \pm \tan(\beta)}{1 \mp \tan(\alpha)\tan(\beta)}"""
                ),
            },
        ],
    },
    {
        "id": "math_trigonometry_ngulo_doble_y_ngulo_mitad",
        "domain": "math",
        "category": "math_trigonometry",
        "level": "NIVEL INTERMEDIO",
        "title": "Ángulo Doble y Ángulo Mitad",
        "variations": [
            {
                "name": "Ángulo Doble (Seno y Coseno)",
                "description": "Identidades trigonométricas de 2θ para seno y coseno",
                "latex": r"""\sin(2\theta) = 2\sin(\theta)\cos(\theta), \quad \cos(2\theta) = \cos^2(\theta) - \sin^2(\theta)""",
                "builder": lambda: _parse_preset(
                    r"""\sin(2\theta) = 2\sin(\theta)\cos(\theta), \quad \cos(2\theta) = \cos^2(\theta) - \sin^2(\theta)"""
                ),
            },
            {
                "name": "Tangente del Ángulo Doble",
                "description": "Identidad trigonométrica para tan(2θ)",
                "latex": r"""\tan(2\theta) = \frac{2\tan(\theta)}{1 - \tan^2(\theta)}""",
                "builder": lambda: _parse_preset(
                    r"""\tan(2\theta) = \frac{2\tan(\theta)}{1 - \tan^2(\theta)}"""
                ),
            },
            {
                "name": "Ángulo Mitad (Seno y Coseno)",
                "description": "Fórmulas de ángulo mitad θ/2 para seno y coseno",
                "latex": r"""\sin\left(\frac{\theta}{2}\right) = \pm \sqrt{\frac{1 - \cos(\theta)}{2}}, \quad \cos\left(\frac{\theta}{2}\right) = \pm \sqrt{\frac{1 + \cos(\theta)}{2}}""",
                "builder": lambda: _parse_preset(
                    r"""\sin\left(\frac{\theta}{2}\right) = \pm \sqrt{\frac{1 - \cos(\theta)}{2}}, \quad \cos\left(\frac{\theta}{2}\right) = \pm \sqrt{\frac{1 + \cos(\theta)}{2}}"""
                ),
            },
            {
                "name": "Tangente del Ángulo Mitad",
                "description": "Fórmulas racionales para la tangente del ángulo mitad",
                "latex": r"""\tan\left(\frac{\theta}{2}\right) = \frac{\sin(\theta)}{1 + \cos(\theta)} = \frac{1 - \cos(\theta)}{\sin(\theta)}""",
                "builder": lambda: _parse_preset(
                    r"""\tan\left(\frac{\theta}{2}\right) = \frac{\sin(\theta)}{1 + \cos(\theta)} = \frac{1 - \cos(\theta)}{\sin(\theta)}"""
                ),
            },
        ],
    },
    {
        "id": "math_trigonometry_leyes_de_tri_ngulos_oblicu_ngulos",
        "domain": "math",
        "category": "math_trigonometry",
        "level": "NIVEL INTERMEDIO",
        "title": "Leyes de Triángulos Oblicuángulos",
        "variations": [
            {
                "name": "Ley de Senos",
                "description": "Proporcionalidad entre lados y senos de ángulos opuestos en cualquier triángulo",
                "latex": r"""\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)} = 2R""",
                "builder": lambda: _parse_preset(
                    r"""\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)} = 2R"""
                ),
            },
            {
                "name": "Ley de Cosenos",
                "description": "Relación métrica entre los tres lados de un triángulo y el coseno de uno de sus ángulos",
                "latex": r"""c^2 = a^2 + b^2 - 2ab \cos(\gamma)""",
                "builder": lambda: _parse_preset(
                    r"""c^2 = a^2 + b^2 - 2ab \cos(\gamma)"""
                ),
            },
            {
                "name": "Área Triangular Trigonométrica",
                "description": "Área de un triángulo en función de dos lados y el seno del ángulo comprendido",
                "latex": r"""A = \frac{1}{2} a b \sin(C)""",
                "builder": lambda: _parse_preset(r"""A = \frac{1}{2} a b \sin(C)"""),
            },
            {
                "name": "Fórmula de Herón",
                "description": "Área de un triángulo a partir de sus tres lados y el semiperímetro s",
                "latex": r"""A = \sqrt{s(s-a)(s-b)(s-c)}, \quad s = \frac{a+b+c}{2}""",
                "builder": lambda: _parse_preset(
                    r"""A = \sqrt{s(s-a)(s-b)(s-c)}, \quad s = \frac{a+b+c}{2}"""
                ),
            },
            {
                "name": "Volumen de una Esfera",
                "description": "Volumen de una esfera tridimensional de radio r",
                "latex": r"""V = \frac{4}{3} \pi r^3""",
                "builder": lambda: _parse_preset(r"""V = \frac{4}{3} \pi r^3"""),
            },
        ],
    },
    {
        "id": "math_trigonometry_transformaciones_de_suma_a_producto_prostaf_resis",
        "domain": "math",
        "category": "math_trigonometry",
        "level": "NIVEL INTERMEDIO",
        "title": "Transformaciones de Suma a Producto (Prostaféresis)",
        "variations": [
            {
                "name": "Suma y Resta de Senos",
                "description": "Fórmula de prostaféresis para convertir suma/resta de senos a producto",
                "latex": r"""\sin(\alpha) \pm \sin(\beta) = 2 \sin\left(\frac{\alpha \pm \beta}{2}\right) \cos\left(\frac{\alpha \mp \beta}{2}\right)""",
                "builder": lambda: _parse_preset(
                    r"""\sin(\alpha) \pm \sin(\beta) = 2 \sin\left(\frac{\alpha \pm \beta}{2}\right) \cos\left(\frac{\alpha \mp \beta}{2}\right)"""
                ),
            },
            {
                "name": "Suma de Cosenos",
                "description": "Fórmula de prostaféresis para convertir la suma de cosenos a producto",
                "latex": r"""\cos(\alpha) + \cos(\beta) = 2 \cos\left(\frac{\alpha + \beta}{2}\right) \cos\left(\frac{\alpha - \beta}{2}\right)""",
                "builder": lambda: _parse_preset(
                    r"""\cos(\alpha) + \cos(\beta) = 2 \cos\left(\frac{\alpha + \beta}{2}\right) \cos\left(\frac{\alpha - \beta}{2}\right)"""
                ),
            },
            {
                "name": "Diferencia de Cosenos",
                "description": "Fórmula de prostaféresis para convertir la resta de cosenos a producto de senos",
                "latex": r"""\cos(\alpha) - \cos(\beta) = -2 \sin\left(\frac{\alpha + \beta}{2}\right) \sin\left(\frac{\alpha - \beta}{2}\right)""",
                "builder": lambda: _parse_preset(
                    r"""\cos(\alpha) - \cos(\beta) = -2 \sin\left(\frac{\alpha + \beta}{2}\right) \sin\left(\frac{\alpha - \beta}{2}\right)"""
                ),
            },
        ],
    },
    {
        "id": "math_trigonometry_transformaciones_de_producto_a_suma",
        "domain": "math",
        "category": "math_trigonometry",
        "level": "NIVEL INTERMEDIO",
        "title": "Transformaciones de Producto a Suma",
        "variations": [
            {
                "name": "Producto Seno-Coseno a Suma",
                "description": "Transformación de producto de seno y coseno a suma de senos",
                "latex": r"""2\sin(\alpha)\cos(\beta) = \sin(\alpha + \beta) + \sin(\alpha - \beta)""",
                "builder": lambda: _parse_preset(
                    r"""2\sin(\alpha)\cos(\beta) = \sin(\alpha + \beta) + \sin(\alpha - \beta)"""
                ),
            },
            {
                "name": "Producto Coseno-Coseno a Suma",
                "description": "Transformación de producto de cosenos a suma de cosenos",
                "latex": r"""2\cos(\alpha)\cos(\beta) = \cos(\alpha + \beta) + \cos(\alpha - \beta)""",
                "builder": lambda: _parse_preset(
                    r"""2\cos(\alpha)\cos(\beta) = \cos(\alpha + \beta) + \cos(\alpha - \beta)"""
                ),
            },
            {
                "name": "Producto Seno-Seno a Suma",
                "description": "Transformación de producto de senos a resta de cosenos",
                "latex": r"""2\sin(\alpha)\sin(\beta) = \cos(\alpha - \beta) - \cos(\alpha + \beta)""",
                "builder": lambda: _parse_preset(
                    r"""2\sin(\alpha)\sin(\beta) = \cos(\alpha - \beta) - \cos(\alpha + \beta)"""
                ),
            },
        ],
    },
    {
        "id": "math_trigonometry_definici_n_compleja_de_funciones_circulares_f_rmula_de_euler",
        "domain": "math",
        "category": "math_trigonometry",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Definición Compleja de Funciones Circulares (Fórmula de Euler)",
        "variations": [
            {
                "name": "Identidad de Euler Trigonométrica",
                "description": "Exponencial compleja expresada en combinación lineal de coseno y seno",
                "latex": r"""e^{i\theta} = \cos(\theta) + i\sin(\theta)""",
                "builder": lambda: _parse_preset(
                    r"""e^{i\theta} = \cos(\theta) + i\sin(\theta)"""
                ),
            },
            {
                "name": "Seno y Coseno Complejos",
                "description": "Definición de funciones circulares en el plano complejo z mediante exponenciales",
                "latex": r"""\sin(z) = \frac{e^{iz} - e^{-iz}}{2i}, \quad \cos(z) = \frac{e^{iz} + e^{-iz}}{2}""",
                "builder": lambda: _parse_preset(
                    r"""\sin(z) = \frac{e^{iz} - e^{-iz}}{2i}, \quad \cos(z) = \frac{e^{iz} + e^{-iz}}{2}"""
                ),
            },
            {
                "name": "Tangente Compleja",
                "description": "Definición de la tangente en términos de exponenciales complejas",
                "latex": r"""\tan(z) = \frac{e^{iz} - e^{-iz}}{i(e^{iz} + e^{-iz})}""",
                "builder": lambda: _parse_preset(
                    r"""\tan(z) = \frac{e^{iz} - e^{-iz}}{i(e^{iz} + e^{-iz})}"""
                ),
            },
        ],
    },
    {
        "id": "math_trigonometry_funciones_hiperb_licas",
        "domain": "math",
        "category": "math_trigonometry",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Funciones Hiperbólicas",
        "variations": [
            {
                "name": "Seno y Coseno Hiperbólico",
                "description": "Definición de sinh(x) y cosh(x) mediante funciones exponenciales reales",
                "latex": r"""\sinh(x) = \frac{e^x - e^{-x}}{2}, \quad \cosh(x) = \frac{e^x + e^{-x}}{2}""",
                "builder": lambda: _parse_preset(
                    r"""\sinh(x) = \frac{e^x - e^{-x}}{2}, \quad \cosh(x) = \frac{e^x + e^{-x}}{2}"""
                ),
            },
            {
                "name": "Tangente Hiperbólica",
                "description": "Cociente entre sinh(x) y cosh(x) expresado en exponenciales",
                "latex": r"""\tanh(x) = \frac{\sinh(x)}{\cosh(x)} = \frac{e^x - e^{-x}}{e^x + e^{-x}}""",
                "builder": lambda: _parse_preset(
                    r"""\tanh(x) = \frac{\sinh(x)}{\cosh(x)} = \frac{e^x - e^{-x}}{e^x + e^{-x}}"""
                ),
            },
            {
                "name": "Identidades Hiperbólicas Fundamentales",
                "description": "Relación pitagórica hiperbólica fundamental y derivada",
                "latex": r"""\cosh^2(x) - \sinh^2(x) = 1, \quad 1 - \tanh^2(x) = \operatorname{sech}^2(x)""",
                "builder": lambda: _parse_preset(
                    r"""\cosh^2(x) - \sinh^2(x) = 1, \quad 1 - \tanh^2(x) = \operatorname{sech}^2(x)"""
                ),
            },
        ],
    },
    {
        "id": "math_trigonometry_relaci_n_entre_funciones_circulares_e_hiperb_licas",
        "domain": "math",
        "category": "math_trigonometry",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Relación entre Funciones Circulares e Hiperbólicas",
        "variations": [
            {
                "name": "Circulares con Argumento Imaginario (iz)",
                "description": "Conexión directa entre funciones circulares evaluadas en iz e hiperbólicas",
                "latex": r"""\sin(iz) = i\sinh(z), \quad \cos(iz) = \cosh(z)""",
                "builder": lambda: _parse_preset(
                    r"""\sin(iz) = i\sinh(z), \quad \cos(iz) = \cosh(z)"""
                ),
            },
            {
                "name": "Hiperbólicas con Argumento Imaginario (iz)",
                "description": "Conexión directa entre funciones hiperbólicas evaluadas en iz y circulares",
                "latex": r"""\sinh(iz) = i\sin(z), \quad \cosh(iz) = \cos(z)""",
                "builder": lambda: _parse_preset(
                    r"""\sinh(iz) = i\sin(z), \quad \cosh(iz) = \cos(z)"""
                ),
            },
        ],
    },
    {
        "id": "math_trigonometry_desarrollo_en_series_de_potencias_taylor_maclaurin",
        "domain": "math",
        "category": "math_trigonometry",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Desarrollo en Series de Potencias (Taylor / Maclaurin)",
        "variations": [
            {
                "name": "Series de Taylor (Seno y Coseno)",
                "description": "Desarrollo en series de Maclaurin para sin(x) y cos(x) centradas en x = 0",
                "latex": r"""\sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}, \quad \cos(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}""",
                "builder": lambda: _parse_preset(
                    r"""\sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}, \quad \cos(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}"""
                ),
            },
            {
                "name": "Series de Taylor (Sinh y Cosh)",
                "description": "Desarrollo en series de potencias para sinh(x) y cosh(x) centradas en x = 0",
                "latex": r"""\sinh(x) = \sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!}, \quad \cosh(x) = \sum_{n=0}^{\infty} \frac{x^{2n}}{(2n)!}""",
                "builder": lambda: _parse_preset(
                    r"""\sinh(x) = \sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!}, \quad \cosh(x) = \sum_{n=0}^{\infty} \frac{x^{2n}}{(2n)!}"""
                ),
            },
        ],
    },
    {
        "id": "math_geometry_per_metros_y_reas_de_figuras_planas_2d",
        "domain": "math",
        "category": "math_geometry",
        "level": "NIVEL BÁSICO",
        "title": "Perímetros y Áreas de Figuras Planas (2D)",
        "variations": [
            {
                "name": "Triángulo (General)",
                "description": "Perímetro P = a + b + c y Área A = (b · h) / 2",
                "latex": r"""P = a + b + c, \quad A = \frac{b \cdot h}{2}""",
                "builder": lambda: _parse_preset(
                    r"""P = a + b + c, \quad A = \frac{b \cdot h}{2}"""
                ),
            },
            {
                "name": "Triángulo Equilátero",
                "description": "Área y altura en función del lado l",
                "latex": r"""A = \frac{\sqrt{3}}{4} l^2, \quad h = \frac{\sqrt{3}}{2} l""",
                "builder": lambda: _parse_preset(
                    r"""A = \frac{\sqrt{3}}{4} l^2, \quad h = \frac{\sqrt{3}}{2} l"""
                ),
            },
            {
                "name": "Cuadrado",
                "description": "Perímetro P = 4l y Área A = l^2 = d^2 / 2",
                "latex": r"""P = 4l, \quad A = l^2 = \frac{d^2}{2}""",
                "builder": lambda: _parse_preset(
                    r"""P = 4l, \quad A = l^2 = \frac{d^2}{2}"""
                ),
            },
            {
                "name": "Rectángulo",
                "description": "Perímetro P = 2(b + h) y Área A = b · h",
                "latex": r"""P = 2(b + h), \quad A = b \cdot h""",
                "builder": lambda: _parse_preset(
                    r"""P = 2(b + h), \quad A = b \cdot h"""
                ),
            },
            {
                "name": "Paralelogramo",
                "description": "Área A = b · h",
                "latex": r"""A = b \cdot h""",
                "builder": lambda: _parse_preset(r"""A = b \cdot h"""),
            },
            {
                "name": "Rombo",
                "description": "Perímetro P = 4l y Área A = (D · d) / 2",
                "latex": r"""P = 4l, \quad A = \frac{D \cdot d}{2}""",
                "builder": lambda: _parse_preset(
                    r"""P = 4l, \quad A = \frac{D \cdot d}{2}"""
                ),
            },
            {
                "name": "Trapecio",
                "description": "Área A = ((B + b) · h) / 2",
                "latex": r"""A = \frac{(B + b) \cdot h}{2}""",
                "builder": lambda: _parse_preset(r"""A = \frac{(B + b) \cdot h}{2}"""),
            },
            {
                "name": "Polígono Regular (n lados)",
                "description": "Perímetro P = n · l y Área A = (P · a_p) / 2",
                "latex": r"""P = n \cdot l, \quad A = \frac{P \cdot a_p}{2}""",
                "builder": lambda: _parse_preset(
                    r"""P = n \cdot l, \quad A = \frac{P \cdot a_p}{2}"""
                ),
            },
            {
                "name": "Círculo",
                "description": "Longitud de circunferencia C = 2πr y Área A = π r^2",
                "latex": r"""C = 2\pi r, \quad A = \pi r^2""",
                "builder": lambda: _parse_preset(r"""C = 2\pi r, \quad A = \pi r^2"""),
            },
            {
                "name": "Sector Circular",
                "description": "Longitud de arco s = r · θ y Área A = (1/2) r^2 θ",
                "latex": r"""s = r\theta, \quad A = \frac{1}{2} r^2 \theta""",
                "builder": lambda: _parse_preset(
                    r"""s = r\theta, \quad A = \frac{1}{2} r^2 \theta"""
                ),
            },
            {
                "name": "Corona Circular",
                "description": "Área entre dos circunferencias concéntricas",
                "latex": r"""A = \pi(R^2 - r^2)""",
                "builder": lambda: _parse_preset(r"""A = \pi(R^2 - r^2)"""),
            },
        ],
    },
    {
        "id": "math_geometry_propiedades_angulares_y_pol_gonos",
        "domain": "math",
        "category": "math_geometry",
        "level": "NIVEL BÁSICO",
        "title": "Propiedades Angulares y Polígonos",
        "variations": [
            {
                "name": "Teorema de Pitágoras",
                "description": "Relación entre catetos e hipotenusa en triángulo rectángulo",
                "latex": r"""a^2 + b^2 = c^2""",
                "builder": lambda: _parse_preset(r"""a^2 + b^2 = c^2"""),
            },
            {
                "name": "Suma de Ángulos Internos del Triángulo",
                "description": "La suma de los ángulos interiores es 180° (π rad)",
                "latex": r"""\alpha + \beta + \gamma = 180^\circ""",
                "builder": lambda: _parse_preset(
                    r"""\alpha + \beta + \gamma = 180^\circ"""
                ),
            },
            {
                "name": "Suma de Ángulos Internos de un Polígono",
                "description": "Suma de ángulos interiores para polígono de n lados",
                "latex": r"""S_{\text{int}} = (n - 2) \cdot 180^\circ""",
                "builder": lambda: _parse_preset(
                    r"""S_{\text{int}} = (n - 2) \cdot 180^\circ"""
                ),
            },
            {
                "name": "Ángulo Interior de Polígono Regular",
                "description": "Medida de cada ángulo interior en polígono regular",
                "latex": r"""\theta_{\text{int}} = \frac{(n - 2) \cdot 180^\circ}{n}""",
                "builder": lambda: _parse_preset(
                    r"""\theta_{\text{int}} = \frac{(n - 2) \cdot 180^\circ}{n}"""
                ),
            },
            {
                "name": "Número Total de Diagonales",
                "description": "Total de diagonales que pueden trazarse en polígono de n lados",
                "latex": r"""N_d = \frac{n(n - 3)}{2}""",
                "builder": lambda: _parse_preset(r"""N_d = \frac{n(n - 3)}{2}"""),
            },
        ],
    },
    {
        "id": "math_geometry_geometr_a_del_espacio_reas_y_vol_menes_3d",
        "domain": "math",
        "category": "math_geometry",
        "level": "NIVEL INTERMEDIO",
        "title": "Geometría del Espacio (Áreas y Volúmenes 3D)",
        "variations": [
            {
                "name": "Prisma Recto",
                "description": "Área lateral A_L = P_{base} · h y Volumen V = A_{base} · h",
                "latex": r"""A_L = P_{\text{base}} \cdot h, \quad V = A_{\text{base}} \cdot h""",
                "builder": lambda: _parse_preset(
                    r"""A_L = P_{\text{base}} \cdot h, \quad V = A_{\text{base}} \cdot h"""
                ),
            },
            {
                "name": "Cilindro Circular Recto",
                "description": "Área total A_T = 2πr(h + r) y Volumen V = π r^2 h",
                "latex": r"""A_T = 2\pi r(h + r), \quad V = \pi r^2 h""",
                "builder": lambda: _parse_preset(
                    r"""A_T = 2\pi r(h + r), \quad V = \pi r^2 h"""
                ),
            },
            {
                "name": "Pirámide",
                "description": "Volumen V = (1/3) A_{base} · h",
                "latex": r"""V = \frac{1}{3} A_{\text{base}} \cdot h""",
                "builder": lambda: _parse_preset(
                    r"""V = \frac{1}{3} A_{\text{base}} \cdot h"""
                ),
            },
            {
                "name": "Cono Circular Recto",
                "description": "Generatriz g = √(r^2 + h^2), Área A_T = πr(g + r), Volumen V = (1/3)π r^2 h",
                "latex": r"""g = \sqrt{r^2 + h^2}, \quad A_T = \pi r(g + r), \quad V = \frac{1}{3} \pi r^2 h""",
                "builder": lambda: _parse_preset(
                    r"""g = \sqrt{r^2 + h^2}, \quad A_T = \pi r(g + r), \quad V = \frac{1}{3} \pi r^2 h"""
                ),
            },
            {
                "name": "Tronco de Cono",
                "description": "Volumen de un tronco de cono circular recto",
                "latex": r"""V = \frac{1}{3} \pi h (R^2 + r^2 + R \cdot r)""",
                "builder": lambda: _parse_preset(
                    r"""V = \frac{1}{3} \pi h (R^2 + r^2 + R \cdot r)"""
                ),
            },
            {
                "name": "Esfera",
                "description": "Área superficial A = 4π r^2 y Volumen V = (4/3) π r^3",
                "latex": r"""A = 4\pi r^2, \quad V = \frac{4}{3} \pi r^3""",
                "builder": lambda: _parse_preset(
                    r"""A = 4\pi r^2, \quad V = \frac{4}{3} \pi r^3"""
                ),
            },
            {
                "name": "Casquete Esférico",
                "description": "Área A = 2π r h y Volumen V = (1/3) π h^2 (3r - h)",
                "latex": r"""A = 2\pi r h, \quad V = \frac{1}{3} \pi h^2 (3r - h)""",
                "builder": lambda: _parse_preset(
                    r"""A = 2\pi r h, \quad V = \frac{1}{3} \pi h^2 (3r - h)"""
                ),
            },
        ],
    },
    {
        "id": "math_geometry_teoremas_m_tricos_y_proporcionalidad",
        "domain": "math",
        "category": "math_geometry",
        "level": "NIVEL INTERMEDIO",
        "title": "Teoremas Métricos y Proporcionalidad",
        "variations": [
            {
                "name": "Teorema de Tales",
                "description": "Proporcionalidad de segmentos determinados por rectas paralelas",
                "latex": r"""\frac{AB}{BC} = \frac{DE}{EF}""",
                "builder": lambda: _parse_preset(r"""\frac{AB}{BC} = \frac{DE}{EF}"""),
            },
            {
                "name": "Teorema de la Bisectriz Interior",
                "description": "Proporción de los lados adyacentes a los segmentos en la base",
                "latex": r"""\frac{a}{b} = \frac{c_1}{c_2}""",
                "builder": lambda: _parse_preset(r"""\frac{a}{b} = \frac{c_1}{c_2}"""),
            },
            {
                "name": "Relaciones Métricas en Triángulo Rectángulo",
                "description": "Relaciones de altura sobre hipotenusa y proyecciones",
                "latex": r"""h^2 = m \cdot n, \quad a^2 = c \cdot m, \quad b^2 = c \cdot n, \quad a \cdot b = c \cdot h""",
                "builder": lambda: _parse_preset(
                    r"""h^2 = m \cdot n, \quad a^2 = c \cdot m, \quad b^2 = c \cdot n, \quad a \cdot b = c \cdot h"""
                ),
            },
            {
                "name": "Potencia de un Punto",
                "description": "Teorema de cuerdas, secantes y tangentes",
                "latex": r"""PA \cdot PB = PC \cdot PD, \quad PT^2 = PA \cdot PB""",
                "builder": lambda: _parse_preset(
                    r"""PA \cdot PB = PC \cdot PD, \quad PT^2 = PA \cdot PB"""
                ),
            },
            {
                "name": "Teorema de Ceva",
                "description": "Condición necesaria y suficiente para cevianas concurrentes",
                "latex": r"""\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1""",
                "builder": lambda: _parse_preset(
                    r"""\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1"""
                ),
            },
            {
                "name": "Teorema de Menelao",
                "description": "Relación métrica para puntos colineales sobre los lados de un triángulo",
                "latex": r"""\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1""",
                "builder": lambda: _parse_preset(
                    r"""\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1"""
                ),
            },
        ],
    },
    {
        "id": "math_geometry_geometr_a_no_euclidiana_y_topolog_a_b_sica",
        "domain": "math",
        "category": "math_geometry",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Geometría no Euclidiana y Topología Básica",
        "variations": [
            {
                "name": "Característica de Euler-Poincaré",
                "description": "Relación para poliedros convexos: Vértices - Aristas + Caras = 2",
                "latex": r"""V - E + F = 2""",
                "builder": lambda: _parse_preset(r"""V - E + F = 2"""),
            },
            {
                "name": "Exceso Esférico",
                "description": "Diferencia entre la suma de ángulos de un triángulo esférico y π",
                "latex": r"""E = \alpha + \beta + \gamma - \pi""",
                "builder": lambda: _parse_preset(
                    r"""E = \alpha + \beta + \gamma - \pi"""
                ),
            },
            {
                "name": "Área de un Triángulo Esférico",
                "description": "Fórmula de Girard para el área de un triángulo sobre la esfera",
                "latex": r"""A = R^2 E = R^2 (\alpha + \beta + \gamma - \pi)""",
                "builder": lambda: _parse_preset(
                    r"""A = R^2 E = R^2 (\alpha + \beta + \gamma - \pi)"""
                ),
            },
            {
                "name": "Curvatura Gaussiana",
                "description": "Producto de las curvaturas principales k_1 y k_2",
                "latex": r"""K = k_1 \cdot k_2""",
                "builder": lambda: _parse_preset(r"""K = k_1 \cdot k_2"""),
            },
            {
                "name": "Teorema de Gauss-Bonnet",
                "description": "Relación entre curvatura intrínseca y topología (característica de Euler χ)",
                "latex": r"""\iint_M K \, dA + \oint_{\partial M} k_g \, ds = 2\pi \chi(M)""",
                "builder": lambda: _parse_preset(
                    r"""\iint_M K \, dA + \oint_{\partial M} k_g \, ds = 2\pi \chi(M)"""
                ),
            },
            {
                "name": "Razón Doble (Cross-Ratio)",
                "description": "Invariante proyectivo para cuatro puntos colineales",
                "latex": r"""(A, B; C, D) = \frac{(c - a)(d - b)}{(c - b)(d - a)}""",
                "builder": lambda: _parse_preset(
                    r"""(A, B; C, D) = \frac{(c - a)(d - b)}{(c - b)(d - a)}"""
                ),
            },
        ],
    },
    {
        "id": "math_analytic_geom_plano_cartesiano_2d",
        "domain": "math",
        "category": "math_analytic_geom",
        "level": "NIVEL BÁSICO",
        "title": "Plano Cartesiano (2D)",
        "variations": [
            {
                "name": "Distancia entre Dos Puntos (2D)",
                "description": "Distancia euclidiana entre P_1(x_1, y_1) y P_2(x_2, y_2)",
                "latex": r"""d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}""",
                "builder": lambda: _parse_preset(
                    r"""d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}"""
                ),
            },
            {
                "name": "Punto Medio de un Segmento",
                "description": "Coordenadas del punto medio M entre dos puntos",
                "latex": r"""M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)""",
                "builder": lambda: _parse_preset(
                    r"""M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)"""
                ),
            },
            {
                "name": "División de Segmento en Razón r",
                "description": "Punto que divide el segmento AP/PB = r",
                "latex": r"""x = \frac{x_1 + r x_2}{1 + r}, \quad y = \frac{y_1 + r y_2}{1 + r}""",
                "builder": lambda: _parse_preset(
                    r"""x = \frac{x_1 + r x_2}{1 + r}, \quad y = \frac{y_1 + r y_2}{1 + r}"""
                ),
            },
        ],
    },
    {
        "id": "math_analytic_geom_la_l_nea_recta_en_2d",
        "domain": "math",
        "category": "math_analytic_geom",
        "level": "NIVEL BÁSICO",
        "title": "La Línea Recta en 2D",
        "variations": [
            {
                "name": "Pendiente de una Recta",
                "description": "Inclinación m = (y_2 - y_1) / (x_2 - x_1) = tan(θ)",
                "latex": r"""m = \frac{y_2 - y_1}{x_2 - x_1} = \tan(\theta)""",
                "builder": lambda: _parse_preset(
                    r"""m = \frac{y_2 - y_1}{x_2 - x_1} = \tan(\theta)"""
                ),
            },
            {
                "name": "Ecuación Punto-Pendiente",
                "description": "Recta que pasa por (x_1, y_1) con pendiente m",
                "latex": r"""y - y_1 = m(x - x_1)""",
                "builder": lambda: _parse_preset(r"""y - y_1 = m(x - x_1)"""),
            },
            {
                "name": "Ecuación Pendiente-Ordenada",
                "description": "Forma explícita y = mx + b",
                "latex": r"""y = mx + b""",
                "builder": lambda: _parse_preset(r"""y = mx + b"""),
            },
            {
                "name": "Ecuación General de la Recta",
                "description": "Forma implícita Ax + By + C = 0 con pendiente m = -A/B",
                "latex": r"""Ax + By + C = 0, \quad m = -\frac{A}{B}""",
                "builder": lambda: _parse_preset(
                    r"""Ax + By + C = 0, \quad m = -\frac{A}{B}"""
                ),
            },
            {
                "name": "Ecuación Simétrica / Canónica",
                "description": "Intersecciones con los ejes en (a, 0) y (0, b)",
                "latex": r"""\frac{x}{a} + \frac{y}{b} = 1""",
                "builder": lambda: _parse_preset(r"""\frac{x}{a} + \frac{y}{b} = 1"""),
            },
            {
                "name": "Rectas Paralelas y Perpendiculares",
                "description": "Condiciones de paralelismo (m_1 = m_2) y perpendicularidad (m_1 · m_2 = -1)",
                "latex": r"""m_1 = m_2, \quad m_1 \cdot m_2 = -1""",
                "builder": lambda: _parse_preset(
                    r"""m_1 = m_2, \quad m_1 \cdot m_2 = -1"""
                ),
            },
            {
                "name": "Ángulo entre Dos Rectas",
                "description": "Tangente del ángulo agudo θ entre rectas de pendientes m_1 y m_2",
                "latex": r"""\tan(\theta) = \left|\frac{m_2 - m_1}{1 + m_1 \cdot m_2}\right|""",
                "builder": lambda: _parse_preset(
                    r"""\tan(\theta) = \left|\frac{m_2 - m_1}{1 + m_1 \cdot m_2}\right|"""
                ),
            },
        ],
    },
    {
        "id": "math_analytic_geom_distancias_y_secciones_c_nicas_en_2d",
        "domain": "math",
        "category": "math_analytic_geom",
        "level": "NIVEL INTERMEDIO",
        "title": "Distancias y Secciones Cónicas en 2D",
        "variations": [
            {
                "name": "Distancia de Punto a Recta",
                "description": "Distancia perpendicular desde P(x_0, y_0) a Ax + By + C = 0",
                "latex": r"""d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}""",
                "builder": lambda: _parse_preset(
                    r"""d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}"""
                ),
            },
            {
                "name": "Ecuaciones de la Circunferencia",
                "description": "Forma ordinaria con centro (h,k) y radio r, y forma general",
                "latex": r"""(x - h)^2 + (y - k)^2 = r^2, \quad x^2 + y^2 + Dx + Ey + F = 0""",
                "builder": lambda: _parse_preset(
                    r"""(x - h)^2 + (y - k)^2 = r^2, \quad x^2 + y^2 + Dx + Ey + F = 0"""
                ),
            },
            {
                "name": "Ecuaciones de la Parábola",
                "description": "Parábolas con eje focal horizontal y vertical, y lado recto LR = |4p|",
                "latex": r"""(y - k)^2 = 4p(x - h), \quad (x - h)^2 = 4p(y - k), \quad LR = |4p|""",
                "builder": lambda: _parse_preset(
                    r"""(y - k)^2 = 4p(x - h), \quad (x - h)^2 = 4p(y - k), \quad LR = |4p|"""
                ),
            },
            {
                "name": "Ecuación de la Elipse",
                "description": "Forma ordinaria horizontal, relación fundamental a^2 = b^2 + c^2, e = c/a",
                "latex": r"""\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1, \quad a^2 = b^2 + c^2, \quad e = \frac{c}{a}, \quad LR = \frac{2b^2}{a}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1, \quad a^2 = b^2 + c^2, \quad e = \frac{c}{a}, \quad LR = \frac{2b^2}{a}"""
                ),
            },
            {
                "name": "Ecuación de la Hipérbola",
                "description": "Forma ordinaria horizontal, c^2 = a^2 + b^2, e = c/a, y asíntotas",
                "latex": r"""\frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1, \quad c^2 = a^2 + b^2, \quad y - k = \pm \frac{b}{a}(x - h)""",
                "builder": lambda: _parse_preset(
                    r"""\frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1, \quad c^2 = a^2 + b^2, \quad y - k = \pm \frac{b}{a}(x - h)"""
                ),
            },
            {
                "name": "Ecuación de Segundo Grado y Discriminante",
                "description": "Clasificación cónica mediante Δ = B^2 - 4AC",
                "latex": r"""Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0, \quad \Delta = B^2 - 4AC""",
                "builder": lambda: _parse_preset(
                    r"""Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0, \quad \Delta = B^2 - 4AC"""
                ),
            },
            {
                "name": "Ángulo de Rotación de Ejes",
                "description": "Eliminación del término mixto Bxy mediante cot(2θ) = (A - C)/B",
                "latex": r"""\cot(2\theta) = \frac{A - C}{B}""",
                "builder": lambda: _parse_preset(
                    r"""\cot(2\theta) = \frac{A - C}{B}"""
                ),
            },
            {
                "name": "Coordenadas Polares y Cartesianas",
                "description": "Transformación bidireccional entre (r, θ) y (x, y)",
                "latex": r"""x = r\cos(\theta), \quad y = r\sin(\theta), \quad r = \sqrt{x^2 + y^2}, \quad \theta = \arctan\left(\frac{y}{x}\right)""",
                "builder": lambda: _parse_preset(
                    r"""x = r\cos(\theta), \quad y = r\sin(\theta), \quad r = \sqrt{x^2 + y^2}, \quad \theta = \arctan\left(\frac{y}{x}\right)"""
                ),
            },
        ],
    },
    {
        "id": "math_analytic_geom_geometr_a_anal_tica_del_espacio_3d",
        "domain": "math",
        "category": "math_analytic_geom",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Geometría Analítica del Espacio (3D)",
        "variations": [
            {
                "name": "Distancia entre Dos Puntos (3D)",
                "description": "Distancia euclidiana en el espacio tridimensional",
                "latex": r"""d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}""",
                "builder": lambda: _parse_preset(
                    r"""d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}"""
                ),
            },
            {
                "name": "Ecuación del Plano",
                "description": "Plano con vector normal n = (A, B, C) que pasa por P_0(x_0, y_0, z_0)",
                "latex": r"""A(x - x_0) + B(y - y_0) + C(z - z_0) = 0, \quad Ax + By + Cz + D = 0""",
                "builder": lambda: _parse_preset(
                    r"""A(x - x_0) + B(y - y_0) + C(z - z_0) = 0, \quad Ax + By + Cz + D = 0"""
                ),
            },
            {
                "name": "Distancia de Punto a Plano",
                "description": "Distancia perpendicular desde P(x_0, y_0, z_0) al plano Ax + By + Cz + D = 0",
                "latex": r"""d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}""",
                "builder": lambda: _parse_preset(
                    r"""d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}"""
                ),
            },
            {
                "name": "Ecuaciones de la Recta (3D)",
                "description": "Formas vectorial, paramétrica y continua/simétrica",
                "latex": r"""\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{v}, \quad \frac{x - x_0}{v_1} = \frac{y - y_0}{v_2} = \frac{z - z_0}{v_3}""",
                "builder": lambda: _parse_preset(
                    r"""\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{v}, \quad \frac{x - x_0}{v_1} = \frac{y - y_0}{v_2} = \frac{z - z_0}{v_3}"""
                ),
            },
            {
                "name": "Distancia entre Rectas Alabeadas",
                "description": "Distancia mínima entre rectas que se cruzan en el espacio",
                "latex": r"""d = \frac{|(\mathbf{r}_2 - \mathbf{r}_1) \cdot (\mathbf{v}_1 \times \mathbf{v}_2)|}{\|\mathbf{v}_1 \times \mathbf{v}_2\|}""",
                "builder": lambda: _parse_preset(
                    r"""d = \frac{|(\mathbf{r}_2 - \mathbf{r}_1) \cdot (\mathbf{v}_1 \times \mathbf{v}_2)|}{\|\mathbf{v}_1 \times \mathbf{v}_2\|}"""
                ),
            },
        ],
    },
    {
        "id": "math_analytic_geom_superficies_cu_dricas_y_coordenadas_3d",
        "domain": "math",
        "category": "math_analytic_geom",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Superficies Cuádricas y Coordenadas 3D",
        "variations": [
            {
                "name": "Elipsoide",
                "description": "Superficie cuádrica acotada centrada en el origen",
                "latex": r"""\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1""",
                "builder": lambda: _parse_preset(
                    r"""\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1"""
                ),
            },
            {
                "name": "Hiperboloides Cuádricos",
                "description": "Hiperboloide de 1 hoja (conexo) y de 2 hojas",
                "latex": r"""\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1, \quad \frac{x^2}{a^2} - \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1""",
                "builder": lambda: _parse_preset(
                    r"""\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1, \quad \frac{x^2}{a^2} - \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1"""
                ),
            },
            {
                "name": "Paraboloides (Elíptico y Silla de Montar)",
                "description": "Paraboloide elíptico y paraboloide hiperbólico",
                "latex": r"""z = \frac{x^2}{a^2} + \frac{y^2}{b^2}, \quad z = \frac{y^2}{b^2} - \frac{x^2}{a^2}""",
                "builder": lambda: _parse_preset(
                    r"""z = \frac{x^2}{a^2} + \frac{y^2}{b^2}, \quad z = \frac{y^2}{b^2} - \frac{x^2}{a^2}"""
                ),
            },
            {
                "name": "Cono Cuádrico",
                "description": "Superficie cónica cuádrica con vértice en el origen",
                "latex": r"""\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{z^2}{c^2}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{z^2}{c^2}"""
                ),
            },
            {
                "name": "Coordenadas Cilíndricas y Esféricas",
                "description": "Transformación a coordenadas cilíndricas y esféricas en ℝ^3",
                "latex": r"""x = r\cos(\theta), \, y = r\sin(\theta), \, z = z, \quad x = \rho\sin(\varphi)\cos(\theta), \, y = \rho\sin(\varphi)\sin(\theta), \, z = \rho\cos(\varphi)""",
                "builder": lambda: _parse_preset(
                    r"""x = r\cos(\theta), \, y = r\sin(\theta), \, z = z, \quad x = \rho\sin(\varphi)\cos(\theta), \, y = \rho\sin(\varphi)\sin(\theta), \, z = \rho\cos(\varphi)"""
                ),
            },
        ],
    },
    {
        "id": "math_linear_algebra_vectores_en_n",
        "domain": "math",
        "category": "math_linear_algebra",
        "level": "NIVEL BÁSICO",
        "title": "Vectores en ℝ^n",
        "variations": [
            {
                "name": "Operaciones Vectoriales en ℝ^n",
                "description": "Suma vectorial y producto escalar por vector",
                "latex": r"""\mathbf{u} + \mathbf{v} = (u_1 + v_1, \dots, u_n + v_n), \quad c\mathbf{u} = (cu_1, \dots, cu_n)""",
                "builder": lambda: _parse_preset(
                    r"""\mathbf{u} + \mathbf{v} = (u_1 + v_1, \dots, u_n + v_n), \quad c\mathbf{u} = (cu_1, \dots, cu_n)"""
                ),
            },
            {
                "name": "Norma Euclidiana y Vector Unitario",
                "description": "Norma L_2 y normalización u_hat = u / ||u||",
                "latex": r"""\|\mathbf{u}\| = \sqrt{u_1^2 + \dots + u_n^2} = \sqrt{\mathbf{u} \cdot \mathbf{u}}, \quad \hat{\mathbf{u}} = \frac{\mathbf{u}}{\|\mathbf{u}\|}""",
                "builder": lambda: _parse_preset(
                    r"""\|\mathbf{u}\| = \sqrt{u_1^2 + \dots + u_n^2} = \sqrt{\mathbf{u} \cdot \mathbf{u}}, \quad \hat{\mathbf{u}} = \frac{\mathbf{u}}{\|\mathbf{u}\|}"""
                ),
            },
        ],
    },
    {
        "id": "math_linear_algebra_productos_vectoriales_y_sistemas",
        "domain": "math",
        "category": "math_linear_algebra",
        "level": "NIVEL BÁSICO",
        "title": "Productos Vectoriales y Sistemas",
        "variations": [
            {
                "name": "Producto Punto y Ortogonalidad",
                "description": "Producto escalar algebraico y geométrico u · v = ||u|| ||v|| cos(θ), u ⊥ v <=> u · v = 0",
                "latex": r"""\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos(\theta), \quad \mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0""",
                "builder": lambda: _parse_preset(
                    r"""\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos(\theta), \quad \mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0"""
                ),
            },
            {
                "name": "Producto Cruz (Vectorial)",
                "description": "Determinante formal y magnitud ||u × v|| = ||u|| ||v|| sin(θ)",
                "latex": r"""\mathbf{u} \times \mathbf{v} = \det\begin{pmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{pmatrix}, \quad \|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\| \|\mathbf{v}\| \sin(\theta)""",
                "builder": lambda: _parse_preset(
                    r"""\mathbf{u} \times \mathbf{v} = \det\begin{pmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{pmatrix}, \quad \|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\| \|\mathbf{v}\| \sin(\theta)"""
                ),
            },
            {
                "name": "Producto Triple Escalar (Volumen)",
                "description": "Volumen del paralelepípedo [u, v, w] = u · (v × w)",
                "latex": r"""[\mathbf{u}, \mathbf{v}, \mathbf{w}] = \mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \det\begin{pmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{pmatrix}""",
                "builder": lambda: _parse_preset(
                    r"""[\mathbf{u}, \mathbf{v}, \mathbf{w}] = \mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \det\begin{pmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{pmatrix}"""
                ),
            },
            {
                "name": "Sistema Matricial y Regla de Cramer",
                "description": "A x = b y solución mediante determinantes x_i = det(A_i) / det(A)",
                "latex": r"""A\mathbf{x} = \mathbf{b}, \quad x_i = \frac{\det(A_i)}{\det(A)}""",
                "builder": lambda: _parse_preset(
                    r"""A\mathbf{x} = \mathbf{b}, \quad x_i = \frac{\det(A_i)}{\det(A)}"""
                ),
            },
        ],
    },
    {
        "id": "math_linear_algebra_lgebra_de_matrices_y_determinantes",
        "domain": "math",
        "category": "math_linear_algebra",
        "level": "NIVEL INTERMEDIO",
        "title": "Álgebra de Matrices y Determinantes",
        "variations": [
            {
                "name": "Multiplicación y Transposición",
                "description": "Elemento (AB)_{ij} = Σ A_{ik} B_{kj} y transpuesta (AB)^T = B^T A^T",
                "latex": r"""(AB)_{ij} = \sum_{k=1}^m A_{ik} B_{kj}, \quad (AB)^T = B^T A^T""",
                "builder": lambda: _parse_preset(
                    r"""(AB)_{ij} = \sum_{k=1}^m A_{ik} B_{kj}, \quad (AB)^T = B^T A^T"""
                ),
            },
            {
                "name": "Traza de una Matriz",
                "description": "Suma de los elementos diagonales Tr(A) y propiedad cíclica Tr(AB) = Tr(BA)",
                "latex": r"""\operatorname{Tr}(A) = \sum_{i=1}^n A_{ii}, \quad \operatorname{Tr}(AB) = \operatorname{Tr}(BA)""",
                "builder": lambda: _parse_preset(
                    r"""\operatorname{Tr}(A) = \sum_{i=1}^n A_{ii}, \quad \operatorname{Tr}(AB) = \operatorname{Tr}(BA)"""
                ),
            },
            {
                "name": "Propiedades del Determinante",
                "description": "Multiplicatividad, transpuesta, inversa y escala det(cA) = c^n det(A)",
                "latex": r"""\det(AB) = \det(A)\det(B), \quad \det(A^T) = \det(A), \quad \det(A^{-1}) = \frac{1}{\det(A)}, \quad \det(cA) = c^n \det(A)""",
                "builder": lambda: _parse_preset(
                    r"""\det(AB) = \det(A)\det(B), \quad \det(A^T) = \det(A), \quad \det(A^{-1}) = \frac{1}{\det(A)}, \quad \det(cA) = c^n \det(A)"""
                ),
            },
        ],
    },
    {
        "id": "math_linear_algebra_espacios_vectoriales_y_ortogonalidad",
        "domain": "math",
        "category": "math_linear_algebra",
        "level": "NIVEL INTERMEDIO",
        "title": "Espacios Vectoriales y Ortogonalidad",
        "variations": [
            {
                "name": "Subespacios y Dependencia Lineal",
                "description": "Cerradura de subespacio y combinación lineal nula",
                "latex": r"""\mathbf{0} \in W, \quad \mathbf{u} + \mathbf{v} \in W, \quad c\mathbf{u} \in W, \quad \sum_{i=1}^k c_i \mathbf{v}_i = \mathbf{0}""",
                "builder": lambda: _parse_preset(
                    r"""\mathbf{0} \in W, \quad \mathbf{u} + \mathbf{v} \in W, \quad c\mathbf{u} \in W, \quad \sum_{i=1}^k c_i \mathbf{v}_i = \mathbf{0}"""
                ),
            },
            {
                "name": "Teorema del Rango-Nulidad",
                "description": "dim(Nuc(T)) + dim(Im(T)) = dim(V) o nulidad(A) + rango(A) = n",
                "latex": r"""\dim(\operatorname{Nuc}(T)) + \dim(\operatorname{Im}(T)) = \dim(V), \quad \operatorname{nulidad}(A) + \operatorname{rango}(A) = n""",
                "builder": lambda: _parse_preset(
                    r"""\dim(\operatorname{Nuc}(T)) + \dim(\operatorname{Im}(T)) = \dim(V), \quad \operatorname{nulidad}(A) + \operatorname{rango}(A) = n"""
                ),
            },
            {
                "name": "Desigualdades de Cauchy-Schwarz y Triangular",
                "description": "|⟨u, v⟩| ≤ ||u|| ||v|| y ||u + v|| ≤ ||u|| + ||v||",
                "latex": r"""|\langle \mathbf{u}, \mathbf{v} \rangle| \le \|\mathbf{u}\| \|\mathbf{v}\|, \quad \|\mathbf{u} + \mathbf{v}\| \le \|\mathbf{u}\| + \|\mathbf{v}\|""",
                "builder": lambda: _parse_preset(
                    r"""|\langle \mathbf{u}, \mathbf{v} \rangle| \le \|\mathbf{u}\| \|\mathbf{v}\|, \quad \|\mathbf{u} + \mathbf{v}\| \le \|\mathbf{u}\| + \|\mathbf{v}\|"""
                ),
            },
            {
                "name": "Proceso de Ortogonalización de Gram-Schmidt",
                "description": "Construcción de base ortogonal y normalización e_i = u_i / ||u_i||",
                "latex": r"""\operatorname{Proy}_{\mathbf{v}}(\mathbf{u}) = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{v}\|^2} \mathbf{v}, \quad \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \operatorname{Proy}_{\mathbf{u}_j}(\mathbf{v}_k), \quad \mathbf{e}_i = \frac{\mathbf{u}_i}{\|\mathbf{u}_i\|}""",
                "builder": lambda: _parse_preset(
                    r"""\operatorname{Proy}_{\mathbf{v}}(\mathbf{u}) = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{v}\|^2} \mathbf{v}, \quad \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \operatorname{Proy}_{\mathbf{u}_j}(\mathbf{v}_k), \quad \mathbf{e}_i = \frac{\mathbf{u}_i}{\|\mathbf{u}_i\|}"""
                ),
            },
        ],
    },
    {
        "id": "math_linear_algebra_autovalores_autovectores_y_diagonalizaci_n",
        "domain": "math",
        "category": "math_linear_algebra",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Autovalores, Autovectores y Diagonalización",
        "variations": [
            {
                "name": "Polinomio Característico y Autovectores",
                "description": "p(λ) = det(A - λI) = 0 y ecuación característica (A - λI)v = 0",
                "latex": r"""p(\lambda) = \det(A - \lambda I) = 0, \quad (A - \lambda I)\mathbf{v} = \mathbf{0} \iff A\mathbf{v} = \lambda\mathbf{v}""",
                "builder": lambda: _parse_preset(
                    r"""p(\lambda) = \det(A - \lambda I) = 0, \quad (A - \lambda I)\mathbf{v} = \mathbf{0} \iff A\mathbf{v} = \lambda\mathbf{v}"""
                ),
            },
            {
                "name": "Teorema de Cayley-Hamilton",
                "description": "Toda matriz cuadrada satisface su propia ecuación característica p(A) = 0",
                "latex": r"""p(A) = O""",
                "builder": lambda: _parse_preset(r"""p(A) = O"""),
            },
            {
                "name": "Diagonalización y Teorema Espectral",
                "description": "A = P D P^(-1) y descomposición espectral simétrica A = Q Λ Q^T",
                "latex": r"""A = PDP^{-1}, \quad A = Q\Lambda Q^T \quad (Q^T = Q^{-1})""",
                "builder": lambda: _parse_preset(
                    r"""A = PDP^{-1}, \quad A = Q\Lambda Q^T \quad (Q^T = Q^{-1})"""
                ),
            },
            {
                "name": "Forma Canónica de Jordan",
                "description": "Representación por bloques de Jordan J_k(λ)",
                "latex": r"""A = P J P^{-1}, \quad J = \operatorname{diag}(J_1, \dots, J_k)""",
                "builder": lambda: _parse_preset(
                    r"""A = P J P^{-1}, \quad J = \operatorname{diag}(J_1, \dots, J_k)"""
                ),
            },
        ],
    },
    {
        "id": "math_linear_algebra_factorizaciones_matriciales_y_m_nimos_cuadrados",
        "domain": "math",
        "category": "math_linear_algebra",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Factorizaciones Matriciales y Mínimos Cuadrados",
        "variations": [
            {
                "name": "Descomposiciones LU, QR y Cholesky",
                "description": "A = LU, A = QR y A = L L^T (Cholesky para matrices simétricas definidas positivas)",
                "latex": r"""A = LU, \quad A = QR, \quad A = LL^T""",
                "builder": lambda: _parse_preset(
                    r"""A = LU, \quad A = QR, \quad A = LL^T"""
                ),
            },
            {
                "name": "Descomposición en Valores Singulares (SVD)",
                "description": "A = U Σ V^T con valores singulares σ_i = √(λ_i(A^T A))",
                "latex": r"""A = U\Sigma V^T, \quad \sigma_i = \sqrt{\lambda_i(A^T A)}""",
                "builder": lambda: _parse_preset(
                    r"""A = U\Sigma V^T, \quad \sigma_i = \sqrt{\lambda_i(A^T A)}"""
                ),
            },
            {
                "name": "Pseudoinversa de Moore-Penrose y Mínimos Cuadrados",
                "description": "A^+ = V Σ^+ U^T y solución óptima de mínimos cuadrados x_hat = (A^T A)^(-1) A^T b",
                "latex": r"""A^+ = V\Sigma^+ U^T = (A^T A)^{-1} A^T, \quad \hat{\mathbf{x}} = (A^T A)^{-1} A^T \mathbf{b}""",
                "builder": lambda: _parse_preset(
                    r"""A^+ = V\Sigma^+ U^T = (A^T A)^{-1} A^T, \quad \hat{\mathbf{x}} = (A^T A)^{-1} A^T \mathbf{b}"""
                ),
            },
            {
                "name": "Producto de Kronecker y Propiedad Mixta",
                "description": "Producto tensorial matricial A ⊗ B y propiedad (A ⊗ B)(C ⊗ D) = (AC) ⊗ (BD)",
                "latex": r"""(A \otimes B)(C \otimes D) = (AC) \otimes (BD)""",
                "builder": lambda: _parse_preset(
                    r"""(A \otimes B)(C \otimes D) = (AC) \otimes (BD)"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_calculus_definici_n_de_l_mite_y_continuidad",
        "domain": "math",
        "category": "math_diff_calculus",
        "level": "NIVEL BÁSICO",
        "title": "Definición de Límite y Continuidad",
        "variations": [
            {
                "name": "Definición Épsilon-Delta de Límite",
                "description": "Definición formal rigurosa de límite lim_{x->a} f(x) = L",
                "latex": r"""\lim_{x \to a} f(x) = L \iff \forall \varepsilon > 0, \, \exists \delta > 0 : 0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon""",
                "builder": lambda: _parse_preset(
                    r"""\lim_{x \to a} f(x) = L \iff \forall \varepsilon > 0, \, \exists \delta > 0 : 0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon"""
                ),
            },
            {
                "name": "Continuidad en un Punto",
                "description": "Condición de continuidad de f(x) en el punto x = a",
                "latex": r"""\lim_{x \to a} f(x) = f(a)""",
                "builder": lambda: _parse_preset(r"""\lim_{x \to a} f(x) = f(a)"""),
            },
        ],
    },
    {
        "id": "math_diff_calculus_definici_n_formal_de_la_derivada",
        "domain": "math",
        "category": "math_diff_calculus",
        "level": "NIVEL BÁSICO",
        "title": "Definición Formal de la Derivada",
        "variations": [
            {
                "name": "Derivada por Incremento (Límite)",
                "description": "Definición fundamental de la derivada mediante el cociente diferencial",
                "latex": r"""f'(x) = \frac{dy}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}""",
                "builder": lambda: _parse_preset(
                    r"""f'(x) = \frac{dy}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}"""
                ),
            },
            {
                "name": "Derivada en un Punto",
                "description": "Definición de derivada evaluada en el punto x = a",
                "latex": r"""f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}""",
                "builder": lambda: _parse_preset(
                    r"""f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_calculus_reglas_y_derivadas_algebraicas_elementales",
        "domain": "math",
        "category": "math_diff_calculus",
        "level": "NIVEL BÁSICO",
        "title": "Reglas y Derivadas Algebraicas Elementales",
        "variations": [
            {
                "name": "Derivada de Constante e Identidad",
                "description": "Derivada de una función constante y de la función identidad",
                "latex": r"""\frac{d}{dx}(c) = 0, \quad \frac{d}{dx}(x) = 1""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}(c) = 0, \quad \frac{d}{dx}(x) = 1"""
                ),
            },
            {
                "name": "Regla de la Potencia",
                "description": "Derivada de una potencia monómica d/dx(x^n) = n · x^(n - 1)",
                "latex": r"""\frac{d}{dx}(x^n) = n x^{n - 1}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}(x^n) = n x^{n - 1}"""
                ),
            },
            {
                "name": "Linealidad de la Derivada",
                "description": "Múltiplo constante y suma/resta de funciones",
                "latex": r"""\frac{d}{dx}[c \cdot f(x)] = c f'(x), \quad \frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}[c \cdot f(x)] = c f'(x), \quad \frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)"""
                ),
            },
            {
                "name": "Derivada de Raíz e Inverso",
                "description": "Derivadas inmediatas de √x y 1/x",
                "latex": r"""\frac{d}{dx}(\sqrt{x}) = \frac{1}{2\sqrt{x}}, \quad \frac{d}{dx}\left(\frac{1}{x}\right) = -\frac{1}{x^2}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}(\sqrt{x}) = \frac{1}{2\sqrt{x}}, \quad \frac{d}{dx}\left(\frac{1}{x}\right) = -\frac{1}{x^2}"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_calculus_reglas_fundamentales_de_derivaci_n",
        "domain": "math",
        "category": "math_diff_calculus",
        "level": "NIVEL INTERMEDIO",
        "title": "Reglas Fundamentales de Derivación",
        "variations": [
            {
                "name": "Reglas del Producto y Cociente",
                "description": "Derivada del producto y cociente de dos funciones",
                "latex": r"""\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x), \quad \frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x), \quad \frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}"""
                ),
            },
            {
                "name": "Regla de la Cadena",
                "description": "Derivada de funciones compuestas y notación de Leibniz",
                "latex": r"""\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x), \quad \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x), \quad \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_calculus_derivadas_de_funciones_trascendentes_elementales",
        "domain": "math",
        "category": "math_diff_calculus",
        "level": "NIVEL INTERMEDIO",
        "title": "Derivadas de Funciones Trascendentes Elementales",
        "variations": [
            {
                "name": "Derivadas Exponenciales y Logarítmicas",
                "description": "Derivadas de e^x, a^x, ln|x| y log_a|x|",
                "latex": r"""\frac{d}{dx}(e^x) = e^x, \quad \frac{d}{dx}(a^x) = a^x \ln(a), \quad \frac{d}{dx}(\ln|x|) = \frac{1}{x}, \quad \frac{d}{dx}(\log_a|x|) = \frac{1}{x\ln(a)}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}(e^x) = e^x, \quad \frac{d}{dx}(a^x) = a^x \ln(a), \quad \frac{d}{dx}(\ln|x|) = \frac{1}{x}, \quad \frac{d}{dx}(\log_a|x|) = \frac{1}{x\ln(a)}"""
                ),
            },
            {
                "name": "Derivadas Trigonométricas Directas",
                "description": "Derivadas de sen(x), cos(x), tan(x), cot(x), sec(x), csc(x)",
                "latex": r"""\frac{d}{dx}[\sin(x)] = \cos(x), \quad \frac{d}{dx}[\cos(x)] = -\sin(x), \quad \frac{d}{dx}[\tan(x)] = \sec^2(x)""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}[\sin(x)] = \cos(x), \quad \frac{d}{dx}[\cos(x)] = -\sin(x), \quad \frac{d}{dx}[\tan(x)] = \sec^2(x)"""
                ),
            },
            {
                "name": "Derivadas de Secante, Cosecante y Cotangente",
                "description": "Derivadas de cot(x), sec(x) y csc(x)",
                "latex": r"""\frac{d}{dx}[\cot(x)] = -\csc^2(x), \quad \frac{d}{dx}[\sec(x)] = \sec(x)\tan(x), \quad \frac{d}{dx}[\csc(x)] = -\csc(x)\cot(x)""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}[\cot(x)] = -\csc^2(x), \quad \frac{d}{dx}[\sec(x)] = \sec(x)\tan(x), \quad \frac{d}{dx}[\csc(x)] = -\csc(x)\cot(x)"""
                ),
            },
            {
                "name": "Derivadas Trigonométricas Inversas (Arcsen, Arccos, Arctan)",
                "description": "Derivadas de arcsen(x), arccos(x) y arctan(x)",
                "latex": r"""\frac{d}{dx}[\arcsin(x)] = \frac{1}{\sqrt{1 - x^2}}, \quad \frac{d}{dx}[\arccos(x)] = -\frac{1}{\sqrt{1 - x^2}}, \quad \frac{d}{dx}[\arctan(x)] = \frac{1}{1 + x^2}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}[\arcsin(x)] = \frac{1}{\sqrt{1 - x^2}}, \quad \frac{d}{dx}[\arccos(x)] = -\frac{1}{\sqrt{1 - x^2}}, \quad \frac{d}{dx}[\arctan(x)] = \frac{1}{1 + x^2}"""
                ),
            },
            {
                "name": "Derivadas Trigonométricas Inversas (Arccot, Arcsec, Arccsc)",
                "description": "Derivadas de arccot(x), arcsec(x) y arccsc(x)",
                "latex": r"""\frac{d}{dx}[\operatorname{arccot}(x)] = -\frac{1}{1 + x^2}, \quad \frac{d}{dx}[\operatorname{arcsec}(x)] = \frac{1}{|x|\sqrt{x^2 - 1}}, \quad \frac{d}{dx}[\operatorname{arccsc}(x)] = -\frac{1}{|x|\sqrt{x^2 - 1}}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}[\operatorname{arccot}(x)] = -\frac{1}{1 + x^2}, \quad \frac{d}{dx}[\operatorname{arcsec}(x)] = \frac{1}{|x|\sqrt{x^2 - 1}}, \quad \frac{d}{dx}[\operatorname{arccsc}(x)] = -\frac{1}{|x|\sqrt{x^2 - 1}}"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_calculus_aplicaciones_y_teoremas_del_c_lculo_diferencial",
        "domain": "math",
        "category": "math_diff_calculus",
        "level": "NIVEL INTERMEDIO",
        "title": "Aplicaciones y Teoremas del Cálculo Diferencial",
        "variations": [
            {
                "name": "Recta Tangente y Recta Normal",
                "description": "Ecuaciones de la recta tangente y normal a una curva en (x_0, y_0)",
                "latex": r"""y - y_0 = f'(x_0)(x - x_0), \quad y - y_0 = -\frac{1}{f'(x_0)}(x - x_0)""",
                "builder": lambda: _parse_preset(
                    r"""y - y_0 = f'(x_0)(x - x_0), \quad y - y_0 = -\frac{1}{f'(x_0)}(x - x_0)"""
                ),
            },
            {
                "name": "Regla de L'Hôpital",
                "description": "Resolución de indeterminaciones 0/0 o ∞/∞ mediante derivadas",
                "latex": r"""\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}""",
                "builder": lambda: _parse_preset(
                    r"""\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}"""
                ),
            },
            {
                "name": "Teoremas de Rolle, Lagrange y Cauchy",
                "description": "Teorema del Valor Medio y su generalización de Cauchy",
                "latex": r"""f'(c) = \frac{f(b) - f(a)}{b - a}, \quad \frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}""",
                "builder": lambda: _parse_preset(
                    r"""f'(c) = \frac{f(b) - f(a)}{b - a}, \quad \frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_calculus_derivadas_de_funciones_hiperb_licas_e_inversas",
        "domain": "math",
        "category": "math_diff_calculus",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Derivadas de Funciones Hiperbólicas e Inversas",
        "variations": [
            {
                "name": "Derivadas Hiperbólicas Directas",
                "description": "Derivadas de sinh(x), cosh(x), tanh(x) y sech(x)",
                "latex": r"""\frac{d}{dx}[\sinh(x)] = \cosh(x), \quad \frac{d}{dx}[\cosh(x)] = \sinh(x), \quad \frac{d}{dx}[\tanh(x)] = \operatorname{sech}^2(x), \quad \frac{d}{dx}[\operatorname{sech}(x)] = -\operatorname{sech}(x)\tanh(x)""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}[\sinh(x)] = \cosh(x), \quad \frac{d}{dx}[\cosh(x)] = \sinh(x), \quad \frac{d}{dx}[\tanh(x)] = \operatorname{sech}^2(x), \quad \frac{d}{dx}[\operatorname{sech}(x)] = -\operatorname{sech}(x)\tanh(x)"""
                ),
            },
            {
                "name": "Derivadas Hiperbólicas Inversas",
                "description": "Derivadas de arsinh(x), arcosh(x) y artanh(x)",
                "latex": r"""\frac{d}{dx}[\operatorname{arsinh}(x)] = \frac{1}{\sqrt{x^2 + 1}}, \quad \frac{d}{dx}[\operatorname{arcosh}(x)] = \frac{1}{\sqrt{x^2 - 1}}, \quad \frac{d}{dx}[\operatorname{artanh}(x)] = \frac{1}{1 - x^2}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}[\operatorname{arsinh}(x)] = \frac{1}{\sqrt{x^2 + 1}}, \quad \frac{d}{dx}[\operatorname{arcosh}(x)] = \frac{1}{\sqrt{x^2 - 1}}, \quad \frac{d}{dx}[\operatorname{artanh}(x)] = \frac{1}{1 - x^2}"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_calculus_diferencial_total_y_series",
        "domain": "math",
        "category": "math_diff_calculus",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Diferencial Total y Series",
        "variations": [
            {
                "name": "Diferencial y Serie de Taylor con Resto de Lagrange",
                "description": "Desarrollo en serie de Taylor con término de error de Lagrange",
                "latex": r"""dy = f'(x) dx, \quad f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x - a)^n, \quad R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} (x - a)^{n+1}""",
                "builder": lambda: _parse_preset(
                    r"""dy = f'(x) dx, \quad f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x - a)^n, \quad R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} (x - a)^{n+1}"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_calculus_geometr_a_diferencial_de_curvas_planas",
        "domain": "math",
        "category": "math_diff_calculus",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Geometría Diferencial de Curvas Planas",
        "variations": [
            {
                "name": "Curvatura y Radio de Curvatura",
                "description": "Cálculo diferencial de curvatura κ y radio de curvatura R",
                "latex": r"""\kappa = \frac{|y''|}{[1 + (y')^2]^{\frac{3}{2}}}, \quad R = \frac{1}{\kappa} = \frac{[1 + (y')^2]^{\frac{3}{2}}}{|y''|}""",
                "builder": lambda: _parse_preset(
                    r"""\kappa = \frac{|y''|}{[1 + (y')^2]^{\frac{3}{2}}}, \quad R = \frac{1}{\kappa} = \frac{[1 + (y')^2]^{\frac{3}{2}}}{|y''|}"""
                ),
            },
        ],
    },
    {
        "id": "math_integral_calculus_definici_n_y_propiedades_fundamentales",
        "domain": "math",
        "category": "math_integral_calculus",
        "level": "NIVEL BÁSICO",
        "title": "Definición y Propiedades Fundamentales",
        "variations": [
            {
                "name": "Antiderivada y Linealidad",
                "description": "Definición de primitiva y propiedad de linealidad de la integral",
                "latex": r"""\int f(x) \, dx = F(x) + C, \quad \int [a f(x) + b g(x)] \, dx = a \int f(x) \, dx + b \int g(x) \, dx""",
                "builder": lambda: _parse_preset(
                    r"""\int f(x) \, dx = F(x) + C, \quad \int [a f(x) + b g(x)] \, dx = a \int f(x) \, dx + b \int g(x) \, dx"""
                ),
            },
        ],
    },
    {
        "id": "math_integral_calculus_integrales_indefinidas_elementales_inmediatas",
        "domain": "math",
        "category": "math_integral_calculus",
        "level": "NIVEL BÁSICO",
        "title": "Integrales Indefinidas Elementales / Inmediatas",
        "variations": [
            {
                "name": "Integrales de Potencias y Exponenciales",
                "description": "Integrales inmediatas de x^n, 1/x, e^x y a^x",
                "latex": r"""\int x^n \, dx = \frac{x^{n+1}}{n+1} + C, \quad \int \frac{1}{x} \, dx = \ln|x| + C, \quad \int e^x \, dx = e^x + C, \quad \int a^x \, dx = \frac{a^x}{\ln(a)} + C""",
                "builder": lambda: _parse_preset(
                    r"""\int x^n \, dx = \frac{x^{n+1}}{n+1} + C, \quad \int \frac{1}{x} \, dx = \ln|x| + C, \quad \int e^x \, dx = e^x + C, \quad \int a^x \, dx = \frac{a^x}{\ln(a)} + C"""
                ),
            },
            {
                "name": "Integrales Trigonométricas Inmediatas",
                "description": "Integrales directas de seno, coseno, secante al cuadrado y cosecante al cuadrado",
                "latex": r"""\int \sin(x) \, dx = -\cos(x) + C, \quad \int \cos(x) \, dx = \sin(x) + C, \quad \int \sec^2(x) \, dx = \tan(x) + C, \quad \int \csc^2(x) \, dx = -\cot(x) + C""",
                "builder": lambda: _parse_preset(
                    r"""\int \sin(x) \, dx = -\cos(x) + C, \quad \int \cos(x) \, dx = \sin(x) + C, \quad \int \sec^2(x) \, dx = \tan(x) + C, \quad \int \csc^2(x) \, dx = -\cot(x) + C"""
                ),
            },
            {
                "name": "Integrales de Productos Trigonométricos",
                "description": "Integrales de sec(x)tan(x) y csc(x)cot(x)",
                "latex": r"""\int \sec(x)\tan(x) \, dx = \sec(x) + C, \quad \int \csc(x)\cot(x) \, dx = -\csc(x) + C""",
                "builder": lambda: _parse_preset(
                    r"""\int \sec(x)\tan(x) \, dx = \sec(x) + C, \quad \int \csc(x)\cot(x) \, dx = -\csc(x) + C"""
                ),
            },
        ],
    },
    {
        "id": "math_integral_calculus_teorema_fundamental_del_c_lculo_tfc",
        "domain": "math",
        "category": "math_integral_calculus",
        "level": "NIVEL INTERMEDIO",
        "title": "Teorema Fundamental del Cálculo (TFC)",
        "variations": [
            {
                "name": "Teorema Fundamental del Cálculo y Regla de Leibniz",
                "description": "TFC Parte 1, Regla de derivación de Leibniz 1D y Regla de Barrow",
                "latex": r"""\frac{d}{dx} \left[ \int_a^x f(t) \, dt \right] = f(x), \quad \frac{d}{dx} \left[ \int_{u(x)}^{v(x)} f(t) \, dt \right] = f(v(x))v'(x) - f(u(x))u'(x), \quad \int_a^b f(x) \, dx = F(b) - F(a)""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx} \left[ \int_a^x f(t) \, dt \right] = f(x), \quad \frac{d}{dx} \left[ \int_{u(x)}^{v(x)} f(t) \, dt \right] = f(v(x))v'(x) - f(u(x))u'(x), \quad \int_a^b f(x) \, dx = F(b) - F(a)"""
                ),
            },
        ],
    },
    {
        "id": "math_integral_calculus_t_cnicas_m_todos_de_integraci_n",
        "domain": "math",
        "category": "math_integral_calculus",
        "level": "NIVEL INTERMEDIO",
        "title": "Técnicas / Métodos de Integración",
        "variations": [
            {
                "name": "Sustitución e Integración por Partes",
                "description": "Fórmulas de cambio de variable e integración por partes ∫ u dv = u v - ∫ v du",
                "latex": r"""\int f(g(x))g'(x) \, dx = \int f(u) \, du, \quad \int u \, dv = u v - \int v \, du""",
                "builder": lambda: _parse_preset(
                    r"""\int f(g(x))g'(x) \, dx = \int f(u) \, du, \quad \int u \, dv = u v - \int v \, du"""
                ),
            },
            {
                "name": "Sustituciones Trigonométricas Estándar",
                "description": "Sustituciones para √(a² - x²), √(a² + x²) y √(x² - a²)",
                "latex": r"""x = a\sin(\theta) \implies \sqrt{a^2 - x^2} = a\cos(\theta), \quad x = a\tan(\theta) \implies \sqrt{a^2 + x^2} = a\sec(\theta), \quad x = a\sec(\theta) \implies \sqrt{x^2 - a^2} = a\tan(\theta)""",
                "builder": lambda: _parse_preset(
                    r"""x = a\sin(\theta) \implies \sqrt{a^2 - x^2} = a\cos(\theta), \quad x = a\tan(\theta) \implies \sqrt{a^2 + x^2} = a\sec(\theta), \quad x = a\sec(\theta) \implies \sqrt{x^2 - a^2} = a\tan(\theta)"""
                ),
            },
        ],
    },
    {
        "id": "math_integral_calculus_integrales_trigonom_tricas_e_inversas_clave",
        "domain": "math",
        "category": "math_integral_calculus",
        "level": "NIVEL INTERMEDIO",
        "title": "Integrales Trigonométricas e Inversas Clave",
        "variations": [
            {
                "name": "Integrales de Tangente, Cotangente, Secante y Cosecante",
                "description": "Integrales logarítmicas de las funciones trigonométricas básicas",
                "latex": r"""\int \tan(x) \, dx = \ln|\sec(x)| + C, \quad \int \cot(x) \, dx = \ln|\sin(x)| + C, \quad \int \sec(x) \, dx = \ln|\sec(x) + \tan(x)| + C, \quad \int \csc(x) \, dx = -\ln|\csc(x) + \cot(x)| + C""",
                "builder": lambda: _parse_preset(
                    r"""\int \tan(x) \, dx = \ln|\sec(x)| + C, \quad \int \cot(x) \, dx = \ln|\sin(x)| + C, \quad \int \sec(x) \, dx = \ln|\sec(x) + \tan(x)| + C, \quad \int \csc(x) \, dx = -\ln|\csc(x) + \cot(x)| + C"""
                ),
            },
            {
                "name": "Integrales Racionales y de Radicales",
                "description": "Integrales que generan arctan, arcsen, arcsec y logaritmos de fracciones",
                "latex": r"""\int \frac{1}{x^2 + a^2} \, dx = \frac{1}{a} \arctan\left(\frac{x}{a}\right) + C, \quad \int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \arcsin\left(\frac{x}{a}\right) + C, \quad \int \frac{1}{x^2 - a^2} \, dx = \frac{1}{2a} \ln\left|\frac{x - a}{x + a}\right| + C""",
                "builder": lambda: _parse_preset(
                    r"""\int \frac{1}{x^2 + a^2} \, dx = \frac{1}{a} \arctan\left(\frac{x}{a}\right) + C, \quad \int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \arcsin\left(\frac{x}{a}\right) + C, \quad \int \frac{1}{x^2 - a^2} \, dx = \frac{1}{2a} \ln\left|\frac{x - a}{x + a}\right| + C"""
                ),
            },
        ],
    },
    {
        "id": "math_integral_calculus_aplicaciones_geom_tricas_y_f_sicas",
        "domain": "math",
        "category": "math_integral_calculus",
        "level": "NIVEL INTERMEDIO",
        "title": "Aplicaciones Geométricas y Físicas",
        "variations": [
            {
                "name": "Área entre Curvas y Longitud de Arco",
                "description": "Cálculo integral de área plana y longitud de trayectoria curva",
                "latex": r"""A = \int_a^b |f(x) - g(x)| \, dx, \quad L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx""",
                "builder": lambda: _parse_preset(
                    r"""A = \int_a^b |f(x) - g(x)| \, dx, \quad L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx"""
                ),
            },
            {
                "name": "Volúmenes de Revolución (Discos, Arandelas y Cascarones)",
                "description": "Métodos de cálculo de sólidos de revolución",
                "latex": r"""V_{\text{discos}} = \pi \int_a^b [f(x)]^2 \, dx, \quad V_{\text{arandelas}} = \pi \int_a^b ([R(x)]^2 - [r(x)]^2) \, dx, \quad V_{\text{cascarones}} = 2\pi \int_a^b x f(x) \, dx""",
                "builder": lambda: _parse_preset(
                    r"""V_{\text{discos}} = \pi \int_a^b [f(x)]^2 \, dx, \quad V_{\text{arandelas}} = \pi \int_a^b ([R(x)]^2 - [r(x)]^2) \, dx, \quad V_{\text{cascarones}} = 2\pi \int_a^b x f(x) \, dx"""
                ),
            },
            {
                "name": "Área de Superficie de Revolución y Valor Medio",
                "description": "Superficie generada por rotación y promedio de una función continua",
                "latex": r"""S = 2\pi \int_a^b f(x) \sqrt{1 + [f'(x)]^2} \, dx, \quad f_{\text{prom}} = \frac{1}{b - a} \int_a^b f(x) \, dx""",
                "builder": lambda: _parse_preset(
                    r"""S = 2\pi \int_a^b f(x) \sqrt{1 + [f'(x)]^2} \, dx, \quad f_{\text{prom}} = \frac{1}{b - a} \int_a^b f(x) \, dx"""
                ),
            },
        ],
    },
    {
        "id": "math_integral_calculus_integrales_impropias",
        "domain": "math",
        "category": "math_integral_calculus",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Integrales Impropias",
        "variations": [
            {
                "name": "Integrales Impropias (Infinito y Discontinuidad)",
                "description": "Límites para integrales en intervalos no acotados o integrandos no acotados",
                "latex": r"""\int_a^\infty f(x) \, dx = \lim_{t \to \infty} \int_a^t f(x) \, dx, \quad \int_a^b f(x) \, dx = \lim_{t \to b^-} \int_a^t f(x) \, dx""",
                "builder": lambda: _parse_preset(
                    r"""\int_a^\infty f(x) \, dx = \lim_{t \to \infty} \int_a^t f(x) \, dx, \quad \int_a^b f(x) \, dx = \lim_{t \to b^-} \int_a^t f(x) \, dx"""
                ),
            },
        ],
    },
    {
        "id": "math_integral_calculus_sustituci_n_universal_de_weierstrass_ngulo_mitad",
        "domain": "math",
        "category": "math_integral_calculus",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Sustitución Universal de Weierstrass (Ángulo Mitad)",
        "variations": [
            {
                "name": "Sustitución de Weierstrass (t = tan(x/2))",
                "description": "Racionalización universal de funciones trigonométricas con t = tan(x/2)",
                "latex": r"""t = \tan\left(\frac{x}{2}\right) \implies dx = \frac{2}{1 + t^2} dt, \quad \sin(x) = \frac{2t}{1 + t^2}, \quad \cos(x) = \frac{1 - t^2}{1 + t^2}""",
                "builder": lambda: _parse_preset(
                    r"""t = \tan\left(\frac{x}{2}\right) \implies dx = \frac{2}{1 + t^2} dt, \quad \sin(x) = \frac{2t}{1 + t^2}, \quad \cos(x) = \frac{1 - t^2}{1 + t^2}"""
                ),
            },
        ],
    },
    {
        "id": "math_integral_calculus_integrales_hiperb_licas_inmediatas",
        "domain": "math",
        "category": "math_integral_calculus",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Integrales Hiperbólicas Inmediatas",
        "variations": [
            {
                "name": "Integrales Hiperbólicas",
                "description": "Integrales de sinh(x), cosh(x) y formas que producen arsinh y arcosh",
                "latex": r"""\int \sinh(x) \, dx = \cosh(x) + C, \quad \int \cosh(x) \, dx = \sinh(x) + C, \quad \int \frac{1}{\sqrt{x^2 + a^2}} \, dx = \operatorname{arsinh}\left(\frac{x}{a}\right) + C""",
                "builder": lambda: _parse_preset(
                    r"""\int \sinh(x) \, dx = \cosh(x) + C, \quad \int \cosh(x) \, dx = \sinh(x) + C, \quad \int \frac{1}{\sqrt{x^2 + a^2}} \, dx = \operatorname{arsinh}\left(\frac{x}{a}\right) + C"""
                ),
            },
        ],
    },
    {
        "id": "math_integral_calculus_funciones_especiales_e_integrales_notables",
        "domain": "math",
        "category": "math_integral_calculus",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Funciones Especiales e Integrales Notables",
        "variations": [
            {
                "name": "Funciones Gamma, Beta e Integral Gaussiana",
                "description": "Definiciones de Γ(z), B(x,y) y la integral de Gauss",
                "latex": r"""\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt, \quad \mathrm{B}(x, y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x + y)}, \quad \int_{-\infty}^\infty e^{-x^2} \, dx = \sqrt{\pi}""",
                "builder": lambda: _parse_preset(
                    r"""\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt, \quad \mathrm{B}(x, y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x + y)}, \quad \int_{-\infty}^\infty e^{-x^2} \, dx = \sqrt{\pi}"""
                ),
            },
            {
                "name": "Diferenciación Bajo el Signo Integral (Leibniz 2D)",
                "description": "Derivada respecto a parámetro x de una integral con límites variables",
                "latex": r"""\frac{d}{dx} \left[ \int_{a(x)}^{b(x)} f(x, t) \, dt \right] = f(x, b(x))b'(x) - f(x, a(x))a'(x) + \int_{a(x)}^{b(x)} \frac{\partial f}{\partial x}(x, t) \, dt""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx} \left[ \int_{a(x)}^{b(x)} f(x, t) \, dt \right] = f(x, b(x))b'(x) - f(x, a(x))a'(x) + \int_{a(x)}^{b(x)} \frac{\partial f}{\partial x}(x, t) \, dt"""
                ),
            },
        ],
    },
    {
        "id": "math_vector_calculus_curvas_param_tricas_y_funciones_vectoriales_en_3",
        "domain": "math",
        "category": "math_vector_calculus",
        "level": "NIVEL BÁSICO",
        "title": "Curvas Paramétricas y Funciones Vectoriales en ℝ^3",
        "variations": [
            {
                "name": "Posición, Velocidad, Rapidez y Aceleración",
                "description": "Cinemática vectorial de trayectorias en ℝ^3",
                "latex": r"""\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}, \quad \mathbf{v}(t) = \mathbf{r}'(t), \quad \|\mathbf{v}(t)\| = \sqrt{[x']^2 + [y']^2 + [z']^2}, \quad \mathbf{a}(t) = \mathbf{r}''(t)""",
                "builder": lambda: _parse_preset(
                    r"""\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}, \quad \mathbf{v}(t) = \mathbf{r}'(t), \quad \|\mathbf{v}(t)\| = \sqrt{[x']^2 + [y']^2 + [z']^2}, \quad \mathbf{a}(t) = \mathbf{r}''(t)"""
                ),
            },
        ],
    },
    {
        "id": "math_vector_calculus_derivadas_parciales_de_funciones_escalares",
        "domain": "math",
        "category": "math_vector_calculus",
        "level": "NIVEL BÁSICO",
        "title": "Derivadas Parciales de Funciones Escalares",
        "variations": [
            {
                "name": "Derivada Parcial y Teorema de Schwarz",
                "description": "Límite de la derivada parcial y simetría de derivadas cruzadas de Clairaut",
                "latex": r"""\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x + h, y, z) - f(x, y, z)}{h}, \quad \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x + h, y, z) - f(x, y, z)}{h}, \quad \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}"""
                ),
            },
        ],
    },
    {
        "id": "math_vector_calculus_gradiente",
        "domain": "math",
        "category": "math_vector_calculus",
        "level": "NIVEL BÁSICO",
        "title": "Gradiente",
        "variations": [
            {
                "name": "Vector Gradiente (∇f)",
                "description": "Gradiente de una función escalar de tres variables",
                "latex": r"""\nabla f = \operatorname{grad}(f) = \frac{\partial f}{\partial x}\mathbf{i} + \frac{\partial f}{\partial y}\mathbf{j} + \frac{\partial f}{\partial z}\mathbf{k}""",
                "builder": lambda: _parse_preset(
                    r"""\nabla f = \operatorname{grad}(f) = \frac{\partial f}{\partial x}\mathbf{i} + \frac{\partial f}{\partial y}\mathbf{j} + \frac{\partial f}{\partial z}\mathbf{k}"""
                ),
            },
        ],
    },
    {
        "id": "math_vector_calculus_diferenciabilidad_y_regla_de_la_cadena_multivariable",
        "domain": "math",
        "category": "math_vector_calculus",
        "level": "NIVEL INTERMEDIO",
        "title": "Diferenciabilidad y Regla de la Cadena Multivariable",
        "variations": [
            {
                "name": "Diferencial Total y Regla de la Cadena Multivariable",
                "description": "Diferencial exacta df y derivada total dw/dt",
                "latex": r"""df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz, \quad \frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt}""",
                "builder": lambda: _parse_preset(
                    r"""df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz, \quad \frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt}"""
                ),
            },
        ],
    },
    {
        "id": "math_vector_calculus_derivada_direccional_y_planos_tangentes",
        "domain": "math",
        "category": "math_vector_calculus",
        "level": "NIVEL INTERMEDIO",
        "title": "Derivada Direccional y Planos Tangentes",
        "variations": [
            {
                "name": "Derivada Direccional y Plano Tangente a Superficie de Nivel",
                "description": "Proyección direccional D_u f = ∇f · u y plano tangente a F(x,y,z) = c",
                "latex": r"""D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = \|\nabla f\|\cos(\theta), \quad F_x(P_0)(x - x_0) + F_y(P_0)(y - y_0) + F_z(P_0)(z - z_0) = 0""",
                "builder": lambda: _parse_preset(
                    r"""D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = \|\nabla f\|\cos(\theta), \quad F_x(P_0)(x - x_0) + F_y(P_0)(y - y_0) + F_z(P_0)(z - z_0) = 0"""
                ),
            },
        ],
    },
    {
        "id": "math_vector_calculus_optimizaci_n_multivariable",
        "domain": "math",
        "category": "math_vector_calculus",
        "level": "NIVEL INTERMEDIO",
        "title": "Optimización Multivariable",
        "variations": [
            {
                "name": "Matriz Hessiana y Multiplicadores de Lagrange",
                "description": "Criterio del discriminante Hessiano D = f_xx f_yy - (f_xy)² y extremos condicionados ∇f = λ ∇g",
                "latex": r"""D = \det\begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix} = f_{xx} f_{yy} - (f_{xy})^2, \quad \nabla f = \lambda \nabla g""",
                "builder": lambda: _parse_preset(
                    r"""D = \det\begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix} = f_{xx} f_{yy} - (f_{xy})^2, \quad \nabla f = \lambda \nabla g"""
                ),
            },
        ],
    },
    {
        "id": "math_vector_calculus_integrales_m_ltiples_y_transformaciones_de_coordenadas",
        "domain": "math",
        "category": "math_vector_calculus",
        "level": "NIVEL INTERMEDIO",
        "title": "Integrales Múltiples y Transformaciones de Coordenadas",
        "variations": [
            {
                "name": "Jacobiano y Elementos de Volumen en Coordenadas Polares, Cilíndricas y Esféricas",
                "description": "Transformación multivariable, Jacobiano y diferenciales dA, dV",
                "latex": r"""J(u, v) = \det\begin{pmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{pmatrix}, \quad dA = r \, dr \, d\theta, \quad dV = r \, dr \, d\theta \, dz = \rho^2 \sin(\varphi) \, d\rho \, d\varphi \, d\theta""",
                "builder": lambda: _parse_preset(
                    r"""J(u, v) = \det\begin{pmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{pmatrix}, \quad dA = r \, dr \, d\theta, \quad dV = r \, dr \, d\theta \, dz = \rho^2 \sin(\varphi) \, d\rho \, d\varphi \, d\theta"""
                ),
            },
        ],
    },
    {
        "id": "math_vector_calculus_operadores_diferenciales_vectoriales",
        "domain": "math",
        "category": "math_vector_calculus",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Operadores Diferenciales Vectoriales",
        "variations": [
            {
                "name": "Divergencia, Rotacional y Laplaciano",
                "description": "Operadores fundamentales div(F), rot(F) y Laplaciano escalar Δf",
                "latex": r"""\operatorname{div}(\mathbf{F}) = \nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}, \quad \operatorname{rot}(\mathbf{F}) = \nabla \times \mathbf{F}, \quad \Delta f = \nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}""",
                "builder": lambda: _parse_preset(
                    r"""\operatorname{div}(\mathbf{F}) = \nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}, \quad \operatorname{rot}(\mathbf{F}) = \nabla \times \mathbf{F}, \quad \Delta f = \nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}"""
                ),
            },
            {
                "name": "Identidades Diferenciales Vectoriales",
                "description": "Rotacional de gradiente nulo, divergencia de rotacional nula y reglas de producto",
                "latex": r"""\nabla \times (\nabla f) = \mathbf{0}, \quad \nabla \cdot (\nabla \times \mathbf{F}) = 0, \quad \nabla \cdot (f\mathbf{F}) = f(\nabla \cdot \mathbf{F}) + \mathbf{F} \cdot (\nabla f)""",
                "builder": lambda: _parse_preset(
                    r"""\nabla \times (\nabla f) = \mathbf{0}, \quad \nabla \cdot (\nabla \times \mathbf{F}) = 0, \quad \nabla \cdot (f\mathbf{F}) = f(\nabla \cdot \mathbf{F}) + \mathbf{F} \cdot (\nabla f)"""
                ),
            },
        ],
    },
    {
        "id": "math_vector_calculus_integrales_de_l_nea_y_superficie",
        "domain": "math",
        "category": "math_vector_calculus",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Integrales de Línea y Superficie",
        "variations": [
            {
                "name": "Integrales de Línea, Trabajo y Flujo de Superficie",
                "description": "Cálculo de circulación W = ∫ F · dr y flujo superficial Φ = ∬ F · dS",
                "latex": r"""W = \int_C \mathbf{F} \cdot d\mathbf{r} = \int_C (P \, dx + Q \, dy + R \, dz), \quad \Phi = \iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_D \mathbf{F} \cdot (\mathbf{r}_u \times \mathbf{r}_v) \, du \, dv""",
                "builder": lambda: _parse_preset(
                    r"""W = \int_C \mathbf{F} \cdot d\mathbf{r} = \int_C (P \, dx + Q \, dy + R \, dz), \quad \Phi = \iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_D \mathbf{F} \cdot (\mathbf{r}_u \times \mathbf{r}_v) \, du \, dv"""
                ),
            },
            {
                "name": "Teorema Fundamental para Integrales de Línea",
                "description": "Independencia de la trayectoria para campos conservativos F = ∇φ",
                "latex": r"""\mathbf{F} = \nabla \varphi \implies \int_C \mathbf{F} \cdot d\mathbf{r} = \varphi(\mathbf{r}(b)) - \varphi(\mathbf{r}(a))""",
                "builder": lambda: _parse_preset(
                    r"""\mathbf{F} = \nabla \varphi \implies \int_C \mathbf{F} \cdot d\mathbf{r} = \varphi(\mathbf{r}(b)) - \varphi(\mathbf{r}(a))"""
                ),
            },
        ],
    },
    {
        "id": "math_vector_calculus_teoremas_integrales_fundamentales_del_an_lisis_vectorial",
        "domain": "math",
        "category": "math_vector_calculus",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Teoremas Integrales Fundamentales del Análisis Vectorial",
        "variations": [
            {
                "name": "Teoremas de Green, Stokes y Divergencia de Gauss",
                "description": "Grandes teoremas del cálculo integral vectorial",
                "latex": r"""\oint_C (P \, dx + Q \, dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA, \quad \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}, \quad \iint_{\partial V} \mathbf{F} \cdot d\mathbf{S} = \iiint_V (\nabla \cdot \mathbf{F}) \, dV""",
                "builder": lambda: _parse_preset(
                    r"""\oint_C (P \, dx + Q \, dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA, \quad \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}, \quad \iint_{\partial V} \mathbf{F} \cdot d\mathbf{S} = \iiint_V (\nabla \cdot \mathbf{F}) \, dV"""
                ),
            },
        ],
    },
    {
        "id": "math_vector_calculus_geometr_a_diferencial_en_3_triedro_de_frenet_serret",
        "domain": "math",
        "category": "math_vector_calculus",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Geometría Diferencial en ℝ^3 (Triedro de Frenet-Serret)",
        "variations": [
            {
                "name": "Triedro y Fórmulas de Frenet-Serret",
                "description": "Vectores Tangente, Normal y Binormal (T, N, B) con curvatura κ y torsión τ",
                "latex": r"""\mathbf{T} = \frac{\mathbf{r}'}{\|\mathbf{r}'\|}, \quad \mathbf{B} = \mathbf{T} \times \mathbf{N}, \quad \frac{d\mathbf{T}}{ds} = \kappa \mathbf{N}, \quad \frac{d\mathbf{N}}{ds} = -\kappa \mathbf{T} + \tau \mathbf{B}, \quad \frac{d\mathbf{B}}{ds} = -\tau \mathbf{N}""",
                "builder": lambda: _parse_preset(
                    r"""\mathbf{T} = \frac{\mathbf{r}'}{\|\mathbf{r}'\|}, \quad \mathbf{B} = \mathbf{T} \times \mathbf{N}, \quad \frac{d\mathbf{T}}{ds} = \kappa \mathbf{N}, \quad \frac{d\mathbf{N}}{ds} = -\kappa \mathbf{T} + \tau \mathbf{B}, \quad \frac{d\mathbf{B}}{ds} = -\tau \mathbf{N}"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_equations_definiciones_y_clasificaci_n",
        "domain": "math",
        "category": "math_diff_equations",
        "level": "NIVEL BÁSICO",
        "title": "Definiciones y Clasificación",
        "variations": [
            {
                "name": "Problema de Valor Inicial (PVI)",
                "description": "EDO de primer orden sujeta a la condición inicial y(x_0) = y_0",
                "latex": r"""y' = f(x, y), \quad y(x_0) = y_0""",
                "builder": lambda: _parse_preset(
                    r"""y' = f(x, y), \quad y(x_0) = y_0"""
                ),
            },
            {
                "name": "Teorema de Picard-Lindelöf",
                "description": "Condiciones de continuidad de f y ∂f/∂y para existencia y unicidad",
                "latex": r"""y' = f(x, y), \quad y(x_0) = y_0 \implies \exists ! \, y(x) \quad \text{en } I""",
                "builder": lambda: _parse_preset(
                    r"""y' = f(x, y), \quad y(x_0) = y_0 \implies \exists ! \, y(x) \quad \text{en } I"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_equations_edos_de_1er_orden_elementales",
        "domain": "math",
        "category": "math_diff_equations",
        "level": "NIVEL BÁSICO",
        "title": "EDOs de 1er Orden Elementales",
        "variations": [
            {
                "name": "Variables Separables",
                "description": "Forma diferencial separable g(y) dy = f(x) dx e integración directa",
                "latex": r"""g(y) \, dy = f(x) \, dx \implies \int g(y) \, dy = \int f(x) \, dx + C""",
                "builder": lambda: _parse_preset(
                    r"""g(y) \, dy = f(x) \, dx \implies \int g(y) \, dy = \int f(x) \, dx + C"""
                ),
            },
            {
                "name": "Ecuación Lineal de Primer Orden",
                "description": "Forma canónica, factor integrante μ(x) = e^{∫ P dx} y solución general",
                "latex": r"""y' + P(x)y = Q(x), \quad \mu(x) = e^{\int P(x) \, dx}, \quad y(x) = \frac{1}{\mu(x)} \left[ \int \mu(x) Q(x) \, dx + C \right]""",
                "builder": lambda: _parse_preset(
                    r"""y' + P(x)y = Q(x), \quad \mu(x) = e^{\int P(x) \, dx}, \quad y(x) = \frac{1}{\mu(x)} \left[ \int \mu(x) Q(x) \, dx + C \right]"""
                ),
            },
            {
                "name": "Ecuaciones Diferenciales Exactas",
                "description": "Condición ∂M/∂y = ∂N/∂x y función potencial Ψ(x,y) = C",
                "latex": r"""M(x, y) \, dx + N(x, y) \, dy = 0, \quad \frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \implies \Psi(x, y) = C""",
                "builder": lambda: _parse_preset(
                    r"""M(x, y) \, dx + N(x, y) \, dy = 0, \quad \frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \implies \Psi(x, y) = C"""
                ),
            },
            {
                "name": "Factores Integrantes Especiales",
                "description": "Factores integrantes dependientes solo de x o de y",
                "latex": r"""\mu(x) = e^{\int \frac{M_y - N_x}{N} \, dx}, \quad \mu(y) = e^{\int \frac{N_x - M_y}{M} \, dy}""",
                "builder": lambda: _parse_preset(
                    r"""\mu(x) = e^{\int \frac{M_y - N_x}{N} \, dx}, \quad \mu(y) = e^{\int \frac{N_x - M_y}{M} \, dy}"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_equations_ecuaciones_reducibles_a_1er_orden",
        "domain": "math",
        "category": "math_diff_equations",
        "level": "NIVEL INTERMEDIO",
        "title": "Ecuaciones Reducibles a 1er Orden",
        "variations": [
            {
                "name": "Ecuación Homogénea de Grado n",
                "description": "Sustitución y = ux y derivada dy/dx = u + x(du/dx)",
                "latex": r"""\frac{dy}{dx} = F\left(\frac{y}{x}\right) \implies y = ux, \quad \frac{dy}{dx} = u + x\frac{du}{dx}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{dy}{dx} = F\left(\frac{y}{x}\right) \implies y = ux, \quad \frac{dy}{dx} = u + x\frac{du}{dx}"""
                ),
            },
            {
                "name": "Ecuación de Bernoulli",
                "description": "Transformación lineal con u = y^{1-n} para n ≠ 0, 1",
                "latex": r"""y' + P(x)y = Q(x)y^n, \quad u = y^{1 - n} \implies u' + (1 - n)P(x)u = (1 - n)Q(x)""",
                "builder": lambda: _parse_preset(
                    r"""y' + P(x)y = Q(x)y^n, \quad u = y^{1 - n} \implies u' + (1 - n)P(x)u = (1 - n)Q(x)"""
                ),
            },
            {
                "name": "Ecuaciones de Riccati y Clairaut",
                "description": "Formas canónicas y soluciones para Riccati y Clairaut",
                "latex": r"""y' = P(x) + Q(x)y + R(x)y^2, \quad y = x y' + f(y') \implies y = Cx + f(C)""",
                "builder": lambda: _parse_preset(
                    r"""y' = P(x) + Q(x)y + R(x)y^2, \quad y = x y' + f(y') \implies y = Cx + f(C)"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_equations_edos_lineales_de_orden_superior_con_coeficientes_constantes",
        "domain": "math",
        "category": "math_diff_equations",
        "level": "NIVEL INTERMEDIO",
        "title": "EDOs Lineales de Orden Superior con Coeficientes Constantes",
        "variations": [
            {
                "name": "Ecuación Característica (2° Orden)",
                "description": "Solución homogénea para raíces reales distintas, repetidas o complejas",
                "latex": r"""a r^2 + b r + c = 0 \implies y_h = c_1 e^{r_1 x} + c_2 e^{r_2 x}, \quad y_h = (c_1 + c_2 x)e^{r x}, \quad y_h = e^{\alpha x}(c_1 \cos(\beta x) + c_2 \sin(\beta x))""",
                "builder": lambda: _parse_preset(
                    r"""a r^2 + b r + c = 0 \implies y_h = c_1 e^{r_1 x} + c_2 e^{r_2 x}, \quad y_h = (c_1 + c_2 x)e^{r x}, \quad y_h = e^{\alpha x}(c_1 \cos(\beta x) + c_2 \sin(\beta x))"""
                ),
            },
            {
                "name": "Wronskiano y Fórmula de Abel",
                "description": "Determinante wronskiano y evolución diferencial de Abel",
                "latex": r"""W(y_1, y_2) = \det\begin{pmatrix} y_1 & y_2 \\ y_1' & y_2' \end{pmatrix} \ne 0, \quad W(x) = W(x_0) e^{-\int P(x) \, dx}""",
                "builder": lambda: _parse_preset(
                    r"""W(y_1, y_2) = \det\begin{pmatrix} y_1 & y_2 \\ y_1' & y_2' \end{pmatrix} \ne 0, \quad W(x) = W(x_0) e^{-\int P(x) \, dx}"""
                ),
            },
            {
                "name": "Variación de Parámetros",
                "description": "Solución particular y_p = u_1 y_1 + u_2 y_2 mediante el Wronskiano",
                "latex": r"""y_p = u_1 y_1 + u_2 y_2, \quad u_1' = -\frac{y_2 g(x)}{W}, \quad u_2' = \frac{y_1 g(x)}{W}""",
                "builder": lambda: _parse_preset(
                    r"""y_p = u_1 y_1 + u_2 y_2, \quad u_1' = -\frac{y_2 g(x)}{W}, \quad u_2' = \frac{y_1 g(x)}{W}"""
                ),
            },
            {
                "name": "Ecuación Equidimensional de Cauchy-Euler",
                "description": "Forma a x^2 y'' + b x y' + c y = 0 y ecuación auxiliar",
                "latex": r"""a x^2 y'' + b x y' + c y = 0 \implies a r(r - 1) + b r + c = 0""",
                "builder": lambda: _parse_preset(
                    r"""a x^2 y'' + b x y' + c y = 0 \implies a r(r - 1) + b r + c = 0"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_equations_transformada_de_laplace_para_edos",
        "domain": "math",
        "category": "math_diff_equations",
        "level": "NIVEL INTERMEDIO",
        "title": "Transformada de Laplace para EDOs",
        "variations": [
            {
                "name": "Transformada de Laplace",
                "description": "Definición integral unilateral ℒ{f(t)} = F(s)",
                "latex": r"""\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st} f(t) \, dt""",
                "builder": lambda: _parse_preset(
                    r"""\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st} f(t) \, dt"""
                ),
            },
            {
                "name": "Transformadas de Derivadas",
                "description": "Propiedad de derivación temporal en el dominio de Laplace",
                "latex": r"""\mathcal{L}\{f'(t)\} = s F(s) - f(0), \quad \mathcal{L}\{f''(t)\} = s^2 F(s) - s f(0) - f'(0)""",
                "builder": lambda: _parse_preset(
                    r"""\mathcal{L}\{f'(t)\} = s F(s) - f(0), \quad \mathcal{L}\{f''(t)\} = s^2 F(s) - s f(0) - f'(0)"""
                ),
            },
            {
                "name": "Propiedades de Traslación, Convolución y Delta de Dirac",
                "description": "Desplazamiento en s y t, teorema de convolución y distribución delta",
                "latex": r"""\mathcal{L}\{e^{at} f(t)\} = F(s - a), \quad \mathcal{L}\{(f * g)(t)\} = F(s)G(s), \quad \mathcal{L}\{\delta(t - t_0)\} = e^{-s t_0}""",
                "builder": lambda: _parse_preset(
                    r"""\mathcal{L}\{e^{at} f(t)\} = F(s - a), \quad \mathcal{L}\{(f * g)(t)\} = F(s)G(s), \quad \mathcal{L}\{\delta(t - t_0)\} = e^{-s t_0}"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_equations_soluci_n_de_edos_por_series_y_funciones_especiales",
        "domain": "math",
        "category": "math_diff_equations",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Solución de EDOs por Series y Funciones Especiales",
        "variations": [
            {
                "name": "Series de Potencias y Método de Frobenius",
                "description": "Solución en punto ordinario y singular regular con ecuación indicial",
                "latex": r"""y(x) = \sum_{n=0}^{\infty} c_n x^n, \quad y(x) = x^r \sum_{n=0}^{\infty} c_n x^n, \quad F(r) = r(r - 1) + p_0 r + q_0 = 0""",
                "builder": lambda: _parse_preset(
                    r"""y(x) = \sum_{n=0}^{\infty} c_n x^n, \quad y(x) = x^r \sum_{n=0}^{\infty} c_n x^n, \quad F(r) = r(r - 1) + p_0 r + q_0 = 0"""
                ),
            },
            {
                "name": "Ecuaciones Diferenciales de Bessel y Legendre",
                "description": "EDOs de la física matemática y soluciones por funciones de Bessel y polinomios de Legendre",
                "latex": r"""x^2 y'' + x y' + (x^2 - \nu^2)y = 0 \implies y = c_1 J_\nu(x) + c_2 Y_\nu(x), \quad (1 - x^2)y'' - 2x y' + n(n + 1)y = 0""",
                "builder": lambda: _parse_preset(
                    r"""x^2 y'' + x y' + (x^2 - \nu^2)y = 0 \implies y = c_1 J_\nu(x) + c_2 Y_\nu(x), \quad (1 - x^2)y'' - 2x y' + n(n + 1)y = 0"""
                ),
            },
        ],
    },
    {
        "id": "math_diff_equations_sistemas_lineales_y_ecuaciones_en_derivadas_parciales",
        "domain": "math",
        "category": "math_diff_equations",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Sistemas Lineales y Ecuaciones en Derivadas Parciales",
        "variations": [
            {
                "name": "Sistemas Lineales y Matriz Exponencial",
                "description": "Sistema x' = Ax + g y solución fundamental homogénea x(t) = e^{At} x(0)",
                "latex": r"""\mathbf{x}'(t) = A\mathbf{x}(t) + \mathbf{g}(t), \quad e^{At} = \sum_{k=0}^{\infty} \frac{A^k t^k}{k!}, \quad \mathbf{x}(t) = e^{At}\mathbf{x}(0)""",
                "builder": lambda: _parse_preset(
                    r"""\mathbf{x}'(t) = A\mathbf{x}(t) + \mathbf{g}(t), \quad e^{At} = \sum_{k=0}^{\infty} \frac{A^k t^k}{k!}, \quad \mathbf{x}(t) = e^{At}\mathbf{x}(0)"""
                ),
            },
            {
                "name": "Ecuaciones de Onda, Calor y Laplace",
                "description": "EDPs clásicas hiperbólica, parabólica y elíptica",
                "latex": r"""\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u, \quad \frac{\partial u}{\partial t} = \alpha \nabla^2 u, \quad \nabla^2 u = 0""",
                "builder": lambda: _parse_preset(
                    r"""\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u, \quad \frac{\partial u}{\partial t} = \alpha \nabla^2 u, \quad \nabla^2 u = 0"""
                ),
            },
            {
                "name": "Soluciones de d'Alembert y Núcleo del Calor",
                "description": "Fórmula 1D de d'Alembert para ondas y núcleo gaussiano del calor",
                "latex": r"""u(x, t) = \frac{f(x - ct) + f(x + ct)}{2} + \frac{1}{2c}\int_{x - ct}^{x + ct} g(s) \, ds, \quad \Phi(x, t) = \frac{1}{\sqrt{4\pi \alpha t}} e^{-\frac{x^2}{4\alpha t}}""",
                "builder": lambda: _parse_preset(
                    r"""u(x, t) = \frac{f(x - ct) + f(x + ct)}{2} + \frac{1}{2c}\int_{x - ct}^{x + ct} g(s) \, ds, \quad \Phi(x, t) = \frac{1}{\sqrt{4\pi \alpha t}} e^{-\frac{x^2}{4\alpha t}}"""
                ),
            },
            {
                "name": "Problemas de Sturm-Liouville y Ortogonalidad",
                "description": "Forma autoadjunta y ortogonalidad de autofunciones respecto al peso w(x)",
                "latex": r"""\frac{d}{dx}\left[ p(x)\frac{dy}{dx} \right] + q(x)y + \lambda w(x)y = 0, \quad \int_a^b \phi_n(x)\phi_m(x)w(x) \, dx = 0""",
                "builder": lambda: _parse_preset(
                    r"""\frac{d}{dx}\left[ p(x)\frac{dy}{dx} \right] + q(x)y + \lambda w(x)y = 0, \quad \int_a^b \phi_n(x)\phi_m(x)w(x) \, dx = 0"""
                ),
            },
        ],
    },
    {
        "id": "math_numerical_methods_teor_a_de_errores",
        "domain": "math",
        "category": "math_numerical_methods",
        "level": "NIVEL BÁSICO",
        "title": "Teoría de Errores",
        "variations": [
            {
                "name": "Teoría de Errores",
                "description": "Cálculo de error absoluto, relativo, porcentual y relativo aproximado",
                "latex": r"""E_a = |x - \hat{x}|, \quad E_r = \frac{|x - \hat{x}|}{|x|}, \quad \varepsilon_a = \left|\frac{x_{\text{actual}} - x_{\text{anterior}}}{x_{\text{actual}}}\right| \cdot 100\%""",
                "builder": lambda: _parse_preset(
                    r"""E_a = |x - \hat{x}|, \quad E_r = \frac{|x - \hat{x}|}{|x|}, \quad \varepsilon_a = \left|\frac{x_{\text{actual}} - x_{\text{anterior}}}{x_{\text{actual}}}\right| \cdot 100\%"""
                ),
            },
        ],
    },
    {
        "id": "math_numerical_methods_ra_ces_de_ecuaciones_no_lineales_m_todos_cerrados",
        "domain": "math",
        "category": "math_numerical_methods",
        "level": "NIVEL BÁSICO",
        "title": "Raíces de Ecuaciones No Lineales (Métodos Cerrados)",
        "variations": [
            {
                "name": "Método de Bisección",
                "description": "Punto medio c = (a+b)/2 y cota teórica del error tras n iteraciones",
                "latex": r"""c = \frac{a + b}{2}, \quad E_n \le \frac{b - a}{2^n}, \quad n \ge \log_2\left(\frac{b - a}{\varepsilon}\right)""",
                "builder": lambda: _parse_preset(
                    r"""c = \frac{a + b}{2}, \quad E_n \le \frac{b - a}{2^n}, \quad n \ge \log_2\left(\frac{b - a}{\varepsilon}\right)"""
                ),
            },
            {
                "name": "Método de Falsa Posición (Regula Falsi)",
                "description": "Intersección secante ponderada para raíces cerradas",
                "latex": r"""c = \frac{a f(b) - b f(a)}{f(b) - f(a)}""",
                "builder": lambda: _parse_preset(
                    r"""c = \frac{a f(b) - b f(a)}{f(b) - f(a)}"""
                ),
            },
        ],
    },
    {
        "id": "math_numerical_methods_ra_ces_de_ecuaciones_no_lineales_m_todos_abiertos",
        "domain": "math",
        "category": "math_numerical_methods",
        "level": "NIVEL INTERMEDIO",
        "title": "Raíces de Ecuaciones No Lineales (Métodos Abiertos)",
        "variations": [
            {
                "name": "Iteración de Punto Fijo",
                "description": "Esquema x_{k+1} = g(x_k) y condición de convergencia |g'(x)| < 1",
                "latex": r"""f(x) = 0 \iff x = g(x), \quad x_{k+1} = g(x_k), \quad |g'(x)| < 1""",
                "builder": lambda: _parse_preset(
                    r"""f(x) = 0 \iff x = g(x), \quad x_{k+1} = g(x_k), \quad |g'(x)| < 1"""
                ),
            },
            {
                "name": "Método de Newton-Raphson",
                "description": "Esquema x_{k+1} = x_k - f(x_k)/f'(x_k) con convergencia cuadrática",
                "latex": r"""x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}""",
                "builder": lambda: _parse_preset(
                    r"""x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}"""
                ),
            },
            {
                "name": "Método de la Secante y Newton Multivariable",
                "description": "Esquema de la secante y esquema multivariable con la matriz Jacobiana J",
                "latex": r"""x_{k+1} = x_k - f(x_k)\frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}, \quad \mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} - [J(\mathbf{x}^{(k)})]^{-1}\mathbf{F}(\mathbf{x}^{(k)})""",
                "builder": lambda: _parse_preset(
                    r"""x_{k+1} = x_k - f(x_k)\frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}, \quad \mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} - [J(\mathbf{x}^{(k)})]^{-1}\mathbf{F}(\mathbf{x}^{(k)})"""
                ),
            },
        ],
    },
    {
        "id": "math_numerical_methods_m_todos_iterativos_para_sistemas_lineales",
        "domain": "math",
        "category": "math_numerical_methods",
        "level": "NIVEL INTERMEDIO",
        "title": "Métodos Iterativos para Sistemas Lineales",
        "variations": [
            {
                "name": "Métodos de Jacobi y Gauss-Seidel",
                "description": "Esquemas iterativos por componentes para resolver Ax = b",
                "latex": r"""x_i^{(k+1)} = \frac{b_i - \sum_{j \ne i} a_{ij}x_j^{(k)}}{a_{ii}}, \quad x_i^{(k+1)} = \frac{b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)}}{a_{ii}}""",
                "builder": lambda: _parse_preset(
                    r"""x_i^{(k+1)} = \frac{b_i - \sum_{j \ne i} a_{ij}x_j^{(k)}}{a_{ii}}, \quad x_i^{(k+1)} = \frac{b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)}}{a_{ii}}"""
                ),
            },
            {
                "name": "Método de Sobrerrelajación Sucesiva (SOR)",
                "description": "Esquema acelerado con factor de relajación 0 < ω < 2",
                "latex": r"""x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \frac{\omega}{a_{ii}}\left[ b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)} \right]""",
                "builder": lambda: _parse_preset(
                    r"""x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \frac{\omega}{a_{ii}}\left[ b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)} \right]"""
                ),
            },
        ],
    },
    {
        "id": "math_numerical_methods_interpolaci_n_y_ajuste_de_curvas",
        "domain": "math",
        "category": "math_numerical_methods",
        "level": "NIVEL INTERMEDIO",
        "title": "Interpolación y Ajuste de Curvas",
        "variations": [
            {
                "name": "Interpolación de Lagrange y Newton",
                "description": "Polinomios interpoladores de Lagrange y diferencias divididas de Newton",
                "latex": r"""P_n(x) = \sum_{i=0}^n y_i \prod_{j \ne i} \frac{x - x_j}{x_i - x_j}, \quad P_n(x) = f[x_0] + \sum_{k=1}^n f[x_0, \dots, x_k] \prod_{j=0}^{k-1} (x - x_j)""",
                "builder": lambda: _parse_preset(
                    r"""P_n(x) = \sum_{i=0}^n y_i \prod_{j \ne i} \frac{x - x_j}{x_i - x_j}, \quad P_n(x) = f[x_0] + \sum_{k=1}^n f[x_0, \dots, x_k] \prod_{j=0}^{k-1} (x - x_j)"""
                ),
            },
            {
                "name": "Regresión Lineal por Mínimos Cuadrados",
                "description": "Fórmulas analíticas de ajuste lineal y = a_0 + a_1 x",
                "latex": r"""a_1 = \frac{n \sum x_i y_i - \sum x_i \sum y_i}{n \sum x_i^2 - (\sum x_i)^2}, \quad a_0 = \bar{y} - a_1 \bar{x}""",
                "builder": lambda: _parse_preset(
                    r"""a_1 = \frac{n \sum x_i y_i - \sum x_i \sum y_i}{n \sum x_i^2 - (\sum x_i)^2}, \quad a_0 = \bar{y} - a_1 \bar{x}"""
                ),
            },
        ],
    },
    {
        "id": "math_numerical_methods_diferenciaci_n_e_integraci_n_num_rica",
        "domain": "math",
        "category": "math_numerical_methods",
        "level": "NIVEL INTERMEDIO",
        "title": "Diferenciación e Integración Numérica",
        "variations": [
            {
                "name": "Diferencias Finitas (1° y 2° Orden)",
                "description": "Aproximaciones numéricas de la primera y segunda derivada",
                "latex": r"""f'(x) \approx \frac{f(x + h) - f(x)}{h}, \quad f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}, \quad f''(x) \approx \frac{f(x + h) - 2f(x) + f(x - h)}{h^2}""",
                "builder": lambda: _parse_preset(
                    r"""f'(x) \approx \frac{f(x + h) - f(x)}{h}, \quad f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}, \quad f''(x) \approx \frac{f(x + h) - 2f(x) + f(x - h)}{h^2}"""
                ),
            },
            {
                "name": "Reglas de Integración de Trapecio y Simpson 1/3, 3/8",
                "description": "Cuadraturas numéricas de Trapecio y Simpson simple y compuesta",
                "latex": r"""\int_a^b f(x) \, dx \approx \frac{h}{2}[f(a) + f(b)], \quad \int_a^b f(x) \, dx \approx \frac{h}{3}[f(x_0) + 4f(x_1) + f(x_2)], \quad \int_a^b f(x) \, dx \approx \frac{3h}{8}[f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]""",
                "builder": lambda: _parse_preset(
                    r"""\int_a^b f(x) \, dx \approx \frac{h}{2}[f(a) + f(b)], \quad \int_a^b f(x) \, dx \approx \frac{h}{3}[f(x_0) + 4f(x_1) + f(x_2)], \quad \int_a^b f(x) \, dx \approx \frac{3h}{8}[f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]"""
                ),
            },
            {
                "name": "Cuadratura de Gauss-Legendre",
                "description": "Integración numérica con pesos y nodos óptimos de Legendre",
                "latex": r"""\int_{-1}^1 g(t) \, dt \approx \sum_{i=1}^n w_i g(t_i), \quad x = \frac{(b - a)t + (a + b)}{2}""",
                "builder": lambda: _parse_preset(
                    r"""\int_{-1}^1 g(t) \, dt \approx \sum_{i=1}^n w_i g(t_i), \quad x = \frac{(b - a)t + (a + b)}{2}"""
                ),
            },
        ],
    },
    {
        "id": "math_numerical_methods_soluci_n_num_rica_de_edos_pvi_y_pvf",
        "domain": "math",
        "category": "math_numerical_methods",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Solución Numérica de EDOs (PVI y PVF)",
        "variations": [
            {
                "name": "Métodos de Euler y Heun (Euler Mejorado)",
                "description": "Esquema explícito de Euler y predictor-corrector de Heun",
                "latex": r"""y_{n+1} = y_n + h f(t_n, y_n), \quad y_{n+1} = y_n + \frac{h}{2}[f(t_n, y_n) + f(t_{n+1}, y_{n+1}^*)]""",
                "builder": lambda: _parse_preset(
                    r"""y_{n+1} = y_n + h f(t_n, y_n), \quad y_{n+1} = y_n + \frac{h}{2}[f(t_n, y_n) + f(t_{n+1}, y_{n+1}^*)]"""
                ),
            },
            {
                "name": "Método de Runge-Kutta de 4° Orden (RK4)",
                "description": "Algoritmo clásico RK4 con pendientes intermedias k_1, k_2, k_3, k_4",
                "latex": r"""y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4), \quad k_1 = f(t_n, y_n), \quad k_2 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)""",
                "builder": lambda: _parse_preset(
                    r"""y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4), \quad k_1 = f(t_n, y_n), \quad k_2 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)"""
                ),
            },
            {
                "name": "Métodos Multipaso de Adams",
                "description": "Esquema explícito de Adams-Bashforth y esquema implícito de Adams-Moulton",
                "latex": r"""y_{n+1} = y_n + \frac{h}{24}[55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3}], \quad y_{n+1} = y_n + \frac{h}{24}[9f_{n+1} + 19f_n - 5f_{n-1} + f_{n-2}]""",
                "builder": lambda: _parse_preset(
                    r"""y_{n+1} = y_n + \frac{h}{24}[55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3}], \quad y_{n+1} = y_n + \frac{h}{24}[9f_{n+1} + 19f_n - 5f_{n-1} + f_{n-2}]"""
                ),
            },
            {
                "name": "Métodos para Problemas de Valor en la Frontera (PVF)",
                "description": "Método de disparo lineal y discretización tridiagonal por diferencias finitas",
                "latex": r"""y(x) = u(x) + \frac{\beta - u(b)}{v(b)} v(x), \quad \frac{y_{i+1} - 2y_i + y_{i-1}}{h^2} = p(x_i)\frac{y_{i+1} - y_{i-1}}{2h} + q(x_i)y_i + r(x_i)""",
                "builder": lambda: _parse_preset(
                    r"""y(x) = u(x) + \frac{\beta - u(b)}{v(b)} v(x), \quad \frac{y_{i+1} - 2y_i + y_{i-1}}{h^2} = p(x_i)\frac{y_{i+1} - y_{i-1}}{2h} + q(x_i)y_i + r(x_i)"""
                ),
            },
        ],
    },
    {
        "id": "math_numerical_methods_soluci_n_num_rica_de_ecuaciones_diferenciales_parciales_edp",
        "domain": "math",
        "category": "math_numerical_methods",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Solución Numérica de Ecuaciones Diferenciales Parciales (EDP)",
        "variations": [
            {
                "name": "Diferencias Finitas para EDPs (Laplace, Crank-Nicolson y CFL)",
                "description": "Esquema de 5 puntos para Laplace, Crank-Nicolson para calor y condición CFL para ondas",
                "latex": r"""u_{i+1, j} + u_{i-1, j} + u_{i, j+1} + u_{i, j-1} - 4u_{i, j} = h^2 f_{i, j}, \quad C = \frac{c \Delta t}{\Delta x} \le 1""",
                "builder": lambda: _parse_preset(
                    r"""u_{i+1, j} + u_{i-1, j} + u_{i, j+1} + u_{i, j-1} - 4u_{i, j} = h^2 f_{i, j}, \quad C = \frac{c \Delta t}{\Delta x} \le 1"""
                ),
            },
        ],
    },
    {
        "id": "math_statistics_distribuciones_de_probabilidad",
        "domain": "math",
        "category": "math_statistics",
        "level": "NIVEL INTERMEDIO",
        "title": "Distribuciones de Probabilidad",
        "variations": [
            {
                "name": "Distribución Normal",
                "description": "Función de densidad de probabilidad gaussiana N(μ, σ²)",
                "latex": r"""f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2}""",
                "builder": lambda: _parse_preset(
                    r"""f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2}"""
                ),
            },
            {
                "name": "Distribución de Poisson",
                "description": "Probabilidad de eventos raros en intervalo continuo",
                "latex": r"""P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}""",
                "builder": lambda: _parse_preset(
                    r"""P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}"""
                ),
            },
        ],
    },
    {
        "id": "math_statistics_probabilidad_condicional",
        "domain": "math",
        "category": "math_statistics",
        "level": "NIVEL INTERMEDIO",
        "title": "Probabilidad Condicional",
        "variations": [
            {
                "name": "Teorema de Bayes",
                "description": "Probabilidad condicional e inferencia bayesiana",
                "latex": r"""P(A|B) = \frac{P(B|A) P(A)}{P(B)}""",
                "builder": lambda: _parse_preset(
                    r"""P(A|B) = \frac{P(B|A) P(A)}{P(B)}"""
                ),
            },
        ],
    },
    {
        "id": "math_statistics_variables_aleatorias",
        "domain": "math",
        "category": "math_statistics",
        "level": "NIVEL INTERMEDIO",
        "title": "Variables Aleatorias",
        "variations": [
            {
                "name": "Esperanza Matemática",
                "description": "Valor esperado de variable aleatoria discreta",
                "latex": r"""\mathbb{E}[X] = \sum_{i} x_i P(X = x_i)""",
                "builder": lambda: _parse_preset(
                    r"""\mathbb{E}[X] = \sum_{i} x_i P(X = x_i)"""
                ),
            },
            {
                "name": "Varianza Poblacional",
                "description": "Dispersión cuadrática respecto a la media",
                "latex": r"""\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2""",
                "builder": lambda: _parse_preset(
                    r"""\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2"""
                ),
            },
        ],
    },
    {
        "id": "phys_kinematics_dynamics_movimiento_rectil_neo_uniforme_mru",
        "domain": "physics",
        "category": "phys_kinematics_dynamics",
        "level": "NIVEL BÁSICO",
        "title": "Movimiento Rectilíneo Uniforme (MRU)",
        "variations": [
            {
                "name": "Posición y Velocidad Media en MRU",
                "description": "Ecuación horaria y velocidad media en movimiento rectilíneo uniforme",
                "latex": r"""x(t) = x_0 + v t, \quad v_m = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}""",
                "builder": lambda: _parse_preset(
                    r"""x(t) = x_0 + v t, \quad v_m = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}"""
                ),
            },
        ],
    },
    {
        "id": "phys_kinematics_dynamics_movimiento_rectil_neo_uniformemente_acelerado_mrua",
        "domain": "physics",
        "category": "phys_kinematics_dynamics",
        "level": "NIVEL BÁSICO",
        "title": "Movimiento Rectilíneo Uniformemente Acelerado (MRUA)",
        "variations": [
            {
                "name": "Ecuaciones de MRUA y Ecuación de Torricelli",
                "description": "Velocidad, posición horaria y relación independiente del tiempo de Torricelli",
                "latex": r"""v(t) = v_0 + a t, \quad x(t) = x_0 + v_0 t + \frac{1}{2} a t^2, \quad v_f^2 = v_0^2 + 2a (x_f - x_0)""",
                "builder": lambda: _parse_preset(
                    r"""v(t) = v_0 + a t, \quad x(t) = x_0 + v_0 t + \frac{1}{2} a t^2, \quad v_f^2 = v_0^2 + 2a (x_f - x_0)"""
                ),
            },
        ],
    },
    {
        "id": "phys_kinematics_dynamics_leyes_del_movimiento_de_newton",
        "domain": "physics",
        "category": "phys_kinematics_dynamics",
        "level": "NIVEL BÁSICO",
        "title": "Leyes del Movimiento de Newton",
        "variations": [
            {
                "name": "Leyes de Newton (Inercia, Dinámica y Acción-Reacción)",
                "description": "Las tres leyes fundamentales de la mecánica clásica newtoniana",
                "latex": r"""\sum \vec{F} = \vec{0}, \quad \sum \vec{F} = m \vec{a} = \frac{d\vec{p}}{dt}, \quad \vec{F}_{AB} = -\vec{F}_{BA}""",
                "builder": lambda: _parse_preset(
                    r"""\sum \vec{F} = \vec{0}, \quad \sum \vec{F} = m \vec{a} = \frac{d\vec{p}}{dt}, \quad \vec{F}_{AB} = -\vec{F}_{BA}"""
                ),
            },
        ],
    },
    {
        "id": "phys_kinematics_dynamics_fuerzas_de_fricci_n_rozamiento",
        "domain": "physics",
        "category": "phys_kinematics_dynamics",
        "level": "NIVEL BÁSICO",
        "title": "Fuerzas de Fricción / Rozamiento",
        "variations": [
            {
                "name": "Fricción Estática Máxima y Fricción Cinética",
                "description": "Leyes fenomenológicas de fricción seca de Coulomb",
                "latex": r"""f_{s,\text{max}} = \mu_s N, \quad f_k = \mu_k N""",
                "builder": lambda: _parse_preset(
                    r"""f_{s,\text{max}} = \mu_s N, \quad f_k = \mu_k N"""
                ),
            },
        ],
    },
    {
        "id": "phys_kinematics_dynamics_movimiento_circular_mcu_y_mcuv",
        "domain": "physics",
        "category": "phys_kinematics_dynamics",
        "level": "NIVEL BÁSICO",
        "title": "Movimiento Circular (MCU y MCUV)",
        "variations": [
            {
                "name": "Cinemática Circular y Aceleración Centrípeta",
                "description": "Relaciones lineales-angulares, aceleración normal a_c = v²/r y cinemática MCUV",
                "latex": r"""v = \omega r, \quad a_c = \frac{v^2}{r} = \omega^2 r, \quad \theta(t) = \theta_0 + \omega_0 t + \frac{1}{2} \alpha t^2, \quad \omega_f^2 = \omega_0^2 + 2\alpha (\theta_f - \theta_0)""",
                "builder": lambda: _parse_preset(
                    r"""v = \omega r, \quad a_c = \frac{v^2}{r} = \omega^2 r, \quad \theta(t) = \theta_0 + \omega_0 t + \frac{1}{2} \alpha t^2, \quad \omega_f^2 = \omega_0^2 + 2\alpha (\theta_f - \theta_0)"""
                ),
            },
        ],
    },
    {
        "id": "phys_kinematics_dynamics_cinem_tica_y_din_mica_vectorial_tridimensional",
        "domain": "physics",
        "category": "phys_kinematics_dynamics",
        "level": "NIVEL INTERMEDIO",
        "title": "Cinemática y Dinámica Vectorial Tridimensional",
        "variations": [
            {
                "name": "Aceleración Intrínseca y Coordenadas Polares Planas",
                "description": "Componentes tangencial/normal de aceleración y componentes radial/transversal",
                "latex": r"""\vec{a} = \frac{dv}{dt}\hat{u}_t + \frac{v^2}{\rho}\hat{u}_n, \quad \vec{v} = \dot{r}\hat{u}_r + r\dot{\theta}\hat{u}_\theta, \quad \vec{a} = (\ddot{r} - r\dot{\theta}^2)\hat{u}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{u}_\theta""",
                "builder": lambda: _parse_preset(
                    r"""\vec{a} = \frac{dv}{dt}\hat{u}_t + \frac{v^2}{\rho}\hat{u}_n, \quad \vec{v} = \dot{r}\hat{u}_r + r\dot{\theta}\hat{u}_\theta, \quad \vec{a} = (\ddot{r} - r\dot{\theta}^2)\hat{u}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{u}_\theta"""
                ),
            },
        ],
    },
    {
        "id": "phys_kinematics_dynamics_sistemas_de_referencia_no_inerciales",
        "domain": "physics",
        "category": "phys_kinematics_dynamics",
        "level": "NIVEL INTERMEDIO",
        "title": "Sistemas de Referencia No Inerciales",
        "variations": [
            {
                "name": "Fuerzas Ficticias (Coriolis y Centrífuga)",
                "description": "Dinámica en sistemas acelerados y rotatorios con fuerzas de inercia",
                "latex": r"""\vec{F}_{\text{Coriolis}} = -2m (\vec{\omega} \times \vec{v}'), \quad \vec{F}_{\text{centrifuga}} = -m\vec{\omega} \times (\vec{\omega} \times \vec{r}')""",
                "builder": lambda: _parse_preset(
                    r"""\vec{F}_{\text{Coriolis}} = -2m (\vec{\omega} \times \vec{v}'), \quad \vec{F}_{\text{centrifuga}} = -m\vec{\omega} \times (\vec{\omega} \times \vec{r}')"""
                ),
            },
        ],
    },
    {
        "id": "phys_kinematics_dynamics_din_mica_rotacional_del_cuerpo_r_gido",
        "domain": "physics",
        "category": "phys_kinematics_dynamics",
        "level": "NIVEL INTERMEDIO",
        "title": "Dinámica Rotacional del Cuerpo Rígido",
        "variations": [
            {
                "name": "Torque, Inercia y Teoremas de Steiner y Ejes Perpendiculares",
                "description": "Ecuación fundamental τ = Iα y teoremas de transporte de momento de inercia",
                "latex": r"""\vec{\tau} = \vec{r} \times \vec{F}, \quad \sum \tau = I \alpha, \quad I = I_{\text{CM}} + M d^2, \quad I_z = I_x + I_y""",
                "builder": lambda: _parse_preset(
                    r"""\vec{\tau} = \vec{r} \times \vec{F}, \quad \sum \tau = I \alpha, \quad I = I_{\text{CM}} + M d^2, \quad I_z = I_x + I_y"""
                ),
            },
        ],
    },
    {
        "id": "phys_kinematics_dynamics_din_mica_tridimensional_del_s_lido_r_gido",
        "domain": "physics",
        "category": "phys_kinematics_dynamics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Dinámica Tridimensional del Sólido Rígido",
        "variations": [
            {
                "name": "Tensor de Inercia y Ecuaciones de Euler para el Sólido Rígido",
                "description": "Momento angular L = Iω y ecuaciones dinámicas de Euler en ejes principales",
                "latex": r"""\vec{L} = \mathbf{I} \vec{\omega}, \quad I_1 \dot{\omega}_1 - (I_2 - I_3)\omega_2 \omega_3 = \tau_1, \quad I_2 \dot{\omega}_2 - (I_3 - I_1)\omega_3 \omega_1 = \tau_2, \quad I_3 \dot{\omega}_3 - (I_1 - I_2)\omega_1 \omega_2 = \tau_3""",
                "builder": lambda: _parse_preset(
                    r"""\vec{L} = \mathbf{I} \vec{\omega}, \quad I_1 \dot{\omega}_1 - (I_2 - I_3)\omega_2 \omega_3 = \tau_1, \quad I_2 \dot{\omega}_2 - (I_3 - I_1)\omega_3 \omega_1 = \tau_2, \quad I_3 \dot{\omega}_3 - (I_1 - I_2)\omega_1 \omega_2 = \tau_3"""
                ),
            },
        ],
    },
    {
        "id": "phys_energy_gravitation_trabajo_y_energ_a_mec_nica",
        "domain": "physics",
        "category": "phys_energy_gravitation",
        "level": "NIVEL BÁSICO",
        "title": "Trabajo y Energía Mecánica",
        "variations": [
            {
                "name": "Trabajo y Teorema de la Energía Cinética",
                "description": "Trabajo de fuerza constante y teorema W_neto = ΔE_k",
                "latex": r"""W = \vec{F} \cdot \Delta\vec{r} = F \Delta r \cos(\theta), \quad E_k = \frac{1}{2} m v^2, \quad W_{\text{neto}} = \Delta E_k = \frac{1}{2} m v_f^2 - \frac{1}{2} m v_0^2""",
                "builder": lambda: _parse_preset(
                    r"""W = \vec{F} \cdot \Delta\vec{r} = F \Delta r \cos(\theta), \quad E_k = \frac{1}{2} m v^2, \quad W_{\text{neto}} = \Delta E_k = \frac{1}{2} m v_f^2 - \frac{1}{2} m v_0^2"""
                ),
            },
            {
                "name": "Energías Potenciales y Conservación de la Energía Mecánica",
                "description": "Energía potencial gravitatoria, elástica y balance de fuerzas no conservativas",
                "latex": r"""E_{p,\text{grav}} = m g h, \quad E_{p,\text{elas}} = \frac{1}{2} k x^2, \quad \Delta E_m = W_{\text{NC}}""",
                "builder": lambda: _parse_preset(
                    r"""E_{p,\text{grav}} = m g h, \quad E_{p,\text{elas}} = \frac{1}{2} k x^2, \quad \Delta E_m = W_{\text{NC}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_energy_gravitation_cantidad_de_movimiento_e_impulso",
        "domain": "physics",
        "category": "phys_energy_gravitation",
        "level": "NIVEL BÁSICO",
        "title": "Cantidad de Movimiento e Impulso",
        "variations": [
            {
                "name": "Momento Lineal, Impulso y Coeficiente de Restitución",
                "description": "Impulso J = Δp y coeficiente de restitución en choques unidimensionales",
                "latex": r"""\vec{p} = m \vec{v}, \quad \vec{J} = \vec{F}_{\text{prom}} \Delta t = \Delta \vec{p}, \quad e = \frac{v_{2f} - v_{1f}}{v_{1i} - v_{2i}}""",
                "builder": lambda: _parse_preset(
                    r"""\vec{p} = m \vec{v}, \quad \vec{J} = \vec{F}_{\text{prom}} \Delta t = \Delta \vec{p}, \quad e = \frac{v_{2f} - v_{1f}}{v_{1i} - v_{2i}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_energy_gravitation_mec_nica_de_sistemas_de_part_culas",
        "domain": "physics",
        "category": "phys_energy_gravitation",
        "level": "NIVEL INTERMEDIO",
        "title": "Mecánica de Sistemas de Partículas",
        "variations": [
            {
                "name": "Potencial Conservativo, Centro de Masas y Teoremas de König",
                "description": "Campo F = -∇U, posición del CM y descomposición de energía cinética y momento angular",
                "latex": r"""\vec{F} = -\nabla U, \quad \vec{R}_{\text{CM}} = \frac{1}{M}\int \vec{r} \, dm, \quad E_k = \frac{1}{2} M v_{\text{CM}}^2 + E_k', \quad \vec{L} = \vec{R}_{\text{CM}} \times \vec{P}_{\text{total}} + \vec{L}'""",
                "builder": lambda: _parse_preset(
                    r"""\vec{F} = -\nabla U, \quad \vec{R}_{\text{CM}} = \frac{1}{M}\int \vec{r} \, dm, \quad E_k = \frac{1}{2} M v_{\text{CM}}^2 + E_k', \quad \vec{L} = \vec{R}_{\text{CM}} \times \vec{P}_{\text{total}} + \vec{L}'"""
                ),
            },
        ],
    },
    {
        "id": "phys_energy_gravitation_gravitaci_n_universal_y_fuerzas_centrales",
        "domain": "physics",
        "category": "phys_energy_gravitation",
        "level": "NIVEL INTERMEDIO",
        "title": "Gravitación Universal y Fuerzas Centrales",
        "variations": [
            {
                "name": "Ley de Gravitación, Leyes de Kepler y Velocidades de Escape",
                "description": "Atracción gravitatoria de Newton, leyes de Kepler y velocidad de escape",
                "latex": r"""\vec{F}_g = -G \frac{m_1 m_2}{r^2} \hat{u}_r, \quad U(r) = -G \frac{m_1 m_2}{r}, \quad T^2 = \left( \frac{4\pi^2}{G(M + m)} \right) a^3, \quad v_{\text{esc}} = \sqrt{\frac{2GM}{R}}""",
                "builder": lambda: _parse_preset(
                    r"""\vec{F}_g = -G \frac{m_1 m_2}{r^2} \hat{u}_r, \quad U(r) = -G \frac{m_1 m_2}{r}, \quad T^2 = \left( \frac{4\pi^2}{G(M + m)} \right) a^3, \quad v_{\text{esc}} = \sqrt{\frac{2GM}{R}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_energy_gravitation_problema_de_dos_cuerpos_y_fuerzas_centrales",
        "domain": "physics",
        "category": "phys_energy_gravitation",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Problema de Dos Cuerpos y Fuerzas Centrales",
        "variations": [
            {
                "name": "Masa Reducida, Potencial Efectivo, Ecuación de Binet y Órbitas",
                "description": "Reducción de dos cuerpos, potencial centrífugo efectivo y trayectoria cónica",
                "latex": r"""\mu = \frac{m_1 m_2}{m_1 + m_2}, \quad U_{\text{eff}}(r) = U(r) + \frac{L^2}{2\mu r^2}, \quad \frac{d^2 u}{d\theta^2} + u = -\frac{\mu}{L^2 u^2} f\left(\frac{1}{u}\right), \quad r(\theta) = \frac{p}{1 + e \cos(\theta)}""",
                "builder": lambda: _parse_preset(
                    r"""\mu = \frac{m_1 m_2}{m_1 + m_2}, \quad U_{\text{eff}}(r) = U(r) + \frac{L^2}{2\mu r^2}, \quad \frac{d^2 u}{d\theta^2} + u = -\frac{\mu}{L^2 u^2} f\left(\frac{1}{u}\right), \quad r(\theta) = \frac{p}{1 + e \cos(\theta)}"""
                ),
            },
        ],
    },
    {
        "id": "phys_oscillations_cinem_tica_del_m_a_s",
        "domain": "physics",
        "category": "phys_oscillations",
        "level": "NIVEL BÁSICO",
        "title": "Cinemática del M.A.S.",
        "variations": [
            {
                "name": "Posición, Velocidad y Aceleración en M.A.S.",
                "description": "Ecuaciones horarias del movimiento armónico simple y valores máximos",
                "latex": r"""x(t) = A \cos(\omega t + \phi), \quad v(t) = -\omega A \sin(\omega t + \phi) = \pm \omega \sqrt{A^2 - x^2}, \quad a(t) = -\omega^2 x(t)""",
                "builder": lambda: _parse_preset(
                    r"""x(t) = A \cos(\omega t + \phi), \quad v(t) = -\omega A \sin(\omega t + \phi) = \pm \omega \sqrt{A^2 - x^2}, \quad a(t) = -\omega^2 x(t)"""
                ),
            },
        ],
    },
    {
        "id": "phys_oscillations_par_metros_temporales_y_frecuenciales",
        "domain": "physics",
        "category": "phys_oscillations",
        "level": "NIVEL BÁSICO",
        "title": "Parámetros Temporales y Frecuenciales",
        "variations": [
            {
                "name": "Periodo, Frecuencia y Frecuencia Angular",
                "description": "Relaciones fundamentales entre periodo T, frecuencia f y frecuencia angular ω",
                "latex": r"""T = \frac{1}{f} = \frac{2\pi}{\omega}, \quad f = \frac{1}{T} = \frac{\omega}{2\pi}, \quad \omega = 2\pi f = \frac{2\pi}{T}""",
                "builder": lambda: _parse_preset(
                    r"""T = \frac{1}{f} = \frac{2\pi}{\omega}, \quad f = \frac{1}{T} = \frac{\omega}{2\pi}, \quad \omega = 2\pi f = \frac{2\pi}{T}"""
                ),
            },
        ],
    },
    {
        "id": "phys_oscillations_energ_a_del_m_a_s",
        "domain": "physics",
        "category": "phys_oscillations",
        "level": "NIVEL BÁSICO",
        "title": "Energía del M.A.S.",
        "variations": [
            {
                "name": "Energía Cinética, Potencial y Mecánica Total",
                "description": "Conservación de energía mecánica en el oscilador armónico simple E_m = 1/2 k A²",
                "latex": r"""E_k = \frac{1}{2} m v^2, \quad E_p = \frac{1}{2} k x^2, \quad E_m = E_k + E_p = \frac{1}{2} k A^2 = \frac{1}{2} m \omega^2 A^2""",
                "builder": lambda: _parse_preset(
                    r"""E_k = \frac{1}{2} m v^2, \quad E_p = \frac{1}{2} k x^2, \quad E_m = E_k + E_p = \frac{1}{2} k A^2 = \frac{1}{2} m \omega^2 A^2"""
                ),
            },
        ],
    },
    {
        "id": "phys_oscillations_sistemas_oscilatorios_simples",
        "domain": "physics",
        "category": "phys_oscillations",
        "level": "NIVEL BÁSICO",
        "title": "Sistemas Oscilatorios Simples",
        "variations": [
            {
                "name": "Masa-Resorte y Péndulo Simple",
                "description": "Frecuencias naturales y periodos para masa-resorte y péndulo simple",
                "latex": r"""\omega_0 = \sqrt{\frac{k}{m}}, \quad T = 2\pi\sqrt{\frac{m}{k}}, \quad \omega_0 = \sqrt{\frac{g}{L}}, \quad T = 2\pi\sqrt{\frac{L}{g}}""",
                "builder": lambda: _parse_preset(
                    r"""\omega_0 = \sqrt{\frac{k}{m}}, \quad T = 2\pi\sqrt{\frac{m}{k}}, \quad \omega_0 = \sqrt{\frac{g}{L}}, \quad T = 2\pi\sqrt{\frac{L}{g}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_oscillations_p_ndulos_compuestos_y_de_torsi_n",
        "domain": "physics",
        "category": "phys_oscillations",
        "level": "NIVEL INTERMEDIO",
        "title": "Péndulos Compuestos y de Torsión",
        "variations": [
            {
                "name": "Péndulo Físico y Péndulo de Torsión",
                "description": "Periodos de oscilación para cuerpos rígidos articulados y alambres de torsión",
                "latex": r"""T_{\text{fisico}} = 2\pi\sqrt{\frac{I}{m g d}}, \quad T_{\text{torsion}} = 2\pi\sqrt{\frac{I}{\kappa}}""",
                "builder": lambda: _parse_preset(
                    r"""T_{\text{fisico}} = 2\pi\sqrt{\frac{I}{m g d}}, \quad T_{\text{torsion}} = 2\pi\sqrt{\frac{I}{\kappa}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_oscillations_oscilaciones_amortiguadas",
        "domain": "physics",
        "category": "phys_oscillations",
        "level": "NIVEL INTERMEDIO",
        "title": "Oscilaciones Amortiguadas",
        "variations": [
            {
                "name": "Oscilador Amortiguado, Decremento y Factor Q",
                "description": "Ecuación diferencial, régimen subamortiguado ω_d, decremento logarítmico δ y factor Q",
                "latex": r"""\ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = 0, \quad x(t) = A_0 e^{-\gamma t} \cos(\omega_d t + \phi), \quad \omega_d = \sqrt{\omega_0^2 - \gamma^2}, \quad Q = \frac{\omega_0}{2\gamma}""",
                "builder": lambda: _parse_preset(
                    r"""\ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = 0, \quad x(t) = A_0 e^{-\gamma t} \cos(\omega_d t + \phi), \quad \omega_d = \sqrt{\omega_0^2 - \gamma^2}, \quad Q = \frac{\omega_0}{2\gamma}"""
                ),
            },
        ],
    },
    {
        "id": "phys_oscillations_oscilaciones_forzadas_y_resonancia",
        "domain": "physics",
        "category": "phys_oscillations",
        "level": "NIVEL INTERMEDIO",
        "title": "Oscilaciones Forzadas y Resonancia",
        "variations": [
            {
                "name": "Oscilaciones Forzadas, Resonancia y Potencia Absorbida",
                "description": "Amplitud estacionaria A(ω), frecuencia de resonancia ω_res y potencia media absorbida",
                "latex": r"""A(\omega) = \frac{F_0 / m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2}}, \quad \omega_{\text{res}} = \sqrt{\omega_0^2 - 2\gamma^2}, \quad \langle P(\omega) \rangle = \frac{F_0^2 \gamma \omega^2}{m [(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2]}""",
                "builder": lambda: _parse_preset(
                    r"""A(\omega) = \frac{F_0 / m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2}}, \quad \omega_{\text{res}} = \sqrt{\omega_0^2 - 2\gamma^2}, \quad \langle P(\omega) \rangle = \frac{F_0^2 \gamma \omega^2}{m [(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2]}"""
                ),
            },
        ],
    },
    {
        "id": "phys_oscillations_osciladores_acoplados_y_modos_normales",
        "domain": "physics",
        "category": "phys_oscillations",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Osciladores Acoplados y Modos Normales",
        "variations": [
            {
                "name": "Osciladores Acoplados y Modos Normales",
                "description": "Ecuación secular matricial det(K - ω²M) = 0 y coordenadas normales",
                "latex": r"""\mathbf{M}\ddot{\mathbf{x}} + \mathbf{K}\mathbf{x} = \mathbf{0}, \quad \det(\mathbf{K} - \omega^2 \mathbf{M}) = 0, \quad \ddot{\eta}_k + \omega_k^2 \eta_k = 0""",
                "builder": lambda: _parse_preset(
                    r"""\mathbf{M}\ddot{\mathbf{x}} + \mathbf{K}\mathbf{x} = \mathbf{0}, \quad \det(\mathbf{K} - \omega^2 \mathbf{M}) = 0, \quad \ddot{\eta}_k + \omega_k^2 \eta_k = 0"""
                ),
            },
        ],
    },
    {
        "id": "phys_oscillations_oscilaciones_no_lineales_y_autoexcitadas",
        "domain": "physics",
        "category": "phys_oscillations",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Oscilaciones No Lineales y Autoexcitadas",
        "variations": [
            {
                "name": "Péndulo No Lineal (Borda / Integrales Elípticas) y Van der Pol",
                "description": "Periodo exacto mediante integral elíptica K(m), fórmula de Borda y oscilador de Van der Pol",
                "latex": r"""T = 4\sqrt{\frac{L}{g}} K\left(\sin^2\left(\frac{\theta_0}{2}\right)\right) \approx 2\pi\sqrt{\frac{L}{g}}\left(1 + \frac{1}{16}\theta_0^2\right), \quad \ddot{x} - \mu(1 - x^2)\dot{x} + \omega_0^2 x = 0""",
                "builder": lambda: _parse_preset(
                    r"""T = 4\sqrt{\frac{L}{g}} K\left(\sin^2\left(\frac{\theta_0}{2}\right)\right) \approx 2\pi\sqrt{\frac{L}{g}}\left(1 + \frac{1}{16}\theta_0^2\right), \quad \ddot{x} - \mu(1 - x^2)\dot{x} + \omega_0^2 x = 0"""
                ),
            },
        ],
    },
    {
        "id": "phys_waves_acoustics_cinem_tica_de_ondas_arm_nicas",
        "domain": "physics",
        "category": "phys_waves_acoustics",
        "level": "NIVEL BÁSICO",
        "title": "Cinemática de Ondas Armónicas",
        "variations": [
            {
                "name": "Función de Onda Progresiva y Cinemática Transversal",
                "description": "Función de onda armónica y relaciones k = 2π/λ, v = λf, velocidad y aceleración transversal",
                "latex": r"""y(x, t) = A \sin(kx \mp \omega t + \phi), \quad k = \frac{2\pi}{\lambda}, \quad v = \lambda f = \frac{\omega}{k}, \quad a_y(x, t) = -\omega^2 y(x, t)""",
                "builder": lambda: _parse_preset(
                    r"""y(x, t) = A \sin(kx \mp \omega t + \phi), \quad k = \frac{2\pi}{\lambda}, \quad v = \lambda f = \frac{\omega}{k}, \quad a_y(x, t) = -\omega^2 y(x, t)"""
                ),
            },
        ],
    },
    {
        "id": "phys_waves_acoustics_superposici_n_e_interferencia",
        "domain": "physics",
        "category": "phys_waves_acoustics",
        "level": "NIVEL BÁSICO",
        "title": "Superposición e Interferencia",
        "variations": [
            {
                "name": "Interferencia Constructiva/Destructiva y Batidos",
                "description": "Amplitud resultante por desfase 2A cos(Δφ/2) y frecuencia de batido f_batido = |f1 - f2|",
                "latex": r"""y_R(x, t) = \left[ 2A \cos\left(\frac{\Delta\phi}{2}\right) \right] \sin\left(kx - \omega t + \frac{\Delta\phi}{2}\right), \quad f_{\text{batido}} = |f_1 - f_2|""",
                "builder": lambda: _parse_preset(
                    r"""y_R(x, t) = \left[ 2A \cos\left(\frac{\Delta\phi}{2}\right) \right] \sin\left(kx - \omega t + \frac{\Delta\phi}{2}\right), \quad f_{\text{batido}} = |f_1 - f_2|"""
                ),
            },
        ],
    },
    {
        "id": "phys_waves_acoustics_escala_decib_lica_y_nivel_de_sonido",
        "domain": "physics",
        "category": "phys_waves_acoustics",
        "level": "NIVEL BÁSICO",
        "title": "Escala Decibélica y Nivel de Sonido",
        "variations": [
            {
                "name": "Nivel de Intensidad Sonora (Decibeles)",
                "description": "Escala logarítmica de intensidad sonora β en dB con umbral de audición I_0 = 10⁻¹² W/m²",
                "latex": r"""\beta = 10 \log_{10}\left(\frac{I}{I_0}\right), \quad L_p = 20 \log_{10}\left(\frac{p_{\text{rms}}}{p_0}\right)""",
                "builder": lambda: _parse_preset(
                    r"""\beta = 10 \log_{10}\left(\frac{I}{I_0}\right), \quad L_p = 20 \log_{10}\left(\frac{p_{\text{rms}}}{p_0}\right)"""
                ),
            },
        ],
    },
    {
        "id": "phys_waves_acoustics_ecuaci_n_diferencial_de_onda_1d",
        "domain": "physics",
        "category": "phys_waves_acoustics",
        "level": "NIVEL INTERMEDIO",
        "title": "Ecuación Diferencial de Onda 1D",
        "variations": [
            {
                "name": "Ecuación de Onda 1D y Solución de d'Alembert",
                "description": "Forma canónica diferencial de d'Alembert y superposición de ondas viajeras",
                "latex": r"""\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2} \implies y(x, t) = f(x - vt) + g(x + vt)""",
                "builder": lambda: _parse_preset(
                    r"""\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2} \implies y(x, t) = f(x - vt) + g(x + vt)"""
                ),
            },
        ],
    },
    {
        "id": "phys_waves_acoustics_velocidad_de_propagaci_n_en_medios_el_sticos",
        "domain": "physics",
        "category": "phys_waves_acoustics",
        "level": "NIVEL INTERMEDIO",
        "title": "Velocidad de Propagación en Medios Elásticos",
        "variations": [
            {
                "name": "Velocidad de Onda en Cuerdas, Sólidos, Fluidos y Gases Ideales",
                "description": "Velocidad en cuerda tensa √(T/μ), barra √(Y/ρ), fluido √(B/ρ) y gas ideal √(γRT/M)",
                "latex": r"""v_{\text{cuerda}} = \sqrt{\frac{T}{\mu}}, \quad v_{\text{solido}} = \sqrt{\frac{Y}{\rho}}, \quad v_{\text{fluido}} = \sqrt{\frac{B}{\rho}}, \quad v_{\text{gas}} = \sqrt{\frac{\gamma R T}{M}} = \sqrt{\frac{\gamma P}{\rho}}""",
                "builder": lambda: _parse_preset(
                    r"""v_{\text{cuerda}} = \sqrt{\frac{T}{\mu}}, \quad v_{\text{solido}} = \sqrt{\frac{Y}{\rho}}, \quad v_{\text{fluido}} = \sqrt{\frac{B}{\rho}}, \quad v_{\text{gas}} = \sqrt{\frac{\gamma R T}{M}} = \sqrt{\frac{\gamma P}{\rho}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_waves_acoustics_transporte_de_energ_a_e_intensidad",
        "domain": "physics",
        "category": "phys_waves_acoustics",
        "level": "NIVEL INTERMEDIO",
        "title": "Transporte de Energía e Intensidad",
        "variations": [
            {
                "name": "Potencia Promedio e Intensidad de Onda",
                "description": "Potencia transmitida en cuerda <P> = 1/2 μvω²A² e intensidad de onda I con ley del inverso del cuadrado",
                "latex": r"""\langle P \rangle = \frac{1}{2} \mu v \omega^2 A^2 = \frac{1}{2} \sqrt{\mu T} \, \omega^2 A^2, \quad I = \frac{\langle P \rangle}{\text{Area}} = \frac{1}{2} \rho v \omega^2 A^2, \quad \frac{I_1}{I_2} = \frac{r_2^2}{r_1^2}""",
                "builder": lambda: _parse_preset(
                    r"""\langle P \rangle = \frac{1}{2} \mu v \omega^2 A^2 = \frac{1}{2} \sqrt{\mu T} \, \omega^2 A^2, \quad I = \frac{\langle P \rangle}{\text{Area}} = \frac{1}{2} \rho v \omega^2 A^2, \quad \frac{I_1}{I_2} = \frac{r_2^2}{r_1^2}"""
                ),
            },
        ],
    },
    {
        "id": "phys_waves_acoustics_ondas_estacionarias_y_modos_normales",
        "domain": "physics",
        "category": "phys_waves_acoustics",
        "level": "NIVEL INTERMEDIO",
        "title": "Ondas Estacionarias y Modos Normales",
        "variations": [
            {
                "name": "Ondas Estacionarias y Frecuencias Resonantes",
                "description": "Ecuación estacionaria 2A sin(kx)cos(ωt) y frecuencias en cuerdas y tubos sonoros abiertos/cerrados",
                "latex": r"""y(x, t) = [2A \sin(kx)] \cos(\omega t), \quad f_n = n \frac{v}{2L}, \quad f_m = (2m - 1) \frac{v}{4L}""",
                "builder": lambda: _parse_preset(
                    r"""y(x, t) = [2A \sin(kx)] \cos(\omega t), \quad f_n = n \frac{v}{2L}, \quad f_m = (2m - 1) \frac{v}{4L}"""
                ),
            },
        ],
    },
    {
        "id": "phys_waves_acoustics_efecto_doppler_y_ondas_de_choque",
        "domain": "physics",
        "category": "phys_waves_acoustics",
        "level": "NIVEL INTERMEDIO",
        "title": "Efecto Doppler y Ondas de Choque",
        "variations": [
            {
                "name": "Efecto Doppler Clásico y Cono de Mach",
                "description": "Desplazamiento Doppler con observador/fuente móviles y ángulo de Mach sin(θ_M) = 1/M",
                "latex": r"""f_o = f_s \left( \frac{v \pm v_o}{v \mp v_s} \right), \quad \sin(\theta_M) = \frac{v}{v_s} = \frac{1}{M}""",
                "builder": lambda: _parse_preset(
                    r"""f_o = f_s \left( \frac{v \pm v_o}{v \mp v_s} \right), \quad \sin(\theta_M) = \frac{v}{v_s} = \frac{1}{M}"""
                ),
            },
        ],
    },
    {
        "id": "phys_waves_acoustics_dispersi_n_e_impedancia_mec_nica",
        "domain": "physics",
        "category": "phys_waves_acoustics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Dispersión e Impedancia Mecánica",
        "variations": [
            {
                "name": "Velocidad de Grupo, Impedancia Z y Coeficientes de Frontera",
                "description": "Velocidad de grupo vg = dω/dk, impedancia Z = ρv y coeficientes de reflexión/transmisión",
                "latex": r"""v_g = \frac{d\omega}{dk}, \quad Z = \rho v, \quad r = \frac{Z_1 - Z_2}{Z_1 + Z_2}, \quad t = \frac{2Z_1}{Z_1 + Z_2}, \quad R + T_w = 1""",
                "builder": lambda: _parse_preset(
                    r"""v_g = \frac{d\omega}{dk}, \quad Z = \rho v, \quad r = \frac{Z_1 - Z_2}{Z_1 + Z_2}, \quad t = \frac{2Z_1}{Z_1 + Z_2}, \quad R + T_w = 1"""
                ),
            },
        ],
    },
    {
        "id": "phys_waves_acoustics_ondas_el_sticas_en_medios_continuos_3d",
        "domain": "physics",
        "category": "phys_waves_acoustics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Ondas Elásticas en Medios Continuos 3D",
        "variations": [
            {
                "name": "Ondas Sísmicas y Elásticas 3D (Ondas P y Ondas S)",
                "description": "Velocidades de ondas compresionales longitudinales P y transversales de cizalladura S",
                "latex": r"""v_P = \sqrt{\frac{\lambda + 2\mu}{\rho}} = \sqrt{\frac{K + \frac{4}{3}G}{\rho}}, \quad v_S = \sqrt{\frac{\mu}{\rho}} = \sqrt{\frac{G}{\rho}}""",
                "builder": lambda: _parse_preset(
                    r"""v_P = \sqrt{\frac{\lambda + 2\mu}{\rho}} = \sqrt{\frac{K + \frac{4}{3}G}{\rho}}, \quad v_S = \sqrt{\frac{\mu}{\rho}} = \sqrt{\frac{G}{\rho}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_waves_acoustics_ac_stica_f_sica_y_ondas_3d",
        "domain": "physics",
        "category": "phys_waves_acoustics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Acústica Física y Ondas 3D",
        "variations": [
            {
                "name": "Ondas de Presión Acústica, Onda 3D y Doppler Vectorial",
                "description": "Presión acústica Δp = Zωs, ecuación diferencial 3D y efecto Doppler vectorial",
                "latex": r"""\Delta p_{\text{max}} = Z \omega s_{\text{max}}, \quad \nabla^2 p - \frac{1}{c^2}\frac{\partial^2 p}{\partial t^2} = 0, \quad f_o = f_s \left( \frac{c - \mathbf{v}_o \cdot \hat{\mathbf{n}}}{c - \mathbf{v}_s \cdot \hat{\mathbf{n}}} \right)""",
                "builder": lambda: _parse_preset(
                    r"""\Delta p_{\text{max}} = Z \omega s_{\text{max}}, \quad \nabla^2 p - \frac{1}{c^2}\frac{\partial^2 p}{\partial t^2} = 0, \quad f_o = f_s \left( \frac{c - \mathbf{v}_o \cdot \hat{\mathbf{n}}}{c - \mathbf{v}_s \cdot \hat{\mathbf{n}}} \right)"""
                ),
            },
        ],
    },
    {
        "id": "phys_fluids_est_tica_de_fluidos",
        "domain": "physics",
        "category": "phys_fluids",
        "level": "NIVEL BÁSICO",
        "title": "Estática de Fluidos",
        "variations": [
            {
                "name": "Presión Hidrostática, Principio de Pascal y Empuje de Arquímedes",
                "description": "Presión a profundidad h, prensa hidráulica y fuerza de empuje boyante",
                "latex": r"""P(h) = P_0 + \rho g h, \quad \frac{F_1}{A_1} = \frac{F_2}{A_2}, \quad E = \rho_{\text{fluido}} g V_{\text{sumergido}}""",
                "builder": lambda: _parse_preset(
                    r"""P(h) = P_0 + \rho g h, \quad \frac{F_1}{A_1} = \frac{F_2}{A_2}, \quad E = \rho_{\text{fluido}} g V_{\text{sumergido}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_fluids_din_mica_de_fluidos_ideales",
        "domain": "physics",
        "category": "phys_fluids",
        "level": "NIVEL INTERMEDIO",
        "title": "Dinámica de Fluidos Ideales",
        "variations": [
            {
                "name": "Ecuación de Continuidad, Bernoulli y Teorema de Torricelli",
                "description": "Conservación de masa y energía para fluidos ideales incompresibles",
                "latex": r"""A_1 v_1 = A_2 v_2 = Q, \quad P_1 + \frac{1}{2}\rho v_1^2 + \rho g z_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g z_2, \quad v = \sqrt{2gh}""",
                "builder": lambda: _parse_preset(
                    r"""A_1 v_1 = A_2 v_2 = Q, \quad P_1 + \frac{1}{2}\rho v_1^2 + \rho g z_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g z_2, \quad v = \sqrt{2gh}"""
                ),
            },
        ],
    },
    {
        "id": "phys_fluids_mec_nica_de_fluidos_y_medios_continuos",
        "domain": "physics",
        "category": "phys_fluids",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Mecánica de Fluidos y Medios Continuos",
        "variations": [
            {
                "name": "Continuidad Diferencial, Navier-Stokes y Tensor de Cauchy",
                "description": "Ecuaciones fundamentales de la dinámica de medios continuos y fluidos viscosos",
                "latex": r"""\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0, \quad \rho \left( \frac{\partial \vec{v}}{\partial t} + (\vec{v} \cdot \nabla)\vec{v} \right) = -\nabla P + \mu \nabla^2 \vec{v} + \rho \vec{g}, \quad \nabla \cdot \boldsymbol{\sigma} + \vec{f}_{\text{ext}} = \rho \frac{d\vec{v}}{dt}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0, \quad \rho \left( \frac{\partial \vec{v}}{\partial t} + (\vec{v} \cdot \nabla)\vec{v} \right) = -\nabla P + \mu \nabla^2 \vec{v} + \rho \vec{g}, \quad \nabla \cdot \boldsymbol{\sigma} + \vec{f}_{\text{ext}} = \rho \frac{d\vec{v}}{dt}"""
                ),
            },
        ],
    },
    {
        "id": "phys_analytical_relativity_mec_nica_lagrangiana",
        "domain": "physics",
        "category": "phys_analytical_relativity",
        "level": "NIVEL INTERMEDIO",
        "title": "Mecánica Lagrangiana",
        "variations": [
            {
                "name": "Lagrangiano, Principio de Hamilton, Euler-Lagrange y Teorema de Noether",
                "description": "Ecuaciones de movimiento variacionales y constantes de movimiento por simetrías",
                "latex": r"""L = T - V, \quad \delta S = \delta \int L \, dt = 0, \quad \frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}_j} \right) - \frac{\partial L}{\partial q_j} = 0, \quad p_j = \frac{\partial L}{\partial \dot{q}_j}""",
                "builder": lambda: _parse_preset(
                    r"""L = T - V, \quad \delta S = \delta \int L \, dt = 0, \quad \frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}_j} \right) - \frac{\partial L}{\partial q_j} = 0, \quad p_j = \frac{\partial L}{\partial \dot{q}_j}"""
                ),
            },
        ],
    },
    {
        "id": "phys_analytical_relativity_mec_nica_hamiltoniana",
        "domain": "physics",
        "category": "phys_analytical_relativity",
        "level": "NIVEL INTERMEDIO",
        "title": "Mecánica Hamiltoniana",
        "variations": [
            {
                "name": "Hamiltoniano y Ecuaciones Canónicas de Hamilton",
                "description": "Transformada de Legendre del espacio de fases y ecuaciones canónicas de primer orden",
                "latex": r"""H(q, p, t) = \sum_{j=1}^n p_j \dot{q}_j - L, \quad \dot{q}_j = \frac{\partial H}{\partial p_j}, \quad \dot{p}_j = -\frac{\partial H}{\partial q_j}, \quad \frac{dH}{dt} = -\frac{\partial L}{\partial t}""",
                "builder": lambda: _parse_preset(
                    r"""H(q, p, t) = \sum_{j=1}^n p_j \dot{q}_j - L, \quad \dot{q}_j = \frac{\partial H}{\partial p_j}, \quad \dot{p}_j = -\frac{\partial H}{\partial q_j}, \quad \frac{dH}{dt} = -\frac{\partial L}{\partial t}"""
                ),
            },
        ],
    },
    {
        "id": "phys_analytical_relativity_formulaciones_can_nicas_avanzadas",
        "domain": "physics",
        "category": "phys_analytical_relativity",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Formulaciones Canónicas Avanzadas",
        "variations": [
            {
                "name": "Corchetes de Poisson, Teorema de Liouville y Ecuación de Hamilton-Jacobi",
                "description": "Álgebra de Poisson, conservación de volumen fásico y ecuación diferencial de la acción S",
                "latex": r"""\{f, g\} = \sum_{j=1}^n \left( \frac{\partial f}{\partial q_j}\frac{\partial g}{\partial p_j} - \frac{\partial f}{\partial p_j}\frac{\partial g}{\partial q_j} \right), \quad \frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}, \quad H\left(q, \frac{\partial S}{\partial q}, t\right) + \frac{\partial S}{\partial t} = 0""",
                "builder": lambda: _parse_preset(
                    r"""\{f, g\} = \sum_{j=1}^n \left( \frac{\partial f}{\partial q_j}\frac{\partial g}{\partial p_j} - \frac{\partial f}{\partial p_j}\frac{\partial g}{\partial q_j} \right), \quad \frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}, \quad H\left(q, \frac{\partial S}{\partial q}, t\right) + \frac{\partial S}{\partial t} = 0"""
                ),
            },
        ],
    },
    {
        "id": "phys_analytical_relativity_mec_nica_relativista",
        "domain": "physics",
        "category": "phys_analytical_relativity",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Mecánica Relativista",
        "variations": [
            {
                "name": "Dinámica Relativista, Relación Energía-Momento y Cuadrivectores",
                "description": "Factor de Lorentz γ, fuerza relativista, relación E² = (pc)² + (m₀c²)² e invariante cuadrimomento",
                "latex": r"""\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}, \quad \vec{p} = \gamma m_0 \vec{v}, \quad E = \gamma m_0 c^2, \quad E^2 = (p c)^2 + (m_0 c^2)^2, \quad P^\mu P_\mu = m_0^2 c^2""",
                "builder": lambda: _parse_preset(
                    r"""\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}, \quad \vec{p} = \gamma m_0 \vec{v}, \quad E = \gamma m_0 c^2, \quad E^2 = (p c)^2 + (m_0 c^2)^2, \quad P^\mu P_\mu = m_0^2 c^2"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_escalas_termom_tricas_y_dilataci_n_t_rmica",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL BÁSICO",
        "title": "Escalas Termométricas y Dilatación Térmica",
        "variations": [
            {
                "name": "Escalas de Temperatura y Dilatación Térmica",
                "description": "Conversión Celsius-Kelvin-Fahrenheit y dilatación lineal, superficial y volumétrica",
                "latex": r"""T(\text{K}) = T(^\circ\text{C}) + 273.15, \quad T(^\circ\text{F}) = \frac{9}{5}T(^\circ\text{C}) + 32, \quad \Delta L = \alpha L_0 \Delta T, \quad \Delta V = \beta V_0 \Delta T""",
                "builder": lambda: _parse_preset(
                    r"""T(\text{K}) = T(^\circ\text{C}) + 273.15, \quad T(^\circ\text{F}) = \frac{9}{5}T(^\circ\text{C}) + 32, \quad \Delta L = \alpha L_0 \Delta T, \quad \Delta V = \beta V_0 \Delta T"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_calorimetr_a_y_capacidad_calor_fica",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL BÁSICO",
        "title": "Calorimetría y Capacidad Calorífica",
        "variations": [
            {
                "name": "Calor Sensible, Calor Latente y Equilibrio Térmico",
                "description": "Calorimetría sensible Q = mcΔT, calor de cambio de fase Q = mL y balance de calor",
                "latex": r"""Q = m c \Delta T = C \Delta T, \quad Q_{\text{fase}} = m L, \quad \sum Q_{\text{ganado}} + \sum Q_{\text{perdido}} = 0""",
                "builder": lambda: _parse_preset(
                    r"""Q = m c \Delta T = C \Delta T, \quad Q_{\text{fase}} = m L, \quad \sum Q_{\text{ganado}} + \sum Q_{\text{perdido}} = 0"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_gas_ideal_y_leyes_emp_ricas",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL BÁSICO",
        "title": "Gas Ideal y Leyes Empíricas",
        "variations": [
            {
                "name": "Ecuación de Gas Ideal y Leyes Empíricas",
                "description": "Ecuación PV = nRT = N k_B T y leyes de Boyle, Charles, Gay-Lussac",
                "latex": r"""P V = n R T = N k_B T, \quad P_1 V_1 = P_2 V_2, \quad \frac{V_1}{T_1} = \frac{V_2}{T_2}, \quad \frac{P_1 V_1}{T_1} = \frac{P_2 V_2}{T_2}""",
                "builder": lambda: _parse_preset(
                    r"""P V = n R T = N k_B T, \quad P_1 V_1 = P_2 V_2, \quad \frac{V_1}{T_1} = \frac{V_2}{T_2}, \quad \frac{P_1 V_1}{T_1} = \frac{P_2 V_2}{T_2}"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_primera_ley_de_la_termodin_mica",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL BÁSICO",
        "title": "Primera Ley de la Termodinámica",
        "variations": [
            {
                "name": "Primera Ley y Trabajo Cuasiestático de Expansión",
                "description": "Balance de energía interna ΔU = Q - W y trabajo de frontera móvil W = ∫ P dV",
                "latex": r"""\Delta U = Q - W, \quad dU = \delta Q - P dV, \quad W = \int_{V_i}^{V_f} P \, dV""",
                "builder": lambda: _parse_preset(
                    r"""\Delta U = Q - W, \quad dU = \delta Q - P dV, \quad W = \int_{V_i}^{V_f} P \, dV"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_procesos_termodin_micos_en_gases_ideales",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL BÁSICO",
        "title": "Procesos Termodinámicos en Gases Ideales",
        "variations": [
            {
                "name": "Procesos Isobárico, Isotérmico, Adiabático y Relación de Mayer",
                "description": "Trabajo y calor en procesos cuasiestáticos, ley adiabática PV^γ = cte y relación C_p - C_v = R",
                "latex": r"""W_{\text{isot}} = n R T \ln\left(\frac{V_f}{V_i}\right), \quad P V^\gamma = \text{cte}, \quad T V^{\gamma - 1} = \text{cte}, \quad C_p - C_v = R""",
                "builder": lambda: _parse_preset(
                    r"""W_{\text{isot}} = n R T \ln\left(\frac{V_f}{V_i}\right), \quad P V^\gamma = \text{cte}, \quad T V^{\gamma - 1} = \text{cte}, \quad C_p - C_v = R"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_mezclas_de_gases_y_coeficientes_termoel_sticos",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL INTERMEDIO",
        "title": "Mezclas de Gases y Coeficientes Termoelásticos",
        "variations": [
            {
                "name": "Leyes de Dalton/Amagat y Coeficientes Termoelásticos (α, κ_T, β_P)",
                "description": "Presiones parciales, coeficiente de dilatación isobárica α y compresibilidad isotérmica κ_T",
                "latex": r"""P_{\text{total}} = \sum P_i, \quad \alpha = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_P, \quad \kappa_T = -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_T, \quad \beta_P = \frac{\alpha}{P \kappa_T}""",
                "builder": lambda: _parse_preset(
                    r"""P_{\text{total}} = \sum P_i, \quad \alpha = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_P, \quad \kappa_T = -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_T, \quad \beta_P = \frac{\alpha}{P \kappa_T}"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_gases_reales_y_ecuaciones_de_estado",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL INTERMEDIO",
        "title": "Gases Reales y Ecuaciones de Estado",
        "variations": [
            {
                "name": "Ecuación de Van der Waals, Constantes Críticas y Expansión Virial",
                "description": "Ecuación de Van der Waals con corrección por volumen propio y fuerzas intermoleculares",
                "latex": r"""\left(P + \frac{a n^2}{V^2}\right)(V - n b) = n R T, \quad T_c = \frac{8a}{27Rb}, \quad P_c = \frac{a}{27b^2}, \quad Z = \frac{PV_m}{RT} = 1 + \frac{B(T)}{V_m}""",
                "builder": lambda: _parse_preset(
                    r"""\left(P + \frac{a n^2}{V^2}\right)(V - n b) = n R T, \quad T_c = \frac{8a}{27Rb}, \quad P_c = \frac{a}{27b^2}, \quad Z = \frac{PV_m}{RT} = 1 + \frac{B(T)}{V_m}"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_procesos_politr_picos",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL INTERMEDIO",
        "title": "Procesos Politrópicos",
        "variations": [
            {
                "name": "Procesos Politrópicos (PV^n = cte)",
                "description": "Trabajo de expansión politrópica y capacidad calorífica dependiente del exponente n",
                "latex": r"""P V^n = \text{cte} \implies W = \frac{P_f V_f - P_i V_i}{1 - n} = \frac{n R (T_f - T_i)}{1 - n}, \quad C_n = C_v \left(\frac{n - \gamma}{n - 1}\right)""",
                "builder": lambda: _parse_preset(
                    r"""P V^n = \text{cte} \implies W = \frac{P_f V_f - P_i V_i}{1 - n} = \frac{n R (T_f - T_i)}{1 - n}, \quad C_n = C_v \left(\frac{n - \gamma}{n - 1}\right)"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_segunda_ley_y_entrop_a",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL INTERMEDIO",
        "title": "Segunda Ley y Entropía",
        "variations": [
            {
                "name": "Definición de Entropía, Desigualdad de Clausius y Entropía en Gases",
                "description": "Definición dS = δQ_rev/T, principio de incremento de entropía y cálculo en gases y mezclas",
                "latex": r"""dS = \frac{\delta Q_{\text{rev}}}{T}, \quad \oint \frac{\delta Q}{T} \le 0, \quad \Delta S_{\text{univ}} \ge 0, \quad \Delta S = n C_v \ln\left(\frac{T_f}{T_i}\right) + n R \ln\left(\frac{V_f}{V_i}\right)""",
                "builder": lambda: _parse_preset(
                    r"""dS = \frac{\delta Q_{\text{rev}}}{T}, \quad \oint \frac{\delta Q}{T} \le 0, \quad \Delta S_{\text{univ}} \ge 0, \quad \Delta S = n C_v \ln\left(\frac{T_f}{T_i}\right) + n R \ln\left(\frac{V_f}{V_i}\right)"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_m_quinas_t_rmicas_y_ciclos_de_potencia",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL INTERMEDIO",
        "title": "Máquinas Térmicas y Ciclos de Potencia",
        "variations": [
            {
                "name": "Eficiencia de Carnot, COP y Ciclos Otto, Diesel y Brayton",
                "description": "Rendimiento térmico de máquinas, coeficientes de refrigeración y ciclos termodinámicos de potencia",
                "latex": r"""\eta = 1 - \frac{|Q_C|}{Q_H}, \quad \eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}, \quad \text{COP}_R = \frac{T_C}{T_H - T_C}, \quad \eta_{\text{Otto}} = 1 - \frac{1}{r^{\gamma - 1}}, \quad \eta_{\text{Brayton}} = 1 - \frac{1}{r_p^{\frac{\gamma - 1}{\gamma}}}""",
                "builder": lambda: _parse_preset(
                    r"""\eta = 1 - \frac{|Q_C|}{Q_H}, \quad \eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}, \quad \text{COP}_R = \frac{T_C}{T_H - T_C}, \quad \eta_{\text{Otto}} = 1 - \frac{1}{r^{\gamma - 1}}, \quad \eta_{\text{Brayton}} = 1 - \frac{1}{r_p^{\frac{\gamma - 1}{\gamma}}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_potenciales_termodin_micos_y_relaciones_de_maxwell",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL INTERMEDIO",
        "title": "Potenciales Termodinámicos y Relaciones de Maxwell",
        "variations": [
            {
                "name": "Potenciales U, H, F, G y Relaciones de Maxwell",
                "description": "Energía interna, entalpía, energías libres de Helmholtz y Gibbs con las 4 relaciones de Maxwell",
                "latex": r"""dU = T dS - P dV, \quad dH = T dS + V dP, \quad dF = -S dT - P dV, \quad dG = -S dT + V dP, \quad \left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V""",
                "builder": lambda: _parse_preset(
                    r"""dU = T dS - P dV, \quad dH = T dS + V dP, \quad dF = -S dT - P dV, \quad dG = -S dT + V dP, \quad \left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V"""
                ),
            },
            {
                "name": "Ecuaciones T dS y Relación General C_p - C_v",
                "description": "Ecuaciones fundamentales T dS y relación universal C_p - C_v = T V α² / κ_T",
                "latex": r"""T dS = C_v dT + \frac{T \alpha}{\kappa_T} dV, \quad T dS = C_p dT - T V \alpha dP, \quad C_p - C_v = \frac{T V \alpha^2}{\kappa_T}, \quad \frac{C_p}{C_v} = \frac{\kappa_T}{\kappa_S} = \gamma""",
                "builder": lambda: _parse_preset(
                    r"""T dS = C_v dT + \frac{T \alpha}{\kappa_T} dV, \quad T dS = C_p dT - T V \alpha dP, \quad C_p - C_v = \frac{T V \alpha^2}{\kappa_T}, \quad \frac{C_p}{C_v} = \frac{\kappa_T}{\kappa_S} = \gamma"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_teor_a_cin_tica_molecular",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Teoría Cinética Molecular",
        "variations": [
            {
                "name": "Presión Cinética, Velocidades Moleculares y Distribución de Maxwell",
                "description": "Presión cinética P = 1/3 ρ v_rms², velocidades cuadrática/media/más probable y distribución de Maxwell",
                "latex": r"""P = \frac{1}{3}\rho v_{\text{rms}}^2, \quad v_{\text{rms}} = \sqrt{\frac{3 k_B T}{m}}, \quad v_{\text{prom}} = \sqrt{\frac{8 k_B T}{\pi m}}, \quad f(v) = 4\pi \left(\frac{m}{2\pi k_B T}\right)^{\frac{3}{2}} v^2 e^{-\frac{m v^2}{2 k_B T}}""",
                "builder": lambda: _parse_preset(
                    r"""P = \frac{1}{3}\rho v_{\text{rms}}^2, \quad v_{\text{rms}} = \sqrt{\frac{3 k_B T}{m}}, \quad v_{\text{prom}} = \sqrt{\frac{8 k_B T}{\pi m}}, \quad f(v) = 4\pi \left(\frac{m}{2\pi k_B T}\right)^{\frac{3}{2}} v^2 e^{-\frac{m v^2}{2 k_B T}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_sistemas_abiertos_y_an_lisis_exerg_tico",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Sistemas Abiertos y Análisis Exergético",
        "variations": [
            {
                "name": "Balances en Sistemas Abiertos, Exergía y Teorema de Gouy-Stodola",
                "description": "Primera y segunda ley en volumen de control, exergía de flujo ψ y destrucción de exergía X_dest = T_0 S_gen",
                "latex": r"""q - w_{\text{eje}} = (h_e - h_i) + \frac{v_e^2 - v_i^2}{2} + g(z_e - z_i), \quad \psi = (h - h_0) - T_0(s - s_0) + \frac{v^2}{2} + gz, \quad \dot{X}_{\text{destruida}} = T_0 \dot{S}_{\text{gen}}""",
                "builder": lambda: _parse_preset(
                    r"""q - w_{\text{eje}} = (h_e - h_i) + \frac{v_e^2 - v_i^2}{2} + g(z_e - z_i), \quad \psi = (h - h_0) - T_0(s - s_0) + \frac{v^2}{2} + gz, \quad \dot{X}_{\text{destruida}} = T_0 \dot{S}_{\text{gen}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_efecto_joule_thomson_y_ecuaci_n_de_gibbs_duhem",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Efecto Joule-Thomson y Ecuación de Gibbs-Duhem",
        "variations": [
            {
                "name": "Coeficiente de Joule-Thomson y Ecuación de Gibbs-Duhem",
                "description": "Coeficiente de expansión isoentálpica μ_JT = (V/C_p)(Tα - 1) y ecuación de Gibbs-Duhem",
                "latex": r"""\mu_{\text{JT}} = \left(\frac{\partial T}{\partial P}\right)_H = \frac{V}{C_p}(T\alpha - 1), \quad S dT - V dP + \sum N_i d\mu_i = 0 \implies \mu_i = \left(\frac{\partial G}{\partial n_i}\right)_{T, P, n_{j \neq i}}""",
                "builder": lambda: _parse_preset(
                    r"""\mu_{\text{JT}} = \left(\frac{\partial T}{\partial P}\right)_H = \frac{V}{C_p}(T\alpha - 1), \quad S dT - V dP + \sum N_i d\mu_i = 0 \implies \mu_i = \left(\frac{\partial G}{\partial n_i}\right)_{T, P, n_{j \neq i}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_transiciones_de_fase_y_equilibrio_qu_mico",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Transiciones de Fase y Equilibrio Químico",
        "variations": [
            {
                "name": "Ecuaciones de Clapeyron, Clausius-Clapeyron, Regla de Fases y Van 't Hoff",
                "description": "Termodinámica de cambios de fase dP/dT = Δh/(TΔv), regla de fases de Gibbs F = C - P + 2 e isoterma de Van 't Hoff",
                "latex": r"""\frac{dP}{dT} = \frac{\Delta h}{T \Delta v}, \quad \ln\left(\frac{P_2}{P_1}\right) = -\frac{\Delta h_{\text{vap}}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right), \quad F = C - \mathcal{P} + 2, \quad \frac{d\ln K_p}{dT} = \frac{\Delta H^\circ}{R T^2}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{dP}{dT} = \frac{\Delta h}{T \Delta v}, \quad \ln\left(\frac{P_2}{P_1}\right) = -\frac{\Delta h_{\text{vap}}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right), \quad F = C - \mathcal{P} + 2, \quad \frac{d\ln K_p}{dT} = \frac{\Delta H^\circ}{R T^2}"""
                ),
            },
        ],
    },
    {
        "id": "phys_thermodynamics_termodin_mica_estad_stica",
        "domain": "physics",
        "category": "phys_thermodynamics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Termodinámica Estadística",
        "variations": [
            {
                "name": "Entropía de Boltzmann, Función de Partición Canónica y Gran Canónica",
                "description": "Entropía estadística S = k_B ln Ω, función de partición Z = ∑ e^{-βE_i} y conexión con potenciales F = -k_B T ln Z",
                "latex": r"""S = k_B \ln(\Omega), \quad Z = \sum \exp(-\beta E_i), \quad F = -k_B T \ln(Z), \quad U = -\frac{\partial \ln Z}{\partial \beta}, \quad \Phi_G = -P V = -k_B T \ln(\Xi)""",
                "builder": lambda: _parse_preset(
                    r"""S = k_B \ln(\Omega), \quad Z = \sum \exp(-\beta E_i), \quad F = -k_B T \ln(Z), \quad U = -\frac{\partial \ln Z}{\partial \beta}, \quad \Phi_G = -P V = -k_B T \ln(\Xi)"""
                ),
            },
            {
                "name": "Estadísticas Cuánticas de Fermi-Dirac y Bose-Einstein",
                "description": "Distribuciones de Fermi-Dirac (con energía de Fermi E_F) y Bose-Einstein (con condensación T_c)",
                "latex": r"""\langle n_i \rangle_{\text{FD}} = \frac{1}{e^{\beta(\epsilon_i - \mu)} + 1}, \quad E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{\frac{2}{3}}, \quad \langle n_i \rangle_{\text{BE}} = \frac{1}{e^{\beta(\epsilon_i - \mu)} - 1}, \quad T_c = \frac{2\pi \hbar^2}{m k_B}\left(\frac{n}{\zeta(3/2)}\right)^{\frac{2}{3}}""",
                "builder": lambda: _parse_preset(
                    r"""\langle n_i \rangle_{\text{FD}} = \frac{1}{e^{\beta(\epsilon_i - \mu)} + 1}, \quad E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{\frac{2}{3}}, \quad \langle n_i \rangle_{\text{BE}} = \frac{1}{e^{\beta(\epsilon_i - \mu)} - 1}, \quad T_c = \frac{2\pi \hbar^2}{m k_B}\left(\frac{n}{\zeta(3/2)}\right)^{\frac{2}{3}}"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_electrost_tica",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL BÁSICO",
        "title": "Electrostática",
        "variations": [
            {
                "name": "Ley de Coulomb y Fuerza Electrostática",
                "description": "Fuerza de atracción/repulsión entre cargas puntuales en el vacío",
                "latex": r"""F = \frac{1}{4\pi\varepsilon_0} \frac{|q_1 q_2|}{r^2} = k_e \frac{|q_1 q_2|}{r^2}, \quad \vec{F}_{12} = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r_{21}^2} \hat{\mathbf{r}}_{21}""",
                "builder": lambda: _parse_preset(
                    r"""F = \frac{1}{4\pi\varepsilon_0} \frac{|q_1 q_2|}{r^2} = k_e \frac{|q_1 q_2|}{r^2}, \quad \vec{F}_{12} = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r_{21}^2} \hat{\mathbf{r}}_{21}"""
                ),
            },
            {
                "name": "Campo Eléctrico, Potencial y Energía Electrostática",
                "description": "Campo E = F/q0, potencial escalar V = q/(4πε0 r) y energía potencial U = q1 q2 / (4πε0 r)",
                "latex": r"""\vec{E} = \frac{\vec{F}}{q_0} = \frac{1}{4\pi\varepsilon_0}\sum \frac{q_i}{r_i^2}\hat{\mathbf{r}}_i, \quad V(r) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}, \quad U = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r}""",
                "builder": lambda: _parse_preset(
                    r"""\vec{E} = \frac{\vec{F}}{q_0} = \frac{1}{4\pi\varepsilon_0}\sum \frac{q_i}{r_i^2}\hat{\mathbf{r}}_i, \quad V(r) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}, \quad U = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r}"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_condensadores_y_diel_ctricos",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL BÁSICO",
        "title": "Condensadores y Dieléctricos",
        "variations": [
            {
                "name": "Capacitancia, Geometrías y Energía Almacenada",
                "description": "Definición C = Q/V, placas plano-paralelas, coaxial, esférico y energía U = 1/2 C V²",
                "latex": r"""C = \frac{Q}{V}, \quad C_{\text{plano}} = \frac{\varepsilon_0 A}{d}, \quad C_{\text{cil}} = \frac{2\pi\varepsilon_0 L}{\ln(b/a)}, \quad U_C = \frac{1}{2} C V^2 = \frac{Q^2}{2C}""",
                "builder": lambda: _parse_preset(
                    r"""C = \frac{Q}{V}, \quad C_{\text{plano}} = \frac{\varepsilon_0 A}{d}, \quad C_{\text{cil}} = \frac{2\pi\varepsilon_0 L}{\ln(b/a)}, \quad U_C = \frac{1}{2} C V^2 = \frac{Q^2}{2C}"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_distribuciones_de_carga_y_ley_de_gauss",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL INTERMEDIO",
        "title": "Distribuciones de Carga y Ley de Gauss",
        "variations": [
            {
                "name": "Flujo Eléctrico y Ley de Gauss en Forma Integral",
                "description": "Flujo de campo eléctrico a través de superficie cerrada y carga neta encerrada",
                "latex": r"""\Phi_E = \iint_S \vec{E} \cdot d\vec{A} \implies \oiint_{\partial V} \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}, \quad \vec{E} = -\nabla V""",
                "builder": lambda: _parse_preset(
                    r"""\Phi_E = \iint_S \vec{E} \cdot d\vec{A} \implies \oiint_{\partial V} \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}, \quad \vec{E} = -\nabla V"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_dipolos_y_medios_diel_ctricos",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL INTERMEDIO",
        "title": "Dipolos y Medios Dieléctricos",
        "variations": [
            {
                "name": "Dipolo Eléctrico, Desplazamiento D y Vector Polarización P",
                "description": "Momento dipolar p = qd, torque τ = p × E, vector D = ε0 E + P y densidades de carga ligada",
                "latex": r"""\vec{p} = q \vec{d}, \quad \vec{\tau} = \vec{p} \times \vec{E}, \quad \vec{D} = \varepsilon_0 \vec{E} + \vec{P} = \varepsilon \vec{E}, \quad \rho_b = -\nabla \cdot \vec{P}, \quad u_e = \frac{1}{2} \vec{D} \cdot \vec{E}""",
                "builder": lambda: _parse_preset(
                    r"""\vec{p} = q \vec{d}, \quad \vec{\tau} = \vec{p} \times \vec{E}, \quad \vec{D} = \varepsilon_0 \vec{E} + \vec{P} = \varepsilon \vec{E}, \quad \rho_b = -\nabla \cdot \vec{P}, \quad u_e = \frac{1}{2} \vec{D} \cdot \vec{E}"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_ecuaciones_diferenciales_y_expansi_n_multipolar",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Ecuaciones Diferenciales y Expansión Multipolar",
        "variations": [
            {
                "name": "Ecuaciones de Poisson y Laplace, Condiciones de Frontera y Expansión Multipolar",
                "description": "Ecuación diferencial ∇²V = -ρ/ε0, condiciones de contorno y serie de multipolos electrostáticos",
                "latex": r"""\nabla^2 V = -\frac{\rho}{\varepsilon_0}, \quad \nabla^2 V = 0, \quad E_{1t} = E_{2t}, \quad D_{1n} - D_{2n} = \sigma_f, \quad V(\vec{r}) = \frac{1}{4\pi\varepsilon_0}\left[\frac{Q}{r} + \frac{\vec{p}\cdot\hat{\mathbf{r}}}{r^2} + \dots\right]""",
                "builder": lambda: _parse_preset(
                    r"""\nabla^2 V = -\frac{\rho}{\varepsilon_0}, \quad \nabla^2 V = 0, \quad E_{1t} = E_{2t}, \quad D_{1n} - D_{2n} = \sigma_f, \quad V(\vec{r}) = \frac{1}{4\pi\varepsilon_0}\left[\frac{Q}{r} + \frac{\vec{p}\cdot\hat{\mathbf{r}}}{r^2} + \dots\right]"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_corriente_y_circuitos_dc",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL BÁSICO",
        "title": "Corriente y Circuitos DC",
        "variations": [
            {
                "name": "Ley de Ohm, Efecto Joule y Leyes de Kirchhoff",
                "description": "Resistencia R = ρ L/A, potencia disipada P = V I = I² R y leyes de nodos y mallas de Kirchhoff",
                "latex": r"""V = I R, \quad R = \rho_e \frac{L}{A}, \quad P = V I = I^2 R = \frac{V^2}{R}, \quad \sum I_k = 0, \quad \sum V_k = 0""",
                "builder": lambda: _parse_preset(
                    r"""V = I R, \quad R = \rho_e \frac{L}{A}, \quad P = V I = I^2 R = \frac{V^2}{R}, \quad \sum I_k = 0, \quad \sum V_k = 0"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_electrodin_mica_y_circuitos_transitorios",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL INTERMEDIO",
        "title": "Electrodinámica y Circuitos Transitorios",
        "variations": [
            {
                "name": "Ley de Ohm Puntual (Drude) y Transitorios RC y RL",
                "description": "Densidad de corriente J = σ E, constante de tiempo τ_RC = RC, τ_RL = L/R y carga/descarga",
                "latex": r"""\vec{J} = \sigma_c \vec{E} = n q \vec{v}_d, \quad q_{RC}(t) = C\mathcal{E}(1 - e^{-\frac{t}{RC}}), \quad i_{RL}(t) = \frac{\mathcal{E}}{R}(1 - e^{-\frac{R t}{L}})""",
                "builder": lambda: _parse_preset(
                    r"""\vec{J} = \sigma_c \vec{E} = n q \vec{v}_d, \quad q_{RC}(t) = C\mathcal{E}(1 - e^{-\frac{t}{RC}}), \quad i_{RL}(t) = \frac{\mathcal{E}}{R}(1 - e^{-\frac{R t}{L}})"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_continuidad_de_carga_y_circuitos_ac",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Continuidad de Carga y Circuitos AC",
        "variations": [
            {
                "name": "Ecuación de Continuidad de Carga y Potencia Compleja en AC",
                "description": "Conservación local de la carga ∇·J + ∂ρ/∂t = 0, impedancia compleja Z y potencia compleja S = P + jQ",
                "latex": r"""\nabla \cdot \vec{J} + \frac{\partial \rho}{\partial t} = 0, \quad \mathbf{V} = \mathbf{I} \mathbf{Z}, \quad Z_L = j\omega L, \quad Z_C = \frac{1}{j\omega C}, \quad \mathbf{S} = \mathbf{V}_{\text{rms}} \mathbf{I}_{\text{rms}}^* = P + j Q""",
                "builder": lambda: _parse_preset(
                    r"""\nabla \cdot \vec{J} + \frac{\partial \rho}{\partial t} = 0, \quad \mathbf{V} = \mathbf{I} \mathbf{Z}, \quad Z_L = j\omega L, \quad Z_C = \frac{1}{j\omega C}, \quad \mathbf{S} = \mathbf{V}_{\text{rms}} \mathbf{I}_{\text{rms}}^* = P + j Q"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_fuerza_magn_tica",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL BÁSICO",
        "title": "Fuerza Magnética",
        "variations": [
            {
                "name": "Fuerza de Lorentz, Movimiento Ciclotrónico y Dipolo Magnético",
                "description": "Fuerza F = q(E + v × B), radio de giro r = mv/(qB) y momento dipolar μ = N I A n",
                "latex": r"""\vec{F} = q(\vec{E} + \vec{v} \times \vec{B}), \quad r_{\text{ciclotron}} = \frac{m v}{|q| B}, \quad \vec{F}_{\text{hilo}} = I(\vec{L} \times \vec{B}), \quad \vec{\tau} = \vec{\mu} \times \vec{B}, \quad U = -\vec{\mu} \cdot \vec{B}""",
                "builder": lambda: _parse_preset(
                    r"""\vec{F} = q(\vec{E} + \vec{v} \times \vec{B}), \quad r_{\text{ciclotron}} = \frac{m v}{|q| B}, \quad \vec{F}_{\text{hilo}} = I(\vec{L} \times \vec{B}), \quad \vec{\tau} = \vec{\mu} \times \vec{B}, \quad U = -\vec{\mu} \cdot \vec{B}"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_leyes_de_biot_savart_y_amp_re",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL INTERMEDIO",
        "title": "Leyes de Biot-Savart y Ampère",
        "variations": [
            {
                "name": "Leyes de Biot-Savart, Ampère Integral y Materia Magnética (H, M)",
                "description": "Cálculo de campo magnético por Biot-Savart, solenoide B = μ0 n I, intensidad H y susceptibilidad χ_m",
                "latex": r"""d\vec{B} = \frac{\mu_0 I}{4\pi}\frac{d\vec{\ell} \times \hat{\mathbf{r}}}{r^2}, \quad \oint_C \vec{B}\cdot d\vec{\ell} = \mu_0 I_{\text{enc}}, \quad B_{\text{solenoide}} = \mu_0 n I, \quad \vec{H} = \frac{1}{\mu_0}\vec{B} - \vec{M} = \frac{\vec{B}}{\mu}""",
                "builder": lambda: _parse_preset(
                    r"""d\vec{B} = \frac{\mu_0 I}{4\pi}\frac{d\vec{\ell} \times \hat{\mathbf{r}}}{r^2}, \quad \oint_C \vec{B}\cdot d\vec{\ell} = \mu_0 I_{\text{enc}}, \quad B_{\text{solenoide}} = \mu_0 n I, \quad \vec{H} = \frac{1}{\mu_0}\vec{B} - \vec{M} = \frac{\vec{B}}{\mu}"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_potencial_vector_y_energ_a_magn_tica",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Potencial Vector y Energía Magnética",
        "variations": [
            {
                "name": "Potencial Vector Magnético A, Ley de Ampère Diferencial y Energía",
                "description": "Campo B = ∇ × A, calibre de Coulomb ∇²A = -μ0 J y densidad de energía magnética u_m = 1/2 B·H",
                "latex": r"""\nabla \cdot \vec{B} = 0, \quad \nabla \times \vec{H} = \vec{J}_f, \quad \vec{B} = \nabla \times \vec{A}, \quad \nabla^2 \vec{A} = -\mu_0 \vec{J}, \quad u_m = \frac{1}{2}\vec{B}\cdot\vec{H} = \frac{1}{2\mu_0}B^2""",
                "builder": lambda: _parse_preset(
                    r"""\nabla \cdot \vec{B} = 0, \quad \nabla \times \vec{H} = \vec{J}_f, \quad \vec{B} = \nabla \times \vec{A}, \quad \nabla^2 \vec{A} = -\mu_0 \vec{J}, \quad u_m = \frac{1}{2}\vec{B}\cdot\vec{H} = \frac{1}{2\mu_0}B^2"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_inducci_n_electromagn_tica",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL BÁSICO",
        "title": "Inducción Electromagnética",
        "variations": [
            {
                "name": "Ley de Faraday-Lenz, FEM Inducida e Inductancia",
                "description": "FEM inducida E = -dΦ_B/dt, FEM de movimiento E = B L v y energía en inductores U = 1/2 L I²",
                "latex": r"""\mathcal{E} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt}\left(\iint \vec{B}\cdot d\vec{A}\right), \quad \mathcal{E}_{\text{mov}} = B L v, \quad L = \frac{N\Phi_B}{I}, \quad U_L = \frac{1}{2} L I^2""",
                "builder": lambda: _parse_preset(
                    r"""\mathcal{E} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt}\left(\iint \vec{B}\cdot d\vec{A}\right), \quad \mathcal{E}_{\text{mov}} = B L v, \quad L = \frac{N\Phi_B}{I}, \quad U_L = \frac{1}{2} L I^2"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_ecuaciones_de_maxwell_y_teorema_de_poynting",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL INTERMEDIO",
        "title": "Ecuaciones de Maxwell y Teorema de Poynting",
        "variations": [
            {
                "name": "Ecuaciones de Maxwell Integrales, Corriente de Desplazamiento y Vector de Poynting",
                "description": "4 ecuaciones integrales de Maxwell, corriente de desplazamiento I_d = ε0 dΦ_E/dt y vector S = E × H",
                "latex": r"""\oint \vec{E}\cdot d\vec{\ell} = -\frac{d\Phi_B}{dt}, \quad \oint \vec{H}\cdot d\vec{\ell} = I_{f,\text{enc}} + \frac{d\Phi_D}{dt}, \quad \vec{S} = \vec{E} \times \vec{H} = \frac{1}{\mu_0}(\vec{E}\times\vec{B}), \quad I = \langle S \rangle = \frac{1}{2}\varepsilon_0 c E_0^2""",
                "builder": lambda: _parse_preset(
                    r"""\oint \vec{E}\cdot d\vec{\ell} = -\frac{d\Phi_B}{dt}, \quad \oint \vec{H}\cdot d\vec{\ell} = I_{f,\text{enc}} + \frac{d\Phi_D}{dt}, \quad \vec{S} = \vec{E} \times \vec{H} = \frac{1}{\mu_0}(\vec{E}\times\vec{B}), \quad I = \langle S \rangle = \frac{1}{2}\varepsilon_0 c E_0^2"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_ecuaciones_de_maxwell_y_potenciales_retardados",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Ecuaciones de Maxwell y Potenciales Retardados",
        "variations": [
            {
                "name": "Ecuaciones Diferenciales de Maxwell, Calibre de Lorenz y Potenciales de Liénard-Wiechert",
                "description": "Formulación diferencial microscópica/macroscópica, calibre de Lorenz y d'Alembertiano Box V = -ρ/ε0",
                "latex": r"""\nabla \cdot \vec{D} = \rho_f, \quad \nabla \cdot \vec{B} = 0, \quad \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}, \quad \nabla \times \vec{H} = \vec{J}_f + \frac{\partial \vec{D}}{\partial t}, \quad \Box V = -\frac{\rho}{\varepsilon_0}, \quad \Box \vec{A} = -\mu_0 \vec{J}""",
                "builder": lambda: _parse_preset(
                    r"""\nabla \cdot \vec{D} = \rho_f, \quad \nabla \cdot \vec{B} = 0, \quad \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}, \quad \nabla \times \vec{H} = \vec{J}_f + \frac{\partial \vec{D}}{\partial t}, \quad \Box V = -\frac{\rho}{\varepsilon_0}, \quad \Box \vec{A} = -\mu_0 \vec{J}"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_ondas_electromagn_ticas_y_tensor_de_maxwell",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Ondas Electromagnéticas y Tensor de Maxwell",
        "variations": [
            {
                "name": "Ondas EM Planas, Velocidad de la Luz c e Impedancia η0, Tensor de Esfuerzos",
                "description": "Ecuación de onda EM en el vacío, c = 1/√(μ0 ε0), impedancia η0 ≈ 377 Ω y tensor de esfuerzos T_ij",
                "latex": r"""\nabla^2 \vec{E} - \frac{1}{c^2}\frac{\partial^2\vec{E}}{\partial t^2} = \vec{0}, \quad c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}, \quad \eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 120\pi\,\Omega, \quad T_{ij} = \varepsilon_0\left(E_i E_j - \frac{1}{2}\delta_{ij}E^2\right) + \frac{1}{\mu_0}\left(B_i B_j - \frac{1}{2}\delta_{ij}B^2\right)""",
                "builder": lambda: _parse_preset(
                    r"""\nabla^2 \vec{E} - \frac{1}{c^2}\frac{\partial^2\vec{E}}{\partial t^2} = \vec{0}, \quad c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}, \quad \eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 120\pi\,\Omega, \quad T_{ij} = \varepsilon_0\left(E_i E_j - \frac{1}{2}\delta_{ij}E^2\right) + \frac{1}{\mu_0}\left(B_i B_j - \frac{1}{2}\delta_{ij}B^2\right)"""
                ),
            },
        ],
    },
    {
        "id": "phys_electromagnetism_electrodin_mica_covariante",
        "domain": "physics",
        "category": "phys_electromagnetism",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Electrodinámica Covariante",
        "variations": [
            {
                "name": "Formulación Covariante, Tensor de Faraday F^μν y Maxwell Cuadridimensional",
                "description": "Cuadrivectores J^μ, A^μ, tensor de campo F^μν, ecuaciones covariantes ∂_μ F^μν = μ0 J^ν e invariantes de Lorentz",
                "latex": r"""J^\mu = (c\rho, \vec{J}), \quad A^\mu = \left(\frac{V}{c}, \vec{A}\right), \quad F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu, \quad \partial_\mu F^{\mu\nu} = \mu_0 J^\nu, \quad \partial_\mu \tilde{F}^{\mu\nu} = 0, \quad F^{\mu\nu}F_{\mu\nu} = 2\left(B^2 - \frac{E^2}{c^2}\right)""",
                "builder": lambda: _parse_preset(
                    r"""J^\mu = (c\rho, \vec{J}), \quad A^\mu = \left(\frac{V}{c}, \vec{A}\right), \quad F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu, \quad \partial_\mu F^{\mu\nu} = \mu_0 J^\nu, \quad \partial_\mu \tilde{F}^{\mu\nu} = 0, \quad F^{\mu\nu}F_{\mu\nu} = 2\left(B^2 - \frac{E^2}{c^2}\right)"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_leyes_de_la_ptica_geom_trica",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL BÁSICO",
        "title": "Leyes de la Óptica Geométrica",
        "variations": [
            {
                "name": "Índice de Refracción, Ley de Snell y Ángulo Crítico",
                "description": "Propagación de la luz n = c/v, reflexión θ_i = θ_r, ley de Snell y reflexión interna total",
                "latex": r"""n = \frac{c}{v}, \quad \theta_i = \theta_r, \quad n_1 \sin(\theta_1) = n_2 \sin(\theta_2), \quad \sin(\theta_c) = \frac{n_2}{n_1}""",
                "builder": lambda: _parse_preset(
                    r"""n = \frac{c}{v}, \quad \theta_i = \theta_r, \quad n_1 \sin(\theta_1) = n_2 \sin(\theta_2), \quad \sin(\theta_c) = \frac{n_2}{n_1}"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_espejos_planos_y_esf_ricos",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL BÁSICO",
        "title": "Espejos Planos y Esféricos",
        "variations": [
            {
                "name": "Ecuación de Descartes para Espejos y Aumento Lateral",
                "description": "Distancia focal f = R/2, ecuación de conjugación 1/so + 1/si = 1/f y aumento m = -si/so",
                "latex": r"""f = \frac{R}{2}, \quad \frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f} = \frac{2}{R}, \quad m = \frac{y_i}{y_o} = -\frac{s_i}{s_o}""",
                "builder": lambda: _parse_preset(
                    r"""f = \frac{R}{2}, \quad \frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f} = \frac{2}{R}, \quad m = \frac{y_i}{y_o} = -\frac{s_i}{s_o}"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_lentes_delgadas_y_dioptrios",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL INTERMEDIO",
        "title": "Lentes Delgadas y Dioptrios",
        "variations": [
            {
                "name": "Fórmula del Fabricante de Lentes, Ecuación de Gauss y Potencia",
                "description": "Fabricante de lentes 1/f = (n-1)(1/R1 - 1/R2), ecuación de Gauss 1/so + 1/si = 1/f y potencia P = 1/f",
                "latex": r"""\frac{n_1}{s_o} + \frac{n_2}{s_i} = \frac{n_2 - n_1}{R}, \quad \frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right), \quad \frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f}, \quad P = \frac{1}{f}""",
                "builder": lambda: _parse_preset(
                    r"""\frac{n_1}{s_o} + \frac{n_2}{s_i} = \frac{n_2 - n_1}{R}, \quad \frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right), \quad \frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f}, \quad P = \frac{1}{f}"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_prismas_y_dispersi_n_crom_tica",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL INTERMEDIO",
        "title": "Prismas y Dispersión Cromática",
        "variations": [
            {
                "name": "Desviación en Prismas, Mínima Desviación y Número de Abbe",
                "description": "Desviación angular δ = θ1 + θ2' - A, índice por mínima desviación y número de Abbe V_d",
                "latex": r"""\delta = \theta_1 + \theta_2' - A, \quad n = \frac{\sin\left(\frac{A + \delta_{\min}}{2}\right)}{\sin\left(\frac{A}{2}\right)}, \quad V_d = \frac{n_d - 1}{n_F - n_C}""",
                "builder": lambda: _parse_preset(
                    r"""\delta = \theta_1 + \theta_2' - A, \quad n = \frac{\sin\left(\frac{A + \delta_{\min}}{2}\right)}{\sin\left(\frac{A}{2}\right)}, \quad V_d = \frac{n_d - 1}{n_F - n_C}"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_ptica_matricial_y_principio_de_fermat",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Óptica Matricial y Principio de Fermat",
        "variations": [
            {
                "name": "Matrices ABCD de Rayos, Principio de Fermat y Ecuación de la Eikonal",
                "description": "Propagación matricial de rayos paraxiales, principio variacional de Fermat y ecuación de la eikonal |∇S|² = n²",
                "latex": r"""\begin{bmatrix} y_2 \\ \theta_2 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} y_1 \\ \theta_1 \end{bmatrix}, \quad \delta \int_{P_1}^{P_2} n(\vec{r})\,ds = 0, \quad \frac{d}{ds}\left(n \frac{d\vec{r}}{ds}\right) = \nabla n, \quad |\nabla S|^2 = n^2(\vec{r})""",
                "builder": lambda: _parse_preset(
                    r"""\begin{bmatrix} y_2 \\ \theta_2 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} y_1 \\ \theta_1 \end{bmatrix}, \quad \delta \int_{P_1}^{P_2} n(\vec{r})\,ds = 0, \quad \frac{d}{ds}\left(n \frac{d\vec{r}}{ds}\right) = \nabla n, \quad |\nabla S|^2 = n^2(\vec{r})"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_interferencia_y_polarizaci_n_b_sica",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL BÁSICO",
        "title": "Interferencia y Polarización Básica",
        "variations": [
            {
                "name": "Experimento de Young, Ley de Malus y Ángulo de Brewster",
                "description": "Interferencia constructiva d sinθ = mλ, separación Δy = λD/d, ley de Malus I = I0 cos²θ y Brewster",
                "latex": r"""d \sin\theta = m \lambda, \quad \Delta y = \frac{\lambda D}{d}, \quad I = I_0 \cos^2\theta, \quad \tan(\theta_B) = \frac{n_2}{n_1}""",
                "builder": lambda: _parse_preset(
                    r"""d \sin\theta = m \lambda, \quad \Delta y = \frac{\lambda D}{d}, \quad I = I_0 \cos^2\theta, \quad \tan(\theta_B) = \frac{n_2}{n_1}"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_pel_culas_delgadas_y_difracci_n",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL INTERMEDIO",
        "title": "Películas Delgadas y Difracción",
        "variations": [
            {
                "name": "Interferencia en Películas Delgadas, Anillos de Newton y Difracción de Fraunhofer",
                "description": "Condición en láminas 2nt = (m + 1/2)λ, difracción en rendija simple I = I0 sinc²(β) y criterio de Rayleigh",
                "latex": r"""2 n t = \left(m + \frac{1}{2}\right)\lambda, \quad r_{\text{oscuro}} = \sqrt{m \lambda R}, \quad I(\theta) = I_0 \left[\frac{\sin(\beta)}{\beta}\right]^2, \quad \sin\theta_{\min} \approx 1.22 \frac{\lambda}{D}""",
                "builder": lambda: _parse_preset(
                    r"""2 n t = \left(m + \frac{1}{2}\right)\lambda, \quad r_{\text{oscuro}} = \sqrt{m \lambda R}, \quad I(\theta) = I_0 \left[\frac{\sin(\beta)}{\beta}\right]^2, \quad \sin\theta_{\min} \approx 1.22 \frac{\lambda}{D}"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_redes_de_difracci_n_y_f_rmulas_de_fresnel",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL INTERMEDIO",
        "title": "Redes de Difracción y Fórmulas de Fresnel",
        "variations": [
            {
                "name": "Redes de Difracción (Poder de Resolución) y Coeficientes de Fresnel",
                "description": "Ecuación de la red d sinθ = mλ, resolución R = mN y coeficientes de reflexión/transmisión de Fresnel",
                "latex": r"""d \sin\theta = m \lambda, \quad \mathcal{R} = \frac{\lambda}{\Delta\lambda} = m N, \quad r_\perp = -\frac{\sin(\theta_i - \theta_t)}{\sin(\theta_i + \theta_t)}, \quad r_\parallel = \frac{\tan(\theta_i - \theta_t)}{\tan(\theta_i + \theta_t)}, \quad R + T_w = 1""",
                "builder": lambda: _parse_preset(
                    r"""d \sin\theta = m \lambda, \quad \mathcal{R} = \frac{\lambda}{\Delta\lambda} = m N, \quad r_\perp = -\frac{\sin(\theta_i - \theta_t)}{\sin(\theta_i + \theta_t)}, \quad r_\parallel = \frac{\tan(\theta_i - \theta_t)}{\tan(\theta_i + \theta_t)}, \quad R + T_w = 1"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_difracci_n_escalar_y_formalismo_de_polarizaci_n",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Difracción Escalar y Formalismo de Polarización",
        "variations": [
            {
                "name": "Difracción de Fresnel-Kirchhoff, Vectores de Jones y Parámetros de Stokes",
                "description": "Integral de difracción, número de Fresnel N_F = a²/(λz), vector de Jones y parámetros de Stokes S0, S1, S2, S3",
                "latex": r"""N_F = \frac{a^2}{\lambda z}, \quad \vec{J} = \begin{bmatrix} E_{0x} e^{i\phi_x} \\ E_{0y} e^{i\phi_y} \end{bmatrix}, \quad \text{DOP} = \frac{\sqrt{S_1^2 + S_2^2 + S_3^2}}{S_0}, \quad \Gamma = \frac{2\pi}{\lambda} |n_e - n_o| d""",
                "builder": lambda: _parse_preset(
                    r"""N_F = \frac{a^2}{\lambda z}, \quad \vec{J} = \begin{bmatrix} E_{0x} e^{i\phi_x} \\ E_{0y} e^{i\phi_y} \end{bmatrix}, \quad \text{DOP} = \frac{\sqrt{S_1^2 + S_2^2 + S_3^2}}{S_0}, \quad \Gamma = \frac{2\pi}{\lambda} |n_e - n_o| d"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_dispersi_n_y_absorci_n",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL INTERMEDIO",
        "title": "Dispersión y Absorción",
        "variations": [
            {
                "name": "Ecuación de Sellmeier, Velocidad de Grupo e Índice Complejo",
                "description": "Fórmula de Sellmeier n²(λ), velocidad de grupo vg = c/ng, ley de Beer-Lambert I = I0 e^{-αz}",
                "latex": r"""n^2(\lambda) = 1 + \sum \frac{B_i \lambda^2}{\lambda^2 - C_i}, \quad v_g = \frac{c}{n_g} = \frac{c}{n - \lambda \frac{dn}{d\lambda}}, \quad \tilde{n} = n + i \kappa, \quad I(z) = I_0 e^{-\alpha z}""",
                "builder": lambda: _parse_preset(
                    r"""n^2(\lambda) = 1 + \sum \frac{B_i \lambda^2}{\lambda^2 - C_i}, \quad v_g = \frac{c}{n_g} = \frac{c}{n - \lambda \frac{dn}{d\lambda}}, \quad \tilde{n} = n + i \kappa, \quad I(z) = I_0 e^{-\alpha z}"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_fibras_pticas_y_ondas_evanescentes",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Fibras Ópticas y Ondas Evanescentes",
        "variations": [
            {
                "name": "Relaciones de Kramers-Kronig, Apertura Numérica NA y Ondas Evanescentes",
                "description": "Relaciones causales de Kramers-Kronig, apertura numérica NA = √(n1² - n2²), parámetro V y ondas evanescentes",
                "latex": r"""\text{Re}[\chi(\omega)] = \frac{2}{\pi}\mathcal{P}\int_0^\infty \frac{\Omega\,\text{Im}[\chi(\Omega)]}{\Omega^2 - \omega^2}d\Omega, \quad \text{NA} = \sqrt{n_1^2 - n_2^2}, \quad V = \frac{2\pi a}{\lambda_0}\text{NA} < 2.4048, \quad \vec{E}_t(z) = \vec{E}_{t0} e^{-\alpha z} e^{i(k_{tx}x - \omega t)}""",
                "builder": lambda: _parse_preset(
                    r"""\text{Re}[\chi(\omega)] = \frac{2}{\pi}\mathcal{P}\int_0^\infty \frac{\Omega\,\text{Im}[\chi(\Omega)]}{\Omega^2 - \omega^2}d\Omega, \quad \text{NA} = \sqrt{n_1^2 - n_2^2}, \quad V = \frac{2\pi a}{\lambda_0}\text{NA} < 2.4048, \quad \vec{E}_t(z) = \vec{E}_{t0} e^{-\alpha z} e^{i(k_{tx}x - \omega t)}"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_fotones_y_cuantos_de_luz",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL BÁSICO",
        "title": "Fotones y Cuantos de Luz",
        "variations": [
            {
                "name": "Energía y Momento del Fotón, Efecto Fotoeléctrico",
                "description": "Relación de Planck-Einstein E = hf = ℏω, momento p = h/λ = ℏk y efecto fotoeléctrico eV_corte = hf - Φ",
                "latex": r"""E = h f = \hbar \omega, \quad p = \frac{h}{\lambda} = \hbar k = \frac{E}{c}, \quad E_{k,\text{max}} = e V_{\text{corte}} = h f - \Phi, \quad P_{\text{rad}} = \frac{I}{c}""",
                "builder": lambda: _parse_preset(
                    r"""E = h f = \hbar \omega, \quad p = \frac{h}{\lambda} = \hbar k = \frac{E}{c}, \quad E_{k,\text{max}} = e V_{\text{corte}} = h f - \Phi, \quad P_{\text{rad}} = \frac{I}{c}"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_radiaci_n_t_rmica_y_f_sica_del_l_ser",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL INTERMEDIO",
        "title": "Radiación Térmica y Física del Láser",
        "variations": [
            {
                "name": "Leyes de Planck, Wien, Stefan-Boltzmann y Umbral Láser",
                "description": "Ley espectral de Planck, desplazamiento de Wien, Stefan-Boltzmann j* = σT⁴ y condición de ganancia láser",
                "latex": r"""u_\lambda(\lambda, T) = \frac{8\pi h c}{\lambda^5}\frac{1}{e^{\frac{h c}{\lambda k_B T}} - 1}, \quad \lambda_{\text{max}} T = b, \quad j^* = \sigma T^4, \quad \gamma_{\text{th}} = \alpha_{\text{perd}} + \frac{1}{2L}\ln\left(\frac{1}{R_1 R_2}\right)""",
                "builder": lambda: _parse_preset(
                    r"""u_\lambda(\lambda, T) = \frac{8\pi h c}{\lambda^5}\frac{1}{e^{\frac{h c}{\lambda k_B T}} - 1}, \quad \lambda_{\text{max}} T = b, \quad j^* = \sigma T^4, \quad \gamma_{\text{th}} = \alpha_{\text{perd}} + \frac{1}{2L}\ln\left(\frac{1}{R_1 R_2}\right)"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_haces_gaussianos",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Haces Gaussianos",
        "variations": [
            {
                "name": "Propagación de Haces Gaussianos TEM00 y Parámetro Complejo q(z)",
                "description": "Distancia confocal de Rayleigh z_R = π w0²/λ, perfil w(z), curvatura R(z) y transformación q2 = (A q1 + B)/(C q1 + D)",
                "latex": r"""z_R = \frac{\pi w_0^2}{\lambda_0}, \quad w(z) = w_0 \sqrt{1 + \left(\frac{z}{z_R}\right)^2}, \quad R(z) = z \left[1 + \left(\frac{z_R}{z}\right)^2\right], \quad \frac{1}{q(z)} = \frac{1}{R(z)} - i \frac{\lambda_0}{\pi n w^2(z)}""",
                "builder": lambda: _parse_preset(
                    r"""z_R = \frac{\pi w_0^2}{\lambda_0}, \quad w(z) = w_0 \sqrt{1 + \left(\frac{z}{z_R}\right)^2}, \quad R(z) = z \left[1 + \left(\frac{z_R}{z}\right)^2\right], \quad \frac{1}{q(z)} = \frac{1}{R(z)} - i \frac{\lambda_0}{\pi n w^2(z)}"""
                ),
            },
        ],
    },
    {
        "id": "phys_optics_ptica_no_lineal",
        "domain": "physics",
        "category": "phys_optics",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Óptica No Lineal",
        "variations": [
            {
                "name": "Polarización No Lineal, Generación de Segundo Armónico y Efecto Kerr",
                "description": "Susceptibilidades no lineales χ^(2), generación de segundo armónico SHG con phase matching y efecto Kerr n(I) = n0 + n2 I",
                "latex": r"""\vec{P}_{\text{NL}} = \varepsilon_0 \left(\chi^{(2)} : \vec{E}\vec{E} + \chi^{(3)} \vdots \vec{E}\vec{E}\vec{E}\right), \quad P^{(2)}(2\omega) = \varepsilon_0 \chi^{(2)} E^2(\omega), \quad \Delta k = 0, \quad n(I) = n_0 + n_2 I""",
                "builder": lambda: _parse_preset(
                    r"""\vec{P}_{\text{NL}} = \varepsilon_0 \left(\chi^{(2)} : \vec{E}\vec{E} + \chi^{(3)} \vdots \vec{E}\vec{E}\vec{E}\right), \quad P^{(2)}(2\omega) = \varepsilon_0 \chi^{(2)} E^2(\omega), \quad \Delta k = 0, \quad n(I) = n_0 + n_2 I"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_teor_a_de_la_relatividad_especial",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL BÁSICO",
        "title": "Teoría de la Relatividad Especial",
        "variations": [
            {
                "name": "Dilatación Temporal, Contracción de Longitud y Relación Energía-Momento",
                "description": "Factor γ, dilatación Δt = γΔt0, contracción L = L0/γ y relación relativista E² = (pc)² + (m0 c²)²",
                "latex": r"""\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}, \quad \Delta t = \gamma \Delta t_0, \quad L = \frac{L_0}{\gamma}, \quad E^2 = (p c)^2 + (m_0 c^2)^2""",
                "builder": lambda: _parse_preset(
                    r"""\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}, \quad \Delta t = \gamma \Delta t_0, \quad L = \frac{L_0}{\gamma}, \quad E^2 = (p c)^2 + (m_0 c^2)^2"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_espacio_tiempo_de_minkowski_y_cuadrivectores",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL INTERMEDIO",
        "title": "Espacio-Tiempo de Minkowski y Cuadrivectores",
        "variations": [
            {
                "name": "Transformaciones de Lorentz, Intervalo Invariante y Cuadrimomento",
                "description": "Transformaciones espaciotemporales de Lorentz, invariante Δs² y cuadrivector momento P^μ = (E/c, p)",
                "latex": r"""x' = \gamma(x - vt), \quad t' = \gamma\left(t - \frac{vx}{c^2}\right), \quad \Delta s^2 = c^2\Delta t^2 - |\Delta\vec{\mathbf{r}}|^2, \quad P^\mu = \left(\frac{E}{c}, \vec{\mathbf{p}}\right)""",
                "builder": lambda: _parse_preset(
                    r"""x' = \gamma(x - vt), \quad t' = \gamma\left(t - \frac{vx}{c^2}\right), \quad \Delta s^2 = c^2\Delta t^2 - |\Delta\vec{\mathbf{r}}|^2, \quad P^\mu = \left(\frac{E}{c}, \vec{\mathbf{p}}\right)"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_relatividad_general",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Relatividad General",
        "variations": [
            {
                "name": "Ecuaciones de Campo de Einstein, Geodésicas y Radio de Schwarzschild",
                "description": "Ecuaciones tensoriales de Einstein G_μν = (8πG/c⁴) T_μν, geodésicas y radio de Schwarzschild rs = 2GM/c²",
                "latex": r"""G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}, \quad \frac{d^2 x^\mu}{d\lambda^2} + \Gamma^\mu_{\alpha\beta}\frac{dx^\alpha}{d\lambda}\frac{dx^\beta}{d\lambda} = 0, \quad r_s = \frac{2GM}{c^2}""",
                "builder": lambda: _parse_preset(
                    r"""G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}, \quad \frac{d^2 x^\mu}{d\lambda^2} + \Gamma^\mu_{\alpha\beta}\frac{dx^\alpha}{d\lambda}\frac{dx^\beta}{d\lambda} = 0, \quad r_s = \frac{2GM}{c^2}"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_fenomenolog_a_cu_ntica_y_modelo_de_bohr",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL BÁSICO",
        "title": "Fenomenología Cuántica y Modelo de Bohr",
        "variations": [
            {
                "name": "Dualidad de De Broglie, Dispersión Compton, Incertidumbre y Niveles de Bohr",
                "description": "Longitud λ = h/p, efecto Compton Δλ = λC(1-cosθ), principio de Heisenberg y niveles En = -13.6 eV Z²/n²",
                "latex": r"""\lambda = \frac{h}{p}, \quad \Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta), \quad \Delta x \cdot \Delta p_x \ge \frac{\hbar}{2}, \quad E_n = -13.6\,\text{eV}\cdot\frac{Z^2}{n^2}""",
                "builder": lambda: _parse_preset(
                    r"""\lambda = \frac{h}{p}, \quad \Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta), \quad \Delta x \cdot \Delta p_x \ge \frac{\hbar}{2}, \quad E_n = -13.6\,\text{eV}\cdot\frac{Z^2}{n^2}"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_ecuaci_n_de_schr_dinger_y_sistemas_cu_nticos_1d",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL INTERMEDIO",
        "title": "Ecuación de Schrödinger y Sistemas Cuánticos 1D",
        "variations": [
            {
                "name": "Ecuación de Schrödinger, Pozo Infinito y Oscilador Armónico Cuántico",
                "description": "Ecuación de Schrödinger iℏ ∂Ψ/∂t = ĤΨ, energías en caja 1D y oscilador En = ℏω(n + 1/2)",
                "latex": r"""i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi, \quad E_n^{\text{caja}} = \frac{n^2 \pi^2 \hbar^2}{2m L^2}, \quad E_n^{\text{osc}} = \hbar\omega\left(n + \frac{1}{2}\right), \quad T_{\text{tunel}} \approx e^{-2\kappa a}""",
                "builder": lambda: _parse_preset(
                    r"""i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi, \quad E_n^{\text{caja}} = \frac{n^2 \pi^2 \hbar^2}{2m L^2}, \quad E_n^{\text{osc}} = \hbar\omega\left(n + \frac{1}{2}\right), \quad T_{\text{tunel}} \approx e^{-2\kappa a}"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_momento_angular_y_tomo_de_hidr_geno",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL INTERMEDIO",
        "title": "Momento Angular y Átomo de Hidrógeno",
        "variations": [
            {
                "name": "Operadores de Momento Angular y Función de Onda Hidrogenoide",
                "description": "Álgebra de conmutadores de momento angular, autovalores L²|l,m> = ℏ²l(l+1)|l,m> y función de onda",
                "latex": r"""[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z, \quad \hat{L}^2|l, m_l\rangle = \hbar^2 l(l+1)|l, m_l\rangle, \quad \hat{L}_z|l, m_l\rangle = \hbar m_l|l, m_l\rangle, \quad \psi_{nlm}(r,\theta,\phi) = R_{nl}(r)Y_l^m(\theta,\phi)""",
                "builder": lambda: _parse_preset(
                    r"""[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z, \quad \hat{L}^2|l, m_l\rangle = \hbar^2 l(l+1)|l, m_l\rangle, \quad \hat{L}_z|l, m_l\rangle = \hbar m_l|l, m_l\rangle, \quad \psi_{nlm}(r,\theta,\phi) = R_{nl}(r)Y_l^m(\theta,\phi)"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_formalismo_de_dirac_y_matrices_de_pauli",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Formalismo de Dirac y Matrices de Pauli",
        "variations": [
            {
                "name": "Conmutación Canónica, Matrices de Pauli, Perturbaciones y Regla de Oro de Fermi",
                "description": "Conmutador canónico [x̂, p̂] = iℏ, matrices de Pauli σ_i, corrección de energía de 2° orden y tasa de transición",
                "latex": r"""[\hat{x}_j, \hat{p}_k] = i\hbar \delta_{jk}, \quad \sigma_x = \begin{bmatrix}0&1\\1&0\end{bmatrix}, \quad \sigma_y = \begin{bmatrix}0&-i\\i&0\end{bmatrix}, \quad \sigma_z = \begin{bmatrix}1&0\\0&-1\end{bmatrix}, \quad \Gamma_{i\to f} = \frac{2\pi}{\hbar}|\langle f|\hat{H}'|i\rangle|^2 \rho(E_f)""",
                "builder": lambda: _parse_preset(
                    r"""[\hat{x}_j, \hat{p}_k] = i\hbar \delta_{jk}, \quad \sigma_x = \begin{bmatrix}0&1\\1&0\end{bmatrix}, \quad \sigma_y = \begin{bmatrix}0&-i\\i&0\end{bmatrix}, \quad \sigma_z = \begin{bmatrix}1&0\\0&-1\end{bmatrix}, \quad \Gamma_{i\to f} = \frac{2\pi}{\hbar}|\langle f|\hat{H}'|i\rangle|^2 \rho(E_f)"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_mec_nica_cu_ntica_relativista",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Mecánica Cuántica Relativista",
        "variations": [
            {
                "name": "Ecuaciones de Klein-Gordon y Dirac",
                "description": "Ecuación escalar de Klein-Gordon (espín 0) y ecuación espinorial de Dirac (espín 1/2) con matrices γ^μ",
                "latex": r"""\left(\Box + \frac{m^2 c^2}{\hbar^2}\right)\phi = 0, \quad \left(i\hbar \gamma^\mu \partial_\mu - mc\right)\psi = 0, \quad \{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu} I_{4\times 4}""",
                "builder": lambda: _parse_preset(
                    r"""\left(\Box + \frac{m^2 c^2}{\hbar^2}\right)\phi = 0, \quad \left(i\hbar \gamma^\mu \partial_\mu - mc\right)\psi = 0, \quad \{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu} I_{4\times 4}"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_estructura_nuclear_y_radiactividad",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL BÁSICO",
        "title": "Estructura Nuclear y Radiactividad",
        "variations": [
            {
                "name": "Energía de Enlace Nuclear, Ley de Desintegración y Periodo de Semidesintegración",
                "description": "Defecto de masa B = Δm c², ley radiactiva N(t) = N0 e^{-λt}, actividad A = λN y semivida t_1/2 = ln(2)/λ",
                "latex": r"""R = R_0 A^{\frac{1}{3}}, \quad B(A, Z) = \Delta m \cdot c^2 = [Z m_p + (A - Z)m_n - M]c^2, \quad N(t) = N_0 e^{-\lambda t}, \quad t_{\frac{1}{2}} = \frac{\ln(2)}{\lambda}""",
                "builder": lambda: _parse_preset(
                    r"""R = R_0 A^{\frac{1}{3}}, \quad B(A, Z) = \Delta m \cdot c^2 = [Z m_p + (A - Z)m_n - M]c^2, \quad N(t) = N_0 e^{-\lambda t}, \quad t_{\frac{1}{2}} = \frac{\ln(2)}{\lambda}"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_modelos_nucleares_y_dosimetr_a",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL INTERMEDIO",
        "title": "Modelos Nucleares y Dosimetría",
        "variations": [
            {
                "name": "Modelo de la Gota Líquida (Bethe-Weizsäcker), Balance Q y Dosimetría",
                "description": "Fórmula semiempírica de masa de Bethe-Weizsäcker, balance energético de reacción Q y dosis equivalente H = w_R D",
                "latex": r"""B(A, Z) = a_v A - a_s A^{\frac{2}{3}} - a_c \frac{Z(Z-1)}{A^{\frac{1}{3}}} - a_a \frac{(A-2Z)^2}{A} + \delta, \quad Q = (m_a + m_X - m_Y - m_b)c^2, \quad H = w_R \cdot D""",
                "builder": lambda: _parse_preset(
                    r"""B(A, Z) = a_v A - a_s A^{\frac{2}{3}} - a_c \frac{Z(Z-1)}{A^{\frac{1}{3}}} - a_a \frac{(A-2Z)^2}{A} + \delta, \quad Q = (m_a + m_X - m_Y - m_b)c^2, \quad H = w_R \cdot D"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_f_sica_de_part_culas_y_modelo_est_ndar",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Física de Partículas y Modelo Estándar",
        "variations": [
            {
                "name": "Potencial de Yukawa, Fórmula de Gell-Mann-Nishijima y Matriz CKM",
                "description": "Fuerza fuerte mediada por mesones V(r) = -g² e^{-μr}/r, relación Q = I3 + Y/2 y mezcla de quarks CKM",
                "latex": r"""V(r) = -g^2 \frac{e^{-\mu r}}{r}, \quad Q = I_3 + \frac{Y}{2}, \quad \begin{bmatrix}d'\\s'\\b'\end{bmatrix} = \mathbf{V}_{\text{CKM}}\begin{bmatrix}d\\s\\b\end{bmatrix}, \quad \sigma(E) = \frac{\pi}{k^2}\frac{g\Gamma_{\text{in}}\Gamma_{\text{out}}}{(E-E_0)^2 + (\Gamma/2)^2}""",
                "builder": lambda: _parse_preset(
                    r"""V(r) = -g^2 \frac{e^{-\mu r}}{r}, \quad Q = I_3 + \frac{Y}{2}, \quad \begin{bmatrix}d'\\s'\\b'\end{bmatrix} = \mathbf{V}_{\text{CKM}}\begin{bmatrix}d\\s\\b\end{bmatrix}, \quad \sigma(E) = \frac{\pi}{k^2}\frac{g\Gamma_{\text{in}}\Gamma_{\text{out}}}{(E-E_0)^2 + (\Gamma/2)^2}"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_cristalograf_a_y_gas_de_fermi",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL INTERMEDIO",
        "title": "Cristalografía y Gas de Fermi",
        "variations": [
            {
                "name": "Ley de Bragg, Condición de Laue, Energía de Fermi y Ley de Wiedemann-Franz",
                "description": "Difracción de rayos X 2d sinθ = nλ, energía de Fermi EF = (ℏ²/2m)(3π²n)^(2/3) y relación de Wiedemann-Franz K/σ = LT",
                "latex": r"""2 d_{hkl}\sin\theta = n \lambda, \quad \Delta\vec{\mathbf{k}} = \vec{\mathbf{G}}_{hkl}, \quad E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{\frac{2}{3}}, \quad g(E) = \frac{3N}{2E_F^{\frac{3}{2}}}\sqrt{E}, \quad \frac{K}{\sigma} = L T""",
                "builder": lambda: _parse_preset(
                    r"""2 d_{hkl}\sin\theta = n \lambda, \quad \Delta\vec{\mathbf{k}} = \vec{\mathbf{G}}_{hkl}, \quad E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{\frac{2}{3}}, \quad g(E) = \frac{3N}{2E_F^{\frac{3}{2}}}\sqrt{E}, \quad \frac{K}{\sigma} = L T"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_teor_a_de_bandas_y_semiconductores",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Teoría de Bandas y Semiconductores",
        "variations": [
            {
                "name": "Teorema de Bloch, Masa Efectiva y Concentración Intrínseca",
                "description": "Ondas de Bloch en redes periódicas ψ_k = e^{ikr} u_k(r), tensor de masa efectiva m* y ley de masas n·p = ni²",
                "latex": r"""\psi_{\vec{\mathbf{k}}}(\vec{\mathbf{r}}) = e^{i\vec{\mathbf{k}}\cdot\vec{\mathbf{r}}} u_{\vec{\mathbf{k}}}(\vec{\mathbf{r}}), \quad \frac{1}{m^*} = \frac{1}{\hbar^2}\frac{\partial^2 E}{\partial k^2}, \quad n_i = \sqrt{N_c N_v} e^{-\frac{E_g}{2k_B T}}, \quad n \cdot p = n_i^2""",
                "builder": lambda: _parse_preset(
                    r"""\psi_{\vec{\mathbf{k}}}(\vec{\mathbf{r}}) = e^{i\vec{\mathbf{k}}\cdot\vec{\mathbf{r}}} u_{\vec{\mathbf{k}}}(\vec{\mathbf{r}}), \quad \frac{1}{m^*} = \frac{1}{\hbar^2}\frac{\partial^2 E}{\partial k^2}, \quad n_i = \sqrt{N_c N_v} e^{-\frac{E_g}{2k_B T}}, \quad n \cdot p = n_i^2"""
                ),
            },
        ],
    },
    {
        "id": "phys_modern_fonones_y_superconductividad",
        "domain": "physics",
        "category": "phys_modern",
        "level": "NIVEL UNIVERSITARIO / AVANZADO",
        "title": "Fonones y Superconductividad",
        "variations": [
            {
                "name": "Modelo de Debye (Calor Específico T³), Ecuaciones de London y Brecha BCS",
                "description": "Capacidad calorífica de Debye Cv ∝ T³, efecto Meissner B(x) = B0 e^{-x/λL} y brecha superconductora BCS Δ(0) ≈ 1.764 kB Tc",
                "latex": r"""C_v^{\text{Debye}} = \frac{12\pi^4}{5} N k_B \left(\frac{T}{\Theta_D}\right)^3, \quad \nabla^2\vec{\mathbf{B}} = \frac{1}{\lambda_L^2}\vec{\mathbf{B}}, \quad B_c(T) = B_c(0)\left[1 - \left(\frac{T}{T_c}\right)^2\right], \quad \Delta(0) \approx 1.764\,k_B T_c""",
                "builder": lambda: _parse_preset(
                    r"""C_v^{\text{Debye}} = \frac{12\pi^4}{5} N k_B \left(\frac{T}{\Theta_D}\right)^3, \quad \nabla^2\vec{\mathbf{B}} = \frac{1}{\lambda_L^2}\vec{\mathbf{B}}, \quad B_c(T) = B_c(0)\left[1 - \left(\frac{T}{T_c}\right)^2\right], \quad \Delta(0) \approx 1.764\,k_B T_c"""
                ),
            },
        ],
    },
]
