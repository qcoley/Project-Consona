import random
import time

import drawing_functions
import combat_scenario
import gameplay_functions


def ectrenos_main(pygame, screen, graphic_dict, player, ectrenos_bg, eldream_building_music, over_world_song_set,
                  interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                  button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
                  info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle, movement_able,
                  current_enemy_battling, quest_star_garan, quest_star_maurelle, quest_star_celeste, quest_star_torune,
                  star_voruke, star_zerah, star_apothecary, terra_mountains, terra_cave, npc_dionte, quest_star_dionte,
                  enemy, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                  muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                  barrier_active, sharp_sense_active, current_npc_interacting, chinzilla, star_dionte, hearth_stone,
                  equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, rock_7,
                  rock_7_con, chinzilla_defeated, eldream_gate_rect, eldream_attuned, in_shop, in_inn,
                  current_building_entering, enemy_tic, eldream_flowers, seldon_enemies, korlok_enemies, snakes, ghouls,
                  magmons, bandiles, interactables_seldon, interactables_korlok, interactables_mines, Enemy, Item,
                  UiElement, seldon_flowers, interactables_ectrenos, ectrenos_entrance, ectrene, ladder,
                  quest_star_leyre, pet_energy_window, chroma_bridge):

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

    if not player.quest_complete["hatch 'em all"]:
        screen.blit(quest_star_leyre.surf, quest_star_leyre.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
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
            interacted = False
            chroma_bridge.update(764, 487, graphic_dict["chroma_bridge"])
            player.current_zone = "ectrenos alcove"
            player.x_coordinate = 425
            player.y_coordinate = 675
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
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
                  current_enemy_battling, quest_star_garan, quest_star_maurelle, quest_star_celeste, quest_star_torune,
                  star_voruke, star_zerah, star_apothecary, terra_mountains, terra_cave, npc_dionte, quest_star_dionte,
                  enemy, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                  muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                  barrier_active, sharp_sense_active, current_npc_interacting, chinzilla, star_dionte, hearth_stone,
                  equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, rock_7,
                  rock_7_con, chinzilla_defeated, eldream_gate_rect, eldream_attuned, in_shop, in_inn,
                  current_building_entering, enemy_tic, eldream_flowers, seldon_enemies, korlok_enemies, snakes, ghouls,
                  magmons, bandiles, interactables_seldon, interactables_korlok, interactables_mines, Enemy, Item,
                  UiElement, seldon_flowers, interactables_ectrenos, ectrenos_entrance, ectrene, ectrenos_pet_entrance,
                  in_menagerie, quest_star_aitor, pet_energy_window):
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

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
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

    screen.blit(player.surf, player.rect)

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

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
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
                   over_world_song_set,
                   interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                   button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
                   info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle, movement_able,
                   current_enemy_battling, quest_star_garan, quest_star_maurelle, quest_star_celeste, quest_star_torune,
                   star_voruke, star_zerah, star_apothecary, terra_mountains, terra_cave, npc_dionte, quest_star_dionte,
                   enemy, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                   muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                   barrier_active, sharp_sense_active, current_npc_interacting, chinzilla, star_dionte, hearth_stone,
                   equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, rock_7,
                   rock_7_con, chinzilla_defeated, eldream_gate_rect, eldream_attuned, in_shop, in_inn,
                   current_building_entering, enemy_tic, eldream_flowers, seldon_enemies, korlok_enemies, snakes,
                   ghouls,
                   magmons, bandiles, interactables_seldon, interactables_korlok, interactables_mines, Enemy, Item,
                   UiElement, seldon_flowers, interactables_ectrenos, ectrenos_entrance, ectrene,
                   ectrenos_shop_entrance, ectrenos_inn_entrance, pet_energy_window):
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

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
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

    screen.blit(player.surf, player.rect)

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

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
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
                   current_enemy_battling, quest_star_garan, quest_star_maurelle, quest_star_celeste, quest_star_torune,
                   star_voruke, star_zerah, star_apothecary, terra_mountains, terra_cave, npc_dionte, quest_star_dionte,
                   enemy, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                   muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                   barrier_active, sharp_sense_active, current_npc_interacting, chinzilla, star_dionte, hearth_stone,
                   equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, rock_7,
                   rock_7_con, chinzilla_defeated, eldream_gate_rect, eldream_attuned, in_shop, in_inn,
                   current_building_entering, enemy_tic, eldream_flowers, seldon_enemies, korlok_enemies, snakes,
                   ghouls, magmons, bandiles, interactables_seldon, interactables_korlok, interactables_mines, Enemy,
                   Item, UiElement, seldon_flowers, interactables_ectrenos, ectrenos_entrance, ectrene,
                   quest_star_everett, pet_energy_window):

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

    if not player.quest_complete["hatch 'em all"]:
        screen.blit(quest_star_everett.surf, quest_star_everett.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
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

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
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

    if 85 > player.x_coordinate and player.y_coordinate < 335:
        player.current_zone = "ectrenos left"
        in_over_world = True
        player.x_coordinate = 850
        player.y_coordinate = 530
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
    if 920 < player.x_coordinate and player.y_coordinate < 335:
        player.current_zone = "ectrenos right"
        in_over_world = True
        player.x_coordinate = 210
        player.y_coordinate = 515
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

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
                    over_world_song_set,
                    interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                    button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
                    info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle, movement_able,
                    current_enemy_battling, quest_star_garan, quest_star_maurelle, quest_star_celeste,
                    quest_star_torune,
                    star_voruke, star_zerah, star_apothecary, terra_mountains, terra_cave, npc_dionte,
                    quest_star_dionte,
                    enemy, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                    muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                    barrier_active, sharp_sense_active, current_npc_interacting, chinzilla, star_dionte, hearth_stone,
                    equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, rock_7,
                    rock_7_con, chinzilla_defeated, eldream_gate_rect, eldream_attuned, in_shop, in_inn,
                    current_building_entering, enemy_tic, eldream_flowers, seldon_enemies, korlok_enemies, snakes,
                    ghouls,
                    magmons, bandiles, interactables_seldon, interactables_korlok, interactables_mines, Enemy, Item,
                    UiElement, seldon_flowers, interactables_ectrenos, ectrenos_entrance, ectrene,
                    pet_energy_window, ladder, chroma_bridge):

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

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
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
            interacted = False
            chroma_bridge.update(477, 493, graphic_dict["chroma_bridge"])
            player.current_zone = "ectrenos"
            player.x_coordinate = 525
            player.y_coordinate = 648
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
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
