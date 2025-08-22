from typing import Optional
import requests

from app_types import ErrorResponse, ErrorResponseKeys, SuccessResponse, SuccessResponseKeys

baseApiUrl : str = "https://pokeapi.co/api/v2/"

def fetchData(url: str, fromScrapper : bool = False) -> SuccessResponse | ErrorResponse:
  try:
      
    response = requests.get(url, timeout=5)
    response.raise_for_status() # raise 4xx/ 5xx responses to be caught in execption below
    
    # you can just use json for the api
    if (not fromScrapper):
      return {
        SuccessResponseKeys.SUCCESS: True,
        SuccessResponseKeys.DATA: response.json()
      }
    # need to use response.text for the scrapper
    else :
      return {
        SuccessResponseKeys.SUCCESS: True,
        SuccessResponseKeys.DATA: response.text
      }
      
  # client error
  except requests.HTTPError as error:
    return {
      ErrorResponseKeys.SUCCESS: False,
      ErrorResponseKeys.ERROR: str(error),
      ErrorResponseKeys.STATUS_CODE: response.status_code,
      ErrorResponseKeys.DETAILS: None
    }
  
  except requests.RequestException as error:
    return {
      ErrorResponseKeys.SUCCESS: False,
      ErrorResponseKeys.ERROR: "Network error",
      ErrorResponseKeys.STATUS_CODE: None,
      ErrorResponseKeys.DETAILS: str(error)
    }