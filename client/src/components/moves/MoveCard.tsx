import type { MoveData } from "../../types";
import { getTypeUrl } from "../../utils";

interface MoveCardProps {
  move : MoveData
}

export const MoveCard = ({ move } : MoveCardProps) => {

  const typeImage = (
    <img
      src={getTypeUrl(move.type_name)}
      alt={"Type"}
      className="move-card-type-img"
    />
  );

  return (
    <div className={`move-card move-card-${move.type_name?.toLowerCase()}`}>
      <div>
        {move.name}
      </div>
      <div>
        {typeImage} {`PP ${move.pp}/${move.pp}`} 
      </div>
    </div>
  );
}