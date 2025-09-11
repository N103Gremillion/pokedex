from typing import List
from app_types import PokemonType

def print_pretty_json(data) -> None:
  import json
  print(json.dumps(data, indent=4))
  
def isValidType(value : str | None) -> bool:
  for type in PokemonType:
    if (value == type.value):
      return True
  return False

def hectogramsToPounds(value : int | None) -> float:
  if value is None:
    return -1.0
  return round((value / 10) * 2.20462, 4)

def filterBySubstringAcrossPools(sub_string : str) -> List[str]:
  res : List[str] = []
  
  res.extend(filterPokemonBySubstring(sub_string))
  res.extend(filterGymLeadersBySubstring(sub_string))
  res.extend(filterTypesBySubstring(sub_string))
  
  return res

def filterPokemonBySubstring(sub_string : str) -> List[str]:
  res : List[str] = []
  
  pokemon : List[str] = []
  
  return res

def filterGymLeadersBySubstring(sub_string : str) -> List[str]:
  from scraper.gymLeaderPageScrapper import GYM_LEADERS
  
  res : List[str] = []
  
  for gym_leader_name in GYM_LEADERS:
    if (gym_leader_name.lower().startswith(sub_string.lower())):
      res.append(gym_leader_name)
  
  return res

def filterTypesBySubstring(sub_string : str) -> List[str]:
  
  res : List[str] = []
  
  for poke_type in PokemonType:
    if (poke_type.value.lower().startswith(sub_string.lower())):
      res.append(poke_type.value)
    
  return res