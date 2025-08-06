import { useEffect, useState } from 'react';
import { Footer } from '../components/Footer';
import { CardSize, InfoCard } from '../components/InfoCard';
import { Leaderboard, LeaderboardTypes } from '../components/Leaderboard';
import { SearchBar } from '../components/SearchBar';
import '../styles/general.css'
import { getMostPickedMap, getMostPickedOperator } from '../api/player-api';

export const HomePage = () => {

  const [averageKD, setAverageKD] = useState<number>(0);
  const [mostPickedOperator, setMostPickedOperator] = useState<string>("");
  const [mostPickedMap, setMostPickedMap] = useState<string>("");

  // on mount fetch info from api
  useEffect(() => {
    const fetchData = async () : Promise<void> => {
      setAverageKD(1);
      setMostPickedOperator(await getMostPickedOperator());
      setMostPickedMap(await getMostPickedMap());
    };

    fetchData();
  }, []);

  return (
    <div className='general-page'>
      <h1 className='header'>R6 SIEGE STATS</h1>
      <p className='raw-text'>check out global stats or search for player stats</p>
      <SearchBar/>
      <h2 className='header2'> General Stats </h2>
      <div className='horizontal-container'>
        <InfoCard size={CardSize.small} title='Average Global K/D' text={averageKD.toString()} imageUrl='https://i.imgur.com/V6LaZum.jpeg'/>
        <InfoCard size={CardSize.small} title='Most Picked Operaoter' text={mostPickedOperator} imageUrl='https://i.imgur.com/weCr7xl.jpeg'/>
        <InfoCard size={CardSize.small} title='Most Played Map' text={mostPickedMap} imageUrl='https://i.imgur.com/mHlxzpf.jpeg'/>
      </div>
      <div className='horizontal-container'>
        <Leaderboard platformType={LeaderboardTypes.Pc}/>
        <Leaderboard platformType={LeaderboardTypes.Console}/>
      </div>
    </div>
  );
}