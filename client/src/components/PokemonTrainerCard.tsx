import type { JSX, SyntheticEvent } from "react";
import type { GymLeaderData, IslandCaptainData, IslandKahunaData } from "../types";

interface PokemonTrainerCardProps {
  gymLeaderData : GymLeaderData | IslandCaptainData | IslandKahunaData;
}

export const PokemonTrainerCard = ({ gymLeaderData } : PokemonTrainerCardProps) => {

  let content: JSX.Element | null = null;
  const defaultImageUrl : string = "/public/default_img.png";

  // construct the handler for when the image doesnt load
  const handleImageNotFound = (event : SyntheticEvent<HTMLImageElement, Event>) => {
    const img = event.currentTarget;
    img.src = defaultImageUrl;
  }

  if ("gym_leader_name" in gymLeaderData) {

    // setup the imgs for this componenent
    content = (
      <div>
        {gymLeaderData.gym_leader_name}
      </div>
    );
  }
  else if ("island_kahuna_name" in gymLeaderData) {
    // setup the imgs for this componenent
    content = (
      <div>
        {gymLeaderData.island_kahuna_name}
      </div>
    );
  }
  else if ("island_captain_name" in gymLeaderData) {
    // setup the imgs for this componenent
    content = (
      <div>
        {gymLeaderData.island_captain_name}
      </div>
    );
  }

  return <div>{content}</div>;
}