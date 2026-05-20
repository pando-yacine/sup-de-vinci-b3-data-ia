# J1 — Big Data approfondi + Spark hands-on

> 20 mai 2026 · Sup de Vinci Nantes · 7h (9h15 — 17h15)

## Thème de la journée

Du B2 au B3 : on revoit les fondamentaux Big Data et on approfondit Spark **sous le capot** (Driver/Executors, lazy evaluation, Catalyst, `.explain()`, DAG).

## Sommaire des ressources

- **[Brief projet fil rouge](projet-fil-rouge-brief.md)** — Le brief 4 jours à lire en premier (livrables, datasets, grille /20)
- **[Quiz diagnostic B2](quiz-diagnostic-10Q.md)** — 10 questions de récap B2 (utilisé en début de matinée sur Qiplim)

## Ateliers

- **[Atelier 1 — MapReduce papier + démo PySpark](ateliers/exercice-mapreduce-papier.md)** (texte papier + suite ci-dessous)
  - Phase 1 papier : 3 paragraphes à compter par 3 groupes (15 min)
  - Phase 2 code : [`atelier1-pyspark-explain.ipynb`](ateliers/atelier1-pyspark-explain.ipynb) (30 min) — découvrir `.explain()`, lazy eval, Spark UI
- **[Atelier 2 — Mini-pipeline Colab (Pandas → PySpark)](ateliers/atelier2-mini-pipeline-spark.ipynb)** (1h15)
  - Charger CSV + JSON, explorer, nettoyer, joindre, analyser, visualiser
  - Bonus B3 : refaire l'agrégation en PySpark, comparer

## Comment ouvrir les notebooks sur Colab

1. Clic droit sur le `.ipynb` → "Open with" → "Colab"

Ou directement :

```
https://colab.research.google.com/github/pando-yacine/sup-de-vinci-b3-data-ia/blob/main/J1/ateliers/atelier1-pyspark-explain.ipynb
https://colab.research.google.com/github/pando-yacine/sup-de-vinci-b3-data-ia/blob/main/J1/ateliers/atelier2-mini-pipeline-spark.ipynb
```

## En fin de J1

Chaque groupe a :
- Son dataset choisi (parmi les 5 du projet fil rouge)
- 1 question prédictive formulée (cible `y`, features `X` candidates)
- Le notebook prêt pour ajouter le modèle ML demain
