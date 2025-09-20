

PORT=${PORT:-5000}

./kill.sh # kill previous running process

echo "Starting backend..."
source ./.venv/bin/activate
exec gunicorn -w 4 -b 0.0.0.0:$PORT entry:app
