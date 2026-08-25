---
file: MEMORY.md
description: Registro histórico de decisiones, aciertos, soluciones y contexto acumulado del proyecto
author: Equipo Traductor Mates
version: 1.0.0
type: documentation/history
relations:
  - AGENTS.md
  - PROGRESS.md
  - PROCESS.md
---

# Registro de Memoria (MEMORY.md)

## Sesión: Estándar y Plantillas de Metadatos YAML Frontmatter (2026-08-24 22:10)

- **[2026-08-25 00:36] Directiva de Despliegue en `AGENTS.md` y Consolidación de Commit Único v1.0.0:**
  1) Se incorporó en la Sección 2 de `AGENTS.md` la directiva obligatoria de actualizar e incluir `MEMORY.md` y `PROGRESS.md` antes de cualquier envío a repositorio remoto (`git push`), garantizando commits atómicos y coherentes.
  2) Se configuraron los datos de autoría en Git (`user.name "NeruDev"` y `user.email "LedKutchi@gmail.com"`).
  3) Se vinculó el origen remoto `origin` a `https://github.com/NeruDev/TRADUCTOR-MATES.git`.
  4) Se resolvió el conflicto con el `README.md` remoto inicial sobreescribiéndolo con el `README.md` canónico v1.0.0 local como único archivo en la raíz.
  5) Se consolidaron todos los cambios en un único commit atómico de lanzamiento v1.0.0 en `main` y `origin/main`.

- **[2026-08-25 00:20] Normalización de Versión Oficial v1.0.0 y Limpieza de Historial Git:**
  1) Se creó y ejecutó el script `sandbox/update_version_to_1_0_0.py` para sincronizar el metadato `version: 1.0.0` y `__version__ = "1.0.0"` en el 100% de los archivos del repositorio (Python, Markdown, JavaScript, Batch scripts, TOML).
  2) Se recompiló `src/assets/mathjax_bundle.js` mediante `node mathjax_build/build.js` verificando el banner estructurado.
  3) Se reseteó el historial de Git a una rama huérfana limpia (`git checkout --orphan`) creando el commit canónico de lanzamiento v1.0.0.
  4) Se ejecutó y aprobó la suite de calidad con `run_qa.bat` al 100% (5/5 compuertas: Ruff OK, Pydoclint 0 violaciones en 37 archivos, Mypy 0 errores de tipado, Pytest 43/43 pasados, Node.js 40/40 pasados).

- **[2026-08-25 00:16] Auditoría Global del Repositorio y Blindaje de `.gitignore`:**
  1) Se verificó que todos los paquetes (`src/core`, `src/ui`, `src/data`, `src/utils`, `src/assets`, `mathjax_build`, `tests`, `docs`) operan sin código obsoleto ni dependencias muertas.
  2) Se blindó `.gitignore` agregando `.ruff_cache/`, `.mypy_cache/`, artefactos de build/distribución (`build/`, `dist/`, `*.egg-info/`), patrones de recuperación y sesiones (`session.log`, `*.tmp`, `*.bak`, `.traductor_mates_*`) y reglas completas de exclusión para `sandbox/` preservando sus archivos README.
  3) Se añadió frontmatter YAML a `sandbox/README.md` conforme a `docs/base/frontmatter_yaml.md`.
  4) Se ejecutó y aprobó la suite de calidad con `run_qa.bat` al 100% (5/5 compuertas: Ruff OK, Pydoclint 0 violaciones en 37 archivos, Mypy 0 errores de tipado, Pytest 43/43 pasados, Node.js 40/40 pasados).

- **[2026-08-25 00:11] Limpieza de Código Obsoleto y Sincronización Arquitectónica:**
  1) Se eliminó el directorio inactivo `src/assets/katex/` (~930 archivos, ~2 MB) y el archivo no utilizado `src/assets/katex_preview.html`, saneando el paquete `src/assets/` a su único bundle activo `mathjax_bundle.js`.
  2) Se eliminó la clase muerta `WebBridge` e imports no utilizados en `src/ui/components/svg_cache.py`.
  3) Se actualizaron las especificaciones arquitectónicas en `src/ui/main_window.py`, `src/README.md`, `README.md`, `docs/ARCHITECTURE.md`, `docs/base/frontmatter_yaml.md`, `docs/directorios_comentados.jsonc` y se regeneró `docs/directorios.json`.
  4) Se ejecutó y aprobó la suite de calidad con `run_qa.bat` al 100% (5/5 compuertas: Ruff OK, Pydoclint 0 violaciones en 37 archivos, Mypy 0 errores de tipado, Pytest 43/43 pasados, Node.js 40/40 pasados).

- **[2026-08-25 00:01] Aplicación de Estándares en `src/__init__.py`, `src/README.md` y Optimización de `run_qa.bat`:**
  1) Se actualizaron los metadatos YAML frontmatter y tipado `from __future__ import annotations` en `src/__init__.py` (`type: core/package`).
  2) Se estandarizó el frontmatter y la sección 3 de ejemplos en `src/README.md` (`type: doc/guide`).
  3) Se optimizó `run_qa.bat` incluyendo explícitamente `main.py` en las 3 primeras compuertas estáticas y validando el pipeline secuencial en 5 fases lógicas: 1. Ruff (linter/formato) -> 2. Pydoclint (Google Style docstrings) -> 3. Mypy (tipado estático estricto) -> 4. Pytest (43/43 tests Python) -> 5. Node.js (40/40 tests JS).
  4) Se ejecutó y aprobó la suite de calidad con `run_qa.bat` al 100% (5/5 compuertas aprobadas, 0 violaciones, 0 errores).

- **[2026-08-24 23:57] Aplicación de Nuevos Estándares en `mathjax_build/`:**
  1) Se actualizaron los metadatos YAML frontmatter de los 5 módulos de compilación en `mathjax_build/` (`package_config.js`, `sanitizer.js`, `engine.js`, `renderer.js`, `index.js`) conforme al esquema oficial de `docs/base/frontmatter_yaml.md` (`file`, `module`, `description`, `type`, `version`, `date`, `dependencies`, `relations`, `exports`, `test`, `constraints`, `keywords`).
  2) Se recompiló `src/assets/mathjax_bundle.js` mediante `build.js` verificando la integridad del bundle empaquetado.
  3) Se ejecutó y aprobó la suite de calidad con `run_qa.bat` al 100% (5/5 compuertas: Ruff OK, Pydoclint 0 violaciones en 36 archivos, Mypy 0 errores de tipado, Pytest 43/43 pasados, Node.js 40/40 pasados).

- **[2026-08-24 23:53] Aplicación de Nuevos Estándares en `docs/` y Archivos Raíz:**
  1) Se actualizaron los metadatos YAML frontmatter en `main.py` (`type: app/entrypoint`), `README.md` (`type: doc/guide`), `run_app.bat`, `run_qa.bat`, `setup_venv.bat`, `docs/ARCHITECTURE.md` (`type: doc/architecture`), y los 13 compendios/catálogos de `docs/fisica/` y `docs/mates/` conforme a `docs/base/frontmatter_yaml.md`.
  2) Se saneó el repositorio eliminando el archivo temporal residual `docs/fisica/unidades/unidades_secundarias.md.bak` en cumplimiento de la Regla 5 de `AGENTS.md`.
  3) Se ejecutó y aprobó la suite de calidad con `run_qa.bat` al 100% (5/5 compuertas: Ruff OK, Pydoclint 0 violaciones en 36 archivos, Mypy 0 errores de tipado, Pytest 43/43 pasados, Node.js 40/40 pasados).

- **[2026-08-24 23:45] Aplicación de Nuevos Estándares en `tests/`:**
  1) Se actualizaron los metadatos YAML frontmatter de los 10 archivos de la suite de pruebas (`tests/README.md`, `__init__.py`, `test_ast.py`, `test_parser.py`, `test_syntax.py`, `test_theme.py`, `test_translator.py`, `test_editor_widget.py`, `test_mathjax_build.js`, `test_mathjax_bundle.js`) al estándar de `docs/base/frontmatter_yaml.md` (`file`, `module`, `description`, `type: test/unit`, `version`, `date`, `dependencies`, `relations`, `exports`, `test`, `constraints`, `keywords`).
  2) Se aplicó tipado estricto inline con `from __future__ import annotations` en todos los módulos de prueba de Python.
  3) Se ejecutó y aprobó la suite de calidad con `run_qa.bat` al 100% (5/5 compuertas: Ruff OK, Pydoclint 0 violaciones en 36 archivos, Mypy 0 errores de tipado, Pytest 43/43 pasados, Node.js 40/40 pasados).

- **[2026-08-24 23:35] Aplicación de Nuevos Estándares en `src/data/`:**
  1) Se actualizaron los metadatos YAML frontmatter de los 4 módulos de datos (`src/data/__init__.py`, `constants.py`, `symbols.py`, `units.py`) al estándar formal de `docs/base/frontmatter_yaml.md` (`file`, `module`, `description`, `type`, `version`, `date`, `dependencies`, `relations`, `exports`, `test`, `constraints`, `keywords`).
  2) Se incorporó `from __future__ import annotations` en todos los archivos del catálogo de datos.
  3) Se ejecutó y aprobó la suite de calidad con `run_qa.bat` al 100% (5/5 compuertas: Ruff OK, Pydoclint 0 violaciones en 36 archivos, Mypy 0 errores de tipado, Pytest 43/43 pasados, Node.js 40/40 pasados).

- **[2026-08-24 23:29] Aplicación de Nuevos Estándares en `src/assets/`:**
  1) Se actualizaron los bloques de metadatos YAML de los recursos en `src/assets/` (`src/assets/mathjax_bundle.js` recompilado con su banner estructurado vía `mathjax_build/build.js`, y `src/assets/katex_preview.html`).
  2) Se actualizaron las aserciones de pruebas en `tests/test_mathjax_bundle.js` para validar la presencia de los campos estandarizados (`file: src/assets/mathjax_bundle.js`).
  3) Se ejecutó y aprobó la suite de calidad con `run_qa.bat` al 100% (5/5 compuertas: Ruff OK, Pydoclint 0 violaciones en 36 archivos, Mypy 0 errores de tipado, Pytest 43/43 pasados, Node.js 40/40 pasados).

- **[2026-08-24 23:23] Aplicación de Nuevos Estándares en `src/ui/` y `src/utils/`:**
  1) Se actualizaron los metadatos YAML frontmatter de los 19 módulos de la capa UI (`src/ui/__init__.py`, `main_window.py`, `theme.py`, y los 16 componentes de `src/ui/components/`) y los 5 módulos de la capa de utilidades (`src/utils/__init__.py`, `favorites_manager.py`, `qt_utils.py`, `recovery_manager.py`, `user_formulas_manager.py`) al esquema formal de `docs/base/frontmatter_yaml.md`.
  2) Se unificó el tipado estricto inline (`PEP 604` unions `T | None`, `from __future__ import annotations`, eliminación de `typing.Optional`), métodos constructores `-> None` y verificación completa con Mypy estricto.
  3) Se ejecutó y aprobó la suite de calidad con `run_qa.bat` al 100% (5/5 compuertas: Ruff OK, Pydoclint 0 violaciones en 36 archivos, Mypy 0 errores de tipado, Pytest 43/43 pasados, Node.js 40/40 pasados).

- **[2026-08-24 23:06] Aplicación de Nuevos Estándares en `src/core/`:**
  1) Se actualizaron los bloques de metadatos YAML de los 7 módulos de `src/core/` (`__init__.py`, `ast.py`, `logger.py`, `parser.py`, `renderer.py`, `syntax.py`, `translator.py`) al nuevo esquema oficial definido en `docs/base/frontmatter_yaml.md` (`file`, `module`, `description`, `type`, `version`, `date`, `dependencies`, `relations`, `exports`, `test`, `constraints`, `keywords`).
  2) Se introdujeron clases de configuración inmutables `@dataclass(frozen=True)` en la Sección 3 de los módulos (`ASTConfig`, `LoggerConfig`, `RendererConfig`, `SyntaxConfig`, `TranslatorConfig`) conforme a `docs/base/clase_configuracion.md`.
  3) Se normalizó el tipado estricto inline (`PEP 604` unions `T | None`) y se verificó la conformidad absoluta con `mypy --strict` y `pydoclint`.
  4) Se validó el 100% de la suite de calidad con `run_qa.bat` (5/5 compuertas aprobadas, 43/43 tests Pytest y 40/40 tests Node.js).

- **[2026-08-24 22:56] Eliminación de Listas de Variables en `src/` (Saneamiento de Anti-patrón):**
  1) Se ejecutó un saneamiento masivo eliminando todas las secciones de listas comentadas de variables (`# Lista de variables del script:` y `// Lista de variables del script:`) al final de los 38 archivos en `src/`, `main.py` y `mathjax_build/`.
  2) Se sustituyó formalmente este anti-patrón por las prácticas óptimas de tipado estricto inline (`docs/base/tipado_estricto_inline.md`) y clases de configuración centralizada (`docs/base/clase_configuracion.md`).
  3) Se ejecutó y aprobó la suite de calidad con `run_qa.bat` al 100% (5/5 compuertas: Ruff OK, Pydoclint 0 violaciones en 36 archivos, Mypy 0 errores de tipado, Pytest 43/43 pruebas unitarias Python pasadas, Node.js 40/40 pruebas JavaScript pasadas).

- **[2026-08-24 22:51] Reorganización Integral de Estándares en `AGENTS.md` (v1.4.0):**
  1) Se estructuró la Sección 1 de `AGENTS.md` en subsecciones jerárquicas (1.1 a 1.6) que integran los 4 estándares base normativos con sus enlaces a `docs/base/`.
  2) Se preservó la plantilla reducida de frontmatter YAML (1.1) y se incorporaron ejemplos de código representativos para tipado estricto inline (1.2), clases de configuración `@dataclass(frozen=True)` (1.3) y gestión de entradas CLI con `argparse` y `main(argv)` (1.4).

- **[2026-08-24 22:45] Publicación del Conjunto de Guías de Estándares Base (`docs/base/`):**
  1) Se analizó el veredicto sobre Google Style Docstrings (10/10) y la identificación de la lista de variables al final como un anti-patrón de software para IA (doc drift, fragmentación de atención, redundancia).
  2) Se estructuraron y crearon las 3 guías normativas complementarias en `docs/base/`:
     - `docs/base/tipado_estricto_inline.md`: Directrices para Type Hints nativos (Python 3.10+ PEP 585/604), tipado de constructores `-> None`, colecciones y JSDoc para JS.
     - `docs/base/clase_configuracion.md`: Patrón `@dataclass(frozen=True)` para parámetros operativos centralizados inmutables con inyección de dependencias y `replace()`.
     - `docs/base/entradas_script.md`: Gestión de `os.environ` tipado, parsers CLI con `argparse` y patrón de punto de entrada testeable `main(argv) -> int`.
  3) Se actualizaron las relaciones de interdependencia en `AGENTS.md`, `frontmatter_yaml.md` y `docs/directorios_comentados.jsonc`.

- **[2026-08-24 22:25] Oficialización de Estándar en `AGENTS.md` (v1.3.0):**
  1) Se incorporó la referencia normativa a `docs/base/frontmatter_yaml.md` en la Sección 1 ("Frontmatter y Metadatos YAML Obligatorios") y Sección 3 ("Navegación e Inspección por Metadatos") de `AGENTS.md`.
  2) Se añadieron las plantillas reducidas con campos y tipos de datos para documentación (`.md`) y ejecutables (`.py`, `.ts`, `.js`, etc.) como guía rápida para agentes y desarrolladores.

- **[2026-08-24 22:18] Sincronización de Ejemplos Reales en `docs/base/frontmatter_yaml.md`:**
  1) Se adaptaron los bloques de ejemplo de ambas plantillas universales con datos reales del proyecto: `docs/ARCHITECTURE.md` para la plantilla de documentación (`covers`, `relations`, `keywords`) y `src/ui/main_window.py` para la plantilla de ejecutables (`module`, `dependencies`, `relations`, `exports`, `test`, `constraints`, `keywords`).
  2) Se mantuvieron los comentarios explicativos por campo de acuerdo a las especificaciones.

- **[2026-08-24 22:10] Creación de `docs/base/frontmatter_yaml.md`:**
  1) Se formalizó el estándar de metadatos YAML frontmatter del repositorio creando el documento central `docs/base/frontmatter_yaml.md`.
  2) Se incluyeron las dos plantillas universales comentadas: una para archivos de documentación (`.md`) y otra para código fuente ejecutable (`.py`, `.ts`, etc.).
  3) Se documentaron las reglas de los campos extendidos (`keywords`, `relations`, `date`) para indexación RAG, grafos de acoplamiento y marcas de tiempo de sincronización.
  4) Se integró al final la tabla descriptiva con todos los campos de metadatos (`file`, `description`, `type`, `version`, `date`, `keywords`, `relations`, `covers`, `module`, `exports`, `dependencies`, `test`, `constraints`), especificando ámbito de uso, tipo de dato, estándar de formato y ejemplos.

## Sesión: Actualización Exhaustiva de Documentación Interna en `src/core/` (2026-08-24 21:58)

- **[2026-08-24 21:58] Estandarización de Metadatos YAML, Google Style Docstrings e Inventario de Variables en `src/core/`:**
  1) Se auditaron y actualizaron todos los archivos del paquete central `src/core/` (`__init__.py`, `ast.py`, `logger.py`, `parser.py`, `renderer.py`, `syntax.py`, `translator.py`) de acuerdo con los estándares formales de `AGENTS.md`.
  2) Se completaron los metadatos YAML en docstring de módulo (campos `script`, `module`, `description`, `author`, `version`, `dependencies`, `keywords`, `classes_and_functions`).
  3) Se estructuraron los docstrings en formato Google Style en español en todas las clases y funciones públicas/internas, validando que los parámetros constructores `Args:` se ubiquen en el docstring de la clase para estricta conformidad con `pydoclint` (regla DOC301 superada con 0 violaciones).
  4) Se añadió y enriqueció la sección `# Lista de variables del script:` al final de cada archivo de `src/core/`, especificando el nombre exacto de cada variable, su tipo de dato estricto, su ámbito (Global, Clase, Método, Función) y una descripción clara de su propósito.
  5) Se validó el 100% de la suite de calidad con `run_qa.bat` (5/5 compuertas aprobadas: Ruff 0 advertencias, Pydoclint 0 violaciones en 36 archivos, Mypy 0 errores de tipado, Pytest 43/43 pruebas unitarias Python pasadas, Node.js 40/40 pruebas JavaScript pasadas).

## Sesión: Corrección de Límites de Integrales / Laplace y Configuración de QSvgRenderer (2026-08-24 21:18)

- **[2026-08-24 21:18] Corrección de Parseo de Límites en Integrales Definidas / Transformada de Laplace y Supresión de Aviso QSvg:**
  1) Se corrigió el error en `_LaTeXStreamParser.parse_arg_slot()` de `src/core/parser.py`, donde los argumentos no delimitados por llaves (`\int_0^\infty`) llamaban a `check_sub_sup()` y devoraban ávidamente el operador de superíndice `^\infty` como exponente del límite inferior (`0^\infty`). Al eliminar esta llamada anticipada en argumentos atómicos, `\int_0^\infty` asigna limpiamente `0` a `lower` e `\infty` a `upper`.
  2) Se resolvió la advertencia de Qt 6.7+ (*"Too many nested nodes at path exceeding max nested limit of 32"*) al seleccionar fórmulas complejas estableciendo `os.environ["QT_SVG_DEFAULT_OPTIONS"] = "2"` y `QSvgRenderer.setDefaultOptions(QtSvg.Option.AssumeTrustedSource)` en `main.py` y `src/ui/components/svg_cache.py`, además de filtrar el aviso en `qt_message_handler`. Se incorporó prueba unitaria `test_parse_definite_integral_laplace_limits` (43/43 tests pytest, 40/40 tests JS, 100% QA superado).

## Sesión: Diagnóstico y Corrección de Renderizado de Plantillas LaTeX en MathJax (2026-08-24 21:07)

- **[2026-08-24 21:07] Corrección de Glifo `\square` y Carga de Paquetes en `mathjax_build`:** Se diagnosticó la causa raíz por la cual todas las plantillas estructuradas de la pestaña "Plantillas" se renderizaban como líneas blancas gruesas (rectángulos de error opacos). La causa radicaba en: 1) Los submódulos de configuración de paquetes de MathJax (`ams`, `unicode`, `configmacros`, etc.) no eran importados explícitamente en `mathjax_build/engine.js`, lo que provocaba que únicamente el paquete `base` quedara registrado y esbuild omitiera sus definiciones. 2) El comando de casilla vacía `\square` (utilizado como marcador de posición por todos los nodos de plantillas como `\frac{\square}{\square}`) no estaba declarado en MathJax 3, disparando el error `Undefined control sequence \square`. 3) La regla CSS de sanitizado inyectaba `fill: ${color} !important` sobre el `<rect data-background="true">` de MathJax, pintando un rectángulo sólido. Se solucionó importando explícitamente las configuraciones de extensiones en `engine.js`, declarando macros TeX personalizadas (`square: '\\unicode{x25A1}'`, `Box: '\\unicode{x25A1}'`, `blacksquare: '\\unicode{x25A0}'`), aislando el fondo de error en `sanitizer.js`, regenerando `src/assets/mathjax_bundle.js` con esbuild y ampliando la batería de pruebas (40/40 tests JS, 42/42 tests pytest, 100% QA superado).

## Sesión: Modularización de MathJax Bundle, Limpieza de Código Legado y Metadatos (2026-08-22 13:41)

- **[2026-08-22 14:25] Estandarización de Reglas de Agente en `AGENTS.md` y Actualización de `main.py`:** Se actualizaron y formalizaron en `AGENTS.md` las directrices obligatorias de: 1) Frontmatter/cabecera YAML estructurada en todos los archivos fuera de `.gitignore`, 2) Formato mandatorio Google Style Docstrings en todo código ejecutable, y 3) Lista explicativa de variables y tipos esperados al final de cada archivo ejecutable (`# Lista de variables del script:`). Se aplicaron rigurosamente estas reglas a `main.py`, actualizando sus dependencias (`src/core/logger.py`, `src/ui/main_window.py`), documentando completamente las funciones de manejo de excepciones y Qt, y añadiendo su bloque de variables. (100% QA superado).

- **[2026-08-22 14:20] Actualización de Documentación Global, ARCHITECTURE.md, README.md y QA Pipeline (5/5):** Se sincronizó la documentación técnica global del repositorio. Se actualizó `docs/ARCHITECTURE.md` (árbol de directorios YAML, flujo de componentes dinámicos y scripts POSIX), se regeneró `docs/directorios.json` filtrando caches y se actualizó `docs/directorios_comentados.jsonc` con las utilidades de usuario y el compilador modular. Se actualizó `README.md` (versión 2.1.0) reflejando la arquitectura de 5 compuertas de calidad en `run_qa.bat` (Ruff, Pydoclint, Mypy, Pytest 42/42 y Node.js tests 38/38) y el paquete `src/README.md`. (100% QA superado).

- **[2026-08-22 14:15] Auditoría, Metadatos y Tipado en Paquete de Utilidades (`src/utils/`):** Se auditaron todos los componentes de `src/utils/` (`favorites_manager.py`, `qt_utils.py`, `recovery_manager.py`, `user_formulas_manager.py`), se creó `src/utils/__init__.py` con metadatos estructurados YAML, se dotó a todos los métodos de tipado estricto (`def __init__(self) -> None:` resolviendo notas de Mypy), se añadieron docstrings Google Style en todas las clases y funciones de gestión de fórmulas y favoritos, y se agregó la sección `# Lista de variables del script:` al final de cada archivo. (42/42 tests pytest, 38/38 tests JS, 0 errores QA).

- **[2026-08-22 14:12] Auditoría, Metadatos y Docstrings en la Capa UI (`src/ui/`):** Se auditaron exhaustivamente los 19 archivos de `src/ui/` y sus componentes. Se dotó a todos los módulos de cabeceras YAML estructuradas, docstrings Google Style validados con Pydoclint (resolviendo DOC301, DOC601 y DOC603 al documentar adecuadamente `Args:` y `Attributes:` en clases de widgets y diálogos), se organizaron los imports y se aseguró la sección `# Lista de variables del script:` al final de cada uno (`action_bar.py`, `edit_formula_dialog.py`, `save_formula_dialog.py`, `constant_card.py`, `unit_card.py`, `procedure_card.py`, `palette_widget.py`, `help_dialog.py`, `main_window.py`). (42/42 tests pytest, 38/38 tests JS, 0 errores QA).

- **[2026-08-22 14:04] Auditoría, Metadatos y Docstrings en Paquete de Datos (`src/data/`):** Se auditaron exhaustivamente `src/data/__init__.py`, `src/data/constants.py`, `src/data/units.py` y `src/data/symbols.py`. Se expandieron los bloques de metadatos estructurados YAML y docstrings Google Style, se tiparon las listas de catálogo `list[dict[str, object]]`, se importó y anotó el tipo de retorno `MathTree` en `_parse_preset` de `symbols.py`, se corrigió un delimitador erróneo en estereorradián dentro de `units.py` (`1\text{ (adimensional)}`), y se agregaron las listas descriptivas de variables (42/42 tests pytest, 38/38 tests JS, 0 errores QA).

- **[2026-08-22 14:00] Auditoría, Metadatos y Tipado en Módulos Core (`src/core/`):** Se auditaron exhaustivamente todos los componentes de `src/core/` (`__init__.py`, `ast.py`, `logger.py`, `parser.py`, `renderer.py`, `syntax.py`, `translator.py`). Se incorporaron metadatos YAML estructurados y docstrings Google Style en `logger.py` y `__init__.py`, se ajustaron anotaciones de tipo estrictas en `MathTree.__init__` de `ast.py` eliminando notas de Mypy, se corrigió la lista de variables de scripts y se preservó la compatibilidad de toda la arquitectura (42/42 tests pytest, 38/38 tests JS, 0 errores QA).

- **[2026-08-22 13:52] Auditoría de KaTeX y Modernización de `katex_preview.html`:** Se inspeccionó la integridad de `src/assets/katex/` (KaTeX v0.16.11 con fuentes y módulos locales intactos). Se rediseñó y sincronizó `src/assets/katex_preview.html` eliminando dependencias de CDN externos (`jsdelivr.net`) para garantizar funcionamiento 100% offline. Se dotó a la plantilla de compatibilidad dual (MathJax Bundle + KaTeX local), metadatos YAML frontmatter, docstrings Google Style, flexbox centrado y scrollbars con la paleta Hatsune Miku.

- **[2026-08-22 13:48] Batería de Pruebas Unitarias en JavaScript (node:test):** Se crearon `tests/test_mathjax_build.js` y `tests/test_mathjax_bundle.js` con 38 pruebas unitarias automatizadas en Node.js nativo. Verifican el funcionamiento aislado de cada submódulo de compilación (`package_config`, `sanitizer`, `engine`, `renderer`, `index`), la exclusión de paquetes legados, la sanitización no destructiva de atributos SVG para Qt TinySVG, y la ejecución del bundle en un contexto VM de V8 idéntico a MiniRacer sobre fórmulas de álgebra, cálculo, ecuaciones diferenciales, matrices, sistemas, electromagnetismo, cuántica y unidades. (38/38 pruebas pasadas en 308ms).

- **[2026-08-22 13:41] Modularización de MathJax y Generación con esbuild:** Se descompuso la lógica del motor de MathJax (`mathjax_build/`) en módulos especializados con responsabilidades únicas: `package_config.js` (selección optimizada de extensiones TeX), `sanitizer.js` (sanitización de dimensiones para TinySVG, inyección de estilos y XMLNS), `engine.js` (instanciación de LiteDOM y documentos virtuales MathJax) y `renderer.js` (orquestación síncrona `renderMathSync`). Se eliminaron módulos legados pesados no utilizados como `mhchem` (>15k líneas de química), `bussproofs`, `colortbl`, `amscd` y `verb`, reduciendo el bundle `mathjax_bundle.js` en más de 9,300 líneas y acelerando el tiempo de pruebas de 9.09s a 5.17s. Se incorporaron cabeceras de metadatos YAML y docstrings Google Style en todos los scripts de JS.

## Sesión: Pestaña de Usuario, Variantes de Fórmulas y Pulido de UI (2026-08-22 02:46)

- **[2026-08-22 03:24] Corrección y Despliegue de Colores Hatsune Miku en Botones:** Se corrigió la asignación de colores de fondo en botones que previamente mostraban el gris superficial por defecto. Se aplicaron los colores característicos del tema Hatsune Miku: Azul Turquesa (`#39C5BB`) a `Guardar Fórmula`, `Exportar ⌄`, `Copiar LaTeX`, `[+] Zoom`, `Restablecer`, `❓ Ayuda` y pestañas activas; Rosa Magenta (`#E3327B`) a `Limpiar`, `Copiar Markdown`, `[-] Zoom` y `📋 Logs`.

- **[2026-08-22 03:19] Emojis Dinámicos de Modo, Estilo Unificado y Nombres Descriptivos:** Se implementó emoji dinámico en el botón conmutador de tema (`☀️ Modo Claro` en modo oscuro / `🌙 Modo Oscuro` en modo claro). Se armonizó el diseño cromático Hatsune Miku para los controles de zoom `[+]` `[-]`, `Restablecer`, `Exportar ⌄`, selector de tamaño de texto `QComboBox`, botón `Limpiar` y `QTabBar` activa e inactiva. Se expandieron los nombres de los cuatro paneles principales a títulos autoexplicativos (*"Editor Visual de Fórmulas"*, *"Catálogo de Fórmulas y Símbolos"*, *"Vista Previa Renderizada"* y *"Traductor de Código Multilenguaje"*).

- **[2026-08-22 03:07] Conservación de Emojis en Pestañas:** Se mantuvieron los emojis identificativos en todas las pestañas de la paleta (`⭐ Favoritos`, `🧩 Plantillas`, `🔣 Símbolos`, `♾️ Constantes`, `📏 Unidades`, `👤 Usuario`, `📚 Formulario`) y botones de ramas temáticas (`📐 Matemáticas`, `⚛️ Física`).

- **[2026-08-22 03:05] Reubicación de Botones y Nombres Concisos de Paneles:** Se trasladaron los botones "Limpiar" y "Guardar Fórmula" a la parte inferior del editor interactivo (`MathEditorWidget`). Se eliminó el indicador de menú duplicado en el botón de exportación dejando un chevron descendente (`⌄`). Se estandarizó la leyenda de zoom a "Zoom" y el botón a "Restablecer". Se asignaron nombres cortos y profesionales a los 4 paneles principales.

- **[2026-08-22 02:51] Nueva Ventana Modal de Ayuda (HelpDialog):** Se creó el componente `HelpDialog` en `src/ui/components/help_dialog.py` con una guía exhaustiva y estilizada que documenta los 4 paneles, atajos del editor interactivo, navegación del formulario por rama y nivel, carruseles de variantes, persistencia y edición de fórmulas de usuario, catálogos de constantes/unidades y herramientas de exportación y logs.

- **[2026-08-22 02:46] Optimización Visual de Niveles e Inicialización Git:** Se reemplazaron los glifos emoji (`🟢`, `🟣`, `🔴`) de los botones de nivel por iconos generados dinámicamente con `QPainter` y anti-aliasing (10px). Esto elimina por completo el desborde y recorte vertical que sufrían las fuentes de emojis en Windows. Se incorporaron demostraciones paso a paso de álgebra (Deducción Cuadrática) y física (Torricelli) y se preparó el commit de la primera versión del proyecto.

- **[2026-08-22 00:30] Sistema de Variantes Interactivas:** Se dotó a `EditFormulaDialog` y `UserFormulasManager` de soporte para múltiples variantes por fórmula (con carrusel interactivo `< >`, botón de añadir/eliminar y casilla de personalización de nombre). La tarjeta `ProcedureCardWidget` en la pestaña de Usuario activa automáticamente sus flechas y contador cuando una fórmula posee 2 o más variantes.

- **[2026-08-22 00:20] Rediseño de Diálogos de Guardado y Edición:** Se reorganizó el orden de campos (Rama, Categoría, Descripción, Subcategoría opcional y Nombre). La descripción se resalta en turquesa Miku en la tarjeta, el desplegable de categoría carga las predeterminadas filtradas por rama sin numeración y la fórmula se previsualiza renderizada en SVG.

- **[2026-08-21 23:40] Persistencia y Estado Vacío en Pestaña Usuario:** Se reubicó la persistencia a `src/data/user_formulas_data.json`, se conectó la inicialización en el arranque de la aplicación y se convirtió la jerarquía de categorías a menús colapsables tipo acordeón con menús contextuales.

## Sesión: Implementación del buscador en la paleta (2026-08-21 16:53)
- **[2026-08-21 16:31] Estandarización de Funciones Trigonométricas:** Se detectó y resolvió un fallo de renderizado visual en el editor y el Preview causado por los símbolos `\sech` y `\csch`, los cuales no están integrados por defecto en KaTeX. Se actualizaron los diccionarios base y se programó un mapeo condicional en `parser.py` para que siempre se traduzcan de forma nativa como `\operatorname{sech}` y `\operatorname{csch}`.
 (2026-08-21 14:27)

- **[2026-08-21 16:06] Políticas de Espacio de Trabajo (Sandbox):** Se actualizó el archivo `AGENTS.md` oficializando la restricción de alojar *scripts* esporádicos o documentación descartable exclusivamente en la carpeta `sandbox/`, evitando el *overhead* en la raíz. El directorio fue agregado a `.gitignore`. La batería `run_qa.bat` arrojó 100% de efectividad en *Linter*, *Mypy*, *Pydoclint* y *Pytest*.

- **[2026-08-21 15:57] Diagnóstico y Traceback de Errores:** Se robusteció el gestor de eventos (`logger.py`) agregando un wrapper especializado (`@capture_error`) e inyectándolo en los puntos críticos de fallo de la arquitectura (`main_window.py`, `preview_panel.py`, `code_panel.py`). Esto asegura que cuando ocurran los fallos típicos (por ej: renderizado WebEngine truncado `[ERR_JS_009]`, o errores de casillas anidadas `[ERR_PARSER_002]`), los registros en `session.log` no solo escupan el código de error genérico, sino que incrusten la traza completa y los argumentos exactos de Python para depuración de los agentes.

- **[2026-08-21 15:47] Creación de Entorno Sandbox:** Se implementó la directiva de área de pruebas (`sandbox/`) para aislar *scripts throwaway* (de un solo uso) generados por agentes IA y desarrolladores, protegiendo el árbol `src/` principal. Adicionalmente, se validó la integridad de paquetes del `.venv` contrastando `pip freeze` contra `pyproject.toml` (PySide6, matplotlib, mini-racer, pytest, etc.), sin necesidad de actualizaciones.

- **[2026-08-21 15:36] Limpieza de Scripts POSIX:** Dado que el desarrollo actual se centra en Windows (usando los equivalentes `.bat`), los archivos `run_app.sh`, `run_qa.sh` y `setup_venv.sh` fueron documentados textualmente en `docs/ARCHITECTURE.md` para resguardar la compatibilidad futura, y luego eliminados del directorio raíz para reducir el ruido.

- **[2026-08-21 15:31] Anidación del AST y Refactorización de Inserción:** Se resolvió el error de diseño donde la inserción de fórmulas preestablecidas reemplazaba el MathTree global de la aplicación. Se implementó insert_nodes en st.py para inyectar limpiamente múltiples sub-nodos directamente en el ctive_slot del usuario sin perder el foco ni sobreescribir el contenedor padre (ditor_widget.py y code_panel.py).

- **[2026-08-21 15:21] Reflejo Estructural de Docs:** Se corrigieron los mapas JSON/JSONC de arquitectura para integrar el traslado de los Markdown de física y matemáticas a la carpeta docs/, completando así la organización semántica del proyecto.

- **[2026-08-21 15:13] Saneamiento del Directorio Raíz:** Eliminados scripts temporales de desarrollo (tests de SVG de QByteArray, parseadores de unidades físicas desde Markdown, limpiadores regex y parches de código a la interfaz) al haber cumplido su función. Se integró una nota arquitectónica en `src/README.md` explicando que el catálogo de unidades/constantes (`data/`) fue compilado dinámicamente mediante este enfoque iterativo, documentando así el *know-how* detrás de la sincronización de las bases de datos locales.

- **[2026-08-21 15:08] Sincronización de Mapas de Directorio:** Se actualizó la estructura en `docs/directorios.json` automatizando un escaneo directo de la carpeta `src/`. Se agregaron los módulos faltantes (tarjetas y catálogos de constantes y unidades) en `docs/directorios_comentados.jsonc` y se reflejaron los avances recientes de arquitectura (WebEngine KaTeX, SearchBar, Constants) en las "Características Principales" del `README.md` raíz.

- **[2026-08-21 15:00] Actualización de Arquitectura y Readmes:** Modificado `src/README.md` y `docs/ARCHITECTURE.md` para reflejar la incorporación de catálogos recientes (`constants.py`, `units.py`) y nuevas tarjetas UI. En `ARCHITECTURE.md` se incrustó un diagrama Mermaid para ilustrar el mecanismo de filtrado del motor de búsqueda.

- **[2026-08-21 14:52] Revisión y Documentación de Código:** Se inspeccionaron los scripts de la carpeta `src` utilizando el linter `pydoclint` (verificando el estándar Google Style de las docstrings, con 0 violaciones reportadas) y un analizador de metadatos YAML en docstrings. Se corrigió la falta de cabeceras YAML en `constants.py` y `units.py` para cumplir con las directrices de `AGENTS.md`.

- **[2026-08-21 14:45] Corrección de Tests:** Se actualizaron las pruebas unitarias para reflejar los cambios recientes en la estructura del catálogo (reemplazando verificaciones obsoletas de uilder por ariations), el ajuste de colores en el tema Miku y las nuevas pestañas integradas en la paleta de símbolos.

- **[2026-08-21 14:27] Buscador Global en Paleta:** Se añadió un QLineEdit en MathPaletteWidget que permite buscar y filtrar en tiempo real todas las categorías y catálogos de la paleta. El filtro (_apply_search_filter) extrae el texto, descripción y comandos LaTeX de cada componente (TemplateCardOption, ProcedureCardWidget, ConstantCardWidget, UnitCardWidget) y oculta las tarjetas que no coinciden con la búsqueda, expandiendo automáticamente las categorías que tienen resultados.

## Sesión: Auditoría de catálogos de constantes (2026-08-20 00:00)

- **[2026-08-21 03:36] Nombres de Magnitudes Secundarias:** Corregido el parser de tablas en `parse_units.py` para la categoría de magnitudes frecuentes en formularios. Anteriormente, la condición para identificar esta tabla de tres columnas era muy estricta y fallaba, ocasionando que la sintaxis LaTeX se filtrara al campo del título en el botón. Ahora muestra correctamente los nombres (ej. "Frecuencia angular").
- **[2026-08-21 03:30] Limpieza de Unidades Secundarias y Celsius:** Corregido el símbolo del grado Celsius (de `$^\circ$C` erróneo a `^\circ\mathrm{C}`) y limpiado el texto base para apuntar únicamente a su contraparte fundamental (`\mathrm{K}`). Se creó y ejecutó un script para limpiar la tabla de unidades no SI e ingeniería (como el electronvoltio), eliminando el ruido del texto `(exacto)`, ecuaciones redundantes (`1 unidad = `) y conflictos internos con signos `$`. Esto soluciona finalmente los errores de "línea gruesa blanca" en MathJax derivados del desbordamiento del modo matemático por texto Markdown incrustado.
- **[2026-08-21 00:20] Solución MathJax `\mathrm{}`:** Eliminado totalmente el uso del entorno `\text{}` en la inserción de unidades fundamentales (`docs` y `parse_units.py`). Se ha reemplazado por `\mathrm{}`. Esto soluciona de raíz las colisiones de renderizado (línea gruesa blanca por errores en SVGMathCache) cuando el usuario agrupaba diferentes unidades fundamentales de forma interactiva en la vista previa.
- **[2026-08-20 23:55] Mejora Visual de Unidades:** Implementada una excepción en `parse_units.py` y modificado `unit_card.py` para ignorar y limpiar la base fundamental (`[s]`, `[m]`, etc.) en las unidades Fundamentales. Esto elimina la redundancia visual (`s [s]`) en la interfaz interactiva y previene problemas de análisis innecesario en el parser.
- **[2026-08-20 23:42] Desempaquetado AST:** Solucionado el fallo `TypeError` en el editor que provocaba que se renderizara el texto de depuración del nodo (ej. `[R[Hz]...]`). Ahora `_on_template_inserted` detecta si el componente insertado es un árbol matemático entero (`MathTree`) y desempaqueta sus nodos en la posición del cursor de manera correcta.
- **[2026-08-20 23:25] Corrección de Renderizado y AST:** Arreglado el error en MathJax (Línea gruesa blanca) sustituyendo entornos `\text` no compatibles por `\mathrm` en las definiciones. Las unidades ahora se insertan como un árbol AST parseado (`_parse_preset()`) para que sean editables en el lienzo matemático.
- **[2026-08-20 23:10] Interfaz de Unidades:** Procesados archivos de unidades físicas en `docs/fisica/unidades/` mediante `parse_units.py` para generar la estructura `UNITS` y añadida una nueva pestaña de Unidades en la interfaz usando el nuevo componente `UnitCardWidget`.
- **[2026-08-20 22:49] Unidades físicas (docs):** Añadidas las unidades físicas secundarias derivadas por rama a `unidades_secundarias.md`, aplicando el reemplazo de corchetes en las equivalencias base y evitando duplicaciones previas.
- **[2026-08-20 22:43] Unidades físicas (docs):** Añadidas las unidades físicas derivadas por rama de la física a `unidades_principales.md`, utilizando notación de corchetes para unidades fundamentales y omitiendo datos duplicados con las tablas superiores.
- **[2026-08-20 22:26] Unidades físicas (docs):** Corregida la estructura de `unidades_fundamentales.md`, ampliadas derivadas SI en `unidades_principales.md` (incluyendo rad, sr, °C y kat) y reemplazado el duplicado de `unidades_secundarias.md` por catálogo de unidades no SI con conversiones exactas/prácticas.
- **[2026-08-20 00:00] Auditoría:** Revisados y reorganizados los catálogos físicos y matemáticos por nivel básico, intermedio y avanzado.
- **[2026-08-20 00:00] Correcciones:** Actualizados valores físicos a CODATA 2022, corregidas definiciones y clasificaciones, y documentada la diferencia entre constantes exactas, convencionales, experimentales y parámetros de modelo.
- **[2026-08-20 00:00] Ampliación:** Añadidas constantes de electromagnetismo, circuitos cuánticos, flujo magnético, energía de campo y fotónica.
- **[2026-08-20 00:00] Informe:** Creado `errores_constantes.md` con hallazgos, correcciones, cobertura didáctica y fuentes.
*Mantiene el contexto histórico del proyecto, aciertos, errores, y objetivos logrados con marcas de tiempo (YYYY-MM-DD HH:MM).*

## Sesión: Reestructuración de la Interfaz del Editor (2026-08-10 14:00)

## Sesión: Auditoría de Formularios Matemático y Físico (2026-08-19 19:11)

- **[2026-08-19 19:11] Auditoría:** Se revisaron `formulario_mates.md` y `formulario_fisica.md` sin eliminar ni modificar fórmulas.
- **[2026-08-19 19:11] Hallazgos:** Se documentaron 32 conflictos verificables de igualdad, hipótesis, signos, convenciones y nomenclatura en `formulas_errores.md`, incluyendo Menelao, pseudoinversa, iteraciones Jacobi/Gauss-Seidel, Binet, Klein-Gordon y Laue.
- **[2026-08-19 19:11] Fuentes:** Se contrastaron los puntos críticos con referencias externas de MathWorld, WPI, University of Maryland y NIST.

- **[2026-08-10 14:00] Objetivo General:** Modificar la interfaz de usuario para que sea más intuitiva (tipo Wolfram Alpha) y solucionar el problema de solapamiento en la paleta de símbolos.
- **[2026-08-10 14:01] Acierto (Paleta):** Se reescribió la limpieza con `_clear_layout` y se redujo tamaño de botones.
- **[2026-08-10 14:02] Acierto (Editor):** Se agregaron `setAttribute(Qt.WA_TransparentForMouseEvents)` y `QSizePolicy.Maximum`.

## Sesión: Sistema de Temas Hatsune Miku y Resaltado de Sintaxis Estricto (2026-08-10 15:14)

- **[2026-08-10 15:13] Acierto (Temas):** Lógica de intercambio de QSS dinámico en `src/ui/theme.py`, `action_bar.py` y `main_window.py` permitiendo alternar entre `☀️ Modo Claro` y `🌙 Modo Oscuro` al vuelo.
- **[2026-08-10 15:13] Resaltado de Sintaxis Estricto:** Reconfigurado `src/core/syntax.py` (Verde RGB(0,255,0), Azul RGB(0,0,255), Rojo RGB(255,0,0), Lila y Naranja).

## Sesión: Layout Tipográfico 24px y Paneles Redimensionables (4 Splitters) (2026-08-10 15:25)

- **[2026-08-10 15:24] Requisito de Escala y Splitters:** Escalar la tipografía del Editor Interactivo para igualar la densidad del renderizado y dividir los 4 paneles principales con divisores verticales y horizontales en tiempo real.
- **[2026-08-10 15:25] Escala Tipográfica 24px:** Incrementado tamaño de fuente base en `src/ui/components/editor_widget.py` (Variables/Textos a 24px, Integrales a 44px, Sumatorios a 38px, Raíces a 28px) con márgenes ultracompactos, imitando la densidad de la fórmula renderizada.
- **[2026-08-10 15:25] Sistema de 4 Paneles Redimensionables:** Reestructurado `src/ui/main_window.py` incorporando 1 splitter horizontal principal y 2 splitters verticales (`left_splitter` y `right_splitter`). Se estilaron las manijas de arrastre en `theme.py` con feedback al pasar el ratón (*hover*) en Cian Miku `#39C5BB`.
- **[2026-08-10 15:25] Pruebas:** Todos los 14 unit tests pasaron en 0.23s.

## Sesión: Corrección de Layout y Jerarquía Visual del Editor (2026-08-10 15:38)

- **[2026-08-10 15:38] Paleta Expandible:** Modificada la `QSizePolicy` de la Paleta de Plantillas y Símbolos en `palette_widget.py` para permitir la expansión dinámica del contenedor al redimensionar.
- **[2026-08-10 15:38] Jerarquía Visual:** Añadida una cuadrícula de fondo estilo Miku en `MathCanvasWidget` y bordes sutiles en `SlotContainerWidget` para delimitar lógicamente las casillas vacías y llenas.
- **[2026-08-10 15:38] Posicionamiento y Escalado Exponencial:** Modificadas las firmas en `editor_widget.py` para propagar el `font_size` recursivamente, aplicando desplazamientos en el eje Y y escalado de fuentes (~30% menor) en `PowerNode`, `SubscriptNode` y `NthRootNode`.

## Sesión: Resaltado de Sintaxis Textual y Renderizado de Matrices (2026-08-10 15:49)

- **[2026-08-10 15:49] Resaltado de Sintaxis Textual (Regex):** Corregidos los colores a puros RGB (`#00FF00` y `#FF0000`) en `syntax.py`. Se ajustó la expresión regular para variables `(?<!\\)\b[a-zA-Z]\b` utilizando *negative lookbehind* (solo un carácter de lookbehind `\\`) para ignorar letras de comandos LaTeX.
- **[2026-08-10 15:49] Compatibilidad de Matrices (Matplotlib):** Se integró una capa de traducción en `MathRenderer` (`renderer.py`) que reemplaza `pmatrix`, `bmatrix` y `vmatrix` por `\left( \begin{matrix} ... \right)` y normaliza los saltos de línea con cuádruple backslash `\\\\` para el parser `mathtext` de Matplotlib, asegurando el renderizado visual sin alterar el código crudo LaTeX.

## Sesión: Documentación Técnica de Scripts y Cabecera de Metadatos YAML (2026-08-10 16:00)

- **[2026-08-10 16:00] Documentación `src/README.md`:** Creado archivo `src/README.md` detallando la arquitectura de scripts, clases, funciones, parámetros, flujo de datos unidireccional y diagrama Mermaid.
- **[2026-08-10 16:00] Cabeceras de Metadatos YAML:** Añadidas cabeceras YAML estandarizadas en las docstrings superiores de los 19 módulos Python del paquete `src/`.
- **[2026-08-10 16:00] Verificación:** Los 14 unit tests continuaron pasando exitosamente (0.23s).

## Sesión: Reglas de Documentación, Árboles YAML y Diagramas Mermaid en AGENTS.md (2026-08-10 16:06)

- **[2026-08-10 16:06] Reglas en `AGENTS.md`:** Añadidas las reglas de modificación obligatoria de documentación/metadatos al alterar la lógica interna de scripts, verificación de interdependencias, formato YAML para árboles de directorios y formato Mermaid para esquemas/gráficos de flujo.
- **[2026-08-10 16:06] Migración a YAML (`src/README.md` & `ARCHITECTURE.md`):** Reemplazada la representación ASCII del árbol de directorios por esquemas YAML estandarizados.
- **[2026-08-10 16:06] Migración a Mermaid (`ARCHITECTURE.md`):** Convertido el esquema ASCII de la interfaz gráfica a diagrama visual `mermaid`.

## Sesión: Árboles JSON, JSONC Comentado y Estructura en docs/ARCHITECTURE.md (2026-08-10 16:11)

- **[2026-08-10 16:11] `docs/directorios.json`:** Generado el árbol de directorios en formato JSON plano excluyendo explícitamente los patrones de `.gitignore`.
- **[2026-08-10 16:11] `docs/directorios_comentados.jsonc`:** Generado el árbol de directorios en formato JSONC con comentarios explicativos (`//`) sobre el propósito y función de cada archivo y directorio dentro del repositorio.
- **[2026-08-10 16:11] `docs/ARCHITECTURE.md`:** Incorporada la nueva estructura de documentación de directorios JSON, JSONC y YAML en la Sección 4.

## Sesión: Eliminación de requirements.txt, pyproject.toml PEP 621 y Documentación de main.py (2026-08-10 16:18)

- **[2026-08-10 16:18] Registro en `pyproject.toml`:** Migradas todas las dependencias principales y opcionales (`pytest>=7.0.0`) a `pyproject.toml` (estándar PEP 621).
- **[2026-08-10 16:18] Eliminación de `requirements.txt`:** Eliminado el archivo `requirements.txt` y actualizadas todas sus referencias en `README.md`, `setup_venv.bat`, `setup_venv.sh` y en los archivos de `docs/`.
- **[2026-08-10 16:18] Documentación de `main.py`:** Incorporada la cabecera de metadatos YAML en la docstring de `main.py` según los estándares de `src/README.md`.

## Sesión: Frontmatter YAML en Archivos de la Raíz e Inspección por Metadatos en AGENTS.md (2026-08-10 16:21)

- **[2026-08-10 16:21] Frontmatter YAML en Documentación:** Inserción de bloques YAML frontmatter (`---`) en todos los archivos Markdown de la raíz (`AGENTS.md`, `README.md`, `MEMORY.md`, `PROGRESS.md`, `docs/ARCHITECTURE.md`) y comentarios de metadatos en scripts de inicialización (`run_app.bat`, `run_app.sh`, `setup_venv.bat`, `setup_venv.sh`).
- **[2026-08-10 16:21] Regla de Inspección por Metadatos:** Actualizada la Sección 3 de `AGENTS.md` para explicitar que los agentes deben consultar en primer lugar la cabecera de metadatos YAML de los archivos para entender su propósito, módulo y relaciones.

## Sesión: Enriquecimiento de Metadatos YAML (Dependencias, Keywords y Funciones) (2026-08-10 16:25)

- **[2026-08-10 16:25] Metadatos Extendidos en Scripts `src/` y `main.py`:** Añadidas las listas de `dependencies` (interdependencias con otros archivos del proyecto), `keywords` (palabras clave de búsqueda rápida para IAs) y `classes_and_functions` (listado explícito de clases y métodos expuestos).
- **[2026-08-10 16:25] Frontmatter YAML en `src/README.md`:** Incorporado el bloque frontmatter YAML con dependencias y palabras clave en la documentación interna del código fuente.

## Sesión: Migración a Renderizado Web con KaTeX y QWebEngineView (2026-08-10 16:33)

- **[2026-08-10 16:33] Migración de Motor de Renderizado:** Se reemplazó el renderizado nativo en `src/ui/components/preview_panel.py` basado en Matplotlib y `QLabel` por un widget de navegador web integrado utilizando `QWebEngineView`.
- **[2026-08-10 16:33] Integración Local de KaTeX:** Se descargó e integró la librería KaTeX localmente en `src/assets/katex` y se diseñó una plantilla `katex_preview.html` que respeta y se camufla con los colores dinámicos del Tema Miku (Claro/Oscuro).
- **[2026-08-10 16:33] Inyección JS y Exportación PNG:** La función `update_preview` fue reprogramada para pasar la cadena LaTeX mediante inyección de JavaScript `runJavaScript`, y la función de captura fue adaptada empleando `self.web_view.grab()` para mantener la exportación a PNG funcional.
- **[2026-08-10 16:38] Actualización de Documentación en `docs/`:** Se actualizaron `docs/directorios.json`, `docs/directorios_comentados.jsonc` y `docs/ARCHITECTURE.md` para reflejar la incorporación de `src/assets` (KaTeX) y se enriqueció `directorios_comentados.jsonc` complementándolo con los metadatos de las clases, funciones, dependencias y palabras clave de cada script.
- **[2026-08-10 16:42] Solución 'katex is not defined':** Se configuró `setHtml(html_content, baseUrl=base_url)` con barra inclinada final en la ruta de assets, se removió `defer` del script en `katex_preview.html` y se activaron los permisos `LocalContentCanAccessFileUrls` y `LocalContentCanAccessRemoteUrls` en `QWebEngineSettings`.
- **[2026-08-10 16:51] Refactorización del Parser Inverso (`LaTeXParser`):** Se reemplazó el bucle ingenuo de `src/core/parser.py` por el tokenizador/parser recursivo descendente `_LaTeXStreamParser`. Ahora tokeniza y mapea semánticamente comandos complejos (`\int`, `\sum`, `\lim`, `\begin{...}`, `\left`, `\sqrt`, `\frac`, `^`, `_`), generando instancias verdaderas de `TemplateNode` (integrales, matrices, sumatorias, límites, etc.) con sus casillas hijas (`Slots`) interactivas. Se añadieron pruebas en `tests/test_parser.py` (17/17 pasadas).
- **[2026-08-10 16:57] Catálogo Extendido y Diálogo Modal con Carrusel (`PresetCatalogDialog`):** Se amplió `PRESET_FORMULAS` en `src/data/symbols.py` a 22 fórmulas emblemáticas universitarias organizadas en 6 categorías didácticas (Álgebra, Trigonometría/Geometría, Cálculo, Álgebra Lineal, Estadística y Física). Se sustituyó la lista desplegable simple por `PresetCatalogDialog` en `src/ui/components/action_bar.py` con pestañas tipo Chips y carrusel interactivo provisto de flechas de navegación lateral (`◀` y `▶`) para cargar fórmulas con sincronización instantánea en los 4 paneles. Pruebas pasadas (18/18 en 0.23s).
- **[2026-08-10 17:17] Rediseño Paleta Estilo Word, Exportación SVG y Recorte BoundingBox:**
  1. **Paleta Ribbon (`palette_widget.py`)**: Se transformó la paleta en un sistema estilo Microsoft Word Ribbon con botones de categoría desplegables (`▾`), desplegando submenús (flyouts) con cajas punteadas `[ □ ]` (`TemplateCardOption`) y etiquetas textuales explicativas debajo.
  2. **Exportación PNG/SVG (`preview_panel.py`)**: Se añadió menú desplegable `💾 Exportar ▾` ofreciendo exportación en formato PNG o SVG vectorial nativo sin pérdida de calidad (`getFormulaSVG()`).
  3. **Centrado y Recorte Exacto (`katex_preview.html` / `preview_panel.py`)**: Se implementó centrado Flexbox en HTML/CSS y cálculo JS de `getBoundingClientRect()` (`getFormulaRect()`) para recortar dinámicamente las capturas PNG al área real de la ecuación más padding (20px), eliminando espacio vacío excedente. Pruebas superadas (18/18 pasadas).
- **[2026-08-10 17:33] Reestructuración Visual de Paleta y Catálogo (Mejora de UX Tipográfica):**
  1. **Escalado Tipográfico 3x:** Se amplió la fuente de los símbolos matemáticos y plantillas a 36px/39px y se ajustaron los `min-width`/`min-height` de los botones (`TemplateCardOption` y `s_btn`) en `palette_widget.py` para facilitar la lectura.
  2. **Separación Lógica Ribbon/Grid:** Los botones de categorías superiores ("Ribbon") ahora despliegan exclusivamente menús flotantes, cesando la actualización del panel inferior.
  3. **Panel Estático Híbrido:** Se dividió el panel estático inferior de `palette_widget.py` en dos secciones permanentes: una cuadrícula (grid) para símbolos "⭐ Favoritos" y un acordeón interactivo (`QToolBox`) para el "📚 Catálogo de Ejemplos", eliminando la ventana modal (eliminado `PresetCatalogDialog` de `action_bar.py`).
- **[2026-08-10 17:42] Separación en Pestañas, Menú Contextual y Renderizado Visual (Mejora UX):**
  1. **Integración de `QTabWidget`:** En el panel inferior de la paleta se reemplazó el diseño apilado por pestañas mutuamente excluyentes ("⭐ Favoritos" y "📚 Ejemplos") para evitar la superposición.
  2. **Añadir a Favoritos (Menú Contextual):** Se vinculó la señal `customContextMenuRequested` (clic derecho) a las plantillas y símbolos de los menús desplegables (flyouts). Al activarse, permite agregarlos al archivo local de favoritos, actualizando instantáneamente la cuadrícula mediante `_load_favorites_grid()`.
  3. **Renderizado de Catálogo en `QPixmap`:** Se solucionó el problema de traslape textual reescribiendo la lista del acordeón "📚 Ejemplos" mediante `FormulaListButton`. Este botón ahora procesa dinámicamente las fórmulas usando `MathRenderer.render_latex_to_pixmap`, sustituyendo el crudo código LaTeX por su representación visual nativa (imagen) renderizada por Matplotlib. Pruebas superadas (18/18).
- **[2026-08-10 17:54] Corrección Crítica del Motor de Exportación (SVG y Crop PNG):**
  1. **Eliminación del Doble Renderizado (Ghost Text SVG):** Se inyectó `output: "html"` en la inicialización de `katex.render()` dentro de `katex_preview.html` y se agregó la regla CSS `.katex-mathml { display: none !important; }` para prevenir la generación e inserción accidental del marcado de accesibilidad en los vectores SVG.
  2. **Recorte Exacto (Bounding Box):** Se modificó la rutina JavaScript de medición (`getFormulaRect()` y `getFormulaSVG()`) para que el `getBoundingClientRect()` se realice sobre la clase interior `.katex-html` en lugar de la envolvente global `.katex-display`. Esto proporciona las coordenadas y el tamaño real de la ecuación, eliminando definitivamente los márgenes negros masivos al exportar PNG. Pruebas superadas (18/18).
- **[2026-08-10 20:50] Refactorización Estructural del AST y Parser (`OperatorNode`, `display`):**
  1. Se simplificó la propiedad gráfica `.display_symbol` y `.latex_code` de los nodos a un formato unificado `.display` y `.latex_cmd`.
  2. Se extrajeron todas las funciones trigonométricas y de cálculo analítico (`\sin`, `\cos`, `\lim`, `\det`) a una nueva clase independiente `OperatorNode`, separándolas de `SymbolNode` (reservado a letras griegas y relaciones).
  3. Se solucionaron errores graves de recursión del parser y el renderizado UI que provocaban excepciones como `'SymbolNode' object has no attribute 'display_symbol'`, recuperando la renderización inmediata al hacer clic en un ejemplo.
- **[2026-08-10 21:05] Infraestructura de Logging y Resguardo de SVG/Markdown:**
  1. **Motor de Logging Central (`logger.py`)**: Se implementó una capa defensiva `try-except` en la interfaz `main_window.py` que detiene caídas y deriva las trazas a `logger.py` y a una ventana gráfica (Visor de Logs en `action_bar.py`).
  2. **Conversión Estándar SVG/PNG**: Se migró unificadamente a `QSvgRenderer` para renderizar archivos nativos desde el caché de MathJax (esquivando bloqueos asíncronos), y se inyectó una capa `<rect>` universal con `fill="#ffffff"` en SVG para garantizar fondo sólido multiplataforma (ej. Illustrator, visores de imágenes).
  3. **Compatibilidad con Tablas Markdown (`\vert`)**: Se reconfiguró `TextNode` y `BracketNode` para interceptar barras literales de valor absoluto (`|`) y exportarlas siempre como `\vert` (o `\left\vert`), evitando que destruyan las tablas estructurales en Obsidian/Jupyter.
  4. **Corrección de Miniaturas Vacías SVG (`defs`)**: Se parcheó la clonación JS en `katex_preview.html` (`getFormulaSVG()`) para que el caché de la paleta absorba obligatoriamente la lista `<defs>` de MathJax, evitando que las plantillas en los menús y botones aparezcan como rectángulos vacíos (`\square`).

## Sesión: Parche Crítico de Compatibilidad SVG para PySide6 TinySVG (2026-08-11 00:31)

- **[2026-08-11 00:31] Corrección de Renderizado de Plantillas SVG:**
  1. **Eliminación de Dimensiones `ex`/`em`:** Se modificó `getFormulaSVG(themeText)` en `src/assets/katex_preview.html` para remover los atributos `width` y `height` del nodo SVG clonado, permitiendo que `QSvgRenderer` (basado en TinySVG) escale adecuadamente la geometría utilizando únicamente el atributo `viewBox`.
  2. **Reemplazo Directo de `currentColor`:** Se inyectó el parámetro `themeText` en `renderMathSync` y se aplicó un reemplazo con expresión regular (`replace(/currentColor/g, themeText)`) para que los glifos adopten el color hexadecimal exacto del tema en lugar de la variable CSS no soportada.
  3. **Pruebas:** 18/18 tests unitarios pasados exitosamente.

- **[2026-08-11 00:34] Limpieza de Código y Linter Flake8 (`palette_widget.py`):**
  1. **Corrección de Importaciones:** Eliminación de importaciones no utilizadas (`QButtonGroup`, `QWebEngineView`, `QWebChannel`, `MathNode`), unificación de imports duplicados de `os` y `json`.
  2. **Estándar PEP 8 y Formato:** Formateo de líneas que superaban los 79 caracteres (`E501`), eliminación de espacios en líneas vacías (`W293`, `W391`), corrección de múltiples instrucciones por línea (`E701`) y renombramiento de variables ambiguas (`l` -> `latex_str`).
  3. **Pruebas:** 18/18 tests unitarios pasados exitosamente.

- **[2026-08-11 00:37] Modularización y Compatibilidad de Enums Qt6/PySide6 (`palette_widget.py`):**
  1. **Nombres de Espacio de Enums Qt6:** Migración completa de atributos legacy (`Qt.transparent`, `Qt.PointingHandCursor`, `Qt.AlignCenter`, `Qt.LeftButton`, `QSizePolicy.Expanding`, `Qt.CustomContextMenu`) a sus clases explicitadas de PySide6 (`Qt.GlobalColor.transparent`, `Qt.CursorShape.PointingHandCursor`, `Qt.AlignmentFlag.AlignCenter`, `Qt.MouseButton.LeftButton`, `QSizePolicy.Policy.Expanding`, `Qt.ContextMenuPolicy.CustomContextMenu`), eliminando advertencias de Pylance `reportAttributeAccessIssue`.
  2. **Modularización:** Extracción del constructor de botones de símbolos a la función reutilizable `_create_symbol_button()` y los paneles a `_create_scroll_tab()`, reduciendo la duplicación de código.
  3. **Resguardo de Excepciones:** Sustitución de `except Exception:` por `except (OSError, json.JSONDecodeError):` y validación de nulidad `item is not None` en `_clear_layout()` para eliminar advertencias `Ruff` (BLE001, S110) y Pylance (`reportOptionalMemberAccess`). Pruebas superadas (18/18).

## Sesión: Corrección de motor MathJax SVG para compatibilidad TinySVG de Qt (2026-08-17 21:44)

- **[2026-08-17 21:44] Corrección de MathJax `fontCache`:** Modificación de `mathjax_build/index.js` reemplazando `fontCache: 'local'` por `fontCache: 'none'`. Esto deshabilita el caché global de geometrías SVG (`<use href="...">`) y anidamiento de sub-`<svg>`, emitiendo rutas puras (`path`) planas e independientes.
- **[2026-08-17 21:44] Refactorización de Inyección CSS SVG:** Adaptada la inyección de `styleNode` en `mathjax_build/index.js` para aplicarse directamente sobre el cierre `</svg>` en vez de `</defs>`, asegurando el coloreado de sintaxis sin depender del nodo de caché.
- **[2026-08-17 21:44] Resolución de Advertencias en Consola (`QSvgRenderer`):** La estructura plana del nuevo formato soluciona inmediatamente las advertencias de Qt (`Invalid path data`, `link is undefined!`, `Skipping a nested svg element` y `QFont::setPointSize`) causadas por las limitaciones del parser nativo de Qt en estándar SVG Tiny 1.2.

## Sesión: Diagnóstico de Inicio, Carga Perezosa de MiniRacer y Feedback en Lanzador (2026-08-18 16:30)

- **[2026-08-18 16:30] Diagnóstico de Traza `KeyboardInterrupt`:** Se identificó que la interrupción ocurrió al presionar `Ctrl+C` durante la inspección de firmas de `shibokensupport` en Python 3.14 mientras se resolvía la importación ávida de `py_mini_racer` / `asyncio`.
- **[2026-08-18 16:30] Carga Perezosa (Lazy Import) en `svg_cache.py`:** Se trasladó `from py_mini_racer import MiniRacer` al interior del método `_ensure_v8_initialized()`, evitando que PySide6 y Shiboken intercepten e inspeccionen los módulos estándar durante el arranque inicial. Esto redujo el tiempo de carga e importación a 0.31s.
- **[2026-08-18 16:30] Mejora de UX en `run_app.bat`:** Se incorporó un mensaje explícito de inicialización (`Iniciando Traductor Mates...`) para evitar la percepción de bloqueo en consola.

## Sesión: Zoom Dinámico Adaptativo en Vista Previa y Expansión Vertical de Ejemplos (2026-08-18 16:38)

- **[2026-08-18 16:38] Zoom Dinámico Adaptativo (`SVGMathCache.get_dynamic_preview_pixmap`):** Se reemplazó el renderizado rígido de `140x60` por un algoritmo de zoom adaptativo que inicia con una escala prominente (escala base ~0.16) para expresiones cortas y simples, y decae suavemente ($w\_factor^{0.38} \cdot h\_factor^{0.28}$) conforme se añaden términos, matrices y símbolos, manteniendo la fórmula centrada y nítida.
- **[2026-08-18 16:38] Integración en `MathPreviewPanel`:** Se conectó `get_dynamic_preview_pixmap()` en `update_preview()`, eliminando el renderizado miniatura en la pantalla principal de previsualización.
- **[2026-08-18 16:38] Expansión Vertical del Catálogo de Ejemplos:** Se ajustaron los divisores (`left_splitter` a `[380, 360]` y `right_splitter` a `[400, 340]`), se incrementó la altura mínima de las tarjetas de ejemplos en `palette_widget.py` a 68px, se ampliaron márgenes/relleno y se escalaron los iconos de vista previa a `180x54`.
- **[2026-08-18 16:38] Pruebas Unitarias:** Se añadieron tests de escalado dinámico en `test_editor_widget.py` (26/26 pruebas pasadas en 0.40s).

## Sesión: Corrección de Exportación de Imágenes PNG y SVG Vectorial (2026-08-18 16:46)

## Sesión: Refactorización Completa de Sintaxis Semántica Hatsune Miku (2026-08-18 17:12)

- **[2026-08-18 17:12] Eliminación de Fatiga Cromática y Colores Puros:**
  - Se eliminaron por completo el rojo `#FF0000` y el verde puro `#00FF00` de las fórmulas, editor y vistas de código.
- **[2026-08-18 17:12] Implementación de Tokens Sintácticos Semánticos Miku (Dark Studio & Light Canvas):**
  - **Modo Oscuro (Dark Studio):** Variables en Rosa Coral Miku (`#FF7597`), Números/Constantes en Verde Menta Suave (`#70D6A3`), Operadores en Cian Miku Brillante (`#56D8CD`), Comandos en Lavanda Eléctrico (`#C084FC`), Delimitadores/Estructura en Gris Acero Azulado (`#828DA4`), y Borde activo de casillas en `#39C5BB`.
  - **Modo Claro (Light Canvas):** Variables en Magenta Profundo (`#C2185B`), Números/Constantes en Menta Bosque (`#0D8A72`), Operadores en Cian Profundo/Océano (`#00838F`), Comandos en Púrpura Imperial (`#6D28D9`), Delimitadores en Gris Pizarra Neutro (`#475569`), y Borde activo en `#00A396`.
- **[2026-08-18 17:12] Sincronización Integral 1:1 en Componentes:**
  - `src/ui/theme.py`: Registrados todos los tokens semánticos en `THEMES["dark"]` y `THEMES["light"]`.
  - `src/core/syntax.py`: Refactorizado con `SYNTAX_COLORS`, `get_token_color(token, theme)`, `format_highlighted_html(text, theme)` y `LaTeXSyntaxHighlighter` con soporte dinámico para `set_theme(theme)`.
  - `src/ui/components/editor_widget.py`: `SlotBoxWidget`, `SlotContainerWidget`, `MathCanvasWidget` y `MathEditorWidget` adaptados dinámicamente al tema activo con método `set_theme(theme)`.
  - `src/ui/components/code_panel.py`: Pestañas y resaltadores LaTeX/Markdown actualizados dinámicamente con `set_theme(theme)`.
  - `src/ui/main_window.py`: Alternancia de temas (`_on_theme_toggled`) propagada reactivamente a todos los paneles.
- **[2026-08-18 17:14] Corrección de Importación y Layout en `CodeTranslationPanel`:**
  - Se importó `COLOR_MIKU_CYAN` y `get_theme_dict` desde `src.ui.theme` en `code_panel.py`.
  - Se restauró la asignación de botones de copiado (`btn_layout`) dentro del constructor `__init__`.
  - Se añadió la prueba `test_main_window_lifecycle_and_theme_toggle` en `tests/test_editor_widget.py` (29/29 pruebas pasadas en 0.90s).

## Sesión: Sincronización de Superficies y Renderizado en Modo Claro (2026-08-18 17:24)

- **[2026-08-18 17:24] Sincronización Integral de Superficies y Renderizado en Modo Claro:**
  - **Tokens de Superficie:** Se añadieron tokens `bg_canvas_editor`, `bg_canvas_render`, `bg_subpanel`, `bg_item_card`, `bg_item_card_hover`, `border_subtle`, `border_grid_dots` y `text_rendered_math` a `THEMES["dark"]` y `THEMES["light"]` en `src/ui/theme.py`.
  - **Sección 1 (Visualización Renderizada):** `MathPreviewPanel` actualizado con `set_theme()` y `_update_theme_ui()`, aplicando lienzo claro `#F8FAFC`, trazos oscuros de alto contraste `#0F172A` para MathJax/SVG, y estilización dinámica de controles de zoom y menú de exportación.
  - **Sección 2 (Editor Interactivo):** `MathCanvasWidget` rellena el lienzo con `#FFFFFF` y cuadrícula de puntos tenue `#CBD5E1` en modo claro. `MathEditorWidget` sincroniza scroll area y cajas de casillas con bordes adaptables.
  - **Sección 3 (Paleta de Plantillas y Símbolos):** `MathPaletteWidget` y `TemplateCardOption` actualizan dinámicamente ribbon buttons, tabs, context menus y tarjetas de ejemplos/fórmulas predefinidas con fondo `#FFFFFF` y renderizado de texto/glifos oscuros sobre fondo claro.
  - **Ventana Principal:** `MainWindow._on_theme_toggled` propaga `update_theme()` y `set_theme()` a todos los componentes hijos (`palette_widget`, `editor_widget`, `code_panel`, `preview_panel`, `action_bar`).
  - **Verificación:** 29/29 pruebas unitarias pasando al 100% en `pytest`.

## Sesión: Balance de Cuadrantes (25%), Selector de Tamaño de Fuente y Escalado de Casillas (2026-08-18 17:34)

- **[2026-08-18 17:34] Distribución Equitativa de Paneles (25% cada uno):**
  - Configuración de `main_splitter`, `left_splitter` y `right_splitter` con proporciones 50/50 y factores de estiramiento `(1, 1)` en `src/ui/main_window.py`.
  - Implementación de `showEvent()` para calcular y balancear automáticamente los 4 paneles en cuadrantes exactos de 1/4 del área total.
- **[2026-08-18 17:34] Menú de Tamaño de Fuente en Traducción (Estilo Word, defecto 16 pt):**
  - Añadido selector `QComboBox` (`[10, 11, 12, 13, 14, 16, 18, 20, 24, 28, 32] pt`) en la cabecera de `CodeTranslationPanel` en `src/ui/components/code_panel.py`.
  - Tamaño por defecto configurado en **16 pt** (similar a Microsoft Word) con aplicación reactiva a `latex_edit` y `markdown_edit`.
- **[2026-08-18 17:34] Aumento de Tamaño de Fórmula y Casillas Editables en Editor Interactivo:**
  - `MathEditorWidget.base_font_size` incrementado a **32px** en `src/ui/components/editor_widget.py`.
  - `SlotBoxWidget` rediseñado con casillas más amplias (`min_w=32px`, `min_h=42px`, `max_w=58px`) y símbolos de relleno `[ □ ]` aumentados para una edición interactiva más ergonómica.
- **[2026-08-18 17:34] Verificación:**
  - 31/31 pruebas unitarias pasadas al 100% en 1.25s (`pytest`).

## Sesión: Ampliación del Formulario y Subpestañas Verticales de Matemáticas y Física (2026-08-18 17:41)

- **[2026-08-18 17:41] Renombrado de Pestaña a "Formulario":**
  - Se cambió el nombre de la tercera pestaña de la paleta de `"📚 Ejemplos"` a `"📚 Formulario"`.
- **[2026-08-18 17:41] Subpestañas Verticales (Matemáticas / Física):**
  - Se implementó una barra lateral izquierda en la pestaña Formulario con dos subpestañas verticales: `[ 📐 Matemáticas ]` y `[ ⚛️ Física ]`.
  - Se añadieron los métodos `_set_domain(domain)` y `_update_subtab_style()` en `MathPaletteWidget` para alternar dinámicamente el catálogo mostrado y sincronizar los estilos con el tema activo.
- **[2026-08-18 17:41] Reestructuración en Ramas Únicas y Ampliación de Fórmulas:**
  - Se expandió el catálogo `PRESET_FORMULAS` en `src/data/symbols.py` a **58 fórmulas fundamentales** distribuidas en 11 ramas específicas:
    - **Matemáticas (5 ramas):** Álgebra y Ecuaciones, Trigonometría y Geometría, Cálculo Diferencial e Integral, Álgebra Lineal y Matrices, Estadística y Probabilidad.
    - **Física (6 ramas):** Cinemática y Movimiento, Dinámica y Leyes de Newton, Trabajo, Energía y Potencia, Electromagnetismo y Circuitos, Termodinámica y Fluidos, Ondas, Óptica y Cuántica.
  - Cada categoría/rama se despliega como una sección acordeón independiente y limpia.
- **[2026-08-18 17:41] Verificación:**
  - Todas las 58 fórmulas parsean y construyen árboles AST válidos sin errores.
  - 32/32 pruebas unitarias pasadas al 100% en 1.57s (`pytest`).

## Sesión: Corrección de Delimitadores de Corchetes, Soporte de Comando `\text` y Simbología Física (2026-08-18 17:56)

- **[2026-08-18 17:56] Corrección de Truncamiento por Corchetes `]` en `LaTeXParser`:**
  - **Causa Raíz:** En `_LaTeXStreamParser.parse_slot()`, la condición `if ch in "}]": break` provocaba que cualquier corchete de cierre `]` (como en `\mathbb{E}[X]`) detuviera prematuramente el análisis del slot raíz, truncando el resto de la fórmula.
  - **Solución:** Se limitó la condición de detención general exclusivamente a `ch == "}"`, y se suministró `stop_tokens={"]"}` explícitamente en el parser de índice de `\sqrt[n]{x}`. Ahora fórmulas con corchetes anidados o literales como `\mathbb{E}[X] = \sum_{i} x_i P(X = x_i)` se analizan y traducen completas.
- **[2026-08-18 17:56] Soporte de Comando de Texto `\text{...}` (Ecuación de Bernoulli):**
  - **Causa Raíz:** El comando `\text` no estaba en `STYLE_CMDS`, provocando que `\text{cte}` se parseara erróneamente como un comando suelto `\textcte` no reconocido por MathJax.
  - **Solución:** Se incorporó `"text"` a `STYLE_CMDS` en `src/core/parser.py`, se integró en `style_map` dentro de `StyleDecoratorNode.to_display_text()` en `src/core/ast.py`, y se añadió el soporte de renderizado en `MathEditorWidget._render_node_into_layout()`.
- **[2026-08-18 17:56] Ampliación de Simbología y Plantillas para Física:**
  - Se añadieron plantillas de vectores y derivadas (`\vec`, `\hat`, `\dot`, `\ddot`, `\mathbf`) a la categoría `"physics"` en `src/data/symbols.py`.
  - Se agregaron operadores y constantes físicas (`\hbar`, `\nabla`, `\partial`, `\oint`, `\iint`, `\iiint`, `\propto`, `\perp`, `\parallel`, `^\circ`, `\Omega`, `\dagger`, `\varepsilon_0`, `\mu_0`) en `SYMBOLS`.
  - Se verificó que el motor MathJax renderiza el 100% de la simbología física en SVG sin fallos.
- **[2026-08-18 17:56] Verificación:**
  - 35/35 pruebas unitarias pasadas al 100% en 1.56s (`pytest`).

## Sesión: Integrales Rellenables en Física, Separación de Límites y Reordenación de Pestañas (2026-08-18 18:08)

- **[2026-08-18 18:08] Integrales Rellenables con Límites en Física (`ContourIntegralNode`, `DoubleIntegralNode`, `TripleIntegralNode`):**
  - Se eliminaron los comandos `\oint`, `\iint`, `\iiint` de la lista de símbolos planos `SYMBOLS`.
  - Se crearon los nodos AST interactivos `ContourIntegralNode`, `DoubleIntegralNode` y `TripleIntegralNode` en `src/core/ast.py` y se añadieron como plantillas rellenables (`contour_integral`, `double_integral`, `triple_integral`) en `TEMPLATES` en `src/data/symbols.py`.
  - Se integró su soporte en `_LaTeXStreamParser` en `src/core/parser.py`.
- **[2026-08-18 18:08] Separación y Separador Holgado para Límites de Integral:**
  - En `AdaptiveIntegralWidget` (`src/ui/components/bracket_widget.py`) y `MathEditorWidget._render_node_into_layout()` (`src/ui/components/editor_widget.py`), se rediseñó el apilado vertical de límites (`sym_v`) con márgenes y espaciados generosos (`setContentsMargins(sym_margin, 2, 4, 2)`, espaciado entre límites y glifo), garantizando que las casillas superior e inferior nunca colisionen ni se encimen con los símbolos $\int$, $\oint$, $\iint$, $\iiint$.
- **[2026-08-18 18:08] Reordenación de Pestañas y Nueva Pestaña de Letras Griegas:**
  - Se reestructuró la barra de pestañas en `MathPaletteWidget` en el orden exacto solicitado:
    1. **`⭐ Favoritos`** (índice 0)
    2. **`📚 Formulario`** (índice 1, a la derecha de favoritos)
    3. **`🔤 Básicos`** (índice 2)
    4. **`🏛️ Letras Griegas`** (índice 3, pestaña dedicada con `_build_greek_grid()`)
  - Se retiró "Letras Griegas" del menú desplegable del Ribbon (para que no esté duplicada) y se amplió el catálogo de caracteres griegos en `src/data/symbols.py` (`\varphi`, `\varrho`, `\varkappa`, `\varpi`, `\varsigma`, `\upsilon`, `\Upsilon`, etc.).
- **[2026-08-18 18:08] Verificación:**
  - 36/36 pruebas unitarias pasadas al 100% en 1.80s (`pytest`).

## Sesión: Límite Vertical de Integral (Barrera 6px) y Corrección de Truncamiento Superior del Glifo (2026-08-18 18:17)

- **[2026-08-18 18:17] Corrección del Truncamiento Superior del Símbolo de Integral:**
  - **Causa Raíz:** El glifo extensible de integral en fuentes matemáticas (como Cambria Math) posee un ascenso de curva superior que se proyecta significativamente por encima de la línea de ascenso estándar del tipo de letra. Al pintarse en un rectángulo acotado con `drawText(AlignVCenter)`, la parte superior del gancho quedaba fuera de coordenadas (`y < 0`) y el `QPainter` la recortaba.
  - **Solución:** Se implementó la clase especializada `IntegralGraphicWidget` en `src/ui/components/bracket_widget.py`. Esta calcula la caja envolvente estricta del glifo (`tightBoundingRect`) y posiciona la línea base en `y = -tight_br.top() + pad_top` con márgenes de seguridad superior e inferior (`pad_top=4`, `pad_bottom=4`). Esto garantiza que el 100% de la curva superior e inferior se renderice completamente y sin recortes.
- **[2026-08-18 18:17] Límite Visual y Barrera Estricta de 6 Píxeles:**
  - `IntegralGraphicWidget` delimita exactamente el último píxel del gráfico de la integral a la derecha.
  - En `AdaptiveIntegralWidget` y `MathEditorWidget._render_node_into_layout()`, se estructuró la columna de límites (`limits_widget`) en un widget separado insertado con una separación física fija de **6 píxeles** (`main_layout.setSpacing(6)`).
  - Gracias a esta barrera física, las casillas de texto interactivo (`SlotBoxWidget`) nunca pueden penetrar ni acercarse a menos de 6 píxeles del borde derecho de la imagen de la integral.
- **[2026-08-18 18:17] Verificación:**
  - 37/37 pruebas unitarias pasadas al 100% en 1.90s (`pytest`).

## Sesión: Consolidación y Certificación del Pipeline de Calidad QA (2026-08-18 18:24)

- **[2026-08-18 18:23] Corrección de Importaciones y Reglas Ruff:**
  - Se importó `get_theme_dict` en [action_bar.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/ui/components/action_bar.py) para el diálogo de ayuda modal.
  - Se eliminaron imports no utilizados y se ordenaron bloques de importación en [tests/test_editor_widget.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/tests/test_editor_widget.py) y [tests/test_syntax.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/tests/test_syntax.py).
- **[2026-08-18 18:23] Certificación Pydoclint (Google Style Docstrings):**
  - Se añadió la anotación de retorno `-> None` en `MathPreviewPanel.update_preview` en [preview_panel.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/ui/components/preview_panel.py), logrando 0 infracciones en todo el proyecto.
- **[2026-08-18 18:23] Tipado Estático Mypy:**
  - Se tipó explícitamente `_rules: list[tuple[re.Pattern[str], QTextCharFormat]]` en [syntax.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/core/syntax.py), alcanzando 0 errores en los 26 archivos fuente.
- **[2026-08-18 18:24] Verificación Integral:**
  - 37/37 pruebas unitarias superadas al 100% en 1.81s (`pytest`).

## Sesión: Escalado Estándar al 125% y Optimización del Algoritmo de Zoom Adaptativo (2026-08-18 18:27)

- **[2026-08-18 18:27] Incremento de Escala Base al 125%:**
  - Se aumentó el factor de escala estándar por defecto a `base_scale = 0.15` (125% exacto respecto al valor anterior de `0.12`) en `SVGMathCache.get_dynamic_preview_pixmap` en [svg_cache.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/ui/components/svg_cache.py) y en [preview_panel.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/ui/components/preview_panel.py).
  - Esto proporciona una visualización nítida y destacada para fórmulas cortas y medianas ($E=mc^2$, $F=-kx$, cuadráticas, integrales estándar, matrices 2x2/3x3).
- **[2026-08-18 18:27] Algoritmo Adaptativo para Fórmulas Muy Largas (Norma Vectorial):**
  - Se refinó la curva de decaimiento en `get_dynamic_preview_pixmap()` introduciendo una amortiguación progresiva para fórmulas con ancho base $w_0 > 8500$ (`w_factor = ((2600.0 / 8500.0) ** 0.38) * ((8500.0 / w0) ** 0.62)`).
  - De esta manera, fórmulas extensas como la norma vectorial (`\|\mathbf{v}\| = \sqrt{v_1^2 + \dots + v_n^2}`), fórmulas de series de Taylor o fórmula de Herón reducen su escala suavemente para mantenerse dentro de proporciones armónicas y no desbordar el lienzo.
- **[2026-08-18 18:27] Verificación:**
  - Suite completa de 37 pruebas unitarias pasando al 100% en 1.74s (`pytest`).

## Sesión: Corrección de Cambio de Tamaño de Fuente Dinámico en Paneles de Traducción (2026-08-18 19:08)

- **[2026-08-18 19:08] Diagnóstico y Causa Raíz:**
  - **Sobrescritura por QSS Global:** En `src/ui/theme.py`, la regla de estilos `QPlainTextEdit.code-block` y `QWidget` definían `font-size: 13px;` de forma estática. Al evaluar el estilo en Qt, la cascada QSS tenía mayor prioridad que `widget.setFont(QFont(...))`, forzando permanentemente un tamaño de 13px e impidiendo que las selecciones del usuario en el menú desplegable cambiaran el tamaño del texto.
- **[2026-08-18 19:08] Solución e Implementación en `CodeTranslationPanel` (`code_panel.py`):**
  - **Eliminación de Tamaño Fijo en QSS Global:** Se removió `font-size: 13px;` de `QPlainTextEdit.code-block` en [theme.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/ui/theme.py).
  - **Método `_update_editor_style()`:** Se implementó en [code_panel.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/ui/components/code_panel.py) para inyectar dinámicamente el `font-size: {size}pt;` en la hoja de estilos inline de `latex_edit` y `markdown_edit`, asegurando que la tipografía monoespaciada escale visualmente de inmediato ante cualquier selección (10, 11, 12, 13, 14, 16, 18, 20, 24, 28, 32 pt) y preservando los colores semánticos y el tema activo (Modo Claro / Modo Oscuro).
  - **Sincronización `QFont` y `QTextDocument`:** Se adaptó `_apply_font_size()` para sincronizar simultáneamente `setFont()`, `document().setDefaultFont()` y la hoja de estilos de los editores.
  - **Defensa ante Objetos Qt Eliminados:** Se reforzó `clear_layout` en [qt_utils.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/utils/qt_utils.py) y `_load_favorites_grid` en [palette_widget.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/ui/components/palette_widget.py) con manejo defensivo de `RuntimeError` ante eventos en widgets cerrados.
- **[2026-08-18 19:08] Verificación y QA:**
  - `pytest`: 37/37 pruebas unitarias pasadas al 100% (incluyendo verificación interactiva de cambios de fuente 10-32 pt y alternancia de temas).
  - `pydoclint`: 0 violaciones en todos los archivos.
  - `mypy`: 0 errores de tipado estático en 27 archivos.
  - `ruff`: 0 infracciones de linter y formato.

## Sesión: Ampliación del Formulario con Compendio Completo y Jerarquía de Secciones/Subsecciones (2026-08-18 19:25)

- **[2026-08-18 19:25] Expansión del Catálogo de Fórmulas Predefinidas (`symbols.py`):**
  - Se incorporó el compendio completo de fórmulas de **Aritmética**, **Álgebra** y **Trigonometría** cubriendo los 3 niveles educativos (`[NIVEL BÁSICO]`, `[NIVEL INTERMEDIO]`, `[NIVEL UNIVERSITARIO / AVANZADO]`), así como las secciones existentes de **Cálculo Diferencial e Integral**, **Estadística y Probabilidad** y las 6 ramas de **Física** (Cinemática, Dinámica, Energía, Electromagnetismo, Termodinámica/Fluidos, Cuántica/Ondas).
  - El catálogo se expandió a más de 80 fórmulas emblemáticas en total, con metadatos completos: `category`, `level`, `subsection`, `title`, `description`, `latex` y funciones factory `builder` λ que instancian árboles AST `MathTree` válidos y parseables.
- **[2026-08-18 19:25] Jerarquía Visual y Distinción de Secciones y Subsecciones en el Formulario (`palette_widget.py`):**
  - **Secciones Principales (Acordeón):** Botones con estilo destacado, tipografía en negrita (`13px`, `700` weight), color primario Cian Miku, bordes redondeados y fondo reactivo que colapsan/expanden el contenedor de la categoría.
  - **Subsecciones con Insignias de Nivel:** Agrupación visual de fórmulas con cabeceras de subsección dedicadas que contienen un chip/badge coloreado según el nivel pedagógico:
    - `[NIVEL BÁSICO]`: Insignia Cian Miku con fondo translúcido (`rgba(57, 197, 187, 0.15)`).
    - `[NIVEL INTERMEDIO]`: Insignia Lavanda (`rgba(192, 132, 252, 0.15)`).
    - `[NIVEL UNIVERSITARIO / AVANZADO]`: Insignia Magenta Miku (`rgba(227, 50, 123, 0.15)`).
  - **Tarjetas de Fórmulas:** Botones con título en el lado izquierdo y previsualización gráfica SVG nítida en el lado derecho generada por `SVGMathCache`, con tooltip didáctico y soporte dinámico de temas claro y oscuro.
- **[2026-08-18 19:25] Pruebas y Certificación de Calidad:**
  - Nuevas pruebas unitarias añadidas en [test_editor_widget.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/tests/test_editor_widget.py): `test_compendio_formulas_structure` y `test_palette_formulario_sections_and_subsections`.
  - 39/39 pruebas unitarias superadas al 100% en `pytest`.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Mapeo y Renderizado Estructurado de Operadores y Símbolos Especiales (2026-08-18 23:45)

- **[2026-08-18 23:45] Soporte Estructurado para `\\operatorname{...}` (`parser.py`, `symbols.py`, `ast.py`):**
  - Se implementó en `_LaTeXStreamParser` el reconocimiento semántico y extracción limpia de operadores personalizados (e.g. `\\operatorname{mcd}`, `\\operatorname{mcm}`, `\\operatorname{Adj}`, `\\operatorname{sech}`).
  - Se mapean como `OperatorNode(latex_cmd=r"\\operatorname{...}", display="...")`, eliminando la salida literal de texto desformateado (`\\operatornamemcd`) y presentándose de forma interactiva y con resaltado semántico (`math_cmd_color`).
- **[2026-08-18 23:45] Plantilla de Congruencia Modular `ModularNode` (`\\pmod{m}`):**
  - Se creó el nodo `ModularNode(TemplateNode)` que encapsula el módulo dentro de una casilla editable interactiva `Slot("módulo")`.
  - En el editor interactivo se renderiza como `(mod [ m ])` permitiendo editar el módulo dinámicamente, y exporta código LaTeX limpio y estándar `\\pmod{ m }`.
- **[2026-08-18 23:45] Plantilla de Productoria `ProductNode` (`\\prod`):**
  - Se integró `ProductNode` con casillas interactivas para límites inferior (`lower`), superior (`upper`) y cuerpo (`body`).
  - Renderizado visual con símbolo tipográfico destacado `∏`, escalado adaptativo de límites y adición a la paleta de plantillas (`TEMPLATES`).
- **[2026-08-18 23:45] Catálogo Completo de Funciones y Símbolos Matemáticos:**
  - Se agregaron a `SYMBOLS` y `LATEX_TO_UNICODE` en [symbols.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/data/symbols.py) y `OPERATOR_CMDS` en [parser.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/core/parser.py):
    - Relacionales / Lógica: `\\equiv` ($≡$), `\\iff` ($⇔$), `\\implies` ($⇒$), `\\mid` ($∣$), `\\nmid` ($∤$), `\\to` ($→$), `\\leftarrow` ($←$), `\\rightarrow` ($→$), `\\leftrightarrow` ($↔$).
    - Hiperbólicas / Trigonométricas: `\\sinh`, `\\cosh`, `\\tanh`, `\\coth`, `\\sech`, `\\csch`, `\\arcsin`, `\\arccos`, `\\arctan`.
    - Álgebra / Análisis: `\\exp`, `\\gcd`, `\\deg`, `\\dim`, `\\ker`, `\\hom`, `\\inf`, `\\sup`, `\\prod`, `\\coprod`.
- **[2026-08-18 23:45] Verificación y QA:**
  - `pytest`: 42/42 pruebas unitarias pasadas al 100%.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Integración del Compendio Completo de Geometría, Geometría Analítica y Álgebra Lineal (2026-08-18 23:58)

- **[2026-08-18 23:58] Expansión del Catálogo de Fórmulas y Secciones ([symbols.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/data/symbols.py)):**
  - Se añadieron 3 nuevas ramas matemáticas principales organizadas por niveles pedagógicos (`NIVEL BÁSICO`, `NIVEL INTERMEDIO`, `NIVEL UNIVERSITARIO / AVANZADO`):
    1. **4. Geometría (Plana y del Espacio / Euclidiana)** (`math_geometry`): 35 fórmulas (Perímetros y Áreas 2D, Propiedades Angulares y Polígonos, Geometría 3D, Teoremas Métricos y Proporcionalidad de Tales/Ceva/Menelao/Potencia, Geometría no Euclidiana y Topología con Euler-Poincaré, Triángulo Esférico, Curvatura Gaussiana, Gauss-Bonnet, Razón Doble).
    2. **5. Geometría Analítica** (`math_analytic_geom`): 28 fórmulas (Plano Cartesiano 2D, Línea Recta, Distancias y Cónicas en 2D con Circunferencia, Parábola, Elipse, Hipérbola, Ecuación General y Discriminante Δ, Rotación de Ejes, Coordenadas Polares, Geometría 3D con Planos, Rectas, Distancia entre Rectas Alabeadas, Superficies Cuádricas y Coordenadas Cilíndricas/Esféricas).
    3. **6. Álgebra Lineal** (`math_linear_algebra`): 21 fórmulas (Vectores en ℝ^n, Norma L_2, Productos Punto/Cruz/Triple, Sistemas y Regla de Cramer, Multiplicación/Traza/Determinante, Subespacios, Rango-Nulidad, Cauchy-Schwarz, Ortogonalización de Gram-Schmidt, Autovalores/Autovectores, Cayley-Hamilton, Diagonalización y Teorema Espectral, Forma Canónica de Jordan, Descomposiciones LU/QR/Cholesky/SVD, Pseudoinversa de Moore-Penrose, Mínimos Cuadrados y Producto de Kronecker).
  - El catálogo total de fórmulas asciende a **209 fórmulas preestablecidas** (181 matemáticas + 28 físicas).
- **[2026-08-18 23:58] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Validación y Verificación de Directiva a.md (2026-08-19 00:01)

- **[2026-08-19 00:01] Verificación Integral de Roles y Tokens Semánticos (`a.md`):**
  - Se validó la correspondencia 1:1 de los tokens cromáticos definidos en [`a.md`](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/a.md) con [`theme.py`](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/ui/theme.py) y [`syntax.py`](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/core/syntax.py):
    - Variables: `#FF7597` (Dark) / `#C2185B` (Light)
    - Números: `#70D6A3` (Dark) / `#0D8A72` (Light)
    - Operadores: `#56D8CD` (Dark) / `#00838F` (Light)
    - Comandos: `#C084FC` (Dark) / `#6D28D9` (Light)
    - Delimitadores: `#828DA4` (Dark) / `#475569` (Light)
    - Bordes y focos de casillas: `#39C5BB` / `rgba(57, 197, 187, 0.08)` (Dark) y `#00A396` / `rgba(0, 163, 150, 0.10)` (Light).
  - Confirmación de cumplimiento de criterios de aceptación de contraste WCAG AA (> 4.5:1), eliminación de colores saturados puros y sincronización bidireccional entre el editor visual y los paneles de código LaTeX/Markdown.
- **[2026-08-19 00:01] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Integración del Compendio Completo de Cálculo Diferencial, Integral y Vectorial (2026-08-19 00:05)

- **[2026-08-19 00:05] Expansión del Catálogo de Cálculo a partir de `a.md` ([symbols.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/data/symbols.py)):**
  - Se modularizó e integró el compendio completo de Cálculo en 3 categorías temáticas organizadas por niveles pedagógicos (`NIVEL BÁSICO`, `NIVEL INTERMEDIO`, `NIVEL UNIVERSITARIO / AVANZADO`):
    1. **7. Cálculo Diferencial** (`math_diff_calculus`): 22 fórmulas (Límites y Continuidad épsilon-delta, Derivada formal por límite, Reglas algebraicas y de potencias, Producto/Cociente/Cadena, Funciones trascendentes exponenciales/logarítmicas/trigonométricas directas e inversas, Recta Tangente/Normal, Regla de L'Hôpital, Teoremas de Rolle/Lagrange/Cauchy, Derivadas hiperbólicas directas e inversas, Diferencial Total, Serie de Taylor con Resto de Lagrange, Curvatura y Radio de Curvatura).
    2. **8. Cálculo Integral** (`math_integral_calculus`): 17 fórmulas (Antiderivada y Linealidad, Integrales inmediatas de potencias/logaritmo/exponenciales/trigonométricas, Teorema Fundamental del Cálculo Parte 1/2 y Regla de Leibniz 1D, Métodos de Sustitución e Integración por Partes, Sustituciones Trigonométricas, Integrales trigonométricas logarítmicas e inversas racionales, Aplicaciones geométricas de área entre curvas, longitud de arco, volúmenes de revolución por discos/arandelas/cascarones, superficie de revolución y valor medio, Integrales Impropias, Sustitución de Weierstrass, Integrales hiperbólicas, Funciones Gamma, Beta, Integral Gaussiana y Regla de Leibniz 2D).
    3. **9. Cálculo Vectorial y Multivariable** (`math_vector_calculus`): 13 fórmulas (Cinemática vectorial de trayectorias en ℝ^3, Derivadas parciales y Teorema de Schwarz/Clairaut, Vector Gradiente ∇f, Diferencial total y Regla de la Cadena multivariable, Derivada direccional y Plano tangente, Matriz Hessiana y Multiplicadores de Lagrange, Jacobiano y diferenciales en coordenadas Polares/Cilíndricas/Esféricas, Operadores diferenciales de Divergencia div(F), Rotacional rot(F) y Laplaciano Δf, Identidades vectoriales, Integrales de línea y superficie de flujo, TFC de integrales de línea para campos conservativos, Teoremas de Green, Stokes y Divergencia de Gauss, Triedro y Fórmulas de Frenet-Serret).
  - El catálogo total asciende a **254 fórmulas preestablecidas** (226 matemáticas y 28 físicas) distribuidas en 16 categorías temáticas.
- **[2026-08-19 00:05] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Integración de Ecuaciones Diferenciales y Métodos Numéricos desde a.md (2026-08-19 00:10)

- **[2026-08-19 00:10] Expansión del Catálogo ([symbols.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/data/symbols.py)):**
  - Se añadieron 2 nuevas categorías matemáticas principales organizadas por niveles pedagógicos (`NIVEL BÁSICO`, `NIVEL INTERMEDIO`, `NIVEL UNIVERSITARIO / AVANZADO`):
    1. **10. Ecuaciones Diferenciales** (`math_diff_equations`): 22 fórmulas (Problema de Valor Inicial PVI, Teorema de Picard-Lindelöf, Variables Separables, Ecuación Lineal y Factor Integrante de Leibniz, Ecuaciones Exactas, Factores Integrantes especiales, Ecuación Homogénea, Bernoulli, Riccati y Clairaut, Ecuación Característica de 2° orden, Wronskiano y Fórmula de Abel, Variación de Parámetros, Cauchy-Euler, Transformada de Laplace y derivadas, Traslación/Convolución/Delta de Dirac, Series de Frobenius, Ecuaciones de Bessel y Legendre, Sistemas matriciales lineales y matriz exponencial, EDPs clásicas de Onda/Calor/Laplace, Soluciones de d'Alembert y Núcleo del calor, Problemas de Sturm-Liouville y Ortogonalidad).
    2. **11. Métodos Numéricos** (`math_numerical_methods`): 18 fórmulas (Teoría de Errores absoluto/relativo/aproximado, Bisección y cota teórica, Falsa Posición, Iteración de Punto Fijo, Newton-Raphson, Secante y Newton multivariable con Jacobiano, Métodos iterativos de Jacobi y Gauss-Seidel, Método SOR, Interpolación de Lagrange y Newton en diferencias divididas, Regresión Lineal por Mínimos Cuadrados, Diferencias Finitas de 1° y 2° orden, Fórmulas de Newton-Cotes de Trapecio y Simpson 1/3 y 3/8, Cuadratura Gauss-Legendre, Métodos de Euler y Heun, Runge-Kutta RK4, Métodos Multipaso de Adams-Bashforth y Adams-Moulton, Problemas de Valor en la Frontera por Disparo y Diferencias Finitas tridiagonales, Diferencias Finitas para EDPs y Condición CFL).
  - El catálogo global de la aplicación ahora cuenta con **294 fórmulas preestablecidas** (266 matemáticas y 28 físicas) organizadas en 18 categorías temáticas completas.
- **[2026-08-19 00:10] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Integración del Compendio Completo de Mecánica Clásica, Fluidos y Analítica (2026-08-19 00:16)

- **[2026-08-19 00:16] Expansión del Catálogo de Física ([symbols.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/data/symbols.py)):**
  - Se modularizó e integró el compendio completo de Mecánica en 4 categorías temáticas organizadas por niveles pedagógicos (`NIVEL BÁSICO`, `NIVEL INTERMEDIO`, `NIVEL UNIVERSITARIO / AVANZADO`):
    1. **1. Cinemática y Dinámica Newtoniana** (`phys_kinematics_dynamics`): 9 fórmulas (MRU posición y velocidad media, MRUA y Torricelli, Leyes de Newton de inercia, dinámica y acción-reacción, Fuerzas de fricción estática y cinética, MCU y MCUV con aceleración centrípeta, Cinemática vectorial 3D con aceleración intrínseca tangencial/normal y polares planas, Fuerzas ficticias en sistemas no inerciales con Coriolis y Centrífuga, Dinámica rotacional con torque, inercia y teoremas de Steiner y ejes perpendiculares, Tensor de Inercia 3D y Ecuaciones de Euler para el sólido rígido).
    2. **2. Trabajo, Energía, Momento y Gravitación** (`phys_energy_gravitation`): 6 fórmulas (Trabajo y teorema de la energía cinética, Energías potenciales gravitatoria y elástica con balance no conservativo, Momento lineal, impulso y coeficiente de restitución de choques, Fuerzas conservativas F = -∇U, centro de masas y teoremas de König, Gravitación universal, leyes de Kepler y velocidades orbital/escape, Problema de dos cuerpos con masa reducida, potencial efectivo, ecuación de Binet y cónicas orbitales).
    3. **3. Oscilaciones y Mecánica de Fluidos** (`phys_fluids_oscillations`): 5 fórmulas (M.A.S. masa-resorte y péndulos simple/físico, Presión hidrostática, principios de Pascal y Arquímedes, Oscilaciones amortiguadas, factor Q y régimen forzado en resonancia, Ecuaciones de continuidad, Bernoulli y Torricelli para fluidos ideales, Continuidad diferencial, ecuaciones de Navier-Stokes para fluidos viscosos y tensor de esfuerzos de Cauchy).
    4. **4. Mecánica Analítica y Relativista** (`phys_analytical_relativity`): 4 fórmulas (Mecánica Lagrangiana con función L = T - V, principio de Hamilton, ecuaciones de Euler-Lagrange, momento canónico y teorema de Noether, Mecánica Hamiltoniana con transformada de Legendre y ecuaciones canónicas, Formulaciones canónicas avanzadas con corchetes de Poisson, teorema de Liouville y ecuación de Hamilton-Jacobi, Mecánica Relativista con factor de Lorentz, momento/fuerza relativista, relación energía-momento y cuadrivectores).
  - El catálogo global de la aplicación ahora cuenta con **306 fórmulas preestablecidas** (266 matemáticas y 40 de física) organizadas en 19 categorías temáticas completas.
- **[2026-08-19 00:16] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Integración del Compendio de Oscilaciones y Ondas Mecánicas (2026-08-19 00:20)

- **[2026-08-19 00:20] Expansión del Catálogo de Física ([symbols.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/data/symbols.py)):**
  - Se modularizó e integró el compendio completo de Oscilaciones y Ondas Mecánicas en categorías físicas dedicadas estructuradas por niveles pedagógicos (`NIVEL BÁSICO`, `NIVEL INTERMEDIO`, `NIVEL UNIVERSITARIO / AVANZADO`):
    1. **3. Movimiento Oscilatorio** (`phys_oscillations`): 9 fórmulas (Cinemática del M.A.S. de posición/velocidad/aceleración, Parámetros temporales y frecuenciales T/f/ω, Conservación de energía mecánica del M.A.S. 1/2 k A², Sistemas oscilatorios simples de masa-resorte y péndulo simple, Péndulos físico y de torsión, Oscilaciones amortiguadas con decremento logarítmico y factor Q, Oscilaciones forzadas con resonancia y potencia media, Osciladores acoplados y modos normales matriciales, Péndulo no lineal con integrales elípticas de Borda y ecuación de Van der Pol).
    2. **4. Ondas Mecánicas y Acústica** (`phys_waves_acoustics`): 11 fórmulas (Cinemática de ondas armónicas 1D y relaciones v = λf = ω/k, Superposición, interferencia constructiva/destructiva y batidos, Escala decibélica de nivel de sonido y presión SPL, Ecuación diferencial de onda 1D y solución de d'Alembert, Velocidad de onda en cuerdas/sólidos/fluidos/gases ideales, Transporte de energía, potencia promedio e intensidad con ley del inverso del cuadrado, Ondas estacionarias y modos normales en cuerdas y tubos sonoros, Efecto Doppler clásico y cono de Mach, Dispersión con velocidad de fase/grupo e impedancia mecánica en fronteras, Ondas sísmicas y elásticas 3D P y S, Acústica física de ondas de presión, ecuación 3D y Doppler vectorial).
    3. **5. Mecánica de Fluidos** (`phys_fluids`): 3 fórmulas (Estática de fluidos con presión hidrostática, Pascal y Arquímedes, Dinámica de fluidos ideales con continuidad, Bernoulli y Torricelli, Mecánica de medios continuos con continuidad diferencial, Navier-Stokes y tensor de Cauchy).
  - El catálogo global de la aplicación ahora cuenta con **324 fórmulas preestablecidas** (266 matemáticas y 58 de física) organizadas en 21 categorías temáticas completas.
- **[2026-08-19 00:20] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Integración del Compendio Completo de Termodinámica Clásica y Estadística (2026-08-19 00:25)

- **[2026-08-19 00:25] Expansión del Catálogo de Física ([symbols.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/data/symbols.py)):**
  - Se modularizó e integró el compendio completo de Termodinámica en la categoría dedicada `7. Termodinámica Clásica y Estadística` (`phys_thermodynamics`): 18 fórmulas estructuradas por niveles pedagógicos (`NIVEL BÁSICO`, `NIVEL INTERMEDIO`, `NIVEL UNIVERSITARIO / AVANZADO`):
    - Escalas de temperatura Celsius/Kelvin/Fahrenheit y dilatación térmica lineal, superficial y volumétrica.
    - Calorimetría de calor sensible Q = mcΔT, calor latente de cambio de fase Q = mL y equilibrio térmico.
    - Gas ideal PV = nRT y leyes empíricas de Boyle, Charles, Gay-Lussac y ley combinada.
    - Primera Ley en sistemas cerrados ΔU = Q - W, diferencial dU = δQ - PdV y trabajo cuasiestático W = ∫ P dV.
    - Procesos en gases ideales isocórico, isobárico, isotérmico, adiabático reversible PV^γ = cte y relación de Mayer C_p - C_v = R.
    - Mezclas de gases con leyes de Dalton y Amagat, coeficientes termoelásticos de dilatación isobárica α, compresibilidad isotérmica κ_T y piezométrico β_P.
    - Gases reales con ecuación de Van der Waals, constantes críticas T_c, P_c, factor de compresibilidad Z y expansión virial.
    - Procesos politrópicos PV^n = cte, trabajo de expansión y capacidad calorífica politrópica C_n.
    - Segunda Ley con definición de entropía de Clausius, desigualdad de Clausius, incremento de entropía y variación en gases y mezclas.
    - Máquinas térmicas con eficiencia de Carnot, COP de refrigeradores y bombas de calor, ciclos Otto, Diesel y Brayton.
    - Potenciales termodinámicos U, H, F, G con las 4 relaciones canónicas de Maxwell.
    - Ecuaciones fundamentales T dS y relación universal de calores específicos C_p - C_v = T V α² / κ_T.
    - Teoría cinética molecular con presión cinética P = 1/3 ρ v_rms², velocidades cuadrática media/promedio/más probable y distribución de Maxwell-Boltzmann.
    - Sistemas abiertos en volumen de control con conservación de masa, primera/segunda ley y análisis exergético con teorema de Gouy-Stodola.
    - Coeficiente de expansión isoentálpica de Joule-Thomson μ_JT y ecuación de Gibbs-Duhem con potencial químico.
    - Transiciones de fase con ecuaciones de Clapeyron y Clausius-Clapeyron, regla de las fases de Gibbs F = C - P + 2 e isoterma de Van 't Hoff.
    - Termodinámica estadística con entropía de Boltzmann S = k_B ln Ω, función de partición canónica Z y gran canónica Ξ con gran potencial Φ_G.
    - Estadísticas cuánticas de Fermi-Dirac con energía de Fermi E_F y Bose-Einstein con temperatura de condensación crítica T_c.
  - El catálogo global de la aplicación ahora cuenta con **338 fórmulas preestablecidas** (266 matemáticas y 72 de física) organizadas en 21 categorías temáticas completas.
- **[2026-08-19 00:25] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Integración del Compendio Completo de Electricidad y Magnetismo (2026-08-19 00:30)

- **[2026-08-19 00:30] Expansión del Catálogo de Física ([symbols.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/data/symbols.py)):**
  - Se modularizó e integró el compendio completo de Electricidad y Magnetismo en la categoría dedicada `8. Electromagnetismo y Circuitos` (`phys_electromagnetism`): 17 fórmulas estructuradas por niveles pedagógicos (`NIVEL BÁSICO`, `NIVEL INTERMEDIO`, `NIVEL UNIVERSITARIO / AVANZADO`):
    - Ley de Coulomb y fuerza electrostática vectorial entre cargas puntuales.
    - Campo eléctrico, potencial escalar electrostático y energía potencial de cargas.
    - Capacitancia general C = Q/V, condensadores de placas plano-paralelas, cilíndrico, esférico y energía electrostática almacenada.
    - Flujo eléctrico y Ley de Gauss en forma integral, relación diferencial de gradiente E = -∇V.
    - Dipolo eléctrico con momento p = qd, torque τ = p × E y medios dieléctricos con vector desplazamiento D = ε E y polarización P.
    - Ecuaciones diferenciales de Poisson y Laplace (∇²V = -ρ/ε0), condiciones de frontera electrostáticas y expansión multipolar del potencial.
    - Corriente eléctrica, Ley de Ohm macroscópica V = IR, efecto Joule y leyes de Kirchhoff para nodos y mallas.
    - Densidad de corriente microscópica J = σ E (modelo de Drude) y transitorios de primer orden RC y RL en DC.
    - Ecuación de continuidad local de la carga ∇·J + ∂ρ/∂t = 0 y análisis fasorial en régimen senoidal permanente (AC) con impedancia compleja y potencia compleja S = P + jQ.
    - Fuerza magnética de Lorentz F = q(E + v × B), movimiento ciclotrónico, fuerza sobre hilos con corriente y dipolo magnético.
    - Leyes de Biot-Savart, Ampère en forma integral, solenoide, intensidad magnética H y susceptibilidad magnética χ_m.
    - Divergencia nula ∇·B = 0, potencial vector magnético A (∇²A = -μ0 J) y densidad de energía magnetostática u_m = 1/2 B·H.
    - Ley de Faraday-Lenz de inducción electromagnética, FEM de movimiento E = B L v y autoinductancia con energía en inductores.
    - Ley de Ampère-Maxwell con corriente de desplazamiento I_d = ε0 dΦ_E/dt, 4 ecuaciones integrales de Maxwell y vector de Poynting S = E × H.
    - Ecuaciones de Maxwell diferenciales (microscópicas y macroscópicas), condición de calibre de Lorenz y potenciales retardados de Liénard-Wiechert.
    - Ondas electromagnéticas planas en el vacío, velocidad de la luz c = 1/√(μ0 ε0), impedancia intrínseca η0 ≈ 377 Ω y tensor de esfuerzos de Maxwell T_ij.
    - Formulación covariante / cuadrivectorial con cuadrivectores J^μ, A^μ, tensor de campo de Faraday F^μν, ecuaciones de Maxwell covariantes e invariantes de Lorentz.
  - El catálogo global de la aplicación ahora cuenta con **349 fórmulas preestablecidas** (266 matemáticas y 83 de física) organizadas en 21 categorías temáticas completas.
- **[2026-08-19 00:30] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Integración del Compendio Completo de Óptica y Fotónica (2026-08-19 00:35)

- **[2026-08-19 00:35] Expansión del Catálogo de Física ([symbols.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/data/symbols.py)):**
  - Se modularizó e integró el compendio completo de Óptica en la categoría dedicada `9. Óptica y Fotónica` (`phys_optics`): 15 fórmulas estructuradas por niveles pedagógicos (`NIVEL BÁSICO`, `NIVEL INTERMEDIO`, `NIVEL UNIVERSITARIO / AVANZADO`):
    - Propagación de la luz n = c/v, reflexión, ley de Snell y ángulo crítico de reflexión interna total.
    - Espejos esféricos con distancia focal f = R/2, ecuación de Descartes y aumento lateral transversal m = -si/so.
    - Dioptrio esférico, fórmula del fabricante de lentes 1/f = (n-1)(1/R1 - 1/R2), ecuación de Gauss y potencia en dioptrías.
    - Prismas y dispersión cromática con desviación angular δ, ángulo de mínima desviación y número de Abbe V_d.
    - Óptica matricial ABCD para rayos paraxiales, principio variacional de Fermat y ecuación de la eikonal |∇S|² = n².
    - Experimento de la doble rendija de Young, separación de franjas, ley de Malus y ángulo de Brewster.
    - Interferencia en películas delgadas, anillos de Newton, difracción de Fraunhofer (sinc² y criterio de Rayleigh).
    - Redes de difracción (poder de resolución R = mN) y ecuaciones de Fresnel para interfaces dieléctricas.
    - Teoría escalar de difracción (número de Fresnel N_F), vectores de Jones, parámetros de Stokes y birrefringencia.
    - Dispersión cromática con ecuación de Sellmeier, velocidad de grupo vg = c/ng e índice de refracción complejo con Beer-Lambert.
    - Relaciones de Kramers-Kronig, apertura numérica NA en fibras ópticas, parámetro V y ondas evanescentes con desplazamiento Goos-Hänchen.
    - Energía y momento del fotón (Planck-Einstein / de Broglie), efecto fotoeléctrico y presión de radiación.
    - Radiación de cuerpo negro (Planck, Wien, Stefan-Boltzmann) y física del láser con coeficientes de Einstein y umbral de cavidad.
    - Propagación de haces Gaussianos TEM00, parámetro de Rayleigh z_R, radio de cintura w(z), curvatura R(z) y ley ABCD.
    - Óptica no lineal con polarización no lineal, generación de segundo armónico SHG con phase matching y efectos electro-ópticos Kerr y Pockels.
  - El catálogo global de la aplicación ahora cuenta con **364 fórmulas preestablecidas** (266 matemáticas y 98 de física) organizadas en 22 categorías temáticas completas.
- **[2026-08-19 00:35] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Integración del Compendio Completo de Física Moderna, Cuántica y Nuclear (2026-08-19 00:40)

- **[2026-08-19 00:40] Expansión del Catálogo de Física ([symbols.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/data/symbols.py)):**
  - Se modularizó e integró el compendio completo de Física Moderna en la categoría dedicada `10. Física Cuántica y Moderna` (`phys_modern`): 14 fórmulas estructuradas por niveles pedagógicos (`NIVEL BÁSICO`, `NIVEL INTERMEDIO`, `NIVEL UNIVERSITARIO / AVANZADO`):
    - Dilatación temporal, contracción de la longitud y relación fundamental energía-momento E² = (pc)² + (m0 c²)².
    - Transformaciones de Lorentz, intervalo espaciotemporal invariante Δs² y cuadrivector momento P^μ = (E/c, p).
    - Ecuaciones de campo de Einstein de la Relatividad General, geodésicas y radio de Schwarzschild rs = 2GM/c².
    - Fenomenología cuántica temprana con dualidad de De Broglie, dispersión Compton, incertidumbre de Heisenberg y niveles atómicos de Bohr.
    - Ecuación de Schrödinger, pozo de potencial infinito 1D, oscilador armónico cuántico y efecto túnel.
    - Momento angular cuántico orbital con conmutadores y funciones de onda completas del átomo de hidrógeno.
    - Formalismo de Dirac con conmutación canónica [x̂, p̂] = iℏ, matrices de Pauli, teoría de perturbaciones y regla de oro de Fermi.
    - Mecánica cuántica relativista con ecuaciones de Klein-Gordon (espín 0) y Dirac (espín 1/2) con álgebra de matrices gamma.
    - Estructura nuclear, defecto de masa B = Δm c², ley de desintegración radiactiva y periodo de semidesintegración t_1/2.
    - Fórmula semiempírica de masa de Bethe-Weizsäcker (modelo de gota líquida), balance de reacción nuclear Q y dosimetría de radiación.
    - Potencial nuclear fuerte de Yukawa, fórmula de Gell-Mann-Nishijima, matriz CKM y resonancia de Breit-Wigner.
    - Cristalografía con ley de Bragg, condición de Laue, gas de electrones de Fermi y relación de Wiedemann-Franz.
    - Teoría de bandas en sólidos, teorema de Bloch, tensor de masa efectiva y concentración intrínseca de semiconductores.
    - Modelo de Debye de capacidad calorífica de la red, ecuaciones de London del efecto Meissner y brecha superconductora BCS.
  - El catálogo global de la aplicación ahora cuenta con **372 fórmulas preestablecidas** (266 matemáticas y 106 de física) organizadas en 22 categorías temáticas completas.
- **[2026-08-19 00:40] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.
  - `pydoclint`: 0 violaciones en todos los archivos de `src/` y `main.py`.
  - `mypy`: 0 errores en 27 archivos fuente.
  - `ruff`: 0 infracciones de estilo y formato.

## Sesión: Conversión de Fórmulas a Formato LaTeX en formulario.md (2026-08-19 18:29)

- **[2026-08-19 18:29] Conversión de Fórmulas a LaTeX ([formulario.md](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/formulario.md)):**
  - Se convirtieron todas las fórmulas de texto plano/pseudocódigo de [formulario.md](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/formulario.md) a sintaxis formal estándar en LaTeX utilizando bloques de visualización `$$ ... $$` e inline `$ ... $`.
  - Estructurado en las secciones de Aritmética, Álgebra, Trigonometría, Geometría (Plana y del Espacio), Geometría Analítica (2D y 3D), Álgebra Lineal, Cálculo Diferencial, Cálculo Integral, Cálculo Vectorial / Multivariable, Ecuaciones Diferenciales y Métodos Numéricos respetando los niveles pedagógicos (`NIVEL BÁSICO`, `NIVEL INTERMEDIO`, `NIVEL UNIVERSITARIO / AVANZADO`) y subsecciones temáticas, en plena concordancia con el formato de [a.md](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/a.md) y [src/data/symbols.py](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/src/data/symbols.py).
- **[2026-08-19 18:42] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.

## Sesión: Encabezados Jerárquicos de Markdown en Formularios (2026-08-19 18:52)

- **[2026-08-19 18:52] Estructuración Jerárquica en Formularios ([formulario_mates.md](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/formulario_mates.md) y [formulario_fisica.md](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/formulario_fisica.md)):**
  - Se eliminaron todas las líneas de separación ASCII `======================================================================` en ambos documentos.
  - Se incorporaron encabezados jerárquicos estándar de Markdown (`#` para Compendios con numeración romana, `##` para Temas secuenciales, `###` para Niveles pedagógicos y `####` para Subtemas indexados `N.M`).
  - **Matemáticas ([formulario_mates.md](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/formulario_mates.md)):** Numeración secuencial de los 11 temas (1. Aritmética a 11. Métodos Numéricos), 33 niveles y 101 subtemas, preservando intactas las 425 fórmulas display y 122 fórmulas inline en LaTeX.
  - **Física ([formulario_fisica.md](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/formulario_fisica.md)):** Numeración secuencial de los 23 temas (1. Cinemática y Dinámica Newtoniana a 23. Física del Estado Sólido), 63 niveles y 173 subtemas, preservando intactas las 661 fórmulas display y 297 fórmulas inline en LaTeX.
  - Se añadieron bloques frontmatter YAML estandarizados y se reajustó la indentación de los ítems a nivel de raíz con fórmulas hijas vinculadas.
- **[2026-08-19 18:52] Certificación y QA:**
  - `pytest`: 42/42 pruebas unitarias superadas al 100%.

## Sesión: Corrección de Fórmulas y Rigor Internacional según Auditoría (2026-08-19 19:25)

- **[2026-08-19 19:25] Corrección Rigurosa de Matemáticas ([formulario_mates.md](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/formulario_mates.md)):**
  - **Teorema de Menelao:** Corregida la razón de segmentos dirigidos a $-1$ y explicitada la relación en longitudes no dirigidas con 1 o 3 puntos en las prolongaciones exteriores.
  - **Pseudoinversa de Moore-Penrose:** Corregida la definición general vía SVD ($A^+ = V\Sigma^+ U^H$) y acotada la forma $(A^H A)^{-1}A^H$ a matrices de rango columna completo.
  - **Métodos de Jacobi y Gauss-Seidel:** Corregidos los signos matriciales bajo la descomposición estándar $A = D + L + U$ ($\mathbf{x}^{(k+1)} = -D^{-1}(L+U)\mathbf{x}^{(k)} + D^{-1}\mathbf{b}$ y $\mathbf{x}^{(k+1)} = -(D+L)^{-1}U\mathbf{x}^{(k)} + (D+L)^{-1}\mathbf{b}$).
  - **Cuadratura Gaussiana:** Añadido el factor de escala de intervalo general $\frac{b-a}{2}\sum w_i f(x_i)$.
  - **Aritmética y Álgebra:** Añadidos cuantificadores universales $\forall a,b\in\mathbb{R}$ en clausura, restricciones de no nulidad en denominadores e inversión, solución constructiva en el Teorema Chino del Resto, $\operatorname{atan2}$ en números complejos y polares, y definición precisa de matriz inversa con adjunta clásica y cofactores.
  - **Geometría y Cálculo:** Explicitadas transversales en Tales, exceso esférico en radianes para triángulo esférico, hipótesis de regularidad en L'Hôpital/Rolle/Lagrange/Cauchy, cota teórica en bisección con techo de iteraciones y contracción de Banach en punto fijo.

- **[2026-08-19 19:25] Corrección Rigurosa de Física ([formulario_fisica.md](file:///G:/REPOSITORIOS%20GITHUB/TRADUCTOR%20MATES/formulario_fisica.md)):**
  - **Cónicas Orbitales:** Unificada la notación de masa reducida $\mu$, interacción $G m_1 m_2$, semilatus rectum $p$ y excentricidad $e = \sqrt{1 + \frac{2EL^2}{\mu(Gm_1m_2)^2}}$.
  - **Termodinámica:** Separada la 1ra Ley general $dU = \delta Q - \delta W$ del trabajo cuasiestático $\delta W = P dV$, temperatura absoluta Rankine $T_{\text{R}}$ y renombrado a Potencial Gran Canónico $\Omega = \Phi_G$.
  - **Electromagnetismo:** Separadas formas de vacío y medios materiales en corriente de desplazamiento $\vec{J}_d$ y vector/densidad de Poynting, explicitada la firma métrica $(+ - - -)$ en la formulación covariante de Maxwell, y notación vectorial rigurosa en distribuciones continuas de carga.
  - **Óptica y Cuántica:** Delimitada la fórmula de Goos-Hänchen a polarización $s$ cerca del ángulo crítico con su relación derivada de fase, corregido el signo d'Alembertiano en Klein-Gordon, corregida la palabra corrupta en la fórmula semiempírica de Bethe-Weizsäcker, estandarizado el sabor $B'$ (bottomness) en Gell-Mann-Nishijima y corregido el signo elástico en la condición de difracción de Laue ($2\vec{k}\cdot\vec{G} + |\vec{G}|^2 = 0$).

- **[2026-08-19 19:25] Certificación y QA:**
  - Suite de pruebas unitarias pytest pasando al 100% (42/42 pruebas superadas).


- **[2026-08-19 19:48] Reestructuracion de Formularios:**
  - Segmentacion de `formulario_mates.md` por nivel (basico, intermedio, avanzado) en la carpeta `docs/mates/`, con renumeracion de la jerarquia markdown.
- **[2026-08-19 19:52] Reestructuracion de Formularios (Fisica):**
  - Segmentacion de `formulario_fisica.md` por nivel (basico, intermedio, avanzado) en la carpeta `docs/fisica/`, con renumeracion de la jerarquia markdown al igual que se hizo con el archivo de matematicas.
- **[2026-08-19 20:25] Mayor Segmentacion de Viñetas (Matematicas):**
  - Segmentacion exhaustiva de todas las viñetas agrupadas en los archivos de `docs/mates/` para aislar cada formula en su propia viñeta independiente (ej. funciones trigonometricas, derivadas, integrales). Esto asegura una renderizacion individual en la app.
- **[2026-08-19 20:39] Mayor Segmentacion de Viñetas (Fisica):**
  - Segmentacion exhaustiva de todas las viñetas agrupadas en los archivos de `docs/fisica/` para aislar cada formula en su propia viñeta independiente, replicando el proceso aplicado en matematicas para asegurar la correcta renderizacion individual de cada ecuacion fisica en la app.

## Sesión: Integración de Constantes Matemáticas (2026-08-20 21:31)

- **[2026-08-20 21:31:13]** Lectura e integración de constantes matemáticas desde docs/mates/constantes.md a la aplicación.
- **[2026-08-20 21:31:13]** Creación de script extractor y almacenamiento estructurado JSON en src/data/constants.py.
- **[2026-08-20 21:31:13]** Creación de widget UI ConstantCardWidget con menú contextual y QSpinBox de rango 0-32 (defecto 9) para ajuste dinámico de precisión decimal.
- **[2026-08-20 21:31:13]** Integración de pestaña ♾️ Constantes en MathPaletteWidget respetando el orden jerárquico y temático establecido en la documentación.

## Tareas Pendientes / Próximos Pasos

- **Buscador de Plantillas y Fórmulas:** Implementar un motor de búsqueda interactivo en la paleta para poder encontrar rápidamente plantillas, símbolos y fórmulas del catálogo.
- **Anidación de Fórmulas:** Revisar y refactorizar la lógica de inserción en el AST (ditor_widget.py, st.py y el panel de traducción) para permitir la anidación de fórmulas. Actualmente, al insertar una fórmula teniendo una casilla seleccionada, la aplicación sobrescribe y reemplaza el contenido por completo en lugar de anidarlo como un sub-nodo, limitando la composición de expresiones matemáticas complejas.

