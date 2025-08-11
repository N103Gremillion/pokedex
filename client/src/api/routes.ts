const backendPort : number = 5000;
export const baseBackendURL : string = `http://localhost:${backendPort}`;

enum ApiGetEndpoints {
  POKEMON = "/pokemon",
  ITEM = ""
}

export const Routes = {
  POKEMON : `${baseBackendURL}${ApiGetEndpoints.POKEMON}`,
} as const;
