# Grille d'évaluation soutenance — /20

> **Module** : B3 Data & IA — Sup de Vinci Nantes
> **Date** : 27 mai 2026, 15h00 - 17h00
> **Format** : 10 min présentation + 3 min Q&A (1 min transition) = 14 min/groupe
> **Tirage au sort** de l'ordre à 14h55

---

## Vue d'ensemble

| Critère | Points | Bloc associé |
|---|---|---|
| Compréhension dataset | /4 | J1 |
| Pipeline data | /4 | J1 + J2 |
| Modèle ML | /5 | J2 |
| App + déploiement | /4 | J3 + J4 |
| Soutenance orale | /3 | J4 |
| **Total** | **/20** | |
| **Bonus** | **+1** | CI/CD GH Actions vert ET visible en démo |
| **Pénalité** | **−1** | Secret committé dans le repo (sécurité) |

---

## Détail par critère

### 1️⃣ Compréhension dataset — /4

| Pts | Ce qui rapporte | Ce qui retire |
|---|---|---|
| **4** | EDA propre montrée en soutenance (1-2 graphes), question prédictive clairement formulée (`y = ...`), 2-3 biais identifiés explicitement (temporel, géographique, échantillonnage), choix du dataset justifié | Pas applicable |
| **3** | EDA mentionnée mais pas montrée, question prédictive claire, 1 biais identifié | EDA non montrée à l'oral |
| **2** | Dataset présenté mais EDA absente, question prédictive vague | Pas de biais mentionnés |
| **1** | « On a pris le dataset Spotify parce qu'on aimait bien la musique » | Pas de réflexion sur les limites du dataset |
| **0** | Dataset non décrit / changé en cours de route sans justification | |

**Question typique formateur** : *« Quel biais important pourrait fausser votre modèle en prod ? »*

---

### 2️⃣ Pipeline data — /4

| Pts | Ce qui rapporte | Ce qui retire |
|---|---|---|
| **4** | Notebook ou script Python **reproductible** (mêmes inputs → mêmes outputs), gestion explicite des manquants, train/val/test split correct (stratifié si applicable), **pas de leakage** + explication de comment vous l'avez évité, sklearn `Pipeline()` utilisé | |
| **3** | Pipeline fonctionnel mais quelques shortcuts (preprocessing manuel hors pipeline), leakage évité mais non expliqué | |
| **2** | Pipeline qui marche mais fragile (random sans seed, train_test_split sans stratify alors que classes déséquilibrées) | |
| **1** | Pipeline présent mais aux pré-requis flous, leakage potentiel non identifié | |
| **0** | Pas de pipeline / preprocessing fait à la main dans le notebook | |

**Question typique formateur** : *« Comment êtes-vous sûr de ne pas avoir de leakage entre votre train et votre test ? »*

---

### 3️⃣ Modèle ML — /5

| Pts | Ce qui rapporte | Ce qui retire |
|---|---|---|
| **5** | Baseline simple (régression linéaire/logistique) + comparaison avec ≥ 2 autres modèles, métriques **adaptées au problème** (F1 pour classif déséquilibrée, RMSE pour régression continue, etc.), justification du choix final, validation croisée mentionnée | |
| **4** | Baseline + 2 modèles comparés, métriques adaptées, justification rapide | |
| **3** | 2 modèles comparés (sans vraie baseline), métriques OK | Pas de baseline |
| **2** | Un seul modèle entraîné, métrique sortie sans contexte | Accuracy sur classes déséquilibrées |
| **1** | Modèle qui tourne mais résultats non interprétés | |
| **0** | Modèle non fonctionnel ou résultats incompréhensibles | |

**Questions typiques formateur** :
- *« Pourquoi avoir choisi cette métrique précise ? »*
- *« Que se passe-t-il si je vous donne une entrée hors-distribution (exemple : âge = 200) ? »*

---

### 4️⃣ App + déploiement — /4

| Pts | Ce qui rapporte | Ce qui retire |
|---|---|---|
| **4** | App React+FastAPI **déployée sur HF Spaces** (URL publique vivante), démo live qui marche, README pro (badges + mermaid), code GitHub propre, **CI/CD GH Actions configuré (bonus +1)** | |
| **3** | App déployée et démo qui marche, README correct | |
| **2** | App déployée mais bugs visibles en démo, README minimal | |
| **1** | Démo locale uniquement (pas de déploiement), URL HF cassée le jour J | |
| **0** | Pas d'app ou app non démontrable | |

**Questions typiques formateur** :
- *« Comment redéployez-vous après un changement ? »*
- *« Si demain vous avez 1000 utilisateurs simultanés, qu'est-ce qui pète ? »*
- *« Combien votre app coûte par mois ? »*

---

### 5️⃣ Soutenance orale — /3

| Pts | Ce qui rapporte | Ce qui retire |
|---|---|---|
| **3** | 10 min tenues (+/- 30 sec), chacun du groupe parle au moins 2 min, structure claire (problème → données → modèle → démo → limites), réponses Q&A solides (1-2 phrases ciblées) | |
| **2** | Structure ok mais dépassement timing ou un membre ne parle pas, réponses Q&A correctes mais flottantes | |
| **1** | Pitch désorganisé, lectures de slides, Q&A évasive | |
| **0** | Hors-sujet ou démo qui plante sans plan B | |

**Critères transversaux observés** :
- Le groupe **regarde le jury** (pas l'écran)
- Le groupe **assume ses choix** (« on a choisi X parce que [...] » > « le prof avait dit de faire X »)
- Le groupe **dit ce qu'il ne sait pas** plutôt que d'inventer

---

## Bonus / Pénalités

### Bonus +1 — CI/CD fonctionnel

Pour gagner le point bonus :
- Workflow `.github/workflows/sync-to-hf.yml` présent
- Run vert visible dans l'onglet Actions de GitHub
- Démontré en soutenance : « Si je push maintenant, ça redéploie tout seul »

### Pénalité −1 — Sécurité

Tout secret (HF_TOKEN, clé API tierce, mot de passe) trouvé en clair dans le repo → −1 point automatique. Si le secret a été poussé en clair PUIS retiré, ça compte toujours (l'historique git le garde).

**Vérification rapide** :
```bash
git log --all --full-history -p | grep -i -E "(token|api[_-]?key|secret|password)" | head
```

---

## 8 questions formateur quasi-systématiques

> Préparez une réponse en 1-2 phrases pour chacune. Si vous ne savez pas, dites-le ; n'inventez pas.

1. « Quel est le plus gros risque de **leakage** dans votre pipeline ? »
2. « Pourquoi **cette métrique** et pas une autre ? »
3. « Si demain vous avez **1000 utilisateurs simultanés**, qu'est-ce qui pète en premier ? »
4. « **Combien** votre app coûte par mois sur HF (ou Azure équivalent) ? »
5. « Pourquoi **React + FastAPI** plutôt que **Streamlit** ? »
6. « Comment vous **redéployez** si vous corrigez un bug ce soir ? »
7. « Quels sont les **biais** de votre dataset ? »
8. « Comment vous valideriez que votre modèle ne se **dégrade pas en prod** ? »

---

## Notation et feedback

### Pendant la soutenance

Le formateur prend des notes en temps réel sur tablette / papier. **Score gardé pour soi**.

### Après la soutenance

- **Feedback oral immédiat (1 min)** : 1-2 forces, 1 axe d'amélioration. Pas de note communiquée à l'oral.
- **Note finale individuelle** : envoyée par mail le soir (groupe + commentaires individualisés si applicable)
- **Note finale du projet** = 40 % projet continu + 30 % soutenance (cette grille) + 30 % rapport individuel (rendu 7j post-J4)

### Médiation

Si vous estimez avoir été noté injustement, écrivez au formateur dans les **48h** post-soutenance avec :
- Le critère contesté
- Les éléments factuels (slides, démo, etc.) qui justifient une note différente
- Une proposition de note alternative

Le formateur répond sous 48h avec décision motivée.

---

## Distribution attendue des notes (calibrage)

Sur ~7 groupes, la distribution typique :
- **17-20** : 1-2 groupes (exceptionnels, prêts pour le monde pro)
- **14-16** : 3-4 groupes (solides, attendus à ce niveau B3 fullstack)
- **10-13** : 1-2 groupes (objectifs partiellement atteints, lacunes identifiées)
- **< 10** : exception (problème majeur de pipeline ou de soutenance)

> Un 14/20 sur un projet B3 = **bonne note**. La grille n'est pas pensée pour distribuer des 18+ par défaut. Pour aller au-dessus de 16, il faut **vraiment** se démarquer (UX, industrialisation, profondeur d'analyse, qualité de l'oral).
