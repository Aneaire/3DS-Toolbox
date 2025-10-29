@echo off
title 3DS/CIA Decryptor GUI
echo Starting 3DS/CIA Decryptor GUI...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo.
    pause
    exit /b 1
)

REM Check if tkinter is available
python -c "import tkinter" >nul 2>&1
if errorlevel 1 (
    echo tkinter is not available
    echo Please reinstall Python with tkinter support
    echo.
    pause
    exit /b 1
)

REM Launch the GUI
python decrypt_gui_windows.py

if errorlevel 1 (
    echo.
    echo GUI encountered an error. Check the error message above.
    pause
)