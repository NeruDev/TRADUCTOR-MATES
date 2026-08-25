---
file: docs/base/frontmatter_yaml.md
description: Estándar y plantillas universales para metadatos frontmatter YAML en documentación y archivos ejecutables
author: Equipo Traductor Mates
version: 1.0.0
date: 2026-08-24
type: doc/guide
relations:
  - AGENTS.md
  - README.md
  - docs/ARCHITECTURE.md
  - docs/base/tipado_estricto_inline.md
  - docs/base/clase_configuracion.md
  - docs/base/entradas_script.md
keywords:
  - frontmatter
  - yaml
  - metadatos
  - plantillas
  - estandar
---

# Guía y Plantillas de Metadatos YAML Frontmatter

Este documento define el estándar oficial de metadatos estructurados en formato YAML para todos los archivos del repositorio, distinguiendo entre archivos de **documentación** (`.md`) y archivos **ejecutables** (`.py`, `.js`, etc.).

---

## 1. Plantilla Universal Comentada: Documentación (`.md`)

```markdown
---
# [String: Ruta relativa] Ubicación exacta del archivo desde la raíz
file: docs/ARCHITECTURE.md

# [String: 1 línea] Propósito funcional del documento
description: Especificación técnica completa de arquitectura, patrones MVC/MVVM, modelo de datos AST y estructura de directorios.

# [Enum: categoria/subtipo] Rol documental (doc/guide, doc/architecture, doc/api, doc/manual)
type: doc/architecture

# [SemVer: X.Y.Z] Versión del documento (debe alinearse con la versión de la API que describe)
version: 1.0.0

# [ISO 8601: YYYY-MM-DD] Fecha de última revisión técnica del documento
date: 2026-08-22

# [List[String]: Archivos de código] Archivos fuente que implementan lo descrito aquí
covers:
  - main.py
  - src/core/ast.py
  - src/core/parser.py
  - src/core/translator.py
  - src/ui/main_window.py
  - src/ui/components/preview_panel.py

# [List[String]: Rutas] Documentos relacionados de lectura previa o complementaria
relations:
  - README.md
  - main.py
  - src/README.md
  - docs/directorios.json
  - docs/directorios_comentados.jsonc

# [List[String]: Minúsculas] Palabras clave conceptuales para búsqueda RAG
keywords:
  - arquitectura
  - ast
  - mvc
  - mvvm
  - miniracer
  - mathjax
  - pyside6
---

# Arquitectura del Sistema - Traductor Mates & Editor de Ecuaciones
...
```

---

## 2. Plantilla Universal Comentada: Archivo Ejecutable (`.py`, `.ts`, etc.)

```python
"""
---
# [String: Ruta relativa] Ubicación física del código fuente
file: src/ui/main_window.py

# [String: Import Path] Ruta canónica de importación en el lenguaje
module: src.ui.main_window

# [String: 1 línea] Qué hace el módulo (responsabilidad única)
description: Ventana principal de la aplicación con layout equilibrado en 4 cuadrantes (25% cada uno), splitters interactivos y gestión de temas.

# [Enum: categoria/rol] Rol en el sistema (core/engine, auth/service, ui/component, db/repo)
type: ui/component

# [SemVer: X.Y.Z] Versión actual del módulo
version: 1.0.0

# [ISO 8601: YYYY-MM-DD] Fecha del último cambio funcional relevante
date: 2026-08-24

# [List[String]: Rutas internas] Módulos locales que este archivo consume
dependencies:
  - src.core.ast
  - src.core.logger
  - src.core.parser
  - src.core.translator
  - src.data.symbols
  - src.ui.theme
  - src.ui.components.action_bar
  - src.ui.components.code_panel
  - src.ui.components.editor_widget
  - src.ui.components.palette_widget
  - src.ui.components.preview_panel
  - src.ui.components.save_formula_dialog
  - src.utils.recovery_manager
  - src.utils.user_formulas_manager

# [List[String]: Rutas] Archivos no importados directamente pero con fuerte acoplamiento lógico
relations:
  - main.py
  - docs/ARCHITECTURE.md

# [List[Mapping]: Entidad -> Rol] Catálogo rápido de la API pública expuesta
exports:
  - MainWindow: "Ventana principal integradora de los 4 paneles de la aplicación en cuadrantes 2x2"

# [String: Comando CLI] Comando canónico para verificar este módulo
test: pytest tests/test_editor_widget.py

# [List[String]: Reglas negativas] Invariantes críticas que el agente no debe violar
constraints:
  - "Mantener la proporción 25% equitativa entre los 4 paneles principales en showEvent"
  - "Garantizar la persistencia y limpieza segura de recuperación de sesión en closeEvent"

# [List[String]: Minúsculas/kebab-case] Términos técnicos para recuperación semántica
keywords:
  - main-window
  - quadrant-layout
  - qsplitter
  - theme-toggle
  - ast-sync
  - pyside6
---
"""

from __future__ import annotations
# Código fuente del módulo...
```

---

## 3. Reglas para los Campos Extendidos

### 1. `keywords` (Indexación y Recuperación)

* **Para Documentación:** Usar conceptos de dominio, flujos de usuario, casos de uso y terminología funcional (ej. `[inicio-sesion, recuperacion-cuenta, flujo-oauth]`).
* **Para Ejecutables:** Usar nombres de patrones de diseño, protocolos técnicos, algoritmos o dependencias centrales (ej. `[jwt, rsa-signature, middleware, token-rotation]`).

### 2. `relations` (Grafo de Acoplamiento)

* **Para Documentación:** Enlazar documentos padre, tutoriales complementarios o diagramas de arquitectura (ej. `[README.md, docs/SECURITY.md]`).
* **Para Ejecutables:** Enlazar archivos que comparten contratos de datos, esquemas de base de datos o configuraciones compartidas, excluyendo dependencias directas de importación que ya van en `dependencies`.

### 3. `date` (Marca de Tiempo y Sincronización)

* **Para Documentación:** Representa la última fecha en que el texto fue revisado para coincidir con la implementación real del código.
* **Para Ejecutables:** Representa la fecha del último cambio estructural, refactorización o actualización de versión del módulo.

---

## 4. Tabla Descriptiva de Campos de Metadatos

| Campo | Ámbito de Uso | Tipo de Dato | Estándar y Regla de Formato | Ejemplo de Uso General |
| --- | --- | --- | --- | --- |
| **`file`** | Ambos | `String` (Ruta) | Ruta relativa estricta desde la raíz del repositorio con separadores `/`. | `src/auth/jwt_service.py` |
| **`description`** | Ambos | `String` | Texto plano de 1 sola línea con alta densidad semántica. Evitar introducciones vacías. | `Servicio de generación, validación y rotación de tokens JWT.` |
| **`type`** | Ambos | `Enum` / `String` | Taxonomía jerárquica corta (`categoria/rol`). | `auth/service` *(script)* o `doc/guide` *(doc)* |
| **`version`** | Ambos | `SemVer` | Formato `X.Y.Z` (Major.Minor.Patch) entrecomillado si contiene guiones. | `1.4.0` |
| **`date`** | Ambos | `ISO 8601` | Fecha en formato estricto `YYYY-MM-DD`. | `2026-08-24` |
| **`keywords`** | Ambos | `List[String]` | Array en línea `[...]` o lista con `-`, términos en minúsculas y kebab-case. | `[jwt, oauth2, auth-token, rsa256]` |
| **`relations`** | Ambos | `List[String]` | Lista de rutas de archivos con acoplamiento lógico, arquitectónico o de lectura. | `[config/auth.yaml, docs/AUTH_SPEC.md]` |
| **`covers`** | Documentación | `List[String]` | Lista de rutas de código fuente exactas que este documento explica. | `[src/auth/jwt_service.py, src/auth/models.py]` |
| **`module`** | Ejecutable | `String` | Notación por puntos estándar del lenguaje para importaciones. | `src.auth.jwt_service` |
| **`exports`** | Ejecutable | `List[Mapping]` | Lista de entidades públicas clave con su rol funcional condensado en 1 línea. | `- TokenManager: "Gestor de ciclo de vida de tokens"` |
| **`dependencies`** | Ejecutable | `List[String]` | Módulos internos del repositorio que este archivo importa directamente. | `[src.utils.crypto, src.config.settings]` |
| **`test`** | Ejecutable | `String` (Comando) | Comando de terminal listo para copiar y ejecutar en el entorno local. | `pytest tests/auth/test_jwt_service.py` |
| **`constraints`** | Ejecutable | `List[String]` | Reglas negativas e invariantes funcionales que el agente jamás debe romper. | `["No almacenar claves privadas en texto plano", "Tokens deben expirar en máx 15 min"]` |
