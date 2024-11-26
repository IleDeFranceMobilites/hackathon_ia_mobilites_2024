from fastapi import APIRouter

from app.core.falcer.base import falc_text_score, falcate
from app.core.falcer.understood import get_all_falc_feedback, store_falc_feedback
from app.models.falc_understood import FalcFeedBack, FalcUnderstood
from app.models.in_text import FalcText, NormalText
from app.models.score_falceur import FalcScore

router = APIRouter()


@router.post("/text_to_falc")
def text_to_falc(in_text: NormalText) -> str:
    """Transforme un texte en version FALC.

    Ce point de terminaison permet de simplifier un texte en une version facile
    à lire et à comprendre.
    Le texte ainsi simplifié peut être compris par les personnes handicapées
    mentales, mais aussi par d'autres comme les personnes dyslexiques,
    malvoyantes, les personnes âgées, les personnes qui maîtrisent mal le
    français.
    """
    return falcate(in_text.text)


@router.post("/score_falc")
def score_falc_isation(in_text: FalcText) -> FalcScore:
    """Mesure la qualité de la FALCisation d'un texte.

    Ce point de terminaison permet de noter un texte fourni sur sa facilité à
    être lu et compris. Ce score sera exprimé en pourcentage (entre 0% et 100%).
    Plus le pourcentage est bas, plus le texte fourni est loin de suivre les
    règles FALC (FAcile à Lire et à Comprendre).
    """
    return falc_text_score(in_text.falc_text)


@router.post("/is_text_understood")
def understood_falc(data: FalcUnderstood) -> None:
    """Indique si un texte falc a été compris ou pas.

    Ce point de terminaison permet de vérifier si un texte FALCisé est bien
    compris. La requête sera stocké dans une base de données pour permettre
    aux prochaines FALCification d'être plus facile à comprendre.
    """
    return store_falc_feedback(data)


@router.get("/get_user_feedbacks")
def get_feedbacks() -> list[FalcFeedBack]:
    """Récupère tous les retours utilisateurs sur la FALCisation.

    Ce point de terminaison permet de récupérer tous les retours utilisateurs
    sur la qualité de la FALCisation d'un texte.
    """
    return get_all_falc_feedback()
