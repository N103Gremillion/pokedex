import { Toolbar } from 'primereact/toolbar';
import { NavBarDropdown } from './NavBarDropdown';
import '../styles/general.css';
import { HomeButton } from './HomeButton';
import { PagePaths } from '../pages/pagePaths';

export const NavBar = () => {
  
  const operatorDropdownLabel : string = "Select Operator";
  const mapDropdownLabel : string = "Select Map";
  const rankDropdownLabel : string = "Select Rank";

  const r6Operators : string[] = [
    "Ash", "Thermite", "Twitch", "Montagne", "Glaz",
    "Fuze", "Blitz", "IQ", "Buck", "Blackbeard", "Capitao", "Hibana",
    "Jackal", "Ying", "Zofia", "Dokkaebi", "Lion", "Finka", "Maverick",
    "Nomad", "Gridlock", "Nokk", "Amaru", "Kali", "Iana", "Ace",
    "Zero", "Flores", "Oryx", "Thorn", "Azami", "Solis", "Fenrir",
    "Jager", "Bandit", "Smoke", "Mute", "Pulse", "Castle", "Doc",
    "Rook", "Kapkan", "Tachanka", "Caveira", "Echo", "Valkyrie", "Lesion",
    "Ela", "Vigil", "Maestro", "Alibi", "Clash", "Kaid", "Mozzie", "Warden",
    "Goyo", "Wamai", "Osa", "Thunderbird", "Thatcher", "Sledge", "Recruit"
  ];
  const r6Maps: string[] = [
    "Bank", "Border", "Chalet", "Clubhouse", "Coastline",
    "Consulate", "Kafe Dostoyevsky", "Oregon", "Outback", "Plane",
    "Skyscraper", "Theme Park", "Tower", "Villa", "Yacht",
    "Fortress", "Hillside", "Reunion", "Kanal", "Favela",
    "House", "Hereford Base", "Presidio", "Pearl", "Oryx Estate",
    "Bartlett University", "Borderlands"
  ];
  const r6Ranks: string[] = [
    "Copper IV", "Copper III", "Copper II", "Copper I",
    "Bronze IV", "Bronze III", "Bronze II", "Bronze I",
    "Silver IV", "Silver III", "Silver II", "Silver I",
    "Gold IV", "Gold III", "Gold II", "Gold I",
    "Platinum IV",  "Platinum III", "Platinum II", "Platinum I",
    "Diamond IV", "Diamond III", "Diamond II", "Diamond I",
    "Champion"
  ];

  return (
    <div>
      <Toolbar
        start={
          <>
            <HomeButton/>
            <NavBarDropdown label={operatorDropdownLabel} options={r6Operators} pagePath={PagePaths.Opterator} />
            <NavBarDropdown label={mapDropdownLabel} options={r6Maps} pagePath={PagePaths.Map}/>
            <NavBarDropdown label={rankDropdownLabel} options={r6Ranks} pagePath={PagePaths.Rank}/>
          </>
        }
        className='navbar'
      />
    </div>
  );
}