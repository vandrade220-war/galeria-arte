import streamlit as st

from src.config import DEFAULT_MOVEMENT, DEFAULT_QUERY, DEFAULT_THUMB_WIDTH
from src.data.movements import MOVEMENTS
from src.services.commons import search_with_filters
from src.utils.text import compact_spaces


def ensure_state():
    """
    Garante que todas as variáveis necessárias existam no session_state.
    """
    st.session_state.setdefault("artworks", [])
    st.session_state.setdefault("idx", 0)
    st.session_state.setdefault("thumb_w", DEFAULT_THUMB_WIDTH)
    st.session_state.setdefault("movement", DEFAULT_MOVEMENT)
    st.session_state.setdefault("artist_name", "")
    st.session_state.setdefault(
        "query",
        MOVEMENTS.get(DEFAULT_MOVEMENT, DEFAULT_QUERY),
    )
    st.session_state.setdefault("show_context", False)
    st.session_state.setdefault("ai_context", "")


def clear_ai_context():
    """
    Limpa o contexto gerado pela IA quando a obra, artista ou lote muda.
    """
    st.session_state["ai_context"] = ""
    st.session_state["show_context"] = False


def load_batch():
    """
    Carrega um novo lote de obras com base nos filtros atuais.
    """
    thumb_w = int(st.session_state["thumb_w"])

    st.session_state["artworks"] = search_with_filters(
        thumb_width=thumb_w,
    )

    st.session_state["idx"] = 0
    clear_ai_context()


def current_art():
    """
    Retorna a obra atual da galeria.
    """
    arts = st.session_state["artworks"]

    if not arts:
        return None

    return arts[st.session_state["idx"] % len(arts)]


def apply_artist_search():
    """
    Aplica o texto digitado no campo de busca por artista.
    Essa função é usada no on_change do st.text_input.
    """
    st.session_state["artist_name"] = compact_spaces(
        st.session_state.get("artist_input", "")
    )

    st.session_state["idx"] = 0
    load_batch()