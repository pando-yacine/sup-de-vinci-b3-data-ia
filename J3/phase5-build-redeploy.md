# Phase 5 — Build & redéploiement final (front + back unifiés)

> **But** : passer du **front local + API en ligne** à **un seul produit en ligne** (front + back **sur la même URL HF**). + CI/CD (auto-deploy sur push) + soutenance prête.

## Pourquoi redéployer ?

En **Phase 2**, on a déployé l'**API seule** sur HF (V1 = juste de la prédiction, pas d'interface).
En **Phase 5**, on **rebuild le Space avec le front en plus** : un Dockerfile multi-stage qui (1) build le React et (2) le fait servir par FastAPI → **un seul process, un seul URL public**.

Résultat : un **lien partageable unique** (« voici mon projet → https://… ») au lieu de deux services à expliquer.

---

## Livrable attendu

- Front buildé (`dist/`) **servi par FastAPI** (uvicorn)
- App qui tourne en **local en mode prod** (`uvicorn` sur port 8000) AVANT de redéployer
- **URL HF Spaces unifiée** qui sert front + API
- **CI/CD** : `git push` → rebuild auto du Space
- `README.md` final propre + capture(s) d'écran
- Soutenance répétée

---

## Étape 5.1 — Build du front

```bash
cd frontend
npm run build         # produit frontend/dist/
ls dist/              # vérifier qu'il y a un index.html + assets
```

> Si erreurs TypeScript : `npm run typecheck` pour les voir avant.

---

## Étape 5.2 — Faire servir `dist/` par FastAPI

Décommenter le bloc `StaticFiles` dans `backend/main.py` (déjà présent dans le template Phase 1) :

```python
from fastapi.staticfiles import StaticFiles
from pathlib import Path

DIST = Path(__file__).parents[1] / "frontend" / "dist"
if DIST.exists():
    app.mount("/", StaticFiles(directory=DIST, html=True), name="static")
```

⚠️ **Ordre des routes** : déclarer les `/api/...` **avant** le `mount("/")`, sinon le static catch-all capture tout.

---

## Étape 5.3 — Tester en local en mode prod

```bash
cd backend
python main.py
# → http://localhost:8000  → vous devez voir VOTRE front, pas du JSON
```

- Tester la prédiction : depuis le front, soumettre → ça doit appeler `/api/predict` **sur la même origine** (plus de CORS !)
- Tester les viz : elles doivent charger `/api/stats` correctement

Si ça marche en local en mode prod → ça marchera sur HF.

---

## Étape 5.4 — Mettre à jour le `Dockerfile` (V2 = multi-stage)

Voir la fiche **`J3/deploy-hugging-face-spaces.md`** §V2 pour le Dockerfile complet. En résumé :

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
COPY --from=frontend-builder /front/dist /app/frontend_dist
EXPOSE 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```

> Adapter le chemin du `StaticFiles` dans `main.py` pour pointer vers `frontend_dist/` en prod (variable d'env ou détection chemin).

---

## Étape 5.5 — Pousser sur HF (auto-rebuild)

```bash
git add -A && git commit -m "feat: front intégré au déploiement (V2)"
git push hf main        # remote HF
# (et) git push origin main   # GitHub aussi
```

HF rebuild en 3-5 min → **votre URL publique sert maintenant le produit complet**.

---

## Étape 5.6 — CI/CD : auto-deploy depuis GitHub

**Option simple (recommandée)** : dans les **Settings du Space HF**, activer « **Sync from GitHub** » et pointer sur votre repo public GitHub. Chaque `push` sur `main` GitHub → rebuild auto du Space.

**Option GitHub Actions** (si vous voulez ajouter des étapes — tests/lint avant deploy) :
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
      - name: Push to HF Spaces
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: |
          git push https://USER:$HF_TOKEN@huggingface.co/spaces/USER/SPACE main
```
(remplacer `USER` / `SPACE`, ajouter `HF_TOKEN` dans les secrets du repo GitHub)

---

## Étape 5.7 — Polish & soutenance

- **`README.md` racine** : présentation + **lien vers l'app en ligne** + capture d'écran + comment lancer en local
- Repo Git **propre** : pas de fichiers inutiles, `.gitignore` à jour, commits clairs
- Vérifier que la **soutenance se fait sur l'URL publique** (pas en local) — ça démontre que c'est vraiment déployé
- **Répéter** la démo (5 min) : ouvrir l'URL, saisir une prédiction, montrer les viz, montrer le code (`docs/architecture.md`)
- Anticiper les questions (cf. roleplay « entretien d'embauche »)

---

## ✅ Checklist Phase 5

- [ ] `npm run build` OK (pas d'erreur TypeScript)
- [ ] FastAPI sert `dist/` (testé en local sur port 8000)
- [ ] `Dockerfile` multi-stage (Node build + Python) à la racine
- [ ] Push HF → build OK (lire les logs)
- [ ] **URL publique unique** sert front + API (1 seul lien à partager)
- [ ] **Auto-deploy** activé (Sync GitHub OU GitHub Action)
- [ ] `README.md` final avec lien + capture
- [ ] Repo GitHub public, à jour
- [ ] Soutenance répétée sur l'URL en ligne

---

## Comment piloter Claude Code sur cette phase

- « Lis `backend/main.py`. Décommente le bloc `StaticFiles` et explique-moi ce que ça change. Vérifie l'ordre des routes (API avant catch-all). »
- *(Plan mode)* « Mets à jour le `Dockerfile` à la racine pour un build multi-stage : Stage 1 = Node 20 qui build `frontend/`, Stage 2 = Python 3.11 qui copie le dist + serve via uvicorn sur 7860. Montre-moi le plan. »
- « Ajoute dans le `README.md` racine : présentation 1 paragraphe + section « Lancer en local » + section « En ligne » avec le lien HF. »
- **Vérifier en local AVANT de pusher** : `cd backend && python main.py` → ouvrir http://localhost:8000 → vous devez voir le **front**, pas du JSON.

---

## Pièges fréquents

| Piège | Solution |
|---|---|
| HF affiche du JSON au lieu du front | `StaticFiles` pas monté, ou monté avant les `/api` |
| HF build échoue sur le Dockerfile | Lire les logs (souvent `npm ci` qui rate → pinner versions) |
| Le front en prod appelle `localhost:8000` | Recompiler avec la **bonne** `VITE_API_URL` (en prod = chemin relatif `/api`, plus rien d'absolu) |
| Push GitHub OK mais Space pas mis à jour | Vérifier que « Sync from GitHub » est activé OU que le push HF se fait |
| Modèle absent en prod | `model.pkl` est-il committé ? Git LFS configuré côté HF ? |
