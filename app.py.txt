import streamlit as st
import pandas as pd
import requests
import time

st.set_page_config(page_title="SportIQ • Live Card", layout="wide", initial_sidebar_state="expanded")

st.title("⚽ SportIQ • Live Card")
st.markdown("**Fixed TheSportsDB Parsing + Full Stats**")

# Sidebar
st.sidebar.header("Live Match Setup")
sport = st.sidebar.selectbox("Sport", ["Soccer", "Tennis", "Basketball"], index=0)
home = st.sidebar.text_input("Home Team", "Fortaleza")
away = st.sidebar.text_input("Away Team", "Ponte Preta")

api_key = st.sidebar.text_input("TheSportsDB Key (test: 3)", value="3")

live_score = "1-1 (48')"
status_info = "Live"

if st.sidebar.button("🔄 Fetch & Parse TheSportsDB"):
    with st.spinner("Fetching & Parsing JSON..."):
        try:
            url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/livescore.php?s=Soccer"
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                data = response.json()
                events = data.get('events', []) or []
                if events:
                    event = events[0]
                    h_score = event.get('intHomeScore', '?')
                    a_score = event.get('intAwayScore', '?')
                    live_score = f"{h_score} - {a_score}"
                    status_info = event.get('strStatus', 'Live')
                    st.success(f"✅ Parsed: {live_score}")
                else:
                    st.warning("No live events — using demo")
            else:
                st.warning(f"API Error {response.status_code} — using demo")
        except Exception as e:
            st.error(f"Error: {str(e)[:100]} — using demo")

# Main Card
st.subheader(f"{home} vs {away}")
st.metric("Live Score", live_score)
st.caption(status_info)

col1, col2, col3 = st.columns([2,1,2])
with col1:
    st.metric("Form", "Strong Home")
with col2:
    st.title("**2-1**")
    st.caption("Predicted Final")
with col3:
    st.metric("Status", status_info)

# Full Stats
st.subheader("⚽ Full Stats")
st.dataframe(pd.DataFrame({
    "Metric": ["Possession", "Shots", "xG", "Corners", "Fouls"],
    home: ["58%", "14", "1.85", "7", "11"],
    away: ["42%", "9", "0.95", "4", "14"]
}), use_container_width=True)

# Ensemble
st.subheader("Ensemble Win Probability")
cols = st.columns(3)
cols[0].metric(f"**{home} Win**", "68%", "🔥")
cols[1].metric("Draw", "22%")
cols[2].metric(f"**{away} Win**", "10%")

st.subheader("1xBet Recommended Markets")
st.dataframe(pd.DataFrame({
    "Market": [f"{home} Win", "Handicap", "Over Total"],
    "Odds": ["1.75", "
