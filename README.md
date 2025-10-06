# Formation Data Science - Machine Learning avec Python : Prédiction des maladies cardiovasculaires

Ce projet explore les **données du dataset Cleveland Heart Disease** pour analyser et prédire la présence de maladies cardiovasculaires. Le projet comprend :

1. Prétraitement des données
2. Statistiques descriptives
3. Visualisations univariées et bivariées
4. Analyses statistiques
5. Modélisation par régression logistique

---

## 1. Prétraitement des données

- Dataset : [Processed Cleveland Data](https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data)
- Colonnes renommées pour plus de clarté : ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg','thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

- Suppression des valeurs manquantes (`?`) pour les colonnes `ca` et `thal`.
- Recodage des variables qualitatives pour plus de lisibilité.
- Transformation de la colonne `target` en 0 = Non, 1 = Oui pour l’analyse et la modélisation.

---

## 2. Statistiques descriptives

- **Variables qualitatives** : calcul des effectifs et des pourcentages.
- **Variables quantitatives** : moyenne, médiane, écart-type, min, max et quartiles.

**Mathématiquement** :

- Moyenne : \(\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i\)  
- Variance : \(s^2 = \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2\)  
- Écart-type : \(s = \sqrt{s^2}\)  
- Pourcentage : \(\% = \frac{\text{effectif de la catégorie}}{\text{effectif total}} \times 100\)

---

## 3. Visualisations

- **Univariées** :
  - Diagrammes à barres pour les variables qualitatives
  - Histogrammes pour les variables quantitatives
- **Bivariées** :
  - Diagrammes à barres croisées pour comparer deux variables qualitatives
  - Boxplots pour les variables quantitatives selon la variable cible

**Interprétation** : ces visualisations permettent de **détecter les tendances, les distributions et les anomalies** dans les données.

---

## 4. Analyses statistiques

### 4.1 Test du Khi-2 d’indépendance

- **Hypothèses** :
  - \(H_0\) : les deux variables sont indépendantes
  - \(H_1\) : les deux variables sont dépendantes
- **Statistique du test** :  
\[
\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}
\]
où \(O_{ij}\) est l’effectif observé et \(E_{ij}\) l’effectif attendu dans la cellule \(i,j\) du tableau de contingence.

- **Décision** : si \(p\text{-value} < 0.05\), on rejette \(H_0\) et on conclut que les variables sont dépendantes.

**Exemple dans le projet** : `sex` vs `target`, `cp` vs `target`.

---

### 4.2 Test de Shapiro-Wilk

- **Hypothèses** :
  - \(H_0\) : l’échantillon suit une loi normale
  - \(H_1\) : l’échantillon ne suit pas une loi normale
- **Statistique de test** :  
\[
W = \frac{\left(\sum_{i=1}^{n} a_i x_{(i)}\right)^2}{\sum_{i=1}^{n} (x_i - \bar{x})^2}
\]
où \(x_{(i)}\) sont les valeurs triées et \(a_i\) des coefficients constants selon \(n\).

- **Décision** : si \(p\text{-value} < 0.05\), l’échantillon n’est pas normal.

---

### 4.3 Test de Mann-Whitney (non paramétrique)

- **Hypothèses** :
  - \(H_0\) : les distributions des deux groupes sont identiques
  - \(H_1\) : les distributions sont différentes
- **Statistique de test** : somme des rangs d’un des groupes comparée à la distribution sous \(H_0\).

- Utilisé lorsque les conditions de normalité ne sont pas vérifiées.

---

### 4.4 Test de Student (t-test)

- **Hypothèses** :
  - \(H_0\) : les moyennes des deux groupes sont égales
  - \(H_1\) : les moyennes diffèrent
- **Statistique de test** :
\[
t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}
\]
où \(s_1^2, s_2^2\) sont les variances et \(n_1, n_2\) les tailles d’échantillon.

---

## 5. Modélisation : Régression logistique

- Transformation des variables qualitatives en variables binaires (`pd.get_dummies`).
- Séparation des données en **train/test** (80/20).
- Modèle : `LogisticRegression` avec la fonction sigmoïde :
\[
P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X_1 + ... + \beta_p X_p)}}
\]
- **Prédiction** : la probabilité \(P(Y=1)\) est convertie en 0 ou 1 selon un seuil (0.5 par défaut).
- Évaluation : précision, matrice de confusion, courbe ROC, AUC.

**Courbe ROC** : sensibilité (TPR) vs 1-spécificité (FPR)  
\[
\text{AUC} = \int_0^1 TPR(FPR) \, dFPR
\]

---

## 6. Instructions pour reproduire

1. Cloner le dépôt :

```bash
git clone git@github.com:celia-chaouchi/Group3.git


