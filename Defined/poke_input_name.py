import requests
import json

def FnPoke_input():
    url_pokemon_name = "https://pokeapi.co/api/v2/pokemon/"
    poke_name = input("The name of the Pokemon: ")

    for i in range(len(list(poke_name))):
        if poke_name[i].isdigit():
            print("Numbers are not pokemon;)")
            break
    

    poke_name = str(poke_name).lower().strip()

    response = requests.get(f"{url_pokemon_name}{poke_name}")

    if response.status_code == 200:
        response = requests.get(f"{url_pokemon_name}{poke_name}")

    else:
        print(f"Error: Pokémon '{poke_name}' not found. Status code: {response.status_code}")
        exit()

    return response.json()


    
