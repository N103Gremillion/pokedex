import type { PokemonType } from "./enums";

export type PokemonData = {
  id? : number;
  name? : string;
  imageUrl? : string;
  types? : PokemonType[];
  level? : number;
}

export type ItemData = {
  id? : number;
  name? : string;
  imageUrl? : string;
}

export type PokedexData = {
  gen_num? : number;
  pokemon? : PokemonData[]
}

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

export type IslandKahunaData = {
  id? : number;
  fight_location? : string;
  island_kahuna_name? : string;
  island_kahuna_image_url? : string;
  element_type? : PokemonType;
  pokemon? : PokemonData[];
}

export type IslandCaptainData = {
  id? : number;
  island_captain_name? : string;
  island_captain_image_url? : string;
  element_type? : PokemonType;
  pokemon? : PokemonData[];
}

export type PokemonRegionGymLeaders = {
  gen_num : number;
  region : string;
  gym_leaders : GymLeaderData[];
  island_kahunas : IslandKahunaData[];
  island_captains : IslandCaptainData[];
}
