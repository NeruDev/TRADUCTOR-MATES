/**
 * ---
 * file: tests/test_mathjax_build.js
 * module: tests.test_mathjax_build
 * description: Pruebas unitarias en JavaScript para los módulos de compilación de MathJax en mathjax_build.
 * type: test/unit
 * version: 1.0.0
 * date: 2026-08-24
 * dependencies: []
 * relations:
 *   - mathjax_build/package_config.js
 *   - mathjax_build/sanitizer.js
 *   - mathjax_build/engine.js
 *   - mathjax_build/renderer.js
 *   - mathjax_build/index.js
 * exports: []
 * test: node --test tests/test_mathjax_build.js
 * constraints:
 *   - "Validar el pipeline de sanitizado SVG y soporte de paquetes TeX esenciales"
 * keywords:
 *   - test-mathjax-build
 *   - sanitizer-tests
 *   - engine-tests
 *   - node-test
 * ---
 */

'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');

const { ACTIVE_PACKAGES } = require('../mathjax_build/package_config.js');
const {
    stripSvgDimensions,
    ensureSvgXmlns,
    applySvgTheme,
    generateFallbackSvg,
    sanitizeSvgOutput
} = require('../mathjax_build/sanitizer.js');
const {
    convertLatexToSvgNode,
    nodeToOuterHtml,
    getAdaptor,
    getMathDocument
} = require('../mathjax_build/engine.js');
const { renderMathSync } = require('../mathjax_build/renderer.js');
const indexModule = require('../mathjax_build/index.js');

test('Suite: mathjax_build/package_config.js', async (t) => {
    await t.test('Debe contener una lista válida de paquetes TeX esenciales', () => {
        assert.ok(Array.isArray(ACTIVE_PACKAGES), 'ACTIVE_PACKAGES debe ser un Array');
        assert.ok(ACTIVE_PACKAGES.length > 10, 'Debe incluir más de 10 paquetes matemáticos');
        
        const requiredPackages = [
            'base', 'ams', 'physics', 'mathtools', 'cancel',
            'textmacros', 'gensymb', 'extpfeil', 'unicode', 'upgreek'
        ];
        for (const pkg of requiredPackages) {
            assert.ok(
                ACTIVE_PACKAGES.includes(pkg),
                `ACTIVE_PACKAGES debe incluir el paquete '${pkg}'`
            );
        }
    });

    await t.test('No debe incluir paquetes legados o pesados descartados', () => {
        const legacyPackages = ['mhchem', 'bussproofs', 'colortbl', 'amscd', 'verb', 'action'];
        for (const legacy of legacyPackages) {
            assert.ok(
                !ACTIVE_PACKAGES.includes(legacy),
                `ACTIVE_PACKAGES NO debe incluir el paquete legado '${legacy}'`
            );
        }
    });
});

test('Suite: mathjax_build/sanitizer.js', async (t) => {
    await t.test('stripSvgDimensions: remueve width y height sólo del <svg> raíz sin dañar stroke-width', () => {
        const inputSvg = '<svg width="24.5ex" height="5.2ex" viewBox="0 0 100 20"><g stroke-width="0" stroke="currentColor"><path d="M0 0"/></g></svg>';
        const cleaned = stripSvgDimensions(inputSvg);
        
        assert.ok(!cleaned.includes('width="24.5ex"'), 'Debe remover width del svg');
        assert.ok(!cleaned.includes('height="5.2ex"'), 'Debe remover height del svg');
        assert.ok(cleaned.includes('viewBox="0 0 100 20"'), 'Debe conservar viewBox');
        assert.ok(cleaned.includes('stroke-width="0"'), 'NO debe romper stroke-width');
        assert.ok(!cleaned.includes('stroke- '), 'No debe generar atributos truncados como stroke-');
    });

    await t.test('stripSvgDimensions: maneja entradas vacías o inválidas de forma segura', () => {
        assert.strictEqual(stripSvgDimensions(''), '');
        assert.strictEqual(stripSvgDimensions(null), '');
        assert.strictEqual(stripSvgDimensions(undefined), '');
    });

    await t.test('ensureSvgXmlns: inyecta xmlns y xmlns:xlink si no existen', () => {
        const rawSvg = '<svg viewBox="0 0 10 10"><path/></svg>';
        const result = ensureSvgXmlns(rawSvg);
        assert.ok(result.includes('xmlns="http://www.w3.org/2000/svg"'), 'Debe inyectar xmlns');
        assert.ok(result.includes('xmlns:xlink="http://www.w3.org/1999/xlink"'), 'Debe inyectar xmlns:xlink');
    });

    await t.test('ensureSvgXmlns: no duplica xmlns si ya está presente', () => {
        const svgWithXmlns = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"></svg>';
        const result = ensureSvgXmlns(svgWithXmlns);
        const matches = result.match(/xmlns="http:\/\/www\.w3\.org\/2000\/svg"/g);
        assert.strictEqual(matches.length, 1, 'Debe haber exactamente un atributo xmlns');
    });

    await t.test('applySvgTheme: inyecta estilos CSS y reemplaza currentColor', () => {
        const inputSvg = '<svg><g stroke="currentColor" fill="currentColor"><path/></g></svg>';
        const themed = applySvgTheme(inputSvg, '#39C5BB');
        
        assert.ok(!themed.includes('currentColor'), 'Debe sustituir currentColor');
        assert.ok(themed.includes('#39C5BB'), 'Debe incrustar el color #39C5BB');
        assert.ok(themed.includes('fill: #39C5BB !important;'), 'Debe inyectar fill con el color');
        assert.ok(themed.includes('stroke: #39C5BB !important;'), 'Debe inyectar stroke con el color');
        assert.ok(themed.includes('<style>'), 'Debe inyectar la etiqueta style');
    });

    await t.test('generateFallbackSvg: genera SVG de error escapado y válido', () => {
        const fallback = generateFallbackSvg('Syntax error: <undefined cmd>', '#E3327B');
        assert.ok(fallback.startsWith('<svg'), 'Debe empezar con <svg');
        assert.ok(fallback.endsWith('</svg>'), 'Debe terminar con </svg>');
        assert.ok(fallback.includes('fill="#E3327B"'), 'Debe usar el color de tema proporcionado');
        assert.ok(fallback.includes('&lt;undefined cmd&gt;'), 'Debe escapar caracteres XML especiales');
    });

    await t.test('sanitizeSvgOutput: ejecuta el pipeline completo correctamente', () => {
        const raw = '<svg width="10ex" height="2ex" viewBox="0 0 100 20"><g stroke-width="2" stroke="currentColor"></g></svg>';
        const sanitized = sanitizeSvgOutput(raw, '#70D6A3');
        
        assert.ok(!sanitized.includes('width="10ex"'), 'No debe tener width fijo');
        assert.ok(!sanitized.includes('height="2ex"'), 'No debe tener height fijo');
        assert.ok(sanitized.includes('xmlns="http://www.w3.org/2000/svg"'), 'Debe tener xmlns');
        assert.ok(sanitized.includes('stroke-width="2"'), 'Debe conservar stroke-width');
        assert.ok(sanitized.includes('#70D6A3'), 'Debe contener el color de tema');
    });
});

test('Suite: mathjax_build/engine.js', async (t) => {
    await t.test('convertLatexToSvgNode y nodeToOuterHtml: renderizan expresiones matemáticas', () => {
        const node = convertLatexToSvgNode('\\frac{1}{2}');
        assert.ok(node, 'convertLatexToSvgNode debe devolver un nodo LiteDOM');
        
        const html = nodeToOuterHtml(node);
        assert.ok(typeof html === 'string', 'nodeToOuterHtml debe devolver una cadena');
        assert.ok(html.includes('<svg'), 'El HTML debe contener el elemento <svg');
        assert.ok(html.includes('</svg>'), 'El HTML debe cerrar el elemento </svg>');
    });

    await t.test('convertLatexToSvgNode: renderiza macros de plantillas como \\square y \\Box', () => {
        const node = convertLatexToSvgNode('\\frac{\\square}{\\square}');
        const html = nodeToOuterHtml(node);
        assert.ok(!html.includes('merror'), 'No debe contener error de compilación');
        assert.ok(!html.includes('Undefined control sequence'), 'No debe reportar \\square como indefinido');
        assert.ok(html.includes('25A1'), 'Debe mapear el glifo de casilla cuadrada Unicode (25A1)');
    });

    await t.test('convertLatexToSvgNode: maneja cadenas vacías aplicando texto por defecto', () => {
        const emptyNode = convertLatexToSvgNode('');
        const html = nodeToOuterHtml(emptyNode);
        assert.ok(html.includes('<svg'), 'Debe generar SVG para cadena vacía');
    });

    await t.test('getAdaptor y getMathDocument: devuelven instancias válidas', () => {
        const adaptor = getAdaptor();
        const doc = getMathDocument();
        assert.ok(adaptor, 'getAdaptor debe devolver un objeto');
        assert.ok(doc, 'getMathDocument debe devolver un objeto');
    });
});

test('Suite: mathjax_build/renderer.js', async (t) => {
    await t.test('renderMathSync: funciona con firma de 2 argumentos (latex, themeColor)', () => {
        const svg = renderMathSync('\\int x dx', '#39C5BB');
        assert.ok(typeof svg === 'string');
        assert.ok(svg.includes('<svg'), 'Debe contener <svg');
        assert.ok(svg.includes('#39C5BB'), 'Debe incluir el color #39C5BB');
    });

    await t.test('renderMathSync: funciona con firma compatible de 3 argumentos (latex, themeBg, themeText)', () => {
        const svg = renderMathSync('\\sum_{i=1}^n i', 'transparent', '#E3327B');
        assert.ok(typeof svg === 'string');
        assert.ok(svg.includes('<svg'), 'Debe contener <svg');
        assert.ok(svg.includes('#E3327B'), 'Debe aplicar themeText');
    });

    await t.test('renderMathSync: maneja expresiones complejas con matrices y física', () => {
        const latex = '\\begin{pmatrix} \\alpha & \\beta \\\\ \\gamma & \\delta \\end{pmatrix} + \\vec{\\nabla} \\cdot \\vec{B}';
        const svg = renderMathSync(latex, '#56D8CD');
        assert.ok(svg.includes('<svg'));
        assert.ok(svg.includes('#56D8CD'));
    });
});

test('Suite: mathjax_build/index.js', async (t) => {
    await t.test('index.js exporta todas las utilidades requeridas y registra el global', () => {
        assert.ok(typeof indexModule.renderMathSync === 'function', 'Debe exportar renderMathSync');
        assert.ok(Array.isArray(indexModule.ACTIVE_PACKAGES), 'Debe exportar ACTIVE_PACKAGES');
        assert.ok(typeof indexModule.sanitizeSvgOutput === 'function', 'Debe exportar sanitizeSvgOutput');
        assert.ok(typeof global.renderMathSync === 'function', 'Debe registrar global.renderMathSync');
    });
});
