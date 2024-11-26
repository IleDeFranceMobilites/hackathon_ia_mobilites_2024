"""
Via l'utilisation d'un LLM, nous classons les signalements des utilisateurs ce qui permet par la suite de mieux identifier le problème.
"""

import os
from openai import AzureOpenAI
from api_key import API_KEY

# Dictionnaire pour faire correspondre les classes à un message d'affichage
CATEGORY_TO_EXPLANATION = {
    "Quai": "Un problème a été signalé au niveau du quai.",
    "Escalator-fonctionnement": "Il semble y avoir un problème avec le fonctionnement de cet escalator.",
    "Escalator-bruit": "L'escalator fait un bruit étonnant.",
    "Escalator-propreté": "L'escalator est sale.",
    "Ascenseur-fonctionnement": "Il semble y avoir un problème avec le fonctionnement de cet ascenseur.",
    "Ascenseur-bruit": "L'ascenseur fait un bruit étonnant.",
    "Ascenseur-propreté": "L'ascenseur est sale.",
    "problème-inconnu": "Problème inconnu",
}


def categorize_signaling(text):
    """Classification des signalements avec chat-gpt4o-mini
    """

    # Récupération des clés d'authentification d'Azure Open AI
    API_VERSION = "2024-08-01-preview"
    AZURE_ENDPOINT = "https://dlb-team02-prd-oai01.openai.azure.com/"

    azure_open_ai_parameters = {
        "api_version": API_VERSION,
        "azure_endpoint": AZURE_ENDPOINT,
        "api_key": API_KEY,
    }

    # Instanciation du modèle
    llm = AzureOpenAI(**azure_open_ai_parameters)

    # Personnalisation du prompt pour classifier les signalements
    completion = llm.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You will receive the signaling of an equipment in a train station. Your goal is to categorize that signaling between : Quai, Escalator-fonctionnement, Escalator-bruit, Escalator-propreté, Ascenseur-fonctionnement, Ascenseur-bruit, Ascenseur-propreté, problème-inconnu",
            },
            {"role": "user", "content": text},
        ],
    )

    return completion.choices[0].message.content


# test unitaire sur les ascenseurs
# text = """J'appuie sur le boutton d'appel, mais ça ne fonctionne pas. Je crois que l'ascenseur est cassé."""

# categorize_signaling(text)
