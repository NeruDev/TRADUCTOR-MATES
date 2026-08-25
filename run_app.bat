@echo off
REM ---
REM file: run_app.bat
REM module: run_app
REM description: Lanzador ejecutable en Windows para iniciar la aplicación Traductor Mates.
REM type: script/launcher
REM version: 1.0.0
REM date: 2026-08-24
REM dependencies: []
REM relations:
REM   - main.py
REM   - setup_venv.bat
REM exports: []
REM test: .\run_app.bat
REM constraints:
REM   - "Verificar existencia previa del entorno virtual .venv antes de invocar python.exe"
REM keywords:
REM   - run-app
REM   - launcher
REM   - windows-batch
REM ---

IF NOT EXIST .venv (
    echo El entorno .venv no existe. Ejecutando setup_venv.bat...
    call setup_venv.bat
)
echo Iniciando Traductor Mates...
.\.venv\Scripts\python.exe main.py

