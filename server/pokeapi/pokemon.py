from .api import baseApiUrl
from enum import Enum
import requests

class PokemonInfoEndpoints(Enum):
  GET_POKEMON = f"{baseApiUrl}/pokemon"

def fetchPokemon(pokemonName : str):
  response = requests.get(f"{PokemonInfoEndpoints.GET_POKEMON.value}/{pokemonName}")
  
  json = response.json()
  
  return json
  