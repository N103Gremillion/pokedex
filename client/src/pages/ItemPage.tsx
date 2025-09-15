import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import type { ItemData } from "../types";
import { getDetailedItemInfo } from "../api/pokemon_api";

export const ItemPage = () => {
  const { itemNameString = "" } = useParams<{ itemNameString? : string }>();
  const [ detailedItemData, setDetailedItemData ] = useState<ItemData>({});

  useEffect(() => {
    const runQuery = async () => {
      setDetailedItemData(await getDetailedItemInfo(itemNameString));
    }
    runQuery();
  }, []);

  console.log(detailedItemData);

  return (
    <div className="general-page">
      <h1>Item Page</h1>
    </div>
  );
}