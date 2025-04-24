import streamlit as st
import os

def render_home():
    theme = st.session_state.get('theme', 'Dark')

    if theme == "Dark":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #0e1117;
                    color: #ffffff;
                }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                .stApp {
                    background-color: #ffffff;
                    color: #000000;
                }
            </style>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<center><img src='https://raw.githubusercontent.com/Maboelhadeed/Elytrix.tech/main/dashboard/assets/elytrix_logo.png' width='200'></center>", unsafe_allow_html=True)
    st.markdown("<center><h1 style='margin-top: 10px;'>Welcome to Elytrix</h1></center>", unsafe_allow_html=True)
    st.markdown("<center><p><i>Precision Wins.</i></p></center>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("Launch Dashboard"):
            st.experimental_set_query_params(page="Dashboard")
