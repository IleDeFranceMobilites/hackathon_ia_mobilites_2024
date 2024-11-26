import os
import re
from typing import Literal
import urllib.parse

import requests
import pandas as pd

from sources.api.api_ilico import get_referentiel_ligne
from sources.entities.process_dico import process_dico

PRIM_API_TOKEN = os.environ['PRIM_API_TOKEN']
HEADERS = {'Accept': 'application/json', 'apikey': PRIM_API_TOKEN}

API_BASE_URL_PLACES = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/places?'
API_BASE_URL_JOURNEY = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/journeys?'
API_BASE_URL_INFO_TRAFIC = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/line_reports/'


def get_place(adresse: str) -> str:
    params = {'q': adresse, 'from': "2.334934;48.86404"}
    url = API_BASE_URL_PLACES + urllib.parse.urlencode(params)

    # Envoi de la requête au serveur
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise ValueError(f"Error code {response.status_code}: {response.text}")
    response_dict = response.json()
    return response_dict["places"][0]["id"]


def call_recherche_itineraire(
    origin: str, destination: str, date: str, datetime_represents: Literal['departure', 'arrival'],
    max_walking_duration_to_pt: int = None, wheelchair: bool = False
) -> pd.DataFrame:
    if re.match(r"\d+.\d+;\d+.\d+", origin):
        origin_long_lat = origin
    else:
        origin_long_lat = get_place(origin)

    destination_long_lat = get_place(destination)

    # URL de l'API
    params = {
        'from': origin_long_lat,
        'to': destination_long_lat,
        'datetime': date,
        'datetime_represents': datetime_represents,
        'wheelchair': wheelchair,
    }

    if max_walking_duration_to_pt is not None:
        params[max_walking_duration_to_pt] = max_walking_duration_to_pt

    url = API_BASE_URL_JOURNEY + urllib.parse.urlencode(params)

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise ValueError(f"Error code {response.status_code}: {response.text}")
    response = pd.json_normalize(response.json())
    return process_dico(response)


def call_info_trafic(ligne: str | None = None) -> pd.DataFrame:
    df_ilico = get_referentiel_ligne()
    try:
        code_ligne = df_ilico.loc[df_ilico['name_line'] == ligne, 'id_line'].iloc[0]
    except IndexError:
        return pd.DataFrame({'Error': ['Ligne non existante']})

    url = f"{API_BASE_URL_INFO_TRAFIC}{urllib.parse.quote(f'lines/line:IDFM:{code_ligne}', safe='')}/line_reports"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise ValueError(f"Error code {response.status_code}: {response.text}")
    return pd.json_normalize(response.json()['disruptions'])


if __name__ == "__main__":
    # origin / destination
    origin = "14 rue du Prévôt, 75004 Paris"
    destination = "Censier-Daubenton"

    # Date et heure du trajet
    jour = "20241121T073000"

    response = call_recherche_itineraire(origin=origin, destination=destination, jour=jour)
