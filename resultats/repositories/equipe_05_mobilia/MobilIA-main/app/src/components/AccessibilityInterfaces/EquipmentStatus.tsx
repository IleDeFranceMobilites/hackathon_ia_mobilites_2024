import React from 'react';
import { GalleryVertical } from 'lucide-react';

export function EquipmentStatus() {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-lg">
      <h3 className="text-xl font-semibold mb-4 text-gray-900 dark:text-white">État des équipements</h3>
      <div className="space-y-3">
        <div className="flex items-center justify-between p-3 bg-green-50 dark:bg-green-900/30 rounded-lg">
          <div className="flex items-center gap-3">
            <GalleryVertical className="h-5 w-5 text-green-600 dark:text-green-400" />
            <span className="text-green-900 dark:text-green-100">Ascenseur Quai 1</span>
          </div>
          <span className="text-green-600 dark:text-green-400">En service</span>
        </div>
        <div className="flex items-center justify-between p-3 bg-red-50 dark:bg-red-900/30 rounded-lg">
          <div className="flex items-center gap-3">
            <GalleryVertical className="h-5 w-5 text-red-600 dark:text-red-400" />
            <span className="text-red-900 dark:text-red-100">Ascenseur Quai 2</span>
          </div>
          <span className="text-red-600 dark:text-red-400">Hors service</span>
        </div>
      </div>
    </div>
  );
}