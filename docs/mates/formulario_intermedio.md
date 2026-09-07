---
file: docs/mates/formulario_intermedio.md
description: Compendio didáctico de fórmulas matemáticas de nivel intermedio (álgebra lineal, cálculo diferencial e integral).
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/symbols.py
relations:
  - docs/mates/formulario_mates.md
  - docs/fisica/formulario_intermedio.md
  - docs/ARCHITECTURE.md
keywords:
  - formulas-intermedias-mates
  - algebra-lineal
  - calculo-diferencial
  - calculo-integral
---
# Compendio I: Aritmética, Álgebra y Trigonometría

*(Nivel Intermedio)*

## 1. Aritmética

### 1.1 Teoría de Números Básica

- Algoritmo de la división (Euclides) (1):
  $$
  D = d \cdot q + r

  $$
- Algoritmo de la división (Euclides) (2):
  $$
  0 \le r < d

  $$
- Relación MCD y MCM:
  $$
  \operatorname{mcd}(a, b) \cdot \operatorname{mcm}(a, b) = |a \cdot b|

  $$

### 1.2 Progresiones Aritméticas (PA)

- Término general:
  $$
  a_n = a_1 + (n - 1)d

  $$
- Suma de los primeros $n$ términos:
  $$
  S_n = \frac{n}{2} (a_1 + a_n)

  $$

### 1.3 Progresiones Geométricas (PG)

- Término general:
  $$
  a_n = a_1 \cdot r^{n - 1}

  $$
- Suma de $n$ términos ($r \ne 1$):
  $$
  S_n = \frac{a_1 (1 - r^n)}{1 - r}

  $$
- Suma infinita ($|r| < 1$):
  $$
  S_\infty = \frac{a_1}{1 - r}

  $$

## 2. Álgebra

### 2.1 Ecuaciones Cuadráticas

- Forma general:
  $$
  ax^2 + bx + c = 0

  $$
- Fórmula cuadrática:
  $$
  x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}

  $$
- Discriminante ($\Delta$):
  $$
  \Delta = b^2 - 4ac

  $$
- Relaciones de Cardano-Vieta ($2^\circ \text{ grado}$) (1):
  $$
  x_1 + x_2 = -\frac{b}{a}

  $$
- Relaciones de Cardano-Vieta ($2^\circ \text{ grado}$) (2):
  $$
  x_1 \cdot x_2 = \frac{c}{a}

  $$

### 2.2 Logaritmos

- Definición ($b > 0, b \ne 1, x > 0$):
  $$
  \log_b(x) = y \iff b^y = x

  $$
- Logaritmo de un producto:
  $$
  \log_b(x \cdot y) = \log_b(x) + \log_b(y)

  $$
- Logaritmo de un cociente:
  $$
  \log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)

  $$
- Logaritmo de una potencia:
  $$
  \log_b(x^k) = k \cdot \log_b(x)

  $$
- Cambio de base:
  $$
  \log_b(x) = \frac{\log_c(x)}{\log_c(b)}

  $$

### 2.3 Teorema del Binomio (Newton)

- Expansión binomial:
  $$
  (a + b)^n = \sum_{k=0}^n \binom{n}{k} a^{n - k} b^k = \sum_{k=0}^n \frac{n!}{k!(n - k)!} a^{n - k} b^k

  $$

## 3. Trigonometría

### 3.1 Fórmulas de Suma y Diferencia de Ángulos

- Seno de suma y diferencia:
  $$
  \sin(\alpha \pm \beta) = \sin(\alpha)\cos(\beta) \pm \cos(\alpha)\sin(\beta)

  $$
- Coseno de suma y diferencia:
  $$
  \cos(\alpha \pm \beta) = \cos(\alpha)\cos(\beta) \mp \sin(\alpha)\sin(\beta)

  $$
- Tangente de suma y diferencia:
  $$
  \tan(\alpha \pm \beta) = \frac{\tan(\alpha) \pm \tan(\beta)}{1 \mp \tan(\alpha)\tan(\beta)}

  $$

### 3.2 Ángulo Doble y Ángulo Mitad

- Seno del ángulo doble:
  $$
  \sin(2\theta) = 2\sin(\theta)\cos(\theta)

  $$
- Coseno del ángulo doble:
  $$
  \cos(2\theta) = \cos^2(\theta) - \sin^2(\theta) = 2\cos^2(\theta) - 1 = 1 - 2\sin^2(\theta)

  $$
- Tangente del ángulo doble:
  $$
  \tan(2\theta) = \frac{2\tan(\theta)}{1 - \tan^2(\theta)}

  $$
- Seno:
  $$
  \sin\left(\frac{\theta}{2}\right) = \pm \sqrt{\frac{1 - \cos(\theta)}{2}}

  $$
- Coseno del ángulo mitad:
  $$
  \cos\left(\frac{\theta}{2}\right) = \pm \sqrt{\frac{1 + \cos(\theta)}{2}}

  $$
- Tangente del ángulo mitad:
  $$
  \tan\left(\frac{\theta}{2}\right) = \frac{\sin(\theta)}{1 + \cos(\theta)} = \frac{1 - \cos(\theta)}{\sin(\theta)}

  $$

### 3.3 Leyes de Triángulos Oblicuángulos

- Ley de Senos ($R = \mathrm{circunradio}$):
  $$
  \frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)} = 2R

  $$
- Ley de Cosenos:
  $$
  a^2 = b^2 + c^2 - 2bc \cos(A)

  $$
- Área de un triángulo:
  $$
  \mathrm{Área} = \frac{1}{2} a b \sin(C)

  $$
- Fórmula de Herón ($s = \frac{a + b + c}{2}$):
  $$
  \mathrm{Área} = \sqrt{s(s - a)(s - b)(s - c)}

  $$

### 3.4 Transformaciones de Suma a Producto (Fórmulas de Prostaféresis)

- Suma y resta de senos:
  $$
  \sin(\alpha) \pm \sin(\beta) = 2 \sin\left(\frac{\alpha \pm \beta}{2}\right) \cos\left(\frac{\alpha \mp \beta}{2}\right)

  $$
- Suma de cosenos:
  $$
  \cos(\alpha) + \cos(\beta) = 2 \cos\left(\frac{\alpha + \beta}{2}\right) \cos\left(\frac{\alpha - \beta}{2}\right)

  $$
- Resta de cosenos:
  $$
  \cos(\alpha) - \cos(\beta) = -2 \sin\left(\frac{\alpha + \beta}{2}\right) \sin\left(\frac{\alpha - \beta}{2}\right)

  $$

### 3.5 Transformaciones de Producto a Suma

- Producto seno-coseno:
  $$
  2\sin(\alpha)\cos(\beta) = \sin(\alpha + \beta) + \sin(\alpha - \beta)

  $$
- Producto coseno-coseno:
  $$
  2\cos(\alpha)\cos(\beta) = \cos(\alpha + \beta) + \cos(\alpha - \beta)

  $$
- Producto seno-seno:
  $$
  2\sin(\alpha)\sin(\beta) = \cos(\alpha - \beta) - \cos(\alpha + \beta)

  $$

# Compendio II: Geometría, Geometría Analítica y Álgebra Lineal

*(Nivel Intermedio)*

## 4. Geometría (Plana y del Espacio / Euclidiana)

### 4.1 Geometría del Espacio (Áreas y Volúmenes 3D)

- Prisma Recto (1):
  $$
  A_L = P_{\mathrm{base}} \cdot h

  $$
- Prisma Recto (2):
  $$
  V = A_{\mathrm{base}} \cdot h

  $$
- Cilindro Circular Recto (1):
  $$
  A_T = 2\pi r(h + r)

  $$
- Cilindro Circular Recto (2):
  $$
  V = \pi r^2 h

  $$
- Pirámide:
  $$
  V = \frac{1}{3} A_{\mathrm{base}} \cdot h

  $$
- Cono Circular Recto (1):
  $$
  g = \sqrt{r^2 + h^2}

  $$
- Cono Circular Recto (2):
  $$
  A_T = \pi r(g + r)

  $$
- Cono Circular Recto (3):
  $$
  V = \frac{1}{3} \pi r^2 h

  $$
- Tronco de Cono:
  $$
  V = \frac{1}{3} \pi h (R^2 + r^2 + R \cdot r)

  $$
- Esfera (1):
  $$
  A = 4\pi r^2

  $$
- Esfera (2):
  $$
  V = \frac{4}{3} \pi r^3

  $$
- Casquete Esférico (1):
  $$
  A = 2\pi r h

  $$
- Casquete Esférico (2):
  $$
  V = \frac{1}{3} \pi h^2 (3r - h)

  $$

### 4.2 Teoremas Métricos y Proporcionalidad

- Teorema de Tales (Rectas paralelas $L_1 \parallel L_2 \parallel L_3$ cortadas por transversales en $A, B, C$ y $D, E, F$):
  $$
  \frac{AB}{BC} = \frac{DE}{EF} \iff \frac{AB}{AC} = \frac{DE}{DF}

  $$
- Teorema de la Bisectriz Interior:
  $$
  \frac{a}{b} = \frac{c_1}{c_2}

  $$
- Relaciones Métricas en el Triángulo Rectángulo (1):
  $$
  h^2 = m \cdot n

  $$
- Relaciones Métricas en el Triángulo Rectángulo (2):
  $$
  a^2 = c \cdot m

  $$
- Relaciones Métricas en el Triángulo Rectángulo (3):
  $$
  b^2 = c \cdot n

  $$
- Relaciones Métricas en el Triángulo Rectángulo (4):
  $$
  a \cdot b = c \cdot h

  $$
- Potencia de un Punto $P$ respecto a una circunferencia (1):
  $$
  PA \cdot PB = PC \cdot PD \quad (\text{Secantes})

  $$
- Potencia de un Punto $P$ respecto a una circunferencia (2):
  $$
  PT^2 = PA \cdot PB \quad (\text{Tangente y secante})

  $$
- Teorema de Ceva (Cevianas concurrentes):
  $$
  \frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1

  $$
- Teorema de Menelao (Puntos $D, E, F$ sobre las rectas de los lados de un $\triangle ABC$ son colineales) (1):
  $$
  \frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = -1 \quad (\text{Razones dirigidas})

  $$
- Teorema de Menelao (Puntos $D, E, F$ sobre las rectas de los lados de un $\triangle ABC$ son colineales) (2):
  $$
  \left( \text{En magnitudes no dirigidas: } \frac{|AF|}{|FB|} \cdot \frac{|BD|}{|DC|} \cdot \frac{|CE|}{|EA|} = 1 \text{ con 1 o 3 puntos en las prolongaciones exteriores} \right)

  $$

## 5. Geometría Analítica

### 5.1 Distancias y Secciones Cónicas en 2D

- Distancia de un punto $P(x_0, y_0)$ a una recta $Ax + By + C = 0$:
  $$
  d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}

  $$

### 5.2 Circunferencia

- Ecuación Ordinaria (Centro $(h, k)$, Radio $r$):
  $$
  (x - h)^2 + (y - k)^2 = r^2

  $$
- Ecuación General:
  $$
  x^2 + y^2 + Dx + Ey + F = 0

  $$

### 5.3 Parábola

- Eje focal horizontal (1):
  $$
  (y - k)^2 = \pm 4p(x - h) \quad | \quad \mathrm{Foco: } (h \pm p, k) \quad |

  $$
- Eje focal horizontal (2):
  $$
  \mathrm{Directriz: } x = h \mp p

  $$
- Eje focal vertical (1):
  $$
  (x - h)^2 = \pm 4p(y - k) \quad | \quad \mathrm{Foco: } (h, k \pm p) \quad |

  $$
- Eje focal vertical (2):
  $$
  \mathrm{Directriz: } y = k \mp p

  $$
- Longitud del Lado Recto:
  $$
  LR = |4p|

  $$

### 5.4 Elipse

- Ecuación Ordinaria (Eje focal horizontal, $a > b$):
  $$
  \frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1

  $$
- Relación fundamental:
  $$
  a^2 = b^2 + c^2

  $$
- Excentricidad ($0 < e < 1$):
  $$
  e = \frac{c}{a}

  $$
- Longitud del Lado Recto:
  $$
  LR = \frac{2b^2}{a}

  $$

### 5.5 Hipérbola

- Ecuación Ordinaria (Eje transversal horizontal):
  $$
  \frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1

  $$
- Relación fundamental:
  $$
  c^2 = a^2 + b^2

  $$
- Excentricidad ($e > 1$):
  $$
  e = \frac{c}{a}

  $$
- Asíntotas (Centro en $(h,k)$):
  $$
  y - k = \pm \frac{b}{a}(x - h)

  $$

### 5.6 Ecuación General de Segundo Grado en 2D

- Forma general:
  $$
  Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0

  $$
- Discriminante ($\delta$):
  $$
  \Delta = B^2 - 4AC

  $$
- Clasificación cónica (1):
  $$
  \Delta < 0 \implies \mathrm{Tipo Elíptico (Elipse, Circunferencia)}

  $$
- Clasificación cónica (2):
  $$
  \Delta = 0 \implies \mathrm{Tipo Parabólico (Parábola, Rectas paralelas)}

  $$
- Clasificación cónica (3):
  $$
  \Delta > 0 \implies \mathrm{Tipo Hiperbólico (Hipérbola, Rectas secantes)}

  $$
- Ángulo de rotación de ejes para eliminar el término $Bxy$:
  $$
  \cot(2\theta) = \frac{A - C}{B}

  $$

### 5.7 Sistemas de Coordenadas Alternativos

- Coseno:
  $$
  x = r\cos(\theta)

  $$
- Seno:
  $$
  y = r\sin(\theta)

  $$
- Cartesianas a Polares (1):
  $$
  r = \sqrt{x^2 + y^2}

  $$
- Cartesianas a Polares (2):
  $$
  \theta = \operatorname{atan2}(y, x) \in (-\pi, \pi]

  $$

## 6. Álgebra Lineal

### 6.1 Álgebra de Matrices

- Multiplicación de Matrices:
  $$
  (AB)_{ij} = \sum_{k=1}^m A_{ik} B_{kj}

  $$
- Transposición:
  $$
  (AB)^T = B^T A^T

  $$
- Traza:
  $$
  \operatorname{Tr}(A) = \sum_{i=1}^n A_{ii}

  $$
- Propiedad cíclica:
  $$
  \operatorname{Tr}(AB) = \operatorname{Tr}(BA)

  $$
- Determinante (Propiedades) (1):
  $$
  \det(AB) = \det(A)\det(B)

  $$
- Determinante (Propiedades) (2):
  $$
  \det(A^T) = \det(A)

  $$
- Determinante (Propiedades) (3):
  $$
  \det(A^{-1}) = \frac{1}{\det(A)}

  $$
- Determinante (Propiedades) (4):
  $$
  \det(cA) = c^n \det(A)

  $$

### 6.2 Espacios Vectoriales

- Subespacios (Criterio de cerradura):
  $$
  \mathbf{0} \in W \quad \mathbf{u} + \mathbf{v} \in W \quad c\mathbf{u} \in W

  $$
- Dependencia Lineal:
  $$
  \sum_{i=1}^k c_i \mathbf{v}_i = \mathbf{0} \quad (\mathrm{con algún } c_i \ne 0)

  $$
- Teorema del Rango-Nulidad:
  $$
  \dim(\operatorname{Nuc}(T)) + \dim(\operatorname{Im}(T)) = \dim(V) \iff \operatorname{nulidad}(A) + \operatorname{rango}(A) = n

  $$

### 6.3 Espacios con Producto Interno y Ortogonalidad

- Desigualdad de Cauchy-Schwarz:
  $$
  |\langle \mathbf{u}, \mathbf{v} \rangle| \le \|\mathbf{u}\| \|\mathbf{v}\|

  $$
- Desigualdad Triangular:
  $$
  \|\mathbf{u} + \mathbf{v}\| \le \|\mathbf{u}\| + \|\mathbf{v}\|

  $$
- Proyección Ortogonal de $\mathbf{u}$ sobre $\mathbf{v}$:
  $$
  \operatorname{Proy}_{\mathbf{v}}(\mathbf{u}) = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{v}\|^2} \mathbf{v}

  $$
- Proceso de Ortogonalización de Gram-Schmidt (1):
  $$
  \mathbf{u}_1 = \mathbf{v}_1

  $$
- Proceso de Ortogonalización de Gram-Schmidt (2):
  $$
  \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \operatorname{Proy}_{\mathbf{u}_j}(\mathbf{v}_k)

  $$
- Proceso de Ortogonalización de Gram-Schmidt (3):
  $$
  \mathbf{e}_i = \frac{\mathbf{u}_i}{\|\mathbf{u}_i\|} \quad (\mathrm{Normalización})

  $$

# Compendio III: Cálculo Diferencial, Integral y Vectorial

*(Nivel Intermedio)*

## 7. Cálculo Diferencial

### 7.1 Reglas Fundamentales de Derivación

- Regla del Producto:
  $$
  \frac{d}{dx}[f(x) \cdot g(x)] = f'(x)g(x) + f(x)g'(x)

  $$
- Regla del Cociente:
  $$
  \frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}

  $$
- Regla de la Cadena:
  $$
  \frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x) \iff \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}

  $$

### 7.2 Derivadas de Funciones Trascendentes Elementales

- Exponenciales (1):
  $$
  \frac{d}{dx}(e^x) = e^x

  $$
- Exponenciales (2):
  $$
  \frac{d}{dx}(a^x) = a^x \ln(a) \quad (a > 0, a \ne 1)

  $$
- Logarítmicas (1):
  $$
  \frac{d}{dx}(\ln|x|) = \frac{1}{x}

  $$
- Logarítmicas (2):
  $$
  \frac{d}{dx}(\log_a|x|) = \frac{1}{x\ln(a)}

  $$
- Derivada de Seno:
  $$
  \frac{d}{dx}[\sin(x)] = \cos(x)

  $$
- Derivada de Coseno:
  $$
  \frac{d}{dx}[\cos(x)] = -\sin(x)

  $$
- Derivada de Tangente:
  $$
  \frac{d}{dx}[\tan(x)] = \sec^2(x)

  $$
- Derivada de Cosecante:
  $$
  \frac{d}{dx}[\cot(x)] = -\csc^2(x)

  $$
- Derivada de Tangente:
  $$
  \frac{d}{dx}[\sec(x)] = \sec(x)\tan(x)

  $$
- Derivada de Cosecante:
  $$
  \frac{d}{dx}[\csc(x)] = -\csc(x)\cot(x)

  $$
- Derivada de Arcoseno:
  $$
  \frac{d}{dx}[\arcsin(x)] = \frac{1}{\sqrt{1 - x^2}}

  $$
- Derivada de Arcocoseno:
  $$
  \frac{d}{dx}[\arccos(x)] = -\frac{1}{\sqrt{1 - x^2}}

  $$
- Derivada de Arcotangente:
  $$
  \frac{d}{dx}[\arctan(x)] = \frac{1}{1 + x^2}

  $$
- Derivada de Arcocotangente:
  $$
  \frac{d}{dx}[\operatorname{arccot}(x)] = -\frac{1}{1 + x^2}

  $$
- Derivada de Arcosecante:
  $$
  \frac{d}{dx}[\operatorname{arcsec}(x)] = \frac{1}{|x|\sqrt{x^2 - 1}}

  $$
- Derivada de Arcocosecante:
  $$
  \frac{d}{dx}[\operatorname{arccsc}(x)] = -\frac{1}{|x|\sqrt{x^2 - 1}}

  $$

### 7.3 Aplicaciones y Teoremas del Cálculo Diferencial

- Recta Tangente en $(x_0, y_0)$:
  $$
  y - y_0 = f'(x_0)(x - x_0)

  $$
- Recta Normal en $(x_0, y_0)$ ($f'(x_0) \ne 0$):
  $$
  y - y_0 = -\frac{1}{f'(x_0)}(x - x_0)

  $$
- Regla de L'Hôpital ($f, g$ derivables, $g'(x) \ne 0$ cerca de $a$, indeterminación $0/0$ o $\pm\infty/\pm\infty$, y existe el límite de $f'/g'$):
  $$
  \lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}

  $$
- Teorema de Rolle ($f$ continua en $[a, b]$, derivable en $(a, b)$ y $f(a) = f(b)$):
  $$
  \exists c \in (a, b) : f'(c) = 0

  $$
- Teorema del Valor Medio (Lagrange, $f$ continua en $[a, b]$ y derivable en $(a, b)$):
  $$
  \exists c \in (a, b) : f'(c) = \frac{f(b) - f(a)}{b - a}

  $$
- Teorema del Valor Medio Generalizado (Cauchy, $f, g$ continuas en $[a, b]$, derivables en $(a, b)$ y $g'(x) \ne 0$ en $(a, b)$):
  $$
  \exists c \in (a, b) : \frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}

  $$

## 8. Cálculo Integral

### 8.1 Teorema Fundamental del Cálculo (TFC)

- Parte 1 (Derivada de la integral):
  $$
  \frac{d}{dx} \left[ \int_a^x f(t) \, dt \right] = f(x)

  $$
- Regla de Leibniz (1D):
  $$
  \frac{d}{dx} \left[ \int_{u(x)}^{v(x)} f(t) \, dt \right] = f(v(x))v'(x) - f(u(x))u'(x)

  $$
- Parte 2 (Regla de Barrow):
  $$
  \int_a^b f(x) \, dx = F(b) - F(a) = [F(x)]_a^b

  $$

### 8.2 Técnicas / Métodos de Integración

- Cambio de Variable / Sustitución ($u = g(x)$):
  $$
  \int f(g(x))g'(x) \, dx = \int f(u) \, du

  $$
- Integración por Partes:
  $$
  \int u \, dv = u v - \int v \, du

  $$
- Seno:
  $$
  \mathrm{Para } \sqrt{a^2 - x^2} \implies x = a\sin(\theta)

  $$
- Coseno:
  $$
  dx = a\cos(\theta) d\theta

  $$
- Coseno:
  $$
  \sqrt{a^2 - x^2} = a\cos(\theta)

  $$
- Tangente:
  $$
  \mathrm{Para } \sqrt{a^2 + x^2} \implies x = a\tan(\theta)

  $$
- Secante:
  $$
  dx = a\sec^2(\theta) d\theta

  $$
- Secante:
  $$
  \sqrt{a^2 + x^2} = a\sec(\theta)

  $$
- Secante:
  $$
  \mathrm{Para } \sqrt{x^2 - a^2} \implies x = a\sec(\theta)

  $$
- Tangente:
  $$
  dx = a\sec(\theta)\tan(\theta) d\theta

  $$
- Tangente:
  $$
  \sqrt{x^2 - a^2} = a\tan(\theta)

  $$

### 8.3 Integrales Trigonométricas e Inversas Clave

- Tangente:
  $$
  \int \tan(x) \, dx = \ln|\sec(x)| + C = -\ln|\cos(x)| + C

  $$
- Cotangente:
  $$
  \int \cot(x) \, dx = \ln|\sin(x)| + C

  $$
- Secante:
  $$
  \int \sec(x) \, dx = \ln|\sec(x) + \tan(x)| + C

  $$
- Cosecante:
  $$
  \int \csc(x) \, dx = -\ln|\csc(x) + \cot(x)| + C = \ln|\csc(x) - \cot(x)| + C

  $$
- Integral de Arcotangente:
  $$
  \int \frac{1}{x^2 + a^2} \, dx = \frac{1}{a} \arctan\left(\frac{x}{a}\right) + C

  $$
- Integral de Arcoseno:
  $$
  \int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \arcsin\left(\frac{x}{a}\right) + C

  $$
- Integral de Arcosecante:
  $$
  \int \frac{1}{|x|\sqrt{x^2 - a^2}} \, dx = \frac{1}{a} \operatorname{arcsec}\left(\frac{|x|}{a}\right) + C

  $$
- Racionales y de Radicales (4):
  $$
  \int \frac{1}{x^2 - a^2} \, dx = \frac{1}{2a} \ln\left|\frac{x - a}{x + a}\right| + C

  $$

### 8.4 Aplicaciones Geométricas y Físicas

- Área entre curvas:
  $$
  A = \int_a^b |f(x) - g(x)| \, dx

  $$
- Longitud de Arco:
  $$
  L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx

  $$
- Volumen de Revolución (Método de Discos):
  $$
  V = \pi \int_a^b [f(x)]^2 \, dx

  $$
- Volumen de Revolución (Método de Arandelas):
  $$
  V = \pi \int_a^b ([R(x)]^2 - [r(x)]^2) \, dx

  $$
- Volumen de Revolución (Método de Cascarones / Capas):
  $$
  V = 2\pi \int_a^b x f(x) \, dx

  $$
- Área de Superficie de Revolución:
  $$
  S = 2\pi \int_a^b f(x) \sqrt{1 + [f'(x)]^2} \, dx

  $$
- Valor Medio de una Función:
  $$
  f_{\mathrm{prom}} = \frac{1}{b - a} \int_a^b f(x) \, dx

  $$

## 9. Cálculo Vectorial y Multivariable

### 9.1 Diferenciabilidad y Regla de la Cadena Multivariable

- Diferencial Total:
  $$
  df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz

  $$
- Regla de la Cadena ($w = f(x, y)$, con $x = x(t)$, $y = y(t)$):
  $$
  \frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt}

  $$

### 9.2 Derivada Direccional y Planos Tangentes

- Derivada de Coseno:
  $$
  D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = \|\nabla f\|\cos(\theta)

  $$
- Derivada Direccional (en dirección del vector unitario $\mathbf{u}$) (2):
  $$
  (\mathrm{Dirección de máximo crecimiento} = \nabla f;

  $$
- Derivada Direccional (en dirección del vector unitario $\mathbf{u}$) (3):
  $$
  \mathrm{Valor máximo} = \|\nabla f\|)

  $$
- Plano Tangente a superficie de nivel $F(x, y, z) = c$ en $P_0(x_0, y_0, z_0)$:
  $$
  \nabla F(P_0) \cdot (\mathbf{r} - \mathbf{r}_0) = 0 \implies F_x(P_0)(x - x_0) + F_y(P_0)(y - y_0) + F_z(P_0)(z - z_0) = 0

  $$

### 9.3 Optimización Multivariable

- Matriz hessiana (2d):
  $$
  H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix}

  $$
- Discriminante ($d$):
  $$
  D = \det(H) = f_{xx} f_{yy} - (f_{xy})^2

  $$
- Criterio de clasificación (1):
  $$
  D > 0 \mathrm{ y } f_{xx} > 0 \implies \mathrm{Mínimo Local}

  $$
- Criterio de clasificación (2):
  $$
  D > 0 \mathrm{ y } f_{xx} < 0 \implies \mathrm{Máximo Local}

  $$
- Criterio de clasificación (3):
  $$
  D < 0 \implies \mathrm{Punto de Silla}

  $$
- Criterio de clasificación (4):
  $$
  D = 0 \implies \mathrm{Criterio no concluyente}

  $$
- Multiplicadores de Lagrange (Restricción $g(x,y,z) = k$):
  $$
  \nabla f = \lambda \nabla g

  $$

### 9.4 Integrales Múltiples y Transformaciones de Coordenadas

- Integral Doble General:
  $$
  \iint_R f(x, y) \, dx \, dy = \iint_S f(x(u,v), y(u,v)) |J(u, v)| \, du \, dv

  $$
- Jacobiano de Transformación:
  $$
  J(u, v) = \frac{\partial(x, y)}{\partial(u, v)} = \det\begin{pmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{pmatrix}

  $$
- Coordenadas Polares (2D):
  $$
  dA = r \, dr \, d\theta

  $$
- Coordenadas Cilíndricas (3D):
  $$
  dV = r \, dr \, d\theta \, dz

  $$
- Coordenadas Esféricas (3D):
  $$
  dV = \rho^2 \sin(\varphi) \, d\rho \, d\varphi \, d\theta

  $$

# Compendio IV: Ecuaciones Diferenciales y Métodos Numéricos

*(Nivel Intermedio)*

## 10. Ecuaciones Diferenciales

### 10.1 Ecuaciones Diferenciales Reducibles a 1er Orden

- Ecuación Homogénea de Grado $n$ (1):
  $$
  \frac{dy}{dx} = F\left(\frac{y}{x}\right) \implies y = ux

  $$
- Ecuación Homogénea de Grado $n$ (2):
  $$
  \frac{dy}{dx} = u + x\frac{du}{dx}

  $$
- Ecuación de bernoulli ($n \ne 0:
  $$
  y' + P(x)y = Q(x)y^n

  $$
- 1$):
  $$
  u = y^{1 - n} \implies u' + (1 - n)P(x)u = (1 - n)Q(x)

  $$
- Ecuación de Riccati (Con solución particular conocida $y_1(x)$) (1):
  $$
  y' = P(x) + Q(x)y + R(x)y^2

  $$
- Ecuación de Riccati (Con solución particular conocida $y_1(x)$) (2):
  $$
  y = y_1(x) + \frac{1}{u(x)}

  $$
- Ecuación de Clairaut:
  $$
  y = x y' + f(y') \implies y = Cx + f(C) \quad (\mathrm{Solución general})

  $$

### 10.2 EDOs Lineales de Orden Superior con Coeficientes Constantes

- Forma General Homogénea:
  $$
  a_n y^{(n)} + a_{n-1} y^{(n-1)} + \dots + a_1 y' + a_0 y = 0

  $$
- Ecuación Característica ($2^\circ \mathrm{ orden}$) (1):
  $$
  a r^2 + b r + c = 0

  $$
- Ecuación Característica ($2^\circ \mathrm{ orden}$) (2):
  $$
  \mathrm{Raíces reales distintas } (r_1 \ne r_2):

  $$
- Ecuación Característica ($2^\circ \mathrm{ orden}$) (3):
  $$
  y_h = c_1 e^{r_1 x} + c_2 e^{r_2 x}

  $$
- Ecuación Característica ($2^\circ \mathrm{ orden}$) (4):
  $$
  \mathrm{Raíces reales repetidas } (r_1 = r_2 = r):

  $$
- Ecuación Característica ($2^\circ \mathrm{ orden}$) (5):
  $$
  y_h = (c_1 + c_2 x)e^{r x}

  $$
- Ecuación Característica ($2^\circ \mathrm{ orden}$) (6):
  $$
  \mathrm{Raíces complejas } (r = \alpha \pm i\beta):

  $$
- Seno:
  $$
  y_h = e^{\alpha x}(c_1 \cos(\beta x) + c_2 \sin(\beta x))

  $$
- Wronskiano e Independencia Lineal:
  $$
  W(y_1, y_2, \dots, y_n) = \det\begin{pmatrix} y_1 & y_2 & \dots & y_n \\ y_1' & y_2' & \dots & y_n' \\ \vdots & \vdots & \ddots & \vdots \\ y_1^{(n-1)} & y_2^{(n-1)} & \dots & y_n^{(n-1)} \end{pmatrix} \ne 0

  $$
- Fórmula de Abel para el Wronskiano:
  $$
  W(x) = W(x_0) e^{-\int P(x) \, dx}

  $$
- Método de Variación de Parámetros ($y'' + P(x)y' + Q(x)y = g(x)$) (1):
  $$
  y_p = u_1(x)y_1(x) + u_2(x)y_2(x)

  $$
- Método de Variación de Parámetros ($y'' + P(x)y' + Q(x)y = g(x)$) (2):
  $$
  u_1'(x) = -\frac{y_2(x) g(x)}{W(y_1, y_2)}

  $$
- Método de Variación de Parámetros ($y'' + P(x)y' + Q(x)y = g(x)$) (3):
  $$
  u_2'(x) = \frac{y_1(x) g(x)}{W(y_1, y_2)}

  $$
- Ecuación Equidimensional de Cauchy-Euler:
  $$
  a x^2 y'' + b x y' + c y = 0 \implies a r(r - 1) + b r + c = a r^2 + (b - a)r + c = 0

  $$

### 10.3 Transformada de Laplace para EDOs

- Definición:
  $$
  \mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st} f(t) \, dt

  $$
- Transformadas de Derivadas (1):
  $$
  \mathcal{L}\{f'(t)\} = s F(s) - f(0)

  $$
- Transformadas de Derivadas (2):
  $$
  \mathcal{L}\{f''(t)\} = s^2 F(s) - s f(0) - f'(0)

  $$
- Transformadas de Derivadas (3):
  $$
  \mathcal{L}\{f^{(n)}(t)\} = s^n F(s) - \sum_{k=1}^n s^{n - k} f^{(k - 1)}(0)

  $$
- Teoremas de Traslación (1):
  $$
  \mathcal{L}\{e^{at} f(t)\} = F(s - a)

  $$
- Teoremas de Traslación (2):
  $$
  \mathcal{L}\{f(t - a)\mathcal{U}(t - a)\} = e^{-as} F(s) \quad (\mathcal{U} = \mathrm{escalón unitario de Heaviside})

  $$
- Transformada de la Convolución:
  $$
  \mathcal{L}\{(f * g)(t)\} = \mathcal{L}\left\{ \int_0^t f(\tau)g(t - \tau) \, d\tau \right\} = F(s) \cdot G(s)

  $$
- Transformada de la Delta de Dirac (1):
  $$
  \mathcal{L}\{\delta(t - t_0)\} = e^{-s t_0}

  $$
- Transformada de la Delta de Dirac (2):
  $$
  \mathcal{L}\{\delta(t)\} = 1

  $$

## 11. Métodos Numéricos

### 11.1 Raíces de Ecuaciones No Lineales (Métodos Abiertos)

- Método de Iteración de Punto Fijo ($g([a, b]) \subseteq [a, b]$ y $\max_{x \in [a, b]} |g'(x)| \le k < 1$) (1):
  $$
  f(x) = 0 \iff x = g(x)

  $$
- Método de Iteración de Punto Fijo ($g([a, b]) \subseteq [a, b]$ y $\max_{x \in [a, b]} |g'(x)| \le k < 1$) (2):
  $$
  x_{k+1} = g(x_k)

  $$
- Método de Iteración de Punto Fijo ($g([a, b]) \subseteq [a, b]$ y $\max_{x \in [a, b]} |g'(x)| \le k < 1$) (3):
  $$
  |x_{k+1} - x^*| \le k |x_k - x^*|

  $$
- Método de Newton-Raphson (Orden cuadrático $p = 2$):
  $$
  x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}

  $$
- Método de la Secante (Orden superlineal $p \approx 1.618$):
  $$
  x_{k+1} = x_k - f(x_k)\frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}

  $$
- Método de Newton-Raphson Multivariable ($\mathbf{F}(\mathbf{x}) = \mathbf{0}$) (1):
  $$
  \mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} - [J(\mathbf{x}^{(k)})]^{-1}\mathbf{F}(\mathbf{x}^{(k)})

  $$
- Método de Newton-Raphson Multivariable ($\mathbf{F}(\mathbf{x}) = \mathbf{0}$) (2):
  $$
  J_{ij} = \frac{\partial F_i}{\partial x_j}

  $$

### 11.2 Métodos Iterativos para Sistemas de Ecuaciones Lineales ($A\mathbf{x} = \mathbf{b}$)

- Método de Jacobi ($A = D + L + U$, con $D$ diagonal, $L$ triangular inferior estricta y $U$ triangular superior estricta) (1):
  $$
  x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \ne i} a_{ij}x_j^{(k)} \right)

  $$
- Método de Jacobi ($A = D + L + U$, con $D$ diagonal, $L$ triangular inferior estricta y $U$ triangular superior estricta) (2):
  $$
  \mathbf{x}^{(k+1)} = -D^{-1}(L + U)\mathbf{x}^{(k)} + D^{-1}\mathbf{b}

  $$
- Método de Gauss-Seidel ($A = D + L + U$) (1):
  $$
  x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)} \right)

  $$
- Método de Gauss-Seidel ($A = D + L + U$) (2):
  $$
  \mathbf{x}^{(k+1)} = -(D + L)^{-1} U \mathbf{x}^{(k)} + (D + L)^{-1} \mathbf{b}

  $$
- Método de Sobrerrelajación Sucesiva (SOR, $0 < \omega < 2$):
  $$
  x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \frac{\omega}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)} \right)

  $$
- Criterio de Convergencia (1):
  $$
  |a_{ii}| > \sum_{j \ne i} |a_{ij}| \quad (\mathrm{Diagonalmente dominante}) \quad \mathrm{o}

  $$
- Criterio de Convergencia (2):
  $$
  \rho(T) < 1

  $$

### 11.3 Interpolación y Ajuste de Curvas

- Polinomio Interpolador de Lagrange (1):
  $$
  P_n(x) = \sum_{i=0}^n y_i L_i(x)

  $$
- Polinomio Interpolador de Lagrange (2):
  $$
  L_i(x) = \prod_{j \ne i}^n \frac{x - x_j}{x_i - x_j}

  $$
- Polinomio de Newton en Diferencias Divididas (1):
  $$
  P_n(x) = f[x_0] + \sum_{k=1}^n f[x_0, x_1, \dots, x_k] \prod_{j=0}^{k-1} (x - x_j)

  $$
- Polinomio de Newton en Diferencias Divididas (2):
  $$
  f[x_i, x_{i+1}] = \frac{f[x_{i+1}] - f[x_i]}{x_{i+1} - x_i}

  $$
- Regresión Lineal por Mínimos Cuadrados ($y = a_0 + a_1 x$) (1):
  $$
  a_1 = \frac{n \sum x_i y_i - \sum x_i \sum y_i}{n \sum x_i^2 - (\sum x_i)^2}

  $$
- Regresión Lineal por Mínimos Cuadrados ($y = a_0 + a_1 x$) (2):
  $$
  a_0 = \bar{y} - a_1 \bar{x}

  $$

### 11.4 Diferenciación e Integración Numérica

- Fórmulas de Diferenciación por Diferencias Finitas (1):
  $$
  f'(x) = \frac{f(x + h) - f(x)}{h} + O(h) \quad (\mathrm{Hacia adelante})

  $$
- Fórmulas de Diferenciación por Diferencias Finitas (2):
  $$
  f'(x) = \frac{f(x) - f(x - h)}{h} + O(h) \quad (\mathrm{Hacia atrás})

  $$
- Fórmulas de Diferenciación por Diferencias Finitas (3):
  $$
  f'(x) = \frac{f(x + h) - f(x - h)}{2h} + O(h^2) \quad (\mathrm{Centrada})

  $$
- Fórmulas de Diferenciación por Diferencias Finitas (4):
  $$
  f''(x) = \frac{f(x + h) - 2f(x) + f(x - h)}{h^2} + O(h^2) \quad (\mathrm{2da derivada centrada})

  $$
- Fórmulas de Integración de Newton-Cotes (1):
  $$
  \mathrm{Regla del Trapecio Simple: } \int_a^b f(x) \, dx \approx \frac{b - a}{2}[f(a) + f(b)]

  $$
- Fórmulas de Integración de Newton-Cotes (2):
  $$
  E = -\frac{h^3}{12}f''(\xi)

  $$
- Fórmulas de Integración de Newton-Cotes (3):
  $$
  \mathrm{Regla del Trapecio Compuesta: } \int_a^b f(x) \, dx \approx \frac{h}{2}\left[ f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]

  $$
- Fórmulas de Integración de Newton-Cotes (4):
  $$
  \mathrm{Regla de Simpson } 1/3 \mathrm{ Simple: } \int_a^b f(x) \, dx \approx \frac{h}{3}[f(x_0) + 4f(x_1) + f(x_2)]

  $$
- Fórmulas de Integración de Newton-Cotes (5):
  $$
  E = -\frac{h^5}{90}f^{(4)}(\xi)

  $$
- Fórmulas de Integración de Newton-Cotes (6):
  $$
  \mathrm{Regla de Simpson } 1/3 \mathrm{ Compuesta: } \int_a^b f(x) \, dx \approx \frac{h}{3}\left[ f(x_0) + 4\sum_{i=1,3,\dots}^{n-1} f(x_i) + 2\sum_{j=2,4,\dots}^{n-2} f(x_j) + f(x_n) \right]

  $$
- Fórmulas de Integración de Newton-Cotes (7):
  $$
  \mathrm{Regla de Simpson } 3/8 \mathrm{ Simple: } \int_a^b f(x) \, dx \approx \frac{3h}{8}[f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]

  $$
- Cuadratura Gaussiana (Gauss-Legendre en $[a, b]$ con transformación a $[-1, 1]$) (1):
  $$
  \int_a^b f(x) \, dx \approx \frac{b - a}{2} \sum_{i=1}^n w_i f(x_i)

  $$
- Cuadratura Gaussiana (Gauss-Legendre en $[a, b]$ con transformación a $[-1, 1]$) (2):
  $$
  x_i = \frac{(b - a)t_i + (a + b)}{2} \quad (t_i, w_i \mathrm{ nodos y pesos en } [-1, 1])

  $$
