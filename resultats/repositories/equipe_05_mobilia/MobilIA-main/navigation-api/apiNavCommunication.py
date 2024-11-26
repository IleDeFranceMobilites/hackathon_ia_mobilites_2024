from requests.auth import HTTPBasicAuth
import requests
import json
import pandas as pd

# TOKEN: XDJujSkUHlvvCOirYONTwk9953G7thie
TOKEN = 'XDJujSkUHlvvCOirYONTwk9953G7thie'

# Affectation des coordonnées au départ et à l'arrivée
dlong = "2.33792"
dlat = "48.85827"
along = "2.3588523"
alat = "48.9271087"

# Date et heure du trajet
jour = "20241121T073000"

# URL de l'API
destination = dlong + "%3B%20" + dlat + "&to=" + along + "%3B%20" + alat + "&datetime=" + jour
url = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/journeys?from=' + destination

# Le header doit contenir la clé API : apikey, remplacer #VOTRE CLE API par votre clé API
headers = {'Accept': 'application/json', 'apikey': TOKEN}

# Envoi de la requête au serveur
req = requests.get(url, headers=headers)

# Affichage du code réponse
print('Status:', req)

# Lecture du json
data = pd.json_normalize(req.json())

# Les différents trajets retournés sont dans data['journeys'][0]
print(data.head())