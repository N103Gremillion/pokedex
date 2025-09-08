import type { JSX, SyntheticEvent } from "react";
import type { GymLeaderData, IslandCaptainData, IslandKahunaData, PokemonData } from "../../types";
import { getTypeUrl } from "../../utils";
import "../../styles/trainer.css"
import { PagePaths } from "../../pages/pagePaths";
import { useNavigate } from 'react-router-dom';

interface PokemonTrainerCardProps {
  gymLeaderData : GymLeaderData | IslandCaptainData | IslandKahunaData;
}

export const PokemonTrainerCard = ({ gymLeaderData } : PokemonTrainerCardProps) => {

  let leaderContent: JSX.Element | null = null;
  const defaultImageUrl : string = "/default_img.png";
  const totalPokemon : number = gymLeaderData.pokemon?.length ?? 0;

  // construct the handler for when the image doesnt load
  const handleImageNotFound = (event : SyntheticEvent<HTMLImageElement, Event>) => {
    const img = event.currentTarget;
    img.src = defaultImageUrl;
  }

  const typeImage = (
    <img
      src={getTypeUrl(gymLeaderData.element_type) || defaultImageUrl} 
      alt="Player card"
      className="trainer-type-img"
      onError= {(error) => handleImageNotFound(error)}
    />
  );
  
  if ("gym_leader_name" in gymLeaderData) {
    
    const trainerImage = (
      <img 
        src={gymLeaderData.gym_leader_image_url || defaultImageUrl} 
        alt="Player card"
        className='trainer-card-trainer-img'
        onError= {(error) => handleImageNotFound(error)}
      />
    );

    const badgeImage = (
      <img
      src={gymLeaderData.badge_image_url || defaultImageUrl} 
      alt="Player card"
      className='badge-img'
      onError= {(error) => handleImageNotFound(error)}
      />
    );

    leaderContent = (
      <div className="gym-leader-card-component">
        {badgeImage}
        {trainerImage}
        <div>
          <div>
            <h3 className="gym-leader-name">{gymLeaderData.gym_leader_name}</h3>
          </div>
          <div>
            {`(${gymLeaderData.gym_name}) `}
          </div>
          <div>
            {typeImage}  
          </div>
        </div>
      </div>
    );
  }
  else if ("island_kahuna_name" in gymLeaderData) {

    const trainerImage = (
      <img 
        src={gymLeaderData.island_kahuna_image_url || defaultImageUrl} 
        alt="Player card"
        className='trainer-card-trainer-img'
        onError= {(error) => handleImageNotFound(error)}
      />
    );

    leaderContent = (
      <div className="gym-leader-card-component">
        {trainerImage}
        <div>
          <div>
            <h3 className="gym-leader-name">{gymLeaderData.island_kahuna_name}</h3>
          </div>
          <div>
            {`(${gymLeaderData.fight_location})`}
          </div>
          <div>
            {typeImage}
          </div>
        </div>
      </div>
    );
  }
  else if ("island_captain_name" in gymLeaderData) {

    const trainerImage = (
      <img 
        src={gymLeaderData.island_captain_image_url || defaultImageUrl} 
        alt="Player card"
        className='trainer-card-trainer-img'
        onError= {(error) => handleImageNotFound(error)}
      />
    );

    // setup the imgs for this componenent
    leaderContent = (
      <div className="gym-leader-card-component">
        {trainerImage}
        <div>
          <div>
            <h3 className="gym-leader-name">{gymLeaderData.island_captain_name}</h3>
          </div>
          <div>
            {typeImage}
          </div>
        </div>
      </div>
    );
  }
  
  return (
    <div className="horizontal-container">
      {leaderContent}
      <div className="trainers-pokemon-container">
        {/* layout there pokemon */}
        {gymLeaderData.pokemon?.map((pokemon) => (
          <div key={pokemon.name ?? Math.random()} className="trainers-pokemon">
            <img
              src={pokemon.imageUrl}
              alt={pokemon.name ?? "Pokemon image"}
              className="trainer-card-pokemon-img"
            />
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
        ))}
        {/* empty components */}
        {[...Array(6 - totalPokemon)].map(() => (
          <div className="trainers-pokemon-empty" />
        ))}
      </div>
    </div>
  );
}

