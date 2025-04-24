import streamlit as st
import pandas as pd
from PIL import Image
import os

def render_dashboard():
    # Theme toggle
    theme = st.sidebar.radio("Select Theme", ("Dark", "Light"))

    # Custom CSS for dark/light mode
    if theme == "Dark":
        st.markdown("""
            <style>
                body {
                    background-color: #0e1117;
                    color: white;
                }
                .stApp {
                    background-color: #0e1117;
                }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                .stApp {
                    background-color: #f8f9fa;
                }
            </style>
        """, unsafe_allow_html=True)

    # Load and show Elytrix logo in the center
    logo_path = os.path.join("dashboard", "assets", "elytrix_logo.png")
    logo = Image.open(logo_path)
    st.image(logo, width=180)

    st.title("Elytrix Dashboard")
    st.markdown("*Precision Wins.*")

    with st.sidebar:
        st.image(logo, width=100)
        st.header("Elytrix Controls")
        st.info("Choose a tab from above")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Capital", "$5,200", "+4.2%")
    with col2:
        st.metric("Daily P/L", "+$210", "+1.3%")
    with col3:
        st.metric("Bot Status", "Running")

    st.markdown("---")
    st.subheader("Strategy Performance")

    chart_data = pd.DataFrame({
        "Strategy A": pd.Series([10, 12, 11, 13, 15]),
        "Strategy B": pd.Series([6, 5, 8, 7, 9]),
        "Strategy C": pd.Series([2, 4, 4, 5, 6])
    })
    st.line_chart(chart_data)
