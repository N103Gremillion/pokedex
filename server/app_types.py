from enum import Enum
from typing import NotRequired, TypedDict, Any, Optional

# generic types for when you make a api fetch
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
  types: NotRequired[list[str]]

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
  GEN_NUMBER = "gen_number"
  POKEMON = "pokemon"
  
class PokedexData(TypedDict):
  gen_number : int
  pokemon : list[PokemonData]
  
