import { reverseGeocode } from '../api/geocoding';

export const getCurrentLocation = async (): Promise<{ address: string; latitude: number; longitude: number }> => {
    try {
        const position = await new Promise<GeolocationPosition>((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(resolve, reject);
        });
        const { latitude, longitude } = position.coords;
        const address = await reverseGeocode(latitude, longitude);
        return { address, latitude, longitude };
    } catch (error) {
        console.error('Erreur de géolocalisation:', error);
        throw new Error('Impossible d\'obtenir votre position actuelle');
    }
};