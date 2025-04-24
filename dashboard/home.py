import streamlit as st
import os

def render_home():
    # Set Elytrix logo path
    logo_path = os.path.join("dashboard", "assets", "elytrix_logo.png")

    st.image(logo_path, width=180)
    st.markdown("<h1 style='text-align: center;'>Welcome to Elytrix</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; font-style: italic;'>Precision Wins.</h4>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Launch Dashboard", use_container_width=True):
        st.switch_page("pages/dashboard_ui.py")
