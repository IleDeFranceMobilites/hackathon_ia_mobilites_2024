# Accit-API

## Présentation du projet

Ce projet a été développé dans le cadre du [Hackathon IA et Mobilités](https://www.iledefrance-mobilites.fr/actualites/hackathon-2024-ia-et-mobilites), organisé par Île-de-France Mobilités les 21 et 22 novembre 2024. Pour en savoir plus, voici le [Guide des participants et participantes](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024).

Il correspond au back-end du projet [accit](https://github.com/idfm-ai-hackathon/accit).

### Le problème et la proposition de valeur 
Le problème général est décrit dans le README du repo Accit.
Ce repo correspond aux solutions back-end et algorithmique pour résoudre les problèmes suivants :
- traduire des messages en FALC en utilisant un LLM (opération de "FALC-isation") et évaluer la qualité de la traduction,
- détecter l’utilisateur en transit et les perturbations pouvant l’impacter,
- calculer un itinéraire prenant en compte les indisponibilités des ascenceurs.

### La solution
#### FALC-isation
Le prompt utilisé comme "system prompt" est construit à partir de guides pour le FALC comme celui de l’UNAPEI donné en ressource. Nous l’avons testé et amélioré en utilisant des messages d’information trafic et en évaluant nous-même la qualité du résultat.

#### Détection de l’utilisateur en transit
Cette partie n’a pas été codée, dans les idées évoquées :
- utiliser l’historique des déplacements de l’utilisateur (avec son accord) pour rapprocher le trajet actuel de ses habitudes (par ex. trajet domicile-travail le matin en semaine à la même heure tous les jours)
- utiliser la géolocalisation (avec l’accord de l’utilisateur) pour détecter la présence aux abords d’une gare suivi d’un déplacement plus rapide (dans un train en mouvement), à combiner avec l’accéléromètre du téléphone pour gérer les tunnels du métro (cf. ce que fait Géovélo pour détecter les trajets à vélo)
- demander à l’utilisateur de confirmer qu’il est en transit via une pop-up

#### Détection de perturbations
Cette partie n’a pas été codée, dans les idées évoquées :
- utiliser l’API `disruptions/v2` de PRIM/IdFM pour connaître les nouvelles perturbations en temps réel
- détecter l’immobilité imprévue d’un utilisateur (via géolocalisation ou accéléromètre) -> pourrait aussi être utilisé à plus large échelle par IdFM comme donnée complémentaire (un peu comme Waze)

#### Calcul d’itinéraire
Lors qu’une perturbation est détectée, le back-end interroge l’API itinéraire IdFM avec les éléments suivants :
- la station de l’utilisateur, tirée de sa position (obtenue par géolocalisation si possible, ou par interpolation sur son parcours si la géolocalisation est impossible, par exemple dans le métro),
- ses paramètres de trajet : destination, accessibilité physique.

Une fois le ou les itinéraires alternatifs calculés, on vérifie la disponibilité des ascenceurs via l’API IdFM associée avant de suggérer l’itinéraire.

### Les problèmes surmontés
> [!TIP]
> Ici vous pouvez présenter les principaux problèmes rencontrés et les solutions apportées

### Et la suite ? 
#### FALC-isation
Le FALC produit doit être validé par des personnes concernées et des associations spécialisées, il sera donc indispensable de se rapprocher d’experts pour consolider notre démarche.

Ce serait intéressant de faire tourner le modèle pour scorer et/ou FALC-iser les messages d’informations du réseau IdFM pour voir à quel point ces messages sont faciles à comprendre d’une part, et d’autre part pour peut-être les faire évoluer vers plus de simplicité.


## Intallation et utilisation
> [!TIP]
> Si vous avez le temps, vous pouvez décrire les étapes d'installation de votre projet (commandes à lancer, ...) et son fonctionnement.

## Ressources
### Pour le FALC
- document "L’information pour tous" [en PDF](https://www.unapei.org/wp-content/uploads/2018/11/L%E2%80%99information-pour-tous-Re%CC%80gles-europe%CC%81ennes-pour-une-information-facile-a%CC%80-lire-et-a%CC%80-comprendre.pdf)
- site LIREC et éditeur/analyseur de FALC (http://51.91.138.70/lirec/#)

### Calcul d’itinéraire 
- https://www.metro-connexion.org/index.php pour la description des correspondances
## Remerciements
Aurélie Chasles, spécialiste du FALC, consultée par téléphone pendant le hackathon (http://aureliechasles-falc.fr/)
