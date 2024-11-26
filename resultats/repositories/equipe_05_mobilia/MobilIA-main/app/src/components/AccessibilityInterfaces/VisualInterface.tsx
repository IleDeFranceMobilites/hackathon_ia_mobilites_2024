import React, { useState } from 'react';
import { Camera, Volume2, VolumeX } from 'lucide-react';

export function VisualInterface() {
  const [isReading, setIsReading] = useState(false);

  return (
    <div className="space-y-6 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-lg">
        <h2 className="text-2xl font-bold mb-4">Mode Lecture</h2>
        <div className="space-y-4">
          <button
            onClick={() => setIsReading(!isReading)}
            className="w-full flex items-center justify-center gap-3 bg-blue-600 text-white py-4 px-6 rounded-lg hover:bg-blue-700 transition-colors"
            aria-label={isReading ? "Arrêter la lecture" : "Commencer la lecture"}
          >
            {isReading ? <VolumeX className="h-6 w-6" /> : <Volume2 className="h-6 w-6" />}
            {isReading ? "Arrêter la lecture" : "Lire le texte à haute voix"}
          </button>

          <button
            className="w-full flex items-center justify-center gap-3 bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-white py-4 px-6 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors"
            aria-label="Scanner un texte avec la caméra"
          >
            <Camera className="h-6 w-6" />
            Scanner un texte
          </button>
        </div>
      </div>

      <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-lg">
        <h3 className="text-xl font-semibold mb-4">Paramètres de lecture</h3>
        <div className="space-y-4">
          <div>
            <label htmlFor="speed" className="block text-sm font-medium mb-2">
              Vitesse de lecture
            </label>
            <input
              type="range"
              id="speed"
              min="0.5"
              max="2"
              step="0.1"
              defaultValue="1"
              className="w-full"
            />
          </div>
          <div>
            <label htmlFor="pitch" className="block text-sm font-medium mb-2">
              Hauteur de la voix
            </label>
            <input
              type="range"
              id="pitch"
              min="0.5"
              max="2"
              step="0.1"
              defaultValue="1"
              className="w-full"
            />
          </div>
        </div>
      </div>
    </div>
  );
}