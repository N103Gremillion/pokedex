import type { PokedexData, PokemonData } from "../api/pokemon_api";
import { PokedexEntry } from "./PokedexEntry";

interface PokedexGridProps {
  pokedex : PokedexData;
}

export const PokedexGrid = ({pokedex} : PokedexGridProps) => {

  return (
    <div className="pokedex-grid-container">
      {pokedex.pokemon?.map((pokemon : PokemonData) => (
        <PokedexEntry pokemonData={pokemon} />
      ))}
    </div>
  );
}