import random
import gameplay_functions


def battle_animation_player(player, player_battle_sprite, barrier_active, sharp_sense_active, graphics):

    if player.race == "amuna":
        if player.gender == "male":
            try:
                if player.equipment["armor"].name == "basic armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_basic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_basic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_basic_barrier_sense"])

                if player.equipment["armor"].name == "forged armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_forged_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_forged_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_forged_barrier_sense"])

                if player.equipment["armor"].name == "mythical armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_mythic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_mythic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_mythic_barrier_sense"])

                if player.equipment["armor"].name == "legendary armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_battle_legend_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_battle_legend_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_battle_legend_barrier_sense"])
            except AttributeError:
                if player.role == "mage":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_mage_amuna_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_battle_barrier_sense"])
                if player.role == "fighter":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_amuna_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_battle_barrier_sense"])
                if player.role == "scout":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_scout_amuna_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_battle_barrier_sense"])
                if player.role == "":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_no_role_amuna_battle"])
        if player.gender == "female":
            try:
                if player.equipment["armor"].name == "basic armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_female_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_battle_basic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female"
                                                                 "_battle_basic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_female_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female"
                                                                 "_battle_basic_barrier_sense"])

                if player.equipment["armor"].name == "forged armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_female_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female"
                                                                 "_battle_forged_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female"
                                                                 "_battle_forged_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_female_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female"
                                                                 "_battle_forged_barrier_sense"])

                if player.equipment["armor"].name == "mythical armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_female_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female"
                                                                 "_battle_mythic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female"
                                                                 "_battle_mythic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_female_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female"
                                                                 "_battle_mythic_barrier_sense"])

                if player.equipment["armor"].name == "legendary armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_female_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female"
                                                                 "_battle_legend_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female"
                                                                 "_battle_legend_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_female_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female"
                                                                 "_battle_legend_barrier_sense"])
            except AttributeError:
                if player.role == "mage":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_mage_amuna_female_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_female_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_female_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_female_battle_barrier_sense"])
                if player.role == "fighter":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_amuna_female_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_battle_barrier_sense"])
                if player.role == "scout":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_scout_amuna_female_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_female_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_female_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_female_battle_barrier_sense"])
                if player.role == "":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_no_role_amuna_female_battle"])
    if player.race == "sorae":
        if player.gender == "male":
            try:
                if player.equipment["armor"].name == "basic armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_basic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_basic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_basic_barrier_sense"])

                if player.equipment["armor"].name == "forged armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_forged_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_forged_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_forged_barrier_sense"])

                if player.equipment["armor"].name == "mythical armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_mythic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_mythic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_mythic_barrier_sense"])

                if player.equipment["armor"].name == "legendary armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_battle_legend_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_battle_legend_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_battle_legend_barrier_sense"])
            except AttributeError:
                if player.role == "mage":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_mage_sorae_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_battle_barrier_sense"])
                if player.role == "fighter":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_sorae_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_battle_barrier_sense"])
                if player.role == "scout":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_scout_sorae_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_battle_barrier_sense"])
                if player.role == "":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_no_role_sorae_battle"])
        if player.gender == "female":
            try:
                if player.equipment["armor"].name == "basic armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_b_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_basic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_basic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_b_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_basic_barrier_sense"])

                if player.equipment["armor"].name == "forged armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_b_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_forged_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_forged_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_b_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_forged_barrier_sense"])

                if player.equipment["armor"].name == "mythical armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_b_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_mythic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_mythic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_b_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_mythic_barrier_sense"])

                if player.equipment["armor"].name == "legendary armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_b_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_battle_legend_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_battle_legend_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_b_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_battle_legend_barrier_sense"])
            except AttributeError:
                if player.role == "mage":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_mage_sorae_b_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_b_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_b_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_b_battle_barrier_sense"])
                if player.role == "fighter":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_sorae_b_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_battle_barrier_sense"])
                if player.role == "scout":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_scout_sorae_b_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_b_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_b_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_b_battle_barrier_sense"])
                if player.role == "":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_no_role_sorae_b_battle"])
    if player.race == "nuldar":
        if player.gender == "male":
            try:
                if player.equipment["armor"].name == "basic armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_basic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_basic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_basic_barrier_sense"])

                if player.equipment["armor"].name == "forged armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_forged_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_forged_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_forged_barrier_sense"])

                if player.equipment["armor"].name == "mythical armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_mythic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_mythic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_mythic_barrier_sense"])

                if player.equipment["armor"].name == "legendary armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_battle_legend_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_battle_legend_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_battle_legend_barrier_sense"])
            except AttributeError:
                if player.role == "mage":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_mage_nuldar_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_battle_barrier_sense"])
                if player.role == "fighter":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_nuldar_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_battle_barrier_sense"])
                if player.role == "scout":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_scout_nuldar_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_battle_barrier_sense"])
                if player.role == "":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_no_role_nuldar_battle"])
        if player.gender == "female":
            try:
                if player.equipment["armor"].name == "basic armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_female_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female"
                                                                 "_battle_basic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female"
                                                                 "_battle_basic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_female_battle_basic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_battle_basic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_battle_basic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female"
                                                                 "_battle_basic_barrier_sense"])

                if player.equipment["armor"].name == "forged armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_female_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female"
                                                                 "_battle_forged_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female"
                                                                 "_battle_forged_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_female_battle_forged"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_battle_forged_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_battle_forged_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female"
                                                                 "_battle_forged_barrier_sense"])

                if player.equipment["armor"].name == "mythical armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_female_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female"
                                                                 "_battle_mythic_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female"
                                                                 "_battle_mythic_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_female_battle_mythic"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_battle_mythic_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_battle_mythic_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female"
                                                                 "_battle_mythic_barrier_sense"])

                if player.equipment["armor"].name == "legendary armor":
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_female_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female"
                                                                 "_battle_legend_barrier_sense"])
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female"
                                                                 "_battle_legend_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_female_battle_legend"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_battle_legend_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_battle_legend_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female"
                                                                 "_battle_legend_barrier_sense"])
            except AttributeError:
                if player.role == "mage":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_mage_nuldar_female_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_female_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_female_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_female_battle_barrier_sense"])
                if player.role == "fighter":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_nuldar_female_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_battle_barrier_sense"])
                if player.role == "scout":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_scout_nuldar_female_battle"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_female_battle_barrier"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_female_battle_sense"])
                    if barrier_active and sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_female_battle_barrier_sense"])
                if player.role == "":
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_no_role_nuldar_female_battle"])


def battle_animation_enemy(enemy, snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                           muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                           in_battle, in_npc_interaction, graphics, necrola_battle_sprite, osodark_battle_sprite,
                           stelli_battle_sprite, chorizon_phase, erebyth_battle_sprite, erebyth_counter,
                           atmon_battle_sprite, jumano_battle_sprite, dreth_battle_sprite, apothis_gift):

    if in_battle and not in_npc_interaction:
        if enemy.kind == "snake":
            snake_battle_sprite.update(715, 250, graphics["snake_battle"])
        if enemy.name == "Ghoul":
            ghoul_battle_sprite.update(698, 280, graphics["ghoul_battle"])
        if enemy.name == "Chorizon":
            if chorizon_phase:
                chorizon_battle_sprite.update(720, 325, graphics["chorizon_phase"])
            else:
                chorizon_battle_sprite.update(720, 325, graphics["chorizon_battle"])
        if enemy.kind == "muchador":
            muchador_battle_sprite.update(705, 290, graphics["muchador_battle"])
        if enemy.kind == "magmon":
            magmon_battle_sprite.update(705, 286, graphics["magmon_battle"])
        if enemy.kind == "bandile":
            bandile_battle_sprite.update(695, 300, graphics["bandile_battle"])
        if enemy.kind == "chinzilla":
            chinzilla_battle_sprite.update(700, 300, graphics["chinzilla_battle"])
        if enemy.kind == "necrola":
            necrola_battle_sprite.update(705, 300, graphics["necrola_battle"])
        if enemy.kind == "osodark":
            osodark_battle_sprite.update(705, 300, graphics["osodark_battle"])
        if enemy.name == "Stellia":
            stelli_battle_sprite.update(stelli_battle_sprite.x_coordinate,
                                        stelli_battle_sprite.y_coordinate,
                                        graphics["stelli_battle_a"])
        if enemy.name == "Stellib":
            stelli_battle_sprite.update(stelli_battle_sprite.x_coordinate,
                                        stelli_battle_sprite.y_coordinate,
                                        graphics["stelli_battle_b"])
        if enemy.name == "Stellic":
            stelli_battle_sprite.update(stelli_battle_sprite.x_coordinate,
                                        stelli_battle_sprite.y_coordinate,
                                        graphics["stelli_battle_c"])
        if enemy.kind == "erebyth":
            erebyth_battle_sprite.update(695, 350, graphics["erebyth_battle"])
            if erebyth_counter == 2:
                erebyth_battle_sprite.update(695, 350, graphics["erebyth_phase_attack"])
        if enemy.kind == "atmon":
            atmon_battle_sprite.update(705, 300, graphics["atmon_battle"])
        if enemy.kind == "jumano":
            jumano_battle_sprite.update(705, 300, graphics["jumano_battle"])
        if enemy.kind == "dreth":
            if apothis_gift:
                dreth_battle_sprite.update(707, 345, graphics["dreth_battle_2"])
            else:
                dreth_battle_sprite.update(707, 345, graphics["dreth_battle"])


# update player character and enemy sprites for combat animation
def attack_animation_player(player, player_battle_sprite, barrier_active, sharp_sense_active, hard_strike, graphics,
                            turn_taken):

    # update player character sprite for combat animation
    if not turn_taken:
        if player.race == "amuna":
            if player.gender == "male":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_basic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_attack_basic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_attack_basic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_attack_basic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_"
                                                                         "attack_basic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_basic_barrier_sense"])

                    if player.equipment["armor"].name == "forged armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_forged_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_attack_forged"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_attack_forged_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_attack_forged_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_"
                                                                         "attack_forged_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_forged_barrier_sense"])

                    if player.equipment["armor"].name == "mythical armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_mythic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_attack_mythic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_attack_mythic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_attack_mythic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_"
                                                                         "attack_mythic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_mythic_barrier_sense"])

                    if player.equipment["armor"].name == "legendary armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_attack_legend_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_attack_legend"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_attack_legend_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_attack_legend_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_"
                                                                         "attack_legend_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_attack_legend_barrier_sense"])
                except AttributeError:
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_attack_barrier_sense"])
                    if player.role == "fighter":
                        if not hard_strike:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_attack"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_attack_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_attack_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_attack_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_attack_barrier_sense"])
                    if player.role == "":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_no_role_amuna_attack"])
            if player.gender == "female":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female"
                                                                     "_attack_basic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_female_attack_basic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_female"
                                                                         "_attack_basic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_female"
                                                                         "_attack_basic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_female"
                                                                         "_attack_basic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female"
                                                                     "_attack_basic_barrier_sense"])

                    if player.equipment["armor"].name == "forged armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female"
                                                                     "_attack_forged_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_female_attack_forged"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_female"
                                                                         "_attack_forged_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_"
                                                                         "female_attack_forged_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_female_"
                                                                         "attack_forged_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female"
                                                                     "_attack_forged_barrier_sense"])

                    if player.equipment["armor"].name == "mythical armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female"
                                                                     "_attack_mythic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_female_attack_mythic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_female"
                                                                         "_attack_mythic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_female"
                                                                         "_attack_mythic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_female_"
                                                                         "attack_mythic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female"
                                                                     "_attack_mythic_barrier_sense"])

                    if player.equipment["armor"].name == "legendary armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_amuna_female"
                                                                     "_attack_legend_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_female_attack_legend"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_female"
                                                                         "_attack_legend_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_female"
                                                                         "_attack_legend_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_amuna_female_"
                                                                         "attack_legend_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_amuna_female"
                                                                     "_attack_legend_barrier_sense"])
                except AttributeError:
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_amuna_female_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_amuna_female_attack_barrier_sense"])
                    if player.role == "fighter":
                        if not hard_strike:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_attack"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_female_attack_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_female_attack_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_amuna_female"
                                                                     "_attack_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_amuna_female_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_amuna_female_attack_barrier_sense"])
                    if player.role == "":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_no_role_amuna_female_attack"])
        if player.race == "sorae":
            if player.gender == "male":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_basic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_attack_basic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_attack_basic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_attack_basic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_"
                                                                         "attack_basic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_basic_barrier_sense"])

                    if player.equipment["armor"].name == "forged armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_forged_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_attack_forged"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_attack_forged_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_attack_forged_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_"
                                                                         "attack_forged_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_forged_barrier_sense"])

                    if player.equipment["armor"].name == "mythical armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_mythic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_attack_mythic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_attack_mythic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_attack_mythic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_"
                                                                         "attack_mythic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_mythic_barrier_sense"])

                    if player.equipment["armor"].name == "legendary armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_attack_legend_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_attack_legend"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_attack_legend_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_attack_legend_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_"
                                                                         "attack_legend_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_attack_legend_barrier_sense"])
                except AttributeError:
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_attack_barrier_sense"])
                    if player.role == "fighter":
                        if not hard_strike:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_attack"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_attack_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_attack_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_attack_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_attack_barrier_sense"])
                    if player.role == "":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_no_role_sorae_attack"])
            if player.gender == "female":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_basic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_b_attack_basic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b_attack_basic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b_attack_basic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b_"
                                                                         "attack_basic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b_attack_basic_barrier_sense"])

                    if player.equipment["armor"].name == "forged armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_forged_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_b_attack_forged"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b_"
                                                                         "attack_forged_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b_attack_forged_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b_"
                                                                         "attack_forged_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b"
                                                                     "_attack_forged_barrier_sense"])

                    if player.equipment["armor"].name == "mythical armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_mythic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_b_attack_mythic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b"
                                                                         "_attack_mythic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b_attack_mythic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b_"
                                                                         "attack_mythic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b"
                                                                     "_attack_mythic_barrier_sense"])

                    if player.equipment["armor"].name == "legendary armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_sorae_b_attack_legend_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_b_attack_legend"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b"
                                                                         "_attack_legend_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b_attack_legend_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_sorae_b_"
                                                                         "attack_legend_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_sorae_b"
                                                                     "_attack_legend_barrier_sense"])
                except AttributeError:
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_sorae_b_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_sorae_b_attack_barrier_sense"])
                    if player.role == "fighter":
                        if not hard_strike:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_attack"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_b_attack_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_b_attack_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_sorae_b_attack_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_sorae_b_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_sorae_b_attack_barrier_sense"])
                    if player.role == "":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_no_role_sorae_b_attack"])
        if player.race == "nuldar":
            if player.gender == "male":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_basic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_attack_basic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_attack_basic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_attack_basic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_"
                                                                         "attack_basic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_basic_barrier_sense"])

                    if player.equipment["armor"].name == "forged armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_forged_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_attack_forged"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_attack_forged_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_attack_forged_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_"
                                                                         "attack_forged_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_forged_barrier_sense"])

                    if player.equipment["armor"].name == "mythical armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_mythic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_attack_mythic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_attack_mythic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_attack_mythic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_"
                                                                         "attack_mythic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_mythic_barrier_sense"])

                    if player.equipment["armor"].name == "legendary armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_attack_legend_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_attack_legend"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_attack_legend_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_attack_legend_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_"
                                                                         "attack_legend_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_attack_legend_barrier_sense"])
                except AttributeError:
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_attack_barrier_sense"])
                    if player.role == "fighter":
                        if not hard_strike:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_attack"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_attack_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_attack_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_attack_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_attack_barrier_sense"])
                    if player.role == "":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_no_role_nuldar_attack"])
            if player.gender == "female":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female"
                                                                     "_attack_basic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_female_attack_basic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female"
                                                                         "_attack_basic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female"
                                                                         "_attack_basic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female_"
                                                                         "attack_basic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_attack_basic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female_attack_basic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female_attack_basic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female"
                                                                     "_attack_basic_barrier_sense"])

                    if player.equipment["armor"].name == "forged armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female"
                                                                     "_attack_forged_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_female_attack_forged"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female"
                                                                         "_attack_forged_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female"
                                                                         "_attack_forged_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female_"
                                                                         "attack_forged_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_attack_forged"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female"
                                                                     "_attack_forged_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female_attack_forged_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female"
                                                                     "_attack_forged_barrier_sense"])

                    if player.equipment["armor"].name == "mythical armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female"
                                                                     "_attack_mythic_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_female_attack_mythic"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female"
                                                                         "_attack_mythic_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female"
                                                                         "_attack_mythic_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female_"
                                                                         "attack_mythic_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_attack_mythic"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female"
                                                                     "_attack_mythic_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female_attack_mythic_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female"
                                                                     "_attack_mythic_barrier_sense"])

                    if player.equipment["armor"].name == "legendary armor":
                        if player.role == "mage":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_mage_nuldar_female"
                                                                     "_attack_legend_barrier_sense"])
                        if player.role == "fighter":
                            if not hard_strike:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_female_attack_legend"])
                                if barrier_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female"
                                                                         "_attack_legend_barrier"])
                                if sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female"
                                                                         "_attack_legend_sense"])
                                if barrier_active and sharp_sense_active:
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                graphics["player_fighter_nuldar_female_"
                                                                         "attack_legend_barrier_sense"])
                        if player.role == "scout":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_attack_legend"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female"
                                                                     "_attack_legend_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female_attack_legend_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_scout_nuldar_female"
                                                                     "_attack_legend_barrier_sense"])
                except AttributeError:
                    if player.role == "mage":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_mage_nuldar_female_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_mage_nuldar_female_attack_barrier_sense"])
                    if player.role == "fighter":
                        if not hard_strike:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_attack"])
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_female_attack_barrier"])
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_female_attack_sense"])
                            if barrier_active and sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            graphics["player_fighter_nuldar_female"
                                                                     "_attack_barrier_sense"])
                    if player.role == "scout":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_scout_nuldar_female_attack"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_attack_barrier"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_attack_sense"])
                        if barrier_active and sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_scout_nuldar_female_attack_barrier_sense"])
                    if player.role == "":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_no_role_nuldar_female_attack"])


def fighter(graphics, player, player_battle_sprite, sharp_sense_active, barrier_active):

    # update animations for hard strike attack
    if player.race == "amuna":
        if player.gender == "male":
            if player.role == "fighter":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_strike_basic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_basic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_basic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_basic_barrier_sense"])
                    if player.equipment["armor"].name == "forged armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_strike_forged"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_forged_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_forged_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_forged_barrier_sense"])
                    if player.equipment["armor"].name == "mythical armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_strike_mythic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_mythic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_mythic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_mythic_barrier_sense"])
                    if player.equipment["armor"].name == "legendary armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_strike_legend"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_legend_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_legend_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_strike_legend_barrier_sense"])
                except AttributeError:
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_amuna_strike"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_strike_sense"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_strike_barrier"])
                    if sharp_sense_active and barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_strike_barrier_sense"])
        if player.gender == "female":
            if player.role == "fighter":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_strike_basic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_strike_basic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_strike_basic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_"
                                                                 "strike_basic_barrier_sense"])
                    if player.equipment["armor"].name == "forged armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_strike_forged"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_strike_forged_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_strike_forged_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_"
                                                                 "female_strike_forged_barrier_sense"])
                    if player.equipment["armor"].name == "mythical armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_strike_mythic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_strike_mythic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_strike_mythic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female"
                                                                 "_strike_mythic_barrier_sense"])
                    if player.equipment["armor"].name == "legendary armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_strike_legend"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_strike_legend_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female_strike_legend_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_amuna_female"
                                                                 "_strike_legend_barrier_sense"])
                except AttributeError:
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_amuna_female_strike"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_strike_sense"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_strike_barrier"])
                    if sharp_sense_active and barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_amuna_female_strike_barrier_sense"])
    if player.race == "sorae":
        if player.gender == "male":
            if player.role == "fighter":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_strike_basic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_basic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_basic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_basic_barrier_sense"])
                    if player.equipment["armor"].name == "forged armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_strike_forged"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_forged_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_forged_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_forged_barrier_sense"])
                    if player.equipment["armor"].name == "mythical armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_strike_mythic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_mythic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_mythic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_mythic_barrier_sense"])
                    if player.equipment["armor"].name == "legendary armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_strike_legend"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_legend_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_legend_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_strike_legend_barrier_sense"])

                except AttributeError:
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_sorae_strike"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_strike_sense"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_strike_barrier"])
                    if sharp_sense_active and barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_strike_barrier_sense"])
        if player.gender == "female":
            if player.role == "fighter":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_strike_basic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_basic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_basic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_basic_barrier_sense"])
                    if player.equipment["armor"].name == "forged armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_strike_forged"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_forged_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_forged_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_forged_barrier_sense"])
                    if player.equipment["armor"].name == "mythical armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_strike_mythic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_mythic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_mythic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_mythic_barrier_sense"])
                    if player.equipment["armor"].name == "legendary armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_strike_legend"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_legend_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_legend_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_sorae_b_strike_legend_barrier_sense"])

                except AttributeError:
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_sorae_b_strike"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_strike_sense"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_strike_barrier"])
                    if sharp_sense_active and barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_sorae_b_strike_barrier_sense"])
    if player.race == "nuldar":
        if player.gender == "male":
            if player.role == "fighter":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_strike_basic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_basic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_basic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_basic_barrier_sense"])
                    if player.equipment["armor"].name == "forged armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_strike_forged"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_forged_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_forged_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_forged_barrier_sense"])
                    if player.equipment["armor"].name == "mythical armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_strike_mythic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_mythic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_mythic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_mythic_barrier_sense"])
                    if player.equipment["armor"].name == "legendary armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_strike_legend"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_legend_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_legend_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_strike_legend_barrier_sense"])

                except AttributeError:
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_nuldar_strike"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_strike_sense"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_strike_barrier"])
                    if sharp_sense_active and barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_strike_barrier_sense"])

        if player.gender == "female":
            if player.role == "fighter":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_strike_basic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_strike_basic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_strike_basic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female"
                                                                 "_strike_basic_barrier_sense"])
                    if player.equipment["armor"].name == "forged armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_strike_forged"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_strike_forged_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_strike_forged_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female"
                                                                 "_strike_forged_barrier_sense"])
                    if player.equipment["armor"].name == "mythical armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_strike_mythic"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_strike_mythic_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_strike_mythic_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female"
                                                                 "_strike_mythic_barrier_sense"])
                    if player.equipment["armor"].name == "legendary armor":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_strike_legend"])
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_strike_legend_sense"])
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female_strike_legend_barrier"])
                        if sharp_sense_active and barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        graphics["player_fighter_nuldar_female"
                                                                 "_strike_legend_barrier_sense"])

                except AttributeError:
                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                player_battle_sprite.y_coordinate,
                                                graphics["player_fighter_nuldar_female_strike"])
                    if sharp_sense_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_strike_sense"])
                    if barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_strike_barrier"])
                    if sharp_sense_active and barrier_active:
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    graphics["player_fighter_nuldar_female_strike_barrier_sense"])


def attack_animation_enemy(enemy, snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                           muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                           graphics, necrola_battle_sprite, osodark_battle_sprite, stelli_battle_sprite,
                           chorizon_phase, damage, erebyth_battle_sprite, erebyth_counter, atmon_battle_sprite,
                           jumano_battle_sprite, dreth_battle_sprite, dreth_counter, apothis_gift):

    if damage > 0:
        if enemy.kind == "snake":
            snake_battle_sprite.update(715, 250, graphics["snake_attack"])
        if enemy.name == "Ghoul":
            ghoul_battle_sprite.update(698, 280, graphics["ghoul_attack"])
        if enemy.name == "Chorizon":
            if chorizon_phase:
                chorizon_battle_sprite.update(720, 325, graphics["chorizon_phase_attack"])
            else:
                chorizon_battle_sprite.update(720, 325, graphics["chorizon_attack"])
        if enemy.kind == "muchador":
            muchador_battle_sprite.update(705, 290, graphics["muchador_attack"])
        if enemy.kind == "magmon":
            magmon_battle_sprite.update(705, 286, graphics["magmon_attack"])
        if enemy.kind == "bandile":
            bandile_battle_sprite.update(695, 300, graphics["bandile_attack"])
        if enemy.kind == "chinzilla":
            chinzilla_battle_sprite.update(700, 300, graphics["chinzilla_attack"])
        if enemy.kind == "necrola":
            necrola_battle_sprite.update(705, 300, graphics["necrola_attack"])
        if enemy.kind == "osodark":
            osodark_battle_sprite.update(705, 300, graphics["osodark_attack"])
        if enemy.kind == "stelli":
            if enemy.name == "Stellia":
                stelli_battle_sprite.update(stelli_battle_sprite.x_coordinate,
                                            stelli_battle_sprite.y_coordinate,
                                            graphics["stelli_attack_a"])
            if enemy.name == "Stellib":
                stelli_battle_sprite.update(stelli_battle_sprite.x_coordinate,
                                            stelli_battle_sprite.y_coordinate,
                                            graphics["stelli_attack_b"])
            if enemy.name == "Stellic":
                stelli_battle_sprite.update(stelli_battle_sprite.x_coordinate,
                                            stelli_battle_sprite.y_coordinate,
                                            graphics["stelli_attack_c"])
        if enemy.kind == "erebyth":
            if erebyth_counter == 2:
                erebyth_battle_sprite.update(695, 350, graphics["erebyth_phase_attack"])
            elif erebyth_counter == 3:
                erebyth_battle_sprite.update(695, 350, graphics["erebyth_big_attack"])
            else:
                erebyth_battle_sprite.update(695, 350, graphics["erebyth_attack"])
        if enemy.kind == "atmon":
            atmon_battle_sprite.update(705, 300, graphics["atmon_attack"])
        if enemy.kind == "jumano":
            jumano_battle_sprite.update(705, 300, graphics["jumano_attack"])
        if enemy.kind == "dreth":
            if apothis_gift:
                if dreth_counter % 4 == 0:
                    dreth_battle_sprite.update(707, 345, graphics["dreth_shatter_2"])
                else:
                    dreth_battle_sprite.update(707, 345, graphics["dreth_attack_2"])
            else:
                if dreth_counter % 4 == 0:
                    dreth_battle_sprite.update(707, 345, graphics["dreth_shatter"])
                else:
                    dreth_battle_sprite.update(707, 345, graphics["dreth_attack"])


def enemy_health_bar(enemys, graphics):
    try:
        enemys.health_bar.update(enemys.health_bar.x_coordinate, enemys.health_bar.y_coordinate,
                                 gameplay_functions.health_bar_update(enemys, graphics))
    except AttributeError:
        pass


def attack_scenario(enemy_combating, combat_event, player, hard_strike_learned, level_up_win, level_up_font, graphics,
                    sharp_sense_active, barrier_active, turn_taken, stun_them, mirror_image, erebyth_counter,
                    atmon_counter, prism_received, dreth_counter, apothis_gift, trading_deck,
                    trading_task_complete, any_card_counter, card_deck, arrow_active):

    # get the all the stuff that happened in this scenario and return it to main loop via dictionary keys and values
    combat_event_dictionary = {"damage done string": 0, "damage taken string": 0, "damage done": 0, "damage taken": 0,
                               "item dropped": "", "experience gained": 0, "quest update": "", "enemy defeated": False,
                               "leveled": False, "effective player": False, "non effective player": False,
                               "effective enemy": False, "non effective enemy": False, "basic_snake": False,
                               "basic_ghoul": False, "basic_bandile": False, "basic_magmon": False,
                               "better_necrola": False, "better_osodark": False, "better_atmon": False,
                               "better_jumano": False}

    if combat_event == "attack":
        if enemy_combating.alive_status:
            if not turn_taken:

                # returns players damage to the enemy based on level and equipment
                attack_dict = gameplay_functions.attack_enemy(player, enemy_combating, sharp_sense_active, arrow_active)
                combat_event_dictionary["effective player"] = attack_dict["effective"]
                combat_event_dictionary["non effective player"] = attack_dict["non effective"]
                combat_event_dictionary["effective pet"] = attack_dict["pet effective"]
                combat_event_dictionary["non effective pet"] = attack_dict["pet non effective"]
                combat_event_dictionary["critical dealt"] = attack_dict["critical"]
                combat_event_dictionary["pet damage"] = attack_dict["pet damage"]
                combat_event_dictionary["player damage"] = attack_dict["damage"]
                damage_to_enemy = attack_dict["damage"] + attack_dict["pet damage"]

                if mirror_image:
                    if attack_dict["effective"]:
                        combat_event_dictionary["mirror damage"] = 5
                        damage_to_enemy += 5
                    elif attack_dict["non effective"]:
                        combat_event_dictionary["mirror damage"] = 1
                        damage_to_enemy += 1
                    else:
                        combat_event_dictionary["mirror damage"] = 3
                        damage_to_enemy += 3

                enemy_combating.health = enemy_combating.health - damage_to_enemy
                enemy_health_bar(enemy_combating, graphics)

            # if enemy is not dead yet
            if enemy_combating.health > 0:
                if not turn_taken:
                    attacked_enemy_string = f" You did {damage_to_enemy} damage to {enemy_combating.kind}."
                    combat_event_dictionary["damage done"] = damage_to_enemy
                    # add damage to enemy to event dictionary to be returned to main loop
                    combat_event_dictionary["damage done string"] = attacked_enemy_string

                # returns total damage output from enemy as attacked_player_health value
                if not stun_them:
                    defend_dict = gameplay_functions.attack_player(player, enemy_combating, barrier_active,
                                                                   arrow_active)
                    combat_event_dictionary["effective enemy"] = defend_dict["effective"]
                    combat_event_dictionary["non effective enemy"] = defend_dict["non effective"]
                    combat_event_dictionary["critical received"] = defend_dict["critical"]
                    damage_to_player = defend_dict["damage"]

                    if enemy_combating.name == "Erebyth":
                        if erebyth_counter == 3:
                            damage_to_player = 25
                            combat_event_dictionary["effective enemy"] = "effective"
                    if enemy_combating.name == "Dreth":
                        if enemy_combating.health < 35:
                            if not apothis_gift:
                                damage_to_player = 100
                                combat_event_dictionary["effective enemy"] = "effective"
                        elif dreth_counter % 4 == 0:
                            damage_to_player = 15
                            combat_event_dictionary["effective enemy"] = "effective"

                    if damage_to_player > 0:
                        attacked_player_string = f"You take {damage_to_player} damage from {enemy_combating.kind}."
                        player.health = player.health - damage_to_player
                        combat_event_dictionary["damage taken"] = damage_to_player
                        # add damage done to player from enemy to dictionary
                        combat_event_dictionary["damage taken string"] = attacked_player_string

                        # player health is less than or equal to 0, player is dead
                        if player.health <= 0:
                            player.alive_status = False
                        return combat_event_dictionary
                    else:
                        enemy_miss_string = f'{enemy_combating.kind} missed.'
                        # add to dictionary that enemy did no damage to player
                        combat_event_dictionary["damage taken string"] = enemy_miss_string
                        return combat_event_dictionary
                else:
                    stun_them = False
                    enemy_stun_string = f'{enemy_combating.kind} is stunned.'
                    # add to dictionary that enemy did no damage to player
                    combat_event_dictionary["damage taken string"] = enemy_stun_string
                    combat_event_dictionary["stunned"] = stun_them
                    return combat_event_dictionary

            # enemy has been defeated, will return an amount of xp based on current levels
            else:
                # if player is on quest to kill snakes
                if enemy_combating.kind == "snake":
                    if player.quest_status["sneaky snakes"]:
                        if player.quest_progress["sneaky snakes"] < 4:
                            player.quest_progress["sneaky snakes"] = player.quest_progress["sneaky snakes"] + 1
                            quest_string = f"{player.quest_progress['sneaky snakes']}/4 snakes"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill ghouls
                if enemy_combating.kind == "ghoul":
                    if player.quest_status["ghouled again"]:
                        if player.quest_progress["ghouled again"] < 4:
                            player.quest_progress["ghouled again"] = player.quest_progress["ghouled again"] + 1
                            quest_string = f"{player.quest_status['ghouled again']}/4 ghouls"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill magmons
                if enemy_combating.kind == "magmon":
                    if player.quest_status["elementary elementals"]:
                        if player.quest_progress["elementary elementals"] < 4:
                            player.quest_progress["elementary elementals"] = \
                                player.quest_progress["elementary elementals"] + 1
                            quest_string = f"{player.quest_status['elementary elementals']}/4 magmons"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill bandiles
                if enemy_combating.kind == "bandile":
                    if player.quest_status["band hammer"]:
                        if player.quest_progress["band hammer"] < 4:
                            player.quest_progress["band hammer"] = \
                                player.quest_progress["band hammer"] + 1
                            quest_string = f"{player.quest_status['band hammer']}/4 bandiles"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill bandiles
                if enemy_combating.kind == "chinzilla":
                    if player.quest_status["it's dangerous to go alone"]:
                        if player.quest_progress["it's dangerous to go alone"] < 1:
                            player.quest_progress["it's dangerous to go alone"] = \
                                player.quest_progress["it's dangerous to go alone"] + 1
                            quest_string = str(player.quest_progress["it's dangerous to go alone"]) + "/1 chinzilla"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill necrolas
                if enemy_combating.kind == "necrola":
                    if player.quest_status["shades of fear"]:
                        if player.quest_progress["shades of fear"] < 4:
                            player.quest_progress["shades of fear"] = \
                                player.quest_progress["shades of fear"] + 1
                            quest_string = f"{player.quest_status['shades of fear']}/4 necrolas"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # experienced gained by player from defeating enemy
                if player.level <= enemy_combating.level + 1:
                    experience = int((enemy_combating.level / player.level) * 30)

                    # stelli are for training knowledge and shouldn't give much if any XP
                    if enemy_combating.kind == "stelli":
                        experience = 1
                    # boss battle gives a full level
                    if enemy_combating.kind == "muchador" or enemy_combating.kind == "chinzilla" or \
                            enemy_combating.kind == "erebyth" or enemy_combating.kind == "dreth":
                        experience = 100

                    player.experience = player.experience + experience
                    enemy_experience = f"{experience}"
                    # add to dictionary experience given from defeating enemy
                    combat_event_dictionary["experience gained"] = enemy_experience
                # player gains less experience if they're 1 level higher or more than enemy
                if player.level > enemy_combating.level + 1:
                    experience = int((enemy_combating.level / player.level))

                    # stelli are for training knowledge and shouldn't give much if any XP
                    if enemy_combating.kind == "stelli":
                        experience = 1
                    # boss battle gives a full level
                    if enemy_combating.kind == "muchador" or enemy_combating.kind == "chinzilla" or \
                            enemy_combating.kind == "erebyth" or enemy_combating.kind == "dreth":
                        experience = 100

                    player.experience = player.experience + experience
                    enemy_experience = f"{experience}"
                    # add to dictionary experience given from defeating enemy
                    combat_event_dictionary["experience gained"] = enemy_experience

                try:
                    if enemy_combating.kind != "atmon":
                        drop_chance = random.randrange(1, 10)
                        # 80% chance (roughly?) to drop merchant item sellable by player for rupees at shops
                        if drop_chance > 2:
                            # if item dropped isn't just a placeholder string
                            if enemy_combating.items != "item":
                                # doesn't give item to player if their inventory is full
                                if len(player.items) < 16:
                                    player.items.append(enemy_combating.items)
                                    enemy_dropped_this = (f"{enemy_combating.name} dropped "
                                                          f"[{enemy_combating.items.name}].")
                                    # add to dictionary anything dropped from enemy upon their defeat
                                    combat_event_dictionary["item dropped"] = enemy_dropped_this
                                else:
                                    combat_event_dictionary["item dropped"] = "Item, but your inventory is full."
                        else:
                            combat_event_dictionary["item dropped"] = "No"
                    else:
                        # atmons chance to drop quest item increases as more are defeated
                        if not prism_received:
                            drop_chance = random.randrange(1, 10)
                            if atmon_counter == 1:
                                if drop_chance > 9:
                                    # if item dropped isn't just a placeholder string
                                    if enemy_combating.items != "item":
                                        # doesn't give item to player if their inventory is full
                                        if len(player.items) < 16:
                                            player.items.append(enemy_combating.items)
                                            enemy_dropped_this = (f"{enemy_combating.name} dropped "
                                                                  f"[{enemy_combating.items.name}].")
                                            # add to dictionary anything dropped from enemy upon their defeat
                                            combat_event_dictionary["item dropped"] = enemy_dropped_this
                                            prism_received = True
                                            combat_event_dictionary["prism_received"] = prism_received
                                        else:
                                            combat_event_dictionary["item dropped"] = ("Item, but your inventory "
                                                                                       "is full.")
                                else:
                                    combat_event_dictionary["item dropped"] = "No"
                            if atmon_counter == 2:
                                if drop_chance > 7:
                                    # if item dropped isn't just a placeholder string
                                    if enemy_combating.items != "item":
                                        # doesn't give item to player if their inventory is full
                                        if len(player.items) < 16:
                                            player.items.append(enemy_combating.items)
                                            enemy_dropped_this = (f"{enemy_combating.name} dropped "
                                                                  f"[{enemy_combating.items.name}].")
                                            # add to dictionary anything dropped from enemy upon their defeat
                                            combat_event_dictionary["item dropped"] = enemy_dropped_this
                                            prism_received = True
                                            combat_event_dictionary["prism_received"] = prism_received
                                        else:
                                            combat_event_dictionary["item dropped"] = ("Item, but your inventory "
                                                                                       "is full.")
                                else:
                                    combat_event_dictionary["item dropped"] = "No"
                            if atmon_counter == 3:
                                if drop_chance > 5:
                                    # if item dropped isn't just a placeholder string
                                    if enemy_combating.items != "item":
                                        # doesn't give item to player if their inventory is full
                                        if len(player.items) < 16:
                                            player.items.append(enemy_combating.items)
                                            enemy_dropped_this = (f"{enemy_combating.name} dropped "
                                                                  f"[{enemy_combating.items.name}].")
                                            # add to dictionary anything dropped from enemy upon their defeat
                                            combat_event_dictionary["item dropped"] = enemy_dropped_this
                                            prism_received = True
                                            combat_event_dictionary["prism_received"] = prism_received
                                        else:
                                            combat_event_dictionary["item dropped"] = ("Item, but your inventory "
                                                                                       "is full.")
                                else:
                                    combat_event_dictionary["item dropped"] = "No"
                            if atmon_counter == 4:
                                if drop_chance > 3:
                                    # if item dropped isn't just a placeholder string
                                    if enemy_combating.items != "item":
                                        # doesn't give item to player if their inventory is full
                                        if len(player.items) < 16:
                                            player.items.append(enemy_combating.items)
                                            enemy_dropped_this = (f"{enemy_combating.name} dropped "
                                                                  f"[{enemy_combating.items.name}].")
                                            # add to dictionary anything dropped from enemy upon their defeat
                                            combat_event_dictionary["item dropped"] = enemy_dropped_this
                                            prism_received = True
                                            combat_event_dictionary["prism_received"] = prism_received
                                        else:
                                            combat_event_dictionary["item dropped"] = ("Item, but your inventory "
                                                                                       "is full.")
                                else:
                                    combat_event_dictionary["item dropped"] = "No"
                            if atmon_counter > 4:
                                if drop_chance > 1:
                                    # if item dropped isn't just a placeholder string
                                    if enemy_combating.items != "item":
                                        # doesn't give item to player if their inventory is full
                                        if len(player.items) < 16:
                                            player.items.append(enemy_combating.items)
                                            enemy_dropped_this = (f"{enemy_combating.name} dropped "
                                                                  f"[{enemy_combating.items.name}].")
                                            # add to dictionary anything dropped from enemy upon their defeat
                                            combat_event_dictionary["item dropped"] = enemy_dropped_this
                                            prism_received = True
                                            combat_event_dictionary["prism_received"] = prism_received
                                        else:
                                            combat_event_dictionary["item dropped"] = ("Item, but your inventory "
                                                                                       "is full.")
                                else:
                                    combat_event_dictionary["item dropped"] = "No"
                        else:
                            combat_event_dictionary["item dropped"] = "No"
                except AttributeError:
                    combat_event_dictionary["item dropped"] = "No"

                # player will level up if experience greater than or equal to 100
                if player.experience >= 100:
                    gameplay_functions.level_up(player, level_up_win, level_up_font)
                    combat_event_dictionary["leveled"] = True

                if enemy_combating.kind != "stelli":
                    enemy_combating.alive_status = False
                    enemy_combating.kill()

                if enemy_combating.kind == "stelli":
                    enemy_combating.health = 100

                # if player has unlocked trading deck, add cards if they are dropped by mob type
                if trading_deck:
                    card_chance = random.randrange(1, 10)
                    if card_chance > 5:
                        # if player has initial task to collect 4 cards
                        if not trading_task_complete and any_card_counter < 4:
                            any_card_counter += 1
                            combat_event_dictionary["any_card_counter"] = any_card_counter
                        if enemy_combating.kind == "snake":
                            card_deck["basic_snake"] += 1
                            combat_event_dictionary["basic_snake"] = True
                        if enemy_combating.kind == "ghoul":
                            card_deck["basic_ghoul"] += 1
                            combat_event_dictionary["basic_ghoul"] = True
                        if enemy_combating.kind == "bandile":
                            card_deck["basic_bandile"] += 1
                            combat_event_dictionary["basic_bandile"] = True
                        if enemy_combating.kind == "magmon":
                            card_deck["basic_magmon"] += 1
                            combat_event_dictionary["basic_magmon"] = True
                        if enemy_combating.kind == "necrola":
                            card_deck["better_necrola"] += 1
                            combat_event_dictionary["better_necrola"] = True
                        if enemy_combating.kind == "osodark":
                            card_deck["better_osodark"] += 1
                            combat_event_dictionary["better_osodark"] = True
                        if enemy_combating.kind == "atmon":
                            card_deck["better_atmon"] += 1
                            combat_event_dictionary["better_atmon"] = True
                        if enemy_combating.kind == "jumano":
                            card_deck["better_jumano"] += 1
                            combat_event_dictionary["better_jumano"] = True

                # add to dictionary True if enemy has been defeated
                combat_event_dictionary["enemy defeated"] = True
                return combat_event_dictionary

    # active combat skill, if player is fighter and has learned hard strike from the academia
    # same as default attack from above, but attack replaced by hard strike skill
    if combat_event == "skill 1":
        if enemy_combating.alive_status:
            if not turn_taken:
                if player.role == "fighter":
                    if hard_strike_learned:
                        # returns players damage to the enemy based on level and equipment
                        if enemy_combating.name == "dreth":
                            if player.offense == 3:
                                striked = 1
                            if player.offense == 4:
                                striked = random.randrange(15, 18)
                        else:
                            striked = random.randrange(15, 18)  # hard strike damage
                        combat_event_dictionary["effective player"] = False
                        combat_event_dictionary["non effective player"] = False
                        combat_event_dictionary["critical dealt"] = False
                        combat_event_dictionary["effective pet"] = False
                        combat_event_dictionary["non effective pet"] = False
                        combat_event_dictionary["pet damage"] = 1
                        combat_event_dictionary["player damage"] = striked
                        damage_to_enemy = striked + 1
                        if mirror_image:
                            combat_event_dictionary["mirror damage"] = 3
                            damage_to_enemy += 3
                        enemy_combating.health = enemy_combating.health - damage_to_enemy
                        enemy_health_bar(enemy_combating, graphics)

                    # if enemy is not dead yet
                    if enemy_combating.health > 0:
                        if not turn_taken:
                            attacked_enemy_string = f" You did {striked} damage to {enemy_combating.kind}."
                            combat_event_dictionary["damage done"] = striked
                            # add damage to enemy to event dictionary to be returned to main loop
                            combat_event_dictionary["damage done string"] = attacked_enemy_string

                        # returns total damage output from enemy as attacked_player_health value
                        if not stun_them:
                            defend_dict = gameplay_functions.attack_player(player, enemy_combating,
                                                                           barrier_active, arrow_active)
                            combat_event_dictionary["effective enemy"] = defend_dict["effective"]
                            combat_event_dictionary["non effective enemy"] = defend_dict["non effective"]
                            combat_event_dictionary["critical received"] = defend_dict["critical"]
                            damage_to_player = defend_dict["damage"]
                            if enemy_combating.name == "erebyth":
                                if erebyth_counter == 3:
                                    damage_to_player = 25
                                    combat_event_dictionary["effective enemy"] = "effective"
                            if enemy_combating.name == "dreth":
                                if enemy_combating.health < 35:
                                    if not apothis_gift:
                                        damage_to_player = 100
                                        combat_event_dictionary["effective enemy"] = "effective"
                                elif dreth_counter % 4 == 0:
                                    damage_to_player = 15
                                    combat_event_dictionary["effective enemy"] = "effective"
                            if damage_to_player > 0:
                                attacked_player_string = f"You take {damage_to_player} damage from " \
                                                         f"{enemy_combating.kind}."
                                player.health = player.health - damage_to_player
                                combat_event_dictionary["damage taken"] = damage_to_player
                                # add damage done to player from enemy to dictionary
                                combat_event_dictionary["damage taken string"] = attacked_player_string

                                # player health is less than or equal to 0, player is dead
                                if player.health <= 0:
                                    player.alive_status = False
                                return combat_event_dictionary
                            else:
                                enemy_miss_string = f'{enemy_combating.kind} missed.'
                                # add to dictionary that enemy did no damage to player
                                combat_event_dictionary["damage taken string"] = enemy_miss_string
                                return combat_event_dictionary
                        else:
                            stun_them = False
                            enemy_stun_string = f'{enemy_combating.kind} is stunned.'
                            # add to dictionary that enemy did no damage to player
                            combat_event_dictionary["damage taken string"] = enemy_stun_string
                            combat_event_dictionary["stunned"] = stun_them
                            return combat_event_dictionary

                    # enemy has been defeated, will return an amount of xp based on current levels
                    else:
                        # if player is on quest to kill snakes
                        if enemy_combating.kind == "snake":
                            if player.quest_status["sneaky snakes"]:
                                if player.quest_progress["sneaky snakes"] < 4:
                                    player.quest_progress["sneaky snakes"] = player.quest_progress[
                                                                                 "sneaky snakes"] + 1
                                    quest_string = f"{player.quest_progress['sneaky snakes']}/4 snakes"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"

                        # if player is on quest to kill ghouls
                        if enemy_combating.kind == "ghoul":
                            if player.quest_status["ghouled again"]:
                                if player.quest_progress["ghouled again"] < 4:
                                    player.quest_progress["ghouled again"] = player.quest_progress[
                                                                                 "ghouled again"] + 1
                                    quest_string = f"{player.quest_status['ghouled again']}/4 ghouls"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"

                        # if player is on quest to kill magmons
                        if enemy_combating.kind == "magmon":
                            if player.quest_status["elementary elementals"]:
                                if player.quest_progress["elementary elementals"] < 4:
                                    player.quest_progress["elementary elementals"] = \
                                        player.quest_progress["elementary elementals"] + 1
                                    quest_string = f"{player.quest_status['elementary elementals']}/4 magmons"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"

                        # if player is on quest to kill bandiles
                        if enemy_combating.kind == "bandile":
                            if player.quest_status["band hammer"]:
                                if player.quest_progress["band hammer"] < 4:
                                    player.quest_progress["band hammer"] = \
                                        player.quest_progress["band hammer"] + 1
                                    quest_string = f"{player.quest_status['band hammer']}/4 bandiles"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"

                        # if player is on quest to kill bandiles
                        if enemy_combating.kind == "chinzilla":
                            if player.quest_status["it's dangerous to go alone"]:
                                if player.quest_progress["it's dangerous to go alone"] < 1:
                                    player.quest_progress["it's dangerous to go alone"] = \
                                        player.quest_progress["it's dangerous to go alone"] + 1
                                    quest_string = str(player.quest_progress[
                                                           "it's dangerous to go alone"]) + "/1 chinzilla"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"

                        # if player is on quest to kill necrolas
                        if enemy_combating.kind == "necrola":
                            if player.quest_status["shades of fear"]:
                                if player.quest_progress["shades of fear"] < 4:
                                    player.quest_progress["shades of fear"] = \
                                        player.quest_progress["shades of fear"] + 1
                                    quest_string = f"{player.quest_status['shades of fear']}/4 necrolas"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"

                        # experienced gained by player from defeating enemy
                        if player.level <= enemy_combating.level + 1:
                            experience = int((enemy_combating.level / player.level) * 30)
                            # stelli are for training knowledge and shouldn't give much if any XP
                            if enemy_combating.kind == "stelli":
                                experience = 1
                            # boss battle gives a full level
                            if enemy_combating.kind == "muchador" or enemy_combating.kind == "chinzilla" or \
                                    enemy_combating.kind == "erebyth" or enemy_combating.kind == "dreth":
                                experience = 100
                            player.experience = player.experience + experience
                            enemy_experience = f"{experience}"
                            # add to dictionary experience given from defeating enemy
                            combat_event_dictionary["experience gained"] = enemy_experience
                        # player gains less experience if they're 1 level higher or more than enemy
                        if player.level > enemy_combating.level + 1:
                            experience = int((enemy_combating.level / player.level))
                            # stelli are for training knowledge and shouldn't give much if any XP
                            if enemy_combating.kind == "stelli":
                                experience = 1
                            # boss battle gives a full level
                            if enemy_combating.kind == "muchador" or enemy_combating.kind == "chinzilla" or \
                                    enemy_combating.kind == "erebyth" or enemy_combating.kind == "dreth":
                                experience = 100
                            player.experience = player.experience + experience
                            enemy_experience = f"{experience}"
                            # add to dictionary experience given from defeating enemy
                            combat_event_dictionary["experience gained"] = enemy_experience
                        try:
                            drop_chance = random.randrange(1, 10)
                            # 80% chance (roughly?) to drop merchant item sellable by player for rupees at shops
                            if drop_chance > 2:
                                # if item dropped isn't just a placeholder string
                                if enemy_combating.items != "item":
                                    # doesn't give item to player if their inventory is full
                                    if len(player.items) < 16:
                                        player.items.append(enemy_combating.items)
                                        enemy_dropped_this = f"{enemy_combating.name} dropped [" \
                                                             f"{enemy_combating.items.name}]."
                                        # add to dictionary anything dropped from enemy upon their defeat
                                        combat_event_dictionary["item dropped"] = enemy_dropped_this
                                    else:
                                        combat_event_dictionary[
                                            "item dropped"] = "Item, but your inventory is full."
                            else:
                                combat_event_dictionary["item dropped"] = "No"
                        except AttributeError:
                            combat_event_dictionary["item dropped"] = "No"

                        # player will level up if experience greater than or equal to 100
                        if player.experience >= 100:
                            gameplay_functions.level_up(player, level_up_win, level_up_font)
                            combat_event_dictionary["leveled"] = True
                        if enemy_combating.kind != "stelli":
                            enemy_combating.alive_status = False
                            enemy_combating.kill()
                        if enemy_combating.kind == "stelli":
                            enemy_combating.health = 100

                        # if player has unlocked trading deck, add cards if they are dropped by mob type
                        if trading_deck:
                            card_chance = random.randrange(1, 10)
                            if card_chance > 5:
                                # if player has initial task to collect 4 cards
                                if not trading_task_complete and any_card_counter < 4:
                                    any_card_counter += 1
                                    combat_event_dictionary["any_card_counter"] = any_card_counter
                                if enemy_combating.kind == "snake":
                                    card_deck["basic_snake"] += 1
                                    combat_event_dictionary["basic_snake"] = True
                                if enemy_combating.kind == "ghoul":
                                    card_deck["basic_ghoul"] += 1
                                    combat_event_dictionary["basic_ghoul"] = True
                                if enemy_combating.kind == "bandile":
                                    card_deck["basic_bandile"] += 1
                                    combat_event_dictionary["basic_bandile"] = True
                                if enemy_combating.kind == "magmon":
                                    card_deck["basic_magmon"] += 1
                                    combat_event_dictionary["basic_magmon"] = True
                                if enemy_combating.kind == "necrola":
                                    card_deck["better_necrola"] += 1
                                    combat_event_dictionary["better_necrola"] = True
                                if enemy_combating.kind == "osodark":
                                    card_deck["better_osodark"] += 1
                                    combat_event_dictionary["better_osodark"] = True
                                if enemy_combating.kind == "atmon":
                                    card_deck["better_atmon"] += 1
                                    combat_event_dictionary["better_atmon"] = True
                                if enemy_combating.kind == "jumano":
                                    card_deck["better_jumano"] += 1
                                    combat_event_dictionary["better_jumano"] = True

                        # add to dictionary True if enemy has been defeated
                        combat_event_dictionary["enemy defeated"] = True
                        return combat_event_dictionary
