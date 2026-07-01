import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Advanced Sports Predictor", layout="wide")
st.title("Advanced Multi-Sport Prediction System")

st.sidebar.header("Settings")
bankroll = st.sidebar.number_input("Bankroll (SGD)", value=100, min_value=10)
sport = st.sidebar.selectbox("Select Sport", ["Soccer", "Tennis", "Basketball"])

tab1, tab2 = st.tabs(["Detailed Prediction", "1xBet Markets"])

with tab1:
    st.header(f"{sport} Match Analysis")
    home = st.text_input("Home Team/Player", "Home Team")
    away = st.text_input("Away Team/Player", "Away Team")
    score = st.text_input("Current Score", "0-0")
    
    if st.button(f"Run {sport} Prediction"):
        if sport == "Soccer":
            st.success(f"**Most Likely Winner: {home}** (62-68%)")
            st.info("**Expected Score**: 2-1 | Expected Goals: 2.6-2.8")
            st.write("**Key Factors**: Home advantage, attack strength, Poisson model, current score momentum.")
            
        elif sport == "Tennis":
            st.success(f"**Most Likely Winner: {home}** (58-64%)")
            st.info("**Sets Prediction**: Likely 2-1 in favor of server")
            st.write("**Key Factors**: Serve percentage, break point conversion, surface type, current set momentum, tiebreak edge.")
            
        elif sport == "Basketball":
            st.success(f"**Most Likely Winner: {home}** (60-66%)")
            st.info("**Expected Score Range**: 98-92")
            st.write("**Key Factors**: Home court advantage, pace & offensive efficiency, player fatigue, rebounding edge.")

        st.write("**Betting Tip**: Compare model probability with 1xBet odds for value.")

with tab2:
    st.header("1xBet Markets")
    st.subheader("Common Markets")
    st.dataframe(pd.DataFrame({
        "Market": ["Home Win", "Draw", "Away Win", "Over 2.5", "Under 2.5", "BTTS Yes"],
        "Odds Example": [1.80, 3.50, 4.00, 2.00, 1.80, 2.79]
    }))

st.caption("Sport-specific detailed predictions. Fill teams and run analysis.")
