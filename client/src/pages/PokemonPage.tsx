import { useParams } from "react-router-dom";

export const  PokemonPage = () => {
  const { pokemonNameString = "" } = useParams<{ pokemonNameString? : string }>();
  
  console.log(pokemonNameString);

  return (
    <div className='general-page'>
      <h1 className="header"> This is the Pokemon page </h1>
    </div>
  );
}