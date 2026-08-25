---
file: docs/fisica/formulario_fisica.md
description: Compendio exhaustivo de fórmulas de física desde nivel básico hasta nivel avanzado/universitario.
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/symbols.py
relations:
  - docs/mates/formulario_mates.md
  - docs/ARCHITECTURE.md
keywords:
  - compendio-fisica
  - formulas-fisica
  - mecanica-clasica
  - termodinamica
  - electromagnetismo
  - mecanica-cuantica
---

# Compendio I: Mecánica Clásica, de Fluidos y Analítica
*(Nivel Básico a Universitario)*

## 1. Cinemática y Dinámica Newtoniana

### Nivel Básico

#### 1.1 Movimiento Rectilíneo Uniforme (MRU)

- Posición en función del tiempo:
  $$x(t) = x_0 + v \cdot t$$
- Velocidad media:
  $$v_m = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}$$

#### 1.2 Movimiento Rectilíneo Uniformemente Acelerado (MRUA)

- Velocidad:
  $$v(t) = v_0 + a \cdot t$$
- Posición:
  $$x(t) = x_0 + v_0 t + \frac{1}{2} a t^2$$
- Ecuación independiente del tiempo (Torricelli):
  $$v_f^2 = v_0^2 + 2a (x_f - x_0)$$
- Desplazamiento medio:
  $$\Delta x = \left( \frac{v_0 + v_f}{2} \right) t$$

#### 1.3 Leyes del Movimiento de Newton

- Primera Ley (Inercia):
  $$\sum \vec{F} = \vec{0} \iff \vec{v} = \text{constante}$$
- Segunda Ley (Ley Fundamental de la Dinámica):
  $$\sum \vec{F} = m \vec{a} = \frac{d\vec{p}}{dt}$$
- Tercera Ley (Acción y Reacción):
  $$\vec{F}_{AB} = -\vec{F}_{BA}$$

#### 1.4 Fuerzas de Fricción / Rozamiento

- Fricción estática máxima:
  $$f_{s,\text{máx}} = \mu_s N \quad \implies \quad f_s \le \mu_s N$$
- Fricción cinética:
  $$f_k = \mu_k N$$

#### 1.5 Movimiento Circular Uniforme (MCU) y Uniformemente Variado (MCUV)

- Relaciones lineales y angulares:
  $$s = \theta \cdot r, \quad v = \omega \cdot r, \quad a_t = \alpha \cdot r$$
- Aceleración centrípeta / normal:
  $$a_c = \frac{v^2}{r} = \omega^2 r$$
- Cinemática angular con $\alpha$ constante:
  $$\omega(t) = \omega_0 + \alpha t, \quad \theta(t) = \theta_0 + \omega_0 t + \frac{1}{2} \alpha t^2, \quad \omega_f^2 = \omega_0^2 + 2\alpha (\theta_f - \theta_0)$$

### Nivel Intermedio

#### 1.6 Cinemática y Dinámica Vectorial Tridimensional

- Vectores cinemáticos fundamentales:
  $$\vec{v}(t) = \frac{d\vec{r}}{dt}, \quad \vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}$$
- Descomposición intrínseca de la aceleración:
  $$\vec{a} = a_t \hat{u}_t + a_n \hat{u}_n = \frac{dv}{dt} \hat{u}_t + \frac{v^2}{\rho} \hat{u}_n$$
- Coordenadas polares planas:
  $$\vec{v} = \dot{r} \hat{u}_r + r \dot{\theta} \hat{u}_\theta$$
  $$\vec{a} = (\ddot{r} - r\dot{\theta}^2)\hat{u}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{u}_\theta$$

#### 1.7 Sistemas de Referencia No Inerciales (Fuerzas Ficticias)

- Aceleración en sistema móvil ($S'$ con origen acelerado $\vec{A}_0 = \frac{d^2\vec{R}_0}{dt^2}$ respecto al marco inercial $S$, y rotando a $\vec{\omega}$):
  $$\vec{a} = \vec{A}_0 + \vec{a}' + \dot{\vec{\omega}} \times \vec{r}' + 2(\vec{\omega} \times \vec{v}') + \vec{\omega} \times (\vec{\omega} \times \vec{r}')$$
- Ecuación de movimiento en el sistema no inercial ($S'$):
  $$m\vec{a}' = \vec{F}_{\text{real}} - m\vec{A}_0 - m\dot{\vec{\omega}} \times \vec{r}' - 2m(\vec{\omega} \times \vec{v}') - m\vec{\omega} \times (\vec{\omega} \times \vec{r}')$$
- Fuerza de Coriolis:
  $$\vec{F}_{\text{Coriolis}} = -2m (\vec{\omega} \times \vec{v}')$$
- Fuerza Centrífuga:
  $$\vec{F}_{\text{centrífuga}} = -m\vec{\omega} \times (\vec{\omega} \times \vec{r}')$$

#### 1.8 Dinámica Rotacional del Cuerpo Rígido (Eje Fijo)

- Momento de torsión / Torque:
  $$\vec{\tau} = \vec{r} \times \vec{F}$$
- Momento de inercia:
  $$I = \sum_i m_i r_i^2 = \int r^2 dm$$
- Ecuación fundamental de la rotación:
  $$\sum \tau = I \alpha$$
- Teorema de los Ejes Paralelos (Steiner):
  $$I = I_{\text{CM}} + M d^2$$
- Teorema de los Ejes Perpendiculares (Cuerpos laminares planos en $xy$):
  $$I_z = I_x + I_y$$

### Nivel Universitario / Avanzado

#### 1.9 Dinámica Tridimensional del Sólido Rígido

- Tensor de Inercia $\mathbf{I}$ (con productos de inercia $I_{ij} = \int x_i x_j dm$):
  $$\mathbf{I} = \begin{bmatrix} I_{xx} & -I_{xy} & -I_{xz} \\ -I_{yx} & I_{yy} & -I_{yz} \\ -I_{zx} & -I_{zy} & I_{zz} \end{bmatrix}, \quad I_{xx} = \int (y^2 + z^2) \, dm, \quad I_{xy} = \int xy \, dm$$
  $$\left( \text{En notación tensorial: } I_{ij} = \int (r^2 \delta_{ij} - x_i x_j) \, dm \right)$$
- Momento angular tridimensional:
  $$\vec{L} = \mathbf{I} \vec{\omega}$$
- Ecuaciones de Euler para el cuerpo rígido (en el sistema de ejes principales):
  $$I_1 \dot{\omega}_1 - (I_2 - I_3)\omega_2 \omega_3 = \tau_1$$
  $$I_2 \dot{\omega}_2 - (I_3 - I_1)\omega_3 \omega_1 = \tau_2$$
  $$I_3 \dot{\omega}_3 - (I_1 - I_2)\omega_1 \omega_2 = \tau_3$$

## 2. Trabajo, Energía, Momento Lineal y Gravitación

### Nivel Básico

#### 2.1 Trabajo y Energía Mecánica

- Trabajo efectuado por fuerza constante:
  $$W = \vec{F} \cdot \Delta\vec{r} = F \Delta r \cos(\theta)$$
- Energía Cinética traslacional:
  $$E_k = \frac{1}{2} m v^2$$
- Energía Potencial Gravitatoria (cerca de la superficie terrestre):
  $$E_{p,\text{grav}} = m g h$$
- Energía Potencial Elástica (Ley de Hooke $F = -kx$):
  $$E_{p,\text{elás}} = \frac{1}{2} k x^2$$
- Teorema del Trabajo y la Energía Cinética:
  $$W_{\text{neto}} = \Delta E_k = \frac{1}{2} m v_f^2 - \frac{1}{2} m v_0^2$$
- Conservación de la Energía Mecánica:
  $$E_m = E_k + E_p \implies \Delta E_m = W_{\text{no conservativas}}$$

#### 2.2 Cantidad de Movimiento e Impulso

- Momento lineal:
  $$\vec{p} = m \vec{v}$$
- Impulso:
  $$\vec{J} = \vec{F}_{\text{prom}} \Delta t = \Delta \vec{p}$$
- Choques unidimensionales y Coeficiente de Restitución ($e$):
  $$e = \frac{v_{2f} - v_{1f}}{v_{1i} - v_{2i}}$$

### Nivel Intermedio

#### 2.3 Mecánica de Sistemas de Partículas

- Trabajo de fuerza variable general:
  $$W = \int_{C} \vec{F} \cdot d\vec{r}$$
- Campos de fuerza conservativos y Potencial:
  $$\vec{F} = -\nabla U = -\left( \frac{\partial U}{\partial x}\hat{i} + \frac{\partial U}{\partial y}\hat{j} + \frac{\partial U}{\partial z}\hat{k} \right)$$
- Centro de Masas (CM):
  $$\vec{R}_{\text{CM}} = \frac{\sum m_i \vec{r}_i}{\sum m_i} = \frac{1}{M}\int \vec{r} \, dm$$
- Teoremas de König:
  $$E_k = \frac{1}{2} M v_{\text{CM}}^2 + E_k' \quad (\text{traslación CM } + \text{ respecto a CM})$$
  $$\vec{L} = \vec{R}_{\text{CM}} \times \vec{P}_{\text{total}} + \vec{L}'$$

#### 2.4 Gravitación Universal y Fuerzas Centrales

- Ley de Gravitación de Newton:
  $$\vec{F}_g = -G \frac{m_1 m_2}{r^2} \hat{u}_r$$
- Energía Potencial Gravitatoria:
  $$U(r) = -G \frac{m_1 m_2}{r}$$
- Leyes de Kepler:
  - 2da Ley (Velocidad areolar constante):
    $$\frac{dA}{dt} = \frac{L}{2m} = \text{constante}$$
  - 3ra Ley:
    $$T^2 = \left( \frac{4\pi^2}{G(M + m)} \right) a^3$$
- Velocidades orbitales y de escape:
  $$v_{\text{orb}} = \sqrt{\frac{GM}{r}}, \quad v_{\text{esc}} = \sqrt{\frac{2GM}{R}}$$

### Nivel Universitario / Avanzado

#### 2.5 Problema de Dos Cuerpos y Fuerzas Centrales

- Masa reducida ($\mu$):
  $$\mu = \frac{m_1 m_2}{m_1 + m_2}$$
- Ecuación de movimiento relativa:
  $$\mu \ddot{\vec{r}} = f(r) \hat{u}_r$$
- Potencial Efectivo:
  $$U_{\text{eff}}(r) = U(r) + \frac{L^2}{2\mu r^2}$$
- Ecuación diferencial de la órbita (Ecuación de Binet para $u = 1/r$):
  $$\frac{d^2 u}{d\theta^2} + u = -\frac{\mu}{L^2 u^2} f\left(\frac{1}{u}\right)$$
- Ecuación de las cónicas orbitales ($p = \text{semilatus rectum}$, $e = \text{excentricidad}$ para $U(r) = -G m_1 m_2 / r$):
  $$r(\theta) = \frac{p}{1 + e \cos(\theta)}, \quad p = \frac{L^2}{\mu G m_1 m_2}, \quad e = \sqrt{1 + \frac{2 E L^2}{\mu (G m_1 m_2)^2}}$$

## 3. Oscilaciones y Mecánica de Fluidos

### Nivel Básico

#### 3.1 Oscilador Armónico Simple (M.A.S.)

- Ecuación diferencial y solución:
  $$\ddot{x} + \omega_0^2 x = 0 \implies x(t) = A \cos(\omega_0 t + \phi)$$
- Frecuencia angular y periodo (sistema masa-resorte):
  $$\omega_0 = \sqrt{\frac{k}{m}}, \quad T = 2\pi\sqrt{\frac{m}{k}}$$
- Péndulo Simple:
  $$T = 2\pi\sqrt{\frac{L}{g}}$$
- Péndulo Físico:
  $$T = 2\pi\sqrt{\frac{I}{m g d}}$$

#### 3.2 Estática de Fluidos

- Presión hidrostática:
  $$P(h) = P_0 + \rho g h$$
- Principio de Pascal:
  $$\frac{F_1}{A_1} = \frac{F_2}{A_2}$$
- Principio de Arquímedes (Fuerza de Empuje):
  $$E = \rho_{\text{fluido}} g V_{\text{sumergido}}$$

### Nivel Intermedio

#### 3.3 Oscilaciones Amortiguadas y Forzadas

- Oscilador amortiguado ($b = \text{coeficiente de fricción}$):
  $$\ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = 0, \quad \gamma = \frac{b}{2m}$$
  $$x(t) = A e^{-\gamma t} \cos(\omega_d t + \phi), \quad \omega_d = \sqrt{\omega_0^2 - \gamma^2} \quad (\text{subamortiguado } \gamma < \omega_0)$$
- Factor de Calidad $Q$:
  $$Q = \frac{\omega_0}{2\gamma}$$
- Oscilaciones forzadas con fuerza impulsora $F_0 \cos(\omega t)$:
  $$\ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = \frac{F_0}{m} \cos(\omega t)$$
  $$A(\omega) = \frac{F_0 / m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2}}$$

#### 3.4 Dinámica de Fluidos Ideales

- Ecuación de Continuidad (Flujo estacionario e incompresible 1D a través de secciones transversales):
  $$A_1 v_1 = A_2 v_2 = Q \quad (\text{Caudal volumétrico constante})$$
  $$\left( \text{Para flujo compresible estacionario: } \rho_1 A_1 v_1 = \rho_2 A_2 v_2 = \dot{m} = \text{constante} \right)$$
- Ecuación de Bernoulli:
  $$P_1 + \frac{1}{2}\rho v_1^2 + \rho g z_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g z_2 = \text{constante}$$
- Teorema de Torricelli:
  $$v = \sqrt{2gh}$$

### Nivel Universitario / Avanzado

#### 3.5 Mecánica de Fluidos y Medios Continuos

- Ecuación de Continuidad diferencial:
  $$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0$$
- Ecuación de Navier-Stokes (Fluidos Newtonianos incompresibles con viscosidad $\mu$):
  $$\rho \left( \frac{\partial \vec{v}}{\partial t} + (\vec{v} \cdot \nabla)\vec{v} \right) = -\nabla P + \mu \nabla^2 \vec{v} + \rho \vec{g}$$
- Tensor de Esfuerzos de Cauchy $\boldsymbol{\sigma}$:
  $$\nabla \cdot \boldsymbol{\sigma} + \vec{f}_{\text{ext}} = \rho \frac{d\vec{v}}{dt}$$
- Ecuación de Navier-Cauchy para Sólidos Elásticos Lineales (Parámetros de Lamé $\lambda, \mu$):
  $$\rho \frac{\partial^2 \vec{u}}{\partial t^2} = (\lambda + \mu)\nabla(\nabla \cdot \vec{u}) + \mu \nabla^2 \vec{u} + \vec{f}_{\text{vol}}$$

## 4. Mecánica Analítica y Relativista

### Nivel Intermedio / Universitario

#### 4.1 Mecánica Lagrangiana

- Coordenadas generalizadas:
  $$q = (q_1, q_2, \dots, q_n), \quad \dot{q} = (\dot{q}_1, \dot{q}_2, \dots, \dot{q}_n)$$
- Función Lagrangiana:
  $$L(q, \dot{q}, t) = T(q, \dot{q}, t) - V(q, t)$$
- Principio de Mínima Acción de Hamilton:
  $$\delta S = \delta \int_{t_1}^{t_2} L(q, \dot{q}, t) dt = 0$$
- Ecuaciones de Euler-Lagrange:
  $$\frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}_j} \right) - \frac{\partial L}{\partial q_j} = 0, \quad j = 1, \dots, n$$
- Momento conjugado o canónico:
  $$p_j = \frac{\partial L}{\partial \dot{q}_j}$$
- Teorema de Noether:
  $$\text{Si } \frac{\partial L}{\partial q_j} = 0 \implies p_j = \text{constante de movimiento}$$

#### 4.2 Mecánica Hamiltoniana

- Función Hamiltoniana (Transformada de Legendre):
  $$H(q, p, t) = \sum_{j=1}^n p_j \dot{q}_j - L(q, \dot{q}, t)$$
- Ecuaciones Canónicas de Hamilton:
  $$\dot{q}_j = \frac{\partial H}{\partial p_j}, \quad \dot{p}_j = -\frac{\partial H}{\partial q_j}$$
- Variación temporal del Hamiltoniano:
  $$\frac{dH}{dt} = \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t}$$

### Nivel Universitario Avanzado

#### 4.3 Formulaciones Canónicas Avanzadas

- Corchetes de Poisson:
  $$\{f, g\}_{q,p} = \sum_{j=1}^n \left( \frac{\partial f}{\partial q_j} \frac{\partial g}{\partial p_j} - \frac{\partial f}{\partial p_j} \frac{\partial g}{\partial q_j} \right)$$
- Evolución temporal de una función observable:
  $$\frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}$$
- Teorema de Liouville (Conservación del volumen en el espacio fásico):
  $$\frac{d\rho}{dt} = \frac{\partial \rho}{\partial t} + \{\rho, H\} = 0$$
- Ecuación de Hamilton-Jacobi:
  $$H\left( q_1, \dots, q_n, \frac{\partial S}{\partial q_1}, \dots, \frac{\partial S}{\partial q_n}, t \right) + \frac{\partial S}{\partial t} = 0$$

#### 4.4 Mecánica Relativista (Relatividad Especial)

- Factor de Lorentz:
  $$\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}$$
- Momento lineal relativista:
  $$\vec{p} = \gamma m_0 \vec{v}$$
- Fuerza relativista:
  $$\vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(\gamma m_0 \vec{v})$$
- Energía total, cinética y en reposo:
  $$E = \gamma m_0 c^2 = E_k + m_0 c^2$$
  $$E_k = (\gamma - 1) m_0 c^2$$
- Relación de dispersión Energía-Momento:
  $$E^2 = (p c)^2 + (m_0 c^2)^2$$
- Cuadrivectores en Cinemática y Dinámica:
  $$X^\mu = (ct, \vec{r}), \quad U^\mu = \frac{dX^\mu}{d\tau} = \gamma(c, \vec{v})$$
  $$P^\mu = m_0 U^\mu = \left( \frac{E}{c}, \vec{p} \right), \quad P^\mu P_\mu = \frac{E^2}{c^2} - |\vec{p}|^2 = m_0^2 c^2$$

# Compendio II: Oscilaciones y Ondas Mecánicas
*(Nivel Básico a Universitario)*

## 5. Movimiento Oscilatorio (Oscilaciones)

### Nivel Básico

#### 5.1 Cinemática del Movimiento Armónico Simple (M.A.S.)

- Posición en función del tiempo:
  $$x(t) = A \cos(\omega t + \phi)$$
- Velocidad:
  $$v(t) = \frac{dx}{dt} = -\omega A \sen(\omega t + \phi) = \pm \omega \sqrt{A^2 - x^2}$$
- Aceleración:
  $$a(t) = \frac{d^2x}{dt^2} = -\omega^2 A \cos(\omega t + \phi) = -\omega^2 x(t)$$
- Valores máximos:
  $$x_{\text{máx}} = A, \quad v_{\text{máx}} = \omega A, \quad a_{\text{máx}} = \omega^2 A$$

#### 5.2 Parámetros Temporales y Frecuenciales

- Periodo ($T$):
  $$T = \frac{1}{f} = \frac{2\pi}{\omega}$$
- Frecuencia ($f$):
  $$f = \frac{1}{T} = \frac{\omega}{2\pi}$$
- Frecuencia angular ($\omega$):
  $$\omega = 2\pi f = \frac{2\pi}{T}$$

#### 5.3 Energía del M.A.S. (Sistema Conservativo)

- Energía Cinética:
  $$E_k = \frac{1}{2} m v^2 = \frac{1}{2} m \omega^2 A^2 \sen^2(\omega t + \phi)$$
- Energía Potencial Elástica:
  $$E_p = \frac{1}{2} k x^2 = \frac{1}{2} k A^2 \cos^2(\omega t + \phi)$$
- Energía Mecánica Total:
  $$E_m = E_k + E_p = \frac{1}{2} k A^2 = \frac{1}{2} m \omega^2 A^2 = \text{constante}$$

#### 5.4 Sistemas Oscilatorios Simples

- Masa-Resorte:
  $$\omega_0 = \sqrt{\frac{k}{m}}, \quad T = 2\pi\sqrt{\frac{m}{k}}$$
- Péndulo Simple (Aproximación para ángulos pequeños $\sen\theta \approx \theta$):
  $$\omega_0 = \sqrt{\frac{g}{L}}, \quad T = 2\pi\sqrt{\frac{L}{g}}$$

### Nivel Intermedio

#### 5.5 Péndulos Compuestos y de Torsión

- Péndulo Físico (Centro de masa a distancia $d$ del eje de giro):
  $$\omega_0 = \sqrt{\frac{m g d}{I}}, \quad T = 2\pi\sqrt{\frac{I}{m g d}}$$
- Péndulo de Torsión (Constante de torsión $\kappa$):
  $$\tau = -\kappa \theta \implies \omega_0 = \sqrt{\frac{\kappa}{I}}, \quad T = 2\pi\sqrt{\frac{I}{\kappa}}$$

#### 5.6 Oscilaciones Amortiguadas

- Ecuación Diferencial Fundamental ($b = \text{coeficiente de amortiguamiento viscoso}$):
  $$m \ddot{x} + b \dot{x} + k x = 0 \implies \ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = 0, \quad \gamma = \frac{b}{2m}, \quad \omega_0 = \sqrt{\frac{k}{m}}$$
- Régimen Subamortiguado ($\gamma < \omega_0$):
  $$x(t) = A_0 e^{-\gamma t} \cos(\omega_d t + \phi), \quad \omega_d = \sqrt{\omega_0^2 - \gamma^2}$$
- Régimen Críticamente Amortiguado ($\gamma = \omega_0$):
  $$x(t) = (C_1 + C_2 t) e^{-\gamma t}$$
- Régimen Sobreamortiguado ($\gamma > \omega_0$):
  $$x(t) = C_1 e^{-(\gamma - \sqrt{\gamma^2 - \omega_0^2})t} + C_2 e^{-(\gamma + \sqrt{\gamma^2 - \omega_0^2})t}$$
- Decremento Logarítmico ($\delta$):
  $$\delta = \ln\left( \frac{x(t)}{x(t + T_d)} \right) = \gamma T_d = \frac{2\pi \gamma}{\omega_d}$$
- Factor de Calidad ($Q$):
  $$Q = \frac{\omega_0}{2\gamma} = \frac{\pi}{\delta} = 2\pi \frac{E}{\Delta E_{\text{ciclo}}}$$

#### 5.7 Oscilaciones Forzadas y Resonancia

- Ecuación Diferencial con Excitación Armónica:
  $$\ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = \frac{F_0}{m} \cos(\omega t)$$
- Solución de Estado Estacionario ($x_p(t) = A(\omega) \cos(\omega t - \delta)$):
  $$A(\omega) = \frac{F_0 / m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2}}$$
  $$\tan(\delta) = \frac{2\gamma \omega}{\omega_0^2 - \omega^2}$$
- Frecuencia de Resonancia de Amplitud:
  $$\omega_{\text{res}} = \sqrt{\omega_0^2 - 2\gamma^2}$$
- Potencia Media Absorbida por el Oscilador:
  $$\langle P(\omega) \rangle = \frac{F_0^2 \gamma \omega^2}{m [(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2]}$$

### Nivel Universitario / Avanzado

#### 5.8 Osciladores Acoplados y Modos Normales

- Ecuación Matricial de Movimiento (Sistemas lineales de $N$ grados de libertad):
  $$\mathbf{M} \ddot{\vec{x}} + \mathbf{K} \vec{x} = \vec{0}$$
- Ecuación Secular / Polinomio Característico:
  $$\det(\mathbf{K} - \omega^2 \mathbf{M}) = 0$$
- Transformación a Coordenadas Normales ($\vec{\eta} = \mathbf{P}^{-1} \vec{x}$):
  $$\ddot{\eta}_k + \omega_k^2 \eta_k = 0, \quad k = 1, 2, \dots, N$$

#### 5.9 Oscilaciones No Lineales (Péndulo Simple de Gran Amplitud)

- Ecuación Diferencial Exacta:
  $$\ddot{\theta} + \omega_0^2 \sen(\theta) = 0$$
- Periodo Exacto mediante Integrales Elípticas Completas de Primera Especie $K(m)$:
  $$T = 4\sqrt{\frac{L}{g}} K\left(\sen^2\left(\frac{\theta_0}{2}\right)\right) = 4\sqrt{\frac{L}{g}} \int_0^{\pi/2} \frac{d\phi}{\sqrt{1 - \sen^2\left(\frac{\theta_0}{2}\right) \sen^2\phi}}$$
- Aproximación de Borda (Series de Taylor):
  $$T \approx 2\pi\sqrt{\frac{L}{g}} \left( 1 + \frac{1}{16}\theta_0^2 + \frac{11}{3072}\theta_0^4 + \dots \right)$$

#### 5.10 Osciladores Autoexcitados (Ecuación de Van der Pol)

- Ecuación con amortiguamiento no lineal:
  $$\ddot{x} - \mu(1 - x^2)\dot{x} + \omega_0^2 x = 0$$

## 6. Ondas Mecánicas en Medios Continuos

### Nivel Básico

#### 6.1 Cinemática de Ondas Armónicas Unidimensionales

- Función de Onda Progresiva (hacia la derecha $-$ / hacia la izquierda $+$):
  $$y(x, t) = A \sen(k x \mp \omega t + \phi)$$
- Relación entre Parámetros Fundamentales:
  $$k = \frac{2\pi}{\lambda}, \quad \omega = \frac{2\pi}{T} = 2\pi f, \quad v = \lambda f = \frac{\lambda}{T} = \frac{\omega}{k}$$
- Velocidad y Aceleración Transversal de las Partículas del Medio:
  $$v_y(x, t) = \frac{\partial y}{\partial t} = \mp \omega A \cos(k x \mp \omega t + \phi)$$
  $$a_y(x, t) = \frac{\partial^2 y}{\partial t^2} = -\omega^2 A \sen(k x \mp \omega t + \phi) = -\omega^2 y(x, t)$$

### Nivel Intermedio

#### 6.2 Ecuación Diferencial de Onda 1D (d'Alembert)

- Forma canónica:
  $$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$$
- Solución General de d'Alembert:
  $$y(x, t) = f(x - vt) + g(x + vt)$$

#### 6.3 Velocidad de Propagación en Medios Elásticos

- Cuerda Tensa (Tensión $T$, densidad lineal de masa $\mu = m/L$):
  $$v = \sqrt{\frac{T}{\mu}}$$
- Barra Sólida (Ondas longitudinales, módulo de Young $Y$, densidad $\rho$):
  $$v = \sqrt{\frac{Y}{\rho}}$$
- Fluido / Gas (Módulo de compresibilidad volumétrica $B$):
  $$v = \sqrt{\frac{B}{\rho}}$$
- Gas Ideal (Ecuación de Newton-Laplace para proceso adiabático):
  $$v = \sqrt{\frac{\gamma R T}{M}} = \sqrt{\frac{\gamma P}{\rho}}$$

#### 6.4 Transporte de Energía e Intensidad

- Densidad Lineal de Energía Mecánica Total:
  $$\frac{dE}{dx} = \mu \omega^2 A^2 \cos^2(kx - \omega t)$$
- Potencia Instantánea Transmitida en Cuerda:
  $$P(x, t) = -T \left( \frac{\partial y}{\partial x} \right) \left( \frac{\partial y}{\partial t} \right) = \sqrt{\mu T} \, \omega^2 A^2 \cos^2(kx - \omega t)$$
- Potencia Promedio Transmitida:
  $$\langle P \rangle = \frac{1}{2} \mu v \omega^2 A^2 = \frac{1}{2} \sqrt{\mu T} \, \omega^2 A^2$$
- Intensidad de Onda ($I$):
  $$I = \frac{\langle P \rangle}{\text{Área}} = \frac{1}{2} \rho v \omega^2 A^2$$
- Ley del Inverso del Cuadrado (Fuente puntual isótropa en medio no disipativo):
  $$I(r) = \frac{P_{\text{fuente}}}{4\pi r^2} \implies \frac{I_1}{I_2} = \frac{r_2^2}{r_1^2}$$

### Nivel Universitario / Avanzado

#### 6.5 Dispersión de Ondas

- Relación de Dispersión:
  $$\omega = \omega(k)$$
- Velocidad de Fase:
  $$v_p = \frac{\omega}{k}$$
- Velocidad de Grupo:
  $$v_g = \frac{d\omega}{dk} = v_p + k \frac{dv_p}{dk} = v_p - \lambda \frac{dv_p}{d\lambda}$$

#### 6.6 Impedancia Mecánica y Fenómenos en Fronteras

- Impedancia Característica del Medio:
  $$Z = \rho v = \sqrt{\rho B} \quad (\text{Fluidos}), \quad Z = \mu v = \sqrt{\mu T} \quad (\text{Cuerdas})$$
- Coeficiente de Reflexión en Amplitud (para ondas de desplazamiento / velocidad incidiendo de medio 1 a medio 2):
  $$r = \frac{Z_1 - Z_2}{Z_1 + Z_2}$$
- Coeficiente de Transmisión en Amplitud (desplazamiento / velocidad):
  $$t = \frac{2Z_1}{Z_1 + Z_2}$$
- Coeficientes de Reflexión y Transmisión de Potencia / Intensidad ($R + T_w = 1$):
  $$R = r^2 = \left( \frac{Z_1 - Z_2}{Z_1 + Z_2} \right)^2, \quad T_w = \frac{Z_2}{Z_1} t^2 = \frac{4 Z_1 Z_2}{(Z_1 + Z_2)^2}$$

#### 6.7 Ondas Elásticas en Medios Continuos 3D (Ecuación de Navier-Cauchy)

- Ondas Longitudinales Primarias (Ondas P / Compresionales):
  $$v_P = \sqrt{\frac{\lambda + 2\mu}{\rho}} = \sqrt{\frac{K + \frac{4}{3}G}{\rho}}$$
- Ondas Transversales Secundarias (Ondas S / Cizalladura):
  $$v_S = \sqrt{\frac{\mu}{\rho}} = \sqrt{\frac{G}{\rho}}$$

## 7. Interferencia, Ondas Estacionarias y Acústica

### Nivel Básico

#### 7.1 Superposición e Interferencia

- Interferencia de dos ondas armónicas con diferencia de fase $\Delta\phi$:
  $$y_R(x, t) = \left[ 2A \cos\left(\frac{\Delta\phi}{2}\right) \right] \sen\left(kx - \omega t + \frac{\Delta\phi}{2}\right)$$
- Condición de Interferencia Constructiva:
  $$\Delta\phi = 2n\pi \implies \Delta r = n\lambda, \quad n \in \mathbb{Z}$$
- Condición de Interferencia Destructiva:
  $$\Delta\phi = (2n + 1)\pi \implies \Delta r = \left(n + \frac{1}{2}\right)\lambda, \quad n \in \mathbb{Z}$$

#### 7.2 Batidos o Pulsaciones

- Superposición de ondas con frecuencias ligeramente diferentes $\omega_1 \approx \omega_2$:
  $$y_R(t) = \left[ 2A \cos\left( \frac{\omega_1 - \omega_2}{2} t \right) \right] \cos\left( \frac{\omega_1 + \omega_2}{2} t \right)$$
- Frecuencia de Batido:
  $$f_{\text{batido}} = |f_1 - f_2|$$

#### 7.3 Escala Decibélica y Nivel de Sonido

- Nivel de Intensidad Sonora ($\beta$):
  $$\beta = 10 \log_{10}\left( \frac{I}{I_0} \right), \quad I_0 = 10^{-12} \, \text{W/m}^2$$
- Nivel de Presión Sonora ($SPL$):
  $$L_p = 20 \log_{10}\left( \frac{p_{\text{rms}}}{p_0} \right), \quad p_0 = 20 \, \mu\text{Pa}$$

### Nivel Intermedio

#### 7.4 Ondas Estacionarias Unidimensionales

- Ecuación Analítica:
  $$y(x, t) = [2A \sen(kx)] \cos(\omega t)$$
- Posición de Nodos (Amplitud nula):
  $$\sen(kx) = 0 \implies x_n = n \frac{\lambda}{2}, \quad n = 0, 1, 2, \dots$$
- Posición de Antinodos o Vientres (Amplitud máxima $2A$):
  $$|\sen(kx)| = 1 \implies x_a = \left( n + \frac{1}{2} \right) \frac{\lambda}{2}, \quad n = 0, 1, 2, \dots$$

#### 7.5 Modos Normales y Frecuencias Resonantes en Sistemas Acotados

- Cuerda Fija en Ambos Extremos o Tubo Abierto-Abierto:
  $$\lambda_n = \frac{2L}{n}, \quad f_n = n \frac{v}{2L} = n f_1, \quad n = 1, 2, 3, \dots$$
- Cuerda con un Extremo Fijo y uno Libre o Tubo Abierto-Cerrado:
  $$\lambda_n = \frac{4L}{2n - 1}, \quad f_n = (2n - 1) \frac{v}{4L} = (2n - 1) f_1, \quad n = 1, 2, 3, \dots$$

#### 7.6 Efecto Doppler Clásico (Velocidad del sonido $v$)

- Fórmula General:
  $$f_o = f_s \left( \frac{v \pm v_o}{v \mp v_s} \right)$$
  $$\text{Signo superior: acercamiento} \quad | \quad \text{Signo inferior: alejamiento}$$

#### 7.7 Ondas de Choque y Cono de Mach

- Ángulo de Mach ($\theta_M$):
  $$\sen(\theta_M) = \frac{v}{v_s} = \frac{1}{M}, \quad M = \frac{v_s}{v} > 1$$

### Nivel Universitario / Avanzado

#### 7.8 Acústica Física y Ondas de Presión

- Onda de Desplazamiento Molecular:
  $$s(x, t) = s_{\text{máx}} \cos(kx - \omega t)$$
- Onda de Presión Acústica Excedente:
  $$\Delta p(x, t) = -B \frac{\partial s}{\partial x} = \Delta p_{\text{máx}} \sen(kx - \omega t)$$
- Amplitud de Presión:
  $$\Delta p_{\text{máx}} = B k s_{\text{máx}} = \rho v \omega s_{\text{máx}} = Z \omega s_{\text{máx}}$$
- Relación entre Intensidad y Presión Acústica:
  $$I = \frac{\Delta p_{\text{máx}}^2}{2\rho v} = \frac{p_{\text{rms}}^2}{\rho v}$$

#### 7.9 Ecuación de Onda Acústica Tridimensional

- Ecuación Diferencial para la Presión:
  $$\nabla^2 p - \frac{1}{c^2} \frac{\partial^2 p}{\partial t^2} = 0$$
- Solución para Ondas Esféricas Monocromáticas:
  $$p(r, t) = \frac{A}{r} e^{i(kr - \omega t)}$$
- Potencial de Velocidad Acústico ($\vec{u} = -\nabla \Phi$):
  $$\nabla^2 \Phi - \frac{1}{c^2} \frac{\partial^2 \Phi}{\partial t^2} = 0, \quad p = \rho_0 \frac{\partial \Phi}{\partial t}$$

#### 7.10 Efecto Doppler Vectorial en Dirección Arbitraria

- Frecuencia Observada:
  $$f_o = f_s \left( \frac{c - \vec{v}_o \cdot \hat{n}}{c - \vec{v}_s \cdot \hat{n}} \right)$$
  $$(\hat{n} = \text{vector unitario dirigido de la fuente al observador})$$

#### 7.11 Atenuación y Absorción Acústica Viscotérmica

- Decaimiento Espacial de Amplitud:
  $$A(x) = A_0 e^{-\alpha x}$$
- Coeficiente de Atenuación Clásico de Stokes-Kirchhoff:
  $$\alpha = \frac{\omega^2}{2\rho c^3} \left[ \frac{4}{3}\eta + \eta_v + \frac{(\gamma - 1)\kappa}{C_p} \right]$$

# Compendio III: Termodinámica Clásica, Química y Estadística
*(Nivel Básico a Universitario)*

## 8. Conceptos Fundamentales, Gases y Ecuaciones de Estado

### Nivel Básico

#### 8.1 Escalas Termométricas y Temperatura

- Escala Celsius a Kelvin:
  $$T(\text{K}) = T(^\circ\text{C}) + 273.15$$
- Escala Celsius a Fahrenheit:
  $$T(^\circ\text{F}) = \frac{9}{5} T(^\circ\text{C}) + 32$$
- Escala Fahrenheit a Rankine (Temperatura absoluta $T_{\text{R}}$):
  $$T_{\text{R}}(\text{Ra}) = T(^\circ\text{F}) + 459.67 = \frac{9}{5} T(\text{K})$$

#### 8.2 Dilatación Térmica

- Dilatación Lineal:
  $$\Delta L = \alpha L_0 \Delta T \implies L(T) = L_0 (1 + \alpha \Delta T)$$
- Dilatación Superficial ($\gamma \approx 2\alpha$):
  $$\Delta A = \gamma A_0 \Delta T \implies A(T) = A_0 (1 + \gamma \Delta T)$$
- Dilatación Volumétrica ($\beta \approx 3\alpha$ para sólidos isótropos):
  $$\Delta V = \beta V_0 \Delta T \implies V(T) = V_0 (1 + \beta \Delta T)$$

#### 8.3 Calorimetría y Capacidad Calorífica

- Calor sensible:
  $$Q = m c \Delta T = n C_m \Delta T = C \Delta T$$
- Calor latente en cambio de fase:
  $$Q = m L$$
- Principio de Conservación de la Energía (Equilibrio térmico):
  $$\sum Q_{\text{ganado}} + \sum Q_{\text{perdido}} = 0 \implies \sum m_i c_i (T_{\text{eq}} - T_i) = 0$$

#### 8.4 Gas Ideal y Leyes Empíricas

- Ecuación de Estado del Gas Ideal:
  $$P V = n R T = N k_B T, \quad R = N_A k_B \approx 8.314 \, \frac{\text{J}}{\text{mol}\cdot\text{K}}$$
- Ley de Boyle-Mariotte ($T = \text{constante}$):
  $$P_1 V_1 = P_2 V_2$$
- Ley de Charles ($P = \text{constante}$):
  $$\frac{V_1}{T_1} = \frac{V_2}{T_2}$$
- Ley de Gay-Lussac ($V = \text{constante}$):
  $$\frac{P_1}{T_1} = \frac{P_2}{T_2}$$
- Ley Combinada:
  $$\frac{P_1 V_1}{T_1} = \frac{P_2 V_2}{T_2}$$

### Nivel Intermedio

#### 8.5 Mezclas de Gases y Propiedades Molares

- Ley de Dalton de las Presiones Parciales:
  $$P_{\text{total}} = \sum_{i=1}^k P_i, \quad P_i = x_i P_{\text{total}}, \quad x_i = \frac{n_i}{n_{\text{total}}}$$
- Ley de Amagat de los Volúmenes Parciales:
  $$V_{\text{total}} = \sum_{i=1}^k V_i, \quad V_i = x_i V_{\text{total}}$$
- Masa molar aparente de una mezcla:
  $$\bar{M} = \sum_{i=1}^k x_i M_i$$

#### 8.6 Coeficientes Termoelásticos

- Coeficiente de Dilatación Térmica Isobárica ($\alpha$ o $\beta$):
  $$\alpha = \frac{1}{V} \left( \frac{\partial V}{\partial T} \right)_P$$
- Compresibilidad Isotérmica ($\kappa_T$ o $\beta_T$):
  $$\kappa_T = -\frac{1}{V} \left( \frac{\partial V}{\partial P} \right)_T$$
- Compresibilidad Adiabática / Isentrópica ($\kappa_S$):
  $$\kappa_S = -\frac{1}{V} \left( \frac{\partial V}{\partial P} \right)_S$$
- Coeficiente Piezométrico / Tensión Térmica ($\beta_P$):
  $$\beta_P = \frac{1}{P} \left( \frac{\partial P}{\partial T} \right)_V = \frac{\alpha}{P \kappa_T}$$

#### 8.7 Ecuaciones de Estado para Gases Reales

- Ecuación de Van der Waals:
  $$\left( P + \frac{a n^2}{V^2} \right)(V - n b) = n R T \iff \left( P + \frac{a}{V_m^2} \right)(V_m - b) = R T$$
- Constantes Críticas de Van der Waals:
  $$T_c = \frac{8a}{27Rb}, \quad P_c = \frac{a}{27b^2}, \quad V_{m,c} = 3b$$
- Factor de Compresibilidad Crítico de Van der Waals:
  $$Z_c = \frac{P_c V_{m,c}}{R T_c} = \frac{3}{8} = 0.375$$
- Ecuación Reducida de Van der Waals ($P_r = P/P_c, \, T_r = T/T_c, \, V_r = V_m/V_{m,c}$):
  $$\left( P_r + \frac{3}{V_r^2} \right)(3V_r - 1) = 8T_r$$
- Factor de Compresibilidad y Expansión Virial:
  $$Z = \frac{P V_m}{R T} = 1 + \frac{B(T)}{V_m} + \frac{C(T)}{V_m^2} + \dots = 1 + B'(T)P + C'(T)P^2 + \dots$$

### Nivel Universitario / Avanzado

#### 8.8 Otras Ecuaciones de Estado Reales

- Redlich-Kwong:
  $$P = \frac{R T}{V_m - b} - \frac{a}{\sqrt{T} V_m (V_m + b)}$$
- Peng-Robinson:
  $$P = \frac{R T}{V_m - b} - \frac{a(T)}{V_m^2 + 2bV_m - b^2}$$
- Dieterici:
  $$P = \frac{R T}{V_m - b} \exp\left( -\frac{a}{R T V_m} \right)$$

#### 8.9 Teoría Cinética Molecular de los Gases

- Presión Cinética:
  $$P = \frac{1}{3} \rho \langle v^2 \rangle = \frac{1}{3} \frac{N m}{V} v_{\text{rms}}^2$$
- Energía Cinética Media Translacional por Molécula:
  $$\langle \epsilon_k \rangle = \frac{1}{2} m \langle v^2 \rangle = \frac{3}{2} k_B T$$
- Velocidades Moleculares Características:
  $$v_{\text{rms}} = \sqrt{\langle v^2 \rangle} = \sqrt{\frac{3 k_B T}{m}} = \sqrt{\frac{3 R T}{M}}$$
  $$v_{\text{prom}} = \langle v \rangle = \sqrt{\frac{8 k_B T}{\pi m}} = \sqrt{\frac{8 R T}{\pi M}}$$
  $$v_{\text{mp}} = \sqrt{\frac{2 k_B T}{m}} = \sqrt{\frac{2 R T}{M}}$$
- Distribución de Rapideces de Maxwell-Boltzmann:
  $$f(v) = 4\pi \left( \frac{m}{2\pi k_B T} \right)^{3/2} v^2 \exp\left( -\frac{m v^2}{2 k_B T} \right)$$
- Teorema de Equipartición de la Energía ($f = \text{grados de libertad activos}$):
  $$U = \frac{f}{2} N k_B T = \frac{f}{2} n R T, \quad C_{v,m} = \frac{f}{2} R, \quad C_{p,m} = \left(\frac{f}{2} + 1\right) R$$

## 9. Primera y Segunda Ley de la Termodinámica

### Nivel Básico

#### 9.1 Primera Ley de la Termodinámica (Sistemas Cerrados)

- Forma Integral (Convención física: trabajo $W$ realizado por el sistema):
  $$\Delta U = Q - W$$
- Forma Diferencial General (Sistema cerrado):
  $$dU = \delta Q - \delta W$$
- Para procesos cuasiestáticos de expansión/compresión hidrostática ($\delta W = P \, dV$):
  $$dU = \delta Q - P \, dV$$
- Trabajo Cuasiestático de Expansión/Compresión:
  $$W = \int_{V_i}^{V_f} P \, dV$$

#### 9.2 Procesos Termodinámicos Cuasiestáticos en Gases Ideales

- Proceso Isocórico ($V = \text{constante}, \, dV = 0$):
  $$W = 0, \quad Q = \Delta U = n C_v \Delta T$$
- Proceso Isobárico ($P = \text{constante}$):
  $$W = P(V_f - V_i) = n R \Delta T, \quad Q = n C_p \Delta T, \quad \Delta U = n C_v \Delta T$$
- Proceso Isotérmico ($T = \text{constante}, \, \Delta T = 0$):
  $$\Delta U = 0 \implies Q = W = n R T \ln\left(\frac{V_f}{V_i}\right) = n R T \ln\left(\frac{P_i}{P_f}\right)$$
- Proceso Adiabático Reversible ($Q = 0, \, \delta Q = 0$):
  $$Q = 0 \implies \Delta U = -W = n C_v (T_f - T_i) = \frac{P_f V_f - P_i V_i}{1 - \gamma}$$
  $$P V^\gamma = \text{constante}, \quad T V^{\gamma - 1} = \text{constante}, \quad T^\gamma P^{1 - \gamma} = \text{constante}$$
- Relación de Mayer y Coeficiente de Dilatación Adiabática:
  $$C_p - C_v = R, \quad \gamma = \frac{C_p}{C_v}$$

### Nivel Intermedio

#### 9.3 Procesos Politrópicos ($P V^n = \text{constante}$)

- Trabajo:
  $$W = \frac{P_f V_f - P_i V_i}{1 - n} = \frac{n R (T_f - T_i)}{1 - n} \quad (n \neq 1)$$
- Capacidad Calorífica Politrópica:
  $$C_n = C_v + \frac{R}{1 - n} = C_v \left( \frac{n - \gamma}{n - 1} \right)$$

#### 9.4 Segunda Ley de la Termodinámica y Entropía

- Definición de Entropía (Clausius):
  $$dS = \frac{\delta Q_{\text{rev}}}{T} \implies \Delta S = \int_i^f \frac{\delta Q_{\text{rev}}}{T}$$
- Desigualdad de Clausius:
  $$\oint \frac{\delta Q}{T} \le 0 \quad (\text{igualdad para ciclos reversibles})$$
- Principio del Incremento de Entropía:
  $$\Delta S_{\text{universo}} = \Delta S_{\text{sistema}} + \Delta S_{\text{entorno}} \ge 0$$
- Variación de Entropía en un Gas Ideal:
  $$\Delta S = n C_v \ln\left( \frac{T_f}{T_i} \right) + n R \ln\left( \frac{V_f}{V_i} \right) = n C_p \ln\left( \frac{T_f}{T_i} \right) - n R \ln\left( \frac{P_f}{P_i} \right)$$
- Variación de Entropía en Sustancias Incompresibles (Líquidos/Sólidos):
  $$\Delta S = m c \ln\left( \frac{T_f}{T_i} \right)$$
- Entropía de Mezcla de Gases Ideales:
  $$\Delta S_{\text{mezcla}} = -n_{\text{total}} R \sum_{i=1}^k x_i \ln(x_i)$$

#### 9.5 Máquinas Térmicas, Refrigeradores y Ciclos de Potencia

- Eficiencia Térmica General de una Máquina Térmica:
  $$\eta = \frac{W_{\text{neto}}}{Q_H} = \frac{Q_H - |Q_C|}{Q_H} = 1 - \frac{|Q_C|}{Q_H}$$
- Eficiencia de Carnot (Límite máximo entre dos focos):
  $$\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}$$
- Coeficiente de Desempeño de Refrigeradores ($\text{COP}_R$):
  $$\text{COP}_R = \beta = \frac{Q_C}{W_{\text{neto}}} = \frac{Q_C}{Q_H - Q_C} \implies \text{COP}_{R,\text{Carnot}} = \frac{T_C}{T_H - T_C}$$
- Coeficiente de Desempeño de Bombas de Calor ($\text{COP}_{\text{HP}}$):
  $$\text{COP}_{\text{HP}} = \gamma' = \frac{Q_H}{W_{\text{neto}}} = \text{COP}_R + 1 \implies \text{COP}_{\text{HP},\text{Carnot}} = \frac{T_H}{T_H - T_C}$$
- Ciclo Otto de Aire Estándar (Relación de compresión $r = V_{\text{máx}}/V_{\text{mín}}$):
  $$\eta_{\text{Otto}} = 1 - \frac{1}{r^{\gamma - 1}}$$
- Ciclo Diesel (Relación de corte de admisión $r_c = V_3/V_2$):
  $$\eta_{\text{Diesel}} = 1 - \frac{1}{r^{\gamma - 1}} \left[ \frac{r_c^\gamma - 1}{\gamma(r_c - 1)} \right]$$
- Ciclo Brayton / Joule (Relación de presiones $r_p = P_2/P_1$):
  $$\eta_{\text{Brayton}} = 1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}}$$

### Nivel Universitario / Avanzado

#### 9.6 Balances de Energía y Entropía en Volúmenes de Control (Sistemas Abiertos)

- Conservación de Masa:
  $$\frac{dm_{\text{VC}}}{dt} = \sum_{\text{ent}} \dot{m}_i - \sum_{\text{sal}} \dot{m}_e$$
- Primera Ley en Volumen de Control:
  $$\frac{dE_{\text{VC}}}{dt} = \dot{Q} - \dot{W}_{\text{eje}} + \sum_{\text{ent}} \dot{m}_i \left( h_i + \frac{v_i^2}{2} + g z_i \right) - \sum_{\text{sal}} \dot{m}_e \left( h_e + \frac{v_e^2}{2} + g z_e \right)$$
- Primera Ley en Estado Estacionario ($\frac{dE_{\text{VC}}}{dt} = 0$, 1 entrada y 1 salida):
  $$q - w_{\text{eje}} = (h_e - h_i) + \frac{v_e^2 - v_i^2}{2} + g(z_e - z_i)$$
- Balance de Entropía en Volumen de Control:
  $$\frac{dS_{\text{VC}}}{dt} = \sum_k \frac{\dot{Q}_k}{T_k} + \sum_{\text{ent}} \dot{m}_i s_i - \sum_{\text{sal}} \dot{m}_e s_e + \dot{S}_{\text{gen}}, \quad \dot{S}_{\text{gen}} \ge 0$$

#### 9.7 Análisis Exergético (Disponibilidad) y Destrucción de Exergía

- Exergía de Sistema Cerrado:
  $$\Phi = (U - U_0) + P_0(V - V_0) - T_0(S - S_0)$$
- Exergía de Flujo (Sistema Abierto):
  $$\psi = (h - h_0) - T_0(s - s_0) + \frac{v^2}{2} + gz$$
- Teorema de Gouy-Stodola (Exergía Destruida / Pérdida de Trabajo Útil):
  $$\dot{X}_{\text{destruida}} = I = T_0 \dot{S}_{\text{gen}}$$

## 10. Potenciales Termodinámicos y Relaciones de Maxwell

### Nivel Intermedio

#### 10.1 Ecuaciones Fundamentales y Potenciales Termodinámicos

- Energía Interna $U(S, V, N)$:
  $$dU = T dS - P dV + \sum_{i=1}^k \mu_i dN_i$$
- Entalpía $H(S, P, N) = U + PV$:
  $$dH = T dS + V dP + \sum_{i=1}^k \mu_i dN_i$$
- Energía Libre de Helmholtz $A(T, V, N) = F = U - TS$:
  $$dA = -S dT - P dV + \sum_{i=1}^k \mu_i dN_i$$
- Energía Libre de Gibbs $G(T, P, N) = H - TS$:
  $$dG = -S dT + V dP + \sum_{i=1}^k \mu_i dN_i$$
- Gran Potencial Termodinámico / Potencial Gran Canónico ($\Omega = \Phi_G(T, V, \mu) = U - TS - \mu N = -PV$):
  $$d\Omega = -S dT - P dV - N d\mu$$

#### 10.2 Relaciones de Maxwell

- A partir de $dU$:
  $$\left( \frac{\partial T}{\partial V} \right)_S = -\left( \frac{\partial P}{\partial S} \right)_V$$
- A partir de $dH$:
  $$\left( \frac{\partial T}{\partial P} \right)_S = \left( \frac{\partial V}{\partial S} \right)_P$$
- A partir de $dA$:
  $$\left( \frac{\partial S}{\partial V} \right)_T = \left( \frac{\partial P}{\partial T} \right)_V$$
- A partir de $dG$:
  $$\left( \frac{\partial S}{\partial P} \right)_T = -\left( \frac{\partial V}{\partial T} \right)_P$$

#### 10.3 Ecuaciones $T dS$ y Propiedades de Calores Específicos

- Primera Ecuación $T dS$:
  $$T dS = C_v dT + T \left( \frac{\partial P}{\partial T} \right)_V dV = C_v dT + \frac{T \alpha}{\kappa_T} dV$$
- Segunda Ecuación $T dS$:
  $$T dS = C_p dT - T \left( \frac{\partial V}{\partial T} \right)_P dP = C_p dT - T V \alpha dP$$
- Relación General $C_p - C_v$:
  $$C_p - C_v = T \left( \frac{\partial P}{\partial T} \right)_V \left( \frac{\partial V}{\partial T} \right)_P = \frac{T V \alpha^2}{\kappa_T}$$
- Relación de Compresibilidades:
  $$\frac{C_p}{C_v} = \frac{\kappa_T}{\kappa_S} = \gamma$$

### Nivel Universitario / Avanzado

#### 10.4 Ecuaciones de Estado de la Energía Interna y Efecto Joule-Thomson

- Primera Ecuación de Estado de la Energía:
  $$\left( \frac{\partial U}{\partial V} \right)_T = T \left( \frac{\partial P}{\partial T} \right)_V - P = \frac{T \alpha}{\kappa_T} - P$$
- Segunda Ecuación de Estado de la Energía (Entalpía):
  $$\left( \frac{\partial H}{\partial P} \right)_T = V - T \left( \frac{\partial V}{\partial T} \right)_P = V(1 - T\alpha)$$
- Coeficiente de Joule-Thomson ($\mu_{\text{JT}}$):
  $$\mu_{\text{JT}} = \left( \frac{\partial T}{\partial P} \right)_H = \frac{1}{C_p} \left[ T \left( \frac{\partial V}{\partial T} \right)_P - V \right] = \frac{V}{C_p}(T\alpha - 1)$$
- Temperatura de Inversión de Joule-Thomson ($\mu_{\text{JT}} = 0$):
  $$T_{\text{inv}} = \frac{V}{\left( \frac{\partial V}{\partial T} \right)_P} = \frac{1}{\alpha}$$

#### 10.5 Ecuación de Gibbs-Duhem y Propiedades Molares Parciales

- Ecuación de Gibbs-Duhem:
  $$S dT - V dP + \sum_{i=1}^k N_i d\mu_i = 0 \implies \sum_{i=1}^k x_i d\mu_i = 0 \quad (\text{a } T, P \text{ ctes.})$$
- Propiedad Molar Parcial general ($\bar{M}_i$):
  $$\bar{M}_i = \left( \frac{\partial M}{\partial n_i} \right)_{T, P, n_{j \neq i}} \implies M = \sum_{i=1}^k n_i \bar{M}_i$$
- Potencial Químico como Propiedad Molar Parcial:
  $$\mu_i = \bar{G}_i = \left( \frac{\partial G}{\partial n_i} \right)_{T, P, n_{j \neq i}}$$

#### 10.6 Transiciones de Fase y Equilibrio Químico

- Ecuación de Clapeyron (Cualquier transición de fase de 1er orden):
  $$\frac{dP}{dT} = \frac{\Delta s}{\Delta v} = \frac{\Delta h}{T \Delta v}$$
- Ecuación de Clausius-Clapeyron (Vaporización/Sublimación con $v_g \gg v_l$ y gas ideal):
  $$\frac{d \ln P}{dT} = \frac{\Delta h_{\text{vap}}}{R T^2} \implies \ln\left( \frac{P_2}{P_1} \right) = -\frac{\Delta h_{\text{vap}}}{R} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)$$
- Regla de las Fases de Gibbs:
  $$F = C - \mathcal{P} + 2$$
  $$(F = \text{grados de libertad}, \, C = \text{número de componentes}, \, \mathcal{P} = \text{número de fases})$$
- Ecuaciones de Ehrenfest (Transiciones de fase de 2do orden):
  $$\frac{dP}{dT} = \frac{\Delta C_p}{T V \Delta \alpha} = \frac{\Delta \alpha}{\Delta \kappa_T}$$
- Isoterma de Van 't Hoff para Equilibrio Químico:
  $$\Delta G^\circ = -R T \ln(K_p) \implies \frac{d \ln K_p}{dT} = \frac{\Delta H^\circ}{R T^2}$$

#### 10.7 Tercera Ley de la Termodinámica (Teorema del Calor de Nernst)

- Comportamiento asíntotico en el cero absoluto:
  $$\lim_{T \to 0} S = 0 \quad (\text{para un cristal perfecto})$$
  $$\lim_{T \to 0} C_p = \lim_{T \to 0} C_v = 0, \quad \lim_{T \to 0} \alpha = 0, \quad \lim_{T \to 0} \left( \frac{\partial P}{\partial T} \right)_V = 0$$

## 11. Termodinámica Estadística

### Nivel Universitario / Avanzado

#### 11.1 Colectividades y Funciones de Partición

- Entropía Estadística de Boltzmann:
  $$S = k_B \ln(\Omega)$$
- Entropía de Gibbs (Distribución general):
  $$S = -k_B \sum_i P_i \ln(P_i)$$
- Factor de Boltzmann ($\beta$):
  $$\beta = \frac{1}{k_B T}$$

#### 11.2 Colectividad Canónica (Sistema cerrado a $N, V, T$ fijos)

- Función de Partición Canónica ($Z$ o $Q$):
  $$Z = \sum_i g_i \exp(-\beta E_i) = \sum_i \exp(-\beta E_i)$$
- Probabilidad de ocupación del microestado $i$:
  $$P_i = \frac{\exp(-\beta E_i)}{Z}$$
- Conexión con los Potenciales Termodinámicos:
  - Energía Libre de Helmholtz:
    $$F = -k_B T \ln(Z)$$
  - Energía Interna:
    $$U = \langle E \rangle = -\frac{\partial \ln Z}{\partial \beta} = k_B T^2 \left( \frac{\partial \ln Z}{\partial T} \right)_{V, N}$$
  - Entropía:
    $$S = k_B \ln(Z) + \frac{U}{T} = -\left( \frac{\partial F}{\partial T} \right)_{V, N}$$
  - Presión:
    $$P = k_B T \left( \frac{\partial \ln Z}{\partial V} \right)_{T, N} = -\left( \frac{\partial F}{\partial V} \right)_{T, N}$$
  - Potencial Químico:
    $$\mu = -k_B T \left( \frac{\partial \ln Z}{\partial N} \right)_{T, V} = \left( \frac{\partial F}{\partial N} \right)_{T, V}$$

#### 11.3 Colectividad Gran Canónica (Sistema abierto a $\mu, V, T$ fijos)

- Gran Función de Partición ($\Xi$):
  $$\Xi = \sum_{N=0}^\infty \sum_i \exp\left[ -\beta (E_{i,N} - \mu N) \right] = \sum_{N=0}^\infty \lambda^N Z_N, \quad \lambda = e^{\beta \mu} \quad (\text{fugacidad})$$
- Conexión con el Gran Potencial:
  $$\Phi_G = -P V = -k_B T \ln(\Xi)$$
- Número medio de partículas:
  $$\langle N \rangle = k_B T \left( \frac{\partial \ln \Xi}{\partial \mu} \right)_{T, V} = \frac{1}{\beta} \left( \frac{\partial \ln \Xi}{\partial \mu} \right)$$

#### 11.4 Estadísticas Cuánticas (Ocupación media del estado monoparticular $\epsilon_i$)

- Estadística de Maxwell-Boltzmann (Partículas clásicas distinguibles):
  $$\langle n_i \rangle_{\text{MB}} = \frac{1}{\exp[\beta(\epsilon_i - \mu)]}$$
- Estadística de Fermi-Dirac (Fermiones, espín semi-entero, Principio de Exclusión):
  $$\langle n_i \rangle_{\text{FD}} = \frac{1}{\exp[\beta(\epsilon_i - \mu)] + 1}$$
  $$\text{Energía de Fermi en } T = 0\text{ K}: \quad E_F = \frac{\hbar^2}{2m} (3\pi^2 n)^{2/3}, \quad n = \frac{N}{V}$$
- Estadística de Bose-Einstein (Bosones, espín entero):
  $$\langle n_i \rangle_{\text{BE}} = \frac{1}{\exp[\beta(\epsilon_i - \mu)] - 1}, \quad \mu \le \epsilon_0$$
  $$\text{Temperatura Crítica de Condensación de Bose-Einstein}: \quad T_c = \frac{2\pi \hbar^2}{m k_B} \left( \frac{n}{\zeta(3/2)} \right)^{2/3}, \quad \zeta(3/2) \approx 2.612$$

# Compendio IV: Electricidad y Magnetismo
*(Nivel Básico a Universitario)*

## 12. Electrostática y Medios Dieléctricos

### Nivel Básico

#### 12.1 Ley de Coulomb y Fuerza Eléctrica

- Magnitud de la fuerza entre dos cargas puntuales:
  $$F = \frac{1}{4\pi\varepsilon_0} \frac{|q_1 q_2|}{r^2} = k_e \frac{|q_1 q_2|}{r^2}, \quad k_e \approx 8.9875 \times 10^9 \, \frac{\text{N}\cdot\text{m}^2}{\text{C}^2}$$
- Forma vectorial de la fuerza sobre $q_1$ debida a $q_2$:
  $$\vec{F}_{12} = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r_{21}^2} \hat{r}_{21}$$

#### 12.2 Campo Eléctrico ($\vec{E}$)

- Definición por carga de prueba:
  $$\vec{E} = \frac{\vec{F}}{q_0}$$
- Campo de una carga puntual:
  $$\vec{E} = \frac{1}{4\pi\varepsilon_0} \frac{q}{r^2} \hat{r}$$
- Principio de superposición para $N$ cargas:
  $$\vec{E}_{\text{total}} = \sum_{i=1}^N \vec{E}_i = \frac{1}{4\pi\varepsilon_0} \sum_{i=1}^N \frac{q_i}{r_i^2} \hat{r}_i$$

#### 12.3 Potencial y Energía Potencial Electrostática

- Potencial eléctrico de una carga puntual:
  $$V(r) = \frac{1}{4\pi\varepsilon_0} \frac{q}{r}$$
- Trabajo y diferencia de potencial:
  $$W_{A \to B} = -q_0 \Delta V = q_0 (V_A - V_B)$$
- Energía potencial electrostática de dos cargas:
  $$U = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r}$$

#### 12.4 Capacitancia y Condensadores

- Definición general:
  $$C = \frac{Q}{V}$$
- Condensador de placas plano-paralelas:
  $$C = \frac{\varepsilon_0 A}{d}$$
- Condensador coaxial / cilíndrico (longitud $L$, radios $a < b$):
  $$C = \frac{2\pi\varepsilon_0 L}{\ln(b/a)}$$
- Condensador esférico (radios $a < b$):
  $$C = 4\pi\varepsilon_0 \left( \frac{a b}{b - a} \right)$$
- Asociación de Condensadores:
  $$\text{En Paralelo: } C_{\text{eq}} = \sum_{i=1}^N C_i \quad | \quad \text{En Serie: } \frac{1}{C_{\text{eq}}} = \sum_{i=1}^N \frac{1}{C_i}$$
- Energía almacenada en un condensador:
  $$U = \frac{1}{2} Q V = \frac{1}{2} C V^2 = \frac{Q^2}{2C}$$

### Nivel Intermedio

#### 12.5 Distribuciones Continuas de Carga

- Campo eléctrico para distribución volumétrica continua:
  $$\vec{E}(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \int_V \frac{\rho(\vec{r}')(\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} \, dV'$$
  $$\left( \text{Superficial: } \vec{E}(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \int_S \frac{\sigma(\vec{r}')(\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} \, dA', \quad \text{Lineal: } \vec{E}(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \int_C \frac{\lambda(\vec{r}')(\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} \, d\ell' \right)$$
- Potencial eléctrico continuo:
  $$V(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \int_V \frac{\rho(\vec{r}')}{|\vec{r} - \vec{r}'|} \, dV'$$

#### 12.6 Ley de Gauss en Forma Integral

- Flujo Eléctrico ($\Phi_E$):
  $$\Phi_E = \iint_S \vec{E} \cdot d\vec{A}$$
- Ley de Gauss:
  $$\Phi_E = \oiint_{\partial V} \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}$$

#### 12.7 Relación Diferencial entre Campo y Potencial

- Campo como gradiente del potencial:
  $$\vec{E} = -\nabla V = -\left( \frac{\partial V}{\partial x}\hat{i} + \frac{\partial V}{\partial y}\hat{j} + \frac{\partial V}{\partial z}\hat{k} \right)$$
- Diferencia de potencial por integral de línea:
  $$V_B - V_A = -\int_A^B \vec{E} \cdot d\vec{\ell}$$

#### 12.8 Dipolo Eléctrico

- Momento dipolar eléctrico:
  $$\vec{p} = q \vec{d}$$
- Potencial de un dipolo puntual en el origen:
  $$V(r, \theta) = \frac{1}{4\pi\varepsilon_0} \frac{\vec{p} \cdot \hat{r}}{r^2} = \frac{1}{4\pi\varepsilon_0} \frac{p \cos\theta}{r^2}$$
- Campo eléctrico del dipolo:
  $$\vec{E}(r, \theta) = \frac{1}{4\pi\varepsilon_0 r^3} \left[ 3(\vec{p} \cdot \hat{r})\hat{r} - \vec{p} \right] = \frac{p}{4\pi\varepsilon_0 r^3} (2\cos\theta \hat{u}_r + \sen\theta \hat{u}_\theta)$$
- Torque y energía de un dipolo en campo externo:
  $$\vec{\tau} = \vec{p} \times \vec{E}, \quad U = -\vec{p} \cdot \vec{E}, \quad \vec{F} = (\vec{p} \cdot \nabla)\vec{E}$$

#### 12.9 Dieléctricos y Polarización

- Vector Desplazamiento Eléctrico ($\vec{D}$):
  $$\vec{D} = \varepsilon_0 \vec{E} + \vec{P} = \varepsilon \vec{E} = \varepsilon_0 \varepsilon_r \vec{E}$$
- Vector Polarización ($\vec{P}$) y Susceptibilidad Eléctrica ($\chi_e$):
  $$\vec{P} = \varepsilon_0 \chi_e \vec{E}, \quad \varepsilon_r = 1 + \chi_e$$
- Densidades de Carga Ligada / Polarización:
  $$\rho_b = -\nabla \cdot \vec{P}, \quad \sigma_b = \vec{P} \cdot \hat{n}$$
- Densidad volumétrica de energía electrostática:
  $$u_e = \frac{1}{2} \vec{D} \cdot \vec{E} = \frac{1}{2} \varepsilon E^2$$

### Nivel Universitario / Avanzado

#### 12.10 Ecuaciones Diferenciales de la Electrostática

- Ley de Gauss Diferencial:
  $$\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0} \quad \implies \quad \nabla \cdot \vec{D} = \rho_f$$
- Carácter conservativo:
  $$\nabla \times \vec{E} = \vec{0}$$
- Ecuación de Poisson:
  $$\nabla^2 V = -\frac{\rho}{\varepsilon_0}$$
- Ecuación de Laplace (en regiones libres de carga $\rho = 0$):
  $$\nabla^2 V = 0$$

#### 12.11 Condiciones de Frontera Electrostáticas

- Componente tangencial del campo eléctrico:
  $$\hat{n} \times (\vec{E}_1 - \vec{E}_2) = \vec{0} \implies E_{1t} = E_{2t}$$
- Componente normal del desplazamiento eléctrico:
  $$\hat{n} \cdot (\vec{D}_1 - \vec{D}_2) = \sigma_f \implies D_{1n} - D_{2n} = \sigma_f$$

#### 12.12 Expansión Multipolar del Potencial Electrostático

- Serie de potencias:
  $$V(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \left[ \frac{Q_{\text{total}}}{r} + \frac{\vec{p} \cdot \hat{r}}{r^2} + \frac{1}{2 r^3} \sum_{i,j} Q_{ij} \hat{r}_i \hat{r}_j + \dots \right]$$
- Tensor del momento cuadrupolar ($Q_{ij}$):
  $$Q_{ij} = \int (3 x'_i x'_j - r'^2 \delta_{ij}) \rho(\vec{r}') dV'$$

#### 12.13 Energía Electrostática Total de un Sistema Continuo

- En términos de fuentes:
  $$U = \frac{1}{2} \int_V \rho(\vec{r}) V(\vec{r}) dV$$
- En términos de campo:
  $$U = \frac{1}{2} \int_{\text{todo el espacio}} \vec{D} \cdot \vec{E} \, dV = \frac{\varepsilon_0}{2} \int E^2 \, dV$$

## 13. Electrodinámica, Corriente y Circuitos Eléctricos

### Nivel Básico

#### 13.1 Corriente, Resistencia y Ley de Ohm

- Intensidad de corriente eléctrica:
  $$I = \frac{dQ}{dt}$$
- Ley de Ohm Macroscópica:
  $$V = I R$$
- Resistencia en función de la geometría:
  $$R = \rho_e \frac{L}{A} = \frac{L}{\sigma_c A}$$
- Variación de la resistividad con la temperatura:
  $$\rho_e(T) = \rho_0 [1 + \alpha (T - T_0)]$$

#### 13.2 Potencia Eléctrica y Efecto Joule

- Potencia disipada / consumida:
  $$P = V I = I^2 R = \frac{V^2}{R}$$
- Energía disipada por efecto Joule:
  $$W = \int P \, dt = I^2 R t \quad (\text{para } I \text{ constante})$$

#### 13.3 Fuerza Electromotriz (FEM) y Asociación de Resistencias

- FEM ($\mathcal{E}$) y voltaje terminal con resistencia interna $r$:
  $$V_{\text{terminal}} = \mathcal{E} - I r$$
- Asociación de Resistencias:
  $$\text{En Serie: } R_{\text{eq}} = \sum_{i=1}^N R_i \quad | \quad \text{En Paralelo: } \frac{1}{R_{\text{eq}}} = \sum_{i=1}^N \frac{1}{R_i}$$

### Nivel Intermedio

#### 13.4 Densidad de Corriente y Ley de Ohm Microscópica

- Densidad de corriente ($\vec{J}$):
  $$\vec{J} = n q \vec{v}_d, \quad I = \iint_S \vec{J} \cdot d\vec{A}$$
- Ley de Ohm Puntual / Microscópica:
  $$\vec{J} = \sigma_c \vec{E} = \frac{1}{\rho_e} \vec{E}$$
- Modelo de Drude para la conductividad:
  $$\sigma_c = \frac{n q^2 \tau_c}{m_e}$$

#### 13.5 Leyes de Kirchhoff

- Ley de Corrientes de Kirchhoff (Nodos - Conservación de carga):
  $$\sum_{k=1}^n I_k = 0$$
- Ley de Voltajes de Kirchhoff (Mallas - Conservación de energía):
  $$\sum_{k=1}^m V_k = \sum_{k=1}^m \mathcal{E}_k - \sum_{k=1}^m I_k R_k = 0$$

#### 13.6 Circuitos Transitorios de Primer Orden en Corriente Continua (DC)

- Circuito RC - Carga del Condensador ($\tau = RC$):
  $$q(t) = C\mathcal{E} (1 - e^{-t/\tau}), \quad i(t) = \frac{\mathcal{E}}{R} e^{-t/\tau}, \quad V_C(t) = \mathcal{E}(1 - e^{-t/\tau})$$
- Circuito RC - Descarga del Condensador:
  $$q(t) = Q_0 e^{-t/\tau}, \quad i(t) = -\frac{Q_0}{\tau} e^{-t/\tau}, \quad V_C(t) = V_0 e^{-t/\tau}$$
- Circuito RL - Crecimiento de Corriente ($\tau = L/R$):
  $$i(t) = \frac{\mathcal{E}}{R} (1 - e^{-t/\tau}), \quad V_L(t) = \mathcal{E} e^{-t/\tau}$$
- Circuito RL - Decaimiento de Corriente:
  $$i(t) = I_0 e^{-t/\tau}$$

### Nivel Universitario / Avanzado

#### 13.7 Ecuación de Continuidad de la Carga

- Conservación local de la carga:
  $$\nabla \cdot \vec{J} + \frac{\partial \rho}{\partial t} = 0$$
- Régimen Estacionario ($\partial\rho/\partial t = 0$):
  $$\nabla \cdot \vec{J} = 0 \implies \oiint_S \vec{J} \cdot d\vec{A} = 0$$

#### 13.8 Análisis de Circuitos en Régimen Senoidal Permanente (AC - Fasores)

- Representación fasorial de tensiones y corrientes:
  $$v(t) = V_m \cos(\omega t + \phi) \iff \mathbf{V} = V_{\text{rms}} e^{j\phi} = \frac{V_m}{\sqrt{2}} \angle \phi$$
- Impedancia Compleja ($Z = R + jX$):
  $$Z_R = R, \quad Z_L = j\omega L = \omega L \angle 90^\circ, \quad Z_C = \frac{1}{j\omega C} = -\frac{j}{\omega C} = \frac{1}{\omega C} \angle -90^\circ$$
- Ley de Ohm Fasorial:
  $$\mathbf{V} = \mathbf{I} \mathbf{Z}$$
- Potencia Compleja ($\mathbf{S}$):
  $$\mathbf{S} = \mathbf{V}_{\text{rms}} \mathbf{I}_{\text{rms}}^* = P + j Q = |\mathbf{S}| \cos\theta + j |\mathbf{S}| \sen\theta$$
  $$P = V_{\text{rms}} I_{\text{rms}} \cos(\theta_v - \theta_i) \quad (\text{Potencia Activa, W})$$
  $$Q = V_{\text{rms}} I_{\text{rms}} \sen(\theta_v - \theta_i) \quad (\text{Potencia Reactiva, VAR})$$
  $$|\mathbf{S}| = V_{\text{rms}} I_{\text{rms}} \quad (\text{Potencia Aparente, VA})$$
- Factor de Potencia:
  $$\text{FP} = \cos(\theta_v - \theta_i) = \frac{P}{|\mathbf{S}|}$$

## 14. Magnetostática y Materia Magnética

### Nivel Básico

#### 14.1 Fuerza Magnética y Fuerza de Lorentz

- Fuerza magnética sobre una carga en movimiento:
  $$\vec{F}_B = q (\vec{v} \times \vec{B}) \implies F_B = |q| v B \sen\theta$$
- Fuerza de Lorentz completa:
  $$\vec{F} = q (\vec{E} + \vec{v} \times \vec{B})$$
- Movimiento ciclotrónico (carga perpendicular a campo uniforme):
  $$r = \frac{m v}{|q| B}, \quad \omega_c = \frac{|q| B}{m}, \quad T = \frac{2\pi m}{|q| B}$$

#### 14.2 Fuerza Magnética sobre Conductores

- Conductor rectilíneo con corriente $I$:
  $$\vec{F} = I (\vec{L} \times \vec{B})$$
- Conductor de geometría arbitraria:
  $$\vec{F} = \int_C I (d\vec{\ell} \times \vec{B})$$
- Fuerza magnética entre dos conductores paralelos largos:
  $$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}, \quad \mu_0 = 4\pi \times 10^{-7} \, \frac{\text{T}\cdot\text{m}}{\text{A}}$$

#### 14.3 Dipolo Magnético

- Momento dipolar magnético de una espira plana:
  $$\vec{\mu} = N I A \hat{n}$$
- Torque sobre una espira en campo magnético:
  $$\vec{\tau} = \vec{\mu} \times \vec{B}$$
- Energía potencial magnética del dipolo:
  $$U = -\vec{\mu} \cdot \vec{B}$$

### Nivel Intermedio

#### 14.4 Ley de Biot-Savart

- Campo magnético de un elemento de corriente:
  $$d\vec{B} = \frac{\mu_0 I}{4\pi} \frac{d\vec{\ell} \times \hat{r}}{r^2} = \frac{\mu_0 I}{4\pi} \frac{d\vec{\ell} \times (\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3}$$
- Campo de un conductor rectilíneo infinito:
  $$B = \frac{\mu_0 I}{2\pi R}$$
- Campo en el eje de una espira circular (radio $R$, distancia $z$):
  $$B(z) = \frac{\mu_0 I R^2}{2(R^2 + z^2)^{3/2}}$$

#### 14.5 Ley de Ampère y Flujo Magnético

- Ley de Ampère en forma integral:
  $$\oint_C \vec{B} \cdot d\vec{\ell} = \mu_0 I_{\text{enc}}$$
- Campo en el interior de un solenoide ideal ($n = N/L$):
  $$B = \mu_0 n I$$
- Campo en el interior de un toroide (radio medio $r$):
  $$B = \frac{\mu_0 N I}{2\pi r}$$
- Flujo Magnético ($\Phi_B$):
  $$\Phi_B = \iint_S \vec{B} \cdot d\vec{A}$$
- Ley de Gauss para el Magnetismo (No existencia de monopolos magnéticos aislados):
  $$\oiint_{\partial V} \vec{B} \cdot d\vec{A} = 0$$

#### 14.6 Efecto Hall

- Voltaje Hall en un conductor rectangular (ancho $w$, espesor $d$):
  $$V_H = \frac{I B}{n q d} = R_H \frac{I B}{d}, \quad R_H = \frac{1}{n q} \quad (\text{Coeficiente de Hall})$$

#### 14.7 Medios Magnéticos y Magnetización

- Vector Intensidad Magnética ($\vec{H}$):
  $$\vec{H} = \frac{1}{\mu_0}\vec{B} - \vec{M} \implies \vec{B} = \mu_0 (\vec{H} + \vec{M}) = \mu \vec{H} = \mu_0 \mu_r \vec{H}$$
- Vector Magnetización ($\vec{M}$) y Susceptibilidad Magnética ($\chi_m$):
  $$\vec{M} = \chi_m \vec{H}, \quad \mu_r = 1 + \chi_m$$
- Corrientes de Magnetización / Amperianas:
  $$\vec{J}_b = \nabla \times \vec{M}, \quad \vec{K}_b = \vec{M} \times \hat{n}$$

### Nivel Universitario / Avanzado

#### 14.8 Ecuaciones Diferenciales de la Magnetostática

- Divergencia nula de la inducción magnética:
  $$\nabla \cdot \vec{B} = 0$$
- Ley de Ampère Diferencial:
  $$\nabla \times \vec{B} = \mu_0 \vec{J} \quad \implies \quad \nabla \times \vec{H} = \vec{J}_f$$

#### 14.9 Potencial Vector Magnético ($\vec{A}$)

- Definición ($\vec{B}$ es solenoidal):
  $$\vec{B} = \nabla \times \vec{A}$$
- Calibre / Gauge de Coulomb ($\nabla \cdot \vec{A} = 0$):
  $$\nabla^2 \vec{A} = -\mu_0 \vec{J}$$
- Solución integral del Potencial Vector:
  $$\vec{A}(\vec{r}) = \frac{\mu_0}{4\pi} \int_V \frac{\vec{J}(\vec{r}')}{|\vec{r} - \vec{r}'|} dV'$$

#### 14.10 Condiciones de Frontera Magnetostáticas

- Componente normal de la inducción magnética:
  $$\hat{n} \cdot (\vec{B}_1 - \vec{B}_2) = 0 \implies B_{1n} = B_{2n}$$
- Componente tangencial de la intensidad magnética:
  $$\hat{n} \times (\vec{H}_1 - \vec{H}_2) = \vec{K}_f \implies H_{1t} - H_{2t} = K_f$$

#### 14.11 Densidad y Energía Magnetostática Total

- Densidad volumétrica de energía magnética:
  $$u_m = \frac{1}{2} \vec{B} \cdot \vec{H} = \frac{1}{2\mu_0} B^2$$
- Energía magnética total:
  $$U = \frac{1}{2} \int_V \vec{A} \cdot \vec{J} \, dV = \frac{1}{2} \int_{\text{todo el espacio}} \vec{B} \cdot \vec{H} \, dV$$

## 15. Inducción Electromagnética, Maxwell y Ondas

### Nivel Básico

#### 15.1 Ley de Faraday-Henry y Ley de Lenz

- Fuerza Electromotriz Inducida ($\mathcal{E}$):
  $$\mathcal{E} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt}\left( \iint_S \vec{B} \cdot d\vec{A} \right)$$
- FEM de movimiento en barra conductora (longitud $L$, velocidad $v \perp B$):
  $$\mathcal{E} = B L v$$

#### 15.2 Inductancia y Autoinducción

- Autoinductancia ($L$):
  $$L = \frac{N \Phi_B}{I} \implies \mathcal{E}_L = -L \frac{dI}{dt}$$
- Inductancia de un solenoide ideal (longitud $l$, área $A$, $N$ vueltas):
  $$L = \mu_0 \frac{N^2 A}{l} = \mu_0 n^2 A l$$
- Inductancia Mutua ($M$):
  $$M_{12} = \frac{N_2 \Phi_{21}}{I_1}, \quad \mathcal{E}_2 = -M_{12} \frac{dI_1}{dt}$$
- Energía acumulada en un inductor:
  $$U = \frac{1}{2} L I^2$$

### Nivel Intermedio

#### 15.3 Ley de Ampère-Maxwell y Corriente de Desplazamiento

- Densidad de corriente de desplazamiento (Forma general macroscópica / Vacío):
  $$\vec{J}_d = \frac{\partial \vec{D}}{\partial t} \quad (\text{General}), \quad \vec{J}_d = \varepsilon \frac{\partial \vec{E}}{\partial t} \quad (\text{Medio lineal}), \quad \vec{J}_d = \varepsilon_0 \frac{\partial \vec{E}}{\partial t} \quad (\text{Vacío})$$
- Corriente de desplazamiento total:
  $$I_d = \iint_S \vec{J}_d \cdot d\vec{A} = \frac{d\Phi_D}{dt} = \varepsilon_0 \frac{d\Phi_E}{dt} \quad (\text{en el vacío})$$

#### 15.4 Ecuaciones de Maxwell en Forma Integral (Medios Lineales Generales)

- Ley de Gauss para el campo eléctrico:
  $$\oiint_{\partial V} \vec{D} \cdot d\vec{A} = Q_{f,\text{enc}} \quad \left( \oiint_{\partial V} \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0} \right)$$
- Ley de Gauss para el campo magnético:
  $$\oiint_{\partial V} \vec{B} \cdot d\vec{A} = 0$$
- Ley de Faraday de la Inducción:
  $$\oint_C \vec{E} \cdot d\vec{\ell} = -\frac{d}{dt} \iint_S \vec{B} \cdot d\vec{A}$$
- Ley de Ampère-Maxwell:
  $$\oint_C \vec{H} \cdot d\vec{\ell} = I_{f,\text{enc}} + \frac{d}{dt} \iint_S \vec{D} \cdot d\vec{A}$$

#### 15.5 Teorema de Poynting y Transporte de Energía

- Vector de Poynting ($\vec{S}$):
  $$\vec{S} = \vec{E} \times \vec{H} \quad (\text{Medio material}), \quad \vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B}) \quad (\text{Vacío e isótropo})$$
- Densidad volumétrica total de energía electromagnética:
  $$u = \frac{1}{2} (\vec{D} \cdot \vec{E} + \vec{B} \cdot \vec{H}) \quad (\text{Medio lineal}), \quad u = \frac{1}{2} \left( \varepsilon_0 E^2 + \frac{1}{\mu_0} B^2 \right) \quad (\text{Vacío})$$
- Teorema de Poynting Diferencial (Balance de Potencia):
  $$\nabla \cdot \vec{S} + \frac{\partial u}{\partial t} = -\vec{J} \cdot \vec{E}$$
- Intensidad de Onda Electromagnética ($\langle S \rangle$):
  $$I = \langle |\vec{S}| \rangle = \frac{1}{2} \varepsilon_0 c E_0^2 = \frac{E_0^2}{2 \mu_0 c} = \frac{E_0 B_0}{2\mu_0}$$

### Nivel Universitario / Avanzado

#### 15.6 Ecuaciones de Maxwell en Forma Diferencial

- Forma Microscópica (en el vacío):
  $$\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$$
  $$\nabla \cdot \vec{B} = 0$$
  $$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$$
  $$\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$$
- Forma Macroscópica (en medios materiales):
  $$\nabla \cdot \vec{D} = \rho_f$$
  $$\nabla \cdot \vec{B} = 0$$
  $$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$$
  $$\nabla \times \vec{H} = \vec{J}_f + \frac{\partial \vec{D}}{\partial t}$$

#### 15.7 Potenciales Electrodinámicos y Transformaciones de Calibre

- Definición de potenciales en términos dependientes del tiempo:
  $$\vec{B} = \nabla \times \vec{A}, \quad \vec{E} = -\nabla V - \frac{\partial \vec{A}}{\partial t}$$
- Transformaciones de Calibre (para cualquier función escalar $\Lambda(\vec{r}, t)$):
  $$\vec{A}' = \vec{A} + \nabla \Lambda, \quad V' = V - \frac{\partial \Lambda}{\partial t}$$
- Condición de Calibre de Lorenz:
  $$\nabla \cdot \vec{A} + \frac{1}{c^2} \frac{\partial V}{\partial t} = 0 \implies \nabla \cdot \vec{A} + \mu_0 \varepsilon_0 \frac{\partial V}{\partial t} = 0$$
- Ecuaciones de Onda Inhomogéneas para los Potenciales (en Calibre de Lorenz):
  $$\nabla^2 V - \frac{1}{c^2} \frac{\partial^2 V}{\partial t^2} = -\frac{\rho}{\varepsilon_0} \iff \Box V = -\frac{\rho}{\varepsilon_0}$$
  $$\nabla^2 \vec{A} - \frac{1}{c^2} \frac{\partial^2 \vec{A}}{\partial t^2} = -\mu_0 \vec{J} \iff \Box \vec{A} = -\mu_0 \vec{J}$$
  $$(\Box = \nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2} = \text{Operador d'Alembertiano})$$
- Potenciales Retardados de Liénard-Wiechert (Tiempo retardado $t_r = t - |\vec{r} - \vec{r}'|/c$):
  $$V(\vec{r}, t) = \frac{1}{4\pi\varepsilon_0} \int \frac{\rho(\vec{r}', t_r)}{|\vec{r} - \vec{r}'|} dV'$$
  $$\vec{A}(\vec{r}, t) = \frac{\mu_0}{4\pi} \int \frac{\vec{J}(\vec{r}', t_r)}{|\vec{r} - \vec{r}'|} dV'$$

#### 15.8 Ondas Electromagnéticas Planas en el Vacío

- Ecuaciones de Onda Homogéneas:
  $$\nabla^2 \vec{E} - \frac{1}{c^2} \frac{\partial^2 \vec{E}}{\partial t^2} = \vec{0}, \quad \nabla^2 \vec{B} - \frac{1}{c^2} \frac{\partial^2 \vec{B}}{\partial t^2} = \vec{0}$$
- Velocidad de la luz en el vacío:
  $$c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 2.9979 \times 10^8 \, \frac{\text{m}}{\text{s}}$$
- Solución de Onda Plana Monocromática ($\vec{k} = \text{vector de onda}$):
  $$\vec{E}(\vec{r}, t) = \vec{E}_0 e^{i(\vec{k} \cdot \vec{r} - \omega t)}, \quad \vec{B}(\vec{r}, t) = \vec{B}_0 e^{i(\vec{k} \cdot \vec{r} - \omega t)}$$
  $$\vec{B}_0 = \frac{1}{\omega} (\vec{k} \times \vec{E}_0) = \frac{1}{c} (\hat{k} \times \vec{E}_0), \quad \vec{k} \cdot \vec{E}_0 = 0, \quad \vec{k} \cdot \vec{B}_0 = 0$$
- Impedancia Característica del Vacío ($\eta_0$):
  $$\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 120\pi \, \Omega \approx 376.73 \, \Omega$$

#### 15.9 Tensor de Esfuerzos de Maxwell ($T_{ij}$) y Momento Electromagnético

- Tensor de Esfuerzos de Maxwell:
  $$T_{ij} = \varepsilon_0 \left( E_i E_j - \frac{1}{2} \delta_{ij} E^2 \right) + \frac{1}{\mu_0} \left( B_i B_j - \frac{1}{2} \delta_{ij} B^2 \right)$$
- Ley de Conservación del Momento Lineal:
  $$\vec{f}_{\text{Lorentz}} + \frac{\partial \vec{g}}{\partial t} = \nabla \cdot \mathbf{T}, \quad \vec{g} = \varepsilon_0 (\vec{E} \times \vec{B}) = \frac{\vec{S}}{c^2} \quad (\text{Densidad de Momento})$$
- Presión de Radiación ($P_{\text{rad}}$ para incidencia normal):
  $$P_{\text{rad}} = \frac{I}{c} \quad (\text{Absorción total}), \quad P_{\text{rad}} = \frac{2I}{c} \quad (\text{Reflexión total})$$

#### 15.10 Formulación Covariante / Cuadrivectorial de la Electrodinámica (Métrica $\eta_{\mu\nu} = \operatorname{diag}(+1, -1, -1, -1)$)

- Cuadrivector Posición, Gradiente y Corriente:
  $$x^\mu = (ct, \vec{r}), \quad \partial_\mu = \left( \frac{1}{c}\frac{\partial}{\partial t}, \nabla \right), \quad \partial^\mu = \left( \frac{1}{c}\frac{\partial}{\partial t}, -\nabla \right), \quad J^\mu = (c\rho, \vec{J})$$
- Cuadripotencial:
  $$A^\mu = \left( \frac{V}{c}, \vec{A} \right), \quad A_\mu = \left( \frac{V}{c}, -\vec{A} \right)$$
- Tensor de Campo Electromagnético de Faraday ($F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$):
  $$F^{\mu\nu} = \begin{bmatrix} 0 & -E_x/c & -E_y/c & -E_z/c \\ E_x/c & 0 & -B_z & B_y \\ E_y/c & B_z & 0 & -B_x \\ E_z/c & -B_y & B_x & 0 \end{bmatrix}$$
- Tensor Dual de Campo Electromagnético ($\tilde{F}^{\mu\nu} = \frac{1}{2} \epsilon^{\mu\nu\alpha\beta} F_{\alpha\beta}$):
  $$\tilde{F}^{\mu\nu} = \begin{bmatrix} 0 & -B_x & -B_y & -B_z \\ B_x & 0 & E_z/c & -E_y/c \\ B_y & -E_z/c & 0 & E_x/c \\ B_z & E_y/c & -E_x/c & 0 \end{bmatrix}$$
- Ecuaciones de Maxwell Covariantes:
  $$\partial_\mu F^{\mu\nu} = \mu_0 J^\nu \quad (\text{Gauss y Ampère-Maxwell})$$
  $$\partial_\mu \tilde{F}^{\mu\nu} = 0 \quad (\text{Gauss Magnética y Faraday})$$
- Invariantes de Lorentz del Campo Electromagnético:
  $$I_1 = F^{\mu\nu} F_{\mu\nu} = 2 \left( B^2 - \frac{E^2}{c^2} \right) = \text{invariante}$$
  $$I_2 = \epsilon_{\mu\nu\alpha\beta} F^{\mu\nu} F^{\alpha\beta} = -\frac{4}{c} (\vec{E} \cdot \vec{B}) = \text{invariante}$$

# Compendio V: Óptica y Luz
*(Nivel Básico a Universitario)*

## 16. Óptica Geométrica y Sistemas Ópticos

### Nivel Básico

#### 16.1 Propagación de la Luz y Leyes Fundamentales

- Índice de refracción absoluto ($c = \text{velocidad en el vacío}$):
  $$n = \frac{c}{v}$$
- Ley de Reflexión:
  $$\theta_i = \theta_r$$
- Ley de Refracción (Ley de Snell):
  $$n_1 \sen(\theta_1) = n_2 \sen(\theta_2)$$
- Ángulo Crítico y Reflexión Interna Total ($n_1 > n_2$):
  $$\sen(\theta_c) = \frac{n_2}{n_1} \implies \theta_c = \arcsen\left( \frac{n_2}{n_1} \right)$$

#### 16.2 Espejos Planos y Esféricos (Aproximación Paraxial)

- Relación entre Radio de Curvatura y Distancia Focal:
  $$f = \frac{R}{2}$$
- Ecuación de Descartes para Espejos Esféricos ($s_o = \text{objeto}, \, s_i = \text{imagen}$):
  $$\frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f} = \frac{2}{R}$$
- Aumento Lateral Transversal ($m$):
  $$m = \frac{y_i}{y_o} = -\frac{s_i}{s_o}$$

### Nivel Intermedio

#### 16.3 Dioptrios Esféricos y Lentes Delgadas

- Refracción en un Dioptrio Esférico:
  $$\frac{n_1}{s_o} + \frac{n_2}{s_i} = \frac{n_2 - n_1}{R}$$
- Fórmula del Fabricante de Lentes (Lente delgada en el aire $n_{\text{medio}} = 1$):
  $$\frac{1}{f} = (n - 1)\left( \frac{1}{R_1} - \frac{1}{R_2} + \frac{(n - 1)d}{n R_1 R_2} \right) \xrightarrow{d \to 0} (n - 1)\left( \frac{1}{R_1} - \frac{1}{R_2} \right)$$
- Ecuación de Gauss para Lentes Delgadas:
  $$\frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f}$$
- Forma Newtoniana de la Ecuación de Lentes ($x_o = s_o - f, \, x_i = s_i - f$):
  $$x_o \cdot x_i = f^2$$
- Potencia Óptica ($P$ en dioptrías $\text{m}^{-1}$):
  $$P = \frac{1}{f}$$
- Lentes Delgadas en Contacto:
  $$P_{\text{eq}} = \sum_{i=1}^N P_i \implies \frac{1}{f_{\text{eq}}} = \frac{1}{f_1} + \frac{1}{f_2} + \dots + \frac{1}{f_N}$$
- Lentes Separadas por una Distancia $d$:
  $$\frac{1}{f_{\text{eq}}} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 f_2}$$

#### 16.4 Prismas y Dispersión Cromática

- Desviación Angular en un Prisma de Ángulo de Ápice $A$:
  $$\delta = \theta_1 + \theta_2' - A$$
- Ángulo de Mínima Desviación ($\delta_{\min}$):
  $$n = \frac{\sen\left( \frac{A + \delta_{\min}}{2} \right)}{\sen\left( \frac{A}{2} \right)}$$
- Número de Abbe / Potencia Dispersiva ($V_d$):
  $$V_d = \frac{n_d - 1}{n_F - n_C}$$

### Nivel Universitario / Avanzado

#### 16.5 Óptica Matricial (Matrices de Rayos ABCD)

- Vector de Rayo Paraxial (Altura $y$, ángulo $\theta$ respecto al eje óptico):
  $$\begin{bmatrix} y_2 \\ \theta_2 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} y_1 \\ \theta_1 \end{bmatrix}, \quad \det\left( \mathbf{M} \right) = AD - BC = \frac{n_1}{n_2}$$
- Matriz de Traslación Libre en Medio Homogéneo (distancia $d$):
  $$\mathbf{M}_{\text{tras}} = \begin{bmatrix} 1 & d \\ 0 & 1 \end{bmatrix}$$
- Matriz de Refracción en Interfaz Plana:
  $$\mathbf{M}_{\text{ref,plana}} = \begin{bmatrix} 1 & 0 \\ 0 & \frac{n_1}{n_2} \end{bmatrix}$$
- Matriz de Refracción en Dioptrio Esférico:
  $$\mathbf{M}_{\text{dioptrio}} = \begin{bmatrix} 1 & 0 \\ -\frac{n_2 - n_1}{n_2 R} & \frac{n_1}{n_2} \end{bmatrix}$$
- Matriz de Lente Delgada:
  $$\mathbf{M}_{\text{lente}} = \begin{bmatrix} 1 & 0 \\ -\frac{1}{f} & 1 \end{bmatrix}$$
- Matriz de Espejo Esférico:
  $$\mathbf{M}_{\text{espejo}} = \begin{bmatrix} 1 & 0 \\ -\frac{2}{R} & 1 \end{bmatrix}$$

#### 16.6 Principio Variacional y Óptica Hamiltoniana

- Principio de Fermat (Camino Óptico Estacionario):
  $$\delta \mathcal{S} = \delta \int_{P_1}^{P_2} n(\vec{r}) \, ds = 0$$
- Longitud de Camino Óptico (OPL):
  $$\text{OPL} = \int_C n(\vec{r}) \, ds$$
- Ecuación Diferencial del Rayo:
  $$\frac{d}{ds}\left( n \frac{d\vec{r}}{ds} \right) = \nabla n$$
- Ecuación de la Eikonal (Límite de longitud de onda cero $\lambda \to 0$ para fase $S$):
  $$|\nabla S|^2 = n^2(\vec{r})$$

## 17. Óptica Ondulatoria (Interferencia, Difracción y Polarización)

### Nivel Básico

#### 17.1 Interferencia por División de Frente de Onda

- Experimento de la Doble Rendija de Young (Separación $d$, distancia a pantalla $D \gg d$):
  - Máximos de Interferencia (Constructiva):
    $$d \sen\theta = m \lambda \implies y_{\text{máx}} \approx m \frac{\lambda D}{d}, \quad m \in \mathbb{Z}$$
  - Mínimos de Interferencia (Destructiva):
    $$d \sen\theta = \left( m + \frac{1}{2} \right)\lambda \implies y_{\text{mín}} \approx \left( m + \frac{1}{2} \right)\frac{\lambda D}{d}, \quad m \in \mathbb{Z}$$
  - Separación entre Franjas Consecutivas ($\Delta y$):
    $$\Delta y = \frac{\lambda D}{d}$$

#### 17.2 Polarización de la Luz

- Ley de Malus (Intensidad tras polarizador lineal con ángulo $\theta$):
  $$I = I_0 \cos^2\theta$$
- Ángulo de Polarización de Brewster:
  $$\tan(\theta_B) = \frac{n_2}{n_1} \implies \theta_B + \theta_t = 90^\circ$$

### Nivel Intermedio

#### 17.3 Distribución de Intensidad en Interferencia

- Superposición de Dos Ondas Armónicas Coherentes:
  $$I = I_1 + I_2 + 2\sqrt{I_1 I_2} \cos(\delta)$$
- Diferencia de Fase ($\delta$) por Diferencia de Camino Óptico ($\Delta r$):
  $$\delta = k \Delta r + \Delta\phi_0 = \frac{2\pi}{\lambda} \Delta r + \Delta\phi_0$$
- Visibilidad o Contraste de Franjas:
  $$\mathcal{V} = \frac{I_{\text{máx}} - I_{\text{mín}}}{I_{\text{máx}} + I_{\text{mín}}} = \frac{2\sqrt{I_1 I_2}}{I_1 + I_2}$$

#### 17.4 Interferencia en Películas Delgadas (Espesor $t$, incidencia casi normal)

- Condición de Interferencia Constructiva (Reflexión):
  $$2 n t = \left( m + \frac{1}{2} \right)\lambda \quad (\text{con un solo cambio de fase de } \pi)$$
  $$2 n t = m \lambda \quad (\text{con } 0 \text{ o } 2 \text{ cambios de fase de } \pi)$$
- Anillos de Newton (Radio del $m$-ésimo anillo brillante/oscuro por reflexión):
  $$r_{\text{oscuro}} = \sqrt{m \lambda R}, \quad r_{\text{brillante}} = \sqrt{\left(m + \frac{1}{2}\right)\lambda R}$$

#### 17.5 Difracción de Fraunhofer (Campo Lejano)

- Rendija Simple de Ancho $a$:
  - Mínimos de difracción:
    $$a \sen\theta = m \lambda, \quad m = \pm 1, \pm 2, \dots$$
  - Distribución de intensidad:
    $$I(\theta) = I_0 \left[ \frac{\sen(\beta)}{\beta} \right]^2 = I_0 \operatorname{sinc}^2(\beta), \quad \beta = \frac{\pi a}{\lambda}\sen\theta$$
- Doble Rendija con Difracción e Interferencia Combinadas:
  $$I(\theta) = I_0 \cos^2(\alpha) \left[ \frac{\sen(\beta)}{\beta} \right]^2, \quad \alpha = \frac{\pi d}{\lambda}\sen\theta, \quad \beta = \frac{\pi a}{\lambda}\sen\theta$$
- Abertura Circular de Diámetro $D$ (Patrón de Airy):
  - Primer anillo oscuro (Criterio de Rayleigh para resolución angular):
    $$\sen\theta_{\min} \approx 1.22 \frac{\lambda}{D}$$
- Redes de Difracción ($N$ rendijas, espaciado $d$):
  - Ecuación de la red (Máximos principales):
    $$d \sen\theta = m \lambda, \quad m \in \mathbb{Z}$$
  - Poder de Resolución Espectral ($R$):
    $$\mathcal{R} = \frac{\lambda}{\Delta\lambda} = m N$$
  - Dispersión Angular ($D_\theta$):
    $$D_\theta = \frac{d\theta}{d\lambda} = \frac{m}{d \cos\theta}$$

#### 17.6 Ecuaciones de Fresnel para Interfaces Dieléctricas Planas

- Coeficientes de Reflexión en Amplitud:
  $$r_\perp = \frac{n_1 \cos\theta_i - n_2 \cos\theta_t}{n_1 \cos\theta_i + n_2 \cos\theta_t} = -\frac{\sen(\theta_i - \theta_t)}{\sen(\theta_i + \theta_t)}$$
  $$r_\parallel = \frac{n_2 \cos\theta_i - n_1 \cos\theta_t}{n_2 \cos\theta_i + n_1 \cos\theta_t} = \frac{\tan(\theta_i - \theta_t)}{\tan(\theta_i + \theta_t)}$$
- Coeficientes de Transmisión en Amplitud:
  $$t_\perp = \frac{2 n_1 \cos\theta_i}{n_1 \cos\theta_i + n_2 \cos\theta_t} = \frac{2 \sen\theta_t \cos\theta_i}{\sen(\theta_i + \theta_t)}$$
  $$t_\parallel = \frac{2 n_1 \cos\theta_i}{n_2 \cos\theta_i + n_1 \cos\theta_t} = \frac{2 \sen\theta_t \cos\theta_i}{\sen(\theta_i + \theta_t)\cos(\theta_i - \theta_t)}$$
- Reflectancia ($R$) y Transmitancia ($T_w$) de Potencia:
  $$R_\perp = |r_\perp|^2, \quad R_\parallel = |r_\parallel|^2, \quad R + T_w = 1$$

### Nivel Universitario / Avanzado

#### 17.7 Teoría Escalar de Difracción (Fresnel y Kirchhoff)

- Integral de Difracción de Fresnel-Kirchhoff:
  $$U(P) = -\frac{i}{2\lambda} \iint_{\Sigma} U_0 \frac{e^{i k r}}{r} [\cos(\hat{n}, \vec{r}) - \cos(\hat{n}, \vec{r}_0)] dS$$
- Integral de Difracción de Fresnel (Paraxial en distancia $z$):
  $$U(x, y, z) = \frac{e^{i k z}}{i \lambda z} \iint_{-\infty}^{\infty} U(\xi, \eta, 0) \exp\left\{ \frac{i k}{2z}\left[ (x - \xi)^2 + (y - \eta)^2 \right] \right\} d\xi d\eta$$
- Número de Fresnel ($N_F$):
  $$N_F = \frac{a^2}{\lambda z} \quad (N_F \gg 1 \text{ Ópt. Geométrica}, \, N_F \sim 1 \text{ Fresnel}, \, N_F \ll 1 \text{ Fraunhofer})$$
- Difracción de Fraunhofer como Transformada de Fourier:
  $$U(x, y) \propto \mathcal{F}\{U(\xi, \eta)\}\Big|_{f_x = \frac{x}{\lambda z}, f_y = \frac{y}{\lambda z}}$$

#### 17.8 Formalismo de Polarización (Jones y Stokes-Mueller)

- Vector de Jones para Estados de Polarización Totalmente Coherentes:
  $$\vec{J} = \begin{bmatrix} E_{0x} e^{i\phi_x} \\ E_{0y} e^{i\phi_y} \end{bmatrix}$$
- Matrices de Jones de Elementos Ópticos Clásicos:
  $$\mathbf{M}_{\text{pol,H}} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \quad \mathbf{M}_{\text{retardador}}(\Gamma) = \begin{bmatrix} e^{i\Gamma/2} & 0 \\ 0 & e^{-i\Gamma/2} \end{bmatrix}$$
- Parámetros de Stokes (Para luz arbitraria o parcialmente polarizada):
  $$S_0 = I = I_H + I_V, \quad S_1 = Q = I_H - I_V, \quad S_2 = U = I_{+45^\circ} - I_{-45^\circ}, \quad S_3 = V = I_R - I_L$$
- Grado de Polarización ($DOP$):
  $$\text{DOP} = \frac{\sqrt{S_1^2 + S_2^2 + S_3^2}}{S_0} \le 1$$
- Ecuación de Transformación de Mueller:
  $$\vec{S}_{\text{sal}} = \mathbf{M}_{\text{Mueller}} \vec{S}_{\text{ent}}$$

#### 17.9 Birrefringencia y Óptica de Cristales Anisótropos

- Elipsoide de Índices Ópticos (Indicatriz Óptica):
  $$\frac{x^2}{n_x^2} + \frac{y^2}{n_y^2} + \frac{z^2}{n_z^2} = 1$$
- Retardo de Fase en Lámina Birrefringente de Espesor $d$:
  $$\Delta\phi = \Gamma = \frac{2\pi}{\lambda} |n_e - n_o| d$$
  $$\text{Lámina de Cuarto de Onda: } d = \frac{\lambda}{4|n_e - n_o|}, \quad \text{Lámina de Media Onda: } d = \frac{\lambda}{2|n_e - n_o|}$$

## 18. Óptica Electromagnética, Dispersión y Guías de Ondas

### Nivel Intermedio

#### 18.1 Dispersión y Propagación en Medios Materiales

- Relación entre Índice de Refracción y Constantes Dieléctricas:
  $$n = \sqrt{\varepsilon_r \mu_r} \approx \sqrt{\varepsilon_r}$$
- Ecuación Empírica de Dispersión de Cauchy:
  $$n(\lambda) = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4} + \dots$$
- Ecuación de Sellmeier:
  $$n^2(\lambda) = 1 + \sum_{i} \frac{B_i \lambda^2}{\lambda^2 - C_i}$$
- Velocidad de Fase y Velocidad de Grupo:
  $$v_p = \frac{\omega}{k} = \frac{c}{n}, \quad v_g = \frac{d\omega}{dk} = \frac{c}{n_g}, \quad n_g = n - \lambda \frac{dn}{d\lambda}$$
- Dispersión por Retardo de Grupo (GVD / Parámetro $D$):
  $$D = -\frac{\lambda}{c} \frac{d^2 n}{d\lambda^2} = -\frac{2\pi c}{\lambda^2} \beta_2, \quad \beta_2 = \frac{d^2 k}{d\omega^2}$$

#### 18.2 Atenuación y Absorción

- Índice de Refracción Complejo:
  $$\tilde{n} = n + i \kappa$$
- Ley de Beer-Lambert (Coeficiente de absorción $\alpha$):
  $$I(z) = I_0 e^{-\alpha z}, \quad \alpha = \frac{2\omega\kappa}{c} = \frac{4\pi\kappa}{\lambda_0}$$
- Profundidad de Penetración / Efecto Piel Óptico ($\delta_s$):
  $$\delta_s = \frac{1}{\alpha} = \frac{\lambda_0}{4\pi\kappa}$$

### Nivel Universitario / Avanzado

#### 18.3 Modelo Microeléctrico de Lorentz-Drude y Relaciones Dispersivas

- Permitividad Relativa Compleja del Modelo de Oscilador de Lorentz:
  $$\tilde{\varepsilon}_r(\omega) = 1 + \frac{N q^2}{\varepsilon_0 m_e} \sum_j \frac{f_j}{\omega_{0j}^2 - \omega^2 - i\gamma_j \omega}$$
- Frecuencia de Plasma (Metales / Modelo de Drude $\omega_{0} = 0$):
  $$\omega_p^2 = \frac{N e^2}{\varepsilon_0 m_e} \implies \varepsilon(\omega) = 1 - \frac{\omega_p^2}{\omega^2 + i\gamma\omega}$$
- Relaciones de Kramers-Kronig (Causalidad en la respuesta dieléctrica):
  $$\text{Re}[\chi(\omega)] = \frac{2}{\pi} \mathcal{P} \int_0^\infty \frac{\Omega \, \text{Im}[\chi(\Omega)]}{\Omega^2 - \omega^2} d\Omega$$
  $$\text{Im}[\chi(\omega)] = -\frac{2\omega}{\pi} \mathcal{P} \int_0^\infty \frac{\text{Re}[\chi(\Omega)]}{\Omega^2 - \omega^2} d\Omega$$

#### 18.4 Fibras Ópticas y Guías de Ondas Dieléctricas

- Apertura Numérica ($\text{NA}$):
  $$\text{NA} = \sen(\theta_{\text{máx}}) = \sqrt{n_{\text{núcleo}}^2 - n_{\text{revestimiento}}^2} \approx n_1 \sqrt{2\Delta}, \quad \Delta = \frac{n_1 - n_2}{n_1}$$
- Parámetro de Frecuencia Normalizada (Número $V$ para fibra de radio $a$):
  $$V = \frac{2\pi a}{\lambda_0} \sqrt{n_1^2 - n_2^2} = \frac{2\pi a}{\lambda_0} \text{NA}$$
- Condición de Monomodo en Fibra de Índice Escalonado:
  $$V < 2.4048 \quad (\text{Primer cero de la función de Bessel } J_0)$$
- Número Aproximado de Modos en Fibra Multimodo de Índice Escalonado ($V \gg 1$):
  $$M \approx \frac{V^2}{2}$$

#### 18.5 Ondas Evanescentes en Reflexión Total Interna

- Vector de onda transversal transmitido imaginario:
  $$k_{tz} = i \alpha = i k_0 \sqrt{n_1^2 \sin^2(\theta_i) - n_2^2}$$
- Decaimiento de la Amplitud del Campo Evanescente:
  $$\vec{E}_t(z) = \vec{E}_{t0} e^{-\alpha z} e^{i(k_{tx} x - \omega t)}$$
- Desplazamiento Lateral de Goos-Hänchen (Polarización s / TE cerca del ángulo crítico):
  $$\Delta x_{\text{GH}} = \frac{2}{k_0 \sqrt{n_1^2 \sin^2(\theta_i) - n_2^2}} \quad \left( \text{Formulación general: } \Delta x_{\text{GH}} = -\frac{d\phi}{dk_x} \right)$$

## 19. Óptica Cuántica, Radiación, Haces Láser y No Lineal

### Nivel Básico

#### 19.1 Fotones y Naturaleza Cuántica de la Luz

- Energía del Fotón (Relación de Planck-Einstein):
  $$E = h f = \hbar \omega, \quad \hbar = \frac{h}{2\pi}$$
- Momento Lineal del Fotón (Relación de De Broglie):
  $$p = \frac{h}{\lambda} = \hbar k = \frac{E}{c}$$
- Ecuación del Efecto Fotoeléctrico de Einstein:
  $$E_{k,\text{máx}} = e V_{\text{corte}} = h f - \Phi$$
- Presión de Radiación ($P_{\text{rad}}$ con densidad de flujo radiante / irradiancia $I$):
  $$P_{\text{rad}} = \frac{I}{c} \quad (\text{Absorción pura}), \quad P_{\text{rad}} = \frac{2I}{c} \quad (\text{Reflexión perfecta})$$

### Nivel Intermedio

#### 19.2 Leyes de Radiación Térmica (Cuerpo Negro)

- Ley de Distribución Espectral de Planck:
  $$u_\lambda(\lambda, T) = \frac{8\pi h c}{\lambda^5} \frac{1}{e^{\frac{h c}{\lambda k_B T}} - 1}, \quad I_\nu(\nu, T) = \frac{2h\nu^3}{c^2}\frac{1}{e^{\frac{h\nu}{k_B T}} - 1}$$
- Ley de Desplazamiento de Wien:
  $$\lambda_{\text{máx}} T = b \approx 2.8978 \times 10^{-3} \, \text{m}\cdot\text{K}$$
- Ley de Stefan-Boltzmann:
  $$j^* = \sigma T^4 = \varepsilon \sigma T^4, \quad \sigma = \frac{2\pi^5 k_B^4}{15 c^2 h^3} \approx 5.6704 \times 10^{-8} \, \frac{\text{W}}{\text{m}^2\cdot\text{K}^4}$$

#### 19.3 Radiometría y Fotometría

- Flujo Radiante ($\Phi_e$ en W) y Flujo Luminoso ($\Phi_v$ en lúmenes lm):
  $$\Phi_v = K_m \int_0^\infty \Phi_{e,\lambda}(\lambda) V(\lambda) d\lambda, \quad K_m \approx 683 \, \frac{\text{lm}}{\text{W}}$$
- Irradiancia ($E_e$) e Iluminancia ($E_v$ en lux):
  $$E_e = \frac{d\Phi_e}{dA}, \quad E_v = \frac{d\Phi_v}{dA}$$
- Intensidad Radiante ($I_e$) e Intensidad Luminosa ($I_v$ en candelas cd):
  $$I = \frac{d\Phi}{d\Omega}$$
- Ley de Lambert (Superficie Difusa Emisora / Reflectora):
  $$I(\theta) = I_0 \cos\theta$$

#### 19.4 Física del Láser y Coeficientes de Einstein

- Relación entre Emisión Espontánea ($A_{21}$), Estimulada ($B_{21}$) y Absorción ($B_{12}$):
  $$g_1 B_{12} = g_2 B_{21}, \quad A_{21} = \frac{8\pi h \nu^3}{c^3} B_{21}$$
- Condición de Inversión de Población para Ganancia Óptica:
  $$N_2 - \frac{g_2}{g_1} N_1 > 0$$
- Ganancia Óptica en Medio Activo (Sección eficaz estimulada $\sigma_{21}$):
  $$I(z) = I_0 e^{\gamma(\nu) z}, \quad \gamma(\nu) = \sigma_{21}(\nu)\left[ N_2 - \frac{g_2}{g_1} N_1 \right]$$
- Condición de Umbral Láser en Cavidad de Longitud $L$ (Reflectancias $R_1, R_2$):
  $$\gamma_{\text{th}} = \alpha_{\text{pérdidas}} + \frac{1}{2L}\ln\left( \frac{1}{R_1 R_2} \right)$$

### Nivel Universitario / Avanzado

#### 19.5 Propagación de Haces Gaussianos ($\text{TEM}_{00}$)

- Parámetro de Rayleigh / Distancia Confocal ($z_R$):
  $$z_R = \frac{\pi w_0^2}{\lambda_0}$$
- Cintura y Perfil del Radio del Haz ($w(z)$ con cintura mínima $w_0$ en $z=0$):
  $$w(z) = w_0 \sqrt{1 + \left( \frac{z}{z_R} \right)^2}$$
- Radio de Curvatura del Frente de Onda ($R(z)$):
  $$R(z) = z \left[ 1 + \left( \frac{z_R}{z} \right)^2 \right]$$
- Divergencia Angular de Campo Lejano ($\theta_{\text{div}}$):
  $$\theta_{\text{div}} = \lim_{z \to \infty} \frac{w(z)}{z} = \frac{\lambda_0}{\pi w_0}$$
- Fase de Gouy:
  $$\zeta(z) = \arctan\left( \frac{z}{z_R} \right)$$
- Parámetro Complejo del Haz $q(z)$ y Transformación $ABCD$:
  $$\frac{1}{q(z)} = \frac{1}{R(z)} - i \frac{\lambda_0}{\pi n w^2(z)} \implies q_2 = \frac{A q_1 + B}{C q_1 + D}$$

#### 19.6 Óptica No Lineal

- Expansión de la Polarización No Lineal:
  $$\vec{P} = \varepsilon_0 \left( \chi^{(1)} \cdot \vec{E} + \chi^{(2)} : \vec{E} \vec{E} + \chi^{(3)} \vdots \vec{E} \vec{E} \vec{E} + \dots \right) = \vec{P}_L + \vec{P}_{\text{NL}}$$
- Generación de Segundo Armónico (SHG):
  $$P^{(2)}(2\omega) = \varepsilon_0 \chi^{(2)} E^2(\omega)$$
- Condición de Ajuste de Fase (Phase Matching):
  $$\Delta k = k(2\omega) - 2k(\omega) = 0 \implies n(2\omega) = n(\omega)$$
- Efecto Kerr Óptico (Índice de refracción dependiente de la intensidad):
  $$n(I) = n_0 + n_2 I, \quad n_2 = \frac{3 \chi^{(3)}}{4 \varepsilon_0 c n_0^2}$$
- Efecto Pockels (Lineal electro-óptico):
  $$\Delta\left(\frac{1}{n^2}\right) = r_{ijk} E_k$$
- Efecto Kerr Electro-óptico (Cuadrático electro-óptico):
  $$\Delta n = \lambda K_{\text{Kerr}} E^2$$

# Compendio VI: Física Moderna
*(Nivel Básico a Universitario)*

## 20. Teoría de la Relatividad (Especial y General)

### Nivel Básico

#### 20.1 Cinemática Relativista Unidimensional

- Factor de Lorentz ($\gamma$ con $\beta = v/c$):
  $$\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} = \frac{1}{\sqrt{1 - \beta^2}}$$
- Dilatación Temporal ($\Delta t_0 = \text{tiempo propio}$):
  $$\Delta t = \gamma \Delta t_0 = \frac{\Delta t_0}{\sqrt{1 - \frac{v^2}{c^2}}}$$
- Contracción de la Longitud ($L_0 = \text{longitud propia}$ en dirección del movimiento):
  $$L = \frac{L_0}{\gamma} = L_0 \sqrt{1 - \frac{v^2}{c^2}}$$
- Adición Relativista de Velocidades (Movimiento en el eje $x$):
  $$u_x' = \frac{u_x - v}{1 - \frac{u_x v}{c^2}} \iff u_x = \frac{u_x' + v}{1 + \frac{u_x' v}{c^2}}$$

#### 20.2 Dinámica y Equivalencia Masa-Energía

- Momento Lineal Relativista:
  $$\vec{p} = \gamma m_0 \vec{v} = \frac{m_0 \vec{v}}{\sqrt{1 - \frac{v^2}{c^2}}}$$
- Energía en Reposo:
  $$E_0 = m_0 c^2$$
- Energía Total de una Partícula Libre:
  $$E = \gamma m_0 c^2 = E_k + m_0 c^2$$
- Energía Cinética Relativista:
  $$E_k = (\gamma - 1) m_0 c^2 = m_0 c^2 \left( \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} - 1 \right)$$
- Relación Fundamental Energía-Momento:
  $$E^2 = (p c)^2 + (m_0 c^2)^2 \implies E = \sqrt{p^2 c^2 + m_0^2 c^4}$$
  $$(\text{Para fotones y partículas sin masa } m_0 = 0 \implies E = p c)$$

#### 20.3 Efecto Doppler Relativista

- Fuente y Observador en Dirección Longitudinal:
  $$f_o = f_s \sqrt{\frac{1 - \beta}{1 + \beta}} \quad (\text{Alejamiento}) \quad | \quad f_o = f_s \sqrt{\frac{1 + \beta}{1 - \beta}} \quad (\text{Acercamiento})$$
- Efecto Doppler Transversal ($\theta = 90^\circ$):
  $$f_o = \frac{f_s}{\gamma} = f_s \sqrt{1 - \beta^2}$$

### Nivel Intermedio

#### 20.4 Transformaciones de Lorentz y Espacio-Tiempo de Minkowski

- Transformación de Coordenadas de Lorentz (Movimiento estándar a lo largo de $x$):
  $$x' = \gamma (x - v t), \quad y' = y, \quad z' = z, \quad t' = \gamma \left( t - \frac{v x}{c^2} \right)$$
- Transformación Inversa:
  $$x = \gamma (x' + v t'), \quad y = y', \quad z = z', \quad t = \gamma \left( t' + \frac{v x'}{c^2} \right)$$
- Intervalo Espaciotemporal Invariante ($s^2$):
  $$\Delta s^2 = c^2 \Delta t^2 - (\Delta x^2 + \Delta y^2 + \Delta z^2) = c^2 \Delta t^2 - |\Delta\vec{r}|^2 = \text{invariante}$$
  $$\Delta s^2 > 0 \quad (\text{Tipo Tiempo}), \quad \Delta s^2 = 0 \quad (\text{Tipo Luz / Nulo}), \quad \Delta s^2 < 0 \quad (\text{Tipo Espacio})$$
- Rapidez Relativista ($\theta$ / Parametrización Hiperbólica):
  $$\beta = \tanh(\theta), \quad \gamma = \cosh(\theta), \quad \gamma\beta = \sinh(\theta) \implies \theta_{\text{total}} = \theta_1 + \theta_2$$

#### 20.5 Formalismo Cuadrivectorial

- Métrica de Minkowski $\eta_{\mu\nu}$ (Convención $+,-,-,-$):
  $$\eta_{\mu\nu} = \operatorname{diag}(1, -1, -1, -1)$$
- Cuadrivector Posición:
  $$X^\mu = (ct, x, y, z) = (ct, \vec{r})$$
- Cuadrivector Velocidad (Tiempo propio $\tau$ con $d\tau = dt/\gamma$):
  $$U^\mu = \frac{dX^\mu}{d\tau} = \gamma(c, \vec{v}), \quad U^\mu U_\mu = \eta_{\mu\nu} U^\mu U^\nu = c^2$$
- Cuadrivector Momento / Cuadrimomento:
  $$P^\mu = m_0 U^\mu = \left( \frac{E}{c}, \vec{p} \right), \quad P^\mu P_\mu = \frac{E^2}{c^2} - |\vec{p}|^2 = m_0^2 c^2$$
- Cuadrivector Fuerza de Minkowski:
  $$K^\mu = \frac{dP^\mu}{d\tau} = \gamma \left( \frac{\vec{F} \cdot \vec{v}}{c}, \vec{F} \right)$$
- Cuadrivector Onda de De Broglie:
  $$K^\mu = \left( \frac{\omega}{c}, \vec{k} \right), \quad P^\mu = \hbar K^\mu$$

### Nivel Universitario / Avanzado

#### 20.6 Elementos de Relatividad General

- Principio de Equivalencia y Desplazamiento al Rojo Gravitacional:
  $$\frac{\Delta f}{f_0} = \frac{\Delta\Phi_g}{c^2} \implies f(r) = f_\infty \sqrt{1 - \frac{2GM}{c^2 r}}$$
- Métrica General del Espacio-Tiempo Curvo:
  $$ds^2 = g_{\mu\nu} dx^\mu dx^\nu$$
- Símbolos de Christoffel (Conexión Levi-Civita):
  $$\Gamma^\mu_{\alpha\beta} = \frac{1}{2} g^{\mu\sigma} \left( \frac{\partial g_{\sigma\alpha}}{\partial x^\beta} + \frac{\partial g_{\sigma\beta}}{\partial x^\alpha} - \frac{\partial g_{\alpha\beta}}{\partial x^\sigma} \right)$$
- Ecuación de las Geodésicas:
  $$\frac{d^2 x^\mu}{d\lambda^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\lambda} \frac{dx^\beta}{d\lambda} = 0$$
- Tensor de Curvatura de Riemann:
  $$R^\rho_{\ \sigma\mu\nu} = \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda} \Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda} \Gamma^\lambda_{\mu\sigma}$$
- Tensor de Ricci y Escalar de Curvatura:
  $$R_{\mu\nu} = R^\lambda_{\ \mu\lambda\nu}, \quad R = g^{\mu\nu} R_{\mu\nu}$$
- Ecuaciones de Campo de Einstein:
  $$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}, \quad G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu}$$
- Métrica de Schwarzschild (Masa esférica estática en el vacío):
  $$ds^2 = -\left( 1 - \frac{r_s}{r} \right) c^2 dt^2 + \left( 1 - \frac{r_s}{r} \right)^{-1} dr^2 + r^2 (d\theta^2 + \sen^2\theta \, d\phi^2)$$
- Radio de Schwarzschild (Horizonte de sucesos):
  $$r_s = \frac{2GM}{c^2}$$

## 21. Mecánica Cuántica y Física Atómica

### Nivel Básico

#### 21.1 Fenomenología Cuántica Temprana

- Hipótesis de De Broglie (Dualidad onda-partícula):
  $$\lambda = \frac{h}{p} = \frac{h}{\gamma m v}, \quad p = \hbar k = \frac{h}{\lambda}$$
- Efecto Fotoeléctrico (Einstein):
  $$E_k^{\text{máx}} = e V_s = h f - \Phi_0 = \hbar \omega - \Phi_0, \quad f_0 = \frac{\Phi_0}{h}$$
- Dispersión Compton (Corrimiento en longitud de onda):
  $$\Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta) = \lambda_C (1 - \cos\theta)$$
  $$\lambda_C = \frac{h}{m_e c} \approx 2.4263 \times 10^{-12} \, \text{m} \quad (\text{Longitud de onda Compton})$$
- Principio de Incertidumbre de Heisenberg:
  $$\Delta x \cdot \Delta p_x \ge \frac{\hbar}{2}, \quad \Delta E \cdot \Delta t \ge \frac{\hbar}{2}$$

#### 21.2 Modelo Atómico de Bohr (Átomos Hidrogenoides de número atómico $Z$)

- Cuantización del Momento Angular Orbital:
  $$L = m_e v r = n \hbar = n \frac{h}{2\pi}, \quad n = 1, 2, 3, \dots$$
- Radios de Órbitas Permitidas ($a_0 = \text{Radio de Bohr}$):
  $$r_n = \frac{4\pi\varepsilon_0 \hbar^2}{m_e e^2} \frac{n^2}{Z} = a_0 \frac{n^2}{Z}, \quad a_0 = \frac{4\pi\varepsilon_0 \hbar^2}{m_e e^2} \approx 0.529 \, \text{Å}$$
- Niveles de Energía Cuantizados:
  $$E_n = -\frac{m_e Z^2 e^4}{32 \pi^2 \varepsilon_0^2 \hbar^2} \frac{1}{n^2} = -E_R \frac{Z^2}{n^2} = -13.6 \, \text{eV} \cdot \frac{Z^2}{n^2}$$
- Fórmula de Rydberg para Transiciones Espectrales:
  $$\frac{1}{\lambda} = R_\infty Z^2 \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right), \quad R_\infty = \frac{m_e e^4}{8 \varepsilon_0^2 h^3 c} \approx 1.09737 \times 10^7 \, \text{m}^{-1}$$

### Nivel Intermedio

#### 21.3 Ecuación de Schrödinger No Relativista

- Dependiente del Tiempo (1D y 3D):
  $$i\hbar \frac{\partial \Psi(\vec{r}, t)}{\partial t} = \hat{H}\Psi(\vec{r}, t) = \left[ -\frac{\hbar^2}{2m}\nabla^2 + V(\vec{r}, t) \right] \Psi(\vec{r}, t)$$
- Independiente del Tiempo (Estados Estacionarios $\Psi(\vec{r}, t) = \psi(\vec{r})e^{-iEt/\hbar}$):
  $$\hat{H}\psi(\vec{r}) = E\psi(\vec{r}) \implies -\frac{\hbar^2}{2m}\nabla^2\psi(\vec{r}) + V(\vec{r})\psi(\vec{r}) = E\psi(\vec{r})$$
- Densidad de Probabilidad ($P$) y Densidad de Corriente de Probabilidad ($\vec{J}$):
  $$P(\vec{r}, t) = |\Psi(\vec{r}, t)|^2 = \Psi^* \Psi, \quad \int_{\text{todo el espacio}} |\Psi|^2 dV = 1$$
  $$\vec{J} = \frac{\hbar}{2mi}(\Psi^* \nabla\Psi - \Psi \nabla\Psi^*) \implies \frac{\partial P}{\partial t} + \nabla \cdot \vec{J} = 0$$

#### 21.4 Problemas Unidimensionales Notables

- Pozo de Potencial Infinito (Caja 1D de longitud $L$ en $[0, L]$):
  $$\psi_n(x) = \sqrt{\frac{2}{L}}\sen\left( \frac{n\pi x}{L} \right), \quad E_n = \frac{n^2 \pi^2 \hbar^2}{2m L^2} = \frac{n^2 h^2}{8m L^2}, \quad n = 1, 2, 3, \dots$$
- Oscilador Armónico Cuántico Simple ($\omega = \sqrt{k/m}$):
  $$E_n = \hbar\omega \left( n + \frac{1}{2} \right), \quad n = 0, 1, 2, \dots$$
  $$\text{Operadores de Aniquilación/Creación (Escalera): } \hat{a} = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} + \frac{i\hat{p}}{m\omega}\right), \quad \hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} - \frac{i\hat{p}}{m\omega}\right)$$
  $$[\hat{a}, \hat{a}^\dagger] = 1, \quad \hat{H} = \hbar\omega\left(\hat{a}^\dagger \hat{a} + \frac{1}{2}\right) = \hbar\omega\left(\hat{N} + \frac{1}{2}\right)$$
- Efecto Túnel a través de Barrera Rectangular ($V_0 > E$, ancho $a$):
  $$T \approx \exp(-2\kappa a), \quad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar} \quad (\text{para } \kappa a \gg 1)$$

#### 21.5 Momento Angular Cuántico y Átomo de Hidrógeno

- Operadores de Momento Angular Orbital ($\hat{\vec{L}} = \hat{\vec{r}} \times \hat{\vec{p}}$):
  $$[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z, \quad [\hat{L}_y, \hat{L}_z] = i\hbar \hat{L}_x, \quad [\hat{L}_z, \hat{L}_x] = i\hbar \hat{L}_y, \quad [\hat{L}^2, \hat{L}_z] = 0$$
- Autovalores de Momento Angular y Proyección:
  $$\hat{L}^2 |l, m_l\rangle = \hbar^2 l(l + 1)|l, m_l\rangle, \quad l = 0, 1, 2, \dots$$
  $$\hat{L}_z |l, m_l\rangle = \hbar m_l |l, m_l\rangle, \quad m_l = -l, -l+1, \dots, l$$
- Función de Onda del Átomo de Hidrógeno:
  $$\psi_{n, l, m_l}(r, \theta, \phi) = R_{nl}(r) Y_l^{m_l}(\theta, \phi)$$
  $$(R_{nl} = \text{Polinomios asociados de Laguerre}, \, Y_l^{m_l} = \text{Armónicos esféricos})$$

### Nivel Universitario / Avanzado

#### 21.6 Formalismo de Dirac (Bra-Ket), Postulados y Espacio de Hilbert

- Valor Esperado de un Observable $\hat{A}$ en el Estado $|\psi\rangle$:
  $$\langle A \rangle = \frac{\langle\psi|\hat{A}|\psi\rangle}{\langle\psi|\psi\rangle}$$
- Relación Generalizada de Incertidumbre de Robertson-Schrödinger:
  $$\sigma_A \sigma_B \ge \frac{1}{2} |\langle [\hat{A}, \hat{B}] \rangle|$$
- Relación de Conmutación Canónica:
  $$[\hat{x}_j, \hat{p}_k] = i\hbar \delta_{jk}$$
- Ecuación de Movimiento de Heisenberg para un Operador $\hat{A}$:
  $$\frac{d\hat{A}_H}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{A}_H] + \left( \frac{\partial\hat{A}}{\partial t} \right)_H$$

#### 21.7 Espín $1/2$ y Matrices de Pauli ($\hat{\vec{S}} = \frac{\hbar}{2}\vec{\sigma}$)

- Matrices de Pauli:
  $$\sigma_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad \sigma_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}, \quad \sigma_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$
- Álgebra de Pauli:
  $$\sigma_i \sigma_j = \delta_{ij} I + i \sum_k \epsilon_{ijk} \sigma_k, \quad [\sigma_i, \sigma_j] = 2i \epsilon_{ijk} \sigma_k, \quad \{\sigma_i, \sigma_j\} = 2\delta_{ij} I$$
- Momento Magnético de Espín:
  $$\vec{\mu}_s = -g_s \frac{e}{2m_e}\vec{S} \approx -\frac{e}{m_e}\vec{S} = -\mu_B \vec{\sigma}, \quad \mu_B = \frac{e\hbar}{2m_e} \quad (\text{Magnetón de Bohr})$$

#### 21.8 Teoría de Perturbaciones y Métodos de Aproximación

- Perturbaciones Estacionarias No Degeneradas (1er y 2do orden):
  $$E_n^{(1)} = \langle n^{(0)} | \hat{H}' | n^{(0)} \rangle$$
  $$E_n^{(2)} = \sum_{k \neq n} \frac{|\langle k^{(0)} | \hat{H}' | n^{(0)} \rangle|^2}{E_n^{(0)} - E_k^{(0)}}$$
  $$|n^{(1)}\rangle = \sum_{k \neq n} \frac{\langle k^{(0)} | \hat{H}' | n^{(0)} \rangle}{E_n^{(0)} - E_k^{(0)}} |k^{(0)}\rangle$$
- Regla de Oro de Fermi (Tasa de transición dependiente del tiempo):
  $$\Gamma_{i \to f} = W_{i \to f} = \frac{2\pi}{\hbar} |\langle f | \hat{H}' | i \rangle|^2 \rho(E_f)$$

#### 21.9 Mecánica Cuántica Relativista

- Ecuación de Klein-Gordon (Partículas escalares de espín 0 con $\Box = \nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}$):
  $$\left( \Box - \frac{m^2 c^2}{\hbar^2} \right) \phi = 0 \iff \nabla^2\phi - \frac{1}{c^2}\frac{\partial^2\phi}{\partial t^2} = \left(\frac{mc}{\hbar}\right)^2 \phi$$
  $$\left( \text{O con firma } \Box = \frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2 = \partial_\mu \partial^\mu: \quad \left(\Box + \frac{m^2 c^2}{\hbar^2}\right)\phi = 0 \right)$$
- Ecuación de Dirac (Fermiones de espín 1/2 en representación covariante):
  $$(i\gamma^\mu \partial_\mu - \frac{mc}{\hbar})\psi = 0 \iff (i\hbar \gamma^\mu \partial_\mu - mc)\psi = 0$$
- Álgebra de Clifford para las Matrices Gamma de Dirac ($\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu} I_{4\times4}$):
  $$\gamma^0 = \begin{bmatrix} I & 0 \\ 0 & -I \end{bmatrix}, \quad \gamma^k = \begin{bmatrix} 0 & \sigma_k \\ -\sigma_k & 0 \end{bmatrix}, \quad \gamma^5 = i\gamma^0 \gamma^1 \gamma^2 \gamma^3 = \begin{bmatrix} 0 & I \\ I & 0 \end{bmatrix}$$

## 22. Física Nuclear, Radiactividad y Partículas Elementales

### Nivel Básico

#### 22.1 Estructura Nuclear y Defecto de Masa

- Radio Nuclear Empírico ($A = \text{número másico}$):
  $$R \approx R_0 A^{1/3}, \quad R_0 \approx 1.2 \, \text{fm} = 1.2 \times 10^{-15} \, \text{m}$$
- Defecto de Masa ($\Delta m$ para un núcleo $_Z^A X_N$ con $N = A - Z$):
  $$\Delta m = Z m_p + N m_n - M_{\text{núcleo}}(A, Z)$$
- Energía de Enlace Nuclear Total ($B$ o $E_b$):
  $$B(A, Z) = \Delta m \cdot c^2 = [Z m_p + (A - Z) m_n - M_{\text{núcleo}}] c^2$$
- Energía de Enlace por Nucleón ($B/A$):
  $$\frac{B}{A} = \frac{B(A, Z)}{A} \quad (\approx 8.8 \, \text{MeV/nucleón para el } ^{56}\text{Fe})$$

#### 22.2 Cinética de la Desintegración Radiactiva

- Ley de Desintegración Radiactiva:
  $$N(t) = N_0 e^{-\lambda t}$$
- Actividad Radiactiva ($A(t)$ en Becquerels $\text{Bq} = \text{des/s}$ o Curie $\text{Ci}$):
  $$A(t) = -\frac{dN}{dt} = \lambda N(t) = A_0 e^{-\lambda t}, \quad A_0 = \lambda N_0$$
- Periodo de Semidesintegración / Vida Media ($t_{1/2}$):
  $$t_{1/2} = \frac{\ln(2)}{\lambda} \approx \frac{0.693}{\lambda}$$
- Tiempo de Vida Medio ($\tau$):
  $$\tau = \frac{1}{\lambda} = \frac{t_{1/2}}{\ln(2)} \approx 1.443 \, t_{1/2}$$

#### 22.3 Tipos Principales de Desintegración Radiactiva

- Desintegración Alfa ($\alpha = \,_2^4\text{He}$):
  $$_Z^A X \longrightarrow \,_{Z-2}^{A-4} Y + \,_2^4\text{He} + Q_\alpha$$
- Desintegración Beta Negativa ($\beta^-$ con emisión de antineutrino electrónico):
  $$_Z^A X \longrightarrow \,_{Z+1}^A Y + e^- + \bar{\nu}_e + Q_{\beta^-} \quad (n \to p + e^- + \bar{\nu}_e)$$
- Desintegración Beta Positiva ($\beta^+$ con emisión de neutrino electrónico):
  $$_Z^A X \longrightarrow \,_{Z-1}^A Y + e^+ + \nu_e + Q_{\beta^+} \quad (p \to n + e^+ + \nu_e)$$
- Captura Electrónica ($\text{CE}$):
  $$_Z^A X + e^- \longrightarrow \,_{Z-1}^A Y + \nu_e + Q_{\text{CE}}$$
- Emisión Gamma ($\gamma = \text{fotón nuclear}$):
  $$_Z^A X^* \longrightarrow \,_Z^A X + \gamma$$

### Nivel Intermedio

#### 22.4 Balances Energéticos y Modelos Nucleares

- Valor $Q$ de una Reacción Nuclear ($a + X \to Y + b$):
  $$Q = (m_a + m_X - m_Y - m_b) c^2 = E_{k,Y} + E_{k,b} - E_{k,a}$$
  $$Q > 0 \quad (\text{Exoenergética / Exotérmica}), \quad Q < 0 \quad (\text{Endoenergética / Endotérmica})$$
- Energía Umbral para Reacciones Endoenergéticas ($Q < 0$ sobre blanco estacionario):
  $$E_{\text{umbral}} = |Q|\left( 1 + \frac{m_a}{m_X} \right)$$
- Fórmula Semiempírica de Masas de Bethe-Weizsäcker (Modelo de la Gota Líquida):
  $$B(A, Z) = a_v A - a_s A^{2/3} - a_c \frac{Z(Z - 1)}{A^{1/3}} - a_a \frac{(A - 2Z)^2}{A} + \delta(A, Z)$$
  $$\delta(A, Z) = \begin{cases} +a_p A^{-1/2} & \text{para } Z \text{ par, } N \text{ par} \\ 0 & \text{para } A \text{ impar (par-impar / impar-par)} \\ -a_p A^{-1/2} & \text{para } Z \text{ impar, } N \text{ impar} \end{cases} \quad (\text{o con término } \delta \propto \pm a_p A^{-3/4})$$
- Ley de Geiger-Nuttall para Desintegración Alfa ($E_\alpha = \text{energía de la partícula } \alpha$):
  $$\log_{10}(\lambda) = A_G + B_G \frac{Z}{\sqrt{E_\alpha}}$$

#### 22.5 Secciones Eficaces y Dosimetría

- Tasa de Reacción Nuclear (Flujo $\Phi$, densidad de núcleos blanco $n_t$, sección eficaz $\sigma$):
  $$R = \Phi \sigma N_t = I n_t x \sigma, \quad 1 \, \text{barn} (\text{b}) = 10^{-28} \, \text{m}^2 = 100 \, \text{fm}^2$$
- Dosis Absorbida ($D$ en Grays $\text{Gy} = \text{J/kg}$) y Dosis Equivalente ($H$ en Sieverts $\text{Sv}$ con factor de calidad $w_R$):
  $$D = \frac{dE_{\text{dep}}}{dm}, \quad H = w_R \cdot D$$

### Nivel Universitario / Avanzado

#### 22.6 Física de Partículas y Modelo Estándar

- Potencial Nuclear Fuerte de Yukawa (Mediado por mesones de masa $m_\pi$):
  $$V(r) = -g^2 \frac{e^{-\mu r}}{r} = -g^2 \frac{e^{-r / \lambda_C}}{r}, \quad \mu = \frac{m_\pi c}{\hbar}$$
- Fórmula de Gell-Mann-Nishijima (Carga, Isoespín, Hipercarga y Número Bariónico):
  $$Q = I_3 + \frac{Y}{2} = I_3 + \frac{B + S + C + B' + T}{2}$$
  $$(\text{donde } B = \text{bariónico}, \, S = \text{extrañeza}, \, C = \text{encanto}, \, B' = \text{bottomness/belleza}, \, T = \text{topness/verdad})$$
- Matriz CKM (Cabibbo-Kobayashi-Maskawa para mezcla de quarks):
  $$\begin{bmatrix} d' \\ s' \\ b' \end{bmatrix} = \mathbf{V}_{\text{CKM}} \begin{bmatrix} d \\ s \\ b \end{bmatrix} = \begin{bmatrix} V_{ud} & V_{us} & V_{ub} \\ V_{cd} & V_{cs} & V_{cb} \\ V_{td} & V_{ts} & V_{tb} \end{bmatrix} \begin{bmatrix} d \\ s \\ b \end{bmatrix}$$
- Relación de Dispersión de Breit-Wigner (Resonancia de desintegración con anchura $\Gamma$):
  $$\sigma(E) = \frac{\pi}{k^2} \frac{g \Gamma_{\text{in}} \Gamma_{\text{out}}}{(E - E_0)^2 + (\Gamma/2)^2}, \quad \tau = \frac{\hbar}{\Gamma}$$

## 23. Física del Estado Sólido y Materia Condensada

### Nivel Básico / Intermedio

#### 23.1 Cristalografía y Difracción

- Ley de Bragg para Difracción de Rayos X ($d_{hkl} = \text{espaciado interplanar}$):
  $$2 d_{hkl} \sen\theta = n \lambda, \quad n \in \mathbb{N}$$
- Espaciado Interplanar para Red Cúbica Simple (Parámetro de red $a$):
  $$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$
- Vectores Primitivos de la Red Recíproca:
  $$\vec{b}_1 = 2\pi \frac{\vec{a}_2 \times \vec{a}_3}{\vec{a}_1 \cdot (\vec{a}_2 \times \vec{a}_3)}, \quad \vec{b}_2 = 2\pi \frac{\vec{a}_3 \times \vec{a}_1}{\vec{a}_1 \cdot (\vec{a}_2 \times \vec{a}_3)}, \quad \vec{b}_3 = 2\pi \frac{\vec{a}_1 \times \vec{a}_2}{\vec{a}_1 \cdot (\vec{a}_2 \times \vec{a}_3)}$$
- Condición de Difracción de Laue ($\vec{G} = \vec{G}_{hkl} = \text{vector de red recíproca}$):
  $$\Delta\vec{k} = \vec{k}' - \vec{k} = \vec{G} \iff 2\vec{k} \cdot \vec{G} + |\vec{G}|^2 = 0 \quad (\text{para dispersión elástica } |\vec{k}'| = |\vec{k}|)$$
  $$\left( \text{O definiendo } \Delta\vec{k} = \vec{k} - \vec{k}' = \vec{G}: \quad 2\vec{k} \cdot \vec{G} = |\vec{G}|^2 \right)$$

#### 23.2 Gas de Electrones Libres de Fermi

- Vector de Onda de Fermi y Momento de Fermi:
  $$k_F = (3\pi^2 n)^{1/3}, \quad p_F = \hbar k_F = \hbar (3\pi^2 n)^{1/3}, \quad n = \frac{N}{V}$$
- Energía de Fermi a $T = 0\text{ K}$:
  $$E_F = \frac{\hbar^2 k_F^2}{2m} = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$$
- Temperatura de Fermi y Velocidad de Fermi:
  $$T_F = \frac{E_F}{k_B}, \quad v_F = \frac{\hbar k_F}{m} = \sqrt{\frac{2E_F}{m}}$$
- Densidad de Estados Tridimensional ($g(E)$ o $D(E)$):
  $$g(E) = \frac{V}{2\pi^2}\left( \frac{2m}{\hbar^2} \right)^{3/2} \sqrt{E} = \frac{3N}{2E_F^{3/2}}\sqrt{E}$$
- Capacidad Calorífica Electrónica Lineal ($T \ll T_F$):
  $$C_{v,e} = \gamma T = \frac{\pi^2}{2}\left( \frac{k_B T}{E_F} \right) N k_B = \frac{\pi^2}{3} g(E_F) k_B^2 T$$

#### 23.3 Transporte Electrónico y Térmico

- Conductividad Eléctrica de Drude-Sommerfeld:
  $$\sigma = \frac{n e^2 \tau_c}{m}$$
- Ley de Wiedemann-Franz (Número de Lorenz $L$):
  $$\frac{K}{\sigma} = L T, \quad L = \frac{\pi^2}{3}\left( \frac{k_B}{e} \right)^2 \approx 2.44 \times 10^{-8} \, \frac{\text{W}\cdot\Omega}{\text{K}^2}$$

### Nivel Universitario / Avanzado

#### 23.4 Teoría de Bandas y Semiconductores

- Teorema de Bloch para Electrones en un Potencial Periódico ($V(\vec{r} + \vec{R}) = V(\vec{r})$):
  $$\psi_{\vec{k}}(\vec{r}) = e^{i\vec{k} \cdot \vec{r}} u_{\vec{k}}(\vec{r}), \quad u_{\vec{k}}(\vec{r} + \vec{R}) = u_{\vec{k}}(\vec{r})$$
- Tensor de Masa Efectiva del Portador:
  $$\left( \frac{1}{m^*} \right)_{ij} = \frac{1}{\hbar^2} \frac{\partial^2 E(\vec{k})}{\partial k_i \partial k_j}$$
- Concentración Intrínseca de Portadores en Semiconductores ($E_g = \text{Banda prohibida / Bandgap}$):
  $$n_i = \sqrt{N_c N_v} \exp\left( -\frac{E_g}{2 k_B T} \right)$$
  $$N_c = 2\left( \frac{m_e^* k_B T}{2\pi\hbar^2} \right)^{3/2}, \quad N_v = 2\left( \frac{m_h^* k_B T}{2\pi\hbar^2} \right)^{3/2}$$
- Ley de Acción de Masas en Semiconductores:
  $$n \cdot p = n_i^2$$
- Nivel de Fermi Intrínseco:
  $$E_{Fi} = \frac{E_c + E_v}{2} + \frac{3}{4} k_B T \ln\left( \frac{m_h^*}{m_e^*} \right)$$

#### 23.5 Fonones y Propiedades Térmicas de la Red

- Modelo de Debye para la Capacidad Calorífica de la Red ($T \ll \Theta_D$):
  $$C_v = \frac{12\pi^4}{5} N k_B \left( \frac{T}{\Theta_D} \right)^3 \propto T^3, \quad \Theta_D = \frac{\hbar v_s}{k_B}(6\pi^2 n)^{1/3}$$
- Modelo de Einstein para la Capacidad Calorífica:
  $$C_v = 3 N k_B \left( \frac{\Theta_E}{T} \right)^2 \frac{e^{\Theta_E / T}}{(e^{\Theta_E / T} - 1)^2}, \quad \Theta_E = \frac{\hbar\omega_E}{k_B}$$

#### 23.6 Superconductividad (Teoría Clásica de London y BCS)

- Ecuaciones de London ($\lambda_L = \text{longitud de penetración de London}$):
  $$\frac{\partial \vec{J}_s}{\partial t} = \frac{n_s e^2}{m} \vec{E}, \quad \nabla \times \vec{J}_s = -\frac{n_s e^2}{m}\vec{B} \implies \nabla^2\vec{B} = \frac{1}{\lambda_L^2}\vec{B}$$
- Efecto Meissner (Atenuación exponencial del campo magnético en el superconductor):
  $$B(x) = B_0 \exp\left( -\frac{x}{\lambda_L} \right), \quad \lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}}$$
- Campo Magnético Crítico Termodinámico:
  $$B_c(T) = B_c(0)\left[ 1 - \left( \frac{T}{T_c} \right)^2 \right]$$
- Brecha de Energía Superconductora BCS a $T = 0\text{ K}$:
  $$\Delta(0) \approx 1.764 \, k_B T_c$$
- Longitud de Coherencia de Cooper / BCS ($\xi_0$):
  $$\xi_0 = \frac{\hbar v_F}{\pi \Delta(0)}$$
