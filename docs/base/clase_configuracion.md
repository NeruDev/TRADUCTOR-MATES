---
file: docs/base/clase_configuracion.md
description: Estándar y arquitectura para clases de configuración centralizada con dataclasses inmutables y parámetros operativos
author: Equipo Traductor Mates
version: 1.0.0
date: 2026-08-24
type: doc/guide
relations:
  - AGENTS.md
  - docs/base/frontmatter_yaml.md
  - docs/base/tipado_estricto_inline.md
  - docs/base/entradas_script.md
keywords:
  - configuracion
  - dataclass
  - inmutabilidad
  - parametros
  - settings
  - modularidad
---

# Guía y Estándar de Clases de Configuración Centralizada

Este documento establece el estándar arquitectónico para la definición y gestión de **parámetros de configuración operativa** en módulos y paquetes del sistema. Sustituye la práctica de listas comentadas al final del archivo por estructuras de datos tipadas, inmutables y auto-documentadas ubicadas en la cabecera operativa del módulo.

---

## 1. Justificación y Beneficios para la IA Agéntica

Cuando un agente de IA o desarrollador necesita ajustar o calibrar el comportamiento de un componente (por ejemplo, límites de recursión, tiempos de timeout, constantes visuales o umbrales de caché), contar con una clase de configuración explícita proporciona:

1. **Punto Único de Control (Single Source of Truth):** El agente sabe exactamente qué variables gobiernan el módulo sin necesidad de explorar o alterar la lógica interna de las funciones.
2. **Inmutabilidad Garantizada (`frozen=True`):** Evita que durante la ejecución se muten accidentalmente valores de configuración global, previniendo condiciones de carrera y efectos secundarios indeseados.
3. **Validación Estática de Tipos:** Los campos cuentan con tipos de datos estrictos comprobados por `mypy` y sugeridos por sistemas de autocompletado (LSP).
4. **Semántica Auto-explicativa:** Cada parámetro se acompaña de un comentario o docstring que define su rango de valores válidos y su impacto operativo.

---

## 2. Patrón Estándar: `@dataclass(frozen=True)`

El mecanismo estándar en Python 3.10+ para configuración a nivel de módulo es una clase decorada con `@dataclass(frozen=True)` situada inmediatamente después de las importaciones y tipos auxiliares.

### 2.1 Estructura Canónica

```python
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class ASTParserConfig:
    """Parámetros de configuración operativa para el analizador sintáctico del AST.

    Attributes:
        max_recursion_depth: Límite de anidamiento de casillas para evitar stack overflow.
        default_placeholder: Símbolo visual predeterminado para casillas vacías.
        auto_balance_delimiters: Indica si se deben cerrar paréntesis automáticamente.
        timeout_ms: Tiempo máximo de parseo antes de abortar la operación.
    """
    max_recursion_depth: int = 50
    default_placeholder: str = "□"
    auto_balance_delimiters: bool = True
    timeout_ms: int = 250

# Instancia singleton inmutable para uso predeterminado en el módulo
DEFAULT_CONFIG = ASTParserConfig()
```

---

## 3. Patrones de Uso e Inyección de Dependencias

### 3.1 Uso por Defecto con Soporte de Sobreescritura

Las clases y funciones consumidoras deben aceptar una instancia opcional de la configuración en su constructor, tomando por defecto la instancia global:

```python
class LaTeXStreamParser:
    """Tokenizador y analizador sintáctico descendente para expresiones LaTeX."""

    def __init__(self, config: ASTParserConfig | None = None) -> None:
        """Inicializa el parser con la configuración especificada.

        Args:
            config: Objeto de configuración operativa. Si es None, utiliza DEFAULT_CONFIG.
        """
        self.config: ASTParserConfig = config or DEFAULT_CONFIG
        self._current_depth: int = 0

    def parse(self, latex_string: str) -> MathTree:
        if self._current_depth >= self.config.max_recursion_depth:
            raise RecursionError(
                f"[ERR_AST_004] Superada la profundidad máxima de {self.config.max_recursion_depth}"
            )
        # Lógica de parseo...
        ...
```

### 3.2 Modificación Segura mediante `dataclasses.replace`

Dado que la configuración es inmutable (`frozen=True`), para crear variantes en pruebas unitarias o flujos específicos se debe utilizar `replace()`:

```python
from dataclasses import replace

# Crear una configuración aislada para pruebas de estrés
stress_test_config = replace(DEFAULT_CONFIG, max_recursion_depth=500, timeout_ms=5000)
custom_parser = LaTeXStreamParser(config=stress_test_config)
```

---

## 4. Ejemplos de Configuración en el Proyecto

### 4.1 Configuración de Motor de Renderizado (`RendererConfig`)

```python
@dataclass(frozen=True)
class MathRendererConfig:
    """Configuración del motor de renderizado vectorial MathJax / KaTeX."""
    dpi: int = 300
    base_font_size_px: int = 24
    integral_font_size_px: int = 44
    sum_font_size_px: int = 38
    root_font_size_px: int = 28
    export_background_color: str = "#ffffff"
    miku_accent_color: str = "#39C5BB"

RENDERER_CONFIG = MathRendererConfig()
```

### 4.2 Configuración de Recuperación ante Fallos (`RecoveryConfig`)

```python
@dataclass(frozen=True)
class SessionRecoveryConfig:
    """Configuración de persistencia y salvaguarda de sesión de usuario."""
    auto_save_interval_seconds: int = 30
    recovery_file_path: str = "src/data/session_recovery.json"
    max_history_snapshots: int = 50
    enable_crash_reporting: bool = True

RECOVERY_CONFIG = SessionRecoveryConfig()
```

---

## 5. Reglas e Invariantes para Agentes

1. **Ubicación Obligatoria:** Las clases de configuración deben declararse en la **Sección 3** del archivo (después de los imports y antes de las clases de lógica funcional).
2. **Inmutabilidad Estricta:** Toda clase de configuración DEBE incluir el decorador `@dataclass(frozen=True)`.
3. **No Mutar Estado Dinámico:** Las clases de configuración solo almacenan parámetros estáticos u operativos; jamás deben contener variables de estado mutable (como contadores, referencias a widgets de UI o listas dinámicas en tiempo de ejecución).
4. **Valores por Defecto Sensatos:** Todo campo debe contar con un valor por defecto seguro y funcional para permitir inicializaciones sin argumentos (`ASTConfig()`).
