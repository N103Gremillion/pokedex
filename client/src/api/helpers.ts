export const NOT_FOUND_STATUS = 404;
export const SERVER_SIDE_ERROR_CUTOFF = 500;
const MAX_POKEMON_ID = 1010;
const MAX_ITEM_ID = 500;

export function getRandomPokemonId() : number {
  return Math.floor(Math.random() * (MAX_POKEMON_ID) + 1);
}

export function getRandomItemId() : number {
  return Math.floor(Math.random() * (MAX_ITEM_ID) + 1);
}