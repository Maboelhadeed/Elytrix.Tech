import streamlit as st
import pandas as pd
import os

def render_dashboard():
    # Theme toggle
    theme = st.sidebar.radio("Select Theme", ["Dark", "Light"], index=0)

    # Apply dark/light background and text styling
    if theme == "Dark":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #0e1117;
                    color: #ffffff;
                }
                .css-10trblm, .css-1v0mbdj, h1, h2, h3, p {
                    color: #ffffff !important;
                }
                .stMetric {
                    color: #ffffff !important;
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

    # Load and display Elytrix logo
    logo_path = os.path.join("dashboard", "assets", "elytrix_logo.png")
    st.image(logo_path, width=150)

    # Dashboard title and slogan
    st.title("Elytrix Dashboard")
    st.markdown("Precision Wins.")

    # Control panel
    with st.sidebar:
        st.header("Elytrix Controls")
        st.info("Choose a tab from above")

    # Capital & Bot metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Capital", "$5,200", "+4.2%")
    with col2:
        st.metric("Daily P/L", "+$210", "+1.3%")
    with col3:
        st.metric("Bot Status", "Running")

    # Chart section
    st.markdown("---")
    st.subheader("Strategy Performance")

    chart_data = pd.DataFrame({
        "AI Adaptive": pd.Series([10, 12, 11, 13, 15]),
        "Scalping": pd.Series([6, 7, 6, 7, 8]),
        "Sniper": pd.Series([2, 3, 4, 5, 6])
    })
    st.line_chart(chart_data)
