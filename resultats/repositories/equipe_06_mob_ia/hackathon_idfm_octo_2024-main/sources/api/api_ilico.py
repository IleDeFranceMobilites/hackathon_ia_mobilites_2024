import json
import requests

import pandas as pd


URL_ILICO = 'https://data.iledefrance-mobilites.fr/api/explore/v2.1/catalog/datasets/referentiel-des-lignes/exports/json'


def get_referentiel_ligne() -> pd.DataFrame:
    response = requests.get(URL_ILICO)

    data = json.loads(response.content)

    df_ilico = pd.DataFrame(data)
    return df_ilico[df_ilico['transportmode'].isin(['tram', 'rail', 'metro'])][['id_line', 'name_line']]
