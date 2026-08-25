---
file: docs/fisica/formulario_intermedio.md
description: Compendio didáctico de fórmulas de física de nivel intermedio (vectorial, gravitación, termodinámica).
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/symbols.py
relations:
  - docs/fisica/formulario_fisica.md
  - docs/mates/formulario_intermedio.md
  - docs/ARCHITECTURE.md
keywords:
  - formulas-intermedias-fisica
  - mecanica-vectorial
  - gravitacion
  - termodinamica-intermedia
---

# Compendio I: Mecánica Clásica, de Fluidos y Analítica
*(Nivel Intermedio)*

## 1. Cinemática y Dinámica Newtoniana

### 1.1 Cinemática y Dinámica Vectorial Tridimensional

- Vectores cinemáticos fundamentales (1):
  $$
  \vec{v}(t) = \frac{d\vec{r}}{dt}
  $$
- Vectores cinemáticos fundamentales (2):
  $$
  \vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}
  $$
- Descomposición intrínseca de la aceleración:
  $$
  \vec{a} = a_t \hat{u}_t + a_n \hat{u}_n = \frac{dv}{dt} \hat{u}_t + \frac{v^2}{\rho} \hat{u}_n
  $$
- Coordenadas polares planas (1):
  $$
  \vec{v} = \dot{r} \hat{u}_r + r \dot{\theta} \hat{u}_\theta
  $$
- Coordenadas polares planas (2):
  $$
  \vec{a} = (\ddot{r} - r\dot{\theta}^2)\hat{u}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{u}_\theta
  $$
### 1.2 Sistemas de Referencia No Inerciales (Fuerzas Ficticias)

- Aceleración en sistema móvil ($S'$ con origen acelerado $\vec{A}_0 = \frac{d^2\vec{R}_0}{dt^2}$ respecto al marco inercial $S$, y rotando a $\vec{\omega}$):
  $$
  \vec{a} = \vec{A}_0 + \vec{a}' + \dot{\vec{\omega}} \times \vec{r}' + 2(\vec{\omega} \times \vec{v}') + \vec{\omega} \times (\vec{\omega} \times \vec{r}')
  $$
- Ecuación de movimiento en el sistema no inercial ($S'$):
  $$
  m\vec{a}' = \vec{F}_{\mathrm{real}} - m\vec{A}_0 - m\dot{\vec{\omega}} \times \vec{r}' - 2m(\vec{\omega} \times \vec{v}') - m\vec{\omega} \times (\vec{\omega} \times \vec{r}')
  $$
- Fuerza de Coriolis:
  $$
  \vec{F}_{\mathrm{Coriolis}} = -2m (\vec{\omega} \times \vec{v}')
  $$
- Fuerza Centrífuga:
  $$
  \vec{F}_{\mathrm{centrífuga}} = -m\vec{\omega} \times (\vec{\omega} \times \vec{r}')
  $$
### 1.3 Dinámica Rotacional del Cuerpo Rígido (Eje Fijo)

- Momento de torsión / Torque:
  $$
  \vec{\tau} = \vec{r} \times \vec{F}
  $$
- Momento de inercia:
  $$
  I = \sum_i m_i r_i^2 = \int r^2 dm
  $$
- Ecuación fundamental de la rotación:
  $$
  \sum \tau = I \alpha
  $$
- Teorema de los Ejes Paralelos (Steiner):
  $$
  I = I_{\mathrm{CM}} + M d^2
  $$
- Teorema de los Ejes Perpendiculares (Cuerpos laminares planos en $xy$):
  $$
  I_z = I_x + I_y
  $$
## 2. Trabajo, Energía, Momento Lineal y Gravitación

### 2.1 Mecánica de Sistemas de Partículas

- Trabajo de fuerza variable general:
  $$
  W = \int_{C} \vec{F} \cdot d\vec{r}
  $$
- Campos de fuerza conservativos y Potencial:
  $$
  \vec{F} = -\nabla U = -\left( \frac{\partial U}{\partial x}\hat{i} + \frac{\partial U}{\partial y}\hat{j} + \frac{\partial U}{\partial z}\hat{k} \right)
  $$
- Centro de Masas (CM):
  $$
  \vec{R}_{\mathrm{CM}} = \frac{\sum m_i \vec{r}_i}{\sum m_i} = \frac{1}{M}\int \vec{r} \, dm
  $$
- Teoremas de König (1):
  $$
  E_k = \frac{1}{2} M v_{\mathrm{CM}}^2 + E_k' \quad (\mathrm{traslación CM } + \mathrm{ respecto a CM})
  $$
- Teoremas de König (2):
  $$
  \vec{L} = \vec{R}_{\mathrm{CM}} \times \vec{P}_{\mathrm{total}} + \vec{L}'
  $$
### 2.2 Gravitación Universal y Fuerzas Centrales

- Ley de Gravitación de Newton:
  $$
  \vec{F}_g = -G \frac{m_1 m_2}{r^2} \hat{u}_r
  $$
- Energía Potencial Gravitatoria:
  $$
  U(r) = -G \frac{m_1 m_2}{r}
  $$
- Leyes de Kepler (1):
  $$
  \frac{dA}{dt} = \frac{L}{2m} = \mathrm{constante}
  $$
- Leyes de Kepler (2):
  $$
  T^2 = \left( \frac{4\pi^2}{G(M + m)} \right) a^3
  $$
- Velocidades orbitales:
  $$
  v_{\mathrm{orb}} = \sqrt{\frac{GM}{r}}
  $$
- De escape:
  $$
  v_{\mathrm{esc}} = \sqrt{\frac{2GM}{R}}
  $$
## 3. Oscilaciones y Mecánica de Fluidos

### 3.1 Oscilaciones Amortiguadas y Forzadas

- Oscilador amortiguado ($b = \mathrm{coeficiente de fricción}$) (1):
  $$
  \ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = 0
  $$
- Oscilador amortiguado ($b = \mathrm{coeficiente de fricción}$) (2):
  $$
  \gamma = \frac{b}{2m}
  $$
- Oscilador amortiguado ($b = \mathrm{coeficiente de fricción}$) (3):
  $$
  x(t) = A e^{-\gamma t} \cos(\omega_d t + \phi)
  $$
- Oscilador amortiguado ($b = \mathrm{coeficiente de fricción}$) (4):
  $$
  \omega_d = \sqrt{\omega_0^2 - \gamma^2} \quad (\mathrm{subamortiguado } \gamma < \omega_0)
  $$
- Factor de Calidad $Q$:
  $$
  Q = \frac{\omega_0}{2\gamma}
  $$
- Oscilaciones forzadas con fuerza impulsora $F_0 \cos(\omega t)$ (1):
  $$
  \ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = \frac{F_0}{m} \cos(\omega t)
  $$
- Oscilaciones forzadas con fuerza impulsora $F_0 \cos(\omega t)$ (2):
  $$
  A(\omega) = \frac{F_0 / m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2}}
  $$
### 3.2 Dinámica de Fluidos Ideales

- Ecuación de Continuidad (Flujo estacionario e incompresible 1D a través de secciones transversales) (1):
  $$
  A_1 v_1 = A_2 v_2 = Q \quad (\mathrm{Caudal volumétrico constante})
  $$
- Ecuación de Continuidad (Flujo estacionario e incompresible 1D a través de secciones transversales) (2):
  $$
  \left( \mathrm{Para flujo compresible estacionario: } \rho_1 A_1 v_1 = \rho_2 A_2 v_2 = \dot{m} = \mathrm{constante} \right)
  $$
- Ecuación de Bernoulli:
  $$
  P_1 + \frac{1}{2}\rho v_1^2 + \rho g z_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g z_2 = \mathrm{constante}
  $$
- Teorema de Torricelli:
  $$
  v = \sqrt{2gh}
  $$
## 4. Mecánica Analítica y Relativista

### 4.1 Mecánica Lagrangiana

- Coordenadas generalizadas (1):
  $$
  q = (q_1, q_2, \dots, q_n)
  $$
- Coordenadas generalizadas (2):
  $$
  \dot{q} = (\dot{q}_1, \dot{q}_2, \dots, \dot{q}_n)
  $$
- Función Lagrangiana:
  $$
  L(q, \dot{q}, t) = T(q, \dot{q}, t) - V(q, t)
  $$
- Principio de Mínima Acción de Hamilton:
  $$
  \delta S = \delta \int_{t_1}^{t_2} L(q, \dot{q}, t) dt = 0
  $$
- Ecuaciones de Euler-Lagrange (1):
  $$
  \frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}_j} \right) - \frac{\partial L}{\partial q_j} = 0
  $$
- Ecuaciones de Euler-Lagrange (2):
  $$
  j = 1, \dots, n
  $$
- Momento conjugado o canónico:
  $$
  p_j = \frac{\partial L}{\partial \dot{q}_j}
  $$
- Teorema de Noether:
  $$
  \mathrm{Si } \frac{\partial L}{\partial q_j} = 0 \implies p_j = \mathrm{constante de movimiento}
  $$
### 4.2 Mecánica Hamiltoniana

- Función Hamiltoniana (Transformada de Legendre):
  $$
  H(q, p, t) = \sum_{j=1}^n p_j \dot{q}_j - L(q, \dot{q}, t)
  $$
- Ecuaciones Canónicas de Hamilton (1):
  $$
  \dot{q}_j = \frac{\partial H}{\partial p_j}
  $$
- Ecuaciones Canónicas de Hamilton (2):
  $$
  \dot{p}_j = -\frac{\partial H}{\partial q_j}
  $$
- Variación temporal del Hamiltoniano:
  $$
  \frac{dH}{dt} = \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t}
  $$
# Compendio II: Oscilaciones y Ondas Mecánicas
*(Nivel Intermedio)*

## 5. Movimiento Oscilatorio (Oscilaciones)

### 5.1 Péndulos Compuestos y de Torsión

- Péndulo Físico (Centro de masa a distancia $d$ del eje de giro) (1):
  $$
  \omega_0 = \sqrt{\frac{m g d}{I}}
  $$
- Péndulo Físico (Centro de masa a distancia $d$ del eje de giro) (2):
  $$
  T = 2\pi\sqrt{\frac{I}{m g d}}
  $$
- Péndulo de Torsión (Constante de torsión $\kappa$) (1):
  $$
  \tau = -\kappa \theta \implies \omega_0 = \sqrt{\frac{\kappa}{I}}
  $$
- Péndulo de Torsión (Constante de torsión $\kappa$) (2):
  $$
  T = 2\pi\sqrt{\frac{I}{\kappa}}
  $$
### 5.2 Oscilaciones Amortiguadas

- Ecuación Diferencial Fundamental ($b = \mathrm{coeficiente de amortiguamiento viscoso}$) (1):
  $$
  m \ddot{x} + b \dot{x} + k x = 0 \implies \ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = 0
  $$
- Ecuación Diferencial Fundamental ($b = \mathrm{coeficiente de amortiguamiento viscoso}$) (2):
  $$
  \gamma = \frac{b}{2m}
  $$
- Ecuación Diferencial Fundamental ($b = \mathrm{coeficiente de amortiguamiento viscoso}$) (3):
  $$
  \omega_0 = \sqrt{\frac{k}{m}}
  $$
- Régimen Subamortiguado ($\gamma < \omega_0$) (1):
  $$
  x(t) = A_0 e^{-\gamma t} \cos(\omega_d t + \phi)
  $$
- Régimen Subamortiguado ($\gamma < \omega_0$) (2):
  $$
  \omega_d = \sqrt{\omega_0^2 - \gamma^2}
  $$
- Régimen Críticamente Amortiguado ($\gamma = \omega_0$):
  $$
  x(t) = (C_1 + C_2 t) e^{-\gamma t}
  $$
- Régimen Sobreamortiguado ($\gamma > \omega_0$):
  $$
  x(t) = C_1 e^{-(\gamma - \sqrt{\gamma^2 - \omega_0^2})t} + C_2 e^{-(\gamma + \sqrt{\gamma^2 - \omega_0^2})t}
  $$
- Decremento Logarítmico ($\delta$):
  $$
  \delta = \ln\left( \frac{x(t)}{x(t + T_d)} \right) = \gamma T_d = \frac{2\pi \gamma}{\omega_d}
  $$
- Factor de Calidad ($Q$):
  $$
  Q = \frac{\omega_0}{2\gamma} = \frac{\pi}{\delta} = 2\pi \frac{E}{\Delta E_{\mathrm{ciclo}}}
  $$
### 5.3 Oscilaciones Forzadas y Resonancia

- Ecuación Diferencial con Excitación Armónica:
  $$
  \ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = \frac{F_0}{m} \cos(\omega t)
  $$
- Solución de Estado Estacionario ($x_p(t) = A(\omega) \cos(\omega t - \delta)$) (1):
  $$
  A(\omega) = \frac{F_0 / m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2}}
  $$
- Solución de Estado Estacionario ($x_p(t) = A(\omega) \cos(\omega t - \delta)$) (2):
  $$
  \tan(\delta) = \frac{2\gamma \omega}{\omega_0^2 - \omega^2}
  $$
- Frecuencia de Resonancia de Amplitud:
  $$
  \omega_{\mathrm{res}} = \sqrt{\omega_0^2 - 2\gamma^2}
  $$
- Potencia Media Absorbida por el Oscilador:
  $$
  \langle P(\omega) \rangle = \frac{F_0^2 \gamma \omega^2}{m [(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2]}
  $$
## 6. Ondas Mecánicas en Medios Continuos

### 6.1 Ecuación Diferencial de Onda 1D (d'Alembert)

- Forma canónica:
  $$
  \frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}
  $$
- Solución General de d'Alembert:
  $$
  y(x, t) = f(x - vt) + g(x + vt)
  $$
### 6.2 Velocidad de Propagación en Medios Elásticos

- Cuerda Tensa (Tensión $T$, densidad lineal de masa $\mu = m/L$):
  $$
  v = \sqrt{\frac{T}{\mu}}
  $$
- Barra Sólida (Ondas longitudinales, módulo de Young $Y$, densidad $\rho$):
  $$
  v = \sqrt{\frac{Y}{\rho}}
  $$
- Fluido / Gas (Módulo de compresibilidad volumétrica $B$):
  $$
  v = \sqrt{\frac{B}{\rho}}
  $$
- Gas Ideal (Ecuación de Newton-Laplace para proceso adiabático):
  $$
  v = \sqrt{\frac{\gamma R T}{M}} = \sqrt{\frac{\gamma P}{\rho}}
  $$
### 6.3 Transporte de Energía e Intensidad

- Densidad Lineal de Energía Mecánica Total:
  $$
  \frac{dE}{dx} = \mu \omega^2 A^2 \cos^2(kx - \omega t)
  $$
- Potencia Instantánea Transmitida en Cuerda:
  $$
  P(x, t) = -T \left( \frac{\partial y}{\partial x} \right) \left( \frac{\partial y}{\partial t} \right) = \sqrt{\mu T} \, \omega^2 A^2 \cos^2(kx - \omega t)
  $$
- Potencia Promedio Transmitida:
  $$
  \langle P \rangle = \frac{1}{2} \mu v \omega^2 A^2 = \frac{1}{2} \sqrt{\mu T} \, \omega^2 A^2
  $$
- Intensidad de Onda ($I$):
  $$
  I = \frac{\langle P \rangle}{\mathrm{Área}} = \frac{1}{2} \rho v \omega^2 A^2
  $$
- Ley del Inverso del Cuadrado (Fuente puntual isótropa en medio no disipativo):
  $$
  I(r) = \frac{P_{\mathrm{fuente}}}{4\pi r^2} \implies \frac{I_1}{I_2} = \frac{r_2^2}{r_1^2}
  $$
## 7. Interferencia, Ondas Estacionarias y Acústica

### 7.1 Ondas Estacionarias Unidimensionales

- Ecuación Analítica:
  $$
  y(x, t) = [2A \sen(kx)] \cos(\omega t)
  $$
- Posición de Nodos (Amplitud nula) (1):
  $$
  \sen(kx) = 0 \implies x_n = n \frac{\lambda}{2}
  $$
- Posición de Nodos (Amplitud nula) (2):
  $$
  n = 0, 1, 2, \dots
  $$
- Posición de antinodos:
  $$
  |\sen(kx)| = 1 \implies x_a = \left( n + \frac{1}{2} \right) \frac{\lambda}{2}
  $$
- Vientres (amplitud máxima $2a$):
  $$
  n = 0, 1, 2, \dots
  $$
### 7.2 Modos Normales y Frecuencias Resonantes en Sistemas Acotados

- Cuerda Fija en Ambos Extremos o Tubo Abierto-Abierto (1):
  $$
  \lambda_n = \frac{2L}{n}
  $$
- Cuerda Fija en Ambos Extremos o Tubo Abierto-Abierto (2):
  $$
  f_n = n \frac{v}{2L} = n f_1
  $$
- Cuerda Fija en Ambos Extremos o Tubo Abierto-Abierto (3):
  $$
  n = 1, 2, 3, \dots
  $$
- Cuerda con un extremo fijo:
  $$
  \lambda_n = \frac{4L}{2n - 1}
  $$
- Uno libre:
  $$
  f_n = (2n - 1) \frac{v}{4L} = (2n - 1) f_1
  $$
- Tubo abierto-cerrado:
  $$
  n = 1, 2, 3, \dots
  $$
### 7.3 Efecto Doppler Clásico (Velocidad del sonido $v$)

- Fórmula General (1):
  $$
  f_o = f_s \left( \frac{v \pm v_o}{v \mp v_s} \right)
  $$
- Fórmula General (2):
  $$
  \mathrm{Signo superior: acercamiento} \quad | \quad \mathrm{Signo inferior: alejamiento}
  $$
### 7.4 Ondas de Choque y Cono de Mach

- Ángulo de Mach ($\theta_M$) (1):
  $$
  \sen(\theta_M) = \frac{v}{v_s} = \frac{1}{M}
  $$
- Ángulo de Mach ($\theta_M$) (2):
  $$
  M = \frac{v_s}{v} > 1
  $$
# Compendio III: Termodinámica Clásica, Química y Estadística
*(Nivel Intermedio)*

## 8. Conceptos Fundamentales, Gases y Ecuaciones de Estado

### 8.1 Mezclas de Gases y Propiedades Molares

- Ley de Dalton de las Presiones Parciales (1):
  $$
  P_{\mathrm{total}} = \sum_{i=1}^k P_i
  $$
- Ley de Dalton de las Presiones Parciales (2):
  $$
  P_i = x_i P_{\mathrm{total}}
  $$
- Ley de Dalton de las Presiones Parciales (3):
  $$
  x_i = \frac{n_i}{n_{\mathrm{total}}}
  $$
- Ley de Amagat de los Volúmenes Parciales (1):
  $$
  V_{\mathrm{total}} = \sum_{i=1}^k V_i
  $$
- Ley de Amagat de los Volúmenes Parciales (2):
  $$
  V_i = x_i V_{\mathrm{total}}
  $$
- Masa molar aparente de una mezcla:
  $$
  \bar{M} = \sum_{i=1}^k x_i M_i
  $$
### 8.2 Coeficientes Termoelásticos

- Coeficiente de Dilatación Térmica Isobárica ($\alpha$ o $\beta$):
  $$
  \alpha = \frac{1}{V} \left( \frac{\partial V}{\partial T} \right)_P
  $$
- Compresibilidad Isotérmica ($\kappa_T$ o $\beta_T$):
  $$
  \kappa_T = -\frac{1}{V} \left( \frac{\partial V}{\partial P} \right)_T
  $$
- Compresibilidad Adiabática / Isentrópica ($\kappa_S$):
  $$
  \kappa_S = -\frac{1}{V} \left( \frac{\partial V}{\partial P} \right)_S
  $$
- Coeficiente Piezométrico / Tensión Térmica ($\beta_P$):
  $$
  \beta_P = \frac{1}{P} \left( \frac{\partial P}{\partial T} \right)_V = \frac{\alpha}{P \kappa_T}
  $$
### 8.3 Ecuaciones de Estado para Gases Reales

- Ecuación de Van der Waals:
  $$
  \left( P + \frac{a n^2}{V^2} \right)(V - n b) = n R T \iff \left( P + \frac{a}{V_m^2} \right)(V_m - b) = R T
  $$
- Constantes Críticas de Van der Waals (1):
  $$
  T_c = \frac{8a}{27Rb}
  $$
- Constantes Críticas de Van der Waals (2):
  $$
  P_c = \frac{a}{27b^2}
  $$
- Constantes Críticas de Van der Waals (3):
  $$
  V_{m,c} = 3b
  $$
- Factor de Compresibilidad Crítico de Van der Waals:
  $$
  Z_c = \frac{P_c V_{m,c}}{R T_c} = \frac{3}{8} = 0.375
  $$
- Ecuación Reducida de Van der Waals ($P_r = P/P_c, \, T_r = T/T_c, \, V_r = V_m/V_{m,c}$):
  $$
  \left( P_r + \frac{3}{V_r^2} \right)(3V_r - 1) = 8T_r
  $$
- Factor de Compresibilidad y Expansión Virial:
  $$
  Z = \frac{P V_m}{R T} = 1 + \frac{B(T)}{V_m} + \frac{C(T)}{V_m^2} + \dots = 1 + B'(T)P + C'(T)P^2 + \dots
  $$
## 9. Primera y Segunda Ley de la Termodinámica

### 9.1 Procesos Politrópicos ($P V^n = \mathrm{constante}$)

- Trabajo:
  $$
  W = \frac{P_f V_f - P_i V_i}{1 - n} = \frac{n R (T_f - T_i)}{1 - n} \quad (n \neq 1)
  $$
- Capacidad Calorífica Politrópica:
  $$
  C_n = C_v + \frac{R}{1 - n} = C_v \left( \frac{n - \gamma}{n - 1} \right)
  $$
### 9.2 Segunda Ley de la Termodinámica y Entropía

- Definición de Entropía (Clausius):
  $$
  dS = \frac{\delta Q_{\mathrm{rev}}}{T} \implies \Delta S = \int_i^f \frac{\delta Q_{\mathrm{rev}}}{T}
  $$
- Desigualdad de Clausius:
  $$
  \oint \frac{\delta Q}{T} \le 0 \quad (\mathrm{igualdad para ciclos reversibles})
  $$
- Principio del Incremento de Entropía:
  $$
  \Delta S_{\mathrm{universo}} = \Delta S_{\mathrm{sistema}} + \Delta S_{\mathrm{entorno}} \ge 0
  $$
- Variación de Entropía en un Gas Ideal:
  $$
  \Delta S = n C_v \ln\left( \frac{T_f}{T_i} \right) + n R \ln\left( \frac{V_f}{V_i} \right) = n C_p \ln\left( \frac{T_f}{T_i} \right) - n R \ln\left( \frac{P_f}{P_i} \right)
  $$
- Variación de Entropía en Sustancias Incompresibles (Líquidos/Sólidos):
  $$
  \Delta S = m c \ln\left( \frac{T_f}{T_i} \right)
  $$
- Entropía de Mezcla de Gases Ideales:
  $$
  \Delta S_{\mathrm{mezcla}} = -n_{\mathrm{total}} R \sum_{i=1}^k x_i \ln(x_i)
  $$
### 9.3 Máquinas Térmicas, Refrigeradores y Ciclos de Potencia

- Eficiencia Térmica General de una Máquina Térmica:
  $$
  \eta = \frac{W_{\mathrm{neto}}}{Q_H} = \frac{Q_H - |Q_C|}{Q_H} = 1 - \frac{|Q_C|}{Q_H}
  $$
- Eficiencia de Carnot (Límite máximo entre dos focos):
  $$
  \eta_{\mathrm{Carnot}} = 1 - \frac{T_C}{T_H}
  $$
- Coeficiente de Desempeño de Refrigeradores ($\mathrm{COP}_R$):
  $$
  \mathrm{COP}_R = \beta = \frac{Q_C}{W_{\mathrm{neto}}} = \frac{Q_C}{Q_H - Q_C} \implies \mathrm{COP}_{R,\mathrm{Carnot}} = \frac{T_C}{T_H - T_C}
  $$
- Coeficiente de Desempeño de Bombas de Calor ($\mathrm{COP}_{\mathrm{HP}}$):
  $$
  \mathrm{COP}_{\mathrm{HP}} = \gamma' = \frac{Q_H}{W_{\mathrm{neto}}} = \mathrm{COP}_R + 1 \implies \mathrm{COP}_{\mathrm{HP},\mathrm{Carnot}} = \frac{T_H}{T_H - T_C}
  $$
- Ciclo Otto de Aire Estándar (Relación de compresión $r = V_{\mathrm{máx}}/V_{\mathrm{mín}}$):
  $$
  \eta_{\mathrm{Otto}} = 1 - \frac{1}{r^{\gamma - 1}}
  $$
- Ciclo Diesel (Relación de corte de admisión $r_c = V_3/V_2$):
  $$
  \eta_{\mathrm{Diesel}} = 1 - \frac{1}{r^{\gamma - 1}} \left[ \frac{r_c^\gamma - 1}{\gamma(r_c - 1)} \right]
  $$
- Ciclo Brayton / Joule (Relación de presiones $r_p = P_2/P_1$):
  $$
  \eta_{\mathrm{Brayton}} = 1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}}
  $$
## 10. Potenciales Termodinámicos y Relaciones de Maxwell

### 10.1 Ecuaciones Fundamentales y Potenciales Termodinámicos

- Energía Interna $U(S, V, N)$:
  $$
  dU = T dS - P dV + \sum_{i=1}^k \mu_i dN_i
  $$
- Entalpía $H(S, P, N) = U + PV$:
  $$
  dH = T dS + V dP + \sum_{i=1}^k \mu_i dN_i
  $$
- Energía Libre de Helmholtz $A(T, V, N) = F = U - TS$:
  $$
  dA = -S dT - P dV + \sum_{i=1}^k \mu_i dN_i
  $$
- Energía Libre de Gibbs $G(T, P, N) = H - TS$:
  $$
  dG = -S dT + V dP + \sum_{i=1}^k \mu_i dN_i
  $$
- Gran Potencial Termodinámico / Potencial Gran Canónico ($\Omega = \Phi_G(T, V, \mu) = U - TS - \mu N = -PV$):
  $$
  d\Omega = -S dT - P dV - N d\mu
  $$
### 10.2 Relaciones de Maxwell

- A partir de $dU$:
  $$
  \left( \frac{\partial T}{\partial V} \right)_S = -\left( \frac{\partial P}{\partial S} \right)_V
  $$
- A partir de $dH$:
  $$
  \left( \frac{\partial T}{\partial P} \right)_S = \left( \frac{\partial V}{\partial S} \right)_P
  $$
- A partir de $dA$:
  $$
  \left( \frac{\partial S}{\partial V} \right)_T = \left( \frac{\partial P}{\partial T} \right)_V
  $$
- A partir de $dG$:
  $$
  \left( \frac{\partial S}{\partial P} \right)_T = -\left( \frac{\partial V}{\partial T} \right)_P
  $$
### 10.3 Ecuaciones $T dS$ y Propiedades de Calores Específicos

- Primera Ecuación $T dS$:
  $$
  T dS = C_v dT + T \left( \frac{\partial P}{\partial T} \right)_V dV = C_v dT + \frac{T \alpha}{\kappa_T} dV
  $$
- Segunda Ecuación $T dS$:
  $$
  T dS = C_p dT - T \left( \frac{\partial V}{\partial T} \right)_P dP = C_p dT - T V \alpha dP
  $$
- Relación General $C_p - C_v$:
  $$
  C_p - C_v = T \left( \frac{\partial P}{\partial T} \right)_V \left( \frac{\partial V}{\partial T} \right)_P = \frac{T V \alpha^2}{\kappa_T}
  $$
- Relación de Compresibilidades:
  $$
  \frac{C_p}{C_v} = \frac{\kappa_T}{\kappa_S} = \gamma
  $$
# Compendio IV: Electricidad y Magnetismo
*(Nivel Intermedio)*

## 11. Electrostática y Medios Dieléctricos

### 11.1 Distribuciones Continuas de Carga

- Campo eléctrico para distribución volumétrica continua (1):
  $$
  \vec{E}(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \int_V \frac{\rho(\vec{r}')(\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} \, dV'
  $$
- Campo eléctrico para distribución volumétrica continua (2):
  $$
  \left( \mathrm{Superficial: } \vec{E}(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \int_S \frac{\sigma(\vec{r}')(\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} \, dA'
  $$
- Campo eléctrico para distribución volumétrica continua (3):
  $$
  \mathrm{Lineal: } \vec{E}(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \int_C \frac{\lambda(\vec{r}')(\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} \, d\ell' \right)
  $$
- Potencial eléctrico continuo:
  $$
  V(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \int_V \frac{\rho(\vec{r}')}{|\vec{r} - \vec{r}'|} \, dV'
  $$
### 11.2 Ley de Gauss en Forma Integral

- Flujo Eléctrico ($\Phi_E$):
  $$
  \Phi_E = \iint_S \vec{E} \cdot d\vec{A}
  $$
- Ley de Gauss:
  $$
  \Phi_E = \oiint_{\partial V} \vec{E} \cdot d\vec{A} = \frac{Q_{\mathrm{enc}}}{\varepsilon_0}
  $$
### 11.3 Relación Diferencial entre Campo y Potencial

- Campo como gradiente del potencial:
  $$
  \vec{E} = -\nabla V = -\left( \frac{\partial V}{\partial x}\hat{i} + \frac{\partial V}{\partial y}\hat{j} + \frac{\partial V}{\partial z}\hat{k} \right)
  $$
- Diferencia de potencial por integral de línea:
  $$
  V_B - V_A = -\int_A^B \vec{E} \cdot d\vec{\ell}
  $$
### 11.4 Dipolo Eléctrico

- Momento dipolar eléctrico:
  $$
  \vec{p} = q \vec{d}
  $$
- Potencial de un dipolo puntual en el origen:
  $$
  V(r, \theta) = \frac{1}{4\pi\varepsilon_0} \frac{\vec{p} \cdot \hat{r}}{r^2} = \frac{1}{4\pi\varepsilon_0} \frac{p \cos\theta}{r^2}
  $$
- Campo eléctrico del dipolo:
  $$
  \vec{E}(r, \theta) = \frac{1}{4\pi\varepsilon_0 r^3} \left[ 3(\vec{p} \cdot \hat{r})\hat{r} - \vec{p} \right] = \frac{p}{4\pi\varepsilon_0 r^3} (2\cos\theta \hat{u}_r + \sen\theta \hat{u}_\theta)
  $$
- Torque y energía de un dipolo en campo externo (1):
  $$
  \vec{\tau} = \vec{p} \times \vec{E}
  $$
- Torque y energía de un dipolo en campo externo (2):
  $$
  U = -\vec{p} \cdot \vec{E}
  $$
- Torque y energía de un dipolo en campo externo (3):
  $$
  \vec{F} = (\vec{p} \cdot \nabla)\vec{E}
  $$
### 11.5 Dieléctricos y Polarización

- Vector Desplazamiento Eléctrico ($\vec{D}$):
  $$
  \vec{D} = \varepsilon_0 \vec{E} + \vec{P} = \varepsilon \vec{E} = \varepsilon_0 \varepsilon_r \vec{E}
  $$
- Vector polarización ($\vec{p}$):
  $$
  \vec{P} = \varepsilon_0 \chi_e \vec{E}
  $$
- Susceptibilidad eléctrica ($\chi_e$):
  $$
  \varepsilon_r = 1 + \chi_e
  $$
- Densidades de Carga Ligada / Polarización (1):
  $$
  \rho_b = -\nabla \cdot \vec{P}
  $$
- Densidades de Carga Ligada / Polarización (2):
  $$
  \sigma_b = \vec{P} \cdot \hat{n}
  $$
- Densidad volumétrica de energía electrostática:
  $$
  u_e = \frac{1}{2} \vec{D} \cdot \vec{E} = \frac{1}{2} \varepsilon E^2
  $$
## 12. Electrodinámica, Corriente y Circuitos Eléctricos

### 12.1 Densidad de Corriente y Ley de Ohm Microscópica

- Densidad de corriente ($\vec{J}$) (1):
  $$
  \vec{J} = n q \vec{v}_d
  $$
- Densidad de corriente ($\vec{J}$) (2):
  $$
  I = \iint_S \vec{J} \cdot d\vec{A}
  $$
- Ley de Ohm Puntual / Microscópica:
  $$
  \vec{J} = \sigma_c \vec{E} = \frac{1}{\rho_e} \vec{E}
  $$
- Modelo de Drude para la conductividad:
  $$
  \sigma_c = \frac{n q^2 \tau_c}{m_e}
  $$
### 12.2 Leyes de Kirchhoff

- Ley de Corrientes de Kirchhoff (Nodos - Conservación de carga):
  $$
  \sum_{k=1}^n I_k = 0
  $$
- Ley de Voltajes de Kirchhoff (Mallas - Conservación de energía):
  $$
  \sum_{k=1}^m V_k = \sum_{k=1}^m \mathcal{E}_k - \sum_{k=1}^m I_k R_k = 0
  $$
### 12.3 Circuitos Transitorios de Primer Orden en Corriente Continua (DC)

- Circuito RC - Carga del Condensador ($\tau = RC$) (1):
  $$
  q(t) = C\mathcal{E} (1 - e^{-t/\tau})
  $$
- Circuito RC - Carga del Condensador ($\tau = RC$) (2):
  $$
  i(t) = \frac{\mathcal{E}}{R} e^{-t/\tau}
  $$
- Circuito RC - Carga del Condensador ($\tau = RC$) (3):
  $$
  V_C(t) = \mathcal{E}(1 - e^{-t/\tau})
  $$
- Circuito RC - Descarga del Condensador (1):
  $$
  q(t) = Q_0 e^{-t/\tau}
  $$
- Circuito RC - Descarga del Condensador (2):
  $$
  i(t) = -\frac{Q_0}{\tau} e^{-t/\tau}
  $$
- Circuito RC - Descarga del Condensador (3):
  $$
  V_C(t) = V_0 e^{-t/\tau}
  $$
- Circuito RL - Crecimiento de Corriente ($\tau = L/R$) (1):
  $$
  i(t) = \frac{\mathcal{E}}{R} (1 - e^{-t/\tau})
  $$
- Circuito RL - Crecimiento de Corriente ($\tau = L/R$) (2):
  $$
  V_L(t) = \mathcal{E} e^{-t/\tau}
  $$
- Circuito RL - Decaimiento de Corriente:
  $$
  i(t) = I_0 e^{-t/\tau}
  $$
## 13. Magnetostática y Materia Magnética

### 13.1 Ley de Biot-Savart

- Campo magnético de un elemento de corriente:
  $$
  d\vec{B} = \frac{\mu_0 I}{4\pi} \frac{d\vec{\ell} \times \hat{r}}{r^2} = \frac{\mu_0 I}{4\pi} \frac{d\vec{\ell} \times (\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3}
  $$
- Campo de un conductor rectilíneo infinito:
  $$
  B = \frac{\mu_0 I}{2\pi R}
  $$
- Campo en el eje de una espira circular (radio $R$, distancia $z$):
  $$
  B(z) = \frac{\mu_0 I R^2}{2(R^2 + z^2)^{3/2}}
  $$
### 13.2 Ley de Ampère y Flujo Magnético

- Ley de Ampère en forma integral:
  $$
  \oint_C \vec{B} \cdot d\vec{\ell} = \mu_0 I_{\mathrm{enc}}
  $$
- Campo en el interior de un solenoide ideal ($n = N/L$):
  $$
  B = \mu_0 n I
  $$
- Campo en el interior de un toroide (radio medio $r$):
  $$
  B = \frac{\mu_0 N I}{2\pi r}
  $$
- Flujo Magnético ($\Phi_B$):
  $$
  \Phi_B = \iint_S \vec{B} \cdot d\vec{A}
  $$
- Ley de Gauss para el Magnetismo (No existencia de monopolos magnéticos aislados):
  $$
  \oiint_{\partial V} \vec{B} \cdot d\vec{A} = 0
  $$
### 13.3 Efecto Hall

- Voltaje hall en un conductor rectangular (ancho $w$:
  $$
  V_H = \frac{I B}{n q d} = R_H \frac{I B}{d}
  $$
- Espesor $d$):
  $$
  R_H = \frac{1}{n q} \quad (\mathrm{Coeficiente de Hall})
  $$
### 13.4 Medios Magnéticos y Magnetización

- Vector Intensidad Magnética ($\vec{H}$):
  $$
  \vec{H} = \frac{1}{\mu_0}\vec{B} - \vec{M} \implies \vec{B} = \mu_0 (\vec{H} + \vec{M}) = \mu \vec{H} = \mu_0 \mu_r \vec{H}
  $$
- Vector magnetización ($\vec{m}$):
  $$
  \vec{M} = \chi_m \vec{H}
  $$
- Susceptibilidad magnética ($\chi_m$):
  $$
  \mu_r = 1 + \chi_m
  $$
- Corrientes de Magnetización / Amperianas (1):
  $$
  \vec{J}_b = \nabla \times \vec{M}
  $$
- Corrientes de Magnetización / Amperianas (2):
  $$
  \vec{K}_b = \vec{M} \times \hat{n}
  $$
## 14. Inducción Electromagnética, Maxwell y Ondas

### 14.1 Ley de Ampère-Maxwell y Corriente de Desplazamiento

- Densidad de corriente de desplazamiento (Forma general macroscópica / Vacío) (1):
  $$
  \vec{J}_d = \frac{\partial \vec{D}}{\partial t} \quad (\mathrm{General})
  $$
- Densidad de corriente de desplazamiento (Forma general macroscópica / Vacío) (2):
  $$
  \vec{J}_d = \varepsilon \frac{\partial \vec{E}}{\partial t} \quad (\mathrm{Medio lineal})
  $$
- Densidad de corriente de desplazamiento (Forma general macroscópica / Vacío) (3):
  $$
  \vec{J}_d = \varepsilon_0 \frac{\partial \vec{E}}{\partial t} \quad (\mathrm{Vacío})
  $$
- Corriente de desplazamiento total:
  $$
  I_d = \iint_S \vec{J}_d \cdot d\vec{A} = \frac{d\Phi_D}{dt} = \varepsilon_0 \frac{d\Phi_E}{dt} \quad (\mathrm{en el vacío})
  $$
### 14.2 Ecuaciones de Maxwell en Forma Integral (Medios Lineales Generales)

- Ley de Gauss para el campo eléctrico (1):
  $$
  \oiint_{\partial V} \vec{D} \cdot d\vec{A} = Q_{f,\mathrm{enc}}
  $$
- Ley de Gauss para el campo eléctrico (2):
  $$
  \left( \oiint_{\partial V} \vec{E} \cdot d\vec{A} = \frac{Q_{\mathrm{enc}}}{\varepsilon_0} \right)
  $$
- Ley de Gauss para el campo magnético:
  $$
  \oiint_{\partial V} \vec{B} \cdot d\vec{A} = 0
  $$
- Ley de Faraday de la Inducción:
  $$
  \oint_C \vec{E} \cdot d\vec{\ell} = -\frac{d}{dt} \iint_S \vec{B} \cdot d\vec{A}
  $$
- Ley de Ampère-Maxwell:
  $$
  \oint_C \vec{H} \cdot d\vec{\ell} = I_{f,\mathrm{enc}} + \frac{d}{dt} \iint_S \vec{D} \cdot d\vec{A}
  $$
### 14.3 Teorema de Poynting y Transporte de Energía

- Vector de Poynting ($\vec{S}$) (1):
  $$
  \vec{S} = \vec{E} \times \vec{H} \quad (\mathrm{Medio material})
  $$
- Vector de Poynting ($\vec{S}$) (2):
  $$
  \vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B}) \quad (\mathrm{Vacío e isótropo})
  $$
- Densidad volumétrica total de energía electromagnética (1):
  $$
  u = \frac{1}{2} (\vec{D} \cdot \vec{E} + \vec{B} \cdot \vec{H}) \quad (\mathrm{Medio lineal})
  $$
- Densidad volumétrica total de energía electromagnética (2):
  $$
  u = \frac{1}{2} \left( \varepsilon_0 E^2 + \frac{1}{\mu_0} B^2 \right) \quad (\mathrm{Vacío})
  $$
- Teorema de Poynting Diferencial (Balance de Potencia):
  $$
  \nabla \cdot \vec{S} + \frac{\partial u}{\partial t} = -\vec{J} \cdot \vec{E}
  $$
- Intensidad de Onda Electromagnética ($\langle S \rangle$):
  $$
  I = \langle |\vec{S}| \rangle = \frac{1}{2} \varepsilon_0 c E_0^2 = \frac{E_0^2}{2 \mu_0 c} = \frac{E_0 B_0}{2\mu_0}
  $$
# Compendio V: Óptica y Luz
*(Nivel Intermedio)*

## 15. Óptica Geométrica y Sistemas Ópticos

### 15.1 Dioptrios Esféricos y Lentes Delgadas

- Refracción en un Dioptrio Esférico:
  $$
  \frac{n_1}{s_o} + \frac{n_2}{s_i} = \frac{n_2 - n_1}{R}
  $$
- Fórmula del Fabricante de Lentes (Lente delgada en el aire $n_{\mathrm{medio}} = 1$):
  $$
  \frac{1}{f} = (n - 1)\left( \frac{1}{R_1} - \frac{1}{R_2} + \frac{(n - 1)d}{n R_1 R_2} \right) \xrightarrow{d \to 0} (n - 1)\left( \frac{1}{R_1} - \frac{1}{R_2} \right)
  $$
- Ecuación de Gauss para Lentes Delgadas:
  $$
  \frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f}
  $$
- Forma Newtoniana de la Ecuación de Lentes ($x_o = s_o - f, \, x_i = s_i - f$):
  $$
  x_o \cdot x_i = f^2
  $$
- Potencia Óptica ($P$ en dioptrías $\mathrm{m}^{-1}$):
  $$
  P = \frac{1}{f}
  $$
- Lentes Delgadas en Contacto:
  $$
  P_{\mathrm{eq}} = \sum_{i=1}^N P_i \implies \frac{1}{f_{\mathrm{eq}}} = \frac{1}{f_1} + \frac{1}{f_2} + \dots + \frac{1}{f_N}
  $$
- Lentes Separadas por una Distancia $d$:
  $$
  \frac{1}{f_{\mathrm{eq}}} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 f_2}
  $$
### 15.2 Prismas y Dispersión Cromática

- Desviación Angular en un Prisma de Ángulo de Ápice $A$:
  $$
  \delta = \theta_1 + \theta_2' - A
  $$
- Ángulo de Mínima Desviación ($\delta_{\min}$):
  $$
  n = \frac{\sen\left( \frac{A + \delta_{\min}}{2} \right)}{\sen\left( \frac{A}{2} \right)}
  $$
- Número de Abbe / Potencia Dispersiva ($V_d$):
  $$
  V_d = \frac{n_d - 1}{n_F - n_C}
  $$
## 16. Óptica Ondulatoria (Interferencia, Difracción y Polarización)

### 16.1 Distribución de Intensidad en Interferencia

- Superposición de Dos Ondas Armónicas Coherentes:
  $$
  I = I_1 + I_2 + 2\sqrt{I_1 I_2} \cos(\delta)
  $$
- Diferencia de Fase ($\delta$) por Diferencia de Camino Óptico ($\Delta r$):
  $$
  \delta = k \Delta r + \Delta\phi_0 = \frac{2\pi}{\lambda} \Delta r + \Delta\phi_0
  $$
- Visibilidad o Contraste de Franjas:
  $$
  \mathcal{V} = \frac{I_{\mathrm{máx}} - I_{\mathrm{mín}}}{I_{\mathrm{máx}} + I_{\mathrm{mín}}} = \frac{2\sqrt{I_1 I_2}}{I_1 + I_2}
  $$
### 16.2 Interferencia en Películas Delgadas (Espesor $t$, incidencia casi normal)

- Condición de Interferencia Constructiva (Reflexión) (1):
  $$
  2 n t = \left( m + \frac{1}{2} \right)\lambda \quad (\mathrm{con un solo cambio de fase de } \pi)
  $$
- Condición de Interferencia Constructiva (Reflexión) (2):
  $$
  2 n t = m \lambda \quad (\mathrm{con } 0 \mathrm{ o } 2 \mathrm{ cambios de fase de } \pi)
  $$
- Anillos de Newton (Radio del $m$-ésimo anillo brillante/oscuro por reflexión) (1):
  $$
  r_{\mathrm{oscuro}} = \sqrt{m \lambda R}
  $$
- Anillos de Newton (Radio del $m$-ésimo anillo brillante/oscuro por reflexión) (2):
  $$
  r_{\mathrm{brillante}} = \sqrt{\left(m + \frac{1}{2}\right)\lambda R}
  $$
### 16.3 Difracción de Fraunhofer (Campo Lejano)

- Rendija Simple de Ancho $a$ (1):
  $$
  a \sen\theta = m \lambda
  $$
- Rendija Simple de Ancho $a$ (2):
  $$
  m = \pm 1, \pm 2, \dots
  $$
- Rendija Simple de Ancho $a$ (3):
  $$
  I(\theta) = I_0 \left[ \frac{\sen(\beta)}{\beta} \right]^2 = I_0 \operatorname{sinc}^2(\beta)
  $$
- Rendija Simple de Ancho $a$ (4):
  $$
  \beta = \frac{\pi a}{\lambda}\sen\theta
  $$
- Doble Rendija con Difracción e Interferencia Combinadas (1):
  $$
  I(\theta) = I_0 \cos^2(\alpha) \left[ \frac{\sen(\beta)}{\beta} \right]^2
  $$
- Doble Rendija con Difracción e Interferencia Combinadas (2):
  $$
  \alpha = \frac{\pi d}{\lambda}\sen\theta
  $$
- Doble Rendija con Difracción e Interferencia Combinadas (3):
  $$
  \beta = \frac{\pi a}{\lambda}\sen\theta
  $$
- Abertura Circular de Diámetro $D$ (Patrón de Airy):
  $$
  \sen\theta_{\min} \approx 1.22 \frac{\lambda}{D}
  $$
- Redes de Difracción ($N$ rendijas, espaciado $d$) (1):
  $$
  d \sen\theta = m \lambda \quad m \in \mathbb{Z}
  $$
- Redes de Difracción ($N$ rendijas, espaciado $d$) (2):
  $$
  \mathcal{R} = \frac{\lambda}{\Delta\lambda} = m N
  $$
- Redes de Difracción ($N$ rendijas, espaciado $d$) (3):
  $$
  D_\theta = \frac{d\theta}{d\lambda} = \frac{m}{d \cos\theta}
  $$
### 16.4 Ecuaciones de Fresnel para Interfaces Dieléctricas Planas

- Coeficientes de Reflexión en Amplitud (1):
  $$
  r_\perp = \frac{n_1 \cos\theta_i - n_2 \cos\theta_t}{n_1 \cos\theta_i + n_2 \cos\theta_t} = -\frac{\sen(\theta_i - \theta_t)}{\sen(\theta_i + \theta_t)}
  $$
- Coeficientes de Reflexión en Amplitud (2):
  $$
  r_\parallel = \frac{n_2 \cos\theta_i - n_1 \cos\theta_t}{n_2 \cos\theta_i + n_1 \cos\theta_t} = \frac{\tan(\theta_i - \theta_t)}{\tan(\theta_i + \theta_t)}
  $$
- Coeficientes de Transmisión en Amplitud (1):
  $$
  t_\perp = \frac{2 n_1 \cos\theta_i}{n_1 \cos\theta_i + n_2 \cos\theta_t} = \frac{2 \sen\theta_t \cos\theta_i}{\sen(\theta_i + \theta_t)}
  $$
- Coeficientes de Transmisión en Amplitud (2):
  $$
  t_\parallel = \frac{2 n_1 \cos\theta_i}{n_2 \cos\theta_i + n_1 \cos\theta_t} = \frac{2 \sen\theta_t \cos\theta_i}{\sen(\theta_i + \theta_t)\cos(\theta_i - \theta_t)}
  $$
- Reflectancia ($R$) y Transmitancia ($T_w$) de Potencia (1):
  $$
  R_\perp = |r_\perp|^2
  $$
- Reflectancia ($R$) y Transmitancia ($T_w$) de Potencia (2):
  $$
  R_\parallel = |r_\parallel|^2
  $$
- Reflectancia ($R$) y Transmitancia ($T_w$) de Potencia (3):
  $$
  R + T_w = 1
  $$
## 17. Óptica Electromagnética, Dispersión y Guías de Ondas

### 17.1 Dispersión y Propagación en Medios Materiales

- Relación entre Índice de Refracción y Constantes Dieléctricas:
  $$
  n = \sqrt{\varepsilon_r \mu_r} \approx \sqrt{\varepsilon_r}
  $$
- Ecuación Empírica de Dispersión de Cauchy:
  $$
  n(\lambda) = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4} + \dots
  $$
- Ecuación de Sellmeier:
  $$
  n^2(\lambda) = 1 + \sum_{i} \frac{B_i \lambda^2}{\lambda^2 - C_i}
  $$
- Velocidad de Fase y Velocidad de Grupo (1):
  $$
  v_p = \frac{\omega}{k} = \frac{c}{n}
  $$
- Velocidad de Fase y Velocidad de Grupo (2):
  $$
  v_g = \frac{d\omega}{dk} = \frac{c}{n_g}
  $$
- Velocidad de Fase y Velocidad de Grupo (3):
  $$
  n_g = n - \lambda \frac{dn}{d\lambda}
  $$
- Dispersión por Retardo de Grupo (GVD / Parámetro $D$) (1):
  $$
  D = -\frac{\lambda}{c} \frac{d^2 n}{d\lambda^2} = -\frac{2\pi c}{\lambda^2} \beta_2
  $$
- Dispersión por Retardo de Grupo (GVD / Parámetro $D$) (2):
  $$
  \beta_2 = \frac{d^2 k}{d\omega^2}
  $$
### 17.2 Atenuación y Absorción

- Índice de Refracción Complejo:
  $$
  \tilde{n} = n + i \kappa
  $$
- Ley de Beer-Lambert (Coeficiente de absorción $\alpha$) (1):
  $$
  I(z) = I_0 e^{-\alpha z}
  $$
- Ley de Beer-Lambert (Coeficiente de absorción $\alpha$) (2):
  $$
  \alpha = \frac{2\omega\kappa}{c} = \frac{4\pi\kappa}{\lambda_0}
  $$
- Profundidad de Penetración / Efecto Piel Óptico ($\delta_s$):
  $$
  \delta_s = \frac{1}{\alpha} = \frac{\lambda_0}{4\pi\kappa}
  $$
## 18. Óptica Cuántica, Radiación, Haces Láser y No Lineal

### 18.1 Leyes de Radiación Térmica (Cuerpo Negro)

- Ley de Distribución Espectral de Planck (1):
  $$
  u_\lambda(\lambda, T) = \frac{8\pi h c}{\lambda^5} \frac{1}{e^{\frac{h c}{\lambda k_B T}} - 1}
  $$
- Ley de Distribución Espectral de Planck (2):
  $$
  I_\nu(\nu, T) = \frac{2h\nu^3}{c^2}\frac{1}{e^{\frac{h\nu}{k_B T}} - 1}
  $$
- Ley de Desplazamiento de Wien:
  $$
  \lambda_{\mathrm{máx}} T = b \approx 2.8978 \times 10^{-3} \, \mathrm{m}\cdot\mathrm{K}
  $$
- Ley de Stefan-Boltzmann (1):
  $$
  j^* = \sigma T^4 = \varepsilon \sigma T^4
  $$
- Ley de Stefan-Boltzmann (2):
  $$
  \sigma = \frac{2\pi^5 k_B^4}{15 c^2 h^3} \approx 5.6704 \times 10^{-8} \, \frac{\mathrm{W}}{\mathrm{m}^2\cdot\mathrm{K}^4}
  $$
### 18.2 Radiometría y Fotometría

- Flujo radiante ($\phi_e$ en w):
  $$
  \Phi_v = K_m \int_0^\infty \Phi_{e,\lambda}(\lambda) V(\lambda) d\lambda
  $$
- Flujo luminoso ($\phi_v$ en lúmenes lm):
  $$
  K_m \approx 683 \, \frac{\mathrm{lm}}{\mathrm{W}}
  $$
- Irradiancia ($E_e$) e Iluminancia ($E_v$ en lux) (1):
  $$
  E_e = \frac{d\Phi_e}{dA}
  $$
- Irradiancia ($E_e$) e Iluminancia ($E_v$ en lux) (2):
  $$
  E_v = \frac{d\Phi_v}{dA}
  $$
- Intensidad Radiante ($I_e$) e Intensidad Luminosa ($I_v$ en candelas cd):
  $$
  I = \frac{d\Phi}{d\Omega}
  $$
- Ley de Lambert (Superficie Difusa Emisora / Reflectora):
  $$
  I(\theta) = I_0 \cos\theta
  $$
### 18.3 Física del Láser y Coeficientes de Einstein

- Relación entre Emisión Espontánea ($A_{21}$), Estimulada ($B_{21}$) y Absorción ($B_{12}$) (1):
  $$
  g_1 B_{12} = g_2 B_{21}
  $$
- Relación entre Emisión Espontánea ($A_{21}$), Estimulada ($B_{21}$) y Absorción ($B_{12}$) (2):
  $$
  A_{21} = \frac{8\pi h \nu^3}{c^3} B_{21}
  $$
- Condición de Inversión de Población para Ganancia Óptica:
  $$
  N_2 - \frac{g_2}{g_1} N_1 > 0
  $$
- Ganancia Óptica en Medio Activo (Sección eficaz estimulada $\sigma_{21}$) (1):
  $$
  I(z) = I_0 e^{\gamma(\nu) z}
  $$
- Ganancia Óptica en Medio Activo (Sección eficaz estimulada $\sigma_{21}$) (2):
  $$
  \gamma(\nu) = \sigma_{21}(\nu)\left[ N_2 - \frac{g_2}{g_1} N_1 \right]
  $$
- Condición de Umbral Láser en Cavidad de Longitud $L$ (Reflectancias $R_1, R_2$):
  $$
  \gamma_{\mathrm{th}} = \alpha_{\mathrm{pérdidas}} + \frac{1}{2L}\ln\left( \frac{1}{R_1 R_2} \right)
  $$
# Compendio VI: Física Moderna
*(Nivel Intermedio)*

## 19. Teoría de la Relatividad (Especial y General)

### 19.1 Transformaciones de Lorentz y Espacio-Tiempo de Minkowski

- Transformación de Coordenadas de Lorentz (Movimiento estándar a lo largo de $x$) (1):
  $$
  x' = \gamma (x - v t)
  $$
- Transformación de Coordenadas de Lorentz (Movimiento estándar a lo largo de $x$) (2):
  $$
  y' = y
  $$
- Transformación de Coordenadas de Lorentz (Movimiento estándar a lo largo de $x$) (3):
  $$
  z' = z
  $$
- Transformación de Coordenadas de Lorentz (Movimiento estándar a lo largo de $x$) (4):
  $$
  t' = \gamma \left( t - \frac{v x}{c^2} \right)
  $$
- Transformación Inversa (1):
  $$
  x = \gamma (x' + v t')
  $$
- Transformación Inversa (2):
  $$
  y = y'
  $$
- Transformación Inversa (3):
  $$
  z = z'
  $$
- Transformación Inversa (4):
  $$
  t = \gamma \left( t' + \frac{v x'}{c^2} \right)
  $$
- Intervalo Espaciotemporal Invariante ($s^2$) (1):
  $$
  \Delta s^2 = c^2 \Delta t^2 - (\Delta x^2 + \Delta y^2 + \Delta z^2) = c^2 \Delta t^2 - |\Delta\vec{r}|^2 = \mathrm{invariante}
  $$
- Intervalo Espaciotemporal Invariante ($s^2$) (2):
  $$
  \Delta s^2 > 0 \quad (\mathrm{Tipo Tiempo})
  $$
- Intervalo Espaciotemporal Invariante ($s^2$) (3):
  $$
  \Delta s^2 = 0 \quad (\mathrm{Tipo Luz / Nulo})
  $$
- Intervalo Espaciotemporal Invariante ($s^2$) (4):
  $$
  \Delta s^2 < 0 \quad (\mathrm{Tipo Espacio})
  $$
- Rapidez Relativista ($\theta$ / Parametrización Hiperbólica) (1):
  $$
  \beta = \tanh(\theta)
  $$
- Rapidez Relativista ($\theta$ / Parametrización Hiperbólica) (2):
  $$
  \gamma = \cosh(\theta)
  $$
- Rapidez Relativista ($\theta$ / Parametrización Hiperbólica) (3):
  $$
  \gamma\beta = \sinh(\theta) \implies \theta_{\mathrm{total}} = \theta_1 + \theta_2
  $$
### 19.2 Formalismo Cuadrivectorial

- Métrica de Minkowski $\eta_{\mu\nu}$ (Convención $+,-,-,-$):
  $$
  \eta_{\mu\nu} = \operatorname{diag}(1, -1, -1, -1)
  $$
- Cuadrivector Posición:
  $$
  X^\mu = (ct, x, y, z) = (ct, \vec{r})
  $$
- Cuadrivector Velocidad (Tiempo propio $\tau$ con $d\tau = dt/\gamma$) (1):
  $$
  U^\mu = \frac{dX^\mu}{d\tau} = \gamma(c, \vec{v})
  $$
- Cuadrivector Velocidad (Tiempo propio $\tau$ con $d\tau = dt/\gamma$) (2):
  $$
  U^\mu U_\mu = \eta_{\mu\nu} U^\mu U^\nu = c^2
  $$
- Cuadrivector Momento / Cuadrimomento (1):
  $$
  P^\mu = m_0 U^\mu = \left( \frac{E}{c}, \vec{p} \right)
  $$
- Cuadrivector Momento / Cuadrimomento (2):
  $$
  P^\mu P_\mu = \frac{E^2}{c^2} - |\vec{p}|^2 = m_0^2 c^2
  $$
- Cuadrivector Fuerza de Minkowski:
  $$
  K^\mu = \frac{dP^\mu}{d\tau} = \gamma \left( \frac{\vec{F} \cdot \vec{v}}{c}, \vec{F} \right)
  $$
- Cuadrivector Onda de De Broglie (1):
  $$
  K^\mu = \left( \frac{\omega}{c}, \vec{k} \right)
  $$
- Cuadrivector Onda de De Broglie (2):
  $$
  P^\mu = \hbar K^\mu
  $$
## 20. Mecánica Cuántica y Física Atómica

### 20.1 Ecuación de Schrödinger No Relativista

- Dependiente del Tiempo (1D y 3D):
  $$
  i\hbar \frac{\partial \Psi(\vec{r}, t)}{\partial t} = \hat{H}\Psi(\vec{r}, t) = \left[ -\frac{\hbar^2}{2m}\nabla^2 + V(\vec{r}, t) \right] \Psi(\vec{r}, t)
  $$
- Independiente del Tiempo (Estados Estacionarios $\Psi(\vec{r}, t) = \psi(\vec{r})e^{-iEt/\hbar}$):
  $$
  \hat{H}\psi(\vec{r}) = E\psi(\vec{r}) \implies -\frac{\hbar^2}{2m}\nabla^2\psi(\vec{r}) + V(\vec{r})\psi(\vec{r}) = E\psi(\vec{r})
  $$
- Densidad de Probabilidad ($P$) y Densidad de Corriente de Probabilidad ($\vec{J}$) (1):
  $$
  P(\vec{r}, t) = |\Psi(\vec{r}, t)|^2 = \Psi^* \Psi
  $$
- Densidad de Probabilidad ($P$) y Densidad de Corriente de Probabilidad ($\vec{J}$) (2):
  $$
  \int_{\mathrm{todo el espacio}} |\Psi|^2 dV = 1
  $$
- Densidad de Probabilidad ($P$) y Densidad de Corriente de Probabilidad ($\vec{J}$) (3):
  $$
  \vec{J} = \frac{\hbar}{2mi}(\Psi^* \nabla\Psi - \Psi \nabla\Psi^*) \implies \frac{\partial P}{\partial t} + \nabla \cdot \vec{J} = 0
  $$
### 20.2 Problemas Unidimensionales Notables

- Pozo de Potencial Infinito (Caja 1D de longitud $L$ en $[0, L]$) (1):
  $$
  \psi_n(x) = \sqrt{\frac{2}{L}}\sen\left( \frac{n\pi x}{L} \right)
  $$
- Pozo de Potencial Infinito (Caja 1D de longitud $L$ en $[0, L]$) (2):
  $$
  E_n = \frac{n^2 \pi^2 \hbar^2}{2m L^2} = \frac{n^2 h^2}{8m L^2}
  $$
- Pozo de Potencial Infinito (Caja 1D de longitud $L$ en $[0, L]$) (3):
  $$
  n = 1, 2, 3, \dots
  $$
- Oscilador Armónico Cuántico Simple ($\omega = \sqrt{k/m}$) (1):
  $$
  E_n = \hbar\omega \left( n + \frac{1}{2} \right)
  $$
- Oscilador Armónico Cuántico Simple ($\omega = \sqrt{k/m}$) (2):
  $$
  n = 0, 1, 2, \dots
  $$
- Oscilador Armónico Cuántico Simple ($\omega = \sqrt{k/m}$) (3):
  $$
  \mathrm{Operadores de Aniquilación/Creación (Escalera): } \hat{a} = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} + \frac{i\hat{p}}{m\omega}\right)
  $$
- Oscilador Armónico Cuántico Simple ($\omega = \sqrt{k/m}$) (4):
  $$
  \hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} - \frac{i\hat{p}}{m\omega}\right)
  $$
- Oscilador Armónico Cuántico Simple ($\omega = \sqrt{k/m}$) (5):
  $$
  [\hat{a}, \hat{a}^\dagger] = 1
  $$
- Oscilador Armónico Cuántico Simple ($\omega = \sqrt{k/m}$) (6):
  $$
  \hat{H} = \hbar\omega\left(\hat{a}^\dagger \hat{a} + \frac{1}{2}\right) = \hbar\omega\left(\hat{N} + \frac{1}{2}\right)
  $$
- Efecto túnel a través de barrera rectangular ($v_0 > e$:
  $$
  T \approx \exp(-2\kappa a)
  $$
- Ancho $a$):
  $$
  \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar} \quad (\mathrm{para } \kappa a \gg 1)
  $$
### 20.3 Momento Angular Cuántico y Átomo de Hidrógeno

- Operadores de Momento Angular Orbital ($\hat{\vec{L}} = \hat{\vec{r}} \times \hat{\vec{p}}$) (1):
  $$
  [\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z
  $$
- Operadores de Momento Angular Orbital ($\hat{\vec{L}} = \hat{\vec{r}} \times \hat{\vec{p}}$) (2):
  $$
  [\hat{L}_y, \hat{L}_z] = i\hbar \hat{L}_x
  $$
- Operadores de Momento Angular Orbital ($\hat{\vec{L}} = \hat{\vec{r}} \times \hat{\vec{p}}$) (3):
  $$
  [\hat{L}_z, \hat{L}_x] = i\hbar \hat{L}_y
  $$
- Operadores de Momento Angular Orbital ($\hat{\vec{L}} = \hat{\vec{r}} \times \hat{\vec{p}}$) (4):
  $$
  [\hat{L}^2, \hat{L}_z] = 0
  $$
- Autovalores de Momento Angular y Proyección (1):
  $$
  \hat{L}^2 |l, m_l\rangle = \hbar^2 l(l + 1)|l, m_l\rangle
  $$
- Autovalores de Momento Angular y Proyección (2):
  $$
  l = 0, 1, 2, \dots
  $$
- Autovalores de Momento Angular y Proyección (3):
  $$
  \hat{L}_z |l, m_l\rangle = \hbar m_l |l, m_l\rangle
  $$
- Autovalores de Momento Angular y Proyección (4):
  $$
  m_l = -l, -l+1, \dots, l
  $$
- Función de Onda del Átomo de Hidrógeno (1):
  $$
  \psi_{n, l, m_l}(r, \theta, \phi) = R_{nl}(r) Y_l^{m_l}(\theta, \phi)
  $$
- Función de Onda del Átomo de Hidrógeno (2):
  $$
  (R_{nl} = \mathrm{Polinomios asociados de Laguerre}, \, Y_l^{m_l} = \mathrm{Armónicos esféricos})
  $$
## 21. Física Nuclear, Radiactividad y Partículas Elementales

### 21.1 Balances Energéticos y Modelos Nucleares

- Valor $Q$ de una Reacción Nuclear ($a + X \to Y + b$) (1):
  $$
  Q = (m_a + m_X - m_Y - m_b) c^2 = E_{k,Y} + E_{k,b} - E_{k,a}
  $$
- Valor $Q$ de una Reacción Nuclear ($a + X \to Y + b$) (2):
  $$
  Q > 0 \quad (\mathrm{Exoenergética / Exotérmica})
  $$
- Valor $Q$ de una Reacción Nuclear ($a + X \to Y + b$) (3):
  $$
  Q < 0 \quad (\mathrm{Endoenergética / Endotérmica})
  $$
- Energía Umbral para Reacciones Endoenergéticas ($Q < 0$ sobre blanco estacionario):
  $$
  E_{\mathrm{umbral}} = |Q|\left( 1 + \frac{m_a}{m_X} \right)
  $$
- Fórmula Semiempírica de Masas de Bethe-Weizsäcker (Modelo de la Gota Líquida) (1):
  $$
  B(A, Z) = a_v A - a_s A^{2/3} - a_c \frac{Z(Z - 1)}{A^{1/3}} - a_a \frac{(A - 2Z)^2}{A} + \delta(A, Z)
  $$
- Fórmula Semiempírica de Masas de Bethe-Weizsäcker (Modelo de la Gota Líquida) (2):
  $$
  \delta(A, Z) = \begin{cases} +a_p A^{-1/2} & \mathrm{para } Z \mathrm{ par, } N \mathrm{ par} \\ 0 & \mathrm{para } A \mathrm{ impar (par-impar / impar-par)} \\ -a_p A^{-1/2} & \mathrm{para } Z \mathrm{ impar, } N \mathrm{ impar} \end{cases} \quad (\mathrm{o con término } \delta \propto \pm a_p A^{-3/4})
  $$
- Ley de Geiger-Nuttall para Desintegración Alfa ($E_\alpha = \mathrm{energía de la partícula } \alpha$):
  $$
  \log_{10}(\lambda) = A_G + B_G \frac{Z}{\sqrt{E_\alpha}}
  $$
### 21.2 Secciones Eficaces y Dosimetría

- Tasa de Reacción Nuclear (Flujo $\Phi$, densidad de núcleos blanco $n_t$, sección eficaz $\sigma$) (1):
  $$
  R = \Phi \sigma N_t = I n_t x \sigma
  $$
- Tasa de Reacción Nuclear (Flujo $\Phi$, densidad de núcleos blanco $n_t$, sección eficaz $\sigma$) (2):
  $$
  1 \, \mathrm{barn} (\mathrm{b}) = 10^{-28} \, \mathrm{m}^2 = 100 \, \mathrm{fm}^2
  $$
- Dosis absorbida ($d$ en grays $\mathrm{gy} = \mathrm{j/kg}$):
  $$
  D = \frac{dE_{\mathrm{dep}}}{dm}
  $$
- Dosis equivalente ($h$ en sieverts $\mathrm{sv}$ con factor de calidad $w_r$):
  $$
  H = w_R \cdot D
  $$
## 22. Física del Estado Sólido y Materia Condensada

### 22.1 Cristalografía y Difracción

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
### 22.2 Gas de Electrones Libres de Fermi

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
### 22.3 Transporte Electrónico y Térmico

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
