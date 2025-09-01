import copy
from bs4 import BeautifulSoup, Tag
from app_types import ErrorResponse, ErrorResponseKeys, GymLeaderData, GymLeaderKeys, IslandCaptainKeys, IslandKahunaKeys, PokemonData, PokemonRegionGymLeaders, PokemonRegionGymLeadersKeys, SuccessResponse, SuccessResponseKeys
from mongo.db_utils import DatabaseCollections
from scraper.gymLeaderPageScrapper import GEN_TO_REGION, fetchGymLeaderWithPokemon
from utils import print_pretty_json, isValidType
from scraper.scraper import BASE_BULBAPEDIA_WIKI_URL, scrape_page_builbapedia
from scraper.gen7data import GEN_7_ISLAND_CAPTAINS, GEN_7_ISLAND_KAHUNAS
from pymongo.collection import Collection

####################### THESE ARE SPECIFIC TO THIS PAGE https://bulbapedia.bulbagarden.net/wiki/Gym ##########################################
def fetchGymLeadersByGeneration(gen_string : str) -> PokemonRegionGymLeaders:
  from entry import globalDb
  
  response : PokemonRegionGymLeaders = {
    PokemonRegionGymLeadersKeys.GEN_NUMBER : -1,
    PokemonRegionGymLeadersKeys.REGION : "undefined",
    PokemonRegionGymLeadersKeys.GYM_LEADERS : [],
    PokemonRegionGymLeadersKeys.ISLAND_KAHUNAS : [],
    PokemonRegionGymLeadersKeys.ISLAND_CAPTAINS : []
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
  
  # check if it is already cached in the database
  pokemonRegionCollection : Collection = globalDb[DatabaseCollections.POKEMON_REGION_GYM_LEADERS.value.name]
  
  cachedDoc = pokemonRegionCollection.find_one({DatabaseCollections.POKEMON_REGION_GYM_LEADERS.value.key: gen})
  
  if (cachedDoc):
    return { 
      PokemonRegionGymLeadersKeys.GEN_NUMBER : cachedDoc[PokemonRegionGymLeadersKeys.GEN_NUMBER], 
      PokemonRegionGymLeadersKeys.REGION : cachedDoc[PokemonRegionGymLeadersKeys.REGION],
      PokemonRegionGymLeadersKeys.GYM_LEADERS : cachedDoc[PokemonRegionGymLeadersKeys.GYM_LEADERS],
      PokemonRegionGymLeadersKeys.ISLAND_KAHUNAS : cachedDoc[PokemonRegionGymLeadersKeys.ISLAND_KAHUNAS],
      PokemonRegionGymLeadersKeys.ISLAND_CAPTAINS : cachedDoc[PokemonRegionGymLeadersKeys.ISLAND_CAPTAINS]
    }
  
  region : str = GEN_TO_REGION[gen]
  response[PokemonRegionGymLeadersKeys.REGION] = region
  response[PokemonRegionGymLeadersKeys.GEN_NUMBER] = gen
  
  # this is an edge case since it does not have gym leaders but a similar thing called island challenges
  if (gen == 7):
    # print("Gen 7 edge case")
    response[PokemonRegionGymLeadersKeys.ISLAND_KAHUNAS] = GEN_7_ISLAND_KAHUNAS
    response[PokemonRegionGymLeadersKeys.ISLAND_CAPTAINS] = GEN_7_ISLAND_CAPTAINS
    
    for kahuna in response[PokemonRegionGymLeadersKeys.ISLAND_KAHUNAS]:
      # print(f"SCRAPING FOR THE KAHUNA {kahuna[IslandKahunaKeys.ISLAND_KAHUNA_NAME]}.")
      leader_pokemon = fetchGymLeaderWithPokemon(kahuna, gen)
      
    for captain in response[PokemonRegionGymLeadersKeys.ISLAND_CAPTAINS]:
      # print(f"SCRAPING FOR THE CAPTAIN {captain[IslandCaptainKeys.ISLAND_CAPTAIN_NAME]}.")
      leader_pokemon = fetchGymLeaderWithPokemon(captain, gen)
      
    return response
  
  # fetch the inital page with all the generic info about the gym leaders
  url : str = f"{BASE_BULBAPEDIA_WIKI_URL}/Gym"
  gym_leaders_page : SuccessResponse | ErrorResponse = scrape_page_builbapedia(url)
  
  if not gym_leaders_page[ErrorResponseKeys.SUCCESS]:
    print("Failed to get gym leader page")
    return response

  html = gym_leaders_page[SuccessResponseKeys.DATA]
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
  
  # remove invalid trainers some trainers in the tables are fromn like spinoffs of this gen
  gym_leaders = removeInvalidTrainersByGen(gym_leaders, gen)
  
  # take off the extra info from the names since we need cleaned up names for later fetching
  for leader in gym_leaders:
    leader[GymLeaderKeys.GYM_LEADER_NAME] = trimGymLeaderName(leader[GymLeaderKeys.GYM_LEADER_NAME])
    
  # iterate over each trainer and scrap the info about there pokemon 
  for leader in gym_leaders:
    print(f"SCRAPING FOR {leader[GymLeaderKeys.GYM_LEADER_NAME]}")
    leader_pokemon = fetchGymLeaderWithPokemon(leader, gen)
    
  response[PokemonRegionGymLeadersKeys.GYM_LEADERS] = gym_leaders
  
  # add to cache pages to prevent unecessary fetches in the future
  pokemonRegionCollection.insert_one({
    DatabaseCollections.POKEMON_REGION_GYM_LEADERS.value.key: gen,
    PokemonRegionGymLeadersKeys.REGION : response[PokemonRegionGymLeadersKeys.REGION],
    PokemonRegionGymLeadersKeys.GYM_LEADERS : response[PokemonRegionGymLeadersKeys.GYM_LEADERS],
    PokemonRegionGymLeadersKeys.ISLAND_KAHUNAS : response[PokemonRegionGymLeadersKeys.ISLAND_KAHUNAS],
    PokemonRegionGymLeadersKeys.ISLAND_CAPTAINS : response[PokemonRegionGymLeadersKeys.ISLAND_CAPTAINS]
  })
  
  return response

def trimGymLeaderName(full_gym_leader_name : str) -> str:
  
  # this is an edge case
  if (full_gym_leader_name == "Tate and Liza"):
    return "Tate & Liza"
  
  n : int = len(full_gym_leader_name)
  res : str = ""
  
  for i in range(n):
    char : str = full_gym_leader_name[i]
    
    if(char == "(" or (char == "R" and i != 0)):
      break
    
    res += char
  
  return res
  
def removeInvalidTrainersByGen(gym_leaders : list[GymLeaderData], gen : int) -> list[GymLeaderData]:
  # remove any invalid trainers (depends on the generation)
  if (gen == 1):
    if (len(gym_leaders) >= 6):
      gym_leaders.pop(5) # this is Janine she is in the remakes 
    if (len(gym_leaders) > 0):
      gym_leaders.pop() # this is Blue he is not a gym leader he is in the elite 4
      
  elif (gen == 3):
    if (len(gym_leaders) > 0):
      gym_leaders.pop() # this is Juan he is in emerald we are doing ruby/saphier
      
  elif (gen == 5):
    if (len(gym_leaders) >= 5):
      gym_leaders.pop(4) # this is Cheren she is in Black and White 2 we are doing Black and White
      
    if (len(gym_leaders) >= 5):
      gym_leaders.pop(4) # this is Roxi she is also in Black and White 2
    
    if (len(gym_leaders) > 0):
      gym_leaders.pop() # this is Marlon he is in Black and White 2
  
  elif (gen == 8):
    if (len(gym_leaders) >= 7):
      gym_leaders.pop(6) # this is Bede he is not a gym leader

    if (len(gym_leaders) >= 10):
      gym_leaders.pop(9) # this is Marnie she is not a gym leader
      
  return gym_leaders

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