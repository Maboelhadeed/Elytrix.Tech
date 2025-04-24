import streamlit as st
from dashboard.dashboard_ui import render_dashboard
from dashboard.home import render_home

# Theme toggle
theme = st.sidebar.radio("Select Theme", ["Dark", "Light"], index=0)
st.session_state['theme'] = theme

# Navigation
page = st.sidebar.selectbox("Choose a tab", ["Home", "Dashboard"])

if page == "Home":
    render_home()
elif page == "Dashboard":
    render_dashboard()
