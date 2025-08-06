from flask import Flask
from enum import Enum
from flask_cors import CORS

def initApp() -> Flask:
  app : Flask = Flask(__name__)
  return app

class ApiGetEndpoints(Enum):
  TOP_PC_PLAYERS = "/top_pc_players"
  TOP_CONSOLE_PLAYERS = "/top_console_players"
  MATCHING_PLAYER = "/matching_player"

def setupRoutes(app : Flask) -> None:
  
  @app.route('/')
  def home():
    print("Fetching home info")
    return "Hello, Flask!"
  
  @app.route(ApiGetEndpoints.TOP_PC_PLAYERS.value)
  def player():
    print("Fetching top 10 pc players")
    return "Hello, Flask!"

  