import type { PokedexData, PokemonData } from "../../types";
import { PokedexEntry } from "./PokedexEntry";
import "../../styles/pokedex.css";

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