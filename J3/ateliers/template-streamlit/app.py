"""Filet de secours -- dashboard Streamlit (si React/CORS bloque).

Lancer : streamlit run app.py
Avantage : tout en Python, un seul fichier, deployable tel quel sur Azure au J4.
"""
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard B3", layout="wide")
st.title("Dashboard B3 -- [votre dataset]")


@st.cache_resource
def load_model():
    return joblib.load("model.pkl")  # exporte depuis le notebook J2


@st.cache_data
def load_data():
    # TODO : charger votre dataset (CSV)
    # return pd.read_csv("data.csv")
    return pd.DataFrame()


# model = load_model()
# df = load_data()

st.header("Explorer les donnees")
# TODO : 2-3 graphiques (st.bar_chart, st.line_chart, st.plotly_chart)

st.header("Predire")
# TODO : un widget par feature, puis prediction
# surface = st.slider("surface", 10, 300, 50)
# pieces = st.number_input("pieces", 1, 10, 3)
# if st.button("Predire"):
#     pred = model.predict([[surface, pieces]])[0]
#     st.metric("Prediction", round(float(pred), 2))

st.header("Performance du modele")
# TODO : afficher les metriques de J2 (R2/RMSE ou accuracy/F1)
