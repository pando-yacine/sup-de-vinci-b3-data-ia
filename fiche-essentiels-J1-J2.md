# Fiche essentiels — J1 + J2 (B3 Data & IA)

> Le socle à avoir en tête pour le J3, le projet, la soutenance, et tout entretien Data. Une page, vous lisez en 5 minutes.

---

## J1 — Big Data (le socle données)

### Les 5V (le cadre Big Data)
- **Volume** : on parle de To/Po — ça ne tient pas en RAM d'une machine.
- **Vélocité** : vitesse de génération et de traitement (streaming temps réel).
- **Variété** : formats hétérogènes (CSV, JSON, images, texte, vidéo).
- **Véracité** : qualité / fiabilité des données.
- **Valeur** : la donnée doit produire une décision utile.

### Pipeline data / ETL (Extract → Transform → Load)
Chaîne classique : **collecte** (sources) → **nettoyage** → **transformation/enrichissement** → **stockage** → **analyse → visualisation**.
> *Le projet fil rouge est un mini-ETL. J3 attaque les 2 derniers maillons (analyse + viz).*

### Spark — pourquoi & comment
- **Quoi** : moteur de traitement de données **distribué** (sur plusieurs machines) et **en mémoire**.
- **Pourquoi** : **10-100× plus rapide** que MapReduce/Hadoop (qui écrivait sur disque entre chaque étape).
- **API** : `DataFrame` Spark ≈ Pandas, mais réparti sur un cluster (`groupBy`, `filter`, `join`, `agg`).

### Lazy evaluation (LE concept Spark)
- Les **transformations** (`filter`, `map`, `groupBy`, `join`) s'accumulent dans un **DAG** (graphe d'opérations) — **rien n'est calculé**.
- Tout s'exécute seulement à une **action** : `show()`, `collect()`, `count()`, `write()`.
- Avantage : Spark peut **optimiser le plan** avant d'exécuter (Catalyst).

### Transformation vs Action
| Type | Exemples | Déclenche le calcul ? |
|---|---|---|
| **Transformation** | `.filter()`, `.map()`, `.groupBy()`, `.join()` | ❌ Non |
| **Action** | `.show()`, `.collect()`, `.count()`, `.write()` | ✅ Oui |

### Scalabilité horizontale vs verticale
- **Verticale** (scale-up) : grossir 1 machine (plus de RAM/CPU). Plafond physique, panne = tout perdu.
- **Horizontale** (scale-out) : **ajouter des machines**. Linéaire, tolérant aux pannes. C'est ce que font Hadoop/Spark/NoSQL.

### Notions à connaître (culture)
- **Hadoop** (2006) : 1er framework Big Data — HDFS (stockage), MapReduce (traitement), YARN (ressources).
- **HDFS** : système de fichiers distribué, blocs répliqués 3× (tolérance aux pannes).
- **MapReduce** : modèle Map (en parallèle) → Reduce (agrégation). Supplanté par Spark.
- **DAG** : la représentation interne du plan d'exécution Spark.

---

## J2 — Machine Learning (le modèle)

### Les 3 familles
| Famille | A-t-on `y` ? | Sous-types | Exemples |
|---|---|---|---|
| **Supervisé** | ✅ Oui | **Régression** (`y` continu) · **Classification** (`y` catégoriel) | Prix immobilier · Spam ou non |
| **Non supervisé** | ❌ Non | **Clustering** · **Réduction de dimension** | Segmentation clients · PCA |
| *(Renforcement)* | récompense | RL | Jeux, robotique — pour la suite |

### Vocabulaire (à maîtriser)
- **X** = les **features** (colonnes d'entrée : surface, nb pièces…).
- **y** = la **target / cible** (ce qu'on prédit : le prix).
- Le modèle apprend `f(X) → y`. **Les bonnes features font 80 % de la perf.**

### Le pipeline ML standard (squelette de tous vos projets)
1. **Data brute** → 2. **EDA** (explorer) → 3. **Preprocessing** (nettoyer, encoder, scaler) → 4. **Split train/val/test** → 5. **Feature engineering** → 6. **Baseline simple** → 7. **Train** (`.fit`) → 8. **Eval** (sur val) → 9. **Itération** → 10. **Test final** (1 seule fois).

### Pipeline sklearn (l'objet — évite le leakage)
Un seul objet qui chaîne **preprocessing + modèle** :
```python
pipe = Pipeline([
    ("prep", ColumnTransformer(...)),   # ex : OneHotEncoder + StandardScaler
    ("model", RandomForestRegressor())
])
pipe.fit(X_train, y_train)
pipe.predict(X_new)
```
> Avantage clé : le preprocessing est appris **uniquement sur le train** → pas de **data leakage**.

### Split train / val / test
- **Train** : pour `.fit()`.
- **Val** : pour comparer modèles / régler les hyperparamètres.
- **Test** : ouvert **UNE seule fois à la fin** pour l'estimation honnête de la perf.
> Si on optimise sur le test, on triche → score gonflé qui ne tient pas en prod.

### Data leakage — 3 cas classiques (à reconnaître)
1. **Scaling avant le split** (statistiques du test fuient dans le train).
2. **Une feature contient indirectement la cible** (ex. : `revenu_annuel_après_crédit` quand on prédit l'accord du crédit).
3. **Random split sur des données temporelles** → utiliser un **temporal split** obligatoirement.

### Cross-validation + GridSearchCV
- **CV k-fold** : on découpe le train en k plis, on entraîne sur k-1 et on valide sur 1, k fois → score **stable** (pas un coup de chance).
- **GridSearchCV** : teste toutes les combinaisons d'hyperparamètres en CV, garde la meilleure.

### Modèles courants à connaître
| Famille | Modèles |
|---|---|
| **Linéaires** | LinearRegression, LogisticRegression, Ridge, Lasso |
| **Arbres / Ensemble** | RandomForest, GradientBoosting, **XGBoost, LightGBM, CatBoost** |
| **Réseaux** | MLP (sklearn), pour la suite : PyTorch / TensorFlow |
| **Clustering** | K-means, DBSCAN |

### Métriques (le bon choix selon le problème)

**Régression** — toujours montrer le trio :
- **MAE** : erreur moyenne absolue, dans l'unité de y. Lisible, robuste aux outliers.
- **RMSE** : pénalise les **grosses** erreurs. Si `RMSE >> MAE` → vous avez des outliers.
- **R²** : part de variance expliquée (1 = parfait, 0 = on prédit la moyenne). Sans unité.

**Classification** — ⚠️ accuracy trompeuse sur classes déséquilibrées :
- **Accuracy** : (% correct). OK si classes équilibrées. **Trompeuse sinon** (99 % d'accuracy sur fraude à 0,1 % ≠ bon modèle).
- **Precision** = TP/(TP+FP) → « parmi mes prédictions positives, combien sont vraies ? » (importe si FP coûte cher).
- **Recall** = TP/(TP+FN) → « parmi les vrais positifs, combien je trouve ? » (importe si FN coûte cher).
- **F1** = moyenne harmonique de precision et recall. Bon compromis sur classes déséquilibrées.
- **Confusion matrix** : pour voir **quels types d'erreurs** on fait.
- **ROC-AUC** : classes équilibrées · **PR-AUC** : classes très déséquilibrées (préférer).

### Overfitting / Underfitting
- **Overfitting** : très bon sur train, mauvais sur val/test → le modèle a **appris par cœur**. Solutions : plus de données, moins de features, régularisation.
- **Underfitting** : mauvais partout → modèle **trop simple**. Solutions : modèle plus puissant, plus de features.

### Règle d'or : **Baseline d'abord**
Une `LinearRegression` ou un `RandomForest` de base avant XGBoost mal réglé. *« Tu ne sais pas si ton XGBoost est bon tant que tu ne sais pas ce que fait la régression linéaire. »*

### 🔑 Le pont vers J3 — Exporter le modèle
```python
import joblib
joblib.dump(pipeline, "model.pkl")     # à la fin du notebook J2
model = joblib.load("model.pkl")       # rechargé dans l'API FastAPI J3
```
> **Votre modèle de J2 n'est pas un notebook — c'est un `model.pkl` qu'on sert dans l'API.**

---

## Pour la suite (mini-anti-sèche entretien)

- **« Présente ton projet en 1 min »** → dataset choisi (et pourquoi) · question prédictive (régression/classif) · pipeline (preprocess + modèle) · métrique principale + score · limites/biais.
- **« Pourquoi cette métrique ? »** → relier au **coût asymétrique** des erreurs (un FN/FP coûte-t-il plus cher ?).
- **« Comment tu sais que ton modèle est bon ? »** → score sur le **test** (pas le train), comparaison à une **baseline**, cross-validation pour la **stabilité**.
- **« Le plus gros risque dans ton pipeline ? »** → souvent le **leakage** (cherchez où) ou un **biais du dataset**.
- **« Avec plus de temps, tu ferais quoi ? »** → feature engineering, modèle plus avancé, plus de données, monitoring en prod.
