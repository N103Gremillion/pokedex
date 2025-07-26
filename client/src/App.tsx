import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { SearchBar } from './components/SearchBar';

function MyButton() {
  return (
    <button>I'm a button</button>
  );

}

function App() {
  return (
    <div>
      <SearchBar></SearchBar>
    </div>
  )
}

export default App
