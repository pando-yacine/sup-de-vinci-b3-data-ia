# Sup de Vinci · B3 Data & IA

Ressources du module **Data & IA** (Bachelor 3 DEV, campus de Nantes), dispensé par [Yacine Arhaliass](https://github.com/pando-yacine) (Pando Studio).

- **Année** : 2026-2027 · **Volume** : 28 h en 4 jours
- **Support en ligne de chaque séance** : https://pando-studio.com/cours/b3-data-ia/
- **Objectif** : construire un produit data complet, du dataset brut à une application en ligne qui embarque un modèle de machine learning.

## Séances

| Jour | Date | Thème | Dossier |
|---|---|---|---|
| **J1** | vendredi 2 octobre 2026 | Big Data et Spark, lancement du projet fil rouge | [J1/](J1/README.md) |
| J2 | à venir | Machine learning avec Scikit-learn | [J2/](J2/README.md) |
| J3 | à venir | Du modèle au produit : FastAPI, React, dataviz | [J3/](J3/README.md) |
| J4 | à venir | Production, CI/CD, soutenances | [J4/](J4/README.md) |

Les dossiers J2 à J4 contiennent les supports de la session précédente (mai 2026). Ils sont mis à jour avant chaque séance.

## Projet fil rouge et évaluation

Tout est dans **[J1/projet-fil-rouge-brief.md](J1/projet-fil-rouge-brief.md)** : livrables jour par jour, barème (40 % projet continu, 30 % soutenance, 30 % rapport individuel), critères de choix du dataset.
Modèle de README à copier dans votre repo : **[J1/modele-README-projet.md](J1/modele-README-projet.md)**.

## Datasets de secours

Vous choisissez votre propre dataset (Kaggle, data.gouv.fr, Hugging Face, API publiques). Ceux-ci restent disponibles en dernier recours, chargeables directement depuis Colab :

```python
import pandas as pd
BASE = "https://raw.githubusercontent.com/pando-yacine/sup-de-vinci-b3-data-ia/main/"
df = pd.read_csv(BASE + "spotify_top_tracks.csv")
```

| Fichier | Lignes | Description |
|---|---|---|
| `spotify_top_tracks.csv` | ~33k | Morceaux Spotify avec caractéristiques audio (danceability, energy, popularity…) |
| `accidents_route_france_2023.csv` | ~50k | Accidents corporels en France, 2023 (date, lieu, gravité, météo) |
| `prix_immobilier_paris_2024.csv` | ~20k | Transactions immobilières à Paris (DVF) |
| `nba_players_2022_23.csv` | ~500 | Statistiques des joueurs NBA 2022-23 |
| `logs_serveur_web.csv` | ~100k | Logs HTTP synthétiques |
| `jeux_video_steam.csv` | ~30k | Jeux Steam (genre, éditeur, note, prix, date de sortie) |

Un dataset déjà travaillé par votre groupe en B2 n'est pas accepté.

## Références

- [Glossaire J1-J2](glossaire-J1-J2.md) : 124 termes data et ML
- [Fiche algorithmes ML](fiche-algos-ML.md) · [Fiche essentiels J1-J2](fiche-essentiels-J1-J2.md)

## Pour aller plus loin : IA, data et souveraineté

| Vidéo | Date | Sujet |
|---|---|---|
| [Arthur Mensch (Mistral AI) auditionné à l'Assemblée nationale](https://www.youtube.com/watch?v=kKWOkWv6pJM) | 12/05/2026 | Commission d'enquête sur les vulnérabilités du secteur du numérique : l'IA comme ressource, la dépendance aux acteurs américains |
| [Octave Klaba (OVHcloud) auditionné à l'Assemblée nationale](https://www.youtube.com/watch?v=vyJI8t_h12E) | 30/09/2026 | Commission des affaires économiques : datacenters, cloud, souveraineté des données, investir dans l'IA en Europe |
| [Quentin Adam (Clever Cloud) sur Underscore_ : « On ne paie plus les développeurs pour écrire du code ? »](https://www.youtube.com/watch?v=AiytemqB_F0) | 07/09/2026 | Industrialiser l'IA dans le développement logiciel |
| [Yann Le Cun à Sciences Po : « Où va l'intelligence artificielle ? »](https://www.youtube.com/watch?v=Y4s8NadbZfU) | 16/09/2026 | Les limites des LLM, les world models |

Datasets issus de sources publiques (data.gouv.fr, TidyTuesday, basketball-reference, Hugging Face, NYC TLC). Usage pédagogique.
