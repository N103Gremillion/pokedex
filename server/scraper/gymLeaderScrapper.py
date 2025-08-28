import random
import copy
from typing import List
from bs4 import BeautifulSoup, Tag
from app_types import ErrorResponse, ErrorResponseKeys, GymLeaderData, GymLeaderKeys, PokemonData, PokemonRegionGymLeaders, PokemonRegionGymLeadersKeys, SuccessResponse, SuccessResponseKeys
from utils import print_pretty_json, isValidType
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

def fetchRandomGymLeader() -> GymLeaderData:
  # first get a random gym leader name and create the url string
  gym_leader_name : str = random.choice(GYM_LEADERS)
  url_string : str = f"{BASE_WIKI_URL}/{gym_leader_name}"
  
  # request this gymLeaders page
  gym_leader_page : SuccessResponse | ErrorResponse = scrape_page(url_string)
  
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

####################### THESE ARE SPECIFIC TO THIS PAGE https://bulbapedia.bulbagarden.net/wiki/Gym ##########################################
def fetchGymLeadersByGeneration(gen_string : str) -> PokemonRegionGymLeaders:
  response : PokemonRegionGymLeaders = {
    PokemonRegionGymLeadersKeys.GEN_NUMBER : -1,
    PokemonRegionGymLeadersKeys.REGION : "undefined",
    PokemonRegionGymLeadersKeys.GYM_LEADERS : [],
    PokemonRegionGymLeadersKeys.ISLAND_LEADERS : []
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
  
  region : str = GEN_TO_REGION[gen]
  response[PokemonRegionGymLeadersKeys.REGION] = region
  response[PokemonRegionGymLeadersKeys.GEN_NUMBER] = gen
  
  # this is an edge case since it does not have gym leaders but a similar thing called island challenges
  if (gen == 7):
    print("This is the edge case")
    return response
  
  # fetch the inital page with all the generic info about the gym leaders
  url : str = f"{BASE_WIKI_URL}/Gym"
  gymLeadersPage : SuccessResponse | ErrorResponse = scrape_page(url)
  
  if not gymLeadersPage[ErrorResponseKeys.SUCCESS]:
    print("Failed to get gym leader page")
    return response

  html = gymLeadersPage[SuccessResponseKeys.DATA]
  soup = BeautifulSoup(html, "html.parser")
  
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
      
    gym_data, rowspan = parseGymRow(cells, offset)
    
    # go ahead and add the inital data to the gymLeaders
    gym_leaders.append(gym_data)
    
    if (rowspan > 1):
      
      # if the cells span multiple rows we now there is at least rowspan number of gym leaders so we need to copy over the previous cells and check to see the ones that have changed
      while (rowspan > 1):
        
        # pull off the next row since it should have some addational info 
        i += 1
        
        if (i >= len(gym_leader_rows)):
          rowspan -= 1
          continue
        
        next_row = gym_leader_rows[i]
        next_cells = next_row.find_all("td")
        
        if not cells:
          rowspan -= 1
          continue
          
        gym_data_copy = parseGymRowCopy(gym_data, next_cells)
        gym_leaders.append(gym_data_copy)
        
        rowspan -= 1
    
    i += 1
  
  # iterate over each trainer and scrap the info about there pokemon 
  for leader in gym_leaders:
    print(f"SCRAPING FOR {leader[GymLeaderKeys.GYM_LEADER_NAME]}")
    leader_pokemon = fetchGymLeaderWithPokemon(leader)
    
  response[PokemonRegionGymLeadersKeys.GYM_LEADERS] = gym_leaders
  
  return response

# this handle the case where a col spans multiple rows and some extra info can be pull off
def parseGymRowCopy(gym_data : GymLeaderData, cells : list[Tag]) -> GymLeaderData:
  count : int = 0
  gym_data_copy : GymLeaderData = copy.deepcopy(gym_data)
  
  for cell in cells:
    text : str = cell.get_text(strip=True)
    img = cell.find("img")
    
    # check if the cell contains a type (identify by if if contains text that appear in or enum)
    if (isValidType(text)): # Type name
      gym_data_copy[GymLeaderKeys.TYPE] = text
  
    # at this point we know it is not a type and if it has an img it has to be gym trainer info
    elif (img and text != "1"): # Gym Tainer info
      gym_data_copy[GymLeaderKeys.GYM_LEADER_NAME] = text
      gym_leader_img_url = img.get("src")
      
      gym_data_copy[GymLeaderKeys.GYM_LEADER_IMAGE_URL] = gym_leader_img_url
      
    # at this point if the text isnt null it is the gym name there are also some other checks you will have to look at the table for Unova make this make sense
    elif (text != "" and text[len(text) - 1] == "m"): # Gym Name
      print(text)
      gym_data_copy[GymLeaderKeys.GYM_NAME] = text
      
    count += 1
    
  return gym_data_copy
  
def parseGymRow(cells : list[Tag], offset : int) -> tuple[GymLeaderData, int]:
  
  response : GymLeaderData = {}
  
  # badge info can only have 1 instance so we use this to determine if another cell has 2 entries 
  gym_name = cells[1 + offset].get_text(strip=True)
  badge_cell = cells[2 + offset]
  badge_name = badge_cell.get_text(strip=True)
  badge_img = badge_cell.find("img")
  gym_type = cells[3 + offset].get_text(strip=True) 
  gym_leader_cell = cells[4 + offset]
  gym_leader_name = gym_leader_cell.get_text(strip=True)
  gym_leader_img = gym_leader_cell.find("img")
  
  if badge_img:
    badge_img_url = badge_img.get("src") 
  else :
    badge_img_url = "" 
  
  if gym_leader_img:
    gym_leader_img_url = gym_leader_img.get("src")
  else:
    gym_leader_img_url = ""
    
  response[GymLeaderKeys.GYM_NAME] = gym_name
  response[GymLeaderKeys.BADGE_NAME] = badge_name
  response[GymLeaderKeys.BADGE_IMAGE_URL] = badge_img_url
  response[GymLeaderKeys.GYM_LEADER_NAME] = gym_leader_name
  response[GymLeaderKeys.GYM_LEADER_IMAGE_URL] = gym_leader_img_url
  
  if (isValidType(gym_type)):
    response[GymLeaderKeys.TYPE] = gym_type
  
  
  # check if there are more possible gym leader names, gym leader images, or gym types 
  rowspan = int(badge_cell.get("rowspan", 1))
  
  return (response, rowspan)
################################################################################################################################
# this pulls off the image url and the pokemon information from the page
# These are use to scrap the trainer pages something like this https://bulbapedia.bulbagarden.net/wiki/Falkner ###################
def fetchGymLeaderWithPokemon(leader : GymLeaderData) -> GymLeaderData:
  # set it up with default values
  pokemon : list[PokemonData] = []
  leader[GymLeaderKeys.POKEMON] = pokemon
  full_leader_name : str | None = leader[GymLeaderKeys.GYM_LEADER_NAME]
  
  if (not full_leader_name or full_leader_name == ""):
    return leader
    
  leader_first_name : str = getGymLeaderUrlName(full_leader_name)
  url : str = f"{BASE_WIKI_URL}/{leader_first_name}"
  gym_leader_page : SuccessResponse | ErrorResponse = scrape_page(url)
  
  print(url)
  
  if not gym_leader_page[ErrorResponseKeys.SUCCESS]:
    print("Failed to get gym leader page")
    return leader
  
  html = gym_leader_page[SuccessResponseKeys.DATA]
  soup = BeautifulSoup(html, "html.parser")
  
  header_id : str = "Pokémon"
  
  if (leader_first_name == "Larry"):
    header_id = "Pokémon_2"
    
  # the header id is different for a few of the gym leaders
  pokemon_span = soup.find("span", id=header_id) # get span with the heading pokemon this is where his pokemon info is
  
  if not pokemon_span:
    print(f"Could not pull of the span with to Pokemon Id for {leader_first_name}.")
    return leader
  
  pokemon_header = pokemon_span.find_parent("h3")
  
  if not pokemon_header:
    print(f"Could not pull of the header with to Pokemon Id for {leader_first_name}.")
    return leader
  
  gym_name : str = leader[GymLeaderKeys.GYM_NAME] # search for the table that has a string matching the name of the gym
  
  if (gym_name == "Spikemuth Gym"): # this is an edge case the name on the page we are parsing is slightly different
    gym_name = "Spikemuth"
    
  gym_leader_table = None
  
  for table in pokemon_header.find_all_next("table"):
    if (table.find("a", title=gym_name)):
      gym_leader_table = table
      break
  
  if not gym_leader_table:
    print(f"Could not find the gym leader table for {leader_first_name}")
    return leader
  
  img = gym_leader_table.find_next("img") # first we will get the gym leader img 
  
  if not img:
    print(f"Could not pull of the gym leader img for {leader_first_name}.")
    return leader
  
  # at this point switch out the previous img_url with this new one (these ones have better imgs)
  leader[GymLeaderKeys.GYM_LEADER_IMAGE_URL] = img.get("src")
  
  imgs = []
  img = img.find_next("img")
  
  while img:
    imgs.append(img)
    next_img = img.find_next("img")
    
    if not next_img or gym_leader_table not in next_img.find_parents("table"):
      break
    
    img = next_img
  
  valid_imgs = imgs[6:]
  
  for img in valid_imgs:
    print(img.get("src"))
  
  return leader

def getGymLeaderUrlName(full_leader_name : str):
  
  if full_leader_name == "Lt. Surge":
    return "Lt._Surge"
  elif full_leader_name == "Tate and Liza":
    return "Tate_and_Liza"
  elif full_leader_name == "Crasher Wake":
    return "Crasher_Wake"
  
  # pull off the 1 portion of the names for gym leader since this is what url uses
  n : int = len(full_leader_name)
  leader_first_name_list : list[str] = []
  
  for i in range(n):
    char : str = full_leader_name[i]
    
    if (char == " " or char == "(" or (i != 0 and char == "R") or (i != 0 and char == "E")):
      break
    
    leader_first_name_list.append(char)
  
  url_name : str = "".join(leader_first_name_list)
  
  if (url_name == "Blue"):
    url_name ="Blue_(game)"
  
  return url_name

###################################################################################################################################