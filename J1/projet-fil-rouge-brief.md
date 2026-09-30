# Projet fil rouge · brief et évaluation

> Data & IA · B3 DEV Sup de Vinci Nantes · 2026-2027 · formateur : Yacine Arhaliass

## L'objectif

Construire en groupe un **produit data complet** : un dataset réel, nettoyé par un pipeline reproductible, un modèle de machine learning comparé à une baseline, exposé par une API, utilisé par une interface web, déployé en ligne. À la fin, vous le défendez devant un jury, démo à l'appui.

## Modalités

- **Groupes de 2 ou 3**, formés au J1. Chaque membre porte au moins une brique (données, modèle, API, front, déploiement) et sait expliquer toutes les autres.
- **Dataset libre**, validé au J1 (critères plus bas). Maximum 2 groupes sur le même dataset.
- **Un repo GitHub par groupe**, commits réguliers et parlants, partagé avec `pando-yacine`.

## Démarrer : le starter et le second brain

1. Un membre du groupe crée le repo depuis **[b3-data-ia-projet-starter](https://github.com/pando-yacine/b3-data-ia-projet-starter)** (bouton « Use this template »), ajoute les autres membres et `pando-yacine`.
2. Le starter contient un `README.md` à remplir, un `CLAUDE.md` (les règles pour l'agent de code), un `AGENTS.md` (mêmes règles pour les autres agents) et un **second brain** dans `docs/brain/` : index et jalons, fiche projet, dataset, décisions, journal des séances, glossaire, questions.
3. Commandes Claude Code fournies : `/point` (faire le point avant une séance), `/decision` (consigner une décision), `/journal` (compte rendu de fin de séance), `/verifie` (notebooks, chiffres, fuites, secrets).

## L'IA sur le projet : autorisée, déclarée, vérifiée, comprise

- **Autorisée et encouragée** : Claude (ou un autre agent) peut écrire du code, explorer les données, documenter.
- **Déclarée** : le journal du brain garde la trace ; le rapport individuel contient une section « usage de l'IA » (ce que vous lui avez confié, ce que vous avez vérifié ou corrigé).
- **Vérifiée** : Explore, Plan, Implement, Verify. Chaque chiffre vient d'une exécution réelle, chaque diff est relu.
- **Comprise** : en soutenance, chaque membre peut expliquer n'importe quelle partie du code. « C'est l'IA qui l'a écrit » ne répond à aucune question.

## Stack

| Brique | Par défaut | Alternatives acceptées |
|---|---|---|
| Données | Pandas (+ PySpark sur une étape) | Polars, DuckDB |
| Modèle | Scikit-learn | XGBoost, LightGBM, CatBoost |
| API | FastAPI (`/predict`) | |
| Interface | React | Streamlit, Dash (outils du syllabus) |
| Déploiement | Docker sur Hugging Face Spaces | Azure App Service, AWS |
| CI/CD | GitHub Actions (bonus) | |

## Livrables, jour par jour

| Fin de | Livrable |
|---|---|
| **J1** (à rendre sous 7 jours, vendredi 9 octobre 2026, 23h59) | Repo créé depuis le starter, README sections 1 à 4, second brain initialisé (fiche projet, dataset, première décision, journal), notebook d'exploration qui tourne de haut en bas |
| **J2** | Preprocessing reproductible (train/test séparés AVANT tout traitement), baseline naïve + au moins 2 modèles comparés sur une métrique justifiée, modèle sauvegardé. Bonus : une brique non supervisée (clustering) évaluée (score de silhouette) et interprétée |
| **J3** | API FastAPI `/predict` qui charge le modèle + interface avec saisie, prédiction et 2 ou 3 visualisations, qui tourne en local |
| **J4** | Application déployée (URL publique), README pro (installation, architecture, limites), soutenance |

## Évaluation

| Part | Qui | Contenu |
|---|---|---|
| **40 % · projet continu** | groupe | 4 jalons à 10 % chacun : J1 cadrage, J2 modèle, J3 application, J4 déploiement et README. Chaque jalon est noté sur ce qui est dans le repo à l'échéance |
| **30 % · soutenance** | groupe, modulée par personne (±2 points) | 10 min de présentation avec démo live + questions. La modulation dépend des réponses individuelles |
| **30 % · rapport individuel** | individuel | 3 à 5 pages, rendu sous 7 jours après le J4, dont une section « usage de l'IA » |

Bonus : **+1** si un CI/CD GitHub Actions vert est montré en démo. Pénalité : **-1** si un secret (clé API, mot de passe) est committé dans le repo.

### Ce qu'on regarde à chaque jalon

- **J1 cadrage** : question claire (qui, quoi, pourquoi), dataset compris (taille, ce qu'une ligne représente, limites), cible et features cohérentes, métrique justifiée, baseline naïve définie, risques identifiés (fuite de données, biais, taille), second brain initialisé.
- **J2 modèle** : pipeline reproductible, pas de fuite de données, comparaison chiffrée contre la baseline, métrique commentée (« 0,85 c'est bien » ne suffit pas).
- **J3 application** : l'API répond, l'interface est lisible, les visualisations racontent quelque chose sur les données.
- **J4 déploiement** : l'URL fonctionne, le README permet à un inconnu de comprendre et relancer le projet.

### Soutenance

- **Format** : 10 minutes de présentation (problème, données, démarche, démo, limites) puis questions. Tout le groupe parle.
- **Démo** : en live, avec un **plan B** prêt (captures d'écran ou vidéo) : une démo qui plante sans plan B coûte cher.
- **Les membres sont alignés** : mêmes chiffres, mêmes métriques. Un score qui change d'un orateur à l'autre fait perdre des points.
- **On parle fort**, face au jury, pas à l'écran.

### Rapport individuel (3 à 5 pages)

Votre contribution personnelle, vos choix techniques justifiés, les difficultés et comment vous les avez surmontées, un regard critique (limites du modèle, biais des données, ce que vous referiez autrement), et l'usage que vous avez fait de l'IA.

## Choisir son dataset

**Critères de validation** : au moins 1 000 lignes et une dizaine de colonnes · une cible évidente à prédire · une source citable et une licence qui autorise l'usage · pas un dataset déjà travaillé par votre groupe en B2 · un sujet que vous savez expliquer à un non-expert.

**Où chercher** : Kaggle, data.gouv.fr, INSEE, Hugging Face datasets, API publiques (Open-Meteo, API sportives). Les [datasets de secours](../README.md#datasets-de-secours) du repo en dernier recours.

Bonus apprécié : enrichir avec une deuxième source (météo, référentiel géographique) et le justifier.

## Ce qui a fait la différence dans la promo précédente

- **Bien noté** : repo rangé (code, données, docs séparés), plusieurs modèles comparés avec des chiffres, biais et limites dits avant qu'on les demande, CI/CD démontré en live.
- **Points perdus** : démo sans plan B, un R² de 0,24 jamais remis en question, une prédiction qui renvoie toujours la même valeur (le modèle prédit la moyenne), deux membres qui annoncent deux scores différents, voix trop faible.
