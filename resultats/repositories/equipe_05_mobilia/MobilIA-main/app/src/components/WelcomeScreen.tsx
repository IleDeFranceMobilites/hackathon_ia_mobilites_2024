import React from 'react';
import { Bot, Eye, Ear, Accessibility, Brain } from 'lucide-react';
import { usePreferences, DisabilityType } from '../store/preferences';

interface DisabilityOption {
  type: DisabilityType;
  icon: React.ReactNode;
  title: string;
  description: string;
}

interface WelcomeScreenProps {
  onComplete: () => void;
}

export function WelcomeScreen({ onComplete }: WelcomeScreenProps) {
  const { disabilities, addDisability, removeDisability, hasDisability } = usePreferences();

  const options: DisabilityOption[] = [
    {
      type: 'visual',
      icon: <Eye className="h-12 w-12 text-blue-600 mb-4 group-hover:scale-110 transition-transform" />,
      title: 'Malvoyant',
      description: 'Lecture audio des panneaux et informations visuelles'
    },
    {
      type: 'hearing',
      icon: <Ear className="h-12 w-12 text-blue-600 mb-4 group-hover:scale-110 transition-transform" />,
      title: 'Malentendant',
      description: 'Conversion des annonces sonores en texte'
    },
    {
      type: 'mobility',
      icon: <Accessibility className="h-12 w-12 text-blue-600 mb-4 group-hover:scale-110 transition-transform" />,
      title: 'Mobilité réduite',
      description: 'Itinéraires optimisés et accessibles'
    },
    {
      type: 'cognitive',
      icon: <Brain className="h-12 w-12 text-blue-600 mb-4 group-hover:scale-110 transition-transform" />,
      title: 'Trouble cognitif',
      description: 'Interface simplifiée et guidage pas à pas'
    }
  ];

  const handleToggleDisability = (type: DisabilityType) => {
    if (hasDisability(type)) {
      removeDisability(type);
    } else {
      addDisability(type);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-[calc(100vh-12rem)] text-center px-4">
      <Bot className="h-24 w-24 text-blue-600 mb-8" aria-hidden="true" />
      <h2 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
        Bienvenue sur Mobil-IA
      </h2>
      <p className="text-xl text-gray-600 dark:text-gray-300 mb-12 max-w-2xl">
        Sélectionnez vos besoins d'accessibilité pour personnaliser votre expérience
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl w-full mb-8">
        {options.map(({ type, icon, title, description }) => (
          <button
            key={type}
            onClick={() => handleToggleDisability(type)}
            className={`flex flex-col items-center p-8 rounded-xl shadow-lg transition-all duration-300 group ${
              hasDisability(type)
                ? 'bg-blue-50 dark:bg-blue-900 border-2 border-blue-500'
                : 'bg-white dark:bg-gray-800 hover:shadow-xl'
            }`}
            aria-pressed={hasDisability(type)}
          >
            {icon}
            <h3 className="text-xl font-semibold mb-2">{title}</h3>
            <p className="text-gray-600 dark:text-gray-300">{description}</p>
          </button>
        ))}
      </div>

      <button
        onClick={onComplete}
        className={`bg-blue-600 text-white px-8 py-3 rounded-lg text-lg font-medium transition-colors ${
          disabilities.length > 0
            ? 'hover:bg-blue-700'
            : 'opacity-50 cursor-not-allowed'
        }`}
        disabled={disabilities.length === 0}
      >
        Continuer
      </button>
    </div>
  );
}