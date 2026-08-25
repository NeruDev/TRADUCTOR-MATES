"""
---
file: src/core/ast.py
module: src.core.ast
description: Motor del Árbol de Sintaxis Abstracta (AST) y gestión de casillas interactivas (Slots).
type: core/engine
version: 1.0.0
date: 2026-08-24
dependencies: []
relations:
  - docs/ARCHITECTURE.md
  - src/core/parser.py
  - src/core/translator.py
  - src/ui/components/editor_widget.py
exports:
  - Slot: "Contenedor interactivo de nodos matemáticos [ □ ]"
  - MathNode: "Clase base abstracta para todos los nodos del árbol"
  - TextNode: "Nodo hoja para caracteres y variables alfanuméricas"
  - SymbolNode: "Nodo hoja para símbolos matemáticos y caracteres griegos"
  - OperatorNode: "Nodo hoja para funciones y operadores analíticos"
  - TemplateNode: "Clase base para estructuras visuales con casillas anidadas"
  - FractionNode: "Plantilla de fracción interactiva con numerador y denominador"
  - PowerNode: "Plantilla de potencia con base y exponente"
  - SubscriptNode: "Plantilla de subíndice"
  - SubSupNode: "Plantilla combinada con subíndice y superíndice"
  - SquareRootNode: "Plantilla de raíz cuadrada"
  - NthRootNode: "Plantilla de raíz enésima con índice y radicando"
  - DefiniteIntegralNode: "Plantilla de integral definida con límites superior e inferior"
  - IndefiniteIntegralNode: "Plantilla de integral indefinida con integrando"
  - ContourIntegralNode: "Plantilla de integral de contorno cerrado"
  - DoubleIntegralNode: "Plantilla de integral doble de superficie"
  - TripleIntegralNode: "Plantilla de integral triple de volumen"
  - SummationNode: "Plantilla de sumatoria con límites inferior y superior"
  - LimitNode: "Plantilla de límite matemático"
  - BracketNode: "Plantilla de delimitadores adaptativos (paréntesis, corchetes, llaves)"
  - MatrixNode: "Plantilla de matriz bidimensional de casillas"
  - DerivativeNode: "Plantilla para derivadas ordinarias y parciales"
  - BinomialNode: "Plantilla para coeficiente binomial"
  - ModularNode: "Plantilla para congruencia modular"
  - ProductNode: "Plantilla para productoria con límites"
  - StyleDecoratorNode: "Plantilla para decoradores de estilo y fuentes matemáticas"
  - MathTree: "Gestor principal del árbol, navegación entre casillas y pila Undo/Redo"
test: pytest tests/test_ast.py
constraints:
  - "Preservar el desacoplamiento estricto del árbol AST respecto a widgets gráficos de PySide6"
  - "Garantizar la navegabilidad bidireccional entre nodos hijos y casillas padre"
keywords:
  - math-ast
  - slot-management
  - template-node
  - math-tree
  - undo-redo
  - tree-traversal
---

Math Abstract Syntax Tree (AST) & Slot Management Engine
Manages the structured mathematical equation tree, slots, nodes, and navigation.
"""

from __future__ import annotations

import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass


# 3. Configuración Operativa del Motor AST
@dataclass(frozen=True)
class ASTConfig:
    """Parámetros de configuración operativa del motor de Árbol de Sintaxis Abstracta.

    Attributes:
        max_history_depth: Límite de estados almacenados en la pila de deshacer/rehacer.
        default_placeholder: Glifo textual predeterminado para casillas vacías.
    """

    max_history_depth: int = 50
    default_placeholder: str = "□"


AST_CONFIG = ASTConfig()


class Slot:
    """Contenedor editable de nodos matemáticos.

    Representa una casilla interactiva y rellenable `[ □ ]` dentro del
    editor visual de fórmulas. Maneja su propio estado, lista de nodos hijos
    y la posición del cursor de texto/inserción.

    Args:
        name: Etiqueta semántica de la casilla (ej. 'numerador', 'denominador').
        parent: Nodo plantilla que contiene a esta casilla o None.
    """

    def __init__(self, name: str = "slot", parent: TemplateNode | None = None) -> None:
        self.id: str = str(uuid.uuid4())[:8]
        self.name: str = name
        self.parent: TemplateNode | None = parent
        self.nodes: list[MathNode] = []
        self.cursor_position: int = 0

    def is_empty(self) -> bool:
        """Determina si la casilla no contiene ningún nodo hijo.

        Returns:
            True si no contiene nodos hijos; False en caso contrario.
        """
        return len(self.nodes) == 0

    def add_node(self, node: MathNode) -> None:
        """Inserta un nodo matemático en la posición actual del cursor de la casilla.

        Args:
            node: El nodo a insertar y asociar como hijo de esta casilla.
        """
        node.parent_slot = self
        self.nodes.insert(self.cursor_position, node)
        self.cursor_position += 1

    def remove_last_node(self) -> MathNode | None:
        """Elimina y retorna el nodo inmediatamente anterior al cursor.

        Returns:
            El nodo extraído de la casilla, o None si el cursor está al inicio o no hay nodos.
        """
        if self.cursor_position > 0 and self.nodes:
            self.cursor_position -= 1
            return self.nodes.pop(self.cursor_position)
        return None

    def insert_text(self, text: str) -> None:
        """Crea e inserta un nodo de texto en la casilla actual.

        Args:
            text: Cadena de caracteres a incorporar en la ecuación.
        """
        if not text:
            return
        node = TextNode(text)
        self.add_node(node)

    def clear(self) -> None:
        """Vacía todos los nodos contenidos y reinicia la posición del cursor a cero."""
        self.nodes.clear()
        self.cursor_position = 0

    def to_latex(self) -> str:
        """Genera el código LaTeX resultante de la concatenación de sus nodos hijos.

        Returns:
            Código LaTeX generado o cadena vacía si la casilla está desocupada.
        """
        if self.is_empty():
            return ""
        return "".join([n.to_latex() for n in self.nodes])

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de visualización indicando el foco activo.

        Args:
            active_slot_id: Identificador de la casilla con el foco del cursor.

        Returns:
            Representación textual interactiva con casillas `[□]` o `[■]`.
        """
        is_active = self.id == active_slot_id
        if self.is_empty():
            symbol = "■" if is_active else "□"
            return f"[{symbol}]"

        inner = "".join([n.to_display_text(active_slot_id) for n in self.nodes])
        return f"[{inner}]" if is_active else inner

    def get_all_child_slots(self) -> list[Slot]:
        """Obtiene una lista recursiva de esta casilla y todas sus casillas descendientes.

        Returns:
            Lista aplanada de instancias de `Slot`.
        """
        result = [self]
        for node in self.nodes:
            result.extend(node.get_all_slots())
        return result


class MathNode(ABC):
    """Clase base abstracta para todos los nodos del árbol de sintaxis abstracta.

    Todos los elementos de una ecuación (textos, símbolos, fracciones,
    matrices) derivan de esta clase y deben implementar métodos de traducción
    a código y texto de visualización.

    Args:
        node_type: Categoría estructural del nodo ('text', 'symbol', 'operator', etc.).
    """

    def __init__(self, node_type: str = "node") -> None:
        self.id: str = str(uuid.uuid4())[:8]
        self.node_type = node_type
        self.parent_slot: Slot | None = None

    @abstractmethod
    def to_latex(self) -> str:
        """Genera el código LaTeX asociado al nodo.

        Returns:
            Cadena con la representación LaTeX del nodo.
        """

    @abstractmethod
    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera la representación en texto legible interactivo.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto representativo del nodo.
        """

    def get_all_slots(self) -> list[Slot]:
        """Devuelve las casillas contenidas directamente en este nodo.

        Returns:
            Lista de casillas hijas (vacía por defecto en nodos hoja).
        """
        return []


class TextNode(MathNode):
    """Nodo hoja de texto plano para caracteres, números y operadores básicos (+, -, =, etc.).

    Args:
        text: Contenido textual o numérico.
    """

    def __init__(self, text: str) -> None:
        super().__init__("text")
        self.text: str = text

    def to_latex(self) -> str:
        """Convierte el nodo de texto a representación LaTeX compatible.

        Returns:
            Cadena de texto LaTeX formateada.
        """
        # Convert common text operators if needed
        tex = self.text
        tex = tex.replace("*", r" \cdot ")
        tex = tex.replace("/", r" / ")
        tex = tex.replace("|", r"\vert ")
        if tex.startswith("\\") and not tex.endswith(" "):
            tex = tex + " "
        return tex

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Obtiene la representación en texto legible del nodo.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            El texto plano del nodo.
        """
        return self.text


class SymbolNode(MathNode):
    """Nodo hoja que representa un símbolo especial LaTeX o letra griega.

    Args:
        latex_cmd: Comando LaTeX asociado (ej. '\\alpha', '\\pi').
        display: Glifo o texto de visualización interactiva.
    """

    def __init__(self, latex_cmd: str, display: str) -> None:
        super().__init__("symbol")
        self.latex_cmd = latex_cmd
        self.display = display

    def to_latex(self) -> str:
        """Genera el código LaTeX del símbolo con espaciado seguro.

        Returns:
            El comando LaTeX con espacio delimitador.
        """
        return self.latex_cmd + " "

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Obtiene el glifo unicode de visualización.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            El glifo representativo en texto.
        """
        return self.display


class OperatorNode(MathNode):
    """Nodo hoja para operadores matemáticos y funciones analíticas (\\sin, \\det, \\lim, etc.).

    Args:
        latex_cmd: Comando LaTeX del operador (ej. '\\sin', '\\det').
        display: Texto de visualización del operador.
    """

    def __init__(self, latex_cmd: str, display: str) -> None:
        super().__init__("operator")
        self.latex_cmd = latex_cmd
        self.display = display

    def to_latex(self) -> str:
        """Genera el código LaTeX del operador matemático.

        Returns:
            Comando LaTeX con espacio delimitador.
        """
        return self.latex_cmd + " "

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Obtiene el texto de visualización interactiva del operador.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto del operador.
        """
        return self.display


class TemplateNode(MathNode):
    """Clase base para estructuras matemáticas complejas compuestas por casillas (Slots).

    Args:
        template_type: Tipo o categoría de la plantilla (e.g. 'fraction', 'matrix').
        slots_dict: Diccionario mapeando nombres de ranura a instancias de `Slot`.
    """

    def __init__(self, template_type: str, slots_dict: dict[str, Slot]) -> None:
        super().__init__()
        self.template_type: str = template_type
        self.slots: dict[str, Slot] = slots_dict
        for slot in self.slots.values():
            slot.parent = self

    def get_all_slots(self) -> list[Slot]:
        """Obtiene la lista aplanada de todas las casillas contenidas recursivamente.

        Returns:
            Lista de todas las casillas hijas en orden jerárquico.
        """
        result = []
        for slot in self.slots.values():
            result.extend(slot.get_all_child_slots())
        return result


class FractionNode(TemplateNode):
    """Plantilla interactiva para fracciones matemáticas (\\frac{num}{den})."""

    def __init__(self) -> None:
        super().__init__(
            "fraction", {"num": Slot("numerador"), "den": Slot("denominador")}
        )

    def to_latex(self) -> str:
        """Genera la representación LaTeX de la fracción.

        Returns:
            Código LaTeX formateado con comando \\frac.
        """
        num_tex = self.slots["num"].to_latex()
        den_tex = self.slots["den"].to_latex()
        return f"\\frac{{ {num_tex} }}{{ {den_tex} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la fracción para el editor interactivo.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato (num / den).
        """
        num = self.slots["num"].to_display_text(active_slot_id)
        den = self.slots["den"].to_display_text(active_slot_id)
        return f"({num} / {den})"


class PowerNode(TemplateNode):
    """Plantilla interactiva para potencias y exponentes (base^{exp})."""

    def __init__(self) -> None:
        super().__init__("power", {"base": Slot("base"), "exp": Slot("exponente")})

    def to_latex(self) -> str:
        """Genera la representación LaTeX de la potencia.

        Returns:
            Código LaTeX formateado en la forma {base}^{exp}.
        """
        base_tex = self.slots["base"].to_latex()
        exp_tex = self.slots["exp"].to_latex()
        return f"{{ {base_tex} }}^{{ {exp_tex} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la potencia para el editor.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato (base^{exp}).
        """
        base = self.slots["base"].to_display_text(active_slot_id)
        exp = self.slots["exp"].to_display_text(active_slot_id)
        return f"({base}^{{{exp}}})"


class SubscriptNode(TemplateNode):
    """Plantilla interactiva para subíndices (base_{sub})."""

    def __init__(self) -> None:
        super().__init__("subscript", {"base": Slot("base"), "sub": Slot("subíndice")})

    def to_latex(self) -> str:
        """Genera la representación LaTeX del subíndice.

        Returns:
            Código LaTeX formateado en la forma {base}_{sub}.
        """
        base_tex = self.slots["base"].to_latex()
        sub_tex = self.slots["sub"].to_latex()
        return f"{{ {base_tex} }}_{{ {sub_tex} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano del subíndice para el editor.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato (base_{sub}).
        """
        base = self.slots["base"].to_display_text(active_slot_id)
        sub = self.slots["sub"].to_display_text(active_slot_id)
        return f"({base}_{{{sub}}})"


class SubSupNode(TemplateNode):
    """Plantilla interactiva combinada con subíndice y superíndice simultáneos ({base}_{sub}^{sup})."""

    def __init__(self) -> None:
        super().__init__(
            "subsup",
            {
                "base": Slot("base"),
                "sub": Slot("subíndice"),
                "sup": Slot("superíndice"),
            },
        )

    def to_latex(self) -> str:
        """Genera la representación LaTeX del nodo combinado.

        Returns:
            Código LaTeX en formato {base}_{sub}^{sup}.
        """
        b = self.slots["base"].to_latex()
        s = self.slots["sub"].to_latex()
        p = self.slots["sup"].to_latex()
        return f"{{ {b} }}_{{ {s} }}^{{ {p} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano del nodo combinado.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato (base_{sub}^{sup}).
        """
        b = self.slots["base"].to_display_text(active_slot_id)
        s = self.slots["sub"].to_display_text(active_slot_id)
        p = self.slots["sup"].to_display_text(active_slot_id)
        return f"({b}_{{{s}}}^{{{p}}})"


class SquareRootNode(TemplateNode):
    """Plantilla interactiva para raíces cuadradas (\\sqrt{radicand})."""

    def __init__(self) -> None:
        super().__init__("sqrt", {"radicand": Slot("radicando")})

    def to_latex(self) -> str:
        """Genera el código LaTeX de la raíz cuadrada.

        Returns:
            Código LaTeX con comando \\sqrt.
        """
        rad = self.slots["radicand"].to_latex()
        return f"\\sqrt{{ {rad} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la raíz cuadrada.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato √(radicand).
        """
        rad = self.slots["radicand"].to_display_text(active_slot_id)
        return f"√({rad})"


class NthRootNode(TemplateNode):
    """Plantilla interactiva para raíces de orden n (\\sqrt[index]{radicand})."""

    def __init__(self) -> None:
        super().__init__(
            "nth_root", {"index": Slot("índice"), "radicand": Slot("radicando")}
        )

    def to_latex(self) -> str:
        """Genera el código LaTeX de la raíz enésima.

        Returns:
            Código LaTeX con comando \\sqrt[n]{x}.
        """
        idx = self.slots["index"].to_latex()
        rad = self.slots["radicand"].to_latex()
        return f"\\sqrt[{idx}]{{ {rad} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la raíz enésima.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato ^(index)√(radicand).
        """
        idx = self.slots["index"].to_display_text(active_slot_id)
        rad = self.slots["radicand"].to_display_text(active_slot_id)
        return f"^{idx}√({rad})"


class DefiniteIntegralNode(TemplateNode):
    """Plantilla interactiva para integrales definidas con límites (\\int_{lower}^{upper} body \\, dvar)."""

    def __init__(self) -> None:
        super().__init__(
            "def_integral",
            {
                "lower": Slot("límite inferior"),
                "upper": Slot("límite superior"),
                "body": Slot("integrando"),
                "var": Slot("variable"),
            },
        )

    def to_latex(self) -> str:
        """Genera el código LaTeX de la integral definida.

        Returns:
            Código LaTeX formateado con límites inferior y superior.
        """
        low = self.slots["lower"].to_latex()
        up = self.slots["upper"].to_latex()
        body = self.slots["body"].to_latex()
        v = self.slots["var"].to_latex() or "x"
        return f"\\int_{{ {low} }}^{{ {up} }} {{ {body} }} \\, d{{ {v} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la integral definida.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato ∫_low^up (body) dvar.
        """
        low = self.slots["lower"].to_display_text(active_slot_id)
        up = self.slots["upper"].to_display_text(active_slot_id)
        body = self.slots["body"].to_display_text(active_slot_id)
        v = self.slots["var"].to_display_text(active_slot_id)
        return f"∫_{low}^{up} ({body}) d{v}"


class IndefiniteIntegralNode(TemplateNode):
    """Plantilla interactiva para integrales indefinidas (\\int body \\, dvar)."""

    def __init__(self) -> None:
        super().__init__(
            "indef_integral", {"body": Slot("integrando"), "var": Slot("variable")}
        )

    def to_latex(self) -> str:
        """Genera el código LaTeX de la integral indefinida.

        Returns:
            Código LaTeX con comando \\int.
        """
        body = self.slots["body"].to_latex()
        v = self.slots["var"].to_latex() or "x"
        return f"\\int {{ {body} }} \\, d{{ {v} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la integral indefinida.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato ∫ (body) dvar.
        """
        body = self.slots["body"].to_display_text(active_slot_id)
        v = self.slots["var"].to_display_text(active_slot_id)
        return f"∫ ({body}) d{v}"


class ContourIntegralNode(TemplateNode):
    """Nodo AST interactivo para integral de contorno cerrado (\\oint)."""

    def __init__(self) -> None:
        super().__init__(
            "contour_integral",
            {
                "lower": Slot("trayectoria C / límite inf"),
                "upper": Slot("límite superior"),
                "body": Slot("integrando"),
                "var": Slot("diferencial dr"),
            },
        )

    def to_latex(self) -> str:
        """Genera el código LaTeX de la integral de contorno.

        Returns:
            Código LaTeX con comando \\oint.
        """
        low = self.slots["lower"].to_latex()
        up = self.slots["upper"].to_latex()
        body = self.slots["body"].to_latex()
        v = self.slots["var"].to_latex() or "r"
        limits = ""
        if low and up:
            limits = f"_{{ {low} }}^{{ {up} }}"
        elif low:
            limits = f"_{{ {low} }}"
        elif up:
            limits = f"^{{ {up} }}"
        return f"\\oint{limits} {{ {body} }} \\, d{{ {v} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la integral de contorno.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato ∮_low^up (body) dvar.
        """
        low = self.slots["lower"].to_display_text(active_slot_id)
        up = self.slots["upper"].to_display_text(active_slot_id)
        body = self.slots["body"].to_display_text(active_slot_id)
        v = self.slots["var"].to_display_text(active_slot_id)
        return f"∮_{low}^{up} ({body}) d{v}"


class DoubleIntegralNode(TemplateNode):
    """Nodo AST interactivo para integral doble de superficie (\\iint)."""

    def __init__(self) -> None:
        super().__init__(
            "double_integral",
            {
                "lower": Slot("región / superficie S"),
                "upper": Slot("límite superior"),
                "body": Slot("integrando"),
                "var": Slot("diferencial dA"),
            },
        )

    def to_latex(self) -> str:
        """Genera el código LaTeX de la integral doble.

        Returns:
            Código LaTeX con comando \\iint.
        """
        low = self.slots["lower"].to_latex()
        up = self.slots["upper"].to_latex()
        body = self.slots["body"].to_latex()
        v = self.slots["var"].to_latex() or "A"
        limits = ""
        if low and up:
            limits = f"_{{ {low} }}^{{ {up} }}"
        elif low:
            limits = f"_{{ {low} }}"
        elif up:
            limits = f"^{{ {up} }}"
        return f"\\iint{limits} {{ {body} }} \\, d{{ {v} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la integral doble.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato ∬_low^up (body) dvar.
        """
        low = self.slots["lower"].to_display_text(active_slot_id)
        up = self.slots["upper"].to_display_text(active_slot_id)
        body = self.slots["body"].to_display_text(active_slot_id)
        v = self.slots["var"].to_display_text(active_slot_id)
        return f"∬_{low}^{up} ({body}) d{v}"


class TripleIntegralNode(TemplateNode):
    """Nodo AST interactivo para integral triple de volumen (\\iiint)."""

    def __init__(self) -> None:
        super().__init__(
            "triple_integral",
            {
                "lower": Slot("región / volumen V"),
                "upper": Slot("límite superior"),
                "body": Slot("integrando"),
                "var": Slot("diferencial dV"),
            },
        )

    def to_latex(self) -> str:
        """Genera el código LaTeX de la integral triple.

        Returns:
            Código LaTeX con comando \\iiint.
        """
        low = self.slots["lower"].to_latex()
        up = self.slots["upper"].to_latex()
        body = self.slots["body"].to_latex()
        v = self.slots["var"].to_latex() or "V"
        limits = ""
        if low and up:
            limits = f"_{{ {low} }}^{{ {up} }}"
        elif low:
            limits = f"_{{ {low} }}"
        elif up:
            limits = f"^{{ {up} }}"
        return f"\\iiint{limits} {{ {body} }} \\, d{{ {v} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la integral triple.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato ∭_low^up (body) dvar.
        """
        low = self.slots["lower"].to_display_text(active_slot_id)
        up = self.slots["upper"].to_display_text(active_slot_id)
        body = self.slots["body"].to_display_text(active_slot_id)
        v = self.slots["var"].to_display_text(active_slot_id)
        return f"∭_{low}^{up} ({body}) d{v}"


class SummationNode(TemplateNode):
    """Plantilla interactiva para sumatorias con límites (\\sum_{lower}^{upper} body)."""

    def __init__(self) -> None:
        super().__init__(
            "summation",
            {
                "lower": Slot("inicio (ej. i=1)"),
                "upper": Slot("fin (ej. n)"),
                "body": Slot("expresión"),
            },
        )

    def to_latex(self) -> str:
        """Genera el código LaTeX de la sumatoria.

        Returns:
            Código LaTeX formateado con comando \\sum.
        """
        low = self.slots["lower"].to_latex()
        up = self.slots["upper"].to_latex()
        body = self.slots["body"].to_latex()
        return f"\\sum_{{ {low} }}^{{ {up} }} {{ {body} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la sumatoria para visualización interactiva.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato ∑_low^up (body).
        """
        low = self.slots["lower"].to_display_text(active_slot_id)
        up = self.slots["upper"].to_display_text(active_slot_id)
        body = self.slots["body"].to_display_text(active_slot_id)
        return f"∑_{low}^{up} ({body})"


class LimitNode(TemplateNode):
    """Plantilla interactiva para límites matemáticos (\\lim_{var \\to target} body)."""

    def __init__(self) -> None:
        super().__init__(
            "limit",
            {
                "var": Slot("variable"),
                "target": Slot("tiende a"),
                "body": Slot("expresión"),
            },
        )

    def to_latex(self) -> str:
        """Genera el código LaTeX del límite matemático.

        Returns:
            Código LaTeX formateado con comando \\lim.
        """
        v = self.slots["var"].to_latex() or "x"
        t = self.slots["target"].to_latex() or "0"
        body = self.slots["body"].to_latex()
        return f"\\lim_{{ {v} \\to {t} }} {{ {body} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano del límite para el editor.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato lim(var→target) (body).
        """
        v = self.slots["var"].to_display_text(active_slot_id)
        t = self.slots["target"].to_display_text(active_slot_id)
        body = self.slots["body"].to_display_text(active_slot_id)
        return f"lim({v}→{t}) ({body})"


class BracketNode(TemplateNode):
    """Plantilla interactiva para delimitadores agrupadores adaptables (paréntesis, corchetes, llaves, barras).

    Args:
        left_delim: Delimitador de apertura ('(', '[', '{', '|').
        right_delim: Delimitador de cierre (')', ']', '}', '|').
    """

    def __init__(self, left_delim: str = "(", right_delim: str = ")") -> None:
        self.left_delim = left_delim
        self.right_delim = right_delim
        super().__init__("bracket", {"body": Slot("contenido")})

    def to_latex(self) -> str:
        """Genera el código LaTeX con comandos de escalado automático \\left y \\right.

        Returns:
            Código LaTeX formateado.
        """
        body = self.slots["body"].to_latex()
        left_map = {
            "(": "\\left(",
            "[": "\\left[",
            "{": "\\left\\{",
            "|": "\\left\\vert",
        }
        right_map = {
            ")": "\\right)",
            "]": "\\right]",
            "}": "\\right\\}",
            "|": "\\right\\vert",
        }
        l_tex = left_map.get(self.left_delim, f"\\left{self.left_delim}")
        r_tex = right_map.get(self.right_delim, f"\\right{self.right_delim}")
        return f"{l_tex} {{ {body} }} {r_tex}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano del delimitador.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto encapsulado en los delimitadores configurados.
        """
        body = self.slots["body"].to_display_text(active_slot_id)
        return f"{self.left_delim}{body}{self.right_delim}"


class MatrixNode(TemplateNode):
    """Plantilla interactiva para matrices rectangulares de R filas por C columnas.

    Args:
        rows: Número de filas.
        cols: Número de columnas.
        matrix_type: Tipo de entorno LaTeX ('matrix', 'pmatrix', 'bmatrix', 'vmatrix', 'Vmatrix').
    """

    def __init__(
        self, rows: int = 2, cols: int = 2, matrix_type: str = "pmatrix"
    ) -> None:
        self.rows = rows
        self.cols = cols
        self.matrix_type = matrix_type
        slots_dict = {}
        for r in range(rows):
            for c in range(cols):
                slots_dict[f"cell_{r}_{c}"] = Slot(f"celda ({r + 1},{c + 1})")
        super().__init__("matrix", slots_dict)

    def to_latex(self) -> str:
        """Genera el código LaTeX del entorno matricial.

        Returns:
            Código LaTeX formateado con & y \\\\.
        """
        rows_tex = []
        for r in range(self.rows):
            row_cells = []
            for c in range(self.cols):
                cell_tex = self.slots[f"cell_{r}_{c}"].to_latex()
                row_cells.append(cell_tex)
            rows_tex.append(" & ".join(row_cells))
        matrix_body = " \\\\ ".join(rows_tex)
        return (
            f"\\begin{{{self.matrix_type}}} {matrix_body} \\end{{{self.matrix_type}}}"
        )

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la matriz.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato [celdas fila 1 | celdas fila 2].
        """
        rows_str = []
        for r in range(self.rows):
            row_cells = [
                self.slots[f"cell_{r}_{c}"].to_display_text(active_slot_id)
                for c in range(self.cols)
            ]
            rows_str.append(", ".join(row_cells))
        return f"[{' | '.join(rows_str)}]"


class DerivativeNode(TemplateNode):
    """Plantilla interactiva para derivadas ordinarias o parciales (\\frac{d f}{d x} o \\frac{\\partial f}{\\partial x}).

    Args:
        is_partial: True si es derivada parcial (∂); False si es derivada ordinaria (d).
    """

    def __init__(self, is_partial: bool = False) -> None:
        self.is_partial = is_partial
        super().__init__(
            "derivative", {"func": Slot("función / expresión"), "var": Slot("variable")}
        )

    def to_latex(self) -> str:
        """Genera el código LaTeX de la derivada.

        Returns:
            Código LaTeX con comando \\frac y operadores d o \\partial.
        """
        f = self.slots["func"].to_latex()
        v = self.slots["var"].to_latex() or "x"
        d = "\\partial" if self.is_partial else "d"
        return f"\\frac{{ {d} {{ {f} }} }}{{ {d} {{ {v} }} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la derivada.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato (df / dx) o (∂f / ∂x).
        """
        f = self.slots["func"].to_display_text(active_slot_id)
        v = self.slots["var"].to_display_text(active_slot_id)
        sym = "∂" if self.is_partial else "d"
        return f"({sym}{f} / {sym}{v})"


class StyleDecoratorNode(TemplateNode):
    """Plantilla interactiva para decoradores y modificadores de estilo (\\mathbf, \\vec, \\hat, etc.).

    Args:
        style_cmd: Nombre del comando TeX (ej. 'mathbf', 'vec', 'hat', 'mathcal').
    """

    def __init__(self, style_cmd: str) -> None:
        super().__init__("style_decorator", {"body": Slot("contenido")})
        self.style_cmd = style_cmd

    def to_latex(self) -> str:
        """Genera el código LaTeX del decorador de estilo.

        Returns:
            Código LaTeX en formato \\cmd{body}.
        """
        body = self.slots["body"].to_latex()
        return f"\\{self.style_cmd}{{{body}}}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano con representaciones unicode para el editor.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto formateado con prefijo/sufijo decorador.
        """
        body = self.slots["body"].to_display_text(active_slot_id)

        # Mapa de estilos a representaciones visuales unicode para el editor de texto
        style_map = {
            "mathbf": ("𝐁[", "]"),
            "textbf": ("𝐁[", "]"),
            "mathit": ("𝐼[", "]"),
            "textit": ("𝐼[", "]"),
            "mathrm": ("𝐑[", "]"),
            "textrm": ("𝐑[", "]"),
            "mathsf": ("𝗦[", "]"),
            "textsf": ("𝗦[", "]"),
            "mathtt": ("𝚃[", "]"),
            "texttt": ("𝚃[", "]"),
            "mathbb": ("𝔹[", "]"),
            "mathcal": ("𝓒[", "]"),
            "mathfrak": ("𝔉[", "]"),
            "text": ("", ""),
            "vec": ("", "\u20d7"),  # Combining Right Arrow Above
            "hat": ("", "\u0302"),  # Combining Circumflex
            "bar": ("", "\u0304"),  # Combining Macron
            "tilde": ("", "\u0303"),  # Combining Tilde
            "ddot": ("", "\u0308"),  # Combining Diaeresis
            "dot": ("", "\u0307"),  # Combining Dot Above
        }

        prefix, suffix = style_map.get(self.style_cmd, (f"{self.style_cmd}(", ")"))
        return f"{prefix}{body}{suffix}"


class BinomialNode(TemplateNode):
    """Plantilla interactiva para coeficientes binomiales y combinatorios (\\binom{n}{k})."""

    def __init__(self) -> None:
        super().__init__(
            "binomial", {"n": Slot("n (superior)"), "k": Slot("k (inferior)")}
        )

    def to_latex(self) -> str:
        """Genera el código LaTeX del coeficiente binomial.

        Returns:
            Código LaTeX con comando \\binom.
        """
        n_tex = self.slots["n"].to_latex()
        k_tex = self.slots["k"].to_latex()
        return f"\\binom{{ {n_tex} }}{{ {k_tex} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano del coeficiente binomial.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato binom(n, k).
        """
        n = self.slots["n"].to_display_text(active_slot_id)
        k = self.slots["k"].to_display_text(active_slot_id)
        return f"binom({n}, {k})"


class ModularNode(TemplateNode):
    """Plantilla interactiva para congruencia modular (\\pmod{m})."""

    def __init__(self) -> None:
        super().__init__("modular", {"mod": Slot("módulo")})

    def to_latex(self) -> str:
        """Genera el código LaTeX de la congruencia modular.

        Returns:
            Código LaTeX con comando \\pmod.
        """
        mod_tex = self.slots["mod"].to_latex().strip()
        return f"\\pmod{{ {mod_tex} }}"

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la congruencia modular.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato (mod m).
        """
        m = self.slots["mod"].to_display_text(active_slot_id)
        return f"(mod {m})"


class ProductNode(TemplateNode):
    """Plantilla interactiva para productorias con límites (\\prod_{lower}^{upper} body)."""

    def __init__(self) -> None:
        super().__init__(
            "product",
            {
                "lower": Slot("límite inferior / condición"),
                "upper": Slot("límite superior"),
                "body": Slot("expresión / factor"),
            },
        )

    def to_latex(self) -> str:
        """Genera el código LaTeX de la productoria.

        Returns:
            Código LaTeX con comando \\prod.
        """
        low = self.slots["lower"].to_latex().strip()
        up = self.slots["upper"].to_latex().strip()
        body = self.slots["body"].to_latex()
        parts = ["\\prod"]
        if low:
            parts.append(f"_{{ {low} }}")
        if up:
            parts.append(f"^{{ {up} }}")
        if body:
            parts.append(f" {body}")
        return "".join(parts)

    def to_display_text(self, active_slot_id: str | None = None) -> str:
        """Genera el texto plano de la productoria.

        Args:
            active_slot_id: Identificador de la casilla activa.

        Returns:
            Texto en formato ∏_low^up (body).
        """
        low = self.slots["lower"].to_display_text(active_slot_id)
        up = self.slots["upper"].to_display_text(active_slot_id)
        body = self.slots["body"].to_display_text(active_slot_id)
        limits = ""
        if low or up:
            limits = f"_{{{low}}}^{{{up}}}"
        return f"∏{limits} ({body})"


class MathTree:
    """Gestor principal del estado del árbol de la ecuación.

    Mantiene la jerarquía completa empezando desde un `Slot` raíz,
    gestiona el foco actual (`active_slot`) para navegación por teclado/clics,
    y preserva el historial de cambios (Undo/Redo stack).
    """

    def __init__(self) -> None:
        self.root_slot: Slot = Slot("expresión principal")
        self.active_slot: Slot = self.root_slot
        self.undo_stack: list[str] = []
        self.redo_stack: list[str] = []

    def set_active_slot(self, slot: Slot) -> None:
        """Establece la casilla activa con el foco del cursor.

        Args:
            slot: Instancia de `Slot` que recibirá el foco.
        """
        self.active_slot = slot

    def insert_node(self, node: MathNode) -> None:
        """Inserta un nodo matemático en la casilla activa y guarda el estado.

        Si el nodo insertado es una plantilla (`TemplateNode`), transfiere automáticamente
        el foco a su primera casilla hija.

        Args:
            node: Instancia de `MathNode` a insertar.
        """
        self.save_state()
        self.active_slot.add_node(node)

        # If the inserted node is a TemplateNode, auto-focus its first child slot
        child_slots = node.get_all_slots()
        if child_slots:
            self.active_slot = child_slots[0]

    def insert_nodes(self, nodes: list[MathNode]) -> None:
        """Inserta una secuencia de nodos matemáticos consecutivamente en la casilla activa.

        Args:
            nodes: Lista de instancias de `MathNode` a insertar.
        """
        self.save_state()
        first_child_slot = None
        for node in nodes:
            self.active_slot.add_node(node)
            if not first_child_slot:
                child_slots = node.get_all_slots()
                if child_slots:
                    first_child_slot = child_slots[0]

        if first_child_slot:
            self.active_slot = first_child_slot

    def insert_text(self, text: str) -> None:
        """Inserta texto plano en la casilla activa.

        Args:
            text: Texto o caracteres a insertar.
        """
        self.save_state()
        self.active_slot.insert_text(text)

    def remove_last(self) -> None:
        """Elimina el último nodo de la casilla activa o retrocede a la casilla anterior si está vacía."""
        self.save_state()
        removed = self.active_slot.remove_last_node()
        if not removed and self.active_slot != self.root_slot:
            # If current slot is empty and backspace pressed, jump to previous slot
            all_slots = self.get_all_slots()
            idx = (
                all_slots.index(self.active_slot)
                if self.active_slot in all_slots
                else 0
            )
            if idx > 0:
                self.active_slot = all_slots[idx - 1]

    def remove_active_template(self) -> None:
        """Elimina la plantilla contenedora de la casilla activa y devuelve el foco a la ranura padre."""
        self.save_state()
        if self.active_slot == self.root_slot:
            return

        template = self.active_slot.parent
        if not template or not template.parent_slot:
            return

        parent_slot = template.parent_slot
        if template in parent_slot.nodes:
            idx = parent_slot.nodes.index(template)
            parent_slot.nodes.remove(template)
            parent_slot.cursor_position = min(idx, len(parent_slot.nodes))

        self.active_slot = parent_slot

    def clear_all(self) -> None:
        """Reinicia el árbol completo a una casilla raíz vacía."""
        self.save_state()
        self.root_slot.clear()
        self.active_slot = self.root_slot

    def get_all_slots(self) -> list[Slot]:
        """Obtiene todas las casillas del árbol en orden de navegación jerárquica.

        Returns:
            Lista completa de casillas (`Slot`) contenidas en el árbol.
        """
        return self.root_slot.get_all_child_slots()

    def navigate_next_slot(self) -> Slot:
        """Avanza cíclicamente el foco activo a la siguiente casilla del árbol.

        Returns:
            La nueva casilla activa (`Slot`).
        """
        all_slots = self.get_all_slots()
        if not all_slots:
            return self.root_slot
        try:
            curr_idx = all_slots.index(self.active_slot)
            next_idx = (curr_idx + 1) % len(all_slots)
            self.active_slot = all_slots[next_idx]
        except ValueError:
            self.active_slot = all_slots[0]
        return self.active_slot

    def navigate_prev_slot(self) -> Slot:
        """Retrocede cíclicamente el foco activo a la casilla previa del árbol.

        Returns:
            La nueva casilla activa (`Slot`).
        """
        all_slots = self.get_all_slots()
        if not all_slots:
            return self.root_slot
        try:
            curr_idx = all_slots.index(self.active_slot)
            prev_idx = (curr_idx - 1) % len(all_slots)
            self.active_slot = all_slots[prev_idx]
        except ValueError:
            self.active_slot = all_slots[-1]
        return self.active_slot

    def to_latex(self) -> str:
        """Exporta todo el contenido estructurado del árbol a código LaTeX.

        Returns:
            Cadena de código LaTeX representativo de la ecuación.
        """
        return self.root_slot.to_latex()

    def to_display_text(self) -> str:
        """Exporta la representación visual de la ecuación con indicadores de foco activo.

        Returns:
            Texto plano formateado para el visor o editor interactivo.
        """
        return self.root_slot.to_display_text(self.active_slot.id)

    def save_state(self) -> None:
        """Registra una instantánea de la fórmula actual en la pila de deshacer."""
        # Save snapshot for undo
        self.undo_stack.append(self.to_latex())
        self.redo_stack.clear()
        if len(self.undo_stack) > 30:
            self.undo_stack.pop(0)
