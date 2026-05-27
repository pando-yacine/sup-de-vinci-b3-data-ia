# Brief créneau 14h-15h — préparation soutenance + révisions

> **Créneau** : 14h00 - 15h00 (1h en autonomie)
> **Objectif** : arriver en soutenance à 15h00 avec un pitch propre, une démo qui marche, et la tête claire pour les questions.

---

## Pourquoi ce créneau est critique

La soutenance pèse **30 %** de votre note finale. En 1 heure, vous pouvez **gagner 3-4 points** ou les perdre. La différence entre un 12 et un 15 ne se joue **pas** sur la qualité du ML — elle se joue sur la **clarté du pitch** et la **capacité à assumer ce que vous avez fait**.

> **Rappel important** : vous êtes des L3 dev fullstack, pas des Data Scientists Master. La grille évalue ce que vous savez faire (un produit qui tourne, présenté correctement), **pas** votre profondeur conceptuelle ML.

---

## Plan suggéré pour les 60 minutes

| Temps | Tâche | Format |
|---|---|---|
| 14h00 - 14h10 | **Brief équipe** : qui dit quoi, dans quel ordre, avec quelles transitions | Discussion |
| 14h10 - 14h30 | **Structurer le pitch 10 min** (slides ou notes) | Travail équipe |
| 14h30 - 14h45 | **Répéter la démo 2 fois** + préparer fallback screenshots | Travail équipe |
| 14h45 - 14h55 | **Anticiper 5 questions formateur** + préparer réponses courtes | Travail équipe |
| 14h55 - 15h00 | **Révisions cours flash** : parcourir `questions-cours-revision.md` | Individuel |

---

## 1️⃣ Structurer le pitch (20 min)

> Format soutenance : 10 min présentation + 3 min Q&A + 1 min transition.

### La structure qui marche (à respecter strictement)

| Min | Quoi dire | Slide / Démo |
|---|---|---|
| 0:00 - 1:00 | **Le problème** : qui (persona), quoi (besoin), pourquoi (intérêt) | Slide texte simple |
| 1:00 - 2:30 | **Le dataset** : source, taille, 1-2 colonnes clés, 1-2 limites identifiées | Slide + 1 graphe |
| 2:30 - 5:00 | **Le modèle** : quel modèle, quelle métrique, ce que ça donne, comparaison rapide si vous en avez 2 | Slide tableau métriques |
| 5:00 - 7:30 | **🎬 Démo live** : 1 scénario simple qui marche | Switch sur l'app HF |
| 7:30 - 9:00 | **Déploiement + industrialisation** : URL HF, README, (CI/CD si vous l'avez) | Slide ou montrer GitHub |
| 9:00 - 10:00 | **Limites + ouvertures** : 2 limites concrètes, 1-2 idées d'amélioration | Slide bullet points |

### Les 5 erreurs qui coûtent cher

| Erreur | Pénalité |
|---|---|
| **Démarrer par le code** au lieu du problème | « Les jurés perdent intérêt en 30 sec » |
| **Lire ses slides** au lieu d'y faire référence | Soutenance orale → −1 |
| **Démo qui plante** sans plan B | App + déploiement → −2 |
| **Un membre du groupe ne parle pas** | Soutenance orale → −1 |
| **Dépasser les 10 min** | Coupure ferme par le formateur à 11 min max |

### Astuce — chronométrez vraiment

Faire **un essai complet** chronométré. Vous **dépasserez** systématiquement. Coupez ce qui est en trop. Mieux vaut finir à 9'30 que se faire couper à 10'00.

---

## 2️⃣ Répéter la démo (15 min)

> La démo est le moment **le plus risqué** de la soutenance. C'est aussi le moment qui rapporte le plus si tout va bien.

### Préparer 2 scénarios

| Scénario | Description | Quand l'utiliser |
|---|---|---|
| **Nominal** | Input habituel → prédiction qui a du sens | Dans le timing normal |
| **Fallback** | Screenshots dans une slide | Si HF est down (rare mais possible) |

### Checklist avant la démo

- [ ] L'URL HF s'ouvre en < 5 sec → si lent, faire un `curl /api/health` **10 min avant** pour réveiller le Space (HF met en veille les Spaces inutilisés)
- [ ] La connexion wifi de la salle est stable
- [ ] Vous avez **les inputs en tête** (ou écrits) — pas de tâtonnement à l'oral
- [ ] Vous avez un **2e onglet ouvert** sur GitHub pour montrer le code en Q&A si demandé

### Comment commenter pendant la démo

- ❌ « Et donc voilà j'ai mis un truc et ça calcule... »
- ✅ « Voici un cas typique : `[input précis]`. Le modèle prédit **X** parce qu'il a appris que [feature] est importante. Si je change [variable] → la prédiction passe à **Y**, ce qui montre que le modèle est sensible à ce paramètre. »

---

## 3️⃣ Anticiper les Q&A (10 min)

> Le formateur va poser **2-3 questions** abordables. Pas une interro de cours. Préparez une réponse courte pour chacune des 6 questions ci-dessous.

### Les 6 questions formateur quasi-systématiques

> Préparez une réponse en **1-2 phrases** pour chacune. Si vous ne savez pas, dites-le honnêtement.

**1. « En une phrase, c'est quoi le problème que votre app résout ? »**

Réponse type : « Notre app permet à [persona] de [action] en utilisant [data]. »

Exemple : « Notre app permet à un acheteur de prédire le prix d'un appartement parisien à partir de sa surface et son arrondissement. »

**2. « Quelle métrique vous avez utilisée et pourquoi celle-là ? »**

Réponse type : « On a utilisé [métrique] parce que [raison liée au problème]. On obtient [valeur], ce qui veut dire [interprétation]. »

Exemple : « On a utilisé l'**accuracy** parce que notre dataset est équilibré (50/50). On obtient 87%, ce qui veut dire que 87 prédictions sur 100 sont correctes. »

Si dataset déséquilibré → mentionner que vous avez utilisé **F1** (ou précision/rappel) au lieu de l'accuracy.

**3. « Comment vous redéployez si vous corrigez un bug ce soir ? »**

Réponse type : « `git push origin main` → CI/CD ou push manuel HF → rebuild auto → URL active en 3-5 min. »

**4. « Combien votre app coûte par mois ? »**

Réponse type : « **0 €** sur HF Spaces free tier (CPU basic 2vCPU / 16 Go RAM). Suffisant pour la démo. Si on passe en prod avec plus de users, on passerait sur Azure App Service (~13 €/mois B1). »

**5. « Qu'est-ce qui ne marcherait pas si demain vous aviez 100 utilisateurs en même temps ? »**

Réponse type : « Le free tier HF a 2 vCPU, donc on tiendrait pas 100 requêtes simultanées sans latence. Le bottleneck serait probablement [le modèle qui n'est pas parallélisé / la latence sklearn / le rate limit]. Solution : passer sur un hardware payant ou scaler avec plusieurs workers. »

> **Niveau B3** : pas grave si vous ne donnez pas une analyse pointue. Dire « probablement le serveur saturerait, on passerait à un plus gros plan » est OK.

**6. « Qu'est-ce que vous auriez fait si vous aviez eu 1 mois de plus ? »**

Réponse type : « On aurait : [1 amélioration modèle], [1 amélioration UX], [1 amélioration infra]. »

Exemple : « On aurait essayé un XGBoost à la place du Random Forest, ajouté une carte interactive Leaflet pour visualiser les prix par quartier, et mis en place un cache Redis pour les requêtes répétées. »

### Si vous ne savez pas répondre

> **NE PAS INVENTER.** Le formateur le voit en 5 sec et la note baisse.

**Phrases acceptables** :
- « Je n'ai pas creusé ce point précis. Mon intuition serait [...] mais je ne suis pas sûr. »
- « C'est exactement la limite qu'on aurait travaillée si on avait eu plus de temps. »
- « Je note la question, je vous reviens dans le rapport individuel. »

**À éviter** :
- Silence total
- Inventer une réponse qui ne tient pas debout
- « C'est pas dans le cours »

---

## 4️⃣ Révisions cours flash (5 min)

> Le formateur peut poser **1 question de cours** pendant la Q&A. Pas une interro, mais un rappel : « C'était quoi déjà accuracy ? » → si vous séchez, ça donne mauvais ton.

### Sprint final : 5 minutes sur les 20 questions

Ouvrir `questions-cours-revision.md` et **survoler** rapidement. Pas besoin d'apprendre par cœur. Vérifier que vous **sauriez répondre en 30 sec à voix haute** sur **au moins 10 questions sur 20**.

Si vous bloquez sur une question, demandez à un coéquipier ou au formateur (qui circule pendant le créneau).

---

## Ce qui est OK de ne pas savoir (rappel)

Vous êtes des **dev fullstack** qui ont fait **28h de Data & IA**. La grille reconnaît votre profil. Vous n'êtes **pas attendus** sur :

- Spark interne (RDD, transformations vs actions, Catalyst...)
- Validation croisée en profondeur
- Détails mathématiques des métriques
- Data leakage en profondeur
- Hyperparameter tuning
- MLOps avancé
- Pydantic v2 / async FastAPI

→ Si on vous pose une question à ce niveau, dire honnêtement « pas creusé dans ce cours, mais [intuition rapide] » est totalement OK.

---

## Logistique pratique

- **Le formateur circule** entre les tables → utilisez-le pour débloquer un point précis (mais pas pour vous faire écrire votre pitch)
- **Tirage au sort de l'ordre des soutenances** à 14h55, pour ne pas stresser pendant la prépa
- **Slides** : Google Slides recommandé (peut s'ouvrir sur n'importe quel laptop)
- **Backup** : avoir le PDF des slides sur clé USB ou Drive partagé

---

## Mindset pour la soutenance

- **Vous êtes en posture de présentateur, pas d'élève**. Vous racontez **votre** projet, vos choix, vos limites. Vous n'êtes pas évalués sur le fait de tout savoir — vous êtes évalués sur votre capacité à **expliquer ce que vous avez fait et pourquoi**.
- **Une démo qui plante n'est pas la fin du monde**. Le fallback screenshots existe pour ça. Reconnaître l'erreur calmement (« mon Space est en veille, voilà les screenshots ») fait meilleur effet que de paniquer.
- **Le jury veut que vous réussissiez**. Le formateur n'est pas là pour vous piéger.
- **3 minutes de Q&A passent vite**. 2-3 questions max.

---

## Critères auto-évaluation avant 15h00

Cochez les 6 points suivants. Si tous cochés → vous êtes prêt.

- [ ] Notre pitch tient en 10 min chrono (testé en vrai)
- [ ] Chacun dans le groupe parle au moins 2 minutes
- [ ] Notre démo a un scénario nominal qui marche **et** un fallback (screenshots)
- [ ] On a réfléchi aux 6 questions formateur avec des réponses courtes
- [ ] Notre URL HF répond en < 5 sec (on l'a réveillée 10 min avant)
- [ ] On a une slide « limites + ouvertures » avec 2 limites honnêtes

> **Si moins de 4/6**, allez voir le formateur tout de suite.

---

## Le mantra à retenir

> *« Je raconte ce qu'on a fait, pourquoi on l'a fait, ce qui marche, ce qui ne marche pas. Je suis honnête sur mes limites. Je suis fier de ce qu'on a livré. C'est ce qu'on attend d'un junior. »*
