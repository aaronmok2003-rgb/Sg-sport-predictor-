import streamlit as st
import pandas as pd
import requests
import time

st.set_page_config(page_title="SportIQ • Live Card", layout="wide", initial_sidebar_state="expanded")

st.title("⚽ SportIQ • Live Card")
st.markdown("**Fixed Version**")

# Sidebar
st.sidebar.header("Live Match Setup")
sport = st.sidebar.selectbox("Sport", ["Soccer", "Tennis", "Basketball"], index=0)
home = st.sidebar.text_input("Home Team", "Fortaleza")
away = st.sidebar.text_input("Away Team", "Ponte Preta")

api_key = st.sidebar.text_input("TheSportsDB Key (test: 3)", value="3")

live_score = "1-1 (48')"
status_info = "Live"

if st.sidebar.button("🔄 Fetch & Parse TheSportsDB"):
    with st.spinner("Fetching..."):
        try:
            url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/livescore.php?s=Soccer"
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                data = response.json()
                events = data.get('events', []) or []
                if events:
                    event = events[0]
                    h = event.get('intHomeScore', '?')
                    a = event.get('intAwayScore', '?')
                    live_score = f"{h} - {a}"
                    status_info = event.get('strStatus', 'Live')
                    st.success(f"✅ Parsed: {live_score}")
                else:
                    st.warning("No live events — using demo")
            else:
                st.warning(f"API Error {response.status_code}")
        except Exception as e:
            st.error(f"Error: {str(e)[:80]}")

# Main Card
st.subheader(f"{home} vs {away}")
st.metric("Live Score", live_score)
st.caption(status_info)

col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    st.metric("Form", "Strong Home")
with col2:
    st.title("**2-1**")
    st.caption("Predicted Final")
with col3:
    st.metric("Status", status_info)

# Stats
st.subheader("⚽ Full Stats")
st.dataframe(pd.DataFrame({
    "Metric": ["Possession", "Shots",
