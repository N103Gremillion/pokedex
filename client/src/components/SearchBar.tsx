import React, {useState} from 'react';
import { InputAdornment, TextField } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import { getMatchingPlayers } from '../api/player-api';


export const SearchBar = () => {
  // visuals
  const label : string = "Search...";

  // used to keep track of the text in the search bar
  const [searchBarText, setSearchBarText] = useState("");

  const handleKeyPress = async (event : React.KeyboardEvent<HTMLInputElement>) : Promise<void> => {
    if (event.key === "Enter") {
      getMatchingPlayers(searchBarText);
    } 
  }

  const handleTextChange = (event : React.ChangeEvent<HTMLInputElement>) : void => {
    const newText : string = event.target.value;
    setSearchBarText(newText);
  }

  return (
    <TextField
      label={label}
      variant="outlined"
      onChange={handleTextChange}
      onKeyUp={handleKeyPress}
      slotProps={{
        input: {
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
            </InputAdornment>
          ),
        }
      }}
    />
  );
}

