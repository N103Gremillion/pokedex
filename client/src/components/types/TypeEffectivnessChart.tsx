import type { DetailedPokemonTypeData } from "../../types";
import "../../styles/types.css"
import { PokemonType } from "../../enums";
import { getTypeSymbolUrl } from "../../utils";
import type { JSX, ReactElement } from "react";

interface TypeEffectivnessChartProps {
  typeData : DetailedPokemonTypeData
}

const allTypes = Object.values(PokemonType)


export const TypeEffectivnessChart = ({typeData} : TypeEffectivnessChartProps) => {

  function getNormalDmgTo(): PokemonType[] {
    const specialTypes: PokemonType[] = [
      ...(typeData.no_dmg_to ?? []),
      ...(typeData.half_dmg_to ?? []),
      ...(typeData.double_dmg_to ?? [])
    ];

    const specialSet = new Set<PokemonType>(specialTypes);

    // filter out the invalid types
    return allTypes.filter(type => !specialSet.has(type) && type != PokemonType.Unkown);
  }

  function getNormalDmgFrom() : PokemonType[] {
    const specialTypes: PokemonType[] = [
      ...(typeData.no_dmg_from ?? []),
      ...(typeData.half_dmg_from ?? []),
      ...(typeData.double_dmg_from ?? [])
    ];

    const specialSet = new Set<PokemonType>(specialTypes);

    // filter out the invalid types
    return allTypes.filter(type => !specialSet.has(type) && type != PokemonType.Unkown);
  }
  
  function renderTypeImages(types: PokemonType[] | undefined): ReactElement {
    if (!types || types.length === 0) {
      return <div>None</div>;
    }

    return (
      <>
        {types.map((type) => (
          <img
            className="type-effectivness-grid-type-img"
            key={type}
            src={getTypeSymbolUrl(type)}
            alt={type}
          />
        ))}
      </>
    );
  }


  const normalDmgTo : PokemonType[] = getNormalDmgTo();
  const normalDmgFrom : PokemonType[] = getNormalDmgFrom();

  return (
    <div>
      {/* Offensive */}
      <h1>Offensive</h1>
      <div className="type-effectivness-grid">
        {/* Super effective */}
        <div className="type-effectivness-grid-label type-effectivness-grid-label-super">
          Super effectivness
        </div>
        <div className="type-effectivness-grid-types" >
          {renderTypeImages(typeData.double_dmg_to)}
        </div>

        {/* Normal */}
        <div className="type-effectivness-grid-label type-effectivness-grid-label-normal">
          Normal
        </div>
        <div className="type-effectivness-grid-types">
          {renderTypeImages(normalDmgTo)}
        </div>
        
        {/* Not very effective */}
        <div className="type-effectivness-grid-label type-effectivness-grid-label-not-very">
          Not very effective
        </div>
        <div className="type-effectivness-grid-types">
          {renderTypeImages(typeData.half_dmg_to)}
        </div>

        {/* No effective */}
        <div className="type-effectivness-grid-label type-effectivness-immune">
          No effective
        </div>
        <div className="type-effectivness-grid-types">
          {renderTypeImages(typeData.no_dmg_to)}
        </div>

      </div>

      {/* Defensive */}
      <h1 style={{paddingTop:"20px"}}>Defensive</h1>
      <div className="type-effectivness-grid">
        {/* Super effective */}
        <div className="type-effectivness-grid-label type-effectivness-grid-label-super">
          Super effectivness
        </div>
        <div className="type-effectivness-grid-types" >
          {renderTypeImages(typeData.double_dmg_from)}
        </div>

        {/* Normal */}
        <div className="type-effectivness-grid-label type-effectivness-grid-label-normal">
          Normal
        </div>
        <div className="type-effectivness-grid-types">
          {renderTypeImages(normalDmgFrom)}
        </div>
        
        {/* Not very effective */}
        <div className="type-effectivness-grid-label type-effectivness-grid-label-not-very">
          Not very effective
        </div>
        <div className="type-effectivness-grid-types">
          {renderTypeImages(typeData.half_dmg_from)}
        </div>

        {/* No effective */}
        <div className="type-effectivness-grid-label type-effectivness-immune">
          No effective
        </div>
        <div className="type-effectivness-grid-types">
          {renderTypeImages(typeData.no_dmg_from)}
        </div>

      </div>
    </div>
  );
}
