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

# Création d'une fonction pour créer un histogramme
def histogramme(variable, couleur, titre_graphique, titre_abcisse):
    sns.histplot(x = variable, data = data, bins = 9, kde = True, color = couleur)
    plt.title(titre_graphique, fontsize = 13, fontweight = "bold")
    plt.xlabel(titre_abcisse, fontsize = 12)
    plt.ylabel("Effectifs", fontsize = 12)
    plt.show()

# Application de la fonction
histogramme("age", "green", "Répartition des patients selon la variable Age", "Age")
histogramme("trestbps", "darkred", "Répartition des patients selon la tension artérielle au repos", "Tension artérielle au repos (mmHg)")
histogramme("chol", "goldenrod", "Répartition des patients selon le taux de cholestérol", "Cholestérol (mg/dl)")
histogramme("thalach", "rosybrown", "Répartition des patients selon la fréquence cardiaque \n maximale atteinte", "Fréquence cardiaque maximale atteinte")

# Création d'une fonction pour créer un diagramme à barres croisées
def diagramme_barres_croisees(variable_x, variable_y, couleur, titre_legende, titre_graphique, titre_x):
    sns.countplot(x = variable_x, data = data, hue = variable_y, palette = couleur, order = variable_x.value_counts(ascending = True).index)
    plt.legend(title = titre_legende)
    plt.title(titre_graphique, fontsize = 13, fontweight = "bold")
    plt.xlabel(titre_x, fontsize = 12)
    plt.ylabel("Effectifs", fontsize = 12)
    plt.show()

# Application de la fonction
diagramme_barres_croisees(data.sex, data.target, "Set2", "Maladie cardiovasculaire", "Répartition des patients selon le sexe et la présence de \n maladie cardiovasculaire", "Sexe")
diagramme_barres_croisees(data.cp, data.target, "RdYlGn_r", "Maladie cardiovasculaire", "Répartition des patients selon la présence de douleurs thoraciques \n et la présence de maladie cardiovasculaire", "Sexe")
diagramme_barres_croisees(data.fbs, data.target, "Set1", "Maladie cardiovasculaire", "Répartition des patients selon la glycémie à jeun \n et la présence de maladie cardiovasculaire", "Glycémie à jeun")

# Création d'une fonction pour créer des boîtes à moustaches
def boites_moustaches(variable_x, variable_y, couleur, titre, titre_x, titre_y):
    sns.boxplot(x = variable_x, y = variable_y, data = data, palette = couleur)
    plt.title(titre, fontweight = "bold", fontsize = 15)
    plt.xlabel(titre_x, fontsize = 13)
    plt.ylabel(titre_y, fontsize = 13)
    plt.show()

# Application de la fonction
boites_moustaches(data.target, data.age, couleur = "seismic", titre = "Boîtes à moustaches de la population selon l'âge et la \n présence d'une maladie cardiovasculaire", titre_x = "Présence d'une maladie cardiovasculaire", titre_y = "Age")
boites_moustaches(data.target, data.trestbps, couleur = "seismic", titre = "Boîtes à moustaches de la population selon la tension artérielle au \n repos (mmHg) et la présence d'une maladie cardiovasculaire", titre_x = "Présence d'une maladie cardiovasculaire", titre_y = "Tension artérielle au repos (mmHg)")
boites_moustaches(data.target, data.chol, couleur = "seismic", titre = "Boîtes à moustaches de la population selon le taux de cholestérol \n (mg/dl) et la présence d'une maladie cardiovasculaire", titre_x = "Présence d'une maladie cardiovasculaire", titre_y = "Taux de cholestérol (mg/dl)")

#Analyses bivariées 
pd.crosstab(data.sex,data.target, margins=True, normalize='index').round(4)*100
pd.crosstab(data.sex,data.target, margins=True)
pd.crosstab(data.cp, data.target, margins = True)
pd.crosstab(data.fbs, data.target, margins = True)

# test du chi 2
# H0 : Les deux variables sont indépendantes (si p-value > 0,05)
# H1 : Les deux variables sont dependantes (si p-value < 0,05)

from scipy.stats import chi2_contingency
chi2_contingency(pd.crosstab(data.sex, data.target))[1] # p-value = 0.000002945 < 0.05
chi2_contingency(pd.crosstab(data.cp, data.target))[1] # p-value < 0.05
chi2_contingency(pd.crosstab(data.fbs, data.target))[1] # p-value > 0.05

# Test de Shapiro-Wilk (quantitatif VS qualitatif)
# H0 : L'échantillon suit une distribution normale (si p-value > 0,05)
# H1 : L'échantillon ne suit pas une distribution normale (si p-value < 0,05)
from scipy.stats import shapiro
shapiro(data[data["target"] == "Oui"].age) # H1
shapiro(data[data["target"] == "Oui"].trestbps) # H1
shapiro(data[data["target"] == "Oui"].chol) # H0

# Reformatage de la colonne target
data2 = data.copy(deep = True)
data2['target'][data2['target'] == "Non"] = 0
data2['target'][data2['target'] == "Oui"] = 1
data2['target'] = data2['target'].astype('int64')

# Test de Mann-Whitney (non-paramétrique)
# H0 : Il n'y a pas de différence significative entre la moyenne des deux variables (si p-value > 0,05)
# H1 : Il y a une différence significative entre la moyenne des deux variables (si p-value < 0,05)
from scipy.stats import mannwhitneyu
mannwhitneyu(data2.age, data2.target, alternative = "two-sided") # H1
mannwhitneyu(data2.trestbps, data2.target, alternative = "two-sided") # H1 (difference non due a l'echantillonnage donc la tension et le status de la maladie sont bien liés)

# Test de Student (paramétrique)
# H0 : Il n'y a pas de différence significative entre la moyenne des deux variables (si p-value > 0,05)
# H1 : Il y a une différence significative entre la moyenne des deux variables (si p-value < 0,05) l
from scipy.stats import ttest_ind
ttest_ind(data2.chol, data2.target) # H1 le taux de cholesterol a bien un impact sur la maladie 

# Transformation des variables qualitatives en variables binaires
data3 = pd.get_dummies(data, drop_first = True)