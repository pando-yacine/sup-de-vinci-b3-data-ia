# J3 — Du modèle au produit (dashboard React + API)

Jour 3 du module **Data & IA (B3)**. Objectif : transformer votre modèle (J2) en **produit en ligne** — un dashboard React branché sur une API FastAPI, **piloté avec Claude Code**, **déployé sur Hugging Face Spaces**.

## Le projet en 5 phases

| Phase | Fiche | Quoi |
|---|---|---|
| **1 — Specs & setup** | [`phase1-specs-et-setup.md`](./phase1-specs-et-setup.md) | Repo monorepo + GitHub public + `CLAUDE.md` + 5 docs (architecture, dataset, question prédictive, user journey, séquence) + mermaid |
| **2 — Modèle + API V1 déployée** | [`phase2-modele-api-v1.md`](./phase2-modele-api-v1.md) | EDA, itérations modèle, `model.pkl`, API FastAPI + tests pytest, **1ʳᵉ URL HF Spaces** |
| **3 — Re-specs (boucle apprentissage)** | [`phase3-re-specs.md`](./phase3-re-specs.md) | Mettre à jour `docs/` à la lumière de la V1, backlog V2 (MoSCoW) |
| **4 — Front + viz (exécuter le dev)** | [`phase4-front-exec-dev.md`](./phase4-front-exec-dev.md) | Dashboard React + Recharts + intégration sur l'API en ligne |
| **5 — Build & redéploiement final** | [`phase5-build-redeploy.md`](./phase5-build-redeploy.md) | Build prod, **1 seul Space HF unifié** (front + back), CI/CD, soutenance |

## Fiches transversales

- [**`deploy-hugging-face-spaces.md`**](./deploy-hugging-face-spaces.md) — référence technique HF (Dockerfile V1 & V2, `README` YAML, push, secrets, free tier)
- [`glossaire-J3.md`](./glossaire-J3.md) — les mots du jour (Claude Code, React/FastAPI, viz, fine-tuning)
- [`brief-autonomie-15h-16h.md`](./brief-autonomie-15h-16h.md) — consignes du créneau d'autonomie
- [`fiche-qui-suivre-en-IA.md`](./fiche-qui-suivre-en-IA.md) — qui suivre pour rester à jour
- (à la racine du repo) [`../fiche-essentiels-J1-J2.md`](../fiche-essentiels-J1-J2.md) — recap des J1 & J2 (utile pour la soutenance)

## Templates de démarrage

- [`ateliers/template-react-fastapi/`](./ateliers/template-react-fastapi/) — **squelette recommandé** : Vite + TS + React Query + Tailwind + Recharts (front) · FastAPI + joblib (back)
- [`ateliers/template-streamlit/`](./ateliers/template-streamlit/) — **filet de secours** (tout en Python)

## Livrable final attendu

Un **dashboard en ligne sur Hugging Face Spaces** (URL publique partageable) :
- on saisit des valeurs → votre modèle prédit
- **2-3 visualisations** Recharts qui répondent à une question
- Repo Git **public sur GitHub**, commits réguliers, documentation à jour, CI/CD vers HF

## Pour démarrer

1. Lire [`phase1-specs-et-setup.md`](./phase1-specs-et-setup.md).
2. Cloner / s'inspirer d'un template depuis [`ateliers/`](./ateliers/).
3. Suivre les **5 phases dans l'ordre** — chaque fiche a sa checklist.

## Le réflexe à garder partout

> Pas de spec, pas de code. Plan d'abord, prompt cadré, lire le diff, « prouve-moi que ça marche », commits petits et fréquents.
