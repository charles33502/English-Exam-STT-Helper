@echo off
cd /d "%~dp0"

echo Current folder:
cd
echo.

where py >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Python launcher "py" not found.
    echo Please install Python from https://www.python.org/downloads/
    echo During install, check "Add python.exe to PATH".
    pause
    exit /b 1
)

echo Python version:
py --version
echo.

if not exist ".venv\Scripts\python.exe" (
    echo Creating .venv ...
    py -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Failed to create .venv.
        pause
        exit /b 1
    )
)

echo Activating .venv ...
call ".venv\Scripts\activate.bat"
if errorlevel 1 (
    echo [ERROR] Failed to activate .venv.
    pause
    exit /b 1
)

echo Upgrading pip ...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo [ERROR] Failed to upgrade pip.
    pause
    exit /b 1
)

echo Installing faster-whisper ...
python -m pip install faster-whisper
if errorlevel 1 (
    echo [ERROR] Failed to install faster-whisper.
    pause
    exit /b 1
)

echo.
echo Install complete.
pause
