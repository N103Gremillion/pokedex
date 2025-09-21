import { useEffect, useState, type ReactNode, type SyntheticEvent } from "react";
import { Button } from 'primereact/button';
import { useNavigate, useParams } from "react-router-dom";
import { getDetailedPokemonData } from "../api/pokemon_api";
import type { MoveData, PokemonData } from "../types";
import "../styles/pokemon-page.css"
import type { PokemonType } from "../enums";
import { getTypeUrl } from "../utils";
import { PokemonStatChart } from "../components/stats/PokemonStatChart";
import { PokedexEntry } from "../components/pokedex/PokedexEntry";
import { PagePaths } from "./pagePaths";

export const  PokemonPage = () => {

  const defaultImageUrl : string = "/public/substitute.png";
  const {pokemonNameString = ""} = useParams<{ pokemonNameString? : string }>();
  const [detailedPokemonData, setDetailedPokemonData] = useState<PokemonData>({});
  const [loading, setLoading] = useState<boolean>(false);
  const [shinySelected, setShinySelected] = useState<boolean>(false);
  const navigate = useNavigate();

  useEffect(() => {
    setLoading(true);
    const runQuery = async () => {
      setDetailedPokemonData(await getDetailedPokemonData(pokemonNameString));
      setLoading(false);
      setShinySelected(false);
      window.scrollTo(0, 0);
    }
    runQuery();
  }, [pokemonNameString]);

  const handleImageNotFound = (event : SyntheticEvent<HTMLImageElement, Event>) => {
    const img = event.currentTarget;
    img.src = defaultImageUrl;
  }

  const handleMoveClick = (move_name : string) => {
    navigate(`${PagePaths.Move}/${move_name}`);
  }

  const PokemonImg = () : ReactNode => {
    return (
      <img 
        className="pokemon-default-img"
        src={shinySelected ? detailedPokemonData.shiny_image_url : detailedPokemonData.imageUrl} 
        alt={detailedPokemonData.name ?? "Unknown"}
        onError={handleImageNotFound}
      />
    );
  }

  console.log(detailedPokemonData.moves_learned);

  if (loading) { return <div className='loading-page'>Loading...</div>};

  return (
    <div className='general-page' style={{display:"flex", flexDirection:"column", flexWrap : "wrap", alignContent:"center"}}>
      {/* General pokemon info */}
      <div className="general-pokemon-info-container">
        {PokemonImg()}
        <div className="pokemon-general-info">
          <Button 
            onClick={() => setShinySelected(!shinySelected)} 
            className="shiny-button" 
            label="shiny" 
            style={{backgroundColor: !shinySelected ? "#121820" : "#66b3ff"}}
          />
          {!detailedPokemonData.name ? "Name : ---" : `Name : ${detailedPokemonData.name}`}<br/>
          {!detailedPokemonData.height ? "Height : ---" : `Height : ${((detailedPokemonData.height / 10) * 3.28).toFixed(2)}ft`} <br/>
          {!detailedPokemonData.weight ? "Weight : ---" : `Weight : ${(detailedPokemonData.weight).toFixed(2)}lbs`}
          <div>
            Types :
            {
            detailedPokemonData.types?.map((type : PokemonType, index : number) => (
              <img key={index} className="pokemon-type-img" src={getTypeUrl(type)} alt="---"/>
            ))
            }
          </div>
        </div>
      </div>
      
      {/* Stats */}
      <div className="pokemon-stats-chart">
        <PokemonStatChart 
          hp={detailedPokemonData.hp ?? 0}
          attack={detailedPokemonData.attack ?? 0}
          defense={detailedPokemonData.defense ?? 0}
          sp_attack={detailedPokemonData.sp_attack ?? 0}
          sp_defense={detailedPokemonData.sp_defense ?? 0}
          speed={detailedPokemonData.speed ?? 0} 
        />
      </div>
      
      {/* evolution info */}
      {detailedPokemonData.evolution_chain && detailedPokemonData.evolution_chain.length > 1 && (
        <>
          <h1 className="h1-tag" >Evolutions</h1>
          <div className="pokemon-evolution-chain">
            {detailedPokemonData.evolution_chain?.map((pokemon_evolution, index) => (
              <div className="pokemon-evolution-chain-entry">
                <PokedexEntry key={index} pokemonData={pokemon_evolution.pokemon ?? {}}/>
                {pokemon_evolution.method && (
                  <span className="evolution-method">{pokemon_evolution.method}</span>
                )}
              </div>
            ))}
          </div>
        </>
      )}

      {/* moves learned by level up */}
      <h1 className="h1-tag">Level-Up Moves</h1>
        <div className="moves-container">
          <div className="move-entry move-header">
          <span className="move-column name">Name</span>
          <span className="move-column type">Type</span>
          <span className="move-column power">Power</span>
          <span className="move-column accuracy">Accuracy</span>
          <span className="move-column pp">PP</span>
          <span className="move-column dmg-class">Class</span>
          <span className="move-column learn-method">Method</span>
        </div>
        {
          detailedPokemonData.moves_learned?.map((move : MoveData, index : number) => (
            move.learn_method === "level-up" && (
              <div className="move-entry" key={index} onClick={() => handleMoveClick(move.name ?? "undefined")}>
                <span className="move-column">{move.name ?? "---"}</span>
                <span className="move-column">
                  {move.type_name && <img src={getTypeUrl(move.type_name)} alt={move.type_name} />}
                </span>
                <span className="move-column">{!move.power || move.power === -1 ? "---" : move.power}</span>
                <span className="move-column">{!move.accuracy || move.accuracy === -1 ? "---" : move.accuracy}</span>
                <span className="move-column">{!move.pp || move.pp === -1 ? "---" : move.pp}</span>
                <span className="move-column">{move.dmg_class ?? "---"}</span>
                <span className="move-column">{(`level ${move.level_learned}`)}</span>
              </div>
            )
          ))
        }
      </div>
      
      {/* moves learned by level up */}
      <h1 className="h1-tag">TM moves</h1>
        <div className="moves-container">
          <div className="move-entry move-header">
          <span className="move-column name">Name</span>
          <span className="move-column type">Type</span>
          <span className="move-column power">Power</span>
          <span className="move-column accuracy">Accuracy</span>
          <span className="move-column pp">PP</span>
          <span className="move-column dmg-class">Class</span>
          <span className="move-column learn-method">Method</span>
        </div>
        {
          detailedPokemonData.moves_learned?.map((move : MoveData, index : number) => (
            move.learn_method === "machine" && (
              <div className="move-entry" key={index} onClick={() => handleMoveClick(move.name ?? "undefined")}>
                <span className="move-column">{move.name ?? "---"}</span>
                <span className="move-column">
                  {move.type_name && <img src={getTypeUrl(move.type_name)} alt={move.type_name} />}
                </span>
                <span className="move-column">{!move.power || move.power === -1 ? "---" : move.power}</span>
                <span className="move-column">{!move.accuracy || move.accuracy === -1 ? "---" : move.accuracy}</span>
                <span className="move-column">{!move.pp || move.pp === -1 ? "---" : move.pp}</span>
                <span className="move-column">{move.dmg_class ?? "---"}</span>
                <span className="move-column">{move.learn_method ?? "---"}</span>
              </div>
            )
          ))
        }
      </div>

    </div>
  );
}