from enum import Enum
from typing import List, NotRequired, TypedDict, Any, Optional

# Helpful Types
class PokemonType (str, Enum):
  Normal = "Normal",
  Fire = "Fire",
  Water = "Water",
  Electric = "Electric",
  Grass = "Grass",
  Ice = "Ice",
  Fighting = "Fighting",
  Poison = "Poison",
  Ground = "Ground",
  Flying = "Flying",
  Psychic = "Psychic",
  Bug = "Bug",
  Rock = "Rock",
  Ghost = "Ghost",
  Dragon = "Dragon",
  Dark = "Dark",
  Steel = "Steel",
  Fairy = "Fairy",
  Unknown = "Unknown"
 
# generic object to return in api fetches
class SuccessResponseKeys(str, Enum):
  SUCCESS = "success"
  DATA = "data"
  
class SuccessResponse(TypedDict):
  success: bool
  data: Any

class ErrorResponseKeys(str, Enum):
  SUCCESS = "success"
  ERROR = "error"
  STATUS_CODE = "status_code"
  DETAILS = "details"
  
class ErrorResponse(TypedDict):
  success: bool
  error: str
  status_code: Optional[int]
  details: Optional[str]
  
# Pokemon
class PokemonKeys(str, Enum):
  ID = "id"
  NAME = "name"
  IMAGE_URL = "imageUrl"
  TYPES = "types"
  LEVEL = "level"
  
class PokemonData(TypedDict):
  id: int
  name: str
  imageUrl : str
  types: NotRequired[list[PokemonType]]
  level : NotRequired[str]

# Moves
class MoveKeys(str, Enum):
  ACCURACY = "accuracy"
  EFFECT_CHANCE = "effect_chance"
  PP = "pp"
  PRIORITY = "priority"
  POWER = "power"
  DMG_CLASS = "dmg_class"
  EFFECTS = "effects"
  NAME = "name"
  TYPE_NAME = "type_name"
  
class MoveData(TypedDict):
  accuracy : int
  effect_chance : int
  pp : int
  priority : int
  power : int
  dmg_class : str
  effects : List[str]
  name : str
  type_name : PokemonType
  
# Items
class ItemKeys(str, Enum):
  ID = "id"
  NAME = "name"
  IMAGE_URL = "imageUrl"
  
class ItemData(TypedDict):
  id: int
  name: str
  imageUrl : str

# Pokedex
class PokedexKeys(str, Enum):
  GEN_NUMBER = "gen_num"
  POKEMON = "pokemon"
  
class PokedexData(TypedDict):
  gen_num : int
  pokemon : list[PokemonData]

# Gym Leaders
class GymLeaderKeys(str, Enum):
  ID = "id"
  GYM_NAME = "gym_name"
  GYM_LEADER_NAME = "gym_leader_name"
  GYM_LEADER_IMAGE_URL = "gym_leader_image_url"
  TYPE = "element_type"
  BADGE_NAME = "badge_name"
  BADGE_IMAGE_URL = "badge_image_url"
  POKEMON = "pokemon"
  
class GymLeaderData(TypedDict):
  id : int
  gym_name : str
  gym_leader_name : str
  gym_leader_image_url : str
  element_type : PokemonType
  badge_name : str
  badge_image_url : str
  pokemon : NotRequired[list[PokemonData]]

# Island Kahunas
class IslandKahunaKeys(str, Enum):
  ID = "id"
  FIGHT_LOCATION = "fight_location"
  ISLAND_KAHUNA_NAME = "island_kahuna_name"
  ISLAND_KAHUNA_IMAGE_URL = "island_kahuna_image_url"
  TYPE = "element_type"
  POKEMON = "pokemon"
  
class IslandKahunaData(TypedDict):
  id : int
  fight_location : str
  island_kahuna_name : str
  island_kahuna_image_url : str
  element_type : PokemonType
  pokemon : NotRequired[list[PokemonData]]
  
# Island Captains
class IslandCaptainKeys(str, Enum):
  ID = "id"
  ISLAND_CAPTAIN_NAME = "island_captain_name"
  ISLAND_CAPTAIN_IMAGE_URL = "island_captain_image_url"
  TYPE = "element_type"
  POKEMON = "pokemon"
  
class IslandCaptainData(TypedDict):
  id : int
  island_captain_name : str
  island_captain_image_url : str
  element_type : PokemonType
  pokemon : NotRequired[list[PokemonData]]

# PokemonRegion Gym/Importan trainer info
class PokemonRegionGymLeadersKeys(str, Enum):
  GEN_NUMBER = "gen_num"
  REGION = "region"
  GYM_LEADERS = "gym_leaders"
  ISLAND_KAHUNAS = "island_kahunas" # for Sun and Moon
  ISLAND_CAPTAINS = "island_captains" # for Sun and Moon
  
class PokemonRegionGymLeaders(TypedDict):
  gen_num : int
  region : str
  gym_leaders : NotRequired[list[GymLeaderData]]
  island_kahunas : NotRequired[list[IslandKahunaData]]
  island_captains : NotRequired[list[IslandCaptainData]]
  
# in depth Type info
class DetailedPokemonTypeKeys(str, Enum):
  TYPE_NAME = "type_name"
  NO_DMG_TO = "no_dmg_to"
  HALF_DMG_TO = "half_dmg_to"
  DOUBLE_DMG_TO = "double_dmg_to"
  NO_DMG_FROM = "no_dmg_from"
  HALF_DMG_FROM = "half_dmg_from"
  DOUBLE_DMG_FROM = "double_dmg_from"
  
class DetailedPokemonType(TypedDict):
  type_name : PokemonType
  no_dmg_to : List[PokemonType]
  half_dmg_to : List[PokemonType]
  double_dmg_to : List[PokemonType]
  no_dmg_from : List[PokemonType]
  half_dmg_from : List[PokemonType]
  double_dmg_from : List[PokemonType]
  