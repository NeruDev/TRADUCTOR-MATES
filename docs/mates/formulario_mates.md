---
file: docs/mates/formulario_mates.md
description: Compendio exhaustivo de fórmulas matemáticas desde nivel básico hasta universitario.
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/symbols.py
relations:
  - docs/fisica/formulario_fisica.md
  - docs/ARCHITECTURE.md
keywords:
  - compendio-matematicas
  - formulas-matematicas
  - algebra
  - calculo
  - trigonometria
  - geometria
---

# Compendio I: Aritmética, Álgebra y Trigonometría
*(Nivel Básico a Universitario)*

## 1. Aritmética

### Nivel Básico

#### 1.1 Propiedades de la Adición y Multiplicación

- Clausura / Cerradura:
  $$\forall a, b \in \mathbb{R}: \quad a + b \in \mathbb{R}, \quad a \cdot b \in \mathbb{R}$$
- Conmutativa:
  $$a + b = b + a, \quad a \cdot b = b \cdot a$$
- Asociativa:
  $$(a + b) + c = a + (b + c), \quad (a \cdot b) \cdot c = a \cdot (b \cdot c)$$
- Elemento Neutro:
  $$a + 0 = a, \quad a \cdot 1 = a$$
- Elemento Inverso:
  $$a + (-a) = 0, \quad a \cdot \left(\frac{1}{a}\right) = 1 \quad (a \ne 0)$$
- Distributiva:
  $$a \cdot (b + c) = a \cdot b + a \cdot c$$

#### 1.2 Operaciones con Fracciones

- Suma/Resta con mismo denominador:
  $$\frac{a}{c} \pm \frac{b}{c} = \frac{a \pm b}{c} \quad (c \ne 0)$$
- Suma/Resta con distinto denominador:
  $$\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd} \quad (b, d \ne 0)$$
- Multiplicación:
  $$\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d} \quad (b, d \ne 0)$$
- División:
  $$\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a \cdot d}{b \cdot c} \quad (b, c, d \ne 0)$$

#### 1.3 Porcentajes y Proporcionalidad

- Tanto por ciento ($P = \text{porcentaje}$, $C = \text{cantidad}$, $r = \text{tasa}$):
  $$P = \frac{C \cdot r}{100}$$
- Regla de tres simple directa ($\frac{a}{b} = \frac{c}{x}$):
  $$x = \frac{b \cdot c}{a}$$

### Nivel Intermedio

#### 1.4 Teoría de Números Básica

- Algoritmo de la división (Euclides):
  $$D = d \cdot q + r, \quad 0 \le r < d$$
- Relación MCD y MCM:
  $$\operatorname{mcd}(a, b) \cdot \operatorname{mcm}(a, b) = |a \cdot b|$$

#### 1.5 Progresiones Aritméticas (PA)

- Término general:
  $$a_n = a_1 + (n - 1)d$$
- Suma de los primeros $n$ términos:
  $$S_n = \frac{n}{2} (a_1 + a_n)$$

#### 1.6 Progresiones Geométricas (PG)

- Término general:
  $$a_n = a_1 \cdot r^{n - 1}$$
- Suma de $n$ términos ($r \ne 1$):
  $$S_n = \frac{a_1 (1 - r^n)}{1 - r}$$
- Suma infinita ($|r| < 1$):
  $$S_\infty = \frac{a_1}{1 - r}$$

### Nivel Universitario / Avanzado

#### 1.7 Aritmética Modular

- Congruencia lineal:
  $$a \equiv b \pmod{m} \iff m \mid (a - b)$$
- Pequeño Teorema de Fermat ($p \text{ es primo y } \operatorname{mcd}(a, p) = 1$):
  $$a^{p - 1} \equiv 1 \pmod{p}$$
- Teorema de Euler-Fermat ($\operatorname{mcd}(a, m) = 1$):
  $$a^{\varphi(m)} \equiv 1 \pmod{m}$$
- Función $\varphi$ de Euler:
  $$\varphi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)$$

#### 1.8 Teorema Chino del Resto

- Solución única módulo $M = m_1 \cdot m_2 \cdots m_k$ para el sistema con $\operatorname{mcd}(m_i, m_j) = 1$ para $i \ne j$:
  $$x \equiv a_i \pmod{m_i}, \quad M = \prod_{i=1}^k m_i, \quad M_i = \frac{M}{m_i}, \quad y_i \equiv M_i^{-1} \pmod{m_i}$$
  $$x \equiv \sum_{i=1}^k a_i M_i y_i \pmod{M}$$

## 2. Álgebra

### Nivel Básico

#### 2.1 Leyes de Exponentes y Radicales

- Multiplicación de bases iguales:
  $$x^a \cdot x^b = x^{a + b}$$
- División de bases iguales:
  $$\frac{x^a}{x^b} = x^{a - b}$$
- Potencia de una potencia:
  $$(x^a)^b = x^{a \cdot b}$$
- Potencia de un producto:
  $$(x \cdot y)^a = x^a \cdot y^a$$
- Exponente negativo ($x \ne 0$):
  $$x^{-a} = \frac{1}{x^a}$$
- Exponente fraccionario:
  $$x^{\frac{a}{b}} = \sqrt[b]{x^a}$$
- Raíz de un producto:
  $$\sqrt[n]{x \cdot y} = \sqrt[n]{x} \cdot \sqrt[n]{y}$$

#### 2.2 Productos Notables y Factorización

- Binomio al cuadrado:
  $$(a \pm b)^2 = a^2 \pm 2ab + b^2$$
- Diferencia de cuadrados:
  $$a^2 - b^2 = (a + b)(a - b)$$
- Binomio al cubo:
  $$(a \pm b)^3 = a^3 \pm 3a^2b + 3ab^2 \pm b^3$$
- Suma de cubos:
  $$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$
- Diferencia de cubos:
  $$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$
- Trinomio al cuadrado:
  $$(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + ac + bc)$$

#### 2.3 Ecuaciones Lineales

- Forma general ($a \ne 0$):
  $$ax + b = 0 \implies x = -\frac{b}{a}$$

### Nivel Intermedio

#### 2.4 Ecuaciones Cuadráticas

- Forma general:
  $$ax^2 + bx + c = 0$$
- Fórmula cuadrática:
  $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
- Discriminante ($\Delta$):
  $$\Delta = b^2 - 4ac$$
- Relaciones de Cardano-Vieta ($2^\circ \text{ grado}$):
  $$x_1 + x_2 = -\frac{b}{a}, \quad x_1 \cdot x_2 = \frac{c}{a}$$

#### 2.5 Logaritmos

- Definición ($b > 0, b \ne 1, x > 0$):
  $$\log_b(x) = y \iff b^y = x$$
- Logaritmo de un producto:
  $$\log_b(x \cdot y) = \log_b(x) + \log_b(y)$$
- Logaritmo de un cociente:
  $$\log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)$$
- Logaritmo de una potencia:
  $$\log_b(x^k) = k \cdot \log_b(x)$$
- Cambio de base:
  $$\log_b(x) = \frac{\log_c(x)}{\log_c(b)}$$

#### 2.6 Teorema del Binomio (Newton)

- Expansión binomial:
  $$(a + b)^n = \sum_{k=0}^n \binom{n}{k} a^{n - k} b^k = \sum_{k=0}^n \frac{n!}{k!(n - k)!} a^{n - k} b^k$$

### Nivel Universitario / Avanzado

#### 2.7 Números Complejos

- Forma rectangular / binómica ($i^2 = -1$):
  $$z = a + bi$$
- Módulo y argumento:
  $$|z| = r = \sqrt{a^2 + b^2}, \quad \theta = \operatorname{atan2}(b, a) = \operatorname{arg}(z) \in (-\pi, \pi]$$
- Forma polar y exponencial (Euler):
  $$z = r(\cos(\theta) + i\sin(\theta)) = r e^{i\theta}$$
- Teorema de De Moivre:
  $$[r(\cos(\theta) + i\sin(\theta))]^n = r^n (\cos(n\theta) + i\sin(n\theta))$$
- Raíces $n$-ésimas de un complejo ($k = 0, 1, \dots, n-1$):
  $$z_k = \sqrt[n]{r} \, e^{i \frac{\theta + 2k\pi}{n}}$$

#### 2.8 Álgebra Lineal y Matrices

- Determinante $2 \times 2$:
  $$\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$
- Matriz Inversa ($2 \times 2$ con $\det(A) \ne 0$):
  $$A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$
- Matriz Inversa general ($\operatorname{adj}(A) = [\operatorname{Cof}(A)]^T$):
  $$A^{-1} = \frac{1}{\det(A)} \operatorname{adj}(A) = \frac{1}{\det(A)} [\operatorname{Cof}(A)]^T \quad (\det(A) \ne 0)$$
- Ecuación Característica (Autovalores):
  $$\det(A - \lambda I) = 0$$
- Autovectores:
  $$(A - \lambda I)\vec{v} = \vec{0}$$

## 3. Trigonometría

### Nivel Básico

#### 3.1 Razones Trigonométricas en el Triángulo Rectángulo

- Seno, Coseno y Tangente:
  $$\sin(\theta) = \frac{\text{Cateto Opuesto}}{\text{Hipotenusa}}, \quad \cos(\theta) = \frac{\text{Cateto Adyacente}}{\text{Hipotenusa}}, \quad \tan(\theta) = \frac{\text{Cateto Opuesto}}{\text{Cateto Adyacente}}$$
- Cosecante, Secante y Cotangente:
  $$\csc(\theta) = \frac{\text{Hipotenusa}}{\text{Cateto Opuesto}} = \frac{1}{\sin(\theta)}$$
  $$\sec(\theta) = \frac{\text{Hipotenusa}}{\text{Cateto Adyacente}} = \frac{1}{\cos(\theta)}$$
  $$\cot(\theta) = \frac{\text{Cateto Adyacente}}{\text{Cateto Opuesto}} = \frac{1}{\tan(\theta)}$$

#### 3.2 Identidades Trigonométricas Fundamentales

- Por cociente:
  $$\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}, \quad \cot(\theta) = \frac{\cos(\theta)}{\sin(\theta)}$$
- Identidad Pitagórica principal:
  $$\sin^2(\theta) + \cos^2(\theta) = 1$$
- Identidades Pitagóricas derivadas:
  $$1 + \tan^2(\theta) = \sec^2(\theta), \quad 1 + \cot^2(\theta) = \csc^2(\theta)$$

### Nivel Intermedio

#### 3.3 Fórmulas de Suma y Diferencia de Ángulos

- Seno de suma y diferencia:
  $$\sin(\alpha \pm \beta) = \sin(\alpha)\cos(\beta) \pm \cos(\alpha)\sin(\beta)$$
- Coseno de suma y diferencia:
  $$\cos(\alpha \pm \beta) = \cos(\alpha)\cos(\beta) \mp \sin(\alpha)\sin(\beta)$$
- Tangente de suma y diferencia:
  $$\tan(\alpha \pm \beta) = \frac{\tan(\alpha) \pm \tan(\beta)}{1 \mp \tan(\alpha)\tan(\beta)}$$

#### 3.4 Ángulo Doble y Ángulo Mitad

- Seno del ángulo doble:
  $$\sin(2\theta) = 2\sin(\theta)\cos(\theta)$$
- Coseno del ángulo doble:
  $$\cos(2\theta) = \cos^2(\theta) - \sin^2(\theta) = 2\cos^2(\theta) - 1 = 1 - 2\sin^2(\theta)$$
- Tangente del ángulo doble:
  $$\tan(2\theta) = \frac{2\tan(\theta)}{1 - \tan^2(\theta)}$$
- Seno y Coseno del ángulo mitad:
  $$\sin\left(\frac{\theta}{2}\right) = \pm \sqrt{\frac{1 - \cos(\theta)}{2}}, \quad \cos\left(\frac{\theta}{2}\right) = \pm \sqrt{\frac{1 + \cos(\theta)}{2}}$$
- Tangente del ángulo mitad:
  $$\tan\left(\frac{\theta}{2}\right) = \frac{\sin(\theta)}{1 + \cos(\theta)} = \frac{1 - \cos(\theta)}{\sin(\theta)}$$

#### 3.5 Leyes de Triángulos Oblicuángulos

- Ley de Senos ($R = \text{circunradio}$):
  $$\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)} = 2R$$
- Ley de Cosenos:
  $$a^2 = b^2 + c^2 - 2bc \cos(A)$$
- Área de un triángulo:
  $$\text{Área} = \frac{1}{2} a b \sin(C)$$
- Fórmula de Herón ($s = \frac{a + b + c}{2}$):
  $$\text{Área} = \sqrt{s(s - a)(s - b)(s - c)}$$

#### 3.6 Transformaciones de Suma a Producto (Fórmulas de Prostaféresis)

- Suma y resta de senos:
  $$\sin(\alpha) \pm \sin(\beta) = 2 \sin\left(\frac{\alpha \pm \beta}{2}\right) \cos\left(\frac{\alpha \mp \beta}{2}\right)$$
- Suma de cosenos:
  $$\cos(\alpha) + \cos(\beta) = 2 \cos\left(\frac{\alpha + \beta}{2}\right) \cos\left(\frac{\alpha - \beta}{2}\right)$$
- Resta de cosenos:
  $$\cos(\alpha) - \cos(\beta) = -2 \sin\left(\frac{\alpha + \beta}{2}\right) \sin\left(\frac{\alpha - \beta}{2}\right)$$

#### 3.7 Transformaciones de Producto a Suma

- Producto seno-coseno:
  $$2\sin(\alpha)\cos(\beta) = \sin(\alpha + \beta) + \sin(\alpha - \beta)$$
- Producto coseno-coseno:
  $$2\cos(\alpha)\cos(\beta) = \cos(\alpha + \beta) + \cos(\alpha - \beta)$$
- Producto seno-seno:
  $$2\sin(\alpha)\sin(\beta) = \cos(\alpha - \beta) - \cos(\alpha + \beta)$$

### Nivel Universitario / Avanzado

#### 3.8 Definición Compleja de Funciones Circulares (Fórmula de Euler)

- Identidad de Euler:
  $$e^{i\theta} = \cos(\theta) + i\sin(\theta)$$
- Seno complejo:
  $$\sin(z) = \frac{e^{iz} - e^{-iz}}{2i}$$
- Coseno complejo:
  $$\cos(z) = \frac{e^{iz} + e^{-iz}}{2}$$
- Tangente compleja:
  $$\tan(z) = \frac{e^{iz} - e^{-iz}}{i(e^{iz} + e^{-iz})}$$

#### 3.9 Funciones Hiperbólicas

- Seno hiperbólico:
  $$\sinh(x) = \frac{e^x - e^{-x}}{2}$$
- Coseno hiperbólico:
  $$\cosh(x) = \frac{e^x + e^{-x}}{2}$$
- Tangente hiperbólica:
  $$\tanh(x) = \frac{\sinh(x)}{\cosh(x)} = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$
- Identidad Fundamental Hiperbólica:
  $$\cosh^2(x) - \sinh^2(x) = 1$$
- Identidad derivada:
  $$1 - \tanh^2(x) = \operatorname{sech}^2(x)$$

#### 3.10 Relación entre Funciones Circulares e Hiperbólicas

- Circular a hiperbólica:
  $$\sin(iz) = i\sinh(z), \quad \cos(iz) = \cosh(z)$$
- Hiperbólica a circular:
  $$\sinh(iz) = i\sin(z), \quad \cosh(iz) = \cos(z)$$

#### 3.11 Desarrollo en Series de Potencias (Taylor / Maclaurin en $x = 0$)

- Seno:
  $$\sin(x) = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$$
- Coseno:
  $$\cos(x) = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$$
- Seno hiperbólico:
  $$\sinh(x) = \sum_{n=0}^\infty \frac{x^{2n+1}}{(2n+1)!} = x + \frac{x^3}{3!} + \frac{x^5}{5!} + \dots$$
- Coseno hiperbólico:
  $$\cosh(x) = \sum_{n=0}^\infty \frac{x^{2n}}{(2n)!} = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \dots$$

# Compendio II: Geometría, Geometría Analítica y Álgebra Lineal
*(Nivel Básico a Universitario)*

## 4. Geometría (Plana y del Espacio / Euclidiana)

### Nivel Básico

#### 4.1 Perímetros y Áreas de Figuras Planas (2D)

- Triángulo (General):
  $$P = a + b + c, \quad A = \frac{b \cdot h}{2}$$
- Triángulo Equilátero:
  $$A = \frac{\sqrt{3}}{4} l^2, \quad h = \frac{\sqrt{3}}{2} l$$
- Cuadrado:
  $$P = 4l, \quad A = l^2 = \frac{d^2}{2}$$
- Rectángulo:
  $$P = 2(b + h), \quad A = b \cdot h$$
- Paralelogramo:
  $$A = b \cdot h$$
- Rombo:
  $$P = 4l, \quad A = \frac{D \cdot d}{2}$$
- Trapecio:
  $$A = \frac{(B + b) \cdot h}{2}$$
- Polígono Regular ($n$ lados):
  $$P = n \cdot l, \quad A = \frac{P \cdot a_p}{2}$$
- Círculo:
  $$C = 2\pi r, \quad A = \pi r^2$$
- Sector Circular:
  $$s = r\theta, \quad A = \frac{1}{2} r^2 \theta \quad (\theta \text{ en rad})$$
- Corona Circular:
  $$A = \pi(R^2 - r^2)$$

#### 4.2 Propiedades Angulares y Polígonos

- Teorema de Pitágoras (Triángulos rectángulos):
  $$a^2 + b^2 = c^2$$
- Suma de ángulos internos de un triángulo:
  $$\alpha + \beta + \gamma = 180^\circ \quad (\text{o } \pi\text{ rad})$$
- Suma de ángulos internos de un polígono de $n$ lados:
  $$S_{\text{int}} = (n - 2) \cdot 180^\circ$$
- Ángulo interior de un polígono regular:
  $$\theta_{\text{int}} = \frac{(n - 2) \cdot 180^\circ}{n}$$
- Número total de diagonales en un polígono:
  $$N_d = \frac{n(n - 3)}{2}$$

### Nivel Intermedio

#### 4.3 Geometría del Espacio (Áreas y Volúmenes 3D)

- Prisma Recto:
  $$A_L = P_{\text{base}} \cdot h, \quad V = A_{\text{base}} \cdot h$$
- Cilindro Circular Recto:
  $$A_T = 2\pi r(h + r), \quad V = \pi r^2 h$$
- Pirámide:
  $$V = \frac{1}{3} A_{\text{base}} \cdot h$$
- Cono Circular Recto:
  $$g = \sqrt{r^2 + h^2}, \quad A_T = \pi r(g + r), \quad V = \frac{1}{3} \pi r^2 h$$
- Tronco de Cono:
  $$V = \frac{1}{3} \pi h (R^2 + r^2 + R \cdot r)$$
- Esfera:
  $$A = 4\pi r^2, \quad V = \frac{4}{3} \pi r^3$$
- Casquete Esférico:
  $$A = 2\pi r h, \quad V = \frac{1}{3} \pi h^2 (3r - h)$$

#### 4.4 Teoremas Métricos y Proporcionalidad

- Teorema de Tales (Rectas paralelas $L_1 \parallel L_2 \parallel L_3$ cortadas por transversales en $A, B, C$ y $D, E, F$):
  $$\frac{AB}{BC} = \frac{DE}{EF} \iff \frac{AB}{AC} = \frac{DE}{DF}$$
- Teorema de la Bisectriz Interior:
  $$\frac{a}{b} = \frac{c_1}{c_2}$$
- Relaciones Métricas en el Triángulo Rectángulo:
  $$h^2 = m \cdot n, \quad a^2 = c \cdot m, \quad b^2 = c \cdot n, \quad a \cdot b = c \cdot h$$
- Potencia de un Punto $P$ respecto a una circunferencia:
  $$PA \cdot PB = PC \cdot PD \quad (\text{Secantes}), \quad PT^2 = PA \cdot PB \quad (\text{Tangente y secante})$$
- Teorema de Ceva (Cevianas concurrentes):
  $$\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$$
- Teorema de Menelao (Puntos $D, E, F$ sobre las rectas de los lados de un $\triangle ABC$ son colineales):
  $$\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = -1 \quad (\text{Razones dirigidas})$$
  $$\left( \text{En magnitudes no dirigidas: } \frac{|AF|}{|FB|} \cdot \frac{|BD|}{|DC|} \cdot \frac{|CE|}{|EA|} = 1 \text{ con 1 o 3 puntos en las prolongaciones exteriores} \right)$$

### Nivel Universitario / Avanzado

#### 4.5 Geometría no Euclidiana y Topología Básica

- Característica de Euler-Poincaré (Poliedros convexos):
  $$V - E + F = 2 \quad (\text{Vértices} - \text{Aristas} + \text{Caras})$$
- Triángulo Esférico (Exceso esférico $E$ en radianes con ángulos $\alpha, \beta, \gamma$):
  $$E = \alpha + \beta + \gamma - \pi \quad (\text{con } E > 0 \text{ en rad})$$
- Área del Triángulo Esférico (Esfera de radio $R$):
  $$\text{Área} = R^2 E = R^2 (\alpha + \beta + \gamma - \pi)$$
- Curvatura Gaussiana ($K$):
  $$K = k_1 \cdot k_2$$
- Teorema de Gauss-Bonnet (Superficies compactas):
  $$\iint_M K \, dA + \oint_{\partial M} k_g \, ds = 2\pi \chi(M)$$
- Razón Doble (Cross-Ratio en Geometría Proyectiva):
  $$(A, B; C, D) = \frac{(c - a)(d - b)}{(c - b)(d - a)}$$

## 5. Geometría Analítica

### Nivel Básico

#### 5.1 Plano Cartesiano (2D)

- Distancia entre dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$:
  $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
- Punto medio $M$:
  $$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$
- División de segmento en una razón $r$ ($\frac{AP}{PB} = r$):
  $$x = \frac{x_1 + r x_2}{1 + r}, \quad y = \frac{y_1 + r y_2}{1 + r}$$

#### 5.2 La Línea Recta en 2D

- Pendiente:
  $$m = \frac{y_2 - y_1}{x_2 - x_1} = \tan(\theta)$$
- Ecuación Punto-Pendiente:
  $$y - y_1 = m(x - x_1)$$
- Ecuación Pendiente-Ordenada al origen:
  $$y = mx + b$$
- Ecuación General ($B \ne 0 \implies m = -\frac{A}{B}$):
  $$Ax + By + C = 0$$
- Ecuación Simétrica / Canónica:
  $$\frac{x}{a} + \frac{y}{b} = 1 \quad (\text{Intersecciones en } (a,0) \text{ y } (0,b))$$
- Rectas Paralelas y Perpendiculares:
  $$m_1 = m_2 \quad (\text{Paralelas}), \quad m_1 \cdot m_2 = -1 \iff m_1 = -\frac{1}{m_2} \quad (\text{Perpendiculares})$$
- Ángulo entre dos rectas:
  $$\tan(\theta) = \left|\frac{m_2 - m_1}{1 + m_1 \cdot m_2}\right|$$

### Nivel Intermedio

#### 5.3 Distancias y Secciones Cónicas en 2D

- Distancia de un punto $P(x_0, y_0)$ a una recta $Ax + By + C = 0$:
  $$d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$$

#### 5.4 Circunferencia

- Ecuación Ordinaria (Centro $(h, k)$, Radio $r$):
  $$(x - h)^2 + (y - k)^2 = r^2$$
- Ecuación General:
  $$x^2 + y^2 + Dx + Ey + F = 0$$

#### 5.5 Parábola

- Eje focal horizontal:
  $$(y - k)^2 = \pm 4p(x - h) \quad | \quad \text{Foco: } (h \pm p, k) \quad | \quad \text{Directriz: } x = h \mp p$$
- Eje focal vertical:
  $$(x - h)^2 = \pm 4p(y - k) \quad | \quad \text{Foco: } (h, k \pm p) \quad | \quad \text{Directriz: } y = k \mp p$$
- Longitud del Lado Recto:
  $$LR = |4p|$$

#### 5.6 Elipse

- Ecuación Ordinaria (Eje focal horizontal, $a > b$):
  $$\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1$$
- Relación fundamental:
  $$a^2 = b^2 + c^2$$
- Excentricidad ($0 < e < 1$):
  $$e = \frac{c}{a}$$
- Longitud del Lado Recto:
  $$LR = \frac{2b^2}{a}$$

#### 5.7 Hipérbola

- Ecuación Ordinaria (Eje transversal horizontal):
  $$\frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1$$
- Relación fundamental:
  $$c^2 = a^2 + b^2$$
- Excentricidad ($e > 1$):
  $$e = \frac{c}{a}$$
- Asíntotas (Centro en $(h,k)$):
  $$y - k = \pm \frac{b}{a}(x - h)$$

#### 5.8 Ecuación General de Segundo Grado en 2D

- Forma general y Discriminante ($\Delta$):
  $$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0, \quad \Delta = B^2 - 4AC$$
- Clasificación cónica:
  $$\Delta < 0 \implies \text{Tipo Elíptico (Elipse, Circunferencia)}$$
  $$\Delta = 0 \implies \text{Tipo Parabólico (Parábola, Rectas paralelas)}$$
  $$\Delta > 0 \implies \text{Tipo Hiperbólico (Hipérbola, Rectas secantes)}$$
- Ángulo de rotación de ejes para eliminar el término $Bxy$:
  $$\cot(2\theta) = \frac{A - C}{B}$$

#### 5.9 Sistemas de Coordenadas Alternativos

- Coordenadas Polares a Cartesianas:
  $$x = r\cos(\theta), \quad y = r\sin(\theta)$$
- Cartesianas a Polares:
  $$r = \sqrt{x^2 + y^2}, \quad \theta = \operatorname{atan2}(y, x) \in (-\pi, \pi]$$

### Nivel Universitario / Avanzado

#### 5.10 Geometría Analítica del Espacio (3D)

- Distancia entre dos puntos en $\mathbb{R}^3$:
  $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$
- Ecuación del Plano (Normal $\vec{n} = (A, B, C)$, pasa por $P_0(x_0, y_0, z_0)$):
  $$A(x - x_0) + B(y - y_0) + C(z - z_0) = 0 \implies Ax + By + Cz + D = 0$$
- Distancia de un punto $P(x_0, y_0, z_0)$ a un plano $Ax + By + Cz + D = 0$:
  $$d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}$$
- Ecuaciones de la Recta en $\mathbb{R}^3$ ($\vec{v} = (v_1, v_2, v_3)$):
  $$\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{v} \quad (\text{Vectorial})$$
  $$x = x_0 + tv_1, \quad y = y_0 + tv_2, \quad z = z_0 + tv_3 \quad (\text{Paramétrica})$$
  $$\frac{x - x_0}{v_1} = \frac{y - y_0}{v_2} = \frac{z - z_0}{v_3} \quad (\text{Continua / Simétrica})$$
- Distancia entre dos rectas alabeadas (cruzadas):
  $$d = \frac{|(\mathbf{r}_2 - \mathbf{r}_1) \cdot (\mathbf{v}_1 \times \mathbf{v}_2)|}{\|\mathbf{v}_1 \times \mathbf{v}_2\|}$$

#### 5.11 Superficies Cuádricas en $\mathbb{R}^3$ (Centro en el origen)

- Elipsoide:
  $$\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$$
- Hiperboloide de 1 hoja:
  $$\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$$
- Hiperboloide de 2 hojas:
  $$\frac{x^2}{a^2} - \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$$
- Paraboloide Elíptico:
  $$z = \frac{x^2}{a^2} + \frac{y^2}{b^2}$$
- Paraboloide Hiperbólico (Silla de montar):
  $$z = \frac{y^2}{b^2} - \frac{x^2}{a^2}$$
- Cono Cuádrico:
  $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{z^2}{c^2}$$

#### 5.12 Transformaciones de Coordenadas en $\mathbb{R}^3$

- Cilíndricas:
  $$x = r\cos(\theta), \quad y = r\sin(\theta), \quad z = z$$
- Esféricas ($\rho \ge 0, 0 \le \theta < 2\pi, 0 \le \varphi \le \pi$):
  $$x = \rho\sin(\varphi)\cos(\theta), \quad y = \rho\sin(\varphi)\sin(\theta), \quad z = \rho\cos(\varphi)$$

## 6. Álgebra Lineal

### Nivel Básico

#### 6.1 Vectores en $\mathbb{R}^n$

- Suma:
  $$\mathbf{u} + \mathbf{v} = (u_1 + v_1, u_2 + v_2, \dots, u_n + v_n)$$
- Producto Escalar por Vector:
  $$c\mathbf{u} = (cu_1, cu_2, \dots, cu_n)$$
- Norma / Módulo Euclidiano ($L_2$):
  $$\|\mathbf{u}\| = \sqrt{u_1^2 + u_2^2 + \dots + u_n^2} = \sqrt{\mathbf{u} \cdot \mathbf{u}}$$
- Vector Unitario:
  $$\hat{\mathbf{u}} = \frac{\mathbf{u}}{\|\mathbf{u}\|}$$

#### 6.2 Productos Vectoriales

- Producto Punto (Escalar) y Ortogonalidad:
  $$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos(\theta), \quad \mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0$$
- Producto Cruz (Vectorial en $\mathbb{R}^3$):
  $$\mathbf{u} \times \mathbf{v} = \det\begin{pmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{pmatrix}, \quad \|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\| \|\mathbf{v}\| \sin(\theta)$$
- Producto Triple Escalar (Volumen del paralelepípedo):
  $$[\mathbf{u}, \mathbf{v}, \mathbf{w}] = \mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \det\begin{pmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{pmatrix}$$

#### 6.3 Sistemas de Ecuaciones Lineales

- Sistema Matricial:
  $$A\mathbf{x} = \mathbf{b}$$
- Regla de Cramer ($\det(A) \ne 0$):
  $$x_i = \frac{\det(A_i)}{\det(A)}$$

### Nivel Intermedio

#### 6.4 Álgebra de Matrices

- Multiplicación de Matrices:
  $$(AB)_{ij} = \sum_{k=1}^m A_{ik} B_{kj}$$
- Transposición:
  $$(AB)^T = B^T A^T$$
- Traza y Propiedad Cíclica:
  $$\operatorname{Tr}(A) = \sum_{i=1}^n A_{ii}, \quad \operatorname{Tr}(AB) = \operatorname{Tr}(BA)$$
- Determinante (Propiedades):
  $$\det(AB) = \det(A)\det(B), \quad \det(A^T) = \det(A), \quad \det(A^{-1}) = \frac{1}{\det(A)}, \quad \det(cA) = c^n \det(A)$$

#### 6.5 Espacios Vectoriales

- Subespacios (Criterio de cerradura):
  $$\mathbf{0} \in W, \quad \mathbf{u} + \mathbf{v} \in W, \quad c\mathbf{u} \in W$$
- Dependencia Lineal:
  $$\sum_{i=1}^k c_i \mathbf{v}_i = \mathbf{0} \quad (\text{con algún } c_i \ne 0)$$
- Teorema del Rango-Nulidad:
  $$\dim(\operatorname{Nuc}(T)) + \dim(\operatorname{Im}(T)) = \dim(V) \iff \operatorname{nulidad}(A) + \operatorname{rango}(A) = n$$

#### 6.6 Espacios con Producto Interno y Ortogonalidad

- Desigualdad de Cauchy-Schwarz:
  $$|\langle \mathbf{u}, \mathbf{v} \rangle| \le \|\mathbf{u}\| \|\mathbf{v}\|$$
- Desigualdad Triangular:
  $$\|\mathbf{u} + \mathbf{v}\| \le \|\mathbf{u}\| + \|\mathbf{v}\|$$
- Proyección Ortogonal de $\mathbf{u}$ sobre $\mathbf{v}$:
  $$\operatorname{Proy}_{\mathbf{v}}(\mathbf{u}) = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{v}\|^2} \mathbf{v}$$
- Proceso de Ortogonalización de Gram-Schmidt:
  $$\mathbf{u}_1 = \mathbf{v}_1$$
  $$\mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \operatorname{Proy}_{\mathbf{u}_j}(\mathbf{v}_k)$$
  $$\mathbf{e}_i = \frac{\mathbf{u}_i}{\|\mathbf{u}_i\|} \quad (\text{Normalización})$$

### Nivel Universitario / Avanzado

#### 6.7 Autovalores, Autovectores y Diagonalización

- Polinomio Característico:
  $$p(\lambda) = \det(A - \lambda I) = 0$$
- Ecuación del Autovector:
  $$(A - \lambda I)\mathbf{v} = \mathbf{0} \iff A\mathbf{v} = \lambda\mathbf{v}$$
- Teorema de Cayley-Hamilton:
  $$p(A) = O$$
- Diagonalización:
  $$A = PDP^{-1}$$
- Teorema Espectral (Matrices Simétricas / Hermíticas):
  $$A = Q\Lambda Q^T \quad (\text{Real simétrica: } Q \text{ ortogonal}), \quad A = U\Lambda U^H \quad (\text{Compleja hermítica: } U \text{ unitaria})$$
- Forma Canónica de Jordan:
  $$A = PJP^{-1}, \quad J = \operatorname{diag}(J_1, \dots, J_k)$$

#### 6.8 Factorizaciones y Descomposiciones Matriciales

- Descomposiciones LU, QR y Cholesky ($A$ simétrica definida positiva):
  $$A = LU, \quad A = QR, \quad A = LL^T$$
- Descomposición en Valores Singulares (SVD):
  $$A = U\Sigma V^T \quad (\text{o } U\Sigma V^*), \quad \sigma_i = \sqrt{\lambda_i(A^T A)}$$
- Pseudoinversa de Moore-Penrose:
  $$A^+ = V\Sigma^+ U^H \quad (\text{General vía SVD; } A^+ = (A^H A)^{-1} A^H \text{ si } \operatorname{rango}(A) = n \text{ [col. completo]})$$
- Solución por Mínimos Cuadrados ($\hat{\mathbf{x}} = A^+ \mathbf{b}$):
  $$\hat{\mathbf{x}} = (A^T A)^{-1} A^T \mathbf{b} \quad (\text{Para } A \text{ real de rango columna completo})$$

#### 6.9 Operaciones Tensoriales

- Producto de Kronecker:
  $$(A \otimes B)_{p(r-1)+v, \, q(s-1)+w} = A_{rs} B_{vw}$$
- Propiedad de Producto Mixto:
  $$(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$$

# Compendio III: Cálculo Diferencial, Integral y Vectorial
*(Nivel Básico a Universitario)*

## 7. Cálculo Diferencial

### Nivel Básico

#### 7.1 Definición de Límite y Continuidad

- Definición épsilon-delta:
  $$\lim_{x \to a} f(x) = L \iff \forall \varepsilon > 0, \, \exists \delta > 0 : 0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon$$
- Continuidad en un punto $a$:
  $$\lim_{x \to a} f(x) = f(a)$$

#### 7.2 Definición Formal de la Derivada

- Por límite (Cociente diferencial):
  $$f'(x) = \frac{dy}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$
- En un punto $a$:
  $$f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$$

#### 7.3 Reglas y Derivadas Algebraicas Elementales

- Constante:
  $$\frac{d}{dx}(c) = 0$$
- Identidad:
  $$\frac{d}{dx}(x) = 1$$
- Regla de la Potencia:
  $$\frac{d}{dx}(x^n) = n x^{n - 1}$$
- Múltiplo Constante:
  $$\frac{d}{dx}[c \cdot f(x)] = c f'(x)$$
- Suma y Resta:
  $$\frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)$$
- Raíz cuadrada:
  $$\frac{d}{dx}(\sqrt{x}) = \frac{1}{2\sqrt{x}}$$
- Inverso:
  $$\frac{d}{dx}\left(\frac{1}{x}\right) = -\frac{1}{x^2}$$

### Nivel Intermedio

#### 7.4 Reglas Fundamentales de Derivación

- Regla del Producto:
  $$\frac{d}{dx}[f(x) \cdot g(x)] = f'(x)g(x) + f(x)g'(x)$$
- Regla del Cociente:
  $$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$$
- Regla de la Cadena:
  $$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x) \iff \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

#### 7.5 Derivadas de Funciones Trascendentes Elementales

- Exponenciales:
  $$\frac{d}{dx}(e^x) = e^x, \quad \frac{d}{dx}(a^x) = a^x \ln(a) \quad (a > 0, a \ne 1)$$
- Logarítmicas:
  $$\frac{d}{dx}(\ln|x|) = \frac{1}{x}, \quad \frac{d}{dx}(\log_a|x|) = \frac{1}{x\ln(a)}$$
- Trigonométricas Directas:
  $$\frac{d}{dx}[\sin(x)] = \cos(x), \quad \frac{d}{dx}[\cos(x)] = -\sin(x), \quad \frac{d}{dx}[\tan(x)] = \sec^2(x)$$
  $$\frac{d}{dx}[\cot(x)] = -\csc^2(x), \quad \frac{d}{dx}[\sec(x)] = \sec(x)\tan(x), \quad \frac{d}{dx}[\csc(x)] = -\csc(x)\cot(x)$$
- Trigonométricas Inversas:
  $$\frac{d}{dx}[\arcsin(x)] = \frac{1}{\sqrt{1 - x^2}}, \quad \frac{d}{dx}[\arccos(x)] = -\frac{1}{\sqrt{1 - x^2}}, \quad \frac{d}{dx}[\arctan(x)] = \frac{1}{1 + x^2}$$
  $$\frac{d}{dx}[\operatorname{arccot}(x)] = -\frac{1}{1 + x^2}, \quad \frac{d}{dx}[\operatorname{arcsec}(x)] = \frac{1}{|x|\sqrt{x^2 - 1}}, \quad \frac{d}{dx}[\operatorname{arccsc}(x)] = -\frac{1}{|x|\sqrt{x^2 - 1}}$$

#### 7.6 Aplicaciones y Teoremas del Cálculo Diferencial

- Recta Tangente en $(x_0, y_0)$:
  $$y - y_0 = f'(x_0)(x - x_0)$$
- Recta Normal en $(x_0, y_0)$ ($f'(x_0) \ne 0$):
  $$y - y_0 = -\frac{1}{f'(x_0)}(x - x_0)$$
- Regla de L'Hôpital ($f, g$ derivables, $g'(x) \ne 0$ cerca de $a$, indeterminación $0/0$ o $\pm\infty/\pm\infty$, y existe el límite de $f'/g'$):
  $$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
- Teorema de Rolle ($f$ continua en $[a, b]$, derivable en $(a, b)$ y $f(a) = f(b)$):
  $$\exists c \in (a, b) : f'(c) = 0$$
- Teorema del Valor Medio (Lagrange, $f$ continua en $[a, b]$ y derivable en $(a, b)$):
  $$\exists c \in (a, b) : f'(c) = \frac{f(b) - f(a)}{b - a}$$
- Teorema del Valor Medio Generalizado (Cauchy, $f, g$ continuas en $[a, b]$, derivables en $(a, b)$ y $g'(x) \ne 0$ en $(a, b)$):
  $$\exists c \in (a, b) : \frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$$

### Nivel Universitario / Avanzado

#### 7.7 Derivadas de Funciones Hiperbólicas e Inversas

- Directas:
  $$\frac{d}{dx}[\sinh(x)] = \cosh(x), \quad \frac{d}{dx}[\cosh(x)] = \sinh(x)$$
  $$\frac{d}{dx}[\tanh(x)] = \operatorname{sech}^2(x), \quad \frac{d}{dx}[\operatorname{sech}(x)] = -\operatorname{sech}(x)\tanh(x)$$
- Inversas:
  $$\frac{d}{dx}[\operatorname{arsinh}(x)] = \frac{1}{\sqrt{x^2 + 1}}$$
  $$\frac{d}{dx}[\operatorname{arcosh}(x)] = \frac{1}{\sqrt{x^2 - 1}} \quad (x > 1)$$
  $$\frac{d}{dx}[\operatorname{artanh}(x)] = \frac{1}{1 - x^2} \quad (|x| < 1)$$

#### 7.8 Diferencial Total y Series

- Diferencial:
  $$dy = f'(x) dx$$
- Serie de Taylor alrededor de $x = a$:
  $$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (x - a)^n$$
- Resto de Lagrange ($\xi \in (a, x)$):
  $$R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} (x - a)^{n+1}$$

#### 7.9 Geometría Diferencial de Curvas Planas

- Curvatura ($\kappa$):
  $$\kappa = \frac{|y''|}{[1 + (y')^2]^{\frac{3}{2}}}$$
- Radio de Curvatura ($R$):
  $$R = \frac{1}{\kappa} = \frac{[1 + (y')^2]^{\frac{3}{2}}}{|y''|}$$

## 8. Cálculo Integral

### Nivel Básico

#### 8.1 Definición y Propiedades Fundamentales

- Antiderivada:
  $$\int f(x) \, dx = F(x) + C \iff F'(x) = f(x)$$
- Linealidad:
  $$\int [a f(x) + b g(x)] \, dx = a \int f(x) \, dx + b \int g(x) \, dx$$

#### 8.2 Integrales Indefinidas Elementales / Inmediatas

- Potencias ($n \ne -1$):
  $$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$$
- Logarítmica:
  $$\int \frac{1}{x} \, dx = \ln|x| + C$$
- Exponenciales:
  $$\int e^x \, dx = e^x + C, \quad \int a^x \, dx = \frac{a^x}{\ln(a)} + C$$
- Trigonométricas Directas:
  $$\int \sin(x) \, dx = -\cos(x) + C, \quad \int \cos(x) \, dx = \sin(x) + C$$
  $$\int \sec^2(x) \, dx = \tan(x) + C, \quad \int \csc^2(x) \, dx = -\cot(x) + C$$
  $$\int \sec(x)\tan(x) \, dx = \sec(x) + C, \quad \int \csc(x)\cot(x) \, dx = -\csc(x) + C$$

### Nivel Intermedio

#### 8.3 Teorema Fundamental del Cálculo (TFC)

- Parte 1 (Derivada de la integral):
  $$\frac{d}{dx} \left[ \int_a^x f(t) \, dt \right] = f(x)$$
- Regla de Leibniz (1D):
  $$\frac{d}{dx} \left[ \int_{u(x)}^{v(x)} f(t) \, dt \right] = f(v(x))v'(x) - f(u(x))u'(x)$$
- Parte 2 (Regla de Barrow):
  $$\int_a^b f(x) \, dx = F(b) - F(a) = [F(x)]_a^b$$

#### 8.4 Técnicas / Métodos de Integración

- Cambio de Variable / Sustitución ($u = g(x)$):
  $$\int f(g(x))g'(x) \, dx = \int f(u) \, du$$
- Integración por Partes:
  $$\int u \, dv = u v - \int v \, du$$
- Sustituciones Trigonométricas:
  $$\text{Para } \sqrt{a^2 - x^2} \implies x = a\sin(\theta), \quad dx = a\cos(\theta) d\theta, \quad \sqrt{a^2 - x^2} = a\cos(\theta)$$
  $$\text{Para } \sqrt{a^2 + x^2} \implies x = a\tan(\theta), \quad dx = a\sec^2(\theta) d\theta, \quad \sqrt{a^2 + x^2} = a\sec(\theta)$$
  $$\text{Para } \sqrt{x^2 - a^2} \implies x = a\sec(\theta), \quad dx = a\sec(\theta)\tan(\theta) d\theta, \quad \sqrt{x^2 - a^2} = a\tan(\theta)$$

#### 8.5 Integrales Trigonométricas e Inversas Clave

- Tangente y Cotangente:
  $$\int \tan(x) \, dx = \ln|\sec(x)| + C = -\ln|\cos(x)| + C$$
  $$\int \cot(x) \, dx = \ln|\sin(x)| + C$$
- Secante y Cosecante:
  $$\int \sec(x) \, dx = \ln|\sec(x) + \tan(x)| + C$$
  $$\int \csc(x) \, dx = -\ln|\csc(x) + \cot(x)| + C = \ln|\csc(x) - \cot(x)| + C$$
- Racionales y de Radicales:
  $$\int \frac{1}{x^2 + a^2} \, dx = \frac{1}{a} \arctan\left(\frac{x}{a}\right) + C$$
  $$\int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \arcsin\left(\frac{x}{a}\right) + C$$
  $$\int \frac{1}{|x|\sqrt{x^2 - a^2}} \, dx = \frac{1}{a} \operatorname{arcsec}\left(\frac{|x|}{a}\right) + C$$
  $$\int \frac{1}{x^2 - a^2} \, dx = \frac{1}{2a} \ln\left|\frac{x - a}{x + a}\right| + C$$

#### 8.6 Aplicaciones Geométricas y Físicas

- Área entre curvas:
  $$A = \int_a^b |f(x) - g(x)| \, dx$$
- Longitud de Arco:
  $$L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx$$
- Volumen de Revolución (Método de Discos):
  $$V = \pi \int_a^b [f(x)]^2 \, dx$$
- Volumen de Revolución (Método de Arandelas):
  $$V = \pi \int_a^b ([R(x)]^2 - [r(x)]^2) \, dx$$
- Volumen de Revolución (Método de Cascarones / Capas):
  $$V = 2\pi \int_a^b x f(x) \, dx$$
- Área de Superficie de Revolución:
  $$S = 2\pi \int_a^b f(x) \sqrt{1 + [f'(x)]^2} \, dx$$
- Valor Medio de una Función:
  $$f_{\text{prom}} = \frac{1}{b - a} \int_a^b f(x) \, dx$$

### Nivel Universitario / Avanzado

#### 8.7 Integrales Impropias

- Límites infinitos:
  $$\int_a^\infty f(x) \, dx = \lim_{t \to \infty} \int_a^t f(x) \, dx$$
- Discontinuidad en $b$:
  $$\int_a^b f(x) \, dx = \lim_{t \to b^-} \int_a^t f(x) \, dx$$

#### 8.8 Sustitución Universal de Weierstrass (Ángulo Mitad)

- Sustitución $t = \tan\left(\frac{x}{2}\right)$:
  $$dx = \frac{2}{1 + t^2} dt, \quad \sin(x) = \frac{2t}{1 + t^2}, \quad \cos(x) = \frac{1 - t^2}{1 + t^2}$$

#### 8.9 Integrales Hiperbólicas Inmediatas

- Seno y Coseno hiperbólico:
  $$\int \sinh(x) \, dx = \cosh(x) + C, \quad \int \cosh(x) \, dx = \sinh(x) + C$$
- Formas hiperbólicas inversas:
  $$\int \frac{1}{\sqrt{x^2 + a^2}} \, dx = \operatorname{arsinh}\left(\frac{x}{a}\right) + C = \ln\left(x + \sqrt{x^2 + a^2}\right) + C$$
  $$\int \frac{1}{\sqrt{x^2 - a^2}} \, dx = \operatorname{arcosh}\left(\frac{x}{a}\right) + C = \ln\left|x + \sqrt{x^2 - a^2}\right| + C \quad (x > a)$$

#### 8.10 Funciones Especiales e Integrales Notables

- Función Gamma ($\Gamma(n + 1) = n!$):
  $$\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt$$
- Función Beta:
  $$\mathrm{B}(x, y) = \int_0^1 t^{x-1} (1 - t)^{y-1} \, dt = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x + y)}$$
- Integral Gaussiana:
  $$\int_{-\infty}^\infty e^{-x^2} \, dx = \sqrt{\pi}$$
- Diferenciación bajo el signo de integral (Regla de Leibniz 2D):
  $$\frac{d}{dx} \left[ \int_{a(x)}^{b(x)} f(x, t) \, dt \right] = f(x, b(x))b'(x) - f(x, a(x))a'(x) + \int_{a(x)}^{b(x)} \frac{\partial f}{\partial x}(x, t) \, dt$$

## 9. Cálculo Vectorial y Multivariable

### Nivel Básico

#### 9.1 Curvas Paramétricas y Funciones Vectoriales en $\mathbb{R}^3$

- Vector de Posición:
  $$\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$$
- Velocidad:
  $$\mathbf{v}(t) = \mathbf{r}'(t) = x'(t)\mathbf{i} + y'(t)\mathbf{j} + z'(t)\mathbf{k}$$
- Rapidez:
  $$\|\mathbf{v}(t)\| = \frac{ds}{dt} = \sqrt{[x'(t)]^2 + [y'(t)]^2 + [z'(t)]^2}$$
- Aceleración:
  $$\mathbf{a}(t) = \mathbf{r}''(t) = \mathbf{v}'(t)$$

#### 9.2 Derivadas Parciales de Funciones Escalares $f(x, y, z)$

- Derivada parcial respecto a $x$:
  $$\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x + h, y, z) - f(x, y, z)}{h}$$
- Teorema de Schwarz / Clairaut (Derivadas cruzadas):
  $$\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$$

#### 9.3 Gradiente

- Vector Gradiente:
  $$\nabla f = \operatorname{grad}(f) = \frac{\partial f}{\partial x}\mathbf{i} + \frac{\partial f}{\partial y}\mathbf{j} + \frac{\partial f}{\partial z}\mathbf{k}$$

### Nivel Intermedio

#### 9.4 Diferenciabilidad y Regla de la Cadena Multivariable

- Diferencial Total:
  $$df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz$$
- Regla de la Cadena ($w = f(x, y)$, con $x = x(t)$, $y = y(t)$):
  $$\frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt}$$

#### 9.5 Derivada Direccional y Planos Tangentes

- Derivada Direccional (en dirección del vector unitario $\mathbf{u}$):
  $$D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = \|\nabla f\|\cos(\theta)$$
  $$(\text{Dirección de máximo crecimiento} = \nabla f; \quad \text{Valor máximo} = \|\nabla f\|)$$
- Plano Tangente a superficie de nivel $F(x, y, z) = c$ en $P_0(x_0, y_0, z_0)$:
  $$\nabla F(P_0) \cdot (\mathbf{r} - \mathbf{r}_0) = 0 \implies F_x(P_0)(x - x_0) + F_y(P_0)(y - y_0) + F_z(P_0)(z - z_0) = 0$$

#### 9.6 Optimización Multivariable

- Matriz Hessiana (2D) y Discriminante ($D$):
  $$H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix}, \quad D = \det(H) = f_{xx} f_{yy} - (f_{xy})^2$$
- Criterio de clasificación:
  $$D > 0 \text{ y } f_{xx} > 0 \implies \text{Mínimo Local}$$
  $$D > 0 \text{ y } f_{xx} < 0 \implies \text{Máximo Local}$$
  $$D < 0 \implies \text{Punto de Silla}$$
  $$D = 0 \implies \text{Criterio no concluyente}$$
- Multiplicadores de Lagrange (Restricción $g(x,y,z) = k$):
  $$\nabla f = \lambda \nabla g$$

#### 9.7 Integrales Múltiples y Transformaciones de Coordenadas

- Integral Doble General:
  $$\iint_R f(x, y) \, dx \, dy = \iint_S f(x(u,v), y(u,v)) |J(u, v)| \, du \, dv$$
- Jacobiano de Transformación:
  $$J(u, v) = \frac{\partial(x, y)}{\partial(u, v)} = \det\begin{pmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{pmatrix}$$
- Coordenadas Polares (2D):
  $$dA = r \, dr \, d\theta$$
- Coordenadas Cilíndricas (3D):
  $$dV = r \, dr \, d\theta \, dz$$
- Coordenadas Esféricas (3D):
  $$dV = \rho^2 \sin(\varphi) \, d\rho \, d\varphi \, d\theta$$

### Nivel Universitario / Avanzado

#### 9.8 Operadores Diferenciales Vectoriales (en Coordenadas Cartesianas)

- Divergencia de un campo vectorial $\mathbf{F} = (P, Q, R)$:
  $$\operatorname{div}(\mathbf{F}) = \nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$
- Rotacional de un campo vectorial $\mathbf{F} = (P, Q, R)$:
  $$\operatorname{rot}(\mathbf{F}) = \nabla \times \mathbf{F} = \det\begin{pmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & R \end{pmatrix} = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}\right)\mathbf{i} + \left(\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}\right)\mathbf{j} + \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\mathbf{k}$$
- Operador Laplaciano Escalar:
  $$\Delta f = \nabla^2 f = \nabla \cdot (\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$
- Operador Laplaciano Vectorial:
  $$\nabla^2 \mathbf{F} = \nabla(\nabla \cdot \mathbf{F}) - \nabla \times (\nabla \times \mathbf{F})$$
- Identidades Diferenciales Fundamentales:
  $$\nabla \times (\nabla f) = \mathbf{0} \quad (\text{Rotacional de gradiente nulo})$$
  $$\nabla \cdot (\nabla \times \mathbf{F}) = 0 \quad (\text{Divergencia de rotacional nula})$$
  $$\nabla \cdot (f \mathbf{F}) = f(\nabla \cdot \mathbf{F}) + \mathbf{F} \cdot (\nabla f)$$
  $$\nabla \times (f \mathbf{F}) = f(\nabla \times \mathbf{F}) + (\nabla f) \times \mathbf{F}$$

#### 9.9 Integrales de Línea y Superficie

- Integral de Línea de Campo Escalar:
  $$\int_C f \, ds = \int_a^b f(\mathbf{r}(t)) \|\mathbf{r}'(t)\| \, dt$$
- Integral de Línea de Campo Vectorial (Trabajo / Circulación):
  $$W = \int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) \, dt = \int_C (P \, dx + Q \, dy + R \, dz)$$
- Teorema Fundamental para Integrales de Línea (Campos Conservativos $\mathbf{F} = \nabla\varphi$):
  $$\int_C \mathbf{F} \cdot d\mathbf{r} = \varphi(\mathbf{r}(b)) - \varphi(\mathbf{r}(a))$$
- Integral de Superficie de Campo Vectorial (Flujo):
  $$\Phi = \iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_D \mathbf{F}(\mathbf{r}(u, v)) \cdot (\mathbf{r}_u \times \mathbf{r}_v) \, du \, dv$$

#### 9.10 Teoremas Integrales Fundamentales del Análisis Vectorial

- Teorema de Green en el Plano (Curva $C$ cerrada, frontera de $D$):
  $$\oint_C (P \, dx + Q \, dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA$$
- Teorema de Stokes:
  $$\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}$$
- Teorema de la Divergencia de Gauss (Superficie cerrada $\partial V$):
  $$\iint_{\partial V} \mathbf{F} \cdot d\mathbf{S} = \iiint_V (\nabla \cdot \mathbf{F}) \, dV$$

#### 9.11 Geometría Diferencial en $\mathbb{R}^3$ (Triedro de Frenet-Serret)

- Vector Tangente Unitario:
  $$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$$
- Vector Normal Principal:
  $$\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|}$$
- Vector Binormal:
  $$\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t)$$
- Fórmulas de Frenet-Serret (Parámetro de longitud de arco $s$):
  $$\frac{d\mathbf{T}}{ds} = \kappa \mathbf{N}$$
  $$\frac{d\mathbf{N}}{ds} = -\kappa \mathbf{T} + \tau \mathbf{B}$$
  $$\frac{d\mathbf{B}}{ds} = -\tau \mathbf{N} \quad (\kappa = \text{curvatura}, \, \tau = \text{torsión})$$

# Compendio IV: Ecuaciones Diferenciales y Métodos Numéricos
*(Nivel Básico a Universitario)*

## 10. Ecuaciones Diferenciales

### Nivel Básico

#### 10.1 Definiciones y Clasificación

- Problema de Valor Inicial (PVI):
  $$y' = f(x, y), \quad y(x_0) = y_0$$
- Teorema de Existencia y Unicidad de Picard-Lindelöf:
  $$y' = f(x, y), \quad y(x_0) = y_0 \implies \exists ! \, y(x) \quad \text{en } I$$

#### 10.2 Ecuaciones Diferenciales Ordinarias (EDO) de 1er Orden Elementales

- Variables Separables:
  $$g(y) \, dy = f(x) \, dx \implies \int g(y) \, dy = \int f(x) \, dx + C$$
- Ecuación Lineal de 1er Orden (Factor Integrante de Leibniz):
  $$y' + P(x)y = Q(x), \quad \mu(x) = e^{\int P(x) \, dx}$$
  $$y(x) = \frac{1}{\mu(x)} \left[ \int \mu(x) Q(x) \, dx + C \right]$$
- Ecuaciones Exactas:
  $$M(x, y) \, dx + N(x, y) \, dy = 0, \quad \frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \implies \Psi(x, y) = C$$
- Factores Integrantes para Ecuaciones no Exactas:
  $$\mu(x) = e^{\int \frac{M_y - N_x}{N} \, dx}, \quad \mu(y) = e^{\int \frac{N_x - M_y}{M} \, dy}$$

### Nivel Intermedio

#### 10.3 Ecuaciones Diferenciales Reducibles a 1er Orden

- Ecuación Homogénea de Grado $n$:
  $$\frac{dy}{dx} = F\left(\frac{y}{x}\right) \implies y = ux, \quad \frac{dy}{dx} = u + x\frac{du}{dx}$$
- Ecuación de Bernoulli ($n \ne 0, 1$):
  $$y' + P(x)y = Q(x)y^n, \quad u = y^{1 - n} \implies u' + (1 - n)P(x)u = (1 - n)Q(x)$$
- Ecuación de Riccati (Con solución particular conocida $y_1(x)$):
  $$y' = P(x) + Q(x)y + R(x)y^2, \quad y = y_1(x) + \frac{1}{u(x)}$$
- Ecuación de Clairaut:
  $$y = x y' + f(y') \implies y = Cx + f(C) \quad (\text{Solución general})$$

#### 10.4 EDOs Lineales de Orden Superior con Coeficientes Constantes

- Forma General Homogénea:
  $$a_n y^{(n)} + a_{n-1} y^{(n-1)} + \dots + a_1 y' + a_0 y = 0$$
- Ecuación Característica ($2^\circ \text{ orden}$):
  $$a r^2 + b r + c = 0$$
  $$\text{Raíces reales distintas } (r_1 \ne r_2): \quad y_h = c_1 e^{r_1 x} + c_2 e^{r_2 x}$$
  $$\text{Raíces reales repetidas } (r_1 = r_2 = r): \quad y_h = (c_1 + c_2 x)e^{r x}$$
  $$\text{Raíces complejas } (r = \alpha \pm i\beta): \quad y_h = e^{\alpha x}(c_1 \cos(\beta x) + c_2 \sin(\beta x))$$
- Wronskiano e Independencia Lineal:
  $$W(y_1, y_2, \dots, y_n) = \det\begin{pmatrix} y_1 & y_2 & \dots & y_n \\ y_1' & y_2' & \dots & y_n' \\ \vdots & \vdots & \ddots & \vdots \\ y_1^{(n-1)} & y_2^{(n-1)} & \dots & y_n^{(n-1)} \end{pmatrix} \ne 0$$
- Fórmula de Abel para el Wronskiano:
  $$W(x) = W(x_0) e^{-\int P(x) \, dx}$$
- Método de Variación de Parámetros ($y'' + P(x)y' + Q(x)y = g(x)$):
  $$y_p = u_1(x)y_1(x) + u_2(x)y_2(x)$$
  $$u_1'(x) = -\frac{y_2(x) g(x)}{W(y_1, y_2)}, \quad u_2'(x) = \frac{y_1(x) g(x)}{W(y_1, y_2)}$$
- Ecuación Equidimensional de Cauchy-Euler:
  $$a x^2 y'' + b x y' + c y = 0 \implies a r(r - 1) + b r + c = a r^2 + (b - a)r + c = 0$$

#### 10.5 Transformada de Laplace para EDOs

- Definición:
  $$\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st} f(t) \, dt$$
- Transformadas de Derivadas:
  $$\mathcal{L}\{f'(t)\} = s F(s) - f(0)$$
  $$\mathcal{L}\{f''(t)\} = s^2 F(s) - s f(0) - f'(0)$$
  $$\mathcal{L}\{f^{(n)}(t)\} = s^n F(s) - \sum_{k=1}^n s^{n - k} f^{(k - 1)}(0)$$
- Teoremas de Traslación:
  $$\mathcal{L}\{e^{at} f(t)\} = F(s - a)$$
  $$\mathcal{L}\{f(t - a)\mathcal{U}(t - a)\} = e^{-as} F(s) \quad (\mathcal{U} = \text{escalón unitario de Heaviside})$$
- Transformada de la Convolución:
  $$\mathcal{L}\{(f * g)(t)\} = \mathcal{L}\left\{ \int_0^t f(\tau)g(t - \tau) \, d\tau \right\} = F(s) \cdot G(s)$$
- Transformada de la Delta de Dirac:
  $$\mathcal{L}\{\delta(t - t_0)\} = e^{-s t_0}, \quad \mathcal{L}\{\delta(t)\} = 1$$

### Nivel Universitario / Avanzado

#### 10.6 Solución de EDOs por Series de Potencias

- En torno a un punto ordinario $x_0 = 0$:
  $$y(x) = \sum_{n=0}^\infty c_n x^n$$
- Método de Frobenius (Punto singular regular $x_0 = 0$):
  $$y(x) = x^r \sum_{n=0}^\infty c_n x^n = \sum_{n=0}^\infty c_n x^{n + r} \quad (c_0 \ne 0)$$
  $$\text{Ecuación Indicial: } F(r) = r(r - 1) + p_0 r + q_0 = 0$$
- Ecuación Diferencial de Bessel:
  $$x^2 y'' + x y' + (x^2 - \nu^2)y = 0 \implies y(x) = c_1 J_\nu(x) + c_2 Y_\nu(x)$$
- Ecuación Diferencial de Legendre:
  $$(1 - x^2)y'' - 2x y' + n(n + 1)y = 0 \implies y(x) = c_1 P_n(x) + c_2 Q_n(x)$$

#### 10.7 Sistemas de Ecuaciones Diferenciales Lineales

- Forma Matricial:
  $$\mathbf{x}'(t) = A\mathbf{x}(t) + \mathbf{g}(t)$$
- Matriz Exponencial:
  $$e^{At} = I + At + \frac{A^2 t^2}{2!} + \dots = \sum_{k=0}^\infty \frac{A^k t^k}{k!}$$
- Solución del Sistema Homogéneo:
  $$\mathbf{x}(t) = e^{At}\mathbf{x}(0) = \Phi(t)\mathbf{c}$$
- Fórmula de Variación de Parámetros Matricial:
  $$\mathbf{x}(t) = e^{A(t - t_0)}\mathbf{x}(t_0) + \int_{t_0}^t e^{A(t - \tau)}\mathbf{g}(\tau) \, d\tau$$

#### 10.8 Ecuaciones Diferenciales Parciales (EDP) Clásicas

- Ecuación de Onda (Hiperbólica):
  $$\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u$$
- Fórmula de d'Alembert (1D en recta infinita):
  $$u(x, t) = \frac{f(x - ct) + f(x + ct)}{2} + \frac{1}{2c}\int_{x - ct}^{x + ct} g(s) \, ds$$
- Ecuación del Calor / Difusión (Parabólica):
  $$\frac{\partial u}{\partial t} = \alpha \nabla^2 u$$
- Solución Fundamental / Núcleo del Calor (1D):
  $$\Phi(x, t) = \frac{1}{\sqrt{4\pi \alpha t}} e^{-\frac{x^2}{4\alpha t}}$$
- Ecuaciones de Laplace y Poisson (Elípticas):
  $$\nabla^2 u = 0 \quad (\text{Laplace}), \quad \nabla^2 u = f(x, y, z) \quad (\text{Poisson})$$
- Método de Separación de Variables (1D):
  $$u(x, t) = X(x)T(t) \implies \frac{X''}{X} = \frac{T'}{\alpha T} = -\lambda$$

#### 10.9 Problemas de Sturm-Liouville

- Forma Autoadjunta ($x \in [a, b]$):
  $$\frac{d}{dx}\left[ p(x)\frac{dy}{dx} \right] + q(x)y + \lambda w(x)y = 0$$
- Relación de Ortogonalidad de Autofunciones ($\lambda_n \ne \lambda_m$):
  $$\int_a^b \phi_n(x)\phi_m(x)w(x) \, dx = 0$$

## 11. Métodos Numéricos

### Nivel Básico

#### 11.1 Teoría de Errores

- Error Absoluto y Relativo:
  $$E_a = |x - \hat{x}|, \quad E_r = \frac{|x - \hat{x}|}{|x|} \quad (x \ne 0)$$
- Error Relativo Porcentual y Aproximado:
  $$E_p = E_r \cdot 100\%, \quad \varepsilon_a = \left|\frac{x_{\text{actual}} - x_{\text{anterior}}}{x_{\text{actual}}}\right| \cdot 100\%$$

#### 11.2 Raíces de Ecuaciones No Lineales (Métodos de Intervalo / Cerrados)

- Teorema de Bolzano:
  $$f(a) \cdot f(b) < 0 \implies \exists c \in (a, b) : f(c) = 0$$
- Método de Bisección (Punto medio $c_n$ tras $n$ iteraciones):
  $$c_n = \frac{a_n + b_n}{2}, \quad E_n = |r - c_n| \le \frac{b - a}{2^{n+1}}, \quad n \ge \left\lceil \log_2\left(\frac{b - a}{2\varepsilon}\right) \right\rceil$$
- Método de Falsa Posición (Regula Falsi):
  $$c = b - \frac{f(b)(a - b)}{f(a) - f(b)} = \frac{a f(b) - b f(a)}{f(b) - f(a)}$$

### Nivel Intermedio

#### 11.3 Raíces de Ecuaciones No Lineales (Métodos Abiertos)

- Método de Iteración de Punto Fijo ($g([a, b]) \subseteq [a, b]$ y $\max_{x \in [a, b]} |g'(x)| \le k < 1$):
  $$f(x) = 0 \iff x = g(x), \quad x_{k+1} = g(x_k), \quad |x_{k+1} - x^*| \le k |x_k - x^*|$$
- Método de Newton-Raphson (Orden cuadrático $p = 2$):
  $$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$
- Método de la Secante (Orden superlineal $p \approx 1.618$):
  $$x_{k+1} = x_k - f(x_k)\frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}$$
- Método de Newton-Raphson Multivariable ($\mathbf{F}(\mathbf{x}) = \mathbf{0}$):
  $$\mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} - [J(\mathbf{x}^{(k)})]^{-1}\mathbf{F}(\mathbf{x}^{(k)}), \quad J_{ij} = \frac{\partial F_i}{\partial x_j}$$

#### 11.4 Métodos Iterativos para Sistemas de Ecuaciones Lineales ($A\mathbf{x} = \mathbf{b}$)

- Método de Jacobi ($A = D + L + U$, con $D$ diagonal, $L$ triangular inferior estricta y $U$ triangular superior estricta):
  $$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \ne i} a_{ij}x_j^{(k)} \right)$$
  $$\mathbf{x}^{(k+1)} = -D^{-1}(L + U)\mathbf{x}^{(k)} + D^{-1}\mathbf{b}$$
- Método de Gauss-Seidel ($A = D + L + U$):
  $$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)} \right)$$
  $$\mathbf{x}^{(k+1)} = -(D + L)^{-1} U \mathbf{x}^{(k)} + (D + L)^{-1} \mathbf{b}$$
- Método de Sobrerrelajación Sucesiva (SOR, $0 < \omega < 2$):
  $$x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \frac{\omega}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)} \right)$$
- Criterio de Convergencia:
  $$|a_{ii}| > \sum_{j \ne i} |a_{ij}| \quad (\text{Diagonalmente dominante}) \quad \text{o} \quad \rho(T) < 1$$

#### 11.5 Interpolación y Ajuste de Curvas

- Polinomio Interpolador de Lagrange:
  $$P_n(x) = \sum_{i=0}^n y_i L_i(x), \quad L_i(x) = \prod_{j \ne i}^n \frac{x - x_j}{x_i - x_j}$$
- Polinomio de Newton en Diferencias Divididas:
  $$P_n(x) = f[x_0] + \sum_{k=1}^n f[x_0, x_1, \dots, x_k] \prod_{j=0}^{k-1} (x - x_j)$$
  $$f[x_i, x_{i+1}] = \frac{f[x_{i+1}] - f[x_i]}{x_{i+1} - x_i}$$
- Regresión Lineal por Mínimos Cuadrados ($y = a_0 + a_1 x$):
  $$a_1 = \frac{n \sum x_i y_i - \sum x_i \sum y_i}{n \sum x_i^2 - (\sum x_i)^2}, \quad a_0 = \bar{y} - a_1 \bar{x}$$

#### 11.6 Diferenciación e Integración Numérica

- Fórmulas de Diferenciación por Diferencias Finitas:
  $$f'(x) = \frac{f(x + h) - f(x)}{h} + O(h) \quad (\text{Hacia adelante})$$
  $$f'(x) = \frac{f(x) - f(x - h)}{h} + O(h) \quad (\text{Hacia atrás})$$
  $$f'(x) = \frac{f(x + h) - f(x - h)}{2h} + O(h^2) \quad (\text{Centrada})$$
  $$f''(x) = \frac{f(x + h) - 2f(x) + f(x - h)}{h^2} + O(h^2) \quad (\text{2da derivada centrada})$$
- Fórmulas de Integración de Newton-Cotes:
  $$\text{Regla del Trapecio Simple: } \int_a^b f(x) \, dx \approx \frac{b - a}{2}[f(a) + f(b)], \quad E = -\frac{h^3}{12}f''(\xi)$$
  $$\text{Regla del Trapecio Compuesta: } \int_a^b f(x) \, dx \approx \frac{h}{2}\left[ f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]$$
  $$\text{Regla de Simpson } 1/3 \text{ Simple: } \int_a^b f(x) \, dx \approx \frac{h}{3}[f(x_0) + 4f(x_1) + f(x_2)], \quad E = -\frac{h^5}{90}f^{(4)}(\xi)$$
  $$\text{Regla de Simpson } 1/3 \text{ Compuesta: } \int_a^b f(x) \, dx \approx \frac{h}{3}\left[ f(x_0) + 4\sum_{i=1,3,\dots}^{n-1} f(x_i) + 2\sum_{j=2,4,\dots}^{n-2} f(x_j) + f(x_n) \right]$$
  $$\text{Regla de Simpson } 3/8 \text{ Simple: } \int_a^b f(x) \, dx \approx \frac{3h}{8}[f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]$$
- Cuadratura Gaussiana (Gauss-Legendre en $[a, b]$ con transformación a $[-1, 1]$):
  $$\int_a^b f(x) \, dx \approx \frac{b - a}{2} \sum_{i=1}^n w_i f(x_i), \quad x_i = \frac{(b - a)t_i + (a + b)}{2} \quad (t_i, w_i \text{ nodos y pesos en } [-1, 1])$$

### Nivel Universitario / Avanzado

#### 11.7 Solución Numérica de EDOs (Problemas de Valor Inicial)

- Método de Euler (Explícito):
  $$y_{n+1} = y_n + h f(t_n, y_n) \quad (\text{Error local } O(h^2), \text{ global } O(h))$$
- Método de Euler Mejorado / Heun (Predictor-Corrector):
  $$y_{n+1}^* = y_n + h f(t_n, y_n), \quad y_{n+1} = y_n + \frac{h}{2}[f(t_n, y_n) + f(t_{n+1}, y_{n+1}^*)]$$
- Método de Runge-Kutta Clásico de 4° Orden (RK4):
  $$k_1 = f(t_n, y_n)$$
  $$k_2 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)$$
  $$k_3 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right)$$
  $$k_4 = f(t_n + h, y_n + hk_3)$$
  $$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4) \quad (\text{Error local } O(h^5), \text{ global } O(h^4))$$
- Métodos Multipaso (Adams-Bashforth / Adams-Moulton):
  $$\text{Adams-Bashforth (4 pasos): } y_{n+1} = y_n + \frac{h}{24}[55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3}]$$
  $$\text{Adams-Moulton (3 pasos): } y_{n+1} = y_n + \frac{h}{24}[9f_{n+1} + 19f_n - 5f_{n-1} + f_{n-2}]$$

#### 11.8 Solución Numérica de Problemas de Valor en la Frontera (PVF)

- Método de Disparo Lineal (Shooting Method):
  $$y(x) = u(x) + \frac{\beta - u(b)}{v(b)} v(x)$$
- Método de Diferencias Finitas para PVF:
  $$\frac{y_{i+1} - 2y_i + y_{i-1}}{h^2} = p(x_i)\frac{y_{i+1} - y_{i-1}}{2h} + q(x_i)y_i + r(x_i) \implies A\mathbf{y} = \mathbf{d}$$

#### 11.9 Solución Numérica de Ecuaciones Diferenciales Parciales (EDP)

- Diferencias Finitas para EDPs Elípticas (Laplace/Poisson 2D con $\Delta x = \Delta y = h$):
  $$u_{i+1, j} + u_{i-1, j} + u_{i, j+1} + u_{i, j-1} - 4u_{i, j} = h^2 f_{i, j}$$
- Diferencias Finitas para EDPs Parabólicas (Calor 1D: $u_t = \alpha u_{xx}$):
  $$\text{Esquema Explícito (FTCS): } u_i^{n+1} = u_i^n + r(u_{i+1}^n - 2u_i^n + u_{i-1}^n), \quad r = \frac{\alpha \Delta t}{(\Delta x)^2} \le \frac{1}{2}$$
  $$\text{Método de Crank-Nicolson: } -r u_{i-1}^{n+1} + 2(1 + r)u_i^{n+1} - r u_{i+1}^{n+1} = r u_{i-1}^n + 2(1 - r)u_i^n + r u_{i+1}^n$$
- Diferencias Finitas para EDPs Hiperbólicas (Onda 1D: $u_{tt} = c^2 u_{xx}$):
  $$u_i^{n+1} = 2(1 - C^2)u_i^n + C^2(u_{i+1}^n + u_{i-1}^n) - u_i^{n-1}$$
  $$\text{Condición CFL: } C = \frac{c \Delta t}{\Delta x} \le 1$$
