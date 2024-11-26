import React, { useState } from "react";
import { Bot, User } from "lucide-react";
import { ItineraryView } from "./AccessibilityInterfaces/ItineraryView";
import { Journey } from "../api/directions";

interface ChatMessageProps {
  message: string;
  journeys?: Journey[];
  isBot: boolean;
}

export function ChatMessage({ message, journeys, isBot }: ChatMessageProps) {
  const [showItinerary, setShowItinerary] = useState<{
    isOpen: boolean;
    journey?: Journey;
  }>({ isOpen: false }); // First suggestion open by default

  const handleJourneyClick = (journey: Journey) => {
    setShowItinerary({ isOpen: true, journey });
  };

  return (
    <>
      <div
        className={`flex gap-3 ${isBot ? "bg-blue-50" : ""} p-4 rounded-lg`}
        role="listitem"
        aria-label={`${isBot ? "Assistant" : "User"} message`}
      >
        <div className="flex-shrink-0">
          {isBot ? (
            <Bot className="h-8 w-8 text-blue-600" aria-hidden="true" />
          ) : (
            <User className="h-8 w-8 text-gray-600" aria-hidden="true" />
          )}
        </div>
        <div className="flex-1">
          <p className="text-gray-800 font-semibold leading-relaxed whitespace-pre-wrap">
            {message}
          </p>
          {journeys && journeys.length > 0 && (
            <div className="mt-2 space-y-2">
              {journeys.map((journey, index) => (
                <div
                  key={index}
                  onClick={() => handleJourneyClick(journey)}
                  className={`cursor-pointer p-4 border border-gray-300 rounded-lg shadow-md hover:bg-blue-100 transition-colors ${
                    index === 0 ? "bg-blue-50" : "bg-white"
                  }`}
                >
                  <div className="flex justify-between items-center mb-2">
                    <p className="text-blue-600 font-bold">{`Itinéraire ${
                      index + 1
                    }`}</p>
                    <p className="text-gray-600">{`${Math.floor(journey.duration / 60)} min ${journey.duration % 60} s`}</p>
                  </div>
                  <div className="flex justify-between items-center mb-2">
                    <p className="text-gray-600">Type:</p>
                    <p className="text-gray-800 font-semibold">{journey.type}</p>
                  </div>
                  <div className="flex justify-between items-center mb-2">
                    <p className="text-gray-600">Distance à pied:</p>
                    <p className="text-gray-800 font-semibold">{`${(journey.walking_distance / 1000).toFixed(2)} km`}</p>
                  </div>
                  <div className="flex justify-between items-center mb-2">
                    <p className="text-gray-600">Départ:</p>
                    <p className="text-gray-800 font-semibold">
                      {new Date(
                        journey.departure_date_time.replace(
                          /(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})/,
                          "$1-$2-$3T$4:$5:$6"
                        )
                      ).toLocaleString("fr-FR", {
                        year: "numeric",
                        month: "numeric",
                        day: "numeric",
                        hour: "2-digit",
                        minute: "2-digit",
                      })}
                    </p>
                  </div>
                  <div className="flex justify-between items-center mb-2">
                    <p className="text-gray-600">Arrivée:</p>
                    <p className="text-gray-800 font-semibold">
                      {new Date( journey.arrival_date_time.replace(
                          /(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})/,
                          "$1-$2-$3T$4:$5:$6"
                        )).toLocaleString(
                        "fr-FR",
                        {
                          year: "numeric",
                          month: "numeric",
                          day: "numeric",
                          hour: "2-digit",
                          minute: "2-digit",
                        }
                      )}
                    </p>
                  </div>
                  <div className="flex justify-between items-center mb-2">
                    <p className="text-gray-600">Nombre de transferts:</p>
                    <p className="text-gray-800 font-semibold">{journey.nb_transfers}</p>
                  </div>
                  <div className="flex justify-between items-center mb-2">
                    <p className="text-gray-600">Émission CO2:</p>
                    <p className="text-gray-800 font-semibold">{`${journey.co2_emission.toFixed(2)} g`}</p>
                  </div>
                 
                  {journey.sections && journey.sections.length > 0 && (
                    <div className="mt-4 bg-gray-100 rounded-lg p-4 shadow-inner">
                      <h3 className="text-lg font-semibold text-blue-600 mb-3">Sections du trajet</h3>
                      <ul className="space-y-4">
                        {journey.sections.map((section, idx) => (
                          <li key={idx} className="bg-white rounded-md p-3 shadow-sm">
                            <div className="flex items-center">
                              {section.type === 'public_transport' ? (
                                <>
                                  <span className={`mr-2 text-2xl ${section.mode === 'bus' ? 'text-red-500' : 'text-blue-500'}`}>
                                    {section.mode === 'bus' ? '🚌' : '🚊'}
                                  </span>
                                  <span className="font-medium">{section.from}</span>
                                  <span className="mx-2">→</span>
                                  <span className="font-medium">{section.to}</span>
                                </>
                              ) : (
                                <>
                                  <span className="mr-2 text-2xl">🚶</span>
                                  <span className="font-medium">{section.type}</span>
                                  <span className="mx-2">de</span>
                                  <span className="font-medium">{section.from}</span>
                                  <span className="mx-2">à</span>
                                  <span className="font-medium">{section.to}</span>
                                </>
                              )}
                            </div>
                            {section.disruptions && section.disruptions.length > 0 && (
                              <div className="mt-2 bg-red-100 rounded p-2">
                                <p className="text-red-600 font-semibold mb-1">⚠️ Perturbations:</p>
                                <ul className="list-disc list-inside text-red-700">
                                  {section.disruptions.flatMap((disruption, disruptionIdx) =>
                                    disruption.messages.map((message, messageIdx) => (
                                      <li key={`${disruptionIdx}-${messageIdx}`} className="text-sm">
                                        {message}
                                      </li>
                                    ))
                                  )}
                                </ul>
                              </div>
                            )}
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
      {showItinerary.isOpen && showItinerary.journey && (
        <ItineraryView
          journey={showItinerary.journey}
          onClose={() => setShowItinerary({ isOpen: false })}
        />
      )}
    </>
  );
}
