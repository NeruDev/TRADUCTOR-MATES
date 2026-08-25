/**
 * ---
 * file: mathjax_build/index.js
 * module: mathjax_build.index
 * description: Punto de entrada principal para el bundle de MathJax en Traductor Mates.
 * type: build/entrypoint
 * version: 1.0.0
 * date: 2026-08-24
 * dependencies:
 *   - mathjax_build.package_config
 *   - mathjax_build.sanitizer
 *   - mathjax_build.engine
 *   - mathjax_build.renderer
 * relations:
 *   - mathjax_build/build.js
 *   - src/assets/mathjax_bundle.js
 * exports:
 *   - renderMathSync: "Punto de acceso global para renderizado síncrono en V8 / MiniRacer"
 * test: node --test tests/test_mathjax_build.js
 * constraints:
 *   - "Registrar renderMathSync en globalThis/global/this para ejecución directa en VM de Python"
 * keywords:
 *   - mathjax-index
 *   - bundle-entrypoint
 *   - global-scope
 *   - v8-bridge
 * ---
 */

'use strict';

const { renderMathSync } = require('./renderer.js');
const { ACTIVE_PACKAGES } = require('./package_config.js');
const {
    stripSvgDimensions,
    ensureSvgXmlns,
    applySvgTheme,
    generateFallbackSvg,
    sanitizeSvgOutput
} = require('./sanitizer.js');
const {
    convertLatexToSvgNode,
    nodeToOuterHtml,
    getAdaptor,
    getMathDocument
} = require('./engine.js');

// Registrar la función global accesible para el motor MiniRacer (V8)
/* global globalThis */
const rootScope = typeof globalThis !== 'undefined'
    ? globalThis
    : (typeof global !== 'undefined' ? global : this);

rootScope.renderMathSync = renderMathSync;

module.exports = {
    renderMathSync,
    ACTIVE_PACKAGES,
    stripSvgDimensions,
    ensureSvgXmlns,
    applySvgTheme,
    generateFallbackSvg,
    sanitizeSvgOutput,
    convertLatexToSvgNode,
    nodeToOuterHtml,
    getAdaptor,
    getMathDocument
};
