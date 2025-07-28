import { Routes } from "./routes";

export type PlayerInfo = {
  id: string;
  gamerTag: string;
  rank?: number;       
  level?: number;     
  platform?: string;
  stats?: {
    kills: number;
    deaths: number;
    wins: number;
    losses: number;
  };
};

enum GetRequestsTypes {
  MATCHING_PLAYER = "/matching_player",
}

export const getMatchingPlayers = async (gamerTag : string) => {
  console.log("requesting gamer tag matches", gamerTag);
  const res  = await fetch(`${Routes.PLAYER}${GetRequestsTypes.MATCHING_PLAYER}`);
  return res.json();
};