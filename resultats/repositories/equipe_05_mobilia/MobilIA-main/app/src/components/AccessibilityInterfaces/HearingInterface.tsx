import React, { useState } from 'react';
import { MessageSquare, Mic, AlertTriangle } from 'lucide-react';

export function HearingInterface() {
  const [isListening, setIsListening] = useState(false);

  return (
    <div className="space-y-6 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-lg">
        <h2 className="text-2xl font-bold mb-4">Transcription en direct</h2>
        <div className="space-y-4">
          <button
            onClick={() => setIsListening(!isListening)}
            className={`w-full flex items-center justify-center gap-3 ${
              isListening ? 'bg-red-600 hover:bg-red-700' : 'bg-blue-600 hover:bg-blue-700'
            } text-white py-4 px-6 rounded-lg transition-colors`}
            aria-label={isListening ? "Arrêter l'écoute" : "Commencer l'écoute"}
          >
            <Mic className={`h-6 w-6 ${isListening ? 'animate-pulse' : ''}`} />
            {isListening ? "Arrêter la transcription" : "Démarrer la transcription"}
          </button>

          <div className="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 min-h-[200px]">
            <p className="text-gray-600 dark:text-gray-400">
              {isListening ? "Transcription en cours..." : "Appuyez sur le bouton pour démarrer la transcription"}
            </p>
          </div>
        </div>
      </div>

      <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-lg">
        <h3 className="text-xl font-semibold mb-4">Alertes visuelles</h3>
        <div className="space-y-4">
          <div className="flex items-center gap-3 p-4 bg-yellow-50 dark:bg-yellow-900/30 rounded-lg">
            <AlertTriangle className="h-6 w-6 text-yellow-600 dark:text-yellow-500" />
            <span>Prochain arrêt : Gare Centrale</span>
          </div>
          <div className="flex items-center gap-3 p-4 bg-blue-50 dark:bg-blue-900/30 rounded-lg">
            <MessageSquare className="h-6 w-6 text-blue-600 dark:text-blue-500" />
            <span>Information : Retard de 5 minutes</span>
          </div>
        </div>
      </div>
    </div>
  );
}