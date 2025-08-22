import React, { useState } from 'react';
import { AutoComplete } from 'primereact/autocomplete';
import { getMatchingPlayers } from '../api/pokemon_api';
import '../styles/general.css';

export const SearchBar = () => {
  const [searchBarText, setSearchBarText] = useState('');
  const [suggestions, setSuggestions] = useState([]);

  const handleSearch = async (queryString : string ) => {
    setSearchBarText(queryString);

    if (!queryString) {
      setSuggestions([]);
      return;
    }

    // Call your API to get matching players based on the query
    const results = await getMatchingPlayers(queryString);
    setSuggestions(results);
  };

  return (
    <div className='search-bar-container'>
      <AutoComplete
        size={50}
        id="player-search"
        value={searchBarText}
        suggestions={suggestions}
        completeMethod={(event) => handleSearch(event.query)} 
        field="name"                
        onChange={(event) => setSearchBarText(event.value)}
        placeholder="Search ..."
        inputClassName='search-bar'
      />
    </div>
  );
};
