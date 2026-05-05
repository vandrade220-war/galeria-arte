import streamlit as st

from src.config import APP_TITLE, PAGE_LAYOUT, INITIAL_SIDEBAR_STATE
from src.state import ensure_state, load_batch, current_art
from src.styles import inject_global_styles
from src.ui.sidebar import render_sidebar
from src.ui.gallery import render_gallery


st.set_page_config(
    page_title=APP_TITLE,
    layout=PAGE_LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE,
)


def main():
    ensure_state()
    inject_global_styles()

    if not st.session_state["artworks"]:
        with st.spinner("Buscando obras de arte..."):
            load_batch()

    render_sidebar()

    if not st.session_state["artworks"]:
        st.warning("Nenhuma imagem encontrada para esse filtro.")
        st.stop()

    art = current_art()

    if not art:
        st.warning("Nenhuma obra disponível.")
        st.stop()

    render_gallery(art)


if __name__ == "__main__":
    main()