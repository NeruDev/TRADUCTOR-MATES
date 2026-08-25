/**
 * ---
 * file: mathjax_build/package_config.js
 * module: mathjax_build.package_config
 * description: Configuración modular de paquetes TeX de MathJax excluyendo módulos legados.
 * type: build/config
 * version: 1.0.0
 * date: 2026-08-24
 * dependencies: []
 * relations:
 *   - mathjax_build/engine.js
 *   - mathjax_build/build.js
 * exports:
 *   - ACTIVE_PACKAGES: "Lista optimizada de paquetes TeX requeridos por el compilador matemático"
 * test: node --test tests/test_mathjax_build.js
 * constraints:
 *   - "Excluir paquetes obsoletos o pesados como mhchem y bussproofs para optimizar peso del bundle"
 * keywords:
 *   - mathjax-packages
 *   - tex-extensions
 *   - modular-config
 * ---
 */

'use strict';

/**
 * Lista de paquetes TeX activos para el motor MathJax.
 *
 * Incluye extensiones esenciales para matemáticas avanzadas, cálculo,
 * física teórica y álgebra lineal, descartando paquetes legados o
 * innecesarios (como 'mhchem' de química o 'bussproofs' de árboles lógicos)
 * para optimizar la velocidad de carga y reducir el tamaño del bundle.
 *
 * @type {string[]}
 */
const ACTIVE_PACKAGES = [
    'base',
    'ams',
    'boldsymbol',
    'braket',
    'cancel',
    'cases',
    'centernot',
    'color',
    'configmacros',
    'empheq',
    'enclose',
    'extpfeil',
    'gensymb',
    'mathtools',
    'newcommand',
    'noerrors',
    'noundefined',
    'physics',
    'tagformat',
    'textcomp',
    'textmacros',
    'unicode',
    'upgreek'
];

module.exports = {
    ACTIVE_PACKAGES
};
