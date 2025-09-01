import { useEffect, useState } from 'react';
import { CardSize, InfoCard } from '../components/general/InfoCard';
import { SearchBar } from '../components/navigation/SearchBar';
import '../styles/general.css'
import { getRandomGymLeader, getRandomItem, getRandomPokemon } from '../api/pokemon_api';
import type { GymLeaderData, ItemData, PokemonData } from '../types';

export const HomePage = () => {

  const [pokemon, setPokemon] = useState<PokemonData | undefined>(undefined);
  const [gymLeader, setGymLeader] = useState<GymLeaderData | undefined>(undefined);
  const [item, setItem] = useState<ItemData | undefined>(undefined);

  // on mount fetch info from api
  useEffect(() => {
    const fetchData = async () : Promise<void> => {
      setPokemon(await getRandomPokemon()); 
      setItem(await getRandomItem());
      setGymLeader(await getRandomGymLeader());
    };

    fetchData();
  }, []);

  return (
    <div className='general-page'>
      <h1 className='header'>PokePluse</h1>
      <p className='raw-text'>Your gateway to Pokémon info and discoveries.</p>
      <SearchBar/>
      <h2 className='header2'> Random Picks for You</h2>
      <div className='horizontal-container'>
        <InfoCard size={CardSize.small} title="Random Pokemon" text={pokemon?.name ?? "Unknown"} imageUrl={pokemon?.imageUrl}/>
        <InfoCard size={CardSize.small} title='Random Gym Leader' text={gymLeader?.gym_leader_name ?? "Unknown"} imageUrl={gymLeader?.gym_leader_image_url}/>
        <InfoCard size={CardSize.small} title='Random Item' text={item?.name ?? "Unkown"} imageUrl={item?.imageUrl}/>
      </div>
    </div>
  );
}