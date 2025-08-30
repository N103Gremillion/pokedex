import os
from flask import Flask, Response, jsonify
from enum import Enum
from app_types import GymLeaderData, ItemData, PokemonData, PokedexKeys, PokemonRegionGymLeaders
from pokeapi.item import fetchItemById, fetchItemByName
from pokeapi.pokedex import fetchPokedexByGeneration
from pokeapi.pokemon import fetchPokemonDataByIdentifier
from scraper.gymLeaderPageScrapper import fetchRandomGymLeader
from scraper.gymLeadersPageScrapper import fetchGymLeadersByGeneration

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
  
  # POKEMON ENDPOINTS ################################################################
  # TO DO add tying to name fetches and implement the rest of the typing
  @app.route("/pokemon/<identifier>")
  def getPokemonByIdentifier(identifier : str) -> Response:   
    if identifier.isdigit():
      # ID fetch
      pokemon_id : int = int(identifier)
      result : PokemonData = fetchPokemonDataByIdentifier(pokemon_id)
    else:
      # Name fetch
      result = fetchPokemonDataByIdentifier(identifier.lower()) # api expects a lower case name
    
    return jsonify(result)
  
  # ITEM ENDPOINTS ###################################################################
  # TO DO add tying to name fetches and implement the rest of the typing
  @app.route("/item/<identifier>")
  def getItemByIdentifier(identifier : str) -> Response:
    if identifier.isdigit():
      # ID fetch
      item_id : int = int(identifier)
      result : ItemData = fetchItemById(item_id)
    else:
      # Name fetch
      result = fetchItemByName(identifier.lower())
    
    return jsonify(result)
  
  # POKEDEX ENDPOINTS ###########################################################
  @app.route("/pokedex/<generation>")
  def getPokemonInPokedexByGeneration(generation : str) -> Response:
    gen_num : int
    
    try:
      gen_num = int(generation)
    except ValueError:
      gen_num = -1
  
    if (gen_num == -1):
      print(f"Invalid query param for generations. {generation}")
      return {PokedexKeys.GEN_NUMBER : -1, PokedexKeys.POKEMON : []}

    result = fetchPokedexByGeneration(gen_num)
    
    return jsonify(result)
  
  # scrapper endpoints (mostly gym stuff)
  # GYMLEADERS ENDPOINTS 
  @app.route("/gym-leader/random")
  def getRandomGymLeader() -> GymLeaderData:
    result : GymLeaderData = fetchRandomGymLeader()
    return jsonify(result)

  @app.route("/gym-leaders/<generation>")
  def getGymLeadersFromGeneration(generation : str) -> PokemonRegionGymLeaders:
    res : list[GymLeaderData] = fetchGymLeadersByGeneration(generation)
    return jsonify(res)