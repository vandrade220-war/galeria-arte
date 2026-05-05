import streamlit as st


def inject_global_styles():
    """
    Injeta o CSS global da aplicação.
    """
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lato:wght@300;400;700&display=swap');

#MainMenu, footer {
    visibility: hidden;
}

[data-testid="stSidebarCollapsedControl"] {
    display: none !important;
}

button[kind="header"],
[data-testid="stHeaderActionElements"] {
    display: none !important;
}

header {
    background: transparent !important;
}

body, .stApp {
    background-color: #0f0e0d;
    color: #e8e0d4;
}

.block-container {
    max-width: 100%;
    padding: 0.8rem 2rem 1.2rem 2rem;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #d4b896 !important;
    letter-spacing: 0.02em;
}

p, label, div, span {
    font-family: 'Lato', sans-serif !important;
}

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
    background: rgba(0,0,0,0.96);
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
    box-shadow: 0 0 80px rgba(212,184,150,0.12);
}

#zoom-toggle:checked + .zoom-overlay {
    display: flex;
}

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

a {
    color: #c9a96e !important;
    text-decoration: none;
}

a:hover {
    color: #e8d0a8 !important;
    text-decoration: underline;
}

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

section[data-testid="stSidebar"] {
    background-color: #130f0c !important;
    border-right: 1px solid #3a3025;
}

section[data-testid="stSidebar"] * {
    color: #cdc4b8 !important;
}

.stTextInput input,
.stSelectbox select {
    background: #1e1a16 !important;
    border: 1px solid #5a4a35 !important;
    color: #e8e0d4 !important;
    border-radius: 3px !important;
    font-family: 'Lato', sans-serif !important;
}

hr {
    border-color: #3a3025 !important;
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
</style>
""",
        unsafe_allow_html=True,
    )