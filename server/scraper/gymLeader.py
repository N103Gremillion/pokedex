import random
from typing import List
from bs4 import BeautifulSoup, Tag
from app_types import ErrorResponse, ErrorResponseKeys, GymLeaderData, GymLeaderKeys, PokemonRegionGymLeaders, PokemonRegionGymLeadersKeys, SuccessResponse, SuccessResponseKeys
from pokeapi.utils import print_pretty_json
from scraper.scraper import BASE_WIKI_URL, scrape_page


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

def fetchGymleadersByGeneration(gen_string : str) -> PokemonRegionGymLeaders:
  
  response : PokemonRegionGymLeaders = {
    PokemonRegionGymLeadersKeys.GEN_NUMBER : -1,
    PokemonRegionGymLeadersKeys.REGION : "undefined",
  }
  
  # try and cast the string to an int
  try:
    gen : int = int(gen_string)
  except ValueError as error:
    print(f"You must give a integer for the gen number. Error {error}.")
    return response
  
  # make sure gen is valid
  if (gen < 1 or gen > 9):
    print(f"Invalid Gen Number for Input {gen}. Must be between 1-9 inclusively.")
    return response
  
  # this is an edge case since it does not have gym leaders but a similar thing called island challenges
  if (gen == 7):
    print("This is the edge case")
    return response
  
  # fetch the inital page with all the generic info about the gym leaders
  general_gymleadrs_fetch_url : str = f"{BASE_WIKI_URL}/Gym"
  gymLeadersPage : SuccessResponse | ErrorResponse = scrape_page(general_gymleadrs_fetch_url)
  
  if not gymLeadersPage[ErrorResponseKeys.SUCCESS]:
    print("Failed to get gym leader page")
    return response

  html = gymLeadersPage[SuccessResponseKeys.DATA]
  soup = BeautifulSoup(html, "html.parser")
  
  region : str = GEN_TO_REGION[gen]
  response[PokemonRegionGymLeadersKeys.REGION] = region
  
  # get the tag with the id=region
  region_span = soup.find("span", id=region)
  
  if not region_span:
    print(f"Could not find the span with id {region}.")
    return response
  
  gymleaders_table = region_span.find_next("table")
  
  if not gymleaders_table:
    print(f"Could not find gymleaders table for the {region} region.")
    return response
  
  gym_leader_rows = gymleaders_table.find_all("tr")
  
  if not gym_leader_rows:
    print(f"Could not pull of rows from the table from the {region} region.")
    return response
  
  
  gym_leaders : list[GymLeaderData] = []
  i : int = 0
  
  # parse out the info from the table
  while (i < len(gym_leader_rows)):
    row = gym_leader_rows[i]
    cells = row.find_all("td") # pull out info about the gym leader from this row
    
    if not cells:
      i += 1
      continue
    
    total_cells = len(cells)
    
    if (total_cells != 5 and total_cells != 6):
      i += 1
      continue
    
    gym_data : GymLeaderData
    rowspan : int
    offset : int = 0
      
    # edge case (1 of these)
    if total_cells == 6:
      offset : int = 1
      
    gym_data, rowspan = parse_gym_row(cells, offset)
    
    i += 1
      
  return response

# this get the general cases in the tables (offset is used for the )
def parse_gym_row(cells : list[Tag], offset : int) -> tuple[GymLeaderData, int]:
  
  response : GymLeaderData = {}
  
  # badge info can only have 1 instance so we use this to determine if another cell has 2 entries 
  badge_cell = cells[2 + offset]
  badge_name = badge_cell.get_text(strip=True)
  badge_img = badge_cell.find("img")
  
  if badge_img:
    badge_img_url = badge_img.get("src") 
  else :
    badge_img_url = "" 
  
  print(f"Badge Name : {badge_name}")
  print(f"Badge Url : {badge_img_url}")
  
  response[GymLeaderKeys.BADGE_NAME] = badge_name
  response[GymLeaderKeys.BADGE_IMAGE_URL] = badge_img_url
  
  # check if there are more possible gym leader names, gym leader images, or gym types 
  rowspan = int(badge_cell.get("rowspan", 1))
  
  print(f"ROWSPAN : {rowspan}")
  print("------------------------------------------------")
  
  return (response, rowspan)

def fetchRandomGymLeader() -> GymLeaderData:
  # first get a random gym leader name and create the url string
  gym_leader_name : str = random.choice(GYM_LEADERS)
  url_string : str = f"{BASE_WIKI_URL}/{gym_leader_name}"
  
  # request this gymLeaders page
  gymLeaderPage : SuccessResponse | ErrorResponse = scrape_page(url_string)
  
  response : GymLeaderData = {
    GymLeaderKeys.GYM_LEADER_NAME : gym_leader_name,
    GymLeaderKeys.GYM_LEADER_IMAGE_URL : ""
  }
  
  if not gymLeaderPage[ErrorResponseKeys.SUCCESS]:
    print("Failed to get gym leader page")
    return response
  
  html = gymLeaderPage[SuccessResponseKeys.DATA]
  
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