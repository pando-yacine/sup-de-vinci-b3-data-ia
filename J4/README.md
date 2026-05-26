# J4 — Industrialiser + soutenances finales

Jour 4 (et dernier) du module **Data & IA (B3)**. Objectif : **industrialiser** votre app déployée hier (J3) sur Hugging Face Spaces (CI/CD GitHub Actions, README pro, monitoring), **préparer** votre soutenance, et **passer** les soutenances finales avec grille /20.

## Esprit de la journée

- **Pas de nouvelle stack à apprendre** — on industrialise ce qui est déjà là (HF Spaces, React, FastAPI)
- **3h30 dédiées au projet** (atelier matin + prépa après-midi)
- **2h de soutenances** (15h00 - 17h00)
- **Azure positionné en culture** (vous le verrez en mastère, pas hands-on aujourd'hui)

## Planning de la journée

### Matin — "Industrialiser" (3h30)

| Créneau | Bloc | Format |
|---|---|---|
| 9h15 - 9h45 | Accueil + **récap 4 jours** | Cours + Quiz Qiplim |
| 9h45 - 10h30 | **Démo vire-app** : un projet PMU pro de Pando (mermaid archi + déploiement) | Cours + démo live |
| 10h30 - 11h00 | **Industrialisation** : CI/CD GH Actions + README pro + monitoring | Cours |
| 11h00 - 11h15 | *Pause* | |
| 11h15 - 12h45 | **Atelier matin** : industrialiser votre projet (CI/CD + README + finitions) | Pratique encadrée |

### Après-midi — "Préparer + soutenir" (3h30)

| Créneau | Bloc | Format |
|---|---|---|
| 13h45 - 14h00 | Brief créneau prépa + révisions | Cadrage |
| 14h00 - 15h00 | **Autonomie : prépa soutenance + révisions cours** | Autonomie |
| 15h00 - 17h00 | **🎤 SOUTENANCES** (10 min + 3 min Q&A) | Présentations /20 |
| 17h00 - 17h15 | Synthèse + carrières + clôture | Cours + exit ticket |

## Fiches du jour

### Pour le matin

- [**`recap-4-jours.md`**](./recap-4-jours.md) — Récap des 4 jours, check minimum d'acquis avant soutenance
- [**`fiche-projet-vire-app.md`**](./fiche-projet-vire-app.md) — Étude de cas vire-app : un projet PMU pro avec mermaid archi + pipeline + déploiement
- [**`industrialisation-projet.md`**](./industrialisation-projet.md) — Fiche atelier matin : CI/CD GH Actions vers HF + README pro + monitoring

### Pour l'après-midi

- [**`brief-prepa-soutenance-14h-15h.md`**](./brief-prepa-soutenance-14h-15h.md) — Brief créneau 14h-15h : structurer pitch, répéter démo, anticiper Q&A
- [**`grille-soutenance-20.md`**](./grille-soutenance-20.md) — Grille évaluation /20 détaillée avec ce qui rapporte / ce qui retire + 8 questions formateur quasi-systématiques
- [**`questions-cours-revision.md`**](./questions-cours-revision.md) — 39 questions de cours pour réviser (J1 + J2 + J3 + J4 + transverses)

### Pour aller plus loin

- [**`azure-culture.md`**](./azure-culture.md) — Positionnement Azure pour le mastère : 5 briques (App Service, Blob, ML Studio, Functions, App Insights), comparaison HF vs Azure, certification AZ-900 gratuite étudiants

## Soutenance — format en bref

- **Durée** : 10 min présentation + 3 min Q&A par groupe
- **Structure attendue** : Problème → Dataset → Modèle → Démo live → Industrialisation → Limites
- **Tirage au sort** de l'ordre à 14h55
- **Notation** : grille /20 (cf. `grille-soutenance-20.md`)
- **Bonus +1** : CI/CD GitHub Actions vert et démontré
- **Pénalité −1** : secret committé dans le repo (sécurité)

## Rapport individuel (à rendre 7j post-J4)

- **Délai** : 3 juin 2026 minuit
- **Format** : 3-5 pages PDF
- **Contenu attendu** :
  1. Présentation du projet de votre groupe (qui faisait quoi)
  2. **Votre rôle perso** : ce que vous avez fait personnellement
  3. **3 choix techniques** justifiés (modèle, métrique, déploiement)
  4. **2 limites** identifiées + plan d'amélioration sur 1 mois
  5. **Retour critique** sur la formation (positif + axes)
- **Envoi** : email à `yacine@pando-studio.com` + délégué en CC
- **Notation** : 30 % de la note finale

## Note finale du module

```
Note finale = 0.4 × projet continu + 0.3 × soutenance + 0.3 × rapport individuel
```

## Mise en garde sécurité

❗ **Ne JAMAIS commiter un token (HF_TOKEN, API keys, mots de passe) en clair dans le repo.** Si vous l'avez fait par erreur, allez **immédiatement** révoquer le token côté plateforme (HF Settings → Tokens → Revoke), puis générez-en un nouveau et ajoutez-le **uniquement** en secret GitHub (Settings → Secrets and variables → Actions).
