import requests

def fetch_pokemon(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def transform_pokemon(raw):
    return {
        "id": raw.get("id"),
        "name": raw.get("name"),
        "height": raw.get("height"),
        "weight": raw.get("weight"),
        "base_experience": raw.get("base_experience"),
        "types": [t["type"]["name"] for t in raw.get("types", [])],
        "abilities": [a["ability"]["name"] for a in raw.get("abilities", [])],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in raw.get("stats", [])},
    }
