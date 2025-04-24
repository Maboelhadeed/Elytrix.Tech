import streamlit as st

def apply_theme():
    theme = st.sidebar.radio("Select Theme", ["Dark", "Light"], index=0)

    # Inject CSS to control background and text color
    if theme == "Dark":
        st.markdown(
            """
            <style>
                body, .stApp {
                    background-color: #0e1117;
                    color: white;
                }
                .css-1d391kg {  /* metrics container */
                    background-color: #1e222d;
                    border-radius: 10px;
                }
                .st-emotion-cache-1v0mbdj {
                    color: white;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
                body, .stApp {
                    background-color: white;
                    color: black;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
