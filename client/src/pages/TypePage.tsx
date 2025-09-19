import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getTypeSymbolUrl, validPokemonType } from "../utils";
import { getAllPokemonOfType, getMovesOfType, getTypeInfo } from "../api/pokemon_api";
import { PokemonType } from "../enums";
import type { DetailedPokemonTypeData, MoveData, PokedexData, PokemonData } from "../types";
import { PokedexGrid } from "../components/pokedex/PokedexGrid";
import { MoveGrid } from "../components/moves/MoveGrid";
import { TypeEffectivnessChart } from "../components/types/TypeEffectivnessChart";

export const TypePage = () => {
  // pull of the type info from the url 
  const { typeString = "" } = useParams<{ typeString? : string }>();
  const [ loading, setLoading ] = useState<boolean>(false);
  const [ movesOfType, setMovesOfType ] = useState<MoveData[]>([]);
  const [ pokemonOfType, setPokemonOfType ] = useState<PokemonData[]>([]);
  const [ typeData, setTypeData ] = useState<DetailedPokemonTypeData>({
    type_name : PokemonType.Unkown,
    no_dmg_to : [],
    half_dmg_to : [],
    double_dmg_to : [],
    no_dmg_from : [],
    half_dmg_from : [],
    double_dmg_from : []
  });

  useEffect (() => {
    const run = async () => {
      setLoading(true);
      
      if (!validPokemonType(typeString)){
        console.log(`Invalid type passed to TypePage. Type : ${typeString}`)
        return
      }
      
      setMovesOfType([]);
      setPokemonOfType([]);
      setTypeData({
        type_name: PokemonType.Unkown,
        no_dmg_to: [],
        half_dmg_to: [],
        double_dmg_to: [],
        no_dmg_from: [],
        half_dmg_from: [],
        double_dmg_from: []
      });
      
      setTypeData(await getTypeInfo(typeString as PokemonType));
      setMovesOfType(await getMovesOfType(typeString as PokemonType));
      setPokemonOfType(await getAllPokemonOfType(typeString as PokemonType));
      

      setLoading(false);
      window.scrollTo(0, 0);
    };

    run();
  }, [typeString]);
  
  const typeSymbolImage = (
    <img
      src={getTypeSymbolUrl(typeString as PokemonType)}
      alt={"Type"}
      className="move-card-type-img"
    />
  );

  if (loading) { return <div className='loading-page'>Loading...</div>};

  return (
    <div className='general-page'>
      <h1 className='header' style={{paddingBottom:"20px"}}>{typeSymbolImage} {typeData.type_name} Type</h1>

      <TypeEffectivnessChart typeData={typeData}/>

      <h2 className="header2">{typeData.type_name} Moves</h2>
      <MoveGrid moves={movesOfType}/>

      <h2 className="header2">{typeData.type_name} Pokemon</h2>
      <PokedexGrid pokedex={{gen_num : -1, pokemon : pokemonOfType } as PokedexData}/>

    </div>
  );
}