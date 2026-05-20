# J2 — Machine Learning Scikit-learn

> 21 mai 2026 · Sup de Vinci Nantes · 7h (9h15 — 17h15)

## Thème de la journée

Du data au modèle ML : 3 familles (régression / classification / clustering), pipeline ML standard avec Scikit-learn, métriques + pièges (overfitting, data leakage, temporal CV), cas réel hippique.

## Sommaire des ressources

- **[Quiz éclair Spark](quiz-eclair-spark-5Q.md)** — 5 questions de récap J1 (utilisé en début de matinée sur Qiplim, 5 min chrono)

## Ateliers

- **[Atelier 1 — Baseline régression (California Housing)](ateliers/atelier1-baseline-immobilier.ipynb)** (1h30)
  - Pipeline complet sur 8 étapes : load → EDA → preprocessing → train/val/test split → `ColumnTransformer` → `LinearRegression` → score R² → scatter pred vs réel
- **[Atelier 2 — CV + 3 modèles + GridSearch](ateliers/atelier2-cv-grid-3modeles.ipynb)** (1h30)
  - Feature engineering, cross-validation 5-fold, comparaison LinearRegression / RandomForest / GradientBoosting, `GridSearchCV`, évaluation finale sur test, bonus `feature_importances_`

## Comment ouvrir les notebooks sur Colab

Clic droit sur le `.ipynb` → "Open with" → "Colab".

Ou directement :

```
https://colab.research.google.com/github/pando-yacine/sup-de-vinci-b3-data-ia/blob/main/J2/ateliers/atelier1-baseline-immobilier.ipynb
https://colab.research.google.com/github/pando-yacine/sup-de-vinci-b3-data-ia/blob/main/J2/ateliers/atelier2-cv-grid-3modeles.ipynb
```

## Livrable J2 — projet fil rouge

Sur **votre dataset** (choisi en fin de J1) :
- 1 modèle baseline ML qui tourne (régression linéaire, logistique, ou Random Forest)
- 1 métrique de performance affichée et commentée
- EDA propre, split train/val/test correct, pas de leakage
