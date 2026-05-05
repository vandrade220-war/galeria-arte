import streamlit as st


def inject_global_styles():
    """
    Injeta o CSS global da aplicação.
    """
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lato:wght@300;400;700&family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,400,0,0&display=swap');

/* =========================
   BASE
========================= */

#MainMenu,
footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* Esconde só ações extras do header, sem mexer na sidebar */
[data-testid="stHeaderActionElements"] {
    display: none !important;
}

body,
.stApp {
    background-color: #0f0e0d !important;
    color: #e8e0d4 !important;
    font-family: 'Lato', sans-serif !important;
}

.block-container {
    max-width: 100%;
    padding: 0.8rem 2rem 1.2rem 2rem;
}

/* =========================
   TIPOGRAFIA
========================= */

h1,
h2,
h3 {
    font-family: 'Playfair Display', serif !important;
    color: #d4b896 !important;
    letter-spacing: 0.02em;
}

p,
label,
input,
textarea,
select,
button,
[data-testid="stMarkdownContainer"] {
    font-family: 'Lato', sans-serif !important;
}

/* IMPORTANTE:
   Não aplique font-family global em div/span.
   Isso quebra os ícones internos do Streamlit.
*/

/* =========================
   LINKS
========================= */

a {
    color: #c9a96e !important;
    text-decoration: none;
}

a:hover {
    color: #e8d0a8 !important;
    text-decoration: underline;
}

/* =========================
   BOTÕES
========================= */

.stButton > button {
    background: transparent !important;
    border: 1px solid #5a4a35 !important;
    color: #d4b896 !important;
    font-family: 'Lato', sans-serif !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.03em !important;
    border-radius: 3px !important;
    padding: 0.45rem 0.9rem !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    background: #3a3025 !important;
    border-color: #c9a96e !important;
    color: #e8d0a8 !important;
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"] {
    background-color: #130f0c !important;
    border-right: 1px solid #3a3025;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] {
    color: #cdc4b8 !important;
}

.sidebar-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
}

.sidebar-header h2 {
    margin: 0;
    font-size: 1.4rem;
}

.menu-icon {
    font-size: 1.5rem;
    color: #d8b88f;
}

/* =========================
   BOTÕES NATIVOS DA SIDEBAR
   abrir / fechar
========================= */

/* Corrige ícones quebrados tipo double_arrow_right */
span[data-testid="stIconMaterial"],
[data-testid="stSidebarCollapsedControl"] span,
[data-testid="stSidebarCollapseButton"] span {
    font-family: "Material Symbols Rounded" !important;
    font-weight: normal !important;
    font-style: normal !important;
    font-size: 22px !important;
    line-height: 1 !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    white-space: nowrap !important;
    word-wrap: normal !important;
    direction: ltr !important;
    color: #ffffff !important;
    -webkit-font-feature-settings: "liga" !important;
    font-feature-settings: "liga" !important;
    -webkit-font-smoothing: antialiased !important;
}

/* Botão para abrir sidebar quando ela está fechada */
[data-testid="stSidebarCollapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    z-index: 999999 !important;
}

[data-testid="stSidebarCollapsedControl"] button {
    color: #ffffff !important;
    background: rgba(0, 0, 0, 0.45) !important;
    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    border-radius: 8px !important;
}

[data-testid="stSidebarCollapsedControl"] svg,
[data-testid="stSidebarCollapsedControl"] span {
    color: #ffffff !important;
    fill: #ffffff !important;
}

/* Botão para fechar sidebar quando ela está aberta */
[data-testid="stSidebarCollapseButton"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    z-index: 999999 !important;
}

[data-testid="stSidebarCollapseButton"] button {
    color: #ffffff !important;
    background: rgba(0, 0, 0, 0.35) !important;
    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    border-radius: 8px !important;
}

[data-testid="stSidebarCollapseButton"] svg,
[data-testid="stSidebarCollapseButton"] span {
    color: #ffffff !important;
    fill: #ffffff !important;
}

/* =========================
   INPUTS
========================= */

.stTextInput input {
    background: #1e1a16 !important;
    border: 1px solid #5a4a35 !important;
    color: #e8e0d4 !important;
    border-radius: 3px !important;
    font-family: 'Lato', sans-serif !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: #1e1a16 !important;
    border-color: #5a4a35 !important;
    color: #e8e0d4 !important;
    border-radius: 3px !important;
}

.stSelectbox div[data-baseweb="select"] span {
    color: #e8e0d4 !important;
}

hr {
    border-color: #3a3025 !important;
}

/* =========================
   VISUALIZADOR DA OBRA
========================= */

.viewer-wrap {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #1a1713;
    border: 1px solid #3a3025;
    border-radius: 4px;
    min-height: 380px;
    max-height: 62vh;
    overflow: hidden;
    position: relative;
    cursor: zoom-in;
}

.viewer-wrap img {
    max-width: 100%;
    max-height: 62vh;
    object-fit: contain;
    display: block;
}

#zoom-toggle {
    display: none;
}

.zoom-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.96);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    cursor: zoom-out;
}

.zoom-overlay img {
    max-width: 95vw;
    max-height: 95vh;
    object-fit: contain;
    box-shadow: 0 0 80px rgba(212, 184, 150, 0.12);
}

#zoom-toggle:checked + .zoom-overlay {
    display: flex;
}

/* =========================
   TEXTOS DA OBRA
========================= */

.artwork-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.35rem;
    color: #d4b896;
    margin: 0.6rem 0 0.2rem 0;
    line-height: 1.4;
}

.ai-context-box {
    background: linear-gradient(135deg, #1e1a16 0%, #231f1a 100%);
    border: 1px solid #5a4a35;
    border-left: 3px solid #c9a96e;
    border-radius: 6px;
    padding: 1.2rem 1.5rem;
    margin-top: 0.8rem;
    font-size: 0.93rem;
    line-height: 1.75;
    color: #cdc4b8;
}

.ai-context-box strong {
    color: #d4b896;
    font-family: 'Playfair Display', serif !important;
}

.nav-counter {
    text-align: center;
    opacity: 0.65;
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    padding-top: 0.5rem;
}

.movement-badge {
    display: inline-block;
    background: #2a2218;
    border: 1px solid #5a4a35;
    border-radius: 2px;
    padding: 0.1rem 0.55rem;
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    color: #a08060;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.artist-filter {
    font-size: 0.82rem;
    color: #9f8a70;
    margin-bottom: 0.5rem;
}

/* =========================
   MOBILE
========================= */

@media (max-width: 768px) {
    .block-container {
        padding: 1.2rem 1rem 1rem 1rem !important;
        max-width: 100% !important;
    }

    h1 {
        font-size: 2rem !important;
        line-height: 1.15 !important;
    }

    h2,
    h3 {
        font-size: 1.2rem !important;
    }

    section[data-testid="stSidebar"] {
        min-width: 280px !important;
        max-width: 86vw !important;
    }

    [data-testid="stHorizontalBlock"] {
        flex-wrap: wrap !important;
        gap: 0.5rem !important;
    }

    [data-testid="stHorizontalBlock"] > div {
        min-width: calc(50% - 0.5rem) !important;
        flex: 1 1 calc(50% - 0.5rem) !important;
    }

    .stButton > button {
        min-height: 44px !important;
        font-size: 0.95rem !important;
        padding: 0.55rem 0.7rem !important;
    }

    .viewer-wrap {
        min-height: 260px !important;
        max-height: none !important;
    }

    .viewer-wrap img {
        max-width: 100% !important;
        max-height: none !important;
        height: auto !important;
        object-fit: contain !important;
    }

    .artwork-title {
        font-size: 1.1rem !important;
    }

    .ai-context-box {
        padding: 1rem !important;
        font-size: 0.9rem !important;
    }
}
</style>
""",
        unsafe_allow_html=True,
    )

 