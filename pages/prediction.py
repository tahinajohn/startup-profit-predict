import streamlit as st
from fire_state import create_store, get_state, set_state
from model import predict

slot = "Prediction"

key1 = create_store(slot, [
    ("RD", 0),
    ("Admin", 0),
    ("Market", 0),
    ("Answer", '')
])

st.markdown("# Prediction :bar_chart: 💵")
st.sidebar.markdown("# Prediction 💵")

rd_spend = st.number_input("R&D spend (en $) : ", value=get_state(slot, 'RD'))
set_state(slot,("RD", rd_spend))

admin_spend = st.number_input("Administration spend (en $) : ", value=get_state(slot, "Admin"))
set_state(slot,("Admin", admin_spend))

market_spend = st.number_input("Marketing spend (en $) : ", value=get_state(slot, "Market"))
set_state(slot,("Market", market_spend))

def predict_value():
    profit = predict(rd_spend, admin_spend, market_spend)
    formated_ans = "{:.2f}".format(profit[0])
    set_state(slot, ("Answer", f"<h2 style='text-align: center;'> Par rapport à vos dépenses, vous devez faire un profit de : {formated_ans} 💲</h2>"))

# if st.button("Prédire profit"):
#     profit = predict(rd_spend, admin_spend, market_spend)
#     st.write("Profit = ", profit[0])

pred_button = st.button("Prédire Profit ", on_click=predict_value)

answer = st.markdown(f"{get_state(slot, 'Answer')}", unsafe_allow_html=True)

