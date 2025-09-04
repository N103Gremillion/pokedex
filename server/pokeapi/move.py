from typing import List
from app_types import ErrorResponse, MoveData, MoveKeys, PokemonType, SuccessResponse, SuccessResponseKeys
from pokeapi.general import fetchData
from pokeapi.pokemon import PokemonInfoEndpoints
from utils import isValidType

def fetchPokemonMove(move_name : str) -> MoveData:
  result : MoveData = {
    MoveKeys.ACCURACY : -1,
    MoveKeys.EFFECT_CHANCE : -1,
    MoveKeys.PP : -1,
    MoveKeys.PRIORITY : 0,
    MoveKeys.POWER : -1,
    MoveKeys.DMG_CLASS : 'unknown',
    MoveKeys.NAME : "unknown",
    MoveKeys.TYPE_NAME : PokemonType.Unknown
  }
  
  url : str = f"{PokemonInfoEndpoints.GET_MOVE.value}/{move_name}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not SuccessResponse[SuccessResponseKeys.SUCCESS]):
    print(f"Non successful request to api for url : {url}")
    return result
  
  data = response[SuccessResponseKeys.DATA]
  
  accuracy = data.get("accuracy") 
  
  if accuracy:
    result[MoveKeys.ACCURACY] = accuracy
    
  effect_chance = data.get("effect_chance")
  
  if effect_chance:
    result[MoveKeys.EFFECT_CHANCE] = effect_chance
    
  pp = data.get("pp")
  
  if pp:
    result[MoveKeys.PP] = pp
    
  priority = data.get("priority")
  
  print(priority)
  
  if priority:
    result[MoveKeys.PRIORITY] = priority
    
  power = data.get("power")
  
  if power:
    result[MoveKeys.POWER] = power
    
  dmg_class_data = data.get("damage_class")
  
  if dmg_class_data:
    dmg_class = dmg_class_data.get("name")
    if dmg_class:
      result[MoveKeys.DMG_CLASS] = dmg_class
    
  name = data.get("name")
  
  if name:
    result[MoveKeys.NAME] = name
  
  effect_entries_data = data.get("effect_entries")
  
  # print(effect_entries_data)
  
  type_data = data.get("type")
  
  if type_data:
    type_name = type_data.get("name")
    if type_name:
      result[MoveKeys.TYPE_NAME] = type_name.capitalize()
  
  return result
  
def fetchPokemonMoves(type_str : str) -> List[MoveData]:
  
  result : List[MoveData] = []
  
  if (not isValidType(type_str)):
    print(f"Could not fetch moves info for type {type_str}")
    return result
  
  url : str = f"{PokemonInfoEndpoints.GET_TYPE.value}/{type_str}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not SuccessResponse[SuccessResponseKeys.SUCCESS]):
    print(f"Non successful request to api for url : {url}")
    return result
  
  data = response[SuccessResponseKeys.DATA]  
  moves_data = data.get("moves")
  
  if (not moves_data):
    return result
  
  for move_data in moves_data:
    move_name : str = move_data.get("name")
    if (move_name):
      result.append(fetchPokemonMove(move_name))
  
  return result