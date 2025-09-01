# pokemondb scrapping rules so they dont block my ip
"""
rules_referenced_from : https://pokemondb.net/robots.txt
1.) 2 seconds between requests
2.) 
  Disallowed_Endpoints:
    Disallow: /pokebase/search?
    Disallow: /pokebase/revisions
    Disallow: /pokebase/meta/search?
    Disallow: /pokebase/meta/revisions
    Disallow: /pokebase/rmt/search?
    Disallow: /pokebase/rmt/revisions

use these to discover pages :     
  Sitemap: https://pokemondb.net/static/sitemaps/pokemondb.xml
  Sitemap: https://pokemondb.net/static/sitemaps/pokebase.xml
  Sitemap: https://pokemondb.net/static/sitemaps/images.xml
  
Note:
  I am using this because some information is not openly availble on the pokeapi.
  
"""

import random
from typing import List
from bs4 import BeautifulSoup, Tag
from app_types import ErrorResponse, ErrorResponseKeys, GymLeaderData, GymLeaderKeys, IslandCaptainData, IslandCaptainKeys, IslandKahunaData, IslandKahunaKeys, PokemonData, PokemonKeys, PokemonType, SuccessResponse, SuccessResponseKeys
from pokeapi.pokemon import fetchPokemonDataByIdentifier
from utils import print_pretty_json, isValidType
from scraper.scraper import BASE_BULBAPEDIA_WIKI_URL, BASE_POKEMON_DB_URL, scrape_page_builbapedia,scrape_page_pokedb

GYM_LEADERS : List[str] = [
  "Brock", "Misty", "Lt._Surge", "Erika", "Koga", "Janine", "Sabrina", "Blaine", "Giovanni", "Blue", # Indigo League
  "Falkner", "Bugsy", "Whitney", "Morty", "Chuck", "Jasmine", "Pryce", "Clair", # Johto League 
  "Roxanne", "Brawly", "Wattson", "Flannery", "Norman", "Winona", "Tate_and_Liza", "Wallace", "Juan", # Hoenn League
  "Roark", "Gardenia", "Maylene", "Crasher_Wake", "Fantina", "Byron", "Candice", "Volkner", # Sinnoh League
  "Cilan", "Chili", "Cress", "Lenora", "Burgh", "Elesa", "Clay", "Skyla", "Brycen", "Drayden", "Iris", # Unova League (Black and White)
  "Cheren", "Roxie", "Marlon", # Unova League (Black and White)
  "Viola", "Grant", "Korrina", "Ramos", "Clemont", "Valerie", "Olympia", "Wulfric", # Kalos League
  "Milo", "Nessa", "Kabu", "Bea", "Allister", "Opal", "Bede", "Gordie", "Melong", "Piers", "Marnie", "Raihan", # Galar League
  "Katy", "Brassius", "Iono", "Kofu", "Larry", "Ryme", "Tulip", "Grusha" # Paldea League
]

GEN_TO_REGION : dict[int, str] = {
  1: "Kanto",
  2: "Johto",
  3: "Hoenn",
  4: "Sinnoh",
  5: "Unova",
  6: "Kalos",
  7: "Alola", # HUGE REMINDER THIS REGION DOES NOT HAVE GYMS SO TREAT IT AS AN EDGE CASE
  8: "Galar", 
  9: "Paldea"
}

GEN_TO_GAME : dict[int, str] = {
  1: "red-blue",
  2: "gold-silver",
  3: "ruby-sapphire",
  4: "diamond-pearl",
  5: "black-white",
  6: "x-y",
  7: "sun-moon",
  8: "sword-shield",
  9: "scarlet-violet"
}

# THIS FUCTION SCRAPES THE GYM LEADERS IMG FROM THIS PAGE https://pokemondb.net/red-blue/gymleaders-elitefour
def fetchRandomGymLeader() -> GymLeaderData:
  # first get a random gym leader name and create the url string
  gym_leader_name : str = random.choice(GYM_LEADERS)
  url_string : str = f"{BASE_BULBAPEDIA_WIKI_URL}/{gym_leader_name}"
  
  # request this gymLeaders page
  gym_leader_page : SuccessResponse | ErrorResponse = scrape_page_builbapedia(url_string)
  
  response : GymLeaderData = {
    GymLeaderKeys.GYM_LEADER_NAME : gym_leader_name,
    GymLeaderKeys.GYM_LEADER_IMAGE_URL : ""
  }
  
  if not gym_leader_page[ErrorResponseKeys.SUCCESS]:
    print("Failed to get gym leader page")
    return response
  
  html = gym_leader_page[SuccessResponseKeys.DATA]
  
  soup = BeautifulSoup(html, "html.parser")
  
  content_div : Tag | None = soup.find("div", id="mw-content-text")
  
  if (not content_div):
    print("Failed to get contient div when fetching gym leader info")
    return response
  
  gym_leader_info_table : Tag | None = content_div.find("table", class_="roundy infobox")
  
  if (not content_div):
    print("Failed to get table div when fetching gym leader info")
    return response
  
  image_info : Tag | None = gym_leader_info_table.find("img")
  
  if (not image_info):
    print("Failed to get image from table when fetching gym leader info")
    return response
  
  response[GymLeaderKeys.GYM_LEADER_IMAGE_URL] = image_info["src"]
  
  return response

# THESE FUNCTIONS ARE USED TO SCRAP FROM https://pokemondb.net/red-blue/gymleaders-elitefour (this one fetches trainer img_url and pokemon info for the trainer input)
def fetchGymLeaderWithPokemon(leader : GymLeaderData | IslandKahunaData | IslandCaptainData, gen : int) -> GymLeaderData:
  
  # set it up with default values
  pokemon : list[PokemonData] = []
  leader[GymLeaderKeys.POKEMON] = pokemon # this has same value for all 3 types
  full_leader_name : str | None = None
  
  if GymLeaderKeys.GYM_LEADER_NAME in leader:
    full_leader_name = leader[GymLeaderKeys.GYM_LEADER_NAME]
    
  elif IslandKahunaKeys.ISLAND_KAHUNA_NAME in leader:
    full_leader_name = leader[IslandKahunaKeys.ISLAND_KAHUNA_NAME]
    
  elif IslandCaptainKeys.ISLAND_CAPTAIN_NAME in leader:
    full_leader_name = leader[IslandCaptainKeys.ISLAND_CAPTAIN_NAME]
  
  if (not full_leader_name or full_leader_name == ""):
    return leader
  
  game : str = GEN_TO_GAME[gen]
  sub_path : str = "gymleaders-elitefour" 
  
  if gen == 7:
    sub_path = "kahunas-elitefour"
  elif gen == 8:
    sub_path = "gymleaders"
     
  url : str = f"{BASE_POKEMON_DB_URL}/{game}/{sub_path}"
  
  # send the fetch
  gym_leader_page : SuccessResponse | ErrorResponse = scrape_page_pokedb(url) 
  
  if (not gym_leader_page[SuccessResponseKeys.SUCCESS]):
    print(f"Issue fetching gym leader page for url : {url}")
    return leader

  html = gym_leader_page[SuccessResponseKeys.DATA]
  soup = BeautifulSoup(html, "html.parser")
  
  print(f"PAGE FOUND FOR {full_leader_name} --------------------")
  print(f"{url}")
  
  # use gym leader name as a reference to find the img 
  img_tag = soup.find("img", {"alt": full_leader_name})
  
  if not img_tag:
    print(f"Could not find img tag with alt {full_leader_name}")
    return leader
  
  if GymLeaderKeys.GYM_LEADER_NAME in leader and full_leader_name == "Larry":
    leader[GymLeaderKeys.GYM_LEADER_IMAGE_URL] = img_tag.get("src")
    
  elif IslandKahunaKeys.ISLAND_KAHUNA_NAME in leader:
    leader[IslandKahunaKeys.ISLAND_KAHUNA_IMAGE_URL] = img_tag.get("src")
    
  elif IslandCaptainKeys.ISLAND_CAPTAIN_NAME in leader:
    leader[IslandCaptainKeys.ISLAND_CAPTAIN_IMAGE_URL] = img_tag.get("src")
  
  # pull out all the pokemon divs for this trainer
  pokemon_div_classes = ["infocard", "trainer-pkmn"]
  pokemon_divs  = []
  
  cur_div = img_tag.find_next("div")
  
  while (cur_div and (pokemon_div_classes == cur_div.get("class"))):
    pokemon_divs.append(cur_div)
    cur_div = cur_div.find_next("div")
  
  for div in pokemon_divs:
  
    pokemon_data : PokemonData = {
      PokemonKeys.NAME : "",
      PokemonKeys.IMAGE_URL : "",
      PokemonKeys.LEVEL : -1,
      PokemonKeys.TYPES : []
    }
    
    # img url 
    img_tag = div.find("img")
      
    # Name
    name_class : str = "ent-name"
    name_tag = div.find_next("a",  class_=name_class)
    
    if not name_tag:
      pokemon.append(pokemon_data)
      continue
    
    pokemon_name = name_tag.get_text(strip=True)

    # Fetch full Pokemon data
    pokemon_data = fetchPokemonDataByIdentifier(pokemon_name)
        
    if img_tag and not pokemon_data.get(PokemonKeys.IMAGE_URL):
      pokemon_data[PokemonKeys.NAME] = pokemon_name
      pokemon_data[PokemonKeys.IMAGE_URL] = img_tag.get("src")
    
    # level
    level_tag = name_tag.find_next("small")
    
    if not level_tag:
      pokemon.append(pokemon_data)
      continue
    
    # sometimes there is a form small which we want to skip
    if "Level" not in level_tag.get_text(strip=True):
      level_tag = level_tag.find_next("small")
      
    pokemon_data[PokemonKeys.LEVEL] = level_tag.get_text(strip=True)
    
    # types
    types_tag = level_tag.find_next("small")
    
    if not types_tag:
      pokemon.append(pokemon_data)
      continue
    
    types : list[PokemonType] = []
    
    for a_tag in types_tag.find_all("a"):
      type_string = a_tag.get_text(strip=True)
      
      if (isValidType(type_string)):
        types.append(PokemonType(type_string))
        
    pokemon_data[PokemonKeys.TYPES] = types
      
    pokemon.append(pokemon_data)
  
  return leader
