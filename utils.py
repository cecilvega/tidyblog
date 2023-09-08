import streamlit as st


def format_footer():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
