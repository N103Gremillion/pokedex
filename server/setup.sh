#!/bin/bash
set -e  # return on error

if [ ! -d ".venv" ]; then # if a .venv doesnt exits create one
  python3 -m venv .venv
fi

source .venv/bin/activate # activate virtual environment

echo "Setup complete!"
