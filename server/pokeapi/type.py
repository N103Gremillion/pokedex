from app_types import DetailedPokemonType, DetailedPokemonTypeKeys, ErrorResponse, PokemonType, SuccessResponse, SuccessResponseKeys
from typing import List
from pokeapi.general import baseApiUrl, fetchData
from pokeapi.pokemon import PokemonInfoEndpoints
from utils import isValidType, print_pretty_json

def fetchDetailedPokemonType(type_str : str) -> DetailedPokemonType:
  result : DetailedPokemonType = {
    DetailedPokemonTypeKeys.TYPE_NAME : PokemonType.Unknown,
    DetailedPokemonTypeKeys.NO_DMG_TO : [],
    DetailedPokemonTypeKeys.HALF_DMG_TO : [],
    DetailedPokemonTypeKeys.DOUBLE_DMG_TO : [],
    DetailedPokemonTypeKeys.NO_DMG_FROM : [],
    DetailedPokemonTypeKeys.HALF_DMG_FROM : [],
    DetailedPokemonTypeKeys.DOUBLE_DMG_FROM : [],
  }
  
  if (not isValidType(type_str)):
    print(f"Could not fetch detailed info for type {type_str}")
    return result
  
  result[DetailedPokemonTypeKeys.TYPE_NAME] = type_str
  url : str = f"{PokemonInfoEndpoints.GET_TYPE.value}/{type_str}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not SuccessResponse[SuccessResponseKeys.SUCCESS]):
    print(f"Non successful request to api for url : {url}")
    return result
  
  data = response[SuccessResponseKeys.DATA]
  
  damage_relations_data = data.get("damage_relations")
  
  if (not damage_relations_data):
    return result

  no_damage_to_data = damage_relations_data.get("no_damage_to")
  half_damage_to_data = damage_relations_data.get("half_damage_to")
  double_damage_to_data = damage_relations_data.get("double_damage_to")
  no_damage_from_data = damage_relations_data.get("no_damage_from")
  half_damage_from_data = damage_relations_data.get("half_damage_from")
  double_damage_from_data = damage_relations_data.get("double_damage_from")
  
  if (no_damage_to_data):
    for entry in no_damage_to_data:
      type : str | None = entry.get("name")
      if (type):
        result[DetailedPokemonTypeKeys.NO_DMG_TO].append(type.capitalize())
    
  if (half_damage_to_data):
    for entry in half_damage_to_data:
      type : str | None = entry.get("name")
      if (type):
        result[DetailedPokemonTypeKeys.HALF_DMG_TO].append(type.capitalize())
        
  if (double_damage_to_data):
    for entry in double_damage_to_data:
      type : str | None = entry.get("name")
      if (type):
        result[DetailedPokemonTypeKeys.DOUBLE_DMG_TO].append(type.capitalize())
        
  if (no_damage_from_data):
    for entry in no_damage_from_data:
      type : str | None = entry.get("name")
      if (type):
        result[DetailedPokemonTypeKeys.NO_DMG_FROM].append(type.capitalize())
        
  if (half_damage_from_data):
    for entry in half_damage_from_data:
      type : str | None = entry.get("name")
      if (type):
        result[DetailedPokemonTypeKeys.HALF_DMG_FROM].append(type.capitalize())
        
  if (double_damage_from_data):
    for entry in double_damage_from_data:
      type : str | None = entry.get("name")
      if (type):
        result[DetailedPokemonTypeKeys.DOUBLE_DMG_FROM].append(type.capitalize())
  
  return result