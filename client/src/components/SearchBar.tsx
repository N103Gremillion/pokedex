import React, {useState, type ChangeEvent, type Dispatch, type SetStateAction} from 'react';

export const SearchBar = () => {

  // used to keep track of the text in the search bar
  const [searchBarText, setSearchBarText] = useState("");

  const handleChange = (event : React.ChangeEvent<HTMLInputElement>) : void => {
    const newText : string = event.target.value;
    setSearchBarText(newText);
    console.log("Typed:", newText);
  }

  return (
    <input
      value={searchBarText} 
      onChange={(event) => handleChange(event)}
      maxLength={100}>
    </input>
  );
};
