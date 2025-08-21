import { useEffect, useState } from 'react';
import { CardSize, InfoCard } from '../components/InfoCard';
import { SearchBar } from '../components/SearchBar';
import '../styles/general.css'
import { getRandomGymLeader, getRandomItem, getRandomPokemon, type GymLeaderData, type ItemData, type PokemonData } from '../api/pokemon_api';

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
        <InfoCard size={CardSize.small} title='Random Gym Leader' text={gymLeader?.name ?? "Unknown"} imageUrl={gymLeader?.imageUrl}/>
        <InfoCard size={CardSize.small} title='Random Item' text={item?.name ?? "Unkown"} imageUrl={item?.imageUrl}/>
      </div>
    </div>
  );
}