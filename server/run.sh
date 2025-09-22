#!/bin/bash
PORT=${PORT:-5000}

# Kill previous running process
./kill.sh

echo "Starting backend..."

# Activate virtualenv
source ./.venv/bin/activate

# Start gunicorn without exec
gunicorn -w 4 -b 0.0.0.0:$PORT entry:app --timeout 60
