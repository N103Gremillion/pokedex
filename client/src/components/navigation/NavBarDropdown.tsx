import { Dropdown } from 'primereact/dropdown';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import type { PagePaths } from '../../pages/pagePaths';

interface NavBarDropdownProps {
  label : string;
  options : string[];
  pagePath : PagePaths
}

export const NavBarDropdown = ({label, options, pagePath} : NavBarDropdownProps) => {

  const [selectedOption, setSelectedOption] = useState("");
  const navigate = useNavigate();

  const handleSelection = (selectedString : string) : void => {
    setSelectedOption(selectedString);
    navigate(`${pagePath}/${selectedString}`);
  }

  const mappedOptions = options.map(opt => ({
    label: opt,
    value: opt
  }));

  return (
    <Dropdown
      className='navbar-component'
      appendTo="self"
      placeholder={label}
      options={mappedOptions}
      onChange={(event) => handleSelection(event.value)}
    />
  );
}