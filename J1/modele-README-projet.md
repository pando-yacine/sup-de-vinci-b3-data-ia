# Nom du projet

> Copiez ce fichier comme `README.md` à la racine de votre repo et remplacez chaque bloc. Livrable J1 : les sections 1 à 4 remplies.

**Groupe** : Prénom NOM · Prénom NOM · Prénom NOM
**Qui porte quoi** : données · modèle · API · interface · déploiement

## 1 · La question

Une phrase : « Prédire **X** à partir de **Y**, pour aider **Z** à décider **W**. »

## 2 · Le dataset

| | |
|---|---|
| Source | lien + producteur |
| Licence | ex. Licence Ouverte Etalab, CC BY 4.0 |
| Taille | lignes × colonnes |
| Une ligne représente | ex. un match, une transaction, un patient |
| Période couverte | |
| Deuxième source (optionnel) | lien + pourquoi |

## 3 · La fiche projet

| Rubrique | Votre réponse |
|---|---|
| **Cible y** | la colonne à prédire |
| **Type de problème** | régression / classification (+ clustering en bonus) |
| **Features X** | 5 à 10 variables candidates, disponibles AVANT le moment de la prédiction |
| **Métrique** | MAE, RMSE, R², accuracy, F1… et pourquoi celle-là |
| **Baseline naïve** | le score à battre : moyenne, classe majoritaire, valeur précédente |
| **Risques** | fuite de données, biais, taille, valeurs manquantes, et votre parade |

## 4 · Premiers constats (exploration)

- 3 à 5 constats tirés du notebook d'exploration (distribution de la cible, valeurs manquantes, corrélations, anomalies).
- Notebook : `notebooks/01-exploration.ipynb`

## 5 · Lancer le projet

À compléter aux J2-J3 : installation, commandes, variables d'environnement (jamais de secret dans le repo).

## 6 · Architecture

À compléter au J3 : données → modèle → API → interface → déploiement (un schéma mermaid est bienvenu).

## 7 · Résultats et limites

À compléter au J2 puis au J4 : modèles comparés, métrique, limites et biais connus.

## Structure du repo

```
data/          # ou un lien vers la source si le fichier est trop gros
notebooks/     # 01-exploration.ipynb, 02-modele.ipynb…
src/           # code réutilisable (preprocessing, API)
docs/          # schémas, captures pour le plan B de la démo
README.md
requirements.txt
.gitignore
```
