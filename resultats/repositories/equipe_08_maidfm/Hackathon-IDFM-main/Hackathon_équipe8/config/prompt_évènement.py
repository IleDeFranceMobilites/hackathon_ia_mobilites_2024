import pandas as pd
from Hackathon_équipe8.domain.llm.llm_management import LLMConfiguration
from Hackathon_équipe8.domain.llm.prompts import prompt_test
import random

# Utiliser la configuration LLM existante
llm_config = LLMConfiguration()

try:
    print("Chargement des fichiers...")
    df = pd.read_csv('data/data_clustered.csv')  # Chargement du premier fichier
    df_events = pd.read_csv('data/evenements-publics-cibul.csv', sep=';', engine='python')  # Chargement du second fichier
    print(f"Data Clustered Rows: {len(df)}, Columns: {df.columns.tolist()}")
    print(f"Events Rows: {len(df_events)}, Columns: {df_events.columns.tolist()}")
except Exception as e:
    print(f"Erreur lors du chargement des fichiers : {e}")
    exit()

def get_relevant_events(user_interests, df_events):
    relevant_events = []
    for index, row in df_events.iterrows():
        event_keywords = row['Mots clés'].split(',') if pd.notna(row['Mots clés']) else []
        if any(interest in event_keywords for interest in user_interests):
            relevant_events.append(row)
        if len(relevant_events) >= 2:
            break
    print(f"Événements pertinents trouvés : {relevant_events}")
    return relevant_events[:2]

def generate_custom_message(user_data, events):
    if not events:
        return ""

    event_details = "\n".join([
        f"- Événement : {event['Titre']}\n  - Description : {event['Description']}\n  - Lien : {event['URL canonique']}"
        for event in events
    ])
    user_interests_str = ', '.join(user_data['centres d\'intérêts'])
    prompt = f"""
    Crée un message personnalisé pour l'utilisateur en fonction de ses centres d'intérêts et des événements disponibles en Île-de-France dans les prochains jours.
    Les centres d'intérêts de l'utilisateur sont : {user_interests_str}
    Voici une liste d'événements récents :
    {event_details}
    """
    print("Prompt envoyé au LLM :")
    print(prompt)
    response = llm_config.invoke(prompt_test.format(input=prompt))
    print(f"Réponse du LLM : {response}")
    return response

print("Début de la génération des messages...")
random_indices = random.sample(range(len(df)), 5)
messages = []
for index in random_indices:
    row = df.iloc[index]
    user_interests = row['centres d\'intérêts']
    relevant_events = get_relevant_events(user_interests, df_events)
    if relevant_events:
        message = generate_custom_message(row, relevant_events)
        if message:
            messages.append((row['user_id'], message))

print("Messages générés :")
for user_id, message in messages:
    print(f"User ID {user_id}: {message}")
