import os

import pandas as pd
import s3fs


def load_parquet_from_s3(bucket: str, file_key: str) -> pd.DataFrame:
    # Create filesystem object
    s3_endpoint_url = f"https://{os.environ['AWS_S3_ENDPOINT']}"
    fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': s3_endpoint_url})
    file_path_s3 = f"{bucket}/{file_key}"

    with fs.open(file_path_s3, mode="rb") as file_in:
        df = pd.read_parquet(file_in)
    return df


def load_historique_info_trafic() -> pd.DataFrame:
    bucket = "dlb-hackathon"
    file_key = "datasets-diffusion/historique_info_trafic/historique_disruptions_2024.parquet"
    return load_parquet_from_s3(bucket, file_key)


def load_zones_arrets() -> pd.DataFrame:
    bucket = "dlb-hackathon"
    file_key = "equipe-10/zones-d-arrets.parquet"
    return load_parquet_from_s3(bucket, file_key)


def load_referentiel_lignes() -> pd.DataFrame:
    bucket = "dlb-hackathon"
    file_key = "equipe-10/referentiel-des-lignes.parquet"
    return load_parquet_from_s3(bucket, file_key)


def load_arrets_et_lignes_associes() -> pd.DataFrame:
    bucket = "dlb-hackathon"
    file_key = "equipe-10/arrets-lignes.parquet"
    return load_parquet_from_s3(bucket, file_key)
