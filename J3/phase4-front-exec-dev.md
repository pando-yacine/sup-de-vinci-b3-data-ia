# Phase 4 — Front + viz (exécuter le dev avec Claude Code)

> **But** : développer le **dashboard React** qui consomme votre **API V1 déjà en ligne**. Construit en **pilotant Claude Code** avec les réflexes du matin (boucle Explore → Plan → Implement → Verify). Front local qui parle au back en prod = **fidèle à la réalité d'une équipe**.

## Livrable attendu

- Dashboard React **fonctionnel en local** (`npm run dev`) qui parle à l'URL HF de la V1
- Sections : **Explorer** (viz Recharts) · **Prédire** (formulaire) · **Performance modèle**
- Gestion d'erreur basique (input vide, API down)
- Commits réguliers, code lisible

---

## Étape 4.1 — Brancher le front sur l'API en ligne

Variable d'environnement pour l'URL de l'API (Vite la prend en compte si elle commence par `VITE_`) :

`frontend/.env` (à **ne pas commiter** s'il contient des secrets — ici l'URL est publique, OK) :
```
VITE_API_URL=https://<user>-<space>.hf.space
```

`frontend/src/api.ts` :
```ts
const API = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'

export async function predire(features: Record<string, unknown>) {
  const r = await fetch(`${API}/api/predict`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(features),
  })
  if (!r.ok) throw new Error('Erreur API /predict')
  return r.json()
}
```

> Tester tout de suite : `fetch('https://<user>-<space>.hf.space/api/health')` depuis la console — si ça répond, vous êtes prêts.

---

## Étape 4.2 — Construire les 3 sections

Le template Phase 1 a déjà 3 sections vides dans `App.tsx`. À remplir une par une, **prompt après prompt** :

### Section « Prédire » (la plus importante)
- 1 champ par feature (cf. `docs/question-predictive.md` pour la liste)
- `useState` pour les valeurs · `useMutation` (React Query) pour l'appel API
- Affiche la prédiction · gère l'erreur

### Section « Explorer » (viz Recharts)
- Charge `/api/stats` au montage (`useQuery`)
- Affiche un `BarChart` (ou `LineChart` selon la nature des données) **dans un `<ResponsiveContainer>`** (sinon rien ne s'affiche)
- 1 graphe = 1 question (cf. principes data viz du matin)

### Section « Performance modèle »
- Afficher les métriques **finales** de la P2 (MAE, R², F1…) en `<Card>` ou simple texte
- Si tableau de confusion : mini grille (Tailwind)
- *(Optionnel)* importance des features

---

## Étape 4.3 — Best practices Claude Code (rappel pour cette phase)

C'est **LA phase où vous pratiquez ce qu'on a vu le matin**. Tenez la ligne :

1. **Plan mode (Shift+Tab)** avant de demander à l'agent de coder un composant.
2. **Prompt cadré** : où (`PredictionForm.tsx`) + quoi exactement + contraintes (« garde `useState`, pas de lib externe »).
3. **Lire chaque diff** avant d'accepter. « **Explique-moi cette ligne.** »
4. **Lancer après chaque modif** (`npm run dev` reste ouvert) — vert à l'écran > « ça a l'air bon ».
5. **Commits petits** entre chaque sous-étape (un par section, à minima).
6. **`/clear` entre deux composants** sans rapport.
7. Si l'agent part en vrille : `git restore .` + reformuler plus petit.

---

## Étape 4.4 — Tests E2E light (optionnel mais valorisé)

Si vous avez le temps, un test Playwright ou Cypress qui vérifie que :
- la page charge
- on peut taper dans le formulaire
- on clique « Prédire »
- une réponse s'affiche (mocker l'API ou tester contre la vraie URL HF)

C'est un **gros plus en soutenance** (et en CV).

---

## ✅ Checklist Phase 4

- [ ] `VITE_API_URL` pointe vers l'URL HF de votre V1
- [ ] Section **Prédire** : formulaire + appel API + affichage prédiction
- [ ] Section **Explorer** : ≥ 1 graphe Recharts (idéalement 2-3) qui répondent à une question
- [ ] Section **Performance** : métriques finales affichées
- [ ] Gestion d'erreur (input vide, API down)
- [ ] Titres de section + titres conclusifs sur les graphes
- [ ] `npm run dev` tourne propre (pas de warning rouge)
- [ ] Commits par section (`feat(front): …`)
- [ ] *(Bonus)* 1 test E2E qui passe

---

## Comment piloter Claude Code sur cette phase

- « Lis `frontend/src/App.tsx` et `frontend/src/PredictionForm.tsx`. Explique-moi la structure et ce qui est à compléter. »
- *(Plan mode)* « Pour `PredictionForm.tsx` : je veux 1 champ contrôlé par feature de `docs/question-predictive.md`, soumis via `useMutation`, qui affiche la prédiction. **Propose-moi un plan** avant de coder. »
- « Implémente le plan validé. Ne touche QUE à `PredictionForm.tsx`. »
- « Ajoute un composant `StatsChart.tsx` qui appelle `/api/stats` via `useQuery` et affiche un `BarChart` Recharts dans un `ResponsiveContainer`. »
- « **Prouve-moi que ça marche** : décris exactement ce que je dois voir à l'écran après cette modif. »

---

## Pièges fréquents

| Piège | Solution |
|---|---|
| **CORS** error | L'API doit autoriser votre origine (Vite = `localhost:5173`). Le template a déjà `CORSMiddleware`. |
| Graphe ne s'affiche pas | Manque `<ResponsiveContainer>`, ou `/api/stats` renvoie vide (onglet Réseau) |
| Modèle plante en prod | Ordre/types des features ≠ entraînement (cf. P2.4) |
| « Ça marchait en local » | URL `localhost:8000` codée en dur au lieu de `VITE_API_URL` |
| Front trop bavard, code illisible | Cadrer Claude Code (« change uniquement X »), refuser les ajouts non demandés |
