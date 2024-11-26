import pandas as pd
import s3fs
import os
from datetime import datetime

from signaling import categorize_signaling

from add_state_to_equipements import AVAILABLE, UNAVAILABLE


# Creation d'un objet filesystem, les variables d'environnement on été automatiquement
# traitées par Onyxia
S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": S3_ENDPOINT_URL})


def add_grievances(equipment_id, state, commentaire):

    category = categorize_signaling(commentaire)

    df = pd.DataFrame(
        data={
            "equipment_id": equipment_id,
            "datetime": datetime.now(),
            "state": state,
            "commentaire": commentaire,
            "category": category,
        },
        index=[0],
    )

    # Ecrire
    BUCKET_OUT = "dlb-hackathon"
    FILE_KEY_OUT_S3 = "equipe-2/grievances.csv"
    FILE_PATH_OUT_S3 = BUCKET_OUT + "/" + FILE_KEY_OUT_S3

    with fs.open(FILE_PATH_OUT_S3, "a") as file_out:
        df.to_csv(file_out, header=None)


# add_grievances(1038, UNAVAILABLE, "l'ascenseur était très sale.")

# add_grievances(1038, UNAVAILABLE, "ascenseur il est tout cassé")

# add_grievances(1038, UNAVAILABLE, "ascenseur il est tout cassé")

# add_grievances(1038, AVAILABLE, "ascenseur il est bien")

# add_grievances(1038, AVAILABLE, "ascenseur il est bien")

# add_grievances(318, UNAVAILABLE, "marche pas")

# add_grievances(1156, UNAVAILABLE, "marche pas")

# add_grievances(1681522, UNAVAILABLE, "escalator recule au lieu d'avancer")

# add_grievances(1681522, UNAVAILABLE, "escalatueur recule au lieu d'avancer")
