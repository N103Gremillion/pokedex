import { CardSize, InfoCard } from '../components/InfoCard';
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
        <InfoCard size={CardSize.small} title='Average Global K/D' text='1.02' imageUrl='https://i.imgur.com/V6LaZum.jpeg'/>
        <InfoCard size={CardSize.small} title='Most Picked Operaoter' text='Ash' imageUrl='https://i.imgur.com/weCr7xl.jpeg'/>
        <InfoCard size={CardSize.small} title='Most Played Map' text='Clubhouse' imageUrl='https://i.imgur.com/mHlxzpf.jpeg'/>
      </div>
    </div>
  );
}