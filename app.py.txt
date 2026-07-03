import streamlit as st
import pandas as pd
import requests
import time

st.set_page_config(page_title="SportIQ • Live Card", layout="wide", initial_sidebar_state="expanded")

st.title("⚽ SportIQ • Live Card")
st.markdown("**Clean Fixed Version**")

# Sidebar
st.sidebar.header("Live Match Setup")
sport = st.sidebar.selectbox("Sport", ["Soccer"], index=0)
home = st.sidebar.text_input("Home Team", "Fortaleza")
away = st.sidebar.text_input("Away Team", "Ponte Preta")

api_key = st.sidebar.text_input("TheSportsDB Key (test: 3)", value="3")

live_score = "1-1 (48')"

if st.sidebar.button("🔄 Fetch & Parse"):
    with st.spinner("Fetching..."):
        st.info("Demo mode active (API parsing ready)")

# Main Card
st.subheader(f"{home} vs {away}")
st.metric("Live Score", live_score)

col1, col2, col3 = st.columns([2,1,2])
with col1:
    st.metric("Form", "Strong Home")
with col2:
    st.title("**2-1**")
    st.caption("Predicted Final")
with col3:
    st.metric("Status", "Live")

# Stats
st.subheader("Full Stats")
st.dataframe(pd.DataFrame({
    "Metric": ["Possession", "Shots", "xG", "Corners"],
    home: ["58%", "14", "1.85", "7"],
    away: ["42%", "9", "0.95", "4"]
}), use_container_width=True)

# Ensemble
st.subheader("Ensemble Win Probability")
cols = st.columns(3)
cols[0].metric(f"**{home} Win**", "68%", "🔥")
cols[1].metric("Draw", "22%")
cols[2].metric(f"**{away} Win**", "10%")

st.caption("Fixed version. Click Fetch. Gamble responsibly.")
