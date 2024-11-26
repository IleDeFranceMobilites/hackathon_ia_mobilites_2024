# MobiWise AI Toolkit pour l'amélioration de l'expérience voyageur IDFM

Ce projet est une boîte à outils basée sur LangGraph permettant de créer des flux d'intelligence artificielle complexes et réutilisables pour améliorer l'expérience des voyageurs d'Île-de-France Mobilités.

## Présentation du projet

Ce projet a été développé dans le cadre du [Hackathon IA et Mobilités](https://www.iledefrance-mobilites.fr/actualites/hackathon-2024-ia-et-mobilites), organisé par Île-de-France Mobilités les 21 et 22 novembre 2024. Pour en savoir plus, voici le [Guide des participants et participantes](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024).

### Le problème et la proposition de valeur

L'expérience voyageur dans les transports en commun d'Île-de-France fait face à plusieurs défis :
- Complexité des parcours multimodaux
- Difficulté à obtenir des informations personnalisées en temps réel
- Besoin d'automatiser des processus d'assistance aux voyageurs

Notre toolkit permet aux développeurs de :
- Créer rapidement des agents IA spécialisés pour différents aspects de l'expérience voyageur
- Composer des workflows complexes grâce à LangGraph
- Réutiliser des composants standardisés pour accélérer le développement

### La solution

Notre solution s'articule autour d'une architecture monorepo comprenant :

```typescript
apps/
  ├── docs/     // Documentation du projet
  └── server/   // Serveur API principal avec Express et WebSocket

packages/
  └── ai-toolkit/    // Cœur de la boîte à outils
      ├── graphs/    // Composants LangGraph réutilisables
      ├── rag/       // Système de RAG pour l'enrichissement contextuel
      ├── registry/  // Registre des agents et workflows
      └── tools/     // Utilitaires communs
```

Le toolkit s'appuie sur :
- LangGraph pour orchestrer des workflows IA complexes
- Un système de RAG (Retrieval Augmented Generation) pour enrichir les réponses
- Un registre centralisé des agents et des outils
- Un serveur Express/WebSocket pour la communication en temps réel

#### Architecture du Serveur

Le serveur se compose de deux parties principales :
1. **Serveur Express** (Port 9999)
  - Endpoints REST pour les requêtes traditionnelles
  - Support des requêtes synchrones

2. **Serveur WebSocket** (Port 9998)
  - Communication bidirectionnelle en temps réel
  - Support du streaming des réponses IA
  - Types de messages supportés :
    - `USER_MESSAGE` : Messages des utilisateurs
    - `TOOL_UPDATE` : Mises à jour des outils
    - `SYSTEM_MESSAGE` : Messages système
    - `NODE_UPDATE` : Mises à jour des nœuds LangGraph

## Installation et utilisation

### Prérequis
- Node.js 18+
- pnpm 8+
- Azure OpenAI API credentials
- Elastic Search credentials

### Installation

```bash
# Cloner le repository
git clone https://github.com/IDFM-MobiWise/ai-framework

cd idfm-hackathon

# Installation de pnpm si non installé
npm install -g pnpm

# Installation des dépendances
pnpm install

# Configuration de l'environnement
cp packages/ai-toolkit/.env.example packages/ai-toolkit/.env
```

### Configuration
Éditer le fichier `.env` avec vos paramètres :

```env
# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_API_VERSION=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_MODELS=gpt-4o-mini
AZURE_OPENAI_MODEL_NAMES=gpt-4o-mini

# Elastic Search Configuration
ELASTIC_API_KEY=votre-mot-de-passe
ELASTIC_URL=https://votre-elastic-url.net/

# Node Configuration
# NODE_TLS_REJECT_UNAUTHORIZED=0 (si vous avez des problèmes avec les certificats)
```

### Développement

Ce projet utilise Turborepo pour la gestion du monorepo. Voici les principales commandes disponibles :

```bash
# Lancement du serveur de développement
pnpm dev

# Build du projet
pnpm build
```

### Utilisation du serveur

Le serveur expose deux interfaces :

1. **API REST** (Port 9999)
```typescript
// Exemple de requête POST
const response = await fetch('http://localhost:9999/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    messages: [{
      role: "user",
      content: "Comment marche le covoiturage?"
    }]
  })
});
```

2. **WebSocket** (Port 9998)
```typescript
// Exemple de connexion WebSocket
const ws = new WebSocket('ws://localhost:9998');

// Envoi d'un message utilisateur
ws.send(JSON.stringify({
  type: 'USER_MESSAGE',
  payload: {
    content: "Comment marche le covoiturage?"
  }
}));

// Réception des mises à jour
ws.onmessage = (event) => {
  const update = JSON.parse(event.data);
  console.log('Received:', update);
};
```

## La licence

Le code et la documentation de ce projet sont sous licence [MIT](LICENSE).

---

Développé avec ❤️ pour le Hackathon IA et Mobilités IDFM 2024.
