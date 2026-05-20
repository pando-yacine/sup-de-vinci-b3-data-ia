# Quiz éclair Spark -- B3 J2 (21 mai)

> **Cible** : étudiants B3 fullstack, retour de J1 (Spark interne, lazy eval, MapReduce papier + démo PySpark).
> **Objectif** : récap rapide en début de J2, avant d'attaquer le ML. 5 questions, 1 min chacune (question + correction).
> **Durée totale** : 5 minutes chrono.
> **Format Qiplim Engage** : Quiz scoring rapide, pas de leaderboard (on ne s'attarde pas), timer 20 s / question.
> **Ton** : énergique, on enchaîne. La correction sert de réveil collectif, pas de cours.

---

## Q1 -- [DataFrame vs RDD] : L'API moderne

**Type Qiplim** : Multiple Choice
**Question** : Aujourd'hui en Spark, vous écrivez plutôt avec quelle API pour du tabular ?
**Choix** :
- A) RDD (l'API bas niveau historique)
- B) DataFrame / Dataset (API haut niveau avec optimisations Catalyst)
- C) MapReduce direct
- D) HDFS bytes

**Réponse** : B
**Explication formateur (10-20s)** : "RDD = API d'origine, encore là mais plus rarement écrit à la main. DataFrame = standard de fait, syntaxe à la Pandas/SQL, plus performante car Catalyst optimise le plan. RDD se cache en dessous."

---

## Q2 -- [Lazy evaluation] : Transformation vs action

**Type Qiplim** : Multiple Choice
**Question** : Vous faites `df.filter(df.age > 18).select("nom")`. Spark exécute le calcul **quand** ?
**Choix** :
- A) Immédiatement, ligne par ligne
- B) Jamais tant que vous n'appelez pas une action (`.show()`, `.count()`, `.collect()`)
- C) Au moment du `import pyspark`
- D) Toutes les 30 secondes en arrière-plan

**Réponse** : B
**Explication formateur (10-20s)** : "Lazy evaluation : `filter` et `select` sont des **transformations**, elles construisent un plan. Rien ne tourne tant qu'une **action** (`show`, `count`, `write`) ne déclenche le job. C'est ce qui permet à Catalyst d'optimiser toute la chaîne d'un coup."

---

## Q3 -- [MapReduce concept] : Le mot juste

**Type Qiplim** : Multiple Choice
**Question** : Dans MapReduce, l'étape **Reduce** sert à :
**Choix** :
- A) Compresser les fichiers pour économiser le disque
- B) Découper le travail en morceaux distribués sur les machines
- C) Agréger les résultats produits par les étapes Map
- D) Supprimer les doublons dans le dataset

**Réponse** : C
**Explication formateur (10-20s)** : "Map = découper et traiter en parallèle. Shuffle = regrouper par clé. Reduce = agréger (somme, moyenne, max). C'est exactement ce qu'on a fait hier au tableau avec les 3 groupes."

---

## Q4 -- [.explain() / plan d'exécution] : Lire ce que Spark va faire

**Type Qiplim** : True-False
**Question** : `df.explain()` affiche le plan d'exécution physique que Spark va exécuter, sans déclencher le calcul.
**Choix** :
- A) Vrai
- B) Faux

**Réponse** : A (Vrai)
**Explication formateur (10-20s)** : "`.explain()` montre le plan logique optimisé + le plan physique (PushedFilters, Exchange, broadcast joins, etc.). C'est le premier outil de debug perf en Spark. Le job ne tourne pas, on lit juste le plan."

---

## Q5 -- [Driver vs Executor] : Qui fait quoi

**Type Qiplim** : Multiple Choice
**Question** : Dans une application Spark, qui exécute le code de transformation sur les partitions de données ?
**Choix** :
- A) Le Driver (le programme principal qui orchestre)
- B) Les Executors (les workers distribués sur le cluster)
- C) Le NameNode HDFS
- D) Le Cluster Manager (YARN, Kubernetes, Standalone)

**Réponse** : B
**Explication formateur (10-20s)** : "Driver = chef d'orchestre, garde le plan et envoie les tâches. Executors = ouvriers, exécutent les tâches sur leurs partitions et stockent les caches. Cluster Manager = RH, alloue les ressources. Erreur classique : `collect()` ramène tout sur le Driver -- OOM garanti sur gros dataset."

---

## Transition vers le bloc ML

"Vous avez du data nettoyé et distribué. Aujourd'hui on lui apprend à prédire. On reste sur Pandas + Scikit-learn pour les ateliers -- Spark MLlib est là si on doit scaler, mais pour 80% des cas pro, Sklearn suffit largement."
