import streamlit as st

from model import predict

rh_spend = st.number_input("R&D spend (en $) : ")

admin_spend = st.number_input("Administration spend (en $) : ")

market_spend = st.number_input("Marketing spend (en $) : ")

if st.button("Prédire profit"):
    profit = predict(rh_spend, admin_spend, market_spend)
    st.write("Profit = ", profit[0])