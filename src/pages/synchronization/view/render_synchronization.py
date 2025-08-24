import streamlit as st
from src.pages.synchronization.view.sections.render_file_system import (
    render_file_system,
)
from src.pages.synchronization.view.sections.render_file_stats import render_file_stats


def synchronization_view() -> None:

    st.set_page_config(layout="wide")
    st.title("Synchronization")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            render_file_system()

    with col2:
        with st.container(border=True):
            render_file_stats()

        with st.container(border=True):
            st.write("Additional content for the second column")

        with st.container(border=True):
            st.write("More content for the second column")
