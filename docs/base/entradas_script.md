---
file: docs/base/entradas_script.md
description: Estándar de gestión de entradas, variables de entorno, argumentos CLI y settings externos para scripts y ejecutables
author: Equipo Traductor Mates
version: 1.0.0
date: 2026-08-24
type: doc/guide
relations:
  - AGENTS.md
  - docs/base/frontmatter_yaml.md
  - docs/base/tipado_estricto_inline.md
  - docs/base/clase_configuracion.md
keywords:
  - entradas-script
  - variables-entorno
  - cli
  - argparse
  - settings
  - entrypoint
---

# Guía y Estándar de Entradas del Script y Variables de Entorno

Este documento establece el estándar técnico para la gestión de **parámetros de entrada externos**, **variables de entorno** (`os.environ`), argumentos de línea de comandos (**CLI**) y esquemas de configuración externa para scripts ejecutables y utilidades del proyecto.

---

## 1. Justificación y Beneficios para la IA Agéntica

Cuando un agente de IA interactúa con herramientas de terminal, scripts de construcción, utilidades de prueba o puntos de entrada ejecutables, necesita comprender inmediatamente:

1. **Cuáles son los argumentos aceptados y sus valores por defecto.**
2. **Qué variables del sistema o del entorno alteran el comportamiento del script.**
3. **Cómo validar las entradas antes de ejecutar operaciones destructivas.**
4. **Cómo capturar códigos de salida de forma determinista (`0` para éxito, `!= 0` para error).**

---

## 2. Gestión de Variables de Entorno (`os.environ`)

Las variables de entorno deben procesarse mediante funciones de lectura con tipado estricto y valores predeterminados seguros (*fallbacks*).

### 2.1 Patrón de Lectura y Parseo Tipado

```python
import os
from pathlib import Path

def get_env_bool(key: str, default: bool = False) -> bool:
    """Obtiene una variable de entorno parseada como booleano seguro."""
    val = os.environ.get(key)
    if val is None:
        return default
    return val.strip().lower() in {"1", "true", "yes", "on"}

def get_env_int(key: str, default: int) -> int:
    """Obtiene una variable de entorno parseada como entero con fallback."""
    val = os.environ.get(key)
    if val is None:
        return default
    try:
        return int(val.strip())
    except ValueError:
        return default

# Variables de entorno operativas del proyecto
QT_SVG_DEFAULT_OPTIONS: int = get_env_int("QT_SVG_DEFAULT_OPTIONS", default=2)
ENABLE_DEBUG_LOGS: bool = get_env_bool("TRADUCTOR_MATES_DEBUG", default=False)
ASSETS_DIR: Path = Path(os.environ.get("TRADUCTOR_MATES_ASSETS", "src/assets"))
```

---

## 3. Argumentos de Línea de Comandos con `argparse`

Para scripts independientes, herramientas de compilación (`build.js`, procesadores de datos) o comandos de verificación, se debe utilizar `argparse` tipado y completamente auto-documentado.

### 3.1 Esquema Canónico de CLI

```python
import argparse
import sys
from collections.abc import Sequence

def create_cli_parser() -> argparse.ArgumentParser:
    """Construye y configura el parser de argumentos de terminal."""
    parser = argparse.ArgumentParser(
        prog="traductor_mates_cli",
        description="Utilidad CLI para compilación, traducción y verificación de fórmulas matemáticas.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Cadena de fórmula en LaTeX o ruta a archivo de entrada.",
    )
    parser.add_argument(
        "-o", "--output-format",
        choices=["latex", "markdown", "ast-json", "svg"],
        default="latex",
        help="Formato de salida deseado.",
    )
    parser.add_argument(
        "--theme",
        choices=["light", "dark"],
        default="dark",
        help="Tema cromático para la renderización SVG.",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="Densidad de puntos por pulgada para exportaciones rasterizadas.",
    )

    return parser
```

---

## 4. Patrón de Punto de Entrada Seguro y Testeable

Todo script ejecutable debe estructurar su función `main` para que acepte una secuencia opcional de argumentos `argv`, facilitando la ejecución desde consola y las pruebas unitarias automatizadas con `pytest`:

```python
def main(argv: Sequence[str] | None = None) -> int:
    """Punto de entrada principal del script ejecutable.

    Args:
        argv: Lista de argumentos de línea de comandos. Si es None, utiliza sys.argv[1:].

    Returns:
        Código de salida del proceso (0 para éxito, 1 para error).
    """
    parser = create_cli_parser()
    args = parser.parse_args(argv)

    try:
        # Lógica de ejecución usando los argumentos parseados
        print(f"Procesando fórmula con formato de salida: {args.output_format}")
        return 0
    except Exception as err:
        print(f"Error durante la ejecución: {err}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

---

## 5. Resumen de la Estructura Modular Recomendada

A continuación se presenta la plantilla de capas estructurales para todo archivo ejecutable del proyecto, integrando Frontmatter YAML, imports tipados, configuración centralizada y entradas de ejecución:

```text
┌────────────────────────────────────────────────────────┐
│ 1. Frontmatter YAML (Metadatos globales, test, constraints)│
├────────────────────────────────────────────────────────┤
│ 2. Imports y Tipos Auxiliares (typing, typing_extensions) │
├────────────────────────────────────────────────────────┤
│ 3. Configuración / Constantes Modificables (@dataclass)│ <── Reemplaza la lista final
├────────────────────────────────────────────────────────┤
│ 4. Clases y Funciones + Google Docstrings + Type Hints │
├────────────────────────────────────────────────────────┤
│ 5. Gestión de Entradas (CLI / os.environ) + main(argv) │
├────────────────────────────────────────────────────────┤
│ 6. Bloque if __name__ == "__main__": sys.exit(main())  │
└────────────────────────────────────────────────────────┘
```

---

## 6. Reglas e Invariantes para Agentes

1. **Auto-descubrimiento:** Todo script CLI debe ser completamente auto-descriptivo mediante `--help`.
2. **Códigos de Salida Deterministas:** Toda función `main()` DEBE retornar un entero (`int`) y usarse con `sys.exit(main())`.
3. **No Hardcodear Rutas Absolutas:** Las rutas deben obtenerse a través de `Path(__file__).parent`, variables de entorno o argumentos CLI, nunca con rutas rígidas dependientes del sistema operativo.
4. **Validación Temprana:** Validar la existencia de archivos y tipos de entrada en la función de parseo antes de iniciar operaciones intensivas de CPU o disco.
