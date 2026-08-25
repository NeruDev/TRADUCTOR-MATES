---
file: docs/fisica/unidades/unidades_secundarias.md
description: Catálogo y especificación de unidades no SI aceptadas y unidades de uso práctico en física.
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/units.py
relations:
  - docs/fisica/unidades/unidades_fundamentales.md
  - docs/fisica/unidades/unidades_principales.md
  - docs/ARCHITECTURE.md
keywords:
  - unidades-secundarias
  - conversiones-unidades
  - unidades-practicas
  - unidades-no-si
---

# 3. Unidades Secundarias y de Uso Práctico

Este archivo debe leerse tercero en la app: agrupa unidades no SI aceptadas y otras conversiones comunes en física aplicada.

## 1. Unidades no SI aceptadas para uso con SI

| Magnitud | Unidad | Símbolo | Valor en SI |
| --- | --- | --- | --- |
| Tiempo | minuto | min | $60\ \mathrm{s}$ |
| Tiempo | hora | h | $3600\ \mathrm{s}$ |
| Tiempo | día | d | $86\,400\ \mathrm{s}$ |
| Ángulo plano | grado | $^\circ$ | $\pi/180\ \mathrm{rad}$ |
| Ángulo plano | minuto de arco | ' | $\pi/10\,800\ \mathrm{rad}$ |
| Ángulo plano | segundo de arco | '' | $\pi/648\,000\ \mathrm{rad}$ |
| Volumen | litro | L | $10^{-3}\ \mathrm{m}^3$ |
| Masa | tonelada | t | $10^3\ \mathrm{kg}$ |
| Área | hectárea | ha | $10^4\ \mathrm{m}^2$ |
| Presión | bar | bar | $10^5\ \mathrm{Pa}$ |
| Presión | atmósfera estándar | atm | $101\,325\ \mathrm{Pa}$ |
| Energía | electronvoltio | eV | $1.602\,176\,634\times10^{-19}\ \mathrm{J}$ |
| Longitud | ångström | Å | $10^{-10}\ \mathrm{m}$ |

## 2. Unidades de ingeniería y laboratorio (muy usadas)

| Magnitud | Unidad | Símbolo | Valor en SI |
| --- | --- | --- | --- |
| Energía | watt-hora | Wh | $3600\ \mathrm{J}$ |
| Energía | kilowatt-hora | kWh | $3.6\times10^6\ \mathrm{J}$ |
| Potencia | caballo de vapor métrico | CV | $735.49875\ \mathrm{W}$ |
| Potencia | horsepower mecánico | hp | $745.699871582...\ \mathrm{W}$ |
| Longitud náutica | milla náutica | nmi | $1852\ \mathrm{m}$ |
| Velocidad | nudo | kn | $0.514444...\ \mathrm{m s}^{-1}$ |

## 3. Magnitudes secundarias frecuentes en formularios

| Magnitud | Unidad habitual | Equivalencia SI |
| --- | --- | --- |
| Frecuencia angular | $\mathrm{rad s}^{-1}$ | $\mathrm{s}^{-1}$ |
| Densidad de carga | $\mathrm{C m}^{-3}$ | $\mathrm{A s m}^{-3}$ |
| Densidad de corriente | $\mathrm{A m}^{-2}$ | $\mathrm{A m}^{-2}$ |
