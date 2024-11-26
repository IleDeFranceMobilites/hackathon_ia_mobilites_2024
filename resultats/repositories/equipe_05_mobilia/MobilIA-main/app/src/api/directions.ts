import axios from 'axios';

export interface Disruption {
  effect: string;
  id: string;
  messages: string[];
  severity: string;
  status: string;
}

export interface Section {
  arrival_time: string;
  departure_time: string;
  from: string | null;
  mode: string | null;
  to: string | null;
  type: string;
  disruptions: Disruption[];
}

export interface Journey {
  arrival_date_time: string;
  co2_emission: number;
  departure_date_time: string;
  duration: number;
  nb_transfers: number;
  sections: Section[];
  status: string;
  type: string;
  walking_distance: number;
}

export async function getDirections(
  originLong: number,
  originLat: number,
  destLong: number,
  destLat: number,
  dateTime: string,
  wheelchair: boolean = false
): Promise<Journey[]> {
  try {
    const response = await axios.get('http://localhost:8000/api/directions', {
      params: {
        origin_long: originLong,
        origin_lat: originLat,
        dest_long: destLong,
        dest_lat: destLat,
        datetime: dateTime,
        wheelchair: wheelchair
      }
    });

    return response.data;
  } catch (error) {
    console.error('Error fetching directions:', error);
    throw error;
  }
}
