from typing import Optional

from flask import json
from app_types import ErrorResponse, PokemonData, PokemonType, SuccessResponse, ErrorResponseKeys, PokemonKeys, SuccessResponseKeys
from pokeapi.utils import isValidType, print_pretty_json
from pokeapi.general import baseApiUrl, fetchData
from enum import Enum
import requests

class PokemonInfoEndpoints(Enum):
  GET_POKEMON = f"{baseApiUrl}/pokemon"
      
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
      if isValidType(type_name):
        types.append(type_name)
  
  # map the data onto the PokemonData to ensure you have these on the frontend
  pokemonData : PokemonData = {
    PokemonKeys.ID : data.get("id"),
    PokemonKeys.NAME : data.get("name"),
    PokemonKeys.IMAGE_URL : data.get("sprites").get("front_default"),
    PokemonKeys.TYPES : types
  }
  
  return pokemonData
  
        