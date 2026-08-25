/**
 * ---
 * file: mathjax_build/sanitizer.js
 * module: mathjax_build.sanitizer
 * description: Sanitizador y normalizador de código XML SVG para compatibilidad con Qt TinySVG.
 * type: build/transformer
 * version: 1.0.0
 * date: 2026-08-24
 * dependencies: []
 * relations:
 *   - mathjax_build/renderer.js
 *   - src/assets/mathjax_bundle.js
 * exports:
 *   - stripSvgDimensions: "Remueve atributos width/height para forzar escalado por viewBox"
 *   - ensureSvgXmlns: "Garantiza la presencia de los espacios de nombres XML estándar"
 *   - applySvgTheme: "Inyecta estilos CSS para forzar el color de tema en todos los nodos SVG"
 *   - generateFallbackSvg: "Genera un SVG de respaldo en caso de error de compilación"
 *   - sanitizeSvgOutput: "Ejecuta la canalización completa de sanitización"
 * test: node --test tests/test_mathjax_build.js
 * constraints:
 *   - "Mantener rectángulos de fondo transparentes y aislar colores temáticos mediante CSS"
 * keywords:
 *   - svg-sanitizer
 *   - tinysvg-compat
 *   - xmlns-injector
 *   - theme-styler
 * ---
 */

'use strict';

/**
 * Remueve los atributos de dimensión fija (`width` y `height`) exclusivamente del elemento `<svg>` raíz.
 *
 * Esto es necesario para que el motor de renderizado TinySVG de Qt (usado por `QSvgRenderer`)
 * no restrinja la escala geométrica a valores fijos en píxeles, permitiendo un escalado
 * adaptativo dinámico basado exclusivamente en las coordenadas del `viewBox`.
 *
 * Se utiliza negative lookbehind para evitar remover erróneamente atributos internos como `stroke-width`.
 *
 * @param {string} svgStr - Cadena de texto que contiene el marcado XML del SVG.
 * @returns {string} Código XML SVG sin los atributos width y height fijos en la raíz.
 */
function stripSvgDimensions(svgStr) {
    if (!svgStr || typeof svgStr !== 'string') {
        return '';
    }
    return svgStr.replace(/<svg\b([^>]*)>/i, (match, attrs) => {
        const cleanedAttrs = attrs
            .replace(/(?<![\w-])width="[^"]*"/g, '')
            .replace(/(?<![\w-])height="[^"]*"/g, '');
        return `<svg${cleanedAttrs}>`;
    });
}

/**
 * Asegura que el elemento raíz `<svg>` posea las declaraciones de espacios de nombres (XMLNS).
 *
 * @param {string} svgStr - Cadena de texto con el código XML SVG.
 * @returns {string} Código XML SVG garantizando la presencia de xmlns y xmlns:xlink.
 */
function ensureSvgXmlns(svgStr) {
    if (!svgStr || typeof svgStr !== 'string') {
        return '';
    }
    if (!svgStr.includes('xmlns="http://www.w3.org/2000/svg"')) {
        svgStr = svgStr.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"');
    }
    return svgStr;
}

/**
 * Inyecta una regla de estilo CSS en el SVG y reemplaza `currentColor` por el color del tema activo.
 *
 * @param {string} svgStr - Cadena de texto con el código XML SVG.
 * @param {string} themeColor - Color hexadecimal a aplicar a los glifos (ej. '#39C5BB').
 * @returns {string} Código XML SVG con estilos de color inyectados.
 */
function applySvgTheme(svgStr, themeColor) {
    if (!svgStr || typeof svgStr !== 'string') {
        return '';
    }
    const color = themeColor || '#39C5BB';
    let themed = svgStr.replace(/currentColor/g, color);
    const styleNode = `<style>svg * { fill: ${color} !important; stroke: ${color} !important; } svg rect[data-background="true"] { fill: transparent !important; stroke: none !important; }</style>`;
    themed = themed.replace('</svg>', `${styleNode}</svg>`);
    return themed;
}

/**
 * Genera un elemento SVG de reserva cuando ocurre un error de sintaxis o evaluación en LaTeX.
 *
 * @param {string} errorMessage - Mensaje de error descriptivo capturado.
 * @param {string} [themeColor='#FF5555'] - Color hexadecimal para el texto de error.
 * @returns {string} Marcado XML SVG conteniendo el texto de error.
 */
function generateFallbackSvg(errorMessage, themeColor) {
    const color = themeColor || '#FF5555';
    const escaped = String(errorMessage || 'Error de compilación')
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
    return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 30"><text x="0" y="20" fill="${color}" font-size="12" font-family="sans-serif">${escaped}</text></svg>`;
}

/**
 * Ejecuta la secuencia completa de sanitización, ajuste de dimensiones y tematizado sobre un SVG.
 *
 * @param {string} rawSvg - Código SVG en bruto retornado por MathJax.
 * @param {string} themeColor - Color hexadecimal del tema activo.
 * @returns {string} Código SVG normalizado y listo para su consumo en PySide6.
 */
function sanitizeSvgOutput(rawSvg, themeColor) {
    let svg = stripSvgDimensions(rawSvg);
    svg = ensureSvgXmlns(svg);
    svg = applySvgTheme(svg, themeColor);
    return svg;
}

module.exports = {
    stripSvgDimensions,
    ensureSvgXmlns,
    applySvgTheme,
    generateFallbackSvg,
    sanitizeSvgOutput
};
