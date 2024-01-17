import streamlit as st
import seaborn as sns
from model import *

st.markdown("# ANALYSE 📈")
st.sidebar.markdown("Analyse📈")
st.markdown(f"<h5>Vu le graphique du dataset ci-dessous, on peut constater que la dépense faite en recherche et développement à plus d'impact sur le profit</h5>", unsafe_allow_html=True)
st.markdown(f"<h5>Donc, plus on augmente la dépense dans la recherche et développement, plus le profit augmente</h5>", unsafe_allow_html=True)

st.markdown(f"<h3 style='color:green;'>GRAPHIQUE:</h3>", unsafe_allow_html=True)
splot = sns.pairplot(dataset)
st.pyplot(splot.fig)
