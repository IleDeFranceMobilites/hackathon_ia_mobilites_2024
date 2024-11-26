# Start of Selection
# Frontend Mobil-IA

Bienvenue dans le dépôt **Frontend** de **Mobil-IA**, un assistant intelligent conçu pour faciliter les déplacements et les transports de manière accessible. Cette application React interagit avec le backend **Mobil-IA Serveur** pour offrir une expérience utilisateur fluide et interactive.

## Table des Matières

- [Start of Selection](#start-of-selection)
- [Frontend Mobil-IA](#frontend-mobil-ia)
  - [Table des Matières](#table-des-matières)
  - [Description](#description)
  - [Fonctionnalités](#fonctionnalités)
  - [Prérequis](#prérequis)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Utilisation](#utilisation)
  - [Structure du Projet](#structure-du-projet)
    - [Hooks](#hooks)
      - [`useRealtime.ts`](#userealtimets)
      - [`geolocation.ts`](#geolocationts)
    - [Composants](#composants)
      - [`ChatInterface.tsx`](#chatinterfacetsx)
  - [API Utilisées](#api-utilisées)
  - [Licence](#licence)
  - [Contact](#contact)
- [End of Selection](#end-of-selection)

## Description

Le frontend de **Mobil-IA** est développé en React et permet aux utilisateurs d'interagir avec l'assistant de mobilité accessible. Il gère la capture de la voix, sa transmission au backend via WebSockets, et affiche les réponses générées par l'IA. L'application se concentre sur l'accessibilité et utilise des API gouvernementales pour garantir la confidentialité et la conformité des données.

## Fonctionnalités

- **Interface de Chat** : Permet aux utilisateurs de communiquer avec l'assistant via texte et voix.
- **Capture de la Voix** : Utilisation de l'API Web Audio pour capturer la voix de l'utilisateur.
- **Transmission en Temps Réel** : Envoi des données audio au backend en temps réel via WebSockets.
- **Géolocalisation** : Détection de la position actuelle de l'utilisateur en utilisant des API gouvernementales.
- **Accessibilité** : Design pensé pour être accessible à tous les utilisateurs.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Node.js** (version 14 ou supérieure)
- **npm** ou **yarn**
- **Clé API Mobil-IA Serveur**
- **Connexion Internet** pour accéder aux API gouvernementales

## Installation

Suivez ces étapes pour configurer le frontend **Mobil-IA** sur votre machine locale :

1. **Cloner le Référentiel**

    ```bash
    git clone https://github.com/votre-utilisateur/mobil-ia-frontend.git
    cd mobil-ia-frontend
    ```

2. **Installer les Dépendances**

    Avec npm :

    ```bash
    npm install
    ```

    Avec yarn :

    ```bash
    yarn install
    ```

3. **Configurer les Variables d'Environnement**

    Créez un fichier `.env` à la racine du projet et ajoutez les variables nécessaires :

    ```env
    REACT_APP_API_URL=http://localhost:8000
    REACT_APP_GOUV_API_KEY=votre_cle_api_gouv
    ```

## Configuration

Assurez-vous que les API gouvernementales utilisées pour la géolocalisation et d'autres services sont correctement configurées et que vous disposez des clés d'accès nécessaires.

## Utilisation

Pour démarrer l'application en mode développement, exécutez :

Avec npm :

```bash
npm start
```

Avec yarn :

```bash
yarn start
```

L'application sera accessible à l'adresse [http://localhost:3000](http://localhost:3000).

## Structure du Projet

### Hooks

#### `useRealtime.ts`

Ce hook gère la capture audio en temps réel, l'enregistrement et la transmission des données audio au backend via WebSockets. Il initialise le `Player` pour jouer les réponses audio et le `Recorder` pour enregistrer la voix de l'utilisateur. Les données audio sont envoyées au serveur sous forme de buffers encodés en base64.

#### `geolocation.ts`

Ce utilitaire récupère la position actuelle de l'utilisateur en utilisant les API de géolocalisation gouvernementales. Il effectue également le géocodage inverse pour obtenir une adresse lisible à partir des coordonnées GPS.

### Composants

#### `ChatInterface.tsx`

Ce composant principal gère l'affichage de l'interface de chat, y compris l'affichage des messages, la gestion des nouvelles entrées et l'intégration avec les hooks de temps réel et de géolocalisation. Il permet aux utilisateurs d'envoyer des messages vocaux ou textuels et de recevoir des réponses de l'assistant intelligent.

## API Utilisées

Le frontend utilise les API gouvernementales pour la géolocalisation et d'autres services essentiels, garantissant ainsi une meilleure confidentialité et conformité réglementaire. Contrairement à l'utilisation des services Google, ces API sont maintenues par le gouvernement et offrent une intégration simplifiée avec les systèmes publics.

## Licence

Ce projet est licencié sous la [MIT License](LICENSE).

## Contact

Pour toute question ou assistance, veuillez contacter l'équipe de développement.
# End of Selection
