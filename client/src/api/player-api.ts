import type { leaderboardPlayerData } from "../components/Leaderboard";
import { PlayerRegion } from "../generalEnums/PlayerRegion";
import { R6rank } from "../generalEnums/R6rank";
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

export const getTopPcPlayers = async () : Promise<leaderboardPlayerData[]> => {
  console.log("requestiong top 10 pc players");

  const playerData : leaderboardPlayerData[] = [
    {
      name: "PCPlayer1",
      rank: R6rank.Champion,
      region: PlayerRegion.NA,
      level: 200,
      kd: 1.75,
      profilePicUrl: "https://i.imgur.com/IqIa3vt.jpeg"
    },
    {
      name: "PCPlayer2",
      rank: R6rank.Champion,
      region: PlayerRegion.EU,
      level: 180,
      kd: 1.43,
      profilePicUrl: "https://i.imgur.com/IqIa3vt.jpeg"
    },
  ];

  return playerData;
}

export const getTopConsolePlayers = async () => {
  console.log("requestiong top 10 console players");

  const playerData : leaderboardPlayerData[] = [
    {
      name: "PCPlayer1",
      rank: R6rank.Champion,
      region: PlayerRegion.NA,
      level: 200,
      kd: 1.75,
      profilePicUrl: "https://i.imgur.com/IqIa3vt.jpeg"
    },
    {
      name: "PCPlayer2",
      rank: R6rank.Champion,
      region: PlayerRegion.EU,
      level: 180,
      kd: 1.43,
      profilePicUrl: "https://i.imgur.com/IqIa3vt.jpeg"
    },
  ];

  return playerData;
}