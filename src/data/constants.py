"""
---
file: src/data/constants.py
module: src.data.constants
description: Catálogo estructurado de constantes matemáticas y físicas con valores de alta precisión y representaciones LaTeX.
type: data/constants
version: 1.0.0
date: 2026-08-24
dependencies: []
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/constant_card.py
  - src/ui/components/palette_widget.py
exports:
  - CONSTANTS: "Lista de categorías con constantes matemáticas y físicas de alta precisión"
test: pytest tests/test_editor_widget.py
constraints:
  - "Preservar las cadenas numéricas completas sin truncamiento prematuro de coma flotante"
keywords:
  - constants
  - math-constants
  - physics-constants
  - precision-values
  - latex-symbols
---

Mathematical and Physical Constants Catalog.
Provides categorized high-precision constants with formatted LaTeX symbols for interactive cards.
"""

from __future__ import annotations

CONSTANTS: list[dict[str, object]] = [
    {
        "name": "Geometría y Trigonometría",
        "constants": [
            {
                "name": "Número Pi",
                "symbol": "$\\pi$",
                "value": "3.14159265358979323846264338327950",
            },
            {
                "name": "Número Áureo",
                "symbol": "$\\phi$",
                "value": "1.61803398874989484820458683436563",
            },
            {
                "name": "Constante de Pitágoras",
                "symbol": "$\\sqrt{2}$",
                "value": "1.41421356237309504880168872420969",
            },
            {
                "name": "Constante de Teodoro",
                "symbol": "$\\sqrt{3}$",
                "value": "1.73205080756887729352744634150587",
            },
        ],
    },
    {
        "name": "Análisis Matemático y Cálculo",
        "constants": [
            {
                "name": "Base del Logaritmo Natural",
                "symbol": "$e$",
                "value": "2.71828182845904523536028747135266",
            },
            {
                "name": "Constante de Gompertz",
                "symbol": "$\\delta_G$",
                "value": "0.59634736232319407434107849936927",
            },
        ],
    },
    {
        "name": "Teoría de Números y Aritmética",
        "constants": [
            {
                "name": "Constante de Euler-Mascheroni",
                "symbol": "$\\gamma$",
                "value": "0.57721566490153286060651209008240",
            },
            {
                "name": "Constante de Catalan",
                "symbol": "$G$",
                "value": "0.91596559417721901505460351493238",
            },
            {
                "name": "Constante de Apéry",
                "symbol": "$\\zeta(3)$",
                "value": "1.20205690315959428539973816151144",
            },
            {
                "name": "Constante de Glaisher-Kinkelin",
                "symbol": "$A$",
                "value": "1.28242712910062263687534256886979",
            },
            {
                "name": "Constante de Khinchin",
                "symbol": "$K_0$",
                "value": "2.68545200106530644530971483548179",
            },
            {
                "name": "Constante de Meissel-Mertens",
                "symbol": "$M_1$",
                "value": "0.26149721284764278375542683860869",
            },
            {
                "name": "Constante de Brun para Primos Gemelos",
                "symbol": "$B_2$",
                "value": "1.902160583104",
            },
        ],
    },
    {
        "name": "Sistemas Dinámicos y Teoría del Caos",
        "constants": [
            {
                "name": "Primera Constante de Feigenbaum",
                "symbol": "$\\delta$",
                "value": "4.66920160910299067185320382046620",
            },
            {
                "name": "Segunda Constante de Feigenbaum",
                "symbol": "$\\alpha$",
                "value": "2.50290787509589282228390287321821",
            },
        ],
    },
    {
        "name": "Combinatoria y Teoría de Algoritmos",
        "constants": [
            {
                "name": "Constante de Conway",
                "symbol": "$\\lambda$",
                "value": "1.30357726903429639125709911215255",
            },
            {
                "name": "Constante de Golomb-Dickman",
                "symbol": "$\\lambda_{GD}$",
                "value": "0.62432998854355087099293638310083",
            },
            {
                "name": "Constante de Chaitin",
                "symbol": "$\\Omega_U$",
                "value": "0.00787499699",
            },
        ],
    },
]
