import { InfoCard } from '../components/InfoCard';
import { SearchBar } from '../components/SearchBar';
import '../styles/general.css'

export const HomePage = () => {
  return (
    <div className='general-page'>
      <h1 className='header'>R6 SIEGE STATS</h1>
      <p className='raw-text'>check out global stats or search for player stats</p>
      <SearchBar/>
      <h2 className='header2'> General Stats </h2>
      <div className='horizontal-container'>
        <InfoCard/>
        <InfoCard/>
        <InfoCard/>
      </div>
    </div>
  );
}