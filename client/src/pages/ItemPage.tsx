import { useEffect, useState, type SyntheticEvent } from "react";
import { useParams } from "react-router-dom";
import type { ItemData } from "../types";
import { getDetailedItemInfo } from "../api/pokemon_api";
import "../styles/item.css"
import "../styles/general.css"

export const ItemPage = () => {

  const { itemNameString = "" } = useParams<{ itemNameString? : string }>();
  const [ detailedItemData, setDetailedItemData ] = useState<ItemData>({});
  const defaultImageUrl : string = "/public/substitute.png";

  useEffect(() => {
    const runQuery = async () => {
      setDetailedItemData(await getDetailedItemInfo(itemNameString));
      window.scrollTo(0, 0);
    }
    runQuery();
  }, []);

  const handleImageNotFound = (event : SyntheticEvent<HTMLImageElement, Event>) => {
    const img = event.currentTarget;
    img.src = defaultImageUrl;
  }

  return (
    <div className="general-page" style={{display:"flex", flexDirection: "column", alignItems:"center", gap:"40px"}}>
      <h1 className="header">Item Page</h1> 
      <div className="item-info-container">
        <div className="general-item-info-container">
          <img
            src={detailedItemData.imageUrl || defaultImageUrl}
            alt={"Pokemon"}
            className="item-info-img"
            onError= {(error) => handleImageNotFound(error)}
          />
          <h2 style={{justifyContent:"left"}}>{detailedItemData.name}</h2>
        </div>
        <div className="item-info-effects">
          -{detailedItemData.effect}
        </div>
      </div>
    </div>
  );
}