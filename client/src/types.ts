import type { PokemonDmgClass, PokemonType } from "./enums";

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

export type MoveData = {
  accuracy? : number;
  effect_chance? : number;
  pp? : number;
  priority? : number;
  power? : number;
  dmg_class? : PokemonDmgClass;
  effects? : string[];
  name? : string;
  type_name? : PokemonType;
}

export type DetailedPokemonTypeData = {
  type_name? : PokemonType;
  no_dmg_to? : PokemonType[];
  half_dmg_to? : PokemonType[];
  double_dmg_to? : PokemonType[];
  no_dmg_from? : PokemonType[];
  half_dmg_from? : PokemonType[];
  double_dmg_from? : PokemonType[];
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
  pokemon? : PokemonData[]
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
