import streamlit as st
from model import *

st.divider()

# Titre de l'application
st.sidebar.markdown("Home🚀")
st.title("Startups Profit Prediction 🚀 :moneybag:")
st.divider()

st.markdown(f"<h5>Anticipez le succès de votre startup avec cette application de prédiction de profit. Estimez votre rentabilité en fonction de vos investissements en recherche et développement, administration et marketing</h5>", unsafe_allow_html=True)

st.write("")

st.markdown("<h3 style='color : yellow'>Dataset utilisé 📶:</h3>", unsafe_allow_html=True)
st.write(dataset)

