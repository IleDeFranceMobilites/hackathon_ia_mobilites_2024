# hackathon_idfm_octo_2024
Hackathon IDFM 2024 - Equipe 6


## Pour préparer l'environnement

```shell
virtualenv .venv
source .venv/bin/activate
echo "../../../../" >> ./.venv/lib/$(ls ./.venv/lib/)/site-packages/local_path.pth
pip install -r requirements.txt
```

## Pour lancer l'application

```shell
streamlit run ./streamlit.py
```

## Présentation du projet

Ce projet a été développé dans le cadre du [Hackathon IA et Mobilités](https://www.iledefrance-mobilites.fr/actualites/hackathon-2024-ia-et-mobilites), organisé par Île-de-France Mobilités les 21 et 22 novembre 2024. Pour en savoir plus, voici le [Guide des participants et participantes](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024).


### Le problème et la proposition de valeur
La recherche d'itinéraires s'effectue majoritairement via des applications ou des outils numériques qui, bien que pratiques, peuvent sembler complexes ou peu accessibles pour les personnes non familières avec les nouvelles technologies. Cette difficulté peut créer un véritable obstacle dans leur quotidien, limitant leur autonomie et leur mobilité.

C’est à partir de ce constat qu’est né ce projet : un agent conversationnel intuitif et accessible dédié à la recherche d’itinéraires. Cet outil permet à tout utilisateur de dialoguer simplement en langage naturel pour connaître son itinéraire.

De la sont ressorties deux problématiques : 
- Comment faciliter l’usage des outils & données d’IDFM pour tous ?
- Comment rendre les applications d’IDFM plus accessibles ?


### La solution

Nous proposons une solution simple et accessible : un agent conversationnel fonctionnant en mode **speech-to-text-to-speech**. Ce système permet aux utilisateurs de dialoguer avec l’agent uniquement par la voix.

- **Étape 1 : Identification des besoins**
  L’utilisateur exprime oralement son point de départ et son point d’arrivée et l'heure, sinon l'heure actuelle sera prise en compte.

- **Étape 2 : Traitement et recherche**
  Grâce à une technologie de reconnaissance vocale avancée (*speech-to-text*), les données sont converties en texte. L’agent utilise ensuite l’API de recherche d’itinéraires de **Prim** pour identifier le trajet optimal.

- **Étape 3 : Retour d’information**
  Une fois le trajet calculé, l’agent restitue les informations en langage naturel via un système de synthèse vocale (*text-to-speech*), en détaillant étape par étape les directions à suivre.



### Les problèmes surmontés
> [!TIP]
> Ici vous pouvez présenter les principaux problèmes rencontrés et les solutions apportées
### Et la suite ?
Avec plus de temps et de ressources, une première évolution majeure consisterait à enrichir les fonctionnalités de recherche d’itinéraires en prenant en compte des paramètres supplémentaires :

- État des infrastructures : Intégration des données en temps réel sur l’état des ascenseurs 
- Données méteos : Intégration des données météorologiques pour indiquer de potentielles perturbations


