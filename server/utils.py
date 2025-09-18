from typing import List
from app_types import IslandCaptainKeys, IslandKahunaKeys, PokemonType
from scraper.gen7data import GEN_7_ISLAND_KAHUNAS
from scraper.gen7data import GEN_7_ISLAND_CAPTAINS

def print_pretty_json(data) -> None:
  import json
  print(json.dumps(data, indent=4))
  
def isValidType(value : str | None) -> bool:
  for type in PokemonType:
    if (value == type.value):
      return True
  return False

def isValidGymLeaderName(leader_name : str) -> bool:
  from scraper.gymLeaderPageScrapper import GYM_LEADERS
  
  leader_name = leader_name.lower()
  
  # typicall gym leaders
  for generation_leaders in GYM_LEADERS:
    for leader in generation_leaders:
      if leader_name == leader.lower():
        return True
        
  # island kahunas
  for kahunas in GEN_7_ISLAND_KAHUNAS:
    if leader_name == kahunas.get(IslandKahunaKeys.ISLAND_KAHUNA_NAME).lower():
      return True
  
  # island captains
  for captains in GEN_7_ISLAND_CAPTAINS:
    if leader_name == captains.get(IslandCaptainKeys.ISLAND_CAPTAIN_NAME).lower():
      return True
    
  return False

def getGenNumFromGymLeaderName(leader_name : str) -> int:
  from scraper.gymLeaderPageScrapper import GYM_LEADERS
  
  leader_name = leader_name.strip().lower()
  
  # island kahunas
  for kahunas in GEN_7_ISLAND_KAHUNAS:
    if leader_name == kahunas.get(IslandKahunaKeys.ISLAND_KAHUNA_NAME).lower():
      return 7
    
  # island captains
  for captains in GEN_7_ISLAND_CAPTAINS:
    if leader_name == captains.get(IslandCaptainKeys.ISLAND_CAPTAIN_NAME).lower():
      return 7
    
  # typicall gym leaders
  gen_index = 1
  for leaders in GYM_LEADERS:
    # If this generation is Gen 7, skip it
    if gen_index == 7:
      gen_index += 1
    if any(leader_name == name.lower() for name in leaders):
      return gen_index
    gen_index += 1
    
  return -1
  
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