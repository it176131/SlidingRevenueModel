import streamlit as st

profit_share = st.slider(
    "Profit Share", min_value=0.0, max_value=30.0, step=0.1
)
monthly_revenue = st.slider(
    "Monthly Revenue", min_value=5_000, max_value=20_000, step=100
)
equity = st.slider("Equity", min_value=0.0, max_value=21.0, step=0.1)
