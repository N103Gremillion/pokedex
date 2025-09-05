import type { SyntheticEvent } from "react";
import { getTypeUrls } from "../../utils";
import { useNavigate } from 'react-router-dom';
import { PagePaths } from "../../pages/pagePaths";
import type { PokemonData } from "../../types";
import "../../styles/pokedex.css";

interface PokedexEntryProps {
  pokemonData : PokemonData
}

export const PokedexEntry = ({pokemonData} : PokedexEntryProps) => {
  
  const defaultImageUrl : string = "/public/substitute.png";
  const typeImageUrls : string[] = getTypeUrls(pokemonData.types);
  const navigate = useNavigate();

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

  const handleClick = (event : React.MouseEvent) : void => {
    const pokemonNameString : string = pokemonData.name ?? "undefined";
    navigate(`${PagePaths.Pokemon}/${pokemonNameString}`);
  }

  return (
    <div className="pokedex-entry" onClick={(event) => handleClick(event)}>
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
  );
}