import requests
from config import ALPHA_VANTAGE_KEY, ALPHA_VANTAGE_BASE_URL


def get_latest_quote(symbol):
    params = {"function": "GLOBAL_QUOTE", "symbol": symbol, "apikey": ALPHA_VANTAGE_KEY}
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


def get_daily_time_series(symbol):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "apikey": ALPHA_VANTAGE_KEY,
    }
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
    response.raise_for_status()
    return response.json()
