import { NavLink } from 'react-router-dom';
import { PagePaths } from '../pages/pagePaths';

export const HomeButton = () => {
  return (
    <NavLink to={PagePaths.Home} className="navbar-component">
      Home
    </NavLink>
  );
}