/**
 * ---
 * file: mathjax_build/build.js
 * module: mathjax_build.build
 * description: Script de compilación y empaquetado de MathJax mediante esbuild.
 * type: build/bundler
 * version: 1.0.0
 * date: 2026-08-24
 * dependencies: []
 * relations:
 *   - src/assets/mathjax_bundle.js
 * exports:
 *   - buildBundle: "Ejecuta la compilación de mathjax_bundle.js con banner de metadatos YAML"
 * test: node mathjax_build/build.js
 * constraints:
 *   - "Empaquetar sin dependencias externas de NodeJS para compatibilidad con V8 MiniRacer"
 * keywords:
 *   - esbuild
 *   - mathjax-bundler
 *   - build-script
 * ---
 */

'use strict';

const path = require('path');
const esbuild = require('esbuild');

const BANNER_METADATA = `/**
 * ---
 * file: src/assets/mathjax_bundle.js
 * module: src.assets.mathjax_bundle
 * description: Bundle autónomo de MathJax v3 para renderizado SVG síncrono en V8 / MiniRacer.
 * type: core/bundle
 * version: 1.0.0
 * date: 2026-08-24
 * dependencies: []
 * relations:
 *   - mathjax_build/build.js
 *   - src/ui/components/svg_cache.py
 * exports:
 *   - renderMathSync: "Renderiza síncronamente una fórmula LaTeX a código SVG sanitizado"
 * test: node --test tests/test_mathjax_bundle.js
 * constraints:
 *   - "Compilado sin dependencias del navegador para ejecución pura en motor V8"
 * keywords:
 *   - mathjax-bundle
 *   - svg-render
 *   - miniracer
 *   - v8-engine
 * ---
 *
 * MathJax SVG Rendering Engine Bundle for Traductor Mates.
 * Compiled with esbuild targeting V8 / MiniRacer execution environment.
 * Configured with fontCache: 'none' and modular TeX extensions for mathematics and theoretical physics.
 */
`;

/**
 * Compila los módulos de mathjax_build hacia el archivo único src/assets/mathjax_bundle.js.
 *
 * @returns {Promise<void>} Promesa que se resuelve al completar la compilación.
 */
async function buildBundle() {
    const entryFile = path.resolve(__dirname, 'index.js');
    const outputFile = path.resolve(__dirname, '..', 'src', 'assets', 'mathjax_bundle.js');

    console.log(`[Build] Compilando ${entryFile} -> ${outputFile}...`);

    try {
        const result = await esbuild.build({
            entryPoints: [entryFile],
            outfile: outputFile,
            bundle: true,
            platform: 'neutral',
            format: 'iife',
            target: ['es2020'],
            minify: false,
            banner: {
                js: BANNER_METADATA
            },
            sourcemap: false
        });

        console.log('[Build] Compilación completada con éxito.');
    } catch (err) {
        console.error('[Build] Error durante la compilación:', err);
        process.exit(1);
    }
}

if (require.main === module) {
    buildBundle();
}

module.exports = {
    buildBundle,
    BANNER_METADATA
};
