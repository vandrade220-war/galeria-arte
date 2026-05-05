import streamlit as st

from src.config import OPENAI_API_KEY
from src.data.movements import MOVEMENTS
from src.services.ai import get_ai_context
from src.state import (
    apply_artist_search,
    clear_ai_context,
    current_art,
    load_batch,
)


def render_sidebar():
    """
    Renderiza a barra lateral com filtros e ações.
    """
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-header">
                <span class="menu-icon">☰</span>
                <h2>Configurações</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        movement_options = list(MOVEMENTS.keys())

        selected_movement = st.selectbox(
            "Movimento artístico",
            movement_options,
            index=(
                movement_options.index(st.session_state["movement"])
                if st.session_state["movement"] in movement_options
                else 0
            ),
        )

        if selected_movement != st.session_state["movement"]:
            st.session_state["movement"] = selected_movement
            st.session_state["idx"] = 0
            clear_ai_context()
            load_batch()
            st.rerun()

        if "artist_input" not in st.session_state:
            st.session_state["artist_input"] = st.session_state.get("artist_name", "")

        st.text_input(
            "Buscar artista",
            key="artist_input",
            placeholder="Ex.: Monet, Van Gogh, Goya",
            on_change=apply_artist_search,
        )

        new_thumb_w = st.slider(
            "Resolução",
            min_value=800,
            max_value=3000,
            value=int(st.session_state["thumb_w"]),
            step=100,
        )

        if new_thumb_w != int(st.session_state["thumb_w"]):
            st.session_state["thumb_w"] = int(new_thumb_w)

        col_a, col_b = st.columns(2)

        with col_a:
            if st.button("🔄 Carregar", use_container_width=True):
                load_batch()
                st.rerun()

        with col_b:
            if st.button("🎲 Aleatório", use_container_width=True):
                load_batch()
                st.rerun()

        if st.button("✦ Contexto com IA", use_container_width=True):
            art_now = current_art()

            if art_now is not None:
                st.session_state["show_context"] = True
                st.session_state["ai_context"] = ""

                with st.spinner("Consultando a IA..."):
                    st.session_state["ai_context"] = get_ai_context(
                        title=art_now["title"],
                        movement=st.session_state["movement"],
                        api_key=OPENAI_API_KEY,
                    )

                st.rerun()