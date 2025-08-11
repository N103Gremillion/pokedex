import requests

from app_types import ErrorResponse, SuccessResponse

baseApiUrl : str = "https://pokeapi.co/api/v2/"

def fetchData(url: str) -> SuccessResponse | ErrorResponse:
  try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return {
      "success": True,
      "data": response.json()
    }
  except requests.HTTPError as error:
    return {
      "success": False,
      "error": str(error),
      "status_code": response.status_code,
      "details": None
    }
  
  except requests.RequestException as error:
    return {
      "success": False,
      "error": "Network error",
      "status_code": None,
      "details": str(error)
    }