import React from 'react';
import { MapContainer, TileLayer, Polyline, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { Icon } from 'leaflet';
import { Accessibility } from 'lucide-react';
import { Journey, Section } from '../../api/directions';

// Fix for default marker icons in React-Leaflet
const defaultIcon = new Icon({
  iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
  iconRetinaUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
});

interface MapViewProps {
  journeys: Journey[];
}

export function MapView({ journeys }: MapViewProps) {
  if (journeys.length === 0) return null;

  const journey = journeys[0]; // We'll display the first journey for now

  const getCoordinates = (section: Section): [number, number] | null => {
    if (section.from && section.from) {
      return [section.from.coordinates.lon, section.from.coordinates.lat];
    }
    return null;
  };

  const pathPoints = journey.sections
    .map(getCoordinates)
    .filter((coord): coord is [number, number] => coord !== null);

  const startPoint = pathPoints[0];
  const endPoint = pathPoints[pathPoints.length - 1];

  const accessiblePoints = journey.sections
    .filter(section => section.type === 'transfer' && section.mode === 'walking')
    .map(section => ({
      position: getCoordinates(section) as [number, number],
      type: 'elevator' as const,
      status: section.disruptions.length > 0 ? 'maintenance' as const : 'operational' as const
    }))
    .filter(point => point.position !== null);

  return (
    <div className="h-[60vh] w-full rounded-lg overflow-hidden shadow-lg">
      <MapContainer
        bounds={pathPoints}
        className="h-full w-full"
        zoom={13}
        center={startPoint}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        
        {/* Main path */}
        <Polyline
          positions={pathPoints}
          pathOptions={{ color: 'blue', weight: 4 }}
        />

        {/* Start marker */}
        <Marker position={startPoint} icon={defaultIcon}>
          <Popup>Point de départ</Popup>
        </Marker>

        {/* End marker */}
        <Marker position={endPoint} icon={defaultIcon}>
          <Popup>Destination</Popup>
        </Marker>

        {/* Accessible points markers */}
        {accessiblePoints.map((point, index) => (
          <Marker
            key={index}
            position={point.position}
            icon={defaultIcon}
          >
            <Popup>
              <div className="flex flex-col gap-2">
                <div className="flex items-center gap-2">
                  <Accessibility className="h-5 w-5 text-blue-600" />
                  <span className="font-medium">
                    {point.type === 'elevator' ? 'Ascenseur' : 'Rampe d\'accès'}
                  </span>
                </div>
                <span className={`text-sm ${
                  point.status === 'operational' ? 'text-green-600' : 'text-red-600'
                }`}>
                  {point.status === 'operational' ? 'En service' : 'En maintenance'}
                </span>
              </div>
            </Popup>
          </Marker>
        ))}

        {/* Waypoint markers */}
        {pathPoints.slice(1, -1).map((point, index) => (
          <Marker key={index} position={point} icon={defaultIcon}>
            <Popup>Point de passage {index + 1}</Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}