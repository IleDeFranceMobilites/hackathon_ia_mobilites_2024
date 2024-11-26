import requests

class GeocodingAPI:
    def __init__(self):
        self.base_url = "https://api-adresse.data.gouv.fr"

    async def reverse_geocode(self, lat: float, lon: float) -> str:
        try:
            response = requests.get(f"{self.base_url}/reverse/", params={"lon": lon, "lat": lat})
            response.raise_for_status()
            data = response.json()

            if data["features"]:
                address = data["features"][0]["properties"]
                return f"{address.get('housenumber', '')} {address.get('street', '')}, {address.get('postcode', '')} {address.get('city', '')}".strip()
            else:
                raise ValueError("No address found for the given coordinates")
        except requests.RequestException as error:
            print(f"Error in reverse geocoding: {error}")
            raise

    async def geocode(self, address: str) -> dict:
        try:
            response = requests.get(f"{self.base_url}/search/", params={"q": address, "limit": 1})
            response.raise_for_status()
            data = response.json()

            if data["features"]:
                feature = data["features"][0]
                lon, lat = feature["geometry"]["coordinates"]
                return {
                    "lat": lat,
                    "lon": lon,
                    "label": feature["properties"]["label"]
                }
            else:
                raise ValueError("No coordinates found for the given address")
        except requests.RequestException as error:
            print(f"Error in geocoding: {error}")
            raise
