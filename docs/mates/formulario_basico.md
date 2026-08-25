---
file: docs/mates/formulario_basico.md
description: Compendio didáctico de fórmulas matemáticas de nivel básico (aritmética, álgebra elemental, trigonometría).
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/symbols.py
relations:
  - docs/mates/formulario_mates.md
  - docs/fisica/formulario_basico.md
  - docs/ARCHITECTURE.md
keywords:
  - formulas-basicas-mates
  - aritmetica-basica
  - algebra-elemental
  - trigonometria-basica
---

# Compendio I: Aritmética, Álgebra y Trigonometría
*(Nivel Básico)*

## 1. Aritmética

### 1.1 Propiedades de la Adición y Multiplicación

- Clausura / Cerradura (Adición):
  $$
  \forall a, b \in \mathbb{R}: \quad a + b \in \mathbb{R}
  $$
- Clausura / Cerradura (Multiplicación):
  $$
  \forall a, b \in \mathbb{R}: \quad a \cdot b \in \mathbb{R}
  $$
- Conmutativa (Adición):
  $$
  a + b = b + a
  $$
- Conmutativa (Multiplicación):
  $$
  a \cdot b = b \cdot a
  $$
- Asociativa (Adición):
  $$
  (a + b) + c = a + (b + c)
  $$
- Asociativa (Multiplicación):
  $$
  (a \cdot b) \cdot c = a \cdot (b \cdot c)
  $$
- Elemento Neutro (Adición):
  $$
  a + 0 = a
  $$
- Elemento Neutro (Multiplicación):
  $$
  a \cdot 1 = a
  $$
- Elemento Inverso (Adición):
  $$
  a + (-a) = 0
  $$
- Elemento Inverso (Multiplicación):
  $$
  a \cdot \left(\frac{1}{a}\right) = 1 \quad (a \ne 0)
  $$
- Distributiva:
  $$
  a \cdot (b + c) = a \cdot b + a \cdot c
  $$
### 1.2 Operaciones con Fracciones

- Suma/Resta con mismo denominador:
  $$
  \frac{a}{c} \pm \frac{b}{c} = \frac{a \pm b}{c} \quad (c \ne 0)
  $$
- Suma/Resta con distinto denominador:
  $$
  \frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd} \quad (b, d \ne 0)
  $$
- Multiplicación:
  $$
  \frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d} \quad (b, d \ne 0)
  $$
- División:
  $$
  \frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a \cdot d}{b \cdot c} \quad (b, c, d \ne 0)
  $$
### 1.3 Porcentajes y Proporcionalidad

- Tanto por ciento ($P = \mathrm{porcentaje}$, $C = \mathrm{cantidad}$, $r = \mathrm{tasa}$):
  $$
  P = \frac{C \cdot r}{100}
  $$
- Regla de tres simple directa ($\frac{a}{b} = \frac{c}{x}$):
  $$
  x = \frac{b \cdot c}{a}
  $$
## 2. Álgebra

### 2.1 Leyes de Exponentes y Radicales

- Multiplicación de bases iguales:
  $$
  x^a \cdot x^b = x^{a + b}
  $$
- División de bases iguales:
  $$
  \frac{x^a}{x^b} = x^{a - b}
  $$
- Potencia de una potencia:
  $$
  (x^a)^b = x^{a \cdot b}
  $$
- Potencia de un producto:
  $$
  (x \cdot y)^a = x^a \cdot y^a
  $$
- Exponente negativo ($x \ne 0$):
  $$
  x^{-a} = \frac{1}{x^a}
  $$
- Exponente fraccionario:
  $$
  x^{\frac{a}{b}} = \sqrt[b]{x^a}
  $$
- Raíz de un producto:
  $$
  \sqrt[n]{x \cdot y} = \sqrt[n]{x} \cdot \sqrt[n]{y}
  $$
### 2.2 Productos Notables y Factorización

- Binomio al cuadrado:
  $$
  (a \pm b)^2 = a^2 \pm 2ab + b^2
  $$
- Diferencia de cuadrados:
  $$
  a^2 - b^2 = (a + b)(a - b)
  $$
- Binomio al cubo:
  $$
  (a \pm b)^3 = a^3 \pm 3a^2b + 3ab^2 \pm b^3
  $$
- Suma de cubos:
  $$
  a^3 + b^3 = (a + b)(a^2 - ab + b^2)
  $$
- Diferencia de cubos:
  $$
  a^3 - b^3 = (a - b)(a^2 + ab + b^2)
  $$
- Trinomio al cuadrado:
  $$
  (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + ac + bc)
  $$
### 2.3 Ecuaciones Lineales

- Forma general ($a \ne 0$):
  $$
  ax + b = 0 \implies x = -\frac{b}{a}
  $$
## 3. Trigonometría

### 3.1 Razones Trigonométricas en el Triángulo Rectángulo

- Seno:
  $$
  \sin(\theta) = \frac{\mathrm{Cateto Opuesto}}{\mathrm{Hipotenusa}}
  $$
- Coseno:
  $$
  \cos(\theta) = \frac{\mathrm{Cateto Adyacente}}{\mathrm{Hipotenusa}}
  $$
- Tangente:
  $$
  \tan(\theta) = \frac{\mathrm{Cateto Opuesto}}{\mathrm{Cateto Adyacente}}
  $$
- Cosecante:
  $$
  \csc(\theta) = \frac{\mathrm{Hipotenusa}}{\mathrm{Cateto Opuesto}} = \frac{1}{\sin(\theta)}
  $$
- Secante:
  $$
  \sec(\theta) = \frac{\mathrm{Hipotenusa}}{\mathrm{Cateto Adyacente}} = \frac{1}{\cos(\theta)}
  $$
- Cotangente:
  $$
  \cot(\theta) = \frac{\mathrm{Cateto Adyacente}}{\mathrm{Cateto Opuesto}} = \frac{1}{\tan(\theta)}
  $$
### 3.2 Identidades Trigonométricas Fundamentales

- Tangente por cociente:
  $$
  \tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}
  $$
- Cotangente por cociente:
  $$
  \cot(\theta) = \frac{\cos(\theta)}{\sin(\theta)}
  $$
- Identidad Pitagórica principal:
  $$
  \sin^2(\theta) + \cos^2(\theta) = 1
  $$
- Identidad Pitagórica (Tangente y Secante):
  $$
  1 + \tan^2(\theta) = \sec^2(\theta)
  $$
- Identidad Pitagórica (Cotangente y Cosecante):
  $$
  1 + \cot^2(\theta) = \csc^2(\theta)
  $$
# Compendio II: Geometría, Geometría Analítica y Álgebra Lineal
*(Nivel Básico)*

## 4. Geometría (Plana y del Espacio / Euclidiana)

### 4.1 Perímetros y Áreas de Figuras Planas (2D)

- Perímetro de Triángulo (General):
  $$
  P = a + b + c
  $$
- Área de Triángulo (General):
  $$
  A = \frac{b \cdot h}{2}
  $$
- Área de Triángulo Equilátero:
  $$
  A = \frac{\sqrt{3}}{4} l^2
  $$
- Altura de Triángulo Equilátero:
  $$
  h = \frac{\sqrt{3}}{2} l
  $$
- Perímetro de Cuadrado:
  $$
  P = 4l
  $$
- Área de Cuadrado:
  $$
  A = l^2 = \frac{d^2}{2}
  $$
- Perímetro de Rectángulo:
  $$
  P = 2(b + h)
  $$
- Área de Rectángulo:
  $$
  A = b \cdot h
  $$
- Paralelogramo:
  $$
  A = b \cdot h
  $$
- Perímetro de Rombo:
  $$
  P = 4l
  $$
- Área de Rombo:
  $$
  A = \frac{D \cdot d}{2}
  $$
- Trapecio:
  $$
  A = \frac{(B + b) \cdot h}{2}
  $$
- Perímetro de Polígono Regular ($n$ lados):
  $$
  P = n \cdot l
  $$
- Área de Polígono Regular ($n$ lados):
  $$
  A = \frac{P \cdot a_p}{2}
  $$
- Circunferencia de Círculo:
  $$
  C = 2\pi r
  $$
- Área de Círculo:
  $$
  A = \pi r^2
  $$
- Longitud de Arco de Sector Circular:
  $$
  s = r\theta \quad (\theta \mathrm{ en rad})
  $$
- Área de Sector Circular:
  $$
  A = \frac{1}{2} r^2 \theta \quad (\theta \mathrm{ en rad})
  $$
- Corona Circular:
  $$
  A = \pi(R^2 - r^2)
  $$
### 4.2 Propiedades Angulares y Polígonos

- Teorema de Pitágoras (Triángulos rectángulos):
  $$
  a^2 + b^2 = c^2
  $$
- Suma de ángulos internos de un triángulo:
  $$
  \alpha + \beta + \gamma = 180^\circ \quad (\mathrm{o } \pi\mathrm{ rad})
  $$
- Suma de ángulos internos de un polígono de $n$ lados:
  $$
  S_{\mathrm{int}} = (n - 2) \cdot 180^\circ
  $$
- Ángulo interior de un polígono regular:
  $$
  \theta_{\mathrm{int}} = \frac{(n - 2) \cdot 180^\circ}{n}
  $$
- Número total de diagonales en un polígono:
  $$
  N_d = \frac{n(n - 3)}{2}
  $$
## 5. Geometría Analítica

### 5.1 Plano Cartesiano (2D)

- Distancia entre dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$:
  $$
  d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
  $$
- Punto medio $M$:
  $$
  M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)
  $$
- Coordenada x en división de segmento en una razón $r$ ($\frac{AP}{PB} = r$):
  $$
  x = \frac{x_1 + r x_2}{1 + r}
  $$
- Coordenada y en división de segmento en una razón $r$ ($\frac{AP}{PB} = r$):
  $$
  y = \frac{y_1 + r y_2}{1 + r}
  $$
### 5.2 La Línea Recta en 2D

- Pendiente:
  $$
  m = \frac{y_2 - y_1}{x_2 - x_1} = \tan(\theta)
  $$
- Ecuación Punto-Pendiente:
  $$
  y - y_1 = m(x - x_1)
  $$
- Ecuación Pendiente-Ordenada al origen:
  $$
  y = mx + b
  $$
- Ecuación General ($B \ne 0 \implies m = -\frac{A}{B}$):
  $$
  Ax + By + C = 0
  $$
- Ecuación Simétrica / Canónica:
  $$
  \frac{x}{a} + \frac{y}{b} = 1 \quad (\mathrm{Intersecciones en } (a,0) \mathrm{ y } (0,b))
  $$
- Rectas Paralelas:
  $$
  m_1 = m_2
  $$
- Rectas Perpendiculares:
  $$
  m_1 \cdot m_2 = -1 \iff m_1 = -\frac{1}{m_2}
  $$
- Ángulo entre dos rectas:
  $$
  \tan(\theta) = \left|\frac{m_2 - m_1}{1 + m_1 \cdot m_2}\right|
  $$
## 6. Álgebra Lineal

### 6.1 Vectores en $\mathbb{R}^n$

- Suma:
  $$
  \mathbf{u} + \mathbf{v} = (u_1 + v_1, u_2 + v_2, \dots, u_n + v_n)
  $$
- Producto Escalar por Vector:
  $$
  c\mathbf{u} = (cu_1, cu_2, \dots, cu_n)
  $$
- Norma / Módulo Euclidiano ($L_2$):
  $$
  \|\mathbf{u}\| = \sqrt{u_1^2 + u_2^2 + \dots + u_n^2} = \sqrt{\mathbf{u} \cdot \mathbf{u}}
  $$
- Vector Unitario:
  $$
  \hat{\mathbf{u}} = \frac{\mathbf{u}}{\|\mathbf{u}\|}
  $$
### 6.2 Productos Vectoriales

- Producto Punto (Escalar):
  $$
  \mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos(\theta)
  $$
- Ortogonalidad:
  $$
  \mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0
  $$
- Producto Cruz (Vectorial en $\mathbb{R}^3$):
  $$
  \mathbf{u} \times \mathbf{v} = \det\begin{pmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{pmatrix}
  $$
- Magnitud del Producto Cruz:
  $$
  \|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\| \|\mathbf{v}\| \sin(\theta)
  $$
- Producto Triple Escalar (Volumen del paralelepípedo):
  $$
  [\mathbf{u}, \mathbf{v}, \mathbf{w}] = \mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \det\begin{pmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{pmatrix}
  $$
### 6.3 Sistemas de Ecuaciones Lineales

- Sistema Matricial:
  $$
  A\mathbf{x} = \mathbf{b}
  $$
- Regla de Cramer ($\det(A) \ne 0$):
  $$
  x_i = \frac{\det(A_i)}{\det(A)}
  $$
# Compendio III: Cálculo Diferencial, Integral y Vectorial
*(Nivel Básico)*

## 7. Cálculo Diferencial

### 7.1 Definición de Límite y Continuidad

- Definición épsilon-delta:
  $$
  \lim_{x \to a} f(x) = L \iff \forall \varepsilon > 0, \, \exists \delta > 0 : 0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon
  $$
- Continuidad en un punto $a$:
  $$
  \lim_{x \to a} f(x) = f(a)
  $$
### 7.2 Definición Formal de la Derivada

- Por límite (Cociente diferencial):
  $$
  f'(x) = \frac{dy}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
  $$
- En un punto $a$:
  $$
  f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}
  $$
### 7.3 Reglas y Derivadas Algebraicas Elementales

- Constante:
  $$
  \frac{d}{dx}(c) = 0
  $$
- Identidad:
  $$
  \frac{d}{dx}(x) = 1
  $$
- Regla de la Potencia:
  $$
  \frac{d}{dx}(x^n) = n x^{n - 1}
  $$
- Múltiplo Constante:
  $$
  \frac{d}{dx}[c \cdot f(x)] = c f'(x)
  $$
- Suma y Resta:
  $$
  \frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)
  $$
- Raíz cuadrada:
  $$
  \frac{d}{dx}(\sqrt{x}) = \frac{1}{2\sqrt{x}}
  $$
- Inverso:
  $$
  \frac{d}{dx}\left(\frac{1}{x}\right) = -\frac{1}{x^2}
  $$
## 8. Cálculo Integral

### 8.1 Definición y Propiedades Fundamentales

- Antiderivada:
  $$
  \int f(x) \, dx = F(x) + C \iff F'(x) = f(x)
  $$
- Linealidad:
  $$
  \int [a f(x) + b g(x)] \, dx = a \int f(x) \, dx + b \int g(x) \, dx
  $$
### 8.2 Integrales Indefinidas Elementales / Inmediatas

- Potencias ($n \ne -1$):
  $$
  \int x^n \, dx = \frac{x^{n+1}}{n+1} + C
  $$
- Logarítmica:
  $$
  \int \frac{1}{x} \, dx = \ln|x| + C
  $$
- Integral de exponencial natural:
  $$
  \int e^x \, dx = e^x + C
  $$
- Integral de exponencial general:
  $$
  \int a^x \, dx = \frac{a^x}{\ln(a)} + C
  $$
- Integral de Seno:
  $$
  \int \sin(x) \, dx = -\cos(x) + C
  $$
- Integral de Coseno:
  $$
  \int \cos(x) \, dx = \sin(x) + C
  $$
- Integral de Secante cuadrada:
  $$
  \int \sec^2(x) \, dx = \tan(x) + C
  $$
- Integral de Cosecante cuadrada:
  $$
  \int \csc^2(x) \, dx = -\cot(x) + C
  $$
- Integral de Secante por Tangente:
  $$
  \int \sec(x)\tan(x) \, dx = \sec(x) + C
  $$
- Integral de Cosecante por Cotangente:
  $$
  \int \csc(x)\cot(x) \, dx = -\csc(x) + C
  $$
## 9. Cálculo Vectorial y Multivariable

### 9.1 Curvas Paramétricas y Funciones Vectoriales en $\mathbb{R}^3$

- Vector de Posición:
  $$
  \mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}
  $$
- Velocidad:
  $$
  \mathbf{v}(t) = \mathbf{r}'(t) = x'(t)\mathbf{i} + y'(t)\mathbf{j} + z'(t)\mathbf{k}
  $$
- Rapidez:
  $$
  \|\mathbf{v}(t)\| = \frac{ds}{dt} = \sqrt{[x'(t)]^2 + [y'(t)]^2 + [z'(t)]^2}
  $$
- Aceleración:
  $$
  \mathbf{a}(t) = \mathbf{r}''(t) = \mathbf{v}'(t)
  $$
### 9.2 Derivadas Parciales de Funciones Escalares $f(x, y, z)$

- Derivada parcial respecto a $x$:
  $$
  \frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x + h, y, z) - f(x, y, z)}{h}
  $$
- Teorema de Schwarz / Clairaut (Derivadas cruzadas):
  $$
  \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}
  $$
### 9.3 Gradiente

- Vector Gradiente:
  $$
  \nabla f = \operatorname{grad}(f) = \frac{\partial f}{\partial x}\mathbf{i} + \frac{\partial f}{\partial y}\mathbf{j} + \frac{\partial f}{\partial z}\mathbf{k}
  $$
# Compendio IV: Ecuaciones Diferenciales y Métodos Numéricos
*(Nivel Básico)*

## 10. Ecuaciones Diferenciales

### 10.1 Definiciones y Clasificación

- Problema de Valor Inicial (PVI) (1):
  $$
  y' = f(x, y)
  $$
- Problema de Valor Inicial (PVI) (2):
  $$
  y(x_0) = y_0
  $$
- Teorema de Existencia:
  $$
  y' = f(x, y)
  $$
- Unicidad de Picard-Lindelöf:
  $$
  y(x_0) = y_0 \implies \exists ! \, y(x) \quad \mathrm{en } I
  $$
### 10.2 Ecuaciones Diferenciales Ordinarias (EDO) de 1er Orden Elementales

- Variables Separables:
  $$
  g(y) \, dy = f(x) \, dx \implies \int g(y) \, dy = \int f(x) \, dx + C
  $$
- Forma estándar de Ecuación Lineal de 1er Orden:
  $$
  y' + P(x)y = Q(x)
  $$
- Factor Integrante de Leibniz:
  $$
  \mu(x) = e^{\int P(x) \, dx}
  $$
- Solución de Ecuación Lineal de 1er Orden:
  $$
  y(x) = \frac{1}{\mu(x)} \left[ \int \mu(x) Q(x) \, dx + C \right]
  $$
- Forma de Ecuación Diferencial Exacta:
  $$
  M(x, y) \, dx + N(x, y) \, dy = 0
  $$
- Condición y Solución de Ecuación Exacta:
  $$
  \frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \implies \Psi(x, y) = C
  $$
- Factor Integrante (dependiente de x) para Ecuaciones no Exactas:
  $$
  \mu(x) = e^{\int \frac{M_y - N_x}{N} \, dx}
  $$
- Factor Integrante (dependiente de y) para Ecuaciones no Exactas:
  $$
  \mu(y) = e^{\int \frac{N_x - M_y}{M} \, dy}
  $$
## 11. Métodos Numéricos

### 11.1 Teoría de Errores

- Error Absoluto:
  $$
  E_a = |x - \hat{x}|
  $$
- Error Relativo:
  $$
  E_r = \frac{|x - \hat{x}|}{|x|} \quad (x \ne 0)
  $$
- Error Relativo Porcentual:
  $$
  E_p = E_r \cdot 100\%
  $$
- Error Aproximado:
  $$
  \varepsilon_a = \left|\frac{x_{\mathrm{actual}} - x_{\mathrm{anterior}}}{x_{\mathrm{actual}}}\right| \cdot 100\%
  $$
### 11.2 Raíces de Ecuaciones No Lineales (Métodos de Intervalo / Cerrados)

- Teorema de Bolzano:
  $$
  f(a) \cdot f(b) < 0 \implies \exists c \in (a, b) : f(c) = 0
  $$
- Punto medio en Método de Bisección:
  $$
  c_n = \frac{a_n + b_n}{2}
  $$
- Cota de Error en Método de Bisección:
  $$
  E_n = |r - c_n| \le \frac{b - a}{2^{n+1}}
  $$
- Número de iteraciones en Método de Bisección:
  $$
  n \ge \left\lceil \log_2\left(\frac{b - a}{2\varepsilon}\right) \right\rceil
  $$
- Método de Falsa Posición (Regula Falsi):
  $$
  c = b - \frac{f(b)(a - b)}{f(a) - f(b)} = \frac{a f(b) - b f(a)}{f(b) - f(a)}
  $$
