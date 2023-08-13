import random
import time

import drawing_functions
import combat_scenario
import gameplay_functions


def stardust_outpost(pygame, player, screen, stardust_song_set, stardust_outpost_music, stardust_cove_bg,
                     nede_sprite_reset, nede, graphic_dict, ghoul_nede, nede_ghoul_defeated, interaction_popup, font,
                     interacted, in_over_world, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite,
                     chorizon_battle_sprite, muchador_battle_sprite, barrier_active, sharp_sense_active,
                     in_npc_interaction, stardust_entrance, save_check_window, user_interface, bar_backdrop, hp_bar,
                     en_bar, xp_bar, button_highlighted, button_highlight, npc_tic, info_text_1, info_text_2,
                     info_text_3, info_text_4, current_enemy_battling, current_building_entering, in_battle,
                     movement_able, in_shop, magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                     equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select,
                     rock, pet_energy_window, stardust_top, necrola_battle_sprite, osodark_battle_sprite, sfx_nede,
                     sfx_door, sfx_rupee, rock_3_con, outpost_show, outpost_notify, stellis, enemy_tic,
                     stelli_battle_sprite, vanished, vanish_overlay, waterfall, level_checked, fishing_spot_1,
                     fishing_spot_2, fishing, walk_tic, fishing_unlocked, fishing_timer, fish_caught, previous_surf,
                     fishing_level, basic_fish_counter, better_fish_counter, even_better_fish_counter,
                     best_fish_counter):

    if not stardust_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(stardust_outpost_music)
            pygame.mixer.music.play(loops=-1)
            stardust_song_set = True

    screen.blit(stardust_cove_bg, (0, 0))
    screen.blit(rock.surf, rock.rect)
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if player.level > 3:
        if not level_checked:
            for stelli in stellis:
                stelli.level = player.level
            level_checked = True

    # stelli movement updates
    if len(stellis) > 0:
        direction_horizontal = random.choice(["left", "right"])
        direction_vertical = random.choice(["up", "down"])
        move_stelli = random.choice(stellis.sprites())
        if movement_able and in_over_world:
            enemy_toc = time.perf_counter()
            if enemy_toc - enemy_tic > 2:
                enemy_tic = time.perf_counter()
                if move_stelli.name == "stellia":
                    move_stelli.update_position([525, 900], [350, 650], direction_horizontal, direction_vertical)
                if move_stelli.name == "stellib":
                    move_stelli.update_position([550, 900], [100, 380], direction_horizontal, direction_vertical)
                if move_stelli.name == "stellic":
                    move_stelli.update_position([225, 550], [350, 625], direction_horizontal, direction_vertical)

    for stelli in stellis:
        screen.blit(stelli.surf, stelli.rect)

    if not fishing:
        if walk_tic % 2 > 1.75:
            fishing_spot_1.update(900, 490, graphic_dict["fishing_spot_1"])
            fishing_spot_2.update(450, 648, graphic_dict["fishing_spot_2"])
        else:
            fishing_spot_1.update(900, 490, graphic_dict["fishing_spot_2"])
            fishing_spot_2.update(450, 648, graphic_dict["fishing_spot_1"])
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
                                                          graphic_dict["amuna_f_fishing_right"],
                                                          graphic_dict["amuna_f_fishing_down"],
                                                          graphic_dict["nuldar_m_fishing_right"],
                                                          graphic_dict["nuldar_m_fishing_down"],
                                                          graphic_dict["nuldar_f_fishing_right"],
                                                          graphic_dict["nuldar_f_fishing_down"],
                                                          graphic_dict["sorae_a_fishing_right"],
                                                          graphic_dict["sorae_a_fishing_down"],
                                                          graphic_dict["sorae_b_fishing_right"],
                                                          graphic_dict["sorae_b_fishing_down"], previous_surf,
                                                          fishing_spot_1, fishing_spot_2, fishing_spot_1,
                                                          fishing_spot_2, graphic_dict["sorae_a_fishing_up"],
                                                          graphic_dict["sorae_b_fishing_up"],
                                                          graphic_dict["amuna_m_fishing_up"],
                                                          graphic_dict["amuna_f_fishing_up"],
                                                          graphic_dict["nuldar_m_fishing_up"],
                                                          graphic_dict["nuldar_f_fishing_up"])
        basic_fish_counter = fish_return["basic_fish_counter"]
        better_fish_counter = fish_return["better_fish_counter"]
        even_better_fish_counter = fish_return["even_better_fish_counter"]
        best_fish_counter = fish_return["best_fish_counter"]
        fish_caught = fish_return["fish_caught"]
        fishing = fish_return["fishing"]
        movement_able = fish_return["movement_able"]

    screen.blit(fishing_spot_1.surf, fishing_spot_1.rect)
    screen.blit(fishing_spot_2.surf, fishing_spot_2.rect)

    if player.quest_progress["where's nede?"] < 1:
        if player.quest_status["where's nede?"]:
            if not nede_sprite_reset:
                nede.update(nede.x_coordinate, nede.y_coordinate, graphic_dict["nede_high_left"])
                ghoul_nede.update_image(ghoul_nede.x_coordinate,
                                        ghoul_nede.y_coordinate,
                                        graphic_dict["ghoul_high"])
                nede_sprite_reset = True
            screen.blit(nede.surf, nede.rect)
            if not nede_ghoul_defeated:
                screen.blit(ghoul_nede.surf, ghoul_nede.rect)
        else:
            screen.blit(nede.surf, nede.rect)
            if not nede_ghoul_defeated:
                screen.blit(ghoul_nede.surf, ghoul_nede.rect)
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
    drawing_functions.draw_level_up(screen, in_over_world)
    if len(drawing_functions.character_sheet_window) == 0 and len(drawing_functions.journal_window) == 0 and \
            len(drawing_functions.world_map_container) == 0:
        screen.blit(stardust_top.surf, stardust_top.rect)

    screen.blit(waterfall.surf, waterfall.rect)
    try:
        for pet in player.pet:
            if pet.active:
                pet_energy_surf = font.render(str(pet.energy) + " /100", True, "dark green", "light yellow")
                pet_energy_rect = pet_energy_surf.get_rect()
                pet_energy_rect.midleft = (345, 57)
                screen.blit(pet_energy_window.surf, pet_energy_window.rect)
                screen.blit(pet_energy_surf, pet_energy_rect)
    except AttributeError:
        pass

    # player encounters Nede for Celeste's quest
    if pygame.sprite.collide_rect(player, nede) and player.quest_progress["where's nede?"] < 1:
        interaction_popup.update(nede.x_coordinate, nede.y_coordinate - 25,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("nede"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (nede.x_coordinate, nede.y_coordinate - 25)
        screen.blit(interaction_info_surf, interaction_info_rect)
        if player.quest_status["where's nede?"]:
            if not nede_ghoul_defeated:
                info_text_1 = "Nede is concerned about the ghoul."
                info_text_2 = "You must defeat it!"
                interacted = False
            else:
                info_text_1 = "Press 'F' key to pet Nede."
                if interacted and in_over_world:
                    pygame.mixer.find_channel(True).play(sfx_nede)
                    if player.quest_progress["where's nede?"] < 1:
                        player.quest_progress["where's nede?"] += 1
                        info_text_2 = "You pet Nede. He seems calm now. "
                        info_text_3 = "Nede heads back towards Seldon. "
                        nede.update(809, 390, graphic_dict["nede_left"])
                        interacted = False
                    else:
                        info_text_1 = "Nede's already been found."
                        interacted = False
        else:
            info_text_1 = "What a nice dog!"
            interacted = False
    # player collides with enemy ghoul for nede's quest
    if pygame.sprite.collide_rect(player, ghoul_nede):
        if not nede_ghoul_defeated:
            if player.quest_status["where's nede?"]:
                interaction_popup.update(ghoul_nede.x_coordinate, ghoul_nede.y_coordinate - 40,
                                         graphic_dict["popup_interaction_red"])
                screen.blit(interaction_popup.surf, interaction_popup.rect)
                interaction_info_surf = font.render(str(ghoul_nede.kind) + " lvl " +
                                                    str(ghoul_nede.level), True, "black",
                                                    (255, 204, 203))
                interaction_info_rect = interaction_info_surf.get_rect()
                interaction_info_rect.center = (ghoul_nede.x_coordinate, ghoul_nede.y_coordinate - 40)
                screen.blit(interaction_info_surf, interaction_info_rect)
                # lets player know if they are in range of enemy they can press f to attack it
                info_text_1 = "Press 'F' key to attack enemy."
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""
                if interacted and in_over_world:
                    current_enemy_battling = ghoul_nede
                    in_over_world = False
                    in_battle = True

                    drawing_functions.loot_popup_container.clear()
                    drawing_functions.loot_text_container.clear()
                    combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                            sharp_sense_active, graphic_dict)
                    combat_scenario.battle_animation_enemy(current_enemy_battling, snake_battle_sprite,
                                                           ghoul_battle_sprite,
                                                           chorizon_battle_sprite, muchador_battle_sprite,
                                                           magmon_battle_sprite, bandile_battle_sprite,
                                                           chinzilla_battle_sprite, in_battle, in_npc_interaction,
                                                           graphic_dict, necrola_battle_sprite,
                                                           osodark_battle_sprite, stelli_battle_sprite,
                                                           False, stelli_battle_sprite, 0)
            else:
                if not player.quest_complete["where's nede?"]:
                    interaction_popup.update(ghoul_nede.x_coordinate, ghoul_nede.y_coordinate - 40,
                                             graphic_dict["popup_interaction_red"])
                    screen.blit(interaction_popup.surf, interaction_popup.rect)
                    interaction_info_surf = font.render(str(ghoul_nede.kind) + " lvl " +
                                                        str(ghoul_nede.level), True, "black",
                                                        (255, 204, 203))
                    interaction_info_rect = interaction_info_surf.get_rect()
                    interaction_info_rect.center = (ghoul_nede.x_coordinate,
                                                    ghoul_nede.y_coordinate - 40)
                    screen.blit(interaction_info_surf, interaction_info_rect)

                    info_text_1 = "What's a ghoul doing here?"
                    interacted = False
    # player collides with stardust inn entrance
    if pygame.sprite.collide_rect(player, stardust_entrance):
        interaction_popup.update(stardust_entrance.x_coordinate, stardust_entrance.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("stardust post"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (stardust_entrance.x_coordinate,
                                        stardust_entrance.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        # lets player know if they are in range of building they can press f to enter it
        info_text_1 = "Press 'F' key to enter building."
        info_text_2 = ""

        if interacted:
            pygame.mixer.find_channel(True).play(sfx_door)
            current_building_entering = stardust_entrance
            movement_able = False
            in_over_world = False
            in_shop = True

    if pygame.sprite.collide_rect(player, rock):
        interaction_popup.update(rock.x_coordinate, rock.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("rock"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rock.x_coordinate, rock.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            try:
                if player.equipment["gloves"].name == "power gloves":
                    if rock.x_coordinate == 675:
                        rock.update(rock.x_coordinate - 110, rock.y_coordinate, graphic_dict["rock_small"])
                        if not rock_3_con:
                            pygame.mixer.find_channel(True).play(sfx_rupee)
                            player.rupees += 10
                            rock_3_con = True
                            info_text_1 = "You found 10 Rupees under the rock!"
                            info_text_2 = ""
                else:
                    info_text_1 = "The rock won't budge."
                    info_text_2 = ""
            except AttributeError:
                info_text_1 = "The rock won't budge."
                info_text_2 = ""
                pass
            interacted = False

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    stelli = pygame.sprite.spritecollideany(player, stellis, pygame.sprite.collide_rect_ratio(0.75))
    if stelli:
        interaction_popup.update(stelli.x_coordinate, stelli.y_coordinate - 40, graphic_dict["popup_interaction_red"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(stelli.name) + " lvl " + str(stelli.level), True, "black",
                                            (255, 204, 203))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (stelli.x_coordinate, stelli.y_coordinate - 40)
        screen.blit(interaction_info_surf, interaction_info_rect)

        # lets player know if they are in range of enemy they can press f to attack it
        info_text_1 = "Press 'F' key to train with stelli."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            current_enemy_battling = stelli
            in_over_world = False
            in_battle = True

            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            drawing_functions.outpost_window.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                    sharp_sense_active, graphic_dict)
            combat_scenario.battle_animation_enemy(current_enemy_battling, snake_battle_sprite, ghoul_battle_sprite,
                                                   chorizon_battle_sprite, muchador_battle_sprite,
                                                   magmon_battle_sprite, bandile_battle_sprite,
                                                   chinzilla_battle_sprite, in_battle, in_npc_interaction,
                                                   graphic_dict, necrola_battle_sprite,
                                                   osodark_battle_sprite, stelli_battle_sprite,
                                                   False, stelli_battle_sprite, 0)

    if not fishing:
        if pygame.sprite.collide_rect(player, fishing_spot_1):
            interaction_popup.update(fishing_spot_1.x_coordinate, fishing_spot_1.y_coordinate - 50,
                                     graphic_dict["popup_interaction_blue"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("fishing spot"), True, "black", "light blue")
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
                    if item.name == "seldon bait":
                        fishing = True
                        interacted = False
                        fishing_timer = time.perf_counter()
                        player.items.remove(item)
                        previous_surf = player.surf
                        fish_caught = False
                        break

        if pygame.sprite.collide_rect(player, fishing_spot_2):
            interaction_popup.update(fishing_spot_2.x_coordinate, fishing_spot_2.y_coordinate - 50,
                                     graphic_dict["popup_interaction_blue"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("fishing spot"), True, "black", "light blue")
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

            # if player interacts with fishing spot and has it unlocked and has bait, use bait and start
            if interacted and in_over_world and fishing_unlocked:
                for item in player.items:
                    if item.name == "seldon bait":
                        fishing = True
                        interacted = False
                        fishing_timer = time.perf_counter()
                        player.items.remove(item)
                        previous_surf = player.surf
                        fish_caught = False
                        break

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)
    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])
    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)
    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2,
                                     info_text_3, info_text_4, in_over_world, basic_fish_counter, better_fish_counter,
                                     even_better_fish_counter, best_fish_counter)
    drawing_functions.draw_it(screen)

    if len(drawing_functions.outpost_window) > 0:
        for outpost_item in drawing_functions.outpost_window:
            screen.blit(outpost_item.surf, outpost_item.rect)

    # move player to seldon district when they approach nascent grove exit
    if player.x_coordinate > 925 and 175 < player.y_coordinate < 300:
        player.current_zone = "seldon"
        stardust_song_set = False
        in_over_world = True
        level_checked = False
        player.x_coordinate = 125
        player.y_coordinate = 375

    # nede movement updates
    if player.quest_status["where's nede?"]:
        if player.quest_progress["where's nede?"] < 1:
            face_direction = random.choice(["left", "right"])
            if movement_able and in_over_world:
                npc_toc = time.perf_counter()
                if npc_toc - npc_tic > 2:
                    npc_tic = time.perf_counter()
                    if face_direction == "left":
                        nede.update(nede.x_coordinate, nede.y_coordinate,
                                    graphic_dict["nede_high_left"])
                    if face_direction == "right":
                        nede.update(nede.x_coordinate, nede.y_coordinate,
                                    graphic_dict["nede_high_right"])
        else:
            if not player.quest_complete["where's nede?"]:
                if outpost_show:
                    drawing_functions.outpost_window.append(outpost_notify)
                    outpost_show = False

    else:
        if player.quest_progress["where's nede?"] < 1:
            face_direction = random.choice(["left", "right"])
            if movement_able and in_over_world:
                npc_toc = time.perf_counter()
                if npc_toc - npc_tic > 2:
                    npc_tic = time.perf_counter()
                    if face_direction == "left":
                        nede.update(nede.x_coordinate, nede.y_coordinate, graphic_dict["nede_left"])
                    if face_direction == "right":
                        nede.update(nede.x_coordinate, nede.y_coordinate, graphic_dict["nede_right"])

    stardust_return = {"stardust_song_set": stardust_song_set, "nede_sprite_reset": nede_sprite_reset,
                       "current_enemy_battling": current_enemy_battling, "in_battle": in_battle, "in_over_world":
                           in_over_world, "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3":
                           info_text_3, "info_text_4": info_text_4, "movement_able": movement_able,
                       "current_building_entering": current_building_entering, "in_shop": in_shop,
                       "interacted": interacted, "npc_tic": npc_tic, "rock_3_con": rock_3_con,
                       "outpost_show": outpost_show, "enemy_tic": enemy_tic, "level_checked": level_checked,
                       "fishing": fishing, "fishing_timer": fishing_timer, "previous_surf": previous_surf,
                       "fish_caught": fish_caught, "basic_fish_counter": basic_fish_counter, "better_fish_counter":
                       better_fish_counter, "even_better_fish_counter": even_better_fish_counter,
                       "best_fish_counter": best_fish_counter}

    return stardust_return
