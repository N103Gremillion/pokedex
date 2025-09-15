import { Routes, Route } from 'react-router-dom';

import { NavBar } from './components/navigation/NavBar';
import { HomePage } from './pages/HomePage';
import { GymLeadersPage } from './pages/GymLeadersPage';
import { PokedexPage } from './pages/PokedexPage';
import { TypePage } from './pages/TypePage';
import { PagePaths } from './pages/pagePaths';
import './App.css';
import './styles/general.css';
import { Footer } from './components/general/Footer';
import { PokemonPage } from './pages/PokemonPage';
import { MovePage } from './pages/MovePage';


function App() {

  return (
    <>
      <NavBar/>
      <Routes>
        <Route path={PagePaths.Home} element={<HomePage />} />
        <Route path={`${PagePaths.Pokedex}/:generationString`} element={<PokedexPage /> }/>
        <Route path={`${PagePaths.GymLeaders}/:generationString`} element={<GymLeadersPage /> }/>
        <Route path={`${PagePaths.Type}/:typeString`} element={<TypePage />} />
        <Route path={`${PagePaths.Pokemon}/:pokemonNameString`} element={<PokemonPage/>}/>
        <Route path={`${PagePaths.Move}/:moveNameString`} element={<MovePage/>}/>
      </Routes> 
      <Footer/>     
    </>
  );
}

export default App
