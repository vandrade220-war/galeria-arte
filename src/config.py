import os


try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


APP_TITLE = "Galeria de Arte"
PAGE_LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

WIKIMEDIA_COMMONS_API_URL = "https://commons.wikimedia.org/w/api.php"

REQUEST_HEADERS = {
    "User-Agent": "MinhaGaleriaArte/1.0 (local)",
    "Api-User-Agent": "MinhaGaleriaArte/1.0 (local)",
    "Accept": "application/json",
}

DEFAULT_MOVEMENT = "Impressionismo (XIX)"
DEFAULT_QUERY = "painting"
DEFAULT_THUMB_WIDTH = 1800

SEARCH_LIMIT = 50
SEARCH_OFFSETS = [0, 40, 80, 120, 160, 200, 240]