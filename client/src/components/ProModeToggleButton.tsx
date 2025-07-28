import { ToggleSlider }  from "react-toggle-slider";
import { Colors } from "../styles/colors";
import "../styles/general.css";
import { useState } from "react";
import { useProMode } from "../context";

export const ProModeToggleButton = () => {
  // visuals 
  const backgroundColor : string = Colors.gray;
  const activeColor : string = Colors.blueDark

  // set global context
  const { isProMode, setIsProMode } = useProMode();

  const handleToggle = () => {
    setIsProMode(!isProMode);
  }

  return (
    <div className="horizontal-center">
      <span>Pro Mode</span>
      <ToggleSlider
        barBackgroundColor={backgroundColor}
        barBackgroundColorActive={activeColor}
        onToggle={handleToggle}
      />
    </div>
  );
}