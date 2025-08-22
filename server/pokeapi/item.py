# general pokemon fetched used for the pokemon specific pages
from enum import Enum
from app_types import ErrorResponse, ErrorResponseKeys, ItemData, ItemKeys, PokemonData, SuccessResponse, SuccessResponseKeys
from pokeapi.pokemon import PokemonInfoEndpoints
from .general import baseApiUrl, fetchData

class ItemInfoEndpoints(Enum):
  GET_ITEM = f"{baseApiUrl}/item"
  
def fetchItemByName(name: str):
  url : str = f"{ItemInfoEndpoints.GET_ITEM.value}/{name}"
  return fetchData(url)
    
# less data for this one since it is not used on the in depth pokemon pages
def fetchItemById(item_id: int) -> ItemData:
  url : str = f"{ItemInfoEndpoints.GET_ITEM.value}/{item_id}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching data for item id: {item_id}. Error: {response['error']}")
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