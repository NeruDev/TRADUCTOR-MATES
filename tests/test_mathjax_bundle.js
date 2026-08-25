/**
 * ---
 * file: tests/test_mathjax_bundle.js
 * module: tests.test_mathjax_bundle
 * description: Pruebas unitarias para validar la ejecución del bundle autónomo src/assets/mathjax_bundle.js en VM V8.
 * type: test/unit
 * version: 1.0.0
 * date: 2026-08-24
 * dependencies: []
 * relations:
 *   - src/assets/mathjax_bundle.js
 *   - mathjax_build/build.js
 * exports: []
 * test: node --test tests/test_mathjax_bundle.js
 * constraints:
 *   - "Validar renderizado síncrono de múltiples ramas matemáticas y físicas en contexto aislado"
 * keywords:
 *   - test-mathjax-bundle
 *   - v8-mock
 *   - miniracer-compatibility
 *   - node-test
 * ---
 */

'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const BUNDLE_PATH = path.resolve(__dirname, '..', 'src', 'assets', 'mathjax_bundle.js');

/**
 * Crea un contexto de máquina virtual (VM) aislado con los mismos shims
 * inyectados por MiniRacer en `SVGMathCache._ensure_v8_initialized()`.
 *
 * @returns {object} Contexto VM inicializado con el bundle de MathJax evaluado.
 */
function createV8MockContext() {
    const sandbox = {};
    const context = vm.createContext(sandbox);

    const shims = `
    var window = this;
    var global = this;
    var document = { 
        createElement: function() { return {}; },
        getElementsByTagName: function() { return []; },
        documentElement: { style: {} }
    };
    var __dirname = '';
    var process = { env: {}, cwd: function() { return ''; } };
    var module = { exports: {} };
    var exports = module.exports;
    var _path = { resolve: function() { return ''; }, join: function() { return ''; }, dirname: function() { return ''; } };
    var _fs = { readFileSync: function() { return ''; }, existsSync: function() { return false; } };
    function require(m) {
        if (m === 'path') return _path;
        if (m === 'fs') return _fs;
        return {};
    }
    `;

    const bundleCode = fs.readFileSync(BUNDLE_PATH, 'utf-8');

    vm.runInContext(shims, context);
    vm.runInContext(bundleCode, context);

    return context;
}

test('Suite: src/assets/mathjax_bundle.js - Integridad y Metadatos', async (t) => {
    await t.test('El archivo bundle existe y contiene la cabecera de metadatos YAML', () => {
        assert.ok(fs.existsSync(BUNDLE_PATH), 'El archivo mathjax_bundle.js debe existir');
        
        const content = fs.readFileSync(BUNDLE_PATH, 'utf-8');
        assert.ok(content.length > 500000, 'El bundle debe tener contenido sustancial (>500KB)');
        assert.ok(content.includes('file: src/assets/mathjax_bundle.js'), 'Debe identificar el archivo');
        assert.ok(content.includes('renderMathSync'), 'Debe documentar la función renderMathSync');
    });

    await t.test('El bundle se evalúa correctamente en un contexto VM idéntico a MiniRacer', () => {
        const ctx = createV8MockContext();
        assert.ok(typeof ctx.renderMathSync === 'function', 'renderMathSync debe ser una función global en el contexto');
    });
});

test('Suite: src/assets/mathjax_bundle.js - Renderizado de Categorías Matemáticas y Físicas', async (t) => {
    const ctx = createV8MockContext();

    const testFormulas = [
        {
            category: 'Álgebra (Fórmula Cuadrática)',
            latex: 'x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}',
            color: '#39C5BB'
        },
        {
            category: 'Cálculo (Integral Gaussiana)',
            latex: '\\int_{-\\infty}^{\\infty} e^{-x^2} \\, dx = \\sqrt{\\pi}',
            color: '#E3327B'
        },
        {
            category: 'Ecuaciones Diferenciales (Onda)',
            latex: '\\frac{\\partial^2 u}{\\partial t^2} = v^2 \\nabla^2 u',
            color: '#70D6A3'
        },
        {
            category: 'Álgebra Lineal (Matrices)',
            latex: '\\begin{pmatrix} a_{11} & a_{12} \\\\ a_{21} & a_{22} \\end{pmatrix}',
            color: '#56D8CD'
        },
        {
            category: 'Sistemas por Casos',
            latex: 'f(x) = \\begin{cases} x^2 & \\text{si } x > 0 \\\\ 0 & \\text{si } x \\le 0 \\end{cases}',
            color: '#C084FC'
        },
        {
            category: 'Sumatorias y Límites',
            latex: '\\lim_{x \\to 0} \\frac{\\sin x}{x} = 1, \\quad \\sum_{k=1}^n k = \\frac{n(n+1)}{2}',
            color: '#39C5BB'
        },
        {
            category: 'Electromagnetismo (Maxwell-Ampère)',
            latex: '\\oint \\vec{B} \\cdot d\\vec{l} = \\mu_0 I_{\\text{enc}} + \\mu_0 \\varepsilon_0 \\frac{d\\Phi_E}{dt}',
            color: '#FF7597'
        },
        {
            category: 'Mecánica Cuántica (Schrödinger)',
            latex: 'i \\hbar \\frac{\\partial}{\\partial t} \\ket{\\Psi(t)} = \\hat{H} \\ket{\\Psi(t)}',
            color: '#39C5BB'
        },
        {
            category: 'Constantes y Unidades Físicas',
            latex: 'c = 299\\,792\\,458\\ \\mathrm{m/s}, \\quad G = 6.67430 \\times 10^{-11}\\ \\mathrm{m^3\\ kg^{-1}\\ s^{-2}}',
            color: '#00838F'
        },
        {
            category: 'Plantillas y Casillas Estructuradas (\\square)',
            latex: '\\frac{\\square}{\\square} + \\sqrt[\\square]{\\square} + \\int_{\\square}^{\\square} {\\square} \\, d{\\square}',
            color: '#39C5BB'
        }
    ];

    for (const item of testFormulas) {
        await t.test(`Renderizado correcto de ${item.category}`, () => {
            const svgOutput = ctx.renderMathSync(item.latex, item.color);
            
            assert.ok(typeof svgOutput === 'string', 'El resultado debe ser una cadena');
            assert.ok(svgOutput.includes('<svg'), 'Debe contener la etiqueta de apertura <svg');
            assert.ok(svgOutput.includes('</svg>'), 'Debe contener la etiqueta de cierre </svg>');
            assert.ok(svgOutput.includes('viewBox='), 'Debe contener el atributo viewBox');
            assert.ok(svgOutput.includes(item.color), `Debe contener el color de tema inyectado ${item.color}`);
            assert.ok(!svgOutput.includes('stroke- '), 'No debe contener atributos XML truncados (stroke- )');
            assert.ok(!svgOutput.match(/<svg\b[^>]*\bwidth="[^"]*"/), 'La etiqueta raíz <svg> no debe tener atributo width fijo');
            assert.ok(!svgOutput.match(/<svg\b[^>]*\bheight="[^"]*"/), 'La etiqueta raíz <svg> no debe tener atributo height fijo');
        });
    }
});

test('Suite: src/assets/mathjax_bundle.js - Compatibilidad de Firmas y Temas Hatsune Miku', async (t) => {
    const ctx = createV8MockContext();

    await t.test('Firma compatible de 3 argumentos (latex, themeBg, themeText)', () => {
        const svg = ctx.renderMathSync('\\alpha + \\beta = \\gamma', 'transparent', '#E3327B');
        assert.ok(svg.includes('<svg'));
        assert.ok(svg.includes('#E3327B'));
    });

    await t.test('Firma moderna de 2 argumentos (latex, themeColor)', () => {
        const svg = ctx.renderMathSync('\\alpha + \\beta = \\gamma', '#39C5BB');
        assert.ok(svg.includes('<svg'));
        assert.ok(svg.includes('#39C5BB'));
    });

    await t.test('Manejo seguro de error sin interrupción del motor', () => {
        const svg = ctx.renderMathSync('\\invalidsyntax{{{{{', '#39C5BB');
        assert.ok(typeof svg === 'string');
        assert.ok(svg.includes('<svg'));
    });
});
