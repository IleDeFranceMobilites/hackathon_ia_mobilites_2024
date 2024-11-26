import React from "react";
import {
  Clock,
  ArrowRight,
  Menu,
  GalleryVertical,
  AlertCircle,
} from "lucide-react";
import { Journey, Section } from "../../api/directions";
import clsx from "clsx";

interface ItineraryViewProps {
  journey: Journey;
  onClose: () => void;
  inline?: boolean;
}

export function ItineraryView({
  journey,
  onClose,
  inline = false,
}: ItineraryViewProps) {
  const from = journey.sections[0]?.from || "";
  const to = journey.sections[journey.sections.length - 1]?.to || "";
  const duration = `${Math.floor(journey.duration / 60)} min`;

  const getSteps = (sections: Section[]) => {
    return sections.map((section) => ({
      instruction: `${
        section.type === "street_network"
          ? "Marcher"
          : section.mode || "Voyager"
      } de ${section.from || ""} à ${section.to || ""}`,
      duration: `${Math.floor(
        (new Date(section.arrival_time).getTime() -
          new Date(section.departure_time).getTime()) /
          60000
      )} min`,
      hasElevator: section.type === "transfer" && section.mode === "walking",
      hasStairs: section.type === "transfer" && section.mode === "walking",
      alert:
        section.disruptions.length > 0
          ? section.disruptions[0].messages.join(". ")
          : undefined,
    }));
  };

  const steps = getSteps(journey.sections);

  return (
    <div
      className={clsx(
        "backdrop-blur-sm z-[9999] flex items-center justify-center p-4",
        !inline && "fixed inset-0 bg-gray-900/50 "
      )}
    >
      <div className="relative bg-white dark:bg-gray-800 rounded-xl shadow-xl max-w-2xl w-full max-h-[80vh] overflow-hidden">
        <div className="sticky top-0 p-6 border-b border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 z-10">
          {!inline && (
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-2xl font-bold">Itinéraire accessible</h3>
              <button
                onClick={onClose}
                className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200"
              >
                ✕
              </button>
            </div>
          )}
          <div className="flex items-center gap-3 text-gray-600 dark:text-gray-300">
            <Clock className="h-5 w-5" />
            <span>{duration}</span>
          </div>
          <div className="mt-4 flex items-center gap-3">
            <div className="flex-1 min-w-0">
              <p className="truncate font-medium">{from}</p>
            </div>
            <ArrowRight className="h-5 w-5 flex-shrink-0" />
            <div className="flex-1 min-w-0">
              <p className="truncate font-medium">{to}</p>
            </div>
          </div>
        </div>

        <div className="overflow-y-auto max-h-[calc(80vh-200px)] p-6">
          <div className="space-y-6">
            {steps.map((step, index) => (
              <div
                key={index}
                className="relative pl-8 border-l-2 border-blue-200 dark:border-blue-800 pb-6 last:pb-0"
              >
                <div className="absolute -left-2 top-0 w-4 h-4 rounded-full bg-blue-600" />
                <div className="space-y-2">
                  <p className="text-lg">{step.instruction}</p>
                  <div className="flex flex-wrap gap-3">
                    {step.hasElevator && (
                      <div className="flex items-center gap-2 text-green-600 bg-green-50 dark:bg-green-900/30 px-3 py-1 rounded-full">
                        <GalleryVertical className="h-4 w-4" />
                        <span>Ascenseur disponible</span>
                      </div>
                    )}
                    {step.hasStairs && (
                      <div className="flex items-center gap-2 text-yellow-600 bg-yellow-50 dark:bg-yellow-900/30 px-3 py-1 rounded-full">
                        <Menu className="h-4 w-4" />
                        <span>Escaliers</span>
                      </div>
                    )}
                  </div>
                  {step.alert && (
                    <div className="flex items-start gap-2 text-red-600 bg-red-50 dark:bg-red-900/30 p-3 rounded-lg mt-2">
                      <AlertCircle className="h-5 w-5 flex-shrink-0" />
                      <span
                        dangerouslySetInnerHTML={{ __html: step.alert }}
                      ></span>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="sticky bottom-0 p-6 border-t border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800">
          <button
            onClick={onClose}
            className="w-full bg-blue-600 text-white py-3 px-6 rounded-lg hover:bg-blue-700 transition-colors"
          >
            Fermer
          </button>
        </div>
      </div>
    </div>
  );
}
