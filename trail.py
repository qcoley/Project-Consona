import random
import time

import drawing_functions
import combat_scenario
import gameplay_functions


def terra_trail(pygame, screen, graphic_dict, player, mountain_trail_bg, korlok_overworld_music, over_world_song_set,
                interaction_popup, font, save_check_window, user_interface, world_map_container, bar_backdrop,
                hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted, info_text_1,
                info_text_2, info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle, movement_able,
                current_enemy_battling, quest_star_garan, quest_star_maurelle, quest_star_celeste, quest_star_torune,
                star_voruke, star_zerah, star_apothecary, terra_mountains, terra_cave, npc_dionte, quest_star_dionte,
                enemy, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                barrier_active, sharp_sense_active, current_npc_interacting, chinzilla, star_dionte, hearth_stone,
                equipment_screen):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(korlok_overworld_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(mountain_trail_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(terra_mountains.surf, terra_mountains.rect)
    screen.blit(terra_cave.surf, terra_cave.rect)
    screen.blit(npc_dionte.surf, npc_dionte.rect)
    if not player.quest_complete["it's dangerous to go alone"]:
        screen.blit(quest_star_dionte.surf, quest_star_dionte.rect)

    gameplay_functions.npc_quest_star_updates(screen, player, quest_star_garan, quest_star_maurelle, quest_star_celeste,
                                              quest_star_torune, graphic_dict["quest_progress_star"],
                                              graphic_dict["quest_complete_star"], star_voruke, star_zerah,
                                              star_apothecary, star_dionte)
    screen.blit(player.surf, player.rect)

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
            combat_scenario.resting_animation(player, enemy, player_battle_sprite, snake_battle_sprite,
                                              ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite,
                                              magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                                              barrier_active, sharp_sense_active, in_battle, in_npc_interaction,
                                              graphic_dict)

    if pygame.sprite.collide_rect(player, terra_cave):
        interaction_popup.update(terra_cave.x_coordinate + 75, terra_cave.y_coordinate + 20,
                                 graphic_dict["popup_interaction_red"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(terra_cave.name), True, "black", (255, 204, 203))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (terra_cave.x_coordinate + 75, terra_cave.y_coordinate + 20)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter cave.."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            current_enemy_battling = chinzilla
            in_over_world = False
            in_battle = True

            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.resting_animation(player, chinzilla, player_battle_sprite, snake_battle_sprite,
                                              ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite,
                                              magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                                              barrier_active, sharp_sense_active, in_battle, in_npc_interaction,
                                              graphic_dict)

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        screen.blit(ui_elements.surf, ui_elements.rect)
    for maps in world_map_container:
        screen.blit(maps.surf, maps.rect)

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
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if button_highlighted:
        screen.blit(button_highlight.surf, button_highlight.rect)

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
                    "current_npc_interacting": current_npc_interacting}

    return trail_return

