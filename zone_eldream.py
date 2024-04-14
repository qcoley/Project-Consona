import random
import time

import drawing_functions
import combat_scenario
import gameplay_functions


def eldream_district(pygame, screen, graphic_dict, player, eldream_district_bg, eldream_overworld_music,
                     over_world_song_set, interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                     hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                     info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle,
                     movement_able, current_enemy_battling, quest_star_garan, quest_star_maurelle, quest_star_celeste,
                     quest_star_torune, star_voruke, star_zerah, star_apothecary, terra_mountains, terra_cave,
                     npc_dionte, quest_star_dionte, enemy, player_battle_sprite, snake_battle_sprite,
                     ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite, magmon_battle_sprite,
                     bandile_battle_sprite, chinzilla_battle_sprite, barrier_active, sharp_sense_active,
                     current_npc_interacting, chinzilla, star_dionte, hearth_stone, equipment_screen, staff, sword, bow,
                     npc_garan, offense_meter, defense_meter, weapon_select, rock_7, rock_7_con, chinzilla_defeated,
                     eldream_gate_rect, eldream_attuned, in_shop, in_inn, current_building_entering, enemy_tic,
                     eldream_flowers, seldon_enemies, korlok_enemies, snakes, ghouls, magmons, bandiles,
                     interactables_seldon, interactables_korlok, interactables_mines, Enemy, Item, UiElement,
                     seldon_flowers, interactables_eldream, ectrenos_entrance, quest_star_omoku, pet_energy_window,
                     omoku, quest_supplies, ectrenos_front_enemies, necrola_battle_sprite, osodark_battle_sprite,
                     sfx_flower, sfx_hearth, sfx_item, kart_full, stelli_battle_sprite, critter, right_move, left_move,
                     critter_tic, walk_move, overlay_marrow_west, overlay_marrow_east, entrance_1, entrance_2,
                     entrance_3, mini_map, basic_fish_counter, better_fish_counter, even_better_fish_counter,
                     best_fish_counter, supplies_highlighted, apothis_gift, dawn, early_morning, morning,
                     early_afternoon, afternoon, dusk, night, time_of_day, kasper_unlocked, torok_unlocked,
                     iriana_unlocked, kasper_battle_sprite, torok_battle_sprite, iriana_battle_sprite, night_music):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            if time_of_day == 0 or time_of_day == 7:
                pygame.mixer.music.load(night_music)
            else:
                pygame.mixer.music.load(eldream_overworld_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(eldream_district_bg, (0, 0))

    if player.quest_status["kart troubles"] and not player.quest_complete["kart troubles"]:
        if not supplies_highlighted:
            for supply in quest_supplies:
                supply.update(supply.x_coordinate, supply.y_coordinate, graphic_dict["quest_supplies_high"])
            supplies_highlighted = True

    if not player.quest_complete["kart troubles"]:
        for supplies in quest_supplies:
            screen.blit(supplies.surf, supplies.rect)
    if player.quest_complete["kart troubles"]:
        screen.blit(kart_full.surf, kart_full.rect)

    respawned_dict = gameplay_functions.enemy_respawn(player, seldon_enemies, korlok_enemies, snakes, ghouls, magmons,
                                                      bandiles, interactables_seldon, interactables_korlok,
                                                      interactables_mines, Enemy, Item, graphic_dict, UiElement,
                                                      seldon_flowers, eldream_flowers, interactables_eldream,
                                                      ectrenos_front_enemies, ectrenos_front_enemies,
                                                      ectrenos_front_enemies, ectrenos_front_enemies,
                                                      ectrenos_front_enemies, False, False, False, False, time_of_day)

    eldream_flowers = respawned_dict["eldream_flowers"]
    interactables_eldream = respawned_dict["interactables_eldream"]

    for flower in eldream_flowers:
        screen.blit(flower.surf, flower.rect)

    screen.blit(hearth_stone.surf, hearth_stone.rect)
    screen.blit(omoku.surf, omoku.rect)

    if time_of_day != 0 and time_of_day != 7:
        screen.blit(critter.surf, critter.rect)
        critter_toc = time.perf_counter()
        if critter_toc - critter_tic > 2:
            if right_move:
                if player.quest_complete["kart troubles"]:
                    if critter.x_coordinate < 730:
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

                if not player.quest_complete["kart troubles"]:
                    if critter.x_coordinate < 555:
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
                if critter.x_coordinate > 350:
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

    if not player.quest_complete["kart troubles"]:
        screen.blit(quest_star_omoku.surf, quest_star_omoku.rect)

    # player collides with flower, if collected adds to player flower count
    flower = pygame.sprite.spritecollideany(player, eldream_flowers)
    if flower and in_over_world:
        flower.update(flower.x_coordinate, flower.y_coordinate, graphic_dict["flower_eldream_high"])
        if interacted:
            pygame.mixer.find_channel(True).play(sfx_flower)
            player.flowers_sorae += 1
            flower.kill()
            info_text_1 = "You collected the Eldream Flower."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""
            interacted = False

    # resets flower surface to non-highlighted if not currently interacting
    for flow in eldream_flowers:
        if flow.surf == graphic_dict["flower_eldream_high"]:
            if flow != flower:
                flow.surf = graphic_dict["flower_eldream"]

    if pygame.sprite.collide_rect(player, hearth_stone):
        interaction_popup.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Hearth stone"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if not eldream_attuned:
            info_text_1 = "Press 'F' key to attune to stone."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world:
                pygame.mixer.find_channel(True).play(sfx_hearth)
                hearth_stone.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate,
                                    graphic_dict["hearth_stone_lit"])
                eldream_attuned = True
                info_text_1 = "You have attuned to the stone."
                info_text_2 = "You may now fast travel here."
                interacted = False
    else:
        hearth_stone.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate, graphic_dict["hearth_stone"])

    if pygame.Rect.colliderect(player.rect, ectrenos_entrance):
        interaction_popup.update(540, 450, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Ectrenos"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (540, 450)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter Ectrenos."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            over_world_song_set = False
            player.current_zone = "ectrenos"
            mini_map.update(915, 596, graphic_dict["ectrenos_mini_map"])
            player.x_coordinate = 515
            player.y_coordinate = 675
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # player encounters a quest item. check progress and add to if interacted with
    if not player.quest_complete["kart troubles"]:
        quest_item = pygame.sprite.spritecollideany(player, quest_supplies, pygame.sprite.collide_rect_ratio(0.75))
        try:
            interaction_popup.update(quest_item.x_coordinate, quest_item.y_coordinate - 35,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Supplies"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (quest_item.x_coordinate, quest_item.y_coordinate - 35)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if quest_item.name == "quest supplies":
                if not player.quest_complete["kart troubles"]:
                    if player.quest_status["kart troubles"]:
                        if player.quest_progress["kart troubles"] < 4:
                            if len(player.items) < 16:
                                info_text_1 = "Press 'F' key to pick up the supplies."
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                            else:
                                info_text_1 = "Inventory is full. "
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                        else:
                            info_text_1 = "You've already gathered these."
                            info_text_2 = ""
                            info_text_3 = ""
                            info_text_4 = ""
                        if interacted and in_over_world:
                            if player.quest_progress["kart troubles"] < 4:
                                if len(player.items) < 16:
                                    pygame.mixer.find_channel(True).play(sfx_item)
                                    player.quest_progress["kart troubles"] += 1
                                    player.items.append(Item("supplies", "item", 200, 200, graphic_dict["supply"], 0))
                                    quest_item.kill()
                                    interacted = False
                                else:
                                    info_text_1 = "Inventory is full."
                                    info_text_2 = ""
                                    info_text_3 = ""
                                    info_text_4 = ""
                                    interacted = False
                            else:
                                info_text_1 = "You've already gathered these."
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                                interacted = False
                if not player.quest_status["kart troubles"]:
                    info_text_1 = "It's someone's supplies."
                    info_text_2 = ""
                    info_text_3 = ""
                    info_text_4 = ""
                    interacted = False
        except AttributeError:
            pass

    # if player collides with npc sprite and chooses to interact with it
    if pygame.sprite.collide_rect(player, omoku):
        interaction_popup.update(omoku.x_coordinate, omoku.y_coordinate - 50, graphic_dict["popup_interaction_purple"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(omoku.name), True, "black", (203, 195, 227))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (omoku.x_coordinate, omoku.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to talk to NPC."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world and not in_battle and not in_shop and not in_inn \
                and not in_npc_interaction:
            current_npc_interacting = omoku
            in_over_world = False
            in_npc_interaction = True
            movement_able = False
            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                    sharp_sense_active, graphic_dict, kasper_unlocked, torok_unlocked,
                                                    iriana_unlocked, kasper_battle_sprite, torok_battle_sprite,
                                                    iriana_battle_sprite)

    # --------------------------------------------------------------------------------------------------
    if player.x_coordinate < 100 and player.y_coordinate < 175:
        player.current_zone = "terra trail"
        in_over_world = True
        if time_of_day != 0 and time_of_day != 7:
            over_world_song_set = False
        player.x_coordinate = 555
        player.y_coordinate = 145
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if 500 < player.x_coordinate < 600 and player.y_coordinate == 705:
        mini_map.update(915, 596, graphic_dict["marrow_mini_map"])
        overlay_marrow_west.update(110, 250, graphic_dict["overlay_marrow_ramps_west"])
        overlay_marrow_east.update(925, 250, graphic_dict["overlay_marrow_ramps_east"])
        entrance_1 = True
        entrance_2 = False
        entrance_3 = False
        player.current_zone = "marrow entrance"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 515
        player.y_coordinate = 75
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # npc movement updates
    face_direction = random.choice(["front", "back", "left", "right"])
    if movement_able and in_over_world:
        npc_toc = time.perf_counter()
        if npc_toc - npc_tic > 5:
            npc_tic = time.perf_counter()
            if face_direction == "front":
                omoku.update(graphic_dict["omoku_down"])
            if face_direction == "back":
                omoku.update(graphic_dict["omoku_up"])
            if face_direction == "left":
                omoku.update(graphic_dict["omoku_left"])
            if face_direction == "right":
                omoku.update(graphic_dict["omoku_right"])

    eldream_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic, "info_text_1": info_text_1,
                      "info_text_2": info_text_2, "info_text_3": info_text_3, "info_text_4": info_text_4,
                      "interacted": interacted, "in_over_world": in_over_world, "in_battle": in_battle,
                      "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                      "current_enemy_battling": current_enemy_battling,
                      "current_npc_interacting": current_npc_interacting, "eldream_attuned": eldream_attuned,
                      "in_shop": in_shop, "in_inn": in_inn, "current_building_entering": current_building_entering,
                      "enemy_tic": enemy_tic, "eldream_flowers": eldream_flowers,
                      "interactables_eldream": interactables_eldream, "right_move": right_move, "left_move": left_move,
                      "critter_tic": critter_tic, "walk_move": walk_move, "entrance_1": entrance_1,
                      "entrance_2": entrance_2, "entrance_3": entrance_3, "supplies_highlighted": supplies_highlighted}

    return eldream_return
