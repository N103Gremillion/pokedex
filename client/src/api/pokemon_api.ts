import type { Generation, PokemonType } from "../types";
import { getRandomItemId, getRandomPokemonId, NOT_FOUND_STATUS, SERVER_SIDE_ERROR_CUTOFF } from "./helpers";
import { Routes } from "./routes";

// General ****************************************************************** //
export const getMatchingPlayers = async (gamerTag : string) => {
  console.log("requesting gamer tag matches", gamerTag);
  const res  = await fetch(``);
  return res.json();
};

// Pokemon **************************************************************** //
export type PokemonData = {
  id? : number;
  name? : string;
  imageUrl? : string;
  types? : PokemonType[];
}

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
    imageUrl: json.imageUrl,
    types : json.types
  };
}

// Items ************************************************************ //
export type ItemData = {
  id? : number;
  name? : string;
  imageUrl? : string;
}

export const getRandomItem = async () : Promise<ItemData> => {
  console.log("fetching a random item.");

  // try and get the data of a pokemon with a random id
  const randomId : number = getRandomItemId();
  const request_url : string = `${Routes.ITEM}/${randomId}`;
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

// Pokedex ********************************************************* //
export type PokedexData = {
  gen_num? : number;
  pokemon? : PokemonData[]
}

export const getPokedexInfo = async (generation : Generation) : Promise<PokedexData> => {
  console.log(`Fetching pokedex info for gen ${generation}`);

  const request_url : string = `${Routes.POKEDEX}/${generation}`;
  const res : Response = await fetch(request_url);
  const json = await res.json();

  console.log(json);

  return {
    gen_num : json.gen_num,
    pokemon : json.pokemon
  };
}

// Gym Leaders ***************************************************** //
export type GymLeaderData = {
  id? : number;
  gym_name? : string;
  gym_leader_name? : string;
  gym_leader_image_url? : string;
  element_type? : PokemonType;
  badge_name? : string,
  badge_image_url? : string,
  pokemon? : PokedexData[]
}

export const getRandomGymLeader = async () : Promise<GymLeaderData> => {
  console.log("fetching a random gym leader.");

  // we have to generate the randomness of the gym leader on the backend since it is not part of the api we have to webscrape it
  const request_url : string = `${Routes.GYM_LEADER}/random`
  const res : Response = await fetch(request_url);
  const json = await res.json();

  console.log(json);

  return {
    gym_leader_name : json.gym_leader_name,
    gym_leader_image_url : json.gym_leader_image_url
  };
}



