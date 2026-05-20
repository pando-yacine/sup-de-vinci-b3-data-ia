# Exercice MapReduce papier

> Imprimer ou projeter. Diviser la classe en 3 groupes.
> Chaque groupe recoit 1 paragraphe et compte les mots.

---

## Consigne

1. Chaque groupe recoit **1 paragraphe**
2. Comptez le nombre d'occurrences de **chaque mot** dans votre paragraphe
3. Ecrivez vos resultats au tableau
4. On rassemble les resultats de tous les groupes

Vous venez de faire du **MapReduce** !

---

## Paragraphe 1 (Groupe A)

La data est partout. Chaque jour des milliards de donnees sont generees par les capteurs les telephones et les applications. La data transforme les entreprises et les gouvernements.

---

## Paragraphe 2 (Groupe B)

Les entreprises utilisent la data pour prendre des decisions. Les capteurs IoT generent des donnees en continu. Les applications collectent des donnees sur les utilisateurs.

---

## Paragraphe 3 (Groupe C)

Le Big Data permet d analyser la data a grande echelle. Les donnees massives necessitent des outils specialises. La data science transforme les donnees en valeur.

---

## Correction (pour le formateur)

| Mot | Groupe A | Groupe B | Groupe C | **Total (Reduce)** |
|---|---|---|---|---|
| la | 2 | 1 | 2 | **5** |
| data | 2 | 1 | 2 | **5** |
| les | 2 | 3 | 2 | **7** |
| donnees | 1 | 2 | 2 | **5** |
| et | 2 | 0 | 0 | **2** |
| des | 1 | 1 | 1 | **3** |
| capteurs | 1 | 1 | 0 | **2** |
| applications | 1 | 1 | 0 | **2** |
| entreprises | 1 | 1 | 0 | **2** |
| transforme | 1 | 0 | 1 | **2** |

## Debrief (3 min)

- **MAP** = chaque groupe a traite sa partie en parallele
- **SHUFFLE** = on a regroupe les mots identiques au tableau
- **REDUCE** = on a additionne les comptages
- Si on avait 1 million de paragraphes, on pourrait avoir 1 million de groupes (= machines)
- Si un groupe s'est trompe (une machine plante), pas grave : le paragraphe est replique, on recommence avec un autre groupe
