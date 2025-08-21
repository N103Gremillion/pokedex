# wiki scrapping rules so they dont block my ip
"""
rules_referenced_from : https://bulbapedia.bulbagarden.net/robots.txt
1.) 5 seconds between requests
2.) 
  Disallowed_Endpoints:
    Disallow: /wiki/Special:Search
    Disallow: /wiki/Special%3ASearch
    Disallow: /wiki/Special:Randompage
    Disallow: /wiki/Special%3ARandompage
    Disallow: /wiki/Shipping:
    Disallow: /wiki/Shipping%3A

use these to discover pages :     
  https://bulbapedia.bulbagarden.net/w/index.php?title=Special:NewPages&feed=atom
  https://bulbapedia.bulbagarden.net/w/sitemap/sitemap-index-bulbapedia.xml
  
Note:
  I am using this because some information is not openly availble on the pokeapi.
"""
import random
import threading
from typing import List
from flask import Response
import requests
import time
from bs4 import BeautifulSoup
from bs4.element import Tag

from app_types import ErrorResponse, GymLeaderData, SuccessResponse
from pokeapi.general import fetchData

BASE_WIKI_URL : str = "https://bulbapedia.bulbagarden.net/wiki"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64; rv:116.0) "
        "Gecko/20100101 Firefox/116.0"
    )
}


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

last_scrape = 0
lock = threading.Lock()

def fetchRandomGymLeader() -> GymLeaderData:
  # first get a random gym leader name and create the url string
  gymLeaderName : str = random.choice(GYM_LEADERS)
  url_string : str = f"{BASE_WIKI_URL}/{gymLeaderName}"
  
  # request this gymLeaders page
  gymLeaderPage : SuccessResponse | ErrorResponse = scrape_page(url_string)
  
  default_response : GymLeaderData = {
    "name": gymLeaderName,
    "imageUrl": ""
  }
  
  if not gymLeaderPage["success"]:
    print("Failed to get gym leader page")
    return default_response
  
  html = gymLeaderPage["data"]
  
  soup = BeautifulSoup(html, "html.parser")
  
  content_div : Tag | None = soup.find("div", id="mw-content-text")
  
  if (not content_div):
    print("Failed to get contient div when fetching gym leader info")
    return default_response
  
  gym_leader_info_table : Tag | None = content_div.find("table", class_="roundy infobox")
  
  if (not content_div):
    print("Failed to get table div when fetching gym leader info")
    return default_response
  
  image_info : Tag | None = gym_leader_info_table.find("img")
  
  if (not image_info):
    print("Failed to get image from table when fetching gym leader info")
    return default_response
  
  return {
    "name": gymLeaderName,
    "imageUrl": image_info["src"]
  }
  
def scrape_page(url_string : str) -> SuccessResponse | ErrorResponse:
  global last_scrape
  
  with lock:
    
    now = time.time()
    if now - last_scrape < 5:
      wait = 5 - (now - last_scrape)
      time.sleep(wait)
    last_scrape = time.time()

    # do the scraping
    response : SuccessResponse | ErrorResponse = fetchData(url_string, True)
    
    return response