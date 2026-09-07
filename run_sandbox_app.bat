@echo off
REM ---
REM file: run_sandbox_app.bat
REM module: run_sandbox_app
REM description: Lanzador en Windows para el prototipo sandbox de GUI en TypeScript con backend en Python vía API REST.
REM type: script/launcher
REM version: 1.0.0
REM date: 2026-08-29
REM dependencies: []
REM relations:
REM   - sandbox/ts_prototype/api_server.py
REM   - sandbox/ts_prototype/README.md
REM exports: []
REM test: .\run_sandbox_app.bat
REM constraints:
REM   - "AVISO: Todas las rutas, módulos y configuraciones dentro de sandbox/ son PROVISIONALES para iteración y pruebas"
REM   - "Verificar existencia previa del entorno virtual .venv antes de invocar python.exe"
REM keywords:
REM   - sandbox-launcher
REM   - typescript-gui
REM   - python-api
REM   - prototype-launcher
REM ---

REM ==============================================================================
REM AVISO IMPORTANTE:
REM Las rutas, scripts y dependencias dentro del directorio "sandbox/" son
REM PROVISIONALES y experimentales. Están diseñadas para iterar la nueva interfaz
REM gráfica en TypeScript con backend Python API sin alterar el código estable
REM de producción en "src/".
REM ==============================================================================

IF NOT EXIST .venv (
    echo El entorno .venv no existe. Ejecutando setup_venv.bat...
    call setup_venv.bat
)

echo ============================================================
echo  Iniciando Prototipo Sandbox (UI TypeScript + Python API)
echo  Direccion local: http://127.0.0.1:8080
echo  (Rutas sandbox provisionales para desarrollo e iteracion)
echo ============================================================

REM Verificar si el frontend esta compilado en sandbox\ts_prototype\frontend\dist
IF NOT EXIST "sandbox\ts_prototype\frontend\dist\index.html" (
    echo Compilando frontend TypeScript por primera vez...
    cd sandbox\ts_prototype\frontend
    call npm install
    call npm run build
    cd ..\..\..
)

REM Iniciar el servidor API en Python que aloja la interfaz y el motor AST
.\.venv\Scripts\python.exe sandbox\ts_prototype\api_server.py
