import { create } from 'zustand';

type ProModeStore = {
  isProMode: boolean;
  setIsProMode: (value: boolean) => void;
};

export const useProModeStore = create<ProModeStore>((set) => ({
  isProMode: false,
  setIsProMode: (value) => set({ isProMode: value }),
}));