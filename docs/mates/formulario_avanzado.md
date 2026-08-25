---
file: docs/mates/formulario_avanzado.md
description: Compendio didáctico de fórmulas matemáticas de nivel avanzado y universitario (ecuaciones diferenciales, cálculo vectorial, métodos numéricos).
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/symbols.py
relations:
  - docs/mates/formulario_mates.md
  - docs/fisica/formulario_avanzado.md
  - docs/ARCHITECTURE.md
keywords:
  - formulas-avanzadas-mates
  - ecuaciones-diferenciales
  - calculo-vectorial
  - metodos-numericos
---

# Compendio I: Aritmética, Álgebra y Trigonometría
*(Nivel Avanzado)*

## 1. Aritmética

### 1.1 Aritmética Modular

- Congruencia lineal:
  $$
  a \equiv b \pmod{m} \iff m \mid (a - b)
  $$
- Pequeño Teorema de Fermat ($p \mathrm{ es primo y } \operatorname{mcd}(a, p) = 1$):
  $$
  a^{p - 1} \equiv 1 \pmod{p}
  $$
- Teorema de Euler-Fermat ($\operatorname{mcd}(a, m) = 1$):
  $$
  a^{\varphi(m)} \equiv 1 \pmod{m}
  $$
- Función $\varphi$ de Euler:
  $$
  \varphi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)
  $$
### 1.2 Teorema Chino del Resto

- Solución única módulo $M = m_1 \cdot m_2 \cdots m_k$ para el sistema con $\operatorname{mcd}(m_i, m_j) = 1$ para $i \ne j$ (1):
  $$
  x \equiv a_i \pmod{m_i}
  $$
- Solución única módulo $M = m_1 \cdot m_2 \cdots m_k$ para el sistema con $\operatorname{mcd}(m_i, m_j) = 1$ para $i \ne j$ (2):
  $$
  M = \prod_{i=1}^k m_i
  $$
- Solución única módulo $M = m_1 \cdot m_2 \cdots m_k$ para el sistema con $\operatorname{mcd}(m_i, m_j) = 1$ para $i \ne j$ (3):
  $$
  M_i = \frac{M}{m_i}
  $$
- Solución única módulo $M = m_1 \cdot m_2 \cdots m_k$ para el sistema con $\operatorname{mcd}(m_i, m_j) = 1$ para $i \ne j$ (4):
  $$
  y_i \equiv M_i^{-1} \pmod{m_i}
  $$
- Solución única módulo $M = m_1 \cdot m_2 \cdots m_k$ para el sistema con $\operatorname{mcd}(m_i, m_j) = 1$ para $i \ne j$ (5):
  $$
  x \equiv \sum_{i=1}^k a_i M_i y_i \pmod{M}
  $$
## 2. Álgebra

### 2.1 Números Complejos

- Forma rectangular / binómica ($i^2 = -1$):
  $$
  z = a + bi
  $$
- Módulo:
  $$
  |z| = r = \sqrt{a^2 + b^2}
  $$
- argumento:
  $$
  \theta = \operatorname{atan2}(b, a) = \operatorname{arg}(z) \in (-\pi, \pi]
  $$
- Forma polar y exponencial (Euler):
  $$
  z = r(\cos(\theta) + i\sin(\theta)) = r e^{i\theta}
  $$
- Teorema de De Moivre:
  $$
  [r(\cos(\theta) + i\sin(\theta))]^n = r^n (\cos(n\theta) + i\sin(n\theta))
  $$
- Raíces $n$-ésimas de un complejo ($k = 0, 1, \dots, n-1$):
  $$
  z_k = \sqrt[n]{r} \, e^{i \frac{\theta + 2k\pi}{n}}
  $$
### 2.2 Álgebra Lineal y Matrices

- Determinante $2 \times 2$:
  $$
  \det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc
  $$
- Matriz Inversa ($2 \times 2$ con $\det(A) \ne 0$):
  $$
  A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
  $$
- Matriz Inversa general ($\operatorname{adj}(A) = [\operatorname{Cof}(A)]^T$):
  $$
  A^{-1} = \frac{1}{\det(A)} \operatorname{adj}(A) = \frac{1}{\det(A)} [\operatorname{Cof}(A)]^T \quad (\det(A) \ne 0)
  $$
- Ecuación Característica (Autovalores):
  $$
  \det(A - \lambda I) = 0
  $$
- Autovectores:
  $$
  (A - \lambda I)\vec{v} = \vec{0}
  $$
## 3. Trigonometría

### 3.1 Definición Compleja de Funciones Circulares (Fórmula de Euler)

- Identidad de Euler:
  $$
  e^{i\theta} = \cos(\theta) + i\sin(\theta)
  $$
- Seno complejo:
  $$
  \sin(z) = \frac{e^{iz} - e^{-iz}}{2i}
  $$
- Coseno complejo:
  $$
  \cos(z) = \frac{e^{iz} + e^{-iz}}{2}
  $$
- Tangente compleja:
  $$
  \tan(z) = \frac{e^{iz} - e^{-iz}}{i(e^{iz} + e^{-iz})}
  $$
### 3.2 Funciones Hiperbólicas

- Seno hiperbólico:
  $$
  \sinh(x) = \frac{e^x - e^{-x}}{2}
  $$
- Coseno hiperbólico:
  $$
  \cosh(x) = \frac{e^x + e^{-x}}{2}
  $$
- Tangente hiperbólica:
  $$
  \tanh(x) = \frac{\sinh(x)}{\cosh(x)} = \frac{e^x - e^{-x}}{e^x + e^{-x}}
  $$
- Identidad Fundamental Hiperbólica:
  $$
  \cosh^2(x) - \sinh^2(x) = 1
  $$
- Identidad derivada:
  $$
  1 - \tanh^2(x) = \operatorname{sech}^2(x)
  $$
### 3.3 Relación entre Funciones Circulares e Hiperbólicas

- Seno:
  $$
  \sin(iz) = i\sinh(z)
  $$
- Coseno:
  $$
  \cos(iz) = \cosh(z)
  $$
- Seno:
  $$
  \sinh(iz) = i\sin(z)
  $$
- Coseno:
  $$
  \cosh(iz) = \cos(z)
  $$
### 3.4 Desarrollo en Series de Potencias (Taylor / Maclaurin en $x = 0$)

- Seno:
  $$
  \sin(x) = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots
  $$
- Coseno:
  $$
  \cos(x) = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots
  $$
- Seno hiperbólico:
  $$
  \sinh(x) = \sum_{n=0}^\infty \frac{x^{2n+1}}{(2n+1)!} = x + \frac{x^3}{3!} + \frac{x^5}{5!} + \dots
  $$
- Coseno hiperbólico:
  $$
  \cosh(x) = \sum_{n=0}^\infty \frac{x^{2n}}{(2n)!} = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \dots
  $$
# Compendio II: Geometría, Geometría Analítica y Álgebra Lineal
*(Nivel Avanzado)*

## 4. Geometría (Plana y del Espacio / Euclidiana)

### 4.1 Geometría no Euclidiana y Topología Básica

- Característica de Euler-Poincaré (Poliedros convexos):
  $$
  V - E + F = 2 \quad (\mathrm{Vértices} - \mathrm{Aristas} + \mathrm{Caras})
  $$
- Triángulo Esférico (Exceso esférico $E$ en radianes con ángulos $\alpha, \beta, \gamma$):
  $$
  E = \alpha + \beta + \gamma - \pi \quad (\mathrm{con } E > 0 \mathrm{ en rad})
  $$
- Área del Triángulo Esférico (Esfera de radio $R$):
  $$
  \mathrm{Área} = R^2 E = R^2 (\alpha + \beta + \gamma - \pi)
  $$
- Curvatura Gaussiana ($K$):
  $$
  K = k_1 \cdot k_2
  $$
- Teorema de Gauss-Bonnet (Superficies compactas):
  $$
  \iint_M K \, dA + \oint_{\partial M} k_g \, ds = 2\pi \chi(M)
  $$
- Razón Doble (Cross-Ratio en Geometría Proyectiva):
  $$
  (A, B; C, D) = \frac{(c - a)(d - b)}{(c - b)(d - a)}
  $$
## 5. Geometría Analítica

### 5.1 Geometría Analítica del Espacio (3D)

- Distancia entre dos puntos en $\mathbb{R}^3$:
  $$
  d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}
  $$
- Ecuación del Plano (Normal $\vec{n} = (A, B, C)$, pasa por $P_0(x_0, y_0, z_0)$):
  $$
  A(x - x_0) + B(y - y_0) + C(z - z_0) = 0 \implies Ax + By + Cz + D = 0
  $$
- Distancia de un punto $P(x_0, y_0, z_0)$ a un plano $Ax + By + Cz + D = 0$:
  $$
  d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}
  $$
- Ecuaciones de la Recta en $\mathbb{R}^3$ ($\vec{v} = (v_1, v_2, v_3)$) (1):
  $$
  \mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{v} \quad (\mathrm{Vectorial})
  $$
- Ecuaciones de la Recta en $\mathbb{R}^3$ ($\vec{v} = (v_1, v_2, v_3)$) (2):
  $$
  x = x_0 + tv_1
  $$
- Ecuaciones de la Recta en $\mathbb{R}^3$ ($\vec{v} = (v_1, v_2, v_3)$) (3):
  $$
  y = y_0 + tv_2
  $$
- Ecuaciones de la Recta en $\mathbb{R}^3$ ($\vec{v} = (v_1, v_2, v_3)$) (4):
  $$
  z = z_0 + tv_3 \quad (\mathrm{Paramétrica})
  $$
- Ecuaciones de la Recta en $\mathbb{R}^3$ ($\vec{v} = (v_1, v_2, v_3)$) (5):
  $$
  \frac{x - x_0}{v_1} = \frac{y - y_0}{v_2} = \frac{z - z_0}{v_3} \quad (\mathrm{Continua / Simétrica})
  $$
- Distancia entre dos rectas alabeadas (cruzadas):
  $$
  d = \frac{|(\mathbf{r}_2 - \mathbf{r}_1) \cdot (\mathbf{v}_1 \times \mathbf{v}_2)|}{\|\mathbf{v}_1 \times \mathbf{v}_2\|}
  $$
### 5.2 Superficies Cuádricas en $\mathbb{R}^3$ (Centro en el origen)

- Elipsoide:
  $$
  \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1
  $$
- Hiperboloide de 1 hoja:
  $$
  \frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1
  $$
- Hiperboloide de 2 hojas:
  $$
  \frac{x^2}{a^2} - \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1
  $$
- Paraboloide Elíptico:
  $$
  z = \frac{x^2}{a^2} + \frac{y^2}{b^2}
  $$
- Paraboloide Hiperbólico (Silla de montar):
  $$
  z = \frac{y^2}{b^2} - \frac{x^2}{a^2}
  $$
- Cono Cuádrico:
  $$
  \frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{z^2}{c^2}
  $$
### 5.3 Transformaciones de Coordenadas en $\mathbb{R}^3$

- Coseno:
  $$
  x = r\cos(\theta)
  $$
- Seno:
  $$
  y = r\sin(\theta)
  $$
- Cilíndricas (3):
  $$
  z = z
  $$
- Esféricas ($\rho \ge 0:
  $$
  x = \rho\sin(\varphi)\cos(\theta)
  $$
- 0 \le \theta < 2\pi:
  $$
  y = \rho\sin(\varphi)\sin(\theta)
  $$
- 0 \le \varphi \le \pi$):
  $$
  z = \rho\cos(\varphi)
  $$
## 6. Álgebra Lineal

### 6.1 Autovalores, Autovectores y Diagonalización

- Polinomio Característico:
  $$
  p(\lambda) = \det(A - \lambda I) = 0
  $$
- Ecuación del Autovector:
  $$
  (A - \lambda I)\mathbf{v} = \mathbf{0} \iff A\mathbf{v} = \lambda\mathbf{v}
  $$
- Teorema de Cayley-Hamilton:
  $$
  p(A) = O
  $$
- Diagonalización:
  $$
  A = PDP^{-1}
  $$
- Teorema Espectral (Matrices Simétricas / Hermíticas) (1):
  $$
  A = Q\Lambda Q^T \quad (\mathrm{Real simétrica: } Q \mathrm{ ortogonal})
  $$
- Teorema Espectral (Matrices Simétricas / Hermíticas) (2):
  $$
  A = U\Lambda U^H \quad (\mathrm{Compleja hermítica: } U \mathrm{ unitaria})
  $$
- Forma Canónica de Jordan (1):
  $$
  A = PJP^{-1}
  $$
- Forma Canónica de Jordan (2):
  $$
  J = \operatorname{diag}(J_1, \dots, J_k)
  $$
### 6.2 Factorizaciones y Descomposiciones Matriciales

- Descomposiciones LU:
  $$
  A = LU
  $$
- QR:
  $$
  A = QR
  $$
- Cholesky ($A$ simétrica definida positiva):
  $$
  A = LL^T
  $$
- Descomposición en Valores Singulares (SVD) (1):
  $$
  A = U\Sigma V^T \quad (\mathrm{o } U\Sigma V^*)
  $$
- Descomposición en Valores Singulares (SVD) (2):
  $$
  \sigma_i = \sqrt{\lambda_i(A^T A)}
  $$
- Pseudoinversa de Moore-Penrose:
  $$
  A^+ = V\Sigma^+ U^H \quad (\mathrm{General vía SVD; } A^+ = (A^H A)^{-1} A^H \mathrm{ si } \operatorname{rango}(A) = n \mathrm{ [col. completo]})
  $$
- Solución por Mínimos Cuadrados ($\hat{\mathbf{x}} = A^+ \mathbf{b}$):
  $$
  \hat{\mathbf{x}} = (A^T A)^{-1} A^T \mathbf{b} \quad (\mathrm{Para } A \mathrm{ real de rango columna completo})
  $$
### 6.3 Operaciones Tensoriales

- Producto de Kronecker:
  $$
  (A \otimes B)_{p(r-1)+v, \, q(s-1)+w} = A_{rs} B_{vw}
  $$
- Propiedad de Producto Mixto:
  $$
  (A \otimes B)(C \otimes D) = (AC) \otimes (BD)
  $$
# Compendio III: Cálculo Diferencial, Integral y Vectorial
*(Nivel Avanzado)*

## 7. Cálculo Diferencial

### 7.1 Derivadas de Funciones Hiperbólicas e Inversas

- Seno:
  $$
  \frac{d}{dx}[\sinh(x)] = \cosh(x)
  $$
- Seno:
  $$
  \frac{d}{dx}[\cosh(x)] = \sinh(x)
  $$
- Tangente:
  $$
  \frac{d}{dx}[\tanh(x)] = \operatorname{sech}^2(x)
  $$
- Tangente:
  $$
  \frac{d}{dx}[\operatorname{sech}(x)] = -\operatorname{sech}(x)\tanh(x)
  $$
- Arcoseno hiperbólico:
  $$
  \frac{d}{dx}[\operatorname{arsinh}(x)] = \frac{1}{\sqrt{x^2 + 1}}
  $$
- Arcocoseno hiperbólico:
  $$
  \frac{d}{dx}[\operatorname{arcosh}(x)] = \frac{1}{\sqrt{x^2 - 1}} \quad (x > 1)
  $$
- Arcotangente hiperbólica:
  $$
  \frac{d}{dx}[\operatorname{artanh}(x)] = \frac{1}{1 - x^2} \quad (|x| < 1)
  $$
### 7.2 Diferencial Total y Series

- Diferencial:
  $$
  dy = f'(x) dx
  $$
- Serie de Taylor alrededor de $x = a$:
  $$
  f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (x - a)^n
  $$
- Resto de Lagrange ($\xi \in (a, x)$):
  $$
  R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} (x - a)^{n+1}
  $$
### 7.3 Geometría Diferencial de Curvas Planas

- Curvatura ($\kappa$):
  $$
  \kappa = \frac{|y''|}{[1 + (y')^2]^{\frac{3}{2}}}
  $$
- Radio de Curvatura ($R$):
  $$
  R = \frac{1}{\kappa} = \frac{[1 + (y')^2]^{\frac{3}{2}}}{|y''|}
  $$
## 8. Cálculo Integral

### 8.1 Integrales Impropias

- Límites infinitos:
  $$
  \int_a^\infty f(x) \, dx = \lim_{t \to \infty} \int_a^t f(x) \, dx
  $$
- Discontinuidad en $b$:
  $$
  \int_a^b f(x) \, dx = \lim_{t \to b^-} \int_a^t f(x) \, dx
  $$
### 8.2 Sustitución Universal de Weierstrass (Ángulo Mitad)

- Sustitución $t = \tan\left(\frac{x}{2}\right)$ (1):
  $$
  dx = \frac{2}{1 + t^2} dt
  $$
- Seno:
  $$
  \sin(x) = \frac{2t}{1 + t^2}
  $$
- Coseno:
  $$
  \cos(x) = \frac{1 - t^2}{1 + t^2}
  $$
### 8.3 Integrales Hiperbólicas Inmediatas

- Seno:
  $$
  \int \sinh(x) \, dx = \cosh(x) + C
  $$
- Coseno hiperbólico:
  $$
  \int \cosh(x) \, dx = \sinh(x) + C
  $$
- Arcoseno hiperbólico:
  $$
  \int \frac{1}{\sqrt{x^2 + a^2}} \, dx = \operatorname{arsinh}\left(\frac{x}{a}\right) + C = \ln\left(x + \sqrt{x^2 + a^2}\right) + C
  $$
- Arcocoseno hiperbólico:
  $$
  \int \frac{1}{\sqrt{x^2 - a^2}} \, dx = \operatorname{arcosh}\left(\frac{x}{a}\right) + C = \ln\left|x + \sqrt{x^2 - a^2}\right| + C \quad (x > a)
  $$
### 8.4 Funciones Especiales e Integrales Notables

- Función Gamma ($\Gamma(n + 1) = n!$):
  $$
  \Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt
  $$
- Función Beta:
  $$
  \mathrm{B}(x, y) = \int_0^1 t^{x-1} (1 - t)^{y-1} \, dt = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x + y)}
  $$
- Integral Gaussiana:
  $$
  \int_{-\infty}^\infty e^{-x^2} \, dx = \sqrt{\pi}
  $$
- Diferenciación bajo el signo de integral (Regla de Leibniz 2D):
  $$
  \frac{d}{dx} \left[ \int_{a(x)}^{b(x)} f(x, t) \, dt \right] = f(x, b(x))b'(x) - f(x, a(x))a'(x) + \int_{a(x)}^{b(x)} \frac{\partial f}{\partial x}(x, t) \, dt
  $$
## 9. Cálculo Vectorial y Multivariable

### 9.1 Operadores Diferenciales Vectoriales (en Coordenadas Cartesianas)

- Divergencia de un campo vectorial $\mathbf{F} = (P, Q, R)$:
  $$
  \operatorname{div}(\mathbf{F}) = \nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}
  $$
- Rotacional de un campo vectorial $\mathbf{F} = (P, Q, R)$:
  $$
  \operatorname{rot}(\mathbf{F}) = \nabla \times \mathbf{F} = \det\begin{pmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & R \end{pmatrix} = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}\right)\mathbf{i} + \left(\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}\right)\mathbf{j} + \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\mathbf{k}
  $$
- Operador Laplaciano Escalar:
  $$
  \Delta f = \nabla^2 f = \nabla \cdot (\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}
  $$
- Operador Laplaciano Vectorial:
  $$
  \nabla^2 \mathbf{F} = \nabla(\nabla \cdot \mathbf{F}) - \nabla \times (\nabla \times \mathbf{F})
  $$
- Identidades Diferenciales Fundamentales (1):
  $$
  \nabla \times (\nabla f) = \mathbf{0} \quad (\mathrm{Rotacional de gradiente nulo})
  $$
- Identidades Diferenciales Fundamentales (2):
  $$
  \nabla \cdot (\nabla \times \mathbf{F}) = 0 \quad (\mathrm{Divergencia de rotacional nula})
  $$
- Identidades Diferenciales Fundamentales (3):
  $$
  \nabla \cdot (f \mathbf{F}) = f(\nabla \cdot \mathbf{F}) + \mathbf{F} \cdot (\nabla f)
  $$
- Identidades Diferenciales Fundamentales (4):
  $$
  \nabla \times (f \mathbf{F}) = f(\nabla \times \mathbf{F}) + (\nabla f) \times \mathbf{F}
  $$
### 9.2 Integrales de Línea y Superficie

- Integral de Línea de Campo Escalar:
  $$
  \int_C f \, ds = \int_a^b f(\mathbf{r}(t)) \|\mathbf{r}'(t)\| \, dt
  $$
- Integral de Línea de Campo Vectorial (Trabajo / Circulación):
  $$
  W = \int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) \, dt = \int_C (P \, dx + Q \, dy + R \, dz)
  $$
- Teorema Fundamental para Integrales de Línea (Campos Conservativos $\mathbf{F} = \nabla\varphi$):
  $$
  \int_C \mathbf{F} \cdot d\mathbf{r} = \varphi(\mathbf{r}(b)) - \varphi(\mathbf{r}(a))
  $$
- Integral de Superficie de Campo Vectorial (Flujo):
  $$
  \Phi = \iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_D \mathbf{F}(\mathbf{r}(u, v)) \cdot (\mathbf{r}_u \times \mathbf{r}_v) \, du \, dv
  $$
### 9.3 Teoremas Integrales Fundamentales del Análisis Vectorial

- Teorema de Green en el Plano (Curva $C$ cerrada, frontera de $D$):
  $$
  \oint_C (P \, dx + Q \, dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA
  $$
- Teorema de Stokes:
  $$
  \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}
  $$
- Teorema de la Divergencia de Gauss (Superficie cerrada $\partial V$):
  $$
  \iint_{\partial V} \mathbf{F} \cdot d\mathbf{S} = \iiint_V (\nabla \cdot \mathbf{F}) \, dV
  $$
### 9.4 Geometría Diferencial en $\mathbb{R}^3$ (Triedro de Frenet-Serret)

- Vector Tangente Unitario:
  $$
  \mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}
  $$
- Vector Normal Principal:
  $$
  \mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|}
  $$
- Vector Binormal:
  $$
  \mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t)
  $$
- Fórmulas de Frenet-Serret (Parámetro de longitud de arco $s$) (1):
  $$
  \frac{d\mathbf{T}}{ds} = \kappa \mathbf{N}
  $$
- Fórmulas de Frenet-Serret (Parámetro de longitud de arco $s$) (2):
  $$
  \frac{d\mathbf{N}}{ds} = -\kappa \mathbf{T} + \tau \mathbf{B}
  $$
- Fórmulas de Frenet-Serret (Parámetro de longitud de arco $s$) (3):
  $$
  \frac{d\mathbf{B}}{ds} = -\tau \mathbf{N} \quad (\kappa = \mathrm{curvatura}, \, \tau = \mathrm{torsión})
  $$
# Compendio IV: Ecuaciones Diferenciales y Métodos Numéricos
*(Nivel Avanzado)*

## 10. Ecuaciones Diferenciales

### 10.1 Solución de EDOs por Series de Potencias

- En torno a un punto ordinario $x_0 = 0$:
  $$
  y(x) = \sum_{n=0}^\infty c_n x^n
  $$
- Método de Frobenius (Punto singular regular $x_0 = 0$) (1):
  $$
  y(x) = x^r \sum_{n=0}^\infty c_n x^n = \sum_{n=0}^\infty c_n x^{n + r} \quad (c_0 \ne 0)
  $$
- Método de Frobenius (Punto singular regular $x_0 = 0$) (2):
  $$
  \mathrm{Ecuación Indicial: } F(r) = r(r - 1) + p_0 r + q_0 = 0
  $$
- Ecuación Diferencial de Bessel:
  $$
  x^2 y'' + x y' + (x^2 - \nu^2)y = 0 \implies y(x) = c_1 J_\nu(x) + c_2 Y_\nu(x)
  $$
- Ecuación Diferencial de Legendre:
  $$
  (1 - x^2)y'' - 2x y' + n(n + 1)y = 0 \implies y(x) = c_1 P_n(x) + c_2 Q_n(x)
  $$
### 10.2 Sistemas de Ecuaciones Diferenciales Lineales

- Forma Matricial:
  $$
  \mathbf{x}'(t) = A\mathbf{x}(t) + \mathbf{g}(t)
  $$
- Matriz Exponencial:
  $$
  e^{At} = I + At + \frac{A^2 t^2}{2!} + \dots = \sum_{k=0}^\infty \frac{A^k t^k}{k!}
  $$
- Solución del Sistema Homogéneo:
  $$
  \mathbf{x}(t) = e^{At}\mathbf{x}(0) = \Phi(t)\mathbf{c}
  $$
- Fórmula de Variación de Parámetros Matricial:
  $$
  \mathbf{x}(t) = e^{A(t - t_0)}\mathbf{x}(t_0) + \int_{t_0}^t e^{A(t - \tau)}\mathbf{g}(\tau) \, d\tau
  $$
### 10.3 Ecuaciones Diferenciales Parciales (EDP) Clásicas

- Ecuación de Onda (Hiperbólica):
  $$
  \frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u
  $$
- Fórmula de d'Alembert (1D en recta infinita):
  $$
  u(x, t) = \frac{f(x - ct) + f(x + ct)}{2} + \frac{1}{2c}\int_{x - ct}^{x + ct} g(s) \, ds
  $$
- Ecuación del Calor / Difusión (Parabólica):
  $$
  \frac{\partial u}{\partial t} = \alpha \nabla^2 u
  $$
- Solución Fundamental / Núcleo del Calor (1D):
  $$
  \Phi(x, t) = \frac{1}{\sqrt{4\pi \alpha t}} e^{-\frac{x^2}{4\alpha t}}
  $$
- Ecuaciones de Laplace:
  $$
  \nabla^2 u = 0 \quad (\mathrm{Laplace})
  $$
- Poisson (Elípticas):
  $$
  \nabla^2 u = f(x, y, z) \quad (\mathrm{Poisson})
  $$
- Método de Separación de Variables (1D):
  $$
  u(x, t) = X(x)T(t) \implies \frac{X''}{X} = \frac{T'}{\alpha T} = -\lambda
  $$
### 10.4 Problemas de Sturm-Liouville

- Forma Autoadjunta ($x \in [a, b]$):
  $$
  \frac{d}{dx}\left[ p(x)\frac{dy}{dx} \right] + q(x)y + \lambda w(x)y = 0
  $$
- Relación de Ortogonalidad de Autofunciones ($\lambda_n \ne \lambda_m$):
  $$
  \int_a^b \phi_n(x)\phi_m(x)w(x) \, dx = 0
  $$
## 11. Métodos Numéricos

### 11.1 Solución Numérica de EDOs (Problemas de Valor Inicial)

- Método de Euler (Explícito):
  $$
  y_{n+1} = y_n + h f(t_n, y_n) \quad (\mathrm{Error local } O(h^2), \mathrm{ global } O(h))
  $$
- Método de Euler Mejorado / Heun (Predictor-Corrector) (1):
  $$
  y_{n+1}^* = y_n + h f(t_n, y_n)
  $$
- Método de Euler Mejorado / Heun (Predictor-Corrector) (2):
  $$
  y_{n+1} = y_n + \frac{h}{2}[f(t_n, y_n) + f(t_{n+1}, y_{n+1}^*)]
  $$
- Método de Runge-Kutta Clásico de 4° Orden (RK4) (1):
  $$
  k_1 = f(t_n, y_n)
  $$
- Método de Runge-Kutta Clásico de 4° Orden (RK4) (2):
  $$
  k_2 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)
  $$
- Método de Runge-Kutta Clásico de 4° Orden (RK4) (3):
  $$
  k_3 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right)
  $$
- Método de Runge-Kutta Clásico de 4° Orden (RK4) (4):
  $$
  k_4 = f(t_n + h, y_n + hk_3)
  $$
- Método de Runge-Kutta Clásico de 4° Orden (RK4) (5):
  $$
  y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4) \quad (\mathrm{Error local } O(h^5), \mathrm{ global } O(h^4))
  $$
- Métodos Multipaso (Adams-Bashforth / Adams-Moulton) (1):
  $$
  \mathrm{Adams-Bashforth (4 pasos): } y_{n+1} = y_n + \frac{h}{24}[55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3}]
  $$
- Métodos Multipaso (Adams-Bashforth / Adams-Moulton) (2):
  $$
  \mathrm{Adams-Moulton (3 pasos): } y_{n+1} = y_n + \frac{h}{24}[9f_{n+1} + 19f_n - 5f_{n-1} + f_{n-2}]
  $$
### 11.2 Solución Numérica de Problemas de Valor en la Frontera (PVF)

- Método de Disparo Lineal (Shooting Method):
  $$
  y(x) = u(x) + \frac{\beta - u(b)}{v(b)} v(x)
  $$
- Método de Diferencias Finitas para PVF:
  $$
  \frac{y_{i+1} - 2y_i + y_{i-1}}{h^2} = p(x_i)\frac{y_{i+1} - y_{i-1}}{2h} + q(x_i)y_i + r(x_i) \implies A\mathbf{y} = \mathbf{d}
  $$
### 11.3 Solución Numérica de Ecuaciones Diferenciales Parciales (EDP)

- Diferencias Finitas para EDPs Elípticas (Laplace/Poisson 2D con $\Delta x = \Delta y = h$):
  $$
  u_{i+1, j} + u_{i-1, j} + u_{i, j+1} + u_{i, j-1} - 4u_{i, j} = h^2 f_{i, j}
  $$
- Diferencias Finitas para EDPs Parabólicas (Calor 1D $u_t = \alpha u_{xx}$) (1):
  $$
  \mathrm{Esquema Explícito (FTCS): } u_i^{n+1} = u_i^n + r(u_{i+1}^n - 2u_i^n + u_{i-1}^n)
  $$
- Diferencias Finitas para EDPs Parabólicas (Calor 1D $u_t = \alpha u_{xx}$) (2):
  $$
  r = \frac{\alpha \Delta t}{(\Delta x)^2} \le \frac{1}{2}
  $$
- Diferencias Finitas para EDPs Parabólicas (Calor 1D $u_t = \alpha u_{xx}$) (3):
  $$
  \mathrm{Método de Crank-Nicolson: } -r u_{i-1}^{n+1} + 2(1 + r)u_i^{n+1} - r u_{i+1}^{n+1} = r u_{i-1}^n + 2(1 - r)u_i^n + r u_{i+1}^n
  $$
- Diferencias Finitas para EDPs Hiperbólicas (Onda 1D $u_{tt} = c^2 u_{xx}$) (1):
  $$
  u_i^{n+1} = 2(1 - C^2)u_i^n + C^2(u_{i+1}^n + u_{i-1}^n) - u_i^{n-1}
  $$
- Diferencias Finitas para EDPs Hiperbólicas (Onda 1D $u_{tt} = c^2 u_{xx}$) (2):
  $$
  \mathrm{Condición CFL: } C = \frac{c \Delta t}{\Delta x} \le 1
  $$
