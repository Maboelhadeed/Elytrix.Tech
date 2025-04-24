import streamlit as st
from PIL import Image
import os

# Load and display logo centered
logo_path = os.path.join("dashboard", "assets", "elytrix_logo.png")
logo = Image.open(logo_path)

st.image(logo, width=180)
def render_dashboard():
    # Load and display centered logo
logo_path = os.path.join("dashboard", "assets", "elytrix_logo.png")
logo = Image.open(logo_path)
st.image(logo, width=180)
    st.title("Elytrix Dashboard")
    st.markdown("**Precision Wins.**")

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
        "Strategy B": pd.Series([5, 6, 8, 7, 9]),
        "Strategy C": pd.Series([3, 4, 4, 5, 6]),
    })
    st.line_chart(chart_data)
