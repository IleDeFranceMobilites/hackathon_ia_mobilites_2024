import axios from 'axios';
import { getCurrentLocation } from '../utils/geolocation';

interface ReverseGeocodeResult {
    features: {
        properties: {
            label: string;
            score: number;
            housenumber: string;
            id: string;
            name: string;
            postcode: string;
            citycode: string;
            x: number;
            y: number;
            city: string;
            context: string;
            type: string;
            importance: number;
            street: string;
        };
    }[];
}

export async function reverseGeocode(lat: number, lon: number): Promise<string> {

    
    try {
        const response = await axios.get<ReverseGeocodeResult>(
            `https://api-adresse.data.gouv.fr/reverse/?lon=${lon}&lat=${lat}`
        );

        if (response.data.features.length > 0) {
            const address = response.data.features[0].properties;
            return `${address.housenumber || ''} ${address.street}, ${address.postcode} ${address.city}`.trim();
        } else {
            throw new Error('No address found for the given coordinates');
        }
    } catch (error) {
        console.error('Error in reverse geocoding:', error);
        throw error;
    }
}

interface GeocodeResult {
    features: {
        geometry: {
            coordinates: [number, number];
        };
        properties: {
            label: string;
            score: number;
            id: string;
            name: string;
            postcode: string;
            citycode: string;
            x: number;
            y: number;
            city: string;
            context: string;
            type: string;
            importance: number;
            street?: string;
        };
    }[];
}

export async function geocode(address: string): Promise<{ lat: number; lon: number; label: string }[]> {
    try {
        const { latitude, longitude } = await getCurrentLocation();
        const response = await axios.get<GeocodeResult>(
            `https://api-adresse.data.gouv.fr/search/?q=${encodeURIComponent(address)}&limit=10&lat=${latitude}&lon=${longitude}`
        );

        if (response.data.features.length > 0) {
            return response.data.features.map(feature => {
                const [lon, lat] = feature.geometry.coordinates;
                return {
                    lat,
                    lon,
                    label: feature.properties.label
                };
            });
        } else {
            throw new Error('No coordinates found for the given address');
        }
    } catch (error) {
        console.error('Error in geocoding:', error);
        throw error;
    }
}
