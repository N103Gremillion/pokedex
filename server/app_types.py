from enum import Enum
from typing import NotRequired, TypedDict, Any, Optional

# Helpful Types
class PokemonType (str, Enum):
  Normal = "normal",
  Fire = "fire",
  Water = "water",
  Electric = "electric",
  Grass = "grass",
  Ice = "ice",
  Fighting = "fighting",
  Poison = "poison",
  Ground = "ground",
  Flying = "flying",
  Psychic = "psychic",
  Bug = "bug",
  Rock = "rock",
  Ghost = "ghost",
  Dragon = "dragon",
  Dark = "dark",
  Steel = "steel",
  Fairy = "fairy"
 
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
  
class PokemonData(TypedDict):
  id: int
  name: str
  imageUrl : str
  types: NotRequired[list[PokemonType]]

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

class PokemonRegionGymLeadersKeys(str, Enum):
  GEN_NUMBER = "gen_num"
  REGION = "region"
  GYM_LEADERS = "gym_leaders"
  ISLAND_LEADERS = "island_leaders" # for Sun and Moon
  
class PokemonRegionGymLeaders(TypedDict):
  gen_num : int
  region : str
  gym_leaders : NotRequired[list[GymLeaderData]]
  island_leaders : NotRequired[list[GymLeaderData]]
