import streamlit as st
import pandas as pd

st.set_page_config(page_title="SportIQ • Live Card", layout="wide")

st.title("⚽ SportIQ • Live Card")
st.markdown("**Clean Working Version**")

home = st.text_input("Home Team", "Fortaleza", key="home")
away = st.text_input("Away Team", "Ponte Preta", key="away")

st.subheader(f"{home} vs {away}")

col1, col2, col3 = st.columns([2,1,2])
with col1:
    st.metric("Form", "Strong Home")
with col2:
    st.title("**2-1**")
    st.caption("Predicted Final")
with col3:
    st.metric("Live Score", "1-1 (48')")

# Full Stats
st.subheader("Full Stats")
st.dataframe(pd.DataFrame({
    "Metric": ["Possession", "Shots", "xG", "Corners", "Fouls"],
    home: ["58%", "14", "1.85", "7", "11"],
    away: ["42%", "9", "0.95", "4", "14"]
}), use_container_width=True)

# Win Probability
st.subheader("Win Probability")
cols = st.columns(3)
cols[0].metric(f"**{home}**", "68%", "🔥")
cols[1].metric("Draw", "22%")
cols[2].metric(f"**{away}**", "10%")

st.caption("App is now working. Add more features if needed.")
