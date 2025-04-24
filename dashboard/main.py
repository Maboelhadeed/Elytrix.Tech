import streamlit as st
from dashboard.dashboard_ui import render_dashboard

# Set page layout and icon
st.set_page_config(
    page_title="Elytrix Dashboard",
    layout="wide",
    page_icon=":chart_with_upwards_trend:"
)

# Apply custom dark theme background and hide Streamlit header/footer
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

# Show the logo in the top-left corner on all pages (in sidebar)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/1024px-Placeholder_view_vector.svg.png", width=120)

# Render the dashboard
render_dashboard()
