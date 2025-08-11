import os
from flask import Flask, Response, jsonify, request
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
  
  # TO DO add tying to name fetches and implement the rest of the typing
  @app.route("/pokemon/<identifier>")
  def getPokemon(identifier : str) -> Response:   
    if identifier.isdigit():
      # ID fetch
      pokemon_id : int = int(identifier)
      result : PokemonData = fetchPokemonById(pokemon_id)
    else:
      # Name fetch
      result = fetchPokemonByName(identifier.lower())
    
    return jsonify(result)
  
  @app.route("/item")
  def getItem() -> Response:
    result = fetchData(PokemonInfoEndpoints.GET_ITEM)
    
    print(result)
    
    # TO DO implement the item fetch
    return jsonify({"id": 1, "name": "Potion", "description": "Restores 20 HP"})
