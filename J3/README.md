# J3 — Du modèle au produit (dashboard React + API)

Jour 3 du module **Data & IA (B3)**. Objectif : transformer votre modèle de J2 en **produit utilisable** — un dashboard **React** branché sur une **API FastAPI** qui sert votre modèle, le tout **piloté avec Claude Code**.

## Contenu de ce dossier

| Fichier | Pour quoi |
|---|---|
| `glossaire-J3.md` | Les mots du jour (Claude Code, API/front/back, React, viz, fine-tuning…) |
| `brief-autonomie-15h-16h.md` | Consignes du créneau d'autonomie (15h-16h) |
| `ateliers/template-react-fastapi/` | **Squelette de départ** à compléter avec Claude Code (Vite + TS + React Query + Tailwind + Recharts / FastAPI + joblib) |
| `ateliers/template-streamlit/` | Filet de secours (tout en Python) si vous bloquez sur React |

## Livrable attendu en fin de J3

Un dashboard **local** qui tourne : on saisit des valeurs → le modèle répond, **+ 2-3 visualisations** de vos données. Repo Git propre, commits réguliers.

## Pour démarrer

1. Choisissez votre template : `ateliers/template-react-fastapi/` (recommandé) ou `ateliers/template-streamlit/` (secours).
2. Suivez le `README.md` du template.
3. Exportez votre modèle de J2 : `joblib.dump(pipeline, "model.pkl")`.
4. Pilotez Claude Code : **plan d'abord**, prompt cadré, **lisez les diffs**, « prouve-moi que ça marche », commits fréquents.

> Le déploiement cloud (Azure) se fait au **J4**.
