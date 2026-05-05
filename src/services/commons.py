import random
import requests
import streamlit as st


from src.config import (
    REQUEST_HEADERS,
    SEARCH_LIMIT,
    SEARCH_OFFSETS,
    WIKIMEDIA_COMMONS_API_URL,
)
from src.data.movements import MOVEMENTS
from src.utils.artwork import looks_like_artwork, artist_match_score, score_item
from src.utils.text import compact_spaces, get_extmetadata_value


SESSION = requests.Session()
SESSION.headers.update(REQUEST_HEADERS)


def parse_commons_pages(data: dict):
    """
    Transforma a resposta da API do Wikimedia Commons em uma lista de obras.
    """
    pages = data.get("query", {}).get("pages", {}) or {}
    arts = []

    for _, page in pages.items():
        image_info = (page.get("imageinfo") or [{}])[0] or {}
        thumb = image_info.get("thumburl") or image_info.get("url")
        original = image_info.get("url")
        meta = image_info.get("extmetadata") or {}

        if not (thumb or original):
            continue

        item = {
            "title": (page.get("title") or "").replace("File:", ""),
            "page_url": page.get("fullurl") or "",
            "thumb_url": thumb or "",
            "image_url": original or "",
            "width": image_info.get("width"),
            "height": image_info.get("height"),
            "artist_meta": get_extmetadata_value(meta, "Artist"),
            "object_name": get_extmetadata_value(meta, "ObjectName"),
            "description": get_extmetadata_value(meta, "ImageDescription"),
            "categories": get_extmetadata_value(meta, "Categories"),
            "license_short": get_extmetadata_value(meta, "LicenseShortName"),
        }

        arts.append(item)

    return arts


def commons_search(
    query: str,
    limit: int = 80,
    offset: int = 0,
    thumb_width: int = 1800,
):
    """
    Faz uma busca na API do Wikimedia Commons.
    """
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": query,
        "gsrlimit": limit,
        "gsroffset": offset,
        "gsrnamespace": 6,
        "gsrwhat": "text",
        "prop": "imageinfo|info",
        "iiprop": "url|size|extmetadata",
        "iiurlwidth": thumb_width,
        "inprop": "url",
        "origin": "*",
    }

    response = SESSION.get(
        WIKIMEDIA_COMMONS_API_URL,
        params=params,
        timeout=25,
    )

    response.raise_for_status()

    return parse_commons_pages(response.json())


@st.cache_data(ttl=600, show_spinner=False)
def cached_search(
    query: str,
    limit: int,
    offset: int,
    thumb_width: int,
):
    """
    Versão cacheada da busca para evitar chamadas repetidas.
    """
    return commons_search(
        query=query,
        limit=limit,
        offset=offset,
        thumb_width=thumb_width,
    )


def build_search_queries(base_query: str, artist_name: str):
    """
    Monta as variações de busca usadas no Wikimedia Commons.
    """
    queries = []

    if artist_name:
        safe_artist = artist_name.replace('"', '\\"')

        queries.append(f'({base_query}) AND ("{safe_artist}")')
        queries.append(f'"{safe_artist}" AND ({base_query})')
        queries.append(f'"{safe_artist}" painting')
        queries.append(f'"{safe_artist}" artwork')
        queries.append(f'"{safe_artist}"')
    else:
        queries.append(base_query)

    seen_queries = set()
    final_queries = []

    for query in queries:
        if query not in seen_queries:
            final_queries.append(query)
            seen_queries.add(query)

    return final_queries


def remove_duplicates(items: list[dict]) -> list[dict]:
    """
    Remove obras repetidas usando URL, página ou título como chave.
    """
    unique = {}

    for item in items:
        key = item.get("image_url") or item.get("page_url") or item.get("title")

        if key not in unique:
            unique[key] = item

    return list(unique.values())


def search_with_filters(thumb_width: int):
    """
    Busca obras aplicando filtros de movimento, artista e qualidade do resultado.
    """
    movement = st.session_state["movement"]
    artist_name = compact_spaces(st.session_state.get("artist_name", ""))
    base_query = MOVEMENTS.get(movement, "painting").strip()

    offsets = SEARCH_OFFSETS.copy()
    random.shuffle(offsets)

    final_queries = build_search_queries(
        base_query=base_query,
        artist_name=artist_name,
    )

    best_results = []

    for query in final_queries:
        collected = []

        for offset in offsets[:4]:
            batch = cached_search(
                query=query,
                limit=SEARCH_LIMIT,
                offset=offset,
                thumb_width=thumb_width,
            )

            collected.extend(batch)

        unique_items = remove_duplicates(collected)

        filtered = [
            item
            for item in unique_items
            if looks_like_artwork(item)
        ]

        if artist_name:
            filtered = [
                item
                for item in filtered
                if artist_match_score(item, artist_name) >= 35
            ]

        ranked = sorted(
            filtered,
            key=lambda item: score_item(item, artist_name),
            reverse=True,
        )

        if ranked:
            st.session_state["query"] = query
            return ranked[:80]

        if not best_results:
            fallback_ranked = sorted(
                [
                    item
                    for item in unique_items
                    if looks_like_artwork(item)
                ],
                key=lambda item: score_item(item, artist_name),
                reverse=True,
            )

            best_results = fallback_ranked[:80]

    st.session_state["query"] = final_queries[0]

    return best_results