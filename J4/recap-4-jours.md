# Récap des 4 jours B3 Data & IA

> À projeter en début de J4 (9h15-9h45). Public : tous les étudiants.

---

## La chaîne complète qu'on a parcourue

```
J1 — Données brutes       J2 — Modèle ML            J3 — Produit              J4 — Industrialiser
─────────────────         ──────────────            ──────────                ───────────────────
   CSV / Spark      →     model.pkl                 App React+FastAPI    →    CI/CD + monitoring
   nettoyage              comparaisons              déployée HF Spaces        soutenance /20
   ETL, lazy eval         métriques                 (URL publique)            rapport individuel
```

**On a fait** la même chaîne qu'un Data Engineer / Data Scientist en mission, du CSV brut à l'app qui tourne en prod accessible depuis n'importe quel téléphone.

---

## Ce que chaque jour vous a apporté

### J1 (20 mai) — Big Data approfondi

| Acquis | Outil | À retenir |
|---|---|---|
| Manipuler des datasets > 1 Go sans planter | **Spark** (PySpark) | Lazy evaluation = rien ne s'exécute tant qu'on ne demande pas une **action** |
| Différence transformations / actions | `.filter()` `.select()` (transfo) vs `.show()` `.count()` (action) | Compter le nombre de jobs Spark dans la Spark UI |
| Différence SQL / NoSQL | Postgres, MongoDB | SQL = schéma rigide, ACID ; NoSQL = schéma flexible, eventual consistency |
| ETL : extract / transform / load | Pandas / Spark | Le pipeline doit être **reproductible** (mêmes inputs → mêmes outputs) |

**Question type soutenance** : *« Pourquoi votre EDA est-il essentiel avant de modéliser ? »*

### J2 (21 mai) — Machine Learning

| Acquis | Outil | À retenir |
|---|---|---|
| Pipeline ML complet | **Scikit-learn** | `Pipeline()` = preprocessing + modèle → pas de leakage entre train et test |
| 3 familles de modèles | Régression / classification / clustering | Toujours **commencer baseline simple** (régression linéaire ou logistique) |
| Train / val / test split | `train_test_split()` | Stratifier si classes déséquilibrées (`stratify=y`) |
| Métriques selon le problème | RMSE/MAE pour régression, accuracy/precision/recall/F1 pour classif | **Accuracy seule = piège** si dataset déséquilibré → utiliser F1 ou ROC AUC |
| Leakage | Anti-patterns | Ne JAMAIS fit le scaler sur le test set. Toujours `fit` sur train, `transform` sur test |
| Sérialisation modèle | `joblib.dump(model, "model.pkl")` | `.pkl` = passeport du modèle entre J2 et J3 |

**Question type soutenance** : *« Comment avez-vous évité le data leakage ? »*

### J3 (26 mai) — Produit (React + FastAPI + HF Spaces)

| Acquis | Outil | À retenir |
|---|---|---|
| Piloter un agent de code | **Claude Code** | Boucle **Explore → Plan → Implement → Verify** + `CLAUDE.md` + plan mode |
| Construire une app de prod | **React + Vite + TypeScript + Tailwind** | Composants, hooks (useState, useEffect, useQuery), composition |
| Servir un modèle ML via API | **FastAPI** | Endpoint `/api/predict`, Pydantic pour valider les inputs, async I/O |
| Déployer sur cloud | **HF Spaces Docker** (port 7860) | `git push hf main` = déploie. Dockerfile multi-stage (front + back unifiés) |
| Cohérence front ↔ back | `VITE_API_URL=/api` + StaticFiles | FastAPI sert l'API ET le bundle React. Pas de CORS en prod, même origine |

**Question type soutenance** : *« Comment redéployez-vous votre app après un changement ? »*

### J4 (27 mai) — Industrialiser + soutenance

| Acquis | Outil | À retenir |
|---|---|---|
| Automatiser le déploiement | **GitHub Actions** | Workflow YAML, triggers (push/PR/cron), secrets (HF_TOKEN) |
| Documenter un projet | **README pro + mermaid** | Badges, sections Install/Dev/Deploy, schéma d'archi |
| Monitorer en prod | Healthcheck + UptimeRobot | `/api/health` doit toujours retourner 200 |
| Présenter un produit | **Soutenance /20** | 10 min structurées + démo live + Q&A solides |
| Positionnement Azure | Culture | Ce qu'on a fait sur HF = transposable sur Azure App Service en mastère |

**Question type soutenance** : *« Si demain vous aviez 1000 utilisateurs, qu'est-ce qui pète en premier ? »*

---

## Check minimum d'acquis avant soutenance

Si tu ne peux pas répondre à ces 10 questions **sans hésiter**, va voir le formateur pendant l'atelier matin. Ce sont les bases attendues.

1. Spark — c'est quoi la **lazy evaluation** et pourquoi c'est utile ?
2. ML — c'est quoi le **leakage** et comment l'éviter ?
3. ML — pourquoi mesure-t-on les performances sur le **test set** et pas le train ?
4. Métriques — sur un dataset 95 % négatif / 5 % positif, accuracy = 95 % en prédisant toujours négatif. C'est utile ?
5. Pipeline — pourquoi un `Pipeline()` sklearn est-il plus sûr qu'un preprocessing manuel ?
6. Claude Code — c'est quoi la **boucle des 4 étapes** ?
7. React — c'est quoi le rôle de **`useQuery`** (TanStack) ?
8. FastAPI — à quoi sert **Pydantic** dans un endpoint ?
9. HF Spaces — pourquoi le **port 7860** dans le Dockerfile ?
10. CI/CD — pourquoi un **secret** ne doit jamais être committé dans le repo ?

---

## Les 3 ponts entre les jours

> Ce qui fait que c'est UN projet et pas 4 cours indépendants.

```
J1 produit un dataset propre        →  J2 le consomme pour entraîner
J2 produit model.pkl                →  J3 le sert via FastAPI
J3 produit une app déployée HF      →  J4 l'industrialise (CI/CD + README + monitoring)
```

Chaque jour **consomme** ce que le précédent a produit. Si vous décrochez sur l'un, le suivant casse.

---

## La pyramide de votre projet pour la soutenance

```
                        🎤 Soutenance /20
                       /                  \
                  démo live           pitch structuré
                      |                       |
        ────── App React+FastAPI HF ──────
                      |
                  model.pkl
                      |
              dataset propre
                      |
                CSV brut
```

**Pendant la soutenance**, partez de la pointe (le problème métier) et descendez vers la base si on vous le demande. **Ne commencez pas par le code** — commencez par **le problème que vous résolvez**.

---

## Si vous voulez aller plus loin (après la formation)

- **DataCamp** — modules de rattrapage sur ce qu'on n'a pas approfondi
- **Kaggle Learn** — exercices gratuits niveau intermédiaire
- **fast.ai** — deep learning pratique
- **Microsoft Learn — Azure** — cf. `azure-culture.md` (positionnement mastère)
- **Anthropic Claude Code docs** — pour devenir vraiment bon en pilotage d'agent

> Le plus dur n'est pas d'apprendre 10 nouveaux outils. C'est de comprendre **comment ils s'enchaînent** dans une chaîne data complète. Cette formation vous a donné cette chaîne. Le mastère vous donnera la profondeur sur chaque maillon.
