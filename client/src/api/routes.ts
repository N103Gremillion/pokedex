const backendPort : number = 3000;
const baseBackendURL : string = `http://localhost:${backendPort}`;

export const Routes = {
  PLAYER: `${baseBackendURL}/player`,
  PRO_TEAM: `${baseBackendURL}/proTeam`,
} as const;
