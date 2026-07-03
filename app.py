import streamlit as st
import pandas as pd
import requests
import time

st.set_page_config(page_title="SportIQ • Live Card", layout="wide", initial_sidebar_state="expanded")

st.title("⚽ SportIQ • Live Card")
st.markdown("**Refined TheSportsDB API Parsing + Multi-Sport Stats**")

# Sidebar
st.sidebar.header("Live Match Setup")
sport = st.sidebar.selectbox("Sport", ["Soccer", "Tennis", "Basketball"], index=0)
home_input = st.sidebar.text_input("Home Team", "Fortaleza")
away_input = st.sidebar.text_input("Away Team", "Ponte Preta")

api_key = st.sidebar.text_input("TheSportsDB Key (test: 3)", value="3")

live_score = "1-1 (48')"
status_info = "Live"

if st.sidebar.button("🔄 Fetch & Parse TheSportsDB"):
    with st.spinner("Fetching & Parsing JSON..."):
        try:
            url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/livescore.php?s={sport.lower() if sport == 'Soccer' else sport}"
            response = requests.get(url, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                events = data.get('events', []) or data.get('livescore', [])
                
                if events:
                    event = events[0]  # Take first match
                    home = event.get('strHomeTeam', home_input)
                    away = event.get('strAwayTeam', away_input)
                    home_score = event.get('intHomeScore', '?
