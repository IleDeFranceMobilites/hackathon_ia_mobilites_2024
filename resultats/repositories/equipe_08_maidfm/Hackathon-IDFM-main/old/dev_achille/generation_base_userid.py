import pandas as pd
import numpy as np
import datetime

# Nombre d'utilisateurs à générer
n_users = 1000

# Date actuelle
today = datetime.date.today()

# Dictionnaire des lignes de transport avec leurs stations correspondantes
lines_dict = {
    "Métro 1": ["La Défense", "Champs-Elysées", "Concorde", "Bastille", "Nation"],
    "Métro 2": ["Porte Dauphine", "Charles de Gaulle - Étoile", "Anvers", "Nation"],
    "Métro 3": ["Pont de Levallois", "Saint-Lazare", "Opéra", "République", "Gambetta"],
    "Métro 4": ["Porte de Clignancourt", "Barbès", "Châtelet", "Montparnasse", "Mairie de Montrouge"],
    "Métro 5": ["Bobigny", "Gare du Nord", "République", "Bastille", "Place d'Italie"],
    "Métro 6": ["Charles de Gaulle - Étoile", "Trocadéro", "Montparnasse", "Nation"],
    "Métro 7": ["La Courneuve", "Gare de l'Est", "Opéra", "Place d'Italie", "Villejuif"],
    "Métro 8": ["Balard", "Invalides", "Opéra", "Bastille", "Créteil"],
    "Métro 9": ["Pont de Sèvres", "Trocadéro", "Chaussée d'Antin", "République", "Mairie de Montreuil"],
    "Métro 10": ["Boulogne", "La Motte-Picquet", "Odéon", "Gare d'Austerlitz"],
    "RER A": ["La Défense", "Charles de Gaulle - Étoile", "Châtelet", "Nation", "Marne-la-Vallée"],
    "RER B": ["Aéroport CDG", "Gare du Nord", "Châtelet", "Denfert-Rochereau", "Robinson"],
    "RER C": ["Versailles", "Invalides", "Musée d'Orsay", "Gare d'Austerlitz"],
    "Bus 38": ["Gare du Nord", "Châtelet", "Luxembourg", "Porte d'Orléans"],
    "Bus 72": ["Parc de Saint-Cloud", "Trocadéro", "Hôtel de Ville"]
}

# Centres d'intérêts disponibles
interests = ["Voyages", "Sport", "Musique", "Lecture", "Cuisine", "Cinéma", "Jeux vidéo", "Art et artisanat", "Randonnée et nature", "Technologie et gadgets"]

# Probabilités pour les centres d'intérêts
interests_prob = [0.2, 0.15, 0.15, 0.1, 0.1, 0.1, 0.075, 0.05, 0.05, 0.025]

# Génération des trajets avec correspondance entre lignes et stations
def generate_trips():
    trips = []
    for _ in range(2):  # Toujours deux trajets favoris
        line = np.random.choice(list(lines_dict.keys()))
        stations = lines_dict[line]
        start, end = np.random.choice(stations, 2, replace=False)
        time = f"{np.random.randint(5, 23)}:{np.random.choice([0, 30]):02d}"
        trips.append([start, end, line, time])
    return trips


def generate_ticket_info():
    types = ["Navigo Mois", "Navigo Semaine", "Ticket t+"]
    type_abo = np.random.choice(types)

    if type_abo == "Navigo Mois":
        # Date de fin le 1er jour du mois suivant
        year = today.year
        month = today.month + 1 if today.month < 12 else 1
        year += 1 if today.month == 12 else 0
        end_date = datetime.date(year, month, 1).isoformat()
        tickets_left = None
    elif type_abo == "Navigo Semaine":
        # Date de fin le prochain lundi après la date actuelle
        days_until_monday = (7 - today.weekday()) % 7
        end_date = (today + datetime.timedelta(days=days_until_monday)).isoformat()
        tickets_left = None
    elif type_abo == "Ticket t+":
        # Nombre de billets restants entre 0 et 4 majoritairement
        tickets_left = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], p=[0.3, 0.2, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05])
        end_date = None  # Pas de date de fin pour les tickets simples

    return type_abo, end_date, tickets_left


# Génération des lieux favoris dans Paris (coordonnées aléatoires à Paris)
def generate_favorite_places():
    # Paris est approximativement compris entre 48.81°N - 48.90°N et 2.25°E - 2.42°E
    places = []
    for _ in range(2):  # Toujours deux lieux favoris
        latitude = np.random.uniform(48.81, 48.90)  # Génération de la latitude dans Paris
        longitude = np.random.uniform(2.25, 2.42)   # Génération de la longitude dans Paris
        places.append([latitude, longitude])
    return places

# Génération des centres d'intérêts
def generate_interests():
    return np.random.choice(interests, 2, replace=False, p=interests_prob).tolist()

# Génération des kilomètres de marche en utilisant une distribution normale
def generate_km_walked():
    mean = np.random.choice([30, 80, 120], p=[0.3, 0.4, 0.3])  # Trois groupes principaux : faible, moyen, élevé
    return np.clip(np.random.normal(mean, 15), 5, 200)  # Limiter les valeurs dans un intervalle réaliste

# Génération des PMR (5% des utilisateurs)
def generate_pmr():
    return np.random.choice([True, False], p=[0.05, 0.95])

# Génération de l'intérêt pour les événements (note de 1 à 5)
def generate_event_interest():
    return np.random.randint(1, 6)

# Création des données fictives
data = {
    "user_id": range(1, n_users + 1),
    "trajets": [generate_trips() for _ in range(n_users)],
    "billettique_type": [],
    "billettique_end_date": [],
    "billettique_tickets_left": [],
    "centres d'intérêts": [generate_interests() for _ in range(n_users)],
    "lieux favoris": [generate_favorite_places() for _ in range(n_users)],
    "km de marche dans les 90 derniers jours": [generate_km_walked() for _ in range(n_users)],
    "PMR": [generate_pmr() for _ in range(n_users)],
    "intérêt événements": [generate_event_interest() for _ in range(n_users)]
}

# Génération des abonnements ou tickets pour chaque utilisateur
for _ in range(n_users):
    type_abo, end_date, tickets_left = generate_ticket_info()
    data["billettique_type"].append(type_abo)
    data["billettique_end_date"].append(end_date)
    data["billettique_tickets_left"].append(tickets_left)

# Création d'un DataFrame
df = pd.DataFrame(data)

# Affichage des premières lignes
df.head(20)
