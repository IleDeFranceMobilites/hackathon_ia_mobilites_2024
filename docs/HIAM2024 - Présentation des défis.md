![Logo du Hackathon IA et Mobilités](/images/Logo%20illustre_Hackathon%20IA%20Mobilites.jpg)

# Présentation des défis du Hackathon IA et Mobilités

Cette page décrit les 4 défis du Hackathon IA et Mobilités. Lien vers [le guide du participant](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024).

## Défi 1 - Améliorer l'accessibilité des services de mobilité

### Contexte

L’accessibilité des services de mobilité doit assurer la capacité à toute personne en incapacité permanente ou temporaire de se déplacer et d’accéder librement à tous services (numériques ou non) et activités. Elle inclut à la fois l’accessibilité au transport (assistance en gare, accessibilité des moyens de transport, …) et celle des services numériques au voyageur.

Les services au voyageur se font au travers d’un nombre important d’informations sous forme de données textuelles, que ce soit pour l’expérience voyageur lors d’un trajet, ou l’accès à de l’information plus froide (accès à un nouveau service, renouvellement des pass Navigo, …). Ces services prennent plusieurs formes : applications, message d’information voyageur, pages du site internet, etc.

L’objectif de ce défi est d’améliorer l’accessibilité des transports et des services numériques au voyageur dans leur diversité

### Projets possibles

- 🗣️ Développer un outil d'IA capable de “traduire” des informations de manière plus diverse et accessible : Facile à Lire et à Comprendre, multilinguisme, pour alimenter les différents services numériques au voyageur
- 🤖 Développer un assistant d’IA pour réduire le décalage entre le vocabulaire des usagers et le vocabulaire “expert”
- ♿ Améliorer la recherche et la restitution des itinéraires accessibles sur le réseau d’Île-de-France Mobilités

### Une réalisation possible

Chatbot IA qui permet de restituer des messages d’information trafic en Facile à Lire et à Comprendre

### Exemple de ressources à disposition
- Historique des messages d'information trafic
- Référentiels des lignes et des arrêts
- Calculateurs d’itinéraires (API) d’Île-de-France Mobilités
- Articles et guides en Facile à Lire et à Comprendre
- Accessibilité en gare
- Historique de fonctionnement des ascenseurs
- Accessibilité des établissements recevant du public (ERP)
- et d'autres !

_Les données publiées [sont accessibles ici](https://airtable.com/appGp6Hwf0NrmXQ9L/shrnmQYmL0lDKgS76). Vous pouvez utiliser un filtre pour voir les données spécifiques au Défi 1. D'autres données sont à venir !_

### L'équipe type idéale

Pour répondre à ce défi, une diversité de profils seront utiles. Les compétences peuvent varier, mais restez vigilant à leur diversité. 

| Rôle                             | Exemple                                                                 | Nombre idéal |
|----------------------------------|-----------------------------------------------------------------------------|--------------|
| Développeurs et développeuses IA |   Développer le produit IA                                        | 2            |
| Ingénieur et ingénieure TAL      | Affiner le RAG          | 1            |
| Ingénieur et ingénieure Data     | Mettre en place la base vectorielle                                              | 1            |
| Designeuse UX et d'information   | Prise en compte des critères d'accessibilité dans la solution proposée | 1            |
| Développeur et développeuse mobile               |  Calculateur d'itinéraires accessibles                                                        | 1            |

## Défi 2 - Construire une boîte à outils pour accélérer le développement de l’IA au service des usagers


### Contexte
Le développement de services utilisant des techniques d’IA nécessite l’utilisation de données de qualité et contextualisées, en particulier avec l’utilisation des LLM dont la connaissance du contexte utilisateur est importante. Île-de-France Mobilités possède de nombreuses données structurées et non-structurées qui seront utiles au développement d’outils IA au service des usagers. 

L’objectif de ce défi est de développer une boîte à outils pour accélérer le développement de l’IA au service des usagers.


### Projets possibles
- ⚙️ Améliorer l'accès, la compréhension et la production des données Open Data d'IDFM. Par exemple, explorer l’utilisation d’un modèle de langage dans la production de jeux de données aux formats standards tels que le GTFS ou le NETEX
- 🤖 Permettre à un assistant IA de requêter les API d’Île-de-France Mobilités à partir de demandes en langage naturel (calculateurs d’itinéraires, prochains passages, messages d’info trafic, etc…)
- 💡 Et toute autre idée pour construire des ressources utiles au développement de l’IA au service des mobilités ! 


### Une réalisation possible
Une application qui permet à partir d’une phrase en langage naturelle d’appeler des API des Île-de-France Mobilités

### Exemple de ressources à disposition
_Les données publiées [sont accessibles ici](https://airtable.com/appGp6Hwf0NrmXQ9L/shrnmQYmL0lDKgS76). Vous pouvez utiliser un filtre pour voir les données spécifiques au Défi 2. D'autres données sont à venir !_

- Catalogue Open Data d’Île-de-France Mobilités
- Spécifications NETEX et GTFS
- Documentation PRIM
- Documents de la FAQ du site Île-de-France Mobilités
- Calculateurs d’itinéraires (API) d’Île-de-France Mobilités
- Bornes et vélos Vélib’ en temps réel
- …


### L'équipe type idéale

Pour répondre à ce défi, une diversité de profils seront utiles. Les compétences peuvent varier, mais restez vigilant à leur diversité. 

| Rôle                             | Exemple                                                                 | Nombre idéal |
|----------------------------------|-----------------------------------------------------------------------------|--------------|
| Développeurs et développeuses IA |   Développer les outils IA                                        | 3            
| Ingénieur et ingénieure Data     | Mettre en place le pipeline de données et APIs                                             | 2            |
| Designer et designeuse UX et d'information   | Prise en compte des critères d'accessibilité dans la solution proposée | 1            |
| Développeur et développeuse mobile               |  Intégrer l'IA dans les applications                                                        | 1            |

## Défi 3 - Améliorer les prévisions au service des mobilités


### Contexte
Les opérateurs de transports, comme les autorités organisatrices, cherchent à anticiper le plus finement le fonctionnement des réseaux de transports. Par exemple, cela permet aux autorités de mettre en place des alternatives (multimodalité) en cas de très forte affluence, et aux usagers d’en être informé. Les techniques d’IA comme le machine learning permettent d’anticiper des événements et comportements à partir d’un apprentissage sur des données historiques. Elles peuvent être mises au service de la prévision. 

L’objectif de ce défi est d’améliorer les prévisions sur le fonctionnement des réseaux de transports.

### Projets possibles
- ⚙️ Prévoir finement l’affluence dans les transports pour permettre aux voyageurs de choisir l’itinéraire qui leur conviendra le mieux. 
- 🤖 Etre en mesure d’anticiper l’impact des événements externes sur la fréquentation et l’affluence des transports en commun. 
- 💡 Et toute autre idée pour construire des ressources utiles au développement de l’IA au service des mobilités ! 


### Une réalisation possible
Modèle de prédiction de l’affluence d’une ligne en fonction des données météo. 


### Exemple de ressources à disposition
_Les données publiées [sont accessibles ici](https://airtable.com/appGp6Hwf0NrmXQ9L/shrnmQYmL0lDKgS76). Vous pouvez utiliser un filtre pour voir les données spécifiques au Défi 3. D'autres données sont à venir !_

- Historique des données de validation sur le réseau de surface et le réseau ferré
- Nombre de validations par jour
- Données météo et données de vigilance
- Lieux de festivals en Île-de-France
- Événements publics en Île-de-France
- …

### L'équipe type idéale
| Rôle                             | Exemple                                                                 | Nombre idéal |
|----------------------------------|-----------------------------------------------------------------------------|--------------|
| Développeurs et développeuses IA |   Développer les outils IA                                        | 1            
| Data scientist     | Apprentissage machine sur des séries temporelles                                             | 2            |
| Data analyst  | Datavisualisation des fréquentations, événéments| 2            |
| Développeur mobile               |  Intégrer les modèles dans l'information voyageur                                                        | 1            |


## Défi 4 - Personnaliser l’expérience utilisateur des services numériques au voyageur

### Contexte
Les usagers des services de mobilités consomment des informations et données sur leur voyage. Ils en produisent également lorsqu’ils utilisent les systèmes d’aide à la mobilité tels que l’application Île-de-France Mobilités . Les données produites peuvent être utilisées pour personnaliser l’expérience usager, par exemple en contextualisant mieux l’information trafic dont il est destinataire à ses parcours favoris.

L’objectif de ce défi est de développer des outils à base d’IA au service de la personnalisation de l’expérience usager, notamment sur les services numériques au voyageur.

### Projets possibles
- 🔔 Donner la possibilité aux voyageurs de créer des alertes personnalisées
- 🧭 Suggérer de manière automatisée des itinéraires grâce à la prise en compte du contexte des utilisateurs de l’application île-de-France Mobilités
- 🤖 Enrichir et améliorer un chatbot basé sur la FAQ d’île-de-France Mobilités


### Une réalisation possible
Templates de suggestions d’itinéraires en fonction des données de l’utilisateurs sur l’application Île-de-France Mobilités

### Exemple de ressources à disposition
_Les données publiées [sont accessibles ici](https://airtable.com/appGp6Hwf0NrmXQ9L/shrnmQYmL0lDKgS76). Vous pouvez utiliser un filtre pour voir les données spécifiques au Défi 4. D'autres données sont à venir !_

- API Prochains passages
- API Messages Info Trafic
- Documents FAQ site Île-de-France Mobilités
- Historique des messages d’information
- Données Open Data
- …


### L'équipe type idéale

| Rôle                             | Exemple                                                                 | Nombre idéal |
|----------------------------------|-----------------------------------------------------------------------------|--------------|
| Développeurs et développeuses IA |   Développer  le produit IA                                        | 3            |         |
| Ingénieur et ingénieure Data     | Prendre en main les données utilisateurs                                              | 1            |
| Designeur et designeuse UX    | Intégration de l'IA dans des applications de mobilités | 1            |
| Développeur et dévelppeuse mobile               |  Utiliser les données contexte des utilisateurs                                                        | 1            |
