# Brief créneau 14h-15h — préparation soutenance + révisions

> **Créneau** : 14h00 - 15h00 (1h en autonomie)
> **Objectif** : arriver en soutenance à 15h00 avec un pitch propre, une démo qui marche, et la tête claire pour les questions de cours.

---

## Pourquoi ce créneau est critique

La soutenance pèse **30 %** de votre note finale. En 1 heure, vous pouvez **gagner 3-4 points** ou les perdre. La différence entre un 12 et un 17 ne se joue pas sur la qualité du code — elle se joue sur la **clarté du pitch** et la **solidité des réponses Q&A**.

---

## Plan suggéré pour les 60 minutes

| Temps | Tâche | Format |
|---|---|---|
| 14h00 - 14h10 | **Brief équipe** : qui dit quoi, dans quel ordre, avec quelles transitions | Discussion 3 |
| 14h10 - 14h30 | **Structurer le pitch 10 min** (slides ou markdown) | Travail équipe |
| 14h30 - 14h45 | **Répéter la démo 2 fois** (deux scénarios + scénario fallback) | Travail équipe |
| 14h45 - 14h55 | **Anticiper 5 Q&A** et préparer la réponse en 1 phrase chacune | Travail équipe |
| 14h55 - 15h00 | **Révisions cours flash** : parcourir `questions-cours-revision.md` | Travail individuel |

---

## 1️⃣ Structurer le pitch (20 min)

> Format soutenance : 10 min présentation + 3 min Q&A + 1 min transition.

### La structure qui marche (à respecter strictement)

| Min | Quoi dire | Slide / Démo |
|---|---|---|
| 0:00 - 1:00 | **Le problème** : qui (persona), quoi (besoin), pourquoi (impact) | Slide texte large |
| 1:00 - 3:00 | **Le dataset** : source, taille, EDA clé, **biais identifiés** | Slide + 1 graphe |
| 3:00 - 6:00 | **Le modèle** : baseline, comparaison ≥ 2 modèles, métrique finale, **comment on a évité le leakage** | Slide tableau métriques |
| 6:00 - 8:00 | **🎬 Démo live** : 1 scénario nominal + 1 cas limite | Switch sur l'app HF |
| 8:00 - 9:00 | **Industrialisation** : URL HF, CI/CD, README, **monitoring** | Slide ou montrer GitHub |
| 9:00 - 10:00 | **Limites + ouvertures** : 2 limites concrètes, 2 idées d'amélioration | Slide bullet points |

### Les 5 erreurs qui coûtent cher

| Erreur | Pénalité |
|---|---|
| **Démarrer par le code** au lieu du problème | « Les jurés perdent intérêt en 30 sec » |
| **Lire ses slides** au lieu d'y faire référence | « Présentation orale » → 0/3 |
| **Démo qui plante** sans plan B | « App + déploiement » → −2 |
| **Un membre du groupe ne parle pas** | « Présentation orale » → −1 |
| **Dépasser les 10 min** | Coupure brutale par le formateur |

### Astuce — chronométrez vraiment

Faire **un essai complet** chronométré. Vous **dépasserez** systématiquement. Coupez ce qui est en trop. Mieux vaut finir à 9'30 que se faire couper à 10'00.

---

## 2️⃣ Répéter la démo (15 min)

> La démo est le moment **le plus risqué** de la soutenance. C'est aussi le moment qui rapporte le plus si tout va bien.

### Préparer 3 scénarios

| Scénario | Description | Quand l'utiliser |
|---|---|---|
| **Nominal** | Input habituel → prédiction qui a du sens | Dans le timing normal |
| **Cas intéressant** | Input qui révèle une feature ou une limite du modèle | Pour montrer que vous comprenez votre modèle |
| **Fallback** | Screenshots dans une slide | Si HF est down (5 % de chance, mais...) |

### Checklist avant la démo

- [ ] L'URL HF s'ouvre en < 5 sec → si lent, faire un curl `/api/health` 1 min avant pour réveiller le Space (HF met en veille les Spaces inutilisés)
- [ ] La connexion wifi de la salle est stable (vérifier avec speed test)
- [ ] Vous avez **les inputs en tête** (ou écrits) — pas de tâtonnement à l'oral
- [ ] Vous avez un **2e onglet ouvert** sur GitHub pour montrer le code en Q&A si demandé

### Comment commenter pendant la démo

- ❌ « Et donc voilà j'ai mis un truc et ça calcule... »
- ✅ « Voici un cas typique : `[input précis]`. Le modèle prédit **X**, parce qu'il a appris que [feature dominante] est très corrélée. Maintenant si je change [variable] → la prédiction passe à **Y**, ce qui confirme la sensibilité attendue. »

---

## 3️⃣ Anticiper les Q&A (10 min)

> Les questions Q&A pèsent dans « Présentation orale » (/3). Une mauvaise réponse coûte 1 point. Une excellente réponse rapporte la note pleine.

### Les 8 questions formateur quasi-certaines

> Préparez une réponse en **1-2 phrases** pour chacune. Si vous ne savez pas, dites « je n'ai pas creusé ce point, mais je pense que [...] » — c'est ACCEPTABLE et honnête.

1. **« Quel est le plus gros risque de leakage dans votre pipeline ? »**
   → Réponse type : « Notre principal risque était [X]. On l'a évité en [Y]. »

2. **« Pourquoi cette métrique et pas une autre ? »**
   → Réponse type : « Le dataset est [équilibré/déséquilibré], donc l'accuracy seule serait [pertinente/trompeuse]. On a choisi [F1/RMSE/...] parce que [...]. »

3. **« Si demain vous avez 1000 utilisateurs simultanés, qu'est-ce qui pète en premier ? »**
   → Réponse type : « Le Space HF free tier a 16 Go RAM et 2 vCPU. Le bottleneck sera probablement [le modèle qui n'est pas thread-safe / la latence sklearn / le rate limit]. La solution serait [...]. »

4. **« Combien votre app coûte par mois ? »**
   → Réponse type : « Sur HF Spaces free tier : 0 €. Si on passe sur Azure App Service B1 ce serait ~13 €/mois. »

5. **« Pourquoi React + FastAPI plutôt que Streamlit ? »**
   → Réponse type : « Streamlit est plus rapide pour prototyper, mais React donne un contrôle UX bien meilleur et c'est une compétence directement utile en stage / job fullstack. »

6. **« Comment vous redéployez si vous corrigez un bug ce soir ? »**
   → Réponse type : « `git push origin main` → CI/CD GitHub Actions push sur HF → rebuild auto en ~3 min. Pas de manipulation manuelle. »

7. **« Quelles sont les biais de votre dataset ? »**
   → Réponse type : « [Décrire 2 biais concrets] — par exemple temporel (données 2023), géographique (focus région X), ou échantillonnage (sur-représentation Y). »

8. **« Comment vous validez que votre modèle ne se dégrade pas en prod ? »**
   → Réponse type : « On a un endpoint `/api/health`. Pour aller plus loin, il faudrait monitorer la distribution des inputs (data drift) et comparer les prédictions au réel quand on a le ground truth — ça s'appelle MLOps. »

### Si vous ne savez pas répondre

> **NE PAS INVENTER.** Le formateur le voit en 5 sec et la note baisse.

Phrases acceptables :
- « Je n'ai pas creusé ce point précis. Mon intuition serait [...] mais je ne suis pas sûr. »
- « C'est exactement la limite qu'on aurait travaillée la semaine prochaine. »
- « Je note la question, je vous reviens dans le rapport. »

---

## 4️⃣ Révisions cours flash (5 min)

> Le formateur peut poser **2-3 questions cours** pendant la Q&A. Pas une interro, mais un rappel : « C'était quoi déjà la lazy eval ? » → si vous séchez, ça donne mauvais ton.

### Sprint final : 5 minutes sur les 10 questions clés

Ouvrir `questions-cours-revision.md` et **survoler** rapidement. Pas besoin d'apprendre par cœur. Vérifier que vous **sauriez répondre en 30 sec** à voix haute.

Si vous bloquez sur une question, **demandez à un coéquipier** ou au formateur (qui circule pendant le créneau).

---

## Logistique pratique

- **Le formateur circule** entre les tables pendant tout le créneau → utilisez-le pour débloquer un point précis (mais pas pour vous faire écrire votre pitch)
- **Tirage au sort de l'ordre des soutenances** à 14h55, pour ne pas stresser pendant la prépa
- **Slides** : Google Slides recommandé (peut s'ouvrir sur n'importe quel laptop)
- **Backup** : avoir le PDF des slides sur clé USB ou Drive partagé

---

## Mindset pour la soutenance

- **Vous êtes en posture de présentateur, pas d'élève**. Vous racontez **votre** projet, vos choix, vos limites. Vous n'êtes pas évalués sur le fait de tout savoir — vous êtes évalués sur votre capacité à **expliquer ce que vous avez fait et pourquoi**.
- **Une démo qui plante n'est pas la fin du monde**. Le fallback screenshots existe pour ça. Reconnaître l'erreur calmement (« mon Space est en veille, voilà les screenshots ») fait meilleur effet que de paniquer.
- **Le jury veut que vous réussissiez**. Le formateur n'est pas là pour vous piéger, il est là pour valider que vous avez compris le pipeline complet.
- **3 minutes de Q&A passent vite**. 2-3 questions max. Pas la panique.

---

## Si vous êtes en avance

- Préparer 1 slide bonus « Si on avait 1 mois de plus » → c'est exactement ce que le formateur aime entendre en clôture
- Faire jouer un coéquipier au rôle de jury et répondre à 3 questions au pied levé
- Aller boire un café — un cerveau frais vaut mieux qu'un cerveau saturé

---

## Critères auto-évaluation avant 15h00

Cochez les 6 points suivants. Si tous cochés → vous êtes prêt.

- [ ] Notre pitch tient en 10 min chrono (testé)
- [ ] Chacun dans le groupe parle au moins 2 minutes
- [ ] Notre démo a un scénario nominal qui marche **et** un fallback
- [ ] On a anticipé 5 questions formateur avec des réponses courtes
- [ ] Notre URL HF répond en < 5 sec (on l'a réveillée 10 min avant)
- [ ] On a une slide « limites + ouvertures » avec 2 limites honnêtes

> **Si moins de 4/6**, allez voir le formateur tout de suite.
