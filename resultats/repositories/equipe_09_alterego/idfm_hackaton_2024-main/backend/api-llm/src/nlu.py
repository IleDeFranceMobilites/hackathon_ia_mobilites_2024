from .client import Client


class Nlu:
    def __init__(self):
        self.client = Client()
        self.client = self.client.get_client()
        self.model = 'gpt-4o-mini'

    def get_intentions_entites(self, message):
        conversation_history = []
        conversation_history.append(
                
            {"role": "system", "content":
                """
                    Tu est un agent intelligent, ton role consiste a detecter si la demande de
                    l'utilisateur concerne l'une des description suivantes:
                    {
                        {
                            "name": "Météo",
                            "description": "Il est possible d'accéder à la météo en temps réel en 
                            utilisant l'API indiquée dans le champ url. Il faut indiquer une
                             position en utilisant la latitude et la longitude. On peut obtenir le 
                             niveau de pluie, le niveau de neige, la vitesse du vent, la 
                             température.",
                            "url": "https://api.openweathermap.org/data/2.5/weather"
                        },
                        {
                            "name": "Liste des lignes",
                            "description": "Il est possible d'accéder à la liste des lignes de 
                            transport en commun d'Île-de-France en lisant le fichier nommé dans le 
                            champ url. Pour chaque ligne, la liste contient l'identifiant 
                            commercial, l'identifiant administratif, son nom, si elle est
                             accessible PMR, son mode de transport. Elle contient les lignes de
                            bus, métro, RER, navette
                             aéroport, tramway, funiculaire.",
                            "url": "referentiel-des-lignes.parquet"
                        },
                        {
                            "name": "Liste des arrêts",
                            "description": "Il est possible d'accéder à la liste des arrêts en
                             lisant le fichier nommé dans le champ url. Pour chaque arrêt, la liste 
                             contient ses coordonnées géographiques en latitude/longitude WGS 84 
                             ainsi que Lambert-93, son identifiant, son nom, son mode de transport, 
                             le nom de sa commune, sa zone de tarif Navigo, si elle est accessible 
                             PMR.",
                            "url": "referentiel-des-lignes.parquet"
                        },
                        {
                            "name": "Correspondance arrêt-ligne",
                            "description": "Il est possible d'accéder à la correspondance entre
                             identifiant d'arrêt et identifiant de ligne commerciale en lisant le 
                             fichier nommé dans le champ url.",
                            "url": "arrets-lignes.parquet"
                        },
                        {
                            "name": "Relations arrêts",
                            "description": "Il est possible d'accéder aux relations entre objets
                             arrêt tels quel arrêt transporteur, arrêt, zone d'arrêts, zone de 
                             correspondance, pôle d'échanges, grâce à leurs identifiants. Il faut
                            utiliser le fichier nommé dans le champ url.",
                            "url": "relations.parquet"
                        }
                }
                Sinon demande à l'utilisateur de dmander une information à propos d'IDFM"

                """})
        conversation_history.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=conversation_history,
            temperature=0,
        )
        return response.choices[0].message.content
