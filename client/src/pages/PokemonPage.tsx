import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getDetailedPokemonData } from "../api/pokemon_api";
import type { PokemonData } from "../types";

export const  PokemonPage = () => {
  const { pokemonNameString = "" } = useParams<{ pokemonNameString? : string }>();
  const [detailedPokemonData, setDetailedPokemonData] = useState<PokemonData>({});

  useEffect(() => {
    const runQuery = async () => {
      setDetailedPokemonData(await getDetailedPokemonData(pokemonNameString));
    }
    runQuery();
  }, []);

  return (
    <div className='general-page'>
      <h1 className="header"> This is the Pokemon page </h1>
      <h2></h2>
    </div>
  );
}