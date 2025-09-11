from typing import List, Optional
from flask import json
from app_types import DetailedPokemonTypeKeys, ErrorResponse, LearnMethod, MoveData, MoveKeys, PokedexKeys, PokemonData, PokemonEvolution, PokemonEvolutionKeys, PokemonType, SuccessResponse, ErrorResponseKeys, PokemonKeys, SuccessResponseKeys
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
  species_response : SuccessResponse | ErrorResponse = fetchData(species_url)
  species_data = species_response[SuccessResponseKeys.DATA]
  evolution_chain : List[PokemonEvolution] = []
  
  if species_data:
    evolution_chain_url = species_data.get("evolution_chain", {}).get("url")
    if evolution_chain_url:
      evolution_chain = fetchEvolutionChainById(evolution_chain_url)
    
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
  
  for entry in api_moves_data:
    move_data = entry.get("move")
    move_name = move_data.get("name")

    if not move_name: continue

    move : MoveData = fetchPokemonMove(move_name)
    level_learned : int = -1
    
    version_details = entry.get("version_group_details") # list of move info from different games
    
    if (version_details and len(version_details) > 0):
      last_entry = version_details[-1]
      level_learned = last_entry.get("level_learned_at", -1)
      learn_method = last_entry.get("move_learn_method", {}).get("name")
      
      match learn_method:
        case "level-up":
          move[MoveKeys.LEARN_METHOD] = LearnMethod.LEVEL_UP
        case "machine":
          move[MoveKeys.LEARN_METHOD] = LearnMethod.MACHINE
        case "egg":
          move[MoveKeys.LEARN_METHOD] = LearnMethod.EGG
        case "tutor":
          move[MoveKeys.LEARN_METHOD] = LearnMethod.TUTOR
        case _:
          move[MoveKeys.LEARN_METHOD] = LearnMethod.OTHER
    
    
    move[MoveKeys.LEVEL_LEARNED] = level_learned
    moves.append(move)
  
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
    PokemonKeys.EVOLUTION_CHAIN : evolution_chain,
    PokemonKeys.MOVES_LEARNED : moves,
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

# should fetch from the evolution-chain endpoint from the api
def fetchEvolutionChainById(evolution_chain_url : str | None) -> List[PokemonEvolution]:
  if not evolution_chain_url:
    return []
  
  res : SuccessResponse | ErrorResponse = fetchData(evolution_chain_url)
  if not res[SuccessResponseKeys.SUCCESS]:
    return []
  
  data = res[SuccessResponseKeys.DATA]
  chain = data.get("chain")  
  result : List[PokemonEvolution] = []
  
  def traverse(node):
    species : str = node.get("species", {})
    
    # general info about the pokemon
    pokemon_name: str = species.get("name", "Unknown")
    pokemon_data : PokemonData = fetchPokemonDataByIdentifier(pokemon_name)
    
    # evolution details
    evolution_details  = node.get("evolution_details", [])

    if evolution_details:
      methods : List[str] = []
      for detail in evolution_details:
        methods.append(getEvolutionMethod(detail))
      method_str = ", ".join(methods)
    else:
      method_str = "none"
    
    result.append({
      PokemonEvolutionKeys.POKEMON : pokemon_data,
      PokemonEvolutionKeys.METHOD : method_str
    })
      
    # traverse all evolutions
    for next_node in node.get("evolves_to", []):
      traverse(next_node)
  
  traverse(chain)
  return result

# constructs a string about the evolution method from the details dict defined in the pokeapi(Type EvolutionDetail)
def getEvolutionMethod(details: dict) -> str:
    res = []

    if details.get("min_level"):
        res.append(f"level-up {details['min_level']}")
    if details.get("min_happiness"):
        res.append(f"happiness ≥ {details['min_happiness']}")
    if details.get("min_beauty"):
        res.append(f"beauty ≥ {details['min_beauty']}")
    if details.get("min_affection"):
        res.append(f"affection ≥ {details['min_affection']}")
    if details.get("item"):
        res.append(f"using {details['item']['name']}")
    if details.get("gender"):
        res.append(f"gender: {details['gender']}")
    if details.get("held_item"):
        res.append(f"holding {details['held_item']['name']}")
    if details.get("known_move"):
        res.append(f"knows move {details['known_move']['name']}")
    if details.get("known_move_type"):
        res.append(f"knows move type {details['known_move_type']['name']}")
    if details.get("location"):
        res.append(f"at {details['location']['name']}")
    if details.get("needs_overworld_rain"):
        res.append("while raining")
    if details.get("relative_physical_stats") is not None:
        val = details['relative_physical_stats']
        match val:
            case 1:
                res.append("Attack > Defense")
            case 0:
                res.append("Attack = Defense")
            case -1:
                res.append("Attack < Defense")
    if details.get("time_of_day"):
        res.append(details["time_of_day"])
    if details.get("trade_species"):
        res.append(f"Trade for {details['trade_species']['name']}")

    if not res:
        return "Other"

    return ", ".join(res)
  