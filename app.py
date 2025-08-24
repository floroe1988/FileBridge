from pathlib import Path
import streamlit as st
from src.pages import SyncPageData
from src.pages import synchronization_view, configuration_view, documentation_view


def main():
    # Initialize application data
    if "PageData" not in st.session_state:
        st.session_state["PageData"] = {}
        st.session_state["PageData"]["Sync"] = SyncPageData(
            conf=Path("config/config.yaml")
        )

    # Initialize the Streamlit app
    page = st.navigation(
        [
            st.Page(synchronization_view, title="Synchronization", icon="🔄"),
            st.Page(configuration_view, title="Configuration", icon="⚙️"),
            st.Page(documentation_view, title="Documentation", icon="📄"),
        ]
    )

    page.run()


if __name__ == "__main__":
    main()
