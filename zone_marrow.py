import drawing_functions
import combat_scenario
import gameplay_functions


def marrow_entrance(pygame, screen, graphic_dict, player, marrow_entrance_bg, over_world_song_set, interaction_popup,
                    font, save_check_window, user_interface, bar_backdrop,
                    hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                    info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                    staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                    overlay_marrow_west, overlay_marrow_east):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        over_world_song_set = True

    screen.blit(marrow_entrance_bg, (0, 0))
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

    if pygame.Rect.colliderect(player.rect, overlay_marrow_west):
        interaction_popup.update(125, 220, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("West Ramparts"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (125, 220)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter Ramparts."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            over_world_song_set = False
            player.current_zone = "ectrenos"
            player.x_coordinate = 500
            player.y_coordinate = 675
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.Rect.colliderect(player.rect, overlay_marrow_east):
        interaction_popup.update(905, 220, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("East Ramparts"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (905, 220)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter Ramparts."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            over_world_song_set = False
            player.current_zone = "ectrenos"
            player.x_coordinate = 500
            player.y_coordinate = 675
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
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if button_highlighted:
        screen.blit(button_highlight.surf, button_highlight.rect)

    if 450 < player.x_coordinate < 550 and player.y_coordinate < 40:
        player.current_zone = "eldream"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 550
        player.y_coordinate = 690
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_entrance_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                              "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                              "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                              "movement_able": movement_able}

    return marrow_entrance_return
