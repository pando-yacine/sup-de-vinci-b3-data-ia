# Glossaire étudiant — J3 (1 page)

> Les mots du jour, expliqués simplement. À garder sous les yeux pendant les ateliers.

## Piloter Claude Code

- **Claude Code** — un assistant de code dans le terminal : il lit ton projet, écrit/modifie des fichiers, lance des commandes. Tu restes le pilote.
- **CLAUDE.md** — la « fiche de consignes » du projet, lue automatiquement par l'agent (stack, commandes, conventions). `/init` la génère.
- **Plan mode** (Shift+Tab) — l'agent **propose un plan sans toucher au code**. À utiliser avant toute tâche un peu large.
- **Prompt cadré** — une demande précise : **où** (fichier), **quoi** exactement, **contraintes** (ce qu'il ne doit PAS faire). Plus c'est cadré, plus c'est relisible.
- **Diff** — le « avant/après » d'une modif. **On le lit toujours avant d'accepter.**
- **`/clear`** — repart d'un contexte vide entre deux tâches sans rapport.
- **commit / `git restore`** — `commit` = sauvegarde du projet ; `git restore` = revenir à la dernière sauvegarde (ton Ctrl+Z). **Commite souvent.**
- **Vibe coding** vs **Agentic engineering** — prompter vaguement (lève le plancher) vs encadrer + tester l'agent (lève le plafond). On vise le second.

## Le produit web (front, back, API)

- **Front-end** (React) — la *salle* du restaurant : ce que l'utilisateur voit.
- **Back-end** (FastAPI, Python) — la *cuisine* : là où le modèle calcule.
- **API** — le *serveur* entre les deux : le front commande, l'API répond.
- **Endpoint** — une adresse d'action de l'API. Ex : `/api/predict` (= « fais une prédiction »).
- **GET / POST** — « donne-moi » (lire) / « voici des données, traite-les » (envoyer).
- **JSON** — le format texte des échanges front ↔ back. Ex : `{"surface": 50}`.
- **CORS** — sécurité du navigateur : il faut **autoriser** le front (`localhost:5173`) à appeler l'API (`localhost:8000`). Erreur fréquente en dev.
- **Pydantic** — le contrôle qualité à l'entrée de l'API (vérifie les types reçus).
- **`.pkl` / joblib** — le modèle « mis en conserve » (`model.pkl`) qu'on recharge sans réentraîner.

## React & viz

- **Composant** — un bloc de page réutilisable (un formulaire, un graphe).
- **state / `useState`** — la mémoire d'un composant ; quand elle change, l'écran se redessine tout seul.
- **`useEffect`** — « fais ça au bon moment » (ex : charger les données au chargement).
- **Vite** — l'outil qui démarre (`npm run dev`) et compile (`npm run build`) le projet React.
- **build / `dist/`** — la version compilée du site, prête à mettre en ligne (dossier `dist/`).
- **Recharts** — la bibliothèque de graphiques pour React. Un graphe = `<BarChart>` + `<XAxis>`, `<Bar>`… dans un `<ResponsiveContainer>`.

## Pour aller plus loin (fine-tuning de LLM, vu en démo)

- **LLM** — « grand modèle de langage » (Claude, Qwen…).
- **Fine-tuning** — adapter un modèle **déjà entraîné** à une tâche précise avec un petit dataset (≠ entraîner de zéro).
- **LoRA** — la version économe du fine-tuning : on entraîne de petits *adaptateurs* (~80 Mo), pas tout le modèle.
- **Hallucination** — quand un LLM invente une réponse fausse avec assurance.
