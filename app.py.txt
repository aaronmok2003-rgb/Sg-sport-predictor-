import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Sports Predictor", layout="wide")
st.title("Advanced Sports Prediction System")

st.sidebar.header("Settings")
bankroll = st.sidebar.number_input("Bankroll (SGD)", value=100, min_value=10)

tab1, tab2 = st.tabs(["Prediction Analysis", "1xBet Markets"])

with tab1:
    st.header("Match Analysis")
    home = st.text_input("Home Team", "Home Team")
    away = st.text_input("Away Team", "Away Team")
    score = st.text_input("Current Score", "0-0")
    
    if st.button("Run Prediction"):
        home_win_prob = 0.58  # Default - change based on analysis
        st.success(f"**Predicted Winner: {home}** (Probability: {home_win_prob*100:.1f}%)")
        st.info(f"Most Likely Score: 2-1")
        st.success("**Recommended Action**: Check 1xBet odds for value")

with tab2:
    st.header("1xBet Markets")
    st.subheader("Main Markets")
    st.dataframe(pd.DataFrame({
        "Market": ["Home Win (1)", "Draw (X)", "Away Win (2)", 
                   "1X (Home or Draw)", "12 (Home or Away)", "2X (Draw or Away)"],
        "Odds Example": [1.80, 3.50, 4.00, 1.25, 1.30, 1.70]
    }))
    
    st.subheader("Over / Under")
    st.dataframe(pd.DataFrame({
        "Market": ["Over 2.5", "Under 2.5", "Over 1.5", "Under 1.5"],
        "Odds Example": [2.00, 1.80, 1.40, 2.80]
    }))
    
    st.write("**Tip**: Compare with model probability to find value bets.")

st.caption("Generic version - fill any teams. More 1xBet markets included.")
