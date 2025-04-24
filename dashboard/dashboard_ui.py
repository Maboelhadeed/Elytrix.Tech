import streamlit as st
import pandas as pd
import os
from PIL import Image

def render_dashboard():
    # Load logo
    logo_path = os.path.join("dashboard", "assets", "elytrix_logo.png")
    st.image(logo_path, width=150)

    # Dashboard Title
    st.title("Elytrix Dashboard")
    st.markdown("Precision Wins.")

    # Key metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Capital", "$5,200", "+4.2%")
    with col2:
        st.metric("Daily P/L", "+$210", "+1.3%")
    with col3:
        st.metric("Bot Status", "Running")

    st.markdown("---")
    st.subheader("Strategy Performance")

    # Chart Example
    chart_data = pd.DataFrame({
        "AI Adaptive": [10, 12, 11, 13, 15],
        "Scalping": [6, 7, 6, 7, 8],
        "Sniper": [2, 3, 4, 5, 6]
    })
    st.line_chart(chart_data)

    # Logs Placeholder
    st.markdown("---")
    st.subheader("Latest Logs")
    st.code("Awaiting data stream...")
