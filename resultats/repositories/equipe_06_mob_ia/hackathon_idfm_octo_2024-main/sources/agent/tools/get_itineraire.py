from typing import Annotated, Literal, Optional

from langchain_core.tools import tool

from sources.api.api_prim import call_recherche_itineraire


@tool
def get_itineraire(
    origin: Annotated[
        str, "[Not null] Point de départ : une adresse ou une geolocation sous forme float;float."],
    destination: Annotated[
        str, "[Not null] Destination de l'itineraire recherché sous la forme d'une adresse."],
    jour: Annotated[
        str, ("[Not null] Jour à laquelle l'utilisateur veut partir au format : YYYYmmdd,"
              "Date de départ ou d’arrivée en fonction du paramètre datetime_represents")],
    heure: Annotated[
        str, ("[Not null] Heure à laquelle l'utilisateur veut partir au format : HHMMSS"
              "Date de départ ou d’arrivée en fonction du paramètre datetime_represents")],
    datetime_represents: Annotated[
        Optional[Literal['depart', 'arrivée']],
        "Si la date et l'heure correspondent à l'heure de départ ou d'arrivée."] = 'departure',
    max_walking_duration_to_pt: Annotated[
        int, "Durée maximale de marche sur l'itineraire, en secondes si précisée."] = None,
    wheelchair: Annotated[
        bool, ("Si True, le voyageur est considéré comme utilisant un fauteuil roulant"
               "et seuls les transports publics accessibles sont utilisés.")] = False,
) -> str:
    """
        Effectue une recherche d'itineraire permettant d'aller de origin à destination
        à une date donnée ou pour une date donnée.
    """
    try:
        datetime_represents = "arrival" if datetime_represents == "arrivée" else 'departure'
        date_str = jour + "T" + heure
        return call_recherche_itineraire(
            origin=origin, destination=destination,
            date=date_str,
            datetime_represents=datetime_represents,
            max_walking_duration_to_pt=max_walking_duration_to_pt,
            wheelchair=wheelchair
        )
    except Exception as err:
        return f"Une erreur est survenue lors de la recherche d'itineraire: {err}"