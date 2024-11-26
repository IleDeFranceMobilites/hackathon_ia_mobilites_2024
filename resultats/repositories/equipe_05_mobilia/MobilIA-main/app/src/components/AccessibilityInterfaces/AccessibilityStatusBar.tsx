import React from 'react';
import { Eye, Ear, Accessibility, Brain } from 'lucide-react';
import { DisabilityType } from '../../store/preferences';

interface AccessibilityStatusBarProps {
  activeFeatures: DisabilityType[];
}

export function AccessibilityStatusBar({ activeFeatures }: AccessibilityStatusBarProps) {
  const features = [
    {
      type: 'visual' as const,
      icon: Eye,
      label: 'Mode malvoyant',
    },
    {
      type: 'hearing' as const,
      icon: Ear,
      label: 'Mode malentendant',
    },
    {
      type: 'mobility' as const,
      icon: Accessibility,
      label: 'Mode mobilité réduite',
    },
    {
      type: 'cognitive' as const,
      icon: Brain,
      label: 'Mode cognitif',
    },
  ];

  if (activeFeatures.length === 0) return null;

  return (
    <div className="fixed bottom-0 left-0 right-0 bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-700 shadow-lg z-[999999]">
      <div className="max-w-4xl mx-auto px-4 py-2">
        <div className="flex items-center gap-4">
          <span className="text-sm text-gray-600 dark:text-gray-400">Modes actifs :</span>
          <div className="flex gap-3">
            {features.map(({ type, icon: Icon, label }) => (
              activeFeatures.includes(type) && (
                <div
                  key={type}
                  className="flex items-center gap-2 px-3 py-1 bg-blue-50 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400 rounded-full text-sm"
                >
                  <Icon className="h-4 w-4" />
                  <span>{label}</span>
                </div>
              )
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}