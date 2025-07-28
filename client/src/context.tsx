import React, { useState, createContext, useContext, type ReactNode } from "react";

// ----------- ProMode context ---------------
type ProModeContextType = {
  isProMode: boolean;
  setIsProMode: (value: boolean) => void;
};

const ProModeContext = createContext<ProModeContextType | undefined>(undefined);

export const ProModeProvider = ({ children } : { children : React.ReactNode }) => {
  const [isProMode, setIsProMode] = useState(false);

  return (
    <ProModeContext.Provider value={{ isProMode, setIsProMode }}>
      {children}
    </ProModeContext.Provider>
  );
};

export const useProMode = () =>  {
  const context = useContext(ProModeContext);
  if (!context) throw new Error("useProMode must be used within ProModeProvider");
  return context;
};

// --- Root provider for all "global" varabiles ---
export const RootProvider = ({ children }: { children: ReactNode }) => {
  return (
    <ProModeProvider>
      {children}
    </ProModeProvider>
  );
};
