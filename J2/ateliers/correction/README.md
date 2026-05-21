# Corrigés des ateliers J2

Notebooks **exécutés et complétés** des ateliers du J2.

> Pour consultation **après** avoir tenté l'atelier en autonomie. Garder l'effort de compléter soi-même est ce qui fait apprendre.

## Contenu

- `atelier1-baseline-immobilier-corrige.ipynb` — California Housing baseline régression
  - Pipeline complet StandardScaler + LinearRegression
  - R² ≈ 0.61 sur le val set
  - Scatter plot prédiction vs réel

## Notes

- Les `random_state=42` sont fixés → vos résultats devraient être identiques à 0.01 près
- Si votre score diffère significativement : vérifiez le split, le scaling avant split, et le `random_state`
