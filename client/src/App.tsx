import { useContext, useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import './styles/general.css';
import { ProModeToggleButton } from './components/ProModeToggleButton';
import { SeachBarPopOut } from './components/SearchBarPopOut';

function App() {

  return (
    <div>
      {/* components in the top left */}
      <div className='position-top-left'>
        <ProModeToggleButton/>
        <SeachBarPopOut/>
      </div>
      
    </div>
  );
}

export default App
