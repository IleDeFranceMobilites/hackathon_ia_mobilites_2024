import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('./data/evenements-publics-cibul.csv', sep=';')

def obtenir_evenements(df, colonne_datetime, n_jours, colonnes_sortie, date_reference):
    """
    Récupère les événements des n prochains jours à partir d'une date de référence.
    
    Args:
        df (pd.DataFrame): DataFrame contenant les événements
        colonne_datetime (str): Nom de la colonne contenant les dates
        n_jours (int): Nombre de jours à considérer
        colonnes_sortie (list): Liste des colonnes à retourner
        date_reference (datetime): Date de référence
        
    Returns:
        pd.DataFrame: DataFrame filtré avec les colonnes demandées
    """
    # Conversion de la colonne datetime si nécessaire
    df[colonne_datetime] = pd.to_datetime(df[colonne_datetime])
    if not pd.api.types.is_datetime64_any_dtype(df[colonne_datetime]):
        df[colonne_datetime] = pd.to_datetime(df[colonne_datetime], utc=True)
    
    # Assurer que la colonne et la date de référence sont en UTC
    if df[colonne_datetime].dt.tz is None:
        df[colonne_datetime] = df[colonne_datetime].dt.tz_localize('UTC')
    if date_reference.tzinfo is None:
        date_reference = date_reference.tz_localize('UTC')
        
    # Calcul de la date limite
    date_limite = date_reference + pd.Timedelta(days=n_jours)
    
    # Filtrage des événements
    masque = (df[colonne_datetime] >= date_reference) & (df[colonne_datetime] <= date_limite)
    df_filtre = df.loc[masque, colonnes_sortie]
    
    return df_filtre.sort_values(colonne_datetime)

# Appel de la fonction
nouveau_df = obtenir_evenements(
    df, 
    colonne_datetime="Première date - Début", 
    n_jours=30, 
    colonnes_sortie=['Identifiant', 'Titre', 'Description', 'Première date - Début', 'Coordonnées géographiques'], 
    date_reference=pd.Timestamp('2024-05-21')
)
