---
file: README.md
description: Manual de uso general, características y guía de inicio rápido de Traductor Mates.
type: doc/guide
version: 1.0.0
date: 2026-08-24
covers:
  - main.py
  - src/ui/main_window.py
relations:
  - docs/ARCHITECTURE.md
  - AGENTS.md
keywords:
  - traductor-mates
  - math-editor
  - latex-translator
  - hatsune-miku-theme
---

# Traductor Mates 🧮

Traductor Mates es una aplicación de escritorio diseñada para escribir ecuaciones matemáticas y físicas complejas de forma visual e intuitiva y traducirlas instantáneamente a código LaTeX y Markdown. Con una estética minimalista inspirada en **Hatsune Miku** (Cyan `#39C5BB` / Magenta `#E3327B`) y **Material 3**, combina la potencia de Microsoft Word Equations con la versatilidad de Wolfram Alpha.

## Características Principales ✨

- **Editor Estructural Interactivo**: Escribe ecuaciones mediante casillas visuales anidadas `[ □ ]` utilizando un árbol AST bidimensional en vez de texto plano.
- **Formulario Compendio de Matemáticas y Física**: Explora fórmulas organizadas por rama (📐 Matemáticas / ⚛️ Física), niveles (Básico, Intermedio, Avanzado), acordeones colapsables y carrusel de variantes (`< >`).
- **Pestaña de Usuario y Demostraciones Paso a Paso**: Guarda y edita tus propias fórmulas y deducciones con renderizado SVG en vivo, clasificación jerárquica y gestión de múltiples variantes.
- **Buscador Global Inteligente**: Filtra dinámicamente y en tiempo real cualquier plantilla, símbolo, fórmula preestablecida, constante física o unidad matemática desde un único campo de búsqueda.
- **Catálogos Especializados de Constantes y Unidades**: Acceso a constantes oficiales CODATA 2022 y tablas completas de magnitudes del SI e ingeniería con selector de decimales de precisión.
- **Traducción Multilenguaje Simultánea**: Traduce el AST en vivo a código LaTeX y bloques Markdown con selector de escala tipográfica (Word style).
- **Vista Previa HD y Exportación Vectorial**: Renderizado de alta resolución offline mediante motor síncrono optimizado de MathJax y MiniRacer V8 con zoom adaptativo y exportación en formato PNG (raster) y SVG (vectorial puro).
- **Guía de Usuario Integrada**: Manual de uso completo y accesible directamente desde el botón `❓ Ayuda` en la barra superior.

## Requisitos del Sistema 💻

- **Python**: 3.10 o superior (Recomendado 3.14+).
- **Node.js**: 18 o superior (para ejecución de pruebas JS y compilación con `esbuild`).
- **Gestor de paquetes**: `pyproject.toml` (Estándar PEP 621 / Setuptools).
- **Dependencias principales**:
  - `PySide6` (Interfaz gráfica y Event Loop Qt6)
  - `py_mini_racer` (Motor V8 embebido para compilación síncrona LaTeX a SVG)
  - `pyperclip` (Gestor de portapapeles multiplataforma)
  - `pytest` (Suite de pruebas unitarias Python)

Se recomienda el uso de un entorno virtual `.venv` activado para aislar los paquetes de Python. Para instalar el proyecto en modo editable o instalar dependencias desde `pyproject.toml`:
```powershell
pip install -e .
```

## Ejecución del Proyecto 🚀

Para lanzar la aplicación mediante el archivo principal [`main.py`](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/main.py), asegúrate de tener el entorno virtual configurado y activado.

### Usando el script de inicio (Recomendado)
El proyecto contiene un archivo `run_app.bat` configurado para ejecutar la aplicación sin invocar ventanas de consola bloqueantes. 

**Opción 1: Ejecución completa (Ruta Relativa desde consola general)**
```powershell
& "G:\REPOSITORIOS GITHUB\TRADUCTOR MATES\run_app.bat"
```

**Opción 2: Ejecución corta (Estando dentro del repositorio)**
```powershell
.\run_app.bat
```

> **Nota para PowerShell:** Si tienes problemas de políticas de ejecución, puedes permitir el proceso localmente usando:
> `(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; .\run_app.bat`

### Ejecución Manual vía Python
Si deseas depurar la app viendo las salidas por consola:
```powershell
.\.venv\Scripts\Activate.ps1
python main.py
```
*(Para evitar la consola remanente en Windows, usa `pythonw main.py`).*

## Estructura de Desarrollo 📂

- [`main.py`](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/main.py): Punto de entrada ejecutable principal de la aplicación.
- [`src/`](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/): Código fuente modular (motor AST, traductores, renderizador SVG y componentes UI PySide6).
- [`mathjax_build/`](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/mathjax_build/): Arquitectura modular del compilador JavaScript de MathJax (esbuild).
- [`tests/`](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/tests/): Batería completa de pruebas unitarias para Python (Pytest) y JavaScript (Node.js).
- [`docs/`](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/docs/): Documentación arquitectónica y estructura de directorios en JSON, JSONC y YAML.
- [`MEMORY.md`](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/MEMORY.md): Registro de contexto histórico y decisiones técnicas del equipo.
- [`PROGRESS.md`](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/PROGRESS.md): Registro de avance incremental y diario de trabajo en segundos.

## Calidad de Código y Pruebas (QA Pipeline) 🛡️

El proyecto implementa una integración continua local mediante una suite unificada de linters, tipado estricto y pruebas unitarias:

**En Windows:**
```powershell
.\run_qa.bat
```

**En Linux / macOS:**
```bash
./run_qa.sh
```

Este proceso evalúa el código en 5 compuertas de calidad:
1. **Ruff**: Analiza y formatea sintaxis, errores y PEP-8.
2. **Pydoclint**: Valida que se respete el estándar de documentación **Google Style Docstrings** (`Args:`, `Returns:`, `Attributes:`).
3. **Mypy**: Valida estáticamente los *type hints* para garantizar tipado estricto y robusto.
4. **Pytest**: Ejecuta las 42 pruebas unitarias de Python del árbol AST, parser inverso y traductores.
5. **Node.js (node:test)**: Ejecuta las 38 pruebas unitarias de JavaScript validando los submódulos de `mathjax_build` y la ejecución del bundle en contexto VM V8.
