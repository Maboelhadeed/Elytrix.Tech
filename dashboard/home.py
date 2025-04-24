import streamlit as st

def render_home():
    theme = st.session_state.get('theme', 'Dark')
    
    # Background style
    if theme == "Dark":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #0e1117;
                    color: white;
                }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                .stApp {
                    background-color: #ffffff;
                    color: black;
                }
            </style>
        """, unsafe_allow_html=True)

    # Centered content
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center'>"
                "<img src='https://raw.githubusercontent.com/Maboelhadeed/Elytrix.tech/main/dashboard/assets/elytrix_logo.png' width='160'>"
                "<h1>Welcome to Elytrix</h1>"
                "<p><i>Precision Wins.</i></p>"
                "<a href='/?Navigate=Dashboard'><button style='padding:10px 20px; font-size:16px; background-color:#292929; color:white; border:none; border-radius:5px;'>Launch Dashboard</button></a>"
                "</div>", unsafe_allow_html=True)
