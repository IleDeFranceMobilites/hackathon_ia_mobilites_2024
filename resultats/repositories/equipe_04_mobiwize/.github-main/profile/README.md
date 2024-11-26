![IDFM_MobiWise](https://github.com/user-attachments/assets/24fbe02a-6baf-4597-9f23-6d057cc4786d)

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
