import openai
import json
import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

from langchain import LLMChain
from langchain import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def generate_messages(trajets_alternatifs: dict, infos_incident: str, ligne_incident: str):
    # Appeler API du LLM
    openai_api_version=os.getenv('AZURE_OPENAI_API_VERSION')
    deployment_name=os.getenv('AZURE_OPENAI_MODELS')
    openai_api_type="azure"

    # Initialisation du LLM

    llm = AzureChatOpenAI(
        openai_api_version=openai_api_version,
        deployment_name=deployment_name,
        openai_api_type=openai_api_type
    )

    # Prompt pour le LLM
    template = f"""
    Ta mission est de générer des messages personnalisés pour chacune des stations d'une ligne de métro perturbée.
    Ces messages doivent informer et rassurer.

    Pour générer ces messages tu t'appuieras exclusivement sur les données suivantes:

    Le message d'incident: {infos_incident}
    La ligne impactée par l'incident: {ligne_incident}
    Les itinéraires alternatifs proposés pour chacun des stations de la ligne: {trajets_alternatifs}

    Pour chaque message tu commences par énoncer la nature de l'incident et la station qui est touchée. Par exemple :
    Si le message incident est "Métro 9 : Bagage oublié sur un quai - Trafic interrompu"
    Et que la ligne impactée est "Métro 9"
    Tu écriras: "Bonjour chers voyageurs, le trafic est interrompu sur la ligne 9 suite à un bagage oublié sur un quai."

    Puis, rassure-les en indiquant que tu vas les aider à trouver le meilleur itinéraire. Par exemple :
    Nous sommes désolés pour cet incident, mais nous sommes là pour vous guider jusqu’à votre destination.

    Situe dans quelle station les voyageurs se trouvent. Par exemple :
    Si la station actuellement traitée est "Pont de Sèvres"
    Vous êtes actuellement à la station Pont de Sèvres de la ligne 9. Voici les itinéraires possibles selon votre destination.

    Maintenant, tu vas expliquer, itinéraire par itinéraire, comment se déplacer. Tu vas utiliser la même structure d'explication pour chacun d’eux.

    Énonce la direction de l’itinéraire pour les voyageurs concernés. Par exemple :
    Si le itinerary_type dans l'itinéraire alternatif est: Nord-Ouest de Paris
    Tu écriras: Pour tous les voyageurs en direction du Nord-Ouest de Paris.

    Énonce la station et le numéro de ligne recommandé. Par exemple :
    Si la route de l'itinéraire alternatif est: {{"start": "Pont de Sèvres", "end": "Marcel Sembat", "ligne": "Métro 9"}}
    Empruntez la ligne 9 pour rejoindre la station Marcel Sembat.

    Fournis les résultats au format JSON, avec comme clés toutes les stations et comme valeur le message qui lui est destiné.
    """
    #     {{"Démocrate" : "Bonjour chers voyageurs, un bagage oublié demande l'intervention d'une équipe spécialisée. La ligne 9 est bloquée entre les stations Belle Vue et Pouvoir pendant un temps indéterminé. Vous êtes actuellement à la station Démocrate. Voici les itinéraires possibles selon votre destination. Pour tous les voyageurs en direction du Nord-Ouest de Paris. Emprunter la ligne 9 en rejoignant la station Balna."}}

    llm_var = llm([HumanMessage(content=template)])

    json_content = llm_var.content.strip("```json").strip("```")
    print(json_content)

    try:
        result = json.loads(json_content)
    except:
        fix_prompt = f"The folloxing JSON string is invalid, fix it and return it as valid JSON: {json_content}"
        fixed_json = llm([HumanMessage(content=fix_prompt)])
        result = json.loads(fixed_json)

    return result

if __name__ == "__main__":
    ligne_incident = "Métro 9"
    trajets_alternatifs = {"Fake_station": [{"itinary_type": "centre Paris",
                                            "routes" : [{"start" : "Démocrate", "end" : "Balna", "ligne": "1"}]}],
                        "Fake_station_2": [{"itinary_type" : "Paris Nord-Est",
                                            "routes" : [{"start" : "Longitude", "end" : "Voltour", "ligne": "10"}]}],
                            }
    infos_incident = """
        Le trafic est interrompu entre Porte de Montreuil et Mairie de Montreuil en raison d'un bagage oublié sur un quai .
        Heure de reprise estimée : 21:30.
        Nous vous invitons à emprunter des itinéraires alternatifs et à vous rapprocher de nos agents.
        Plus d'informations sur le site ratp.fr
    """
    messages = generate_messages(trajets_alternatifs, infos_incident, ligne_incident)
    print(messages)
