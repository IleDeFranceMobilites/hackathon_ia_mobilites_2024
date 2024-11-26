from itinerary_data import Itinerary, Route
from dataloaders import load_arrets_et_lignes_associes
from itinerary import itinerary_with_line_exclusion
from datetime import datetime
from pathlib import Path
import json
from dacite import from_dict
from dataclasses import asdict

class ItineraryCalculator:
    def __init__(self):
        self.stations_by_lines = load_arrets_et_lignes_associes()
        self.standard_destination_ids = ["IDFM:483454", "IDFM:491486", "IDFM:22073", "IDFM:5823"]
        self.standard_itinerary_types = ["Centre de Paris", "Grands Boulevards", "Est de Paris", "Ouest de Paris"]

    def compute_alternate_itineraries(self, line_id: str) -> dict[str, Itinerary]:
        cache_file_path = Path(f"data/{line_id.split(':')[-1]}_cache.json")
        if cache_file_path.is_file():
            with cache_file_path.open('r', encoding="utf-8") as f:
                data = json.load(f)
                for key, val in data.items():
                    data[key] = [from_dict(Itinerary, it) for it in val]
            return data
        station_ids = self.stations_by_lines[self.stations_by_lines["id"] == line_id]["stop_id"]
        alt_itineraries = {}
        for station_id in station_ids:
            station_name = self.stations_by_lines[self.stations_by_lines["stop_id"] == station_id]["stop_name"].head(1).item()
            alt_itineraries[station_name] = []
            for std_destination_id, std_itin_type in zip(self.standard_destination_ids, self.standard_itinerary_types):
                destination_name = self.stations_by_lines[self.stations_by_lines["stop_id"] == std_destination_id]["stop_name"].head(1).item()
                itin = itinerary_with_line_exclusion(station_id, std_destination_id, datetime.now(), line_id)
                alt_itineraries[station_name].append(Itinerary.from_navitia_response(itin, std_itin_type, station_name, destination_name))

        cache_file_path.parent.mkdir(parents=True, exist_ok=True)
        with cache_file_path.open("w", encoding="utf-8") as f:
            data = {k: [asdict(it) for it in v] for k, v in alt_itineraries.items()}
            json.dump(data, f, ensure_ascii=False)
        return alt_itineraries

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv(override=True)
    ic = ItineraryCalculator()
    # ID ligne 9: line:IDFM:C01379
    ais = ic.compute_alternate_itineraries(line_id="IDFM:C01379")
