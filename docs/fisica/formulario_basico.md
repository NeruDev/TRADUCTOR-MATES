---
file: docs/fisica/formulario_basico.md
description: Compendio didáctico de fórmulas de física de nivel básico (cinemática, newton, ondas, fluidos).
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/symbols.py
relations:
  - docs/fisica/formulario_fisica.md
  - docs/mates/formulario_basico.md
  - docs/ARCHITECTURE.md
keywords:
  - formulas-basicas-fisica
  - cinematica-basica
  - dinamica-newton
  - fluidos-basicos
---

# Compendio I: Mecánica Clásica, de Fluidos y Analítica
*(Nivel Básico)*

## 1. Cinemática y Dinámica Newtoniana

### 1.1 Movimiento Rectilíneo Uniforme (MRU)

- Posición en función del tiempo:
  $$
  x(t) = x_0 + v \cdot t
  $$
- Velocidad media:
  $$
  v_m = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}
  $$
### 1.2 Movimiento Rectilíneo Uniformemente Acelerado (MRUA)

- Velocidad:
  $$
  v(t) = v_0 + a \cdot t
  $$
- Posición:
  $$
  x(t) = x_0 + v_0 t + \frac{1}{2} a t^2
  $$
- Ecuación independiente del tiempo (Torricelli):
  $$
  v_f^2 = v_0^2 + 2a (x_f - x_0)
  $$
- Desplazamiento medio:
  $$
  \Delta x = \left( \frac{v_0 + v_f}{2} \right) t
  $$
### 1.3 Leyes del Movimiento de Newton

- Primera Ley (Inercia):
  $$
  \sum \vec{F} = \vec{0} \iff \vec{v} = \mathrm{constante}
  $$
- Segunda Ley (Ley Fundamental de la Dinámica):
  $$
  \sum \vec{F} = m \vec{a} = \frac{d\vec{p}}{dt}
  $$
- Tercera Ley (Acción y Reacción):
  $$
  \vec{F}_{AB} = -\vec{F}_{BA}
  $$
### 1.4 Fuerzas de Fricción / Rozamiento

- Fricción estática máxima (1):
  $$
  f_{s,\mathrm{máx}} = \mu_s N
  $$
- Fricción estática máxima (2):
  $$
  \implies
  $$
- Fricción estática máxima (3):
  $$
  f_s \le \mu_s N
  $$
- Fricción cinética:
  $$
  f_k = \mu_k N
  $$
### 1.5 Movimiento Circular Uniforme (MCU) y Uniformemente Variado (MCUV)

- Relaciones lineales y angulares (1):
  $$
  s = \theta \cdot r
  $$
- Relaciones lineales y angulares (2):
  $$
  v = \omega \cdot r
  $$
- Relaciones lineales y angulares (3):
  $$
  a_t = \alpha \cdot r
  $$
- Aceleración centrípeta / normal:
  $$
  a_c = \frac{v^2}{r} = \omega^2 r
  $$
- Cinemática angular con $\alpha$ constante (1):
  $$
  \omega(t) = \omega_0 + \alpha t
  $$
- Cinemática angular con $\alpha$ constante (2):
  $$
  \theta(t) = \theta_0 + \omega_0 t + \frac{1}{2} \alpha t^2
  $$
- Cinemática angular con $\alpha$ constante (3):
  $$
  \omega_f^2 = \omega_0^2 + 2\alpha (\theta_f - \theta_0)
  $$
## 2. Trabajo, Energía, Momento Lineal y Gravitación

### 2.1 Trabajo y Energía Mecánica

- Trabajo efectuado por fuerza constante:
  $$
  W = \vec{F} \cdot \Delta\vec{r} = F \Delta r \cos(\theta)
  $$
- Energía Cinética traslacional:
  $$
  E_k = \frac{1}{2} m v^2
  $$
- Energía Potencial Gravitatoria (cerca de la superficie terrestre):
  $$
  E_{p,\mathrm{grav}} = m g h
  $$
- Energía Potencial Elástica (Ley de Hooke $F = -kx$):
  $$
  E_{p,\mathrm{elás}} = \frac{1}{2} k x^2
  $$
- Teorema del Trabajo y la Energía Cinética:
  $$
  W_{\mathrm{neto}} = \Delta E_k = \frac{1}{2} m v_f^2 - \frac{1}{2} m v_0^2
  $$
- Conservación de la Energía Mecánica:
  $$
  E_m = E_k + E_p \implies \Delta E_m = W_{\mathrm{no conservativas}}
  $$
### 2.2 Cantidad de Movimiento e Impulso

- Momento lineal:
  $$
  \vec{p} = m \vec{v}
  $$
- Impulso:
  $$
  \vec{J} = \vec{F}_{\mathrm{prom}} \Delta t = \Delta \vec{p}
  $$
- Choques unidimensionales y Coeficiente de Restitución ($e$):
  $$
  e = \frac{v_{2f} - v_{1f}}{v_{1i} - v_{2i}}
  $$
## 3. Oscilaciones y Mecánica de Fluidos

### 3.1 Oscilador Armónico Simple (M.A.S.)

- Ecuación diferencial y solución:
  $$
  \ddot{x} + \omega_0^2 x = 0 \implies x(t) = A \cos(\omega_0 t + \phi)
  $$
- Frecuencia angular:
  $$
  \omega_0 = \sqrt{\frac{k}{m}}
  $$
- Periodo (sistema masa-resorte):
  $$
  T = 2\pi\sqrt{\frac{m}{k}}
  $$
- Péndulo Simple:
  $$
  T = 2\pi\sqrt{\frac{L}{g}}
  $$
- Péndulo Físico:
  $$
  T = 2\pi\sqrt{\frac{I}{m g d}}
  $$
### 3.2 Estática de Fluidos

- Presión hidrostática:
  $$
  P(h) = P_0 + \rho g h
  $$
- Principio de Pascal:
  $$
  \frac{F_1}{A_1} = \frac{F_2}{A_2}
  $$
- Principio de Arquímedes (Fuerza de Empuje):
  $$
  E = \rho_{\mathrm{fluido}} g V_{\mathrm{sumergido}}
  $$
# Compendio II: Oscilaciones y Ondas Mecánicas
*(Nivel Básico)*

## 4. Movimiento Oscilatorio (Oscilaciones)

### 4.1 Cinemática del Movimiento Armónico Simple (M.A.S.)

- Posición en función del tiempo:
  $$
  x(t) = A \cos(\omega t + \phi)
  $$
- Velocidad:
  $$
  v(t) = \frac{dx}{dt} = -\omega A \sen(\omega t + \phi) = \pm \omega \sqrt{A^2 - x^2}
  $$
- Aceleración:
  $$
  a(t) = \frac{d^2x}{dt^2} = -\omega^2 A \cos(\omega t + \phi) = -\omega^2 x(t)
  $$
- Valores máximos (1):
  $$
  x_{\mathrm{máx}} = A
  $$
- Valores máximos (2):
  $$
  v_{\mathrm{máx}} = \omega A
  $$
- Valores máximos (3):
  $$
  a_{\mathrm{máx}} = \omega^2 A
  $$
### 4.2 Parámetros Temporales y Frecuenciales

- Periodo ($T$):
  $$
  T = \frac{1}{f} = \frac{2\pi}{\omega}
  $$
- Frecuencia ($f$):
  $$
  f = \frac{1}{T} = \frac{\omega}{2\pi}
  $$
- Frecuencia angular ($\omega$):
  $$
  \omega = 2\pi f = \frac{2\pi}{T}
  $$
### 4.3 Energía del M.A.S. (Sistema Conservativo)

- Energía Cinética:
  $$
  E_k = \frac{1}{2} m v^2 = \frac{1}{2} m \omega^2 A^2 \sen^2(\omega t + \phi)
  $$
- Energía Potencial Elástica:
  $$
  E_p = \frac{1}{2} k x^2 = \frac{1}{2} k A^2 \cos^2(\omega t + \phi)
  $$
- Energía Mecánica Total:
  $$
  E_m = E_k + E_p = \frac{1}{2} k A^2 = \frac{1}{2} m \omega^2 A^2 = \mathrm{constante}
  $$
### 4.4 Sistemas Oscilatorios Simples

- Masa-Resorte (1):
  $$
  \omega_0 = \sqrt{\frac{k}{m}}
  $$
- Masa-Resorte (2):
  $$
  T = 2\pi\sqrt{\frac{m}{k}}
  $$
- Péndulo Simple (Aproximación para ángulos pequeños $\sen\theta \approx \theta$) (1):
  $$
  \omega_0 = \sqrt{\frac{g}{L}}
  $$
- Péndulo Simple (Aproximación para ángulos pequeños $\sen\theta \approx \theta$) (2):
  $$
  T = 2\pi\sqrt{\frac{L}{g}}
  $$
## 5. Ondas Mecánicas en Medios Continuos

### 5.1 Cinemática de Ondas Armónicas Unidimensionales

- Función de Onda Progresiva (hacia la derecha $-$ / hacia la izquierda $+$):
  $$
  y(x, t) = A \sen(k x \mp \omega t + \phi)
  $$
- Relación entre Parámetros Fundamentales (1):
  $$
  k = \frac{2\pi}{\lambda}
  $$
- Relación entre Parámetros Fundamentales (2):
  $$
  \omega = \frac{2\pi}{T} = 2\pi f
  $$
- Relación entre Parámetros Fundamentales (3):
  $$
  v = \lambda f = \frac{\lambda}{T} = \frac{\omega}{k}
  $$
- Velocidad:
  $$
  v_y(x, t) = \frac{\partial y}{\partial t} = \mp \omega A \cos(k x \mp \omega t + \phi)
  $$
- Aceleración transversal de las partículas del medio:
  $$
  a_y(x, t) = \frac{\partial^2 y}{\partial t^2} = -\omega^2 A \sen(k x \mp \omega t + \phi) = -\omega^2 y(x, t)
  $$
## 6. Interferencia, Ondas Estacionarias y Acústica

### 6.1 Superposición e Interferencia

- Interferencia de dos ondas armónicas con diferencia de fase $\Delta\phi$:
  $$
  y_R(x, t) = \left[ 2A \cos\left(\frac{\Delta\phi}{2}\right) \right] \sen\left(kx - \omega t + \frac{\Delta\phi}{2}\right)
  $$
- Condición de Interferencia Constructiva:
  $$
  \Delta\phi = 2n\pi \implies \Delta r = n\lambda \quad n \in \mathbb{Z}
  $$
- Condición de Interferencia Destructiva:
  $$
  \Delta\phi = (2n + 1)\pi \implies \Delta r = \left(n + \frac{1}{2}\right)\lambda \quad n \in \mathbb{Z}
  $$
### 6.2 Batidos o Pulsaciones

- Superposición de ondas con frecuencias ligeramente diferentes $\omega_1 \approx \omega_2$:
  $$
  y_R(t) = \left[ 2A \cos\left( \frac{\omega_1 - \omega_2}{2} t \right) \right] \cos\left( \frac{\omega_1 + \omega_2}{2} t \right)
  $$
- Frecuencia de Batido:
  $$
  f_{\mathrm{batido}} = |f_1 - f_2|
  $$
### 6.3 Escala Decibélica y Nivel de Sonido

- Nivel de Intensidad Sonora ($\beta$) (1):
  $$
  \beta = 10 \log_{10}\left( \frac{I}{I_0} \right)
  $$
- Nivel de Intensidad Sonora ($\beta$) (2):
  $$
  I_0 = 10^{-12} \, \mathrm{W/m}^2
  $$
- Nivel de Presión Sonora ($SPL$) (1):
  $$
  L_p = 20 \log_{10}\left( \frac{p_{\mathrm{rms}}}{p_0} \right)
  $$
- Nivel de Presión Sonora ($SPL$) (2):
  $$
  p_0 = 20 \, \mu\mathrm{Pa}
  $$
# Compendio III: Termodinámica Clásica, Química y Estadística
*(Nivel Básico)*

## 7. Conceptos Fundamentales, Gases y Ecuaciones de Estado

### 7.1 Escalas Termométricas y Temperatura

- Escala Celsius a Kelvin:
  $$
  T(\mathrm{K}) = T(^\circ\mathrm{C}) + 273.15
  $$
- Escala Celsius a Fahrenheit:
  $$
  T(^\circ\mathrm{F}) = \frac{9}{5} T(^\circ\mathrm{C}) + 32
  $$
- Escala Fahrenheit a Rankine (Temperatura absoluta $T_{\mathrm{R}}$):
  $$
  T_{\mathrm{R}}(\mathrm{Ra}) = T(^\circ\mathrm{F}) + 459.67 = \frac{9}{5} T(\mathrm{K})
  $$
### 7.2 Dilatación Térmica

- Dilatación Lineal:
  $$
  \Delta L = \alpha L_0 \Delta T \implies L(T) = L_0 (1 + \alpha \Delta T)
  $$
- Dilatación Superficial ($\gamma \approx 2\alpha$):
  $$
  \Delta A = \gamma A_0 \Delta T \implies A(T) = A_0 (1 + \gamma \Delta T)
  $$
- Dilatación Volumétrica ($\beta \approx 3\alpha$ para sólidos isótropos):
  $$
  \Delta V = \beta V_0 \Delta T \implies V(T) = V_0 (1 + \beta \Delta T)
  $$
### 7.3 Calorimetría y Capacidad Calorífica

- Calor sensible:
  $$
  Q = m c \Delta T = n C_m \Delta T = C \Delta T
  $$
- Calor latente en cambio de fase:
  $$
  Q = m L
  $$
- Principio de Conservación de la Energía (Equilibrio térmico):
  $$
  \sum Q_{\mathrm{ganado}} + \sum Q_{\mathrm{perdido}} = 0 \implies \sum m_i c_i (T_{\mathrm{eq}} - T_i) = 0
  $$
### 7.4 Gas Ideal y Leyes Empíricas

- Ecuación de Estado del Gas Ideal (1):
  $$
  P V = n R T = N k_B T
  $$
- Ecuación de Estado del Gas Ideal (2):
  $$
  R = N_A k_B \approx 8.314 \, \frac{\mathrm{J}}{\mathrm{mol}\cdot\mathrm{K}}
  $$
- Ley de Boyle-Mariotte ($T = \mathrm{constante}$):
  $$
  P_1 V_1 = P_2 V_2
  $$
- Ley de Charles ($P = \mathrm{constante}$):
  $$
  \frac{V_1}{T_1} = \frac{V_2}{T_2}
  $$
- Ley de Gay-Lussac ($V = \mathrm{constante}$):
  $$
  \frac{P_1}{T_1} = \frac{P_2}{T_2}
  $$
- Ley Combinada:
  $$
  \frac{P_1 V_1}{T_1} = \frac{P_2 V_2}{T_2}
  $$
## 8. Primera y Segunda Ley de la Termodinámica

### 8.1 Primera Ley de la Termodinámica (Sistemas Cerrados)

- Forma Integral (Convención física: trabajo $W$ realizado por el sistema):
  $$
  \Delta U = Q - W
  $$
- Forma Diferencial General (Sistema cerrado):
  $$
  dU = \delta Q - \delta W
  $$
- Para procesos cuasiestáticos de expansión/compresión hidrostática ($\delta W = P \, dV$):
  $$
  dU = \delta Q - P \, dV
  $$
- Trabajo Cuasiestático de Expansión/Compresión:
  $$
  W = \int_{V_i}^{V_f} P \, dV
  $$
### 8.2 Procesos Termodinámicos Cuasiestáticos en Gases Ideales

- Proceso Isocórico ($V = \mathrm{constante}, \, dV = 0$) (1):
  $$
  W = 0
  $$
- Proceso Isocórico ($V = \mathrm{constante}, \, dV = 0$) (2):
  $$
  Q = \Delta U = n C_v \Delta T
  $$
- Proceso Isobárico ($P = \mathrm{constante}$) (1):
  $$
  W = P(V_f - V_i) = n R \Delta T
  $$
- Proceso Isobárico ($P = \mathrm{constante}$) (2):
  $$
  Q = n C_p \Delta T
  $$
- Proceso Isobárico ($P = \mathrm{constante}$) (3):
  $$
  \Delta U = n C_v \Delta T
  $$
- Proceso Isotérmico ($T = \mathrm{constante}, \, \Delta T = 0$):
  $$
  \Delta U = 0 \implies Q = W = n R T \ln\left(\frac{V_f}{V_i}\right) = n R T \ln\left(\frac{P_i}{P_f}\right)
  $$
- Proceso Adiabático Reversible ($Q = 0, \, \delta Q = 0$) (1):
  $$
  Q = 0 \implies \Delta U = -W = n C_v (T_f - T_i) = \frac{P_f V_f - P_i V_i}{1 - \gamma}
  $$
- Proceso Adiabático Reversible ($Q = 0, \, \delta Q = 0$) (2):
  $$
  P V^\gamma = \mathrm{constante}
  $$
- Proceso Adiabático Reversible ($Q = 0, \, \delta Q = 0$) (3):
  $$
  T V^{\gamma - 1} = \mathrm{constante}
  $$
- Proceso Adiabático Reversible ($Q = 0, \, \delta Q = 0$) (4):
  $$
  T^\gamma P^{1 - \gamma} = \mathrm{constante}
  $$
- Relación de mayer:
  $$
  C_p - C_v = R
  $$
- Coeficiente de dilatación adiabática:
  $$
  \gamma = \frac{C_p}{C_v}
  $$
# Compendio IV: Electricidad y Magnetismo
*(Nivel Básico)*

## 9. Electrostática y Medios Dieléctricos

### 9.1 Ley de Coulomb y Fuerza Eléctrica

- Magnitud de la fuerza entre dos cargas puntuales (1):
  $$
  F = \frac{1}{4\pi\varepsilon_0} \frac{|q_1 q_2|}{r^2} = k_e \frac{|q_1 q_2|}{r^2}
  $$
- Magnitud de la fuerza entre dos cargas puntuales (2):
  $$
  k_e \approx 8.9875 \times 10^9 \, \frac{\mathrm{N}\cdot\mathrm{m}^2}{\mathrm{C}^2}
  $$
- Forma vectorial de la fuerza sobre $q_1$ debida a $q_2$:
  $$
  \vec{F}_{12} = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r_{21}^2} \hat{r}_{21}
  $$
### 9.2 Campo Eléctrico ($\vec{E}$)

- Definición por carga de prueba:
  $$
  \vec{E} = \frac{\vec{F}}{q_0}
  $$
- Campo de una carga puntual:
  $$
  \vec{E} = \frac{1}{4\pi\varepsilon_0} \frac{q}{r^2} \hat{r}
  $$
- Principio de superposición para $N$ cargas:
  $$
  \vec{E}_{\mathrm{total}} = \sum_{i=1}^N \vec{E}_i = \frac{1}{4\pi\varepsilon_0} \sum_{i=1}^N \frac{q_i}{r_i^2} \hat{r}_i
  $$
### 9.3 Potencial y Energía Potencial Electrostática

- Potencial eléctrico de una carga puntual:
  $$
  V(r) = \frac{1}{4\pi\varepsilon_0} \frac{q}{r}
  $$
- Trabajo y diferencia de potencial:
  $$
  W_{A \to B} = -q_0 \Delta V = q_0 (V_A - V_B)
  $$
- Energía potencial electrostática de dos cargas:
  $$
  U = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r}
  $$
### 9.4 Capacitancia y Condensadores

- Definición general:
  $$
  C = \frac{Q}{V}
  $$
- Condensador de placas plano-paralelas:
  $$
  C = \frac{\varepsilon_0 A}{d}
  $$
- Condensador coaxial / cilíndrico (longitud $L$, radios $a < b$):
  $$
  C = \frac{2\pi\varepsilon_0 L}{\ln(b/a)}
  $$
- Condensador esférico (radios $a < b$):
  $$
  C = 4\pi\varepsilon_0 \left( \frac{a b}{b - a} \right)
  $$
- Asociación de Condensadores (1):
  $$
  \mathrm{En Paralelo: } C_{\mathrm{eq}} = \sum_{i=1}^N C_i \quad |
  $$
- Asociación de Condensadores (2):
  $$
  \mathrm{En Serie: } \frac{1}{C_{\mathrm{eq}}} = \sum_{i=1}^N \frac{1}{C_i}
  $$
- Energía almacenada en un condensador:
  $$
  U = \frac{1}{2} Q V = \frac{1}{2} C V^2 = \frac{Q^2}{2C}
  $$
## 10. Electrodinámica, Corriente y Circuitos Eléctricos

### 10.1 Corriente, Resistencia y Ley de Ohm

- Intensidad de corriente eléctrica:
  $$
  I = \frac{dQ}{dt}
  $$
- Ley de Ohm Macroscópica:
  $$
  V = I R
  $$
- Resistencia en función de la geometría:
  $$
  R = \rho_e \frac{L}{A} = \frac{L}{\sigma_c A}
  $$
- Variación de la resistividad con la temperatura:
  $$
  \rho_e(T) = \rho_0 [1 + \alpha (T - T_0)]
  $$
### 10.2 Potencia Eléctrica y Efecto Joule

- Potencia disipada / consumida:
  $$
  P = V I = I^2 R = \frac{V^2}{R}
  $$
- Energía disipada por efecto Joule:
  $$
  W = \int P \, dt = I^2 R t \quad (\mathrm{para } I \mathrm{ constante})
  $$
### 10.3 Fuerza Electromotriz (FEM) y Asociación de Resistencias

- FEM ($\mathcal{E}$) y voltaje terminal con resistencia interna $r$:
  $$
  V_{\mathrm{terminal}} = \mathcal{E} - I r
  $$
- Asociación de Resistencias (1):
  $$
  \mathrm{En Serie: } R_{\mathrm{eq}} = \sum_{i=1}^N R_i \quad |
  $$
- Asociación de Resistencias (2):
  $$
  \mathrm{En Paralelo: } \frac{1}{R_{\mathrm{eq}}} = \sum_{i=1}^N \frac{1}{R_i}
  $$
## 11. Magnetostática y Materia Magnética

### 11.1 Fuerza Magnética y Fuerza de Lorentz

- Fuerza magnética sobre una carga en movimiento:
  $$
  \vec{F}_B = q (\vec{v} \times \vec{B}) \implies F_B = |q| v B \sen\theta
  $$
- Fuerza de Lorentz completa:
  $$
  \vec{F} = q (\vec{E} + \vec{v} \times \vec{B})
  $$
- Movimiento ciclotrónico (carga perpendicular a campo uniforme) (1):
  $$
  r = \frac{m v}{|q| B}
  $$
- Movimiento ciclotrónico (carga perpendicular a campo uniforme) (2):
  $$
  \omega_c = \frac{|q| B}{m}
  $$
- Movimiento ciclotrónico (carga perpendicular a campo uniforme) (3):
  $$
  T = \frac{2\pi m}{|q| B}
  $$
### 11.2 Fuerza Magnética sobre Conductores

- Conductor rectilíneo con corriente $I$:
  $$
  \vec{F} = I (\vec{L} \times \vec{B})
  $$
- Conductor de geometría arbitraria:
  $$
  \vec{F} = \int_C I (d\vec{\ell} \times \vec{B})
  $$
- Fuerza magnética entre dos conductores paralelos largos (1):
  $$
  \frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}
  $$
- Fuerza magnética entre dos conductores paralelos largos (2):
  $$
  \mu_0 = 4\pi \times 10^{-7} \, \frac{\mathrm{T}\cdot\mathrm{m}}{\mathrm{A}}
  $$
### 11.3 Dipolo Magnético

- Momento dipolar magnético de una espira plana:
  $$
  \vec{\mu} = N I A \hat{n}
  $$
- Torque sobre una espira en campo magnético:
  $$
  \vec{\tau} = \vec{\mu} \times \vec{B}
  $$
- Energía potencial magnética del dipolo:
  $$
  U = -\vec{\mu} \cdot \vec{B}
  $$
## 12. Inducción Electromagnética, Maxwell y Ondas

### 12.1 Ley de Faraday-Henry y Ley de Lenz

- Fuerza Electromotriz Inducida ($\mathcal{E}$):
  $$
  \mathcal{E} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt}\left( \iint_S \vec{B} \cdot d\vec{A} \right)
  $$
- FEM de movimiento en barra conductora (longitud $L$, velocidad $v \perp B$):
  $$
  \mathcal{E} = B L v
  $$
### 12.2 Inductancia y Autoinducción

- Autoinductancia ($L$):
  $$
  L = \frac{N \Phi_B}{I} \implies \mathcal{E}_L = -L \frac{dI}{dt}
  $$
- Inductancia de un solenoide ideal (longitud $l$, área $A$, $N$ vueltas):
  $$
  L = \mu_0 \frac{N^2 A}{l} = \mu_0 n^2 A l
  $$
- Inductancia Mutua ($M$) (1):
  $$
  M_{12} = \frac{N_2 \Phi_{21}}{I_1}
  $$
- Inductancia Mutua ($M$) (2):
  $$
  \mathcal{E}_2 = -M_{12} \frac{dI_1}{dt}
  $$
- Energía acumulada en un inductor:
  $$
  U = \frac{1}{2} L I^2
  $$
# Compendio V: Óptica y Luz
*(Nivel Básico)*

## 13. Óptica Geométrica y Sistemas Ópticos

### 13.1 Propagación de la Luz y Leyes Fundamentales

- Índice de refracción absoluto ($c = \mathrm{velocidad en el vacío}$):
  $$
  n = \frac{c}{v}
  $$
- Ley de Reflexión:
  $$
  \theta_i = \theta_r
  $$
- Ley de Refracción (Ley de Snell):
  $$
  n_1 \sen(\theta_1) = n_2 \sen(\theta_2)
  $$
- Ángulo Crítico y Reflexión Interna Total ($n_1 > n_2$):
  $$
  \sen(\theta_c) = \frac{n_2}{n_1} \implies \theta_c = \arcsen\left( \frac{n_2}{n_1} \right)
  $$
### 13.2 Espejos Planos y Esféricos (Aproximación Paraxial)

- Relación entre Radio de Curvatura y Distancia Focal:
  $$
  f = \frac{R}{2}
  $$
- Ecuación de Descartes para Espejos Esféricos ($s_o = \mathrm{objeto}, \, s_i = \mathrm{imagen}$):
  $$
  \frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f} = \frac{2}{R}
  $$
- Aumento Lateral Transversal ($m$):
  $$
  m = \frac{y_i}{y_o} = -\frac{s_i}{s_o}
  $$
## 14. Óptica Ondulatoria (Interferencia, Difracción y Polarización)

### 14.1 Interferencia por División de Frente de Onda

- Experimento de la Doble Rendija de Young (Separación $d$, distancia a pantalla $D \gg d$) (1):
  $$
  d \sen\theta = m \lambda \implies y_{\mathrm{máx}} \approx m \frac{\lambda D}{d} \quad m \in \mathbb{Z}
  $$
- Experimento de la Doble Rendija de Young (Separación $d$, distancia a pantalla $D \gg d$) (2):
  $$
  d \sen\theta = \left( m + \frac{1}{2} \right)\lambda \implies y_{\mathrm{mín}} \approx \left( m + \frac{1}{2} \right)\frac{\lambda D}{d} \quad m \in \mathbb{Z}
  $$
- Experimento de la Doble Rendija de Young (Separación $d$, distancia a pantalla $D \gg d$) (3):
  $$
  \Delta y = \frac{\lambda D}{d}
  $$
### 14.2 Polarización de la Luz

- Ley de Malus (Intensidad tras polarizador lineal con ángulo $\theta$):
  $$
  I = I_0 \cos^2\theta
  $$
- Ángulo de Polarización de Brewster:
  $$
  \tan(\theta_B) = \frac{n_2}{n_1} \implies \theta_B + \theta_t = 90^\circ
  $$
## 15. Óptica Cuántica, Radiación, Haces Láser y No Lineal

### 15.1 Fotones y Naturaleza Cuántica de la Luz

- Energía del Fotón (Relación de Planck-Einstein) (1):
  $$
  E = h f = \hbar \omega
  $$
- Energía del Fotón (Relación de Planck-Einstein) (2):
  $$
  \hbar = \frac{h}{2\pi}
  $$
- Momento Lineal del Fotón (Relación de De Broglie):
  $$
  p = \frac{h}{\lambda} = \hbar k = \frac{E}{c}
  $$
- Ecuación del Efecto Fotoeléctrico de Einstein:
  $$
  E_{k,\mathrm{máx}} = e V_{\mathrm{corte}} = h f - \Phi
  $$
- Presión de Radiación ($P_{\mathrm{rad}}$ con densidad de flujo radiante / irradiancia $I$) (1):
  $$
  P_{\mathrm{rad}} = \frac{I}{c} \quad (\mathrm{Absorción pura})
  $$
- Presión de Radiación ($P_{\mathrm{rad}}$ con densidad de flujo radiante / irradiancia $I$) (2):
  $$
  P_{\mathrm{rad}} = \frac{2I}{c} \quad (\mathrm{Reflexión perfecta})
  $$
# Compendio VI: Física Moderna
*(Nivel Básico)*

## 16. Teoría de la Relatividad (Especial y General)

### 16.1 Cinemática Relativista Unidimensional

- Factor de Lorentz ($\gamma$ con $\beta = v/c$):
  $$
  \gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} = \frac{1}{\sqrt{1 - \beta^2}}
  $$
- Dilatación Temporal ($\Delta t_0 = \mathrm{tiempo propio}$):
  $$
  \Delta t = \gamma \Delta t_0 = \frac{\Delta t_0}{\sqrt{1 - \frac{v^2}{c^2}}}
  $$
- Contracción de la Longitud ($L_0 = \mathrm{longitud propia}$ en dirección del movimiento):
  $$
  L = \frac{L_0}{\gamma} = L_0 \sqrt{1 - \frac{v^2}{c^2}}
  $$
- Adición Relativista de Velocidades (Movimiento en el eje $x$):
  $$
  u_x' = \frac{u_x - v}{1 - \frac{u_x v}{c^2}} \iff u_x = \frac{u_x' + v}{1 + \frac{u_x' v}{c^2}}
  $$
### 16.2 Dinámica y Equivalencia Masa-Energía

- Momento Lineal Relativista:
  $$
  \vec{p} = \gamma m_0 \vec{v} = \frac{m_0 \vec{v}}{\sqrt{1 - \frac{v^2}{c^2}}}
  $$
- Energía en Reposo:
  $$
  E_0 = m_0 c^2
  $$
- Energía Total de una Partícula Libre:
  $$
  E = \gamma m_0 c^2 = E_k + m_0 c^2
  $$
- Energía Cinética Relativista:
  $$
  E_k = (\gamma - 1) m_0 c^2 = m_0 c^2 \left( \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} - 1 \right)
  $$
- Relación Fundamental Energía-Momento (1):
  $$
  E^2 = (p c)^2 + (m_0 c^2)^2 \implies E = \sqrt{p^2 c^2 + m_0^2 c^4}
  $$
- Relación Fundamental Energía-Momento (2):
  $$
  (\mathrm{Para fotones y partículas sin masa } m_0 = 0 \implies E = p c)
  $$
### 16.3 Efecto Doppler Relativista

- Fuente:
  $$
  f_o = f_s \sqrt{\frac{1 - \beta}{1 + \beta}} \quad (\mathrm{Alejamiento}) \quad |
  $$
- Observador en dirección longitudinal:
  $$
  f_o = f_s \sqrt{\frac{1 + \beta}{1 - \beta}} \quad (\mathrm{Acercamiento})
  $$
- Efecto Doppler Transversal ($\theta = 90^\circ$):
  $$
  f_o = \frac{f_s}{\gamma} = f_s \sqrt{1 - \beta^2}
  $$
## 17. Mecánica Cuántica y Física Atómica

### 17.1 Fenomenología Cuántica Temprana

- Hipótesis de De Broglie (Dualidad onda-partícula) (1):
  $$
  \lambda = \frac{h}{p} = \frac{h}{\gamma m v}
  $$
- Hipótesis de De Broglie (Dualidad onda-partícula) (2):
  $$
  p = \hbar k = \frac{h}{\lambda}
  $$
- Efecto Fotoeléctrico (Einstein) (1):
  $$
  E_k^{\mathrm{máx}} = e V_s = h f - \Phi_0 = \hbar \omega - \Phi_0
  $$
- Efecto Fotoeléctrico (Einstein) (2):
  $$
  f_0 = \frac{\Phi_0}{h}
  $$
- Dispersión Compton (Corrimiento en longitud de onda) (1):
  $$
  \Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta) = \lambda_C (1 - \cos\theta)
  $$
- Dispersión Compton (Corrimiento en longitud de onda) (2):
  $$
  \lambda_C = \frac{h}{m_e c} \approx 2.4263 \times 10^{-12} \, \mathrm{m} \quad (\mathrm{Longitud de onda Compton})
  $$
- Principio de Incertidumbre de Heisenberg (1):
  $$
  \Delta x \cdot \Delta p_x \ge \frac{\hbar}{2}
  $$
- Principio de Incertidumbre de Heisenberg (2):
  $$
  \Delta E \cdot \Delta t \ge \frac{\hbar}{2}
  $$
### 17.2 Modelo Atómico de Bohr (Átomos Hidrogenoides de número atómico $Z$)

- Cuantización del Momento Angular Orbital (1):
  $$
  L = m_e v r = n \hbar = n \frac{h}{2\pi}
  $$
- Cuantización del Momento Angular Orbital (2):
  $$
  n = 1, 2, 3, \dots
  $$
- Radios de Órbitas Permitidas ($a_0 = \mathrm{Radio de Bohr}$) (1):
  $$
  r_n = \frac{4\pi\varepsilon_0 \hbar^2}{m_e e^2} \frac{n^2}{Z} = a_0 \frac{n^2}{Z}
  $$
- Radios de Órbitas Permitidas ($a_0 = \mathrm{Radio de Bohr}$) (2):
  $$
  a_0 = \frac{4\pi\varepsilon_0 \hbar^2}{m_e e^2} \approx 0.529 \, \mathrm{Å}
  $$
- Niveles de Energía Cuantizados:
  $$
  E_n = -\frac{m_e Z^2 e^4}{32 \pi^2 \varepsilon_0^2 \hbar^2} \frac{1}{n^2} = -E_R \frac{Z^2}{n^2} = -13.6 \, \mathrm{eV} \cdot \frac{Z^2}{n^2}
  $$
- Fórmula de Rydberg para Transiciones Espectrales (1):
  $$
  \frac{1}{\lambda} = R_\infty Z^2 \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right)
  $$
- Fórmula de Rydberg para Transiciones Espectrales (2):
  $$
  R_\infty = \frac{m_e e^4}{8 \varepsilon_0^2 h^3 c} \approx 1.09737 \times 10^7 \, \mathrm{m}^{-1}
  $$
## 18. Física Nuclear, Radiactividad y Partículas Elementales

### 18.1 Estructura Nuclear y Defecto de Masa

- Radio Nuclear Empírico ($A = \mathrm{número másico}$) (1):
  $$
  R \approx R_0 A^{1/3}
  $$
- Radio Nuclear Empírico ($A = \mathrm{número másico}$) (2):
  $$
  R_0 \approx 1.2 \, \mathrm{fm} = 1.2 \times 10^{-15} \, \mathrm{m}
  $$
- Defecto de Masa ($\Delta m$ para un núcleo $_Z^A X_N$ con $N = A - Z$):
  $$
  \Delta m = Z m_p + N m_n - M_{\mathrm{núcleo}}(A, Z)
  $$
- Energía de Enlace Nuclear Total ($B$ o $E_b$):
  $$
  B(A, Z) = \Delta m \cdot c^2 = [Z m_p + (A - Z) m_n - M_{\mathrm{núcleo}}] c^2
  $$
- Energía de Enlace por Nucleón ($B/A$):
  $$
  \frac{B}{A} = \frac{B(A, Z)}{A} \quad (\approx 8.8 \, \mathrm{MeV/nucleón para el } ^{56}\mathrm{Fe})
  $$
### 18.2 Cinética de la Desintegración Radiactiva

- Ley de Desintegración Radiactiva:
  $$
  N(t) = N_0 e^{-\lambda t}
  $$
- Actividad radiactiva ($a(t)$ en becquerels $\mathrm{bq} = \mathrm{des/s}$:
  $$
  A(t) = -\frac{dN}{dt} = \lambda N(t) = A_0 e^{-\lambda t}
  $$
- Curie $\mathrm{ci}$):
  $$
  A_0 = \lambda N_0
  $$
- Periodo de Semidesintegración / Vida Media ($t_{1/2}$):
  $$
  t_{1/2} = \frac{\ln(2)}{\lambda} \approx \frac{0.693}{\lambda}
  $$
- Tiempo de Vida Medio ($\tau$):
  $$
  \tau = \frac{1}{\lambda} = \frac{t_{1/2}}{\ln(2)} \approx 1.443 \, t_{1/2}
  $$
### 18.3 Tipos Principales de Desintegración Radiactiva

- Desintegración Alfa ($\alpha = \,_2^4\mathrm{He}$):
  $$
  _Z^A X \longrightarrow \,_{Z-2}^{A-4} Y + \,_2^4\mathrm{He} + Q_\alpha
  $$
- Desintegración Beta Negativa ($\beta^-$ con emisión de antineutrino electrónico):
  $$
  _Z^A X \longrightarrow \,_{Z+1}^A Y + e^- + \bar{\nu}_e + Q_{\beta^-} \quad (n \to p + e^- + \bar{\nu}_e)
  $$
- Desintegración Beta Positiva ($\beta^+$ con emisión de neutrino electrónico):
  $$
  _Z^A X \longrightarrow \,_{Z-1}^A Y + e^+ + \nu_e + Q_{\beta^+} \quad (p \to n + e^+ + \nu_e)
  $$
- Captura Electrónica ($\mathrm{CE}$):
  $$
  _Z^A X + e^- \longrightarrow \,_{Z-1}^A Y + \nu_e + Q_{\mathrm{CE}}
  $$
- Emisión Gamma ($\gamma = \mathrm{fotón nuclear}$):
  $$
  _Z^A X^* \longrightarrow \,_Z^A X + \gamma
  $$
## 19. Física del Estado Sólido y Materia Condensada

### 19.1 Cristalografía y Difracción

- Ley de Bragg para Difracción de Rayos X ($d_{hkl} = \mathrm{espaciado interplanar}$):
  $$
  2 d_{hkl} \sen\theta = n \lambda \quad n \in \mathbb{N}
  $$
- Espaciado Interplanar para Red Cúbica Simple (Parámetro de red $a$):
  $$
  d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}
  $$
- Vectores Primitivos de la Red Recíproca (1):
  $$
  \vec{b}_1 = 2\pi \frac{\vec{a}_2 \times \vec{a}_3}{\vec{a}_1 \cdot (\vec{a}_2 \times \vec{a}_3)}
  $$
- Vectores Primitivos de la Red Recíproca (2):
  $$
  \vec{b}_2 = 2\pi \frac{\vec{a}_3 \times \vec{a}_1}{\vec{a}_1 \cdot (\vec{a}_2 \times \vec{a}_3)}
  $$
- Vectores Primitivos de la Red Recíproca (3):
  $$
  \vec{b}_3 = 2\pi \frac{\vec{a}_1 \times \vec{a}_2}{\vec{a}_1 \cdot (\vec{a}_2 \times \vec{a}_3)}
  $$
- Condición de Difracción de Laue ($\vec{G} = \vec{G}_{hkl} = \mathrm{vector de red recíproca}$) (1):
  $$
  \Delta\vec{k} = \vec{k}' - \vec{k} = \vec{G} \iff 2\vec{k} \cdot \vec{G} + |\vec{G}|^2 = 0 \quad (\mathrm{para dispersión elástica } |\vec{k}'| = |\vec{k}|)
  $$
- Condición de Difracción de Laue ($\vec{G} = \vec{G}_{hkl} = \mathrm{vector de red recíproca}$) (2):
  $$
  \left( \mathrm{O definiendo } \Delta\vec{k} = \vec{k} - \vec{k}' = \vec{G}:
  $$
- Condición de Difracción de Laue ($\vec{G} = \vec{G}_{hkl} = \mathrm{vector de red recíproca}$) (3):
  $$
  2\vec{k} \cdot \vec{G} = |\vec{G}|^2 \right)
  $$
### 19.2 Gas de Electrones Libres de Fermi

- Vector de Onda de Fermi y Momento de Fermi (1):
  $$
  k_F = (3\pi^2 n)^{1/3}
  $$
- Vector de Onda de Fermi y Momento de Fermi (2):
  $$
  p_F = \hbar k_F = \hbar (3\pi^2 n)^{1/3}
  $$
- Vector de Onda de Fermi y Momento de Fermi (3):
  $$
  n = \frac{N}{V}
  $$
- Energía de Fermi a $T = 0\mathrm{ K}$:
  $$
  E_F = \frac{\hbar^2 k_F^2}{2m} = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}
  $$
- Temperatura de fermi:
  $$
  T_F = \frac{E_F}{k_B}
  $$
- Velocidad de fermi:
  $$
  v_F = \frac{\hbar k_F}{m} = \sqrt{\frac{2E_F}{m}}
  $$
- Densidad de Estados Tridimensional ($g(E)$ o $D(E)$):
  $$
  g(E) = \frac{V}{2\pi^2}\left( \frac{2m}{\hbar^2} \right)^{3/2} \sqrt{E} = \frac{3N}{2E_F^{3/2}}\sqrt{E}
  $$
- Capacidad Calorífica Electrónica Lineal ($T \ll T_F$):
  $$
  C_{v,e} = \gamma T = \frac{\pi^2}{2}\left( \frac{k_B T}{E_F} \right) N k_B = \frac{\pi^2}{3} g(E_F) k_B^2 T
  $$
### 19.3 Transporte Electrónico y Térmico

- Conductividad Eléctrica de Drude-Sommerfeld:
  $$
  \sigma = \frac{n e^2 \tau_c}{m}
  $$
- Ley de Wiedemann-Franz (Número de Lorenz $L$) (1):
  $$
  \frac{K}{\sigma} = L T
  $$
- Ley de Wiedemann-Franz (Número de Lorenz $L$) (2):
  $$
  L = \frac{\pi^2}{3}\left( \frac{k_B}{e} \right)^2 \approx 2.44 \times 10^{-8} \, \frac{\mathrm{W}\cdot\Omega}{\mathrm{K}^2}
  $$
