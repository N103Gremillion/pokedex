from typing import List, Optional
from flask import json
from app_types import DetailedPokemonTypeKeys, ErrorResponse, PokedexKeys, PokemonData, PokemonType, SuccessResponse, ErrorResponseKeys, PokemonKeys, SuccessResponseKeys
from mongo.db_utils import DatabaseCollections
from utils import isValidType, print_pretty_json
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