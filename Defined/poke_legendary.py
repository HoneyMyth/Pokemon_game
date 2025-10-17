import requests

def FnPoke_legendary(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("is_legendary", False)
    else:
        print("Pokémon not found.")
        return None

