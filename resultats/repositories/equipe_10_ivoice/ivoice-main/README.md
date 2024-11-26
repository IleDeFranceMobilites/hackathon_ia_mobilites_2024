# IVoice

## Présentation du projet

Ivoice is a demonstration tool illustrating how during an incident on the metro network. Customised messages can be generated for each station on the impacted line.

The tool provides a streamlit frontend to simulate the occurence of an incident and display the generated messages for each station on a map.

### Le problème et la proposition de valeur
> [!TIP]
> Ici vous pouvez répondre aux questions suivantes :
> - A quel problème votre projet répond-t-il ?
> - Quels sont les usagers cibles ?


### La solution
> [!TIP]
> Ici vous pouvez présenter
> - Votre solution et son fonctionnement général
> - Les données mobilisées
> - Comment elle répond au problème

### Les problèmes surmontés
> [!TIP]
> Ici vous pouvez présenter les principaux problèmes rencontrés et les solutions apportées

### Et la suite ?
> [!TIP]
> Ici vous vous projetez sur comment vous auriez aimé développer votre projet si vous aviez eu plus de temps ! (Quel cas d'usage pour la suite ? Quelles ressources à mobiliser ?)


## Installation et utilisation

In addition to the libraries provided in the Onyxia environment the project requires extra dependencies to run.

Install the dependencies using:
```
pip install -r requirements.txt
```

Certain environment variables must be provided as well these variables are listed in the .env.template file.
Copy the .env.template file to a file names .env and replace the "XXX" for each variable with the appropriate value.

To run the project, simply run
```
streamlit run src/front.py
```

## La licence
Le code et la documentation de ce projet sont sous licence [MIT](LICENSE).