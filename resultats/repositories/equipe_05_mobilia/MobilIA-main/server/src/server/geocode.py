import requests


class GeocodingAPI:
    def __init__(self):
        self.base_url = "https://api-adresse.data.gouv.fr"

    async def reverse_geocode(self, lat: float, lon: float) -> str:
        try:
            response = requests.get(
                f"{self.base_url}/reverse/", params={"lon": lon, "lat": lat})
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
    async def geocode(self, address: str) -> list:
        try:
            postcodes = [
                "75000", "75001", "75002", "75003", "75004", "75005", "75006", "75007", "75008", "75009",
                "75010", "75011", "75012", "75013", "75014", "75015", "75016", "75017", "75018", "75019", "75020",
                "77000", "78000", "91000", "92000", "93000", "94000", "95000"
            ]
            # Calculate the center of Paris
            paris_center_lat = 48.8566
            paris_center_lon = 2.3522

            response = requests.get(f"{self.base_url}/search/", params={
                "q": address,
                "limit": 10,
                "lat": paris_center_lat,
                "lon": paris_center_lon
            })
            response.raise_for_status()
            data = response.json()
            print(f"Geocoding request for address: {address}")
            print(f"API response: {data}")

            if data["features"]:
                results = []
                for feature in data["features"]:
                    lon, lat = feature["geometry"]["coordinates"]
                    results.append({
                        "lat": lat,
                        "lon": lon,
                        "label": feature["properties"]["label"]
                    })
                return results
            else:
                raise ValueError("No coordinates found for the given address")
        except requests.RequestException as error:
            print(f"Error in geocoding: {error}")
            raise
