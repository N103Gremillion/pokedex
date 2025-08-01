#!/bin/bash

PORT=5000

# Kill any process using the port
PID=$(lsof -ti tcp:$PORT)
if [ -n "$PID" ]; then
  echo "Killing process $PID on port $PORT"
  kill -9 $PID
fi
