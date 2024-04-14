import random
import time

import drawing_functions
import combat_scenario
import gameplay_functions


def ectrenos_main(pygame, screen, graphic_dict, player, ectrenos_bg, eldream_building_music, over_world_song_set,
                  interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                  button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
                  info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle, movement_able,
                  current_enemy_battling, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite,
                  chorizon_battle_sprite, muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite,
                  chinzilla_battle_sprite, barrier_active, sharp_sense_active, current_npc_interacting,
                  equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select,
                  eldream_attuned, in_shop, in_inn, current_building_entering, enemy_tic, eldream_flowers,
                  interactables_ectrenos, ectrene, ladder, quest_star_leyre, pet_energy_window, chroma_bridge,
                  npc_leyre, necrola_battle_sprite, osodark_battle_sprite, sfx_ladder, stelli_battle_sprite, critter,
                  right_move, left_move, critter_tic, walk_move, mini_map, basic_fish_counter, better_fish_counter,
                  even_better_fish_counter, best_fish_counter, vanished, illisare, star_illisare, apothis_gift,
                  time_of_day, ectrenos_alcove_enemies, kasper_unlocked, torok_unlocked, iriana_unlocked,
                  kasper_battle_sprite, torok_battle_sprite, iriana_battle_sprite):
    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(eldream_building_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(ectrenos_bg, (0, 0))

    if time_of_day != 0 and time_of_day != 7:
        screen.blit(critter.surf, critter.rect)
        critter_toc = time.perf_counter()
        if critter_toc - critter_tic > 2:
            if right_move:
                if critter.x_coordinate < 680:
                    if walk_move and critter.x_coordinate % 9 == 0:
                        critter.update(critter.x_coordinate, critter.y_coordinate,
                                       graphic_dict["critter_side_right_walk"])
                        walk_move = False
                    else:
                        if critter.x_coordinate % 9 == 0:
                            critter.update(critter.x_coordinate, critter.y_coordinate,
                                           graphic_dict["critter_side_right"])
                            walk_move = True
                    critter.x_coordinate += 1
                else:
                    critter.update(critter.x_coordinate, critter.y_coordinate, graphic_dict["critter_front"])
                    right_move = False
                    left_move = True
                    critter.x_coordinate -= 1
                    critter_tic = time.perf_counter()
                critter.rect = critter.surf.get_rect(center=(critter.x_coordinate, critter.y_coordinate))

        if critter_toc - critter_tic > 2:
            if left_move:
                if critter.x_coordinate > 360:
                    if walk_move and critter.x_coordinate % 9 == 0:
                        critter.update(critter.x_coordinate, critter.y_coordinate,
                                       graphic_dict["critter_side_left_walk"])
                        walk_move = False
                    else:
                        if critter.x_coordinate % 9 == 0:
                            critter.update(critter.x_coordinate, critter.y_coordinate,
                                           graphic_dict["critter_side_left"])
                            walk_move = True
                    critter.x_coordinate -= 1
                else:
                    critter.update(critter.x_coordinate, critter.y_coordinate, graphic_dict["critter_front"])
                    right_move = True
                    left_move = False
                    critter.x_coordinate += 1
                    critter_tic = time.perf_counter()
                critter.rect = critter.surf.get_rect(center=(critter.x_coordinate, critter.y_coordinate))

    if not player.quest_status["las escondidas"] or player.quest_progress["las escondidas"] == 4:
        if not player.quest_complete["las escondidas"]:
            screen.blit(quest_star_leyre.surf, quest_star_leyre.rect)
    if not player.quest_status["las escondidas"] or player.quest_progress["las escondidas"] == 4:
        npc_leyre.update_position(682, 420)
        screen.blit(npc_leyre.surf, npc_leyre.rect)

    screen.blit(illisare.surf, illisare.rect)
    if not player.quest_complete["madness in marrow"]:
        screen.blit(star_illisare.surf, star_illisare.rect)
    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
    screen.blit(ectrene.surf, ectrene.rect)

    if pygame.Rect.colliderect(player.rect, ladder):
        interaction_popup.update(515, 452, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Alcove"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (515, 452)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to climb down ladder."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_ladder)
            interacted = False
            chroma_bridge.update(764, 487, graphic_dict["chroma_bridge"])
            player.current_zone = "ectrenos alcove"
            player.x_coordinate = 425
            player.y_coordinate = 675
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
            if time_of_day == 0 or time_of_day == 7:
                for osodark in ectrenos_alcove_enemies:
                    osodark.update_image(osodark.x_coordinate, osodark.y_coordinate,
                                         graphic_dict["osodark_night"])
            else:
                for osodark in ectrenos_alcove_enemies:
                    osodark.update_image(osodark.x_coordinate, osodark.y_coordinate,
                                         graphic_dict["osodark"])

    # if player collides with npc sprite and chooses to interact with it
    if not player.quest_status["las escondidas"] or player.quest_progress["las escondidas"] == 4:
        if pygame.sprite.collide_rect(player, npc_leyre):
            interaction_popup.update(npc_leyre.x_coordinate, npc_leyre.y_coordinate - 50,
                                     graphic_dict["popup_interaction_purple"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str(npc_leyre.name), True, "black", (203, 195, 227))
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (npc_leyre.x_coordinate, npc_leyre.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            info_text_1 = "Press 'F' key to talk to NPC."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world and not in_battle and not in_shop and not in_inn \
                    and not in_npc_interaction:
                current_npc_interacting = npc_leyre
                in_over_world = False
                in_npc_interaction = True
                movement_able = False
                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active, graphic_dict, kasper_unlocked,
                                                        torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                        torok_battle_sprite, iriana_battle_sprite)

    if pygame.sprite.collide_rect(player, illisare):
        interaction_popup.update(illisare.x_coordinate, illisare.y_coordinate - 50,
                                 graphic_dict["popup_interaction_purple"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(illisare.name), True, "black", (203, 195, 227))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (illisare.x_coordinate, illisare.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to talk to NPC."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world and not in_battle and not in_shop and not in_inn \
                and not in_npc_interaction:
            current_npc_interacting = illisare
            in_over_world = False
            in_npc_interaction = True
            movement_able = False
            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                    sharp_sense_active, graphic_dict, kasper_unlocked,
                                                    torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                    torok_battle_sprite, iriana_battle_sprite)

    # --------------------------------------------------------------------------------------------------
    screen.blit(mini_map.surf, mini_map.rect)

    if 380 < player.x_coordinate < 650 and player.y_coordinate > 700:
        player.current_zone = "eldream"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 540
        player.y_coordinate = 565
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if player.x_coordinate < 35 and 565 > player.y_coordinate > 470:
        player.current_zone = "ectrenos left"
        mini_map.update(915, 596, graphic_dict["ectrenos_mini_map_left"])
        chroma_bridge.update(477, 493, graphic_dict["chroma_bridge"])
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 850
        player.y_coordinate = 530
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if player.x_coordinate > 995 and 570 > player.y_coordinate > 470:
        player.current_zone = "ectrenos right"
        mini_map.update(915, 596, graphic_dict["ectrenos_mini_map_right"])
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 210
        player.y_coordinate = 515
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # npc movement updates
    face_direction = random.choice(["front", "back", "left", "right"])
    this_npc = random.choice(["illisare", "leyre"])
    if movement_able and in_over_world:
        npc_toc = time.perf_counter()
        if npc_toc - npc_tic > 5:
            npc_tic = time.perf_counter()
            if face_direction == "front":
                if this_npc == "leyre":
                    npc_leyre.update(graphic_dict["leyre_down"])
                if this_npc == "illisare":
                    illisare.update(graphic_dict["illisare_down"])
            if face_direction == "back":
                if this_npc == "leyre":
                    npc_leyre.update(graphic_dict["leyre_up"])
                if this_npc == "illisare":
                    illisare.update(graphic_dict["illisare_up"])
            if face_direction == "left":
                if this_npc == "leyre":
                    npc_leyre.update(graphic_dict["leyre_left"])
                if this_npc == "illisare":
                    illisare.update(graphic_dict["illisare_left"])
            if face_direction == "right":
                if this_npc == "leyre":
                    npc_leyre.update(graphic_dict["leyre_right"])
                if this_npc == "illisare":
                    illisare.update(graphic_dict["illisare_right"])

    ectrenos_main_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic, "info_text_1": info_text_1,
                            "info_text_2": info_text_2, "info_text_3": info_text_3, "info_text_4": info_text_4,
                            "interacted": interacted, "in_over_world": in_over_world, "in_battle": in_battle,
                            "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                            "current_enemy_battling": current_enemy_battling,
                            "current_npc_interacting": current_npc_interacting, "eldream_attuned": eldream_attuned,
                            "in_shop": in_shop, "in_inn": in_inn,
                            "current_building_entering": current_building_entering,
                            "enemy_tic": enemy_tic, "eldream_flowers": eldream_flowers,
                            "interactables_ectrenos": interactables_ectrenos, "right_move": right_move,
                            "left_move": left_move, "critter_tic": critter_tic, "walk_move": walk_move}

    return ectrenos_main_return


def ectrenos_left(pygame, screen, graphic_dict, player, ectrenos_left_bg, eldream_overworld_music, over_world_song_set,
                  interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                  button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
                  info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle, movement_able,
                  current_enemy_battling, current_npc_interacting, equipment_screen, staff, sword, bow, npc_garan,
                  offense_meter, defense_meter, weapon_select, eldream_attuned, in_shop, in_inn,
                  current_building_entering, enemy_tic, eldream_flowers, interactables_ectrenos, ectrenos_pet_entrance,
                  in_menagerie, quest_star_aitor, pet_energy_window, npc_leyre, sfx_find, critter, right_move,
                  left_move, critter_tic, walk_move, altar, mini_map, basic_fish_counter, better_fish_counter,
                  even_better_fish_counter, best_fish_counter, item_block, item_block_got, sfx_item_block, Item,
                  kasper_unlocked, torok_unlocked, iriana_unlocked, apothis_gift, dawn, early_morning, morning,
                  early_afternoon, afternoon, dusk, night, time_of_day, sfx_door, night_music):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            if time_of_day == 0 or time_of_day == 7:
                pygame.mixer.music.load(night_music)
            else:
                pygame.mixer.music.load(eldream_overworld_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(ectrenos_left_bg, (0, 0))

    if player.quest_progress["las escondidas"] == 0 and player.quest_status["las escondidas"]:
        npc_leyre.update_position(626, 355)
        screen.blit(npc_leyre.surf, npc_leyre.rect)

    if time_of_day != 0 and time_of_day != 7:
        if critter.x_coordinate < 590:
            screen.blit(critter.surf, critter.rect)
        critter_toc = time.perf_counter()
        if critter_toc - critter_tic > 2:
            if right_move:
                if critter.x_coordinate < 680:
                    if walk_move and critter.x_coordinate % 9 == 0:
                        critter.update(critter.x_coordinate, critter.y_coordinate,
                                       graphic_dict["critter_side_right_walk"])
                        walk_move = False
                    else:
                        if critter.x_coordinate % 9 == 0:
                            critter.update(critter.x_coordinate, critter.y_coordinate,
                                           graphic_dict["critter_side_right"])
                            walk_move = True
                    critter.x_coordinate += 1
                else:
                    critter.update(critter.x_coordinate, critter.y_coordinate, graphic_dict["critter_front"])
                    right_move = False
                    left_move = True
                    critter.x_coordinate -= 1
                    critter_tic = time.perf_counter()
                critter.rect = critter.surf.get_rect(center=(critter.x_coordinate, critter.y_coordinate))

        if critter_toc - critter_tic > 2:
            if left_move:
                if critter.x_coordinate > 475:
                    if walk_move and critter.x_coordinate % 9 == 0:
                        critter.update(critter.x_coordinate, critter.y_coordinate,
                                       graphic_dict["critter_side_left_walk"])
                        walk_move = False
                    else:
                        if critter.x_coordinate % 9 == 0:
                            critter.update(critter.x_coordinate, critter.y_coordinate,
                                           graphic_dict["critter_side_left"])
                            walk_move = True
                    critter.x_coordinate -= 1
                else:
                    critter.update(critter.x_coordinate, critter.y_coordinate, graphic_dict["critter_front"])
                    right_move = True
                    left_move = False
                    critter.x_coordinate += 1
                    critter_tic = time.perf_counter()
                critter.rect = critter.surf.get_rect(center=(critter.x_coordinate, critter.y_coordinate))

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)

    if time_of_day == 0:
        screen.blit(dawn, (0, 0))
    if time_of_day == 1:
        screen.blit(early_morning, (0, 0))
    if time_of_day == 2:
        screen.blit(morning, (0, 0))
    if time_of_day == 4:
        screen.blit(early_afternoon, (0, 0))
    if time_of_day == 5:
        screen.blit(afternoon, (0, 0))
    if time_of_day == 6:
        screen.blit(dusk, (0, 0))
    if time_of_day == 7:
        screen.blit(night, (0, 0))

    if not item_block_got:
        screen.blit(item_block.surf, item_block.rect)

    if pygame.Rect.colliderect(player.rect, ectrenos_pet_entrance):
        interaction_popup.update(816, 178, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Menagerie"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (816, 178)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter Menagerie."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_door)
            interacted = False
            movement_able = False
            in_over_world = False
            over_world_song_set = False
            in_menagerie = True

    if pygame.sprite.collide_rect(player, altar):
        interaction_popup.update(altar.x_coordinate + 8, altar.y_coordinate - 115,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Altar"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (altar.x_coordinate + 8, altar.y_coordinate - 115)
        screen.blit(interaction_info_surf, interaction_info_rect)
        info_text_1 = "Press 'F' key to enter the Altar."

        if interacted:
            interacted = False
            over_world_song_set = False
            player.current_zone = "altar"
            player.x_coordinate = 515
            player.y_coordinate = 650
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # if player collides with npc sprite and chooses to interact with it
    if player.quest_progress["las escondidas"] == 0 and player.quest_status["las escondidas"]:
        if pygame.sprite.collide_rect(player, npc_leyre):
            interaction_popup.update(npc_leyre.x_coordinate, npc_leyre.y_coordinate - 50,
                                     graphic_dict["popup_interaction_purple"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str(npc_leyre.name), True, "black", (203, 195, 227))
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (npc_leyre.x_coordinate, npc_leyre.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            info_text_1 = "Press 'F' key to talk to NPC."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world and not in_battle and not in_shop and not in_inn \
                    and not in_npc_interaction:
                interacted = False
                player.quest_progress["las escondidas"] += 1
                pygame.mixer.find_channel(True).play(sfx_find)
                info_text_1 = "You've found Leyre!"
                info_text_2 = "Looks like they went to hide again. "
                info_text_3 = ""
                info_text_4 = ""

    if pygame.sprite.collide_rect(player, item_block):
        if not item_block_got:
            interaction_popup.update(item_block.x_coordinate, item_block.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Item Block"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (item_block.x_coordinate, item_block.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not item_block_got:
                    if len(player.items) < 16:
                        item = random.randint(1, 14)
                        item_block_got = True
                        pygame.mixer.find_channel(True).play(sfx_item_block)
                        if item == 1:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Big Health Potion!"
                            player.items.append(Item("big health potion", "potion", 200, 200,
                                                     graphic_dict["health_pot_img"], 0))
                        if item == 2:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Big Energy Potion!"
                            player.items.append(Item("big energy potion", "potion", 200, 200,
                                                     graphic_dict["energy_pot_img"], 0))
                        if item == 3:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "50 Rupees!"
                            player.rupees += 50
                        if item == 4:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "Eldream Bait!"
                            player.items.append(Item("eldream bait", "bait", 200, 200,
                                                     graphic_dict["eldream_bait"], 0))
                        if item == 5:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Pet Snack!"
                            if kasper_unlocked:
                                player.items.append(Item("pet cookie", "cookie", 200, 200,
                                                         graphic_dict["pet_cookie_img"], 1))
                            elif torok_unlocked:
                                player.items.append(Item("pet candy", "candy", 200, 200,
                                                         graphic_dict["pet_candy_img"], 1))
                            elif iriana_unlocked:
                                player.items.append(Item("pet tart", "tart", 200, 200,
                                                         graphic_dict["pet_tart_img"], 1))
                            else:
                                player.items.append(Item("pet cookie", "cookie", 200, 200,
                                                         graphic_dict["pet_cookie_img"], 1))
                        if item == 6:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A mage book!"
                            player.items.append(Item("mage book", "book", 200, 200,
                                                     graphic_dict["mage_book"], 0))
                        if item == 7:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A fighter book!"
                            player.items.append(Item("fighter book", "book", 200, 200,
                                                     graphic_dict["fighter_book"], 0))
                        if item == 8:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A scout book!"
                            player.items.append(Item("scout book", "book", 200, 200,
                                                     graphic_dict["scout_book"], 0))
                        if item == 9:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A poison cure potion!"
                            player.items.append(Item("cure poison potion", "potion", 200, 200,
                                                     graphic_dict["poison_cure"], 0))
                        if item == 10:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A burn cure potion!"
                            player.items.append(Item("cure burn potion", "potion", 200, 200,
                                                     graphic_dict["burn_cure"], 0))
                        if item == 11:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A bandage wrap!"
                            player.items.append(Item("bandage wrap", "wrap", 200, 200,
                                                     graphic_dict["bandage_wrap"], 0))
                        if item == 12:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A big cure potion!"
                            player.items.append(Item("big cure potion", "potion", 200, 200,
                                                     graphic_dict["big_cure_potion"], 0))
                        if item == 13:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A reinforcing brace!"
                            player.items.append(Item("brace", "brace", 200, 200,
                                                     graphic_dict["brace"], 0))
                        if item == 14:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A big mend potion!"
                            player.items.append(Item("big mend potion", "potion", 200, 200,
                                                     graphic_dict["big_mend_potion"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""

            interacted = False

    # --------------------------------------------------------------------------------------------------
    screen.blit(mini_map.surf, mini_map.rect)

    if 990 < player.x_coordinate and 395 < player.y_coordinate < 625:
        player.current_zone = "ectrenos"
        mini_map.update(915, 596, graphic_dict["ectrenos_mini_map"])
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 80
        player.y_coordinate = 535
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
    if 660 < player.x_coordinate < 975 and 675 < player.y_coordinate:
        player.current_zone = "ectrenos front"
        mini_map.update(915, 596, graphic_dict["ectrenos_mini_map_front"])
        in_over_world = True
        player.x_coordinate = 120
        player.y_coordinate = 445
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # npc movement updates
    if player.quest_status["las escondidas"] and not player.quest_complete["las escondidas"]:
        face_direction = random.choice(["front", "back", "left", "right"])
        if movement_able and in_over_world:
            npc_toc = time.perf_counter()
            if npc_toc - npc_tic > 5:
                npc_tic = time.perf_counter()
                if face_direction == "front":
                    npc_leyre.update(graphic_dict["leyre_down"])
                if face_direction == "back":
                    npc_leyre.update(graphic_dict["leyre_up"])
                if face_direction == "left":
                    npc_leyre.update(graphic_dict["leyre_left"])
                if face_direction == "right":
                    npc_leyre.update(graphic_dict["leyre_right"])

    ectrenos_left_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic, "info_text_1": info_text_1,
                            "info_text_2": info_text_2, "info_text_3": info_text_3, "info_text_4": info_text_4,
                            "interacted": interacted, "in_over_world": in_over_world, "in_battle": in_battle,
                            "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                            "current_enemy_battling": current_enemy_battling,
                            "current_npc_interacting": current_npc_interacting, "eldream_attuned": eldream_attuned,
                            "in_shop": in_shop, "in_inn": in_inn,
                            "current_building_entering": current_building_entering,
                            "enemy_tic": enemy_tic, "eldream_flowers": eldream_flowers,
                            "interactables_ectrenos": interactables_ectrenos, "in_menagerie": in_menagerie,
                            "right_move": right_move, "left_move": left_move, "critter_tic": critter_tic,
                            "walk_move": walk_move, "item_block_got": item_block_got}

    return ectrenos_left_return


def ectrenos_right(pygame, screen, graphic_dict, player, ectrenos_right_bg, eldream_overworld_music,
                   over_world_song_set, interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                   hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted, info_text_1,
                   info_text_2, info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle, movement_able,
                   current_enemy_battling, current_npc_interacting, equipment_screen, staff, sword, bow, npc_garan,
                   offense_meter, defense_meter, weapon_select, eldream_attuned, in_shop, in_inn,
                   current_building_entering, enemy_tic, eldream_flowers, interactables_ectrenos,
                   ectrenos_shop_entrance, ectrenos_inn_entrance, pet_energy_window, npc_leyre, sfx_find, critter,
                   right_move, left_move, critter_tic, walk_move, mini_map, basic_fish_counter,
                   better_fish_counter, even_better_fish_counter, best_fish_counter, item_block, item_block_got,
                   sfx_item_block, Item, kasper_unlocked, torok_unlocked, iriana_unlocked, apothis_gift, dawn,
                   early_morning, morning, early_afternoon, afternoon, dusk, night, time_of_day, sfx_door,
                   night_music):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            if time_of_day == 0 or time_of_day == 7:
                pygame.mixer.music.load(night_music)
            else:
                pygame.mixer.music.load(eldream_overworld_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(ectrenos_right_bg, (0, 0))

    if player.quest_progress["las escondidas"] == 1 and player.quest_status["las escondidas"]:
        npc_leyre.update_position(722, 350)
        screen.blit(npc_leyre.surf, npc_leyre.rect)

    if time_of_day != 0 and time_of_day != 7:
        if critter.x_coordinate > 450:
            screen.blit(critter.surf, critter.rect)
        critter_toc = time.perf_counter()
        if critter_toc - critter_tic > 2:
            if right_move:
                if critter.x_coordinate < 575:
                    if walk_move and critter.x_coordinate % 9 == 0:
                        critter.update(critter.x_coordinate, critter.y_coordinate,
                                       graphic_dict["critter_side_right_walk"])
                        walk_move = False
                    else:
                        if critter.x_coordinate % 9 == 0:
                            critter.update(critter.x_coordinate, critter.y_coordinate,
                                           graphic_dict["critter_side_right"])
                            walk_move = True
                    critter.x_coordinate += 1
                else:
                    critter.update(critter.x_coordinate, critter.y_coordinate, graphic_dict["critter_front"])
                    right_move = False
                    left_move = True
                    critter.x_coordinate -= 1
                    critter_tic = time.perf_counter()
                critter.rect = critter.surf.get_rect(center=(critter.x_coordinate, critter.y_coordinate))

        if critter_toc - critter_tic > 2:
            if left_move:
                if critter.x_coordinate > 400:
                    if walk_move and critter.x_coordinate % 9 == 0:
                        critter.update(critter.x_coordinate, critter.y_coordinate,
                                       graphic_dict["critter_side_left_walk"])
                        walk_move = False
                    else:
                        if critter.x_coordinate % 9 == 0:
                            critter.update(critter.x_coordinate, critter.y_coordinate,
                                           graphic_dict["critter_side_left"])
                            walk_move = True
                    critter.x_coordinate -= 1
                else:
                    critter.update(critter.x_coordinate, critter.y_coordinate, graphic_dict["critter_front"])
                    right_move = True
                    left_move = False
                    critter.x_coordinate += 1
                    critter_tic = time.perf_counter()
                critter.rect = critter.surf.get_rect(center=(critter.x_coordinate, critter.y_coordinate))

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)

    if time_of_day == 0:
        screen.blit(dawn, (0, 0))
    if time_of_day == 1:
        screen.blit(early_morning, (0, 0))
    if time_of_day == 2:
        screen.blit(morning, (0, 0))
    if time_of_day == 4:
        screen.blit(early_afternoon, (0, 0))
    if time_of_day == 5:
        screen.blit(afternoon, (0, 0))
    if time_of_day == 6:
        screen.blit(dusk, (0, 0))
    if time_of_day == 7:
        screen.blit(night, (0, 0))

    if not item_block_got:
        screen.blit(item_block.surf, item_block.rect)

    if pygame.Rect.colliderect(player.rect, ectrenos_shop_entrance):
        interaction_popup.update(217, 178, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Shop"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (217, 178)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if time_of_day == 0 or time_of_day == 7:
            info_text_1 = "Press 'F' key to enter shop."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""
        else:
            info_text_1 = "Shop only open at night."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

        if interacted and in_over_world:
            if time_of_day == 0 or time_of_day == 7:
                pygame.mixer.find_channel(True).play(sfx_door)
                interacted = False
                movement_able = False
                in_over_world = False
                over_world_song_set = False
                in_shop = True
            else:
                interacted = False

    if pygame.Rect.colliderect(player.rect, ectrenos_inn_entrance):
        interaction_popup.update(875, 275, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Inn"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (875, 275)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter inn."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            movement_able = False
            in_over_world = False
            over_world_song_set = False
            in_inn = True

    # if player collides with npc sprite and chooses to interact with it
    if player.quest_progress["las escondidas"] == 1 and player.quest_status["las escondidas"]:
        if pygame.sprite.collide_rect(player, npc_leyre):
            interaction_popup.update(npc_leyre.x_coordinate, npc_leyre.y_coordinate - 50,
                                     graphic_dict["popup_interaction_purple"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str(npc_leyre.name), True, "black", (203, 195, 227))
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (npc_leyre.x_coordinate, npc_leyre.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            info_text_1 = "Press 'F' key to talk to NPC."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world and not in_battle and not in_shop and not in_inn \
                    and not in_npc_interaction:
                interacted = False
                player.quest_progress["las escondidas"] += 1
                pygame.mixer.find_channel(True).play(sfx_find)
                info_text_1 = "You've found Leyre!"
                info_text_2 = "Looks like they went to hide again. "
                info_text_3 = ""
                info_text_4 = ""

    if pygame.sprite.collide_rect(player, item_block):
        if not item_block_got:
            interaction_popup.update(item_block.x_coordinate, item_block.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Item Block"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (item_block.x_coordinate, item_block.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not item_block_got:
                    if len(player.items) < 16:
                        item = random.randint(1, 14)
                        item_block_got = True
                        pygame.mixer.find_channel(True).play(sfx_item_block)
                        if item == 1:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Big Health Potion!"
                            player.items.append(Item("big health potion", "potion", 200, 200,
                                                     graphic_dict["health_pot_img"], 0))
                        if item == 2:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Big Energy Potion!"
                            player.items.append(Item("big energy potion", "potion", 200, 200,
                                                     graphic_dict["energy_pot_img"], 0))
                        if item == 3:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "50 Rupees!"
                            player.rupees += 50
                        if item == 4:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "Eldream Bait!"
                            player.items.append(Item("eldream bait", "bait", 200, 200,
                                                     graphic_dict["eldream_bait"], 0))
                        if item == 5:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Pet Snack!"
                            if kasper_unlocked:
                                player.items.append(Item("pet cookie", "cookie", 200, 200,
                                                         graphic_dict["pet_cookie_img"], 1))
                            elif torok_unlocked:
                                player.items.append(Item("pet candy", "candy", 200, 200,
                                                         graphic_dict["pet_candy_img"], 1))
                            elif iriana_unlocked:
                                player.items.append(Item("pet tart", "tart", 200, 200,
                                                         graphic_dict["pet_tart_img"], 1))
                            else:
                                player.items.append(Item("pet cookie", "cookie", 200, 200,
                                                         graphic_dict["pet_cookie_img"], 1))
                        if item == 6:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A mage book!"
                            player.items.append(Item("mage book", "book", 200, 200,
                                                     graphic_dict["mage_book"], 0))
                        if item == 7:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A fighter book!"
                            player.items.append(Item("fighter book", "book", 200, 200,
                                                     graphic_dict["fighter_book"], 0))
                        if item == 8:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A scout book!"
                            player.items.append(Item("scout book", "book", 200, 200,
                                                     graphic_dict["scout_book"], 0))
                        if item == 9:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A poison cure potion!"
                            player.items.append(Item("cure poison potion", "potion", 200, 200,
                                                     graphic_dict["poison_cure"], 0))
                        if item == 10:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A burn cure potion!"
                            player.items.append(Item("cure burn potion", "potion", 200, 200,
                                                     graphic_dict["burn_cure"], 0))
                        if item == 11:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A bandage wrap!"
                            player.items.append(Item("bandage wrap", "wrap", 200, 200,
                                                     graphic_dict["bandage_wrap"], 0))
                        if item == 12:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A big cure potion!"
                            player.items.append(Item("big cure potion", "potion", 200, 200,
                                                     graphic_dict["big_cure_potion"], 0))
                        if item == 13:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A reinforcing brace!"
                            player.items.append(Item("brace", "brace", 200, 200,
                                                     graphic_dict["brace"], 0))
                        if item == 14:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A big mend potion!"
                            player.items.append(Item("big mend potion", "potion", 200, 200,
                                                     graphic_dict["big_mend_potion"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""

            interacted = False

    # --------------------------------------------------------------------------------------------------
    screen.blit(mini_map.surf, mini_map.rect)

    if 50 > player.x_coordinate and 400 < player.y_coordinate < 620:
        player.current_zone = "ectrenos"
        mini_map.update(915, 596, graphic_dict["ectrenos_mini_map"])
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 958
        player.y_coordinate = 535
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if 50 < player.x_coordinate < 375 and 675 < player.y_coordinate:
        player.current_zone = "ectrenos front"
        mini_map.update(915, 596, graphic_dict["ectrenos_mini_map_front"])
        in_over_world = True
        player.x_coordinate = 900
        player.y_coordinate = 445
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # npc movement updates
    if player.quest_status["las escondidas"] and not player.quest_complete["las escondidas"]:
        face_direction = random.choice(["front", "back", "left", "right"])
        if movement_able and in_over_world:
            npc_toc = time.perf_counter()
            if npc_toc - npc_tic > 5:
                npc_tic = time.perf_counter()
                if face_direction == "front":
                    npc_leyre.update(graphic_dict["leyre_down"])
                if face_direction == "back":
                    npc_leyre.update(graphic_dict["leyre_up"])
                if face_direction == "left":
                    npc_leyre.update(graphic_dict["leyre_left"])
                if face_direction == "right":
                    npc_leyre.update(graphic_dict["leyre_right"])

    ectrenos_right_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic, "info_text_1": info_text_1,
                             "info_text_2": info_text_2, "info_text_3": info_text_3, "info_text_4": info_text_4,
                             "interacted": interacted, "in_over_world": in_over_world, "in_battle": in_battle,
                             "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                             "current_enemy_battling": current_enemy_battling,
                             "current_npc_interacting": current_npc_interacting, "eldream_attuned": eldream_attuned,
                             "in_shop": in_shop, "in_inn": in_inn,
                             "current_building_entering": current_building_entering,
                             "enemy_tic": enemy_tic, "eldream_flowers": eldream_flowers,
                             "interactables_ectrenos": interactables_ectrenos, "right_move": right_move,
                             "left_move": left_move, "critter_tic": critter_tic, "walk_move": walk_move,
                             "item_block_got": item_block_got}

    return ectrenos_right_return


def ectrenos_front(pygame, screen, graphic_dict, player, ectrenos_front_bg, eldream_overworld_music,
                   over_world_song_set, interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                   hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted, info_text_1,
                   info_text_2, info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle, movement_able,
                   current_enemy_battling, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite,
                   chorizon_battle_sprite, muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite,
                   chinzilla_battle_sprite, barrier_active, sharp_sense_active, current_npc_interacting,
                   equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select,
                   eldream_attuned, in_shop, in_inn, current_building_entering, enemy_tic, eldream_flowers,
                   seldon_enemies, korlok_enemies, snakes, ghouls, magmons, bandiles, interactables_seldon,
                   interactables_korlok, interactables_mines, Enemy, Item, UiElement, seldon_flowers,
                   interactables_ectrenos, quest_star_everett, pet_energy_window, npc_everett, npc_leyre,
                   ectrenos_front_enemies, interactables_eldream, necrola_battle_sprite, osodark_battle_sprite,
                   sfx_find, stelli_battle_sprite, vanished, vanish_overlay, mini_map, basic_fish_counter,
                   better_fish_counter, even_better_fish_counter, best_fish_counter, necrolas_highlighted,
                   necrolas_reset, apothis_gift, dawn, early_morning, morning, early_afternoon, afternoon, dusk, night,
                   time_of_day, cloaked, kasper_unlocked, torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                   torok_battle_sprite, iriana_battle_sprite, night_music, chroma_bridge):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            if time_of_day == 0 or time_of_day == 7:
                pygame.mixer.music.load(night_music)
            else:
                pygame.mixer.music.load(eldream_overworld_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(ectrenos_front_bg, (0, 0))

    respawned_dict = gameplay_functions.enemy_respawn(player, seldon_enemies, korlok_enemies, snakes, ghouls, magmons,
                                                      bandiles, interactables_seldon, interactables_korlok,
                                                      interactables_mines, Enemy, Item, graphic_dict, UiElement,
                                                      seldon_flowers, eldream_flowers, interactables_eldream,
                                                      ectrenos_front_enemies, ectrenos_front_enemies,
                                                      ectrenos_front_enemies, ectrenos_front_enemies,
                                                      ectrenos_front_enemies, False, False, False, False, time_of_day)
    ectrenos_front_enemies = respawned_dict["ectrenos_front_enemies"]

    if player.quest_status["shades of fear"] and not player.quest_complete["shades of fear"]:
        if not necrolas_highlighted:
            for enemy_sprite in ectrenos_front_enemies:
                if enemy_sprite.name == "Necrola":
                    enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                              graphic_dict["necrola_high"])
            necrolas_highlighted = True
    if player.quest_complete["shades of fear"]:
        if not necrolas_reset:
            for enemy_sprite in ectrenos_front_enemies:
                if enemy_sprite.name == "Necrola":
                    enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                              graphic_dict["necrola"])
            necrolas_reset = True

    for enemy in ectrenos_front_enemies:
        screen.blit(enemy.surf, enemy.rect)
    screen.blit(npc_everett.surf, npc_everett.rect)

    if player.quest_progress["las escondidas"] == 2 and player.quest_status["las escondidas"]:
        npc_leyre.update_position(672, 532)
        screen.blit(npc_leyre.surf, npc_leyre.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
    if vanished:
        vanish_overlay.update(player.x_coordinate, player.y_coordinate, graphic_dict["vanish_img"])
        screen.blit(vanish_overlay.surf, vanish_overlay.rect)

    if time_of_day == 0:
        screen.blit(dawn, (0, 0))
    if time_of_day == 1:
        screen.blit(early_morning, (0, 0))
    if time_of_day == 2:
        screen.blit(morning, (0, 0))
    if time_of_day == 4:
        screen.blit(early_afternoon, (0, 0))
    if time_of_day == 5:
        screen.blit(afternoon, (0, 0))
    if time_of_day == 6:
        screen.blit(dusk, (0, 0))
    if time_of_day == 7:
        screen.blit(night, (0, 0))

    if not player.quest_complete["shades of fear"]:
        screen.blit(quest_star_everett.surf, quest_star_everett.rect)

    # if player collides with npc sprite and chooses to interact with it
    if pygame.sprite.collide_rect(player, npc_everett):
        interaction_popup.update(npc_everett.x_coordinate, npc_everett.y_coordinate - 50,
                                 graphic_dict["popup_interaction_purple"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(npc_everett.name), True, "black", (203, 195, 227))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (npc_everett.x_coordinate, npc_everett.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to talk to NPC."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world and not in_battle and not in_shop and not in_inn \
                and not in_npc_interaction:
            current_npc_interacting = npc_everett
            in_over_world = False
            in_npc_interaction = True
            movement_able = False
            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                    sharp_sense_active, graphic_dict, kasper_unlocked,
                                                    torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                    torok_battle_sprite, iriana_battle_sprite)
            combat_scenario.battle_animation_enemy(current_enemy_battling, snake_battle_sprite,
                                                   ghoul_battle_sprite,
                                                   chorizon_battle_sprite, muchador_battle_sprite,
                                                   magmon_battle_sprite, bandile_battle_sprite,
                                                   chinzilla_battle_sprite, in_battle, in_npc_interaction,
                                                   graphic_dict, necrola_battle_sprite,
                                                   osodark_battle_sprite, stelli_battle_sprite,
                                                   False, stelli_battle_sprite, 0, ectrenos_front_enemies,
                                                   stelli_battle_sprite, stelli_battle_sprite, False, False,
                                                   time_of_day, True)

    # if player collides with npc sprite and chooses to interact with it
    if player.quest_progress["las escondidas"] == 2 and player.quest_status["las escondidas"]:
        if pygame.sprite.collide_rect(player, npc_leyre):
            interaction_popup.update(npc_leyre.x_coordinate, npc_leyre.y_coordinate - 50,
                                     graphic_dict["popup_interaction_purple"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str(npc_leyre.name), True, "black", (203, 195, 227))
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (npc_leyre.x_coordinate, npc_leyre.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            info_text_1 = "Press 'F' key to talk to NPC."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world and not in_battle and not in_shop and not in_inn \
                    and not in_npc_interaction:
                interacted = False
                player.quest_progress["las escondidas"] += 1
                pygame.mixer.find_channel(True).play(sfx_find)
                info_text_1 = "You've found Leyre!"
                info_text_2 = "Looks like they went to hide again. "
                info_text_3 = ""
                info_text_4 = ""

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, ectrenos_front_enemies)
    if enemy:
        interaction_popup.update(enemy.x_coordinate, enemy.y_coordinate - 40, graphic_dict["popup_interaction_red"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(enemy.name) + " lvl " + str(enemy.level), True, "black",
                                            (255, 204, 203))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (enemy.x_coordinate, enemy.y_coordinate - 40)
        screen.blit(interaction_info_surf, interaction_info_rect)

        # lets player know if they are in range of enemy they can press f to attack it
        info_text_1 = "Press 'F' key to attack enemy."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            current_enemy_battling = enemy
            in_over_world = False
            in_battle = True

            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                    sharp_sense_active, graphic_dict, kasper_unlocked,
                                                    torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                    torok_battle_sprite, iriana_battle_sprite)
            combat_scenario.battle_animation_enemy(current_enemy_battling, snake_battle_sprite,
                                                   ghoul_battle_sprite,
                                                   chorizon_battle_sprite, muchador_battle_sprite,
                                                   magmon_battle_sprite, bandile_battle_sprite,
                                                   chinzilla_battle_sprite, in_battle, in_npc_interaction,
                                                   graphic_dict, necrola_battle_sprite,
                                                   osodark_battle_sprite, stelli_battle_sprite,
                                                   False, stelli_battle_sprite, 0, ectrenos_front_enemies,
                                                   ectrenos_front_enemies, stelli_battle_sprite, False, cloaked,
                                                   time_of_day, True)

    # --------------------------------------------------------------------------------------------------
    screen.blit(mini_map.surf, mini_map.rect)

    if 85 > player.x_coordinate and player.y_coordinate < 375:
        player.current_zone = "ectrenos left"
        mini_map.update(915, 596, graphic_dict["ectrenos_mini_map_left"])
        chroma_bridge.update(477, 493, graphic_dict["chroma_bridge"])
        in_over_world = True
        player.x_coordinate = 850
        player.y_coordinate = 530
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
    if 920 < player.x_coordinate and player.y_coordinate < 375:
        player.current_zone = "ectrenos right"
        mini_map.update(915, 596, graphic_dict["ectrenos_mini_map_right"])
        in_over_world = True
        player.x_coordinate = 210
        player.y_coordinate = 515
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # npc movement updates
    face_direction = random.choice(["front", "back", "left", "right"])
    if movement_able and in_over_world:
        npc_toc = time.perf_counter()
        if npc_toc - npc_tic > 5:
            npc_tic = time.perf_counter()
            if face_direction == "front":
                npc_everett.update(graphic_dict["everett_down"])
                if player.quest_status["las escondidas"] and not player.quest_complete["las escondidas"]:
                    npc_leyre.update(graphic_dict["leyre_up"])
            if face_direction == "back":
                npc_everett.update(graphic_dict["everett_up"])
                if player.quest_status["las escondidas"] and not player.quest_complete["las escondidas"]:
                    npc_leyre.update(graphic_dict["leyre_down"])
            if face_direction == "left":
                npc_everett.update(graphic_dict["everett_left"])
                if player.quest_status["las escondidas"] and not player.quest_complete["las escondidas"]:
                    npc_leyre.update(graphic_dict["leyre_right"])
            if face_direction == "right":
                npc_everett.update(graphic_dict["everett_right"])
                if player.quest_status["las escondidas"] and not player.quest_complete["las escondidas"]:
                    npc_leyre.update(graphic_dict["leyre_left"])

    # enemy movement updates
    direction_horizontal = random.choice(["left", "right"])
    direction_vertical = random.choice(["up", "down"])
    move_mon = random.choice(ectrenos_front_enemies.sprites())
    if movement_able and in_over_world:
        enemy_toc = time.perf_counter()
        if enemy_toc - enemy_tic > 1:
            enemy_tic = time.perf_counter()
            move_mon.update_position([200, 600], [300, 500], direction_horizontal, direction_vertical)

    ectrenos_front_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic, "info_text_1": info_text_1,
                             "info_text_2": info_text_2, "info_text_3": info_text_3, "info_text_4": info_text_4,
                             "interacted": interacted, "in_over_world": in_over_world, "in_battle": in_battle,
                             "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                             "current_enemy_battling": current_enemy_battling,
                             "current_npc_interacting": current_npc_interacting, "eldream_attuned": eldream_attuned,
                             "in_shop": in_shop, "in_inn": in_inn,
                             "current_building_entering": current_building_entering,
                             "enemy_tic": enemy_tic, "eldream_flowers": eldream_flowers,
                             "interactables_ectrenos": interactables_ectrenos,
                             "necrolas_highlighted": necrolas_highlighted, "necrolas_reset": necrolas_reset}

    return ectrenos_front_return


def ectrenos_alcove(pygame, screen, graphic_dict, player, ectrenos_alcove_bg, eldream_building_music,
                    over_world_song_set, interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                    hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                    info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle,
                    movement_able, current_enemy_battling, current_npc_interacting, equipment_screen, staff, sword, bow,
                    npc_garan, offense_meter, defense_meter, weapon_select, eldream_attuned, in_shop, in_inn,
                    current_building_entering, enemy_tic, eldream_flowers, interactables_ectrenos,
                    pet_energy_window, ladder, chroma_bridge, alcove_star, npc_leyre, enemies, sfx_find, sfx_ladder,
                    vanished, vanish_overlay, mini_map, osodark_battle_sprite, player_battle_sprite,
                    barrier_active, sharp_sense_active, Enemy, Item, UiElement, alcove_rect, basic_fish_counter,
                    better_fish_counter, even_better_fish_counter, best_fish_counter, apothis_gift, time_of_day,
                    kasper_unlocked, torok_unlocked, iriana_unlocked, kasper_battle_sprite, torok_battle_sprite,
                    iriana_battle_sprite):
    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(eldream_building_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(ectrenos_alcove_bg, (0, 0))
    respawned_dict = gameplay_functions.enemy_respawn(player, enemies, enemies, enemies, enemies, enemies, enemies,
                                                      enemies, enemies, enemies, Enemy, Item, graphic_dict, UiElement,
                                                      eldream_flowers, eldream_flowers, enemies, enemies, enemies,
                                                      enemies, enemies, enemies, False, False, False, False,
                                                      time_of_day)
    enemies = respawned_dict["ectrenos_alcove_enemies"]

    if player.quest_progress["las escondidas"] == 3 and player.quest_status["las escondidas"]:
        npc_leyre.update_position(965, 382)
        screen.blit(npc_leyre.surf, npc_leyre.rect)

    for enemy in enemies:
        screen.blit(enemy.surf, enemy.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
    if vanished:
        vanish_overlay.update(player.x_coordinate, player.y_coordinate, graphic_dict["vanish_img"])
        screen.blit(vanish_overlay.surf, vanish_overlay.rect)
    screen.blit(alcove_star.surf, alcove_star.rect)

    if pygame.Rect.colliderect(player.rect, ladder):
        interaction_popup.update(420, 525, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Ectrenos"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (420, 525)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to climb up ladder."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_ladder)
            interacted = False
            chroma_bridge.update(477, 493, graphic_dict["chroma_bridge"])
            player.current_zone = "ectrenos"
            player.x_coordinate = 525
            player.y_coordinate = 648
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.Rect.colliderect(player.rect, alcove_rect):
        interaction_popup.update(410, 25, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Fishing alcove"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (410, 25)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            player.current_zone = "fishing alcove"
            player.x_coordinate = 415
            player.y_coordinate = 625
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # if player collides with npc sprite and chooses to interact with it
    if player.quest_progress["las escondidas"] == 3 and player.quest_status["las escondidas"]:
        if pygame.sprite.collide_rect(player, npc_leyre):
            interaction_popup.update(npc_leyre.x_coordinate, npc_leyre.y_coordinate - 50,
                                     graphic_dict["popup_interaction_purple"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str(npc_leyre.name), True, "black", (203, 195, 227))
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (npc_leyre.x_coordinate, npc_leyre.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            info_text_1 = "Press 'F' key to talk to NPC."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world and not in_battle and not in_shop and not in_inn \
                    and not in_npc_interaction:
                interacted = False
                player.quest_progress["las escondidas"] += 1
                pygame.mixer.find_channel(True).play(sfx_find)
                info_text_1 = "You've found Leyre!"
                info_text_2 = "You've finished hide and seek. "
                info_text_3 = ""
                info_text_4 = ""

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, enemies)
    if enemy:
        interaction_popup.update(enemy.x_coordinate, enemy.y_coordinate - 40, graphic_dict["popup_interaction_red"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(enemy.name) + " lvl " + str(enemy.level), True, "black",
                                            (255, 204, 203))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (enemy.x_coordinate, enemy.y_coordinate - 40)
        screen.blit(interaction_info_surf, interaction_info_rect)

        # lets player know if they are in range of enemy they can press f to attack it
        info_text_1 = "Press 'F' key to attack enemy."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            current_enemy_battling = enemy
            in_over_world = False
            in_battle = True

            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                    sharp_sense_active, graphic_dict, kasper_unlocked,
                                                    torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                    torok_battle_sprite, iriana_battle_sprite)
            combat_scenario.battle_animation_enemy(current_enemy_battling, osodark_battle_sprite, osodark_battle_sprite,
                                                   osodark_battle_sprite, osodark_battle_sprite, osodark_battle_sprite,
                                                   osodark_battle_sprite, osodark_battle_sprite, in_battle,
                                                   in_npc_interaction, graphic_dict, osodark_battle_sprite,
                                                   osodark_battle_sprite, osodark_battle_sprite, False,
                                                   osodark_battle_sprite, 0, osodark_battle_sprite,
                                                   osodark_battle_sprite, osodark_battle_sprite, False, False,
                                                   time_of_day, True)

    # --------------------------------------------------------------------------------------------------
    screen.blit(mini_map.surf, mini_map.rect)

    # npc movement updates
    if player.quest_status["las escondidas"] and not player.quest_complete["las escondidas"]:
        face_direction = random.choice(["front", "back", "left", "right"])
        if movement_able and in_over_world:
            npc_toc = time.perf_counter()
            if npc_toc - npc_tic > 5:
                npc_tic = time.perf_counter()
                if face_direction == "front":
                    npc_leyre.update(graphic_dict["leyre_down"])
                if face_direction == "back":
                    npc_leyre.update(graphic_dict["leyre_up"])
                if face_direction == "left":
                    npc_leyre.update(graphic_dict["leyre_left"])
                if face_direction == "right":
                    npc_leyre.update(graphic_dict["leyre_right"])

    # enemy movement updates
    if time_of_day != 7 and time_of_day != 0:
        direction_horizontal = random.choice(["left", "right"])
        direction_vertical = random.choice(["up", "down"])
        move_mon = random.choice(enemies.sprites())
        if movement_able and in_over_world:
            enemy_toc = time.perf_counter()
            if enemy_toc - enemy_tic > 1:
                enemy_tic = time.perf_counter()
                move_mon.update_position([200, 700], [100, 300], direction_horizontal, direction_vertical)

    ectrenos_alcove_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                              "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                              "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                              "in_battle": in_battle, "in_npc_interaction": in_npc_interaction,
                              "movement_able": movement_able, "current_enemy_battling": current_enemy_battling,
                              "current_npc_interacting": current_npc_interacting, "eldream_attuned": eldream_attuned,
                              "in_shop": in_shop, "in_inn": in_inn, "ectrenos_alcove_enemies": enemies,
                              "current_building_entering": current_building_entering, "enemy_tic": enemy_tic,
                              "eldream_flowers": eldream_flowers, "interactables_ectrenos": interactables_ectrenos}

    return ectrenos_alcove_return


def fishing_alcove(pygame, screen, player, over_world_song_set, eldream_building_music, fishing, walk_tic,
                   fishing_spot_1, fishing_spot_2, graphic_dict, fishing_timer, fishing_level, basic_fish_counter,
                   better_fish_counter, even_better_fish_counter, best_fish_counter, fish_caught, previous_surf,
                   water_fish_1, water_fish_3, fishing_alcove_bg, equipment_screen, offense_meter,
                   defense_meter, staff, sword, bow, npc_garan, weapon_select, save_check_window, user_interface,
                   bar_backdrop, hp_bar, en_bar, xp_bar, font, info_text_1, info_text_2, info_text_3, info_text_4,
                   in_over_world, interaction_popup, interacted, fishing_unlocked, movement_able, in_hut,
                   pet_energy_window, alcove_rect, mini_map, sfx_fishing_cast, item_block, item_block_got,
                   sfx_item_block, Item, kasper_unlocked, torok_unlocked, iriana_unlocked, apothis_gift,
                   time_of_day, ectrenos_alcove_enemies):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(eldream_building_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    # if player isn't currently fishing, periodically update spots for animation
    if not fishing:
        if walk_tic % 2 > 1.75:
            fishing_spot_1.update(250, 335, graphic_dict["fishing_spot_1"])
            fishing_spot_2.update(645, 335, graphic_dict["fishing_spot_2"])
        else:
            fishing_spot_1.update(250, 335, graphic_dict["fishing_spot_2"])
            fishing_spot_2.update(645, 335, graphic_dict["fishing_spot_1"])

    # if player is fishing
    else:
        fish_return = gameplay_functions.fishing_function(pygame, fishing_timer, player, player.current_zone,
                                                          graphic_dict["fishing_spot_3"],
                                                          graphic_dict["fishing_spot_4"],
                                                          fishing_spot_1, fishing_spot_2, fishing_level,
                                                          basic_fish_counter, better_fish_counter,
                                                          even_better_fish_counter, best_fish_counter, fishing,
                                                          fish_caught,
                                                          graphic_dict["amuna_m_fishing_right"],
                                                          graphic_dict["amuna_m_fishing_down"],
                                                          graphic_dict["amuna_m_fishing_right_2"],
                                                          graphic_dict["amuna_m_fishing_down_2"],
                                                          graphic_dict["amuna_m_fishing_right_3"],
                                                          graphic_dict["amuna_m_fishing_down_3"],
                                                          graphic_dict["amuna_f_fishing_right"],
                                                          graphic_dict["amuna_f_fishing_down"],
                                                          graphic_dict["amuna_f_fishing_right_2"],
                                                          graphic_dict["amuna_f_fishing_down_2"],
                                                          graphic_dict["amuna_f_fishing_right_3"],
                                                          graphic_dict["amuna_f_fishing_down_3"],
                                                          graphic_dict["nuldar_m_fishing_right"],
                                                          graphic_dict["nuldar_m_fishing_down"],
                                                          graphic_dict["nuldar_m_fishing_right_2"],
                                                          graphic_dict["nuldar_m_fishing_down_2"],
                                                          graphic_dict["nuldar_m_fishing_right_3"],
                                                          graphic_dict["nuldar_m_fishing_down_3"],
                                                          graphic_dict["nuldar_f_fishing_right"],
                                                          graphic_dict["nuldar_f_fishing_down"],
                                                          graphic_dict["nuldar_f_fishing_right_2"],
                                                          graphic_dict["nuldar_f_fishing_down_2"],
                                                          graphic_dict["nuldar_f_fishing_right_3"],
                                                          graphic_dict["nuldar_f_fishing_down_3"],
                                                          graphic_dict["sorae_a_fishing_right"],
                                                          graphic_dict["sorae_a_fishing_down"],
                                                          graphic_dict["sorae_a_fishing_right_2"],
                                                          graphic_dict["sorae_a_fishing_down_2"],
                                                          graphic_dict["sorae_a_fishing_right_3"],
                                                          graphic_dict["sorae_a_fishing_down_3"],
                                                          graphic_dict["sorae_b_fishing_right"],
                                                          graphic_dict["sorae_b_fishing_down"],
                                                          graphic_dict["sorae_b_fishing_right_2"],
                                                          graphic_dict["sorae_b_fishing_down_2"],
                                                          graphic_dict["sorae_b_fishing_right_3"],
                                                          graphic_dict["sorae_b_fishing_down_3"],
                                                          previous_surf, fishing_spot_1, fishing_spot_2, fishing_spot_1,
                                                          fishing_spot_2, graphic_dict["sorae_a_fishing_up"],
                                                          graphic_dict["sorae_b_fishing_up"],
                                                          graphic_dict["sorae_a_fishing_up_2"],
                                                          graphic_dict["sorae_b_fishing_up_2"],
                                                          graphic_dict["sorae_a_fishing_up_3"],
                                                          graphic_dict["sorae_b_fishing_up_3"],
                                                          graphic_dict["amuna_m_fishing_up"],
                                                          graphic_dict["amuna_f_fishing_up"],
                                                          graphic_dict["amuna_m_fishing_up_2"],
                                                          graphic_dict["amuna_f_fishing_up_2"],
                                                          graphic_dict["amuna_m_fishing_up_3"],
                                                          graphic_dict["amuna_f_fishing_up_3"],
                                                          graphic_dict["nuldar_m_fishing_up"],
                                                          graphic_dict["nuldar_f_fishing_up"],
                                                          graphic_dict["nuldar_m_fishing_up_2"],
                                                          graphic_dict["nuldar_f_fishing_up_2"],
                                                          graphic_dict["nuldar_m_fishing_up_3"],
                                                          graphic_dict["nuldar_f_fishing_up_3"], fishing_spot_1)
        basic_fish_counter = fish_return["basic_fish_counter"]
        better_fish_counter = fish_return["better_fish_counter"]
        even_better_fish_counter = fish_return["even_better_fish_counter"]
        best_fish_counter = fish_return["best_fish_counter"]
        fish_caught = fish_return["fish_caught"]
        fishing = fish_return["fishing"]
        movement_able = fish_return["movement_able"]

    # water movement animation -------------------------------------------------------------------------
    if 675 > water_fish_1.x_coordinate > 185:
        water_fish_1.x_coordinate -= 1
        water_fish_1.rect.midbottom = (water_fish_1.x_coordinate, water_fish_1.y_coordinate)
    else:
        water_fish_1.update(650, water_fish_1.y_coordinate, graphic_dict["water"])

    if 675 > water_fish_3.x_coordinate > 185:
        water_fish_3.x_coordinate -= 1
        water_fish_3.rect.midbottom = (water_fish_3.x_coordinate, water_fish_3.y_coordinate)
    else:
        water_fish_3.update(650, water_fish_3.y_coordinate, graphic_dict["water"])
    # --------------------------------------------------------------------------------------------------

    screen.blit(fishing_alcove_bg, (0, 0))
    screen.blit(water_fish_1.surf, water_fish_1.rect)
    screen.blit(water_fish_3.surf, water_fish_3.rect)
    screen.blit(fishing_spot_1.surf, fishing_spot_1.rect)
    screen.blit(fishing_spot_2.surf, fishing_spot_2.rect)

    if not item_block_got:
        screen.blit(item_block.surf, item_block.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)

    if pygame.Rect.colliderect(player.rect, alcove_rect):
        interaction_popup.update(412, 675, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Ectrenos alcove"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (412, 675)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            player.current_zone = "ectrenos alcove"
            player.x_coordinate = 415
            player.y_coordinate = 125
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
            if time_of_day == 0 or time_of_day == 7:
                for osodark in ectrenos_alcove_enemies:
                    osodark.update_image(osodark.x_coordinate, osodark.y_coordinate,
                                         graphic_dict["osodark_night"])
            else:
                for osodark in ectrenos_alcove_enemies:
                    osodark.update_image(osodark.x_coordinate, osodark.y_coordinate,
                                         graphic_dict["osodark"])

    if not fishing:
        if pygame.sprite.collide_rect(player, fishing_spot_1):
            interaction_popup.update(fishing_spot_1.x_coordinate, fishing_spot_1.y_coordinate - 50,
                                     graphic_dict["popup_interaction_blue"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Fishing spot"), True, "black", "light blue")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (fishing_spot_1.x_coordinate, fishing_spot_1.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if fishing_unlocked:
                info_text_1 = "Press 'F' key to fish."
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""
            else:
                info_text_1 = "You need to unlock fishing. "
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""

            # if player interacts with fishing spot and has it unlocked and has bait, use bait and start
            if interacted and in_over_world and fishing_unlocked:
                for item in player.items:
                    if item.name == "eldream bait":
                        pygame.mixer.find_channel(True).play(sfx_fishing_cast)
                        fishing = True
                        fishing_timer = time.perf_counter()
                        player.items.remove(item)
                        previous_surf = player.surf
                        fish_caught = False
                        break
                interacted = False

        if pygame.sprite.collide_rect(player, fishing_spot_2):
            interaction_popup.update(fishing_spot_2.x_coordinate, fishing_spot_2.y_coordinate - 50,
                                     graphic_dict["popup_interaction_blue"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Fishing spot"), True, "black", "light blue")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (fishing_spot_2.x_coordinate, fishing_spot_2.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if fishing_unlocked:
                info_text_1 = "Press 'F' key to fish."
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""
            else:
                info_text_1 = "You need to unlock fishing. "
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""

            if interacted and in_over_world and fishing_unlocked:
                for item in player.items:
                    if item.name == "eldream bait":
                        pygame.mixer.find_channel(True).play(sfx_fishing_cast)
                        fishing = True
                        fishing_timer = time.perf_counter()
                        player.items.remove(item)
                        previous_surf = player.surf
                        fish_caught = False
                        break
                interacted = False

    if pygame.sprite.collide_rect(player, item_block):
        if not item_block_got:
            interaction_popup.update(item_block.x_coordinate, item_block.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Item Block"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (item_block.x_coordinate, item_block.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not item_block_got:
                    if len(player.items) < 16:
                        item = random.randint(1, 14)
                        item_block_got = True
                        pygame.mixer.find_channel(True).play(sfx_item_block)
                        if item == 1:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Big Health Potion!"
                            player.items.append(Item("big health potion", "potion", 200, 200,
                                                     graphic_dict["health_pot_img"], 0))
                        if item == 2:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Big Energy Potion!"
                            player.items.append(Item("big energy potion", "potion", 200, 200,
                                                     graphic_dict["energy_pot_img"], 0))
                        if item == 3:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "50 Rupees!"
                            player.rupees += 50
                        if item == 4:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "Eldream Bait!"
                            player.items.append(Item("eldream bait", "bait", 200, 200,
                                                     graphic_dict["eldream_bait"], 0))
                        if item == 5:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Pet Snack!"
                            if kasper_unlocked:
                                player.items.append(Item("pet cookie", "cookie", 200, 200,
                                                         graphic_dict["pet_cookie_img"], 1))
                            elif torok_unlocked:
                                player.items.append(Item("pet candy", "candy", 200, 200,
                                                         graphic_dict["pet_candy_img"], 1))
                            elif iriana_unlocked:
                                player.items.append(Item("pet tart", "tart", 200, 200,
                                                         graphic_dict["pet_tart_img"], 1))
                            else:
                                player.items.append(Item("pet cookie", "cookie", 200, 200,
                                                         graphic_dict["pet_cookie_img"], 1))
                        if item == 6:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A mage book!"
                            player.items.append(Item("mage book", "book", 200, 200,
                                                     graphic_dict["mage_book"], 0))
                        if item == 7:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A fighter book!"
                            player.items.append(Item("fighter book", "book", 200, 200,
                                                     graphic_dict["fighter_book"], 0))
                        if item == 8:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A scout book!"
                            player.items.append(Item("scout book", "book", 200, 200,
                                                     graphic_dict["scout_book"], 0))
                        if item == 9:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A poison cure potion!"
                            player.items.append(Item("cure poison potion", "potion", 200, 200,
                                                     graphic_dict["poison_cure"], 0))
                        if item == 10:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A burn cure potion!"
                            player.items.append(Item("cure burn potion", "potion", 200, 200,
                                                     graphic_dict["burn_cure"], 0))
                        if item == 11:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A bandage wrap!"
                            player.items.append(Item("bandage wrap", "wrap", 200, 200,
                                                     graphic_dict["bandage_wrap"], 0))
                        if item == 12:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A big cure potion!"
                            player.items.append(Item("big cure potion", "potion", 200, 200,
                                                     graphic_dict["big_cure_potion"], 0))
                        if item == 13:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A reinforcing brace!"
                            player.items.append(Item("brace", "brace", 200, 200,
                                                     graphic_dict["brace"], 0))
                        if item == 14:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A big mend potion!"
                            player.items.append(Item("big mend potion", "potion", 200, 200,
                                                     graphic_dict["big_mend_potion"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""

            interacted = False

    # --------------------------------------------------------------------------------------------------
    screen.blit(mini_map.surf, mini_map.rect)

    fishing_alcove_return = {"over_world_song_set": over_world_song_set, "basic_fish_counter": basic_fish_counter,
                             "better_fish_counter": better_fish_counter,
                             "even_better_fish_counter": even_better_fish_counter,
                             "best_fish_counter": best_fish_counter, "fish_caught": fish_caught,
                             "movement_able": movement_able, "info_text_1": info_text_1, "info_text_2": info_text_2,
                             "info_text_3": info_text_3, "info_text_4": info_text_4, "in_hut": in_hut,
                             "fishing": fishing, "fishing_timer": fishing_timer, "previous_surf": previous_surf,
                             "interacted": interacted, "in_over_world": in_over_world, "item_block_got": item_block_got}

    return fishing_alcove_return
