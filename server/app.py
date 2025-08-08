import os
from flask import Flask
from enum import Enum
from flask_cors import CORS
from dotenv import load_dotenv
from pokeapi.pokemon import *

def initApp() -> Flask:
  app : Flask = Flask(__name__)
  return app

class ApiGetEndpoints(Enum):
  POKEMON = "/pokemon"

def setupRoutes(app : Flask) -> None:
  
  @app.route('/')
  def home():
    print("Fetching home info")
    return "Hello, Flask!"
  
  @app.route(f"{ApiGetEndpoints.POKEMON.value}/<string:name>")
  def get_pokemon(name):
      print(f"Fetching pokemon: {name}")
      response = fetchPokemon(name)
      return response

  