import html
import random
import streamlit as st

from src.state import clear_ai_context, current_art, load_batch


def render_header():
    """
    Renderiza o cabeçalho principal da galeria.
    """
    st.markdown(
        """
<div style="font-family:Playfair Display,serif; font-size:1.9rem;
color:#d4b896; margin-bottom:0.1rem; letter-spacing:0.03em;">
Galeria de Arte
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div style="font-size:0.8rem; color:#7a6a58; letter-spacing:0.12em;
text-transform:uppercase; margin-bottom:1.2rem;">
Coleção permanente • Wikimedia Commons
</div>
""",
        unsafe_allow_html=True,
    )


def render_navigation():
    """
    Renderiza os botões de navegação entre obras.
    """
    n1, n2, n3, n4, n5 = st.columns([1, 1, 2, 1, 1])

    with n1:
        if st.button("← Anterior"):
            st.session_state["idx"] = (
                st.session_state["idx"] - 1
            ) % len(st.session_state["artworks"])
            clear_ai_context()
            st.rerun()

    with n2:
        if st.button("⚄ Aleatória"):
            st.session_state["idx"] = random.randrange(
                len(st.session_state["artworks"])
            )
            clear_ai_context()
            st.rerun()

    with n3:
        st.markdown(
            f"""
<div class="nav-counter">
{st.session_state["idx"] + 1} / {len(st.session_state["artworks"])}
</div>
""",
            unsafe_allow_html=True,
        )

    with n4:
        if st.button("Próxima →"):
            st.session_state["idx"] = (
                st.session_state["idx"] + 1
            ) % len(st.session_state["artworks"])
            clear_ai_context()
            st.rerun()

    with n5:
        if st.button("↻ Novo lote"):
            load_batch()
            st.rerun()


def render_artwork_image(art: dict):
    """
    Renderiza a imagem da obra com zoom ao clicar.
    """
    img_url = art["thumb_url"] or art["image_url"]
    safe_title = html.escape(art["title"] or "")

    st.markdown(
        f"""
<label class="viewer-wrap" for="zoom-toggle" title="Clique para ampliar">
    <img src="{html.escape(img_url)}" alt="{safe_title}">
</label>

<input type="checkbox" id="zoom-toggle">

<label class="zoom-overlay" for="zoom-toggle" title="Clique para fechar">
    <img src="{html.escape(art["image_url"] or img_url)}" alt="{safe_title}">
</label>
""",
        unsafe_allow_html=True,
    )


def render_artwork_info(art: dict):
    """
    Renderiza título, movimento, artista filtrado e links da obra.
    """
    safe_title = html.escape(art["title"] or "")

    st.markdown(
        f"""
<div class="movement-badge">
{html.escape(st.session_state["movement"])}
</div>
""",
        unsafe_allow_html=True,
    )

    if st.session_state.get("artist_name", "").strip():
        st.markdown(
            f"""
<div class="artist-filter">
Artista filtrado: {html.escape(st.session_state["artist_name"])}
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown(
        f'<div class="artwork-title">{safe_title}</div>',
        unsafe_allow_html=True,
    )

    link_parts = []

    if art.get("page_url"):
        link_parts.append(
            f'<a href="{html.escape(art["page_url"])}" target="_blank">'
            f"Página no Commons</a>"
        )

    if art.get("image_url"):
        link_parts.append(
            f'<a href="{html.escape(art["image_url"])}" target="_blank">'
            f"Imagem original</a>"
        )

    if link_parts:
        st.markdown(
            """
<div style="font-size:0.8rem; color:#7a6a58; margin-bottom:0.8rem;">
"""
            + " &nbsp;·&nbsp; ".join(link_parts)
            + """
</div>
""",
            unsafe_allow_html=True,
        )


def render_ai_context():
    """
    Renderiza o contexto gerado pela IA, quando existir.
    """
    if st.session_state.get("show_context") and st.session_state.get("ai_context"):
        safe_context = html.escape(st.session_state["ai_context"]).replace(
            "\n",
            "<br>",
        )

        st.markdown(
            f"""
<div class="ai-context-box">
<strong>✦ Contexto da obra</strong><br><br>
{safe_context}
</div>
""",
            unsafe_allow_html=True,
        )


def render_gallery(art: dict):
    """
    Renderiza a galeria completa.
    """
    render_header()
    render_navigation()

    art = current_art()

    if not art:
        st.warning("Nenhuma obra disponível.")
        st.stop()

    render_artwork_image(art)
    render_artwork_info(art)
    render_ai_context()