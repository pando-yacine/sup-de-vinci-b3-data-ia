# J1 · Du Big Data au projet data

> Vendredi 2 octobre 2026 · 9h15-12h45 / 13h45-17h15 · Support en ligne : https://pando-studio.com/cours/b3-data-ia/j1/

## Au programme

Spark sous le capot (Driver, executors, partitions, lazy evaluation, shuffle, Catalyst, `.explain()`), l'architecture data en 2026 (lake, warehouse, lakehouse, Parquet), puis le lancement du projet fil rouge.

## Ateliers

| Atelier | Quand | Notebook |
|---|---|---|
| **Atelier 1 · Spark sur 3 millions de courses de taxi** (en autonomie, en binôme) | 10h50-11h50 | [Ouvrir dans Colab](https://colab.research.google.com/github/pando-yacine/sup-de-vinci-b3-data-ia/blob/main/J1/ateliers/atelier1-spark-taxis-nyc.ipynb) · [fichier](ateliers/atelier1-spark-taxis-nyc.ipynb) |
| **Atelier 2 · Le pipeline sur VOTRE dataset** (en groupe projet) | 14h05-15h20 | Squelette : [Ouvrir dans Colab](https://colab.research.google.com/github/pando-yacine/sup-de-vinci-b3-data-ia/blob/main/J1/ateliers/atelier2-mini-pipeline-spark.ipynb) (reprendre les 7 étapes sur vos données) |

Atelier 1 : dans Colab, **Fichier > Enregistrer une copie dans Drive** avant de commencer. Les cellules `# À VOUS` sont à compléter, la solution est repliée juste en dessous. Les 4 questions finales se postent sur Qiplim (une réponse par binôme).

Pour aller plus loin : [`atelier1-pyspark-explain.ipynb`](ateliers/atelier1-pyspark-explain.ipynb), le word count PySpark de la session précédente.

## Livrable J1 (à rendre sous 7 jours, vendredi 9 octobre 2026, 23h59)

1. Un repo GitHub par groupe, public ou partagé avec `pando-yacine`, lien posté sur Qiplim.
2. Le notebook d'exploration de votre dataset, qui tourne de haut en bas.
3. Le README rempli à partir du [modèle](modele-README-projet.md), avec la **fiche projet** : question, cible, features, métrique, baseline naïve, risques.

Détail des attendus et du barème : **[projet-fil-rouge-brief.md](projet-fil-rouge-brief.md)**.
