# Filet de secours — Dashboard Streamlit

Pour un groupe bloqué sur React/CORS/build. Tout en Python, un seul fichier.

## Démarrer
```bash
pip install -r requirements.txt
# placez votre model.pkl ici (exporté du notebook J2)
streamlit run app.py        # ouvre http://localhost:8501
```

## À compléter (`TODO` dans `app.py`)
- charger le dataset
- 2-3 graphiques
- un widget par feature → `model.predict(...)`

## Prompt Claude Code
« Lis `app.py`. Complète-le : charge `data.csv`, ajoute un `st.bar_chart` de la moyenne de `<cible>` par `<catégorie>`, et un formulaire (1 widget par feature) qui appelle `model.predict`. »

## Déploiement J4
Startup Azure App Service : `streamlit run app.py --server.port 8000 --server.address 0.0.0.0`
