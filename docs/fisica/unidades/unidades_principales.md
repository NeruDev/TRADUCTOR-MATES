---
file: docs/fisica/unidades/unidades_principales.md
description: Catálogo y especificación de unidades derivadas principales del SI con y sin nombre especial.
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/units.py
relations:
  - docs/fisica/unidades/unidades_fundamentales.md
  - docs/fisica/unidades/unidades_secundarias.md
  - docs/ARCHITECTURE.md
keywords:
  - unidades-derivadas
  - sistema-internacional
  - magnitudes-fisicas
  - equivalencias-si
---

# 2. Unidades Principales Derivadas del SI

Este archivo debe leerse segundo en la app: recopila unidades derivadas SI de uso transversal en física (con y sin nombre especial), con su equivalencia en unidades base.

## 1. Derivadas SI con nombre especial

| Magnitud | Unidad | Símbolo | Equivalencia en SI base |
| --- | --- | --- | --- |
| Ángulo plano | radián | rad | $1$ (adimensional) |
| Ángulo sólido | estereorradián | sr | $1$ (adimensional) |
| Frecuencia | hertz | Hz | $\mathrm{s^{-1}}$ |
| Fuerza | newton | N | $\mathrm{kg\ m\ s^{-2}}$ |
| Presión | pascal | Pa | $\mathrm{kg\ m^{-1}\ s^{-2}}$ |
| Energía, trabajo, calor | joule | J | $\mathrm{kg\ m^2\ s^{-2}}$ |
| Potencia | watt | W | $\mathrm{kg\ m^2\ s^{-3}}$ |
| Carga eléctrica | coulomb | C | $\mathrm{A\ s}$ |
| Diferencia de potencial | volt | V | $\mathrm{kg\ m^2\ s^{-3}\ A^{-1}}$ |
| Capacitancia | farad | F | $\mathrm{kg^{-1}\ m^{-2}\ s^4\ A^2}$ |
| Resistencia eléctrica | ohm | $\Omega$ | $\mathrm{kg\ m^2\ s^{-3}\ A^{-2}}$ |
| Conductancia eléctrica | siemens | S | $\mathrm{kg^{-1}\ m^{-2}\ s^3\ A^2}$ |
| Flujo magnético | weber | Wb | $\mathrm{kg\ m^2\ s^{-2}\ A^{-1}}$ |
| Densidad de flujo magnético | tesla | T | $\mathrm{kg\ s^{-2}\ A^{-1}}$ |
| Inductancia | henry | H | $\mathrm{kg\ m^2\ s^{-2}\ A^{-2}}$ |
| Temperatura Celsius | grado Celsius | $^\circ\mathrm{C}$ | $\mathrm{K}$ |
| Flujo luminoso | lumen | lm | $\mathrm{cd\ sr}$ |
| Iluminancia | lux | lx | $\mathrm{lm\ m^{-2}} = \mathrm{cd\ sr\ m^{-2}}$ |
| Actividad radiactiva | becquerel | Bq | $\mathrm{s^{-1}}$ |
| Dosis absorbida | gray | Gy | $\mathrm{m^2\ s^{-2}}$ |
| Dosis equivalente/efectiva | sievert | Sv | $\mathrm{m^2\ s^{-2}}$ |
| Actividad catalítica | katal | kat | $\mathrm{mol\ s^{-1}}$ |

## 2. Derivadas SI frecuentes sin nombre especial

| Magnitud | Unidad habitual | Equivalencia en SI base |
| --- | --- | --- |
| Velocidad | $\mathrm{m\ s^{-1}}$ | $\mathrm{m\ s^{-1}}$ |
| Aceleración | $\mathrm{m\ s^{-2}}$ | $\mathrm{m\ s^{-2}}$ |
| Densidad de masa | $\mathrm{kg\ m^{-3}}$ | $\mathrm{kg\ m^{-3}}$ |
| Viscosidad dinámica | $\mathrm{Pa\ s}$ | $\mathrm{kg\ m^{-1}\ s^{-1}}$ |
| Viscosidad cinemática | $\mathrm{m^2\ s^{-1}}$ | $\mathrm{m^2\ s^{-1}}$ |
| Campo eléctrico | $\mathrm{V\ m^{-1}}$ | $\mathrm{kg\ m\ s^{-3}\ A^{-1}}$ |
| Campo magnético auxiliar | $\mathrm{A\ m^{-1}}$ | $\mathrm{A\ m^{-1}}$ |
| Entropía/capacidad calorífica | $\mathrm{J\ K^{-1}}$ | $\mathrm{kg\ m^2\ s^{-2}\ K^{-1}}$ |
| Calor específico másico | $\mathrm{J\ kg^{-1}\ K^{-1}}$ | $\mathrm{m^2\ s^{-2}\ K^{-1}}$ |
| Conductividad térmica | $\mathrm{W\ m^{-1}\ K^{-1}}$ | $\mathrm{kg\ m\ s^{-3}\ K^{-1}}$ |

## 3. Otras Unidades Derivadas por Rama de la Física (SI)

*(Se omiten las magnitudes ya listadas en las tablas superiores para evitar duplicidad de datos)*

- ### 1. Mecánica Clásica
  - #### Momento de una Fuerza (Torque)
    $$ \mathrm{Newton metro} = \mathrm{N}\cdot\mathrm{m} \left[\frac{\mathrm{kg}\cdot\mathrm{m}^2}{\mathrm{s}^2}\right] $$
  - #### Cantidad de Movimiento (Momento lineal)
    $$ \mathrm{Kilogramo metro por segundo} = \mathrm{kg}\cdot\mathrm{m}/\mathrm{s} \left[\frac{\mathrm{kg}\cdot\mathrm{m}}{\mathrm{s}}\right] $$
  - #### Momento Angular y Acción
    $$ \mathrm{Joule segundo} = \mathrm{J}\cdot\mathrm{s} \left[\frac{\mathrm{kg}\cdot\mathrm{m}^2}{\mathrm{s}}\right] $$

- ### 2. Termodinámica y Mecánica Estadística
  - #### Entropía Molar y Capacidad Calorífica Molar
    $$ \mathrm{Joule por mol Kelvin} = \mathrm{J}/(\mathrm{mol}\cdot\mathrm{K}) \left[\frac{\mathrm{kg}\cdot\mathrm{m}^2}{\mathrm{s}^2\cdot\mathrm{mol}\cdot\mathrm{K}}\right] $$

- ### 3. Ondas, Oscilaciones y Acústica
  - #### Número de Onda Espacial
    $$ \mathrm{Metro a la menos uno} = \mathrm{m}^{-1} \left[\frac{1}{\mathrm{m}}\right] $$
  - #### Intensidad Sonora y Densidad de Flujo de Potencia
    $$ \mathrm{Watt por metro cuadrado} = \mathrm{W}/\mathrm{m}^2 \left[\frac{\mathrm{kg}}{\mathrm{s}^3}\right] $$
  - #### Impedancia Acústica Específica
    $$ \mathrm{Pascal segundo por metro} = \mathrm{Pa}\cdot\mathrm{s}/\mathrm{m} \left[\frac{\mathrm{kg}}{\mathrm{m}^2\cdot\mathrm{s}}\right] $$

- ### 4. Óptica y Fotometría
  - #### Luminancia (Brillo fotométrico)
    $$ \mathrm{Candela por metro cuadrado} = \mathrm{cd}/\mathrm{m}^2 \left[\frac{\mathrm{cd}}{\mathrm{m}^2}\right] $$
  - #### Potencia Óptica (Refringencia / Convergencia)
    $$ \mathrm{Dioptría} = \mathrm{dpt} \left[\frac{1}{\mathrm{m}}\right] $$

- ### 5. Física Atómica, Nuclear y de Radiaciones
  - #### Exposición a Radiación Ionizante
    $$ \mathrm{Coulomb por kilogramo} = \mathrm{C}/\mathrm{kg} \left[\frac{\mathrm{A}\cdot\mathrm{s}}{\mathrm{kg}}\right] $$
  - #### Energía a Escala Atómica
    $$ \mathrm{Electronvoltio} = \mathrm{eV} = 1.602176634 \times 10^{-19}\mathrm{ J} \left[1.602176634 \times 10^{-19}\frac{\mathrm{kg}\cdot\mathrm{m}^2}{\mathrm{s}^2}\right] $$

## 4. Nota de alcance

- Estas son las unidades principales recomendadas para visualización didáctica y consistencia en la app.
- Las unidades no SI o de uso convencional se listan en el archivo de unidades secundarias.
