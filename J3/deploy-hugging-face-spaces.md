# Déployer sur Hugging Face Spaces (Docker — React + FastAPI)

> Fiche **technique** de référence pour les phases 2 (V1 = API seule) et 5 (V2 = API + front unifiés). Free tier, public, auto-deploy depuis Git.

## Pourquoi HF Spaces (pour ce projet)

- **Gratuit** (free tier « CPU basic » : 2 vCPU / 16 Go RAM, suffisant pour un `.pkl` sklearn + FastAPI)
- **ML-friendly** : conçu pour héberger des démos ML — **excellente carte de visite** sur votre CV
- **Auto-deploy** sur `git push` (Git HF) ou sync GitHub
- **URL publique** stable (`https://<user>-<space>.hf.space`)
- **Pas de carte bleue** à donner pour démarrer

---

## Pré-requis

- Un **compte Hugging Face** (gratuit, huggingface.co)
- Le `huggingface-cli` installé : `pip install huggingface_hub`
- Authentifié : `huggingface-cli login` (token créé dans Settings → Access Tokens, type **write**)

---

## Architecture (toujours la même)

1 Space Docker, port 7860 (défaut HF), qui contient :
- **V1 (fin de Phase 2)** : `backend/` seul, FastAPI sert `/api/...`
- **V2 (fin de Phase 5)** : `backend/` + `frontend/dist/` buildé en stage Docker, FastAPI sert l'API **ET** le front

> ⚠️ **Port 7860** est la convention HF Spaces. Adapter le `uvicorn ... --port 7860` (et `EXPOSE 7860` dans le Dockerfile).

---

## Étape 1 — Créer un Space

**Option UI (recommandée la première fois)** : https://huggingface.co/new-space
- **Owner** : votre user/orga
- **Name** : `b3-data-ia-<votre-projet>` (sera l'URL)
- **License** : `mit` (libre)
- **SDK** : **Docker** (PAS Streamlit/Gradio/Static)
- **Hardware** : `cpu-basic` (free)
- **Visibility** : **Public** (recommandé pour la soutenance)

→ HF crée un dépôt Git vide `https://huggingface.co/spaces/<user>/<space>`

**Option CLI** :
```bash
huggingface-cli repo create --type space --space_sdk docker <space-name>
```

---

## Étape 2 — Le `README.md` du Space (header YAML obligatoire)

À la racine de votre repo (peut coexister avec votre README projet — utiliser le **header YAML** que HF lit) :

```markdown
---
title: Dashboard B3 — [Mon Projet]
emoji: 📊
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
license: mit
---

# Mon projet B3

(votre contenu README habituel ici)
```

> `app_port` doit matcher celui exposé par le `Dockerfile` (7860 par défaut).

---

## Étape 3 — Le `Dockerfile`

### V1 — API seule (fin de Phase 2)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Dépendances Python
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code + modèle
COPY backend/ ./

EXPOSE 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```

### V2 — API + front buildé (fin de Phase 5)

Build multi-stage :
```dockerfile
# Stage 1 : build du front React
FROM node:20-alpine AS frontend-builder
WORKDIR /front
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

# Stage 2 : Python + FastAPI servant l'API et le dist/
FROM python:3.11-slim
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ ./
# Copier le dist depuis le stage 1
COPY --from=frontend-builder /front/dist /app/frontend_dist

EXPOSE 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```

> Côté `main.py`, monter `StaticFiles(directory="/app/frontend_dist", html=True)`. **Déclarer les routes `/api/...` AVANT le mount** sinon le static catch-all les capture.

---

## Étape 4 — Pousser sur HF

### Méthode 1 : remote Git HF direct

```bash
# une seule fois
git remote add hf https://huggingface.co/spaces/<user>/<space>

# à chaque déploiement
git push hf main
```
À la 1ère fois, HF demande votre **token** (créé dans Settings → Access Tokens, scope **write**). Le navigateur ouvre, on accepte.

### Méthode 2 : Sync GitHub ↔ HF (la plus pro)

Dans les **Settings du Space** → « Sync from GitHub » :
- Coller l'URL de votre repo GitHub public
- Choisir la branche (`main`)
- **Activé** : chaque push sur GitHub → rebuild auto du Space

Avantage : un seul push (GitHub) propage tout. Vous voyez les builds dans l'onglet « Logs » du Space.

### Méthode 3 : GitHub Action (si vous voulez du contrôle)

```yaml
# .github/workflows/deploy-hf.yml
name: Deploy to HF Spaces
on:
  push:
    branches: [main]
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { lfs: true }
      - run: |
          git push https://USER:${{ secrets.HF_TOKEN }}@huggingface.co/spaces/USER/SPACE main
```
(remplacer `USER` / `SPACE`, ajouter `HF_TOKEN` dans les **Settings → Secrets** GitHub)

---

## Étape 5 — Vérifier

- Onglet **« Logs »** du Space → suivre le build (~2-5 min)
- Quand status = **Running** : ouvrir l'URL `https://<user>-<space>.hf.space`
- Test API : `curl https://<user>-<space>.hf.space/api/health`

---

## Variables d'environnement / secrets

Dans **Settings du Space** :
- **Variables** : valeurs publiques (ex : `LOG_LEVEL=info`)
- **Secrets** : valeurs sensibles (ex : clé API d'un service tiers) — exposées au runtime via `os.environ`

> ⚠️ **Ne JAMAIS commiter** de secret dans le repo.

---

## Free tier — limites à connaître

| Item | Free tier (CPU basic) |
|---|---|
| RAM | 16 Go |
| vCPU | 2 |
| Stockage | ~50 Go (modèles, datasets) |
| GPU | ❌ (payant à partir de ~0,40 $/h) |
| Concurrent users | OK pour démo (quelques dizaines max simultanés) |
| Build time | jusqu'à ~30 min |
| Mise en veille | Possible après très longue inactivité (réveil en quelques secondes au 1er hit) |

---

## Pièges fréquents

| Piège | Solution |
|---|---|
| Build échoue : `npm ci` rate | Pinner les versions Node + libs ; vérifier `package-lock.json` commité |
| 502 Bad Gateway / port mismatch | Vérifier `app_port` du `README.md` Space = `EXPOSE` du Dockerfile = `--port` d'uvicorn (= **7860**) |
| HF affiche du JSON au lieu du front (V2) | `StaticFiles` mal monté, OU monté **avant** les routes `/api/...` (catch-all) |
| `model.pkl` absent en prod | Vérifier qu'il est **committé** (pas dans `.gitignore`). Si > 100 Mo → Git LFS configuré |
| Front compilé pointe vers `localhost:8000` | Rebuilder avec `VITE_API_URL=/api` (chemin **relatif** en prod = même origine) |
| « Sync from GitHub » ne déclenche rien | Vérifier les **permissions GitHub App** côté HF settings |

---

## Pour aller plus loin (optionnel)

- **Hardware payant** : Spaces avec GPU (T4 / A10G) à l'heure — utile pour un LLM, pas pour ce projet
- **Persistent storage** : disque persistant (payant) si besoin de garder des données entre redémarrages
- **Spaces Dev Mode** : pour debug en live via SSH (compte Pro)
- **Inference Endpoints** : pour servir des modèles à plus grande échelle (au-delà des Spaces)

---

## Récap : la commande clé

Une fois tout configuré (Space créé, `README.md` YAML, `Dockerfile` à la racine, remote `hf` ajouté), le déploiement tient en **une commande** :

```bash
git push hf main      # … ou git push origin main si Sync GitHub activé
```

HF rebuild → URL active en quelques minutes.
