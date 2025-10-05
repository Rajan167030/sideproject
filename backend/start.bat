@echo off
REM Simple batch script to start the Flask backend
cd /d "%~dp0"
echo Starting Flask backend server...
echo.
venv\Scripts\python.exe app.py
