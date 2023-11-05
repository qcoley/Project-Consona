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
                barrier_active, sharp_sense_active, current_npc_interacting, chinzilla, hearth_stone,
                equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, rock_7,
                rock_7_con, chinzilla_defeated, eldream_gate_rect, pet_energy_window, necrola_battle_sprite,
                osodark_battle_sprite, sfx_rupee, stelli_battle_sprite, apothis_music, scene_1, scene_2, scene_3,
                scene_4, scene_5, scene_6, scene_7, scene_8, skip_button, SCREEN_WIDTH, SCREEN_HEIGHT, game_window,
                dreth_cutscenes_not_viewed, dreth_0, vanished, vanish_overlay, critter, right_move, left_move,
                critter_tic, walk_move, basic_fish_counter, better_fish_counter, even_better_fish_counter,
                best_fish_counter):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(korlok_overworld_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(mountain_trail_bg, (0, 0))
    screen.blit(rock_7.surf, rock_7.rect)
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)
    screen.blit(terra_mountains.surf, terra_mountains.rect)
    screen.blit(terra_cave.surf, terra_cave.rect)
    screen.blit(npc_dionte.surf, npc_dionte.rect)

    if critter.x_coordinate < 1010:
        screen.blit(critter.surf, critter.rect)

    critter_toc = time.perf_counter()
    if critter_toc - critter_tic > 2:
        if right_move:
            if critter.x_coordinate < 1100:
                if walk_move and critter.x_coordinate % 9 == 0:
                    critter.update(critter.x_coordinate, critter.y_coordinate, graphic_dict["critter_side_right_walk"])
                    walk_move = False
                else:
                    if critter.x_coordinate % 9 == 0:
                        critter.update(critter.x_coordinate, critter.y_coordinate, graphic_dict["critter_side_right"])
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
            if critter.x_coordinate > 940:
                if walk_move and critter.x_coordinate % 9 == 0:
                    critter.update(critter.x_coordinate, critter.y_coordinate, graphic_dict["critter_side_left_walk"])
                    walk_move = False
                else:
                    if critter.x_coordinate % 9 == 0:
                        critter.update(critter.x_coordinate, critter.y_coordinate, graphic_dict["critter_side_left"])
                        walk_move = True
                critter.x_coordinate -= 1
            else:
                critter.update(critter.x_coordinate, critter.y_coordinate, graphic_dict["critter_front"])
                right_move = True
                left_move = False
                critter.x_coordinate += 1
                critter_tic = time.perf_counter()
            critter.rect = critter.surf.get_rect(center=(critter.x_coordinate, critter.y_coordinate))

    if not player.quest_complete["it's dangerous to go alone"]:
        screen.blit(quest_star_dionte.surf, quest_star_dionte.rect)
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
                                                    sharp_sense_active, graphic_dict)

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
                                                            sharp_sense_active, graphic_dict)
                    combat_scenario.battle_animation_enemy(current_enemy_battling, snake_battle_sprite,
                                                           ghoul_battle_sprite,
                                                           chorizon_battle_sprite, muchador_battle_sprite,
                                                           magmon_battle_sprite, bandile_battle_sprite,
                                                           chinzilla_battle_sprite, in_battle, in_npc_interaction,
                                                           graphic_dict, necrola_battle_sprite,
                                                           osodark_battle_sprite, stelli_battle_sprite,
                                                           False, stelli_battle_sprite, 0, stelli_battle_sprite,
                                                           stelli_battle_sprite, stelli_battle_sprite, False)

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
                        rock_7.update(rock_7.x_coordinate - 120, rock_7.y_coordinate, graphic_dict["rock_small"])
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
        interaction_popup.update(700, 25, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Eldream"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (700, 25,)
        screen.blit(interaction_info_surf, interaction_info_rect)
        if player.quest_complete["it's dangerous to go alone"]:
            info_text_1 = "Press 'F' key to enter Eldream."
            info_text_2 = ""

        if interacted:
            if player.quest_complete["it's dangerous to go alone"]:
                interacted = False
                over_world_song_set = False
                player.current_zone = "eldream"
                player.x_coordinate = 255
                player.y_coordinate = 175
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                hearth_stone.update(968, 595, graphic_dict["hearth_stone"])
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
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world, basic_fish_counter, better_fish_counter, even_better_fish_counter,
                                     best_fish_counter)
    drawing_functions.draw_it(screen)

    if player.x_coordinate < 75 and player.y_coordinate < 225:
        player.current_zone = "korlok"
        in_over_world = True
        player.x_coordinate = 900
        player.y_coordinate = 175
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
        hearth_stone.update(885, 230, graphic_dict["hearth_stone"])

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
                    "left_move": left_move, "critter_tic": critter_tic, "walk_move": walk_move}

    return trail_return
