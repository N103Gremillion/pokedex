./kill.sh # kill previous running process

pwd

echo "Starting backend..."
source ./.venv/bin/activate
python ./entry.py 
