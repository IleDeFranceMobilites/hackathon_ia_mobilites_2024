![Logo du Hackathon IA et Mobilités](/images/Logo%20illustre_Hackathon%20IA%20Mobilites.jpg)

# Guide des participants au Hackathon IA et Mobilités d'Île-de-France Mobilités 

Bienvenue dans le Hackathon IA et Mobilités !

## Comment l’usage de l’IA peut-il améliorer les services mobilités ?

C'est la question que vous allez vous poser les 21 et 22 novembre 2024 à Paris. 

Vous allez travailler en équipe afin de **faire émerger des idées et des prototypes afin d’explorer la pertinence de l'IA et d’en étudier l’usage et les limites dans le domaine de la mobilité.** Île-de-France Mobilités vous mets à disposition un certain nombre de ressources, dont un Datalab : Onyxia.

Ce document va vous servir de guide tout au long de ce Hackathon et dans sa pahse de préparation.


## Sommaire
1. [Le programme](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024?tab=readme-ov-file#le-programme)
2. [Les défis](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024?tab=readme-ov-file#les-d%C3%A9fis)
2. [Les ressources et les outils](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024?tab=readme-ov-file#les-ressources-et-les-outils)
3. [Vos résultats](https://github.com/IleDeFranceMobilites/hackathon_ia_mobilites_2024?tab=readme-ov-file#vos-r%C3%A9sultats)

## Le programme

- Jeudi 21 : Acceuil café à **9h**, fin de la journée à 19h
- Vendredi 22 : Acceuil café à **8h**, début du cocktail à 17h30

## Les défis

Pendant ces deux jours, vous allez répondre en équipe de 4 à 7 personnes à un défi. L'objectif est de proposer un projet qui répondre à un des 4 défis proposés. [Les défis sont présentés dans ce document](/docs/defis.md). 

- **Défi 1** - Améliorer l'**accessibilité** des services de mobilité
- **Défi 2** - Construire une **boîte à outils** pour accélérer le développement de l’IA au service des usagers
- **Défi 3** - Améliorer les **prévisions** au service des mobilités
- **Défi 4** - **Personnaliser** l’expérience utilisateur des services numériques au voyageur

**Défi transveral frugalité** : Comment la frugalité des systèmes d’IA utilisés peut-elle améliorer mon projet ?

## Les ressources et les outils

#### Le Slack

C'est sur le slack qu'aurons lieu les principaux échanges ([lien d'invitation au slack](https://join.slack.com/t/dataiailedefr-mya4689/shared_invite/zt-2u2bo2v10-YcUO~FlnNwl~W0mLCZLBUQ)). Chaque canal possède une description dans un message épinglé.
- **00-general** : pour échanger librement sur le Hackathon IA et Mobilités, et poser vos question à l'équipe d'organisation.
- **01-welcome** : pour vous présenter quelques mots : vous, vos domaines d'expertise (votre profil), le défi qui vous intéresse et si vous être à la recherche d'une équipe
- **03-ressources-outils-données** : pour échanger sur les ressources, outils et données mises à disposition par Île-de-France Mobilités dans le cadre du Hackathon IA et Mobilités
- **04x-défis** : pour échanger sur les 4 défis proposés lors de ce hackathon
- **05x-équipe-nom-équipe** : les canaux d'équipes seront créés au fur et à mesure de la constitution des équipes

Une fois ajouté sur le slack, **vous pouvez vous présenter dans le canal 01-welcome et vous mettre à la recherche d'une équipe** dans les canaux dédiés aux différents défis. 

Les équipes se composeront librement, mais les Organisateurs se réservent les droits de rééquilibrer les profils et niveaux entre les équipes ! Une fois les équipes constituées, vous aurez alors rejoins le salon de votre équipe. C'est l'occasion pour commencer à vous mieux vous connaître et échanger sur la découverte des ressources et données mises à diposition. 

#### La plateforme Onyxia et ses services

Onyxia est la plateforme que vous allez utiliser tout au long de ces deux jours. 

C'est une application web open-source développée par l’Insee conçue pour les data scientists en leur offrant un environnement de travail de pointe. En substance, Onyxia propose un catalogue de services (VSCode, Jupyter, etc...) que vous pouvez lancer depuis la plateforme.

1. Se connecter à [Onyxia](https://datalab.data-platform-self-service.net). Il faut créer un compte avec l'adresse email avec laquelle vous vous êtes inscrits au Hackathon. 
2. Une fois connecté à Onyxia vous avez accès votre projet personnel. Vous serez ajouté dans les jours qui suivent votre connexion au projet dédié au hackathon **"dlb-hackathon"** (voir image ci-dessous).
3. C'est dans ce projet que sont partagées en tant que variables d'envrionnement les clés des différentes APIs et ressources mises à disposition. Vous pouvez donc découvrir la plateforme dans votre projet personnel, puis les ressources dans le projet dlb-hackathon une fois ajouté à celui-ci.

![Capture d'écran sélection du projet Onyxia](/images/projet-onyxia.png)

Vous pouvez ensuite lancer des services (par exemple un service Visual Studio Code Python), et les lier au repositoire de code de votre groupe.

 Attention, les services ne sont pas stables si ils sont éteins, alors vous perdez leurs configurations. Voir [ce tutoriel](https://docs.onyxia.sh/user-doc/setting-up-your-dev-environment-in-onyxia) pour configurer automatiquement un sevice. 

Les principaux services proposés : 
| Nom du service | Description | Catégorie de service |
|----------------|-------------|----------------------|
| Jupyter python | IDE Jupyter avec les libraires data python pré-installées | Environnements de développement |
| VSCode python | Visual Studio Code avec les libraire data python pré-installées | Environnements de développement |
| Elastic | pour vos bases vectorielles et stockages de documents JSON | Base de données |
| Cloudbeaver | pour vos bases de données | Base de données |
| OpenWebIU | une interface web "no-code" (ou pas) pour créer des chatbots personnalisés à partir d'une grande diversité de modèles de langage | Spécifique au Hackathon |

#### Les ressources à votre disposition

Vous disposez d'un certain nombre de ressources à votre disposition. Le but n'est pas de toute les consulter, mais qu'elle puissent vous faire gagner du temps lors de la production de vos projets. 

##### Les données et documents

Pour entraîner vos algorithmes, visualiser des données, utilser des APIs ou encore alimenter votre RAG on a sélectionner pour vous des **données et documents**. 

Ils sont accessible [depuis ce lien](https://airtable.com/appGp6Hwf0NrmXQ9L/shrnmQYmL0lDKgS76/tblC8dlSqeplzyg0A). Vous pouvez **filtrer les données sur le défi qui vous intéresse**. Certaines ressources sont issues du [Catalogue PRIM](https://prim.iledefrance-mobilites.fr/fr), d'autres sont directement ajoutés dans les fichiers du projet Onyxia 'dlb-hackathon'.

<img src="images/airtable.png" alt="liste des données" width="800"/>

##### Les snippets de code

Ces **[snippets de code](/notebooks/snippets_code.ipynb)** vont vous permettre de gagner du temps dans la prise en main des ressources à disposition et de l'écosystème data d'île-de-France Mobilités.

#### Les exemples (notebook)

Les équipe d'Île-de-France Mobilités ont préparé un **exemple de Retrieval Augemented Generation RAG** (de la base vectorielle à la requête), qui permet d'enrichir les connaissances d'un modèle de langage avec des données spécifiques. 

Cet exemple est **disponible dans les notebooks** du [dossier dédié](/notebooks/).

Vous pouvez **lancer les notebooks exemple directement sur Onyxia**. Pour cela, **assurez vous d'être connectés sur Onyxia et d'être sur le projet "dlb-hackathon"**, suivez ce [lien.](https://datalab.data-platform-self-service.net/launcher/ide/jupyter-python?autoLaunch=true&onyxia.friendlyName=%C2%ABpython-rag%C2%BB&init.personalInit=%C2%ABhttps%3A%2F%2Fraw.githubusercontent.com%2FIleDeFranceMobilites%2Fhackathon_mobilite%2Frefs%2Fheads%2Fmain%2Fscripts%2Finit_jupyter.sh&vault.secret=«project-key»)

Le service se lance sur le projet actuellement ouvert dans votre instance Onyxia. Vous pouvez ouvrir le service dans l'espace dédié au Hackathon 'dlb-hackathon'.

#### La documentation
Au fur est à mesure des questions, nous ajouterons les liens vers les documentations pertinentes dans ce guide.

## Vos résultats
Vos projets viendront alimenter la communauté Data IA et mobilités. **Les réalisation seront publiées sous licences libres** (type MIT) et publiées sur **un répertoire en ligne**. 

Concrètement, vous allez réaliser :
- un support de présentation ;
- le projet : des notebooks, applications, templates, jeux de données … ;
- tout autre forme qui pourra valoriser votre projet ! 

**Chaque équipe présentera son projet au jury à l’oral**, dans un temps limité.

Vous serez guidés par les équipes d’organisation pour pticher au mieux votre projet !
