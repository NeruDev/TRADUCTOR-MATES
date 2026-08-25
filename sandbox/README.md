---
file: sandbox/README.md
description: Guía y reglas del entorno aislado de pruebas temporales (sandbox) para desarrollo seguro.
type: doc/guide
version: 2.1.0
date: 2026-08-25
covers: []
relations:
  - AGENTS.md
  - docs/ARCHITECTURE.md
keywords:
  - sandbox
  - throwaway-scripts
  - testing-environment
  - temporary-tools
---

# Sandbox (Entorno de Pruebas) 🧪

Bienvenido al directorio `sandbox`. Este espacio está diseñado como un entorno seguro y aislado tanto para humanos como para asistentes de Inteligencia Artificial (Agentes) que trabajan en el desarrollo de *Traductor Mates*.

## Propósito del Directorio 🎯

1. **Pruebas Destructivas:** Realizar pruebas de scripts que requieran leer/escribir archivos temporales masivos, iterar sobre la estructura del proyecto o modificar datos sin comprometer la integridad del código fuente principal (`src/`).
2. **Prototipado (Agentes IA):** Proveer a la IA de una zona de trabajo pre-acordada donde pueda arrojar *scripts* de *throwaway* (de un solo uso), validadores temporales o *playgrounds* para testear algoritmos de parseo de LaTeX o WebEngine antes de integrarlos a producción.
3. **Mantenimiento Limpio:** Prevenir la acumulación de archivos `.py` residuales en la raíz del proyecto, garantizando que el árbol base se mantenga limpio y enfocado al despliegue.

## Reglas de Uso 📜

- **Archivos de un solo uso:** Cualquier script creado aquí debe ser considerado temporal.
- **GitIgnore:** Asegúrate de que los archivos generados en este directorio (a excepción de este README) estén excluidos de los *commits* principales si no aportan valor arquitectónico (opcional según el desarrollador).
- **No Importar a `src/`:** El código base en `src/` nunca debe depender ni importar módulos situados dentro de `sandbox/`.
