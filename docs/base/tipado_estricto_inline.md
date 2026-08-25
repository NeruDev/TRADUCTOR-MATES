---
file: docs/base/tipado_estricto_inline.md
description: Guía y estándar de tipado estricto inline mediante Type Hints nativos para firmas de funciones, métodos y atributos
author: Equipo Traductor Mates
version: 1.0.0
date: 2026-08-24
type: doc/guide
relations:
  - AGENTS.md
  - docs/base/frontmatter_yaml.md
  - docs/base/clase_configuracion.md
  - docs/base/entradas_script.md
keywords:
  - tipado-estricto
  - type-hints
  - mypy
  - pep-484
  - typing
  - type-annotations
---

# Guía y Estándar de Tipado Estricto Inline

Este documento establece el estándar obligatorio de **tipado estricto inline** (*Type Hints* nativos) en todo el código fuente del proyecto (Python y JavaScript/TypeScript). Define las directrices técnicas para garantizar la verificabilidad estática de tipos, la asistencia a herramientas de análisis (`mypy`, `pylance`) y la optimización de la atención contextual para agentes de Inteligencia Artificial.

---

## 1. Justificación y Ventajas para la IA Agéntica

El uso de *Type Hints* nativos colocados directamente en las firmas de funciones y atributos de clase resuelve de raíz los problemas asociados a la documentación redundante o separada:

| Dimensión | Tipado Estricto Inline | Lista de Variables al Final (Anti-patrón) |
| --- | --- | --- |
| **Localidad Contextual** | La información de tipo reside en la misma ventana de atención del modelo de lenguaje donde se usa la función o variable. | Obliga a la IA a fragmentar su ventana atencional entre el código y el pie del archivo. |
| **Sincronización (Doc Drift)** | La firma y el tipo se actualizan conjuntamente en cada refactorización. | Se desactualiza rápidamente al modificarse la lógica interna. |
| **Verificación Automatizada** | Validado formalmente en CI/CD por analizadores estáticos (`mypy --strict`). | Texto plano no ejecutable ni validable por compiladores o linters. |
| **Consumo de Tokens** | Compacto, nativo y semánticamente denso. | Redundante, duplica información ya presente en el AST. |

---

## 2. Estándar de Tipado en Python (3.10+)

### 2.1 Uso de Tipos Nativos y Operador de Unión (`|`)

Conforme a `PEP 585` y `PEP 604`, se deben utilizar las colecciones genéricas nativas y el operador `|` para uniones y tipos opcionales, evitando la importación de `typing.List`, `typing.Dict`, `typing.Union` o `typing.Optional`.

```python
# CORRECTO: Tipos nativos de Python 3.10+
def parse_slot_content(
    raw_input: str,
    max_depth: int = 5,
    fallback_node: MathNode | None = None,
) -> list[MathNode]:
    """Parsea el contenido textual de una casilla interactiva a nodos del AST.

    Args:
        raw_input: Cadena cruda ingresada por el usuario.
        max_depth: Profundidad máxima de recursión permitida.
        fallback_node: Nodo alternativo en caso de error o None.

    Returns:
        Lista de nodos matemáticos generados.
    """
    ...
```

```python
# INCORRECTO: Sintaxis obsoleta o sin tipar
from typing import List, Optional, Union

def parse_slot_content(raw_input, max_depth=5, fallback_node=None): # Sin tipos
    ...

def parse_legacy(items: List[str], opt: Optional[Union[int, str]]) -> None: # Obsoleto
    ...
```

---

### 2.2 Tipado Explícito en Inicializadores y Métodos Especiales

Todos los constructores `__init__` deben incluir explícitamente la anotación de retorno `-> None:`. Esto previene advertencias de `mypy` y aclara el ciclo de vida del objeto:

```python
class SlotBoxWidget(QFrame):
    """Widget gráfico que representa una casilla editable dentro del editor visual."""

    def __init__(
        self,
        parent: QWidget | None = None,
        slot_id: str = "",
        initial_text: str = "",
    ) -> None:
        super().__init__(parent)
        self.slot_id: str = slot_id
        self.current_text: str = initial_text
        self.is_active: bool = False
```

---

### 2.3 Atributos de Clase y Variables de Instancia Complejas

Cuando una variable de instancia no se inicializa con un valor del que `mypy` pueda inferir el tipo unívocamente (por ejemplo, colecciones vacías o referencias opcionales), se debe declarar su tipo de forma explícita:

```python
class MathPaletteWidget(QWidget):
    """Paleta interactiva de símbolos, plantillas y fórmulas."""

    # Atributos con anotación explícita
    _flyout_menus: list[QMenu] = []
    _active_theme: str = "dark"

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.cached_pixmaps: dict[str, QPixmap] = {}
        self.current_selected_node: MathNode | None = None
```

---

### 2.4 Tipos Avanzados: `Callable`, `TypeVar`, `Literal` y `Protocol`

Para contratos de orden superior, callbacks y polimorfismo estructural:

```python
from typing import Callable, Literal, TypeVar

T = TypeVar("T", bound="MathNode")
ThemeMode = Literal["light", "dark"]
NodeVisitor = Callable[[MathNode], str]

def traverse_tree(root: MathNode, visitor: NodeVisitor, mode: ThemeMode = "dark") -> str:
    """Recorre un árbol matemático aplicando una función visitante tipada.

    Args:
        root: Nodo raíz del árbol AST.
        visitor: Función callback que transforma un nodo en texto.
        mode: Modo visual del tema actual.

    Returns:
        Representación serializada resultante.
    """
    ...
```

---

## 3. Tipado en JavaScript / TypeScript

Para módulos JavaScript del proyecto (como los del motor de compilación `mathjax_build/` o scripts auxiliares), el tipado estricto se logra mediante **JSDoc exhaustivo** con anotaciones de tipo que analizadores como TypeScript y editores LSP pueden verificar:

```javascript
/**
 * Sanitiza una cadena SVG para compatibilidad con Qt TinySVG.
 *
 * @param {string} svgString - Código XML crudo del SVG generado por MathJax.
 * @param {string} [themeColor='#39C5BB'] - Color hexadecimal del tema actual.
 * @returns {string} Cadena SVG completamente sanitizada.
 * @throws {Error} Si el marcado SVG es sintácticamente inválido.
 */
export function sanitizeSvgOutput(svgString, themeColor = '#39C5BB') {
  if (!svgString || typeof svgString !== 'string') {
    throw new Error('[ERR_SVG_001] La entrada SVG debe ser una cadena no vacía');
  }
  // Lógica de transformación...
  return svgString;
}
```

---

## 4. Matriz de Buenas Prácticas y Reglas Críticas

1. **Evitar `Any` Desmedido:** No usar `Any` para "silenciar" errores del linter. Utilizar tipos específicos, uniones precisas (`int | float`), o `object` con comprobaciones `isinstance()`.
2. **Coherencia con Google Style Docstrings:** Los nombres de parámetros en `Args:` deben coincidir con la firma tipada de la función sin discrepancias (`pydoclint` valida esto automáticamente).
3. **Inclusión de `from __future__ import annotations`:** Permite la evaluación diferida de anotaciones de tipo, mejorando los tiempos de importación y resolviendo referencias circulares de tipo hacia adelante.
4. **Verificación Continua:** Todo código nuevo o modificado debe pasar sin advertencias el linter `mypy` como parte del pipeline de calidad:
   ```bash
   mypy src/ tests/
   ```
