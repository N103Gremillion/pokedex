import { useState } from 'react';
import { AutoComplete } from 'primereact/autocomplete';
import { getMatchingSearchs } from '../../api/pokemon_api';


export const SearchBar = () => {
  const [searchBarText, setSearchBarText] = useState('');
  const [suggestions, setSuggestions] = useState<string[]>([]);

  const handleSearch = async (queryString : string ) => {
    setSearchBarText(queryString);
    
    if (!queryString) {
      setSuggestions([]);
      return;
    }

    // Call your API to get matching players based on the query
    setSuggestions(await getMatchingSearchs (queryString));
  };

  return (
    <div className='search-bar-container'>
      <AutoComplete
        size={50}
        id="player-search"
        value={searchBarText}
        suggestions={suggestions}
        completeMethod={(event) => handleSearch(event.query)}                 
        onChange={(event) => setSearchBarText(event.value)}
        placeholder="Search ..."
        inputClassName='search-bar'
        panelStyle={{ width: '400px', backgroundColor : "royalblue"}}
      />
    </div>
  );
};
