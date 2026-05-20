# Quiz diagnostic Big Data -- B3 J1 (20 mai)

> **Cible** : étudiants B3 fullstack Sup de Vinci Nantes, B2 validé.
> **Objectif** : calibrer le niveau réel sur les fondamentaux Big Data avant d'attaquer Spark approfondi.
> **Format Qiplim Engage** : Quiz scoring + leaderboard. Timer 30 s / question. Correction immédiate après chaque question = rappel pédagogique.
> **Durée totale** : 25-30 min (questions + corrections).
> **Filtrage** : 7 questions issues du quiz final B2-J3 recalibrées + 3 questions originales orientées fullstack B3.

---

## Q1 -- [5V] : Distinguer les 5V

**Type Qiplim** : Multiple Choice
**Question** : Lequel de ces V ne fait PAS partie des 5V du Big Data ?
**Choix** :
- A) Vélocité
- B) Variété
- C) Visibilité
- D) Véracité

**Réponse** : C
**Explication formateur (10-20s)** : "Les 5V c'est Volume, Vitesse (ou Vélocité), Variété, Véracité, Valeur. La Visibilité n'en fait pas partie -- piège classique. Si la classe se trompe sur celle-là, on rallonge le rappel."

---

## Q2 -- [SQL vs NoSQL] : Schéma fixe ou flexible

**Type Qiplim** : Multiple Choice
**Question** : Quelle est la principale différence entre une base SQL et une base NoSQL ?
**Choix** :
- A) SQL est toujours plus rapide que NoSQL
- B) NoSQL n'a pas de schéma fixe, SQL impose un schéma rigide
- C) SQL est gratuit, NoSQL est payant
- D) NoSQL ne supporte pas les requêtes complexes

**Réponse** : B
**Explication formateur (10-20s)** : "SQL = colonnes prédéfinies, parfait quand la structure est stable. NoSQL = schéma flexible. En tant que fullstack, vous choisirez selon le pattern d'accès, pas selon une religion."

---

## Q3 -- [Hadoop/HDFS] : Stockage distribué

**Type Qiplim** : Multiple Choice
**Question** : Dans HDFS, un fichier de 1 To est stocké comment ?
**Choix** :
- A) Sur un seul gros disque dur dédié
- B) Découpé en blocs répartis et répliqués sur plusieurs machines
- C) Compressé puis envoyé dans un Data Warehouse
- D) Dans une base MongoDB

**Réponse** : B
**Explication formateur (10-20s)** : "HDFS découpe en blocs de 128 Mo, répartit sur le cluster, réplique x3 par défaut pour la tolérance aux pannes. Le NameNode garde la carte. C'est l'ancêtre conceptuel de S3 et Azure Blob."

---

## Q4 -- [MapReduce] : Les 2 étapes

**Type Qiplim** : Multiple Choice
**Question** : Le paradigme MapReduce divise un traitement distribué en 2 étapes principales. Lesquelles ?
**Choix** :
- A) Collecter et stocker
- B) Map (découper le travail) et Reduce (agréger les résultats)
- C) Upload et download
- D) Compiler et exécuter

**Réponse** : B
**Explication formateur (10-20s)** : "Map = chaque machine traite sa part en parallèle. Reduce = on regroupe et on agrège. C'est ce qu'on va simuler au tableau dans 1h avec 3 groupes de la classe."

---

## Q5 -- [Spark vs Pandas] : Quand utiliser quoi

**Type Qiplim** : Multiple Choice
**Question** : Vous avez un CSV de 500 Go à traiter sur votre laptop avec 16 Go de RAM. Quel outil choisir ?
**Choix** :
- A) Pandas, c'est plus simple
- B) Excel avec Power Query
- C) Spark sur un cluster (ou Spark managé type Databricks/Synapse)
- D) MongoDB avec une requête find()

**Réponse** : C
**Explication formateur (10-20s)** : "Pandas charge tout en RAM = MemoryError immédiat. Spark distribue le calcul sur plusieurs machines. Règle de pouce : si ça tient en RAM, Pandas suffit. Sinon, Spark. On verra l'API Spark cet après-midi -- syntaxe très proche de Pandas."

---

## Q6 -- [ETL / Pipelines] : Ordre canonique

**Type Qiplim** : Ranking
**Question** : Classez les étapes d'un pipeline data classique dans l'ordre.
**Choix** (à classer) :
- A) Analyse / Visualisation
- B) Collecte (Extract)
- C) Stockage / Load
- D) Transformation / Nettoyage

**Réponse** : B → C → D → A (ELT moderne : Extract → Load → Transform → Analyze)
**Explication formateur (10-20s)** : "Variante ETL classique = Extract → Transform → Load (on nettoie avant). Variante ELT moderne = Extract → Load → Transform (on stocke brut, on transforme à la demande). Sur le projet fil rouge, vous ferez de l'ELT."

---

## Q7 -- [Data Lake vs Data Warehouse] : Brut ou structuré

**Type Qiplim** : Multiple Choice
**Question** : Quelle affirmation décrit le mieux un Data Lake ?
**Choix** :
- A) Une base SQL hyper optimisée pour les requêtes
- B) Un stockage de données brutes sans schéma prédéfini (schema-on-read)
- C) Un cache distribué type Redis
- D) Un système de messagerie type Kafka

**Réponse** : B
**Explication formateur (10-20s)** : "Data Lake = on stocke tout en brut (S3, Azure Blob), on impose un schéma au moment de la lecture. Data Warehouse = données déjà nettoyées et structurées (BigQuery, Synapse). Aujourd'hui souvent combinés en 'Lakehouse'."

---

## Q8 -- [Pandas pratique] : Lire un score

**Type Qiplim** : Multiple Choice
**Question** : Vous tapez `df.groupby("ville")["prix"].mean()`. Vous obtenez quoi ?
**Choix** :
- A) Le prix de chaque ligne du DataFrame
- B) Une Series avec le prix moyen par ville
- C) Le nombre de villes distinctes
- D) Une erreur car groupby n'accepte pas mean()

**Réponse** : B
**Explication formateur (10-20s)** : "C'est l'opération la plus utilisée en analyse tabulaire : agréger par catégorie. En Spark vous écrirez `df.groupBy('ville').mean('prix')` -- même logique, syntaxe quasi identique."

---

## Q9 -- [Pandas pratique] : Joindre 2 sources

**Type Qiplim** : True-False
**Question** : `pd.merge(df_a, df_b, on="id_client", how="left")` garde toutes les lignes de `df_a` même si `id_client` n'existe pas dans `df_b`.
**Choix** :
- A) Vrai
- B) Faux

**Réponse** : A (Vrai)
**Explication formateur (10-20s)** : "`how='left'` = on garde tout à gauche, on remplit avec NaN à droite si pas de match. `inner` = intersection seulement. Cette nuance fait sauter ou doubler des lignes dans 80% des bugs de pipeline."

---

## Q10 -- [Cas d'usage] : Reconnaître un cas Big Data temps réel

**Type Qiplim** : Multiple Choice
**Question** : Quel cas relève le plus typiquement d'une stack Big Data **streaming** (Kafka + Spark Streaming) plutôt que batch ?
**Choix** :
- A) Rapport mensuel des ventes
- B) Détection de fraude bancaire à la transaction
- C) Backup quotidien de la base de production
- D) Entraînement nocturne d'un modèle ML

**Réponse** : B
**Explication formateur (10-20s)** : "Fraude bancaire = on doit bloquer la transaction en moins d'une seconde. Streaming obligatoire. Les 3 autres tolèrent du batch (toutes les nuits suffit). En tant que fullstack, retenez la règle : SLA latence < 5 s → streaming, sinon batch."

---

## Synthèse formateur après le quiz

- **Score moyen > 7/10** → classe solide, on accélère sur Spark interne (Driver/Executors, lazy eval, `.explain()`).
- **Score moyen 4-7/10** → niveau normal, on suit le plan tel quel.
- **Score moyen < 4/10** → on rallonge le rappel Hadoop/Spark de 15 min et on compresse NoSQL/ETL en fin de matinée.

Transition vers le bloc suivant : "On a les fondamentaux. Maintenant on plonge dans le **comment** : architecture Spark interne, lazy evaluation, et pourquoi vous écrirez peut-être plus de Spark que de Pandas en stage."
