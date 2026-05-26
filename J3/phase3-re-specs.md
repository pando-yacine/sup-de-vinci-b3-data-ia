# Phase 3 — Re-specs (boucle d'apprentissage)

> **But** : maintenant que votre **V1 tourne en prod**, vous avez appris des choses qu'on ne pouvait pas savoir avant. On **retravaille les specs** à la lumière de ce qu'on sait, et on **priorise** ce qu'on construit en V2.

C'est la phase **la plus discrète mais la plus précieuse**. C'est ce qui distingue un projet d'amateur d'un projet livré par quelqu'un qui sait. *Specs-first ne veut PAS dire « specs immuables » — ça veut dire « specs maintenues ».*

## Livrable attendu

- Les 5 docs de `docs/` **mis à jour** avec ce qu'on a appris en V1
- Un **backlog V2 priorisé** (`docs/backlog-v2.md`) — ce qu'on construit en P4-P5

---

## Étape 3.1 — Regarder honnêtement la V1

Listez (par groupe, 15 min en binôme/trinôme) :

| Dimension | Question à se poser |
|---|---|
| **Performance modèle** | Le score est-il acceptable ? Sur quelles classes/zones le modèle se plante-t-il ? |
| **Biais** | Le dataset surreprésente-t-il un sous-groupe ? Le modèle est-il juste sur les minorités ? |
| **Vraies limites** | Quelles prédictions n'ont aucun sens (out-of-distribution) ? |
| **API** | Le contrat (input/output) est-il pratique pour un front ? Manque-t-il un endpoint (`/api/stats`, `/api/explain`) ? |
| **Question prédictive** | Avec le recul, est-ce la bonne ? Une autre cible serait-elle plus utile ? |
| **User journey** | Si vous étiez l'utilisateur, qu'est-ce qui manque ? Qu'est-ce qui est inutile ? |

> Demander à un·e camarade d'un **autre groupe** d'utiliser votre URL HF V1 (5 min) — leurs retours valent de l'or.

---

## Étape 3.2 — Mettre à jour `docs/`

Toucher chaque fichier en assumant ce qu'on a appris :

- **`docs/question-predictive.md`** — formulation **finale** (peut-être plus précise qu'en P1), métrique **confirmée** par les chiffres réels.
- **`docs/dataset.md`** — biais **découverts**, valeurs manquantes **mesurées**, classes **réellement** déséquilibrées, distribution **réelle** de la cible.
- **`docs/architecture.md`** — si l'archi a évolué (ex : on ajoute `/api/stats`), mettre à jour le schéma mermaid.
- **`docs/user-journey.md`** — ce qui a du sens **vraiment** (avec un peu de recul), pas ce qu'on imaginait.
- **`docs/diagramme-sequence.md`** — ajouter les nouveaux endpoints / corriger les étapes.

> Les **commits docs** comptent. `docs:` clean, message qui explique **pourquoi** le changement (« suite à test V1 »).

---

## Étape 3.3 — Backlog V2 priorisé (`docs/backlog-v2.md`)

Format **MoSCoW** (lisible et défendable en soutenance) :

```markdown
# Backlog V2

## 🟢 Must (sans ça, pas livrable)
- [ ] Front avec formulaire de prédiction branché sur l'API V1
- [ ] 2-3 visualisations Recharts (depuis /api/stats)
- [ ] Page « Performance modèle » avec les métriques J2

## 🔵 Should (vraiment souhaitable)
- [ ] Gestion d'erreur si input vide / hors plage
- [ ] Endpoint /api/stats côté API

## 🟡 Could (si le temps le permet)
- [ ] Section « explication » de la prédiction (feature importance)
- [ ] Animation Recharts
- [ ] Light/dark mode

## 🔴 Won't (consciemment, pour cette itération)
- [ ] Authentification utilisateur
- [ ] Historique des prédictions
- [ ] Mobile responsive parfait
```

Le **Won't** est aussi important que le Must — décider ce qu'on **ne fait pas** évite le scope creep.

---

## ✅ Checklist Phase 3

- [ ] URL V1 testée par un binôme **externe** (retour récolté)
- [ ] `docs/question-predictive.md` — version finale
- [ ] `docs/dataset.md` — biais/limites mis à jour
- [ ] `docs/architecture.md` — schéma à jour si évolution
- [ ] `docs/user-journey.md` — affiné avec le recul
- [ ] `docs/diagramme-sequence.md` — nouveaux endpoints intégrés
- [ ] `docs/backlog-v2.md` — Must / Should / Could / **Won't** explicites
- [ ] Commits `docs:` propres (avec le **pourquoi**)

---

## Comment piloter Claude Code sur cette phase

C'est une phase de **rédaction guidée**. Bons prompts :

- « Lis `notebook.ipynb` (résultats finaux du modèle) et `docs/question-predictive.md`. Identifie ce qui n'est plus à jour. Propose-moi les changements en **plan mode**. »
- « Voici les retours du groupe X qui a testé notre V1 : [liste]. Mets à jour `docs/user-journey.md` en intégrant ce qui est pertinent, **sans inventer**. »
- « Génère un `docs/backlog-v2.md` au format MoSCoW à partir de ces retours + ce qu'il reste à faire pour la soutenance. »

---

## Pourquoi cette phase compte (à dire en soutenance)

> *« On a livré une V1 minimale tôt, on a observé, on a réajusté la spec, puis on a construit la V2. C'est exactement ce qu'on fait en équipe en prod. »*

C'est la phase qui démontre votre **maturité d'ingénieur** — capacité à **mesurer, écouter, réajuster** plutôt que de coder en aveugle.
