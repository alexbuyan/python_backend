import json

from httpx import Client

pokemon_url = "https://pokeapi.co/api/v2/pokemon"


def get_pokemon_abilities(name: str):
    client = Client()
    response = client.get(f"{pokemon_url}/{name}")
    if response.status_code != 200:
        return {"error": "Invalid response"}
    response_json = json.loads(response.text)
    response_abilities = response_json["abilities"]
    abilites = []
    for ability in response_abilities:
        ability_name = ability["ability"]["name"]
        abilites.append(ability_name)
    return {name: abilites}
