from typing import Optional
from app_types import ErrorResponse, PokemonData, SuccessResponse
from .general import baseApiUrl, fetchData
from enum import Enum
import requests

class PokemonInfoEndpoints(Enum):
  GET_POKEMON = f"{baseApiUrl}/pokemon"
  

# general pokemon fetched used for the pokemon specific pages
def fetchPokemonByName(name: str):
  url : str = f"{PokemonInfoEndpoints.GET_POKEMON.value}/{name}"
  return fetchData(url)
    
# less data for this one since it is not used on the in depth pokemon pages
def fetchPokemonById(pokemon_id: int) -> PokemonData:
  url : str = f"{PokemonInfoEndpoints.GET_POKEMON.value}/{pokemon_id}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response["success"]):
    print(f"Error fetching data for pokemon id: {pokemon_id}. Error: {response['error']}")
    return {
      "id": -1,
      "name": "Unknown",
      "imageUrl": ""
    }
  
  data = response["data"]
  
  # map the data onto the PokemonData to ensure you have these on the frontend
  pokemonData : PokemonData = {
    "id": data.get("id"),
    "name": data.get("name"),
    "imageUrl": data.get("sprites").get("front_default"),
  }
  
  return pokemonData
  
        