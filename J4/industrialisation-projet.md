# Industrialiser votre projet — atelier matin J4

> **Créneau** : 11h15 - 12h45 (1h30)
> **Objectif** : passer du « ça marche chez moi sur HF » au « c'est propre et auto-déployé ».

---

## Les 4 phases de l'atelier

| Phase | Quoi | Durée | Priorité |
|---|---|---|---|
| **1** | Debug / stabilisation HF (si cassé depuis hier) | 20 min | 🔴 obligatoire si HF KO |
| **2** | CI/CD GitHub Actions → HF auto | 30 min | 🟠 priorité haute |
| **3** | README pro + mermaid | 25 min | 🟠 priorité haute |
| **4** | Finitions UX (tooltip, error, onboarding) | 15 min | 🟡 si temps |

> **Règle d'arbitrage** : si vous êtes en retard, faites Phase 1 + 3 (un README propre vaut plus en soutenance qu'un CI/CD qui n'est pas vu).

---

## Phase 1 — Debug HF (20 min)

> Si votre Space n'a pas redémarré depuis hier ou affiche une erreur, on répare.

### Symptômes courants et fixes

| Symptôme | Cause probable | Fix |
|---|---|---|
| **502 Bad Gateway** | Port mismatch | `EXPOSE 7860` dans Dockerfile = `app_port: 7860` dans `README.md` YAML = `--port 7860` dans uvicorn |
| **Build échoue : `npm ci`** | `package-lock.json` absent ou non synchro | Soit committer `package-lock.json`, soit remplacer `npm ci` par `npm install --no-audit --no-fund` |
| **Build échoue : version Python** | Image Docker incompatible avec une lib | Coller le `requirements.txt` qui marche en local et **pinner les versions** (`pandas==2.2.3`) |
| **Build OK mais app affiche JSON au lieu du front** | `StaticFiles` monté avant les routes API | Déclarer **toutes** les routes `/api/...` AVANT `app.mount("/", StaticFiles(...))` |
| **Modèle absent** | `.pkl` dans `.gitignore` | Vérifier qu'il est committé (`git status`). Si > 100 MB → Git LFS |
| **App affiche `localhost:8000`** | Front compilé avec mauvais `VITE_API_URL` | Rebuilder le front avec `VITE_API_URL=/api` (chemin **relatif** = même origine en prod) |

### Outils de debug

- **Logs Space HF** : onglet « Logs » de votre Space → onglets « Build » et « Container » (runtime)
- **curl** depuis votre laptop : `curl https://<user>-<space>.hf.space/api/health` doit retourner 200
- **Forcer un rebuild** : Space → Settings → Factory rebuild

---

## Phase 2 — CI/CD GitHub Actions → HF (30 min)

> Aujourd'hui : vous push sur GitHub PUIS vous push sur HF manuellement. Demain : 1 seul push suffit.

### Étape 1 — Créer le token HF (5 min)

1. Aller sur https://huggingface.co/settings/tokens
2. **New token** → nom : `github-action-deploy` → type : **write**
3. Copier le token (commence par `hf_...`)

### Étape 2 — Ajouter le secret GitHub (5 min)

1. Aller sur votre repo GitHub → Settings → Secrets and variables → Actions
2. **New repository secret** → nom : `HF_TOKEN` → valeur : coller le token
3. Save

> ⚠️ **Ne commitez JAMAIS un token en clair dans votre code.** Si vous l'avez fait par erreur, allez **immédiatement** révoquer le token HF (Settings → Tokens → Revoke).

### Étape 3 — Créer le workflow (15 min)

Créer le fichier `.github/workflows/sync-to-hf.yml` à la racine de votre repo :

```yaml
name: Sync to HF Spaces

on:
  push:
    branches: [main]
  workflow_dispatch:   # bouton "Run workflow" manuel dans l'UI Actions

jobs:
  sync-to-hf:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout (avec LFS pour les .pkl/.cbm)
        uses: actions/checkout@v4
        with:
          lfs: true
          fetch-depth: 0   # IMPORTANT : full history pour pouvoir push sur HF

      - name: Push to HF Space
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: |
          # Remplacer USER et SPACE par vos valeurs
          git push --force \
            https://USER:${HF_TOKEN}@huggingface.co/spaces/USER/SPACE \
            main
```

**À adapter** :
- Remplacer `USER` (2x) par votre user HF
- Remplacer `SPACE` par le nom de votre Space
- Le `--force` est pour gérer les cas où HF a des commits que GitHub n'a pas (sync ré-aligne)

### Étape 4 — Tester (5 min)

1. Faire un petit changement (ex: une virgule dans le README)
2. `git add . && git commit -m "test ci" && git push origin main`
3. Aller sur GitHub → onglet **Actions** → vérifier que le workflow tourne en vert
4. Aller sur votre HF Space → onglet **Logs** → vérifier le rebuild
5. ⏰ Patienter ~3-5 min puis tester l'URL

---

## Phase 3 — README pro + mermaid (25 min)

> Un beau README rapporte des points à la soutenance ET impressionne en entretien.

### Structure attendue

```markdown
# Nom du projet

[![Build](https://img.shields.io/github/actions/workflow/status/USER/REPO/sync-to-hf.yml)](https://github.com/USER/REPO/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![HF Spaces](https://img.shields.io/badge/🤗_HF_Space-live-yellow.svg)](https://huggingface.co/spaces/USER/SPACE)

> Une phrase qui résume le projet (problème résolu).

## 🎯 Le problème

3-4 lignes : qui (persona), quoi (besoin), pourquoi (impact).

## 🛠️ Stack

| Couche | Tech |
|---|---|
| Frontend | React + Vite + Tailwind |
| Backend | FastAPI + Pydantic |
| Modèle | sklearn / xgboost / etc. |
| Déploiement | HF Spaces Docker |

## 📐 Architecture

\`\`\`mermaid
graph LR
    User[👤 User] -->|HTTPS| HF[HF Space]
    HF -->|/api/predict| Model[model.pkl]
    HF -->|sert front| React[React app]
\`\`\`

## 🚀 Démo live

👉 https://USER-SPACE.hf.space

## 💻 Installation locale

\`\`\`bash
# Backend
cd backend
pip install -r requirements.txt
python main.py    # port 8000

# Frontend
cd frontend
npm install
npm run dev       # port 5173, proxy /api → :8000
\`\`\`

## 🚢 Déploiement

`git push origin main` → CI/CD GitHub Actions → HF Space rebuild → URL live.

## 📊 Modèle & Données

- Dataset : [nom + lien + nombre de lignes]
- Cible : `colonne_y`
- Métrique : F1 = X.XX sur le test set
- Modèle final : [Random Forest / XGBoost / ...] choisi vs baseline [Régression Logistique]

## ⚠️ Limites

- Limite 1
- Limite 2

## 👤 Auteurs

- Prénom Nom (LinkedIn / GitHub)
```

### Faire un schéma mermaid

Mermaid est natif sur GitHub. Pas besoin d'install. Exemples utiles :

**Architecture système** :
```
graph TB
    User --> HF
    HF --> Model
```

**Pipeline de données** :
```
sequenceDiagram
    User->>FastAPI: POST /predict
    FastAPI->>Model: predict(input)
    Model-->>FastAPI: proba
    FastAPI-->>User: JSON response
```

**Cycle de vie du modèle** :
```
flowchart LR
    Train[Train sklearn] --> PKL[model.pkl]
    PKL --> API[FastAPI /predict]
    API --> User
```

> Tester sur https://mermaid.live avant de coller dans le README.

---

## Phase 4 — Finitions UX (15 min, optionnel)

> Si vous avez du temps, **un petit truc visible** fait plus pour votre soutenance qu'un gros truc invisible.

### Idées rapides (5-10 min chacune)

| Truc | Effort | Impact démo |
|---|---|---|
| **Tooltip** sur 1-2 termes techniques de votre domaine | XS | « Ah, ils ont pensé à expliquer » |
| **Spinner** pendant le `/api/predict` (`isLoading` de `useQuery`) | XS | « Ah, ils gèrent les états » |
| **Message d'erreur user-friendly** au lieu de l'erreur brute | XS | « Ah, ça plante pas bizarre » |
| **Onboarding mini-modal** au 1er chargement (3 phrases + bouton Got it) | S | « Ils ont pensé au 1er user » |
| **Badge statut** sur les prédictions (high/low confidence) | S | « Ils contextualisent l'output » |
| **Bouton refresh** sur les données | XS | « Ils ont pensé à l'interactivité » |

> **Ne** commencez **pas** une feature complexe. Vous risquez de casser ce qui marche déjà.

---

## Checklist fin d'atelier matin (12h45)

- [ ] HF Space affiche **RUNNING** et l'URL ouvre l'app
- [ ] Push origin déclenche le rebuild HF auto (workflow vert)
- [ ] README a un titre, badges, mermaid, sections Install / Demo / Stack
- [ ] `requirements.txt` à jour (pas de versions wildcard `>=`)
- [ ] Pas de secret en clair dans le repo (`git log -p | grep -i token` ne doit rien remonter)
- [ ] 1 finition UX visible (optionnel)

> Si tout est vert, vous pouvez aller manger sereinement. **Sinon, restez 5 min de plus** — le déjeuner ne vaut pas une soutenance compromise.

---

## Erreurs fréquentes à éviter

- ❌ **Tester le CI/CD pour la première fois pendant la soutenance**. → Le faire tourner avant.
- ❌ **Push un secret** par erreur. → Si arrivé, révoquer **immédiatement** le token côté HF (et GitHub si applicable), puis générer un nouveau token et l'ajouter en secret.
- ❌ **Modifier la structure du modèle au dernier moment**. → Si votre `.pkl` marchait hier, ne le retouchez **pas** ce matin. Risque : casser features sklearn vs Python.
- ❌ **Faire un README de 300 lignes**. → Court > exhaustif. 1 page max.
- ❌ **Lancer un test pytest qui rate** avant la démo. → Vérifier avant.

---

## Pour aller plus loin (après la formation)

- **Dependabot** sur GitHub : update auto des dépendances avec PR proposée
- **Test pytest dans la CI** : workflow ajoute un step `pytest` avant le push HF
- **Logs structurés** : structlog ou loguru pour debug en prod
- **Healthcheck externe** : UptimeRobot (gratuit, 50 ping/5min)
- **Multi-env** : Space `staging` et `prod`, push sur `dev` → staging, push sur `main` → prod
