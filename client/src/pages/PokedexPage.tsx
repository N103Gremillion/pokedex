import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Generation, getGenerationFromString } from "../enums";
import { getPokedexInfo } from "../api/pokemon_api";
import { PokedexGrid } from "../components/pokedex/PokedexGrid";
import type { PokedexData } from "../types";

export const PokedexPage = () => {
  // pull of the genreatoin info from the url 
  const { generationString = "" } = useParams<{ generationString? : string }>();
  const [ loading, setLoading ] = useState<boolean>(false);
  const [ pokedexInfo, setPokedexInfo ] = useState<PokedexData>({gen_num : -1, pokemon : []});

  // request the pokedex info from the backend every time a different generation is selected
  useEffect(() => {
    const run = async () => {
      setLoading(true);
    
      // map the genrationString to the enum
      const generation : Generation = getGenerationFromString(generationString);
      
      // only make the fetch if the generatoin is not INVALID
      if (generation === Generation.INVALID) {
        setLoading(false)
        return
      }

      try {
        setPokedexInfo(await getPokedexInfo(generation));
      } catch (error) {
        console.log(`Issue getting pokedex info for gen : ${generation} | Error : ${error}`);
      } finally {
        setLoading(false);
      }
    };
    
    run();
  }, [generationString]);

  if (loading) { return <div className='loading-page'>Loading...</div>};
  
  return (
    <div className='general-page'>
      <h1 className='header'>Generation {pokedexInfo.gen_num} Pokedex</h1>
      <PokedexGrid pokedex={pokedexInfo}/> 
    </div>
  );
}