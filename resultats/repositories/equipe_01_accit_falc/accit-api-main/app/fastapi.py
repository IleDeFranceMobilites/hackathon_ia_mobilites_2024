# Run with the following command:
# uvicorn app.fastapi:app --reload

from fastapi import FastAPI

from .api.routes import api_router

# Create FastAPI app instance
app = FastAPI(
    title="IDFM accessible text API",
    description="""
    Une API pour simplifier des textes en FALC.

    ## Fonctionnalités

    * Générer un texte FALC à partir d'un texte normal
    * Noter un texte FALCisé (mesurer à quel point il est FALC) en se basant sur des retours utilisateurs
    * Indiquer si un texte FALCisé a été compris ou non
    * Récupérer tous les retours utilisateurs sur la FALCisation
    """,
    version="1.0.0",
)

app.include_router(api_router)
