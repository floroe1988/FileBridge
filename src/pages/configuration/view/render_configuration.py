import streamlit as st


@st.fragment()
def configuration_view() -> None:
    st.set_page_config(layout="wide")
    st.title("Configuration")
