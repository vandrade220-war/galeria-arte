# -*- coding: utf-8 -*-

from src.data.filters import (
    ART_RELATED_TERMS,
    BAD_EXTENSIONS,
    BAD_TITLE_TERMS,
    GOOD_IMAGE_EXTENSIONS,
)
from src.utils.text import compact_spaces, normalize_text


def artist_aliases(name: str):
    """
    Cria variações simples do nome do artista para melhorar o filtro.
    Exemplo: 'Vincent van Gogh' vira também 'Gogh' e 'Vincent Gogh'.
    """
    clean = compact_spaces(name)

    if not clean:
        return []

    aliases = {clean}
    parts = clean.split()

    if len(parts) >= 2:
        aliases.add(parts[-1])
        aliases.add(f"{parts[0]} {parts[-1]}")

    return [alias for alias in aliases if alias]


def extension_ok(title: str) -> bool:
    """
    Verifica se o arquivo parece ser uma imagem válida.
    """
    title_normalized = normalize_text(title)

    if title_normalized.endswith(BAD_EXTENSIONS):
        return False

    return title_normalized.endswith(GOOD_IMAGE_EXTENSIONS)


def is_bad_document_like(item: dict) -> bool:
    """
    Remove resultados que parecem páginas de livros, catálogos, PDFs etc.
    """
    combined = " ".join(
        [
            normalize_text(item.get("title", "")),
            normalize_text(item.get("artist_meta", "")),
            normalize_text(item.get("object_name", "")),
            normalize_text(item.get("description", "")),
            normalize_text(item.get("categories", "")),
        ]
    )

    if any(term in combined for term in BAD_TITLE_TERMS):
        return True

    if "google books" in combined or "internet archive" in combined:
        return True

    return False


def looks_like_artwork(item: dict) -> bool:
    """
    Verifica se o item parece ser uma obra de arte utilizável na galeria.
    """
    title = item.get("title", "")

    if not extension_ok(title):
        return False

    if is_bad_document_like(item):
        return False

    combined = " ".join(
        [
            normalize_text(item.get("title", "")),
            normalize_text(item.get("artist_meta", "")),
            normalize_text(item.get("object_name", "")),
            normalize_text(item.get("description", "")),
            normalize_text(item.get("categories", "")),
        ]
    )

    if any(term in combined for term in ART_RELATED_TERMS):
        return True

    return False


def artist_match_score(item: dict, artist_name: str) -> int:
    """
    Dá uma pontuação de compatibilidade entre o item e o artista buscado.
    """
    artist_name = compact_spaces(artist_name)

    if not artist_name:
        return 0

    aliases = artist_aliases(artist_name)

    haystacks = {
        "artist_meta": normalize_text(item.get("artist_meta", "")),
        "object_name": normalize_text(item.get("object_name", "")),
        "description": normalize_text(item.get("description", "")),
        "title": normalize_text(item.get("title", "")),
        "categories": normalize_text(item.get("categories", "")),
    }

    score = 0

    for alias in aliases:
        alias_normalized = normalize_text(alias)

        if not alias_normalized:
            continue

        if alias_normalized in haystacks["artist_meta"]:
            score += 120

        if alias_normalized in haystacks["object_name"]:
            score += 70

        if alias_normalized in haystacks["description"]:
            score += 45

        if alias_normalized in haystacks["title"]:
            score += 35

        if alias_normalized in haystacks["categories"]:
            score += 25

    artist_normalized = normalize_text(artist_name)

    if "after " + artist_normalized in haystacks["description"]:
        score -= 50

    if "school of " + artist_normalized in haystacks["description"]:
        score -= 40

    if "attributed to " + artist_normalized in haystacks["description"]:
        score -= 15

    return score


def score_item(item: dict, artist_name: str) -> int:
    """
    Calcula a pontuação final para ordenar os resultados.
    """
    score = 0

    if looks_like_artwork(item):
        score += 100
    else:
        score -= 200

    score += artist_match_score(item, artist_name)

    title_normalized = normalize_text(item.get("title", ""))

    if any(
        term in title_normalized
        for term in ["portrait", "painting", "retrato", "pintura"]
    ):
        score += 8

    return score