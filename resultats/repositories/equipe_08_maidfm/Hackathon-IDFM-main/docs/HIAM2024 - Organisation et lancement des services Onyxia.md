# Hackathon IA et Mobilités 2024

## Principes d'organisation des projets dans Onyxia

**Obligatoire : pendant le hackathon, l'ensemble des travaux seront à mener au sein du projet dlb-hackathon**

![image](https://github.com/user-attachments/assets/37d78872-c563-4382-a991-65b81e6e5297)

Chaque participant peut créer des services partagés ou non au sein du projet "dlb-hackathon", certains services seront mono-utilisateurs, d'autres seront multi-utilisateurs et destinés à être partagés au sein de l'équipe. 

**Chaque instance de service est à préfixer du numéro d'équipe**, ex "EQUIPE 0 - open-webui", lorsqu'il s'agit de services individuels, les nommer avec son prénom ex : "EQUIPE 0 - Clément".

Des ressources "back" mise en place par l'Organisation permettent de mutualiser des ressources techniques, notamment une base vectorielle et des instances d'Ollama :

![image](https://github.com/user-attachments/assets/7bb45429-f8f9-42ac-8b9f-92409f2f0406)

## Gestion des secrets

Des secrets sont prédéfinis par équipe et permettent l'utilisation des ressources mutualisées, ceux-ci sont visibles dans l'espace "My secrets" d'Onyxia :

![image](https://github.com/user-attachments/assets/dc7752e7-308e-4db6-96cc-e1c5858d0498)

Cette interface permet de naviguer dans les listes de secrets, qui constitueront des variables d'environnement pour les services instanciés, par exemple pour l'équipe 00 :

![image](https://github.com/user-attachments/assets/0d7f4be0-23d6-4360-b445-61e1be0a7ac1)

**⚠ Le chemin vers les secrets de l'équipe sont à indiquer dans les paramètre du service avant son instanciation : ⚠**

1. **Récupération du chemin vers les variables d'environnement de l'équipe :**
- Cliquer sur le fichier de l'équipe dlb-team00-xxxxxx
- Cliquer sur utiliser dans le service (cela va copier le chemin d'accès Vault à ce fichier de secrets) :
  
![image](https://github.com/user-attachments/assets/d86824ca-4002-4d70-a6e7-28f247b355d8)

2. **Paramétrage du chemin avant instanciation d'un service**
- Aller dans le catalogue de services et sélectionner un service (Juypter, VSCODE, ou OpenWebUI), et parametrer Vault pour prendre en compte ce chemin :
  
![image](https://github.com/user-attachments/assets/1a4bdafc-4b91-4016-8cc2-9ad8983bc5a4)

- Un fois au sein du service les variables d'environnement suivantes devraient être accessibles :
AZURE_OPENAI_API_KEY
AZURE_OPENAI_API_VERSION
AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_MODELS
AZURE_OPENAI_MODEL_NAMES
ELASTICSEARCH_PASSWORD
