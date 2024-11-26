# Hackathon IA et Mobilités 2024

## Configuration générale des services pendant le hackathon (rappels)

Pour rappel, pendant le hackathon, l'ensemble des travaux seront à mener au sein du projet dlb-hackathon :

![image](https://github.com/user-attachments/assets/37d78872-c563-4382-a991-65b81e6e5297)

### Architecture des services Onyxia ciblée :

Chaque participant peut créer des services partagés ou non au sein du projet "dlb-hackathon", certains services seront mono-utilisateurs, d'autres seront multi-utilisateurs et destinés à être partagés au sein de l'équipe. 

**Chaque instance de service est à préfixer** du numéro d'équipe, ex "EQUIPE 0 - open-webui", lorsqu'il s'agit de services individuels, les nommer avec son prénom ex : "EQUIPE 0 - Ali".

Des ressources "back" mise en place par l'Organisation permettent de mutualiser des ressources techniques, notamment une base vectorielle et des instances d'Ollama :

![image](https://github.com/user-attachments/assets/7bb45429-f8f9-42ac-8b9f-92409f2f0406)

## Déploiement conseillé d'OpenWebUI

### Initialisation du service 

1. Création d'un service par équipe dans "dlb-hackathon"

2. Partage du service, cliquer sur l'icone :
![image](https://github.com/user-attachments/assets/d47808ae-6dd4-47b1-8fea-13d318ae2456)

3. Après premier lancement du service il faudra s'authentifier en cliquant sur "Inscrivez vous" :
![image](https://github.com/user-attachments/assets/8daa60d2-d8eb-41fa-bb7f-4bc79971fe91)

4. Créer un compte, l’adresse mail doit être celle d’onyxia mais le mdp peut être faux

**Le premier utilisateur connecté devient administrateur de la plateforme et peut la configurer (via le bouton "Tableau de bord administrateur", il peut accepter les nouveaux utilisateurs et les rendre aussi administrateurs**

![image](https://github.com/user-attachments/assets/08b958be-3791-4ade-bbaf-7956c1b43419)

![image](https://github.com/user-attachments/assets/5218b67f-bf0f-4175-8090-df83e1660159)

### Paramétrage des modèles 

Le service OpenWebui sera préconfiguré pour pointer vers un service ollama, il suffit d'indiquer le nom du modèle et sa taille pour que celui-ci puisse être téléchargé et déployé.

**<!> Le système n'est pas dimensionné pour des modèles supérieurs à 9b <!>**

![image](https://github.com/user-attachments/assets/a3ed3c63-c2a0-44ab-9482-79b20f610cfb)


### Paramétrage de la connexion vers Open AI 

Les paramètres de connexion aux ressources OpenAi seront communiquées sur place pendant le hackathon. 
