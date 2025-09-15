import type { MoveData } from "../../types";
import { getTypeUrl } from "../../utils";
import "../../styles/moves.css"
import { useNavigate } from "react-router-dom";
import { PagePaths } from "../../pages/pagePaths";

interface MoveCardProps {
  move : MoveData
}

export const MoveCard = ({ move } : MoveCardProps) => {

  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`${PagePaths.Move}/${move.name}`);
  }

  const typeImage = (
    <img
      src={getTypeUrl(move.type_name)}
      alt={"Type"}
      className="move-card-type-img"
    />
  );

  return (
    <div className={`move-card move-card-${move.type_name?.toLowerCase()}`} onClick={handleClick}>
      <div>
        {move.name}
      </div>
      <div>
        {typeImage} {`PP ${move.pp}/${move.pp}`} 
      </div>
    </div>
  );
}