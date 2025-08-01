const backendPort : number = 3000;
const baseBackendURL : string = `http://localhost:${backendPort}`;

export const Routes = {
  PLAYER: `${baseBackendURL}/player`,
  GENERAL_STATS: `${baseBackendURL}/general-stats`,
} as const;
