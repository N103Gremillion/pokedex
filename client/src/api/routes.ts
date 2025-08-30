const backendPort : number = 5000;
export const baseBackendURL : string = `http://localhost:${backendPort}`;

enum ApiGetEndpoints {
  POKEMON = "/pokemon",
  ITEM = "/item",
  GYM_LEADER = "/gym-leader",
  GYM_LEADERS = "/gym-leaders",
  POKEDEX = "/pokedex",
}

export const Routes = {
  POKEMON : `${baseBackendURL}${ApiGetEndpoints.POKEMON}`,
  ITEM : `${baseBackendURL}${ApiGetEndpoints.ITEM}`,
  GYM_LEADER : `${baseBackendURL}${ApiGetEndpoints.GYM_LEADER}`,
  GYM_LEADERS : `${baseBackendURL}${ApiGetEndpoints.GYM_LEADERS}`,
  POKEDEX : `${baseBackendURL}${ApiGetEndpoints.POKEDEX}`
} as const;
