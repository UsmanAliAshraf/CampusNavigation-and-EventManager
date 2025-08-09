@echo off
echo 🏫 Campus Connect - Streamlit GUI
echo ==================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo ✅ Python is installed
echo.

REM Change to the GUI directory
cd /d "%~dp0"

REM Check if requirements.txt exists and install dependencies
if exist requirements.txt (
    echo 📦 Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
    echo ✅ Dependencies installed
    echo.
)

REM Launch Streamlit
echo 🚀 Launching Campus Connect GUI...
echo 📱 The application will open in your default web browser
echo 🌐 URL: http://localhost:8501
echo ==================================================
echo.

streamlit run streamlit_app.py --server.port 8501

echo.
echo 👋 Campus Connect GUI closed
pause
