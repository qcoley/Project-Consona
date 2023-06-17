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
                  chinzilla_battle_sprite, barrier_active, sharp_sense_active, current_npc_interacting, hearth_stone,
                  equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select,
                  eldream_attuned, in_shop, in_inn, current_building_entering, enemy_tic, eldream_flowers,
                  interactables_ectrenos, ectrene, ladder, quest_star_leyre, pet_energy_window, chroma_bridge,
                  npc_leyre, necrola_battle_sprite, osodark_battle_sprite, sfx_ladder, stelli_battle_sprite):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(eldream_building_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(ectrenos_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if not player.quest_status["las escondidas"] or player.quest_progress["las escondidas"] == 4:
        if not player.quest_complete["las escondidas"]:
            screen.blit(quest_star_leyre.surf, quest_star_leyre.rect)
    if not player.quest_status["las escondidas"] or player.quest_progress["las escondidas"] == 4:
        npc_leyre.update_position(682, 420)
        screen.blit(npc_leyre.surf, npc_leyre.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
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
                combat_scenario.resting_animation(player, npc_leyre, player_battle_sprite, snake_battle_sprite,
                                                  ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite,
                                                  magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                                                  barrier_active, sharp_sense_active, in_battle, in_npc_interaction,
                                                  graphic_dict, necrola_battle_sprite, osodark_battle_sprite,
                                                  stelli_battle_sprite)

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
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if button_highlighted:
        screen.blit(button_highlight.surf, button_highlight.rect)

    if 380 < player.x_coordinate < 650 and player.y_coordinate > 700:
        player.current_zone = "eldream"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 540
        player.y_coordinate = 565
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
        hearth_stone.update(968, 595, graphic_dict["hearth_stone"])

    if player.x_coordinate < 35 and 565 > player.y_coordinate > 470:
        player.current_zone = "ectrenos left"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 850
        player.y_coordinate = 530
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if player.x_coordinate > 995 and 570 > player.y_coordinate > 470:
        player.current_zone = "ectrenos right"
        in_over_world = True
        over_world_song_set = False
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
                npc_leyre.update(graphic_dict["leyre_down"])
            if face_direction == "back":
                npc_leyre.update(graphic_dict["leyre_up"])
            if face_direction == "left":
                npc_leyre.update(graphic_dict["leyre_left"])
            if face_direction == "right":
                npc_leyre.update(graphic_dict["leyre_right"])

    ectrenos_main_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic, "info_text_1": info_text_1,
                            "info_text_2": info_text_2, "info_text_3": info_text_3, "info_text_4": info_text_4,
                            "interacted": interacted, "in_over_world": in_over_world, "in_battle": in_battle,
                            "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                            "current_enemy_battling": current_enemy_battling,
                            "current_npc_interacting": current_npc_interacting, "eldream_attuned": eldream_attuned,
                            "in_shop": in_shop, "in_inn": in_inn,
                            "current_building_entering": current_building_entering,
                            "enemy_tic": enemy_tic, "eldream_flowers": eldream_flowers,
                            "interactables_ectrenos": interactables_ectrenos}

    return ectrenos_main_return


def ectrenos_left(pygame, screen, graphic_dict, player, ectrenos_left_bg, eldream_overworld_music, over_world_song_set,
                  interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                  button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
                  info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle, movement_able,
                  current_enemy_battling, current_npc_interacting, equipment_screen, staff, sword, bow, npc_garan,
                  offense_meter, defense_meter, weapon_select, eldream_attuned, in_shop, in_inn,
                  current_building_entering, enemy_tic, eldream_flowers, interactables_ectrenos, ectrenos_pet_entrance,
                  in_menagerie, quest_star_aitor, pet_energy_window, npc_leyre, sfx_find):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(eldream_overworld_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(ectrenos_left_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if not player.quest_complete["hatch 'em all"]:
        screen.blit(quest_star_aitor.surf, quest_star_aitor.rect)

    if player.quest_progress["las escondidas"] == 0 and player.quest_status["las escondidas"]:
        npc_leyre.update_position(626, 355)
        screen.blit(npc_leyre.surf, npc_leyre.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
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

    if pygame.Rect.colliderect(player.rect, ectrenos_pet_entrance):
        interaction_popup.update(816, 178, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("menagerie"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (816, 178)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter menagerie."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            movement_able = False
            in_over_world = False
            over_world_song_set = False
            in_menagerie = True

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
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if button_highlighted:
        screen.blit(button_highlight.surf, button_highlight.rect)

    if 990 < player.x_coordinate and 395 < player.y_coordinate < 625:
        player.current_zone = "ectrenos"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 80
        player.y_coordinate = 515
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
    if 660 < player.x_coordinate < 975 and 675 < player.y_coordinate:
        player.current_zone = "ectrenos front"
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
                            "interactables_ectrenos": interactables_ectrenos, "in_menagerie": in_menagerie}

    return ectrenos_left_return


def ectrenos_right(pygame, screen, graphic_dict, player, ectrenos_right_bg, eldream_overworld_music,
                   over_world_song_set, interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                   hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted, info_text_1,
                   info_text_2, info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle, movement_able,
                   current_enemy_battling, current_npc_interacting, equipment_screen, staff, sword, bow, npc_garan,
                   offense_meter, defense_meter, weapon_select, eldream_attuned, in_shop, in_inn,
                   current_building_entering, enemy_tic, eldream_flowers, interactables_ectrenos,
                   ectrenos_shop_entrance, ectrenos_inn_entrance, pet_energy_window, npc_leyre, sfx_find):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(eldream_overworld_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(ectrenos_right_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if player.quest_progress["las escondidas"] == 1 and player.quest_status["las escondidas"]:
        npc_leyre.update_position(722, 350)
        screen.blit(npc_leyre.surf, npc_leyre.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
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

    if pygame.Rect.colliderect(player.rect, ectrenos_shop_entrance):
        interaction_popup.update(217, 178, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("shop"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (217, 178)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter shop."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            movement_able = False
            in_over_world = False
            over_world_song_set = False
            in_shop = True

    if pygame.Rect.colliderect(player.rect, ectrenos_inn_entrance):
        interaction_popup.update(875, 275, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("inn"), True, "black", "light yellow")
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
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if button_highlighted:
        screen.blit(button_highlight.surf, button_highlight.rect)

    if 50 > player.x_coordinate and 400 < player.y_coordinate < 620:
        player.current_zone = "ectrenos"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 958
        player.y_coordinate = 525
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if 50 < player.x_coordinate < 375 and 675 < player.y_coordinate:
        player.current_zone = "ectrenos front"
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
                             "interactables_ectrenos": interactables_ectrenos}

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
                   sfx_find, stelli_battle_sprite):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(eldream_overworld_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(ectrenos_front_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    respawned_dict = gameplay_functions.enemy_respawn(player, seldon_enemies, korlok_enemies, snakes, ghouls, magmons,
                                                      bandiles, interactables_seldon, interactables_korlok,
                                                      interactables_mines, Enemy, Item, graphic_dict, UiElement,
                                                      seldon_flowers, eldream_flowers, interactables_eldream,
                                                      ectrenos_front_enemies)
    ectrenos_front_enemies = respawned_dict["ectrenos_front_enemies"]

    for enemy_sprite in ectrenos_front_enemies:  # update enemy sprite to a highlighted version
        if not player.quest_complete["shades of fear"]:
            if player.quest_status["shades of fear"]:
                enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                          graphic_dict["necrola_high"])
    for enemy_sprite in ectrenos_front_enemies:
        if player.quest_complete["shades of fear"]:
            enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate, graphic_dict["necrola"])

    for enemy in ectrenos_front_enemies:
        screen.blit(enemy.surf, enemy.rect)

    if not player.quest_complete["shades of fear"]:
        screen.blit(quest_star_everett.surf, quest_star_everett.rect)
    screen.blit(npc_everett.surf, npc_everett.rect)

    if player.quest_progress["las escondidas"] == 2 and player.quest_status["las escondidas"]:
        npc_leyre.update_position(828, 532)
        screen.blit(npc_leyre.surf, npc_leyre.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
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
            combat_scenario.resting_animation(player, enemy, player_battle_sprite, snake_battle_sprite,
                                              ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite,
                                              magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                                              barrier_active, sharp_sense_active, in_battle, in_npc_interaction,
                                              graphic_dict, necrola_battle_sprite, osodark_battle_sprite,
                                              stelli_battle_sprite)

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
            combat_scenario.resting_animation(player, enemy, player_battle_sprite, snake_battle_sprite,
                                              ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite,
                                              magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                                              barrier_active, sharp_sense_active, in_battle, in_npc_interaction,
                                              graphic_dict, necrola_battle_sprite, osodark_battle_sprite,
                                              stelli_battle_sprite)

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
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if button_highlighted:
        screen.blit(button_highlight.surf, button_highlight.rect)

    if 85 > player.x_coordinate and player.y_coordinate < 375:
        player.current_zone = "ectrenos left"
        in_over_world = True
        player.x_coordinate = 850
        player.y_coordinate = 530
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
    if 920 < player.x_coordinate and player.y_coordinate < 375:
        player.current_zone = "ectrenos right"
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
        if enemy_toc - enemy_tic > 2:
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
                             "interactables_ectrenos": interactables_ectrenos}

    return ectrenos_front_return


def ectrenos_alcove(pygame, screen, graphic_dict, player, ectrenos_alcove_bg, eldream_building_music,
                    over_world_song_set, interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                    hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                    info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle,
                    movement_able, current_enemy_battling, current_npc_interacting, equipment_screen, staff, sword, bow,
                    npc_garan, offense_meter, defense_meter, weapon_select, eldream_attuned, in_shop, in_inn,
                    current_building_entering, enemy_tic, eldream_flowers, interactables_ectrenos,
                    pet_energy_window, ladder, chroma_bridge, alcove_star, npc_leyre, enemies, sfx_find, sfx_ladder):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(eldream_building_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(ectrenos_alcove_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if player.quest_progress["las escondidas"] == 3 and player.quest_status["las escondidas"]:
        npc_leyre.update_position(967, 530)
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
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if button_highlighted:
        screen.blit(button_highlight.surf, button_highlight.rect)

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
    direction_horizontal = random.choice(["left", "right"])
    direction_vertical = random.choice(["up", "down"])
    move_mon = random.choice(enemies.sprites())
    if movement_able and in_over_world:
        enemy_toc = time.perf_counter()
        if enemy_toc - enemy_tic > 2:
            enemy_tic = time.perf_counter()
            move_mon.update_position([200, 700], [100, 300], direction_horizontal, direction_vertical)

    ectrenos_alcove_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                              "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                              "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                              "in_battle": in_battle, "in_npc_interaction": in_npc_interaction,
                              "movement_able": movement_able, "current_enemy_battling": current_enemy_battling,
                              "current_npc_interacting": current_npc_interacting, "eldream_attuned": eldream_attuned,
                              "in_shop": in_shop, "in_inn": in_inn,
                              "current_building_entering": current_building_entering, "enemy_tic": enemy_tic,
                              "eldream_flowers": eldream_flowers, "interactables_ectrenos": interactables_ectrenos}

    return ectrenos_alcove_return
