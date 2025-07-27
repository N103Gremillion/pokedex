import { ToggleSlider }  from "react-toggle-slider";
import { Colors } from "../styles/colors";
import "../styles/general.css";
import { useState } from "react";

export const ProModeToggleButton = () => {
  // visuals 
  const backgroundColor : string = Colors.gray;
  const activeColor : string = Colors.grayDark

  // state
  const [isProMode, setIsProMode] = useState(false);

  const handleToggle = (newState : boolean) => {
    setIsProMode(newState);
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