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
  
TODOS:
  Add caching of requested html pages for the trainer information also host images on firebase cuz some of them are having binding issues
"""
import threading
import time

from app_types import ErrorResponse, SuccessResponse
from pokeapi.general import fetchData

BASE_BULBAPEDIA_WIKI_URL : str = "https://bulbapedia.bulbagarden.net/wiki"
BASE_POKEMON_DB_URL : str = "https://pokemondb.net"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64; rv:116.0) "
        "Gecko/20100101 Firefox/116.0"
    )
}

last_builbapedia_scrape = 0
buildbapedia_lock = threading.Lock()

  
def scrape_page_builbapedia(url_string : str) -> SuccessResponse | ErrorResponse:
  global last_builbapedia_scrape
  
  with buildbapedia_lock:
    
    now = time.time()
    if now - last_builbapedia_scrape < 5:
      wait = 5 - (now - last_builbapedia_scrape)
      time.sleep(wait)
    last_builbapedia_scrape = time.time()

    # do the scraping
    response : SuccessResponse | ErrorResponse = fetchData(url_string, True)
    
    return response

last_pokedb_scrape = 0
pokedb_lock = threading.Lock()

def scrape_page_pokedb(url_string: str) -> 'SuccessResponse | ErrorResponse':
    global last_pokedb_scrape

    with pokedb_lock:
        now = time.time()
        if now - last_pokedb_scrape < 2:  # 2-second polite delay
            wait = 2 - (now - last_pokedb_scrape)
            time.sleep(wait)
        last_pokedb_scrape = time.time()

        # do the scraping
        response: 'SuccessResponse | ErrorResponse' = fetchData(url_string, True)
        return response