# -*- coding: utf-8 -*-

import html
import re


def normalize_text(value: str) -> str:
    """
    Normaliza textos para facilitar buscas e comparações.
    """
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    value = value.replace("_", " ")
    value = re.sub(r"\s+", " ", value).strip().lower()

    return value


def compact_spaces(value: str) -> str:
    """
    Remove espaços extras.
    """
    return re.sub(r"\s+", " ", (value or "").strip())


def strip_html(value: str) -> str:
    """
    Remove tags HTML e compacta o texto.
    """
    text = html.unescape(value or "")
    text = re.sub(r"<[^>]+>", " ", text)

    return compact_spaces(text)


def get_extmetadata_value(meta: dict, key: str) -> str:
    """
    Lê um valor do extmetadata da API do Wikimedia Commons.
    """
    raw = (meta or {}).get(key, {})

    if isinstance(raw, dict):
        return strip_html(raw.get("value", ""))

    return ""