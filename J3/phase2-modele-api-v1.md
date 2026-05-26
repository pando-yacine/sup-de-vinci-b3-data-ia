# Phase 2 — Modèle + API V1 déployée

> **But** : transformer votre dataset en un **modèle qui tourne, servi par une API déployée**. À la fin de cette phase, vous avez une **URL publique** sur Hugging Face Spaces qui renvoie une prédiction. Pas encore de front — juste la prédiction en prod.

## Livrable attendu

- `backend/model.pkl` (versionné en Git LFS si > 100 Mo)
- API FastAPI (`backend/main.py`) avec `/api/health` et `/api/predict`
- **Tests unitaires** (`backend/tests/`) qui passent
- **1ère URL publique HF Spaces** qui renvoie une prédiction
- `docs/` mis à jour si la question prédictive a évolué

---

## Étape 2.1 — EDA approfondie & question prédictive validée

L'occasion de **confirmer ou ajuster** la question définie en P1.
- Distributions des features (histos, scatter)
- **Valeurs manquantes** : combien ? on impute ou on drop ?
- **Outliers** (box plots)
- Si classif : **équilibre des classes**
- **Corrélations** entre features (multicolinéarité)
- **Décider et écrire** : cible `y`, features `X` retenues, famille (régression / classif), **métrique principale et pourquoi**.

> Si la question évolue par rapport à P1 → mettre à jour `docs/question-predictive.md` **maintenant**.

---

## Étape 2.2 — Itérer : baseline → comparaison → tuning

**1. Baseline** d'abord — `LinearRegression` / `LogisticRegression`. C'est l'étalon.

**2. Comparer 2-3 modèles** sur le même split, mêmes features, **même métrique** :
```python
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

modeles = {
    "Linear": LinearRegression(),
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
    "GradientBoosting": GradientBoostingRegressor(random_state=42),
}
for nom, m in modeles.items():
    pipe = Pipeline([("prep", preprocessor), ("model", m)])
    s = cross_val_score(pipe, X_train, y_train, scoring="neg_mean_absolute_error", cv=5)
    print(f"{nom}: MAE = {-s.mean():.0f} ± {s.std():.0f}")
```

**3. Tuning** sur le meilleur via `GridSearchCV` ou `RandomizedSearchCV` (plus rapide pour un gros espace d'hyperparamètres).

**4. Évaluation finale** sur le **test set** — UNE SEULE FOIS. C'est votre score à reporter.

> ⚠️ **Anti data-leakage** : tout le preprocessing **dans le `Pipeline` sklearn**. Pas de `scaler.fit_transform` avant le split.

---

## Étape 2.3 — Exporter le modèle

```python
import joblib
joblib.dump(pipeline, "backend/model.pkl")
```

**Pin les versions** dans `backend/requirements.txt` (sinon le `.pkl` peut planter au chargement) :
```
fastapi==0.115.0
uvicorn[standard]==0.30.6
pydantic==2.9.2
scikit-learn==1.5.2
joblib==1.4.2
pandas==2.2.3
```

> **Si `model.pkl > 100 Mo`** : `git lfs install && git lfs track "*.pkl"`. Sinon GitHub râle.

---

## Étape 2.4 — API FastAPI minimale

**Le minimum vital** : `/api/health` + `/api/predict`. Le template Phase 1 a déjà le squelette.

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

model = joblib.load("model.pkl")  # chargé UNE fois au démarrage

class Features(BaseModel):
    surface: float
    pieces: int
    # … vos features

@app.get("/api/health")
def health():
    return {"status": "ok", "model_loaded": True}

@app.post("/api/predict")
def predict(f: Features):
    x = [[f.surface, f.pieces]]  # MÊME ORDRE qu'à l'entraînement
    return {"prediction": float(model.predict(x)[0])}
```

---

## Étape 2.5 — Tests unitaires (pytest)

`backend/tests/test_api.py` :
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict_returns_number():
    r = client.post("/api/predict", json={"surface": 50, "pieces": 3})
    assert r.status_code == 200
    assert isinstance(r.json()["prediction"], (int, float))

def test_predict_rejects_bad_input():
    r = client.post("/api/predict", json={"surface": "vingt"})
    assert r.status_code == 422   # validation Pydantic
```

Lancer : `pytest -q backend/tests`. Ajouter `pytest` dans `requirements.txt`.

---

## Étape 2.6 — Premier déploiement HF Spaces (V1 = API seule)

Voir la fiche dédiée : **`J3/deploy-hugging-face-spaces.md`**. En résumé :
1. Créer un Space Docker sur **huggingface.co/new-space**
2. Ajouter un `Dockerfile` (API only) à la racine du repo
3. `git remote add hf https://huggingface.co/spaces/<user>/<space>` puis `git push hf main`
4. HF builde → **URL publique active en 2-5 min**
5. Tester : `curl https://<user>-<space>.hf.space/api/health`

---

## ✅ Checklist Phase 2

- [ ] EDA documentée (notebook + résumé dans `docs/dataset.md`)
- [ ] Question prédictive **validée** (cible, features, famille, métrique)
- [ ] **Baseline** + comparaison ≥ 2 modèles + tuning
- [ ] Test set évalué **1 seule fois** → score final reporté
- [ ] `Pipeline` sklearn complet (anti-leakage)
- [ ] `model.pkl` exporté + versions pinnées dans `requirements.txt`
- [ ] API FastAPI : `/api/health` + `/api/predict`
- [ ] Tests pytest verts (≥ 3 tests)
- [ ] **URL publique HF Spaces** active
- [ ] Commits propres (`feat:`, `test:`, `chore:`)

---

## Comment piloter Claude Code sur cette phase

- « Lis `docs/question-predictive.md` et `docs/dataset.md`. Propose en **plan mode** le `Pipeline` sklearn (preprocessing + modèle) cohérent avec ces choix. »
- « Génère le code de comparaison (CV 5-fold, 3 modèles, même métrique) dans `notebook.ipynb`. Ne lance pas, montre-moi d'abord. »
- « Dans `backend/main.py`, ajoute `/api/predict` qui charge `model.pkl` au démarrage, valide via Pydantic, renvoie `{"prediction": float}`. **Pas plus.** »
- « Écris 3 tests pytest dans `backend/tests/test_api.py` : health, predict OK, predict invalid. »
- **« Prouve-moi que ça marche »** → lance `pytest` après chaque ajout.

---

## Pièges fréquents

| Piège | Solution |
|---|---|
| `model.pkl` ne se recharge pas en prod | Versions sklearn/joblib **pinnées** dans `requirements.txt` |
| Ordre des features différent à `predict()` | Toujours via le `Pipeline` sklearn (fige l'ordre) |
| Score parfait au train, mauvais en prod | Data leakage → preprocessing **dans** le Pipeline |
| HF Space en erreur après push | Lire les **build logs** dans l'onglet « Logs » du Space |
| Modèle trop gros | Réduire `n_estimators` / `max_depth`, ou Git LFS |
