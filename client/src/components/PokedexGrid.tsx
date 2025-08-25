import type { ReactNode } from "react";
import type { PokedexData } from "../api/pokemon_api";
import { DataView, DataViewLayoutOptions } from 'primereact/dataview';
        

interface PokedexGridProps {
  pokedex : PokedexData;
}

type Layouts = 
  | "grid"
  | "list"
  | string & Record<string, unknown>;

export const PokedexGrid = ({pokedex} : PokedexGridProps) => {

  const temp_vals : string[] = ["hello", "my", "name", "is", "Nathan"];

  const callback = (items : any[], layout : Layouts ) : ReactNode | ReactNode [] => {
    layout = layout
    // get the 1st 20 pokemon out
    items = temp_vals;
    return items;
  } 

  return (
    <div>
      <DataView value={temp_vals} listTemplate={() => callback(temp_vals, "grid")}/>
    </div>
  );
}