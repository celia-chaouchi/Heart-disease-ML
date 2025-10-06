import pandas as pd
data = pd.read_csv("6 - data.csv")
data.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
#suppression des valeurs manquante
data['ca'] = pd.to_numeric(data['ca'], errors='coerce') #transforme les valeurs en nuùérique et en Nan si impossible
data['thal'] = pd.to_numeric(data['thal'], errors='coerce')
data.dropna(subset=['thal','ca'], inplace=True) #suppression de svaleurs nulles 
#print (data.isnull().sum())#verifier qu'on a aucune valeurs manquantes

#recodage des modalité
cols_to_object = ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal", "target"]
for col in cols_to_object:
    data[col] = data[col].astype(object)

data.loc[data["sex"] == 0, "sex"] = "Femme"
data.loc[data["sex"] == 1, "sex"] = "Homme"
data.loc[data["cp"] == 1, "cp"] = "Angine stable"
data.loc[data["cp"] == 2, "cp"] = "Angine instable"
data.loc[data["cp"] == 3, "cp"] = "Autres douleurs"
data.loc[data["cp"] == 4, "cp"] = "Asymptomatique"
data.loc[data["fbs"] == 0, "fbs"] = "Inférieur à 120 mg/dl"
data.loc[data["fbs"] == 1, "fbs"] = "Supérieur à 120 mg/dl"
data.loc[data["restecg"] == 0, "restecg"] = "Normal"
data.loc[data["restecg"] == 1, "restecg"] = "Anomalies"
data.loc[data["restecg"] == 2, "restecg"] = "Hypertrophie"
data.loc[data["exang"] == 0, "exang"] = "Non"
data.loc[data["exang"] == 1, "exang"] = "Oui"
data.loc[data["slope"] == 1, "slope"] = "En hausse"
data.loc[data["slope"] == 2, "slope"] = "Stable"
data.loc[data["slope"] == 3, "slope"] = "En baisse"
data.loc[data["ca"] == 0.0, "ca"] = "Absence d'anomalie"
data.loc[data["ca"] == 1.0, "ca"] = "Faible"
data.loc[data["ca"] == 2.0, "ca"] = "Moyen"
data.loc[data["ca"] == 3.0, "ca"] = "Élevé"
data.loc[data["thal"] == 3.0, "thal"] = "Non"
data.loc[data["thal"] == 6.0, "thal"] = "Thalassémie sous contrôle"
data.loc[data["thal"] == 7.0, "thal"] = "Thalassémie instable"
data.loc[data["target"] == 0, "target"] = "Non"
data.loc[data["target"].isin([1, 2, 3, 4]), "target"] = "Oui"
#observer les effectifs 
print (data.target.value_counts())
data.sex.value_counts()
data.cp.value_counts()
data.fbs.value_counts()
#observer les frequences (pct)
print (data.target.value_counts(normalize =True).round (4).mul(100))
data.sex.value_counts(normalize =True).round (4).mul(100)
data.cp.value_counts(normalize =True).round (4).mul(100)
data.fbs.value_counts(normalize =True).round (4).mul(100)

def tableaux(variable, nom_variable):
    effectifs = variable.value_counts()
    pourcentages = variable.value_counts(normalize = True).round(4).mul(100)
    print(pd.concat([effectifs, pourcentages], axis = 1, keys = ['Effectifs', 'Pourcentages (%)'], names = [nom_variable]))

# Application de la fonction pour calculer les effectifs et les pourcentages dans un tableau
tableaux(data.target, "Maladie")
tableaux(data.sex, "Sexe des patients")
tableaux(data.cp, "Douleurs thoraciques")
tableaux(data.fbs, "Glycémie à jeun")

# Statistiques descriptives pour les variables quantitatives
print(data.age.describe().round(2))
print(data.trestbps.describe().round(2))
print(data.chol.describe().round(2))
print(data.thalach.describe().round(2))
print(data.oldpeak.describe().round(2))

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

# Création d'une fonction pour créer un diagramme à barres 
def diagramme_barres(variable, palette_couleurs, titre_graphique, titre_abcisses):
    sns.countplot(x = variable, data = data, palette = palette_couleurs, order = variable.value_counts(ascending = True).index)
    plt.title(titre_graphique, fontweight = "bold")
    plt.xlabel(titre_abcisses)
    plt.ylabel("Effectifs")
    plt.show()

# Application de la fonction
diagramme_barres(data.target, "bwr_r", "Répartition des patients selon la présence d'une maladie cardiovasculaire", "Présence d'une maladie cardiovasculaire")
diagramme_barres(data.sex, ("#2a9d8f", "#e9c46a"), "Répartition des patients selon le sexe", "Sexe")
diagramme_barres(data.cp, "YlOrRd_r", "Répartition des patients selon la présence d'une angine de poitrine", "Angine de poitrine")
diagramme_barres(data.fbs, "coolwarm_r", "Répartition des patients selon la glycémie à jeun", "Glycémie à jeun")

# Statistiques descriptives pour les variables quantitatives
print(data.age.describe().round(2))
print(data.trestbps.describe().round(2))
print(data.chol.describe().round(2))
print(data.thalach.describe().round(2))
print(data.oldpeak.describe().round(2))