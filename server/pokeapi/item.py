# general pokemon fetched used for the pokemon specific pages
from enum import Enum
from app_types import ErrorResponse, ErrorResponseKeys, ItemData, ItemKeys, PokemonData, SuccessResponse, SuccessResponseKeys
from pokeapi.pokemon import PokeApiEndpoints
from pokeapi.general import baseApiUrl, fetchData

# less data for this one since it is not used on the in depth pokemon pages
def fetchItemByIdentifier(identifier: int | str) -> ItemData:
  url : str = f"{PokeApiEndpoints.GET_ITEM.value}/{identifier}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching data for item id: {identifier}. Error: {response['error']}")
    return {
      ItemKeys.ID: -1,
      ItemKeys.NAME: "Unknown",
      ItemKeys.IMAGE_URL: "",
    }
  
  data = response[SuccessResponseKeys.DATA]
  
  # map the data onto the PokemonData to ensure you have these on the frontend
  itemData : ItemData = {
    ItemKeys.ID: data.get("id"),
    ItemKeys.NAME: data.get("name"),
    ItemKeys.IMAGE_URL: data.get("sprites").get("default"),
  }
  
  return itemData

def fetchDetailedItemByIdentifier(identifier : int | str) -> ItemData:
  url : str = f"{PokeApiEndpoints.GET_ITEM.value}/{identifier}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching data for item id: {identifier}. Error: {response['error']}")
    return {
      ItemKeys.ID: -1,
      ItemKeys.NAME: "Unknown",
      ItemKeys.IMAGE_URL: "",
    }
  
  data = response[SuccessResponseKeys.DATA]
  
  # Get effect
  effect_entries = data.get("effect_entries", [])
  effect_text = ""
  for entry in effect_entries:
    if entry.get("language", {}).get("name") == "en":
        effect_text = entry.get("effect", "")
        break
          
  # map the data onto the PokemonData to ensure you have these on the frontend
  itemData : ItemData = {
    ItemKeys.ID: data.get("id"),
    ItemKeys.NAME: data.get("name"),
    ItemKeys.IMAGE_URL: data.get("sprites").get("default"),
    ItemKeys.EFFECT : effect_text
  }
  
  return itemData
