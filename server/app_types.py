from typing import TypedDict, Any, Optional


class SuccessResponse(TypedDict):
  success: bool
  data: Any

class ErrorResponse(TypedDict):
  success: bool
  error: str
  status_code: Optional[int]
  details: Optional[str]

class PokemonData(TypedDict):
  id: int
  name: str
  imageUrl : str

class ItemData(TypedDict):
  id: int
  name: str
  imageUrl : str
