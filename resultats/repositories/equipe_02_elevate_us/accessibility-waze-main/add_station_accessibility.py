# Installation des dépendances :
import pandas as pd
import s3fs
import os

# !pip install s3fs

# import des dépendances

# Creation d'un objet filesystem, les variables d'environnement on été automatiquement traitées par Onyxia
S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": S3_ENDPOINT_URL})

# Liste des documents du répertoire partagé dédié au hackathon :
fs.ls("dlb-hackathon/datasets-diffusion", refresh=True)

def get_accessibility():