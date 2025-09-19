import { useParams, useSearchParams } from "react-router-dom"
import "../styles/general.css"
import "../styles/moves.css"
import { useEffect, useState, type JSX, type ReactElement, type ReactNode } from "react";
import type { MoveData } from "../types";
import { getDetailedMoveInfo } from "../api/pokemon_api";
import { getDmgClassUrl, getTypeUrl } from "../utils";

export const MovePage = () => {

  const { moveNameString = "" } = useParams<"moveNameString">();
  const [moveInfo, setMoveInfo] = useState<MoveData>({});

  useEffect(() => {
    const queryMoveInfo = async () => {
      setMoveInfo(await getDetailedMoveInfo(moveNameString));
      window.scrollTo(0, 0);
    }
    queryMoveInfo();
  }, []);

  const TypeImage  = () : ReactNode => {
    return (
      <img className="move-info-type-img" src={getTypeUrl(moveInfo.type_name)} alt="Unknown type"/>
    );
  }

  const DmgClassImage = () : ReactNode => {
    return (
      <img className="move-info-type-img" src={getDmgClassUrl(moveInfo.dmg_class)} alt="Unknown dmg class"/>
    );
  }

  return (
    <div className="general-page">

      <div className={`move-info-container`}>
        
        {/* general move info */}
        <div className={`general-move-info-container move-card-${moveInfo.type_name?.toLowerCase()}`}>
          <div>
            Move Name: {moveInfo.name}
            {TypeImage()}
          </div>
          <div>
            Damage Class: {moveInfo.dmg_class}
            {DmgClassImage()}
          </div>
        </div>


        {/* move stats info */}
        <div className={`move-info-stats-container move-card-${moveInfo.type_name?.toLowerCase()}`}> 
          <div>
            Power: {moveInfo.power === -1 ? "---" : moveInfo.power} <br/>
            PP: {moveInfo.pp} <br/>
            Effect Chance: {moveInfo.effect_chance == null || moveInfo.effect_chance === -1 ? "---" : `${moveInfo.effect_chance}%`}
          </div>
          <div style={{paddingLeft:"40px"}}>
            Accuracy : {moveInfo.accuracy === null || moveInfo.accuracy === -1 ? "---" : `${moveInfo.accuracy}%`} <br/>
            Priority : {moveInfo.priority ?? "0"}
          </div>
        </div> 

        <div className={`move-effects-container move-card-${moveInfo.type_name?.toLowerCase()}`}>
          Effects : <br/>
          { moveInfo.effects?.length != 0 && moveInfo.effects ? 
            moveInfo.effects?.map((effect, index) => (
              <div key={index}>
                -
                {effect ?? "no effects"}
              </div>
            )) : "None"
          }
        </div>

    </div>
  </div>
  )
}