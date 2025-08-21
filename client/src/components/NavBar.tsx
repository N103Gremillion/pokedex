import { Toolbar } from 'primereact/toolbar';
import { NavBarDropdown } from './NavBarDropdown';
import '../styles/general.css';
import { HomeButton } from './HomeButton';
import { PagePaths } from '../pages/pagePaths';

export const NavBar = () => {
  
  const pokedexDropdownLabel : string = "Pokedex";
  const gymLeaderDropdownLabel : string = "Gym Leader";
  const typeDropdownLabel : string = "Type";

  const pokemonGenerations: string[] = [
    "Generation I",
    "Generation II",
    "Generation III",
    "Generation IV",
    "Generation V",
    "Generation VI",
    "Generation VII",
    "Generation VIII",
    "Generation IX"
  ];

  const pokemonTypes: string[] = [
    "Normal",
    "Fire",
    "Water",
    "Electric",
    "Grass",
    "Ice",
    "Fighting",
    "Poison",
    "Ground",
    "Flying",
    "Psychic",
    "Bug",
    "Rock",
    "Ghost",
    "Dragon",
    "Dark",
    "Steel",
    "Fairy"
  ];


  return (
    <div>
      <Toolbar
        start={
          <>
            <HomeButton/>
            <NavBarDropdown label={pokedexDropdownLabel} options={pokemonGenerations} pagePath={PagePaths.Pokedex} />
            <NavBarDropdown label={gymLeaderDropdownLabel} options={pokemonGenerations} pagePath={PagePaths.GymLeaders}/>
            <NavBarDropdown label={typeDropdownLabel} options={pokemonTypes} pagePath={PagePaths.Rank}/>
          </>
        }
        className='navbar'
      />
    </div>
  );
}