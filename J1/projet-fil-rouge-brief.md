# Projet fil rouge B3 Data & IA -- Brief

> **Module** : Data & IA -- B3 fullstack Sup de Vinci Nantes
> **Durée** : 4 jours (20-21 mai, 26-27 mai 2026)
> **Format** : groupes de 2-3, choix du dataset en fin de J1

---

## Objectif

Construire un **pipeline data complet**, des données brutes jusqu'au déploiement cloud. Sur 4 jours, votre groupe traverse la même chaîne qu'un Data Engineer / Data Scientist en mission : collecte → nettoyage → modélisation ML → dashboard → mise en production sur Azure. À la fin du J4, vous présentez un produit qui tourne, pas un notebook orphelin.

## Modalités

- **Groupes** : 2 à 3 personnes (max). Constitution en fin de J1.
- **Dataset** : choisi en fin de J1 parmi 5 options (premier arrivé, max 2 groupes par dataset).
- **Outils imposés** : Python, Pandas/Scikit-learn, Streamlit, Azure App Service.
- **Code** : un repo Git par groupe, commits réguliers.
- **Notebook + app** sont les deux livrables techniques. La soutenance au J4 fait le lien.

## 5 datasets au choix

Tous les datasets sont hébergés sur GitHub. Chargement direct depuis Colab :

```python
import pandas as pd
BASE = "https://raw.githubusercontent.com/pando-yacine/sup-de-vinci-b3-data-ia/main/"
df = pd.read_csv(BASE + "spotify_top_tracks.csv")  # remplacer par votre dataset
```

| # | Dataset | Lignes | Cible naturelle | URL |
|---|---|---|---|---|
| 1 | **Spotify Top Tracks** | ~33k | Prédire `popularity` (régression) ou `explicit` (classification) | `spotify_top_tracks.csv` |
| 2 | **Accidents route France 2023** | ~50k | Prédire `gravite` (classification) | `accidents_route_france_2023.csv` |
| 3 | **Prix immobilier Paris** | ~20k | Prédire `valeur_fonciere` (régression) | `prix_immobilier_paris_2024.csv` |
| 4 | **Stats NBA 2022-23** | ~500 | Prédire `salary` ou `position` | `nba_players_2022_23.csv` |
| 5 | **Logs serveur web** | ~100k | Détecter anomalies / classer `status_code` | `logs_serveur_web.csv` |

Bonus optionnel : `jeux_video_steam.csv` (~30k jeux Steam) — prédire la note ou le succès commercial.

Premier arrivé premier servi, **max 2 groupes par dataset**.

## Livrables progressifs

| Fin de jour | Livrable attendu |
|---|---|
| **J1 (20 mai)** | Dataset chargé sur Colab, exploration initiale (`.info()`, `.describe()`), 1 question prédictive formulée (cible `y`, features `X` candidates). |
| **J2 (21 mai)** | Modèle baseline ML qui tourne (régression linéaire, logistique ou random forest), 1 métrique de performance affichée et commentée. |
| **J3 (26 mai)** | Dashboard Streamlit **local** avec modèle intégré (input utilisateur → prédiction), 2-3 visualisations data, narratif. |
| **J4 (27 mai)** | App déployée sur **Azure App Service** (URL publique), code sur GitHub, soutenance **8 min** + 4 min Q/R. |

## Grille d'évaluation (/20)

| Critère | Pts | Ce qu'on regarde |
|---|---|---|
| Compréhension dataset | /4 | EDA propre, choix de la question prédictive justifié, conscience des biais et limites du dataset |
| Pipeline data | /4 | Nettoyage reproductible, gestion des manquants et types, séparation train/val/test correcte, pas de leakage |
| Modèle ML | /5 | Baseline pertinent, métriques adaptées au problème, comparaison d'au moins 2 modèles, justification du final |
| Dashboard | /4 | Streamlit fonctionnel en local et déployé, UX lisible, prédiction interactive, viz exploitables |
| Soutenance | /3 | 8 min tenues, démo live qui marche, répartition du temps de parole équilibrée, réponses solides en Q/R |

## Conseils d'organisation

- **Cadrez la question prédictive dès J1**. Un projet flou en J1 = panique en J4. Une cible `y` claire + 3-5 features candidates suffit pour démarrer.
- **Baseline simple d'abord, optimisation après**. Une régression linéaire ou un RandomForest par défaut est plus utile qu'un XGBoost mal réglé. Vous comparez ensuite.
- **Versionnez tout sur Git dès J1**. Branche `main` propre, commits par étape. Un repo bordélique se paie en démo.
- **Préparez le déploiement Azure dès J3 soir, pas J4 matin**. Le déploiement initial casse toujours quelque chose (variables d'env, requirements.txt, port). Anticipez.
- **Répartissez les rôles dans le binôme/trinôme** : data/modèle vs dashboard/déploiement. Vous gagnez 30 % de temps avec un découpage net.

Le projet est noté sur la **trajectoire** autant que sur le résultat final. Un dataset modeste avec un pipeline propre vaut mieux qu'un dataset ambitieux laissé en chantier.
