# Brief d'autonomie — 15h00-16h00 (J3 B3 Data & IA)

> **À distribuer / projeter aux étudiants à 15h00.** Le formateur est en réunion pendant cette heure. Vous travaillez **en autonomie** sur votre projet, en binôme/trinôme.

---

## Objectif de l'heure

À 16h, votre dashboard doit afficher :
1. **Une prédiction** : on saisit des valeurs → le modèle (J2) répond. *(Ça, c'est fait avant 15h avec le formateur.)*
2. **Au moins 1 visualisation** (idéalement 2-3) qui raconte quelque chose sur vos données.
3. Une **mise en page lisible**.

C'est aussi le test de ce que vous avez appris ce matin : **piloter Claude Code seuls, sans qu'on vous tienne la main.**

---

## La méthode (rappel — affichez-la)

**Explore → Plan → Implement → Verify**, par petits pas.
- **Plan mode** (Shift+Tab) avant toute tâche un peu large.
- **Lisez chaque diff.** Vous ne comprenez pas une ligne ? Demandez à l'agent de l'expliquer. Ne validez pas à l'aveugle.
- **Lancez le code** après chaque modif (`npm run dev`). Vert à l'écran > « ça a l'air bon ».
- **Commitez souvent.** Avant chaque grosse demande à l'agent : `git add -A && git commit -m "..."`.

---

## Tâches cadrées (dans l'ordre)

> Donnez à Claude Code des prompts **précis** (où / quoi / contraintes). Exemples ci-dessous — adaptez à VOS features et VOTRE constat data de l'atelier 1.

### 1. Un endpoint de stats (backend)
> Prompt type :
> « Dans `backend/main.py`, ajoute un endpoint GET `/api/stats` qui renvoie, en JSON, la moyenne de `<cible>` par `<colonne catégorielle>` à partir du dataset. Réutilise le DataFrame déjà chargé. Ne touche pas à `/api/predict`. »

### 2. Les visualisations (frontend, Recharts)
> Prompt type :
> « Dans `frontend/`, crée un composant `StatsChart` qui appelle `/api/stats` au montage (`useEffect`) et affiche un `BarChart` Recharts. Wrappe-le dans un `ResponsiveContainer`. Garde du `useState`, pas de lib de state externe. »
- Visez 2-3 graphes qui **répondent à une question** (pas de déco) — cf. votre constat data.
- Titre **conclusif** (« Les prix grimpent dans le centre » plutôt que « Prix par quartier »).

### 3. Mise en page
> Prompt type :
> « Organise `App.jsx` en 3 sections claires : **Explorer** (les graphes), **Prédire** (le formulaire), **Performance modèle** (les métriques J2). Ajoute des titres de section. Ne change pas la logique existante. »

### 4. Robustesse
> Prompt type :
> « Dans `PredictionForm`, si un champ est vide, désactive le bouton et affiche un message. Ne modifie rien d'autre. »

---

## Checklist (cochez avant 16h)

- [ ] `/api/stats` renvoie du JSON correct (testé dans le navigateur ou via la console réseau)
- [ ] Au moins 1 graphe Recharts s'affiche
- [ ] La prédiction marche toujours (vous ne l'avez pas cassée)
- [ ] Page lisible (sections + titres)
- [ ] **Commits réguliers** (au moins 3 sur l'heure)

---

## Si vous êtes bloqués (sans le formateur)

1. **Relisez le diff** et demandez à l'agent : « explique-moi ce que tu viens de changer et pourquoi ».
2. **Ça a cassé ?** → `git restore .` (revenez au dernier commit qui marchait). D'où : commitez souvent.
3. **L'agent part en vrille / radote ?** → `/clear` et reformulez en plus petit et plus précis.
4. **Erreurs fréquentes** :
   - *CORS error* → l'API n'autorise pas `localhost:5173` (le `CORSMiddleware` est déjà dans le template ; vérifiez qu'il est actif).
   - *Le graphe ne s'affiche pas* → manque `<ResponsiveContainer>`, ou `/api/stats` renvoie vide (regardez l'onglet Réseau).
   - *Le modèle plante* → l'ordre/les types des features doivent correspondre à l'entraînement J2.
5. **Toujours bloqués ?** → **notez la question** dans [canal questions : Qiplim OpenText / doc partagé]. On la traite au débrief de 16h. **Ne restez pas coincés une heure dessus** — passez à la tâche suivante.

---

## Règle d'or

> Mieux vaut **1 graphe qui marche + un commit propre** que 3 graphes à moitié cassés. Avancez par petits pas vérifiés.
