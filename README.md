# Sup de Vinci — B3 Data & IA

Ressources du module **B3 Data & IA** dispensé par [Yacine Arhaliass](https://github.com/pando-yacine) (Pando Studio) à Sup de Vinci — campus Nantes.

- **4 jours** : 20-21 mai + 26-27 mai 2026
- **Volume** : 28h (4 × 7h)
- **Public** : étudiants B3 fullstack

## Navigation

- **[J1 — Big Data approfondi + Spark](J1/README.md)** (20 mai)
- **[J2 — Machine Learning Scikit-learn](J2/README.md)** (21 mai)
- **[J3 — Du modèle au produit (React + FastAPI + HF Spaces, piloté Claude Code)](J3/README.md)** (26 mai)
- **[J4 — Industrialiser + soutenances finales (CI/CD, README pro, grille /20)](J4/README.md)** (27 mai)

## Datasets pour le projet fil rouge

Tous les datasets sont à la racine du repo. Chargement direct depuis Colab/Jupyter :

```python
import pandas as pd
BASE = "https://raw.githubusercontent.com/pando-yacine/sup-de-vinci-b3-data-ia/main/"

spotify = pd.read_csv(BASE + "spotify_top_tracks.csv")
accidents = pd.read_csv(BASE + "accidents_route_france_2023.csv")
immobilier = pd.read_csv(BASE + "prix_immobilier_paris_2024.csv")
nba = pd.read_csv(BASE + "nba_players_2022_23.csv")
logs = pd.read_csv(BASE + "logs_serveur_web.csv")
steam = pd.read_csv(BASE + "jeux_video_steam.csv")  # bonus
```

| Fichier | Lignes | Taille | Description |
|---|---|---|---|
| `spotify_top_tracks.csv` | ~33k | 3.1 MB | Top tracks Spotify avec features audio (danceability, energy, popularity...) |
| `accidents_route_france_2023.csv` | ~50k | 3.7 MB | Accidents corporels France 2023 (date, lieu, gravité, météo) |
| `prix_immobilier_paris_2024.csv` | ~20k | 1.8 MB | Transactions immobilières Paris (DVF) |
| `nba_players_2022_23.csv` | ~500 | 40 KB | Stats joueurs NBA saison 2022-23 |
| `logs_serveur_web.csv` | ~100k | 7.3 MB | Logs HTTP synthétiques (timestamp, method, status, response_time) |
| `jeux_video_steam.csv` | ~30k | 2.5 MB | Jeux Steam (genre, éditeur, note, prix, date sortie) — bonus |

## Glossaire transverse

Référence des termes utilisés en J1 et J2 : [`glossaire-J1-J2.md`](glossaire-J1-J2.md) — 124 entrées, ordre alphabétique, tags [J1] / [J2] / [J1+J2].

## Licence

Datasets publics issus de sources libres (data.gouv.fr, TidyTuesday, basketball-reference, HuggingFace). Usage pédagogique.
