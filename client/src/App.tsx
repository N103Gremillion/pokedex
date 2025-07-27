import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import './styles/general.css'
import { SearchBar } from './components/SearchBar';
import { ProModeToggleButton } from './components/ProModeToggleButton';

function App() {
  return (
    <div>
      <div className='position-top-left'>
        <ProModeToggleButton/>
      </div>
    </div>
  )
}

export default App
