import uuid
import streamlit as st
from src.pages.synchronization.model.files import Folder, File
from src.pages.synchronization.controller.file_system import toggle_folder


def render_folder(folder: Folder) -> None:
    with st.container(border=True):
        col_exp, col_name, col_button = st.columns([1, 10, 1])
        with col_exp:
            if folder.collapsed:
                st.button(
                    "",
                    key=str(uuid.uuid4()),
                    icon="➡️",
                    on_click=toggle_folder,
                    args=(folder,),
                )
            else:
                st.button(
                    "",
                    key=str(uuid.uuid4()),
                    icon="⬇️",
                    on_click=toggle_folder,
                    args=(folder,),
                )
        with col_name:
            st.markdown(folder.path.name)
        with col_button:
            st.button(
                "", key=str(uuid.uuid4()), disabled=folder.statistics.synced, icon="🔄"
            )

        if not folder.collapsed:
            for subfolder in folder.folders:
                render_folder(subfolder)
            for file in folder.files:
                render_file(file)


def render_file(file: File) -> None:
    with st.container(border=True):
        col_name, col_button = st.columns([11, 1])
        with col_name:
            st.markdown(file.name)
        with col_button:
            st.button("", key=str(uuid.uuid4()), disabled=file.synced, icon="🔄")


def render_file_system() -> None:

    st.header("File System")

    if "Sync" in st.session_state["PageData"]:
        file_system = st.session_state["PageData"]["Sync"]

        # render the file system tree
        for folder in file_system.file_system.folders:
            render_folder(folder)
        for file in file_system.file_system.files:
            render_file(file)
    else:
        st.spinner("Loading file system...")
