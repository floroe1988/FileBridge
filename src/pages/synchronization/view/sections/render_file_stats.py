import streamlit as st


def render_element(text: str, number: int) -> None:
    with st.container(border=True):
        st.markdown(f"**{text}**: {number}")


def render_file_stats():

    st.header("File Overview")

    if "Sync" in st.session_state["PageData"]:
        file_system = st.session_state["PageData"]["Sync"]
        col_left, col_right = st.columns(2)

        with col_left:
            render_element("Total Folders", file_system.folder_stats.total_folders)
            render_element(
                "Unsynced Folders", file_system.folder_stats.unsynced_folders
            )

        with col_right:
            render_element("Total Files", file_system.folder_stats.total_files)
            render_element("Unsynced Files", file_system.folder_stats.unsynced_files)
    else:
        st.spinner("Loading file system...")
