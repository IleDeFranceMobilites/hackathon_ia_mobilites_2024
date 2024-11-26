import requests
import pandas as pd

from .specification import Coordinates


def get_journeys(
    api_key: str, departure: Coordinates, arrival: Coordinates, datetime: str
) -> pd.DataFrame:
    """
    Fetches journey details from the API.

    Args:
        api_key (str): API key for authentication.
        departure (Coordinates): Departure GPS coordinates.
        arrival (Coordinates): Arrival GPS coordinates.
        datetime (str): Date and time for the journey in the format YYYYMMDDTHHMMSS.

    Returns:
        pd.DataFrame: A DataFrame containing journey details.
    """
    destination = f"{departure.longitude}%3B%20{departure.latitude}&to={arrival.longitude}%3B%20{arrival.latitude}&datetime={datetime}"
    url = f"https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/journeys?from={destination}"

    headers = {"Accept": "application/json", "apikey": api_key}

    # API request
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError(
            f"Failed to fetch data. Status code: {response.status_code}, Message: {response.text}"
        )

    # Process response
    try:
        data = response.json()
        return data
    except Exception as e:
        raise ValueError(f"Error processing response: {e}")
