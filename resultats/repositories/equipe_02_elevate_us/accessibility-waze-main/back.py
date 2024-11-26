# ce fichier contient les fonctions "back-end" de notre démonstrateur
import pandas as pd
import s3fs
import os

from add_state_to_equipements import (
    get_history_state_of_equipement,
    compute_state_for_elevators,
    compute_state_for_escaliers,
)

# Creation d'un objet filesystem, les variables d'environnement on été
# automatiquement traitées par Onyxia
S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": S3_ENDPOINT_URL})

# Liste des documents du répertoire partagé dédié au hackathon :
fs.ls("dlb-hackathon/datasets-diffusion", refresh=True)


def get_all_stations() -> list[str]:
    """Fonction qui retourne toutes les stations / arrêt de métro ou de train en Île-de-France"""
    referential = pd.read_csv("static/arrets-lignes.csv", sep=";")
    referential = referential[referential["mode"] == "Metro"]
    return referential["stop_name"].sort_values().unique()


def get_all_zdc() -> list[str]:
    """Retourne toutes les zones de correspondances des trains en Île-de-France"""
    referential = pd.read_csv("static/zones-de-correspondance.csv", sep=";")
    referential = referential[
        referential["ZdCType"].isin(["railStation", "metroStation"])
    ]
    return referential["ZdCName"].sort_values().unique()


def get_list_of_equipements(zdc: str) -> dict[str, pd.Series]:
    # Escaliers
    BUCKET = "dlb-hackathon"
    FILE_KEY_S3 = "equipe-2/ratp_localisation_escaliers.csv"
    FILE_PATH_S3 = BUCKET + "/" + FILE_KEY_S3
    with fs.open(FILE_PATH_S3, mode="rb") as file_in:
        escaliers = pd.read_csv(file_in)

    escaliers_mecanique_par_arret = escaliers.loc[
        lambda x: (x["nom"] == zdc) & (x["type_esc"] == "EM")
    ].pipe(compute_state_for_escaliers)

    # Ascenseurs
    BUCKET = "dlb-hackathon"
    FILE_KEY_S3 = "equipe-2/etat-des-ascenseurs.parquet"
    FILE_PATH_S3 = BUCKET + "/" + FILE_KEY_S3

    with fs.open(FILE_PATH_S3, mode="rb") as file_in:
        etat_ascenseurs = pd.read_parquet(file_in)

    ascenseurs_par_arret = (
        etat_ascenseurs.loc[lambda x: x["zdcname"] == zdc]
        .assign(
            **{
                "average_time_before_failure": lambda df: df["liftid"].map(
                    get_history_state_of_equipement
                )
            }
        )
        .pipe(compute_state_for_elevators)
    )

    return {
        "elevators": {
            liftid: values
            for liftid, values in ascenseurs_par_arret.set_index("liftid").iterrows()
        },
        "escalators": {
            escalatorid: values
            for escalatorid, values in escaliers_mecanique_par_arret.set_index(
                "id_escalier"
            ).iterrows()
        },
    }


def get_accessibilite(stop_name):
    BUCKET = "dlb-hackathon"
    FILE_KEY_S3 = "equipe-2/accessibilite-en-gare.parquet"
    FILE_PATH_S3 = BUCKET + "/" + FILE_KEY_S3

    with fs.open(FILE_PATH_S3, mode="rb") as file_in:
        accessibilite = pd.read_parquet(file_in)

    return accessibilite[
        ["stop_name", "accessibility_level_id", "accessibility_level_name"]
    ].loc[lambda x: x["stop_name"] == stop_name]
