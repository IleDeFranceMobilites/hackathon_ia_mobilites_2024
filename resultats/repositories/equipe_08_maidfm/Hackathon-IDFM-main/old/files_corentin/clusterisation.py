import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder, MultiLabelBinarizer
from sklearn.cluster import KMeans
from ast import literal_eval

class UserClustering:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        
    def preprocess_data_for_knn(self, df):
        """
        Prépare les données pour une clusterisation avec KNN.
        
        Args:
        - df (pd.DataFrame): Le DataFrame brut.

        Returns:
        - pd.DataFrame: Le DataFrame prêt pour le machine learning.
        """
        df = df.copy()
        
        # Encodage de 'billettique_type'
        le = LabelEncoder()
        df['billettique_type'] = le.fit_transform(df['billettique_type'])
        
        # Remplacement des NaN dans 'billettique_tickets_left' par 0
        df['billettique_tickets_left'] = df['billettique_tickets_left'].fillna(0)
        
        # Encodage de la colonne 'PMR' (False -> 0, True -> 1)
        df['PMR'] = df['PMR'].astype(int)
        
        # Encodage des 'centres d'intérêts' avec MultiLabelBinarizer
        mlb = MultiLabelBinarizer()
        interests = df["centres d'intérêts"].apply(eval)  # Convert strings to lists
        interest_encoded = mlb.fit_transform(interests)
        interest_df = pd.DataFrame(interest_encoded, columns=mlb.classes_, index=df.index)
        df = pd.concat([df, interest_df], axis=1)
        df.drop(columns=["centres d'intérêts"], inplace=True)
        
        # Trajets : Compter le nombre de trajets
        df['nombre_trajets'] = df['trajets'].apply(lambda x: len(eval(x)))
        df.drop(columns=['trajets'], inplace=True)
        
        # Lieux favoris : Calculer la moyenne des coordonnées géographiques
        def average_coordinates(lieux):
            lieux = eval(lieux)
            avg_lat = np.mean([coord[0] for coord in lieux])
            avg_lon = np.mean([coord[1] for coord in lieux])
            return avg_lat, avg_lon

        df[['lieux_avg_lat', 'lieux_avg_lon']] = df['lieux favoris'].apply(
            lambda x: pd.Series(average_coordinates(x))
        )
        df.drop(columns=['lieux favoris'], inplace=True)
        
        # Conserver les colonnes numériques directement
        numeric_cols = ['km de marche dans les 90 derniers jours', 'intérêt événements']
        
        # Retourner le DataFrame final
        return df[numeric_cols + ['user_id', 'billettique_type', 'billettique_tickets_left', 'PMR', 
                                'nombre_trajets', 'lieux_avg_lat', 'lieux_avg_lon'] + list(mlb.classes_)]

    
    def fit_transform(self, df):
        """Transforme le dataframe et effectue le clustering"""
        # Copie du dataframe
        processed_df = pd.DataFrame()
        processed_df['user_id'] = df['user_id']

        processed_df = self.preprocess_data_for_knn(df)
        
        # Normalisation des données
        features = processed_df.drop('user_id', axis=1).values
        scaled_features = self.scaler.fit_transform(features)
        
        # Application du clustering
        clusters = self.kmeans.fit_predict(scaled_features)
        
        # Création du résultat
        result = pd.DataFrame({
            'user_id': df['user_id'],
            'cluster': clusters
        })
        
        return result


df = pd.read_csv('./data/data_generic.csv', sep=';')
clusterer = UserClustering(n_clusters=3)
new_df = clusterer.fit_transform(df)
print(new_df)

new_df['cluster'].value_counts()