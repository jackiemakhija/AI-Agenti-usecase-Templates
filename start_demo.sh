#!/bin/bash

echo "========================================"
echo "Data Steward Council - Demo Launcher"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.10+ from https://www.python.org/downloads/"
    exit 1
fi

# Check if Node is installed
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed"
    echo "Please install Node.js 18+ from https://nodejs.org/"
    exit 1
fi

echo "[1/5] Checking backend setup..."
cd backend

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Check if dependencies are installed
if ! pip show pyautogen &> /dev/null; then
    echo "Installing Python dependencies..."
    pip install -r requirements.txt
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo ""
    echo "WARNING: .env file not found!"
    echo "Please create backend/.env with your OpenAI API key"
    echo ""
    echo "Example:"
    echo "OPENAI_API_KEY=sk-your-key-here"
    echo "OPENAI_MODEL=gpt-4o-mini"
    echo ""
    exit 1
fi

echo "[2/5] Initializing database..."
if [ ! -f "data_steward.db" ]; then
    python scripts/init_database.py
fi

echo "[3/5] Generating synthetic data..."
if [ ! -f "data/customer_data.csv" ]; then
    python scripts/generate_synthetic_data.py
fi

echo "[4/5] Starting backend server..."
# Start backend in background
python main.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 5

cd ../frontend

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

echo "[5/5] Starting frontend dashboard..."
# Start frontend in background
npm run dev &
FRONTEND_PID=$!

echo ""
echo "========================================"
echo "Demo is running!"
echo "========================================"
echo ""
echo "Backend:  http://localhost:8000"
echo "Frontend: http://localhost:5173"
echo ""
echo "Backend PID:  $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
echo ""
echo "Open your browser to: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop all services..."
echo ""

# Wait for Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait

