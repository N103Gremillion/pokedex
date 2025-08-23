import type { PokedexData } from "../api/pokemon_api";
import { DataView, DataViewLayoutOptions } from 'primereact/dataview';
        

interface PokedexGridProps {
  pokedex : PokedexData;
}

const PokedexGrid = ({pokedex} : PokedexGridProps) => {
  return (
    <div>
      <DataView layout={"grid"}/>
    </div>
  );
}