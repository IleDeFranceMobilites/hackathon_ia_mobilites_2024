##################################
#   creation d'un jeu de donnees
##################################

import pandas as pd
from datetime import datetime, timedelta
import numpy as np

### import data

path = "C:/Users/9920510N/SNCF/Pôle data - Lab' MTA GrpO365 - Documents/Projets/Hackathon/Données/Données brutes"

# referentiel
data_PA_UIC = pd.read_csv(path + "/PA_UIC.csv", sep = ";")
data_PA_Ligne = pd.read_csv(path + "/PA_Ligne.csv", sep = ";")
data_ordre_gare = pd.read_csv(path + "/Ordre-gares-all.csv", encoding="latin-1", sep = ";")

# selection
ligne = "H"
branche = "Gare du Nord - Pontoise"

data_ordre_gare_H = data_ordre_gare[data_ordre_gare['Ligne'] == ligne]
data_ordre_gare_H_branche = data_ordre_gare_H[data_ordre_gare_H['Branche'] == branche]

dicti = {"Pontoise":"PSE",
"Saint-Ouen-L'aumone":"SOA",
"Saint-Ouen-L'aumone-Liesse":"SOL",
"Pierrelaye":"PRY",
"Montigny-Beauchamp":"MBP",
"Franconville-Plessis-Bouchard":"FPB",
"Cernay":"CEJ",
"Ermont-Eaubonne":"ERT",
"Saint-Denis":"SDE",
"Epinay-Villetaneuse":"EPV",
"Gare du Nord":"PNB",
"La Barre-Ormesson":"LBJ",
"Enghien-les-Bains":"EN",
"Champ De Courses D'enghien":"CEG"
}


# merge entre les differents referentiels
data_ordre_gare_H_branche['CodeGare'] = data_ordre_gare_H_branche['Lib_gare_TN'].map(dicti)
print(data_ordre_gare_H_branche['CodeGare'].unique())
#data_ordre_gare_H_branche = data_ordre_gare_H_branche.merge(data_PA_UIC, left_on = "Lib_gare_TN", right_on = "LibelleLong", how='left')

# générer un vecteur de temps
def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

dts = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in 
       datetime_range(datetime(2023, 11, 1, 6), datetime(2023, 11, 15, 23), 
       timedelta(minutes=5))]

# créer les combinaison de gare
data_ordre_gare_H_branche.to_csv(path + "/data_ordre_gare_H_branche.csv")
data = pd.read_csv(path + "/data_ordre_gare_H_branche.csv", sep = ",")

# creer le jeu données
data["Gare_B"] = np.roll(data["CodeGare"], shift = -1)
data["Gare_A"] = data["CodeGare"]



select = ["Gare_A", "Gare_B", "Ligne", "Ordre", 'Sens']
dts = pd.DataFrame({"Jour-heure" : dts})
data_final = data[select].merge(dts, how='cross')

data_final.to_csv(path + "/Base_de_donnees_finale.csv")

data_final = pd.read_csv(path + "/Base_de_donnees_finale.csv")

### add lat et long
referentiel_gare = pd.read_csv(path + "/Referentiel_gare.csv", sep = ";")

coordonnees = referentiel_gare['Position géographique'].str.split(",", expand=True)
coordonnees = coordonnees.rename(columns={0:"lat", 1:"long"})
referentiel_gare = pd.concat([referentiel_gare, coordonnees], axis = 1)


data_final = data_final.merge(referentiel_gare[['Trigramme', 'lat', 'long']],
                              left_on = "Gare_A", right_on = "Trigramme",how='left')

data_final = data_final.rename(columns={"lat":"Lat_A", "long":"Long_A"})

data_final = data_final.merge(referentiel_gare[['Trigramme', 'lat', 'long']],
                              left_on = "Gare_B", right_on = "Trigramme",how='left')

data_final = data_final.rename(columns={"lat":"Lat_B", "long":"Long_B"})
data_final["Gare_A"] = data_final["Gare_A"].replace("PNB", "GDS")
data_final["Gare_B"] = data_final["Gare_B"].replace("PNB", "GDS")
data_final.to_csv(path + "/Base_de_donnees_finale_v2.csv")

### add column score nul

# taux d'occupation
# en gare : (nombre de validations/nombre de trains)/ (200m * 3m = surface estimée des quais)
# à bord : charge à bord / places totales
data_final["Taux_occ_AB"] = 0.25
data_final["Taux_occ_A"] = 0.1
data_final["Taux_occ_B"] = 0.8

# temps de contact avec le service
# temps de trajet
data_final["Temps_AB"] = 3
data_final["Temps_A"] = 2
data_final["Temps_B"] = 2

# présence en gare
data_final["Presence_gare_A"] = 1.5
data_final["Presence_gare_B"] = 0.8

# fraude
data_final["Fraude_A"] = 0.55
data_final["Fraude_B"] = 0.1

# criminalite adjacente
data_final["Taux_criminalite_A"] = 0.3
data_final["Taux_criminalite_B"] = 0.8

# indicateur final
data_final["Indice_troncon_AB"] = 0
data_final["Indice_gare_A"] = 0
data_final["Indice_gare_B"] = 0

data_final.to_csv(path + "/Base_de_donnees_finale_v3.csv")

def score_occupation_bord(taux_occ_bord):
    taux_occ_bord[taux_occ_bord < 0.1] = 4
    taux_occ_bord[(taux_occ_bord > 0.1) & (taux_occ_bord < 0.25)] = 1
    taux_occ_bord[(taux_occ_bord > 0.25) & (taux_occ_bord < 0.5)] = 2
    taux_occ_bord[(taux_occ_bord > 0.5)] = 3
    return(taux_occ_bord)
    
def score_occupation_quai(taux_occ_quai):
    taux_occ_quai[taux_occ_quai < 0.1] = 4
    taux_occ_quai[(taux_occ_quai > 0.1) & (taux_occ_quai < 0.25)] = 1
    taux_occ_quai[(taux_occ_quai > 0.25) & (taux_occ_quai < 0.5)] = 2
    taux_occ_quai[(taux_occ_quai > 0.5)] = 3
    return(taux_occ_quai)
    
def score_temps_trajet(temps_trajet):
    temps_trajet = 1
    return(temps_trajet)
    
def score_temps_attente(temps_attente):
    temps_attente[temps_attente < 2] = 1
    temps_attente[(temps_attente > 2) & (temps_attente < 5)] = 2
    temps_attente[(temps_attente > 5)] = 3
    return(temps_attente)

def score_presence_en_gare(presence_en_gare):
    presence_en_gare = 1
    return(presence_en_gare)

def score_fraude(fraude):
    fraude[fraude > 50] = 4
    fraude[(fraude > 20) & (fraude < 50) ] = 3
    fraude[(fraude > 10) & (fraude < 20) ] = 2
    fraude[(fraude < 10) ] = 1
    return(fraude)

def score_taux_criminalite(taux_criminalite):
    taux_criminalite = 1
    return(taux_criminalite)
    
def feel_safe_score(data):
    # Taux d'occupation
    score_occupation_A = score_occupation_quai(data["Taux_occ_A"]) 
    score_occupation_B = score_occupation_quai(data["Taux_occ_B"]) 
    score_occupation_AB = score_occupation_bord(data["Taux_occ_AB"]) 
    
    # Temps de contact avec le service
    # Temps d'attente
    score_attente_A = score_temps_attente(data["Temps_A"])
    score_attente_B = score_temps_attente(data["Temps_B"])
    # score_attente_AB = ...
    
    # Fraude
    score_fraude_A = score_fraude(data["Fraude_A"])
    score_fraude_B = score_fraude(data["Fraude_B"]) 
    
    # Présence en gare
    score_presence_gare_A = score_presence_en_gare(data["Presence_gare_A"]) 
    score_presence_gare_B = score_presence_en_gare(data["Presence_gare_B"]) 
  
    # Taux de criminalité
    score_criminalite_gare_A = score_presence_en_gare(data["Taux_criminalite_A"]) 
    score_criminalite_gare_B = score_presence_en_gare(data["Taux_criminalite_B"])
    
    max_score_A = 4 * 2 + 2 * 1 + 3
    max_score_B = 4 * 2 + 2 * 1 + 3
    max_score_AB = 4
    
    
    data["Indice_troncon_AB"] = score_occupation_AB / max_score_AB
    data["Indice_gare_A"] = (score_occupation_A + score_attente_A + score_fraude_A +
                                   score_presence_gare_A + score_criminalite_gare_A) / max_score_A
    data["Indice_gare_B"] = (score_occupation_B + score_attente_B + score_fraude_B +
                                   score_presence_gare_B + score_criminalite_gare_B) / max_score_B
    
    return(data)
    

data_final_safe_score = feel_safe_score(data_final)

data_final_safe_score.to_csv(path + "/Base_finale.csv")