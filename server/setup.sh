#!/bin/bash

# Exit on any error
set -e

# Define the Python version
PYTHON_VERSION="3.10"
VENV_DIR=".venv310"

echo "📦 Creating virtual environment with Python $PYTHON_VERSION..."

# Check for python3.10
if ! command -v python$PYTHON_VERSION &>/dev/null; then
    echo "❌ Python $PYTHON_VERSION is not installed. Please install it using:"
    echo "    sudo apt install python3.10 python3.10-venv python3.10-dev"
    exit 1
fi

# Create the virtual environment
python$PYTHON_VERSION -m venv "$VENV_DIR"

echo "✅ Virtual environment created at $VENV_DIR"

# Activate the environment
source "$VENV_DIR/bin/activate"

echo "🔄 Upgrading pip..."
pip install --upgrade pip

echo "📥 Installing dependencies..."

# Install packages with compatible versions
pip install flask r6statsapi==0.1.9 aiohttp==3.6.2

echo "📄 Freezing requirements to requirements.txt..."
pip freeze > requirements.txt

echo "✅ Environment setup complete."
