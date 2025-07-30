import React, {useState} from 'react';
import { InputAdornment, TextField } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import { getMatchingPlayers } from '../api/player-api';
import '../styles/general.css'


export const SearchBar = () => {
  const backgroundColor : string = '#424242';
  const textColor : string = '#d8d8d8';
  const borderColor : string = '#5a5a5a';
  const focusBorderColor : string = '#ffffff';

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

  // sx "like css"
  const searchBarSx = {
    marginTop: '20px',
    backgroundColor: backgroundColor,
    color: '#d8d8d8',
    borderRadius: '6px',
    input: {
      color: textColor,
    },
    label: {
      color: borderColor
    },
    '& .MuiOutlinedInput-root': {
      '& fieldset': {
        borderColor: borderColor,
      },
      '&:hover fieldset': {
        borderColor: focusBorderColor,
      },
      '&.Mui-focused fieldset': {
        borderColor: focusBorderColor,
      },
    },
    '& .MuiInputLabel-root': {
      color: textColor,
    },
    '& .MuiInputLabel-root.Mui-focused': {
      color: focusBorderColor,
    },
  }

  return (
    <TextField
      label={label}
      color="primary"
      sx={searchBarSx}
      className='.search-bar'
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

