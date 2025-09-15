import { useParams, useSearchParams } from "react-router-dom"
import "../styles/general.css"
import "../styles/moves.css"
import { useEffect, useState, type JSX, type ReactElement, type ReactNode } from "react";
import type { MoveData } from "../types";
import { getDetailedMoveInfo } from "../api/pokemon_api";
import { getTypeUrl } from "../utils";

export const MovePage = () => {

  const { moveNameString = "" } = useParams<"moveNameString">();
  const [moveInfo, setMoveInfo] = useState<MoveData>({});

  useEffect(() => {
    const queryMoveInfo = async () => {
      setMoveInfo(await getDetailedMoveInfo(moveNameString));
    }
    queryMoveInfo();
  }, []);

  const TypeImage  = () : ReactNode => {
    return (
      <img className="move-info-type-img" src={getTypeUrl(moveInfo.type_name)} alt="Unknown type"/>
    );
  }

  return (
    <div className="general-page">

      <div className={`move-info-container`}>
        
        {/* general move info */}
        <div className={`general-move-info-container move-card-${moveInfo.type_name?.toLowerCase()}`}>
          <div>
            Move Name : {moveInfo.name}
            {TypeImage()}
          </div>
          <div>
            Damage Class : {moveInfo.dmg_class}
          </div>
        </div>


        {/* move stats info */}
        <div className="move-info-stats-container"> 
          <div>
            Hello World!
          </div>
        </div> 

    </div>
  </div>
  )
}