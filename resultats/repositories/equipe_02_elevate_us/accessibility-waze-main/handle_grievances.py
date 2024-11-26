import pandas as pd
import s3fs
import os


S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': S3_ENDPOINT_URL})


def update_grievances():
    BUCKET = "dlb-hackathon"
    FILE_KEY_S3 = "equipe-2/grievances.csv"
    FILE_PATH_S3 = BUCKET + "/" + FILE_KEY_S3

    with fs.open(FILE_PATH_S3, mode="r") as file_in:
        grievances = pd.read_csv(file_in)

    grievances = grievances.groupby("equipement_id").apply(handle_equipement)

    with fs.open(FILE_PATH_S3, "w") as file_out:
        grievances.to_csv(file_out)


def handle_equipement(single_grievances: pd.DataFrame) -> pd.DataFrame:
    # delete useless data
    pass