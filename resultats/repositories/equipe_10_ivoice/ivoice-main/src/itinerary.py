import os

import requests
from datetime import datetime
from dotenv import load_dotenv

from dataloaders import load_arrets_et_lignes_associes

API_URL = "https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/"


def get_station_pos(station_id: str):
    station_data = load_arrets_et_lignes_associes()
    station_lon = station_data[station_data["stop_id"] == station_id]["stop_lon"].head(1).item()
    station_lat = station_data[station_data["stop_id"] == station_id]["stop_lat"].head(1).item()

    return (station_lon, station_lat)


def basic_itinerary(start_station_id: str, end_station_id: str, departure_time: datetime) -> dict:
    start_station_pos = get_station_pos(start_station_id)
    end_station_pos = get_station_pos(end_station_id)

    parameters = {
        "from": ";".join(start_station_pos),
        "to": ";".join(end_station_pos),
        "datetime": departure_time,
    }
    response = requests.get(url=API_URL, params=parameters, headers={"apiKey": os.environ["IDFM_API_KEY"]})

    return response.json()

def itinerary_with_line_exclusion(start_station_id: str, end_station_id: str, departure_time: datetime, excluded_line_id: str) -> dict:
    start_station_pos = get_station_pos(start_station_id)
    end_station_pos = get_station_pos(end_station_id)
    forbidden_uri = f"line:{excluded_line_id}"

    parameters = {
        "from": ";".join(start_station_pos),
        "to": ";".join(end_station_pos),
        "datetime": departure_time,
        "forbidden_uris[]": forbidden_uri,
    }
    response = requests.get(url=f"{API_URL}/journeys", params=parameters, headers={"apiKey": os.environ["IDFM_API_KEY"]})

    return response.json()

if __name__ == "__main__":
    load_dotenv(override=True)
    # print(get_station_pos("IDFM:490900"))
    # print(get_station_pos("IDFM:37539"))
    # itin = basic_itinerary("IDFM:490900", "IDFM:37539", "20241211T1215")
    itin = itinerary_with_line_exclusion("IDFM:490900", "IDFM:37539", "20241211T1215", "IDFM:C01374")
    import json
    with open("test.json", "w") as f:
        json.dump(itin, f, indent=4)
    # get_station_pos("IDFM:490900")
