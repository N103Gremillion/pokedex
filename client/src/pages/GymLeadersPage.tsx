import { useParams } from "react-router-dom";
import { Generation, getGenerationFromString } from "../enums";
import { useEffect, useState } from "react";
import { sleep } from "../utils";
import { getPokemonRegionGymLeaders } from "../api/pokemon_api";
import type { PokemonRegionGymLeaders } from "../types";
import { PokemonTrainerCard } from "../components/PokemonTrainerCard";

export const GymLeadersPage = () => {
  // pull of the genreatoin info from the url 
  const { generationString = "" } = useParams<{ generationString? : string }>();
  const [ loading, setLoading ] = useState<boolean>(false);
  const [ pokemonRegionInfo, setPokemonRegionInfo ] = useState<PokemonRegionGymLeaders>({ gen_num : -1, region : "undefined", gym_leaders : [], island_captains : [], island_kahunas : []});

  // request the gymLeaders info from the backend every time a different generation is selected
  useEffect(() => {
    console.log("hit page")
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
        setPokemonRegionInfo(await getPokemonRegionGymLeaders(generation));
      } catch (error) {
        console.log(`Issue getting pokemonRegionInfo for gen : ${generation} | Error : ${error}`);
      } finally {
        console.log(pokemonRegionInfo);
        setLoading(false);
      }
    };
    
    run();
  }, [generationString]);
  
  if (loading) { return <div className='loading-page'>Loading...</div>};

  return (
    <div className='general-page'>

      <h1 className='header'>{`Generation ${pokemonRegionInfo.gen_num} (${pokemonRegionInfo.region})`}</h1>
      <div className='gym-leaders-container'>
        {/* if this is any gen but 7 then it just has gym leaders  */}
        {pokemonRegionInfo.gen_num !== 7 && (
        <div>
          <h2 className='header'>Gym Leaders</h2>
          {pokemonRegionInfo.gym_leaders.map((gymLeaderInfo) => (
            <PokemonTrainerCard gymLeaderData={gymLeaderInfo}/>
          ))}
        </div>
      )}

        {/* if this is gen 7 then it has island captains and island kahunas instead of gym leaders */}
        {pokemonRegionInfo.gen_num === 7 && (
          <div>
            <h2 className='header'>Kahunas</h2>
            {pokemonRegionInfo.island_kahunas.map((islandKahunaInfo) => (
              <PokemonTrainerCard gymLeaderData={islandKahunaInfo}/>
            ))}
          </div>
        )}

        {pokemonRegionInfo.gen_num === 7 && (
          <div>
            <h2 className='header'>Captians</h2>
            {pokemonRegionInfo.island_captains.map((islandCaptainInfo) => (
              <PokemonTrainerCard gymLeaderData={islandCaptainInfo}/>
            ))}
          </div>
        )}

      </div>
    </div>
  );
}