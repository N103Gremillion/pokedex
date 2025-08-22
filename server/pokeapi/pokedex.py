from enum import Enum
from flask import json
from app_types import ErrorResponse, ErrorResponseKeys, PokedexData, PokedexKeys, SuccessResponse, SuccessResponseKeys, PokemonData
from .general import baseApiUrl, fetchData
from .utils import print_pretty_json
from .pokemon import fetchPokemonById

class PokedexInfoEndpoints(Enum):
  GET_GENERATION = f"{baseApiUrl}/generation"

def fetchPokedexByGeneration(gen_num) -> PokedexData:
  url : str = f"{PokedexInfoEndpoints.GET_GENERATION.value}/{gen_num}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  res : PokedexData = {PokedexKeys.GEN_NUMBER :  gen_num, PokedexKeys.POKEMON : []}
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching data generation: {gen_num}. Error: {response['error']}")
    return res
  
  data = response[SuccessResponseKeys.DATA]
  
  # this is a dict
  pokemon_entries = data.get("pokemon_species")
  
  if (not pokemon_entries):
    print(f"Could not pull off pokemon entries when trying to fetch pokemon from generation {gen_num}")
    return res
  
  # id -> PokemonData
  pokemon_map : dict[int, PokemonData] = {}
  
  # note pokemon is a dict with {"name" : , "url" : }
  for pokemon in pokemon_entries:
    
    # try and pull of the url
    try:
      pokemon_url : str = pokemon["url"]
    except KeyError:
      print(f"Missing the key value url on one of the pokemon in gen {gen_num}. pokemon_info : {pokemon}")
      continue
    
    path_segments : list[str] = pokemon_url.split("/")
    
    try:
      pokemon_id : int = int(path_segments[-2])
    except ValueError:
      print(f"Issue pulling off the pokemon_id for a pokemon in gen {gen_num}. pokemon_info : {pokemon}")
      continue
    
    pokemon_map[pokemon_id] = fetchPokemonById(pokemon_id)
    
  sorted_pokemon = [pokemon_map[id_] for id_ in sorted(pokemon_map.keys())]
  res[PokedexKeys.POKEMON] = sorted_pokemon
  
  return res