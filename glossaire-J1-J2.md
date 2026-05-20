# Glossaire B3 Data & IA — J1 + J2

> Référence formateur pour réviser avant et après les jours 1 et 2.
> Termes ordonnés alphabétiquement, tag entre crochets après le terme :
> [J1] = vu en jour 1 (Big Data + Spark), [J2] = vu en jour 2 (ML Scikit-learn), [J1+J2] = transverse.
> Les **termes en gras** dans les définitions renvoient à un autre entry du glossaire.

---

## A

**Accuracy** [J2] — Métrique de classification = (prédictions correctes) / (total). Piège : sur un dataset déséquilibré (fraude 0.1%), un modèle qui prédit "non" partout a 99.9% d'accuracy mais est inutile. Préférer **F1 score**, **PR-AUC**, ou la **confusion matrix**.

**Action (Spark)** [J1] — Opération qui déclenche l'exécution effective d'un calcul Spark. Exemples : `.collect()`, `.count()`, `.show()`, `.write()`. Avant une action, Spark accumule les **transformations** sans rien faire (**lazy evaluation**). Une action force le **DAG** à s'exécuter.

**Apache Hadoop** [J1] — Premier framework open source de Big Data (2006). 3 composants : **HDFS** (stockage), **MapReduce** (traitement), **YARN** (gestion de ressources). Créé par Yahoo en s'inspirant des papers Google. A dominé le Big Data ~10 ans avant l'arrivée de **Spark**.

**Apprentissage non supervisé** [J2] — Famille de ML où l'on a uniquement `X` (pas de cible `y`). On cherche une structure cachée. Deux sous-familles vues en J2 : **clustering** (K-means, DBSCAN) et **réduction de dimension** (PCA, t-SNE, UMAP).

**Apprentissage supervisé** [J2] — Famille de ML où l'on a `(X, y)` et où l'on prédit `y`. Deux sous-familles : **régression** (`y` continu) et **classification** (`y` catégoriel). C'est la famille la plus utilisée en pratique (prix, fraude, churn).

**Atelier 1 J1 (MapReduce papier + démo PySpark)** [J1] — Compter les mots dans un texte en 3 paragraphes, d'abord à la main (Map → Reduce), puis en **PySpark** avec `.explain()` pour lire le **plan d'exécution**.

**Atelier 1 J2 (baseline immobilier)** [J2] — Pipeline complet sur dataset Prix immobilier (California Housing) : EDA → preprocessing → train/val/test split → **ColumnTransformer** → `LinearRegression` → score R². Le baseline avant toute optimisation.

**Atelier 2 J1 (mini-pipeline Colab)** [J1] — Pipeline Pandas → PySpark sur 2 sources (CSV + JSON) : chargement, exploration, nettoyage, jointure, agrégation, visualisation. Bonus : refaire l'agrégation en Spark pour comparer.

**Atelier 2 J2 (CV + 3 modèles)** [J2] — Passer du baseline à un vrai pipeline : feature engineering, **cross-validation** k-fold, comparaison de 3 modèles (LinearRegression, **RandomForest**, **GradientBoosting**), tuning par **GridSearchCV**, évaluation finale sur test set.

**Azure** [J1+J2] — Plateforme cloud de Microsoft. Briques data : Blob Storage, Synapse (DWH), Cosmos DB (NoSQL), Event Hubs (streaming), Azure ML. En B3, chaque étudiant a 100 € provisionnés sur son compte Azure pour les ateliers J3-J4.

---

## B

**Backtest** [J2] — Évaluation d'un modèle prédictif sur des données historiques. Mesure "comme si" le modèle avait été utilisé dans le passé. Piège classique : les résultats de backtest sont souvent plus optimistes que la production réelle (gap backtest/prod), surtout si peu d'événements rares ont porté la performance.

**Backtest vs production** [J2] — Cas hippique : +914% en backtest, mais reposait sur 8 courses rares / 103 → variance énorme. Leçon : un backtest n'est PAS un audit de prod. Vérifier la stabilité (variance, intervalle de confiance) avant de déployer.

**Baseline (modèle)** [J2] — Modèle simple servant de point de comparaison. Ex : régression linéaire pour un problème de régression, prédiction de la classe majoritaire pour une classification. Règle d'or : "tu ne sais pas si ton XGBoost est bon tant que tu ne sais pas ce que fait la régression linéaire."

**BigQuery** [J1] — Service de **data warehouse** de Google Cloud. Permet d'exécuter des requêtes SQL sur des pétaoctets de données sans gérer d'infrastructure. Modèle serverless, facturé à la requête. Concurrent direct de Redshift et Snowflake.

**Bigtable** [J1] — Système de stockage distribué créé par Google (paper 2006). Base **NoSQL** à colonnes larges, conçue pour gérer des pétaoctets. A inspiré HBase, **Cassandra**, et Accumulo.

**Broadcast join** [J1] — Optimisation de jointure en Spark : si une des deux tables est petite (< quelques centaines de Mo), Spark l'envoie en mémoire sur tous les **executors** plutôt que de faire un **shuffle** coûteux. Activable manuellement via `broadcast(df)`. Peut transformer un job de 1h en 1 minute.

**Bus de données / event bus** [J1] — Infrastructure qui permet à plusieurs systèmes d'émettre et de consommer des événements de manière découplée. Pattern **Pub/Sub**. Implémenté par **Kafka**, Google Pub/Sub, Azure Event Hubs. Utilisé dans le cas Cosa Travel pour la sync Persona → Odoo.

---

## C

**C4 (modèle d'architecture)** [J1] — Méthode de documentation d'architecture logicielle en 4 niveaux de zoom : Context (qui utilise quoi), Containers (apps, bases), Components (modules), Code. Utilisé pour communiquer l'architecture avec des non-techniques. Voir cas Cosa Travel.

**Cartographie IT** [J1] — Inventaire visuel des systèmes d'une entreprise et de leurs interactions (apps, bases, flux). Première étape d'un projet ETL : avant de pipeliner, on comprend la topologie. Souvent matérialisée en **C4**.

**Cassandra (Apache)** [J1] — Base de données **NoSQL** distribuée à colonnes larges. Créée par Facebook. Points forts : haute disponibilité, scalabilité linéaire, écritures rapides. Utilisée pour les logs, IoT, données massives.

**Catalyst optimizer (Spark)** [J1] — Moteur d'optimisation de **Spark SQL**. Lit le plan logique des **transformations**, le réécrit (prédicat pushdown, élimination de colonnes inutiles, réordonnancement des joins) avant de générer un plan physique exécutable. À NE PAS confondre avec **CatBoost** (algo de ML totalement différent). Le secret de la perf Spark vs Pandas.

**CatBoost** [J2] — Algorithme de **gradient boosting** (famille **XGBoost**, **LightGBM**). Construit des arbres de décision successifs, chaque arbre corrigeant les erreurs du précédent. Avantage : gère nativement les variables catégorielles (nom du jockey, hippodrome) sans encodage manuel. Utilisé dans le cas hippique.

**Classification** [J2] — Tâche de ML supervisée où `y` est catégoriel : spam/pas spam, accident grave/léger, top5/pas top5. Métriques typiques : **accuracy**, **precision**, **recall**, **F1**, **ROC-AUC**, **PR-AUC**, **confusion matrix**.

**Cluster computing** [J1] — Faire travailler ensemble plusieurs machines reliées en réseau pour exécuter un calcul. La base de **Hadoop** et **Spark**. À opposer à un seul gros serveur (scalabilité verticale).

**Cluster Manager (Spark)** [J1] — Composant qui alloue les ressources (CPU, RAM) aux applications Spark sur un cluster. 3 options majeures : standalone (Spark natif), **YARN** (Hadoop), Kubernetes. Discute avec le **Driver** pour lancer les **Executors**.

**Clustering** [J2] — Tâche de ML non supervisée : regrouper des points similaires sans cible. Algorithmes principaux : **K-means** (sphérique, nb de clusters fixé), **DBSCAN** (densité, détecte outliers). Cas d'usage : segmentation client, détection d'anomalies.

**Colab (Google Colab)** [J1+J2] — Environnement de notebooks Python gratuit dans le navigateur, basé sur Jupyter. Utilisé pour tous les ateliers de B3 (apprentissage). La production B3 se fait sur **Azure** (J3-J4).

**ColumnTransformer (sklearn)** [J2] — Outil Scikit-learn qui applique des transformations différentes à des colonnes différentes du DataFrame. Ex : OneHotEncoder sur les colonnes catégorielles + StandardScaler sur les colonnes numériques, en parallèle. Brique essentielle d'un **Pipeline (sklearn)** propre.

**Confusion matrix** [J2] — Tableau 2x2 (en binaire) qui croise prédictions et vraie classe : TP, FP, TN, FN. Permet de voir les types d'erreurs. Indispensable quand le coût des FP ≠ coût des FN (fraude, médical).

**Cotes PMU** [J2] — Probabilités implicites du marché PMU sur les chevaux d'une course. Dans le cas hippique, utilisées comme **feature** : preuve d'utilité = sans cotes le modèle fait 3.07/5 vs marché seul 2.77/5 → l'expertise (ferrure, **latéralité**) apporte 5.7% + 2.7%.

**Cross-validation (CV)** [J2] — Méthode de validation robuste : on découpe le train set en k plis (k-fold, typiquement 5), on entraîne sur k-1 plis et valide sur le restant, k fois. La moyenne des scores donne une métrique stable. Variantes : k-fold simple, **stratifiée** (préserve la proportion des classes), **temporal CV** (chronologique).

---

## D

**DAG (Directed Acyclic Graph)** [J1] — Graphe orienté sans cycle. En Spark, c'est la représentation interne des **transformations** accumulées avant une **action**. **Catalyst optimizer** et le scheduler manipulent ce DAG pour optimiser et planifier l'exécution. Visualisable dans la **Spark UI**.

**Data Lake** [J1] — Système de stockage qui conserve les données brutes dans leur format d'origine (CSV, JSON, images, logs). **Schema-on-read** : structure définie au moment de la lecture. Ex : bucket S3, cluster **HDFS**, Azure Blob.

**Data leakage** [J2] — Erreur méthodologique où le modèle ML a accès à des informations qu'il ne devrait pas avoir au moment de la prédiction. 3 cas typiques : (1) **scaling** avant **split train/val/test**, (2) feature qui contient indirectement la cible, (3) données temporelles avec random split au lieu de **temporal CV**. Symptôme : score validation trop beau pour être vrai, qui s'effondre en prod.

**Data Warehouse** [J1] — Base de données optimisée pour l'analyse (OLAP). Données nettoyées, structurées et organisées avant chargement (**schema-on-write**). Ex : Redshift, **BigQuery**, Snowflake, Azure Synapse. À opposer au **Data Lake**.

**DataFrame** [J1+J2] — Structure de données tabulaire (lignes et colonnes). En Pandas : in-memory une machine. En **Spark** : distribuée sur un cluster, avec optimisation **Catalyst**. API riche : `.filter()`, `.groupBy()`, `.join()`, `.agg()`. Équivalent in-memory d'une table SQL.

**Databricks** [J1] — Plateforme commerciale (cloud) construite autour de **Spark**, fondée par les créateurs du framework. Notebooks managés, MLflow intégré, autoscaling. Databricks Community Edition = backup gratuit si Colab + Spark pose problème.

**DBSCAN** [J2] — Algorithme de **clustering** par densité : un cluster = zone dense de points, les points isolés deviennent "outliers" (label -1). Avantages vs **K-means** : pas besoin de fixer le nombre de clusters, détecte les outliers, gère les formes non-sphériques. Inconvénient : sensible aux hyperparamètres `eps` et `min_samples`.

**Déduplication** [J1] — Processus d'identification et fusion des enregistrements en double dans une base. Techniques : match exact (nom + coordonnées <100m), match flou (**Levenshtein**, **fuzzy match**), match par attribut (téléphone, email). Couche centrale d'un pipeline **ETL** de consolidation. Voir **Golden Record**.

**Document AI** [J1] — Service (Google, Azure) qui extrait des données structurées d'un document non structuré (PDF, scan, image) : facture, passeport, contrat. Brique d'enrichissement IA dans le pipeline Cosa Travel (extraction visa, billets). Vecteur d'attaque potentiel : **prompt injection** via texte invisible.

**Driver (Spark)** [J1] — Processus pilote d'une application Spark. Contient le `SparkContext`, parse le code utilisateur, génère le **DAG**, demande des ressources au **Cluster Manager**, distribue les tâches aux **Executors**. Si le Driver crashe, l'app crashe.

---

## E

**EDA (Exploratory Data Analysis)** [J2] — Phase d'exploration des données avant modélisation : `.head()`, `.describe()`, `.info()`, distributions, corrélations, valeurs manquantes, outliers. Indispensable : on ne modélise pas un dataset qu'on n'a pas regardé.

**ELT (Extract-Load-Transform)** [J1] — Variante moderne d'**ETL**. On charge d'abord les données brutes dans le **Data Lake** / Warehouse, puis on les transforme sur place (avec dbt, Spark SQL). Avantage : stockage bon marché, on garde tout, on reprocess à volonté.

**Encodage (catégoriel)** [J2] — Transformer des variables catégorielles en numériques pour un modèle ML. 3 méthodes courantes : **OneHotEncoder** (1 colonne binaire par modalité, défaut), **LabelEncoder** (ordinal — attention à la fausse hiérarchie), **TargetEncoder** (remplacer par la moyenne de y, risque de **data leakage** si pas dans un **Pipeline (sklearn)**).

**Enrichissement IA** [J1] — Étape d'un pipeline ETL où l'on utilise un modèle IA pour extraire ou inférer des données (catégorisation, extraction depuis PDF, normalisation). Dans Cosa Travel : **Document AI** pour visas, Gemini API pour normalisation textuelle.

**ETL (Extract-Transform-Load)** [J1] — Pipeline classique de traitement de données. Extract : récupérer depuis les sources. Transform : nettoyer, structurer, dédupliquer. Load : charger vers la destination. C'est le quotidien d'un Data Engineer. Le projet fil rouge B3 est un mini-ETL.

**Executor (Spark)** [J1] — Processus worker qui exécute les tâches Spark sur un nœud du cluster. Stocke aussi les **partitions** en RAM. Le **Driver** distribue le travail aux Executors. Plus d'executors = plus de parallélisme (jusqu'à la limite du **shuffle**).

**`.explain()`** [J1] — Méthode Spark qui affiche le **plan d'exécution** d'un **DataFrame** : plan parsé, plan analysé, plan optimisé par **Catalyst**, plan physique. Utile pour comprendre pourquoi une requête est lente (shuffle, broadcast, predicate pushdown). Démontré en atelier 1 J1.

---

## F

**F1 score** [J2] — Métrique de classification = moyenne harmonique de **precision** et **recall**. Va de 0 à 1. Pertinent quand on veut équilibrer faux positifs et faux négatifs, surtout sur classes déséquilibrées. F1 macro = moyenne sur les classes ; F1 weighted = pondéré par effectif.

**Feature** [J2] — Variable explicative `X` utilisée par un modèle ML pour prédire `y`. Ex : surface, nb pièces, code postal pour prédire un prix immobilier. Les bonnes features font 80% de la perf d'un modèle.

**Feature engineering** [J2] — Création de nouvelles features à partir des données brutes. Ex : extraire le mois d'une date, calculer un ratio (surface/pièces), one-hot encoder un catégoriel. Étape la plus créative et la plus impactante du pipeline ML. Cas hippique : 29 features construites (marché, cheval, expert).

**Feature importance** [J2] — Mesure de la contribution de chaque **feature** à la prédiction. Méthodes : impureté (RandomForest), permutation importance, SHAP values. Permet de comprendre le modèle et de simplifier (drop features inutiles).

**Fuzzy match (matching flou)** [J1] — Reconnaissance de chaînes proches mais non identiques : "Hôtel de Paris" vs "Hotel Paris". Algos : **Levenshtein**, Jaro-Winkler, n-grammes. Cœur des opérations de **déduplication** sur données saisies à la main.

---

## G

**GFS (Google File System)** [J1] — Système de fichiers distribué créé par Google (paper 2003). Découpe les fichiers en blocs de 64-128 Mo, les répartit sur des centaines de machines, et les réplique 3 fois. A inspiré **HDFS**. Premier maillon de la chaîne Big Data moderne.

**Golden Record** [J1] — Enregistrement unique et canonique résultant de la fusion de plusieurs sources pour une même entité. Contient les meilleures données de chaque source, avec un audit trail complet. Résultat final d'un pipeline ETL de consolidation. Ex Cosa Travel : 1 hôtel = 1 golden record consolidé depuis KML + Mendix + DMC.

**GradientBoosting (sklearn)** [J2] — Algorithme d'ensemble qui construit des arbres de décision séquentiellement, chaque arbre corrigeant les erreurs résiduelles du précédent. Sklearn fournit `GradientBoostingRegressor` / `GradientBoostingClassifier`. Plus rapide en perf qu'un **RandomForest**, mais plus lent à entraîner et plus sensible aux hyperparamètres. Versions modernes : **XGBoost**, **LightGBM**, **CatBoost**.

**GridSearchCV** [J2] — Outil sklearn qui teste exhaustivement toutes les combinaisons d'hyperparamètres dans une grille, avec **cross-validation**. Renvoie le meilleur jeu d'hyperparamètres. Coûteux ; alternatives : `RandomizedSearchCV` (échantillonne), Optuna (bayésien).

---

## H

**Hadoop** — voir **Apache Hadoop**.

**HDFS (Hadoop Distributed File System)** [J1] — Système de fichiers distribué de **Hadoop**. Inspiré de **GFS**. Découpe les fichiers en blocs, les répartit sur un cluster, les réplique 3 fois pour la **tolérance aux pannes**. Le NameNode sait où est chaque bloc.

**Hyperparamètres** [J2] — Réglages d'un modèle qui ne sont PAS appris par `.fit()` mais fixés en amont : profondeur d'arbre, learning rate, nombre de voisins K, regularisation. Distingués des "paramètres" (poids appris). Tunés via **GridSearchCV** ou Optuna, toujours avec **cross-validation**.

---

## I

**In-memory computing** [J1] — Stratégie d'exécution où les données restent en RAM entre les étapes, au lieu d'être écrites sur disque. C'est la différence fondamentale **Spark** vs **MapReduce** Hadoop → 10-100x plus rapide. Limite : la RAM est plus chère et moins durable que le disque.

---

## J

**JSON (JavaScript Object Notation)** [J1] — Format texte léger et lisible, structure clé-valeur, supporte objets imbriqués et tableaux. Format natif de **MongoDB** et des APIs web. Utilisé en J1 atelier 2 comme 2ème source du mini-pipeline.

---

## K

**K-means** [J2] — Algorithme de **clustering** : K clusters fixés à l'avance, chaque point assigné au centre le plus proche, centres recalculés itérativement. Rapide, simple, fonctionne bien sur clusters sphériques. Faiblesses : nombre K à choisir (méthode du coude), sensible aux outliers, ne marche pas sur formes complexes (cf. **DBSCAN**).

**Kafka (Apache)** [J1] — Plateforme de streaming distribuée. Fonctionne comme un **bus de données** : producteurs envoient des événements dans des "topics", consommateurs les lisent. Utilisé pour ingestion temps réel, logs, event-driven architecture. Créé par LinkedIn.

---

## L

**Latéralité (cheval)** [J2] — Feature du cas hippique : préférence d'un cheval pour les pistes gauche/droite. Apporte 2.7% de gain de performance dans le modèle prédictif Quinté+. Exemple typique de **feature engineering** issue d'expertise métier.

**Lazy evaluation** [J1] — Stratégie d'exécution où rien ne se passe tant que le résultat final n'est pas demandé. **Spark** accumule les **transformations** (`.filter`, `.map`, `.groupBy`) dans un **DAG**, puis attend une **action** (`.show`, `.collect`) pour exécuter. Permet à **Catalyst optimizer** de réordonner le plan pour optimiser.

**Learning curve** [J2] — Graphique qui montre l'évolution du score (train et val) selon la taille du train set ou le nombre d'itérations. Diagnostic clé : si train >> val → **overfitting** ; si les deux courbes plafonnent bas → underfitting ; si l'écart se réduit avec plus de données → on en veut plus.

**Levenshtein (distance de)** [J1] — Mesure de la différence entre deux chaînes : nombre minimum d'opérations (insertion, suppression, substitution) pour passer de l'une à l'autre. Ex : "Hôtel Paris" vs "Hôtel de Paris" → distance 3. Algorithme classique de **fuzzy match** et **déduplication**.

**LightGBM** [J2] — Algorithme de **gradient boosting** open source (Microsoft). Variante de **XGBoost** optimisée pour la vitesse et la mémoire (croissance "leaf-wise" plutôt que "level-wise"). Performant sur datasets tabulaires moyens à grands.

---

## M

**MAE (Mean Absolute Error)** [J2] — Métrique de **régression** : moyenne des erreurs absolues `|y_pred - y_true|`. Robuste aux outliers, interprétable dans l'unité de y (ex : 15 000 € d'erreur moyenne sur prix immobilier). À comparer à **RMSE** (qui pénalise plus fortement les grosses erreurs).

**MapReduce** [J1] — Modèle de programmation pour le traitement distribué inventé par Google (paper 2004). Deux étapes : **Map** (chaque machine traite sa partition en parallèle) → **Reduce** (on rassemble et agrège). Analogie : compter les mots dans 1000 livres avec 1000 personnes. À la base d'**Hadoop**, supplanté par **Spark** pour les workloads itératifs.

**Master data** [J1] — Données de référence partagées par toute l'entreprise : clients, produits, fournisseurs. Doivent être uniques, consolidées, à jour. La **System of Record (SoR)** est le système qui fait autorité sur une master data. Voir **Golden Record**.

**Matching flou** — voir **Fuzzy match**.

**Métriques (régression vs classification)** [J2] — Régression : **MAE**, **RMSE**, **R²**. Classification : **accuracy**, **F1**, **precision**/**recall**, **ROC-AUC**, **PR-AUC**, **confusion matrix**. Le choix dépend du type de problème ET du coût asymétrique des erreurs.

**MLflow** [J2] — Plateforme open source de tracking et déploiement de modèles ML (créée par Databricks). Logs des runs, métriques, hyperparamètres, artefacts. Positionné en J2 mais approfondi au J4 (mise en production).

**MLlib** [J1] — Bibliothèque de Machine Learning intégrée à **Spark**. Algorithmes distribués (régression, classification, clustering, recommandation). Utile quand le dataset ne tient pas en RAM d'une machine. Mention rapide en J1, peu utilisé dans le cours (on reste sur Scikit-learn).

**MongoDB** [J1] — Base **NoSQL** orientée document. Stocke en BSON (JSON binaire). Schéma flexible : chaque document peut avoir des champs différents. Gratuit et open source.

---

## N

**Neo4j** [J1] — Base **NoSQL** orientée graphe : stocke nœuds et relations. Idéale pour réseaux sociaux, détection de fraude, recommandation. Une des 4 familles **NoSQL** (avec document, clé-valeur, colonnes larges).

**NoSQL (Not Only SQL)** [J1] — Famille de bases qui ne reposent PAS sur le modèle relationnel SQL classique. 4 sous-familles : **document** (**MongoDB**), **clé-valeur** (**Redis**), **colonnes larges** (**Cassandra**, HBase), **graphe** (**Neo4j**). Avantages : schéma flexible, scalabilité horizontale, données hétérogènes.

---

## O

**OneHotEncoder** [J2] — Encodage catégoriel : transforme une colonne avec K modalités en K colonnes binaires (0/1). Ex : "ville" → "ville_paris", "ville_lyon", "ville_marseille". Par défaut dans sklearn `ColumnTransformer`. Inconvénient : explose le nombre de colonnes si forte cardinalité.

**Overfitting** [J2] — Un modèle qui a "appris par cœur" les données d'entraînement, au lieu d'apprendre les patterns. Symptôme : score excellent sur train, mauvais sur val/test. Analogie : élève qui mémorise les exos sans comprendre la méthode → s'effondre à l'examen. Diagnostiquer avec **learning curve** ou **cross-validation**. Combattre par régularisation, plus de données, moins de features.

---

## P

**Partitionnement (Spark)** [J1] — Découpage logique d'un **DataFrame** en morceaux (partitions) traités en parallèle par les **executors**. Bon partitionnement = bon parallélisme. Mauvais partitionnement (trop, trop peu, déséquilibré) = perf catastrophique, ou **shuffle** énormes.

**PCA (Principal Component Analysis)** [J2] — Méthode de **réduction de dimension** linéaire : trouve les axes de plus forte variance dans les données, projette dessus. Sortie : N composantes orthogonales triées par variance expliquée. Cas d'usage : compression, visualisation 2D-3D, débruitage. Très rapide. À comparer à **t-SNE** / **UMAP** (non linéaires).

**Persona (Cosa Travel)** [J1] — Application client de Cosa Travel = **System of Record** des profils clients dans le pipeline ETL. Master pour identité, préférences. Synchro vers Odoo (facturation) en unidirectionnel via **Pub/Sub**.

**Pipeline (data)** [J1] — Chaîne d'étapes orchestrée qui transporte la donnée depuis ses sources jusqu'à sa destination : collecte → nettoyage → enrichissement → stockage → analyse → viz. En B3, le projet fil rouge est un mini-pipeline data + ML.

**Pipeline (sklearn)** [J2] — Objet Scikit-learn qui chaîne transformations (preprocessing) et modèle final dans un seul objet. Avantages : (1) appel unique à `.fit()` / `.predict()`, (2) évite le **data leakage** car le preprocessing est appris UNIQUEMENT sur le train, (3) prêt à sérialiser pour production. Pattern standard : `Pipeline([('prep', ColumnTransformer(...)), ('model', RandomForest())])`.

**Pipeline 7 couches (Cosa Travel)** [J1] — Architecture du pipeline ETL Cosa Travel en 7 étapes : (1) ingestion sources, (2) nettoyage, (3) **déduplication**, (4) **résolution de conflits** + **scoring de fiabilité**, (5) **enrichissement IA**, (6) **revue humaine** des cas ambigus, (7) **Golden Record** publié vers consommateurs. Utilisé comme illustration B3 du projet fil rouge.

**Plan d'exécution (Spark)** — voir **`.explain()`** et **DAG**.

**PR-AUC (Precision-Recall AUC)** [J2] — Aire sous la courbe precision-recall. Métrique de **classification** plus pertinente que **ROC-AUC** sur classes très déséquilibrées (fraude 0.1%, défaut de paiement) : se concentre sur les positifs rares. À privilégier dès que la classe positive < 10%.

**Precision** [J2] — Métrique de classification = TP / (TP + FP) = "parmi mes prédictions positives, combien sont vraiment positives ?" Importante quand un faux positif coûte cher (spam → bloquer un mail légitime).

**Pub/Sub** [J1] — Pattern de messagerie asynchrone : un producteur publie un événement dans un "topic", tous les abonnés reçoivent le message. Découple les systèmes. Implémentations : Google Cloud Pub/Sub, **Kafka**, Azure Event Hubs. Utilisé dans Cosa Travel pour sync Persona → Odoo.

---

## Q

**Quinté+** [J2] — Pari hippique PMU : prédire les 5 premiers chevaux d'une course donnée. Cas réel utilisé en J2 pour illustrer pipeline ML complet : 11 360 courses sur 3 ans, 29 features, **temporal CV** 5-fold, résultat 3.24/5 ± 0.06. Voir **backtest vs production**, **latéralité**, **cotes PMU**.

---

## R

**R² (coefficient de détermination)** [J2] — Métrique de **régression** : proportion de variance expliquée par le modèle. Va de -∞ à 1. R² = 1 → parfait, R² = 0 → équivalent à prédire la moyenne, R² < 0 → pire que la moyenne. Attention : R² élevé n'implique PAS un bon modèle (overfit possible).

**RandomForest** [J2] — Algorithme d'ensemble : entraîne plusieurs arbres de décision sur des sous-échantillons bootstrap avec sous-ensembles aléatoires de features, agrège par vote (classif) ou moyenne (reg). Robuste, peu sensible aux hyperparamètres, donne une **feature importance**. Bon baseline d'ensemble avant de tester des **gradient boosting**.

**RDD (Resilient Distributed Dataset)** [J1] — Structure de données fondamentale historique de **Spark**. Collection distribuée tolérante aux pannes (lineage rejoué si perte). API bas niveau, supplantée par **DataFrame** en pratique car Catalyst optimizer ne s'applique qu'au DataFrame. À connaître pour la culture, peu utilisé en production.

**Recall (rappel)** [J2] — Métrique de classification = TP / (TP + FN) = "parmi les vrais positifs, combien j'en ai trouvé ?" Importante quand un faux négatif coûte cher (cancer manqué, fraude non détectée).

**Redis** [J1] — Base **NoSQL** clé-valeur en mémoire. Ultra-rapide (microsecondes). Utilisée pour cache, sessions web, compteurs temps réel, queues légères. Une des 4 familles **NoSQL**.

**Régression** [J2] — Tâche de ML supervisée où `y` est continu : prix, durée, popularité, score. Métriques : **MAE**, **RMSE**, **R²**. Modèles courants : LinearRegression, **RandomForest** regressor, **GradientBoosting** regressor, **XGBoost** regressor.

**Résolution de conflits** [J1] — Étape d'un pipeline ETL où plusieurs sources contradictoires existent pour un même champ d'une même entité. Stratégies : (1) **trust hierarchy** (la source la plus fiable gagne), (2) **scoring de fiabilité** (confidence score), (3) **revue humaine** si confiance trop basse. Centrale dans la consolidation Cosa Travel.

**Revue humaine** [J1] — Étape d'un pipeline ETL où un opérateur humain valide les cas ambigus que l'IA n'a pas pu trancher (confidence < seuil). Garde-fou anti-**data poisoning** et anti-**prompt injection**. Dans Cosa Travel : déclenchée si confidence < 0.90.

**RMSE (Root Mean Squared Error)** [J2] — Métrique de **régression** : racine de la moyenne des carrés des erreurs. Pénalise fortement les grosses erreurs (vs **MAE**). Même unité que `y`. Si RMSE >> MAE → quelques grosses erreurs portent le score → enquêter sur outliers.

**ROC-AUC** [J2] — Aire sous la courbe ROC (taux de vrais positifs vs taux de faux positifs). Métrique de **classification** binaire, de 0.5 (aléatoire) à 1.0 (parfait). Pertinent sur classes équilibrées. Sur classes très déséquilibrées, préférer **PR-AUC**.

**ROI (Return On Investment)** [J2] — Métrique business : (gain - coût) / coût. Dans le cas hippique : +914% en backtest, mais variance énorme → ROI réel beaucoup plus bas. Rappel : un ROI de backtest n'est PAS un ROI de production.

---

## S

**Scalabilité horizontale vs verticale** [J1] — Verticale (scale-up) : faire plus gros = plus de CPU/RAM sur 1 machine. Plafond physique, panne = tout perdu. Horizontale (scale-out) : faire plus nombreux = ajouter des machines. Linéaire si bien architecturé, tolérance aux pannes. **Hadoop**, **Spark**, **NoSQL** privilégient l'horizontale.

**Scaling (sklearn)** [J2] — Mise à l'échelle des features numériques pour qu'elles aient des magnitudes comparables. **StandardScaler** (moyenne=0, écart-type=1, le défaut), **MinMaxScaler** (entre 0 et 1, pour images / réseaux de neurones), **RobustScaler** (médiane + IQR, robuste aux outliers). Indispensable pour SVM, KNN, régression linéaire, réseaux. Doit être appris UNIQUEMENT sur le train (sinon **data leakage**).

**Schema-on-read vs schema-on-write** [J1] — Schema-on-read (**Data Lake**, **MongoDB**) : on stocke brut, la structure est imposée à la lecture. Flexible mais qualité non garantie. Schema-on-write (SQL, **Data Warehouse**) : on impose un schéma à l'écriture. Strict mais fiable.

**Scikit-learn (sklearn)** [J2] — Bibliothèque Python centrale du ML classique. API unifiée `.fit()` / `.predict()` / `.transform()`. Couvre régression, classification, clustering, preprocessing, pipelines, **cross-validation**, **GridSearchCV**, métriques. Le couteau suisse du ML tabulaire avant les frameworks deep learning.

**Shuffle (Spark)** [J1] — Réorganisation des données entre **executors** lors d'opérations comme `groupBy`, `join`, `distinct`, `repartition`. C'est l'opération la plus coûteuse en Spark (réseau + disque). À minimiser : préférer **broadcast join** si possible, repartitionner finement.

**Spark (Apache)** [J1] — Framework open source de traitement distribué (2014). Successeur de **MapReduce** **Hadoop**. Travaille en mémoire (**in-memory computing**), donc 10-100x plus rapide. Modules : **Spark SQL**, **Spark Streaming**, **MLlib**, GraphX. Syntaxe **DataFrame** proche de Pandas.

**Spark SQL** [J1] — Module Spark qui permet d'exécuter du SQL sur des **DataFrames**. Bénéficie de **Catalyst optimizer**. Permet de mixer SQL et API DataFrame dans le même script. C'est la couche la plus utilisée de Spark.

**Spark Streaming** [J1] — Module de **Spark** pour le traitement de données en flux (vs batch). Modèle micro-batch : on agrège des micro-fenêtres temporelles (1 sec, 10 sec) et on traite chacune comme un batch. Alternative : Apache Flink (vrai streaming continu). Évolution moderne : Structured Streaming sur DataFrame API.

**Spark UI** [J1] — Interface web (port 4040) exposée par Spark pendant l'exécution d'un job. Affiche jobs, stages, tasks, **DAG**, durées, mémoire, shuffle. Outil n°1 pour diagnostiquer un job lent. Démontré en atelier 1 J1.

**Split train/val/test** [J2] — Découpage du dataset en 3 sous-ensembles. **Train** : pour `.fit()`. **Val** (validation) : pour comparer modèles et tuner **hyperparamètres**. **Test** : ouvert UNE SEULE FOIS à la fin pour une estimation honnête de la perf prod. Règle d'or : si on optimise sur le test, on triche. Sur données temporelles → **temporal CV** obligatoire.

**StandardScaler** [J2] — **Scaling** standard : `(x - mean) / std`. Résultat centré sur 0, écart-type 1. Le scaling par défaut pour la plupart des cas.

**System of Record (SoR)** [J1] — Système qui fait autorité pour un type de donnée. Règle : celui qui édite la donnée en est le master. Ex Cosa Travel : Persona = master pour profils clients, Odoo = master pour facturation. La synchro est unidirectionnelle : master → consommateurs, jamais l'inverse.

---

## T

**Temporal cross-validation (Temporal CV)** [J2] — Méthode de **cross-validation** pour données temporelles. Au lieu d'un random split (qui crée du **data leakage**), on entraîne sur les mois 1-6 et on teste sur le mois 7, puis 1-7 / 8, etc. Règle d'or : si ton dataset a une date, TEMPORAL SPLIT obligatoire. Illustré par le cas hippique (3.24/5 ± 0.06).

**Tolérance aux pannes** [J1] — Capacité d'un système distribué à continuer à fonctionner si une machine tombe. **HDFS** : réplique chaque bloc 3 fois. **Spark** : rejoue le lineage RDD/DAG sur les partitions perdues. Sans tolérance aux pannes, un cluster de 1000 machines tomberait toutes les heures.

**Transformation (Spark)** [J1] — Opération **Spark** qui produit un nouveau **DataFrame** / RDD SANS déclencher de calcul. Exemples : `.filter()`, `.map()`, `.groupBy()`, `.join()`. Les transformations s'accumulent dans un **DAG** et ne s'exécutent que lors d'une **action** (**lazy evaluation**).

**t-SNE** [J2] — Méthode de **réduction de dimension** non linéaire, optimisée pour la visualisation 2D/3D. Préserve les distances locales (points proches en HD restent proches en BD). Lente, non déterministe, mauvaise pour les distances globales. Privilégier **UMAP** pour les gros datasets.

---

## U

**UMAP (Uniform Manifold Approximation and Projection)** [J2] — Méthode de **réduction de dimension** non linéaire, alternative à **t-SNE**. Plus rapide, préserve mieux la structure globale, scalable. Devenue standard de la visualisation 2D moderne (single-cell biology, embeddings NLP).

---

## V

**Variance d'un modèle** [J2] — Sensibilité d'un modèle aux fluctuations du train set. Modèles à forte variance (arbres profonds, KNN K=1) overfittent facilement. À évaluer par l'écart-type des scores en **cross-validation**. Cas hippique : 3.24/5 ± 0.06 → variance faible, robuste. Variance énorme = on ne peut PAS faire confiance au modèle en prod.

---

## X

**XGBoost** [J2] — Algorithme de **gradient boosting** open source (Tianqi Chen). Bibliothèque de référence pour ML tabulaire, gagne la plupart des compétitions Kaggle. Optimisations : régularisation L1/L2, gestion des valeurs manquantes, parallélisation. Versions concurrentes : **LightGBM**, **CatBoost**.

---

## Y

**YARN (Yet Another Resource Negotiator)** [J1] — Gestionnaire de ressources de **Hadoop**. Décide quelle machine du cluster exécute quelle tâche. Composant clé pour distribuer le travail entre les nœuds. Un des 3 **Cluster Manager** Spark possibles (avec standalone et Kubernetes).

---

## 5V (chiffres en tête)

**5V (les cinq V du Big Data)** [J1] — Framework pour caractériser le Big Data, supposé acquis à l'entrée en B3 (quiz diagnostic) :
- **Volume** : quantité massive de données (To, Po, Eo)
- **Vélocité (Velocity)** : rapidité de génération et de traitement
- **Variété (Variety)** : formats hétérogènes (JSON, images, texte, vidéo)
- **Véracité (Veracity)** : fiabilité et qualité des données
- **Valeur (Value)** : capacité à transformer la donnée en décision utile
