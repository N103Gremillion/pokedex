from typing import List
from app_types import IslandCaptainKeys, IslandKahunaKeys, PokemonType
from scraper.gen7data import GEN_7_ISLAND_KAHUNAS
from scraper.gen7data import GEN_7_ISLAND_CAPTAINS

def print_pretty_json(data) -> None:
  import json
  print(json.dumps(data, indent=4))
  
def isValidType(value : str | None) -> bool:
  if not value:
    return False
  
  value = value.lower()
  
  for type in PokemonType:
    if (value == type.value.lower()):
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

def isValidPokemon(pokemon_name : str) -> bool:
  from pokeapi.pokemon import POKEMON_SET
  
  pokemon_name = pokemon_name.lower().replace(" ", "-")
  return pokemon_name in POKEMON_SET

def isValidPokemonMove(move_name : str) -> bool:
  from pokeapi.move import POKEMON_MOVES_SET
  move_name = move_name.lower().replace(" ", "-")
  move_name = move_name.lower().replace("_", "-")
  return move_name in POKEMON_MOVES_SET

def isValidItem(item_name : str) -> bool:
  from pokeapi.item import ITEMS_SET
  item_name = item_name.lower().replace(" ", "-")
  item_name = item_name.lower().replace("_", "-")
  return item_name in ITEMS_SET
  
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
  
  res.extend(filterTypesBySubstring(sub_string))
  res.extend(filterGymLeadersBySubstring(sub_string))
  res.extend(filterPokemonBySubstring(sub_string))
  res.extend(filterMoveBySubstring(sub_string))
  res.extend(filterItemBySubstring(sub_string))
  
  return res

def filterItemBySubstring(sub_string : str) -> List[str]:
  from pokeapi.item import ITEM_NAMES
  
  sub_string = sub_string.lower().replace(" ", "-")
  sub_string = sub_string.lower().replace("_", "-")
  
  res : List[str] = []
  
  for item_name in ITEM_NAMES:
    if item_name.startswith(sub_string):
      res.append(item_name)
  
  return res
  
def filterMoveBySubstring(sub_string : str) -> List[str]:
  from pokeapi.move import POKEMON_MOVES
  
  sub_string = sub_string.lower().replace(" ", "-")
  sub_string = sub_string.lower().replace("_", "-")
  
  res : List[str] = []
  
  for move_name in POKEMON_MOVES:
    if move_name.startswith(sub_string):
      res.append(move_name)
  
  return res
  
def filterPokemonBySubstring(sub_string : str) -> List[str]:
  from pokeapi.pokemon import POKEMON_NAMES
  
  sub_string = sub_string.lower().replace(" ", "-")
  sub_string = sub_string.lower().replace("_", "-")
  
  res : List[str] = []
  
  for name in POKEMON_NAMES:
    if name.startswith(sub_string):
      res.append(name)
  
  return res

def filterGymLeadersBySubstring(sub_string : str) -> List[str]:
  from scraper.gymLeaderPageScrapper import GYM_LEADERS
  
  sub_string = sub_string.lower()
  sub_string = sub_string.replace(" ", "_")
  
  res : List[str] = []
  
  for generation_gym_leaders in GYM_LEADERS:
    for gym_leader_name in generation_gym_leaders:
      if (gym_leader_name.lower().startswith(sub_string)):
        res.append(gym_leader_name)
  
  return res

def filterTypesBySubstring(sub_string : str) -> List[str]:
  
  res : List[str] = []
  
  for poke_type in PokemonType:
    if (poke_type.value.lower().startswith(sub_string.lower())):
      res.append(poke_type.value)
    
  return res