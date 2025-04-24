import streamlit as st
from dashboard.dashboard_ui import render_dashboard
from dashboard.home import render_home

# Set page config
st.set_page_config(page_title="Elytrix", layout="wide")

# Theme toggle (top right)
theme = st.selectbox("Select Theme", ["Dark", "Light"], index=0)
st.session_state["theme"] = theme

# Navigation menu
page = st.selectbox("Navigate", ["Home", "Dashboard"])

# Routing
if page == "Home":
    render_home()
elif page == "Dashboard":
    render_dashboard()
