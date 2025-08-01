from flask import Flask, jsonify
import r6statsapi

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the R6 Stats API!"

@app.route('/player/<platform>/<region>/<player_name>')
def get_player_stats(platform, region, player_name):
  try:
    player = r6statsapi.Player(platform, player_name, region)
    stats = player.stats
    return jsonify(stats)
  except Exception as e:
    return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run()
