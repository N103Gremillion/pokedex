import type { Generation, PokemonType, SearchPool } from "../enums";
import type { DetailedPokemonTypeData, GymLeaderData, ItemData, MoveData, PokedexData, PokemonData, PokemonRegionGymLeaders } from "../types";
import { getRandomItemId, getRandomPokemonId, NOT_FOUND_STATUS, SERVER_SIDE_ERROR_CUTOFF } from "./helpers";
import { Routes } from "./routes";

//  Search Bar 
export const getMatchingSearchPool = async (queryString : string) : Promise<SearchPool> => {
  queryString = queryString.replace(/ /g, "_")

  const url : string = `${Routes.SEARCH}/${queryString}`;
  const res : Response = await fetch(url);
  const json = await res.json();
  return json as SearchPool;
}

export const getMatchingSearchs = async (queryString : string) : Promise<string[]> => {
  const url : string = `${Routes.SEARCH}/match/${queryString}`;
  const res : Response = await fetch(url);
  const json = await res.json();
  return json;
}

// Pokemon **************************************************************** //
export const getRandomPokemon = async () : Promise<PokemonData> => {

  // try and get the data of a pokemon with a random id
  const randomId : number = getRandomPokemonId();
  const url : string = `${Routes.POKEMON}/${randomId}`;
  const res : Response = await fetch(url);

  if (res.status === NOT_FOUND_STATUS) throw new Error("Pokemon not found");
  if (res.status >= SERVER_SIDE_ERROR_CUTOFF) throw new Error("Sever error");

  const json = await res.json();

  return json as PokemonData;
}

export const getAllPokemonOfType = async (type : PokemonType) : Promise<PokemonData[]> => {
  const url : string = `${Routes.POKEMON}/type/${type}`;
  const res : Response = await fetch(url);
  const json = await res.json();
  console.log(`Fetching all pokemon of Type ${type}`);

  console.log(json);

  return json.pokemon;
}

export const getDetailedPokemonData = async (pokemonName : string) : Promise<PokemonData> => {
  const url : string = `${Routes.POKEMON}/detailed/${pokemonName}`;

  const res : Response = await fetch(url);
  const json = await res.json();

  return json as PokemonData;
}

// Items ************************************************************ //
export const getRandomItem = async () : Promise<ItemData> => {

  // try and get the data of a pokemon with a random id
  const randomId : number = getRandomItemId();
  const url : string = `${Routes.ITEM}/${randomId}`;
  const res : Response = await fetch(url);
  const json = await res.json();

  return {
    id: json.id,
    name: json.name,
    imageUrl: json.imageUrl
  };
}

export const getDetailedItemInfo = async(itemName : string) : Promise<ItemData> => {
  const url : string = `${Routes.ITEM}/detailed/${itemName}`;
  const res : Response = await fetch(url);
  const json = await res.json();

  return json as ItemData;
} 

// Pokedex ********************************************************* //
export const getPokedexInfo = async (generation : Generation) : Promise<PokedexData> => {
  console.log(`Fetching pokedex info for gen ${generation}`);

  const url : string = `${Routes.POKEDEX}/${generation}`;
  const res : Response = await fetch(url);
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
  const url : string = `${Routes.GYM_LEADER}/random`;
  const res : Response = await fetch(url);
  const json = await res.json();

  return {
    gym_leader_name : json.gym_leader_name,
    gym_leader_image_url : json.gym_leader_image_url
  };
}

export const getDetailedGymLeaderInfo = async (gymLeaderName : string) : Promise<GymLeaderData> => {
  const url : string = `${Routes.GYM_LEADER}/detailed/${gymLeaderName}`;
  const res : Response = await fetch(url);
  const json = await res.json();

  return json as GymLeaderData;
}

// PokemonRegionGymLeaders************************************//
export const getPokemonRegionGymLeaders = async (generation : Generation) : Promise<PokemonRegionGymLeaders> => {
  console.log(`fetching the gym leaders info for generatoin ${generation}.`);

  const url : string = `${Routes.GYM_LEADERS}/${generation}`;
  const res : Response = await fetch(url);
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

export const getDetailedMoveInfo = async (moveName : string) : Promise<MoveData> => {
  const url : string = `${Routes.MOVES}/detailed/${moveName}`;
  const res : Response = await fetch(url);
  const json = await res.json();

  console.log(json);

  return json as MoveData;
}