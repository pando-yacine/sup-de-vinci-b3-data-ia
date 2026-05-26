# Questions de cours — révisions B3 Data & IA

> À utiliser pendant le créneau 14h-15h pour balayer les bases. **Pas une interro à apprendre par cœur** — un check que vous sauriez répondre **à voix haute en 30 sec** à chacune.

Si vous bloquez sur une question, allez voir le formateur (il circule pendant le créneau).

---

## J1 — Big Data approfondi (8 questions)

1. **Spark — lazy evaluation** : qu'est-ce que c'est et pourquoi c'est utile ?

2. **Spark — transformations vs actions** : donne 2 exemples de chaque type. Que se passe-t-il si tu n'appelles jamais une action ?

3. **Spark — DataFrame vs RDD** : quelle est la différence principale et pourquoi DataFrame est préféré aujourd'hui ?

4. **SQL vs NoSQL** : quand choisir l'un ou l'autre ? Donne un cas d'usage typique pour chaque.

5. **ETL** : à quoi correspondent les 3 lettres ? Quel maillon est généralement le plus coûteux en temps ?

6. **Reproductibilité** : qu'est-ce qui rend un pipeline data **non reproductible** ? Cite 3 causes courantes.

7. **EDA (Exploratory Data Analysis)** : pourquoi est-ce essentiel **avant** de modéliser ? Cite 3 choses que tu cherches.

8. **Manquants (`NaN`)** : quelles sont les 3 stratégies courantes pour gérer les valeurs manquantes ? Quand utilise-t-on chacune ?

---

## J2 — Machine Learning (10 questions)

9. **Pipeline sklearn** : pourquoi un `Pipeline()` est-il plus sûr qu'un preprocessing manuel ?

10. **Train / validation / test** : à quoi servent ces 3 splits ? Pourquoi ne pas juste utiliser train + test ?

11. **Data leakage** : c'est quoi exactement, et donne 2 exemples concrets de comment ça arrive.

12. **Overfitting vs underfitting** : comment les diagnostiques tu ? Quelle est la stratégie pour chacun ?

13. **Classification — accuracy** : pourquoi est-ce un piège sur un dataset déséquilibré (par exemple 95 % négatif / 5 % positif) ? Quelle métrique préférer ?

14. **Précision vs rappel (recall)** : explique chacun en 1 phrase. Quand préférer l'un à l'autre ? Donne un exemple.

15. **F1-score** : c'est quoi et pourquoi est-ce une métrique « équilibrée » ?

16. **Régression — RMSE vs MAE** : quelle est la différence ? Quand RMSE est-elle préférable ?

17. **Cross-validation** : à quoi ça sert ? Que fait `cross_val_score(model, X, y, cv=5)` ?

18. **Sérialisation modèle** : pourquoi utilise-t-on `joblib` plutôt que `pickle` ? Quel est le risque de partager un `.pkl` reçu de quelqu'un d'autre ?

---

## J3 — Produit (8 questions)

19. **Claude Code — boucle des 4 étapes** : cite-les dans l'ordre et explique pourquoi chacune est importante.

20. **CLAUDE.md** : à quoi sert ce fichier ? Que mets-tu dedans ?

21. **Plan mode (Claude Code)** : quand l'utiliser et pourquoi ? Quel est le risque de ne pas l'utiliser ?

22. **React — hooks de base** : explique le rôle de `useState`, `useEffect`, et `useQuery` (TanStack) en 1 phrase chacun.

23. **React — composant fonctionnel vs classe** : lequel est préféré aujourd'hui et pourquoi ?

24. **FastAPI — Pydantic** : à quoi sert ce module dans un endpoint ? Donne un exemple.

25. **FastAPI — async vs sync** : quelle est la différence ? Quand utiliser `async def` ?

26. **FastAPI — middleware CORS** : à quoi sert CORS ? Pourquoi en a-t-on besoin en dev (front Vite sur 5173 + back FastAPI sur 8000) ?

---

## J4 — Industrialisation & Cloud (8 questions)

27. **HF Spaces — port 7860** : pourquoi cette valeur précise ? Que se passe-t-il si tu mets 8000 dans ton Dockerfile mais 7860 dans `app_port` du README ?

28. **HF Spaces — `app_port` dans le YAML du README** : à quoi ça correspond ? Pourquoi 3 endroits doivent matcher (Dockerfile EXPOSE + uvicorn `--port` + README `app_port`) ?

29. **Dockerfile multi-stage** : à quoi ça sert ? Donne le cas d'usage typique d'un projet React + FastAPI.

30. **GitHub Actions — anatomie d'un workflow** : explique brièvement ce que sont les `jobs`, `steps`, `runs-on`, `triggers (on:)`.

31. **GitHub Actions — secrets** : pourquoi ne JAMAIS commiter un token en clair ? Comment on stocke un secret pour qu'un workflow puisse l'utiliser ?

32. **CI/CD — triggers (`on:`)** : cite 3 triggers possibles. Donne un cas d'usage pour chacun (push, pull_request, schedule).

33. **Monitoring `/api/health`** : à quoi sert un endpoint de healthcheck ? Comment l'utiliser en pratique ?

34. **Cloud — HF Spaces vs Azure** : quels sont les **trois différences principales** entre HF Spaces et Azure App Service ? Quand passer de l'un à l'autre ?

---

## Questions transversales / projet (5 questions)

35. **Stack** : peux-tu dessiner sur tableau (à main levée) le pipeline complet de ton projet, du CSV brut à l'app HF ? Y compris CI/CD ?

36. **Versioning** : si tu casses ton modèle et que ça plante en prod, comment tu reviens à la version d'avant ? Combien de temps ça prend ?

37. **Coûts** : aujourd'hui sur HF tu paies 0 €. Si tu migres sur Azure App Service B1 (~13 €/mois), qu'est-ce que tu gagnes ? Qu'est-ce que tu perds ?

38. **Sécurité** : quels sont les 3 risques sécurité principaux d'une app comme la tienne en prod ? (Input adversarial, injection, fuite de données, model theft, etc.)

39. **Évolution** : si on te demandait d'ajouter une feature « batch prediction » (uploader un CSV de 1000 lignes et obtenir 1000 prédictions), comment tu t'y prendrais ? Quelles modifs sur ton API et ton front ?

---

## Conseils de révision (5 min express)

**Sprint final** : ne lisez pas les 39 questions. Faites comme ça :

1. Parcourir uniquement les **titres de section** (1 min)
2. Identifier les **3-5 questions où vous bloquez** (2 min)
3. Aller voir le formateur ou un coéquipier pour **éclaircir ces 3-5 points** (2 min)
4. Repos cerveau jusqu'à 15h00

**Ne réviser PAS ce que vous savez déjà.** Concentrez-vous sur les trous.

---

## Notation Q&A pendant la soutenance

> Les 2-3 questions Q&A du formateur (dans les 3 min après votre pitch) pèsent dans le critère **« Soutenance orale » /3**.

| Réponse | Effet sur la note |
|---|---|
| Réponse précise, claire, 1-2 phrases | Maintient ou monte la note |
| Réponse approximative mais qui montre la compréhension | Maintient la note |
| « Je ne sais pas, mais mon intuition serait [...] » | **Maintient** la note (l'honnêteté est valorisée) |
| Réponse inventée qui est fausse | **Fait baisser** la note (le formateur le voit) |
| Silence ou « je sais pas, désolé » sans tentative | Fait baisser la note |

> Mieux vaut **dire qu'on ne sait pas** avec une piste d'intuition, que d'inventer une réponse fausse. C'est aussi ce qu'on attend de vous **en stage / en job** quand vous serez face à un client.
