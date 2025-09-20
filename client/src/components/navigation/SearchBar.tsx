import { useState } from 'react';
import { AutoComplete } from 'primereact/autocomplete';
import { getMatchingSearchPool, getMatchingSearchs } from '../../api/pokemon_api';
import { SearchPool } from '../../enums';
import { useNavigate } from 'react-router-dom';
import { PagePaths } from '../../pages/pagePaths';

export const SearchBar = () => {
  const [searchBarText, setSearchBarText] = useState('');
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [noResult, setNoResult] = useState(false);
  const navigate = useNavigate();

  const handleAutoCompleteSuggestions = async (queryString : string ) => {
    setNoResult(false);
    setSearchBarText(queryString);
    
    if (!queryString) {
      setSuggestions([]);
      return;
    }

    // Call your API to get matching players based on the query
    setSuggestions(await getMatchingSearchs (queryString));
  };

  const handleSearch = async (queryString : string) => {
    setNoResult(false);
    const pool : SearchPool = await getMatchingSearchPool(queryString);

    if (pool === SearchPool.GymLeader) {
      navigate(`${PagePaths.GymLeader}/${queryString}`);
    }
    else if (pool === SearchPool.Type) {
      navigate(`${PagePaths.Type}/${queryString}`);
    }
    else if (pool === SearchPool.Pokemon) {
      navigate(`${PagePaths.Pokemon}/${queryString}`);
    }
    else if (pool === SearchPool.Move) {
      navigate(`${PagePaths.Move}/${queryString}`);
    }
    else if (pool === SearchPool.Item) {
      navigate(`${PagePaths.Item}/${queryString}`);
    }
    else {
      setSuggestions([]);
      setSearchBarText("");
      setNoResult(true);
      console.log(`CANT FIND A POOL FOR QUERY : ${queryString}`)
    }
  }

  return (
    <div className='search-bar-container'>
      <AutoComplete
        size={50}
        id="player-search"
        value={searchBarText}
        suggestions={suggestions}
        completeMethod={(event) => handleAutoCompleteSuggestions(event.query)}                 
        onChange={(event) => setSearchBarText(event.value)}
        placeholder="Search ..."
        inputClassName='search-bar'
        panelStyle={{ width: '400px', backgroundColor : "royalblue"}}
        onKeyDown={(event : React.KeyboardEvent) => {
          if (event.key === "Enter"){
            handleSearch(searchBarText);
          }
        }}
        emptyMessage="No results"
      />
      {noResult && (
        <div style={{ color: "red", marginTop: "4px" }}>No results</div>
      )}
    </div>
  );
};
