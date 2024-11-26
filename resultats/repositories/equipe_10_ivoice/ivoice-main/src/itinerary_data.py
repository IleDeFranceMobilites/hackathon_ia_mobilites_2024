from dataclasses import dataclass


@dataclass
class Route:
    start: str
    end: str
    line: str


@dataclass
class Itinerary:
    itinerary_type: str
    routes: list[Route]

    @classmethod
    def from_navitia_response(cls, navitia_reponse: dict, itinerary_type: str, start_name: str, destination_name: str):
        routes = []
        for section in navitia_reponse["journeys"][0]["sections"]:
            if section["type"] == "waiting":
                continue

            if section["type"] == "street_network" and section["mode"] == "walking":
                line = "A pied"
            elif section["type"] == "public_transport":
                line = f"{section['display_informations']['commercial_mode']} {section['display_informations']['name']}"
            else:
                line = "Inconnue"

            routes.append(Route(
                start=section["from"]["stop_point"]["name"] if "stop_point" in section["from"] else start_name,
                end=section["to"]["stop_point"]["name"] if "stop_point" in section["to"] else destination_name,
                line=line
            ))
            # Quick hack to return only the first route
            break

        return Itinerary(itinerary_type, routes)


@dataclass
class Disruption:
    period_begin: str
    status: str
    severity: str
    message: str
    line_id: str
