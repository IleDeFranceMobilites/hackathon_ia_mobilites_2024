
import React, { useState } from 'react';
import { Volume2, Ear, Mic } from 'lucide-react';

interface AccessibilityFeaturesProps {
  disabilities: string[];
}

export function AccessibilityFeatures({ disabilities }: AccessibilityFeaturesProps) {
  const [isReading, setIsReading] = useState(false);
  const [isListening, setIsListening] = useState(false);

  return (
    <>
      {disabilities.includes('visual') && (
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-lg">
          <h3 className="text-xl font-semibold mb-4 text-gray-900 dark:text-white">Paramètres de lecture</h3>
          <div className="space-y-4">
            <div>
              <label htmlFor="speed" className="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">
                Vitesse de lecture
              </label>
              <input
                type="range"
                id="speed"
                min="0.5"
                max="2"
                step="0.1"
                defaultValue="1"
                className="w-full accent-blue-600 dark:accent-blue-400"
              />
            </div>
            <div>
              <label htmlFor="pitch" className="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">
                Hauteur de la voix
              </label>
              <input
                type="range"
                id="pitch"
                min="0.5"
                max="2"
                step="0.1"
                defaultValue="1"
                className="w-full accent-blue-600 dark:accent-blue-400"
              />
            </div>
          </div>
          <button
            onClick={() => setIsReading(!isReading)}
            className={`mt-4 px-4 py-2 rounded-lg transition-colors ${
              isReading ? 'bg-red-600 hover:bg-red-700' : 'bg-green-600 hover:bg-green-700'
            } text-white`}
            aria-label={isReading ? "Arrêter la lecture" : "Lire à haute voix"}
          >
            <Volume2 className="h-6 w-6 inline-block mr-2" />
            {isReading ? "Arrêter la lecture" : "Lire à haute voix"}
          </button>
        </div>
      )}

      {disabilities.includes('hearing') && (
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-lg">
          <div className="flex items-center gap-3 mb-4">
            <Ear className="h-6 w-6 text-blue-600 dark:text-blue-400" />
            <h3 className="text-xl font-semibold text-gray-900 dark:text-white">Alertes textuelles</h3>
          </div>
          <div className="space-y-3 text-sm">
            <div className="p-3 bg-blue-50 dark:bg-blue-900/30 rounded-lg text-blue-900 dark:text-blue-100">
              "Le prochain train arrive dans 3 minutes"
            </div>
            <div className="p-3 bg-yellow-50 dark:bg-yellow-900/30 rounded-lg text-yellow-900 dark:text-yellow-100">
              "Attention à la marche en descendant du train"
            </div>
          </div>
          <button
            onClick={() => setIsListening(!isListening)}
            className={`mt-4 px-4 py-2 rounded-lg transition-colors ${
              isListening ? 'bg-red-600 hover:bg-red-700' : 'bg-green-600 hover:bg-green-700'
            } text-white`}
            aria-label={isListening ? "Arrêter la transcription" : "Démarrer la transcription"}
          >
            <Mic className={`h-6 w-6 inline-block mr-2 ${isListening ? 'animate-pulse' : ''}`} />
            {isListening ? "Arrêter la transcription" : "Démarrer la transcription"}
          </button>
        </div>
      )}
    </>
  );
}

