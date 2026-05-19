# Sup de Vinci — Datasets cours Big Data / Data & IA

Datasets utilisés pour le projet fil rouge des modules **B2 Big Data Initiation** et **B3 Data & IA** dispensés à Sup de Vinci — campus Nantes par Yacine Arhaliass (Pando Studio).

## Chargement direct depuis Colab / Jupyter

```python
import pandas as pd

URL = "https://raw.githubusercontent.com/pando-yacine/sup-de-vinci-datasets/main/"

spotify = pd.read_csv(URL + "spotify_top_tracks.csv")
accidents = pd.read_csv(URL + "accidents_route_france_2023.csv")
immobilier = pd.read_csv(URL + "prix_immobilier_paris_2024.csv")
nba = pd.read_csv(URL + "nba_players_2022_23.csv")
logs = pd.read_csv(URL + "logs_serveur_web.csv")
steam = pd.read_csv(URL + "jeux_video_steam.csv")
```

## Datasets disponibles

| Fichier | Taille | Lignes | Source | Description |
|---|---|---|---|---|
| `spotify_top_tracks.csv` | 3.1 MB | ~33k | TidyTuesday | Top tracks Spotify avec features audio (danceability, energy, popularity...) |
| `accidents_route_france_2023.csv` | 3.7 MB | ~50k | data.gouv.fr (BAAC 2023) | Accidents corporels France 2023 : date, lieu, gravité, météo |
| `prix_immobilier_paris_2024.csv` | 1.8 MB | ~20k | data.gouv.fr (DVF) | Transactions immobilières Paris : prix, surface, pièces, code postal |
| `nba_players_2022_23.csv` | 40 KB | ~500 | basketball-reference | Stats joueurs NBA saison 2022-23 |
| `logs_serveur_web.csv` | 7.3 MB | ~100k | Synthétique | Logs HTTP : timestamp, method, status, response_time, user_agent |
| `jeux_video_steam.csv` | 2.5 MB | ~30k | HuggingFace (Steam) | Jeux Steam : genre, éditeur, note, prix, date sortie |

## Licence

Datasets publics issus de sources libres (data.gouv.fr, TidyTuesday, basketball-reference, Steam). Usage pédagogique.
