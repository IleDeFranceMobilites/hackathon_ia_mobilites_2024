import os
import s3fs
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta
from signaling import CATEGORY_TO_EXPLANATION

import duckdb as ddb

AVAILABLE = 0
UNCERTAIN_AVAILABLE = 1
UNCERTAIN = 2
UNCERTAIN_UNAVAILABLE = 3
UNAVAILABLE = 4


S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": S3_ENDPOINT_URL})


ddb.execute("SET s3_region='fr-central';")
ddb.execute("SET s3_url_style='path';")
ddb.execute("SET s3_endpoint='minio.data-platform-self-service.net';")
ddb.execute(
    f"SET s3_access_key_id='{os.environ["AWS_ACCESS_KEY_ID"]}' ;"
)  # Aussi récupérable dans les paramètres "Valeurs de Helm" du service
ddb.execute(
    f"SET s3_secret_access_key='{os.environ["AWS_SECRET_ACCESS_KEY"]}';"
)  # Aussi récupérable dans les paramètres "Valeurs de Helm"


def get_history_state_of_equipement(equipment_id) -> datetime:
    limit_date = (datetime.now() - relativedelta(month=6)).strftime("%Y-%m-%d %H:%M:%S")

    history_ascenseur = ddb.sql(
        f""" 
        select * from 's3://dlb-hackathon/datasets-diffusion/ascenseurs_historique_etat/RELEVES_ETATS_ASCENSEURS_SNCF_RATP_2021-2024.parquet'
        where code_appareil = {equipment_id}
        and date_releve >= '{limit_date}'
        """
    ).to_df()

    return (
        history_ascenseur[
            history_ascenseur["etat"] != history_ascenseur["etat"].shift()
        ]
        .assign(
            **{
                "datetime_delta": lambda df: df["date_releve"]
                - df["date_releve"].shift()
            }
        )
        .loc[lambda df: df["etat"] == "1"]["datetime_delta"]
        .mean()
    )


def get_state_from_grievances(equipements) -> pd.Series:
    BUCKET = "dlb-hackathon"
    FILE_KEY_S3 = "equipe-2/grievances.csv"
    FILE_PATH_S3 = BUCKET + "/" + FILE_KEY_S3

    with fs.open(FILE_PATH_S3, mode="r") as file_in:
        grievances = pd.read_csv(file_in, index_col=0).astype(
            {"equipment_id": str, "state": int}
        )

    states = (
        grievances[grievances["equipment_id"].isin(equipements["id"].astype(str))]
        .sort_values(by=["equipment_id", "datetime"])
        .groupby("equipment_id")
        .apply(find_state_from_grievances_for_equipement)
    )

    return states


CONFIDENCE_THRESHOLD = 10
DATETIME_THRESHOLD = {AVAILABLE: np.inf, UNAVAILABLE: relativedelta(hours=24)}
UNSURE_STATE = {AVAILABLE: UNCERTAIN_AVAILABLE, UNAVAILABLE: UNCERTAIN_UNAVAILABLE}


def find_state_from_grievances_for_equipement(grievances: pd.DataFrame) -> dict:
    if grievances.empty:
        return pd.Series({"state": UNCERTAIN, "last_datetime": pd.NaT, "reasons": []})

    last_state = grievances.iloc[-1]["state"]
    last_datetime = grievances.iloc[-1]["datetime"]
    nb_identical = (grievances["state"] == last_state).iloc[::-1].cumprod().sum()
    reasons = (
        grievances.iloc[-nb_identical:]["category"]
        .map(CATEGORY_TO_EXPLANATION)
        .fillna("Problème inconnu")
        .unique()
        .tolist()
    )

    if (
        nb_identical >= CONFIDENCE_THRESHOLD
        and last_datetime >= DATETIME_THRESHOLD[last_state]
    ):
        return pd.Series(
            {"state": last_state, "last_datetime": last_datetime, "reasons": reasons}
        )
    else:
        return pd.Series(
            {
                "state": UNSURE_STATE.get(int(last_state), last_state),
                "last_datetime": last_datetime,
                "reasons": reasons,
            }
        )


def compute_state_for_elevators(elevators: pd.DataFrame) -> pd.DataFrame:
    if elevators.empty:
        return elevators.assign(
            **{
                "state": None,
                "reasons_grievances": [],
            }
        )

    states_from_grievances = get_state_from_grievances(
        elevators.rename(columns={"liftid": "id"})
    )

    elevators["state"] = elevators["liftstatus"].map(
        {"available": AVAILABLE, "unknown": UNCERTAIN, "notavailable": UNAVAILABLE}
    )

    if not states_from_grievances.empty:
        elevators = elevators.merge(
            states_from_grievances.add_suffix("_grievances"),
            left_on="liftid",
            right_index=True,
            how="left",
        ).assign(
            **{
                "state_grievances": lambda df: df["state_grievances"].fillna(
                    df["state"]
                )
            }
        )

        elevators.loc[elevators["state"] == UNCERTAIN, "state"] = elevators[
            "state_grievances"
        ]
        news_from_grievances = (
            pd.to_datetime(elevators["liftstateupdate"])
            < elevators["last_datetime_grievances"]
        )
        elevators.loc[~news_from_grievances, "reasons_grievances"] = ""
        elevators.loc[
            ~news_from_grievances & elevators["state"] == UNAVAILABLE,
            "reasons_grievances",
        ] = CATEGORY_TO_EXPLANATION["Ascenseur-fonctionnement"]

        grievances_and_idfm_agree_available = (elevators["state"] == AVAILABLE) & (
            elevators["state_grievances"].isin(
                [AVAILABLE, UNCERTAIN_AVAILABLE, UNCERTAIN]
            )
        )
        grievances_and_idfm_agree_unavailable = (elevators["state"] == UNAVAILABLE) & (
            elevators["state_grievances"].isin(
                [UNAVAILABLE, UNCERTAIN_UNAVAILABLE, UNCERTAIN]
            )
        )
        elevators.loc[
            news_from_grievances & grievances_and_idfm_agree_available, "state"
        ] = AVAILABLE
        elevators.loc[
            news_from_grievances & grievances_and_idfm_agree_unavailable, "state"
        ] = UNAVAILABLE

        elevators.loc[
            news_from_grievances
            & (~grievances_and_idfm_agree_available)
            & (~grievances_and_idfm_agree_unavailable),
            "state",
        ] = elevators.loc[
            news_from_grievances
            & (~grievances_and_idfm_agree_available)
            & (~grievances_and_idfm_agree_unavailable)
        ][
            "state_grievances"
        ]

    return elevators


def compute_state_for_escaliers(escaliers: pd.DataFrame) -> pd.DataFrame:
    return (
        escaliers.astype({"id_escalier": str})
        .merge(
            get_state_from_grievances(escaliers.rename(columns={"id_escalier": "id"})),
            how="left",
            right_index=True,
            left_on="id_escalier",
        )
        .assign(**{"state": lambda df: df["state"].fillna(UNCERTAIN)})
        .rename(columns={"reasons": "reasons_grievances"})
    )
