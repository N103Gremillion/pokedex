from typing import List, Optional
from flask import json
from app_types import DetailedPokemonTypeKeys, ErrorResponse, LearnMethod, MoveData, MoveKeys, PokedexKeys, PokemonData, PokemonEvolution, PokemonType, SuccessResponse, ErrorResponseKeys, PokemonKeys, SuccessResponseKeys
from mongo.db_utils import DatabaseCollections
from utils import hectogramsToPounds, isValidType, print_pretty_json
from pokeapi.general import baseApiUrl, fetchData
from enum import Enum
import requests
from pymongo.collection import Collection

class PokemonInfoEndpoints(Enum):
  GET_POKEMON = f"{baseApiUrl}/pokemon"
  GET_TYPE = f"{baseApiUrl}/type"
  GET_MOVE = f"{baseApiUrl}/move"
      
# less data for this one since it is not used on the in depth pokemon pages
def fetchPokemonDataByIdentifier(pokemon_identifier : int | str) -> PokemonData:
  url : str = f"{PokemonInfoEndpoints.GET_POKEMON.value}/{pokemon_identifier}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching data for pokemon identifier: {pokemon_identifier}. Error: {response['error']}")
    return {
      PokemonKeys.ID : -1,
      PokemonKeys.NAME : "Unknown",
      PokemonKeys.IMAGE_URL : ""
    }
  
  data = response[SuccessResponseKeys.DATA]
  
  # add type information
  type_info = data.get("types")
  types : list[PokemonType] = []
  
  for entry in type_info:
    type_data = entry.get("type")
    if (type_data):
      type_name = type_data.get("name")
      if isValidType(type_name.capitalize()):
        types.append(PokemonType(type_name.capitalize()))
  
  # map the data onto the PokemonData to ensure you have these on the frontend
  pokemonData : PokemonData = {
    PokemonKeys.ID : data.get("id"),
    PokemonKeys.NAME : data.get("name"),
    PokemonKeys.IMAGE_URL : data.get("sprites").get("front_default"),
    PokemonKeys.TYPES : types
  }
  
  return pokemonData

# this is used to extract all data necessary for the in depth pokemon page
def fetchDetailedPokemonDataByIdentifier(pokemon_identifier : int | str) -> PokemonData:
  from pokeapi.move import fetchPokemonMove
  
  url : str = f"{PokemonInfoEndpoints.GET_POKEMON.value}/{pokemon_identifier}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching data for pokemon identifier: {pokemon_identifier}. Error: {response['error']}")
    return {
      PokemonKeys.ID : -1,
      PokemonKeys.NAME : "Unknown",
      PokemonKeys.IMAGE_URL : ""
    }
  
  data = response[SuccessResponseKeys.DATA]
  
  # add type information
  type_info = data.get("types")
  types : list[PokemonType] = []
  
  for entry in type_info:
    type_data = entry.get("type")
    if (type_data):
      type_name = type_data.get("name")
      if isValidType(type_name.capitalize()):
        types.append(PokemonType(type_name.capitalize()))
  
  # evolution chain
  species_url = data.get("species").get("url")
  response : SuccessResponse | ErrorResponse = fetchData(url)
  species_data = response[SuccessResponseKeys.DATA]
  
  if species_data:
    evolution_chain : List[PokemonEvolution] = fetchEvolutionChainById(species_data.get("id"))
    
  # stats
  hp = attack = defense = sp_attack = sp_defense = speed = -1
  
  for entry in data.get("stats", []):
    name : str | None = entry.get("stat").get("name")
    base : int = entry.get("base_stat", -1)
    match name:
      case "hp":
        hp = base
      case "attack":
        attack = base
      case "defense":
        defense = base
      case "special-attack":
        sp_attack = base
      case "special-defense":
        sp_defense = base
      case "speed":
        speed = base
        
  # moves
  api_moves_data  = data.get("moves")
  moves : List[MoveData]  = []
  
  # for entry in api_moves_data:
  #   move_data = entry.get("move")
  #   move_name = move_data.get("name")

  #   if not move_name: continue

  #   move : MoveData = fetchPokemonMove(move_name)
  #   level_learned : int = -1
    
  #   version_details = entry.get("version_group_details") # list of move info from different games
    
  #   if (version_details and len(version_details) > 0):
  #     last_entry = version_details[-1]
  #     level_learned = last_entry.get("level_learned_at", -1)
  #     learn_method = last_entry.get("move_learn_method", {}).get("name")
      
  #     match learn_method:
  #       case "level-up":
  #         move[MoveKeys.LEARN_METHOD] = LearnMethod.LEVEL_UP
  #       case "machine":
  #         move[MoveKeys.LEARN_METHOD] = LearnMethod.MACHINE
  #       case "egg":
  #         move[MoveKeys.LEARN_METHOD] = LearnMethod.EGG
  #       case "tutor":
  #         move[MoveKeys.LEARN_METHOD] = LearnMethod.TUTOR
  #       case _:
  #         move[MoveKeys.LEARN_METHOD] = LearnMethod.OTHER
    
    
  #   move[MoveKeys.LEVEL_LEARNED] = level_learned
  #   moves.append(move)
  
  # map the data onto the PokemonData to ensure you have these on the frontend
  pokemonData : PokemonData = {
    PokemonKeys.ID : data.get("id"),
    PokemonKeys.NAME : data.get("name"),
    PokemonKeys.IMAGE_URL : data.get("sprites").get("front_default"),
    PokemonKeys.TYPES : types,
    PokemonKeys.HEIGHT : data.get("height"),
    PokemonKeys.WEIGHT : hectogramsToPounds(data.get("weight")),
    PokemonKeys.SHINY_IMAGE_URL : data.get("sprites").get("front_shiny"),
    PokemonKeys.HP : hp,
    PokemonKeys.ATTACK : attack,
    PokemonKeys.DEFENSE : defense,
    PokemonKeys.SP_ATTACK : sp_attack,
    PokemonKeys.SP_DEFENSE : sp_defense,
    PokemonKeys.SPEED : speed,
    PokemonKeys.MOVES_LEARNED : moves
  }
  
  return pokemonData

  
def fetchAllPokemonOfType(pokemon_type : PokemonType) -> List[PokemonData]:
  from entry import globalDb 
  

  pokemOfTypeCollection : Collection = globalDb[DatabaseCollections.POKEMON_OF_TYPE.value.name]
  pokemonOfTypeDoc = pokemOfTypeCollection.find_one({ DetailedPokemonTypeKeys.TYPE_NAME : pokemon_type })
  
  if pokemonOfTypeDoc:
    return pokemonOfTypeDoc[PokedexKeys.POKEMON]
  
  url : str = f"{PokemonInfoEndpoints.GET_TYPE.value}/{pokemon_type.lower()}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching data for pokemon by type: {pokemon_type}. Error: {response['error']}")
    return []
  
  data = response[SuccessResponseKeys.DATA]
  
  if not data.get("pokemon"):
    print(f"Could not pull of pokemon from data when fetching pokemon of type {pokemon_type}.")
    return []
  
  pokemon : List[PokemonData] = []
  
  for entry in data.get("pokemon"):
    pokemon_entry = entry.get("pokemon", {})
    name: str | None = pokemon_entry.get("name")
    if not name:
      continue
    pokemon.append(fetchPokemonDataByIdentifier(name))
  
  pokemOfTypeCollection.insert_one({
    DetailedPokemonTypeKeys.TYPE_NAME : pokemon_type,
    PokedexKeys.POKEMON : pokemon
  })
  
  return pokemon

def fetchAllPokemonNames() -> List[str]:
  url : str = f"{PokemonInfoEndpoints.GET_POKEMON}?limit=100000&offset=0"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching all pokemon. Error: {response['error']}")
    return []
  
  data = response[SuccessResponseKeys.DATA]
  pokemon_names : List[str] = []
  
  for pokemon in data:
    if pokemon:
      name = pokemon["name"]
      if name:
        pokemon_names.append(name)
  
  return pokemon_names

def fetchEvolutionChainById(id : int | None) -> List[PokemonEvolution]:
  if not id:
    return []
  
  evolution_chain_url : str = f"{baseApiUrl}/evolution-chain/{id}"
  
  return []
  
  
  