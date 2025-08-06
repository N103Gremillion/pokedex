const backendPort : number = 5000;
export const baseBackendURL : string = `http://localhost:${backendPort}`;

enum ApiGetEndpoints {
  TOP_PC_PLAYERS = "/top_pc_players",
  TOP_CONSOLE_PLAYERS = "/top_console_players",
  MATCHING_PLAYERS = "/matching_player",
}

export const Routes = {
  TOP_PC_PLAYERS: `${baseBackendURL}${ApiGetEndpoints.TOP_PC_PLAYERS}`,
  TOP_CONSOLE_PLAYERS: `${baseBackendURL}${ApiGetEndpoints.TOP_CONSOLE_PLAYERS}`,
  MATCHING_PLAYERS: `${baseBackendURL}${ApiGetEndpoints.MATCHING_PLAYERS}`,
} as const;
