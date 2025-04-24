import streamlit as st
from dashboard.dashboard_ui import render_dashboard

st.set_page_config(page_title="Elytrix Dashboard", layout="wide")
render_dashboard()
