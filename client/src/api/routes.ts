export const baseBackendURL = import.meta.env.VITE_BACKEND_URL || "http://localhost:5000";

enum ApiGetEndpoints {
  POKEMON = "/pokemon",
  ITEM = "/item",
  GYM_LEADER = "/gym-leader",
  GYM_LEADERS = "/gym-leaders",
  POKEDEX = "/pokedex",
  TYPE = "/type",
  MOVES = "/moves",
  SEARCH = "/search",
}

export const Routes = {
  POKEMON : `${baseBackendURL}${ApiGetEndpoints.POKEMON}`,
  ITEM : `${baseBackendURL}${ApiGetEndpoints.ITEM}`,
  GYM_LEADER : `${baseBackendURL}${ApiGetEndpoints.GYM_LEADER}`,
  GYM_LEADERS : `${baseBackendURL}${ApiGetEndpoints.GYM_LEADERS}`,
  POKEDEX : `${baseBackendURL}${ApiGetEndpoints.POKEDEX}`,
  TYPE : `${baseBackendURL}${ApiGetEndpoints.TYPE}`,
  MOVES : `${baseBackendURL}${ApiGetEndpoints.MOVES}`,
  SEARCH : `${baseBackendURL}${ApiGetEndpoints.SEARCH}`
} as const;
