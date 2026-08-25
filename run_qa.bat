@echo off
REM ---
REM file: run_qa.bat
REM module: run_qa
REM description: Pipeline de calidad automatizado (Ruff, Pydoclint, Mypy, Pytest, Node.js).
REM type: script/qa-pipeline
REM version: 1.0.0
REM date: 2026-08-24
REM dependencies: []
REM relations:
REM   - AGENTS.md
REM   - pyproject.toml
REM exports: []
REM test: .\run_qa.bat
REM constraints:
REM   - "Ejecutar secuencialmente las 5 compuertas de calidad sin omitir ninguna fase"
REM keywords:
REM   - qa-pipeline
REM   - quality-gates
REM   - ruff
REM   - mypy
REM   - pytest
REM ---
echo ==============================================
echo  Iniciando Evaluacion de Calidad (QA Pipeline)
echo ==============================================
echo.

echo [1/5] Ejecutando Ruff (Linter y Formato)...
python -m ruff check src/ tests/ main.py
if %ERRORLEVEL% neq 0 ( echo [!] Ruff detecto problemas. ) else ( echo [OK] Ruff superado. )
echo.

echo [2/5] Ejecutando Pydoclint (Google Style Docstrings)...
pydoclint src/ main.py
if %ERRORLEVEL% neq 0 ( echo [!] Pydoclint detecto problemas. ) else ( echo [OK] Pydoclint superado. )
echo.

echo [3/5] Ejecutando Mypy (Tipado Estatico)...
python -m mypy src/ main.py
if %ERRORLEVEL% neq 0 ( echo [!] Mypy detecto problemas. ) else ( echo [OK] Mypy superado. )
echo.

echo [4/5] Ejecutando Pytest (Pruebas Unitarias Python)...
python -m pytest tests/
if %ERRORLEVEL% neq 0 ( echo [!] Pytest detecto problemas. ) else ( echo [OK] Pytest superado. )
echo.

echo [5/5] Ejecutando Node.js (Pruebas Unitarias JavaScript)...
node --test tests/test_mathjax_build.js tests/test_mathjax_bundle.js
if %ERRORLEVEL% neq 0 ( echo [!] Node.js detecto problemas en pruebas JS. ) else ( echo [OK] Pruebas JavaScript superadas. )
echo.

echo ==============================================
echo  Evaluacion Finalizada
echo ==============================================
