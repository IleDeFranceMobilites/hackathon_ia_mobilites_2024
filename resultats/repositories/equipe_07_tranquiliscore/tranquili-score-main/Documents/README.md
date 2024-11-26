# Projet " Tranquil'iti " - Équipe 7

Ce projet propose un estimateur du sentiment d'insécurité dans les transports. L'objectif est d'attirer un nouveau public dans les transports en communs en proposant des itinéraires tranquilles. Pour chaque gare et chaque tronçon de ligne, nous estimons un indice reflétant le sentiment d'insécurité. A partir de ces indices, nous évaluons la tranquillité de chaque trajet demandé par l'utilisateur. En parallèle, une interface opérateur permet de visualiser sur une carte les zones où nous estimons un sentiment de sécurité fort. 

## Présentation du projet

Ce projet a été développé dans le cadre du [Hackathon IA et Mobilités](https://www.iledefrance-mobilites.fr/actualites/hackathon-2024-ia-et-mobilites), organisé par Île-de-France Mobilités les 21 et 22 novembre 2024. Pour en savoir plus, voici le [Guide des participants et participantes](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024).


### Le problème et la proposition de valeur 

> - A quel problème le projet répond-t-il ?

Le projet vise à réconcilier les personnes hésitantes à prendre les transports en commun. Les transports en commun peuvent en effet être considéré comme un milieu hostile (inconfort, promiscuité, VSS, sentiment d'insécurité, ...). On va donc chercher à identifier des itinéraires "tranquilles" pour encourager ces personnes à prendre les transports.

> - Quels sont les usagers cibles ? 

En particulier, on s'adreses à un public fragile (personnes agées, enfants) et les femmes.

Personae :

Je suis Louise, j’ai 27 ans, « je veux qu’il y ai des agents en gare ça me rassure ».
Je suis Nathalie, j’ai 60 ans, « je ne prends pas les transports en commun le soir car ça fait peur ».
Je suis Antoine, j’ai 45 ans, « je veux avoir de la place assises ».
Je suis Robert, j’ai 80 ans, « j’ai peur de tomber quand je suis dans la foule ».

### La solution
> - Notre solution et son fonctionnement général

On a créé une brique logiciel sous forme de page web permettant la visualisation des "tranquili'scores". La page web puise dans une base de données contenant les données géographiques et temporelles ainsi que les indices prédits. Pour l'instant, la base de donnée est chargée à la main via un bouton mais on l'imagine être actualisé en temps réel en back-end.

> - Les données mobilisées

Techniquement, l'indice est calculé à partir de données telles que :

- taux de fraude dans la gare
- temps d'attente à quai
- date, jour de la semaine, heure, minute
- taux d'occupation à bord
- taux d'occupation à quai

et d'autres données non implémentées dans le calcul à date (taux de criminalité INSEE, nombre de bornes dans la gare, temps de trajet, ...).

> - Comment elle répond au problème

Quand un utilisateur souhaite voyager sur un itinéraire "tranquille", il peut utiliser notre brique logiciel qui lui affiche un indice de tranquillité (le "tranquili'score"), par gare et par tronçon de son itinéraire. 

En plus, un indice global est calculé pour l'itinéraire (non implémenté à date).

> La solution sous forme de web app

Nous avons créé une web app en nous inspirant du site d'Île-de-France mobilités. Nous avons repris le système de recherche d'un itinéraire, et nous y avons ajouté des informations pour renseigner le niveau d'insécurité calculé par notre algorithme 

Nous avons développé 3 vues :
- Vue itinéraire
- Vue sécurité en gare
- Vue liste des trajets

Les vues itinéraire et sécurité en gare contiennent une carte Openstreetmap du module Leaflet 

La vue itinéraire permet de visualiser le sentiment d'insécurité prédit par tronçon entre chaque gare.

La vue sécurité en gare permet de visualiser le sentiment d'insécurité prédit dans chaque gare.

La vue liste des trajets permet à l'utilisateur de consulter le niveau d'insécurité prédit pour chaque trajet sur une ligne, ce qui lui permet de choisir parmis les prochains trajets prévus.

### Les problèmes surmontés

- Difficultés dans le merge entre les bases de données, manque de référentiels

- Manque de données fiables et pertinentes pour le calcul de notre indice

- Gérer la "sensibilité" du sujet (lié aux VSS, à la sécurité)

- Trouver le bonne équilibre entre solution technique viable et idée

### Et la suite ? 

- Si on avait eu plus de temps, on aurait voulu fiabiliser l'indice en introduisant d'autres sources de données (notamment les autres sources de données évoquées plus haut, mais aussi d'autres sur la fiabilité des lignes, les signalements d'incidents, des données issues de plateformes VSS comme THE SORORITY, ...)

- On imagine une validation de notre indice via des donneés de crowdsourcing (sondage sur le sentiment de sécurité ou la tranquillité liée à un itinéraire)

- On intégrerait notre brique logiciel dans l'application Ile de France Mobilité et on sugererait l'utilisation de Tranquil'iti pour les personnes appartenant au public cible

## Intallation et utilisation

Utiliser la webapp :
1) Cliquer sur la page index.html
2) Pour afficher les trajets dans la vue utilisateur, il faut importer le fichier Test Sécurité Trajet Utilisateur.csv qui contient des informations crées par le programme de prévision
3) De même pour la vue des gares, il faut importer le fichier Test Sécurité Gare Agents.csv

## La licence
> Ici, il faut décrire la ou les licences du projet. Vous pouvez utiliser la licence [MIT](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt), qui est très permissive. Si on souhaite s'assurer que les dérivés du projet restent Open-Source, vous pouvez utiliser la licence [GPLv3](https://github.com/Illumina/licenses/blob/master/gpl-3.0.txt).

Le code et la documentation de ce projet sont sous licence [MIT](LICENSE).
