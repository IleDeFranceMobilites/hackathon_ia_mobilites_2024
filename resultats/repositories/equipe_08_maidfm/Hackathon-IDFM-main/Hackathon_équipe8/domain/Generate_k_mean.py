import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Charger les données enregistrées
df = pd.read_csv('./Hackathon_équipe8/data/data_clustered.csv')  # Chargement du premier fichier

# Préparation des données pour le clustering
# Nous allons utiliser les colonnes numériques et convertir certaines colonnes qualitatives en indicateurs

# Colonnes numériques
numeric_features = ['km de marche dans les 90 derniers jours', 'intérêt événements']

# Colonnes qualitatives à encoder
categorical_features = ['billettique_type', 'PMR']

# Convertir les colonnes qualitatives en indicateurs (one-hot encoding)
df_encoded = pd.get_dummies(df[categorical_features], drop_first=True)

# Transformer les colonnes contenant des listes (trajets, centres d'intérêts, lieux favoris) en compte ou caractéristiques simplifiées
# Compter le nombre de trajets pour chaque utilisateur
trajet_count = df['trajets'].apply(len)
# Compter le nombre de centres d'intérêts pour chaque utilisateur
centres_interet_count = df['centres d\'intérêts'].apply(len)
# Compter le nombre de lieux favoris pour chaque utilisateur
lieux_favoris_count = df['lieux favoris'].apply(len)

# Ajouter ces nouvelles colonnes au DataFrame
X = pd.concat([df[numeric_features], df_encoded, trajet_count.rename('trajet_count'), centres_interet_count.rename('centres_interet_count'), lieux_favoris_count.rename('lieux_favoris_count')], axis=1)

# Normaliser les données
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Appliquer la règle du coude pour déterminer le nombre optimal de clusters
inertia = []
K = range(1, 10)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Tracer le graphique de la règle du coude
plt.figure(figsize=(10, 6))
plt.plot(K, inertia, 'bo-', markersize=8)
plt.xlabel('Nombre de clusters')
plt.ylabel('Inertie (Inertia)')
plt.title("Règle du coude pour déterminer le nombre optimal de clusters")
plt.grid(True)
plt.show()

# Appliquer le clustering k-means avec un nombre de clusters optimal (choisi arbitrairement ici à 3)
optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
labels = kmeans.fit_predict(X_scaled)

# Ajouter les labels de clusters au DataFrame original
df['cluster'] = labels

# Évaluation du clustering avec l'indice de silhouette
silhouette_avg = silhouette_score(X_scaled, labels)
print(f"Silhouette Score: {silhouette_avg:.2f}")

# Quelques statistiques sur les clusters formés
cluster_counts = df['cluster'].value_counts()
print("\nNombre d'utilisateurs par cluster :")
print(cluster_counts)

# Statistiques descriptives pour chaque cluster
cluster_stats = df.groupby('cluster').mean()
print("\nStatistiques descriptives par cluster :")
print(cluster_stats)
