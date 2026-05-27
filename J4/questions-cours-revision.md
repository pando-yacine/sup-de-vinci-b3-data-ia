# Questions de cours — révisions B3 Data & IA

> **Niveau attendu** : L3 dev fullstack qui a fait 28h de Data & IA. **Ce n'est pas un master.** Si vous savez répondre à **10 questions sur 20**, vous êtes au niveau. Si vous en avez 15+, vous êtes très bons. Si vous en avez 20+, vous êtes prêts pour un mastère data.
>
> **À utiliser** pendant le créneau 14h-15h. Pas pour apprendre par cœur — pour **vérifier que vous sauriez répondre en 30 sec à voix haute**.

Si vous bloquez sur une question, allez voir le formateur (il circule pendant le créneau).

---

## J1 — Big Data approfondi (4 questions)

1. **Big Data** — c'est quoi un « gros dataset » ? À partir de quand a-t-on besoin de Spark plutôt que Pandas ?

2. **Spark — à quoi ça sert ?** En 1 phrase. *(Pas besoin d'expliquer la lazy eval en détail, mais savoir « ça permet de traiter des données qui ne tiennent pas en RAM »)*

3. **SQL vs NoSQL** — quand préférer l'un ou l'autre ? Donne 1 exemple pour chaque.

4. **EDA (Exploratory Data Analysis)** — c'est quoi et pourquoi on en fait **avant** de modéliser ?

---

## J2 — Machine Learning (6 questions)

5. **Régression vs classification** — quelle est la différence ? Donne 1 exemple de chaque dans ton projet ou un autre projet.

6. **Train / test split** — pourquoi on sépare nos données en 2 ensembles avant d'entraîner ? Que se passe-t-il si on entraîne sur 100 % des données ?

7. **Overfitting** — c'est quoi simplement ? Comment on le détecte ?

8. **Accuracy** — qu'est-ce que ça mesure ? Pourquoi c'est trompeur si on prédit toujours « non spam » sur un dataset 99 % non-spam / 1 % spam ?

9. **Précision vs Rappel** — explique chacune en 1 phrase. *(Tu peux prendre l'exemple d'un détecteur de spam, ou de fraude bancaire.)*

10. **`model.pkl`** — c'est quoi ? À quoi ça sert ? Comment on l'utilise dans une API ?

---

## J3 — Produit (5 questions)

11. **Claude Code** — c'est quoi la grande idée ? Pourquoi on ne demande pas juste « écris-moi le code » mais on suit une **boucle** ?

12. **CLAUDE.md** — à quoi sert ce fichier dans ton repo ?

13. **React + FastAPI** — pourquoi on a une **API séparée** plutôt que de tout faire dans le front ?

14. **Endpoint `/api/predict`** — quel est son rôle dans ton projet ? Que reçoit-il en entrée ? Que renvoie-t-il en sortie ?

15. **Hugging Face Spaces** — c'est quoi ? Pourquoi on a choisi ça plutôt qu'un serveur classique ?

---

## J4 — Industrialisation (5 questions)

16. **HF Spaces — pourquoi le port 7860 ?** *(Indice : c'est une convention HF.)*

17. **Docker** — c'est quoi à quoi ça sert dans ton projet ? En quoi c'est utile pour le déploiement ?

18. **GitHub Actions — c'est quoi un workflow ?** Donne un exemple de quand un workflow se déclenche.

19. **Secret (`HF_TOKEN`)** — pourquoi ne JAMAIS commiter un token directement dans le code ? Où on le met à la place ?

20. **`/api/health`** — quel est le rôle d'un endpoint healthcheck ? À quoi peut-il servir en prod ?

---

## Conseils de révision (5 min express)

**Sprint final** : ne lisez pas les 20 questions une par une. Faites comme ça :

1. **Parcourir uniquement les titres** (1 min)
2. **Identifier les 3-5 questions où vous bloquez vraiment** (2 min)
3. **Aller voir le formateur ou un coéquipier** pour éclaircir ces 3-5 points (2 min)
4. **Souffler** jusqu'à 15h00 — un cerveau frais vaut mieux qu'un cerveau saturé

**Ne révisez PAS ce que vous savez déjà.** Concentrez-vous sur les vrais trous.

---

## Ce qui est OK de ne pas savoir en B3

Vous êtes des **développeurs fullstack** qui ont fait **28h de Data & IA** au total. Ce n'est pas une formation de Data Scientist. Vous n'êtes **pas** attendus sur :

- ❌ Les détails internes de Spark (RDD vs DataFrame, transformations vs actions lazy, Catalyst optimizer...)
- ❌ La validation croisée (cross-validation) en profondeur
- ❌ Les détails mathématiques des métriques (formule exacte de F1, de la précision-rappel curve, ROC AUC...)
- ❌ Le data leakage en profondeur (target leakage, train-test contamination, etc.)
- ❌ Les hyperparamètres pointus (gridsearch, randomsearch, Bayesian optimization)
- ❌ Le MLOps avancé (drift, A/B testing, model registry...)
- ❌ Le tuning fin de FastAPI (Pydantic v2 avancé, async/await, dependency injection...)

> **C'est normal**. Le mastère / la spécialisation, c'est là pour ça. Aujourd'hui on attend que vous **compreniez le pipeline complet** et que vous puissiez **expliquer ce que vous avez fait**. Pas que vous deveniez data scientist en 4 jours.

---

## Notation Q&A pendant la soutenance

> Le formateur pose **2-3 questions** pendant la Q&A (les 3 min après votre pitch). Pas une interro de cours.

| Réponse | Effet sur la note |
|---|---|
| Réponse précise et claire en 1-2 phrases | ✅ Maintient ou monte la note |
| Réponse approximative mais qui montre la compréhension | ✅ Maintient la note |
| **« Je ne sais pas, mais mon intuition serait [...] »** | ✅ **Maintient** la note (l'honnêteté est valorisée) |
| Réponse inventée qui est fausse | ❌ Fait baisser la note (le formateur le voit) |
| Silence prolongé sans tentative | ❌ Fait baisser la note |

> **Mieux vaut dire qu'on ne sait pas** avec une piste d'intuition, que d'inventer une réponse fausse. C'est aussi ce qu'on attend de vous **en stage / en 1er job** quand vous serez face à un client / tech lead.

---

## Le mantra à retenir

> *« Je ne sais pas tout. Je sais où chercher. Je sais ce que j'ai fait et pourquoi. C'est suffisant pour un junior. »*
