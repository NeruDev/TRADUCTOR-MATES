"""
---
file: src/data/units.py
module: src.data.units
description: Catálogo estructurado de unidades físicas del Sistema Internacional (SI) y derivadas con magnitudes y símbolos LaTeX.
type: data/units
version: 1.0.0
date: 2026-08-24
dependencies: []
relations:
  - docs/ARCHITECTURE.md
  - src/ui/components/unit_card.py
  - src/ui/components/palette_widget.py
exports:
  - UNITS: "Lista de categorías de unidades fundamentales y derivadas con magnitudes"
test: pytest tests/test_editor_widget.py
constraints:
  - "Garantizar que todos los símbolos utilicen fuentes normalizadas mathrm en LaTeX"
keywords:
  - units
  - physical-units
  - international-system
  - magnitudes
  - latex-units
---

Physical Units (SI) & Dimensions Catalog.
Provides categorized physical units with formatted LaTeX symbols for interactive unit cards.
"""

from __future__ import annotations

UNITS: list[dict[str, object]] = [
    {
        "name": "Fundamentales",
        "units": [
            {
                "magnitude": r"Tiempo",
                "name": r"Segundo",
                "symbol": r"\mathrm{s}",
                "base": r"",
            },
            {
                "magnitude": r"Longitud",
                "name": r"Metro",
                "symbol": r"\mathrm{m}",
                "base": r"",
            },
            {
                "magnitude": r"Masa",
                "name": r"Kilogramo",
                "symbol": r"\mathrm{kg}",
                "base": r"",
            },
            {
                "magnitude": r"Corriente eléctrica",
                "name": r"Amperio",
                "symbol": r"\mathrm{A}",
                "base": r"",
            },
            {
                "magnitude": r"Temperatura termodinámica",
                "name": r"Kelvin",
                "symbol": r"\mathrm{K}",
                "base": r"",
            },
            {
                "magnitude": r"Cantidad de sustancia",
                "name": r"Mol",
                "symbol": r"\mathrm{mol}",
                "base": r"",
            },
            {
                "magnitude": r"Intensidad luminosa",
                "name": r"Candela",
                "symbol": r"\mathrm{cd}",
                "base": r"",
            },
        ],
    },
    {
        "name": "Derivadas SI con nombre especial",
        "units": [
            {
                "magnitude": r"Ángulo sólido",
                "name": r"estereorradián",
                "symbol": r"\mathrm{sr}",
                "base": r"\left[1\text{ (adimensional)}\right]",
            },
            {
                "magnitude": r"Frecuencia",
                "name": r"hertz",
                "symbol": r"\mathrm{Hz}",
                "base": r"\left[\mathrm{s^{-1}}\right]",
            },
            {
                "magnitude": r"Fuerza",
                "name": r"newton",
                "symbol": r"\mathrm{N}",
                "base": r"\left[\mathrm{kg\ m\ s^{-2}}\right]",
            },
            {
                "magnitude": r"Presión",
                "name": r"pascal",
                "symbol": r"\mathrm{Pa}",
                "base": r"\left[\mathrm{kg\ m^{-1}\ s^{-2}}\right]",
            },
            {
                "magnitude": r"Energía, trabajo, calor",
                "name": r"joule",
                "symbol": r"\mathrm{J}",
                "base": r"\left[\mathrm{kg\ m^2\ s^{-2}}\right]",
            },
            {
                "magnitude": r"Potencia",
                "name": r"watt",
                "symbol": r"\mathrm{W}",
                "base": r"\left[\mathrm{kg\ m^2\ s^{-3}}\right]",
            },
            {
                "magnitude": r"Carga eléctrica",
                "name": r"coulomb",
                "symbol": r"\mathrm{C}",
                "base": r"\left[\mathrm{A\ s}\right]",
            },
            {
                "magnitude": r"Diferencia de potencial",
                "name": r"volt",
                "symbol": r"\mathrm{V}",
                "base": r"\left[\mathrm{kg\ m^2\ s^{-3}\ A^{-1}}\right]",
            },
            {
                "magnitude": r"Capacitancia",
                "name": r"farad",
                "symbol": r"\mathrm{F}",
                "base": r"\left[\mathrm{kg^{-1}\ m^{-2}\ s^4\ A^2}\right]",
            },
            {
                "magnitude": r"Resistencia eléctrica",
                "name": r"ohm",
                "symbol": r"\Omega",
                "base": r"\left[\mathrm{kg\ m^2\ s^{-3}\ A^{-2}}\right]",
            },
            {
                "magnitude": r"Conductancia eléctrica",
                "name": r"siemens",
                "symbol": r"\mathrm{S}",
                "base": r"\left[\mathrm{kg^{-1}\ m^{-2}\ s^3\ A^2}\right]",
            },
            {
                "magnitude": r"Flujo magnético",
                "name": r"weber",
                "symbol": r"\mathrm{Wb}",
                "base": r"\left[\mathrm{kg\ m^2\ s^{-2}\ A^{-1}}\right]",
            },
            {
                "magnitude": r"Densidad de flujo magnético",
                "name": r"tesla",
                "symbol": r"\mathrm{T}",
                "base": r"\left[\mathrm{kg\ s^{-2}\ A^{-1}}\right]",
            },
            {
                "magnitude": r"Inductancia",
                "name": r"henry",
                "symbol": r"\mathrm{H}",
                "base": r"\left[\mathrm{kg\ m^2\ s^{-2}\ A^{-2}}\right]",
            },
            {
                "magnitude": r"Temperatura Celsius",
                "name": r"grado Celsius",
                "symbol": r"^\circ\mathrm{C}",
                "base": r"\left[\mathrm{K}\right]",
            },
            {
                "magnitude": r"Flujo luminoso",
                "name": r"lumen",
                "symbol": r"\mathrm{lm}",
                "base": r"\left[\mathrm{cd\ sr}\right]",
            },
            {
                "magnitude": r"Iluminancia",
                "name": r"lux",
                "symbol": r"\mathrm{lx}",
                "base": r"\left[\mathrm{lm\ m^{-2}} = \mathrm{cd\ sr\ m^{-2}}\right]",
            },
            {
                "magnitude": r"Actividad radiactiva",
                "name": r"becquerel",
                "symbol": r"\mathrm{Bq}",
                "base": r"\left[\mathrm{s^{-1}}\right]",
            },
            {
                "magnitude": r"Dosis absorbida",
                "name": r"gray",
                "symbol": r"\mathrm{Gy}",
                "base": r"\left[\mathrm{m^2\ s^{-2}}\right]",
            },
            {
                "magnitude": r"Dosis equivalente/efectiva",
                "name": r"sievert",
                "symbol": r"\mathrm{Sv}",
                "base": r"\left[\mathrm{m^2\ s^{-2}}\right]",
            },
            {
                "magnitude": r"Actividad catalítica",
                "name": r"katal",
                "symbol": r"\mathrm{kat}",
                "base": r"\left[\mathrm{mol\ s^{-1}}\right]",
            },
        ],
    },
    {
        "name": "Derivadas SI frecuentes sin nombre especial",
        "units": [
            {
                "magnitude": r"Velocidad",
                "name": r"Velocidad",
                "symbol": r"\mathrm{m\ s^{-1}}",
                "base": r"\left[\mathrm{m\ s^{-1}}\right]",
            },
            {
                "magnitude": r"Aceleración",
                "name": r"Aceleración",
                "symbol": r"\mathrm{m\ s^{-2}}",
                "base": r"\left[\mathrm{m\ s^{-2}}\right]",
            },
            {
                "magnitude": r"Densidad de masa",
                "name": r"Densidad de masa",
                "symbol": r"\mathrm{kg\ m^{-3}}",
                "base": r"\left[\mathrm{kg\ m^{-3}}\right]",
            },
            {
                "magnitude": r"Viscosidad dinámica",
                "name": r"Viscosidad dinámica",
                "symbol": r"\mathrm{Pa\ s}",
                "base": r"\left[\mathrm{kg\ m^{-1}\ s^{-1}}\right]",
            },
            {
                "magnitude": r"Viscosidad cinemática",
                "name": r"Viscosidad cinemática",
                "symbol": r"\mathrm{m^2\ s^{-1}}",
                "base": r"\left[\mathrm{m^2\ s^{-1}}\right]",
            },
            {
                "magnitude": r"Campo eléctrico",
                "name": r"Campo eléctrico",
                "symbol": r"\mathrm{V\ m^{-1}}",
                "base": r"\left[\mathrm{kg\ m\ s^{-3}\ A^{-1}}\right]",
            },
            {
                "magnitude": r"Campo magnético auxiliar",
                "name": r"Campo magnético auxiliar",
                "symbol": r"\mathrm{A\ m^{-1}}",
                "base": r"\left[\mathrm{A\ m^{-1}}\right]",
            },
            {
                "magnitude": r"Entropía/capacidad calorífica",
                "name": r"Entropía/capacidad calorífica",
                "symbol": r"\mathrm{J\ K^{-1}}",
                "base": r"\left[\mathrm{kg\ m^2\ s^{-2}\ K^{-1}}\right]",
            },
            {
                "magnitude": r"Calor específico másico",
                "name": r"Calor específico másico",
                "symbol": r"\mathrm{J\ kg^{-1}\ K^{-1}}",
                "base": r"\left[\mathrm{m^2\ s^{-2}\ K^{-1}}\right]",
            },
            {
                "magnitude": r"Conductividad térmica",
                "name": r"Conductividad térmica",
                "symbol": r"\mathrm{W\ m^{-1}\ K^{-1}}",
                "base": r"\left[\mathrm{kg\ m\ s^{-3}\ K^{-1}}\right]",
            },
        ],
    },
    {
        "name": "Unidades no SI aceptadas para uso con SI",
        "units": [
            {
                "magnitude": r"Tiempo",
                "name": r"minuto",
                "symbol": r"\mathrm{min}",
                "base": r"\left[60\ \mathrm{s}\right]",
            },
            {
                "magnitude": r"Tiempo",
                "name": r"hora",
                "symbol": r"\mathrm{h}",
                "base": r"\left[3600\ \mathrm{s}\right]",
            },
            {
                "magnitude": r"Tiempo",
                "name": r"día",
                "symbol": r"\mathrm{d}",
                "base": r"\left[86\,400\ \mathrm{s}\right]",
            },
            {
                "magnitude": r"Volumen",
                "name": r"litro",
                "symbol": r"\mathrm{L}",
                "base": r"\left[10^{-3}\ \mathrm{m}^3\right]",
            },
            {
                "magnitude": r"Masa",
                "name": r"tonelada",
                "symbol": r"\mathrm{t}",
                "base": r"\left[10^3\ \mathrm{kg}\right]",
            },
            {
                "magnitude": r"Área",
                "name": r"hectárea",
                "symbol": r"\mathrm{ha}",
                "base": r"\left[10^4\ \mathrm{m}^2\right]",
            },
            {
                "magnitude": r"Presión",
                "name": r"bar",
                "symbol": r"\mathrm{bar}",
                "base": r"\left[10^5\ \mathrm{Pa}\right]",
            },
            {
                "magnitude": r"Presión",
                "name": r"atmósfera estándar",
                "symbol": r"\mathrm{atm}",
                "base": r"\left[101\,325\ \mathrm{Pa}\right]",
            },
            {
                "magnitude": r"Energía",
                "name": r"electronvoltio",
                "symbol": r"\mathrm{eV}",
                "base": r"\left[1.602\,176\,634\times10^{-19}\ \mathrm{J}\right]",
            },
            {
                "magnitude": r"Longitud",
                "name": r"ångström",
                "symbol": r"\mathrm{Å}",
                "base": r"\left[10^{-10}\ \mathrm{m}\right]",
            },
        ],
    },
    {
        "name": "Unidades de ingeniería y laboratorio (muy usadas)",
        "units": [
            {
                "magnitude": r"Energía",
                "name": r"watt-hora",
                "symbol": r"\mathrm{Wh}",
                "base": r"\left[3600\ \mathrm{J}\right]",
            },
            {
                "magnitude": r"Energía",
                "name": r"kilowatt-hora",
                "symbol": r"\mathrm{kWh}",
                "base": r"\left[3.6\times10^6\ \mathrm{J}\right]",
            },
            {
                "magnitude": r"Potencia",
                "name": r"caballo de vapor métrico",
                "symbol": r"\mathrm{CV}",
                "base": r"\left[735.49875\ \mathrm{W}\right]",
            },
            {
                "magnitude": r"Potencia",
                "name": r"horsepower mecánico",
                "symbol": r"\mathrm{hp}",
                "base": r"\left[745.699871582...\ \mathrm{W}\right]",
            },
            {
                "magnitude": r"Longitud náutica",
                "name": r"milla náutica",
                "symbol": r"\mathrm{nmi}",
                "base": r"\left[1852\ \mathrm{m}\right]",
            },
            {
                "magnitude": r"Velocidad",
                "name": r"nudo",
                "symbol": r"\mathrm{kn}",
                "base": r"\left[0.514444...\ \mathrm{m s}^{-1}\right]",
            },
        ],
    },
    {
        "name": "Magnitudes secundarias frecuentes en formularios",
        "units": [
            {
                "magnitude": r"Frecuencia angular",
                "name": r"Frecuencia angular",
                "symbol": r"\mathrm{rad s}^{-1}",
                "base": r"\left[\mathrm{s}^{-1}\right]",
            },
            {
                "magnitude": r"Densidad de carga",
                "name": r"Densidad de carga",
                "symbol": r"\mathrm{C m}^{-3}",
                "base": r"\left[\mathrm{A s m}^{-3}\right]",
            },
            {
                "magnitude": r"Densidad de corriente",
                "name": r"Densidad de corriente",
                "symbol": r"\mathrm{A m}^{-2}",
                "base": r"\left[\mathrm{A m}^{-2}\right]",
            },
        ],
    },
]
