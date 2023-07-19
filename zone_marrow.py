import drawing_functions
import combat_scenario
import random
import time


def marrow_district(pygame, screen, graphic_dict, player, marrow_bg, over_world_song_set, marrow_music,
                    interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                    button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
                    info_text_3, info_text_4, npc_tic, movement_able, equipment_screen, staff, sword, bow, npc_garan,
                    offense_meter, defense_meter, weapon_select, pet_energy_window):
    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(marrow_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(marrow_bg, (0, 0))
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

    if player.y_coordinate <= 50:
        player.current_zone = "marrow entrance"
        over_world_song_set = False
        in_over_world = True
        player.x_coordinate = 465
        player.y_coordinate = 675
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_district_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                              "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                              "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                              "movement_able": movement_able}

    return marrow_district_return


def marrow_entrance(pygame, screen, graphic_dict, player, marrow_entrance_bg, over_world_song_set, interaction_popup,
                    font, save_check_window, user_interface, bar_backdrop,
                    hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                    info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                    staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                    overlay_marrow_west, overlay_marrow_east, overlay_switch, switch_shadow, switch_phase, switch_box,
                    marrow_entrance_bg_open, entrance_music, entrance_npc, entrance_1, entrance_2, entrance_3,
                    entrance_popup, sfx_switch):
    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(entrance_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    if switch_phase == "complete":
        screen.blit(marrow_entrance_bg_open, (0, 0))
    else:
        screen.blit(marrow_entrance_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    screen.blit(entrance_npc.surf, entrance_npc.rect)

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

    screen.blit(overlay_switch.surf, overlay_switch.rect)

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
            player.current_zone = "marrow tower west"
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
            player.current_zone = "marrow tower east"
            player.x_coordinate = 500
            player.y_coordinate = 675
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.Rect.colliderect(player.rect, switch_box):
        interaction_popup.update(515, 225, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Barrier Switch"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (515, 225)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to activate switch."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_switch)
            interacted = False
            if switch_phase == "purple":
                switch_phase = "complete"
                overlay_switch.update(640, 360, graphic_dict["marrow_switch_complete"])

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

    if switch_phase != "complete":
        face_direction = random.choice(["left", "right", "front", "back"])
        if movement_able and in_over_world:
            npc_toc = time.perf_counter()
            if npc_toc - npc_tic > 7:
                npc_tic = time.perf_counter()
                if entrance_2:
                    entrance_3 = True
                if entrance_1:
                    entrance_1 = False
                    entrance_2 = True
                if face_direction == "left":
                    entrance_npc.update(graphic_dict["entrance_npc_left"])
                if face_direction == "right":
                    entrance_npc.update(graphic_dict["entrance_npc_right"])
                if face_direction == "front":
                    entrance_npc.update(graphic_dict["entrance_npc_down"])
                if face_direction == "back":
                    entrance_npc.update(graphic_dict["entrance_npc_up"])
        if entrance_1:
            entrance_text_surf = font.render("Please, you must help.", True, "black", "light yellow")
        if entrance_2:
            entrance_text_surf = font.render("The barrier is locked.", True, "black", "light yellow")
        if entrance_3:
            entrance_text_surf = font.render("The vanguard is trapped.", True, "black", "light yellow")

    else:
        face_direction = random.choice(["left", "right", "front", "back"])
        if movement_able and in_over_world:
            npc_toc = time.perf_counter()
            if npc_toc - npc_tic > 7:
                npc_tic = time.perf_counter()
                if face_direction == "left":
                    entrance_npc.update(graphic_dict["entrance_npc_left"])
                if face_direction == "right":
                    entrance_npc.update(graphic_dict["entrance_npc_right"])
                if face_direction == "front":
                    entrance_npc.update(graphic_dict["entrance_npc_down"])
                if face_direction == "back":
                    entrance_npc.update(graphic_dict["entrance_npc_up"])
            entrance_text_surf = font.render("Thank you.", True, "black", "light yellow")

    screen.blit(entrance_popup.surf, entrance_popup.rect)
    entrance_text_rect = entrance_text_surf.get_rect()
    entrance_text_rect.center = (entrance_popup.x_coordinate, entrance_popup.y_coordinate)
    screen.blit(entrance_text_surf, entrance_text_rect)

    if 450 < player.x_coordinate < 550 and player.y_coordinate < 40:
        player.current_zone = "eldream"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 545
        player.y_coordinate = 690
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
    if player.y_coordinate > 690:
        player.current_zone = "marrow"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 685
        player.y_coordinate = 170
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_entrance_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                              "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                              "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                              "movement_able": movement_able, "switch_phase": switch_phase, "entrance_1": entrance_1,
                              "entrance_2": entrance_2, "entrance_3": entrance_3}

    return marrow_entrance_return


def marrow_tower_west(pygame, screen, graphic_dict, player, marrow_tower_w_bg, over_world_song_set, marrow_music,
                      interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                      hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                      info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                      staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                      overlay_marrow_west, overlay_marrow_east, crate_1, crate_2, ramps_crate_1_got,
                      ramps_crate_2_got, sfx_item_potion, Item):
    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(marrow_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(marrow_tower_w_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if not ramps_crate_1_got:
        screen.blit(crate_1.surf, crate_1.rect)
    if not ramps_crate_2_got:
        screen.blit(crate_2.surf, crate_2.rect)

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

    if pygame.sprite.collide_rect(player, crate_1):
        if not ramps_crate_1_got:
            interaction_popup.update(crate_1.x_coordinate, crate_1.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_1.x_coordinate, crate_1.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not ramps_crate_1_got:
                    if len(player.items) < 16:
                        ramps_crate_1_got = True
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
        if not ramps_crate_2_got:
            interaction_popup.update(crate_2.x_coordinate, crate_2.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_2.x_coordinate, crate_2.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not ramps_crate_2_got:
                    if len(player.items) < 16:
                        ramps_crate_2_got = True
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

    if 425 < player.x_coordinate < 600 and player.y_coordinate >= 710:
        overlay_marrow_west.update(110, 250, graphic_dict["overlay_marrow_ramps_west"])
        overlay_marrow_east.update(925, 250, graphic_dict["overlay_marrow_ramps_east"])
        player.current_zone = "marrow entrance"
        in_over_world = True
        player.x_coordinate = 120
        player.y_coordinate = 385
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if 315 < player.x_coordinate < 350 and player.y_coordinate >= 575:
        overlay_marrow_west.update(570, 55, graphic_dict["overlay_marrow_ramps_west"])
        player.current_zone = "marrow ramps west"
        in_over_world = True
        player.x_coordinate = 515
        player.y_coordinate = 200
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_tower_west_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                                "movement_able": movement_able, "ramps_crate_1_got": ramps_crate_1_got,
                                "ramps_crate_2_got": ramps_crate_2_got}

    return marrow_tower_west_return


def marrow_tower_east(pygame, screen, graphic_dict, player, marrow_tower_e_bg, over_world_song_set, marrow_music,
                      interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                      hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                      info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                      staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                      overlay_marrow_west, overlay_marrow_east, crate_3, crate_4, ramps_crate_3_got, ramps_crate_4_got,
                      sfx_item_potion, Item):
    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(marrow_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(marrow_tower_e_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if not ramps_crate_3_got:
        screen.blit(crate_3.surf, crate_3.rect)
    if not ramps_crate_4_got:
        screen.blit(crate_4.surf, crate_4.rect)

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

    if pygame.sprite.collide_rect(player, crate_3):
        if not ramps_crate_3_got:
            interaction_popup.update(crate_3.x_coordinate, crate_3.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_3.x_coordinate, crate_3.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not ramps_crate_3_got:
                    if len(player.items) < 16:
                        ramps_crate_3_got = True
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

    if pygame.sprite.collide_rect(player, crate_4):
        if not ramps_crate_4_got:
            interaction_popup.update(crate_4.x_coordinate, crate_4.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_4.x_coordinate, crate_4.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not ramps_crate_4_got:
                    if len(player.items) < 16:
                        ramps_crate_4_got = True
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

    if 425 < player.x_coordinate < 600 and player.y_coordinate >= 710:
        overlay_marrow_west.update(110, 250, graphic_dict["overlay_marrow_ramps_west"])
        overlay_marrow_east.update(925, 250, graphic_dict["overlay_marrow_ramps_east"])
        player.current_zone = "marrow entrance"
        in_over_world = True
        player.x_coordinate = 900
        player.y_coordinate = 385
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if 700 < player.x_coordinate < 725 and player.y_coordinate >= 575:
        overlay_marrow_east.update(570, 55, graphic_dict["overlay_marrow_ramps_east"])
        player.current_zone = "marrow ramps east"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 515
        player.y_coordinate = 200
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_tower_east_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                                "movement_able": movement_able, "ramps_crate_3_got": ramps_crate_3_got,
                                "ramps_crate_4_got": ramps_crate_4_got}

    return marrow_tower_east_return


def marrow_ramps_west(pygame, screen, graphic_dict, player, marrow_ramps_w_bg, over_world_song_set, marrow_music,
                      interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                      hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                      info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                      staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                      overlay_marrow_west, chroma_bridge):
    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(marrow_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(marrow_ramps_w_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    screen.blit(chroma_bridge.surf, chroma_bridge.rect)

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

    if pygame.Rect.colliderect(player.rect, overlay_marrow_west):
        interaction_popup.update(570, 55, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("West Tower"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (570, 55)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter Tower."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            player.current_zone = "marrow tower west"
            player.x_coordinate = 100
            player.y_coordinate = 550
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if player.y_coordinate >= 675:
        player.current_zone = "marrow ramps west end"
        in_over_world = True
        player.x_coordinate = 515
        player.y_coordinate = 150
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_tower_west_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                                "movement_able": movement_able}

    return marrow_tower_west_return


def marrow_ramps_east(pygame, screen, graphic_dict, player, marrow_ramps_e_bg, over_world_song_set, marrow_music,
                      interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                      hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                      info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                      staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                      overlay_marrow_east):
    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(marrow_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(marrow_ramps_e_bg, (0, 0))
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

    if pygame.Rect.colliderect(player.rect, overlay_marrow_east):
        interaction_popup.update(570, 55, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("East Tower"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (570, 55)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter Tower."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            over_world_song_set = False
            player.current_zone = "marrow tower east"
            player.x_coordinate = 930
            player.y_coordinate = 550
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if player.y_coordinate >= 675:
        player.current_zone = "marrow ramps east end"
        in_over_world = True
        player.x_coordinate = 515
        player.y_coordinate = 150
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_ramps_east_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                                "movement_able": movement_able}

    return marrow_ramps_east_return


def marrow_ramps_east_end(pygame, screen, graphic_dict, player, marrow_ramps_e_end_bg, over_world_song_set,
                          interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                          hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                          info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                          staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                          dungeon_chest, boots_obtained, chroma_boots, sfx_chest, switch_2, marrow_switch_phase,
                          main_switch, sfx_switch, erebyth_defeated, marrow_ramps_e_end_bg_block, erebyth,
                          player_battle_sprite, barrier_active, sharp_sense_active, snake_battle_sprite,
                          ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite,
                          magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite, in_npc_interaction,
                          necrola_battle_sprite, osodark_battle_sprite, stelli_battle_sprite, in_battle, boss_music,
                          erebyth_battle_sprite):
    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(boss_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    if erebyth_defeated:
        screen.blit(marrow_ramps_e_end_bg, (0, 0))
    else:
        screen.blit(marrow_ramps_e_end_bg_block, (0, 0))
        screen.blit(erebyth.surf, erebyth.rect)
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if erebyth_defeated:
        screen.blit(dungeon_chest.surf, dungeon_chest.rect)

    screen.blit(switch_2.surf, switch_2.rect)

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

    if erebyth_defeated:
        if pygame.sprite.collide_rect(player, dungeon_chest):
            interaction_popup.update(dungeon_chest.x_coordinate, dungeon_chest.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("chest"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (dungeon_chest.x_coordinate, dungeon_chest.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted and in_over_world:
                if not boots_obtained:
                    if len(player.items) < 16:
                        dungeon_chest.update(dungeon_chest.x_coordinate, dungeon_chest.y_coordinate,
                                             graphic_dict["dungeon_chest_open"])
                        pygame.mixer.find_channel(True).play(sfx_chest)
                        info_text_1 = "You've obtained the chroma boots!"
                        info_text_2 = ""
                        player.items.append(chroma_boots)
                        boots_obtained = True
                    else:
                        info_text_1 = "You're inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "You've already obtained this item."
                    info_text_2 = ""
                interacted = False

    if not erebyth_defeated:
        if pygame.sprite.collide_rect(player, erebyth):
            interaction_popup.update(erebyth.x_coordinate, erebyth.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("erebyth"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (erebyth.x_coordinate, erebyth.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            # lets player know if they are in range of enemy they can press f to attack it
            info_text_1 = "Press 'F' key to attack enemy."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted:
                current_enemy_battling = erebyth
                in_over_world = False
                in_battle = True

                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active, graphic_dict)
                combat_scenario.battle_animation_enemy(current_enemy_battling, snake_battle_sprite, ghoul_battle_sprite,
                                                       chorizon_battle_sprite, muchador_battle_sprite,
                                                       magmon_battle_sprite, bandile_battle_sprite,
                                                       chinzilla_battle_sprite, in_battle, in_npc_interaction,
                                                       graphic_dict, necrola_battle_sprite,
                                                       osodark_battle_sprite, stelli_battle_sprite,
                                                       False, erebyth_battle_sprite, erebyth_counter=0)

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

    if player.y_coordinate <= 75:
        player.current_zone = "marrow ramps east"
        in_over_world = True
        player.x_coordinate = 515
        player.y_coordinate = 650
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.Rect.colliderect(player.rect, switch_2):
        interaction_popup.update(195, 135, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Gate Switch"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (195, 135)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to activate switch."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_switch)
            interacted = False
            switch_2.update(147, 74, graphic_dict["ramp_switch_east"])

            if marrow_switch_phase == 'none':
                main_switch.update(640, 360, graphic_dict["marrow_switch_red"])
                marrow_switch_phase = 'red'
            if marrow_switch_phase == 'blue':
                main_switch.update(640, 360, graphic_dict["marrow_switch_purple"])
                marrow_switch_phase = 'purple'

    marrow_ramps_east_end_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                    "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                    "info_text_4": info_text_4, "interacted": interacted,
                                    "in_over_world": in_over_world, "movement_able": movement_able, "boots obtained":
                                    boots_obtained, "marrow_switch_phase": marrow_switch_phase,
                                    "erebyth_defeated": erebyth_defeated, "in_battle": in_battle}
    if in_battle:
        marrow_ramps_east_end_return["current_enemy_battling"] = erebyth

    return marrow_ramps_east_end_return


def marrow_ramps_west_end(pygame, screen, graphic_dict, player, marrow_ramps_w_end_bg, over_world_song_set,
                          marrow_music, interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                          hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                          info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                          staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                          switch_1, marrow_switch_phase, main_switch, sfx_switch):
    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(marrow_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(marrow_ramps_w_end_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    screen.blit(switch_1.surf, switch_1.rect)

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

    if player.y_coordinate <= 75:
        player.current_zone = "marrow ramps west"
        in_over_world = True
        player.x_coordinate = 515
        player.y_coordinate = 650
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.Rect.colliderect(player.rect, switch_1):
        interaction_popup.update(945, 135, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Gate Switch"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (945, 135)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to activate switch."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_switch)
            interacted = False
            switch_1.update(995, 90, graphic_dict["ramp_switch_west"])

            if marrow_switch_phase == 'none':
                main_switch.update(640, 360, graphic_dict["marrow_switch_blue"])
                marrow_switch_phase = 'blue'
            if marrow_switch_phase == 'red':
                main_switch.update(640, 360, graphic_dict["marrow_switch_purple"])
                marrow_switch_phase = 'purple'

    marrow_ramps_west_end_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                    "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                    "info_text_4": info_text_4, "interacted": interacted,
                                    "in_over_world": in_over_world, "movement_able": movement_able,
                                    "marrow_switch_phase": marrow_switch_phase}

    return marrow_ramps_west_end_return
