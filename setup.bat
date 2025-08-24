@echo off
REM FileBridge Project Setup Script
REM This script initializes the Python virtual environment and installs dependencies

SET VENV_DIR=venv
SET REQUIREMENTS=requirements.txt

ECHO =============================
ECHO FileBridge Project Setup
ECHO =============================

REM Check if venv directory exists
IF EXIST %VENV_DIR% (
    ECHO [Step 1] Virtual environment already exists.
    ECHO [Step 2] Activating virtual environment...
    CALL %VENV_DIR%\Scripts\activate.bat
    ECHO [Step 3] Virtual environment activated.
) ELSE (
    ECHO [Step 1] Creating virtual environment...
    python -m venv %VENV_DIR%
    IF ERRORLEVEL 1 (
        ECHO [ERROR] Failed to create virtual environment.
        EXIT /B 1
    )
    ECHO [Step 2] Activating virtual environment...
    CALL %VENV_DIR%\Scripts\activate.bat
    IF ERRORLEVEL 1 (
        ECHO [ERROR] Failed to activate virtual environment.
        EXIT /B 1
    )
    ECHO [Step 3] Installing dependencies from %REQUIREMENTS%...
    pip install --upgrade pip
    pip install -r %REQUIREMENTS%
    IF ERRORLEVEL 1 (
        ECHO [ERROR] Failed to install dependencies.
        EXIT /B 1
    )
    ECHO [Step 4] Setup complete. Virtual environment is ready.
)

ECHO =============================
ECHO Setup finished.
ECHO =============================
