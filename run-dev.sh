#!/bin/bash

# kill previous process running on port 5000
./server/kill.sh

# Activate Python backend venv and run backend in background
echo "Starting backend..."
source ./server/.venv/bin/activate
python3 ./server/entry.py &

BACKEND_PID=$! # get pid of backend process

# Run frontend dev server
echo "Starting frontend..."
cd ./client
npm start &

FRONTEND_PID=$! # get pid of frontend instance

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID
