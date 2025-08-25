import { Routes, Route } from 'react-router-dom';

import { NavBar } from './components/NavBar';
import { HomePage } from './pages/HomePage';
import { GymLeadersPage } from './pages/GymLeadersPage';
import { PokedexPage } from './pages/PokedexPage';
import { TypePage } from './pages/TypePage';
import { PagePaths } from './pages/pagePaths';
import './App.css';
import './styles/general.css';
import { Footer } from './components/Footer';
import { PokemonPage } from './pages/PokemonPage';


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
      </Routes> 
      <Footer/>     
    </>
  );
}

export default App
