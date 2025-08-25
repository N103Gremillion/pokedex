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
    return (
      <div className="grid grid-cols-5 gap-4">
        {items.map((item, index) => (
          <div
            key={index}
            className="flex items-center justify-center h-24 rounded-lg shadow bg-gray-100"
          >
            {item}
          </div>
        ))}
      </div>
    );
  } 

  return (
    <div>
      <DataView 
      value={temp_vals} 
      layout="grid"
      listTemplate={() => callback(temp_vals, "grid")}/>
    </div>
  );
}