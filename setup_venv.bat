@echo off
REM ---
REM file: setup_venv.bat
REM module: setup_venv
REM description: Script para creación de entorno virtual .venv e instalación de dependencias en Windows.
REM type: script/setup
REM version: 1.0.0
REM date: 2026-08-24
REM dependencies: []
REM relations:
REM   - pyproject.toml
REM   - run_app.bat
REM exports: []
REM test: .\setup_venv.bat
REM constraints:
REM   - "Instalar dependencias en modo editable PEP 621"
REM keywords:
REM   - setup-venv
REM   - virtualenv
REM   - pip-install
REM ---

echo ========================================================
echo   Configurando entorno virtual .venv para Traductor Mates
echo ========================================================

IF NOT EXIST .venv (
    echo Creando entorno virtual .venv...
    python -m venv .venv
) ELSE (
    echo El entorno virtual .venv ya existe.
)

echo Instalando dependencias en .venv...
call .\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -e .

echo.
echo ========================================================
echo   ¡Entorno virtual preparado exitosamente!
echo   Para ejecutar la app usa: run_app.bat
echo ========================================================
pause
