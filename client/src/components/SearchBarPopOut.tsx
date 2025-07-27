import { SwipeableDrawer } from '@mui/material';
import { useState } from 'react';
import Button from "@mui/material/Button";
import "../styles/general.css";
import { SearchBar } from './SearchBar';

export const SeachBarPopOut = () => {
  const [isOpen, setIsOpen] = useState(false);

  const handleOpen = () : void => setIsOpen(true);
  const handleClose = () : void => setIsOpen(false);

  return (
    <div>
      <Button onClick={handleOpen}>Search Stats</Button>

      <SwipeableDrawer
        anchor="right"
        open={isOpen}   
        onClose={handleClose}
        onOpen={handleOpen}
      >
        <div style={{ width: 250, padding: 16 }}>
          <SearchBar/>
        </div>
      </SwipeableDrawer>
    </div>
  );
}