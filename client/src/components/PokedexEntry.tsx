import type { SyntheticEvent } from "react";
import type { PokemonData } from "../api/pokemon_api";
import { getTypeUrls } from "../utils";

interface PokedexEntryProps {
  pokemonData : PokemonData
}

export const PokedexEntry = ({pokemonData} : PokedexEntryProps) => {
  
  const defaultImageUrl : string = "/public/substitute.png";
  const typeImageUrls : string[] = getTypeUrls(pokemonData.types);
  
  // construct the handler for when the img doesn't load
  const handleImageNotFound = (event : SyntheticEvent<HTMLImageElement, Event>) => {
    const img = event.currentTarget;
    img.src = defaultImageUrl;
  }

  const pokemonImage = (
    <img
      src={pokemonData.imageUrl || defaultImageUrl}
      alt={"Pokemon"}
      className="pokedex-entry-img"
      onError= {(error) => handleImageNotFound(error)}
    />
  );

  return (
    <div style={{width:"150px", height:"150px"}}>
      <div className="pokedex-entry">
        {pokemonImage}
        <div className="pokedex-entry-types-container">
          {typeImageUrls.map((url, index) => (
            <img
              key={index}
              src={url}
              alt={`type-image`}
              className="pokedex-entry-type-image"
            />
          ))}
        </div>
        <div className="pokedex-entry-name">
          {pokemonData.name} <br/>
        </div>
        
      </div>
    </div>
  );
}