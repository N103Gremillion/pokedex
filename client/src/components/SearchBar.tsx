import React, {useState, type ChangeEvent, type Dispatch, type SetStateAction} from 'react';
import { InputAdornment, TextField } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import { useProMode } from '../context';
import { getMatchingPlayers } from '../api/player-api';


export const SearchBar = () => {
  // visuals
  const label : string = "Search...";

  // used to keep track of the text in the search bar
  const [searchBarText, setSearchBarText] = useState("");

  const { isProMode } = useProMode();

  const handleKeyPress = async (event : React.KeyboardEvent<HTMLInputElement>) : Promise<void> => {
    if (event.key === "Enter") {
      if (isProMode) {
        console.log("Checking ProTeam database", searchBarText);
      } else {
        const json = await getMatchingPlayers(searchBarText);
        console.log(json);
      }
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

