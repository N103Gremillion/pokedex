const backendPort : number = 5000;
export const baseBackendURL : string = `http://localhost:${backendPort}`;

export const Routes = {
  PLAYER: `${baseBackendURL}/player`,
  GENERAL_STATS: `${baseBackendURL}/general-stats`,
} as const;
