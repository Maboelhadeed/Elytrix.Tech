import streamlit as st

# This must be FIRST Streamlit command
st.set_page_config(
    page_title="Elytrix Dashboard",
    layout="wide",
    page_icon=":chart_with_upwards_trend:"
)

from dashboard.dashboard_ui import render_dashboard

# Apply background style
st.markdown("""
    <style>
        .reportview-container {
            background: linear-gradient(90deg, #0f2027, #203a43, #2c5364);
            color: white;
        }
        header, footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar logo
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/1024px-Placeholder_view_vector.svg.png", width=120)

# Render dashboard
render_dashboard()
