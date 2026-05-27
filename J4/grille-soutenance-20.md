# Grille d'évaluation soutenance — /20

> **Module** : B3 Data & IA — Sup de Vinci Nantes
> **Date** : 27 mai 2026, 15h00 - 17h00
> **Format** : 10 min présentation + 3 min Q&A (1 min transition) = 14 min/groupe
> **Tirage au sort** de l'ordre à 14h55

---

## ⚠️ Note de calibrage importante

> **Cette grille est calibrée pour des L3 dev fullstack qui ont eu 28h de Data & IA.** Elle valorise **le fait d'avoir fait tourner le pipeline complet** (collecte → modèle → app → déploiement) plus que la profondeur conceptuelle ML qu'on attendrait d'un Data Scientist.
>
> Un projet qui marche de bout en bout, présenté clairement, avec quelques limites identifiées = **15-16/20**, c'est très bien à ce niveau.

---

## Vue d'ensemble

| Critère | Points | Bloc associé |
|---|---|---|
| Compréhension du problème + dataset | /3 | J1 |
| Pipeline data | /3 | J1 + J2 |
| Modèle ML qui tourne | /4 | J2 |
| App + déploiement | /5 | J3 + J4 |
| Soutenance orale | /5 | J4 |
| **Total** | **/20** | |
| **Bonus** | **+1** | CI/CD GH Actions vert ET visible en démo |
| **Pénalité** | **−1** | Secret committé dans le repo (sécurité) |

> Le poids sur **App + déploiement (/5)** et **Soutenance orale (/5)** reflète le profil dev fullstack : on valorise ce qu'ils savent vraiment faire (un produit qui tourne en ligne) et ce qu'ils doivent apprendre (présenter techniquement).

---

## Détail par critère

### 1️⃣ Compréhension du problème + dataset — /3

| Pts | Ce qui rapporte |
|---|---|
| **3** | Problème métier clair (qui, quoi, pourquoi), dataset présenté (taille, colonnes principales), 1-2 limites du dataset mentionnées ("c'est que des données 2023", "biaisé région X", etc.) |
| **2** | Problème clair mais dataset survolé, ou inverse |
| **1** | « On a pris le dataset Spotify parce qu'on aimait la musique » sans aller plus loin |
| **0** | Hors-sujet ou dataset changé en cours sans justification |

**Question typique formateur** :
- *« En une phrase, c'est quoi le problème que votre app résout ? »*
- *« Qui pourrait utiliser votre app en vrai ? »*

---

### 2️⃣ Pipeline data — /3

| Pts | Ce qui rapporte |
|---|---|
| **3** | Code Python qui prend le CSV brut et le rend exploitable (chargement, gestion des valeurs manquantes, encoding catégoriel si besoin), reproductible (refaire tourner = mêmes résultats), train/test split fait |
| **2** | Pipeline fonctionnel mais quelques shortcuts (preprocessing un peu manuel, pas de seed sur le random) |
| **1** | Pipeline présent mais fragile, beaucoup de code ad hoc dans le notebook |
| **0** | Pas de preprocessing, données brutes balancées telles quelles au modèle |

**Question typique formateur** :
- *« Comment vous avez géré les valeurs manquantes ? »*
- *« Pourquoi vous avez fait un train/test split ? »*

> **Sur le leakage** : on n'attend PAS d'eux qu'ils en parlent spontanément. Si on leur demande "êtes-vous sûr qu'il n'y a pas de leakage ?" et qu'ils disent "on a séparé train et test avant de fitter", c'est déjà très bien.

---

### 3️⃣ Modèle ML qui tourne — /4

| Pts | Ce qui rapporte |
|---|---|
| **4** | Modèle entraîné, 1 métrique sortie et commentée ("on a 85% d'accuracy, c'est correct parce que..."), comparaison avec **au moins 1 autre modèle** (ne serait-ce qu'une régression linéaire vs un random forest), `model.pkl` exporté et utilisé dans l'API |
| **3** | Un seul modèle entraîné, métrique sortie et commentée, model.pkl OK |
| **2** | Modèle qui tourne, métrique sortie mais pas vraiment commentée ("on a 0.85 c'est bien") |
| **1** | Modèle qui tourne mais ne sait pas dire ce que la métrique signifie |
| **0** | Modèle non fonctionnel ou pas intégré dans l'app |

**Questions typiques formateur** (graduées) :
- 🟢 **Facile** : *« Quelle métrique vous avez utilisée et pourquoi celle-là ? »* (attendu : "accuracy / F1 / RMSE parce que [...]")
- 🟡 **Moyen** : *« Si je vous donne une entrée bizarre (âge = 200), qu'est-ce qui se passe ? »* (attendu : un peu de bon sens, "ça va prédire n'importe quoi")
- 🔴 **Bonus** : *« Comment vous êtes sûr que votre modèle généralise sur des données qu'il n'a jamais vues ? »* (attendu : référence au test set ; si réponse "parce qu'on a un test set" = OK)

---

### 4️⃣ App + déploiement — /5

> **Le critère qui pèse le plus** parce que c'est ce que ces L3 dev fullstack savent vraiment faire. On valorise.

| Pts | Ce qui rapporte |
|---|---|
| **5** | App React+FastAPI **déployée sur HF Spaces** (URL publique qui répond), démo live qui marche, README pro (avec mermaid), code GitHub propre, **CI/CD GH Actions configuré (bonus +1)** |
| **4** | App déployée et démo qui marche, README correct (sans mermaid) |
| **3** | App déployée mais bugs visibles en démo, ou démo locale fallback |
| **2** | Démo locale uniquement (pas de déploiement HF), README minimal |
| **1** | Démo qui plante sans plan B, ou pas d'app |
| **0** | Rien de démontrable |

**Questions typiques formateur** :
- *« Comment vous redéployez après un changement ? »* (attendu : "git push, ça se redéploie tout seul")
- *« Si je veux ajouter une feature ce soir, qu'est-ce que vous faites ? »*
- *« Combien votre app coûte par mois ? »* (attendu : "0 € sur HF free tier")

---

### 5️⃣ Soutenance orale — /5

> Critère TRES important pour ces L3 dev qui vont passer en stage. On les évalue sur leur capacité à **présenter techniquement** un produit qu'ils ont fait.

| Pts | Ce qui rapporte |
|---|---|
| **5** | 10 min tenues (+/- 1 min), chacun du groupe parle au moins 2 min, structure claire (problème → données → modèle → démo → limites), réponses Q&A solides ou honnêtes ("je sais pas mais je pense que..."), **assume ses choix** ("on a choisi X parce que [...]") |
| **4** | Structure ok, légère hésitation en Q&A mais reste pertinent |
| **3** | Structure OK mais dépassement timing OU un membre ne parle pas, réponses Q&A flottantes |
| **2** | Pitch désorganisé, beaucoup de lecture de slides, Q&A évasive |
| **1** | Pitch confus, démos qui plantent, jeune équipe paniquée |
| **0** | Hors-sujet total ou groupe absent |

**Critères transversaux observés** :
- ✅ Le groupe **regarde le jury** (pas l'écran)
- ✅ Le groupe **assume ses choix** (« on a choisi X parce que » > « le prof avait dit de faire X »)
- ✅ Le groupe **reconnaît ses limites** (« on n'a pas eu le temps de... »)
- ✅ Le groupe **dit ce qu'il ne sait pas** plutôt que d'inventer
- ❌ Lecture intégrale des slides
- ❌ Tous les membres du groupe pas équilibrés sur le temps de parole

---

## Bonus / Pénalités

### Bonus +1 — CI/CD fonctionnel

Pour gagner le point bonus :
- Workflow `.github/workflows/sync-to-hf.yml` présent
- Run vert visible dans l'onglet Actions de GitHub
- **Démontré** en soutenance : « Si je push maintenant, ça redéploie tout seul »

### Pénalité −1 — Sécurité

Tout secret (HF_TOKEN, clé API tierce, mot de passe) trouvé en clair dans le repo → −1 point automatique.

Si le secret a été poussé en clair puis retiré, ça compte toujours (l'historique git le garde).

**Vérification rapide** :
```bash
git log --all -p | grep -iE "(token|api[_-]?key|secret)" | head
```

---

## 6 questions formateur quasi-systématiques (niveau B3)

> Ces questions sont volontairement **abordables**. On ne cherche pas à les piéger.

1. **« En une phrase, c'est quoi le problème que votre app résout ? »**
   → On vérifie qu'ils ont compris le côté business avant le technique.

2. **« Quelle métrique vous avez utilisée et pourquoi celle-là ? »**
   → On vérifie qu'ils ont une métrique et qu'ils peuvent justifier.

3. **« Comment vous redéployez si vous corrigez un bug ce soir ? »**
   → On vérifie qu'ils comprennent leur déploiement.

4. **« Combien votre app coûte par mois ? »**
   → On vérifie la conscience pratique. Réponse attendue : "0 € sur HF".

5. **« Qu'est-ce qui ne marcherait pas si demain vous aviez 100 utilisateurs en même temps ? »**
   → On invite à réfléchir aux limites pratiques (pas besoin de réponse technique précise).

6. **« Qu'est-ce que vous auriez fait si vous aviez eu 1 mois de plus ? »**
   → On vérifie qu'ils ont conscience de leurs limites. Bonus : on apprend leurs idées.

### Variantes plus pointues (réservées aux groupes qui assurent)

> À utiliser **uniquement** si le groupe a montré qu'il maîtrise les bases.

7. *« Comment vous êtes sûr que votre modèle ne fait pas que de la mémoire par cœur ? »*
8. *« Pourquoi vous avez choisi React + FastAPI plutôt que Streamlit ? »*

---

## Notation et feedback

### Pendant la soutenance

Le formateur prend des notes en temps réel sur tablette / papier. **Score gardé pour soi**.

### Après la soutenance

- **Feedback oral immédiat (30 sec à 1 min)** : 1-2 forces, 1 axe d'amélioration. **Pas de note communiquée à l'oral.**
- **Note finale individuelle** : envoyée par mail le soir
- **Note finale du projet** = 40 % projet continu + 30 % soutenance (cette grille) + 30 % rapport individuel (rendu 7j post-J4)

---

## Distribution attendue des notes (calibrage B3)

> **Important** : ces niveaux sont calibrés pour L3 dev fullstack, pas Master Data.

Sur ~7 groupes, la distribution typique :

- **17-20** : 1 groupe (exceptionnel, prêt pour stage de Data Scientist / ML Engineer)
- **14-16** : 3-4 groupes (**solides**, attendus à ce niveau B3) ← cible normale
- **11-13** : 2-3 groupes (objectifs partiellement atteints, ça marche mais limites visibles)
- **8-10** : 1 groupe maximum (problème majeur de pipeline ou d'app)
- **< 8** : exception (groupe qui n'a rien livré)

> **Un 15/20 = très bonne note** pour un L3 dev. Pas de raison de tirer vers le bas par excès de rigueur Master.
>
> **Un 12/20 = note honnête** pour un projet qui marche mais avec des trous visibles.
>
> **Pour aller au-delà de 17**, il faut : code propre, README pro avec mermaid, CI/CD vert, démo fluide, oral qui assume, conscience des limites. Réservé aux 1-2 groupes qui se sont vraiment investis.

---

## Anti-patterns formateur à éviter

> À me rappeler à moi-même pendant les soutenances.

- ❌ **Poser une question de Master à un L3** : « Quel est le risque de target leakage dans votre pipeline ? » → Ils n'ont pas eu le cours pour. → Reformuler : « Vous êtes sûrs que votre modèle ne triche pas en regardant la réponse ? »
- ❌ **Pénaliser l'absence de cross-validation** : ils n'en ont pas fait, c'est OK.
- ❌ **Pénaliser un seul modèle entraîné** : si le modèle marche et est commenté, 3/4 est juste.
- ❌ **Pénaliser un README sans mermaid** : c'est en bonus, pas en exigence.
- ❌ **Pénaliser un dépassement de 30 sec** : couper à 11 min max, pas avant.

> **L'esprit** : on évalue ce qu'ils savent faire (un produit qui marche, présenté correctement), pas ce qu'ils ne savent pas (ML profond).
