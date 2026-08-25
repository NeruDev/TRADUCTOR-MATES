/**
 * ---
 * file: mathjax_build/renderer.js
 * module: mathjax_build.renderer
 * description: Función principal de renderizado síncrono que orquesta la compilación y sanitización SVG.
 * type: build/renderer
 * version: 1.0.0
 * date: 2026-08-24
 * dependencies:
 *   - mathjax_build.engine
 *   - mathjax_build.sanitizer
 * relations:
 *   - mathjax_build/index.js
 *   - src/assets/mathjax_bundle.js
 * exports:
 *   - renderMathSync: "Renderiza síncronamente una fórmula LaTeX a código SVG sanitizado y coloreado"
 * test: node --test tests/test_mathjax_build.js
 * constraints:
 *   - "Soportar simultáneamente firma moderna (2 args) y compatible (3 args) sin lanzar excepciones no controladas"
 * keywords:
 *   - mathjax-renderer
 *   - sync-renderer
 *   - svg-generator
 *   - error-fallback
 * ---
 */

'use strict';

const { convertLatexToSvgNode, nodeToOuterHtml } = require('./engine.js');
const { sanitizeSvgOutput, generateFallbackSvg } = require('./sanitizer.js');

/**
 * Renderiza síncronamente una cadena LaTeX y devuelve un fragmento XML SVG válido y tematizado.
 *
 * Esta función es invocada directamente desde Python a través del contexto V8 de MiniRacer.
 * Admite tanto la firma moderna de dos argumentos `(latexText, themeColor)` como la firma
 * heredada de tres argumentos `(latexText, themeBg, themeText)` para garantizar completa
 * compatibilidad hacia atrás con todos los componentes existentes.
 *
 * @param {string} latexText - Expresión matemática en formato LaTeX.
 * @param {string} [themeBgOrColor='#39C5BB'] - Fondo (legado) o color primario del tema en formato HEX.
 * @param {string} [themeText] - Color del texto/trazos matemáticos (en firma de 3 parámetros).
 * @returns {string} Código XML SVG sanitizado, compatible con TinySVG y listo para QSvgRenderer.
 */
function renderMathSync(latexText, themeBgOrColor, themeText) {
    // Determinar el color final del tema admitiendo firmas de 2 o 3 parámetros
    const activeColor = themeText || themeBgOrColor || '#39C5BB';

    try {
        const svgNode = convertLatexToSvgNode(latexText);
        const rawSvg = nodeToOuterHtml(svgNode);
        return sanitizeSvgOutput(rawSvg, activeColor);
    } catch (err) {
        const errorMsg = (err && err.message) ? err.message : String(err);
        return generateFallbackSvg(errorMsg, activeColor);
    }
}

module.exports = {
    renderMathSync
};
