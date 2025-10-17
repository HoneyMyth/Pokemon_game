def FnPoke_stats(pokemon_file):
    pokemon_stats_list = pokemon_file["stats"]
    return pokemon_stats_list

#speed
def FnPoke_speed(pokemon_stats_list):
    dict_stat = pokemon_stats_list[5]

    return dict_stat["base_stat"]

#spdefense
def FnPoke_spdefense(poke_list):
    dict_stat = poke_list[4]

    return dict_stat["base_stat"]

#spattack
def FnPoke_spattack(poke_list):
    dict_stat = poke_list[3]

    return dict_stat["base_stat"]

#defense
def FnPoke_defense(poke_list):
    dict_stat = poke_list[2]

    return dict_stat["base_stat"]

#attack
def FnPoke_attack(poke_list):
    dict_stat = poke_list[1]

    return dict_stat["base_stat"]


#hp
def FnPoke_hp(poke_list):    
    dict_stat = poke_list[0]

    return dict_stat["base_stat"]

