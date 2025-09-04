import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { validPokemonType } from "../utils";
import { getAllPokemonOfType, getMovesOfType, getTypeInfo } from "../api/pokemon_api";
import { PokemonType } from "../enums";

export const TypePage = () => {
  // pull of the type info from the url 
  const { typeString = "" } = useParams<{ typeString? : string }>();
  const [ loading, setLoading ] = useState<boolean>(false);

  useEffect (() => {
    const run = async () => {
      setLoading(true);
      
      if (!validPokemonType(typeString)){
        console.log(`Invalid type passed to TypePage. Type : ${typeString}`)
        return
      }
      
      // await getTypeInfo(typeString as PokemonType);
      await getMovesOfType(typeString as PokemonType);
      // await getAllPokemonOfType(typeString as PokemonType);
      
      setLoading(false);
    };

    run();
  }, [typeString]);
  
  if (loading) { return <div className='loading-page'>Loading...</div>};

  return (
    <div className='general-page'>

      <h1 className='header'>Type Page</h1>
      <p>This is the type page.</p>

    </div>
  );
}