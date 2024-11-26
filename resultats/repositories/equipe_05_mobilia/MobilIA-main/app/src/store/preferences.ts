import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export type DisabilityType = 'visual' | 'hearing' | 'mobility' | 'cognitive';

interface PreferencesState {
  disabilities: DisabilityType[];
  addDisability: (type: DisabilityType) => void;
  removeDisability: (type: DisabilityType) => void;
  clearPreferences: () => void;
  hasDisability: (type: DisabilityType) => boolean;
}

export const usePreferences = create<PreferencesState>()(
  persist(
    (set, get) => ({
      disabilities: [],
      addDisability: (type) => 
        set((state) => ({
          disabilities: state.disabilities.includes(type) 
            ? state.disabilities 
            : [...state.disabilities, type]
        })),
      removeDisability: (type) =>
        set((state) => ({
          disabilities: state.disabilities.filter(d => d !== type)
        })),
      clearPreferences: () => set({ disabilities: [] }),
      hasDisability: (type) => get().disabilities.includes(type),
    }),
    {
      name: 'mobil-ia-preferences',
    }
  )
);