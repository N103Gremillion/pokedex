import os
from typing import List
from flask import Flask, Response, jsonify
from enum import Enum
from pokeapi.move import fetchPokemonMove, fetchPokemonMoves
from pokeapi.type import fetchDetailedPokemonType
from utils import filterBySubstringAcrossPools, isValidType
from app_types import DetailedPokemonType, DetailedPokemonTypeKeys, GymLeaderData, ItemData, MoveData, PokemonData, PokedexKeys, PokemonRegionGymLeaders, PokemonType
from pokeapi.item import fetchDetailedItemByIdentifier, fetchItemByIdentifier
from pokeapi.pokedex import fetchPokedexByGeneration
from pokeapi.pokemon import fetchAllPokemonOfType, fetchDetailedPokemonDataByIdentifier, fetchPokemonDataByIdentifier
from scraper.gymLeaderPageScrapper import fetchDetailedGymLeader, fetchRandomGymLeader
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
  
  # POKEMON ENDPOINTS ###############################################################
  @app.route("/pokemon/<identifier>")
  def getPokemonByIdentifier(identifier : str) -> Response:   
    if identifier.isdigit():
      # ID fetch
      pokemon_id : int = int(identifier)
      result : PokemonData = fetchPokemonDataByIdentifier(pokemon_id)
    else:
      # Name fetch
      result = fetchPokemonDataByIdentifier(identifier.lower()) # api expects a lower case name
    
    print(result)
    
    return jsonify(result)
  
  @app.route("/pokemon/type/<type_name>")
  def getAllPokemonOfType(type_name : PokemonType) -> Response:
    
    if (not isValidType(type_name)):
      return { PokedexKeys.POKEMON : []}
    
    pokemon : List[PokemonData] = fetchAllPokemonOfType(type_name)
    
    return jsonify({ PokedexKeys.POKEMON : pokemon })
  
  @app.route("/pokemon/detailed/<pokemon_name>")
  def getDetailedPokemon(pokemon_name : str):
    result = fetchDetailedPokemonDataByIdentifier(pokemon_name)
    return jsonify(result)
    
  # ITEM ENDPOINTS ###################################################################
  @app.route("/item/<identifier>")
  def getItemByIdentifier(identifier : str) -> Response:
    if identifier.isdigit():
      # ID fetch
      item_id : int = int(identifier)
      result : ItemData = fetchItemByIdentifier(item_id)
    else:
      # Name fetch
      result = fetchItemByIdentifier(identifier.lower())
    
    return jsonify(result)
  
  @app.route("/item/detailed/<item_name>")
  def getDetailedItem(item_name : str):
    result = fetchDetailedItemByIdentifier(item_name)
    print(f"Detailed item {item_name}")
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
  
  # TYPE ENDPOINTS ###########################################################
  @app.route("/type/<type_str>")
  def getTypeInfo(type_str : str) -> DetailedPokemonType:
    result : DetailedPokemonType = fetchDetailedPokemonType(type_str)
    return  jsonify(result)
  
  # MOVE ENDPOINTS ###########################################################
  @app.route("/moves/<type_str>")
  def getMovesOfType(type_str : str) -> List[MoveData]:
    result : List[MoveData] = fetchPokemonMoves(type_str)
    return jsonify(result)
  
  @app.route("/moves/detailed/<move_name>")
  def getDetailedMove(move_name : str):
    result : List[MoveData] = fetchPokemonMove(move_name)
    return jsonify(result)
  
  # GYMLEADERS ENDPOINTS #####################################################
  @app.route("/gym-leader/random")
  def getRandomGymLeader() -> GymLeaderData:
    result : GymLeaderData = fetchRandomGymLeader()
    return jsonify(result)
  
  @app.route("/gym-leader/detailed/<leader_name>")
  def getDetailedGymLeader(leader_name : str) -> Response:
    print(leader_name)
    result = fetchDetailedGymLeader(leader_name)
    print(result)
    return result

  @app.route("/gym-leaders/<generation>")
  def getGymLeadersFromGeneration(generation : str) -> PokemonRegionGymLeaders:
    res : list[GymLeaderData] = fetchGymLeadersByGeneration(generation)
    return jsonify(res)
  
  # for SEARCH BAR
  @app.route("/search/match/<sub_string>")
  def getMatchingSearchResults(sub_string) -> List[str]:
    print(f"Searching for strings that match {sub_string}")
    matches : List[str] = filterBySubstringAcrossPools(sub_string)
    return jsonify(matches)
  