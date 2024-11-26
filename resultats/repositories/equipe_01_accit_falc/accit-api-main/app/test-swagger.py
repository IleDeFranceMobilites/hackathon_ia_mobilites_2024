# app/test-swagger.py
# Run with the following command:
# uvicorn app.test-swagger:app --reload
from fastapi import FastAPI, Query
from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

# Create FastAPI app instance
app = FastAPI(
    title="IDFM Transport API",
    description="""
    A simple API to get transportation information in Paris.

    ## Features
    * Get list of stations
    * Get information about transport lines
    * Search stations by name
    """,
    version="1.0.0",
)


# Define some enums for validation
class TransportType(str, Enum):
    METRO = "metro"
    BUS = "bus"
    RER = "rer"
    TRAM = "tram"


# Define data models
class Station(BaseModel):
    id: int
    name: str
    transport_type: str  # Changed from TransportType to str
    accessible: bool
    lines: List[str]

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Châtelet",
                "transport_type": "metro",
                "accessible": True,
                "lines": ["1", "4", "7", "11", "14"]
            }
        }


# Sample data
SAMPLE_STATIONS = [
    {
        "id": 1,
        "name": "Châtelet",
        "transport_type": "metro",  # Changed from TransportType.METRO to string
        "accessible": True,
        "lines": ["1", "4", "7", "11", "14"]
    },
    {
        "id": 2,
        "name": "Gare du Nord",
        "transport_type": "rer",  # Changed from TransportType.RER to string
        "accessible": True,
        "lines": ["B", "D", "E"]
    },
    {
        "id": 3,
        "name": "La Défense",
        "transport_type": "rer",  # Changed from TransportType.RER to string
        "accessible": True,
        "lines": ["A", "1"]
    }
]


@app.get(
    "/stations",
    response_model=List[Station],
    summary="Get list of stations",
    description="Returns a list of stations with optional filtering by transport type and accessibility."
)
async def get_stations(
        transport_type: Optional[str] = Query(
            None,
            description="Filter stations by transport type (metro, bus, rer, tram)",
            example="metro"
        ),
        accessible_only: bool = Query(
            False,
            description="Filter only accessible stations"
        )
) -> List[Station]:
    """Get list of stations with optional filters."""
    filtered_stations = SAMPLE_STATIONS

    if transport_type:
        filtered_stations = [
            station for station in filtered_stations
            if station["transport_type"] == transport_type
        ]

    if accessible_only:
        filtered_stations = [
            station for station in filtered_stations
            if station["accessible"]
        ]

    return filtered_stations


@app.get(
    "/stations/{station_id}",
    response_model=Station,
    summary="Get station by ID",
    description="Returns detailed information about a specific station."
)
async def get_station(
        station_id: int
) -> Station:
    """Get station by ID."""
    for station in SAMPLE_STATIONS:
        if station["id"] == station_id:
            return station
    return {"error": "Station not found"}


@app.get(
    "/search",
    response_model=List[Station],
    summary="Search stations",
    description="Search stations by name (case-insensitive partial match)."
)
async def search_stations(
        query: str = Query(
            ...,
            min_length=2,
            description="Search term (minimum 2 characters)",
            example="gare"
        )
) -> List[Station]:
    """Search stations by name."""
    query = query.lower()
    return [
        station for station in SAMPLE_STATIONS
        if query in station["name"].lower()
    ]


@app.get(
    "/transport-types",
    response_model=List[str],
    summary="Get transport types",
    description="Returns list of available transport types."
)
async def get_transport_types():
    """Get list of transport types."""
    return [t.value for t in TransportType]
