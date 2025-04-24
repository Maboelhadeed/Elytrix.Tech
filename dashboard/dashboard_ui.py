import streamlit as st
import pandas as pd
from PIL import Image
import os

def render_dashboard():
    # Load and show the main Elytrix logo at the top center
    logo_path = os.path.join("dashboard", "assets", "elytrix_logo.png")
    logo = Image.open(logo_path)
    st.image(logo, width=180)

    st.title("Elytrix Dashboard")
    st.markdown("*Precision Wins.*")

    # Sidebar section with logo and controls
    with st.sidebar:
        st.image(logo, width=100)
        st.header("Elytrix Controls")
        st.info("Choose a tab from above")

    # Display metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Capital", "$5,200", "+4.2%")
    with col2:
        st.metric("Daily P/L", "+$210", "+1.3%")
    with col3:
        st.metric("Bot Status", "Running")

    st.markdown("---")
    st.subheader("Strategy Performance")

    # Example chart data
    chart_data = pd.DataFrame({
        "Strategy A": pd.Series([10, 12, 11, 13, 15]),
        "Strategy B": pd.Series([6, 5, 8, 7, 9]),
        "Strategy C": pd.Series([2, 4, 4, 5, 6])
    })
    st.line_chart(chart_data)
