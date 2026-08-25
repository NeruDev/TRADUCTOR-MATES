---
file: docs/fisica/formulario_avanzado.md
description: Compendio didáctico de fórmulas de física de nivel avanzado y universitario (cuántica, relatividad, analítica).
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/symbols.py
relations:
  - docs/fisica/formulario_fisica.md
  - docs/mates/formulario_avanzado.md
  - docs/ARCHITECTURE.md
keywords:
  - formulas-avanzadas-fisica
  - mecanica-analitica
  - relatividad-general
  - fisica-cuantica
---

# Compendio I: Mecánica Clásica, de Fluidos y Analítica
*(Nivel Avanzado)*

## 1. Cinemática y Dinámica Newtoniana

### 1.1 Dinámica Tridimensional del Sólido Rígido

- Tensor de Inercia $\mathbf{I}$ (con productos de inercia $I_{ij} = \int x_i x_j dm$) (1):
  $$
  \mathbf{I} = \begin{bmatrix} I_{xx} & -I_{xy} & -I_{xz} \\ -I_{yx} & I_{yy} & -I_{yz} \\ -I_{zx} & -I_{zy} & I_{zz} \end{bmatrix}
  $$
- Tensor de Inercia $\mathbf{I}$ (con productos de inercia $I_{ij} = \int x_i x_j dm$) (2):
  $$
  I_{xx} = \int (y^2 + z^2) \, dm
  $$
- Tensor de Inercia $\mathbf{I}$ (con productos de inercia $I_{ij} = \int x_i x_j dm$) (3):
  $$
  I_{xy} = \int xy \, dm
  $$
- Tensor de Inercia $\mathbf{I}$ (con productos de inercia $I_{ij} = \int x_i x_j dm$) (4):
  $$
  \left( \mathrm{En notación tensorial: } I_{ij} = \int (r^2 \delta_{ij} - x_i x_j) \, dm \right)
  $$
- Momento angular tridimensional:
  $$
  \vec{L} = \mathbf{I} \vec{\omega}
  $$
- Ecuaciones de Euler para el cuerpo rígido (en el sistema de ejes principales) (1):
  $$
  I_1 \dot{\omega}_1 - (I_2 - I_3)\omega_2 \omega_3 = \tau_1
  $$
- Ecuaciones de Euler para el cuerpo rígido (en el sistema de ejes principales) (2):
  $$
  I_2 \dot{\omega}_2 - (I_3 - I_1)\omega_3 \omega_1 = \tau_2
  $$
- Ecuaciones de Euler para el cuerpo rígido (en el sistema de ejes principales) (3):
  $$
  I_3 \dot{\omega}_3 - (I_1 - I_2)\omega_1 \omega_2 = \tau_3
  $$
## 2. Trabajo, Energía, Momento Lineal y Gravitación

### 2.1 Problema de Dos Cuerpos y Fuerzas Centrales

- Masa reducida ($\mu$):
  $$
  \mu = \frac{m_1 m_2}{m_1 + m_2}
  $$
- Ecuación de movimiento relativa:
  $$
  \mu \ddot{\vec{r}} = f(r) \hat{u}_r
  $$
- Potencial Efectivo:
  $$
  U_{\mathrm{eff}}(r) = U(r) + \frac{L^2}{2\mu r^2}
  $$
- Ecuación diferencial de la órbita (Ecuación de Binet para $u = 1/r$):
  $$
  \frac{d^2 u}{d\theta^2} + u = -\frac{\mu}{L^2 u^2} f\left(\frac{1}{u}\right)
  $$
- Ecuación de las cónicas orbitales ($p = \mathrm{semilatus rectum}$, $e = \mathrm{excentricidad}$ para $U(r) = -G m_1 m_2 / r$) (1):
  $$
  r(\theta) = \frac{p}{1 + e \cos(\theta)}
  $$
- Ecuación de las cónicas orbitales ($p = \mathrm{semilatus rectum}$, $e = \mathrm{excentricidad}$ para $U(r) = -G m_1 m_2 / r$) (2):
  $$
  p = \frac{L^2}{\mu G m_1 m_2}
  $$
- Ecuación de las cónicas orbitales ($p = \mathrm{semilatus rectum}$, $e = \mathrm{excentricidad}$ para $U(r) = -G m_1 m_2 / r$) (3):
  $$
  e = \sqrt{1 + \frac{2 E L^2}{\mu (G m_1 m_2)^2}}
  $$
## 3. Oscilaciones y Mecánica de Fluidos

### 3.1 Mecánica de Fluidos y Medios Continuos

- Ecuación de Continuidad diferencial:
  $$
  \frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0
  $$
- Ecuación de Navier-Stokes (Fluidos Newtonianos incompresibles con viscosidad $\mu$):
  $$
  \rho \left( \frac{\partial \vec{v}}{\partial t} + (\vec{v} \cdot \nabla)\vec{v} \right) = -\nabla P + \mu \nabla^2 \vec{v} + \rho \vec{g}
  $$
- Tensor de Esfuerzos de Cauchy $\boldsymbol{\sigma}$:
  $$
  \nabla \cdot \boldsymbol{\sigma} + \vec{f}_{\mathrm{ext}} = \rho \frac{d\vec{v}}{dt}
  $$
- Ecuación de Navier-Cauchy para Sólidos Elásticos Lineales (Parámetros de Lamé $\lambda, \mu$):
  $$
  \rho \frac{\partial^2 \vec{u}}{\partial t^2} = (\lambda + \mu)\nabla(\nabla \cdot \vec{u}) + \mu \nabla^2 \vec{u} + \vec{f}_{\mathrm{vol}}
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
### 4.3 Formulaciones Canónicas Avanzadas

- Corchetes de Poisson:
  $$
  \{f, g\}_{q,p} = \sum_{j=1}^n \left( \frac{\partial f}{\partial q_j} \frac{\partial g}{\partial p_j} - \frac{\partial f}{\partial p_j} \frac{\partial g}{\partial q_j} \right)
  $$
- Evolución temporal de una función observable:
  $$
  \frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}
  $$
- Teorema de Liouville (Conservación del volumen en el espacio fásico):
  $$
  \frac{d\rho}{dt} = \frac{\partial \rho}{\partial t} + \{\rho, H\} = 0
  $$
- Ecuación de Hamilton-Jacobi:
  $$
  H\left( q_1, \dots, q_n, \frac{\partial S}{\partial q_1}, \dots, \frac{\partial S}{\partial q_n}, t \right) + \frac{\partial S}{\partial t} = 0
  $$
### 4.4 Mecánica Relativista (Relatividad Especial)

- Factor de Lorentz:
  $$
  \gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}
  $$
- Momento lineal relativista:
  $$
  \vec{p} = \gamma m_0 \vec{v}
  $$
- Fuerza relativista:
  $$
  \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(\gamma m_0 \vec{v})
  $$
- Energía total, cinética y en reposo (1):
  $$
  E = \gamma m_0 c^2 = E_k + m_0 c^2
  $$
- Energía total, cinética y en reposo (2):
  $$
  E_k = (\gamma - 1) m_0 c^2
  $$
- Relación de dispersión Energía-Momento:
  $$
  E^2 = (p c)^2 + (m_0 c^2)^2
  $$
- Cuadrivectores en Cinemática y Dinámica (1):
  $$
  X^\mu = (ct, \vec{r})
  $$
- Cuadrivectores en Cinemática y Dinámica (2):
  $$
  U^\mu = \frac{dX^\mu}{d\tau} = \gamma(c, \vec{v})
  $$
- Cuadrivectores en Cinemática y Dinámica (3):
  $$
  P^\mu = m_0 U^\mu = \left( \frac{E}{c}, \vec{p} \right)
  $$
- Cuadrivectores en Cinemática y Dinámica (4):
  $$
  P^\mu P_\mu = \frac{E^2}{c^2} - |\vec{p}|^2 = m_0^2 c^2
  $$
# Compendio II: Oscilaciones y Ondas Mecánicas
*(Nivel Avanzado)*

## 5. Movimiento Oscilatorio (Oscilaciones)

### 5.1 Osciladores Acoplados y Modos Normales

- Ecuación Matricial de Movimiento (Sistemas lineales de $N$ grados de libertad):
  $$
  \mathbf{M} \ddot{\vec{x}} + \mathbf{K} \vec{x} = \vec{0}
  $$
- Ecuación Secular / Polinomio Característico:
  $$
  \det(\mathbf{K} - \omega^2 \mathbf{M}) = 0
  $$
- Transformación a Coordenadas Normales ($\vec{\eta} = \mathbf{P}^{-1} \vec{x}$) (1):
  $$
  \ddot{\eta}_k + \omega_k^2 \eta_k = 0
  $$
- Transformación a Coordenadas Normales ($\vec{\eta} = \mathbf{P}^{-1} \vec{x}$) (2):
  $$
  k = 1, 2, \dots, N
  $$
### 5.2 Oscilaciones No Lineales (Péndulo Simple de Gran Amplitud)

- Ecuación Diferencial Exacta:
  $$
  \ddot{\theta} + \omega_0^2 \sen(\theta) = 0
  $$
- Periodo Exacto mediante Integrales Elípticas Completas de Primera Especie $K(m)$:
  $$
  T = 4\sqrt{\frac{L}{g}} K\left(\sen^2\left(\frac{\theta_0}{2}\right)\right) = 4\sqrt{\frac{L}{g}} \int_0^{\pi/2} \frac{d\phi}{\sqrt{1 - \sen^2\left(\frac{\theta_0}{2}\right) \sen^2\phi}}
  $$
- Aproximación de Borda (Series de Taylor):
  $$
  T \approx 2\pi\sqrt{\frac{L}{g}} \left( 1 + \frac{1}{16}\theta_0^2 + \frac{11}{3072}\theta_0^4 + \dots \right)
  $$
### 5.3 Osciladores Autoexcitados (Ecuación de Van der Pol)

- Ecuación con amortiguamiento no lineal:
  $$
  \ddot{x} - \mu(1 - x^2)\dot{x} + \omega_0^2 x = 0
  $$
## 6. Ondas Mecánicas en Medios Continuos

### 6.1 Dispersión de Ondas

- Relación de Dispersión:
  $$
  \omega = \omega(k)
  $$
- Velocidad de Fase:
  $$
  v_p = \frac{\omega}{k}
  $$
- Velocidad de Grupo:
  $$
  v_g = \frac{d\omega}{dk} = v_p + k \frac{dv_p}{dk} = v_p - \lambda \frac{dv_p}{d\lambda}
  $$
### 6.2 Impedancia Mecánica y Fenómenos en Fronteras

- Impedancia Característica del Medio (1):
  $$
  Z = \rho v = \sqrt{\rho B} \quad (\mathrm{Fluidos})
  $$
- Impedancia Característica del Medio (2):
  $$
  Z = \mu v = \sqrt{\mu T} \quad (\mathrm{Cuerdas})
  $$
- Coeficiente de Reflexión en Amplitud (para ondas de desplazamiento / velocidad incidiendo de medio 1 a medio 2):
  $$
  r = \frac{Z_1 - Z_2}{Z_1 + Z_2}
  $$
- Coeficiente de Transmisión en Amplitud (desplazamiento / velocidad):
  $$
  t = \frac{2Z_1}{Z_1 + Z_2}
  $$
- Coeficientes de reflexión:
  $$
  R = r^2 = \left( \frac{Z_1 - Z_2}{Z_1 + Z_2} \right)^2
  $$
- Transmisión de potencia / intensidad ($r + t_w = 1$):
  $$
  T_w = \frac{Z_2}{Z_1} t^2 = \frac{4 Z_1 Z_2}{(Z_1 + Z_2)^2}
  $$
### 6.3 Ondas Elásticas en Medios Continuos 3D (Ecuación de Navier-Cauchy)

- Ondas Longitudinales Primarias (Ondas P / Compresionales):
  $$
  v_P = \sqrt{\frac{\lambda + 2\mu}{\rho}} = \sqrt{\frac{K + \frac{4}{3}G}{\rho}}
  $$
- Ondas Transversales Secundarias (Ondas S / Cizalladura):
  $$
  v_S = \sqrt{\frac{\mu}{\rho}} = \sqrt{\frac{G}{\rho}}
  $$
## 7. Interferencia, Ondas Estacionarias y Acústica

### 7.1 Acústica Física y Ondas de Presión

- Onda de Desplazamiento Molecular:
  $$
  s(x, t) = s_{\mathrm{máx}} \cos(kx - \omega t)
  $$
- Onda de Presión Acústica Excedente:
  $$
  \Delta p(x, t) = -B \frac{\partial s}{\partial x} = \Delta p_{\mathrm{máx}} \sen(kx - \omega t)
  $$
- Amplitud de Presión:
  $$
  \Delta p_{\mathrm{máx}} = B k s_{\mathrm{máx}} = \rho v \omega s_{\mathrm{máx}} = Z \omega s_{\mathrm{máx}}
  $$
- Relación entre Intensidad y Presión Acústica:
  $$
  I = \frac{\Delta p_{\mathrm{máx}}^2}{2\rho v} = \frac{p_{\mathrm{rms}}^2}{\rho v}
  $$
### 7.2 Ecuación de Onda Acústica Tridimensional

- Ecuación Diferencial para la Presión:
  $$
  \nabla^2 p - \frac{1}{c^2} \frac{\partial^2 p}{\partial t^2} = 0
  $$
- Solución para Ondas Esféricas Monocromáticas:
  $$
  p(r, t) = \frac{A}{r} e^{i(kr - \omega t)}
  $$
- Potencial de Velocidad Acústico ($\vec{u} = -\nabla \Phi$) (1):
  $$
  \nabla^2 \Phi - \frac{1}{c^2} \frac{\partial^2 \Phi}{\partial t^2} = 0
  $$
- Potencial de Velocidad Acústico ($\vec{u} = -\nabla \Phi$) (2):
  $$
  p = \rho_0 \frac{\partial \Phi}{\partial t}
  $$
### 7.3 Efecto Doppler Vectorial en Dirección Arbitraria

- Frecuencia Observada (1):
  $$
  f_o = f_s \left( \frac{c - \vec{v}_o \cdot \hat{n}}{c - \vec{v}_s \cdot \hat{n}} \right)
  $$
- Frecuencia Observada (2):
  $$
  (\hat{n} = \mathrm{vector unitario dirigido de la fuente al observador})
  $$
### 7.4 Atenuación y Absorción Acústica Viscotérmica

- Decaimiento Espacial de Amplitud:
  $$
  A(x) = A_0 e^{-\alpha x}
  $$
- Coeficiente de Atenuación Clásico de Stokes-Kirchhoff:
  $$
  \alpha = \frac{\omega^2}{2\rho c^3} \left[ \frac{4}{3}\eta + \eta_v + \frac{(\gamma - 1)\kappa}{C_p} \right]
  $$
# Compendio III: Termodinámica Clásica, Química y Estadística
*(Nivel Avanzado)*

## 8. Conceptos Fundamentales, Gases y Ecuaciones de Estado

### 8.1 Otras Ecuaciones de Estado Reales

- Redlich-Kwong:
  $$
  P = \frac{R T}{V_m - b} - \frac{a}{\sqrt{T} V_m (V_m + b)}
  $$
- Peng-Robinson:
  $$
  P = \frac{R T}{V_m - b} - \frac{a(T)}{V_m^2 + 2bV_m - b^2}
  $$
- Dieterici:
  $$
  P = \frac{R T}{V_m - b} \exp\left( -\frac{a}{R T V_m} \right)
  $$
### 8.2 Teoría Cinética Molecular de los Gases

- Presión Cinética:
  $$
  P = \frac{1}{3} \rho \langle v^2 \rangle = \frac{1}{3} \frac{N m}{V} v_{\mathrm{rms}}^2
  $$
- Energía Cinética Media Translacional por Molécula:
  $$
  \langle \epsilon_k \rangle = \frac{1}{2} m \langle v^2 \rangle = \frac{3}{2} k_B T
  $$
- Velocidades Moleculares Características (1):
  $$
  v_{\mathrm{rms}} = \sqrt{\langle v^2 \rangle} = \sqrt{\frac{3 k_B T}{m}} = \sqrt{\frac{3 R T}{M}}
  $$
- Velocidades Moleculares Características (2):
  $$
  v_{\mathrm{prom}} = \langle v \rangle = \sqrt{\frac{8 k_B T}{\pi m}} = \sqrt{\frac{8 R T}{\pi M}}
  $$
- Velocidades Moleculares Características (3):
  $$
  v_{\mathrm{mp}} = \sqrt{\frac{2 k_B T}{m}} = \sqrt{\frac{2 R T}{M}}
  $$
- Distribución de Rapideces de Maxwell-Boltzmann:
  $$
  f(v) = 4\pi \left( \frac{m}{2\pi k_B T} \right)^{3/2} v^2 \exp\left( -\frac{m v^2}{2 k_B T} \right)
  $$
- Teorema de Equipartición de la Energía ($f = \mathrm{grados de libertad activos}$) (1):
  $$
  U = \frac{f}{2} N k_B T = \frac{f}{2} n R T
  $$
- Teorema de Equipartición de la Energía ($f = \mathrm{grados de libertad activos}$) (2):
  $$
  C_{v,m} = \frac{f}{2} R
  $$
- Teorema de Equipartición de la Energía ($f = \mathrm{grados de libertad activos}$) (3):
  $$
  C_{p,m} = \left(\frac{f}{2} + 1\right) R
  $$
## 9. Primera y Segunda Ley de la Termodinámica

### 9.1 Balances de Energía y Entropía en Volúmenes de Control (Sistemas Abiertos)

- Conservación de Masa:
  $$
  \frac{dm_{\mathrm{VC}}}{dt} = \sum_{\mathrm{ent}} \dot{m}_i - \sum_{\mathrm{sal}} \dot{m}_e
  $$
- Primera Ley en Volumen de Control:
  $$
  \frac{dE_{\mathrm{VC}}}{dt} = \dot{Q} - \dot{W}_{\mathrm{eje}} + \sum_{\mathrm{ent}} \dot{m}_i \left( h_i + \frac{v_i^2}{2} + g z_i \right) - \sum_{\mathrm{sal}} \dot{m}_e \left( h_e + \frac{v_e^2}{2} + g z_e \right)
  $$
- Primera Ley en Estado Estacionario ($\frac{dE_{\mathrm{VC}}}{dt} = 0$, 1 entrada y 1 salida):
  $$
  q - w_{\mathrm{eje}} = (h_e - h_i) + \frac{v_e^2 - v_i^2}{2} + g(z_e - z_i)
  $$
- Balance de Entropía en Volumen de Control (1):
  $$
  \frac{dS_{\mathrm{VC}}}{dt} = \sum_k \frac{\dot{Q}_k}{T_k} + \sum_{\mathrm{ent}} \dot{m}_i s_i - \sum_{\mathrm{sal}} \dot{m}_e s_e + \dot{S}_{\mathrm{gen}}
  $$
- Balance de Entropía en Volumen de Control (2):
  $$
  \dot{S}_{\mathrm{gen}} \ge 0
  $$
### 9.2 Análisis Exergético (Disponibilidad) y Destrucción de Exergía

- Exergía de Sistema Cerrado:
  $$
  \Phi = (U - U_0) + P_0(V - V_0) - T_0(S - S_0)
  $$
- Exergía de Flujo (Sistema Abierto):
  $$
  \psi = (h - h_0) - T_0(s - s_0) + \frac{v^2}{2} + gz
  $$
- Teorema de Gouy-Stodola (Exergía Destruida / Pérdida de Trabajo Útil):
  $$
  \dot{X}_{\mathrm{destruida}} = I = T_0 \dot{S}_{\mathrm{gen}}
  $$
## 10. Potenciales Termodinámicos y Relaciones de Maxwell

### 10.1 Ecuaciones de Estado de la Energía Interna y Efecto Joule-Thomson

- Primera Ecuación de Estado de la Energía:
  $$
  \left( \frac{\partial U}{\partial V} \right)_T = T \left( \frac{\partial P}{\partial T} \right)_V - P = \frac{T \alpha}{\kappa_T} - P
  $$
- Segunda Ecuación de Estado de la Energía (Entalpía):
  $$
  \left( \frac{\partial H}{\partial P} \right)_T = V - T \left( \frac{\partial V}{\partial T} \right)_P = V(1 - T\alpha)
  $$
- Coeficiente de Joule-Thomson ($\mu_{\mathrm{JT}}$):
  $$
  \mu_{\mathrm{JT}} = \left( \frac{\partial T}{\partial P} \right)_H = \frac{1}{C_p} \left[ T \left( \frac{\partial V}{\partial T} \right)_P - V \right] = \frac{V}{C_p}(T\alpha - 1)
  $$
- Temperatura de Inversión de Joule-Thomson ($\mu_{\mathrm{JT}} = 0$):
  $$
  T_{\mathrm{inv}} = \frac{V}{\left( \frac{\partial V}{\partial T} \right)_P} = \frac{1}{\alpha}
  $$
### 10.2 Ecuación de Gibbs-Duhem y Propiedades Molares Parciales

- Ecuación de Gibbs-Duhem:
  $$
  S dT - V dP + \sum_{i=1}^k N_i d\mu_i = 0 \implies \sum_{i=1}^k x_i d\mu_i = 0 \quad (\mathrm{a } T, P \mathrm{ ctes.})
  $$
- Propiedad Molar Parcial general ($\bar{M}_i$):
  $$
  \bar{M}_i = \left( \frac{\partial M}{\partial n_i} \right)_{T, P, n_{j \neq i}} \implies M = \sum_{i=1}^k n_i \bar{M}_i
  $$
- Potencial Químico como Propiedad Molar Parcial:
  $$
  \mu_i = \bar{G}_i = \left( \frac{\partial G}{\partial n_i} \right)_{T, P, n_{j \neq i}}
  $$
### 10.3 Transiciones de Fase y Equilibrio Químico

- Ecuación de Clapeyron (Cualquier transición de fase de 1er orden):
  $$
  \frac{dP}{dT} = \frac{\Delta s}{\Delta v} = \frac{\Delta h}{T \Delta v}
  $$
- Ecuación de Clausius-Clapeyron (Vaporización/Sublimación con $v_g \gg v_l$ y gas ideal):
  $$
  \frac{d \ln P}{dT} = \frac{\Delta h_{\mathrm{vap}}}{R T^2} \implies \ln\left( \frac{P_2}{P_1} \right) = -\frac{\Delta h_{\mathrm{vap}}}{R} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)
  $$
- Regla de las Fases de Gibbs (1):
  $$
  F = C - \mathcal{P} + 2
  $$
- Regla de las Fases de Gibbs (2):
  $$
  (F = \mathrm{grados de libertad}, \, C = \mathrm{número de componentes}, \, \mathcal{P} = \mathrm{número de fases})
  $$
- Ecuaciones de Ehrenfest (Transiciones de fase de 2do orden):
  $$
  \frac{dP}{dT} = \frac{\Delta C_p}{T V \Delta \alpha} = \frac{\Delta \alpha}{\Delta \kappa_T}
  $$
- Isoterma de Van 't Hoff para Equilibrio Químico:
  $$
  \Delta G^\circ = -R T \ln(K_p) \implies \frac{d \ln K_p}{dT} = \frac{\Delta H^\circ}{R T^2}
  $$
### 10.4 Tercera Ley de la Termodinámica (Teorema del Calor de Nernst)

- Comportamiento asíntotico en el cero absoluto (1):
  $$
  \lim_{T \to 0} S = 0 \quad (\mathrm{para un cristal perfecto})
  $$
- Comportamiento asíntotico en el cero absoluto (2):
  $$
  \lim_{T \to 0} C_p = \lim_{T \to 0} C_v = 0
  $$
- Comportamiento asíntotico en el cero absoluto (3):
  $$
  \lim_{T \to 0} \alpha = 0
  $$
- Comportamiento asíntotico en el cero absoluto (4):
  $$
  \lim_{T \to 0} \left( \frac{\partial P}{\partial T} \right)_V = 0
  $$
## 11. Termodinámica Estadística

### 11.1 Colectividades y Funciones de Partición

- Entropía Estadística de Boltzmann:
  $$
  S = k_B \ln(\Omega)
  $$
- Entropía de Gibbs (Distribución general):
  $$
  S = -k_B \sum_i P_i \ln(P_i)
  $$
- Factor de Boltzmann ($\beta$):
  $$
  \beta = \frac{1}{k_B T}
  $$
### 11.2 Colectividad Canónica (Sistema cerrado a $N, V, T$ fijos)

- Función de Partición Canónica ($Z$ o $Q$):
  $$
  Z = \sum_i g_i \exp(-\beta E_i) = \sum_i \exp(-\beta E_i)
  $$
- Probabilidad de ocupación del microestado $i$:
  $$
  P_i = \frac{\exp(-\beta E_i)}{Z}
  $$
- Conexión con los Potenciales Termodinámicos (1):
  $$
  F = -k_B T \ln(Z)
  $$
- Conexión con los Potenciales Termodinámicos (2):
  $$
  U = \langle E \rangle = -\frac{\partial \ln Z}{\partial \beta} = k_B T^2 \left( \frac{\partial \ln Z}{\partial T} \right)_{V, N}
  $$
- Conexión con los Potenciales Termodinámicos (3):
  $$
  S = k_B \ln(Z) + \frac{U}{T} = -\left( \frac{\partial F}{\partial T} \right)_{V, N}
  $$
- Conexión con los Potenciales Termodinámicos (4):
  $$
  P = k_B T \left( \frac{\partial \ln Z}{\partial V} \right)_{T, N} = -\left( \frac{\partial F}{\partial V} \right)_{T, N}
  $$
- Conexión con los Potenciales Termodinámicos (5):
  $$
  \mu = -k_B T \left( \frac{\partial \ln Z}{\partial N} \right)_{T, V} = \left( \frac{\partial F}{\partial N} \right)_{T, V}
  $$
### 11.3 Colectividad Gran Canónica (Sistema abierto a $\mu, V, T$ fijos)

- Gran Función de Partición ($\Xi$) (1):
  $$
  \Xi = \sum_{N=0}^\infty \sum_i \exp\left[ -\beta (E_{i,N} - \mu N) \right] = \sum_{N=0}^\infty \lambda^N Z_N
  $$
- Gran Función de Partición ($\Xi$) (2):
  $$
  \lambda = e^{\beta \mu} \quad (\mathrm{fugacidad})
  $$
- Conexión con el Gran Potencial:
  $$
  \Phi_G = -P V = -k_B T \ln(\Xi)
  $$
- Número medio de partículas:
  $$
  \langle N \rangle = k_B T \left( \frac{\partial \ln \Xi}{\partial \mu} \right)_{T, V} = \frac{1}{\beta} \left( \frac{\partial \ln \Xi}{\partial \mu} \right)
  $$
### 11.4 Estadísticas Cuánticas (Ocupación media del estado monoparticular $\epsilon_i$)

- Estadística de Maxwell-Boltzmann (Partículas clásicas distinguibles):
  $$
  \langle n_i \rangle_{\mathrm{MB}} = \frac{1}{\exp[\beta(\epsilon_i - \mu)]}
  $$
- Estadística de Fermi-Dirac (Fermiones, espín semi-entero, Principio de Exclusión) (1):
  $$
  \langle n_i \rangle_{\mathrm{FD}} = \frac{1}{\exp[\beta(\epsilon_i - \mu)] + 1}
  $$
- Estadística de Fermi-Dirac (Fermiones, espín semi-entero, Principio de Exclusión) (2):
  $$
  \mathrm{Energía de Fermi en } T = 0\mathrm{ K}:
  $$
- Estadística de Fermi-Dirac (Fermiones, espín semi-entero, Principio de Exclusión) (3):
  $$
  E_F = \frac{\hbar^2}{2m} (3\pi^2 n)^{2/3}
  $$
- Estadística de Fermi-Dirac (Fermiones, espín semi-entero, Principio de Exclusión) (4):
  $$
  n = \frac{N}{V}
  $$
- Estadística de Bose-Einstein (Bosones, espín entero) (1):
  $$
  \langle n_i \rangle_{\mathrm{BE}} = \frac{1}{\exp[\beta(\epsilon_i - \mu)] - 1}
  $$
- Estadística de Bose-Einstein (Bosones, espín entero) (2):
  $$
  \mu \le \epsilon_0
  $$
- Estadística de Bose-Einstein (Bosones, espín entero) (3):
  $$
  \mathrm{Temperatura Crítica de Condensación de Bose-Einstein}:
  $$
- Estadística de Bose-Einstein (Bosones, espín entero) (4):
  $$
  T_c = \frac{2\pi \hbar^2}{m k_B} \left( \frac{n}{\zeta(3/2)} \right)^{2/3}
  $$
- Estadística de Bose-Einstein (Bosones, espín entero) (5):
  $$
  \zeta(3/2) \approx 2.612
  $$
# Compendio IV: Electricidad y Magnetismo
*(Nivel Avanzado)*

## 12. Electrostática y Medios Dieléctricos

### 12.1 Ecuaciones Diferenciales de la Electrostática

- Ley de Gauss Diferencial (1):
  $$
  \nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}
  $$
- Ley de Gauss Diferencial (2):
  $$
  \implies
  $$
- Ley de Gauss Diferencial (3):
  $$
  \nabla \cdot \vec{D} = \rho_f
  $$
- Carácter conservativo:
  $$
  \nabla \times \vec{E} = \vec{0}
  $$
- Ecuación de Poisson:
  $$
  \nabla^2 V = -\frac{\rho}{\varepsilon_0}
  $$
- Ecuación de Laplace (en regiones libres de carga $\rho = 0$):
  $$
  \nabla^2 V = 0
  $$
### 12.2 Condiciones de Frontera Electrostáticas

- Componente tangencial del campo eléctrico:
  $$
  \hat{n} \times (\vec{E}_1 - \vec{E}_2) = \vec{0} \implies E_{1t} = E_{2t}
  $$
- Componente normal del desplazamiento eléctrico:
  $$
  \hat{n} \cdot (\vec{D}_1 - \vec{D}_2) = \sigma_f \implies D_{1n} - D_{2n} = \sigma_f
  $$
### 12.3 Expansión Multipolar del Potencial Electrostático

- Serie de potencias:
  $$
  V(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \left[ \frac{Q_{\mathrm{total}}}{r} + \frac{\vec{p} \cdot \hat{r}}{r^2} + \frac{1}{2 r^3} \sum_{i,j} Q_{ij} \hat{r}_i \hat{r}_j + \dots \right]
  $$
- Tensor del momento cuadrupolar ($Q_{ij}$):
  $$
  Q_{ij} = \int (3 x'_i x'_j - r'^2 \delta_{ij}) \rho(\vec{r}') dV'
  $$
### 12.4 Energía Electrostática Total de un Sistema Continuo

- En términos de fuentes:
  $$
  U = \frac{1}{2} \int_V \rho(\vec{r}) V(\vec{r}) dV
  $$
- En términos de campo:
  $$
  U = \frac{1}{2} \int_{\mathrm{todo el espacio}} \vec{D} \cdot \vec{E} \, dV = \frac{\varepsilon_0}{2} \int E^2 \, dV
  $$
## 13. Electrodinámica, Corriente y Circuitos Eléctricos

### 13.1 Ecuación de Continuidad de la Carga

- Conservación local de la carga:
  $$
  \nabla \cdot \vec{J} + \frac{\partial \rho}{\partial t} = 0
  $$
- Régimen Estacionario ($\partial\rho/\partial t = 0$):
  $$
  \nabla \cdot \vec{J} = 0 \implies \oiint_S \vec{J} \cdot d\vec{A} = 0
  $$
### 13.2 Análisis de Circuitos en Régimen Senoidal Permanente (AC - Fasores)

- Representación fasorial de tensiones y corrientes:
  $$
  v(t) = V_m \cos(\omega t + \phi) \iff \mathbf{V} = V_{\mathrm{rms}} e^{j\phi} = \frac{V_m}{\sqrt{2}} \angle \phi
  $$
- Impedancia Compleja ($Z = R + jX$) (1):
  $$
  Z_R = R
  $$
- Impedancia Compleja ($Z = R + jX$) (2):
  $$
  Z_L = j\omega L = \omega L \angle 90^\circ
  $$
- Impedancia Compleja ($Z = R + jX$) (3):
  $$
  Z_C = \frac{1}{j\omega C} = -\frac{j}{\omega C} = \frac{1}{\omega C} \angle -90^\circ
  $$
- Ley de Ohm Fasorial:
  $$
  \mathbf{V} = \mathbf{I} \mathbf{Z}
  $$
- Potencia Compleja ($\mathbf{S}$) (1):
  $$
  \mathbf{S} = \mathbf{V}_{\mathrm{rms}} \mathbf{I}_{\mathrm{rms}}^* = P + j Q = |\mathbf{S}| \cos\theta + j |\mathbf{S}| \sen\theta
  $$
- Potencia Compleja ($\mathbf{S}$) (2):
  $$
  P = V_{\mathrm{rms}} I_{\mathrm{rms}} \cos(\theta_v - \theta_i) \quad (\mathrm{Potencia Activa, W})
  $$
- Potencia Compleja ($\mathbf{S}$) (3):
  $$
  Q = V_{\mathrm{rms}} I_{\mathrm{rms}} \sen(\theta_v - \theta_i) \quad (\mathrm{Potencia Reactiva, VAR})
  $$
- Potencia Compleja ($\mathbf{S}$) (4):
  $$
  |\mathbf{S}| = V_{\mathrm{rms}} I_{\mathrm{rms}} \quad (\mathrm{Potencia Aparente, VA})
  $$
- Factor de Potencia:
  $$
  \mathrm{FP} = \cos(\theta_v - \theta_i) = \frac{P}{|\mathbf{S}|}
  $$
## 14. Magnetostática y Materia Magnética

### 14.1 Ecuaciones Diferenciales de la Magnetostática

- Divergencia nula de la inducción magnética:
  $$
  \nabla \cdot \vec{B} = 0
  $$
- Ley de Ampère Diferencial (1):
  $$
  \nabla \times \vec{B} = \mu_0 \vec{J}
  $$
- Ley de Ampère Diferencial (2):
  $$
  \implies
  $$
- Ley de Ampère Diferencial (3):
  $$
  \nabla \times \vec{H} = \vec{J}_f
  $$
### 14.2 Potencial Vector Magnético ($\vec{A}$)

- Definición ($\vec{B}$ es solenoidal):
  $$
  \vec{B} = \nabla \times \vec{A}
  $$
- Calibre / Gauge de Coulomb ($\nabla \cdot \vec{A} = 0$):
  $$
  \nabla^2 \vec{A} = -\mu_0 \vec{J}
  $$
- Solución integral del Potencial Vector:
  $$
  \vec{A}(\vec{r}) = \frac{\mu_0}{4\pi} \int_V \frac{\vec{J}(\vec{r}')}{|\vec{r} - \vec{r}'|} dV'
  $$
### 14.3 Condiciones de Frontera Magnetostáticas

- Componente normal de la inducción magnética:
  $$
  \hat{n} \cdot (\vec{B}_1 - \vec{B}_2) = 0 \implies B_{1n} = B_{2n}
  $$
- Componente tangencial de la intensidad magnética:
  $$
  \hat{n} \times (\vec{H}_1 - \vec{H}_2) = \vec{K}_f \implies H_{1t} - H_{2t} = K_f
  $$
### 14.4 Densidad y Energía Magnetostática Total

- Densidad volumétrica de energía magnética:
  $$
  u_m = \frac{1}{2} \vec{B} \cdot \vec{H} = \frac{1}{2\mu_0} B^2
  $$
- Energía magnética total:
  $$
  U = \frac{1}{2} \int_V \vec{A} \cdot \vec{J} \, dV = \frac{1}{2} \int_{\mathrm{todo el espacio}} \vec{B} \cdot \vec{H} \, dV
  $$
## 15. Inducción Electromagnética, Maxwell y Ondas

### 15.1 Ecuaciones de Maxwell en Forma Diferencial

- Forma Microscópica (en el vacío) (1):
  $$
  \nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}
  $$
- Forma Microscópica (en el vacío) (2):
  $$
  \nabla \cdot \vec{B} = 0
  $$
- Forma Microscópica (en el vacío) (3):
  $$
  \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}
  $$
- Forma Microscópica (en el vacío) (4):
  $$
  \nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}
  $$
- Forma Macroscópica (en medios materiales) (1):
  $$
  \nabla \cdot \vec{D} = \rho_f
  $$
- Forma Macroscópica (en medios materiales) (2):
  $$
  \nabla \cdot \vec{B} = 0
  $$
- Forma Macroscópica (en medios materiales) (3):
  $$
  \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}
  $$
- Forma Macroscópica (en medios materiales) (4):
  $$
  \nabla \times \vec{H} = \vec{J}_f + \frac{\partial \vec{D}}{\partial t}
  $$
### 15.2 Potenciales Electrodinámicos y Transformaciones de Calibre

- Definición de potenciales en términos dependientes del tiempo (1):
  $$
  \vec{B} = \nabla \times \vec{A}
  $$
- Definición de potenciales en términos dependientes del tiempo (2):
  $$
  \vec{E} = -\nabla V - \frac{\partial \vec{A}}{\partial t}
  $$
- Transformaciones de calibre (para cualquier función escalar $\lambda(\vec{r}:
  $$
  \vec{A}' = \vec{A} + \nabla \Lambda
  $$
- T)$):
  $$
  V' = V - \frac{\partial \Lambda}{\partial t}
  $$
- Condición de Calibre de Lorenz:
  $$
  \nabla \cdot \vec{A} + \frac{1}{c^2} \frac{\partial V}{\partial t} = 0 \implies \nabla \cdot \vec{A} + \mu_0 \varepsilon_0 \frac{\partial V}{\partial t} = 0
  $$
- Ecuaciones de Onda Inhomogéneas para los Potenciales (en Calibre de Lorenz) (1):
  $$
  \nabla^2 V - \frac{1}{c^2} \frac{\partial^2 V}{\partial t^2} = -\frac{\rho}{\varepsilon_0} \iff \Box V = -\frac{\rho}{\varepsilon_0}
  $$
- Ecuaciones de Onda Inhomogéneas para los Potenciales (en Calibre de Lorenz) (2):
  $$
  \nabla^2 \vec{A} - \frac{1}{c^2} \frac{\partial^2 \vec{A}}{\partial t^2} = -\mu_0 \vec{J} \iff \Box \vec{A} = -\mu_0 \vec{J}
  $$
- Ecuaciones de Onda Inhomogéneas para los Potenciales (en Calibre de Lorenz) (3):
  $$
  (\Box = \nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2} = \mathrm{Operador d'Alembertiano})
  $$
- Potenciales Retardados de Liénard-Wiechert (Tiempo retardado $t_r = t - |\vec{r} - \vec{r}'|/c$) (1):
  $$
  V(\vec{r}, t) = \frac{1}{4\pi\varepsilon_0} \int \frac{\rho(\vec{r}', t_r)}{|\vec{r} - \vec{r}'|} dV'
  $$
- Potenciales Retardados de Liénard-Wiechert (Tiempo retardado $t_r = t - |\vec{r} - \vec{r}'|/c$) (2):
  $$
  \vec{A}(\vec{r}, t) = \frac{\mu_0}{4\pi} \int \frac{\vec{J}(\vec{r}', t_r)}{|\vec{r} - \vec{r}'|} dV'
  $$
### 15.3 Ondas Electromagnéticas Planas en el Vacío

- Ecuaciones de Onda Homogéneas (1):
  $$
  \nabla^2 \vec{E} - \frac{1}{c^2} \frac{\partial^2 \vec{E}}{\partial t^2} = \vec{0}
  $$
- Ecuaciones de Onda Homogéneas (2):
  $$
  \nabla^2 \vec{B} - \frac{1}{c^2} \frac{\partial^2 \vec{B}}{\partial t^2} = \vec{0}
  $$
- Velocidad de la luz en el vacío:
  $$
  c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 2.9979 \times 10^8 \, \frac{\mathrm{m}}{\mathrm{s}}
  $$
- Solución de Onda Plana Monocromática ($\vec{k} = \mathrm{vector de onda}$) (1):
  $$
  \vec{E}(\vec{r}, t) = \vec{E}_0 e^{i(\vec{k} \cdot \vec{r} - \omega t)}
  $$
- Solución de Onda Plana Monocromática ($\vec{k} = \mathrm{vector de onda}$) (2):
  $$
  \vec{B}(\vec{r}, t) = \vec{B}_0 e^{i(\vec{k} \cdot \vec{r} - \omega t)}
  $$
- Solución de Onda Plana Monocromática ($\vec{k} = \mathrm{vector de onda}$) (3):
  $$
  \vec{B}_0 = \frac{1}{\omega} (\vec{k} \times \vec{E}_0) = \frac{1}{c} (\hat{k} \times \vec{E}_0)
  $$
- Solución de Onda Plana Monocromática ($\vec{k} = \mathrm{vector de onda}$) (4):
  $$
  \vec{k} \cdot \vec{E}_0 = 0
  $$
- Solución de Onda Plana Monocromática ($\vec{k} = \mathrm{vector de onda}$) (5):
  $$
  \vec{k} \cdot \vec{B}_0 = 0
  $$
- Impedancia Característica del Vacío ($\eta_0$):
  $$
  \eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 120\pi \, \Omega \approx 376.73 \, \Omega
  $$
### 15.4 Tensor de Esfuerzos de Maxwell ($T_{ij}$) y Momento Electromagnético

- Tensor de Esfuerzos de Maxwell:
  $$
  T_{ij} = \varepsilon_0 \left( E_i E_j - \frac{1}{2} \delta_{ij} E^2 \right) + \frac{1}{\mu_0} \left( B_i B_j - \frac{1}{2} \delta_{ij} B^2 \right)
  $$
- Ley de Conservación del Momento Lineal (1):
  $$
  \vec{f}_{\mathrm{Lorentz}} + \frac{\partial \vec{g}}{\partial t} = \nabla \cdot \mathbf{T}
  $$
- Ley de Conservación del Momento Lineal (2):
  $$
  \vec{g} = \varepsilon_0 (\vec{E} \times \vec{B}) = \frac{\vec{S}}{c^2} \quad (\mathrm{Densidad de Momento})
  $$
- Presión de Radiación ($P_{\mathrm{rad}}$ para incidencia normal) (1):
  $$
  P_{\mathrm{rad}} = \frac{I}{c} \quad (\mathrm{Absorción total})
  $$
- Presión de Radiación ($P_{\mathrm{rad}}$ para incidencia normal) (2):
  $$
  P_{\mathrm{rad}} = \frac{2I}{c} \quad (\mathrm{Reflexión total})
  $$
### 15.5 Formulación Covariante / Cuadrivectorial de la Electrodinámica (Métrica $\eta_{\mu\nu} = \operatorname{diag}(+1, -1, -1, -1)$)

- Cuadrivector Posición, Gradiente y Corriente (1):
  $$
  x^\mu = (ct, \vec{r})
  $$
- Cuadrivector Posición, Gradiente y Corriente (2):
  $$
  \partial_\mu = \left( \frac{1}{c}\frac{\partial}{\partial t}, \nabla \right)
  $$
- Cuadrivector Posición, Gradiente y Corriente (3):
  $$
  \partial^\mu = \left( \frac{1}{c}\frac{\partial}{\partial t}, -\nabla \right)
  $$
- Cuadrivector Posición, Gradiente y Corriente (4):
  $$
  J^\mu = (c\rho, \vec{J})
  $$
- Cuadripotencial (1):
  $$
  A^\mu = \left( \frac{V}{c}, \vec{A} \right)
  $$
- Cuadripotencial (2):
  $$
  A_\mu = \left( \frac{V}{c}, -\vec{A} \right)
  $$
- Tensor de Campo Electromagnético de Faraday ($F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$):
  $$
  F^{\mu\nu} = \begin{bmatrix} 0 & -E_x/c & -E_y/c & -E_z/c \\ E_x/c & 0 & -B_z & B_y \\ E_y/c & B_z & 0 & -B_x \\ E_z/c & -B_y & B_x & 0 \end{bmatrix}
  $$
- Tensor Dual de Campo Electromagnético ($\tilde{F}^{\mu\nu} = \frac{1}{2} \epsilon^{\mu\nu\alpha\beta} F_{\alpha\beta}$):
  $$
  \tilde{F}^{\mu\nu} = \begin{bmatrix} 0 & -B_x & -B_y & -B_z \\ B_x & 0 & E_z/c & -E_y/c \\ B_y & -E_z/c & 0 & E_x/c \\ B_z & E_y/c & -E_x/c & 0 \end{bmatrix}
  $$
- Ecuaciones de Maxwell Covariantes (1):
  $$
  \partial_\mu F^{\mu\nu} = \mu_0 J^\nu \quad (\mathrm{Gauss y Ampère-Maxwell})
  $$
- Ecuaciones de Maxwell Covariantes (2):
  $$
  \partial_\mu \tilde{F}^{\mu\nu} = 0 \quad (\mathrm{Gauss Magnética y Faraday})
  $$
- Invariantes de Lorentz del Campo Electromagnético (1):
  $$
  I_1 = F^{\mu\nu} F_{\mu\nu} = 2 \left( B^2 - \frac{E^2}{c^2} \right) = \mathrm{invariante}
  $$
- Invariantes de Lorentz del Campo Electromagnético (2):
  $$
  I_2 = \epsilon_{\mu\nu\alpha\beta} F^{\mu\nu} F^{\alpha\beta} = -\frac{4}{c} (\vec{E} \cdot \vec{B}) = \mathrm{invariante}
  $$
# Compendio V: Óptica y Luz
*(Nivel Avanzado)*

## 16. Óptica Geométrica y Sistemas Ópticos

### 16.1 Óptica Matricial (Matrices de Rayos ABCD)

- Vector de rayo paraxial (altura $y$:
  $$
  \begin{bmatrix} y_2 \\ \theta_2 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} y_1 \\ \theta_1 \end{bmatrix}
  $$
- Ángulo $\theta$ respecto al eje óptico):
  $$
  \det\left( \mathbf{M} \right) = AD - BC = \frac{n_1}{n_2}
  $$
- Matriz de Traslación Libre en Medio Homogéneo (distancia $d$):
  $$
  \mathbf{M}_{\mathrm{tras}} = \begin{bmatrix} 1 & d \\ 0 & 1 \end{bmatrix}
  $$
- Matriz de Refracción en Interfaz Plana:
  $$
  \mathbf{M}_{\mathrm{ref,plana}} = \begin{bmatrix} 1 & 0 \\ 0 & \frac{n_1}{n_2} \end{bmatrix}
  $$
- Matriz de Refracción en Dioptrio Esférico:
  $$
  \mathbf{M}_{\mathrm{dioptrio}} = \begin{bmatrix} 1 & 0 \\ -\frac{n_2 - n_1}{n_2 R} & \frac{n_1}{n_2} \end{bmatrix}
  $$
- Matriz de Lente Delgada:
  $$
  \mathbf{M}_{\mathrm{lente}} = \begin{bmatrix} 1 & 0 \\ -\frac{1}{f} & 1 \end{bmatrix}
  $$
- Matriz de Espejo Esférico:
  $$
  \mathbf{M}_{\mathrm{espejo}} = \begin{bmatrix} 1 & 0 \\ -\frac{2}{R} & 1 \end{bmatrix}
  $$
### 16.2 Principio Variacional y Óptica Hamiltoniana

- Principio de Fermat (Camino Óptico Estacionario):
  $$
  \delta \mathcal{S} = \delta \int_{P_1}^{P_2} n(\vec{r}) \, ds = 0
  $$
- Longitud de Camino Óptico (OPL):
  $$
  \mathrm{OPL} = \int_C n(\vec{r}) \, ds
  $$
- Ecuación Diferencial del Rayo:
  $$
  \frac{d}{ds}\left( n \frac{d\vec{r}}{ds} \right) = \nabla n
  $$
- Ecuación de la Eikonal (Límite de longitud de onda cero $\lambda \to 0$ para fase $S$):
  $$
  |\nabla S|^2 = n^2(\vec{r})
  $$
## 17. Óptica Ondulatoria (Interferencia, Difracción y Polarización)

### 17.1 Teoría Escalar de Difracción (Fresnel y Kirchhoff)

- Integral de Difracción de Fresnel-Kirchhoff:
  $$
  U(P) = -\frac{i}{2\lambda} \iint_{\Sigma} U_0 \frac{e^{i k r}}{r} [\cos(\hat{n}, \vec{r}) - \cos(\hat{n}, \vec{r}_0)] dS
  $$
- Integral de Difracción de Fresnel (Paraxial en distancia $z$):
  $$
  U(x, y, z) = \frac{e^{i k z}}{i \lambda z} \iint_{-\infty}^{\infty} U(\xi, \eta, 0) \exp\left\{ \frac{i k}{2z}\left[ (x - \xi)^2 + (y - \eta)^2 \right] \right\} d\xi d\eta
  $$
- Número de Fresnel ($N_F$):
  $$
  N_F = \frac{a^2}{\lambda z} \quad (N_F \gg 1 \mathrm{ Ópt. Geométrica}, \, N_F \sim 1 \mathrm{ Fresnel}, \, N_F \ll 1 \mathrm{ Fraunhofer})
  $$
- Difracción de Fraunhofer como Transformada de Fourier:
  $$
  U(x, y) \propto \mathcal{F}\{U(\xi, \eta)\}\Big|_{f_x = \frac{x}{\lambda z}, f_y = \frac{y}{\lambda z}}
  $$
### 17.2 Formalismo de Polarización (Jones y Stokes-Mueller)

- Vector de Jones para Estados de Polarización Totalmente Coherentes:
  $$
  \vec{J} = \begin{bmatrix} E_{0x} e^{i\phi_x} \\ E_{0y} e^{i\phi_y} \end{bmatrix}
  $$
- Matrices de Jones de Elementos Ópticos Clásicos (1):
  $$
  \mathbf{M}_{\mathrm{pol,H}} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}
  $$
- Matrices de Jones de Elementos Ópticos Clásicos (2):
  $$
  \mathbf{M}_{\mathrm{retardador}}(\Gamma) = \begin{bmatrix} e^{i\Gamma/2} & 0 \\ 0 & e^{-i\Gamma/2} \end{bmatrix}
  $$
- Parámetros de Stokes (Para luz arbitraria o parcialmente polarizada) (1):
  $$
  S_0 = I = I_H + I_V
  $$
- Parámetros de Stokes (Para luz arbitraria o parcialmente polarizada) (2):
  $$
  S_1 = Q = I_H - I_V
  $$
- Parámetros de Stokes (Para luz arbitraria o parcialmente polarizada) (3):
  $$
  S_2 = U = I_{+45^\circ} - I_{-45^\circ}
  $$
- Parámetros de Stokes (Para luz arbitraria o parcialmente polarizada) (4):
  $$
  S_3 = V = I_R - I_L
  $$
- Grado de Polarización ($DOP$):
  $$
  \mathrm{DOP} = \frac{\sqrt{S_1^2 + S_2^2 + S_3^2}}{S_0} \le 1
  $$
- Ecuación de Transformación de Mueller:
  $$
  \vec{S}_{\mathrm{sal}} = \mathbf{M}_{\mathrm{Mueller}} \vec{S}_{\mathrm{ent}}
  $$
### 17.3 Birrefringencia y Óptica de Cristales Anisótropos

- Elipsoide de Índices Ópticos (Indicatriz Óptica):
  $$
  \frac{x^2}{n_x^2} + \frac{y^2}{n_y^2} + \frac{z^2}{n_z^2} = 1
  $$
- Retardo de Fase en Lámina Birrefringente de Espesor $d$ (1):
  $$
  \Delta\phi = \Gamma = \frac{2\pi}{\lambda} |n_e - n_o| d
  $$
- Retardo de Fase en Lámina Birrefringente de Espesor $d$ (2):
  $$
  \mathrm{Lámina de Cuarto de Onda: } d = \frac{\lambda}{4|n_e - n_o|}
  $$
- Retardo de Fase en Lámina Birrefringente de Espesor $d$ (3):
  $$
  \mathrm{Lámina de Media Onda: } d = \frac{\lambda}{2|n_e - n_o|}
  $$
## 18. Óptica Electromagnética, Dispersión y Guías de Ondas

### 18.1 Modelo Microeléctrico de Lorentz-Drude y Relaciones Dispersivas

- Permitividad Relativa Compleja del Modelo de Oscilador de Lorentz:
  $$
  \tilde{\varepsilon}_r(\omega) = 1 + \frac{N q^2}{\varepsilon_0 m_e} \sum_j \frac{f_j}{\omega_{0j}^2 - \omega^2 - i\gamma_j \omega}
  $$
- Frecuencia de Plasma (Metales / Modelo de Drude $\omega_{0} = 0$):
  $$
  \omega_p^2 = \frac{N e^2}{\varepsilon_0 m_e} \implies \varepsilon(\omega) = 1 - \frac{\omega_p^2}{\omega^2 + i\gamma\omega}
  $$
- Relaciones de Kramers-Kronig (Causalidad en la respuesta dieléctrica) (1):
  $$
  \mathrm{Re}[\chi(\omega)] = \frac{2}{\pi} \mathcal{P} \int_0^\infty \frac{\Omega \, \mathrm{Im}[\chi(\Omega)]}{\Omega^2 - \omega^2} d\Omega
  $$
- Relaciones de Kramers-Kronig (Causalidad en la respuesta dieléctrica) (2):
  $$
  \mathrm{Im}[\chi(\omega)] = -\frac{2\omega}{\pi} \mathcal{P} \int_0^\infty \frac{\mathrm{Re}[\chi(\Omega)]}{\Omega^2 - \omega^2} d\Omega
  $$
### 18.2 Fibras Ópticas y Guías de Ondas Dieléctricas

- Apertura Numérica ($\mathrm{NA}$) (1):
  $$
  \mathrm{NA} = \sen(\theta_{\mathrm{máx}}) = \sqrt{n_{\mathrm{núcleo}}^2 - n_{\mathrm{revestimiento}}^2} \approx n_1 \sqrt{2\Delta}
  $$
- Apertura Numérica ($\mathrm{NA}$) (2):
  $$
  \Delta = \frac{n_1 - n_2}{n_1}
  $$
- Parámetro de Frecuencia Normalizada (Número $V$ para fibra de radio $a$):
  $$
  V = \frac{2\pi a}{\lambda_0} \sqrt{n_1^2 - n_2^2} = \frac{2\pi a}{\lambda_0} \mathrm{NA}
  $$
- Condición de Monomodo en Fibra de Índice Escalonado:
  $$
  V < 2.4048 \quad (\mathrm{Primer cero de la función de Bessel } J_0)
  $$
- Número Aproximado de Modos en Fibra Multimodo de Índice Escalonado ($V \gg 1$):
  $$
  M \approx \frac{V^2}{2}
  $$
### 18.3 Ondas Evanescentes en Reflexión Total Interna

- Vector de onda transversal transmitido imaginario:
  $$
  k_{tz} = i \alpha = i k_0 \sqrt{n_1^2 \sin^2(\theta_i) - n_2^2}
  $$
- Decaimiento de la Amplitud del Campo Evanescente:
  $$
  \vec{E}_t(z) = \vec{E}_{t0} e^{-\alpha z} e^{i(k_{tx} x - \omega t)}
  $$
- Desplazamiento Lateral de Goos-Hänchen (Polarización s / TE cerca del ángulo crítico) (1):
  $$
  \Delta x_{\mathrm{GH}} = \frac{2}{k_0 \sqrt{n_1^2 \sin^2(\theta_i) - n_2^2}}
  $$
- Desplazamiento Lateral de Goos-Hänchen (Polarización s / TE cerca del ángulo crítico) (2):
  $$
  \left( \mathrm{Formulación general: } \Delta x_{\mathrm{GH}} = -\frac{d\phi}{dk_x} \right)
  $$
## 19. Óptica Cuántica, Radiación, Haces Láser y No Lineal

### 19.1 Propagación de Haces Gaussianos ($\mathrm{TEM}_{00}$)

- Parámetro de Rayleigh / Distancia Confocal ($z_R$):
  $$
  z_R = \frac{\pi w_0^2}{\lambda_0}
  $$
- Cintura y Perfil del Radio del Haz ($w(z)$ con cintura mínima $w_0$ en $z=0$):
  $$
  w(z) = w_0 \sqrt{1 + \left( \frac{z}{z_R} \right)^2}
  $$
- Radio de Curvatura del Frente de Onda ($R(z)$):
  $$
  R(z) = z \left[ 1 + \left( \frac{z_R}{z} \right)^2 \right]
  $$
- Divergencia Angular de Campo Lejano ($\theta_{\mathrm{div}}$):
  $$
  \theta_{\mathrm{div}} = \lim_{z \to \infty} \frac{w(z)}{z} = \frac{\lambda_0}{\pi w_0}
  $$
- Fase de Gouy:
  $$
  \zeta(z) = \arctan\left( \frac{z}{z_R} \right)
  $$
- Parámetro Complejo del Haz $q(z)$ y Transformación $ABCD$:
  $$
  \frac{1}{q(z)} = \frac{1}{R(z)} - i \frac{\lambda_0}{\pi n w^2(z)} \implies q_2 = \frac{A q_1 + B}{C q_1 + D}
  $$
### 19.2 Óptica No Lineal

- Expansión de la Polarización No Lineal:
  $$
  \vec{P} = \varepsilon_0 \left( \chi^{(1)} \cdot \vec{E} + \chi^{(2)} : \vec{E} \vec{E} + \chi^{(3)} \vdots \vec{E} \vec{E} \vec{E} + \dots \right) = \vec{P}_L + \vec{P}_{\mathrm{NL}}
  $$
- Generación de Segundo Armónico (SHG):
  $$
  P^{(2)}(2\omega) = \varepsilon_0 \chi^{(2)} E^2(\omega)
  $$
- Condición de Ajuste de Fase (Phase Matching):
  $$
  \Delta k = k(2\omega) - 2k(\omega) = 0 \implies n(2\omega) = n(\omega)
  $$
- Efecto Kerr Óptico (Índice de refracción dependiente de la intensidad) (1):
  $$
  n(I) = n_0 + n_2 I
  $$
- Efecto Kerr Óptico (Índice de refracción dependiente de la intensidad) (2):
  $$
  n_2 = \frac{3 \chi^{(3)}}{4 \varepsilon_0 c n_0^2}
  $$
- Efecto Pockels (Lineal electro-óptico):
  $$
  \Delta\left(\frac{1}{n^2}\right) = r_{ijk} E_k
  $$
- Efecto Kerr Electro-óptico (Cuadrático electro-óptico):
  $$
  \Delta n = \lambda K_{\mathrm{Kerr}} E^2
  $$
# Compendio VI: Física Moderna
*(Nivel Avanzado)*

## 20. Teoría de la Relatividad (Especial y General)

### 20.1 Elementos de Relatividad General

- Principio de Equivalencia y Desplazamiento al Rojo Gravitacional:
  $$
  \frac{\Delta f}{f_0} = \frac{\Delta\Phi_g}{c^2} \implies f(r) = f_\infty \sqrt{1 - \frac{2GM}{c^2 r}}
  $$
- Métrica General del Espacio-Tiempo Curvo:
  $$
  ds^2 = g_{\mu\nu} dx^\mu dx^\nu
  $$
- Símbolos de Christoffel (Conexión Levi-Civita):
  $$
  \Gamma^\mu_{\alpha\beta} = \frac{1}{2} g^{\mu\sigma} \left( \frac{\partial g_{\sigma\alpha}}{\partial x^\beta} + \frac{\partial g_{\sigma\beta}}{\partial x^\alpha} - \frac{\partial g_{\alpha\beta}}{\partial x^\sigma} \right)
  $$
- Ecuación de las Geodésicas:
  $$
  \frac{d^2 x^\mu}{d\lambda^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\lambda} \frac{dx^\beta}{d\lambda} = 0
  $$
- Tensor de Curvatura de Riemann:
  $$
  R^\rho_{\ \sigma\mu\nu} = \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda} \Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda} \Gamma^\lambda_{\mu\sigma}
  $$
- Tensor de ricci:
  $$
  R_{\mu\nu} = R^\lambda_{\ \mu\lambda\nu}
  $$
- Escalar de curvatura:
  $$
  R = g^{\mu\nu} R_{\mu\nu}
  $$
- Ecuaciones de Campo de Einstein (1):
  $$
  G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
  $$
- Ecuaciones de Campo de Einstein (2):
  $$
  G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu}
  $$
- Métrica de Schwarzschild (Masa esférica estática en el vacío):
  $$
  ds^2 = -\left( 1 - \frac{r_s}{r} \right) c^2 dt^2 + \left( 1 - \frac{r_s}{r} \right)^{-1} dr^2 + r^2 (d\theta^2 + \sen^2\theta \, d\phi^2)
  $$
- Radio de Schwarzschild (Horizonte de sucesos):
  $$
  r_s = \frac{2GM}{c^2}
  $$
## 21. Mecánica Cuántica y Física Atómica

### 21.1 Formalismo de Dirac (Bra-Ket), Postulados y Espacio de Hilbert

- Valor Esperado de un Observable $\hat{A}$ en el Estado $|\psi\rangle$:
  $$
  \langle A \rangle = \frac{\langle\psi|\hat{A}|\psi\rangle}{\langle\psi|\psi\rangle}
  $$
- Relación Generalizada de Incertidumbre de Robertson-Schrödinger:
  $$
  \sigma_A \sigma_B \ge \frac{1}{2} |\langle [\hat{A}, \hat{B}] \rangle|
  $$
- Relación de Conmutación Canónica:
  $$
  [\hat{x}_j, \hat{p}_k] = i\hbar \delta_{jk}
  $$
- Ecuación de Movimiento de Heisenberg para un Operador $\hat{A}$:
  $$
  \frac{d\hat{A}_H}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{A}_H] + \left( \frac{\partial\hat{A}}{\partial t} \right)_H
  $$
### 21.2 Espín $1/2$ y Matrices de Pauli ($\hat{\vec{S}} = \frac{\hbar}{2}\vec{\sigma}$)

- Matrices de Pauli (1):
  $$
  \sigma_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
  $$
- Matrices de Pauli (2):
  $$
  \sigma_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}
  $$
- Matrices de Pauli (3):
  $$
  \sigma_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}
  $$
- Álgebra de Pauli (1):
  $$
  \sigma_i \sigma_j = \delta_{ij} I + i \sum_k \epsilon_{ijk} \sigma_k
  $$
- Álgebra de Pauli (2):
  $$
  [\sigma_i, \sigma_j] = 2i \epsilon_{ijk} \sigma_k
  $$
- Álgebra de Pauli (3):
  $$
  \{\sigma_i, \sigma_j\} = 2\delta_{ij} I
  $$
- Momento Magnético de Espín (1):
  $$
  \vec{\mu}_s = -g_s \frac{e}{2m_e}\vec{S} \approx -\frac{e}{m_e}\vec{S} = -\mu_B \vec{\sigma}
  $$
- Momento Magnético de Espín (2):
  $$
  \mu_B = \frac{e\hbar}{2m_e} \quad (\mathrm{Magnetón de Bohr})
  $$
### 21.3 Teoría de Perturbaciones y Métodos de Aproximación

- Perturbaciones Estacionarias No Degeneradas (1er y 2do orden) (1):
  $$
  E_n^{(1)} = \langle n^{(0)} | \hat{H}' | n^{(0)} \rangle
  $$
- Perturbaciones Estacionarias No Degeneradas (1er y 2do orden) (2):
  $$
  E_n^{(2)} = \sum_{k \neq n} \frac{|\langle k^{(0)} | \hat{H}' | n^{(0)} \rangle|^2}{E_n^{(0)} - E_k^{(0)}}
  $$
- Perturbaciones Estacionarias No Degeneradas (1er y 2do orden) (3):
  $$
  |n^{(1)}\rangle = \sum_{k \neq n} \frac{\langle k^{(0)} | \hat{H}' | n^{(0)} \rangle}{E_n^{(0)} - E_k^{(0)}} |k^{(0)}\rangle
  $$
- Regla de Oro de Fermi (Tasa de transición dependiente del tiempo):
  $$
  \Gamma_{i \to f} = W_{i \to f} = \frac{2\pi}{\hbar} |\langle f | \hat{H}' | i \rangle|^2 \rho(E_f)
  $$
### 21.4 Mecánica Cuántica Relativista

- Ecuación de Klein-Gordon (Partículas escalares de espín 0 con $\Box = \nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}$) (1):
  $$
  \left( \Box - \frac{m^2 c^2}{\hbar^2} \right) \phi = 0 \iff \nabla^2\phi - \frac{1}{c^2}\frac{\partial^2\phi}{\partial t^2} = \left(\frac{mc}{\hbar}\right)^2 \phi
  $$
- Ecuación de Klein-Gordon (Partículas escalares de espín 0 con $\Box = \nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}$) (2):
  $$
  \left( \mathrm{O con firma } \Box = \frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2 = \partial_\mu \partial^\mu:
  $$
- Ecuación de Klein-Gordon (Partículas escalares de espín 0 con $\Box = \nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}$) (3):
  $$
  \left(\Box + \frac{m^2 c^2}{\hbar^2}\right)\phi = 0 \right)
  $$
- Ecuación de Dirac (Fermiones de espín 1/2 en representación covariante):
  $$
  (i\gamma^\mu \partial_\mu - \frac{mc}{\hbar})\psi = 0 \iff (i\hbar \gamma^\mu \partial_\mu - mc)\psi = 0
  $$
- Álgebra de Clifford para las Matrices Gamma de Dirac ($\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu} I_{4\times4}$) (1):
  $$
  \gamma^0 = \begin{bmatrix} I & 0 \\ 0 & -I \end{bmatrix}
  $$
- Álgebra de Clifford para las Matrices Gamma de Dirac ($\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu} I_{4\times4}$) (2):
  $$
  \gamma^k = \begin{bmatrix} 0 & \sigma_k \\ -\sigma_k & 0 \end{bmatrix}
  $$
- Álgebra de Clifford para las Matrices Gamma de Dirac ($\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu} I_{4\times4}$) (3):
  $$
  \gamma^5 = i\gamma^0 \gamma^1 \gamma^2 \gamma^3 = \begin{bmatrix} 0 & I \\ I & 0 \end{bmatrix}
  $$
## 22. Física Nuclear, Radiactividad y Partículas Elementales

### 22.1 Física de Partículas y Modelo Estándar

- Potencial Nuclear Fuerte de Yukawa (Mediado por mesones de masa $m_\pi$) (1):
  $$
  V(r) = -g^2 \frac{e^{-\mu r}}{r} = -g^2 \frac{e^{-r / \lambda_C}}{r}
  $$
- Potencial Nuclear Fuerte de Yukawa (Mediado por mesones de masa $m_\pi$) (2):
  $$
  \mu = \frac{m_\pi c}{\hbar}
  $$
- Fórmula de Gell-Mann-Nishijima (Carga, Isoespín, Hipercarga y Número Bariónico) (1):
  $$
  Q = I_3 + \frac{Y}{2} = I_3 + \frac{B + S + C + B' + T}{2}
  $$
- Fórmula de Gell-Mann-Nishijima (Carga, Isoespín, Hipercarga y Número Bariónico) (2):
  $$
  (\mathrm{donde } B = \mathrm{bariónico}, \, S = \mathrm{extrañeza}, \, C = \mathrm{encanto}, \, B' = \mathrm{bottomness/belleza}, \, T = \mathrm{topness/verdad})
  $$
- Matriz CKM (Cabibbo-Kobayashi-Maskawa para mezcla de quarks):
  $$
  \begin{bmatrix} d' \\ s' \\ b' \end{bmatrix} = \mathbf{V}_{\mathrm{CKM}} \begin{bmatrix} d \\ s \\ b \end{bmatrix} = \begin{bmatrix} V_{ud} & V_{us} & V_{ub} \\ V_{cd} & V_{cs} & V_{cb} \\ V_{td} & V_{ts} & V_{tb} \end{bmatrix} \begin{bmatrix} d \\ s \\ b \end{bmatrix}
  $$
- Relación de Dispersión de Breit-Wigner (Resonancia de desintegración con anchura $\Gamma$) (1):
  $$
  \sigma(E) = \frac{\pi}{k^2} \frac{g \Gamma_{\mathrm{in}} \Gamma_{\mathrm{out}}}{(E - E_0)^2 + (\Gamma/2)^2}
  $$
- Relación de Dispersión de Breit-Wigner (Resonancia de desintegración con anchura $\Gamma$) (2):
  $$
  \tau = \frac{\hbar}{\Gamma}
  $$
## 23. Física del Estado Sólido y Materia Condensada

### 23.1 Teoría de Bandas y Semiconductores

- Teorema de Bloch para Electrones en un Potencial Periódico ($V(\vec{r} + \vec{R}) = V(\vec{r})$) (1):
  $$
  \psi_{\vec{k}}(\vec{r}) = e^{i\vec{k} \cdot \vec{r}} u_{\vec{k}}(\vec{r})
  $$
- Teorema de Bloch para Electrones en un Potencial Periódico ($V(\vec{r} + \vec{R}) = V(\vec{r})$) (2):
  $$
  u_{\vec{k}}(\vec{r} + \vec{R}) = u_{\vec{k}}(\vec{r})
  $$
- Tensor de Masa Efectiva del Portador:
  $$
  \left( \frac{1}{m^*} \right)_{ij} = \frac{1}{\hbar^2} \frac{\partial^2 E(\vec{k})}{\partial k_i \partial k_j}
  $$
- Concentración Intrínseca de Portadores en Semiconductores ($E_g = \mathrm{Banda prohibida / Bandgap}$) (1):
  $$
  n_i = \sqrt{N_c N_v} \exp\left( -\frac{E_g}{2 k_B T} \right)
  $$
- Concentración Intrínseca de Portadores en Semiconductores ($E_g = \mathrm{Banda prohibida / Bandgap}$) (2):
  $$
  N_c = 2\left( \frac{m_e^* k_B T}{2\pi\hbar^2} \right)^{3/2}
  $$
- Concentración Intrínseca de Portadores en Semiconductores ($E_g = \mathrm{Banda prohibida / Bandgap}$) (3):
  $$
  N_v = 2\left( \frac{m_h^* k_B T}{2\pi\hbar^2} \right)^{3/2}
  $$
- Ley de Acción de Masas en Semiconductores:
  $$
  n \cdot p = n_i^2
  $$
- Nivel de Fermi Intrínseco:
  $$
  E_{Fi} = \frac{E_c + E_v}{2} + \frac{3}{4} k_B T \ln\left( \frac{m_h^*}{m_e^*} \right)
  $$
### 23.2 Fonones y Propiedades Térmicas de la Red

- Modelo de Debye para la Capacidad Calorífica de la Red ($T \ll \Theta_D$) (1):
  $$
  C_v = \frac{12\pi^4}{5} N k_B \left( \frac{T}{\Theta_D} \right)^3 \propto T^3
  $$
- Modelo de Debye para la Capacidad Calorífica de la Red ($T \ll \Theta_D$) (2):
  $$
  \Theta_D = \frac{\hbar v_s}{k_B}(6\pi^2 n)^{1/3}
  $$
- Modelo de Einstein para la Capacidad Calorífica (1):
  $$
  C_v = 3 N k_B \left( \frac{\Theta_E}{T} \right)^2 \frac{e^{\Theta_E / T}}{(e^{\Theta_E / T} - 1)^2}
  $$
- Modelo de Einstein para la Capacidad Calorífica (2):
  $$
  \Theta_E = \frac{\hbar\omega_E}{k_B}
  $$
### 23.3 Superconductividad (Teoría Clásica de London y BCS)

- Ecuaciones de London ($\lambda_L = \mathrm{longitud de penetración de London}$) (1):
  $$
  \frac{\partial \vec{J}_s}{\partial t} = \frac{n_s e^2}{m} \vec{E}
  $$
- Ecuaciones de London ($\lambda_L = \mathrm{longitud de penetración de London}$) (2):
  $$
  \nabla \times \vec{J}_s = -\frac{n_s e^2}{m}\vec{B} \implies \nabla^2\vec{B} = \frac{1}{\lambda_L^2}\vec{B}
  $$
- Efecto Meissner (Atenuación exponencial del campo magnético en el superconductor) (1):
  $$
  B(x) = B_0 \exp\left( -\frac{x}{\lambda_L} \right)
  $$
- Efecto Meissner (Atenuación exponencial del campo magnético en el superconductor) (2):
  $$
  \lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}}
  $$
- Campo Magnético Crítico Termodinámico:
  $$
  B_c(T) = B_c(0)\left[ 1 - \left( \frac{T}{T_c} \right)^2 \right]
  $$
- Brecha de Energía Superconductora BCS a $T = 0\mathrm{ K}$:
  $$
  \Delta(0) \approx 1.764 \, k_B T_c
  $$
- Longitud de Coherencia de Cooper / BCS ($\xi_0$):
  $$
  \xi_0 = \frac{\hbar v_F}{\pi \Delta(0)}
  $$
