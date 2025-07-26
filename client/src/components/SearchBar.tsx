import React, {useState, type ChangeEvent, type Dispatch, type SetStateAction} from 'react';

export const SearchBar = () => {

  // used to keep track of the text in the search bar
  const [searchBarText, setSearchBarText] = useState("");

  const handleKeyPress = (event : React.KeyboardEvent<HTMLInputElement>) : void => {
    if (event.key === "Enter") { 
      console.log("Enter Pressed.");
    } 
  }

  const handleTextChange = (event : React.ChangeEvent<HTMLInputElement>) : void => {
    const newText : string = event.target.value;
    setSearchBarText(newText);
    console.log(newText);
  }

  return (
    <input
      type="text"
      placeholder="Search..."
      value={searchBarText} 
      onKeyUp={handleKeyPress}
      onChange={handleTextChange}
      maxLength={100}>
    </input>
  );
};
