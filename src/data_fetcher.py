from .config import config
import requests

def get_latest_version():
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    return requests.get(url).json()[0]

def fetch_items(version=None):
    if version is None:
        version = get_latest_version()
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{config.lang}/item.json"
    return requests.get(url).json()["data"]