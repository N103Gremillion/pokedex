
import type { PokedexData, PokemonData } from "../../types";
import { PokedexEntry } from "./PokedexEntry";

interface PokedexGridProps {
  pokedex : PokedexData;
}

export const PokedexGrid = ({pokedex} : PokedexGridProps) => {

  console.log(pokedex);
  
  return (
    <div className="pokedex-grid-container">
      {pokedex.pokemon?.map((pokemon : PokemonData) => (
        <PokedexEntry pokemonData={pokemon} />
      ))}
    </div>
  );
}