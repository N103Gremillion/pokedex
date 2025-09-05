import type { MoveData } from "../../types";
import { MoveCard } from "./MoveCard";

interface MoveGridProps {
  moves : MoveData[]
}

export const MoveGrid = ({moves} : MoveGridProps) => {

  return (
    <div className="move-grid">
      {moves.map((moveData : MoveData) => (
        <MoveCard move={moveData}/>
      ))}
    </div>
  );
}