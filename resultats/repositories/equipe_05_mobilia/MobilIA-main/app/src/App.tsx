import React, { useState } from 'react';
import { Menu, MoonStar, Sun, Globe2, Mic } from 'lucide-react';
import { WelcomeScreen } from './components/WelcomeScreen';
import { ChatInterface } from './components/ChatInterface';
import { VisualInterface } from './components/AccessibilityInterfaces/VisualInterface';
import { HearingInterface } from './components/AccessibilityInterfaces/HearingInterface';
import { MobilityInterface } from './components/AccessibilityInterfaces/MobilityInterface';
import { usePreferences } from './store/preferences';

type InterfaceType = 'welcome' | 'visual' | 'hearing' | 'mobility' | 'chat';
type Language = 'fr' | 'en' | 'es' | 'de';

function App() {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [currentInterface, setCurrentInterface] = useState<InterfaceType>('welcome');
  const [language, setLanguage] = useState<Language>('fr');
  const { disabilities, clearPreferences } = usePreferences();

  const handleReset = () => {
    clearPreferences();
    setCurrentInterface('welcome');
  };

  const renderInterface = () => {
    switch (currentInterface) {
      case 'visual':
        return <VisualInterface />;
      case 'hearing':
        return <HearingInterface />;
      case 'mobility':
        return <MobilityInterface />;
      case 'chat':
        return <ChatInterface />;
      default:
        return <WelcomeScreen onComplete={() => setCurrentInterface('mobility')} />;
    }
  };

  const languages: { code: Language; label: string }[] = [
    { code: 'fr', label: 'Français' },
    { code: 'en', label: 'English' },
    { code: 'es', label: 'Español' },
    { code: 'de', label: 'Deutsch' },
  ];

  return (
    <div className={`min-h-screen ${isDarkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <header className="bg-white dark:bg-gray-800 shadow-sm">
        <div className="max-w-4xl mx-auto px-4 py-3 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <button 
              onClick={handleReset}
              className="text-xl font-semibold text-gray-900 dark:text-white hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
            >
              Mobil-IA
            </button>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={() => setCurrentInterface('chat')}
              className="px-4 py-2 text-sm font-medium text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 flex items-center"
            >
              <Mic className="h-4 w-4 mr-2" />
              Assistant Vocal
            </button>
            <button
              onClick={() => setIsDarkMode(!isDarkMode)}
              className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700"
              aria-label={isDarkMode ? 'Activer le mode clair' : 'Activer le mode sombre'}
            >
              {isDarkMode ? (
                <Sun className="h-5 w-5 text-gray-600 dark:text-gray-300" />
              ) : (
                <MoonStar className="h-5 w-5 text-gray-600" />
              )}
            </button>
            <button
              className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700"
              aria-label="Menu"
            >
              <Menu className="h-5 w-5 text-gray-600 dark:text-gray-300" />
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-4xl mx-auto p-4">
        {renderInterface()}
      </main>

      <footer className="max-w-4xl mx-auto px-4 py-3 flex items-center justify-between text-sm text-gray-600 dark:text-gray-400">
        <p>Mobil-IA - Votre assistant de mobilité accessible © 2024</p>
        <div className="flex items-center gap-2">
          <Globe2 className="h-4 w-4" />
          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value as Language)}
            className="bg-transparent border-none text-sm text-gray-600 dark:text-gray-400 focus:ring-0 cursor-pointer hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
            aria-label="Sélectionner la langue"
          >
            {languages.map(({ code, label }) => (
              <option key={code} value={code}>
                {label}
              </option>
            ))}
          </select>
        </div>
      </footer>
    </div>
  );
}

export default App;