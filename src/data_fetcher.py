import requests

# detects the latest version
def get_latest_version():
    versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    return requests.get(versions_url).json()[0]

# loads item data / Korean mode
def fetch_items(version = None, language = "en_US"):
    if version is None:
        version = get_latest_version()
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/item.json"
    return requests.get(url).json()["data"]