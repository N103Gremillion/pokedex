import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { sleep, validPokemonType } from "../utils";

export const TypePage = () => {
  // pull of the type info from the url 
  const { typeString = "" } = useParams<{ typeString? : string }>();
  const [ loading, setLoading ] = useState<boolean>(false);

  useEffect (() => {
    const run = async () => {
      setLoading(true);
      
      await sleep(2);

      if (!validPokemonType(typeString)){
        console.log(`Invalid type passed to TypePage. Type : ${typeString}`)
        return
      }
      
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