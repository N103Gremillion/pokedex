import { Dropdown } from 'primereact/dropdown';
import '../styles/general.css';
import { useState } from 'react';

interface NavBarDropdownProps {
  label : string;
  options : string[];
}

export const NavBarDropdown = ({label, options} : NavBarDropdownProps) => {

  const [selectedOption, setSelectedOption] = useState("");

  const handleSelection = (selectedString : string) => {
    setSelectedOption(selectedString);
    console.log(selectedOption);
  }

  const mappedOptions = options.map(opt => ({
    label: opt,
    value: opt
  }));

  return (
    <Dropdown
      value={selectedOption}
      className='navbar-component'
      placeholder={label}
      options={mappedOptions}
      onChange={(event) => handleSelection(event.value)}
    />
  );
}