---
file: tests/README.md
description: Documentación y catálogo de la suite de pruebas unitarias automatizadas (Python pytest y Node.js).
type: doc/manual
version: 1.0.0
date: 2026-08-24
covers:
  - tests/test_ast.py
  - tests/test_parser.py
  - tests/test_syntax.py
  - tests/test_translator.py
  - tests/test_editor_widget.py
  - tests/test_theme.py
  - tests/test_mathjax_build.js
  - tests/test_mathjax_bundle.js
relations:
  - docs/ARCHITECTURE.md
  - AGENTS.md
keywords:
  - test-suite
  - pytest
  - node-test
  - qa-pipeline
---

# Pruebas Unitarias (`tests/`) 🧪

Este directorio contiene la batería de pruebas automatizadas (construidas con `pytest`) destinadas a garantizar la estabilidad, corrección y fiabilidad de los componentes principales de Traductor Mates.

## 1. Cobertura de las Pruebas

Los tests están diseñados para probar de manera robusta:
- **Casos Normales**: Flujos de uso estándar y predecibles por parte del usuario.
- **Casos de Límite (Edge Cases)**: Manejo de llaves de LaTeX sin cerrar, recuperación de errores y navegación al límite del árbol.
- **Renderizado y Parsing Difíciles**: Interpretación y generación de símbolos matemáticos poco frecuentes (ej. `leph`, `\infty`, `
abla`) y plantillas anidadas complejas (Límites, Derivadas Parciales y Matrices).

## 2. Descripción de Archivos

* **`test_ast.py`**: Pruebas para la manipulación y navegación del Árbol de Sintaxis Abstracta (`MathTree`), el manejo activo del cursor y la inserción de símbolos raros y plantillas.
* **`test_parser.py`**: Pruebas de análisis inverso desde texto LaTeX a objetos AST. Incluye evaluación de límites, derivadas, manejo seguro de errores sintácticos y reconstrucción de matrices complejas.
* **`test_syntax.py`**: Pruebas enfocadas en el coloreado de expresiones regulares léxicas.
* **`test_translator.py`**: Pruebas de la exportación a bloques Markdown (`$$`), Markdown en línea (`$`) y la canonización estructural (simplificación de `{base}_{sub}^{sup}`).
* **`test_editor_widget.py`**: Pruebas básicas sobre el componente gráfico.
* **`test_theme.py`**: Pruebas del generador de estilos QSS.
* **`test_mathjax_build.js`**: Pruebas unitarias nativas en JavaScript (`node:test`) para los submódulos de `mathjax_build` (`package_config.js`, `sanitizer.js`, `engine.js`, `renderer.js`, `index.js`).
* **`test_mathjax_bundle.js`**: Pruebas unitarias nativas en JavaScript (`node:test`) que validan la ejecución del bundle autónomo `mathjax_bundle.js` dentro de un contexto V8 / MiniRacer para múltiples categorías matemáticas y físicas.

## 3. Ejecución de las Pruebas

Para ejecutar las pruebas en Python con `pytest`:
```bash
pytest tests/
```

Para ejecutar las pruebas de JavaScript con el ejecutor nativo de Node.js:
```bash
node --test tests/*.js
```
