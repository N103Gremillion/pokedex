#!/bin/bash


sudo apt update
sudo apt install -y python3.12-dev build-essential

# Remove old venv if it exists
if [ -d ".venv" ]; then
  echo "Removing old virtual environment..."
  rm -rf .venv
fi

# Create new venv using the default python3
echo "Creating new virtual environment with the default python3..."
python3 -m venv .venv

# Activate the venv
source .venv/bin/activate

# Upgrade pip to latest version
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
if [ -f "requirements.txt" ]; then
  echo "Installing packages from requirements.txt..."
  pip install -r requirements.txt
else
  echo "No requirements.txt file found."
fi

echo "Environment setup complete!"
