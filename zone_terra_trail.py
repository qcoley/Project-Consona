import random
import time

import cutscenes
import drawing_functions
import combat_scenario


def terra_trail(pygame, screen, graphic_dict, player, mountain_trail_bg, korlok_overworld_music, over_world_song_set,
                interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2, info_text_3,
                info_text_4, npc_tic, in_npc_interaction, in_battle, movement_able, current_enemy_battling,
                terra_mountains, terra_cave, npc_dionte, quest_star_dionte, enemy,
                player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                barrier_active, sharp_sense_active, current_npc_interacting, chinzilla,
                equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, rock_7,
                rock_7_con, chinzilla_defeated, eldream_gate_rect, pet_energy_window, necrola_battle_sprite,
                osodark_battle_sprite, sfx_rupee, stelli_battle_sprite, apothis_music, scene_1, scene_2, scene_3,
                scene_4, scene_5, scene_6, scene_7, scene_8, skip_button, SCREEN_WIDTH, SCREEN_HEIGHT, game_window,
                dreth_cutscenes_not_viewed, dreth_0, vanished, vanish_overlay, critter, right_move, left_move,
                critter_tic, walk_move, basic_fish_counter, better_fish_counter, even_better_fish_counter,
                best_fish_counter, item_block, item_block_got, sfx_item_block, Item, sfx_gate, apothis_gift,
                rohir_gate, dawn, early_morning, morning, early_afternoon, afternoon, dusk, night, time_of_day,
                magmons, overlay_sleep, kasper_unlocked, torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                torok_battle_sprite, iriana_battle_sprite, night_music):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            if time_of_day == 0 or time_of_day == 7:
                pygame.mixer.music.load(night_music)
            else:
                pygame.mixer.music.load(korlok_overworld_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(mountain_trail_bg, (0, 0))
    screen.blit(rock_7.surf, rock_7.rect)
    screen.blit(terra_mountains.surf, terra_mountains.rect)
    screen.blit(terra_cave.surf, terra_cave.rect)
    screen.blit(npc_dionte.surf, npc_dionte.rect)

    if time_of_day != 0 and time_of_day != 7 and not player.quest_complete["it's dangerous to go alone"]:
        screen.blit(overlay_sleep.surf, overlay_sleep.rect)

    if time_of_day != 0 and time_of_day != 7:
        if critter.x_coordinate < 995:
            screen.blit(critter.surf, critter.rect)

    if time_of_day != 0 and time_of_day != 7:
        critter_toc = time.perf_counter()
        if critter_toc - critter_tic > 2:
            if right_move:
                if critter.x_coordinate < 1100:
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
                if critter.x_coordinate > 935:
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

    if not item_block_got:
        screen.blit(item_block.surf, item_block.rect)

    if not player.quest_complete["it's dangerous to go alone"]:
        screen.blit(quest_star_dionte.surf, quest_star_dionte.rect)

    if pygame.sprite.collide_rect(player, npc_dionte):
        interaction_popup.update(npc_dionte.x_coordinate, npc_dionte.y_coordinate - 50,
                                 graphic_dict["popup_interaction_purple"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(npc_dionte.name), True, "black", (203, 195, 227))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (npc_dionte.x_coordinate, npc_dionte.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to talk to NPC."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            current_npc_interacting = npc_dionte
            in_over_world = False
            in_npc_interaction = True
            movement_able = False
            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                    sharp_sense_active, graphic_dict, kasper_unlocked, torok_unlocked,
                                                    iriana_unlocked, kasper_battle_sprite, torok_battle_sprite,
                                                    iriana_battle_sprite)

    if pygame.sprite.collide_rect(player, terra_cave):
        interaction_popup.update(terra_cave.x_coordinate + 75, terra_cave.y_coordinate + 20,
                                 graphic_dict["popup_interaction_red"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Terra cave"), True, "black", (255, 204, 203))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (terra_cave.x_coordinate + 75, terra_cave.y_coordinate + 20)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if player.quest_status["it's dangerous to go alone"] and not \
                player.quest_complete["it's dangerous to go alone"]:
            info_text_1 = "Press 'F' key to enter the cave.."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""
        elif player.quest_complete["it's dangerous to go alone"]:
            info_text_1 = "The monster has been vanquished!"
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""
        else:
            info_text_1 = "You hear howls from within.."
            info_text_2 = "Maybe you should ask around?"
            info_text_3 = ""
            info_text_4 = ""

        if interacted and in_over_world:
            if player.quest_status["it's dangerous to go alone"] and not \
                    player.quest_complete["it's dangerous to go alone"]:
                if not chinzilla_defeated:
                    current_enemy_battling = chinzilla
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
                                                           False, stelli_battle_sprite, 0, stelli_battle_sprite,
                                                           stelli_battle_sprite, stelli_battle_sprite, False, False,
                                                           time_of_day, True)

            interacted = False

    if pygame.sprite.collide_rect(player, rock_7):
        interaction_popup.update(rock_7.x_coordinate, rock_7.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Rock"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rock_7.x_coordinate, rock_7.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            try:
                if player.equipment["gloves"].name == "power gloves":
                    if rock_7.x_coordinate == 515:
                        rock_7.update(rock_7.x_coordinate - 85, rock_7.y_coordinate, graphic_dict["rock_small"])
                        if not rock_7_con:
                            pygame.mixer.find_channel(True).play(sfx_rupee)
                            player.rupees += 20
                            rock_7_con = True
                            info_text_1 = "You found 20 Rupees under the rock!"
                            info_text_2 = ""
                else:
                    info_text_1 = "The rock won't budge."
                    info_text_2 = ""
            except AttributeError:
                info_text_1 = "The rock won't budge."
                info_text_2 = ""
                pass
            interacted = False

    if pygame.Rect.colliderect(player.rect, eldream_gate_rect):
        interaction_popup.update(675, 28, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Eldream"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (675, 28)
        screen.blit(interaction_info_surf, interaction_info_rect)
        if player.quest_complete["it's dangerous to go alone"]:
            info_text_1 = "Press 'F' key to enter Eldream."
            info_text_2 = ""

        if interacted:
            if player.quest_complete["it's dangerous to go alone"]:
                pygame.mixer.find_channel(True).play(sfx_gate)
                interacted = False
                over_world_song_set = False
                player.current_zone = "eldream"
                player.x_coordinate = 255
                player.y_coordinate = 175
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

                if dreth_cutscenes_not_viewed:
                    cutscene_tic = time.perf_counter()
                    if SCREEN_WIDTH != 1280 and SCREEN_HEIGHT != 720:
                        screen.blit(dreth_0, (0, 0))
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                    else:
                        game_window.blit(dreth_0, (0, 0))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    cutscenes.cutscenes_apothis_dreth(pygame, apothis_music, screen, scene_1, scene_2, scene_3, scene_4,
                                                      scene_5, scene_6, scene_7, scene_8, cutscene_tic, skip_button,
                                                      SCREEN_WIDTH, SCREEN_HEIGHT, game_window)
                    dreth_cutscenes_not_viewed = False
            else:
                interacted = False
                info_text_1 = "The gate appears to be shut."
                info_text_2 = "Perhaps the nearby guard knows why?"

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
                        item = random.randint(1, 12)
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
                            info_text_2 = "Korlok Bait!"
                            player.items.append(Item("korlok bait", "bait", 200, 200,
                                                     graphic_dict["korlok_bait"], 0))
                        if item == 5:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A mage book!"
                            player.items.append(Item("mage book", "book", 200, 200,
                                                     graphic_dict["mage_book"], 0))
                        if item == 6:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A fighter book!"
                            player.items.append(Item("fighter book", "book", 200, 200,
                                                     graphic_dict["fighter_book"], 0))
                        if item == 7:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A scout book!"
                            player.items.append(Item("scout book", "book", 200, 200,
                                                     graphic_dict["scout_book"], 0))
                        if item == 8:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A poison cure potion!"
                            player.items.append(Item("cure poison potion", "potion", 200, 200,
                                                     graphic_dict["poison_cure"], 0))
                        if item == 9:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A burn cure potion!"
                            player.items.append(Item("cure burn potion", "potion", 200, 200,
                                                     graphic_dict["burn_cure"], 0))
                        if item == 10:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A bandage wrap!"
                            player.items.append(Item("bandage wrap", "wrap", 200, 200,
                                                     graphic_dict["bandage_wrap"], 0))
                        if item == 11:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A big cure potion!"
                            player.items.append(Item("big cure potion", "potion", 200, 200,
                                                     graphic_dict["big_cure_potion"], 0))
                        if item == 12:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A reinforcing brace!"
                            player.items.append(Item("brace", "brace", 200, 200,
                                                     graphic_dict["brace"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""

            interacted = False

    # --------------------------------------------------------------------------------------------------
    if player.x_coordinate < 75 and player.y_coordinate < 225:
        rohir_gate.update(525, 600, graphic_dict["rohir_gate"])
        player.current_zone = "korlok"
        in_over_world = True
        player.x_coordinate = 900
        player.y_coordinate = 175
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

        if time_of_day == 0 or time_of_day == 7:
            for magmon in magmons:
                if (player.quest_status["elementary elementals"]
                        and not player.quest_complete["elementary elementals"]):
                    magmon.update_image(magmon.x_coordinate, magmon.y_coordinate,
                                        graphic_dict["magmon_high_night"])
                else:
                    magmon.update_image(magmon.x_coordinate, magmon.y_coordinate,
                                        graphic_dict["magmon_night"])
        else:
            for magmon in magmons:
                if (player.quest_status["elementary elementals"]
                        and not player.quest_complete["elementary elementals"]):
                    magmon.update_image(magmon.x_coordinate, magmon.y_coordinate,
                                        graphic_dict["magmon_high"])
                else:
                    magmon.update_image(magmon.x_coordinate, magmon.y_coordinate,
                                        graphic_dict["magmon"])

    # npc movement updates
    face_direction = random.choice(["front", "back", "left", "right"])
    if movement_able and in_over_world:
        npc_toc = time.perf_counter()
        if npc_toc - npc_tic > 5:
            npc_tic = time.perf_counter()
            if face_direction == "front":
                npc_dionte.update(graphic_dict["dionte_down"])
            if face_direction == "back":
                npc_dionte.update(graphic_dict["dionte_up"])
            if face_direction == "left":
                npc_dionte.update(graphic_dict["dionte_left"])
            if face_direction == "right":
                npc_dionte.update(graphic_dict["dionte_right"])

    trail_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic, "info_text_1": info_text_1,
                    "info_text_2": info_text_2, "info_text_3": info_text_3, "info_text_4": info_text_4,
                    "interacted": interacted, "in_over_world": in_over_world, "in_battle": in_battle,
                    "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                    "current_enemy_battling": current_enemy_battling,
                    "current_npc_interacting": current_npc_interacting, "rock_7_con": rock_7_con,
                    "dreth_cutscenes_not_viewed": dreth_cutscenes_not_viewed, "right_move": right_move,
                    "left_move": left_move, "critter_tic": critter_tic, "walk_move": walk_move,
                    "item_block_got": item_block_got}

    return trail_return
