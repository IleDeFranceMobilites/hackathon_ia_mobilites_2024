import React, { useState } from "react";
import { Accessibility, Map, Loader2 } from "lucide-react";
import { ItineraryView } from "./ItineraryView";
import { MapView } from "./MapView";
import { AccessibilityStatusBar } from "./AccessibilityStatusBar";
import { usePreferences } from "../../store/preferences";
import { getDirections, Journey } from "../../api/directions";
import { geocode, reverseGeocode } from "../../api/geocoding";
import { AddressInput } from "./AddressInput";
import { AccessibilityFeatures } from "./AccessibilityFeatures";
import { EquipmentStatus } from "./EquipmentStatus";
import { getCurrentLocation } from "../../utils/geolocation";

export function MobilityInterface() {
  const { disabilities, hasDisability } = usePreferences();
  const [departure, setDeparture] = useState("");
  const [arrival, setArrival] = useState("");
  const [showItinerary, setShowItinerary] = useState(false);
  const [journeys, setJourneys] = useState<Journey[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleGeolocation = async () => {
    try {
      const { address } = await getCurrentLocation();
      setDeparture(address);
    } catch (error) {
      console.error("Erreur de géolocalisation:", error);
      setError("Impossible d'obtenir votre position actuelle");
    }
  };

  const fetchDirections = async () => {
    setLoading(true);
    setError(null);
    try {
      const departureCoords = await geocode(departure);
      const arrivalCoords = await geocode(arrival);
      const dateTime = new Date().toISOString();
      const wheelchair = hasDisability("mobility");

      const fetchedJourneys = await getDirections(
        departureCoords[0].lon,
        departureCoords[0].lat,
        arrivalCoords[0].lon,
        arrivalCoords[0].lat,
        dateTime,
        wheelchair
      );
      setJourneys(fetchedJourneys);
      setShowItinerary(true);
    } catch (err) {
      setError("Erreur lors de la récupération des directions");
      console.error("Error fetching directions:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6 pb-16">
      <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-lg">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
          Itinéraire accessible
        </h2>
        <div className="space-y-4">
          <AddressInput
            value={departure}
            onChange={setDeparture}
            onGeolocation={handleGeolocation}
            placeholder="Point de départ"
          />
          <AddressInput
            value={arrival}
            onChange={setArrival}
            placeholder="Point d'arrivée"
          />
          <div className="flex gap-2">
            <button
              onClick={fetchDirections}
              className="flex-1 flex items-center justify-center gap-3 bg-blue-600 text-white py-4 px-6 rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              disabled={!departure || !arrival || loading}
            >
              {loading ? (
                <Loader2 className="h-6 w-6 animate-spin" />
              ) : (
                <Map className="h-6 w-6" />
              )}
              {loading ? "Chargement..." : "Calculer l'itinéraire"}
            </button>
          </div>
        </div>
      </div>

      {error && (
        <div
          className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative"
          role="alert"
        >
          <strong className="font-bold">Erreur!</strong>
          <span className="block sm:inline"> {error}</span>
        </div>
      )}

      {/* {journeys.length > 0 && <MapView journeys={journeys} />} */}

      <AccessibilityFeatures disabilities={disabilities} />

      {hasDisability("mobility") && <EquipmentStatus />}

      <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-lg">
        <h3 className="text-xl font-semibold mb-4 text-gray-900 dark:text-white">
          Assistance
        </h3>
        <button className="w-full flex items-center justify-center gap-3 bg-purple-600 text-white py-4 px-6 rounded-lg hover:bg-purple-700 transition-colors">
          <Accessibility className="h-6 w-6" />
          Demander une assistance
        </button>
      </div>

      {showItinerary && journeys.length > 0 && (
        <ItineraryView
          inline={false}
          journey={journeys[0]}
          onClose={() => setShowItinerary(false)}
        />
      )}

      <AccessibilityStatusBar activeFeatures={disabilities} />
    </div>
  );
}
