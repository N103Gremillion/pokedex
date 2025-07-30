import { useContext, useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import { Routes, Route } from 'react-router-dom';

import { NavBar } from './components/NavBar';
import { HomePage } from './pages/HomePage';
import { MapPage } from './pages/MapPage';
import { OperatorPage } from './pages/OperatorPage';
import { PlayerPage } from './pages/PlayterPage';
import { RankPage } from './pages/RankPage';
import { PagePaths } from './pages/pagePaths';
import './App.css';
import './styles/general.css';


function App() {

  return (
    <>
      <NavBar/>
      <Routes>
        <Route path={PagePaths.Home} element={<HomePage />} />
        <Route path={PagePaths.Opterator} element={<OperatorPage /> }/>
        <Route path={PagePaths.Map} element={<MapPage /> }/>
        <Route path={PagePaths.Rank} element={<RankPage />} />
        <Route path={PagePaths.Player} element={<PlayerPage />} />
      </Routes>      
    </>
  );
}

export default App
