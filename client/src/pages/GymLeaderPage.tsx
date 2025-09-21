import { useEffect, useState, type ReactNode, type SyntheticEvent } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { getDetailedGymLeaderInfo, getProxyUrl } from "../api/pokemon_api";
import type { GymLeaderData, PokemonData } from "../types";
import { PagePaths } from "./pagePaths";
import { getTypeUrl } from "../utils";
import "../styles/gym-leader-page.css"
import "../styles/trainer.css"

export const GymLeaderPage = () => {
  
  const defaultImageUrl : string = "/public/substitute.png";
  const { gymLeaderNameString = "" } = useParams<{ gymLeaderNameString? : string }>();
  const [detailedGymLeaderData, setDetailedGymLeaderData] = useState<GymLeaderData>({});
  const [loading, setLoading] = useState<boolean>(false);
  const navigate = useNavigate();
  
  useEffect(() => {
    setLoading(true);

    const runQuery = async () => {
      setDetailedGymLeaderData(await getDetailedGymLeaderInfo(gymLeaderNameString));
      setLoading(false);
      window.scrollTo(0, 0);
    }

    runQuery();
  }, []);

  const handleImageNotFound = (event : SyntheticEvent<HTMLImageElement, Event>) => {
    const img = event.currentTarget;
    img.src = defaultImageUrl;
  }

  const handleGymLeaderClick = () => {
    navigate(`${PagePaths.GymLeader}/${detailedGymLeaderData.gym_leader_name}`);
  }

  const handlePokemonClick = (pokemonName : string) => {
    navigate(`${PagePaths.Pokemon}/${pokemonName}`);
  }

  const GymLeaderImg = () : ReactNode => {
    return (
      <img 
        className="gym-leader-img"
        src={
          detailedGymLeaderData.gym_leader_image_url ?
          getProxyUrl(detailedGymLeaderData.gym_leader_image_url) : defaultImageUrl
        } 
        alt={detailedGymLeaderData.gym_name ?? "Unknown"}
        onError={handleImageNotFound}
      />
    );
  }

  console.log(detailedGymLeaderData);

  if (loading) { return <div className='loading-page'>Loading...</div>};

  return (
    <div className="general-page" style={{ display:"flex", flexDirection : "column", alignItems:"center"}}>
      {/* General gym leader info */}
      <div className="general-gym-leader-info-container" onClick={handleGymLeaderClick}>
        {GymLeaderImg()}

        <div style={{textAlign:"left", paddingLeft:"30px", fontSize:"25px"}}>
          <h1 className="gym-leader-header ">
            {detailedGymLeaderData.gym_leader_name ?? "Unknown Name"}
          </h1>
          {!detailedGymLeaderData.generation ? "Generation : Unknown" : `Generation : ${detailedGymLeaderData.generation}`} <br/>
          {!detailedGymLeaderData.gym_name  || detailedGymLeaderData.gym_name == "Unknown" ? "Gym Name : ----" : `Gym Location : ${detailedGymLeaderData.gym_name}`} <br/>
          {!detailedGymLeaderData.gym_number || detailedGymLeaderData.gym_number == -1 ? "Gym Number : ----" : `Gym Number : ${detailedGymLeaderData.gym_number}`} <br/>
          
        </div>
      </div>

      {/* Description */}
      <div className="gym-leader-description">
        {!detailedGymLeaderData.description ? `Description : There name is ${detailedGymLeaderData.gym_leader_name}` : `Description : ${detailedGymLeaderData.description}`}
      </div>

      {/* Pokemon */}
      <h1 className="gym-leader-header" style={{paddingTop:"20px"}}>Pokemon</h1>
      <div className="pokemon-container">
        {!detailedGymLeaderData.pokemon || detailedGymLeaderData.pokemon.length === 0 ? "Unknown" :
        detailedGymLeaderData.pokemon?.map((pokemon : PokemonData, index : number) => (
          <div key={index} className="pokemon-instance-container" onClick={() => handlePokemonClick(pokemon.name ?? "Undefined")}>
            <img src={pokemon.imageUrl} alt={pokemon.name ?? "Uknown"} onError={handleImageNotFound} className="trainer-card-pokemon-img"/>
            <p>{pokemon.name ?? "Unknown"}</p>
            <p>{pokemon.level ?? "-"}</p>
            {pokemon.types?.map((type, index) => (
              <img
                key={index}
                src={getTypeUrl(type) || defaultImageUrl}
                style={{ width: "50px", height: "20px" }}
                onError={(error) => handleImageNotFound(error)}
              />
            ))}
          </div>
        ))
        }
      </div>

    </div>
  );
}