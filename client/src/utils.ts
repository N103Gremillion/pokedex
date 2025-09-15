import { PokemonDmgClass, PokemonType } from "./enums";

const basetypeImageUrl : string = "/type_logos";

export const sleep = async(seconds : number) : Promise<void> => {
  await new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

export function validPokemonType(typeString : string) : boolean {

  for (const type of Object.values(PokemonType)) {
    if (typeString === type) {
      return true;
    }
  }

  return false;
}

export function getDmgClassUrl(type : PokemonDmgClass | undefined) : string {
  if (type === undefined) {
    return ""
  }
  return `/type_logos/${type}.png`
}

export function getTypeUrl(type : PokemonType | undefined) : string {

  if (type === undefined) {
    return ""
  }
  
  return `/type_logos/${type}.png`
} 

export function getTypeUrls(types : PokemonType[] | undefined) : string[] {
  if (types === undefined) {
    return []
  }
  const urls : string[] = [];
  const n : number = types.length;

  for (let i = 0; i < n; i++) {
    urls.push(`/type_logos/${types[i]}.png`);
  }

  return urls;
}

export function getTypeSymbolUrl(type : PokemonType | undefined) : string {
  if (type === undefined) {
    return ""
  }
  
  return `/type_symbols/${type.toLowerCase()}.png`
}
