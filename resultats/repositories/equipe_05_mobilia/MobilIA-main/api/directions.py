import requests

from geocode import GeocodingAPI

class DirectionsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.geocoding_api = GeocodingAPI()
    
    async def get_journey_from_verbal_points(self, start: str, finish: str, datetime_str: str, wheelchair: bool = False):
        """
        Get journey information from verbal start and finish points.
        """
        
        try:
            # Geocode start and finish points
            start_coords = await self.geocoding_api.geocode(start)
            finish_coords = await self.geocoding_api.geocode(finish)
            
            # Get journey info using the geocoded coordinates
            journey_info = self.get_journey_info(
                origin_long=start_coords['lon'],
                origin_lat=start_coords['lat'],
                dest_long=finish_coords['lon'],
                dest_lat=finish_coords['lat'],
                datetime_str=datetime_str,
                wheelchair=wheelchair
            )
            
            return journey_info
        except ValueError as e:
            print(f"Geocoding error: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    def get_journey_info(self, origin_long, origin_lat, dest_long, dest_lat, datetime_str, wheelchair=False):
        """
        Fetch journey information from the transportation API.
        """
        base_url = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/journeys'
        params = {
            'from': f"{origin_long};{origin_lat}",
            'to': f"{dest_long};{dest_lat}",
            'datetime': datetime_str,
            'data_freshness': 'realtime'
        }
        if wheelchair:
            params['wheelchair'] = 'true'
            params['max_duration_to_pt'] = 300

        headers = {
            'Accept': 'application/json',
            'apikey': self.api_key
        }

        # Log the API key being used (for debugging purposes only)
        print(f"Using API key: {self.api_key}")

        try:
            response = requests.get(base_url, headers=headers, params=params)
            response.raise_for_status()
            journey_data = response.json()
            return journey_data
        except requests.exceptions.RequestException as e:
            print(f"API request error: {e}")
            return None

    def parse_journey_data(self, journey_data):
        """
        Parse the journey data and extract relevant information, including disruptions.
        """
        try:
            journeys = journey_data['journeys']
            disruptions = journey_data.get('disruptions', [])
            parsed_journeys = []
            for journey in journeys:
                journey_info = {
                    'duration': journey.get('duration'),
                    'walking_distance': journey.get('distances', {}).get('walking', 0),
                    'departure_date_time': journey.get('departure_date_time'),
                    'arrival_date_time': journey.get('arrival_date_time'),
                    'nb_transfers': journey.get('nb_transfers'),
                    'status': journey.get('status'),
                    'type': journey.get('type'),
                    'co2_emission': journey.get('co2_emission', {}).get('value'),
                    'sections': []
                }
                for section in journey.get('sections', []):
                    section_info = {
                        'type': section.get('type'),
                        'mode': section.get('mode'),
                        'departure_time': section.get('departure_date_time'),
                        'arrival_time': section.get('arrival_date_time'),
                        'from': section.get('from', {}).get('name'),
                        'to': section.get('to', {}).get('name'),
                        'disruptions': []
                    }
                    
                    # Link disruptions to the section
                    display_info = section.get('display_informations', {})
                    for link in display_info.get('links', []):
                        if link.get('type') == 'disruption':
                            disruption_id = link.get('id')
                            matching_disruption = next((d for d in disruptions if d['id'] == disruption_id), None)
                            if matching_disruption:
                                section_info['disruptions'].append({
                                    'id': matching_disruption['id'],
                                    'status': matching_disruption['status'],
                                    'severity': matching_disruption.get('severity', {}).get('name'),
                                    'effect': matching_disruption.get('severity', {}).get('effect'),
                                    'messages': [msg['text'] for msg in matching_disruption.get('messages', [])]
                                })
                    
                    journey_info['sections'].append(section_info)
                parsed_journeys.append(journey_info)
            return parsed_journeys
        except KeyError as e:
            print(f"Error parsing journey data: missing key {e}")
            return []
