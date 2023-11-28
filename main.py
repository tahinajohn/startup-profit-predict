import streamlit as st
import seaborn as sns
from model import *

st.divider()

# Titre de l'application
st.title("Startups Profit Prediction :moneybag:")
st.divider()
splot = sns.pairplot(dataset)

st.write(dataset)

st.pyplot(splot.fig)
