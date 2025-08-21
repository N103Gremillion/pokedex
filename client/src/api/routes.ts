const backendPort : number = 5000;
export const baseBackendURL : string = `http://localhost:${backendPort}`;

enum ApiGetEndpoints {
  POKEMON = "/pokemon",
  ITEM = "/item",
  GYM_LEADER = "/gym-leader",
}

export const Routes = {
  POKEMON : `${baseBackendURL}${ApiGetEndpoints.POKEMON}`,
  ITEM : `${baseBackendURL}${ApiGetEndpoints.ITEM}`,
  GYM_LEADER : `${baseBackendURL}${ApiGetEndpoints.GYM_LEADER}`
} as const;
