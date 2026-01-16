# -*- coding: utf-8 -*-
import random
import requests
import streamlit as st

API = "https://commons.wikimedia.org/w/api.php"

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "MinhaGaleriaArte/1.0 (local; contato: seu_email@exemplo.com)",
    "Api-User-Agent": "MinhaGaleriaArte/1.0 (local; contato: seu_email@exemplo.com)",
    "Accept": "application/json",
})


# Map: nome do movimento -> query no Commons
MOVEMENTS = {
    "Grega (beleza ideal e proporcao)": 'greek art OR "ancient greek" OR "classical greece" OR hellenic OR sculpture AND (vase OR pottery OR statue OR relief OR mosaic OR painting)',
    "Romana (realismo e monumentalidade)": 'roman art OR "ancient rome" OR "roman empire" AND (sculpture OR bust OR relief OR fresco OR mosaic OR architecture)',
    "Paleocrista": '"early christian" OR paleochristian OR catacomb OR basilica AND (mosaic OR fresco OR icon OR church)',
    "Bizantina (mosaicos e arte religiosa)": 'byzantine OR "byzantine art" AND (mosaic OR icon OR church OR religious)',
    "Romanica (formas solidas e temas biblicos)": 'romanesque OR "romanesque art" AND (church OR cathedral OR fresco OR sculpture OR tympanum)',
    "Gotica (vitrais, verticalidade e luz)": 'gothic OR "gothic art" AND (stained glass OR cathedral OR altarpiece OR illumination OR sculpture)',
    "Renascimento (XIV-XVI)": 'renaissance OR "italian renaissance" OR (Leonardo OR Michelangelo OR Raphael) AND (painting OR fresco OR sculpture)',
    "Maneirismo (XVI)": 'mannerism OR manierismo OR (El Greco OR Parmigianino OR Pontormo OR Bronzino) AND (painting OR altarpiece)',
    "Barroco (XVII-XVIII)": 'baroque OR barroco OR (Caravaggio OR Rubens OR Rembrandt OR Bernini OR Velazquez) AND (painting OR sculpture)',
    "Rococo (XVIII)": 'rococo OR rococó OR (Watteau OR Fragonard OR Boucher) AND (painting OR portrait)',
    "Neoclassicismo (XVIII-XIX)": 'neoclassicism OR neoclassical OR (Jacques-Louis David OR Ingres OR Canova) AND (painting OR sculpture)',
    "Romantismo (XIX)": 'romanticism OR romantismo OR (Delacroix OR Goya OR Turner OR Friedrich) AND (painting)',
    "Realismo (XIX)": 'realism art OR realismo AND (Courbet OR Millet OR Daumier OR "social realism") AND (painting)',
    "Impressionismo (XIX)": 'impressionism OR impressionist AND (Monet OR Renoir OR Degas OR Pissarro) AND (painting)',
    "Pos-Impressionismo (XIX)": '"post-impressionism" OR postimpressionism OR (Van Gogh OR Cezanne OR Gauguin OR Seurat) AND (painting)',
    "Expressionismo (XX)": 'expressionism OR expressionist AND (Munch OR Kirchner OR Kandinsky) AND (painting)',
    "Cubismo (XX)": 'cubism OR cubist AND (Picasso OR Braque OR Gris) AND (painting)',
    "Futurismo (XX)": 'futurism OR futurist AND (Boccioni OR Balla OR Severini) AND (painting OR sculpture)',
    "Dadaismo (XX)": 'dada OR dadaism AND (Duchamp OR Arp OR Hausmann) AND (artwork OR collage OR painting)',
    "Surrealismo (XX)": 'surrealism OR surrealist AND (Dali OR Magritte OR Ernst OR Miro) AND (painting)',
}


def commons_search(query: str, limit: int = 80, offset: int = 0, thumb_width: int = 1800):
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": query,
        "gsrlimit": limit,
        "gsroffset": offset,
        "gsrnamespace": 6,  # File:
        "gsrwhat": "text",
        "prop": "imageinfo|info",
        "iiprop": "url|size",
        "iiurlwidth": thumb_width,
        "inprop": "url",
        "origin": "*",
    }

    r = SESSION.get(API, params=params, timeout=20)
    r.raise_for_status()
    data = r.json()

    pages = data.get("query", {}).get("pages", {}) or {}
    arts = []
    for _, page in pages.items():
        ii = (page.get("imageinfo") or [{}])[0] or {}
        thumb = ii.get("thumburl") or ii.get("url")
        original = ii.get("url")

        if not (thumb or original):
            continue

        arts.append({
            "title": (page.get("title") or "").replace("File:", ""),
            "page_url": page.get("fullurl") or "",
            "thumb_url": thumb or "",
            "image_url": original or "",
            "width": ii.get("width"),
            "height": ii.get("height"),
        })

    random.shuffle(arts)
    return arts


@st.cache_data(ttl=600, show_spinner=False)
def cached_search(query: str, limit: int, offset: int, thumb_width: int):
    return commons_search(query=query, limit=limit, offset=offset, thumb_width=thumb_width)


def ensure_state():
    st.session_state.setdefault("artworks", [])
    st.session_state.setdefault("idx", 0)
    st.session_state.setdefault("thumb_w", 1800)
    st.session_state.setdefault("movement", "Impressionismo (XIX)")
    st.session_state.setdefault("query", MOVEMENTS.get(st.session_state["movement"], "painting"))


def load_batch():
    # offsets diferentes para variar
    offset = random.choice([0, 40, 80, 120, 160, 200, 240])
    q = st.session_state["query"].strip()
    tw = int(st.session_state["thumb_w"])

    st.session_state["artworks"] = cached_search(query=q, limit=80, offset=offset, thumb_width=tw)
    st.session_state["idx"] = 0


def current_art():
    arts = st.session_state["artworks"]
    if not arts:
        return None
    return arts[st.session_state["idx"] % len(arts)]


# ---------------- UI ----------------
ensure_state()
st.set_page_config(page_title="Galeria de Arte", layout="wide")

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}

.block-container { max-width: 100%; padding-top: 0.6rem; }

/* area principal */
.viewer {
    width: 100%;
    height: calc(100vh - 310px);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: zoom-in;
}
.viewer img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain; /* troque para cover se quiser preencher cortando */
}

/* zoom overlay (CSS-only) */
#zoom-toggle { display: none; }
.zoom-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.92);
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
}
#zoom-toggle:checked + .zoom-overlay { display: flex; }
</style>
""", unsafe_allow_html=True)

st.title("Galeria de Arte (filtro por periodo/movimento)")

# ---- Painel de filtros ----
with st.expander("Filtros (movimento, busca e resolucao)", expanded=True):
    a, b, c = st.columns([2, 3, 1])

    with a:
        movement = st.selectbox(
            "Escolha um movimento",
            list(MOVEMENTS.keys()),
            index=list(MOVEMENTS.keys()).index(st.session_state["movement"]) if st.session_state["movement"] in MOVEMENTS else 0,
        )
        if movement != st.session_state["movement"]:
            st.session_state["movement"] = movement
            st.session_state["query"] = MOVEMENTS[movement]
            st.session_state["artworks"] = []
            st.session_state["idx"] = 0

    with b:
        st.session_state["query"] = st.text_input(
            "Query (voce pode editar)",
            value=st.session_state["query"],
            help="Isso e o que vai para a busca do Commons (MediaWiki search).",
        )

    with c:
        st.session_state["thumb_w"] = st.number_input(
            "Resolucao (px)",
            min_value=800,
            max_value=3000,
            value=int(st.session_state["thumb_w"]),
            step=100,
        )

    x, y = st.columns([1, 1])
    with x:
        if st.button("Carregar / atualizar", type="primary"):
            load_batch()
    with y:
        if st.button("Novo lote (aleatorio)"):
            load_batch()

# carrega automaticamente se estiver vazio
if not st.session_state["artworks"]:
    with st.spinner("Buscando obras..."):
        load_batch()

art = current_art()
if not art:
    st.warning("Nao encontrei imagens com essa busca. Troque o movimento ou ajuste a query.")
    st.stop()

# ---- Navegacao ----
c1, c2, c3, c4, c5 = st.columns([1, 1, 2, 1, 1])

with c1:
    if st.button("⬅ Anterior"):
        st.session_state["idx"] = (st.session_state["idx"] - 1) % len(st.session_state["artworks"])
with c2:
    if st.button("Aleatoria"):
        st.session_state["idx"] = random.randrange(len(st.session_state["artworks"]))
with c4:
    if st.button("Proxima ➡"):
        st.session_state["idx"] = (st.session_state["idx"] + 1) % len(st.session_state["artworks"])
with c5:
    if st.button("Novo lote"):
        load_batch()

with c3:
    st.markdown(
        f"<div style='text-align:center; opacity:0.8; padding-top: 0.4rem;'>"
        f"{st.session_state['idx'] + 1} / {len(st.session_state['artworks'])}"
        f"</div>",
        unsafe_allow_html=True
    )

# ---- Viewer + zoom ----
img_url = art["thumb_url"] or art["image_url"]

st.markdown(
    f"""
<label class="viewer" for="zoom-toggle" title="Clique para ampliar">
    <img src="{img_url}">
</label>

<input type="checkbox" id="zoom-toggle">

<label class="zoom-overlay" for="zoom-toggle" title="Clique para fechar">
    <img src="{art["image_url"] or img_url}">
</label>
""",
    unsafe_allow_html=True,
)

# ---- Infos ----
st.markdown(f"### {art['title']}")
links = []
if art.get("page_url"):
    links.append(f"[pagina no Commons]({art['page_url']})")
if art.get("image_url"):
    links.append(f"[abrir imagem original]({art['image_url']})")
if links:
    st.markdown(" | ".join(links))
