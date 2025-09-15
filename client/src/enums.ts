export enum PokemonType {
  Normal = "Normal",
  Fire = "Fire",
  Water = "Water",
  Electric = "Electric",
  Grass = "Grass",
  Ice = "Ice",
  Fighting = "Fighting",
  Poison = "Poison",
  Ground = "Ground",
  Flying = "Flying",
  Psychic = "Psychic",
  Bug = "Bug",
  Rock = "Rock",
  Ghost = "Ghost",
  Dragon = "Dragon",
  Dark = "Dark",
  Steel = "Steel",
  Fairy = "Fairy",
  Unkown = "Unknown"
}

export enum PokemonDmgClass {
  Physical = "Physical",
  Special = "Special",
  Status = "Status",
  Unkown = "Unkown"
}

export enum Generation {
  Gen1 = "1",
  Gen2 = "2",
  Gen3 = "3",
  Gen4 = "4",
  Gen5 = "5",
  Gen6 = "6",
  Gen7 = "7",
  Gen8 = "8",
  Gen9 = "9",
  INVALID = "-1"
}

export enum LearnMethod {
  LevelUp = "level-up",
  Machine = "machine",
  Egg = "egg",
  Tutor = "tutor",
  Other = "other",
}

export function getGenerationFromString(generationsString : string) : Generation{
  switch (generationsString) {
    case "GenerationI":
      return Generation.Gen1;
    case "GenerationII":
      return Generation.Gen2;
    case "GenerationIII":
      return Generation.Gen3;
    case "GenerationIV":
      return Generation.Gen4;
    case "GenerationV":
      return Generation.Gen5;
    case "GenerationVI":
      return Generation.Gen6;
    case "GenerationVII":
      return Generation.Gen7;
    case "GenerationVIII":
      return Generation.Gen8;
    case "GenerationIX":
      return Generation.Gen9;
    default:
      return Generation.INVALID;
  }
}

