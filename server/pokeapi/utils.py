from app_types import PokemonType


def print_pretty_json(data) -> None:
  import json
  print(json.dumps(data, indent=4))
  
def isValidType(value : str | None) -> bool:
  for type in PokemonType:
    if (value == type.value):
      return True
  return False