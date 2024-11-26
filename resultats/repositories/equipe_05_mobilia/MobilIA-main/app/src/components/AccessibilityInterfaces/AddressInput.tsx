import React, { useState } from 'react';
import { MapPin } from 'lucide-react';

interface AddressInputProps {
  value: string;
  onChange: (value: string) => void;
  onGeolocation?: () => void;
  placeholder: string;
}

import { geocode } from '../../api/geocoding';

export function AddressInput({ value, onChange, onGeolocation, placeholder }: AddressInputProps) {
  const [suggestions, setSuggestions] = useState<string[]>([]);

  const handleInputChange = async (inputValue: string) => {
    onChange(inputValue);
    if (inputValue.length > 3) { // Fetch suggestions only if input length is greater than 3
      try {
        const response = await geocode(inputValue);
        setSuggestions(response.map((item: { label: string }) => item.label)); // Assuming geocode returns an array of objects with a label
      } catch (error) {
        console.error('Error fetching address suggestions:', error);
        setSuggestions([]);
      }
    } else {
      setSuggestions([]);
    }
  };

  const handleSuggestionClick = (suggestion: string) => {
    onChange(suggestion);
    setSuggestions([]); // Clear suggestions after selection
  };

  return (
    <div className="relative flex gap-2">
      <input
        type="text"
        value={value}
        onChange={(e) => handleInputChange(e.target.value)}
        placeholder={placeholder}
        className="flex-1 p-3 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400"
        aria-label={placeholder}
      />
      {onGeolocation && (
        <button
          onClick={onGeolocation}
          className="px-3 bg-blue-100 dark:bg-blue-900 text-blue-600 dark:text-blue-300 rounded-lg hover:bg-blue-200 dark:hover:bg-blue-800 transition-colors"
          aria-label="Utiliser ma position actuelle"
        >
          <MapPin className="h-6 w-6" />
        </button>
      )}
      {suggestions.length > 0 && (
        <ul className="absolute z-10 bg-white border border-gray-300 rounded-lg shadow-lg mt-14 w-full">
          {suggestions.map((suggestion, index) => (
            <li key={index} className="p-2 hover:bg-gray-200 cursor-pointer" onClick={() => handleSuggestionClick(suggestion)}>
              {suggestion}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
