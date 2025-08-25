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

# Gym Leaders
class GymLeaderKeys(str, Enum):
  ID = "id"
  NAME = "name"
  IMAGE_URL = "imageUrl"
  
class GymLeaderData(TypedDict):
  id : int
  name : str
  imageUrl : str

# Pokedex
class PokedexKeys(str, Enum):
  GEN_NUMBER = "gen_num"
  POKEMON = "pokemon"
  
class PokedexData(TypedDict):
  gen_number : int
  pokemon : list[PokemonData]


