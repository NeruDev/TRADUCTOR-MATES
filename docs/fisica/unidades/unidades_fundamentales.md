---
file: docs/fisica/unidades/unidades_fundamentales.md
description: Catálogo y especificación de las 7 unidades fundamentales base del SI (redefinición 2019).
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/units.py
relations:
  - docs/fisica/unidades/unidades_principales.md
  - docs/fisica/unidades/unidades_secundarias.md
  - docs/ARCHITECTURE.md
keywords:
  - unidades-fundamentales
  - sistema-internacional
  - unidades-base
  - constantes-definitorias
---

# 1. Unidades Fundamentales del SI

Este archivo debe leerse primero en la app: define las 7 unidades base del SI (redefinición 2019), ancladas a constantes con valor exacto.

| Magnitud fundamental | Unidad base | Símbolo | Constante definitoria asociada | Símbolo de constante | Valor exacto estandarizado (sin incertidumbre) |
| --- | --- | --- | --- | --- | --- |
| **Tiempo** | Segundo | $\mathrm{s}$ | Frecuencia de transición hiperfina del estado fundamental del átomo de $^{133}\mathrm{Cs}$ | $\Delta\nu_{\mathrm{Cs}}$ | $9\,192\,631\,770\ \mathrm{s}^{-1}\ (\mathrm{Hz})$ |
| **Longitud** | Metro | $\mathrm{m}$ | Velocidad de la luz en el vacío | $c$ | $299\,792\,458\ \mathrm{m s}^{-1}$ |
| **Masa** | Kilogramo | $\mathrm{kg}$ | Constante de Planck | $h$ | $6.626\,070\,15 \times 10^{-34}\ \mathrm{kg m}^2\mathrm{ s}^{-1}\ (\mathrm{J s})$ |
| **Corriente eléctrica** | Amperio | $\mathrm{A}$ | Carga elemental | $e$ | $1.602\,176\,634 \times 10^{-19}\ \mathrm{A s}\ (\mathrm{C})$ |
| **Temperatura termodinámica** | Kelvin | $\mathrm{K}$ | Constante de Boltzmann | $k_{\mathrm{B}}$ | $1.380\,649 \times 10^{-23}\ \mathrm{kg m}^2\mathrm{ s}^{-2}\mathrm{ K}^{-1}\ (\mathrm{J K}^{-1})$ |
| **Cantidad de sustancia** | Mol | $\mathrm{mol}$ | Constante de Avogadro | $N_{\mathrm{A}}$ | $6.022\,140\,76 \times 10^{23}\ \mathrm{mol}^{-1}$ |
| **Intensidad luminosa** | Candela | $\mathrm{cd}$ | Eficacia luminosa de radiación monocromática de frecuencia $540 \times 10^{12}\ \mathrm{Hz}$ | $K_{\mathrm{cd}}$ | $683\ \mathrm{cd sr kg}^{-1}\mathrm{ m}^{-2}\mathrm{ s}^3\ (\mathrm{lm W}^{-1})$ |
