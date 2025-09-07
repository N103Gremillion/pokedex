import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getDetailedPokemonData } from "../api/pokemon_api";

export const  PokemonPage = () => {
  const { pokemonNameString = "" } = useParams<{ pokemonNameString? : string }>();
  const [detailedPokemonData, setDetailedPokemonData] = useState<string>("");

  useEffect(() => {
    const run = async () => {
      console.log("running the query");
      setDetailedPokemonData(pokemonNameString);
      await getDetailedPokemonData(pokemonNameString)
    }
    run();
  }, []);

  return (
    <div className='general-page'>
      <h1 className="header"> This is the Pokemon page </h1>
      <h2> {detailedPokemonData} </h2>
    </div>
  );
}