import pandas as pd
from Hackathon_équipe8.domain.llm.llm_management import LLMConfiguration
from Hackathon_équipe8.domain.llm.prompts import prompt_test
import random

# Utiliser la configuration LLM existante
llm_config = LLMConfiguration()

# Charger les données enregistrées
df = pd.read_csv('data/data_clustered.csv')  # Chargement du premier fichier

# Fonction pour générer un message personnalisé en utilisant Azure OpenAI
def generate_custom_message(user_data):
    prompt = f"""
    Crée un message personnalisé pour l'utilisateur en fonction de ses informations d'abonnement :
    - Abonnement : {user_data['billettique_type']}
    - Fin de validité : {user_data['billettique_end_date']}
    - Tickets restants : {user_data['billettique_tickets_left']}
    Ne génère le message que si l'utilisateur a besoin d'être averti, par exemple :
    - S'il reste moins de 2 tickets.
    - Si l'abonnement expire dans moins de 7 jours.
    Le message doit être court, il doit y avoir de la place pour plein de message dans l'écran
    """

    # Utiliser l'objet llm_config pour générer le message
    response = llm_config.invoke(prompt_test.format(input=prompt))
    return response

# Test simple pour vérifier la communication avec le LLM
def test_llm():
    input = "Bonjour, pouvez-vous me donner une recommandation de livre ?"
    response = llm_config.invoke(prompt_test.format(input=input))
    print("Test LLM Response:", response)


# Sélectionner aléatoirement 5 utilisateurs pour générer des messages
random_indices = random.sample(range(len(df)), 15)

# Appliquer la fonction à chaque utilisateur sélectionné et récupérer les messages personnalisés
messages = []
for index in random_indices:
    row = df.iloc[index]
    if row['billettique_type'] in ['Navigo Mois', 'Navigo Semaine']:
        end_date = pd.to_datetime(row['billettique_end_date'], errors='coerce')
        if pd.notna(end_date) and (end_date - pd.Timestamp.today()).days <= 7:
            messages.append((row['user_id'], generate_custom_message(row)))
    elif row['billettique_type'] == 'Ticket t+' and row['billettique_tickets_left'] < 3:
        messages.append((row['user_id'], generate_custom_message(row)))

# Afficher les messages à envoyer
for user_id, message in messages:
    print(f"User ID {user_id}: {message}")
