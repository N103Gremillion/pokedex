import { StatBar } from "./StatBar";

interface PokemonStatChartPromps {
  hp : number;
  attack : number;
  defense : number;
  sp_attack : number;
  sp_defense : number;
  speed : number;
}

export const PokemonStatChart = ({ hp, attack, defense, sp_attack, sp_defense, speed } : PokemonStatChartPromps) => {
  return (
    <>
      <StatBar label="HP" value={hp} max={255} color="#ff5959" />
      <StatBar label="Attack" value={attack} max={255} color="#f5ac78" />
      <StatBar label="Defense" value={defense} max={255} color="#fae078" />
      <StatBar label="Sp_Attack" value={sp_attack} max={255} color="#9db7f5" />
      <StatBar label="Sp_Defense" value={sp_defense} max={255} color="#a7db8d" />
      <StatBar label="Speed" value={speed} max={255} color="#fa92b2" />
    </>
  );
}