
## La solution

### Fonctionnement général

Mobil-IA est un assistant intelligent propulsé par l'IA, intégrant des datasources de Île-de-France Mobilités (IDFM) pour fournir des informations en temps réel et personnalisées sur les trajets. L'application combine un frontend développé en React avec un backend en Node.js, utilisant des WebSockets pour une communication fluide et instantanée entre le client et le serveur.

### Données mobilisées

- **Datasources IDFM** : Informations en temps réel sur les horaires, les perturbations et les disponibilités des transports en commun.
- **API OpenAI** : Génération de réponses intelligentes et contextuelles pour l'assistant.
- **Services de géolocalisation** : Fournissent des données précises sur la position des utilisateurs et des transports.

### Réponse au problème

Mobil-IA répond aux besoins d'accessibilité et d'efficacité des utilisateurs en leur offrant une interface intuitive pour planifier et suivre leurs trajets en temps réel, quel que soit leurs handicap. L'intégration avec les datasources IDFM permet d'obtenir des informations actualisées, tandis que l'assistant IA facilite la navigation et la prise de décision.

## Les problèmes surmontés

L'un des principaux défis rencontrés a été de créer un agent capable de s'intégrer efficacement avec les datasources de IDFM. Assurer la fiabilité et la rapidité des échanges de données en temps réel a nécessité la mise en place de WebSockets robustes et une gestion optimale des appels API. De plus, garantir la sécurité et la confidentialité des données utilisateur a été une priorité, impliquant la mise en place de mécanismes d'authentification et de gestion des sessions sécurisées.

## Et la suite ?

Avec davantage de temps, nous envisageons d'enrichir Mobil-IA en intégrant des fonctionnalités avancées telles que :
- **Prédiction des temps de trajet** : Utilisation de l'apprentissage automatique pour anticiper les délais et proposer des alternatives en fonction des contraintes (Chaise roulante, Accessibilité Aveugle etc).
- **Personnalisation avancée** : Adaptation des recommandations en fonction des préférences et des habitudes de chaque utilisateur.
- **Intégration avec d'autres services** : Possible collaboration avec des applications de réservation de taxis, de vélos en libre-service, etc.
- **Amélioration de l'accessibilité** : Développement de fonctionnalités supplémentaires pour les utilisateurs à besoins spécifiques
