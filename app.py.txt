import streamlit as st
import pandas as pd

st.set_page_config(page_title="SportIQ • Live Card", layout="wide")

st.title("⚽🎾🏀 SportIQ • Live Card")
st.markdown("**Clean & Beautiful Multi-Sport Predictor**")

home = st.text_input("Home Team", "Fortaleza")
away = st.text_input("Away Team", "Ponte Preta")
sport = st.selectbox("Sport", ["Soccer", "Tennis", "Basketball", "Volleyball"])

tab1, tab2, tab3 = st.tabs(["Overview", "Full Stats", "Prediction"])

with tab1:
    st.subheader(f"{home} vs {away}")
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.metric("Live Score", "1-1 (48')")
    with col2:
        st.metric("Form", "Strong Home")
    with col3:
        st.metric("Status", "Live")

with tab2:
    st.subheader("Full Stats")
    if sport == "Soccer":
        st.dataframe(pd.DataFrame({
            "Metric": ["Possession", "Shots", "xG", "Corners"],
            home: ["58%", "14", "1.85", "7"],
            away: ["42%", "9", "0.95", "4"]
        }), use_container_width=True)
    else:
        st.info(f"{sport} stats coming soon - using Soccer demo for now")

with tab3:
    st.subheader("Win Probability")
    col_a, col_b, col_c = st.columns(3)
    col_a.metric(f"**{home}**", "68%", "🔥")
    col_b.metric("Draw", "22%")
    col_c.metric(f"**{away}**", "10%")
    
    st.subheader("Recommended Markets")
    st.dataframe(pd.DataFrame({
        "Market": [f"{home} Win", "Over 2.5 Goals"],
        "Odds": ["1.80", "2.10"],
        "Value": ["Strong", "Good"]
    }), use_container_width=True)

st.caption("Clean version. Select sport and fill teams. More features coming.")
