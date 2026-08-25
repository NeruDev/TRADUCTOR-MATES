---
file: AGENTS.md
description: Reglas fundamentales de agente, desarrollo, metadatos, estándares de código y gestión de variables
author: Equipo Traductor Mates
version: 1.0.0
type: configuration/guidelines
relations:
  - README.md
  - MEMORY.md
  - PROGRESS.md
  - docs/ARCHITECTURE.md
  - docs/base/frontmatter_yaml.md
  - docs/base/tipado_estricto_inline.md
  - docs/base/clase_configuracion.md
  - docs/base/entradas_script.md
  - main.py
---

# Reglas de Agente y Estándares de Código (AGENTS.md)

Este documento contiene las reglas fundamentales de desarrollo, convenciones de nombres, codificación de archivos, metadatos estructurados y gestión de variables para todos los agentes y desarrolladores que trabajen en este repositorio.

---

## 1. Codificación, Metadatos y Formato de Archivos

- **Codificación Estándar:** Todos los archivos del proyecto (código fuente Python, JavaScript, documentación Markdown, scripts y archivos de configuración) DEBEN guardarse en formato **UTF-8** sin BOM.
- **Nomenclatura de Archivos:** Todos los nombres de archivos y directorios deben seguir estrictamente la convención **`snake_case`** en minúsculas (por ejemplo, `main_window.py`, `editor_widget.py`, `test_syntax.py`, `package_config.js`).

### 1.1 Estándar de Frontmatter y Metadatos YAML Obligatorios
Todos los archivos del repositorio que no estén excluidos en `.gitignore` (documentación Markdown, archivos de configuración, código fuente Python con cabeceras YAML en docstrings y módulos JavaScript con comentarios YAML) DEBEN incluir un bloque estructurado de metadatos YAML. El estándar oficial, reglas de campos extendidos y catálogo descriptivo se definen en [`docs/base/frontmatter_yaml.md`](docs/base/frontmatter_yaml.md) (consultar la referencia en caso de dudas).

*Plantilla reducida para Documentación (`.md`):*
```yaml
---
file: String (Ruta relativa desde la raíz)
description: String (1 sola línea con propósito funcional)
type: Enum/String (doc/guide, doc/architecture, doc/api, doc/manual)
version: SemVer (X.Y.Z)
date: ISO 8601 (YYYY-MM-DD)
covers: List[String] (Rutas de código fuente que este documento explica)
relations: List[String] (Documentos relacionados o de lectura previa)
keywords: List[String] (Conceptos en minúsculas/kebab-case para RAG)
---
```

*Plantilla reducida para Ejecutables (`.py`, `.ts`, `.js`, etc.):*
```yaml
---
file: String (Ruta relativa física del código)
module: String (Ruta canónica de importación)
description: String (1 sola línea con responsabilidad única)
type: Enum/String (core/engine, auth/service, ui/component, db/repo)
version: SemVer (X.Y.Z)
date: ISO 8601 (YYYY-MM-DD)
dependencies: List[String] (Módulos internos importados directamente)
relations: List[String] (Archivos acoplados lógicamente o contratos)
exports: List[Mapping] (Entidades públicas y rol funcional)
test: String (Comando CLI para verificar el módulo)
constraints: List[String] (Invariantes y reglas negativas críticas)
keywords: List[String] (Términos técnicos en minúsculas/kebab-case)
---
```

### 1.2 Estándar de Tipado Estricto Inline (*Type Hints*)
Es MANDATORIO el uso de **Type Hints nativos inline** (Python 3.10+ PEP 585 y PEP 604) en todas las firmas de funciones, métodos (`-> None` explícito en `__init__`) y atributos de clase, validado automáticamente con `mypy --strict`. El estándar detallado se define en [`docs/base/tipado_estricto_inline.md`](docs/base/tipado_estricto_inline.md) (consultar la referencia en caso de dudas).

*Ejemplo de uso:*
```python
def parse_slot_content(
    raw_input: str,
    max_depth: int = 5,
    fallback_node: MathNode | None = None,
) -> list[MathNode]:
    """Parsea el contenido textual de una casilla interactiva a nodos del AST."""
    ...
```

### 1.3 Estándar de Clases de Configuración Centralizada
Para definir y modificar los parámetros que gobiernan el comportamiento de un módulo (límites, timeouts, formatos, constantes), se DEBE emplear una clase decorada con `@dataclass(frozen=True)` al inicio del archivo (Sección 3), proporcionando un punto único de control inmutable. El estándar detallado se define en [`docs/base/clase_configuracion.md`](docs/base/clase_configuracion.md) (consultar la referencia en caso de dudas).

*Ejemplo de uso:*
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ASTParserConfig:
    max_recursion_depth: int = 50
    default_placeholder: str = "□"
    auto_balance_delimiters: bool = True

CONFIG = ASTParserConfig()
```

### 1.4 Estándar de Entradas del Script y Variables de Entorno
Para scripts ejecutables, utilidades CLI y herramientas de compilación, se DEBE estructurar el procesamiento de variables de entorno (`os.environ`) con tipado seguro, argumentos CLI con `argparse` auto-documentados y una función `main(argv: Sequence[str] | None = None) -> int` testeable. El estándar detallado se define en [`docs/base/entradas_script.md`](docs/base/entradas_script.md) (consultar la referencia en caso de dudas).

*Ejemplo de uso:*
```python
import argparse
import sys
from collections.abc import Sequence

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CLI de utilidades")
    parser.add_argument("-i", "--input", type=str, required=True, help="Ruta de entrada")
    args = parser.parse_args(argv)
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### 1.5 Docstrings y Estilo Google
Es MANDATORIO el uso de **Google Style Docstrings** para toda la documentación interna de código ejecutable (módulos, clases, métodos y funciones), detallando explícitamente secciones `Args:`, `Returns:`, `Raises:`, `Yields:` y `Attributes:`, validado automáticamente a través de herramientas de *linting* (`pydoclint`).

---

## 2. Gestión de Memoria y Contexto (Ahorro de Tokens)

- **Inspección Previa:** Consultar e inspeccionar siempre en primer lugar `MEMORY.md` y `PROGRESS.md` para verificar el estado y avance del proyecto.
- **Registro en `MEMORY.md`:** Registrar fecha y hora (`YYYY-MM-DD HH:MM`) por cada lección o acción relevante.
- **Registro en `PROGRESS.md`:** Registrar fecha, hora y segundos (`YYYY-MM-DD HH:MM:SS`) para cada actualización del diario de trabajo.
- **Lectura Eficiente de Contexto:** Al reanudar una tarea o cuando los archivos sean extensos, consultar únicamente la última fecha/marca de tiempo para continuar la ejecución de forma eficiente y ahorrar tokens.
- **Actualización Previa a Despliegue Remoto (`git push`):** Si el repositorio local va a subirse o enviarse al repositorio remoto, los archivos `MEMORY.md` y `PROGRESS.md` en la raíz DEBEN actualizarse e incluirse en el commit correspondiente ANTES de realizar el envío (`git push`), asegurando que el commit de despliegue sea atómico, completo y coherente sin generar commits residuales posteriores.

---

## 3. Mantenimiento de Documentación, Metadatos e Interdependencias

- **Sincronización de Documentación y Metadatos:** Si un script cuenta con documentación, metadatos (como cabeceras YAML en docstrings o frontmatter YAML) o ambos, estos DEBEN modificarse obligatoriamente si se modifica su lógica interna.
- **Navegación e Inspección por Metadatos:** Al buscar archivos, funciones o relaciones e interdependencias entre componentes del sistema, se DEBE realizar la inspección a través de sus metadatos básicos en formato YAML (frontmatter en Markdown y cabeceras YAML en docstrings) conforme al estándar oficial de [`docs/base/frontmatter_yaml.md`](docs/base/frontmatter_yaml.md), los cuales detallan la función, módulo y dependencias del archivo.
- **Verificación de Interdependencias:** Al realizar modificaciones en cualquier script, se DEBE revisar explícitamente que su interdependencia con otros componentes y módulos no sea afectada.

---

## 4. Estándares de Representación Visual en Documentación

- **Árbol de Directorios en Formato YAML:** Para la representación del árbol de directorios de cualquier archivo o paquete en la documentación, SIEMPRE se debe generar en formato **YAML** (` ```yaml ... ``` `), reemplazando esquemas e hilos ASCII.
- **Gráficos y Diagramas en Formato Mermaid:** Para representar gráficos de flujo de trabajo, esquemas de interfaz, diagramas de arquitectura o modelos de datos, se recurre obligatoriamente al formato **Mermaid** (` ```mermaid ... ``` `), con el objetivo de reducir y eliminar el uso de sintaxis ASCII para representaciones visuales.

---

## 5. Entorno de Pruebas (Sandbox) y Scripts Temporales

- **Uso Obligatorio de \sandbox/\:** Todos los scripts temporales, utilidades *throwaway* de un solo uso, pruebas destructivas y borradores de documentación que no cuenten con metadatos estructurados DEBEN ser creados y almacenados únicamente dentro del directorio \sandbox/\.
- **Mantenimiento del Repositorio:** Está estrictamente prohibido crear scripts de prueba o archivos temporales en la raíz del proyecto o en la carpeta \src/\, a fin de evitar la acumulación de archivos residuales y mantener limpio el árbol de despliegue principal.
