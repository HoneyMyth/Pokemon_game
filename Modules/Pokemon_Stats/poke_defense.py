import pokemon_stats

def FnPoke_defense(poke_list):
    dict_stat = poke_list[2]

    return dict_stat["base_stat"]

if __name__ == "__main__":
    FnPoke_defense()
