/**
 * ---
 * file: mathjax_build/engine.js
 * module: mathjax_build.engine
 * description: Inicialización y gestión del motor MathJax para conversión de LaTeX a nodos SVG.
 * type: build/engine
 * version: 1.0.0
 * date: 2026-08-24
 * dependencies:
 *   - mathjax_build.package_config
 * relations:
 *   - mathjax_build/renderer.js
 *   - src/assets/mathjax_bundle.js
 * exports:
 *   - convertLatexToSvgNode: "Convierte una cadena LaTeX a un árbol de nodos LiteDOM de MathJax"
 *   - nodeToOuterHtml: "Serializa un nodo LiteDOM a su representación en cadena XML"
 *   - getAdaptor: "Obtiene la instancia de liteAdaptor activa"
 *   - getMathDocument: "Obtiene el documento MathJax configurado"
 *   - CUSTOM_MACROS: "Macros TeX personalizadas para casillas y plantillas estructuradas"
 * test: node --test tests/test_mathjax_build.js
 * constraints:
 *   - "Requerir explícitamente todas las extensiones TeX antes de la instanciación de MathJax"
 * keywords:
 *   - mathjax-engine
 *   - tex-to-svg
 *   - litedom
 *   - custom-macros
 * ---
 */

'use strict';

// Cargar explícitamente las configuraciones de extensiones TeX de MathJax
require('mathjax-full/js/input/tex/base/BaseConfiguration.js');
require('mathjax-full/js/input/tex/ams/AmsConfiguration.js');
require('mathjax-full/js/input/tex/boldsymbol/BoldsymbolConfiguration.js');
require('mathjax-full/js/input/tex/braket/BraketConfiguration.js');
require('mathjax-full/js/input/tex/cancel/CancelConfiguration.js');
require('mathjax-full/js/input/tex/cases/CasesConfiguration.js');
require('mathjax-full/js/input/tex/centernot/CenternotConfiguration.js');
require('mathjax-full/js/input/tex/color/ColorConfiguration.js');
require('mathjax-full/js/input/tex/configmacros/ConfigMacrosConfiguration.js');
require('mathjax-full/js/input/tex/empheq/EmpheqConfiguration.js');
require('mathjax-full/js/input/tex/enclose/EncloseConfiguration.js');
require('mathjax-full/js/input/tex/extpfeil/ExtpfeilConfiguration.js');
require('mathjax-full/js/input/tex/gensymb/GensymbConfiguration.js');
require('mathjax-full/js/input/tex/mathtools/MathtoolsConfiguration.js');
require('mathjax-full/js/input/tex/newcommand/NewcommandConfiguration.js');
require('mathjax-full/js/input/tex/noerrors/NoErrorsConfiguration.js');
require('mathjax-full/js/input/tex/noundefined/NoUndefinedConfiguration.js');
require('mathjax-full/js/input/tex/physics/PhysicsConfiguration.js');
require('mathjax-full/js/input/tex/tagformat/TagFormatConfiguration.js');
require('mathjax-full/js/input/tex/textcomp/TextcompConfiguration.js');
require('mathjax-full/js/input/tex/textmacros/TextMacrosConfiguration.js');
require('mathjax-full/js/input/tex/unicode/UnicodeConfiguration.js');
require('mathjax-full/js/input/tex/upgreek/UpgreekConfiguration.js');

const { mathjax } = require('mathjax-full/js/mathjax.js');
const { TeX } = require('mathjax-full/js/input/tex.js');
const { SVG } = require('mathjax-full/js/output/svg.js');
const { liteAdaptor } = require('mathjax-full/js/adaptors/liteAdaptor.js');
const { RegisterHTMLHandler } = require('mathjax-full/js/handlers/html.js');
const { ACTIVE_PACKAGES } = require('./package_config.js');

/**
 * Macros personalizadas para soporte de glifos y plantillas de casillas interactivas.
 * Define `\square`, `\Box` y `\blacksquare` apuntando a sus respectivos puntos de código Unicode.
 *
 * @type {Record<string, string>}
 */
const CUSTOM_MACROS = {
    square: '\\unicode{x25A1}',
    Box: '\\unicode{x25A1}',
    blacksquare: '\\unicode{x25A0}'
};

/** @type {ReturnType<typeof liteAdaptor>} */
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);

/** @type {TeX<unknown, unknown, unknown>} */
const texInput = new TeX({
    packages: ACTIVE_PACKAGES,
    macros: CUSTOM_MACROS
});

/** @type {SVG<unknown, unknown, unknown>} */
const svgOutput = new SVG({ fontCache: 'none' });

/**
 * Documento virtual MathJax configurado para renderizar expresiones LaTeX a SVG plano.
 */
const mathDocument = mathjax.document('', {
    InputJax: texInput,
    OutputJax: svgOutput
});

/**
 * Convierte una expresión matemática en LaTeX a un nodo LiteDOM.
 *
 * @param {string} latexText - Expresión en sintaxis LaTeX.
 * @returns {object} Nodo LiteDOM del SVG renderizado.
 * @throws {Error} Si la conversión en MathJax falla por sintaxis inválida.
 */
function convertLatexToSvgNode(latexText) {
    const safeLatex = (latexText && typeof latexText === 'string' && latexText.trim() !== '')
        ? latexText
        : '\\text{Selecciona o escribe una fórmula}';
    return mathDocument.convert(safeLatex, { display: true });
}

/**
 * Serializa un nodo LiteDOM de MathJax a una cadena XML SVG.
 *
 * @param {object} node - Nodo DOM retornado por convertLatexToSvgNode.
 * @returns {string} Marcado XML como cadena de texto.
 */
function nodeToOuterHtml(node) {
    return adaptor.outerHTML(node);
}

/**
 * Devuelve el adaptador LiteDOM activo.
 *
 * @returns {object} Instancia de LiteAdaptor.
 */
function getAdaptor() {
    return adaptor;
}

/**
 * Devuelve el documento MathJax activo.
 *
 * @returns {object} Instancia del documento MathJax.
 */
function getMathDocument() {
    return mathDocument;
}

module.exports = {
    convertLatexToSvgNode,
    nodeToOuterHtml,
    getAdaptor,
    getMathDocument,
    CUSTOM_MACROS
};
