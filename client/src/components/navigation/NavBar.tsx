import { Toolbar } from 'primereact/toolbar';
import { NavBarDropdown } from './NavBarDropdown';
import { HomeButton } from '../butttons/HomeButton';
import { PagePaths } from '../../pages/pagePaths';
import "../../styles/navbar.css"

export const NavBar = () => {
  
  const pokedexDropdownLabel : string = "Pokedex";
  const gymLeaderDropdownLabel : string = "Gym Leader";
  const typeDropdownLabel : string = "Type";

  const pokemonGenerations: string[] = [
    "GenerationI",
    "GenerationII",
    "GenerationIII",
    "GenerationIV",
    "GenerationV",
    "GenerationVI",
    "GenerationVII",
    "GenerationVIII",
    "GenerationIX"
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
            <NavBarDropdown label={typeDropdownLabel} options={pokemonTypes} pagePath={PagePaths.Type}/>
          </>
        }
        className='navbar'
      />
    </div>
  );
}