---
file: docs/mates/constantes/constantes.md
description: Catálogo de constantes matemáticas organizado por nivel didáctico y propiedades de irracionalidad/trascendencia.
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - src/data/constants.py
relations:
  - docs/fisica/constantes/constantes.md
  - docs/ARCHITECTURE.md
keywords:
  - constantes-matematicas
  - numeros-irracionales
  - numeros-trascendentes
  - constantes-geometricas
---

# Catalogo de constantes matematicas

Las constantes exactas se muestran mediante una definicion; los decimales son aproximaciones truncadas o redondeadas. La clasificacion distingue lo demostrado de lo que permanece abierto.

## 1. Nivel basico: geometria, aritmetica y calculo elemental

- **Pi ($\pi$):** $C/d=3.14159265358979323846264338327950\ldots$; real, irracional y trascendente.
- **Numero aureo ($\varphi$):** $(1+\sqrt5)/2=1.61803398874989484820458683436563\ldots$; algebraico de grado 2.
- **Proporcion de plata ($\delta_S$):** $1+\sqrt2=2.41421356237309504880168872420969\ldots$; algebraico de grado 2.
- **Constante de Pitagoras ($\sqrt2$):** diagonal de un cuadrado unitario, $x^2=2$; $1.41421356237309504880168872420969\ldots$.
- **Constante de Teodoro ($\sqrt3$):** diagonal de un rectangulo de lados $1$ y $\sqrt2$ (o diagonal espacial de un cubo unitario), $x^2=3$; $1.73205080756887729352744634150587\ldots$.
- **Base del logaritmo natural ($e$):** $\lim_{n\to\infty}(1+1/n)^n=\sum_{k=0}^\infty1/k!=2.71828182845904523536028747135266\ldots$; trascendente.

## 2. Nivel intermedio: analisis, numeros y combinatoria

- **Euler-Mascheroni ($\gamma$):** $\lim_{n\to\infty}(H_n-\ln n)=0.57721566490153286060651209008240\ldots$; su irracionalidad aun no esta demostrada.
- **Catalan ($G$):** $\beta(2)=\sum_{n=0}^\infty(-1)^n/(2n+1)^2=0.91596559417721901505460351493238\ldots$; irracionalidad no resuelta.
- **Apery ($\zeta(3)$):** $\sum_{n=1}^\infty n^{-3}=1.20205690315959428539973816151144\ldots$; irracional, trascendencia no demostrada.
- **Liouville ($c$):** $\sum_{n=1}^\infty 10^{-n!}=0.110001000000000000000001\ldots$; el primer numero trascendente construido explicitamente.
- **Gompertz ($\delta_G$):** $\int_0^\infty e^{-t}/(1+t)\,dt=-e\operatorname{Ei}(-1)=0.59634736232319407434107849936927\ldots$.
- **Glaisher-Kinkelin ($A$):** constante definida por la expansion asintotica del hiperfactorial, $1.28242712910062263687534256886979\ldots$; no se debe afirmar que su trascendencia esta demostrada.
- **Khinchin ($K_0$):** media geometrica de los cocientes de fracciones continuas para casi todo real, $2.68545200106530644530971483548179\ldots$; no se conoce su irracionalidad.
- **Meissel-Mertens ($M$):** $\lim_{x\to\infty}(\sum_{p\le x}1/p-\ln\ln x)=0.26149721284764278375542683860869\ldots$.
- **Brun para primos gemelos ($B_2$):** suma de los inversos de ambos primos de cada pareja gemela, aproximadamente $1.902160583104$; la cota depende del calculo numerico y no es un “rango analitico” de la constante.

## 3. Nivel avanzado: dinamica, algoritmos e informacion

- **Feigenbaum ($\delta$):** razon limite de intervalos sucesivos de duplicacion de periodo, $4.66920160910299067185320382046620\ldots$; universal para una clase de mapas, no “analiticamente exacta” en forma cerrada.
- **Feigenbaum ($\alpha$):** razon de escalas espaciales de atractores sucesivos, $2.50290787509589282228390287321821\ldots$; la convencion puede cambiar el signo.
- **Conway ($\lambda$):** crecimiento de *look-and-say*, $L_n\sim C\lambda^n$, $1.30357726903429639125709911215255\ldots$; algebraico de grado 71.
- **Golomb-Dickman ($\lambda_{GD}$):** fraccion esperada del ciclo mas largo de una permutacion aleatoria, $0.62432998854355087099293638310083\ldots$.
- **Chaitin ($\Omega_U$):** $\sum_{p\in\operatorname{dom}(U)}2^{-|p|}$, dependiente de la maquina universal $U$, no computable y aleatoria algoritmicamente. Un decimal atribuido a una “maquina estandar” no es universal y debe citar su construccion concreta.

### Cobertura didactica

- **Basico:** constantes geometricas y $e$, adecuadas para aritmetica, algebra, trigonometria y calculo inicial.
- **Intermedio:** $\gamma$, Catalan, $\zeta(3)$ y constantes de teoria de numeros, con series y limites convergentes.
- **Avanzado:** Feigenbaum, Conway, Golomb-Dickman y Chaitin, que requieren dinamica, asintotica, combinatoria o teoria de la computacion.
