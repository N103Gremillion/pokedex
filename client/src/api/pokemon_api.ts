import type { Generation, PokemonType } from "../enums";
import type { DetailedPokemonTypeData, GymLeaderData, ItemData, MoveData, PokedexData, PokemonData, PokemonRegionGymLeaders } from "../types";
import { getRandomItemId, getRandomPokemonId, NOT_FOUND_STATUS, SERVER_SIDE_ERROR_CUTOFF } from "./helpers";
import { Routes } from "./routes";

export const getMatchingPlayers = async (queryString : string) : Promise<string[]> => {
  return [];
}

// Pokemon **************************************************************** //
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

export const getAllPokemonOfType = async (type : PokemonType) : Promise<PokemonData[]> => {
  const request_url : string = `${Routes.POKEMON}/type/${type}`;
  const res : Response = await fetch(request_url);
  const json = await res.json();
  console.log(`Fetching all pokemon of Type ${type}`);

  console.log(json);

  return json.pokemon;
}

// Items ************************************************************ //
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
export const getRandomGymLeader = async () : Promise<GymLeaderData> => {
  console.log("fetching a random gym leader.");

  // we have to generate the randomness of the gym leader on the backend since it is not part of the api we have to webscrape it
  const request_url : string = `${Routes.GYM_LEADER}/random`;
  const res : Response = await fetch(request_url);
  const json = await res.json();

  return {
    gym_leader_name : json.gym_leader_name,
    gym_leader_image_url : json.gym_leader_image_url
  };
}

// PokemonRegionGymLeaders************************************//
export const getPokemonRegionGymLeaders = async (generation : Generation) : Promise<PokemonRegionGymLeaders> => {
  console.log(`fetching the gym leaders info for generatoin ${generation}.`);

  const request_url : string = `${Routes.GYM_LEADERS}/${generation}`;
  const res : Response = await fetch(request_url);
  const json = await res.json();

  console.log(json);
  
  return {
    gen_num : json.gen_num,
    region : json.region,
    gym_leaders : json.gym_leaders,
    island_kahunas : json.island_kahunas,
    island_captains : json.island_captains
  }
}

// TypeInfo **************************************************//
export const getTypeInfo = async (type : PokemonType) : Promise<DetailedPokemonTypeData> => {
  const url : string = `${Routes.TYPE}/${type}`;
  const res : Response = await fetch(url);
  const json = await res.json();

  console.log(json);

  return {
    type_name : json.type_name,
    no_dmg_to : json.no_dmg_to,
    half_dmg_to : json.half_dmg_to,
    double_dmg_to : json.double_dmg_to,
    no_dmg_from : json.no_dmg_from,
    half_dmg_from : json.half_dmg_from,
    double_dmg_from : json.double_dmg_from
  };
}

// Moves
export const  getMovesOfType = async (type : PokemonType) : Promise<MoveData[]>  => {
  const url : string = `${Routes.MOVES}/${type}`;
  const res : Response = await fetch(url);
  const json = await res.json();
  
  return json as MoveData[];
}