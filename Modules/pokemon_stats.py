import poke_input_name

def FnPoke_stats():
    pokemon_file = poke_input_name.FnPoke_input()
    pokemon_stats_list = pokemon_file["stats"]
    return pokemon_stats_list

if __name__ == "__main__":
    FnPoke_stats()