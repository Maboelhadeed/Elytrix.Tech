import streamlit as st
from dashboard import dashboard_ui, home, theme_manager

# Theme toggle
theme_manager.apply_theme()

# Page selection
page = st.sidebar.selectbox("Choose a tab", ("Home", "Dashboard"))

# Navigation logic
if page == "Home":
    home.render_home()
elif page == "Dashboard":
    dashboard_ui.render_dashboard()
