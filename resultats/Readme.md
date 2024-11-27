![Logo du Hackathon IA et Mobilités](/images/Logo%20illustre_Hackathon%20IA%20Mobilites.jpg)

# Les 🌟Pépites🌟 du Hackathon IA et Mobilités

Bienvenue dans ce recueil de pépites issues du Hackathon IA et Mobilités organisé par Ile-de-France Mobilités. 

Vous trouverez ici des extraits de code soigneusement sélectionnés (merci l'IA 😅) pour leur impact et leur réutilisabilité.
Ce document doit mettre en valeur le gros travail réalisé au cours des deux jours de hackathon et contribuer a faciliter la prise en main des données et API d'IDFM mais aussi accélérer le lancement de projets IA en faveur des mobilités.

Vous trouverez donc de quoi vous inspirer selon ces différentes thématiques qui ont émergé de vos travaux :
- **Utilisation de l'API IDFM**
- **Utilisation d'autres API**
- **Appel à un LLM**
- **Création d'une interface utilisateur (IHM)**
- **Création d'une API**
- **Appel à Whisper (audio)**
- **Utilisation d'un référentiel d'événements**
- **Intégration avec un Data Lake**
- **Utilisation de Retrieval-Augmented Generation (RAG)**
- **Traitement audio ou vocal**
- **Traitement d'images**
- **Données de validation**
- **Machine Learning (ML)**
- **Utilisation de LangChain**
- **Fonctionnalités de cartographie**
- **Traitement du langage naturel (NLP)**
- **Utilisation de Websockets**
- **Conception de prompts**
- **Géocodage**
- **Utilisation d'Angular**
- **Génération de données**
- **Prise en compte de la frugalité**
- **Manipulation de données**

Nous espérons que ces exemples inspireront vos propres projets et souligneront l'importance de l'innovation collaborative dans le domaine de la mobilité.

Encore bravo à toutes et tous pour votre participation !!! 🔥🔥🔥

---

<div style="page-break-after: always;"></div>




# 💡 Appel à un LLM, 
## 🌟 Équipe : **equipe_01_accit_falc**
### 👨‍🏫 Description du code
Ce code charge dynamiquement un modèle de langage en utilisant des configurations spécifiées et remplit les secrets à partir des variables d'environnement.
### 🚌 Spécificités fonctionnelles
Permet de gérer dynamiquement les modèles de langage en fonction des besoins de l'application, en assurant la sécurité des secrets via les variables d'environnement.
### ✍ Réutilisabilité
La fonction `get_model` est hautement réutilisable pour charger différents modèles de langage en fonction de configurations dynamiques, ce qui est crucial pour des applications nécessitant une flexibilité dans le choix des modèles d'IA.
### 📜 Snippet de code
```python
import importlib
import os

from app.models.config import LLMConfig


def get_model(model_name: str, params: LLMConfig):
    model_package, module_name = params.model_class.rsplit(".", 1)

    module = importlib.import_module(model_package)
    module = getattr(module, module_name)

    fill_secrets_from_env(model_name, params)

    return module(**params.model_dump(exclude=["model_class"]))


def fill_secrets_from_env(model_name: str, params: LLMConfig):
    for key, value in params.model_dump().items():
        if value == "SECRET":
            setattr(params, key, os.getenv(f"{model_name.upper()}_{key.upper()}"))
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_01_accit_falc/app/core/models.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce fichier charge les variables d'environnement nécessaires pour configurer l'accès à l'API Azure OpenAI, notamment la clé API, l'endpoint et le nom du modèle.
### 🚌 Spécificités fonctionnelles
Fournit les configurations de base pour l'accès à un service LLM via Azure.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant une configuration d'accès à l'API Azure OpenAI. Il centralise les informations de configuration, facilitant leur gestion et leur modification.
### 📜 Snippet de code
```python
from dotenv import load_dotenv
import os
load_dotenv(".env")

AZURE_OPENAI_KEY = "REMOVED"
OPENAI_ENDPOINT = "https://dlb-team08-prd-oai01.openai.azure.com/"
MODEL_NAME = "gpt-4o-mini"
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm/Hackathon-IDFM-main/Hackathon_équipe8/domain/llm/keys.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce fichier utilise un modèle de langage pour générer des messages personnalisés pour les utilisateurs en fonction de leurs informations de billettique.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de notifier les utilisateurs sur l'état de leur billettique, améliorant ainsi l'expérience utilisateur.
### ✍ Réutilisabilité
La fonction de génération de messages personnalisés est réutilisable pour tout projet nécessitant une communication personnalisée basée sur des données utilisateurs.
### 📜 Snippet de code
```python
def generate_custom_message(user_data): ... def test_llm(): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm%20%-%20%Hackathon-IDFM/prompt_billettique.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce fichier charge les variables d'environnement nécessaires pour configurer l'accès à l'API Azure OpenAI, notamment la clé API, l'endpoint et le nom du modèle.
### 🚌 Spécificités fonctionnelles
Ce fichier répond au besoin de sécuriser et de centraliser les informations de configuration pour l'accès à l'API Azure OpenAI.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant une configuration d'accès à l'API Azure OpenAI. Il centralise les informations de configuration, facilitant ainsi leur gestion et leur modification.
### 📜 Snippet de code
```python
from dotenv import load_dotenv
import os
load_dotenv(".env")

AZURE_OPENAI_KEY = "REMOVED"
OPENAI_ENDPOINT = "https://dlb-team08-prd-oai01.openai.azure.com/"
MODEL_NAME = "gpt-4o-mini"
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm/Hackathon-IDFM-main/old/llm/keys.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code initialise un client pour interagir avec l'API Azure OpenAI en chargeant les clés API et les points de terminaison à partir d'un fichier d'environnement.
### 🚌 Spécificités fonctionnelles
Permet de configurer et d'initialiser un client pour interagir avec l'API Azure OpenAI.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant une connexion à l'API Azure OpenAI, car il centralise la gestion des clés API et des points de terminaison.
### 📜 Snippet de code
```python
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from pathlib import Path


class Client:
    def __init__(self):
        path_secrets = os.getcwd()+"/secrets.env"
        load_dotenv(dotenv_path=Path(path_secrets).resolve())
        self.openAiKey = os.getenv("OPENAI_API_KEY")
        self.end_point = os.getenv("OPENAI_AZURE_ENDPOINT")
        self.api_version = os.getenv("API_VERSION")

    def get_client(self):
        client = AzureOpenAI(
            azure_endpoint=self.end_point,
            api_key=self.openAiKey,
            api_version=self.api_version
        )
        return client
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/backend/api-llm/src/client.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Conception de prompts, Génération de données, 
## 🌟 Équipe : **equipe_04_mobiwize**
### 👨‍🏫 Description du code
Génère des requêtes de recherche basées sur une question donnée en utilisant un modèle de langage.
### 🚌 Spécificités fonctionnelles
Permet de créer des requêtes de recherche variées pour couvrir différents aspects d'une question.
### ✍ Réutilisabilité
La génération de requêtes est un composant réutilisable pour tout système nécessitant des recherches basées sur des questions.
### 📜 Snippet de code
```javascript
export const generateQueries = async (state: typeof ResearcherGraphAnnotation.State): Promise<ResearcherGraphReturnType> => { const modelWithTool = llm.withStructuredOutput(z.object({ queries: z.array(z.string()).describe("List of generated search queries").max(3) }), {name: "generate_queries"}); const messages = [ {role: "system", content: getDefaultPromptConfig().generateQueriesSystemPrompt}, {role: "human", content: state.question} ]; const response = await modelWithTool.invoke(messages); return {queries: response.queries}; };
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_04_mobiwize/ai-framework-main/packages/ai-toolkit/src/graphs/researcher/index.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Conception de prompts, Prise en compte de la frugalité, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce fichier configure et gère les interactions avec un modèle de langage (LLM) via l'API Azure OpenAI. Il initialise le client AzureOpenAI et définit une méthode pour envoyer des prompts et recevoir des réponses.
### 🚌 Spécificités fonctionnelles
Permet l'intégration d'un LLM dans des applications, facilitant l'interaction utilisateur via des prompts.
### ✍ Réutilisabilité
La classe LLMConfiguration est hautement réutilisable pour toute application nécessitant des interactions avec un LLM via Azure. Elle encapsule la logique d'appel à l'API, rendant le code modulaire et facile à intégrer.
### 📜 Snippet de code
```python
from openai import AzureOpenAI
from llm.keys import OPENAI_ENDPOINT, MODEL_NAME, AZURE_OPENAI_KEY
from ecologits import EcoLogits

EcoLogits.init()

class LLMConfiguration:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=AZURE_OPENAI_KEY,
            api_version="2024-03-01-preview",
            azure_endpoint=OPENAI_ENDPOINT
        )
        
        self.default_params = {
            "model": MODEL_NAME,
            "temperature": 0,
            "response_format": {"type": "json_object"},
            "max_tokens": None
        }
        
    def invoke(self, prompt):
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            **self.default_params
        )
        return response
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm/Hackathon-IDFM-main/Hackathon_équipe8/domain/llm/llm_management.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Conception de prompts, Prise en compte de la frugalité, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce fichier configure et gère les interactions avec le modèle de langage Azure OpenAI. Il initialise le client avec les paramètres par défaut et fournit une méthode pour invoquer le modèle avec un prompt.
### 🚌 Spécificités fonctionnelles
Répond au besoin de gérer les interactions avec un modèle de langage, en fournissant une interface simple pour envoyer des prompts et recevoir des réponses.
### ✍ Réutilisabilité
La classe LLMConfiguration est hautement réutilisable pour toute application nécessitant des interactions avec un modèle de langage Azure OpenAI. Elle encapsule la logique d'appel et de configuration, facilitant ainsi l'intégration dans d'autres projets.
### 📜 Snippet de code
```python
from openai import AzureOpenAI
from llm.keys import OPENAI_ENDPOINT, MODEL_NAME, AZURE_OPENAI_KEY
from ecologits import EcoLogits

EcoLogits.init()

class LLMConfiguration:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=AZURE_OPENAI_KEY,
            api_version="2024-03-01-preview",
            azure_endpoint=OPENAI_ENDPOINT
        )
        
        self.default_params = {
            "model": MODEL_NAME,
            "temperature": 0,
            "response_format": {"type": "json_object"},
            "max_tokens": None
        }
        
    def invoke(self, prompt):
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            **self.default_params
        )
        return response
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm/Hackathon-IDFM-main/old/llm/llm_management.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Création d\'une interface utilisateur (IHM), Conception de prompts, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Génération de messages personnalisés pour les utilisateurs en fonction de leurs données d'abonnement en utilisant Azure OpenAI.
### 🚌 Spécificités fonctionnelles
Permet de notifier les utilisateurs sur l'état de leur abonnement de manière personnalisée.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant la génération de messages personnalisés basés sur des données utilisateur.
### 📜 Snippet de code
```python
def generate_custom_message(user_data):
    prompt = f"""
    Crée un message personnalisé pour l'utilisateur en fonction de ses informations d'abonnement :
    - Abonnement : {user_data['billettique_type']}
    - Fin de validité : {user_data['billettique_end_date']}
    - Tickets restants : {user_data['billettique_tickets_left']}
    Ne génère le message que si l'utilisateur a besoin d'être averti, par exemple :
    - S'il reste moins de 2 tickets.
    - Si l'abonnement expire dans moins de 7 jours.
    Le message doit être court, il doit y avoir de la place pour plein de message dans l'écran
    """

    response = llm_config.llm.invoke(prompt_test.format(input=prompt))
    return response
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm%20%-%20%Hackathon-IDFM/old/prompt_billettique.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Création d\'une interface utilisateur (IHM), Conception de prompts, Génération de données, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Cette fonction génère un message personnalisé pour un utilisateur en fonction de ses informations d'abonnement, en utilisant un modèle de langage (LLM) pour formuler le message.
### 🚌 Spécificités fonctionnelles
Répond au besoin de notifier les utilisateurs sur l'état de leur abonnement de manière proactive.
### ✍ Réutilisabilité
La fonction est réutilisable pour générer des messages personnalisés basés sur des conditions spécifiques d'abonnement, ce qui peut être adapté à d'autres contextes nécessitant des notifications personnalisées.
### 📜 Snippet de code
```python
def generate_custom_message(user_data):
    prompt = f"""
    Crée un message personnalisé pour l'utilisateur en fonction de ses informations d'abonnement :
    - Abonnement : {user_data['billettique_type']}
    - Fin de validité : {user_data['billettique_end_date']}
    - Tickets restants : {user_data['billettique_tickets_left']}
    Ne génère le message que si l'utilisateur a besoin d'être averti, par exemple :
    - S'il reste moins de 2 tickets.
    - Si l'abonnement expire dans moins de 7 jours.
    Le message doit être court, il doit y avoir de la place pour plein de message dans l'écran
    """

    response = llm_config.invoke(prompt_test.format(input=prompt))
    return response
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm%20%-%20%Hackathon-IDFM-main/config/prompt_billettique.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Création d\'une interface utilisateur (IHM), Conception de prompts, Prise en compte de la frugalité, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce code initialise une configuration de modèle de langage (LLM) et invoque une réponse en utilisant un prompt formaté. Il affiche ensuite la réponse du modèle ainsi que des informations sur l'impact énergétique et CO2.
### 🚌 Spécificités fonctionnelles
Le code permet de tester l'interaction avec un modèle de langage et d'évaluer l'impact environnemental de l'utilisation de ce modèle.
### ✍ Réutilisabilité
Le code est précieux pour son abstraction de l'invocation d'un modèle de langage, ce qui permet de réutiliser facilement cette logique pour d'autres prompts ou configurations.
### 📜 Snippet de code
```python
from Hackathon_équipe8.domain.llm.llm_management import LLMConfiguration
from Hackathon_équipe8.config.prompts import prompt_test

llm_config = LLMConfiguration()

input = "I am a human"
response = llm_config.invoke(prompt_test.format(input = input))

print(f'response: {response.choices[0].message.content}')

print(f'Impact energy: {response.impacts.energy.value.max} kWh')
print(f'Impact co2: {response.impacts.usage.gwp.value.max} CO2eq')
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/resultats/repositories/equipe_08_maidfm/Hackathon-IDFM-main/Hackathon_équipe8/domain/llm/main.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Création d\'une interface utilisateur (IHM), Utilisation d\'un référentiel d\'événements, Conception de prompts, Génération de données, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Cette fonction génère un message personnalisé pour un utilisateur en fonction de ses centres d'intérêts et des événements disponibles, en utilisant un modèle de langage (LLM) pour formuler le message.
### 🚌 Spécificités fonctionnelles
Répond au besoin de recommander des événements pertinents aux utilisateurs en fonction de leurs intérêts.
### ✍ Réutilisabilité
La fonction est réutilisable pour créer des messages personnalisés basés sur les intérêts des utilisateurs et les événements, ce qui peut être adapté à d'autres contextes nécessitant des recommandations personnalisées.
### 📜 Snippet de code
```python
def generate_custom_message(user_data, events):
    if not events:
        return ""

    event_details = "\n".join([
        f"- Événement : {event['Titre']}\n  - Description : {event['Description']}\n  - Lien : {event['URL canonique']}"
        for event in events
    ])
    user_interests_str = ', '.join(user_data['centres d\'intérêts'])
    prompt = f"""
    Crée un message personnalisé pour l'utilisateur en fonction de ses centres d'intérêts et des événements disponibles en Île-de-France dans les prochains jours.
    Les centres d'intérêts de l'utilisateur sont : {user_interests_str}
    Voici une liste d'événements récents :
    {event_details}
    """
    response = llm_config.invoke(prompt_test.format(input=prompt))
    return response
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm%20%-%20%Hackathon-IDFM-main/config/prompt_évènement.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Transcrit un fichier audio en texte en utilisant le modèle Whisper d'OpenAI.
### 🚌 Spécificités fonctionnelles
Facilite la transcription de contenu audio, essentiel pour l'accessibilité et l'archivage de données vocales.
### ✍ Réutilisabilité
Utile pour les applications nécessitant la transcription automatique de l'audio, comme les services de sous-titrage ou de transcription de réunions.
### 📜 Snippet de code
```python
def transcribe_audio_with_openai(audio_path): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/api/functions.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Traitement d\'images, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce code initialise un client OpenAI et définit une fonction pour envoyer une image encodée en base64 à l'API OpenAI afin d'obtenir une description de l'image.
### 🚌 Spécificités fonctionnelles
Permet l'analyse d'images pour extraire des descriptions textuelles, ce qui peut être utilisé dans des applications d'accessibilité ou de gestion de contenu.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant l'analyse d'images via l'API OpenAI, ce qui est utile pour des tâches de reconnaissance d'image ou de transcription de texte dans des images.
### 📜 Snippet de code
```python
client = OpenAI(api_key='XXX')

# Fonction pour envoyer l'image encodée en base64 à l'API OpenAI et récupérer une description
def image_to_description_with_openai(image_path):
    try:
        print("Encodage de l'image en base64...")
        base64_image = encode_image_to_base64(image_path)

        if not base64_image:
            return "Erreur lors de l'encodage de l'image."

        print("Envoi de l'image encodée à OpenAI pour analyse...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What's in this image? If there is some text, write the full transcript, keeping the same language."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )

        # Récupération de la description générée
        description = response.choices[0].message.content
        print(f"Description extraite par OpenAI : {description}")
        return description
    except Exception as e:
        print(f"Erreur avec l'API OpenAI : {e}")
        return "Une erreur est survenue lors de l'analyse de l'image."
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/final.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Traitement d\'images, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Cette fonction encode une image en base64, l'analyse via l'API OpenAI pour obtenir une description, et gère les erreurs potentielles.
### 🚌 Spécificités fonctionnelles
Permet l'analyse et la transcription de contenu d'image, ce qui est crucial pour l'accessibilité et l'interprétation de données visuelles.
### ✍ Réutilisabilité
La fonction est utile pour toute application nécessitant une analyse d'image automatisée, et peut être intégrée dans des systèmes de reconnaissance d'image ou de transcription de texte.
### 📜 Snippet de code
```python
def analyze_image_with_openai(image_path): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/api/functions.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Traitement du langage naturel (NLP), 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code utilise un modèle de langage pour détecter les intentions et entités dans un message utilisateur, en se basant sur des descriptions prédéfinies.
### 🚌 Spécificités fonctionnelles
Permet de déterminer si un message utilisateur correspond à des services ou données spécifiques, comme la météo ou les lignes de transport.
### ✍ Réutilisabilité
Le code est hautement réutilisable pour toute application nécessitant une analyse des intentions et entités à l'aide d'un modèle de langage.
### 📜 Snippet de code
```python
from .client import Client


class Nlu:
    def __init__(self):
        self.client = Client()
        self.client = self.client.get_client()
        self.model = 'gpt-4o-mini'

    def get_intentions_entites(self, message):
        conversation_history = []
        conversation_history.append(
                
            {"role": "system", "content":
                """
                    Tu est un agent intelligent, ton role consiste a detecter si la demande de
                    l'utilisateur concerne l'une des description suivantes:
                    {
                        {
                            "name": "Météo",
                            "description": "Il est possible d'accéder à la météo en temps réel en 
                            utilisant l'API indiquée dans le champ url. Il faut indiquer une
                             position en utilisant la latitude et la longitude. On peut obtenir le 
                             niveau de pluie, le niveau de neige, la vitesse du vent, la 
                             température.",
                            "url": "https://api.openweathermap.org/data/2.5/weather"
                        },
                        {
                            "name": "Liste des lignes",
                            "description": "Il est possible d'accéder à la liste des lignes de 
                            transport en commun d'Île-de-France en lisant le fichier nommé dans le 
                            champ url. Pour chaque ligne, la liste contient l'identifiant 
                            commercial, l'identifiant administratif, son nom, si elle est
                             accessible PMR, son mode de transport. Elle contient les lignes de
                            bus, métro, RER, navette
                             aéroport, tramway, funiculaire.",
                            "url": "referentiel-des-lignes.parquet"
                        },
                        {
                            "name": "Liste des arrêts",
                            "description": "Il est possible d'accéder à la liste des arrêts en
                             lisant le fichier nommé dans le champ url. Pour chaque arrêt, la liste 
                             contient ses coordonnées géographiques en latitude/longitude WGS 84 
                             ainsi que Lambert-93, son identifiant, son nom, son mode de transport, 
                             le nom de sa commune, sa zone de tarif Navigo, si elle est accessible 
                             PMR.",
                            "url": "referentiel-des-lignes.parquet"
                        },
                        {
                            "name": "Correspondance arrêt-ligne",
                            "description": "Il est possible d'accéder à la correspondance entre
                             identifiant d'arrêt et identifiant de ligne commerciale en lisant le 
                             fichier nommé dans le champ url.",
                            "url": "arrets-lignes.parquet"
                        },
                        {
                            "name": "Relations arrêts",
                            "description": "Il est possible d'accéder aux relations entre objets
                             arrêt tels quel arrêt transporteur, arrêt, zone d'arrêts, zone de 
                             correspondance, pôle d'échanges, grâce à leurs identifiants. Il faut
                            utiliser le fichier nommé dans le champ url.",
                            "url": "relations.parquet"
                        }
                }
                Sinon demande à l'utilisateur de dmander une information à propos d'IDFM"

                """})
        conversation_history.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=conversation_history,
            temperature=0,
        )
        return response.choices[0].message.content
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/backend/api-llm/src/nlu.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Utilisation de LangChain, 
## 🌟 Équipe : **equipe_04_mobiwize**
### 👨‍🏫 Description du code
Ce code initialise un modèle de langage (LLM) Azure OpenAI pour des interactions de chat, en configurant les paramètres d'API et de modèle.
### 🚌 Spécificités fonctionnelles
Facilite l'intégration de capacités de chat IA dans des applications, avec des paramètres ajustables pour le modèle et l'API.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant des interactions de chat basées sur Azure OpenAI, avec des paramètres configurables pour le modèle et l'API.
### 📜 Snippet de code
```javascript
import {AzureChatOpenAI} from "@langchain/openai";

export const llm = new AzureChatOpenAI({
  azureOpenAIEndpoint: process.env.AZURE_OPENAI_ENDPOINT,
  azureOpenAIApiKey: process.env.AZURE_OPENAI_API_KEY,
  azureOpenAIApiDeploymentName: process.env.AZURE_OPENAI_MODELS,
  azureOpenAIApiVersion: process.env.AZURE_OPENAI_API_VERSION,
  model: process.env.AZURE_OPENAI_MODELS,
  temperature: 0.1,
});
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_04_mobiwize%20%-%20%ai-framework-main/https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/blob/main/packages/ai-toolkit/src/registry/registry.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Utilisation de LangChain, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce fichier configure une ancienne version de la gestion des interactions avec un LLM via l'API Azure OpenAI, utilisant la bibliothèque langchain_openai.
### 🚌 Spécificités fonctionnelles
Fournit une configuration alternative pour l'intégration d'un LLM, utile pour comparer différentes approches d'implémentation.
### ✍ Réutilisabilité
Bien que ce soit une version ancienne, la classe LLMConfiguration reste réutilisable pour des applications nécessitant une interaction avec un LLM. Elle montre une approche alternative pour configurer et utiliser l'API Azure OpenAI.
### 📜 Snippet de code
```python
from langchain_openai import AzureChatOpenAI
from llm.keys import OPENAI_ENDPOINT, MODEL_NAME, AZURE_OPENAI_KEY

class LLMConfiguration:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            model=MODEL_NAME,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=AZURE_OPENAI_KEY,
            azure_endpoint=OPENAI_ENDPOINT,
            api_version="2024-03-01-preview"
        )
        self.llm.bind(response_format={"type": "json_object"})
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm/Hackathon-IDFM-main/Hackathon_équipe8/domain/llm/llm_management_old.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Utilisation de LangChain, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce fichier configure une instance de AzureChatOpenAI pour interagir avec le modèle de langage. Il initialise le modèle avec des paramètres spécifiques et lie le format de réponse.
### 🚌 Spécificités fonctionnelles
Fournit une configuration prête à l'emploi pour interagir avec AzureChatOpenAI, répondant aux besoins de gestion des interactions avec un modèle de langage.
### ✍ Réutilisabilité
La classe LLMConfiguration est réutilisable pour configurer et interagir avec AzureChatOpenAI. Elle offre une abstraction pour gérer les paramètres de connexion et de réponse, facilitant l'intégration dans d'autres systèmes.
### 📜 Snippet de code
```python
from langchain_openai import AzureChatOpenAI
from llm.keys import OPENAI_ENDPOINT, MODEL_NAME, AZURE_OPENAI_KEY

class LLMConfiguration:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            model=MODEL_NAME,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=AZURE_OPENAI_KEY,
            azure_endpoint=OPENAI_ENDPOINT,
            api_version="2024-03-01-preview"
        )
        self.llm.bind(response_format={"type": "json_object"})
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm/Hackathon-IDFM-main/old/llm/llm_management_old.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Utilisation de LangChain, Conception de prompts, 
## 🌟 Équipe : **equipe_10_ivoice**
### 👨‍🏫 Description du code
Ce code utilise l'API Azure OpenAI pour générer des messages personnalisés concernant des perturbations sur une ligne de métro, en utilisant des itinéraires alternatifs et des informations d'incident.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de communication rapide et personnalisée en cas de perturbations sur les lignes de transport, en fournissant des messages clairs et informatifs aux voyageurs.
### ✍ Réutilisabilité
Le code est hautement réutilisable pour générer des messages personnalisés en cas de perturbations, grâce à l'utilisation de modèles de langage et de prompts structurés.
### 📜 Snippet de code
```python
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
    openai_api_version=os.getenv('AZURE_OPENAI_API_VERSION')
    deployment_name=os.getenv('AZURE_OPENAI_MODELS')
    openai_api_type="azure"

    llm = AzureChatOpenAI(
        openai_api_version=openai_api_version,
        deployment_name=deployment_name,
        openai_api_type=openai_api_type
    )

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

    llm_var = llm([HumanMessage(content=template)])

    json_content = llm_var.content.strip("").strip(",")
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
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_10_ivoice/ivoice-main/ivoice-main/src/langchain_openai.py)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Utilisation de Retrieval-Augmented Generation (RAG), Conception de prompts, 
## 🌟 Équipe : **equipe_04_mobiwize**
### 👨‍🏫 Description du code
Cette fonction crée un plan de recherche en utilisant un modèle de langage pour structurer les étapes de recherche basées sur les messages d'entrée.
### 🚌 Spécificités fonctionnelles
Répond au besoin de créer un plan de recherche structuré basé sur les requêtes utilisateur.
### ✍ Réutilisabilité
Le code est modulaire et utilise un modèle de langage pour générer dynamiquement un plan de recherche, ce qui le rend réutilisable pour différents types de requêtes de recherche.
### 📜 Snippet de code
```javascript
export const createResearchPlan = async (state: typeof RetrievalGraphAnnotation.State, config: LangGraphRunnableConfig): Promise<RetrievalGraphReturnType> => { const modelWithTool = llm.withStructuredOutput(z.object({ steps: z.array(z.string()) }), {name: "create_plan"}); const messages = [ {role: "system", content: getDefaultPromptConfig().researchPlanSystemPrompt}, ...state.messages ]; const response = await modelWithTool.invoke(messages); const lastMessage = state.messages[state.messages.length - 1]; return { steps: response.steps, documents: undefined, query: lastMessage?.content as string, }; };
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_04_mobiwize/ai-framework-main/packages/ai-toolkit/src/graphs/rag/index.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Utilisation de Retrieval-Augmented Generation (RAG), Utilisation de LangChain, 
## 🌟 Équipe : **equipe_04_mobiwize**
### 👨‍🏫 Description du code
Ce code configure et initialise une recherche vectorielle ElasticSearch en utilisant des embeddings générés par Azure OpenAI. Il établit une connexion avec un client ElasticSearch en utilisant des configurations d'authentification et de connexion spécifiques.
### 🚌 Spécificités fonctionnelles
Permet l'intégration de capacités de recherche vectorielle avancées dans des applications utilisant ElasticSearch et OpenAI.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant une recherche vectorielle basée sur des embeddings OpenAI, intégrant ElasticSearch pour le stockage et la recherche de vecteurs.
### 📜 Snippet de code
```javascript
import {type ElasticClientArgs, ElasticVectorSearch,} from "@langchain/community/vectorstores/elasticsearch";
import {AzureOpenAIEmbeddings} from "@langchain/openai";
import {Client, type ClientOptions} from "@elastic/elasticsearch";
import * as process from "node:process";

export const embeddings = new AzureOpenAIEmbeddings({
  azureOpenAIApiDeploymentName: "text-embedding-3-large",
  azureOpenAIApiInstanceName: "dlb-team04-prd-oai01",
  azureOpenAIApiKey: process.env.AZURE_OPENAI_API_KEY,
  azureOpenAIApiVersion: process.env.AZURE_OPENAI_API_VERSION,
  model: "text-embedding-3-large",
});


const config: ClientOptions = {
  node: process.env.ELASTIC_URL ?? "https://127.0.0.1:9200",
};

config.auth = {
  apiKey: process.env.ELASTIC_API_KEY as string,
};

const clientArgs: ElasticClientArgs = {
  client: new Client(config),
  indexName: "idfm-eq4"
};

export const vectorStore = new ElasticVectorSearch(embeddings, clientArgs);
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_04_mobiwize%20%-%20%ai-framework-main/https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/blob/main/packages/ai-toolkit/src/rag/elastic.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Utilisation de Retrieval-Augmented Generation (RAG), Utilisation de LangChain, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce code initialise un modèle d'embedding basé sur OpenAI, hébergé sur Azure, pour générer des vecteurs à partir de documents.
### 🚌 Spécificités fonctionnelles
Permet de transformer des documents en vecteurs pour une indexation efficace dans une base de données vectorielle.
### ✍ Réutilisabilité
Utile pour les applications nécessitant des embeddings de texte, notamment pour l'indexation et la recherche dans des bases de données vectorielles.
### 📜 Snippet de code
```python
from langchain_openai import AzureOpenAIEmbeddings

embedding_model = AzureOpenAIEmbeddings(
    **azure_open_ai_parameters,
    model="text-embedding-3-large", # Voir comment pointer sur variables d'environnement ou sur Vault
)
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm/Hackathon-IDFM-main/notebooks/HIAM2024)

---

<div style="page-break-after: always;"></div>

# 💡 Appel à un LLM, Conception de prompts, 
## 🌟 Équipe : **equipe_01_accit_falc**
### 👨‍🏫 Description du code
Ce fichier définit des configurations pour différents composants de l'application, y compris les modèles de langage (LLM), la base de données, et les modèles spécifiques à l'application. Il utilise Pydantic pour la validation et la gestion des configurations.
### 🚌 Spécificités fonctionnelles
Le code permet de configurer et de personnaliser facilement les modèles de langage et les connexions à la base de données, ce qui est essentiel pour le bon fonctionnement de l'application.
### ✍ Réutilisabilité
Le code est hautement réutilisable grâce à son abstraction et à sa modularité. Il permet de gérer les configurations de manière centralisée et flexible, facilitant l'intégration avec différents modèles de langage et bases de données.
### 📜 Snippet de code
```python
from functools import cache
from typing import Type

from pydantic import BaseModel, ConfigDict
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    YamlConfigSettingsSource,
)


class ModelConfig(BaseModel):
    model_config = ConfigDict(extra="allow", protected_namespaces=tuple())
    model: str
    system_prompt: str


class LLMConfig(BaseModel):
    model_config = ConfigDict(extra="allow", protected_namespaces=tuple())
    model_class: str


class DBConfig(BaseModel):
    url: str
    echo: bool = False


class Config(BaseSettings):

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            YamlConfigSettingsSource(settings_cls, yaml_file="config.yaml"),
            env_settings,
            dotenv_settings,
            file_secret_settings,
        )

    falceur: ModelConfig
    falc_scorer: ModelConfig
    db: DBConfig
    models: dict[str, LLMConfig]


@cache
def get_config():
    return Config()
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_01_accit_falc/app/models/config.py)

---

<div style="page-break-after: always;"></div>

# 💡 Conception de prompts, 
## 🌟 Équipe : **equipe_01_accit_falc**
### 👨‍🏫 Description du code
Cette fonction utilise un modèle de chat pour générer une réponse à partir d'un prompt utilisateur et d'un prompt système.
### 🚌 Spécificités fonctionnelles
Permet de générer des réponses textuelles basées sur des prompts, ce qui est essentiel pour des applications de simplification de texte.
### ✍ Réutilisabilité
La fonction est modulaire et peut être réutilisée pour intégrer différents modèles de chat en modifiant simplement les prompts et le modèle.
### 📜 Snippet de code
```python
def falcate_a_text(model: BaseChatModel, system_prompt: str, user_prompt: str) -> str: ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_01_accit_falc/app/core/falcer/base.py)

---

<div style="page-break-after: always;"></div>

# 💡 Conception de prompts, 
## 🌟 Équipe : **equipe_01_accit_falc**
### 👨‍🏫 Description du code
Cette fonction évalue un texte en utilisant un modèle de chat et retourne un score sous forme de dictionnaire.
### 🚌 Spécificités fonctionnelles
Fournit une évaluation des textes, ce qui est crucial pour ajuster et améliorer les modèles de génération de texte.
### ✍ Réutilisabilité
La fonction est utile pour évaluer des textes générés, ce qui peut être réutilisé dans divers contextes nécessitant une évaluation qualitative.
### 📜 Snippet de code
```python
def score_a_text(model: BaseChatModel, system_prompt: str, user_prompt: str) -> dict: ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_01_accit_falc/app/core/falcer/base.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une API, 
## 🌟 Équipe : **equipe_01_accit_falc**
### 👨‍🏫 Description du code
Ce script initialise un projet FastAPI avec une structure standard, crée des fichiers de configuration, initialise un dépôt git et configure un environnement virtuel.
### 🚌 Spécificités fonctionnelles
Le script répond au besoin fonctionnel d'automatiser la configuration initiale d'un projet FastAPI, ce qui est essentiel pour les équipes de développement cherchant à standardiser leurs environnements de travail.
### ✍ Réutilisabilité
Le script est hautement réutilisable pour initialiser rapidement de nouveaux projets FastAPI avec une structure de base cohérente et des configurations standardisées.
### 📜 Snippet de code
```python
def create_directory_structure():
    ...

def create_config_files():
    ...

def initialize_git():
    ...

def setup_virtual_environment():
    ...

def main():
    ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_01_accit_falc/setup-env.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une API, 
## 🌟 Équipe : **equipe_01_accit_falc**
### 👨‍🏫 Description du code
Ce fichier initialise une application FastAPI pour une API qui simplifie les textes en FALC (Facile à Lire et à Comprendre).
### 🚌 Spécificités fonctionnelles
L'application répond au besoin de simplification de texte pour les utilisateurs ayant des difficultés de compréhension, ce qui est crucial pour l'accessibilité numérique.
### ✍ Réutilisabilité
La structure de l'application FastAPI est réutilisable pour créer d'autres APIs avec des fonctionnalités similaires, en particulier celles nécessitant une interface utilisateur pour simplifier les textes.
### 📜 Snippet de code
```python
app = FastAPI(
    title="IDFM accessible text API",
    description="""
    Une API pour simplifier des textes en FALC.
    ...
    """,
    version="1.0.0",
)

app.include_router(api_router)
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_01_accit_falc/fastapi.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une API, 
## 🌟 Équipe : **equipe_01_accit_falc**
### 👨‍🏫 Description du code
Ce fichier définit une API FastAPI pour obtenir des informations sur les stations de transport à Paris, avec des fonctionnalités de recherche et de filtrage.
### 🚌 Spécificités fonctionnelles
L'API répond aux besoins de gestion et de recherche d'informations sur les stations de transport, ce qui est essentiel pour les applications de mobilité urbaine.
### ✍ Réutilisabilité
Les modèles de données et les routes API sont réutilisables pour d'autres projets nécessitant des fonctionnalités similaires de gestion et de recherche de données de transport.
### 📜 Snippet de code
```python
class TransportType(str, Enum):
    METRO = "metro"
    BUS = "bus"
    RER = "rer"
    TRAM = "tram"

class Station(BaseModel):
    id: int
    name: str
    transport_type: str
    accessible: bool
    lines: List[str]

@app.get("/stations", ...)
async def get_stations(...):
    ...

@app.get("/stations/{station_id}", ...)
async def get_station(...):
    ...

@app.get("/search", ...)
async def search_stations(...):
    ...

@app.get("/transport-types", ...)
async def get_transport_types():
    ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_01_accit_falc/test-swagger.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une API, 
## 🌟 Équipe : **equipe_01_accit_falc**
### 👨‍🏫 Description du code
Ce fichier définit plusieurs routes API utilisant FastAPI pour transformer un texte en version FALC (Facile à Lire et à Comprendre), évaluer la qualité de cette transformation, vérifier la compréhension du texte transformé, et récupérer les retours utilisateurs.
### 🚌 Spécificités fonctionnelles
Le code répond à des besoins d'accessibilité en transformant des textes pour les rendre plus compréhensibles par des personnes ayant des difficultés de lecture, ce qui est essentiel pour l'inclusion numérique.
### ✍ Réutilisabilité
Les fonctions sont bien définies et encapsulées, ce qui permet de les réutiliser dans d'autres projets nécessitant des transformations de texte en FALC. L'utilisation de FastAPI facilite l'intégration dans d'autres services web.
### 📜 Snippet de code
```python
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
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_01_accit_falc/app/api/routes/falc.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une API, 
## 🌟 Équipe : **equipe_01_accit_falc**
### 👨‍🏫 Description du code
Ce code initialise un routeur API FastAPI et inclut un sous-routeur pour les routes FALC (Facile à Lire et à Comprendre).
### 🚌 Spécificités fonctionnelles
Permet de structurer les routes de l'application en séparant les fonctionnalités FALC, ce qui est essentiel pour une application modulaire.
### ✍ Réutilisabilité
Le routeur API est un composant modulaire qui peut être facilement étendu pour inclure d'autres sous-routeurs, facilitant ainsi l'organisation et la gestion des routes dans une application FastAPI.
### 📜 Snippet de code
```python
from fastapi import APIRouter

from .falc import router as router_falc

api_router = APIRouter()
api_router.include_router(router_falc, tags=["falc"])
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_01_accit_falc/app/api/routes/__init__.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une API, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code initialise une application FastAPI avec deux endpoints : un endpoint racine qui retourne un message de bienvenue et un autre qui retourne un item basé sur un identifiant et un paramètre optionnel.
### 🚌 Spécificités fonctionnelles
Fournit une structure de base pour une API RESTful, ce qui est essentiel pour le développement de services web.
### ✍ Réutilisabilité
Ce code est un exemple de base pour démarrer une API avec FastAPI, ce qui est utile pour créer rapidement des services web RESTful.
### 📜 Snippet de code
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/backend/api-ml-model/src/api_mlmodel/idfmhk24.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une API, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Lancement d'un serveur FastAPI en utilisant Uvicorn pour héberger l'application web.
### 🚌 Spécificités fonctionnelles
Permet de déployer une application web, ce qui est essentiel pour exposer des services de mobilité via une API.
### ✍ Réutilisabilité
Ce code est réutilisable pour démarrer des applications web basées sur FastAPI, un framework populaire pour créer des APIs rapides et performantes.
### 📜 Snippet de code
```python
import uvicorn
from idfmhk24.app import app

def main():
    print("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main%20%-%20%idfm_hackaton_2024/backend/api-ml-model/src/api_mlmodel/__main__.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une API, Traitement du langage naturel (NLP), 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code met en place une API FastAPI avec un point de terminaison pour analyser les intentions et entités d'un message utilisateur en utilisant un module NLU.
### 🚌 Spécificités fonctionnelles
Fournit un service web pour l'analyse des intentions et entités des messages utilisateurs.
### ✍ Réutilisabilité
La structure de l'API est modulaire et peut être étendue pour inclure d'autres fonctionnalités d'analyse de langage naturel.
### 📜 Snippet de code
```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .nlu import Nlu

app = FastAPI()

# Need to specify the list of ports, else it won't work with only "*"
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://10.244.1.53:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nlu = Nlu()

class MessageRequest(BaseModel):
    message: str

@app.post("/get_intentions_entites")
async def get_intentions_entites(request: MessageRequest):
    answer = nlu.get_intentions_entites(request.message)
    return JSONResponse(content={"answer": answer})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/backend/api-llm/src/main.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une interface utilisateur (IHM), 
## 🌟 Équipe : **equipe_07_tranquiliscore**
### 👨‍🏫 Description du code
Ce code crée dynamiquement des éléments HTML pour afficher une liste de gares avec leur niveau de dangerosité. Chaque gare est représentée par un div contenant des informations sur le nom et le niveau de danger.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de visualiser des informations sur les gares et leur dangerosité de manière claire et interactive.
### ✍ Réutilisabilité
Le code est réutilisable pour générer dynamiquement des listes d'éléments HTML à partir de données structurées, ce qui est utile pour les interfaces utilisateur interactives.
### 📜 Snippet de code
```javascript
const gares = [
    { name: "RER A", danger: "Élevé" },
    { name: "RER B", danger: "Moyen" },
    { name: "RER C", danger: "Bas" },
  ];
  
  const container = document.querySelector(".gares-container");
  
  gares.forEach((gare) => {
    const gareElement = document.createElement("div");
    gareElement.classList.add("gare");
    gareElement.innerHTML = `
      <span class="gare-icon">🚇</span>
      <span class="gare-name">${gare.name}</span>
      <span class="gare-danger">⚠️ Niveau : ${gare.danger}</span>
    `;
    container.appendChild(gareElement);
  });
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_07_tranquiliscore/tranquili-score-main/Documents/t-app-js/script.js)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une interface utilisateur (IHM), Appel à Whisper (audio), Traitement audio ou vocal, Traitement d\'images, 
## 🌟 Équipe : **equipe_02_elevate_us**
### 👨‍🏫 Description du code
Ce code utilise Streamlit pour créer une interface utilisateur permettant de signaler des problèmes d'accessibilité dans les gares, avec la possibilité de transcrire des doléances audio en texte.
### 🚌 Spécificités fonctionnelles
Facilite la collecte de signalements d'accessibilité en permettant aux utilisateurs de soumettre des doléances via texte ou audio.
### ✍ Réutilisabilité
L'utilisation de Streamlit pour créer des interfaces interactives est hautement réutilisable pour d'autres applications nécessitant une interaction utilisateur simple et rapide.
### 📜 Snippet de code
```python
import streamlit as st
from back import get_all_zdc, get_list_of_equipements, get_accessibilite
from edit_grievances import add_grievances
import time
from pathlib import Path
import whisper
from add_state_to_equipements import (
    AVAILABLE,
    UNAVAILABLE,
    UNCERTAIN_AVAILABLE,
    UNCERTAIN_UNAVAILABLE,
    UNCERTAIN,
)

st.set_page_config(page_title="Hackathon accessibilité")

@st.cache_resource
def get_whisper():
    return whisper.load_model("base")

@st.dialog("Signalement")
def grieve(key, supposed_state):
    left, right = st.columns([0.8, 0.2])
    text = left.text_area("décrivez la situation (optionnel)")
    audio = right.audio_input("", key="audio_input_" + key)
    if audio:
        with open("audio.wav", "wb") as f:
            f.write(audio.getbuffer())
        text = get_whisper().transcribe("audio.wav", language="fr", fp16=False)["text"]
        st.write(text)
        time.sleep(4)
    skip = st.button("Ignorer")
    if len(text) > 0 or skip:
        add_grievances(key, supposed_state, text)
        st.rerun()

zdc = st.selectbox("Sélectionner gare", get_all_zdc(), index=None)

if zdc is None:
    st.stop()

if not (accessibility := get_accessibilite(zdc)).empty:
    st.info(accessibility["accessibility_level_name"].iloc[0].capitalize())

zdc_formatted = (
    zdc.replace(" - ", "_")
    .replace(" ", "_")
    .replace("é", "e")
    .replace("è", "e")
    .replace("-", "_")
    .lower()
)
path = Path(f"static/img/{zdc_formatted}.png")
if path.exists():
    st.image(str(path))

for type_of_equipment, d in get_list_of_equipements(zdc).items():
    for key, values in d.items():
        left, middle_left, middle_right, right = st.columns(
            [0.3, 0.1, 0.3, 0.3], vertical_alignment="center"
        )

        state = values.get("state")

        if type_of_equipment == "elevators":
            left.write(str(values["liftsituation"] or "ascenseur inconnu"))
        elif type_of_equipment == "escalators":
            left.write(str(values["etage"] or "escalator inconnu"))

        middle_left.image(f"static/img/{type_of_equipment}.png", width=50)

        if state == AVAILABLE or state == UNCERTAIN_AVAILABLE:
            message = "signaler un problème"
            middle_right.image(
                "static/img/thumb-up.png",
                width=20,
            )
        elif state == UNAVAILABLE or state == UNCERTAIN_UNAVAILABLE:
            message = "l'équipement fonctionne"
            middle_right.image(
                "static/img/thumb-down.png",
                width=20,
            )
            middle_right.markdown(" / ".join(values["reasons_grievances"]))
        else:
            message = "décrire le fonctionnement de l'équipement"
            middle_right.image(
                "static/img/question.png",
                width=20,
            )

        if right.button(message, key=key):
            grieve(
                key,
                (
                    AVAILABLE
                    if state in [UNAVAILABLE, UNCERTAIN_UNAVAILABLE]
                    else (
                        UNAVAILABLE
                        if state in [AVAILABLE, UNCERTAIN_AVAILABLE]
                        else UNCERTAIN  # stays uncertain whatever the message
                    )
                ),
            )
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_02_elevate_us/accessibility-waze-main/main.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une interface utilisateur (IHM), Conception de prompts, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce code définit un prompt pour interagir avec un modèle d'IA, spécifiant que la réponse doit être en français et au format JSON.
### 🚌 Spécificités fonctionnelles
Le prompt est conçu pour garantir que les réponses de l'IA sont en français et structurées, ce qui est essentiel pour des applications nécessitant une intégration facile des réponses de l'IA.
### ✍ Réutilisabilité
Le prompt est réutilisable pour toute application nécessitant des interactions avec un modèle d'IA, en particulier pour obtenir des réponses structurées en JSON.
### 📜 Snippet de code
```python
prompt_test = " Réponds en Francais et en json : {input}"
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm/Hackathon_équipe8/config/prompts.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une interface utilisateur (IHM), Création d\'une API, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
This code sets up a FastAPI application with CORS middleware and defines an endpoint to summarize user data from a JSON file. It returns an HTML response with the total number of users and their names.
### 🚌 Spécificités fonctionnelles
The code provides a summary of user data, which is useful for applications that need to display user statistics or profiles.
### ✍ Réutilisabilité
The code is modular and can be reused for setting up similar API endpoints that need to handle JSON data and return HTML responses. The CORS setup is also reusable for other FastAPI applications.
### 📜 Snippet de code
```python
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://10.244.1.53:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open('../../frontend-angular/db.json', 'r') as file:
    data = json.load(file)

users = data['users']

@app.get("/summarize_user_data", response_class=HTMLResponse)
async def summarize_user_data():
    summary = {
        "total_users": len(users),
        "total_preferences": len(users),
        "user_names": [user["name"] for user in users]
    }
    html_content = f"""
    <html>
        <body>
            <h1>Summary:</h1>
            <pre>{json.dumps(summary, indent=4)}</pre>
        </body>
    </html>
    """
    return html_content
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main%20%-%20%idfm_hackaton_2024-main/backend/api-reading-conversations/main.py)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une interface utilisateur (IHM), Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce code définit un processeur audio pour la lecture de données audio. Il gère les messages entrants pour remplir un tampon de données audio et traite ces données pour les envoyer à un canal de sortie audio.
### 🚌 Spécificités fonctionnelles
Le code répond à des besoins de traitement audio en temps réel, ce qui est crucial pour des applications interactives ou multimédia.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant un traitement audio en temps réel dans un contexte de travail audio Web. Il est modulaire et peut être intégré dans d'autres projets nécessitant une gestion de tampon audio.
### 📜 Snippet de code
```javascript
class AudioPlaybackWorklet extends AudioWorkletProcessor {
    constructor() {
        super();
        this.port.onmessage = this.handleMessage.bind(this);
        this.buffer = [];
    }

    handleMessage(event) {
        if (event.data === null) {
            this.buffer = [];
            return;
        }
        this.buffer.push(...event.data);
    }

    process(inputs, outputs, parameters) {
        const output = outputs[0];
        const channel = output[0];

        if (this.buffer.length > channel.length) {
            const toProcess = this.buffer.slice(0, channel.length);
            this.buffer = this.buffer.slice(channel.length);
            channel.set(toProcess.map(v => v / 32768));
        } else {
            channel.set(this.buffer.map(v => v / 32768));
            this.buffer = [];
        }

        return true;
    }
}

registerProcessor("audio-playback-worklet", AudioPlaybackWorklet);
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/app/public/audio-playback-worklet.js)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une interface utilisateur (IHM), Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce code définit un processeur audio qui convertit des données audio en format float32 en format int16. Il traite les entrées audio et envoie les données converties via un port de message.
### 🚌 Spécificités fonctionnelles
Le code répond à des besoins de conversion de format audio, essentiel pour le traitement et la transmission de données audio dans des formats compatibles.
### ✍ Réutilisabilité
Le code est précieux pour les applications nécessitant une conversion de format audio, notamment pour l'interopérabilité entre différents systèmes audio. Sa modularité permet une intégration facile dans d'autres projets.
### 📜 Snippet de code
```javascript
const MIN_INT16 = -0x8000;
const MAX_INT16 = 0x7fff;

class PCMAudioProcessor extends AudioWorkletProcessor {
    constructor() {
        super();
    }

    process(inputs, outputs, parameters) {
        const input = inputs[0];
        if (input.length > 0) {
            const float32Buffer = input[0];
            const int16Buffer = this.float32ToInt16(float32Buffer);
            this.port.postMessage(int16Buffer);
        }
        return true;
    }

    float32ToInt16(float32Array) {
        const int16Array = new Int16Array(float32Array.length);
        for (let i = 0; i < float32Array.length; i++) {
            let val = Math.floor(float32Array[i] * MAX_INT16);
            val = Math.max(MIN_INT16, Math.min(MAX_INT16, val));
            int16Array[i] = val;
        }
        return int16Array;
    }
}

registerProcessor("audio-processor-worklet", PCMAudioProcessor);
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/app/public/audio-processor-worklet.js)

---

<div style="page-break-after: always;"></div>

# 💡 Création d\'une interface utilisateur (IHM), Utilisation d\'Angular, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce composant Angular gère plusieurs fonctionnalités, notamment l'ajout de deux à un nombre donné, la récupération de résumés de conversations et de données utilisateur, ainsi que l'obtention d'intentions et d'entités à partir d'un message. Il utilise des appels API pour interagir avec des services backend.
### 🚌 Spécificités fonctionnelles
Le composant répond à des besoins fonctionnels tels que l'analyse de données utilisateur et de conversations, ainsi que l'interaction avec des services backend pour enrichir l'expérience utilisateur.
### ✍ Réutilisabilité
Le code est modulaire et utilise des appels API pour des fonctionnalités spécifiques, ce qui le rend réutilisable dans d'autres projets nécessitant des interactions similaires avec des services backend.
### 📜 Snippet de code
```javascript
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-directions',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './directions.component.html',
  styleUrls: ['./directions.component.css']
})
export class DirectionsComponent implements OnInit {
  inputNumber: number | null = null;
  result: number | null = null;
  loading: boolean = false;
  conversationSummary: string = '';
  userDataSummary: string = '';
  optionsAndMetadata: string = '';
  message: string = '';
  intentionsEntities: string = '';

  addTwo() {
    if (this.inputNumber !== null) {
      this.loading = true;
      fetch(`http://localhost:8002/add_two/${this.inputNumber}`)
        .then(response => response.json())
        .then(data => {
          this.result = data.result;
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
          alert('Error fetching data');
        });
    }
  }

  fetchConversationSummary() {
    fetch('http://localhost:8003/summarize_conversations')
      .then(response => response.text())
      .then(data => {
        this.conversationSummary = data;
      })
      .catch(() => {
        alert('Error fetching conversation summary');
      });
  }

  fetchUserDataSummary() {
    fetch('http://localhost:8003/summarize_user_data')
      .then(response => response.text())
      .then(data => {
        this.userDataSummary = data;
      })
      .catch(() => {
        alert('Error fetching user data summary');
      });
  }

  fetchOptionsAndMetadata() {
    fetch('http://localhost:8002/options_and_metadata')
      .then(response => response.json())
      .then(data => {
        this.optionsAndMetadata = JSON.stringify(data, null, 2);
      })
      .catch(() => {
        alert('Error fetching options and metadata');
      });
  }

  fetchIntentionsEntities() {
    if (this.message.trim() !== '') {
      fetch('http://localhost:8001/get_intentions_entites', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: this.message })
      })
      .then(response => response.json())
      .then(data => {
        this.intentionsEntities = JSON.stringify(data, null, 2);
      })
      .catch(() => {
        alert('Error fetching intentions and entities');
      });
    }
  }

  ngOnInit() {
    this.fetchConversationSummary();
    this.fetchUserDataSummary();
    this.fetchOptionsAndMetadata();
  }
}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/components/directions/directions.component.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Fonctionnalités de cartographie, 
## 🌟 Équipe : **equipe_10_ivoice**
### 👨‍🏫 Description du code
Ce code crée une carte interactive de Paris avec des marqueurs pour chaque station de métro spécifiée. Chaque marqueur affiche un message contextuel lorsqu'il est cliqué.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de visualiser des informations de transport en commun sur une carte, ce qui est essentiel pour les applications de mobilité.
### ✍ Réutilisabilité
Le code utilise la bibliothèque Folium pour créer des cartes interactives, ce qui est réutilisable pour toute application nécessitant une visualisation géographique des données.
### 📜 Snippet de code
```python
import folium

def create_map(messages_dict):
    paris = [48.8566, 2.3522]
    carto = folium.Map(location=paris, zoom_start=12)
    stations = [
        "Pont de Sèvres", "Billancourt", "Marcel Sembat", "Porte de Saint-Cloud", "Exelmans", "Michel-Ange - Molitor",
        "Jasmin", "Ranelagh", "La Muette", "Rue de la Pompe", "Trocadéro", "Iéna", "Alma-Marceau", "Franklin D. Roosevelt",
        "Saint-Philippe-du-Roule", "Miromesnil", "Saint-Augustin", "Havre - Caumartin", "Chaussée d'Antin - La Fayette",
        "Richelieu - Drouot", "Grands Boulevards", "Bonne Nouvelle", "Strasbourg - Saint-Denis", "République", "Oberkampf",
        "Saint-Ambroise", "Voltaire", "Charonne", "Rue des Boulets", "Nation", "Buzenval", "Maraîchers", "Porte de Montreuil",
        "Robespierre", "Croix de Chavaux", "Mairie de Montreuil"
    ]
    latitudes = [
        48.823964, 48.835907, 48.836888, 48.839375, 48.841398, 48.844135, 48.848396, 48.856180, 48.860417, 48.865891,
        48.863516, 48.865298, 48.863292, 48.869229, 48.872070, 48.876091, 48.874364, 48.874632, 48.874384, 48.871696,
        48.870002, 48.869400, 48.867317, 48.866147, 48.863762, 48.861379, 48.857391, 48.852542, 48.847788, 48.849933,
        48.850933, 48.850716, 48.853238, 48.861215, 48.871215
    ]
    longitudes = [
        2.233380, 2.239462, 2.246494, 2.259622, 2.264682, 2.268228, 2.273601, 2.278307, 2.280910, 2.282769, 2.288353,
        2.293115, 2.300285, 2.307716, 2.312528, 2.316154, 2.320072, 2.328104, 2.333535, 2.339269, 2.348722, 2.354295,
        2.363048, 2.369687, 2.377587, 2.383494, 2.389027, 2.392810, 2.397401, 2.406544, 2.412216, 2.418861, 2.432307,
        2.440926, 2.446745
    ]
    for station, lat, lon in zip(stations, latitudes, longitudes):
        message_voyageur = messages_dict.get(station)
        popup_content = f"""<div style="font-size:16px;"><b style="color:blue; font-size:20px;">{station}</b><br><span style="font-size:18px;">{message_voyageur}</span></div>"""
        folium.Marker([lat, lon], popup=folium.Popup(popup_content, max_width=400, min_width=200)).add_to(carto)
    html_string = carto.get_root().render()
    return html_string
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_10_ivoice/ivoice-main/src/front_map.py)

---

<div style="page-break-after: always;"></div>

# 💡 Génération de données, 
## 🌟 Équipe : **equipe_07_tranquiliscore**
### 👨‍🏫 Description du code
Cette fonction génère une liste de timestamps à intervalles réguliers de 5 minutes entre deux dates données.
### 🚌 Spécificités fonctionnelles
Génère des intervalles de temps réguliers pour structurer des données temporelles dans un jeu de données.
### ✍ Réutilisabilité
Utile pour générer des séries temporelles à intervalles réguliers, applicable dans divers contextes nécessitant des données temporelles.
### 📜 Snippet de code
```python
def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

dts = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in 
       datetime_range(datetime(2023, 11, 1, 6), datetime(2023, 11, 15, 23), 
       timedelta(minutes=5))]
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_07_tranquiliscore/tranquili-score-main/pre-processing-creation-squelette-jddonness.py)

---

<div style="page-break-after: always;"></div>

# 💡 Génération de données, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce fichier génère des données fictives pour des utilisateurs, incluant des trajets favoris, des informations de billettique, des lieux favoris, des centres d'intérêts, des kilomètres de marche, et des informations sur l'accessibilité PMR.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de simuler des données utilisateurs pour tester des fonctionnalités liées aux transports et à la billettique.
### ✍ Réutilisabilité
Les fonctions de génération de données sont modulaires et peuvent être réutilisées pour simuler des données utilisateurs dans d'autres projets nécessitant des données de transport ou de billettique.
### 📜 Snippet de code
```python
def generate_trips(): ... def generate_ticket_info(): ... def generate_favorite_places(): ... def generate_interests(): ... def generate_km_walked(): ... def generate_pmr(): ... def generate_event_interest(): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm%20%-%20%Hackathon-IDFM/generation_base_userid.py)

---

<div style="page-break-after: always;"></div>

# 💡 Génération de données, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce fichier génère des messages personnalisés pour les utilisateurs en fonction de leurs centres d'intérêts et des événements disponibles en Île-de-France.
### 🚌 Spécificités fonctionnelles
Le code permet de recommander des événements pertinents aux utilisateurs, enrichissant ainsi leur expérience culturelle et sociale.
### ✍ Réutilisabilité
Les fonctions de sélection d'événements pertinents et de génération de messages peuvent être réutilisées pour d'autres applications nécessitant une personnalisation basée sur les intérêts des utilisateurs.
### 📜 Snippet de code
```python
def get_relevant_events(user_interests, df_events): ... def generate_custom_message(user_data, events): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm%20%-%20%Hackathon-IDFM/prompt_évènement.py)

---

<div style="page-break-after: always;"></div>

# 💡 Génération de données, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Cette fonction génère une représentation textuelle de la structure d'un répertoire, en excluant les chemins spécifiés.
### 🚌 Spécificités fonctionnelles
Facilite la visualisation de la structure de fichiers, ce qui est essentiel pour comprendre l'organisation d'un projet.
### ✍ Réutilisabilité
Utile pour visualiser la structure de répertoires dans divers contextes, notamment pour des outils de documentation ou d'analyse de projets.
### 📜 Snippet de code
```python
def print_directory_structure(start_path: str, exclusion_patterns: Set[str]) -> str:
    def _generate_tree(dir_path: str, prefix: str = '') -> List[str]:
        entries = os.listdir(dir_path)
        entries = sorted(entries, key=lambda x: (not os.path.isdir(os.path.join(dir_path, x)), x.lower()))
        tree = []
        for i, entry in enumerate(entries):
            rel_path = os.path.relpath(os.path.join(dir_path, entry), start_path)
            if is_excluded(rel_path, exclusion_patterns):
                continue
            
            if i == len(entries) - 1:
                connector = '└── '
                new_prefix = prefix + '    '
            else:
                connector = '├── '
                new_prefix = prefix + '│   '
            
            full_path = os.path.join(dir_path, entry)
            if os.path.isdir(full_path):
                tree.append(f"{prefix}{connector}{entry}/")
                tree.extend(_generate_tree(full_path, new_prefix))
            else:
                tree.append(f"{prefix}{connector}{entry}")
        return tree

    tree = ['/ '] + _generate_tree(start_path)
    return '\n'.join(tree)
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/blob/main/dump.py)

---

<div style="page-break-after: always;"></div>

# 💡 Génération de données, 
## 🌟 Équipe : **equipe_10_ivoice**
### 👨‍🏫 Description du code
Génère des messages basés sur les itinéraires et les informations d'incident fournies.
### 🚌 Spécificités fonctionnelles
Facilite la communication des informations d'incident aux utilisateurs finaux.
### ✍ Réutilisabilité
La fonction est modulaire et peut être utilisée pour générer des messages pour différents types d'incidents et itinéraires.
### 📜 Snippet de code
```python
def message_generation(itineraries: dict[str, list[Itinerary]], infos_incident: str): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_10_ivoice/ivoice-main/src/front.py)

---

<div style="page-break-after: always;"></div>

# 💡 Génération de données, 
## 🌟 Équipe : **equipe_10_ivoice**
### 👨‍🏫 Description du code
Génère des itinéraires alternatifs en utilisant l'ID de ligne spécifié.
### 🚌 Spécificités fonctionnelles
Permet de proposer des solutions de repli en cas de perturbation sur une ligne de transport.
### ✍ Réutilisabilité
Peut être réutilisé pour calculer des itinéraires alternatifs pour différentes lignes, ce qui est crucial pour la planification de trajets.
### 📜 Snippet de code
```python
def itineraire_generation(): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_10_ivoice/ivoice-main/src/front.py)

---

<div style="page-break-after: always;"></div>

# 💡 Géocodage, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Cette classe fournit des méthodes pour géocoder et géocoder inversement des adresses en utilisant l'API de data.gouv.fr.
### 🚌 Spécificités fonctionnelles
Permet la conversion d'adresses en coordonnées et vice versa, essentiel pour les applications de navigation et de localisation.
### ✍ Réutilisabilité
La classe est modulaire et peut être intégrée dans d'autres projets nécessitant des services de géocodage, facilitant la conversion entre adresses et coordonnées.
### 📜 Snippet de code
```python
class GeocodingAPI: ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/api/geocode.py)

---

<div style="page-break-after: always;"></div>

# 💡 Géocodage, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce code utilise l'API de géolocalisation du navigateur pour obtenir la position actuelle de l'utilisateur, puis utilise une fonction de géocodage inversé pour obtenir l'adresse correspondante.
### 🚌 Spécificités fonctionnelles
Permet de récupérer la position actuelle de l'utilisateur et de la convertir en une adresse lisible, ce qui est essentiel pour des applications de navigation ou de services basés sur la localisation.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant la géolocalisation de l'utilisateur et la conversion de coordonnées en adresse. Il est modulaire et peut être intégré dans divers projets nécessitant des fonctionnalités de localisation.
### 📜 Snippet de code
```javascript
import { reverseGeocode } from '../api/geocoding';

export const getCurrentLocation = async (): Promise<{ address: string; latitude: number; longitude: number }> => {
    try {
        const position = await new Promise<GeolocationPosition>((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(resolve, reject);
        });
        const { latitude, longitude } = position.coords;
        const address = await reverseGeocode(latitude, longitude);
        return { address, latitude, longitude };
    } catch (error) {
        console.error('Erreur de géolocalisation:', error);
        throw new Error('Impossible d\'obtenir votre position actuelle');
    }
};
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/app/src/utils/geolocation.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Intégration avec un Data Lake, 
## 🌟 Équipe : **equipe_02_elevate_us**
### 👨‍🏫 Description du code
Ce code initialise un système de fichiers S3 en utilisant un point de terminaison AWS personnalisé et liste les documents dans un répertoire S3 spécifique.
### 🚌 Spécificités fonctionnelles
Permet l'accès aux données partagées pour le hackathon, facilitant ainsi l'intégration et le traitement des données.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant l'accès à des fichiers stockés sur un système S3, en particulier dans des environnements où les variables d'environnement sont utilisées pour configurer les points de terminaison.
### 📜 Snippet de code
```python
S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": S3_ENDPOINT_URL})
fs.ls("dlb-hackathon/datasets-diffusion", refresh=True)
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_02_elevate_us/accessibility-waze-main%20%-%20%accessibility-waze-main/add_station_accessibility.py)

---

<div style="page-break-after: always;"></div>

# 💡 Intégration avec un Data Lake, 
## 🌟 Équipe : **equipe_10_ivoice**
### 👨‍🏫 Description du code
Cette fonction charge un fichier Parquet depuis un bucket S3 spécifié et le retourne sous forme de DataFrame Pandas.
### 🚌 Spécificités fonctionnelles
Permet de centraliser et simplifier l'accès aux données stockées sur S3 pour le projet.
### ✍ Réutilisabilité
La fonction est générique et peut être réutilisée pour charger n'importe quel fichier Parquet depuis S3, ce qui est utile pour la gestion de données volumineuses.
### 📜 Snippet de code
```python
def load_parquet_from_s3(bucket: str, file_key: str) -> pd.DataFrame: ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_10_ivoice/ivoice-main/src/dataloaders.py)

---

<div style="page-break-after: always;"></div>

# 💡 Intégration avec un Data Lake, Manipulation de données, 
## 🌟 Équipe : **equipe_02_elevate_us**
### 👨‍🏫 Description du code
Ce fichier Python contient des fonctions pour évaluer l'état des équipements tels que les ascenseurs et les escaliers en utilisant des données historiques et des réclamations. Il utilise DuckDB pour interroger des données stockées sur S3 et pandas pour le traitement des données.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de surveiller l'état des équipements de transport en commun, en particulier les ascenseurs et les escaliers, en utilisant des données historiques et des réclamations pour fournir une évaluation précise de leur disponibilité.
### ✍ Réutilisabilité
Le code est précieux pour son intégration avec DuckDB et S3, permettant de traiter efficacement de grandes quantités de données. Les fonctions sont modulaires et peuvent être réutilisées pour d'autres projets nécessitant une évaluation de l'état des équipements basés sur des données historiques et des réclamations.
### 📜 Snippet de code
```python
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
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_02_elevate_us/accessibility-waze-main/accessibility-waze-main/add_state_to_equipements.py)

---

<div style="page-break-after: always;"></div>

# 💡 Intégration avec un Data Lake, Manipulation de données, 
## 🌟 Équipe : **equipe_02_elevate_us**
### 👨‍🏫 Description du code
Cette fonction ajoute une réclamation concernant un équipement spécifique, en catégorisant le commentaire et en enregistrant les données dans un fichier CSV sur S3.
### 🚌 Spécificités fonctionnelles
Permet de suivre et de catégoriser les réclamations sur les équipements, ce qui est essentiel pour la maintenance et l'amélioration des services.
### ✍ Réutilisabilité
La fonction est utile pour toute application nécessitant la gestion et le stockage de réclamations ou de feedbacks utilisateurs, avec une catégorisation automatique des commentaires.
### 📜 Snippet de code
```python
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
    with fs.open(FILE_PATH_OUT_S3, "a") as file_out:
        df.to_csv(file_out, header=None)
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_02_elevate_us/accessibility-waze-main%20%-%20%accessibility-waze-main/edit_grievances.py)

---

<div style="page-break-after: always;"></div>

# 💡 Intégration avec un Data Lake, Manipulation de données, 
## 🌟 Équipe : **equipe_02_elevate_us**
### 👨‍🏫 Description du code
Ce code lit un fichier CSV depuis un bucket S3, traite les données par groupe d'équipement, puis réécrit le fichier mis à jour dans le même emplacement S3.
### 🚌 Spécificités fonctionnelles
Gère les doléances liées aux équipements en les regroupant par identifiant d'équipement.
### ✍ Réutilisabilité
Le code est réutilisable pour toute opération de lecture/écriture de fichiers CSV sur S3, ce qui est courant dans les applications de traitement de données.
### 📜 Snippet de code
```python
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
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_02_elevate_us/accessibility-waze-main/handle_grievances.py)

---

<div style="page-break-after: always;"></div>

# 💡 Intégration avec un Data Lake, Utilisation de Retrieval-Augmented Generation (RAG), 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce code configure l'accès à un stockage S3 en utilisant DuckDB pour exécuter des requêtes SQL sur des fichiers stockés dans un environnement cloud.
### 🚌 Spécificités fonctionnelles
Le code permet de configurer l'accès à des données stockées dans le cloud, facilitant ainsi l'analyse de données à grande échelle.
### ✍ Réutilisabilité
La configuration de DuckDB pour accéder à un stockage S3 est hautement réutilisable pour tout projet nécessitant l'accès à des données stockées dans le cloud.
### 📜 Snippet de code
```python
# Paramétrage pour un appel Duckdb
%pip install duckdb
import duckdb as ddb
ddb.execute("SET s3_region='fr-central';")
ddb.execute("SET s3_url_style='path';")
ddb.execute("SET s3_endpoint='minio.data-platform-self-service.net';")
ddb.execute(f"SET s3_access_key_id='{os.environ["AWS_ACCESS_KEY_ID"]}' ;") # Aussi récupérable dans les paramètres "Valeurs de Helm" du service
ddb.execute(f"SET s3_secret_access_key='{os.environ["AWS_SECRET_ACCESS_KEY"]}';") # Aussi récupérable dans les paramètres "Valeurs de Helm" du service
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/resultats/repositories/equipe_08_maidfm/Hackathon-IDFM-main/notebooks/HIAM2024)

---

<div style="page-break-after: always;"></div>

# 💡 Machine Learning (ML), 
## 🌟 Équipe : **equipe_07_tranquiliscore**
### 👨‍🏫 Description du code
Ce code encode les colonnes 'Gare_A' et 'Gare_B' en variables indicatrices et applique la fonction de classification des indices sur les colonnes de score.
### 🚌 Spécificités fonctionnelles
Prépare les données pour l'entraînement de modèles de machine learning en encodant les catégories et en classifiant les scores.
### ✍ Réutilisabilité
L'encodage en variables indicatrices est une technique standard en machine learning, réutilisable pour préparer des données catégorielles pour des modèles.
### 📜 Snippet de code
```python
df_encoded = pd.get_dummies(df, columns=['Gare_A','Gare_B'], dtype=int)

df_encoded["Indice_troncon_AB"] = df_encoded["Indice_troncon_AB"].apply(class_from_indice)
df_encoded["Indice_gare_A"] = df_encoded["Indice_gare_A"].apply(class_from_indice)
df_encoded["Indice_gare_B"] = df_encoded["Indice_gare_B"].apply(class_from_indice)
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_07_tranquiliscore/tranquili-score-main/classifier.ipynb)

---

<div style="page-break-after: always;"></div>

# 💡 Manipulation de données, 
## 🌟 Équipe : **equipe_02_elevate_us**
### 👨‍🏫 Description du code
Cette fonction lit un fichier CSV contenant des arrêts de lignes et retourne une liste unique de noms de stations de métro.
### 🚌 Spécificités fonctionnelles
Répond au besoin de lister toutes les stations de métro pour des analyses ou des visualisations spécifiques au projet.
### ✍ Réutilisabilité
La fonction est réutilisable pour extraire et manipuler des données de stations de métro à partir de fichiers CSV, ce qui est utile pour des analyses de données ou des applications de transport.
### 📜 Snippet de code
```python
def get_all_stations() -> list[str]:
    referential = pd.read_csv("static/arrets-lignes.csv", sep=";")
    referential = referential[referential["mode"] == "Metro"]
    return referential["stop_name"].sort_values().unique()
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_02_elevate_us/accessibility-waze-main%20%-%20%accessibility-waze-main/back.py)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Convertit du texte en parole et enregistre le résultat sous forme de fichier audio.
### 🚌 Spécificités fonctionnelles
Améliore l'accessibilité en permettant la conversion de texte en audio, utile pour les utilisateurs malvoyants.
### ✍ Réutilisabilité
Cette fonction est réutilisable dans des applications nécessitant des capacités de synthèse vocale, comme les assistants vocaux ou les applications d'accessibilité.
### 📜 Snippet de code
```python
def text_to_speech(text, filename, audio_folder='audio'): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/api/functions.py)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce hook React gère la navigation en temps réel en utilisant la géolocalisation et l'orientation de l'appareil pour guider l'utilisateur le long d'un itinéraire prédéfini. Il utilise des API de géolocalisation pour suivre la position de l'utilisateur et des événements d'orientation pour ajuster les instructions de navigation.
### 🚌 Spécificités fonctionnelles
Fournit des instructions de navigation basées sur la position actuelle et l'orientation de l'appareil, avec des retours vocaux pour améliorer l'accessibilité.
### ✍ Réutilisabilité
Le hook est modulaire et peut être réutilisé dans d'autres projets nécessitant une navigation en temps réel. Il intègre des API natives pour la géolocalisation et l'orientation, ce qui le rend adaptable à divers cas d'utilisation de navigation.
### 📜 Snippet de code
```javascript
import { useState, useEffect } from 'react';

const useNavigation = () => {
    const [currentStep, setCurrentStep] = useState(0);
    const [route, setRoute] = useState([]);
    const [currentLocation, setCurrentLocation] = useState(null);
    const [deviceOrientation, setDeviceOrientation] = useState(null);

    useEffect(() => {
        fetchRouteData();
        requestLocationPermission();
        startLocationTracking();
        startOrientationTracking();

        return () => {
            navigator.geolocation.clearWatch(watchId);
            window.removeEventListener('deviceorientation', handleDeviceOrientation);
        };
    }, []);

    const fetchRouteData = async () => {
        // Fetch route data logic
    };

    const requestLocationPermission = async () => {
        if ('geolocation' in navigator) {
            const permission = await navigator.permissions.query({ name: 'geolocation' });
            if (permission.state !== 'granted') {
                alert('Location permission is required for navigation.');
            }
        } else {
            alert('Geolocation is not supported by your browser.');
        }
    };

    let watchId: any;
    const startLocationTracking = () => {
        watchId = navigator.geolocation.watchPosition(
            (position) => {
                setCurrentLocation(position.coords);
                checkNextStep(position.coords);
            },
            (error) => {
                console.error('Error getting location:', error);
            },
            { enableHighAccuracy: true, timeout: 5000, maximumAge: 0 }
        );
    };

    const startOrientationTracking = () => {
        window.addEventListener('deviceorientation', handleDeviceOrientation);
    };

    const handleDeviceOrientation = (event) => {
        const { alpha, beta, gamma } = event;
        setDeviceOrientation({ alpha, beta, gamma });
    };

    const checkNextStep = (coords) => {
        if (currentStep < route.length) {
            const nextPoint = route[currentStep].geopoint;
            const distance = calculateDistance(coords, nextPoint);
            const direction = calculateDirection(coords, nextPoint);

            if (distance < 10) {
                handleNextStep();
            } else {
                provideDirectionalGuidance(direction);
            }
        }
    };

    const calculateDistance = (point1, point2) => {
        // Haversine formula to calculate distance between two points
    };

    const calculateDirection = (from, to) => {
        const dx = to.longitude - from.longitude;
        const dy = to.latitude - from.latitude;
        let angle = Math.atan2(dy, dx) * 180 / Math.PI;
        if (angle < 0) {
            angle += 360;
        }
        return angle;
    };

    const provideDirectionalGuidance = (targetDirection) => {
        if (deviceOrientation) {
            const { beta, gamma } = deviceOrientation;
            const deviceHeading = Math.atan2(beta, gamma) * 180 / Math.PI;

            const relativeDirection = (targetDirection - deviceHeading + 360) % 360;

            let guidance;
            if (relativeDirection > 345 || relativeDirection <= 15) {
                guidance = "Straight ahead";
            } else if (relativeDirection > 15 && relativeDirection <= 75) {
                guidance = "Turn slight right";
            } else if (relativeDirection > 75 && relativeDirection <= 105) {
                guidance = "Turn right";
            } else if (relativeDirection > 105 && relativeDirection <= 165) {
                guidance = "Turn sharp right";
            } else if (relativeDirection > 165 && relativeDirection <= 195) {
                guidance = "Turn around";
            } else if (relativeDirection > 195 && relativeDirection <= 255) {
                guidance = "Turn sharp left";
            } else if (relativeDirection > 255 && relativeDirection <= 285) {
                guidance = "Turn left";
            } else {
                guidance = "Turn slight left";
            }

            if ('speechSynthesis' in window) {
                const utterance = new SpeechSynthesisUtterance(guidance);
                window.speechSynthesis.speak(utterance);
            } else {
                console.log('Speech synthesis not supported');
            }
        }
    };

    const handleNextStep = () => {
        // Logic to handle moving to the next step
    };

    return {
        currentStep,
        route,
        currentLocation,
        deviceOrientation,
        setRoute,
        handleNextStep,
    };
};

export default useNavigation;
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/app/src/hooks/orientation.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce fichier contient les instructions pour un assistant IA spécialisé dans la mobilité, adapté aux besoins des utilisateurs avec différents types de handicaps.
### 🚌 Spécificités fonctionnelles
Fournit des directives pour adapter les interactions de l'IA aux besoins spécifiques des utilisateurs handicapés, améliorant ainsi l'accessibilité et l'efficacité de l'assistance.
### ✍ Réutilisabilité
Les instructions sont réutilisables pour configurer des assistants IA dans des contextes similaires, en particulier pour des applications nécessitant une personnalisation en fonction des handicaps.
### 📜 Snippet de code
```python
INSTRUCTIONS = """Tu es un assistant IA spécialisé dans la mobilité, capable de t'adapter aux besoins spécifiques de chaque utilisateur en fonction de ses handicaps. Voici comment tu dois te comporter :

1. Analyse attentivement la liste des handicaps fournie pour chaque utilisateur.

2. Si l'utilisateur a un handicap cognitif, utilise le langage FALC (Facile à Lire et à Comprendre) :
   - Utilise des mots simples et des phrases courtes.
   - Explique les idées complexes étape par étape.
   - Évite les métaphores et le langage figuré.
   - Sois direct et concret dans tes explications.

3. Pour les handicaps physiques :
   - Propose des solutions adaptées à leurs capacités motrices.
   - Sois attentif aux besoins d'accessibilité spécifiques.

4. Pour les handicaps sensoriels (vue, ouïe) :
   - Adapte tes recommandations en conséquence.
   - Suggère des alternatives ou des aides techniques appropriées.

5. Reste patient, bienveillant et prêt à reformuler ou à donner plus de détails si nécessaire.

6. Concentre-toi sur les capacités de l'utilisateur plutôt que sur ses limitations.

7. Propose toujours des solutions sûres et pratiques pour améliorer la mobilité de l'utilisateur.

8. Si l'utilisateur te demande d'analyser le contenu du bande son d'une annonce :
    - Demande-lui de te faire écouter l'annonce.
    - Analyse le contenu audio et indique ce qu'il contient, par exemple pour une personne sourde.

Adapte ton langage et tes recommandations en fonction des handicaps spécifiques de chaque utilisateur pour offrir une assistance personnalisée et efficace.

Voici la liste des handicaps possibles pour un utilisateur:
- Cognitifs : déficience auditiva, déficience visuelle, déficience à la parole, déficience en raison de l'échec de la connaissance
- Physiques : maladie cardiovasculaire, maladie respiratoire, maladie neurologique, handicap cérébral
- Sensoriels : handicap auditif, handicap visuel

L'utilisateur actuel a les handicap suivants :
- Visuel : déficient visuel

Commencez la conversation en demandant à l'utilisateur où il veut aller. 
C'est un échange vocal, donc soyez concis. Sois interactif, demande à l'utilisateur de choisir sans tout detailler par exemple.

PARLE TOUJOURS EN FRANCAIS.

ATTENTION : POUR DONNER UNE DIRECTION TU DOIS UTILISER LES OUTILS DISPONIBLES ! ET SI BESOIN DEMANDER A UTILISATEUR DE PRECISER SA DEMANDE.

```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main%20%-%20%MobilIA/server/src/server/prompt.py)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce code définit une classe AudioPlaybackWorklet qui hérite de AudioWorkletProcessor. Elle gère la lecture audio en traitant les messages reçus et en ajustant le buffer audio pour la sortie.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de traitement audio en temps réel, essentiel pour des applications interactives ou multimédia.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant un traitement audio en temps réel dans un contexte de travail audio Web. Il offre une abstraction pour gérer les buffers audio.
### 📜 Snippet de code
```javascript
class AudioPlaybackWorklet extends AudioWorkletProcessor { ... }
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/server/src/server/static/audio-playback-worklet.js)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce code définit une classe PCMAudioProcessor qui convertit des buffers audio de float32 à int16, puis envoie les données traitées via un port de message.
### 🚌 Spécificités fonctionnelles
Le code assure la conversion de données audio, ce qui est crucial pour l'interopérabilité entre différents systèmes audio.
### ✍ Réutilisabilité
La conversion de formats audio est une tâche courante dans le traitement audio numérique, rendant ce code utile pour d'autres projets nécessitant une telle conversion.
### 📜 Snippet de code
```javascript
class PCMAudioProcessor extends AudioWorkletProcessor { ... }
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/server/src/server/static/audio-processor-worklet.js)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_06_mob_ia**
### 👨‍🏫 Description du code
Ce code utilise Streamlit pour créer une interface utilisateur permettant de rechercher des itinéraires avec Mob'IA. Il intègre la géolocalisation, la reconnaissance vocale, et la synthèse vocale.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de fournir une interface utilisateur interactive pour la recherche d'itinéraires, intégrant des fonctionnalités de géolocalisation et de traitement vocal.
### ✍ Réutilisabilité
L'intégration de la géolocalisation et des services de conversion texte-parole et parole-texte est précieuse pour des applications interactives nécessitant une interface utilisateur simple et efficace.
### 📜 Snippet de code
```python
import streamlit as st ... st.audio(audio, autoplay=True)
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_06_mob_ia/hackathon_idfm_octo_2024-main/hackathon_idfm_octo_2024-main/streamlit.py)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_06_mob_ia**
### 👨‍🏫 Description du code
Cette fonction utilise la reconnaissance vocale pour convertir la parole en texte, en utilisant l'API de Google.
### 🚌 Spécificités fonctionnelles
Permet l'interaction vocale avec l'application, facilitant l'accessibilité et l'utilisation mains libres.
### ✍ Réutilisabilité
La fonction est réutilisable pour toute application nécessitant une interface de commande vocale ou de transcription.
### 📜 Snippet de code
```python
def recognize_speech() -> str: ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_06_mob_ia/hackathon_idfm_octo_2024-main/sources/converter/speech_to_text.py)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_06_mob_ia**
### 👨‍🏫 Description du code
Ce code utilise la bibliothèque gTTS pour convertir un texte en audio, en générant un fichier audio en mémoire.
### 🚌 Spécificités fonctionnelles
Répond à un besoin d'accessibilité en permettant la conversion de texte en audio.
### ✍ Réutilisabilité
La fonction est réutilisable pour toute application nécessitant une conversion de texte en audio, notamment pour des fonctionnalités d'accessibilité ou des assistants vocaux.
### 📜 Snippet de code
```python
from gtts import gTTS
from io import BytesIO

def generate_audio(text: str) -> BytesIO:
    sound_file = BytesIO()
    tts = gTTS(text, lang='fr')
    tts.write_to_fp(sound_file)

    return sound_file
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_06_mob_ia/hackathon_idfm_octo_2024-main/sources/converter/text_to_speech.py)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Déclaration du composant ChatComponent, qui inclut un enregistreur vocal et utilise des fichiers de template et de style spécifiques.
### 🚌 Spécificités fonctionnelles
Intègre un enregistreur vocal, ce qui peut être crucial pour des fonctionnalités de chat vocal ou d'interaction utilisateur.
### ✍ Réutilisabilité
Le composant est modulaire et peut être réutilisé dans d'autres parties de l'application ou dans d'autres projets nécessitant une fonctionnalité de chat.
### 📜 Snippet de code
```javascript
@Component({
  selector: 'app-chat',
  imports: [VoiceRecorderComponent],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css'
})
export class ChatComponent {

}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/components/chat/chat.component.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce fichier définit une interface TypeScript pour représenter les données d'un enregistrement audio, incluant le blob audio, la durée et le titre.
### 🚌 Spécificités fonctionnelles
L'interface structure les données audio de manière standardisée, facilitant leur manipulation et leur intégration dans d'autres composants ou services.
### ✍ Réutilisabilité
L'interface est réutilisable dans tout projet nécessitant une structure de données pour gérer des enregistrements audio. Elle fournit une abstraction claire pour manipuler les données audio.
### 📜 Snippet de code
```javascript
export interface RecordedAudioOutput {
    blob: Blob;
    duration: number;
    title: string;
  }
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/models/recorded-audio-output.model.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce fichier contient un test unitaire pour le service AudioRecorderService, vérifiant que le service est correctement créé.
### 🚌 Spécificités fonctionnelles
Le test assure que le service AudioRecorderService est instancié correctement, ce qui est essentiel pour garantir la fiabilité des fonctionnalités d'enregistrement audio.
### ✍ Réutilisabilité
Le test est un exemple de test unitaire de base pour un service Angular, réutilisable comme modèle pour tester d'autres services dans des projets Angular.
### 📜 Snippet de code
```javascript
import { TestBed } from '@angular/core/testing';

import { AudioRecorderService } from './audio-recorder.service';

describe('AudioRecorderService', () => {
  let service: AudioRecorderService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AudioRecorderService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/services/audio-recorder.service.spec.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, Utilisation d\'Angular, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code est un test unitaire pour le composant Angular VoiceRecorderComponent. Il vérifie que le composant peut être créé sans erreur.
### 🚌 Spécificités fonctionnelles
Assure la création correcte du composant VoiceRecorder, ce qui est crucial pour le bon fonctionnement de l'application.
### ✍ Réutilisabilité
Les tests unitaires sont essentiels pour garantir la stabilité et la fiabilité du code. Ce modèle de test peut être réutilisé pour tester d'autres composants Angular.
### 📜 Snippet de code
```javascript
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VoiceRecorderComponent } from './voice-recorder.component';

describe('VoiceRecorderComponent', () => {
  let component: VoiceRecorderComponent;
  let fixture: ComponentFixture<VoiceRecorderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VoiceRecorderComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VoiceRecorderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/components/voice-recorder/voice-recorder.component.spec.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement audio ou vocal, Utilisation d\'Angular, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce composant Angular gère l'enregistrement audio, y compris le démarrage, l'arrêt, l'effacement et le téléchargement de l'enregistrement. Il utilise un service pour gérer la logique d'enregistrement et un sanitizer pour sécuriser les URL des blobs audio.
### 🚌 Spécificités fonctionnelles
Le composant répond au besoin de capturer et de gérer des enregistrements audio dans une application web, ce qui peut être utile pour des fonctionnalités de reconnaissance vocale ou de messagerie vocale.
### ✍ Réutilisabilité
Le composant est modulaire et peut être réutilisé dans d'autres projets nécessitant une fonctionnalité d'enregistrement audio. Il encapsule la logique d'enregistrement et d'interaction avec le DOM de manière propre.
### 📜 Snippet de code
```javascript
import { Component } from '@angular/core';
import { AudioRecorderService } from '../../services/audio-recorder.service';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';
import { RecordedAudioOutput } from '../../models/recorded-audio-output.model';
import { blob } from 'stream/consumers';

@Component({
  selector: 'app-voice-recorder',
  imports: [],
  templateUrl: './voice-recorder.component.html',
  styleUrl: './voice-recorder.component.css'
})
export class VoiceRecorderComponent {
  isRecording = false;
  recordedTime = '00:00';
  blobUrl!: SafeUrl;
  recordedAudio!: RecordedAudioOutput;

  constructor(private audioRecordingService: AudioRecorderService,
private sanitizer: DomSanitizer) { 
  this.audioRecordingService.getRecordingFailed().subscribe(() => {
    this.isRecording = false;
  });

}

  startRecording() {
    this.isRecording = true;
    this.audioRecordingService.startRecording();
    this.audioRecordingService.getRecordedTime().subscribe((time) => {
      this.recordedTime = time;
    });
  }

  stopRecording() {
    this.isRecording = false;
    this.audioRecordingService.stopRecording();
    this.audioRecordingService.getRecorded().subscribe(event => {
      this.recordedAudio = event;
    });
    this.blobUrl = this.sanitizer.bypassSecurityTrustUrl(URL.createObjectURL(this.recordedAudio.blob));
  }

  clearRecording() {
    this.blobUrl = ''; 
    this.recordedTime = '00:00';
    this.isRecording = false;
  }

  downloadRecording() {
    const url = window.URL.createObjectURL(this.recordedAudio.blob);
    const link =document.createElement('a');
    link.href = url;
    link.download = this.recordedAudio.title + '.webm';
    link.click();
  }

}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/components/voice-recorder/voice-recorder.component.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement d\'images, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Analyse une image pour en extraire une description, puis traduit cette description dans une langue cible en utilisant l'API OpenAI.
### 🚌 Spécificités fonctionnelles
Facilite la traduction et la compréhension de descriptions d'images, ce qui est essentiel pour les utilisateurs multilingues.
### ✍ Réutilisabilité
Cette fonction est précieuse pour les applications nécessitant une traduction automatique de descriptions d'images, facilitant l'internationalisation.
### 📜 Snippet de code
```python
def analyze_and_translate_image(image_path, target_language="en"): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/api/functions.py)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement d\'images, Conception de prompts, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Analyse une image en utilisant GPT-4 Vision et retourne une description.
### 🚌 Spécificités fonctionnelles
Permet l'analyse d'images pour extraire des informations textuelles ou contextuelles, utile dans des applications de reconnaissance d'image.
### ✍ Réutilisabilité
Cette fonction est réutilisable pour toute application nécessitant une analyse d'image automatisée, en intégrant GPT-4 Vision pour l'analyse de contenu visuel.
### 📜 Snippet de code
```python
@tool
async def analyze_image(image_url: str, prompt: Optional[str] = None):
    ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/server/src/server/tools.py)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement du langage naturel (NLP), 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Cette classe implémente un chatbot utilisant un modèle de langage GPT pour répondre aux messages en fonction de l'intention détectée.
### 🚌 Spécificités fonctionnelles
Répond aux besoins de communication automatisée avec les utilisateurs, en intégrant des capacités de compréhension du langage naturel.
### ✍ Réutilisabilité
La structure de la classe et l'utilisation de modèles GPT la rendent réutilisable pour divers cas d'utilisation de chatbots nécessitant une compréhension du langage naturel.
### 📜 Snippet de code
```python
class Chatbot:
    def __init__(self, history):
        self.client = Client()
        self.client = self.client.get_client()
        self.model = 'gpt-4o-mini'

    def ask_gpt(self, conversation_history, message):
        nlu = Nlu()
        intention = nlu.get_intentions_entites(message)
        if (intention == "RELATED_IDFM"){
            retrun "Comment je peux vous aider"
        }
        else{
            retrun ""
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/blob/main/backend/api-llm/src/chat.py)

---

<div style="page-break-after: always;"></div>

# 💡 Traitement du langage naturel (NLP), 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code utilise un module NLU pour analyser un message et extraire les intentions et entités. Il est utilisé pour comprendre les requêtes utilisateur concernant les itinéraires.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de comprendre les requêtes utilisateur en langage naturel pour fournir des informations sur les itinéraires.
### ✍ Réutilisabilité
Le code est réutilisable pour toute application nécessitant une compréhension du langage naturel pour extraire des intentions et des entités, ce qui est crucial pour les systèmes de dialogue et les assistants virtuels.
### 📜 Snippet de code
```python
from nlu import Nlu

nlu = Nlu()
message = "Donne moi l'itinéraire entre Poissy et Puteaux"
answer = nlu.get_intentions_entites(message)

answer
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main%20%-%20%idfm_hackaton_2024/backend/api-llm/src/test-llm.ipynb)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation d\'Angular, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code configure un serveur Express pour servir une application Angular côté serveur. Il utilise Angular Universal pour le rendu côté serveur et sert des fichiers statiques depuis un dossier spécifique.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de servir une application Angular avec rendu côté serveur, ce qui est essentiel pour le SEO et les performances initiales de chargement.
### ✍ Réutilisabilité
Le code est réutilisable pour toute application Angular nécessitant un rendu côté serveur avec Express. Il offre une structure modulaire pour servir des applications Angular universelles.
### 📜 Snippet de code
```javascript
import { APP_BASE_HREF } from '@angular/common';
import { CommonEngine, isMainModule } from '@angular/ssr/node';
import express from 'express';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import bootstrap from './main.server';

const serverDistFolder = dirname(fileURLToPath(import.meta.url));
const browserDistFolder = resolve(serverDistFolder, '../browser');
const indexHtml = join(serverDistFolder, 'index.server.html');

const app = express();
const commonEngine = new CommonEngine();

app.get(
  '**',
  express.static(browserDistFolder, {
    maxAge: '1y',
    index: 'index.html'
  }),
);

app.get('**', (req, res, next) => {
  const { protocol, originalUrl, baseUrl, headers } = req;

  commonEngine
    .render({
      bootstrap,
      documentFilePath: indexHtml,
      url: `${protocol}://${headers.host}${originalUrl}`,
      publicPath: browserDistFolder,
      providers: [{ provide: APP_BASE_HREF, useValue: baseUrl }],
    })
    .then((html) => res.send(html))
    .catch((err) => next(err));
});

if (isMainModule(import.meta.url)) {
  const port = process.env['PORT'] || 4000;
  app.listen(port, () => {
    console.log(`Node Express server listening on http://localhost:${port}`);
  });
}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/server.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation d\'Angular, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code configure le rendu côté serveur pour une application Angular en fusionnant la configuration de l'application avec des paramètres spécifiques au serveur.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de rendre l'application Angular côté serveur, ce qui est crucial pour les applications nécessitant un rendu universel.
### ✍ Réutilisabilité
La fusion de configurations pour le rendu côté serveur est une pratique réutilisable dans les applications Angular nécessitant un rendu universel, ce qui est courant pour améliorer le SEO et les performances.
### 📜 Snippet de code
```javascript
import { mergeApplicationConfig, ApplicationConfig } from '@angular/core';
import { provideServerRendering } from '@angular/platform-server';
import { appConfig } from './app.config';

const serverConfig: ApplicationConfig = {
  providers: [
    provideServerRendering(),
  ]
};

export const config = mergeApplicationConfig(appConfig, serverConfig);
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/app.config.server.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation d\'Angular, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code configure l'application Angular pour le client, en définissant des fournisseurs pour la détection des changements de zone, le routage, et l'hydratation du client avec relecture d'événements.
### 🚌 Spécificités fonctionnelles
Le code assure une configuration client robuste pour l'application Angular, en intégrant des fonctionnalités essentielles comme le routage et l'hydratation.
### ✍ Réutilisabilité
La configuration modulaire et l'utilisation de fournisseurs pour des fonctionnalités spécifiques comme le routage et l'hydratation sont des pratiques réutilisables dans de nombreuses applications Angular.
### 📜 Snippet de code
```javascript
import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideClientHydration, withEventReplay } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
  providers: [provideZoneChangeDetection({ eventCoalescing: true }), provideRouter(routes), provideClientHydration(withEventReplay())]
};
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/app.config.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation d\'Angular, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code définit les routes pour une application Angular, associant des chemins d'URL à des composants spécifiques.
### 🚌 Spécificités fonctionnelles
Permet la navigation entre différentes sections de l'application, telles que les préférences, le chat, et les directions.
### ✍ Réutilisabilité
La configuration des routes est un aspect fondamental et réutilisable dans toute application Angular, facilitant la navigation et la gestion des vues.
### 📜 Snippet de code
```javascript
export const routes: Routes = [
  {
    path: '',
    component: LandingComponent,
    title: 'Landing',
  }, {
    path: 'preferences',
    component: PreferencesComponent,
    title: 'Preferences',
  },
  {
    path: 'chat',
    component: ChatComponent,
    title: 'Chat',
  },
  {
    path: 'directions',
    component: DirectionsComponent,
    title: 'Directions',
  }
];
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/app.routes.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation d\'Angular, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code est un test unitaire pour le composant Angular PreferencesComponent. Il vérifie que le composant peut être créé sans erreur.
### 🚌 Spécificités fonctionnelles
Assure la création correcte du composant Preferences, ce qui est crucial pour le bon fonctionnement de l'application.
### ✍ Réutilisabilité
Les tests unitaires sont essentiels pour garantir la stabilité et la fiabilité du code. Ce modèle de test peut être réutilisé pour tester d'autres composants Angular.
### 📜 Snippet de code
```javascript
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PreferencesComponent } from './preferences.component';

describe('PreferencesComponent', () => {
  let component: PreferencesComponent;
  let fixture: ComponentFixture<PreferencesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PreferencesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PreferencesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/components/preferences/preferences.component.spec.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation d\'Angular, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Déclaration du composant Angular PreferencesComponent, qui gère les préférences utilisateur dans l'application.
### 🚌 Spécificités fonctionnelles
Fournit une structure de base pour la gestion des préférences utilisateur dans l'application.
### ✍ Réutilisabilité
Ce composant est réutilisable dans toute application Angular nécessitant une gestion des préférences utilisateur.
### 📜 Snippet de code
```javascript
import { Component } from '@angular/core';

@Component({
  selector: 'app-preferences',
  imports: [],
  templateUrl: './preferences.component.html',
  styleUrl: './preferences.component.css'
})
export class PreferencesComponent {

}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/components/preferences/preferences.component.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation d\'autres API, Géocodage, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce fichier contient des fonctions pour la géocodage et le géocodage inverse en utilisant l'API de l'adresse de data.gouv.fr. Il permet de convertir des adresses en coordonnées géographiques et vice versa.
### 🚌 Spécificités fonctionnelles
Facilite la conversion entre adresses et coordonnées géographiques, ce qui est crucial pour les applications de mobilité et de cartographie.
### ✍ Réutilisabilité
Les fonctions `geocode` et `reverseGeocode` sont réutilisables pour toute application nécessitant la conversion entre adresses et coordonnées géographiques, ce qui est essentiel pour les services de localisation.
### 📜 Snippet de code
```javascript
import axios from 'axios';
import { getCurrentLocation } from '../utils/geolocation';

interface ReverseGeocodeResult {
    features: {
        properties: {
            label: string;
            score: number;
            housenumber: string;
            id: string;
            name: string;
            postcode: string;
            citycode: string;
            x: number;
            y: number;
            city: string;
            context: string;
            type: string;
            importance: number;
            street: string;
        };
    }[];
}

export async function reverseGeocode(lat: number, lon: number): Promise<string> {

    
    try {
        const response = await axios.get<ReverseGeocodeResult>(
            `https://api-adresse.data.gouv.fr/reverse/?lon=${lon}&lat=${lat}`
        );

        if (response.data.features.length > 0) {
            const address = response.data.features[0].properties;
            return `${address.housenumber || ''} ${address.street}, ${address.postcode} ${address.city}`.trim();
        } else {
            throw new Error('No address found for the given coordinates');
        }
    } catch (error) {
        console.error('Error in reverse geocoding:', error);
        throw error;
    }
}

interface GeocodeResult {
    features: {
        geometry: {
            coordinates: [number, number];
        };
        properties: {
            label: string;
            score: number;
            id: string;
            name: string;
            postcode: string;
            citycode: string;
            x: number;
            y: number;
            city: string;
            context: string;
            type: string;
            importance: number;
            street?: string;
        };
    }[];
}

export async function geocode(address: string): Promise<{ lat: number; lon: number; label: string }[]> {
    try {
        const { latitude, longitude } = await getCurrentLocation();
        const response = await axios.get<GeocodeResult>(
            `https://api-adresse.data.gouv.fr/search/?q=${encodeURIComponent(address)}&limit=10&lat=${latitude}&lon=${longitude}`
        );

        if (response.data.features.length > 0) {
            return response.data.features.map(feature => {
                const [lon, lat] = feature.geometry.coordinates;
                return {
                    lat,
                    lon,
                    label: feature.properties.label
                };
            });
        } else {
            throw new Error('No coordinates found for the given address');
        }
    } catch (error) {
        console.error('Error in geocoding:', error);
        throw error;
    }
}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/app/src/api/geocoding.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation d\'autres API, Géocodage, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Cette classe et méthode permettent de géocoder une adresse en utilisant l'API de géocodage du gouvernement français. Elle retourne une liste de suggestions de coordonnées géographiques.
### 🚌 Spécificités fonctionnelles
Fournit des suggestions de géocodage précises pour des adresses en France, centrées sur Paris.
### ✍ Réutilisabilité
Le code est réutilisable pour toute application nécessitant une conversion d'adresses en coordonnées géographiques. Il est basé sur une API publique et gère les erreurs de requête.
### 📜 Snippet de code
```python
class GeocodingAPI:
    def __init__(self):
        self.base_url = "https://api-adresse.data.gouv.fr"

    async def geocode(self, address: str) -> list:
        try:
            response = requests.get(f"{self.base_url}/search/", params={
                "q": address,
                "limit": 10,
                "lat": 48.8566,
                "lon": 2.3522
            })
            response.raise_for_status()
            data = response.json()

            if data["features"]:
                results = []
                for feature in data["features"]:
                    lon, lat = feature["geometry"]["coordinates"]
                    results.append({
                        "lat": lat,
                        "lon": lon,
                        "label": feature["properties"]["label"]
                    })
                return results
            else:
                raise ValueError("No coordinates found for the given address")
        except requests.RequestException as error:
            print(f"Error in geocoding: {error}")
            raise
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main%20%-%20%MobilIA/server/src/server/geocode.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation d\'autres API, Utilisation de LangChain, 
## 🌟 Équipe : **equipe_06_mob_ia**
### 👨‍🏫 Description du code
Cette fonction effectue une recherche d'itinéraire entre un point de départ et une destination, en tenant compte de divers paramètres comme la date, l'heure, et l'accessibilité.
### 🚌 Spécificités fonctionnelles
Répond au besoin de calculer des itinéraires personnalisés, y compris pour les personnes à mobilité réduite.
### ✍ Réutilisabilité
La fonction est hautement réutilisable pour toute application nécessitant des calculs d'itinéraires personnalisés en Île-de-France.
### 📜 Snippet de code
```python
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
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_06_mob_ia/hackathon_idfm_octo_2024-main/sources/agent/tools/get_itineraire.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation d\'un référentiel d\'événements, Utilisation de Retrieval-Augmented Generation (RAG), 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Cette classe effectue la clusterisation des utilisateurs en fonction de leurs données personnelles et de leurs comportements, en utilisant l'algorithme KMeans.
### 🚌 Spécificités fonctionnelles
Permet de segmenter les utilisateurs pour des analyses ou des actions marketing ciblées.
### ✍ Réutilisabilité
La classe est hautement réutilisable pour tout projet nécessitant une segmentation des utilisateurs basée sur des caractéristiques multiples, grâce à son approche modulaire et paramétrable.
### 📜 Snippet de code
```python
class UserClustering:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        
    def preprocess_data_for_knn(self, df):
        df = df.copy()
        
        le = LabelEncoder()
        df['billettique_type'] = le.fit_transform(df['billettique_type'])
        
        df['billettique_tickets_left'] = df['billettique_tickets_left'].fillna(0)
        
        df['PMR'] = df['PMR'].astype(int)
        
        mlb = MultiLabelBinarizer()
        interests = df["centres d'intérêts"].apply(eval)
        interest_encoded = mlb.fit_transform(interests)
        interest_df = pd.DataFrame(interest_encoded, columns=mlb.classes_, index=df.index)
        df = pd.concat([df, interest_df], axis=1)
        df.drop(columns=["centres d'intérêts"], inplace=True)
        
        df['nombre_trajets'] = df['trajets'].apply(lambda x: len(eval(x)))
        df.drop(columns=['trajets'], inplace=True)
        
        def average_coordinates(lieux):
            lieux = eval(lieux)
            avg_lat = np.mean([coord[0] for coord in lieux])
            avg_lon = np.mean([coord[1] for coord in lieux])
            return avg_lat, avg_lon

        df[['lieux_avg_lat', 'lieux_avg_lon']] = df['lieux favoris'].apply(
            lambda x: pd.Series(average_coordinates(x))
        )
        df.drop(columns=['lieux favoris'], inplace=True)
        
        numeric_cols = ['km de marche dans les 90 derniers jours', 'intérêt événements']
        
        return df[numeric_cols + ['user_id', 'billettique_type', 'billettique_tickets_left', 'PMR', 
                                'nombre_trajets', 'lieux_avg_lat', 'lieux_avg_lon'] + list(mlb.classes_)]

    def fit_transform(self, df):
        processed_df = pd.DataFrame()
        processed_df['user_id'] = df['user_id']

        processed_df = self.preprocess_data_for_knn(df)
        
        features = processed_df.drop('user_id', axis=1).values
        scaled_features = self.scaler.fit_transform(features)
        
        clusters = self.kmeans.fit_predict(scaled_features)
        
        result = pd.DataFrame({
            'user_id': df['user_id'],
            'cluster': clusters
        })
        
        return result
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm%20%-%20%Hackathon-IDFM-main/domain/clusterisation.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de LangChain, 
## 🌟 Équipe : **equipe_04_mobiwize**
### 👨‍🏫 Description du code
Ce code définit un outil de formatage générique, prêt à être utilisé dans un cadre plus large où des informations doivent être formatées ou traitées.
### 🚌 Spécificités fonctionnelles
Fournit une structure de base pour l'intégration d'outils de formatage dans des applications, avec une description et un nom configurables.
### ✍ Réutilisabilité
Ce code est réutilisable comme un modèle pour créer des outils de traitement ou de formatage dans des applications nécessitant une telle fonctionnalité.
### 📜 Snippet de code
```javascript
import {tool} from "@langchain/core/tools";

export const formatTool = tool(
  () => {

  },
  {
    name: "format_tool",
    description:
      "This tool should be called when the informations are available it can end the integration",
  }
)
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_04_mobiwize%20%-%20%ai-framework-main/https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/blob/main/packages/ai-toolkit/src/tools/format.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de Retrieval-Augmented Generation (RAG), 
## 🌟 Équipe : **equipe_04_mobiwize**
### 👨‍🏫 Description du code
Cette fonction exécute la recherche en utilisant les étapes définies dans le plan de recherche et invoque le graphe de recherche pour obtenir des documents pertinents.
### 🚌 Spécificités fonctionnelles
Permet l'exécution séquentielle des étapes de recherche définies.
### ✍ Réutilisabilité
Le code est conçu pour être réutilisé dans différents contextes de recherche en utilisant un graphe de recherche modulaire.
### 📜 Snippet de code
```javascript
export const conductResearch = async (state: typeof RetrievalGraphAnnotation.State): Promise<RetrievalGraphReturnType> => { if (!state.steps || state.steps.length === 0) { throw new Error("No research steps found"); } const result = await researcherGraph.invoke({ question: state.steps[0], messages: [] }); return { documents: result.documents, steps: state.steps.slice(1) }; };
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_04_mobiwize/ai-framework-main/packages/ai-toolkit/src/graphs/rag/index.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de Retrieval-Augmented Generation (RAG), Conception de prompts, 
## 🌟 Équipe : **equipe_04_mobiwize**
### 👨‍🏫 Description du code
Définit un ensemble de prompts utilisés pour guider le système de récupération d'informations dans différentes situations.
### 🚌 Spécificités fonctionnelles
Fournit des instructions claires pour guider le comportement du système de recherche.
### ✍ Réutilisabilité
Les prompts sont centralisés et peuvent être facilement modifiés ou étendus pour d'autres systèmes de récupération d'informations.
### 📜 Snippet de code
```javascript
export const RETRIEVAL_PROMPTS = { ROUTER_SYSTEM_PROMPT: `You are a research assistant...`, GENERAL_SYSTEM_PROMPT: `You are a research assistant...`, MORE_INFO_SYSTEM_PROMPT: `You are a research assistant...`, RESEARCH_PLAN_SYSTEM_PROMPT: `You are an expert researcher...`, RESPONSE_SYSTEM_PROMPT: `You are an expert researcher...` } as const;
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_04_mobiwize/ai-framework-main/packages/ai-toolkit/src/graphs/rag/prompts.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de Retrieval-Augmented Generation (RAG), Traitement audio ou vocal, Utilisation de Websockets, Utilisation d\'Angular, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce service Angular permet d'enregistrer de l'audio à partir du microphone de l'utilisateur. Il utilise l'API MediaRecorder pour capturer l'audio et RxJS pour gérer les flux de données asynchrones.
### 🚌 Spécificités fonctionnelles
Répond au besoin d'enregistrement audio dans une application web, avec gestion des erreurs et suivi du temps d'enregistrement.
### ✍ Réutilisabilité
Le service est modulaire et peut être réutilisé dans n'importe quelle application Angular nécessitant une fonctionnalité d'enregistrement audio. Il encapsule la logique complexe de l'enregistrement audio et fournit une interface simple via des observables.
### 📜 Snippet de code
```javascript
import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { RecordedAudioOutput } from '../models/recorded-audio-output.model';

@Injectable({
  providedIn: 'root'
})
export class AudioRecorderService {
  private recorder!: MediaRecorder;
  private stream!: MediaStream;
  private startTime!: Date;
  private interval: any;
  private _recorded: Subject<RecordedAudioOutput> = new Subject<RecordedAudioOutput>();
  private _recordingTime = new Subject<string>();
  private _recordingFailed = new Subject<string>();

  getRecorded(): Observable<RecordedAudioOutput> {
    return this._recorded.asObservable();
  }

  getRecordedTime(): Observable<string> {
    return this._recordingTime.asObservable();
  }

  getRecordingFailed(): Observable<string> {
    return this._recordingFailed.asObservable();
  }

  startRecording() {
    if (this.recorder) {
      return;
    }
    let chunks : Blob[] = [];

    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        this.stream = stream;
        this.recorder = new MediaRecorder(this.stream, { mimeType: 'audio/webm' });
        this.recorder.ondataavailable = (event: BlobEvent) => {
          chunks.push(event.data);
        }

        this.recorder.onstop = () => {
            this._recorded.next({ blob: new Blob(chunks, {type : 'audio/webm'}), duration: new Date().getTime() - this.startTime.getTime(), title: 'audio.webm' });
        }
        this.recorder.start();
        this.startTime = new Date();
        this.interval = setInterval(() => {
          const currentTime = new Date();
          const diffTime = currentTime.getTime() - this.startTime.getTime();
          const minutes = Math.floor(diffTime / 60000);
          const seconds = Math.floor((diffTime % 60000) / 1000);
          const time = this.toString(minutes) + ':' + this.toString(seconds);
          this._recordingTime.next(time);
        }, 1000);
      })
      .catch(() => {
        this._recordingFailed.next('Error recording');
      });
  }

  stopRecording() {
    if (this.recorder ) {
      this.recorder.stop();
      clearInterval(this.interval);
    }
  }

  abortRecording() {
    this.stopRecording();
  }

  private toString(value: number): string {
    return value < 10 ? '0' + value : value.toString();
  }
}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/frontend-angular/src/app/services/audio-recorder.service.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de Retrieval-Augmented Generation (RAG), Utilisation de LangChain, Conception de prompts, 
## 🌟 Équipe : **equipe_08_maidfm**
### 👨‍🏫 Description du code
Ce code définit un prompt personnalisé pour un modèle de RAG, spécifiant comment le modèle doit répondre aux questions en utilisant le contexte fourni.
### 🚌 Spécificités fonctionnelles
Assure que les réponses générées sont basées sur le contexte des documents, ce qui est crucial pour la précision des informations fournies.
### ✍ Réutilisabilité
Le prompt est adaptable pour diverses applications de RAG, facilitant l'intégration de données contextuelles dans les réponses générées par l'IA.
### 📜 Snippet de code
```python
from langchain_core.prompts import PromptTemplate

template = """
Tu es un agent d'assistance de recherche documentaire d'île de France mobilité (IDFM),
à partir des documents donnés donne toujours une réponse provenant du contexte.
Ne donne pas de réponse si le contexte ne te le permet pas.
Répond de manière concise, en trois phrases maximum.
Répond dans la langue de la question
Inclut toujours un extrait textuel des documents.

On dispose du contexte suivants : {context}

Utilisateur : "{question}"
Chat bot :

custom_rag_prompt = PromptTemplate.from_template(template)
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_08_maidfm/Hackathon-IDFM-main/notebooks/HIAM2024)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de Websockets, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Cette fonction asynchrone fusionne plusieurs flux asynchrones en un seul flux. Elle utilise asyncio pour gérer les tâches asynchrones et retourne un itérateur asynchrone de tuples contenant la clé du flux et la valeur.
### 🚌 Spécificités fonctionnelles
Permet de gérer efficacement plusieurs flux de données asynchrones, ce qui est essentiel pour des applications en temps réel.
### ✍ Réutilisabilité
La fonction 'amerge' est précieuse pour sa capacité à combiner plusieurs flux asynchrones en un seul, ce qui est utile dans des applications nécessitant la gestion simultanée de plusieurs sources de données asynchrones.
### 📜 Snippet de code
```python
async def amerge(**streams: AsyncIterator[T]) -> AsyncIterator[tuple[str, T]]: ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main%20%-%20%MobilIA/server/src/langchain_openai_voice/utils.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de Websockets, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Cette fonction gère la connexion à l'API OpenAI en utilisant un gestionnaire de contexte asynchrone. Elle envoie et reçoit des messages via un websocket, permettant une interaction en temps réel avec le modèle d'IA.
### 🚌 Spécificités fonctionnelles
Facilite l'intégration avec l'API OpenAI pour des interactions en temps réel, crucial pour des applications vocales ou de chat.
### ✍ Réutilisabilité
La fonction 'connect' est hautement réutilisable pour toute application nécessitant une connexion en temps réel avec l'API OpenAI, grâce à son abstraction des détails de connexion et de gestion des websockets.
### 📜 Snippet de code
```python
@asynccontextmanager async def connect(*, api_key: str, model: str, url: str) -> AsyncGenerator[...]: ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main%20%-%20%MobilIA/server/src/langchain_openai_voice/__init__.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de Websockets, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Gère un flux de données via WebSocket, permettant la réception continue de messages textuels.
### 🚌 Spécificités fonctionnelles
Permet la gestion de communications en temps réel, utile pour des applications interactives ou de suivi en direct.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant une communication en temps réel via WebSocket, en fournissant un modèle de flux asynchrone.
### 📜 Snippet de code
```python
async def websocket_stream(websocket: WebSocket) -> AsyncIterator[str]:
    ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/server/src/server/utils.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_04_mobiwize**
### 👨‍🏫 Description du code
Configuration ESLint pour le package UI, étendant une configuration interne et désactivant la règle 'no-redeclare'.
### 🚌 Spécificités fonctionnelles
Assure la conformité du code UI avec les standards internes tout en permettant des exceptions spécifiques comme 'no-redeclare'.
### ✍ Réutilisabilité
Permet de réutiliser une configuration ESLint standardisée pour les composants UI, facilitant la gestion des règles de codage.
### 📜 Snippet de code
```javascript
/** @type {import("eslint").Linter.Config} */
module.exports = {
  root: true,
  extends: ['@repo/eslint-config/react-internal.js'],
  parser: '@typescript-eslint/parser',
  rules: {
    'no-redeclare': 'off',
  },
};
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_04_mobiwize%20%-%20%ai-framework-main/packages/ui/.eslintrc.js)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce code définit une API Flask pour obtenir des directions de voyage en utilisant une API Directions personnalisée. Il extrait les paramètres de la requête, valide les entrées, et renvoie les informations de trajet.
### 🚌 Spécificités fonctionnelles
Répond aux besoins de calcul de trajets en tenant compte de l'accessibilité, ce qui est crucial pour les applications de transport inclusif.
### ✍ Réutilisabilité
Ce code est réutilisable pour toute application nécessitant des services de direction, en particulier pour des applications de mobilité ou de transport.
### 📜 Snippet de code
```python
directions = DirectionsAPI(api_key=os.getenv('DIRECTIONS_API_KEY', 'REMOVED'))

@app.route('/api/directions', methods=['GET'])
def get_directions():
    try:
        # Extract parameters from the request
        origin_long = request.args.get('origin_long')
        origin_lat = request.args.get('origin_lat')
        dest_long = request.args.get('dest_long')
        dest_lat = request.args.get('dest_lat')
        datetime_str = request.args.get('datetime')
        wheelchair = request.args.get('wheelchair', 'false').lower() == 'true'

        # Validate required parameters
        if not all([origin_long, origin_lat, dest_long, dest_lat, datetime_str]):
            return jsonify({"error": "Missing required parameters"}), 400

        # Get journey information
        journey_data = directions.get_journey_info(
            origin_long, origin_lat, dest_long, dest_lat, datetime_str, wheelchair
        )

        if journey_data is None:
            return jsonify({"error": "Failed to fetch journey information"}), 500

        # Parse journey data
        parsed_journeys = directions.parse_journey_data(journey_data)

        return jsonify(parsed_journeys)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/api/app.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Cette classe gère les directions en utilisant des points de départ et d'arrivée verbaux, les géocode en coordonnées, et récupère les informations de trajet via l'API PRIM.
### 🚌 Spécificités fonctionnelles
Répond aux besoins de calcul de trajets en temps réel, en tenant compte des perturbations et de l'accessibilité.
### ✍ Réutilisabilité
La classe est modulaire et peut être réutilisée pour intégrer des fonctionnalités de navigation dans d'autres applications. Elle encapsule la logique de géocodage et d'appel à l'API de transport.
### 📜 Snippet de code
```python
class DirectionsAPI: ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/api/directions.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce notebook Jupyter interagit avec l'API Navitia de PRIM pour obtenir des informations de trajet entre deux points géographiques, en tenant compte de l'accessibilité pour les fauteuils roulants.
### 🚌 Spécificités fonctionnelles
Répond aux besoins de planification de trajets en temps réel, avec une attention particulière à l'accessibilité pour les utilisateurs en fauteuil roulant.
### ✍ Réutilisabilité
Le code est précieux pour les applications nécessitant des calculs de trajets en temps réel, en particulier celles qui doivent prendre en compte l'accessibilité. Il peut être adapté pour d'autres services de transport ou d'itinéraires.
### 📜 Snippet de code
```python
from requests.auth import HTTPBasicAuth
import requests
import json
import pandas as pd

# API key
TOKEN = 'XDJujSkUHlvvCOirYONTwk9953G7thie'

# Affectation des coordonnées au départ et à l'arrivée
dlong = "2.357795224218518"
dlat = "48.881422645383765"
along = "2.2858484602361986"
alat = "48.846779058452746"

with_wheelchair = True

# Date et heure du trajet
jour = "20241121T150000"

# URL de l'API
destination = (dlong + "%3B%20" + dlat + "&to=" + along + "%3B%20" + alat + "&datetime=" + jour +
               ('&wheelchair=true&max_duration_to_pt=300&data_freshness=realtime' if with_wheelchair else '&data_freshness=realtime'))
url = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/journeys?from=' + destination

# Le header doit contenir la clé API : apikey, remplacer #VOTRE CLE API par votre clé API
headers = {'Accept': 'application/json', 'apikey': TOKEN}

# Envoi de la requête au serveur
req = requests.get(url, headers=headers)
print('Status:', req)

with open('response.json', 'w') as response:
    json.dump(req.json(), response, indent=4)

# Lecture du json
data_json = req.json()
# data = pd.json_normalize(req.json())

# Les différents trajets retournés sont dans data['journeys'][0]
print(data_json['journeys'][0]['distances'])

journeys = list()

labels = ['walking_distance']

for journey in data_json['journeys']:
    infos = list()
    infos.append(journey['distances']['walking'])
    journeys.append(infos)
    
df_journeys = pd.DataFrame(journeys, columns=labels)
df_journeys
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/navigation-api/apiNav.ipynb)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce script Python envoie une requête à l'API Navitia de PRIM pour obtenir des informations de trajet, puis normalise et affiche les données JSON reçues.
### 🚌 Spécificités fonctionnelles
Fournit une solution pour récupérer et afficher des informations de trajet, ce qui est essentiel pour des applications de planification de voyages ou de gestion de mobilité.
### ✍ Réutilisabilité
Le script est réutilisable pour toute application nécessitant des informations de trajet en temps réel. Il peut être facilement adapté pour d'autres API de transport ou pour intégrer des fonctionnalités similaires dans d'autres projets.
### 📜 Snippet de code
```python
from requests.auth import HTTPBasicAuth
import requests
import json
import pandas as pd

# TOKEN: XDJujSkUHlvvCOirYONTwk9953G7thie
TOKEN = 'XDJujSkUHlvvCOirYONTwk9953G7thie'

# Affectation des coordonnées au départ et à l'arrivée
dlong = "2.33792"
dlat = "48.85827"
along = "2.3588523"
alat = "48.9271087"

# Date et heure du trajet
jour = "20241121T073000"

# URL de l'API
destination = dlong + "%3B%20" + dlat + "&to=" + along + "%3B%20" + alat + "&datetime=" + jour
url = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/journeys?from=' + destination

# Le header doit contenir la clé API : apikey, remplacer #VOTRE CLE API par votre clé API
headers = {'Accept': 'application/json', 'apikey': TOKEN}

# Envoi de la requête au serveur
req = requests.get(url, headers=headers)

# Affichage du code réponse
print('Status:', req)

# Lecture du json
data = pd.json_normalize(req.json())

# Les différents trajets retournés sont dans data['journeys'][0]
print(data.head())
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/navigation-api/apiNavCommunication.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_06_mob_ia**
### 👨‍🏫 Description du code
Cette fonction appelle l'API PRIM pour rechercher un itinéraire entre une origine et une destination, avec des options pour la date, l'heure, et l'accessibilité.
### 🚌 Spécificités fonctionnelles
Gère les itinéraires en tenant compte des besoins spécifiques comme l'accessibilité pour les fauteuils roulants.
### ✍ Réutilisabilité
La fonction est hautement réutilisable pour toute application nécessitant des calculs d'itinéraires, en particulier avec des considérations d'accessibilité.
### 📜 Snippet de code
```python
def call_recherche_itineraire(...): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_06_mob_ia/hackathon_idfm_octo_2024-main/sources/api/api_prim.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_06_mob_ia**
### 👨‍🏫 Description du code
Cette fonction récupère les informations de trafic pour une ligne donnée en utilisant l'API PRIM.
### 🚌 Spécificités fonctionnelles
Fournit des informations sur les perturbations de trafic pour des lignes spécifiques.
### ✍ Réutilisabilité
Utile pour toute application nécessitant des mises à jour en temps réel sur l'état du trafic des lignes de transport.
### 📜 Snippet de code
```python
def call_info_trafic(ligne: str | None = None) -> pd.DataFrame: ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_06_mob_ia/hackathon_idfm_octo_2024-main/sources/api/api_prim.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_06_mob_ia**
### 👨‍🏫 Description du code
Ce code traite une réponse JSON contenant des informations sur un itinéraire et extrait des détails pertinents pour les étapes du trajet, les disruptions, et d'autres métadonnées.
### 🚌 Spécificités fonctionnelles
Répond à un besoin de traitement et d'analyse des données d'itinéraires pour les transports en commun.
### ✍ Réutilisabilité
La fonction est précieuse pour toute application nécessitant le traitement et l'analyse de données d'itinéraires, notamment dans le contexte des transports en commun.
### 📜 Snippet de code
```python
def process_dico(response: dict) -> dict:
    dicomax = {}

    itineraire = response['journeys'][0][0]

    etapes = {}

    for idx, step in enumerate(itineraire['sections']):
        try:
            etapes[idx] = {
                'durée': step['duration'],
                'arrivée': step['to']['name'],
                'départ': step['from']['name'],
                'chemin': {}
            }
        except KeyError:
            continue
        if 'path' in step:
            for idx2, _ in enumerate(step['path']):
                etapes[idx]['chemin'][idx2] = step['path'][idx2]['instruction']
            etapes[idx]['mode de mobilité'] = 'marche'
        else:
            try:
                etapes[idx]['chemin']['direction'] = step['display_informations']['direction']
                etapes[idx]['mode de mobilité'] = (
                    step['display_informations']['commercial_mode'] + ' ' +
                    step['display_informations']['label'])
            except KeyError:
                continue

    dicomax[f'Itineraire {itineraire['type']}'] = {
        'duration': itineraire['duration'],
        'nombre changement': itineraire['nb_transfers'],
        'heure de départ': itineraire['departure_date_time'],
        'heure d'arrivée': itineraire['arrival_date_time'],
        'heure demandée': itineraire['requested_date_time'],
        'distance marche': itineraire['distances']['walking'],
        'prix du trajet': itineraire['fare'],
        'étapes': etapes,
    }

    dicomax['problèmes'] = {}
    try:
        for idx, pb in enumerate(response['disruptions'][0]):
            source_pb = pb['messages'][1]['text'].split(' ')[0]
            dicomax['problèmes'][f'{source_pb}_{idx}'] = pb['messages'][1]['text'][len(source_pb):]
    except KeyError:
        pass

    return dicomax
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_06_mob_ia/hackathon_idfm_octo_2024-main/sources/entities/process_dico.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Cette fonction lit un fichier d'exclusion et extrait les motifs d'exclusion, les stockant dans un ensemble pour une utilisation ultérieure.
### 🚌 Spécificités fonctionnelles
Permet de filtrer les fichiers ou répertoires à exclure lors de l'analyse de la structure de fichiers.
### ✍ Réutilisabilité
La fonction est réutilisable pour tout projet nécessitant de gérer des motifs d'exclusion à partir d'un fichier, ce qui est courant dans les scripts de traitement de fichiers ou de répertoires.
### 📜 Snippet de code
```python
def parse_exclusion_file(file_path: str) -> Set[str]:
    patterns = set()
    if file_path and os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    patterns.add(line)
    return patterns
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/blob/main/dump.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Cette fonction définit une route API qui récupère des itinéraires en utilisant l'API PRIM de Île-de-France Mobilités. Elle construit une requête avec des coordonnées de départ et d'arrivée, ainsi qu'une date et heure actuelles, puis envoie une requête GET à l'API PRIM pour obtenir des données de trajet.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin fonctionnel de récupérer des informations de trajet en temps réel, ce qui est essentiel pour les applications de planification de voyage et de mobilité.
### ✍ Réutilisabilité
Ce code est précieux car il encapsule l'appel à l'API PRIM pour récupérer des itinéraires, ce qui est une fonctionnalité clé pour des applications de mobilité. Il peut être réutilisé dans d'autres projets nécessitant l'intégration avec l'API PRIM pour des fonctionnalités similaires.
### 📜 Snippet de code
```python
@app.get("/options_and_metadata")
def get_routes():
    departure = Coordinates(latitude=48.85021352679651,
                         longitude=2.4735419963428593)

    arrival = Coordinates(latitude=48.875460818207635,
                                longitude=2.3088650247211775)

    current_time = datetime.now()
    current_time = current_time.strftime("%Y%m%dT%H%M%S")

    destination = f"{departure.longitude}%3B%20{departure.latitude}&to={arrival.longitude}%3B%20{arrival.latitude}&datetime={current_time}"
    url = f"https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/journeys?from={destination}"

    headers = {"Accept": "application/json", "apikey": api_key}

    # API request
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError(
            f"Failed to fetch data. Status code: {response.status_code}, Message: {response.text}"
        )

    # Process response
    try:
        data = response.json()
        return data
    except Exception as e:
        raise ValueError(f"Error processing response: {e}")
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/backend/api-ml-model/main.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code envoie une requête à l'API PRIM pour obtenir des informations de trajet entre deux points géographiques à une date et heure spécifiées. Il utilise les coordonnées de départ et d'arrivée pour construire l'URL de la requête et affiche le statut de la réponse.
### 🚌 Spécificités fonctionnelles
Le code permet de récupérer des informations de trajet spécifiques à une date et heure données, ce qui est crucial pour les applications de planification de voyage.
### ✍ Réutilisabilité
Le code est réutilisable pour toute application nécessitant l'accès aux données de trajet de l'API PRIM. Il montre comment formater les requêtes et traiter les réponses JSON, ce qui est utile pour l'intégration de services de mobilité.
### 📜 Snippet de code
```python
dlong = "2.33792"
dlat = "48.85827"
along = "2.3588523"
alat = "48.9271087"

jour = "20241121T073000"

destination = dlong + "%3B%20" + dlat + "&to=" + along + "%3B%20" + alat + "&datetime=" + jour
url = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/journeys?from=' + destination

headers = {'Accept': 'application/json', 'apikey': apikey}

req = requests.get(url, headers=headers)

print('Status:',req)

data = pd.json_normalize(req.json())
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/backend/api-ml-model/notebooks/route.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce code interagit avec l'API PRIM pour récupérer des détails de trajets entre deux coordonnées GPS à une date et heure données.
### 🚌 Spécificités fonctionnelles
Répond au besoin de récupération de données de trajets pour des applications de mobilité en Île-de-France.
### ✍ Réutilisabilité
La fonction est hautement réutilisable pour toute application nécessitant des informations de trajet en Île-de-France, grâce à son abstraction des détails de l'API et son retour sous forme de DataFrame.
### 📜 Snippet de code
```python
import requests
import pandas as pd

from .specification import Coordinates


def get_journeys(
    api_key: str, departure: Coordinates, arrival: Coordinates, datetime: str
) -> pd.DataFrame:
    """
    Fetches journey details from the API.

    Args:
        api_key (str): API key for authentication.
        departure (Coordinates): Departure GPS coordinates.
        arrival (Coordinates): Arrival GPS coordinates.
        datetime (str): Date and time for the journey in the format YYYYMMDDTHHMMSS.

    Returns:
        pd.DataFrame: A DataFrame containing journey details.
    """
    destination = f"{departure.longitude}%3B%20{departure.latitude}&to={arrival.longitude}%3B%20{arrival.latitude}&datetime={datetime}"
    url = f"https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/journeys?from={destination}"

    headers = {"Accept": "application/json", "apikey": api_key}

    # API request
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError(
            f"Failed to fetch data. Status code: {response.status_code}, Message: {response.text}"
        )

    # Process response
    try:
        data = response.json()
        return data
    except Exception as e:
        raise ValueError(f"Error processing response: {e}")
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/backend/api-ml-model/src/api_mlmodel/journey.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_09_alterego**
### 👨‍🏫 Description du code
Ce script Python interagit avec l'API PRIM pour récupérer des informations de trajet entre deux points géographiques à une date et heure spécifiées. Il utilise la bibliothèque requests pour envoyer des requêtes HTTP et pandas pour traiter les données JSON reçues.
### 🚌 Spécificités fonctionnelles
Permet de calculer des itinéraires en utilisant l'API PRIM, ce qui est essentiel pour des applications de mobilité et de transport.
### ✍ Réutilisabilité
Le code est un bon exemple d'intégration avec l'API PRIM pour obtenir des informations de trajet. Il peut être réutilisé dans d'autres projets nécessitant des fonctionnalités similaires de calcul d'itinéraires.
### 📜 Snippet de code
```python
# %%
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path
import os

# Specify the path to the .env file
secrets_path = Path(os.getcwd() + '/../secrets.env').resolve()
load_dotenv(dotenv_path=secrets_path)
apikey = os.getenv('PRIM')


# %%
from requests.auth import HTTPBasicAuth
import requests
import json
import pandas as pd

#Affectation des coordonnées au départ et à l'arrivée
dlong = "2.33792"
dlat = "48.85827"
along = "2.3588523"
alat = "48.9271087"

#Date et heure du trajet
jour = "20241121T073000"

#URL de l'API
destination = dlong + "%3B%20" + dlat + "&to=" + along + "%3B%20" + alat + "&datetime=" + jour
url = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/journeys?from=' + destination

#Le header doit contenir la clé API : apikey, remplacer #VOTRE CLE API par votre clé API
headers = {'Accept': 'application/json', 'apikey': apikey}

#Envoi de la requête au serveur
req = requests.get(url, headers=headers)

#Affichage du code réponse
print('Status:',req)

#Lecture du json
data = pd.json_normalize(req.json())
# %%
journeys = data['journeys'][0].pop()

# %%
from IPython.display import JSON
JSON(journeys)

# %%

```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_09_alterego/idfm_hackaton_2024-main/notebooks/route.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_10_ivoice**
### 👨‍🏫 Description du code
Ce code interagit avec l'API PRIM pour obtenir des itinéraires de transport en commun, avec la possibilité d'exclure certaines lignes.
### 🚌 Spécificités fonctionnelles
Le code permet de calculer des itinéraires en transport en commun, ce qui est crucial pour les applications de mobilité.
### ✍ Réutilisabilité
Les fonctions d'itinéraire sont modulaires et peuvent être réutilisées pour toute application nécessitant des calculs d'itinéraires basés sur l'API PRIM.
### 📜 Snippet de code
```python
import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from dataloaders import load_arrets_et_lignes_associes

API_URL = "https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/"

def get_station_pos(station_id: str):
    station_data = load_arrets_et_lignes_associes()
    station_lon = station_data[station_data["stop_id"] == station_id]["stop_lon"].head(1).item()
    station_lat = station_data[station_data["stop_id"] == station_id]["stop_lat"].head(1).item()
    return (station_lon, station_lat)

def basic_itinerary(start_station_id: str, end_station_id: str, departure_time: datetime) -> dict:
    start_station_pos = get_station_pos(start_station_id)
    end_station_pos = get_station_pos(end_station_id)
    parameters = {
        "from": ";".join(start_station_pos),
        "to": ";".join(end_station_pos),
        "datetime": departure_time,
    }
    response = requests.get(url=API_URL, params=parameters, headers={"apiKey": os.environ["IDFM_API_KEY"]})
    return response.json()

def itinerary_with_line_exclusion(start_station_id: str, end_station_id: str, departure_time: datetime, excluded_line_id: str) -> dict:
    start_station_pos = get_station_pos(start_station_id)
    end_station_pos = get_station_pos(end_station_id)
    forbidden_uri = f"line:{excluded_line_id}"
    parameters = {
        "from": ";".join(start_station_pos),
        "to": ";".join(end_station_pos),
        "datetime": departure_time,
        "forbidden_uris[]": forbidden_uri,
    }
    response = requests.get(url=f"{API_URL}/journeys", params=parameters, headers={"apiKey": os.environ["IDFM_API_KEY"]})
    return response.json()
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_10_ivoice/ivoice-main/src/itinerary.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_10_ivoice**
### 👨‍🏫 Description du code
Cette classe calcule des itinéraires alternatifs en excluant certaines lignes, et utilise un cache pour stocker les résultats.
### 🚌 Spécificités fonctionnelles
Le code permet de calculer des itinéraires alternatifs, ce qui est essentiel pour offrir des options de transport flexibles aux utilisateurs.
### ✍ Réutilisabilité
La classe ItineraryCalculator est hautement réutilisable pour toute application nécessitant des calculs d'itinéraires alternatifs avec exclusion de lignes.
### 📜 Snippet de code
```python
from itinerary_data import Itinerary, Route
from dataloaders import load_arrets_et_lignes_associes
from itinerary import itinerary_with_line_exclusion
from datetime import datetime
from pathlib import Path
import json
from dacite import from_dict
from dataclasses import asdict

class ItineraryCalculator:
    def __init__(self):
        self.stations_by_lines = load_arrets_et_lignes_associes()
        self.standard_destination_ids = ["IDFM:483454", "IDFM:491486", "IDFM:22073", "IDFM:5823"]
        self.standard_itinerary_types = ["Centre de Paris", "Grands Boulevards", "Est de Paris", "Ouest de Paris"]

    def compute_alternate_itineraries(self, line_id: str) -> dict[str, Itinerary]:
        cache_file_path = Path(f"data/{line_id.split(':')[-1]}_cache.json")
        if cache_file_path.is_file():
            with cache_file_path.open('r', encoding="utf-8") as f:
                data = json.load(f)
                for key, val in data.items():
                    data[key] = [from_dict(Itinerary, it) for it in val]
            return data
        station_ids = self.stations_by_lines[self.stations_by_lines["id"] == line_id]["stop_id"]
        alt_itineraries = {}
        for station_id in station_ids:
            station_name = self.stations_by_lines[self.stations_by_lines["stop_id"] == station_id]["stop_name"].head(1).item()
            alt_itineraries[station_name] = []
            for std_destination_id, std_itin_type in zip(self.standard_destination_ids, self.standard_itinerary_types):
                destination_name = self.stations_by_lines[self.stations_by_lines["stop_id"] == std_destination_id]["stop_name"].head(1).item()
                itin = itinerary_with_line_exclusion(station_id, std_destination_id, datetime.now(), line_id)
                alt_itineraries[station_name].append(Itinerary.from_navitia_response(itin, std_itin_type, station_name, destination_name))
        cache_file_path.parent.mkdir(parents=True, exist_ok=True)
        with cache_file_path.open("w", encoding="utf-8") as f:
            data = {k: [asdict(it) for it in v] for k, v in alt_itineraries.items()}
            json.dump(data, f, ensure_ascii=False)
        return alt_itineraries
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_10_ivoice/ivoice-main/src/itinerary_calculator.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, 
## 🌟 Équipe : **equipe_10_ivoice**
### 👨‍🏫 Description du code
Ce code définit des classes de données pour représenter des itinéraires et des routes, et inclut une méthode pour créer un objet Itinerary à partir d'une réponse de l'API Navitia.
### 🚌 Spécificités fonctionnelles
Le code permet de convertir les données brutes de l'API Navitia en objets structurés, facilitant leur manipulation et affichage.
### ✍ Réutilisabilité
La méthode from_navitia_response est réutilisable pour transformer les réponses de l'API Navitia en objets Itinerary, facilitant l'intégration avec d'autres systèmes de gestion d'itinéraires.
### 📜 Snippet de code
```python
from dataclasses import dataclass

@dataclass
class Route:
    start: str
    end: str
    line: str

@dataclass
class Itinerary:
    itinerary_type: str
    routes: list[Route]

    @classmethod
    def from_navitia_response(cls, navitia_reponse: dict, itinerary_type: str, start_name: str, destination_name: str):
        routes = []
        for section in navitia_reponse["journeys"][0]["sections"]:
            if section["type"] == "waiting":
                continue

            if section["type"] == "street_network" and section["mode"] == "walking":
                line = "A pied"
            elif section["type"] == "public_transport":
                line = f"{section['display_informations']['commercial_mode']} {section['display_informations']['name']}"
            else:
                line = "Inconnue"

            routes.append(Route(
                start=section["from"]["stop_point"]["name"] if "stop_point" in section["from"] else start_name,
                end=section["to"]["stop_point"]["name"] if "stop_point" in section["to"] else destination_name,
                line=line
            ))
            break

        return Itinerary(itinerary_type, routes)
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_10_ivoice/ivoice-main/ivoice-main/src/itinerary_data.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Appel à un LLM, 
## 🌟 Équipe : **equipe_02_elevate_us**
### 👨‍🏫 Description du code
Ce code utilise un modèle de langage d'Azure OpenAI pour classifier les signalements d'équipements en différentes catégories prédéfinies.
### 🚌 Spécificités fonctionnelles
Permet de catégoriser automatiquement les signalements d'équipements pour une gestion plus efficace des problèmes.
### ✍ Réutilisabilité
La fonction de classification des signalements peut être réutilisée pour d'autres types de signalements ou dans d'autres contextes nécessitant une catégorisation automatique.
### 📜 Snippet de code
```python
import os
from openai import AzureOpenAI
from api_key import API_KEY

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
    API_VERSION = "2024-08-01-preview"
    AZURE_ENDPOINT = "https://dlb-team02-prd-oai01.openai.azure.com/"

    azure_open_ai_parameters = {
        "api_version": API_VERSION,
        "azure_endpoint": AZURE_ENDPOINT,
        "api_key": API_KEY,
    }

    llm = AzureOpenAI(**azure_open_ai_parameters)

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
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_02_elevate_us/accessibility-waze-main/signaling.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Appel à un LLM, Création d\'une interface utilisateur (IHM), Utilisation de LangChain, 
## 🌟 Équipe : **equipe_04_mobiwize**
### 👨‍🏫 Description du code
Ce code définit un graphe de flux de travail utilisant des nœuds et des arêtes pour orchestrer différentes tâches dans un système de gestion de la mobilité. Les nœuds représentent des appels de modèles, des outils, et des logiques spécifiques au transport et aux perturbations. Le graphe est compilé pour orchestrer les interactions entre ces composants.
### 🚌 Spécificités fonctionnelles
Le code répond aux besoins fonctionnels de gestion de la mobilité en orchestrant des tâches telles que la planification de trajets, le support client, la billetterie, l'accessibilité, et le suivi en temps réel. Il gère également les perturbations, offrant des routes alternatives et des estimations de résolution.
### ✍ Réutilisabilité
Le code est hautement réutilisable grâce à son abstraction et sa modularité. Les nœuds et les arêtes peuvent être facilement adaptés pour intégrer de nouvelles fonctionnalités ou services. Il permet une intégration fluide avec des APIs de mobilité et des outils externes, facilitant ainsi l'extension et la personnalisation du système.
### 📜 Snippet de code
```javascript
// Enhanced node types
import {Annotation, END, MessagesAnnotation, START, StateGraph} from "@langchain/langgraph";

type ModelNode = (input: any) => Promise<any>;
type ToolNode = (input: any) => Promise<any>;
type TransportNode = (input: any) => Promise<any>;
type DisruptionNode = (input: any) => Promise<any>;

// Define condition check functions
const shouldContinue = (state: any): string => {
  return "next"
};

// Node implementations
const callModel: ModelNode = async (input) => {
  // Base model call logic
  return {};
};

const toolNode: ToolNode = async (input) => {
  // Tool execution logic
  return {};
};

const transportNode: TransportNode = async (input) => {
  // Transport-specific logic (schedules, routes, etc.)
  return {
    schedules: [],
    availableRoutes: [],
    realTimeStatus: {}
  };
};

const disruptionNode: DisruptionNode = async (input) => {
  // Disruption handling logic
  return {
    activeDisruptions: [],
    alternativeRoutes: [],
    estimatedResolution: null
  };
};

// Create enhanced workflow graph
const workflow = new StateGraph(Annotation.Root({
  ...MessagesAnnotation.spec,
}))
  // Core nodes
  .addNode("cache", callModel)
  .addNode("router", callModel)
  .addNode("filter", callModel)
  .addNode("CONTEXT", callModel)
  .addNode("JOURNEY_PLANNER", toolNode)
  .addNode("CUSTOMER_SUPPORT", toolNode)
  .addNode("TICKETING", toolNode)
  .addNode("ACCESSIBILITY", toolNode)
  .addNode("REAL_TIME_TRACKING", toolNode)
  .addNode("agent", toolNode)
  .addNode("tools", toolNode)

  // Base edges
  .addEdge(START, "cache")
  .addEdge("CONTEXT", "router")
  .addConditionalEdges("cache", shouldContinue, ["CONTEXT", END])
  .addConditionalEdges("router", shouldContinue, ["JOURNEY_PLANNER", "CUSTOMER_SUPPORT", "TICKETING", "ACCESSIBILITY", "REAL_TIME_TRACKING"])
  .addEdge("JOURNEY_PLANNER", "agent")
  .addEdge("CUSTOMER_SUPPORT", "agent")
  .addEdge("TICKETING", "agent")
  .addEdge("ACCESSIBILITY", "agent")
  .addEdge("tools", "agent")
  .addEdge("REAL_TIME_TRACKING", "agent")
  .addConditionalEdges("agent", shouldContinue, ["tools", "filter"])
  .addEdge("filter", END)

export const graph = workflow.compile();
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_04_mobiwize%20%-%20%ai-framework-main/packages/ai-toolkit/src/graphs/orchestrator/index.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Appel à un LLM, Création d\'une interface utilisateur (IHM), Utilisation de LangChain, Conception de prompts, Génération de données, 
## 🌟 Équipe : **equipe_06_mob_ia**
### 👨‍🏫 Description du code
Ce code définit un agent conversationnel utilisant Azure OpenAI pour aider les usagers de l'Île-de-France à trouver des itinéraires de transport en commun. Il utilise des outils pour obtenir des itinéraires et des informations sur le trafic, et génère des réponses basées sur des prompts personnalisés.
### 🚌 Spécificités fonctionnelles
Le code répond aux besoins fonctionnels du projet en fournissant des itinéraires de transport en commun personnalisés pour les usagers de l'Île-de-France, en tenant compte de la géolocalisation et des préférences de l'utilisateur.
### ✍ Réutilisabilité
Le code est hautement réutilisable grâce à son abstraction et modularité. Il intègre des outils pour obtenir des itinéraires et des informations sur le trafic, ce qui peut être adapté à d'autres régions ou services de transport. L'utilisation de prompts personnalisés permet de modifier facilement le comportement de l'agent.
### 📜 Snippet de code
```python
from datetime import datetime
import os

from langchain.agents import AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import AzureChatOpenAI

from sources.agent.tools.get_itineraire import get_itineraire
from sources.agent.tools.get_info_trafic import get_info_trafic


from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser

API_VERSION = os.getenv('AZURE_OPENAI_API_VERSION')
AZURE_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
API_KEY = os.getenv('AZURE_OPENAI_API_KEY')

MEMORY_KEY = "chat_history"
CHAT_HISTORY = []

TOOLS = [get_itineraire, get_info_trafic]

azure_open_ai_parameters = {
    "api_version": API_VERSION,
    "azure_endpoint": AZURE_ENDPOINT,
    "api_key": API_KEY
}

llm = AzureChatOpenAI(
    **azure_open_ai_parameters,
    model=os.getenv('AZURE_OPENAI_MODELS'),
    temperature=0.2,
)

llm_with_tools = llm.bind_tools(TOOLS)

custom_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            f"""
            Vous êtes un assistant spécialisé pour aider les usagers de l'Île-de-France à trouver leur itinéraire dans les transports en commun.

            Consignes :
            Utilisez un langage simple et naturel, car le texte sera lu à voix haute.
            Nous sommes le {datetime.now().strftime("%Y-%m-%d")}.
            Il est {datetime.now().strftime("%H:%M:%S")}.
            Si l'utilisateur n'en fournit pas, considère que c'est la date et heure de départ.
            Si le point de départ n’est pas précisé :
            Utilisez la géolocalisation de l’usager si elle est disponible.
            Sinon, invitez-le à l’activer ou à préciser son départ. Ne faites pas d’hypothèses.
            Mais utilisez le point de départ s'il est précisé.

            Si la requête semble incomplete demandez plus de précisions.

            Répondez en 4 lignes maximum.
            Fournissez la réponse en indiquant l'origine et la destination, la date de départ et la date d'arrivée et les étapes principales, comme suit :
            Exemple :
            En partant 56 Rue de Bagnolet au 34 avenue de l'Opéra aujourd'hui à 14h, vous arriverez à 14h38. Marchez 6 minutes jusqu'à la station Alexandre Dumas, puis prenez la ligne 2 pendant 3 minutes direction Porte Dauphine jusqu'à Père Lachaise. Changez pour la ligne 3 direction Pont de Levallois pendant 11 minutes et descendez à Opéra.
            """,
        ),
        ("system", "User location: {user_location}"),
        MessagesPlaceholder(variable_name=MEMORY_KEY),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent = (
    {
        "input": lambda x: x["input"],
        "user_location": lambda x: x["user_location"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
        "chat_history": lambda x: x["chat_history"],
    }
    | custom_prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)


agent_executor = AgentExecutor(agent=agent, tools=TOOLS, verbose=True)


def invoke_agent(message: str, location: str) -> str:

    result = agent_executor.invoke({"input": message, "user_location": location, "chat_history": CHAT_HISTORY})

    CHAT_HISTORY.extend(
        [
            HumanMessage(content=message),
            AIMessage(content=result["output"]),
        ]
    )

    return result["output"]


if __name__ == "__main__":
    invoke_agent(
        message=("Je veux aller de la basilique Montmartre a la gare Montparnasse"),
        location=None
    )
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_06_mob_ia/hackathon_idfm_octo_2024-main%20%-%20%hackathon_idfm_octo_2024/sources/agent/agent.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Création d\'une interface utilisateur (IHM), Manipulation de données, 
## 🌟 Équipe : **equipe_07_tranquiliscore**
### 👨‍🏫 Description du code
Ce code initialise une carte interactive avec Leaflet, charge un fichier CSV, et place des marqueurs sur la carte en fonction des données de sécurité des gares. Les marqueurs sont personnalisés avec des icônes en fonction de l'indice de sécurité.
### 🚌 Spécificités fonctionnelles
Le code répond au besoin de visualiser des données de sécurité des gares sur une carte, ce qui est pertinent pour des applications de transport ou de sécurité publique.
### ✍ Réutilisabilité
Le code est réutilisable pour toute application nécessitant l'affichage de données géographiques à partir d'un fichier CSV. La fonction de parsing CSV et l'intégration avec Leaflet pour l'affichage de cartes sont des composants modulaires.
### 📜 Snippet de code
```javascript
// Fonction pour parser le CSV
function parseCSV(csv, delimiter = ';') {
    const lines = csv.split('\n'); // Diviser le CSV en lignes
    const headers = lines[0].split(delimiter); // Extraire l'en-tête

    // Créer des objets pour chaque ligne
    return lines.slice(1).map(line => {
        const values = line.split(delimiter);
        const obj = {};
        headers.forEach((header, index) => {
            obj[header.trim()] = values[index]?.trim();
        });
        return obj;
    });
}

// Initialiser la carte
const map = L.map('map').setView([48.8566, 2.3522], 13);

// Ajouter une couche de tuiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Fonction pour charger et parser le fichier CSV
function loadCSV() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0]; // Obtenir le fichier sélectionné

    if (!file) {
        alert('Veuillez sélectionner un fichier CSV.');
        return;
    }

    const reader = new FileReader();

    // Lire le fichier en tant que texte
    reader.onload = function(event) {
        const csvText = event.target.result;
        const data = parseCSV(csvText); // Parser le CSV en objets

        // Effacer les anciens marqueurs (si nécessaire)
        map.eachLayer(layer => {
            if (layer instanceof L.Marker) {
                map.removeLayer(layer);
            }
        });

        console.log(data);
        // Ajouter des marqueurs en fonction des données du CSV
        data.forEach(row => {
            const latitude = row['Lat_A'];
            const longitude = row['Long_A'];
            const securite = parseFloat(row['Indice_gare_A']);
            const nom = row['Gare_A'];
            console.log(latitude,longitude);
            console.log(securite);
            if (!isNaN(securite)) {
                const [lat, lng] = [latitude,longitude];

                // Déterminer l'icône et sa classe en fonction de l'indice de sécurité
                if (securite >= 0 && securite < 0.2) {
                    iconPath =  'ressources/visage_effrayé.png';
                    iconClass = 'red-smiley';
                } else if (securite >= 0.2 && securite < 0.4) {
                    iconPath = 'ressources/visage_inquiet.png';
                    iconClass = 'yellow-smiley';
                } else if (securite >= 0.4 && securite <= 0.6) {
                    iconPath = 'ressources/visage_neutre.png';
                    iconClass = 'yellow-smiley';
                }else if (securite >= 0.6 && securite <= 0.8) {
                    iconPath = 'ressources/visage_sourire.png';
                    iconClass = 'green-smiley';
                }else if (securite >= 0.8 && securite <= 1) {
                    iconPath = 'ressources/visage_rieur.png';
                    iconClass = 'green-smiley';
                }

                // Créer une icône personnalisée
                const customIcon = L.icon({
                    className: iconClass,
                    iconUrl: iconPath,
                    iconSize: [25, 25],
                    iconAnchor: [16, 16],
                    popupAnchor: [0, -16],
                });

                // Ajouter un marqueur à la carte
                L.marker([lat, lng], { icon: customIcon })
                    .addTo(map)
                    .bindPopup(`Gare : ${nom}<br>Indice de sécurité : ${securite}`);
                
            }
        });
    };

    reader.readAsText(file); // Lire le fichier CSV comme texte
}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_07_tranquiliscore/tranquili-score-main/Documents/t-app-js/script_agent.js)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Création d\'une interface utilisateur (IHM), Manipulation de données, 
## 🌟 Équipe : **equipe_07_tranquiliscore**
### 👨‍🏫 Description du code
Ce code charge un fichier CSV, parse les données, et affiche des trajets entre deux points sur une carte Leaflet. Les trajets sont colorés en fonction d'un indice de sécurité.
### 🚌 Spécificités fonctionnelles
Le code permet de visualiser des trajets entre gares avec des indices de sécurité, ce qui est utile pour des applications de transport ou de planification de trajets sécurisés.
### ✍ Réutilisabilité
Le code est réutilisable pour des applications nécessitant l'affichage de trajets ou de routes sur une carte à partir de données CSV. La fonction de parsing CSV et l'utilisation de Leaflet pour le rendu cartographique sont des éléments modulaires.
### 📜 Snippet de code
```javascript
// Fonction pour parser le CSV
function parseCSV(csv, delimiter = ';') {
    const lines = csv.split('\n'); // Diviser le CSV en lignes
    const headers = lines[0].split(delimiter);

    return lines.slice(1).map(line => {
        const values = line.split(delimiter);
        const obj = {};
        headers.forEach((header, index) => {
            obj[header.trim()] = values[index]?.trim();
        });
        return obj;
    });
}

// Initialiser la carte
const map = L.map('map').setView([48.8566, 2.3522], 13);

// Ajouter une couche de tuiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

function loadCSV() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0]; // Obtenir le fichier sélectionné

    if (!file) {
        alert('Veuillez sélectionner un fichier CSV.');
        return;
    }

    const reader = new FileReader();

    // Lire le fichier en tant que texte
    reader.onload = function (event) {
        const csvText = event.target.result;
        const data = parseCSV(csvText); // Parser le CSV en objets

        // Effacer les anciennes lignes ou marqueurs (si nécessaire)
        map.eachLayer(layer => {
            if (layer instanceof L.Polyline || layer instanceof L.Marker) {
                map.removeLayer(layer);
            }
        });

        // Créer une enveloppe pour ajuster les limites de la carte
        const bounds = L.latLngBounds();

        // Fonction pour déterminer la couleur en fonction de l'indice
        function getColor(indice) {
            if (indice <= 0.2) return 'red';
            if (indice <= 0.4) return 'orange';
            if (indice <= 0.6) return 'yellow';
            if (indice <= 0.8) return '#2ea822';
            return '#007c01';
        }

        // Parcourir chaque ligne du fichier et tracer un trajet
        data.forEach(row => {
            const latA = parseFloat(row['Lat_A']);
            const longA = parseFloat(row['Long_A']);
            const latB = parseFloat(row['Lat_B']);
            const longB = parseFloat(row['Long_B']);
            const indiceTroncon = parseFloat(row['Indice_troncon_AB']); // Indice du tronçon

            if (!isNaN(latA) && !isNaN(longA) && !isNaN(latB) && !isNaN(longB) && !isNaN(indiceTroncon)) {
                // Déterminer la couleur du chemin en fonction de l'indice
                const color = getColor(indiceTroncon);

                // Ajouter les points aux limites
                bounds.extend([latA, longA]);
                bounds.extend([latB, longB]);

                // Créer une polyligne entre les deux points
                const polyline = L.polyline(
                    [
                        [latA, longA],
                        [latB, longB],
                    ],
                    {
                        color: color,
                        weight: 10,
                        opacity: 1,
                        lineJoin: 'round',
                    }
                ).addTo(map);

                // Ajouter des marqueurs pour chaque gare avec leurs infos
                const iconA = L.divIcon({
                    className: 'icon-a',
                    html: `<b style="color: blue;">O</b>`,
                    iconSize: [20, 20],
                });
                const iconB = L.divIcon({
                    className: 'icon-b',
                    html: `<b style="color: red;"></b>`,
                    iconSize: [0, 0],
                });

                L.marker([latA, longA], { icon: iconA })
                    .addTo(map)
                    .bindPopup(`Gare A : ${row['Gare_A']}<br>Indice : ${row['Indice_gare_A']}`);

                L.marker([latB, longB], { icon: iconB })
                    .addTo(map)
                    .bindPopup(`Gare B : ${row['Gare_B']}<br>Indice : ${row['Indice_gare_B']}`);
            }
        });

        // Centrer la carte pour inclure toutes les lignes tracées
        map.fitBounds(bounds);
    };

    reader.readAsText(file);
}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_07_tranquiliscore/tranquili-score-main/Documents/t-app-js/script_utilisateur.js)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Création d\'une interface utilisateur (IHM), Traitement audio ou vocal, Utilisation de Websockets, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce hook React gère la capture et la transmission audio en temps réel via WebSocket. Il permet de démarrer et d'arrêter l'enregistrement audio, d'envoyer des données audio à un serveur WebSocket, et de traiter les réponses reçues, notamment les transcriptions audio.
### 🚌 Spécificités fonctionnelles
Permet l'interaction vocale en temps réel, ce qui est essentiel pour des applications de navigation ou d'assistance vocale.
### ✍ Réutilisabilité
Le hook est hautement réutilisable pour toute application nécessitant une communication audio en temps réel. Il encapsule la logique de gestion des WebSockets et de l'audio, ce qui le rend adaptable à divers scénarios d'interaction vocale.
### 📜 Snippet de code
```javascript
import { useState, useEffect, useCallback } from 'react';
import { Player } from '../lib/player';
import { Recorder } from '../lib/recorder';
import { getCurrentLocation } from '../utils/geolocation';
import { Journey } from '../api/directions';

const BUFFER_SIZE = 4096;

export const useRealtime = (onNewMessage?: (message: string, isBot: boolean, journeys?: Journey[]) => void) => {
    const [isAudioOn, setIsAudioOn] = useState(false);
    const [audioPlayer] = useState(() => new Player());
    const [audioRecorder, setAudioRecorder] = useState<Recorder | null>(null);
    const [webSocket, setWebSocket] = useState<WebSocket | null>(null);

    const [currentLocation, setCurrentLocation] = useState<{ latitude: number; longitude: number } | null>(null);

    const startAudio = useCallback(async () => {
        try {
            const ws = new WebSocket("ws://localhost:8000/ws");
            setWebSocket(ws);

            await audioPlayer.init(24000);

            let buffer = new Uint8Array();

            const appendToBuffer = (newData: Uint8Array) => {
                const newBuffer = new Uint8Array(buffer.length + newData.length);
                newBuffer.set(buffer);
                newBuffer.set(newData, buffer.length);
                buffer = newBuffer;
            };

            const handleAudioData = (data: ArrayBuffer) => {
                const uint8Array = new Uint8Array(data);
                appendToBuffer(uint8Array);

                if (buffer.length >= BUFFER_SIZE) {
                    const toSend = new Uint8Array(buffer.slice(0, BUFFER_SIZE));
                    buffer = new Uint8Array(buffer.slice(BUFFER_SIZE));

                    const regularArray = String.fromCharCode(...toSend);
                    const base64 = btoa(regularArray);

                    ws.send(JSON.stringify({ type: 'input_audio_buffer.append', audio: base64 }));
                }
            };

            const recorder = new Recorder(handleAudioData);
            setAudioRecorder(recorder);

            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            await recorder.start(stream);

            setIsAudioOn(true);
        } catch (error) {
            console.error('Error starting audio:', error);
            alert('Error accessing the microphone. Please check your settings and try again.');
        }
    }, [audioPlayer]);

    const stopAudio = useCallback(() => {
        if (audioRecorder) {
            audioRecorder.stop();
        }
        if (webSocket) {
            webSocket.close();
        }
        setIsAudioOn(false);
    }, [audioRecorder, webSocket]);

    useEffect(() => {
        if (webSocket) {
            webSocket.onmessage = (event) => {
                const data = JSON.parse(event.data);
                const handleTranscription = (transcript: string, isAIResponse: boolean) => {
                    console.log(`${isAIResponse ? 'AI' : 'User'} transcription:`, transcript);
                    if (typeof onNewMessage === 'function') {
                        onNewMessage?.(transcript, isAIResponse);
                    }
                };

                if (data?.type === 'conversation.item.input_audio_transcription.completed') {
                    handleTranscription(data.transcript, false);
                } else if (data?.type === 'response.audio_transcript.done') {
                    handleTranscription(data.transcript, true);
                }
                if (data?.type === 'response.function_call_arguments.done') {
                    console.log('AI function_call_arguments:', data.transcript);
                }
                if (data?.type === 'tools.tool_outputs') {
                    console.log('Received tool output:', data);
                    const args = JSON.parse(data.response.item.args);
                    const output = JSON.parse(data.response.item.output);
                    console.log('tools.tool_outputs:', output);
                    if (args.start && output.length > 0) {
                        onNewMessage?.("Voici les résultats : ", true, output);
                    }

                }
                if (data?.type !== 'response.audio.delta') return;

                const binary = atob(data.delta);
                const bytes = Uint8Array.from(binary, c => c.charCodeAt(0));
                const pcmData = new Int16Array(bytes.buffer);

                audioPlayer.play(pcmData);
            };
        }
    }, [webSocket, audioPlayer, onNewMessage]);

    return {
        isAudioOn,
        startAudio,
        stopAudio
    };
}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/app/src/hooks/realtime.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Génération de données, 
## 🌟 Équipe : **equipe_10_ivoice**
### 👨‍🏫 Description du code
Cette fonction génère une perturbation aléatoire à partir d'un historique de perturbations pour la ligne 9 du métro.
### 🚌 Spécificités fonctionnelles
Répond au besoin de simuler des perturbations pour tester la robustesse des systèmes de gestion de trafic.
### ✍ Réutilisabilité
La fonction peut être adaptée pour générer des perturbations pour d'autres lignes ou services, ce qui est utile pour simuler des scénarios de perturbation.
### 📜 Snippet de code
```python
def create_disruption(): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_10_ivoice/ivoice-main/src/disruption_generation.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Géocodage, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Cette classe et méthode permettent de récupérer des informations de trajet en utilisant l'API de transport de PRIM. Elle gère les paramètres de localisation, de date et d'accessibilité pour les utilisateurs en fauteuil roulant.
### 🚌 Spécificités fonctionnelles
Répond aux besoins de mobilité en temps réel et inclut des options pour les utilisateurs en fauteuil roulant.
### ✍ Réutilisabilité
Le code est modulaire et peut être réutilisé pour intégrer des fonctionnalités de recherche de trajets dans d'autres applications de mobilité. Il utilise des appels d'API standardisés et gère les exceptions.
### 📜 Snippet de code
```python
class DirectionsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.geocoding_api = GeocodingAPI()

    async def get_journey_info(self, origin_long, origin_lat, dest_long, dest_lat, datetime_str, wheelchair=False):
        base_url = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/journeys'
        params = {
            'from': f"{origin_long};{origin_lat}",
            'to': f"{dest_long};{dest_lat}",
            'datetime': datetime_str,
            'data_freshness': 'realtime'
        }
        if wheelchair:
            params['wheelchair'] = 'true'
            params['max_duration_to_pt'] = 300

        headers = {
            'Accept': 'application/json',
            'apikey': self.api_key
        }

        try:
            response = requests.get(base_url, headers=headers, params=params)
            response.raise_for_status()
            journey_data = response.json()
            return journey_data
        except requests.exceptions.RequestException as e:
            print(f"API request error: {e}")
            return None
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main%20%-%20%MobilIA/server/src/server/directions.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Prise en compte de la frugalité, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Ce code définit des interfaces pour les perturbations, les sections et les trajets, et implémente une fonction asynchrone pour obtenir des directions en utilisant une API locale. La fonction prend en compte les coordonnées d'origine et de destination, la date et l'heure, et une option pour les utilisateurs en fauteuil roulant.
### 🚌 Spécificités fonctionnelles
Répond aux besoins de calcul d'itinéraires en tenant compte des perturbations et des options d'accessibilité pour les personnes en fauteuil roulant.
### ✍ Réutilisabilité
La fonction `getDirections` est hautement réutilisable pour toute application nécessitant des calculs d'itinéraires, en particulier dans le contexte de la mobilité. Les interfaces définies permettent une structuration claire des données de trajet.
### 📜 Snippet de code
```javascript
import axios from 'axios';

export interface Disruption {
  effect: string;
  id: string;
  messages: string[];
  severity: string;
  status: string;
}

export interface Section {
  arrival_time: string;
  departure_time: string;
  from: string | null;
  mode: string | null;
  to: string | null;
  type: string;
  disruptions: Disruption[];
}

export interface Journey {
  arrival_date_time: string;
  co2_emission: number;
  departure_date_time: string;
  duration: number;
  nb_transfers: number;
  sections: Section[];
  status: string;
  type: string;
  walking_distance: number;
}

export async function getDirections(
  originLong: number,
  originLat: number,
  destLong: number,
  destLat: number,
  dateTime: string,
  wheelchair: boolean = false
): Promise<Journey[]> {
  try {
    const response = await axios.get('http://localhost:8000/api/directions', {
      params: {
        origin_long: originLong,
        origin_lat: originLat,
        dest_long: destLong,
        dest_lat: destLat,
        datetime: dateTime,
        wheelchair: wheelchair
      }
    });

    return response.data;
  } catch (error) {
    console.error('Error fetching directions:', error);
    throw error;
  }
}
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/app/src/api/directions.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Utilisation d\'autres API, 
## 🌟 Équipe : **equipe_06_mob_ia**
### 👨‍🏫 Description du code
Cette fonction utilise l'API PRIM pour obtenir l'identifiant d'un lieu à partir d'une adresse donnée.
### 🚌 Spécificités fonctionnelles
Permet de convertir une adresse en un identifiant de lieu utilisable pour d'autres appels API.
### ✍ Réutilisabilité
La fonction encapsule l'appel à l'API PRIM pour la recherche de lieux, ce qui la rend réutilisable pour toute application nécessitant une géolocalisation basée sur une adresse.
### 📜 Snippet de code
```python
def get_place(adresse: str) -> str: ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_06_mob_ia/hackathon_idfm_octo_2024-main/sources/api/api_prim.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Utilisation de LangChain, 
## 🌟 Équipe : **equipe_06_mob_ia**
### 👨‍🏫 Description du code
Cette fonction récupère les informations de trafic pour une ligne de transport donnée, en utilisant l'API PRIM.
### 🚌 Spécificités fonctionnelles
Répond au besoin de fournir des informations de trafic en temps réel pour les utilisateurs des transports en commun.
### ✍ Réutilisabilité
La fonction est réutilisable pour toute application nécessitant des informations de trafic en temps réel pour les lignes de transport en Île-de-France.
### 📜 Snippet de code
```python
from typing import Annotated

from sources.api.api_prim import call_info_trafic

from langchain_core.tools import tool


@tool
def get_info_trafic(
    ligne: Annotated[
        str, "Ligne de transport sur laquelle nous cherchons des informations sans le type (métro/rer/...)"
             "Exemple RER E -> E"]
) -> str:
    """
        Récupère les informations sur les potentiels problèmes des moyens de transport.
    """
    try:
        return call_info_trafic(ligne)
    except Exception as err:
        return f"Une erreur est survenue lors de la recherche d'info trafic: {err}"
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_06_mob_ia/hackathon_idfm_octo_2024-main/sources/agent/tools/get_info_trafic.py)

---

<div style="page-break-after: always;"></div>

# 💡 Utilisation de l\'API IDFM, Utilisation de Retrieval-Augmented Generation (RAG), Utilisation de Websockets, 
## 🌟 Équipe : **equipe_04_mobiwize**
### 👨‍🏫 Description du code
Ce code met en place un serveur Express et un serveur WebSocket pour gérer les communications en temps réel. Il définit plusieurs types de messages WebSocket et des gestionnaires pour traiter les messages utilisateur, les mises à jour d'outils et les messages système. Le serveur utilise la bibliothèque 'graphRag' pour traiter les flux de données en temps réel et diffuser les mises à jour aux clients connectés.
### 🚌 Spécificités fonctionnelles
Le code répond aux besoins de communication en temps réel et de traitement de données en continu, ce qui est essentiel pour les applications nécessitant des mises à jour instantanées et une gestion efficace des flux de données.
### ✍ Réutilisabilité
Le code est hautement réutilisable grâce à sa modularité et à son abstraction des types de messages. Il intègre un serveur WebSocket pour la communication en temps réel, ce qui est précieux pour les applications nécessitant des mises à jour instantanées. L'utilisation de 'graphRag' pour le traitement des flux de données en fait un composant clé pour les applications de traitement de données en temps réel.
### 📜 Snippet de code
```javascript
import express from 'express';
import WebSocket from "ws";
import {graphRag} from "@repo/ai-toolkit/graphs/rag";

// Message type definitions
interface BaseMessage {
  type: string;
  payload: any;
}

interface UserMessage extends BaseMessage {
  type: 'USER_MESSAGE';
  payload: {
    content: string;
  };
}

interface ToolUpdate extends BaseMessage {
  type: 'TOOL_UPDATE';
  payload: {
    toolName: string;
    data: any;
  };
}

interface SystemMessage extends BaseMessage {
  type: 'SYSTEM_MESSAGE';
  payload: {
    status: string;
    message: string;
  };
}

type WebSocketMessage = UserMessage | ToolUpdate | SystemMessage;

const app = express();

// Create WebSocket server
const wss = new WebSocket.Server({port: 9998});

// Broadcast to all connected clients
const broadcast = (message: any) => {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(message));
    }
  });
};

const processRagStream = async (content: string) => {
  try {
    for await (const chunk of await graphRag.stream({
      messages: [{role: "user", content}]
    }, {
      configurable: {
        thread_id: "1"
      },
      streamMode: "updates",
    })) {
      for (const [node, values] of Object.entries(chunk)) {
        console.log(`Receiving update from node: ${node}`);

        // Broadcast node updates
        broadcast({
          type: 'NODE_UPDATE',
          payload: {
            node,
            values
          }
        });
      }
    }
  } catch (error) {
    console.error('Error processing RAG stream:', error);
    broadcast({
      type: 'SYSTEM_MESSAGE',
      payload: {
        status: 'error',
        message: 'Error processing request'
      }
    });
  }
};

// Message handlers
const messageHandlers = {
  USER_MESSAGE: async (payload: UserMessage['payload'], ws: WebSocket) => {
    console.log('Processing user message:', payload.content);
    await processRagStream(payload.content);
  },

  TOOL_UPDATE: (payload: ToolUpdate['payload'], ws: WebSocket) => {
    console.log(`Tool update received from ${payload.toolName}:`, payload.data);
  },

  SYSTEM_MESSAGE: (payload: SystemMessage['payload'], ws: WebSocket) => {
    console.log('System message:', payload.message);
    broadcast({
      type: 'SYSTEM_MESSAGE',
      payload
    });
  }
};

// WebSocket connection handler
wss.on('connection', (ws: WebSocket) => {
  console.log('New client connected');

  // Message handler
  ws.on('message', async (message: string) => {
    try {
      const parsedMessage = JSON.parse(message) as WebSocketMessage;

      if (messageHandlers[parsedMessage.type]) {
        await messageHandlers[parsedMessage.type](parsedMessage.payload as any, ws);
      } else {
        ws.send(JSON.stringify({
          type: 'SYSTEM_MESSAGE',
          payload: {
            status: 'error',
            message: `Unsupported message type: ${parsedMessage.type}`
          }
        }));
      }
    } catch (error) {
      console.error('Error processing message:', error);
      ws.send(JSON.stringify({
        type: 'SYSTEM_MESSAGE',
        payload: {
          status: 'error',
          message: 'Error processing message'
        }
      }));
    }
  });

  // Error handler
  ws.on('error', (error) => {
    console.error('WebSocket error:', error);
  });

  // Disconnection handler
  ws.on('close', () => {
    console.log('Client disconnected');
  });
});

// Express routes
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start server
app.listen(9999, () => {
  console.info(`Express server listening on port 9999`);
  console.info(`WebSocket server listening on port 9998`);
});
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_04_mobiwize/index.ts)

---

<div style="page-break-after: always;"></div>

# 💡 Validation de données, 
## 🌟 Équipe : **equipe_01_accit_falc**
### 👨‍🏫 Description du code
Ce code définit un modèle de données nommé FalcScore utilisant Pydantic, qui est une bibliothèque de validation de données. Le modèle contient des listes de chaînes de caractères pour les catégories 'good', 'bad', et 'improve', ainsi qu'un score de type float.
### 🚌 Spécificités fonctionnelles
Le modèle répond à un besoin fonctionnel de structuration et de validation de données de score, ce qui est essentiel pour garantir l'intégrité des données dans l'application.
### ✍ Réutilisabilité
Le modèle FalcScore est réutilisable pour structurer et valider des données de score dans d'autres parties de l'application ou dans d'autres projets nécessitant une évaluation qualitative et quantitative.
### 📜 Snippet de code
```python
from pydantic import BaseModel


class FalcScore(BaseModel):
    good: list[str]
    bad: list[str]
    improve: list[str]
    score: float
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_01_accit_falc/accit-api-main/app/models/score_falceur.py)

---

<div style="page-break-after: always;"></div>

# 💡 Validation de données, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Cette fonction gère une requête HTTP pour obtenir des directions. Elle extrait les paramètres de la requête, valide leur présence, et utilise une API externe pour récupérer et parser les informations de trajet.
### 🚌 Spécificités fonctionnelles
Répond aux besoins de calcul de trajets en intégrant une API de directions, avec une gestion des erreurs et des validations robustes.
### ✍ Réutilisabilité
La fonction 'get_directions' est réutilisable pour toute application nécessitant des services de direction, grâce à son abstraction des détails de validation des paramètres et de l'appel à l'API de directions.
### 📜 Snippet de code
```python
async def get_directions(request: Request): ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main%20%-%20%MobilIA/server/src/server/app.py)

---

<div style="page-break-after: always;"></div>

# 💡 Validation de données, 
## 🌟 Équipe : **equipe_05_mobilia**
### 👨‍🏫 Description du code
Fonction asynchrone pour vérifier ou désambiguïser une adresse en utilisant une API de géocodage.
### 🚌 Spécificités fonctionnelles
Répond au besoin de validation et de désambiguïsation d'adresses dans le cadre de la gestion de trajets.
### ✍ Réutilisabilité
Cette fonction est précieuse pour toute application nécessitant une vérification ou une désambiguïsation d'adresses, en encapsulant l'appel à une API de géocodage.
### 📜 Snippet de code
```python
@tool
async def check_address(address: str):
    ...
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_05_mobilia/MobilIA-main/server/src/server/tools.py)

---

<div style="page-break-after: always;"></div>

# 💡 Données de validation, 
## 🌟 Équipe : **equipe_07_tranquiliscore**
### 👨‍🏫 Description du code
Ce code prépare les données de validation en nettoyant et en transformant les colonnes pour créer un champ 'Datetime' utilisable.
### 🚌 Spécificités fonctionnelles
Prépare les données de validation pour une analyse temporelle en créant un champ datetime standardisé.
### ✍ Réutilisabilité
La transformation des données temporelles en un format standardisé est une pratique courante et réutilisable dans le prétraitement des données.
### 📜 Snippet de code
```python
data_val_final = data_val.drop(['ventilation_ligne','validations_entree','validations_sortie','PA','type_jour','Key'],axis=1).rename(columns={'date':'Date','CodeGare':'Gare_A'})
data_val_final['Date'] = data_val_final['Date'].apply(lambda x: str(x)[:10])
data_val_final['Datetime'] = data_val_final['Date'] + ' ' + data_val_final['tranche_horaire'].replace({24:0,25:1,26:2}).astype(str) +':'+ data_val_final['demi_heure'].apply(lambda x: '00' if x=='0-30' else '30')+":00"

data_val_final['Datetime'] = pd.to_datetime(data_val_final['Datetime'])
```
### 🔎 En voir plus : 

[Voir le code sur GitHub](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024/tree/main/resultats/repositories/equipe_07_tranquiliscore/tranquili-score-main/pre-processing-creation)

---

<div style="page-break-after: always;"></div>
