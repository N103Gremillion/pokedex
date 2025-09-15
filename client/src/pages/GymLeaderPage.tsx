import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getDetailedGymLeaderInfo } from "../api/pokemon_api";
import type { GymLeaderData } from "../types";

export const GymLeaderPage = () => {
  
  const { gymLeaderNameString = "" } = useParams<{ gymLeaderNameString? : string }>();
  const [detailedGymLeaderData, setDetailedGymLeaderData] = useState<GymLeaderData>({});

  useEffect(() => {
    const runQuery = async () => {
      setDetailedGymLeaderData(await getDetailedGymLeaderInfo(gymLeaderNameString));
    }
    runQuery();
  }, []);

  return (
    <div className="general-page">
      <h1>Gym Leader Page</h1>
    </div>
  );
}