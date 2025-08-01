import type { leaderboardPlayerData } from "../components/Leaderboard";
import { PlayerRegion } from "../generalEnums/PlayerRegion";
import { R6rank } from "../generalEnums/R6rank";
import { baseBackendURL, Routes } from "./routes";

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

enum ApiGetEndpoints {
  AVERAGE_KD = "/average_kd",
  MOST_PICKED_OPERATOR = "/most_picked_operator",
  MOST_PICKED_MAP = "/most_picked_map",
  MATCHING_PLAYER = "/matching_player",
}

// HOME PAGE STUFF ************************************* //
export const getAverageKD = async () : Promise<number> => {
  const response : Response  = await fetch(`${Routes.PLAYER}`);
  const data : number = 1;
  return data;
}

export const getMostPickedOperator = async () : Promise<string> => {
  return "Ash";
}

export const getMostPickedMap = async () : Promise<string> => {
  return "Clubhouse";
}

export const getMatchingPlayers = async (gamerTag : string) => {
  console.log("requesting gamer tag matches", gamerTag);
  const res  = await fetch(`${Routes.PLAYER}${ApiGetEndpoints.MATCHING_PLAYER}`);
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
    {
      name: "PCPlayer2",
      rank: R6rank.Champion,
      region: PlayerRegion.EU,
      level: 180,
      kd: 1.43,
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
    {
      name: "PCPlayer2",
      rank: R6rank.Champion,
      region: PlayerRegion.EU,
      level: 180,
      kd: 1.43,
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
    {
      name: "PCPlayer2",
      rank: R6rank.Champion,
      region: PlayerRegion.EU,
      level: 180,
      kd: 1.43,
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
    {
      name: "PCPlayer2",
      rank: R6rank.Champion,
      region: PlayerRegion.EU,
      level: 180,
      kd: 1.43,
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
    {
      name: "PCPlayer2",
      rank: R6rank.Champion,
      region: PlayerRegion.EU,
      level: 180,
      kd: 1.43,
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
    {
      name: "PCPlayer2",
      rank: R6rank.Champion,
      region: PlayerRegion.EU,
      level: 180,
      kd: 1.43,
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
    {
      name: "PCPlayer2",
      rank: R6rank.Champion,
      region: PlayerRegion.EU,
      level: 180,
      kd: 1.43,
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
    {
      name: "PCPlayer2",
      rank: R6rank.Champion,
      region: PlayerRegion.EU,
      level: 180,
      kd: 1.43,
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