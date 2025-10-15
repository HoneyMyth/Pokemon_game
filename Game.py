from Defined.poke_input_name import FnPoke_input
from Defined.poke_attack import FnPoke_attack
from Defined.poke_defense import FnPoke_defense
from Defined.poke_hp import FnPoke_hp
from Defined.poke_spattack import FnPoke_spattack
from Defined.poke_speed import FnPoke_speed
from Defined.poke_spdefense import FnPoke_spdefense
from Defined.poke_stats import FnPoke_stats


print(r"""
███████╗███╗   ██╗████████╗███████╗██████╗     ██╗   ██╗ ██████╗ ██╗   ██╗██████╗      ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗
██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗    ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗     ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║
█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝     ╚████╔╝ ██║   ██║██║   ██║██████╔╝     ██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗      ╚██╔╝  ██║   ██║██║   ██║██╔══██╗     ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
███████╗██║ ╚████║   ██║   ███████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝██║  ██║     ██║     ╚██████╔╝██║  ╚██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═╝      ╚═════╝ ╚═╝   ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
""")


pokemon_1 = FnPoke_input()

print(f"\nExcellent choice! Your pokemon is ready for battle!")

pokemon_1_stats = FnPoke_stats(pokemon_1)

spdefense_1 = FnPoke_spdefense(pokemon_1_stats)
spattack_1 = FnPoke_spattack(pokemon_1_stats)
attack_1 = FnPoke_attack(pokemon_1_stats)
defense_1 = FnPoke_defense(pokemon_1_stats)
hp_1 = FnPoke_hp(pokemon_1_stats)
speed_1 = FnPoke_speed(pokemon_1_stats)


pokemon_1_stats = [hp_1,defense_1,attack_1,spdefense_1,spattack_1,speed_1]

for stat in pokemon_1_stats:
    print(stat)

print("\n" * 50)


print(r"""
███████╗███╗   ██╗████████╗███████╗██████╗     ██╗   ██╗ ██████╗ ██╗   ██╗██████╗      ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗
██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗    ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗     ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║
█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝     ╚████╔╝ ██║   ██║██║   ██║██████╔╝     ██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗      ╚██╔╝  ██║   ██║██║   ██║██╔══██╗     ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
███████╗██║ ╚████║   ██║   ███████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝██║  ██║     ██║     ╚██████╔╝██║  ╚██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═╝      ╚═════╝ ╚═╝   ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
""")


pokemon_2 = FnPoke_input()

print(f"\nExcellent choice! Your pokemon is ready for battle!")

pokemon_2_stats = FnPoke_stats(pokemon_2)

spdefense_2 = FnPoke_spdefense(pokemon_2_stats)
spattack_2 = FnPoke_spattack(pokemon_2_stats)
attack_2 = FnPoke_attack(pokemon_2_stats)
defense_2 = FnPoke_defense(pokemon_2_stats)
hp_2 = FnPoke_hp(pokemon_2_stats)
speed_2 = FnPoke_speed(pokemon_2_stats)


pokemon_2_stats = [hp_2,defense_2,attack_2,spdefense_2,spattack_2,speed_2]

for stat in pokemon_2_stats:
    print(stat)





