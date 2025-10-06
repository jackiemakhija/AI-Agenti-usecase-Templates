@echo off
echo ========================================
echo Data Steward Council - Demo Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if Node is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js 18+ from https://nodejs.org/
    pause
    exit /b 1
)

echo [1/5] Checking backend setup...
cd backend

REM Check if venv exists
if not exist "venv\" (
    echo Creating Python virtual environment...
    python -m venv venv
)

REM Activate venv
call venv\Scripts\activate

REM Check if dependencies are installed
pip show pyautogen >nul 2>&1
if errorlevel 1 (
    echo Installing Python dependencies...
    pip install -r requirements.txt
)

REM Check if .env exists
if not exist ".env" (
    echo.
    echo WARNING: .env file not found!
    echo Please create backend\.env with your OpenAI API key
    echo.
    echo Example:
    echo OPENAI_API_KEY=sk-your-key-here
    echo OPENAI_MODEL=gpt-4o-mini
    echo.
    pause
    exit /b 1
)

echo [2/5] Initializing database...
if not exist "data_steward.db" (
    python scripts\init_database.py
)

echo [3/5] Generating synthetic data...
if not exist "data\customer_data.csv" (
    python scripts\generate_synthetic_data.py
)

echo [4/5] Starting backend server...
start "Data Steward Council - Backend" cmd /k "cd /d %CD% && venv\Scripts\activate && python main.py"

REM Wait for backend to start
timeout /t 5 /nobreak >nul

cd ..\frontend

REM Check if node_modules exists
if not exist "node_modules\" (
    echo Installing frontend dependencies...
    call npm install
)

echo [5/5] Starting frontend dashboard...
start "Data Steward Council - Frontend" cmd /k "cd /d %CD% && npm run dev"

echo.
echo ========================================
echo Demo is starting!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:5173
echo.
echo Two terminal windows will open:
echo 1. Backend server (FastAPI)
echo 2. Frontend dashboard (Vite)
echo.
echo Wait a few seconds, then open your browser to:
echo http://localhost:5173
echo.
echo Press any key to exit this launcher...
pause >nul

