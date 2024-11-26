###################
# Import & config #
###################
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path
import os
from typing import Any

from api_mlmodel.specification import Coordinates
from api_mlmodel.journey import get_journeys

from dotenv import load_dotenv
from pathlib import Path


from datetime import datetime
import requests

from dotenv import load_dotenv
from pathlib import Path

secret_path = Path(__file__).parent / "secrets.env"
secret_path = secret_path.resolve()

load_dotenv(dotenv_path=secret_path)

api_key = os.getenv("PRIM")

app = FastAPI()

# Need to specify the list of ports, else it wont work with only "*"
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://10.244.1.53:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

##########
# Exemple API route #
##########

@app.get("/add_two/{number}")
async def add_two(number: int):
    return {"result": number + 2}


# Fix the endpoint for route metadata
@app.get("/options_and_metadata")
def get_routes():
    departure = Coordinates(latitude=48.85021352679651,
                         longitude=2.4735419963428593)

    arrival = Coordinates(latitude=48.875460818207635,
                                longitude=2.3088650247211775)

    current_time = datetime.now()
    current_time = current_time.strftime("%Y%m%dT%H%M%S")

    destination = f"{departure.longitude}%3B%20{departure.latitude}&to={arrival.longitude}%3B%20{arrival.latitude}&datetime={current_time}"
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


    # Extract

    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
