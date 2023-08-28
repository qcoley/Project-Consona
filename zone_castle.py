import time
import random
import drawing_functions
import gameplay_functions
import combat_scenario


def castle_one(pygame, screen, graphic_dict, player, castle_one_bg, over_world_song_set, castle_music,
               interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
               button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
               info_text_3, info_text_4, npc_tic, movement_able, equipment_screen, staff, sword, bow, npc_garan,
               offense_meter, defense_meter, weapon_select, pet_energy_window, artherian, player_battle_sprite,
               current_npc_interacting, in_npc_interaction, hearth_stone, marrow_attuned, sfx_hearth,
               marrow_ghouls, enemy_tic, barrier_active, sharp_sense_active, ghoul_battle_sprite, in_battle,
               current_enemy_battling, Enemy, Item, UiElement, artherian_star, noren, boro, maydria, npcs,
               maydria_star, sub_marrow_ladder, sfx_ladder, vanished, vanish_overlay, basic_fish_counter,
               better_fish_counter, even_better_fish_counter, best_fish_counter, castle_bridge, prism_activate,
               prism_tic, sfx_chroma, castle_exit, chandelier, crate_1, crate_2, castle_crate_1_got,
               castle_crate_2_got, sfx_item_potion):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(castle_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(castle_one_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if not castle_crate_1_got:
        screen.blit(crate_1.surf, crate_1.rect)
    if not castle_crate_2_got:
        screen.blit(crate_2.surf, crate_2.rect)

    respawned_dict = gameplay_functions.enemy_respawn(player, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, Enemy, Item, graphic_dict,
                                                      UiElement, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, marrow_ghouls, marrow_ghouls)
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

    screen.blit(chandelier.surf, chandelier.rect)

    if pygame.sprite.collide_rect(player, crate_1):
        if not castle_crate_1_got:
            interaction_popup.update(crate_1.x_coordinate, crate_1.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_1.x_coordinate, crate_1.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not castle_crate_1_got:
                    if len(player.items) < 16:
                        castle_crate_1_got = True
                        pygame.mixer.find_channel(True).play(sfx_item_potion)
                        info_text_1 = "You found a health potion!"
                        info_text_2 = ""
                        player.items.append(Item("small health potion", "potion", 200, 200,
                                                 graphic_dict["health_pot_img"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""

            interacted = False

    if pygame.sprite.collide_rect(player, crate_2):
        if not castle_crate_2_got:
            interaction_popup.update(crate_2.x_coordinate, crate_2.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_2.x_coordinate, crate_2.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not castle_crate_2_got:
                    if len(player.items) < 16:
                        castle_crate_2_got = True
                        pygame.mixer.find_channel(True).play(sfx_item_potion)
                        info_text_1 = "You found an energy potion!"
                        info_text_2 = ""
                        player.items.append(Item("small energy potion", "potion", 200, 200,
                                                 graphic_dict["energy_pot_img"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""

            interacted = False

    if pygame.Rect.colliderect(player.rect, castle_exit):
        interaction_popup.update(515, 25, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Marrow"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (515, 25)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to exit castle."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            over_world_song_set = False
            player.current_zone = "marrow"
            player.x_coordinate = 710
            player.y_coordinate = 525
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

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

    if player.x_coordinate < 35 and player.y_coordinate > 560:
        player.current_zone = "castle two"
        in_over_world = True
        player.x_coordinate = 860
        player.y_coordinate = 640
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    castle_one_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                         "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                         "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                         "movement_able": movement_able, "current_npc_interacting": current_npc_interacting,
                         "in_npc_interaction": in_npc_interaction, "marrow_attuned": marrow_attuned,
                         "enemy_tic": enemy_tic, "in_battle": in_battle, "current_enemy": current_enemy_battling,
                         "marrow_ghouls": marrow_ghouls, "prism_tic": prism_tic,
                         "castle_crate_1_got": castle_crate_1_got, "castle_crate_2_got": castle_crate_2_got}

    return castle_one_return


def castle_two(pygame, screen, graphic_dict, player, castle_two_bg, over_world_song_set, castle_music,
               interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
               button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
               info_text_3, info_text_4, npc_tic, movement_able, equipment_screen, staff, sword, bow, npc_garan,
               offense_meter, defense_meter, weapon_select, pet_energy_window, artherian, player_battle_sprite,
               current_npc_interacting, in_npc_interaction, hearth_stone, marrow_attuned, sfx_hearth,
               marrow_ghouls, enemy_tic, barrier_active, sharp_sense_active, ghoul_battle_sprite, in_battle,
               current_enemy_battling, Enemy, Item, UiElement, artherian_star, noren, boro, maydria, npcs,
               maydria_star, sub_marrow_ladder, sfx_ladder, vanished, vanish_overlay, basic_fish_counter,
               better_fish_counter, even_better_fish_counter, best_fish_counter, castle_bridge, prism_activate,
               prism_tic, sfx_chroma, castle_exit, chandelier, crate_1, crate_2, rock_1, rock_2, sfx_rocks):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(castle_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(castle_two_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    respawned_dict = gameplay_functions.enemy_respawn(player, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, Enemy, Item, graphic_dict,
                                                      UiElement, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, marrow_ghouls, marrow_ghouls)

    screen.blit(rock_1.surf, rock_1.rect)
    screen.blit(rock_2.surf, rock_2.rect)

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

    if pygame.sprite.collide_rect(player, rock_1):
        interaction_popup.update(rock_1.x_coordinate, rock_1.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("rock"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rock_1.x_coordinate, rock_1.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            try:
                if player.equipment["gloves"].name == "power gloves":
                    if rock_1.y_coordinate == 275:
                        pygame.mixer.find_channel(True).play(sfx_rocks)
                        rock_1.update(rock_1.x_coordinate, rock_1.y_coordinate - 275, graphic_dict["rock"])
                else:
                    info_text_1 = "The rock won't budge."
                    info_text_2 = ""
            except AttributeError:
                info_text_1 = "The rock won't budge."
                info_text_2 = ""
                pass
            interacted = False

    if pygame.sprite.collide_rect(player, rock_2):
        interaction_popup.update(rock_2.x_coordinate, rock_2.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("rock"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rock_2.x_coordinate, rock_2.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            try:
                if player.equipment["gloves"].name == "power gloves":
                    if rock_2.y_coordinate == 275:
                        pygame.mixer.find_channel(True).play(sfx_rocks)
                        rock_2.update(rock_2.x_coordinate, rock_2.y_coordinate - 275, graphic_dict["rock"])
                else:
                    info_text_1 = "The rock won't budge."
                    info_text_2 = ""
            except AttributeError:
                info_text_1 = "The rock won't budge."
                info_text_2 = ""
                pass
            interacted = False

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

    if player.x_coordinate > 975 and player.y_coordinate > 560:
        player.current_zone = "castle one"
        in_over_world = True
        player.x_coordinate = 115
        player.y_coordinate = 600
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    castle_two_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                         "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                         "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                         "movement_able": movement_able, "current_npc_interacting": current_npc_interacting,
                         "in_npc_interaction": in_npc_interaction, "marrow_attuned": marrow_attuned,
                         "enemy_tic": enemy_tic, "in_battle": in_battle, "current_enemy": current_enemy_battling,
                         "marrow_ghouls": marrow_ghouls, "prism_tic": prism_tic}

    return castle_two_return
