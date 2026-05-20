---
title: "B3 Data & IA — Fiche algorithmes ML"
subtitle: "Référence formateur — tous les algos cités en J2"
---

<div class="cover">
<h1>Fiche algorithmes ML</h1>
<div class="subtitle">B3 Data &amp; IA — Référence formateur<br/>Tous les modèles cités en J2 expliqués un par un</div>
<div class="meta">
Yacine Arhaliass · Pando Studio · mai 2026<br/>
<em>Pour comprendre, choisir et défendre un choix d'algo</em>
</div>
</div>

# Comment utiliser cette fiche

Pour chaque algo :

- **Type** : famille ML
- **Idée intuitive** : analogie / fonctionnement en 2 lignes
- **Quand l'utiliser** : cas pratiques
- **Hyperparamètres clés** : ce qu'il faut connaître
- **Pièges** : ce qui peut foirer
- **Code rapide** : 1-3 lignes pour démarrer

Si on te demande en classe *"Quel algo pour mon problème ?"*, tu retrouves ici en 30 secondes.

---

# 🟢 Régression — modèles linéaires

## LinearRegression — la régression linéaire ordinaire

**Type** : régression supervisée linéaire (Ordinary Least Squares — OLS)

**Idée intuitive** : trouve la **droite** (ou hyperplan en N dimensions) qui passe au plus près de tous les points. Minimise la somme des carrés des erreurs entre prédit et réel.

> *"y = a₁·x₁ + a₂·x₂ + ... + b. C'est le HelloWorld du ML."*

**Quand l'utiliser** :
- **TOUJOURS en premier** comme baseline. Si ton XGBoost ne bat pas la régression linéaire de >5%, il ne sert à rien.
- Quand les relations sont à peu près linéaires (prix immobilier vs surface)
- Quand tu veux **interpréter** les coefficients (ce coefficient veut dire que +1 m² ajoute +3000€)

**Hyperparamètres clés** : aucun en pratique. C'est le point fort.

**Pièges** :
- **Sensible aux outliers** (1 valeur extrême peut dévier la droite)
- **Suppose linéarité** : sur une relation y = x², la régression linéaire foire
- **Multicollinéarité** (features très corrélées entre elles) → coefficients instables

**Code** :
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X_train, y_train)
print(model.score(X_val, y_val))  # R²
```

---

## Ridge — régression linéaire régularisée L2

**Type** : régression linéaire avec **pénalité L2** (somme des carrés des coefficients)

**Idée intuitive** : même droite que LinearRegression, mais on **pénalise les gros coefficients**. Résultat : la droite est moins sensible aux outliers et à la multicollinéarité.

> *"Mêmes voitures que la LinearRegression, mais avec ceinture de sécurité."*

**Quand l'utiliser** :
- Quand tu as **beaucoup de features** dont certaines corrélées
- Quand LinearRegression overfit (gros écart train vs val)
- Quand tu veux garder toutes les features mais avec des coefficients raisonnables

**Hyperparamètres clés** :
- `alpha` (force de régularisation) : 0.01 à 100. Plus haut = plus de régularisation. Trouve la bonne valeur avec `GridSearchCV`.

**Pièges** :
- **Ne sélectionne pas les features** (les garde toutes, juste avec petits coefficients) — pour ça il faut Lasso
- `alpha` mal choisi → underfitting (trop régularisé) ou inutile (alpha trop bas)

**Code** :
```python
from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0).fit(X_train, y_train)
```

---

## Lasso — régression linéaire régularisée L1

**Type** : régression linéaire avec **pénalité L1** (somme des valeurs absolues des coefficients)

**Idée intuitive** : comme Ridge mais avec une propriété magique : la pénalité L1 **force certains coefficients à exactement zéro**. Donc Lasso fait de la **sélection de features automatique**.

> *"Lasso = Ridge + sélection automatique des features importantes. Les coefficients zéro = features virées."*

**Quand l'utiliser** :
- Quand tu as **beaucoup de features et tu veux savoir lesquelles comptent**
- Pour des modèles **parcimonieux** (peu de features actives = interprétable)
- En génomique ou texte (milliers de features)

**Hyperparamètres clés** :
- `alpha` : 0.001 à 10. Plus haut = plus de features virées.

**Pièges** :
- **Si features très corrélées**, Lasso choisit arbitrairement une seule des deux
- Sur dataset petit → instabilité (un nouveau split peut changer les features sélectionnées)

**Code** :
```python
from sklearn.linear_model import Lasso
model = Lasso(alpha=0.1).fit(X_train, y_train)
features_actives = X.columns[model.coef_ != 0]  # les features gardées
```

---

## ElasticNet (mention bonus)

**Type** : combine Ridge + Lasso (pénalité L1 + L2)

**Idée intuitive** : compromis entre Ridge (stable mais garde tout) et Lasso (sélectionne mais instable sur features corrélées).

**Quand l'utiliser** : si tu hésites entre Ridge et Lasso → ElasticNet avec `l1_ratio=0.5`.

---

# 🟢 Classification — modèle linéaire

## LogisticRegression — la régression logistique

**Type** : classification supervisée linéaire (malgré son nom "régression")

**Idée intuitive** : trouve la **frontière linéaire** qui sépare les classes. Sortie : une **probabilité** (0 à 1) qu'un point appartienne à la classe positive.

> *"Comme LinearRegression mais avec une fonction sigmoïde qui écrase la sortie entre 0 et 1. C'est la classification linéaire de référence."*

**Pourquoi ça s'appelle 'régression' alors que c'est de la classification ?**
- Historique : la méthode prédit la **log-cote** (logit), qui est une valeur continue → c'est techniquement une régression sous le capot
- En pratique : on l'utilise pour classifier
- Mauvais terme, mais resté

**Quand l'utiliser** :
- **TOUJOURS en premier** pour la classification (baseline)
- Quand tu veux des **probabilités calibrées** (pas juste un yes/no)
- Quand tu veux interpréter les coefficients

**Hyperparamètres clés** :
- `C` (inverse de la régularisation) : 0.01 à 100. **Petit C = plus de régularisation** (attention au sens inversé !).
- `penalty` : `l1` (Lasso-like, sélection features), `l2` (Ridge-like, défaut), `elasticnet`
- `class_weight='balanced'` : crucial sur classes déséquilibrées

**Pièges** :
- Le nom : ce n'est PAS de la régression au sens "prédire un nombre"
- Sur problème non linéaire → frontière linéaire = limitée
- Sur classes très déséquilibrées sans `class_weight='balanced'` → modèle qui prédit toujours la majoritaire

**Code** :
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(C=1.0, class_weight='balanced').fit(X_train, y_train)
proba = model.predict_proba(X_val)  # probabilités
```

---

# 🌳 Arbres et ensembles — régression ET classification

## DecisionTreeRegressor / DecisionTreeClassifier

**Type** : arbre de décision (supervisé)

**Idée intuitive** : suite de **questions oui/non** sur les features qui découpent l'espace en zones. À chaque feuille, on prédit la valeur (ou classe) moyenne des points qui y sont arrivés.

> *"Comme un akinator. À chaque nœud, une question. À la fin de la branche, une prédiction."*

**Quand l'utiliser** :
- Quand tu veux **interpréter** (visualisable, explicable au métier)
- Quand les **relations sont non linéaires** ou avec des seuils nets
- Comme **brique de base** pour Random Forest et Gradient Boosting (jamais seul en prod)

**Hyperparamètres clés** :
- `max_depth` : profondeur max de l'arbre (3-20). **C'est l'hyperparam le plus important**.
- `min_samples_split` : nb min de points pour faire un split (10-100)
- `min_samples_leaf` : nb min par feuille (5-50)

**Pièges** :
- **Overfitting** garanti si tu laisses pousser l'arbre à fond (`max_depth=None`)
- **Instable** : un point différent dans train peut changer tout l'arbre
- **Pas top en perf** seul → c'est pour ça qu'on fait Random Forest derrière

**Code** :
```python
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(max_depth=5).fit(X_train, y_train)
```

---

## RandomForestRegressor / RandomForestClassifier

**Type** : ensemble d'arbres (bagging)

**Idée intuitive** : on construit **100 arbres** sur des échantillons aléatoires (bootstrap) des données, avec des sous-ensembles aléatoires de features à chaque split. On fait **voter** ou **moyenner** les prédictions.

> *"Un seul arbre est instable. 100 arbres qui votent = robuste. C'est l'effet 'sagesse de la foule' appliqué au ML."*

**Quand l'utiliser** :
- **Excellent baseline** sur tabular (souvent meilleur que régression linéaire d'office)
- Quand tu veux peu d'effort de tuning (marche bien avec params par défaut)
- Quand tu veux la **feature importance** intégrée

**Hyperparamètres clés** :
- `n_estimators` : nb d'arbres (100-500). Plus = meilleur mais plus lent.
- `max_depth` : 10-20 (laisser `None` est risqué)
- `max_features` : nb de features par split (`sqrt` pour classification, `1/3` pour régression)
- `n_jobs=-1` : parallélise sur tous les cœurs

**Pièges** :
- **Gros modèle en mémoire** (100 arbres × N nœuds chacun)
- **Pas adapté aux données très haute dimension** (texte, images brutes)
- Plus lent que XGBoost en pratique

**Code** :
```python
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=200, max_depth=15, n_jobs=-1).fit(X_train, y_train)
importances = model.feature_importances_  # bar chart magique
```

---

## GradientBoostingRegressor / GradientBoostingClassifier

**Type** : ensemble d'arbres (boosting)

**Idée intuitive** : on construit des arbres **séquentiellement**, chaque arbre apprend les **erreurs résiduelles** des arbres précédents. À la fin, on additionne les prédictions de tous les arbres pondérées par un learning rate.

> *"Random Forest = arbres en parallèle qui votent. Gradient Boosting = arbres en série qui se corrigent. C'est la différence."*

**Quand l'utiliser** :
- Quand RandomForest atteint un plateau → souvent Gradient Boosting passe au-dessus
- Sur **tabular** : c'est la famille qui gagne presque toutes les compétitions Kaggle
- Quand la **performance brute** est l'objectif

**Hyperparamètres clés** :
- `learning_rate` : 0.01 à 0.3. Petit = plus précis mais plus long.
- `n_estimators` : 100-500. Couplé au learning rate (petit lr → plus d'estimators)
- `max_depth` : 3-10 (arbres peu profonds, contrairement à Random Forest)
- `subsample` : 0.8 (utilise 80% des données par arbre) — régularise

**Pièges** :
- **Sensible au tuning** (vs RandomForest qui marche d'office)
- **Plus lent** à entraîner que Random Forest
- **Overfit** facilement si learning_rate trop grand + trop d'estimators
- → En pratique, utiliser **XGBoost / LightGBM / CatBoost** plutôt que celui de sklearn (10-100x plus rapides)

**Code** :
```python
from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.05, max_depth=5).fit(X_train, y_train)
```

---

## XGBoost — la référence sur tabular

**Type** : gradient boosting optimisé (eXtreme Gradient Boosting)

**Idée intuitive** : Gradient Boosting réécrit en C++ avec **régularisation intégrée** + parallélisation. Souvent meilleure perf + 10x plus rapide que `sklearn.GradientBoosting`.

> *"Le couteau suisse de Kaggle. Si tu fais du tabular et que tu veux gagner, tu commences par XGBoost."*

**Quand l'utiliser** :
- Tabular > 1000 lignes
- Quand RandomForest atteint un plateau
- Compétitions, projets pro avec budget

**Hyperparamètres clés** :
- `learning_rate` : 0.01 à 0.3
- `n_estimators` : 100-1000
- `max_depth` : 4-8
- `subsample`, `colsample_bytree` : 0.7-0.9
- `reg_alpha` (L1), `reg_lambda` (L2) : régularisation

**Pièges** :
- **Beaucoup de hyperparams à tuner** (utiliser Optuna ou GridSearch progressif)
- **Pas dans sklearn par défaut** (`pip install xgboost`)
- **Mauvaise gestion des catégorielles natives** → utiliser CatBoost dans ce cas

**Code** :
```python
from xgboost import XGBRegressor
model = XGBRegressor(n_estimators=200, learning_rate=0.05, max_depth=6).fit(X_train, y_train)
```

---

## LightGBM — XGBoost mais plus rapide

**Type** : gradient boosting optimisé (Microsoft)

**Idée intuitive** : XGBoost mais avec une stratégie d'arbres "leaf-wise" (vs "level-wise") qui rend l'entraînement **5-10x plus rapide**, avec souvent une perf équivalente ou meilleure.

> *"LightGBM = XGBoost moderne. Si tu débutes en boosting, commence par LightGBM."*

**Quand l'utiliser** :
- Mêmes cas que XGBoost
- Surtout sur **gros datasets** (> 100k lignes) — l'écart de vitesse compte
- Quand tu as **beaucoup de features catégorielles** (LightGBM les gère bien)

**Hyperparamètres clés** : similaires à XGBoost.

**Pièges** :
- **Overfit plus facilement** que XGBoost sur petits datasets (< 10k lignes) — il faut limiter `num_leaves`
- API légèrement différente de sklearn (mais sklearn-compatible)

**Code** :
```python
from lightgbm import LGBMRegressor
model = LGBMRegressor(n_estimators=200, learning_rate=0.05, num_leaves=31).fit(X_train, y_train)
```

---

## CatBoost — gradient boosting catégoriel-friendly

**Type** : gradient boosting optimisé (Yandex) avec gestion native des catégorielles

**Idée intuitive** : LightGBM mais avec une **gestion intelligente des features catégorielles** (pas besoin d'OneHotEncoder en amont). Les variables catégorielles à 1000+ valeurs (city, user_id) sont natives.

> *"CatBoost = Boosting pour la vraie vie. Tu lui balances tes catégorielles brutes, il se débrouille."*

**Quand l'utiliser** :
- Données avec **beaucoup de features catégorielles**
- Quand tu veux **éviter le OneHot** qui explose la dimension
- Le cas hippique du J2 (29 features dont jockey, hippodrome, ferrure) → CatBoost utilisé

**Hyperparamètres clés** :
- `iterations` : 100-1000
- `learning_rate` : 0.01-0.1
- `depth` : 4-10
- `cat_features` : liste des indices/noms des colonnes catégorielles

**Pièges** :
- Un peu plus lent que LightGBM
- Documentation moins riche que XGBoost

**Code** :
```python
from catboost import CatBoostRegressor
model = CatBoostRegressor(iterations=500, learning_rate=0.05, depth=6,
                          cat_features=['jockey', 'hippodrome']).fit(X_train, y_train, verbose=False)
```

---

# 🧠 Réseaux de neurones

## MLPRegressor / MLPClassifier

**Type** : Multi-Layer Perceptron (réseau de neurones feed-forward)

**Idée intuitive** : couches de **neurones connectés**. Chaque neurone reçoit des entrées pondérées, applique une activation non linéaire (ReLU, tanh), passe au neurone suivant. On apprend les poids par rétropropagation.

> *"Plusieurs couches de régressions logistiques empilées et entraînées ensemble. C'est le 'shallow DL' de sklearn."*

**Quand l'utiliser** :
- Pour **expérimenter le DL** dans sklearn sans installer PyTorch/TF
- Sur tabular **complexe non linéaire** où Random Forest plateau
- En pratique : rarement la meilleure option sur tabular (les boostings sont meilleurs)

**Hyperparamètres clés** :
- `hidden_layer_sizes` : ex `(100, 50)` = 2 couches de 100 puis 50 neurones
- `activation` : `relu` (défaut), `tanh`, `logistic`
- `learning_rate_init` : 0.001
- `max_iter` : 200 (souvent insuffisant, augmenter)

**Pièges** :
- **Sensible au scaling** (StandardScaler obligatoire)
- **Lent à entraîner** sur sklearn (pas de GPU)
- **Pas la bonne option** si tu veux du vrai DL → PyTorch ou TensorFlow

**Code** :
```python
from sklearn.neural_network import MLPRegressor
model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=500).fit(X_train_scaled, y_train)
```

---

# 🔵 Clustering — apprentissage non supervisé

## K-means

**Type** : clustering par centroïdes

**Idée intuitive** : tu choisis `k` (nombre de clusters). L'algo place `k` points (centroïdes) au hasard, assigne chaque donnée au centroïde le plus proche, déplace les centroïdes au barycentre de leurs points, répète jusqu'à stabilité.

> *"Imagine k aimants au milieu d'un nuage de billes. Les billes vont vers l'aimant le plus proche. Les aimants se recentrent. Et ainsi de suite jusqu'à équilibre."*

**Quand l'utiliser** :
- Quand tu sais **combien de groupes** tu cherches (segmentation clients en 4 personas par exemple)
- Quand les clusters sont **sphériques** et de **taille similaire**
- Comme **baseline** de clustering

**Hyperparamètres clés** :
- `n_clusters` (k) : à choisir avec la **méthode du coude** (elbow method) ou silhouette score
- `random_state` : fixe pour reproductibilité
- `n_init=10` : nb d'initialisations aléatoires (garder le meilleur)

**Pièges** :
- **Tu dois choisir k à l'avance** → contraignant
- **Suppose des clusters sphériques** → foire sur formes allongées (utiliser DBSCAN)
- **Sensible aux outliers** (un outlier déplace le centroïde)
- **Sensible au scaling** : si une feature est en m² et une autre en €, K-means la considère comme "plus importante"

**Code** :
```python
from sklearn.cluster import KMeans
model = KMeans(n_clusters=4, n_init=10, random_state=42).fit(X_scaled)
labels = model.labels_  # 0, 1, 2, 3 pour chaque point
```

---

## DBSCAN — Density-Based Spatial Clustering

**Type** : clustering par densité

**Idée intuitive** : un cluster = une **zone dense** de points. Les points dans des zones denses sont regroupés. Les points dans des zones peu denses sont marqués comme **outliers** (label -1).

> *"Ce ne sont pas les centroïdes qui définissent les clusters, c'est la densité locale. Et bonus : les anomalies sont détectées."*

**Quand l'utiliser** :
- Quand tu **ne sais pas combien de clusters** tu cherches
- Quand les clusters ont des **formes complexes** (anneaux, croissants)
- Quand tu veux **détecter les anomalies** en même temps
- Détection de fraude, segmentation géographique

**Hyperparamètres clés** :
- `eps` (epsilon) : distance max entre 2 points pour être considérés voisins
- `min_samples` : nb min de voisins pour former un cluster (5-20)
- Le tuning de `eps` est **délicat** → utiliser HDBSCAN si possible

**Pièges** :
- **Très sensible à `eps`** : trop petit = tout est outlier. Trop grand = tout est 1 cluster.
- **Mauvais sur clusters de densités très différentes** → utiliser HDBSCAN
- **Lent** sur gros datasets

**Code** :
```python
from sklearn.cluster import DBSCAN
model = DBSCAN(eps=0.5, min_samples=5).fit(X_scaled)
labels = model.labels_  # -1 = outlier
```

---

## HDBSCAN — DBSCAN hiérarchique

**Type** : clustering par densité hiérarchique

**Idée intuitive** : DBSCAN mais **sans avoir besoin de choisir `eps`**. L'algo construit une hiérarchie de clusters à différentes densités et te ressort la meilleure structure.

> *"DBSCAN qui s'auto-règle. Tu lui donnes juste min_cluster_size."*

**Quand l'utiliser** :
- Quand DBSCAN est tentant mais que `eps` est dur à choisir
- Sur clusters de **densités variables** (DBSCAN foire dessus)
- **Recommandé en pratique** plutôt que DBSCAN dans 80% des cas

**Hyperparamètres clés** :
- `min_cluster_size` : taille min d'un cluster (10-50)
- `min_samples` : robustesse aux outliers

**Pièges** :
- Pas dans sklearn natif → `pip install hdbscan`
- **Plus lent** que DBSCAN
- Quelques warnings de paramètres mal réglés à ignorer

**Code** :
```python
import hdbscan
model = hdbscan.HDBSCAN(min_cluster_size=15).fit(X_scaled)
labels = model.labels_  # -1 = outlier
```

---

## GMM — Gaussian Mixture Models

**Type** : clustering probabiliste

**Idée intuitive** : on suppose que les données sont générées par un **mélange de `k` gaussiennes** (cloches). L'algo apprend les paramètres (centre, écart-type, poids) de chaque gaussienne. Chaque point reçoit une **probabilité d'appartenance** à chaque cluster.

> *"K-means version probabiliste + gère les clusters elliptiques (pas seulement sphériques)."*

**Quand l'utiliser** :
- Quand tu veux des **probas d'appartenance** au cluster (pas un label dur)
- Quand les clusters sont **elliptiques** plutôt que sphériques
- En **détection d'anomalie** (probabilité faible = anomalie)

**Hyperparamètres clés** :
- `n_components` : nb de gaussiennes (= nb de clusters)
- `covariance_type` : `full` (ellipses), `diag`, `spherical`, `tied`

**Pièges** :
- **Tu dois choisir n_components** à l'avance (comme K-means)
- **Plus lent** que K-means
- Peut **converger sur des solutions absurdes** si init aléatoire malheureuse

**Code** :
```python
from sklearn.mixture import GaussianMixture
model = GaussianMixture(n_components=4, covariance_type='full', random_state=42).fit(X_scaled)
labels = model.predict(X_scaled)
proba = model.predict_proba(X_scaled)
```

---

# 🔻 Réduction de dimension

## PCA — Principal Component Analysis

**Type** : réduction linéaire

**Idée intuitive** : trouve les **axes (composantes principales)** qui captent le plus de variance dans les données. Tu projettes tes données sur les 2 ou 3 premiers axes → tu visualises ou tu compresses.

> *"Tu prends une boule de pâte 3D, tu trouves le 'profil' (axe long) et tu projettes tout dessus. Tu as une 1D qui résume bien."*

**Quand l'utiliser** :
- **TOUJOURS en premier** pour visualiser un dataset à >3 features
- Pour **compresser** avant un autre modèle (gagner du temps)
- Quand les features sont **corrélées** (PCA les décorrèle)

**Hyperparamètres clés** :
- `n_components` : nb de composantes (2 ou 3 pour viz, plus pour compression)
- Variance expliquée : `model.explained_variance_ratio_.cumsum()` → garder 90-95%

**Pièges** :
- **Linéaire seulement** : ne capte pas les structures courbes (utiliser t-SNE/UMAP)
- **Sensible au scaling** : StandardScaler avant
- Les composantes ne sont pas interprétables directement (mélange des features originales)

**Code** :
```python
from sklearn.decomposition import PCA
model = PCA(n_components=2).fit(X_scaled)
X_2d = model.transform(X_scaled)
print(model.explained_variance_ratio_)  # variance par composante
```

---

## TruncatedSVD — PCA pour matrices creuses

**Type** : réduction linéaire (variante de PCA)

**Idée intuitive** : comme PCA mais sans **centrer** les données. Avantage : marche sur des **matrices creuses** (sparse) comme du TF-IDF en NLP.

> *"PCA = pour matrices denses. TruncatedSVD = pour matrices creuses (texte, recommandation)."*

**Quand l'utiliser** :
- En **NLP** sur du TF-IDF ou Bag-of-Words (matrices avec 99% de zéros)
- En **systèmes de recommandation** (matrice utilisateur × item)
- Au lieu de PCA si tes données sont sparse

**Hyperparamètres clés** :
- `n_components` : 2-500 selon usage

**Pièges** :
- **Peu utilisé en tabular** (PCA suffit)
- Quand on dit "LSA" (Latent Semantic Analysis), c'est TruncatedSVD sur du TF-IDF

**Code** :
```python
from sklearn.decomposition import TruncatedSVD
model = TruncatedSVD(n_components=100).fit(X_sparse)
X_reduced = model.transform(X_sparse)
```

---

## t-SNE — t-distributed Stochastic Neighbor Embedding

**Type** : réduction **non linéaire** pour visualisation

**Idée intuitive** : essaie de **préserver les voisinages locaux** quand on passe de N dimensions à 2D. Les points proches en haute dim restent proches en 2D.

> *"Si en 50D deux points sont voisins, t-SNE essaie de les garder voisins en 2D — même si la projection globale n'a aucun sens géométrique."*

**Quand l'utiliser** :
- **Visualisation** (jolis graphiques à mettre dans des présentations)
- Pour **explorer** la structure d'un dataset à haute dimension
- **Jamais pour compresser** avant un autre modèle (la projection n'a pas de sens linéaire)

**Hyperparamètres clés** :
- `perplexity` : 5-50. Plus haut = vue plus globale. 30 par défaut.
- `n_iter` : 1000 (assez)
- `random_state` : fixe pour reproductibilité

**Pièges** :
- **Lent** sur > 10k points
- **Les distances entre clusters n'ont pas de sens** (seul le voisinage local est préservé)
- **Stochastique** : 2 runs donnent 2 résultats différents → mettre random_state
- **Pas de `.transform()`** sur nouvelles données → re-fit nécessaire

**Code** :
```python
from sklearn.manifold import TSNE
model = TSNE(n_components=2, perplexity=30, random_state=42)
X_2d = model.fit_transform(X_scaled)  # pas de .fit() séparé
```

---

## UMAP — Uniform Manifold Approximation and Projection

**Type** : réduction **non linéaire** moderne

**Idée intuitive** : comme t-SNE mais **plus rapide** et **préserve mieux la structure globale** (les distances entre clusters ont un peu plus de sens).

> *"UMAP = t-SNE 2.0. Si tu utilises t-SNE en 2024+, demande-toi pourquoi tu n'es pas sur UMAP."*

**Quand l'utiliser** :
- Mêmes cas que t-SNE → **préférer UMAP par défaut**
- Sur **gros datasets** (UMAP scale mieux que t-SNE)
- Quand tu veux **transformer de nouvelles données** (UMAP a un `.transform()`)

**Hyperparamètres clés** :
- `n_neighbors` : 5-50. Plus haut = vue plus globale.
- `min_dist` : 0.01-0.5. Petit = clusters plus serrés.
- `n_components` : 2 pour viz, plus pour pré-traitement

**Pièges** :
- Pas dans sklearn natif → `pip install umap-learn`
- **Stochastique** comme t-SNE → mettre `random_state`

**Code** :
```python
import umap
model = umap.UMAP(n_neighbors=15, min_dist=0.1, random_state=42)
X_2d = model.fit_transform(X_scaled)
```

---

## Autoencoders — réduction non linéaire par réseau de neurones

**Type** : réseau de neurones **encodeur-décodeur** (deep learning)

**Idée intuitive** : un réseau de neurones avec une **architecture en sablier**. L'encodeur compresse `X` (N dimensions) en `z` (peu de dimensions, le "bottleneck"). Le décodeur reconstruit `X` depuis `z`. Le modèle apprend à compresser sans perdre trop d'info.

```
X (100D) → [encoder] → z (10D) → [decoder] → X' (100D)
                       ↑
                   Représentation compressée apprise
```

> *"Le PCA est un autoencoder linéaire. L'autoencoder est un PCA avec des activations non linéaires (donc plus puissant)."*

**Quand l'utiliser** :
- Réduction de dimension **non linéaire** sur des données complexes (images, texte)
- **Détection d'anomalie** : reconstruction d'erreur élevée = anomalie
- **Génération** : variante "Variational Autoencoder" (VAE) pour générer de nouvelles données

**Hyperparamètres clés** :
- Architecture (nb de couches, taille du bottleneck)
- `learning_rate`, `epochs` (entraînement deep learning classique)

**Pièges** :
- **Pas dans sklearn** → PyTorch ou TensorFlow nécessaire
- **Nécessite tuning + GPU** pour datasets non triviaux
- **Hors scope B3** → juste mentionner que ça existe

**Code (PyTorch, très simplifié)** :
```python
import torch.nn as nn
class Autoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(100, 50), nn.ReLU(), nn.Linear(50, 10))
        self.decoder = nn.Sequential(nn.Linear(10, 50), nn.ReLU(), nn.Linear(50, 100))
    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z)
```

---

# 🎯 Tableau de synthèse — quel algo pour quel problème ?

## Apprentissage supervisé

| Problème | Premier réflexe | Si plateau | Best in class |
|---|---|---|---|
| **Régression tabular, baseline** | LinearRegression | Ridge / Lasso | XGBoost / LightGBM |
| **Classification binaire** | LogisticRegression | RandomForest | LightGBM / CatBoost |
| **Classification déséquilibrée** | LogisticRegression(class_weight='balanced') | RandomForest + SMOTE | LightGBM + scale_pos_weight |
| **Classification multiclasse** | LogisticRegression(multi_class='multinomial') | RandomForest | LightGBM |
| **Beaucoup de catégorielles** | OneHot + RandomForest | LightGBM | CatBoost |
| **Interprétabilité requise** | LinearRegression / LogisticRegression | DecisionTree (depth ≤5) | LightGBM + SHAP |
| **Tu veux du DL** | MLPRegressor (sklearn) | PyTorch | PyTorch + GPU |

## Apprentissage non supervisé

| Problème | Premier réflexe | Si plateau | Notes |
|---|---|---|---|
| **Segmentation, k connu** | K-means | GMM | Sensible au scaling |
| **Segmentation, k inconnu** | DBSCAN | HDBSCAN | HDBSCAN > DBSCAN en pratique |
| **Détection d'anomalie** | DBSCAN | IsolationForest, GMM | Variante : OneClassSVM |
| **Visualisation 2D** | PCA | UMAP | Toujours commencer par PCA |
| **NLP / texte sparse** | TruncatedSVD | UMAP | Sur TF-IDF par exemple |
| **Compression dim** | PCA | Autoencoder | Si linéarité suffit → PCA |

---

# Phrases-clés à dire à la classe

## Sur le choix d'algo
- *"Toujours commencer par LinearRegression ou LogisticRegression. C'est votre étalon."*
- *"Si XGBoost ne bat pas Random Forest de plus de 2%, gardez RandomForest. Plus simple = plus maintenable."*
- *"En 2026, sur du tabular, ce sera presque toujours LightGBM ou CatBoost en finale."*

## Sur le clustering
- *"K-means si tu connais k. DBSCAN/HDBSCAN sinon. GMM si tu veux des probas."*
- *"Toujours scaler avant clustering."*
- *"Un cluster sans interprétation business = inutile."*

## Sur la réduction de dim
- *"PCA d'abord, toujours. C'est rapide, linéaire, ça donne déjà 80% de l'info."*
- *"t-SNE et UMAP, c'est pour les jolies viz en slide. Pas pour mettre en prod."*
- *"Autoencoders, c'est du deep learning. Hors scope B3. Mention pour culture."*

## Sur la rigueur méthodologique
- *"Le baseline n'est PAS un perdant qu'on jette. C'est la référence qui valide ton ML."*
- *"Si Random Forest et XGBoost donnent le même score, c'est que ton signal vient des features, pas de l'algo."*

---

# Bonus — algorithmes mentionnés mais hors scope J2

Pour ne pas être pris de court si un étudiant les nomme :

- **SVM (Support Vector Machine)** : ancien standard de classification linéaire/non linéaire (avec kernels). Détrôné par les boostings sur tabular. Encore utilisé sur petits datasets et texte.
- **KNN (K-Nearest Neighbors)** : prédit selon les k voisins les plus proches. Simple, baseline, lent en prédiction.
- **Naive Bayes** : classification probabiliste basée sur Bayes + hypothèse d'indépendance des features. Très utilisé en classification de texte.
- **Isolation Forest** : détection d'anomalie par arbres aléatoires. Souvent meilleur que GMM pour ça.
- **XGBoost Survival** : variante de XGBoost pour les analyses de survie (durée avant événement).
- **Prophet (Facebook)** : pour séries temporelles. Hors ML classique, plus statistique.
