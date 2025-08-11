import { getRandomItemId, getRandomPokemonId, NOT_FOUND_STATUS, SERVER_SIDE_ERROR_CUTOFF } from "./helpers";
import { Routes } from "./routes";

export type PokemonData = {
  id? : number;
  name? : string;
  imageUrl? : string;
};

export type ItemData = {
  id? : number;
  name? : string;
  imageUrl? : string;
}

// HOME PAGE STUFF ************************************* //
export const getRandomPokemon = async () : Promise<PokemonData> => {
  console.log("fetching a random pokemon.");

  // try and get the data of a pokemon with a random id
  const randomId : number = getRandomPokemonId();
  const request_url : string = `${Routes.POKEMON}/${randomId}`;
  const res : Response = await fetch(request_url);

  if (res.status === NOT_FOUND_STATUS) throw new Error("Pokemon not found");
  if (res.status >= SERVER_SIDE_ERROR_CUTOFF) throw new Error("Sever error");

  const json = await res.json();

  return {
    id: json.id,
    name: json.name,
    imageUrl: json.imageUrl
  };
}

export const getRandomItem = async () : Promise<ItemData> => {
  console.log("fetching a random item.");

  // try and get the data of a pokemon with a random id
  const randomId : number = getRandomItemId();
  const request_url : string = `${Routes.POKEMON}/${randomId}`;
  const res : Response = await fetch(request_url);

  if (res.status === NOT_FOUND_STATUS) throw new Error("Pokemon not found");
  if (res.status >= SERVER_SIDE_ERROR_CUTOFF) throw new Error("Sever error");

  const json = await res.json();

  return {
    id: json.id,
    name: json.name,
    imageUrl: json.imageUrl
  };
}

export const getMostPickedOperator = async () : Promise<string> => {
  return "Ash";
}

export const getMostPickedMap = async () : Promise<string> => {
  return "Clubhouse";
}

export const getMatchingPlayers = async (gamerTag : string) => {
  console.log("requesting gamer tag matches", gamerTag);
  const res  = await fetch(``);
  return res.json();
};


