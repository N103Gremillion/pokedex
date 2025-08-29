from enum import Enum
from typing import NotRequired, TypedDict, Any, Optional

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
  Various = "Various"
 
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
