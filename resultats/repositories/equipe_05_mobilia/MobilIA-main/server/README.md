# Mobil-IA Serveur

Bienvenue dans le composant serveur de **Mobil-IA**, un assistant intelligent propulsé par l'IA, conçu pour faciliter les voyages et les transports de manière accessible. Ce guide détaillé vous fournira une compréhension approfondie du code du serveur, de ses fonctionnalités, de son installation et de son utilisation.

## Table des Matières

- [Mobil-IA Serveur](#mobil-ia-serveur)
  - [Table des Matières](#table-des-matières)
  - [Présentation](#présentation)
  - [Fonctionnalités](#fonctionnalités)
  - [Prérequis](#prérequis)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Architecture du Code](#architecture-du-code)
    - [Description des Composants Clés](#description-des-composants-clés)
  - [API](#api)
    - [Endpoints Principaux](#endpoints-principaux)
      - [Itinéraires](#itinéraires)
      - [WebSockets](#websockets)
    - [Exemple d'Utilisation](#exemple-dutilisation)
  - [Exécution du Serveur](#exécution-du-serveur)
  - [Licence](#licence)

## Présentation

Le serveur **Mobil-IA** est le cœur du backend de l'application. Il gère les requêtes des utilisateurs, interagit avec des services externes tels que l'API OpenAI, gère la persistance des données et assure la logique métier nécessaire au fonctionnement fluide de l'assistant de mobilité accessible.

## Fonctionnalités

- **Gestion des Utilisateurs** : Authentification, gestion des sessions et sécurisation des endpoints.
- **Intégration OpenAI** : Utilisation des modèles GPT pour fournir des réponses intelligentes et contextuelles.
- **Traitement d'Images** : Upload d'images, analyse et génération de descriptions via l'API OpenAI.
- **Text-to-Speech (TTS)** : Conversion de texte en audio pour une accessibilité renforcée.
- **Géocodage** : Conversion des coordonnées géographiques en adresses lisibles.
- **Gestion des Itinéraires** : Création, modification et suivi des plans de voyage avec prise en compte des besoins d'accessibilité.
- **WebSockets** : Communication en temps réel entre le client et le serveur.
- **CORS** : Configuration des politiques de partage des ressources entre origines multiples.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.10+**
- **uv** (Gestionnaire de paquets et exécution rapide)
- **Clé API OpenAI**
- **Clé API Directions** (pour les services de géolocalisation)
- **Git**
- **curl**

## Installation

Suivez ces étapes pour configurer le serveur **Mobil-IA** sur votre machine locale :

1. **Cloner le Référentiel**

    ```bash
    git clone https://github.com/pfarret81/MobilIA
    cd ./
    ```

2. **Créer et Activer un Environnement Virtuel**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Cela crée un environnement Python isolé pour le projet.

3. **Installer `uv`**

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    `uv` est utilisé pour gérer les dépendances et exécuter le serveur de manière efficace.

4. **Installer les Dépendances du Projet**

    ```bash
    python -m pip install -e .
    ```

    Cette commande installe le projet et ses dépendances en mode editable.

## Configuration

1. **Variables d'Environnement**

    Créez un fichier `.env` à la racine du projet `/server` et ajoutez les variables suivantes :

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    DIRECTIONS_API_KEY=your_directions_api_key_here
    SECRET_KEY=your_secret_key
    ```

    - Remplacez `your_openai_api_key_here` par votre clé API OpenAI.
    - Remplacez `your_directions_api_key_here` par votre clé API Directions.
    - Remplacez `your_secret_key` par une clé secrète sécurisée pour la gestion des sessions.

2. **Configuration des Fichiers**

    Assurez-vous que les configurations dans `server/src/server/app.py`, `server/src/server/prompt.py`, et `server/src/server/__init__.py` sont correctement définies selon vos besoins spécifiques.

## Architecture du Code

Le projet est structuré de manière modulaire pour faciliter la maintenance et les évolutions futures. Voici un aperçu de l'architecture du serveur **Mobil-IA** :

```
server/
├── src/
│   ├── server/
│   │   ├── app.py
│   │   ├── routes/
│   │   │   ├── directions.py
│   │   │   ├── geocode.py
│   │   │   └── websocket_endpoint.py
│   │   ├── models/
│   │   │   └── user.py
│   │   ├── services/
│   │   │   ├── openai_service.py
│   │   │   └── directions_api.py
│   │   ├── utils/
│   │   │   ├── auth.py
│   │   │   └── helpers.py
│   │   ├── prompt.py
│   │   ├── tools.py
│   │   └── __init__.py
│   └── langchain_openai_voice/
│       └── __init__.py
├── tests/
│   └── test_app.py
├── static/
│   └── ...
├── templates/
│   └── final-improved.html
├── pyproject.toml
└── README.md
```

### Description des Composants Clés

- **app.py** : Point d'entrée de l'application serveur, configure les middleware, les routes et démarre le serveur.
- **routes/** : Contient les différents endpoints API et WebSockets.
- **models/** : Définitions des modèles de données utilisés par l'application.
- **services/** : Logique métier et intégrations avec des services externes (OpenAI, Directions API).
- **utils/** : Fonctions utilitaires et helpers pour l'authentification, le traitement des requêtes, etc.
- **prompt.py** : Instructions et prompts utilisés par l'assistant IA.
- **tools.py** : Outils et fonctions auxiliaires pour l'IA.
- **__init__.py** : Initie certaines fonctionnalités de base du serveur, comme une simple fonction de test.

## API

### Endpoints Principaux


#### Itinéraires

- **GET** `/api/directions` : Récupère les itinéraires à partir des intentions de départ et destination. On utilise pour le geocoding, l'api GOUV ADRESSES qui nous renvoi les adresses les plus probables.

#### WebSockets

- **WS** `/ws` : Endpoint pour les communications en temps réel entre le client et le serveur.

### Exemple d'Utilisation

Voici un exemple d'appel à l'API pour obtenir des directions :

```bash
curl -X GET "http://localhost:8000/api/directions?origin_long=2.357795&origin_lat=48.881423&dest_long=2.285848&dest_lat=48.846779&datetime=20241121T150000&wheelchair=true" \
     -H "Accept: application/json" \
     -H "apikey: your_directions_api_key_here"
```

## Exécution du Serveur

Pour démarrer le serveur en mode développement avec rechargement automatique :

```bash
uv run src/server/app.py --reload
```

Le serveur sera accessible à l'adresse [http://localhost:8000](http://localhost:8000).


## Licence

Ce projet est licencié sous la [MIT License](LICENSE).

---

Pour toute question ou assistance, veuillez contacter l'équipe de développement.
```
