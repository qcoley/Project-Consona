import time

import gameplay_functions
import drawing_functions


def fishing_hut(pygame, screen, player, over_world_song_set, fishing_music, fishing, walk_tic, fishing_spot_1,
                fishing_spot_2, graphic_dict, fishing_timer, fishing_level, basic_fish_counter, better_fish_counter,
                even_better_fish_counter, best_fish_counter, fish_caught, previous_surf, water_fish_1,
                water_fish_3, water_fish_4, fishing_hut_bg, equipment_screen, offense_meter, defense_meter, staff,
                sword, bow, npc_garan, weapon_select, save_check_window, user_interface, bar_backdrop, hp_bar,
                en_bar, xp_bar, font, info_text_1, info_text_2, info_text_3, info_text_4, in_over_world,
                fishing_hut_rect, interaction_popup, interacted, fishing_unlocked, movement_able, in_hut,
                pet_energy_window):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(fishing_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    # if player isn't currently fishing, periodically update spots for animation
    if not fishing:
        if walk_tic % 2 > 1.75:
            fishing_spot_1.update(740, 410, graphic_dict["fishing_spot_1"])
            fishing_spot_2.update(575, 525, graphic_dict["fishing_spot_2"])
        else:
            fishing_spot_1.update(740, 410, graphic_dict["fishing_spot_2"])
            fishing_spot_2.update(575, 525, graphic_dict["fishing_spot_1"])

    # if player is fishing
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

    # water movement animation -------------------------------------------------------------------------
    if 1000 > water_fish_1.x_coordinate > 35:
        water_fish_1.x_coordinate -= 1
        water_fish_1.rect.midbottom = (water_fish_1.x_coordinate, water_fish_1.y_coordinate)
    else:
        water_fish_1.update(850, water_fish_1.y_coordinate, graphic_dict["water"])

    if 1000 > water_fish_3.x_coordinate > 35:
        water_fish_3.x_coordinate -= 1
        water_fish_3.rect.midbottom = (water_fish_3.x_coordinate, water_fish_3.y_coordinate)
    else:
        water_fish_3.update(850, water_fish_3.y_coordinate, graphic_dict["water"])

    if 1000 > water_fish_4.x_coordinate > 35:
        water_fish_4.x_coordinate -= 1
        water_fish_4.rect.midbottom = (water_fish_4.x_coordinate, water_fish_4.y_coordinate)
    else:
        water_fish_4.update(850, water_fish_4.y_coordinate, graphic_dict["water"])
    # --------------------------------------------------------------------------------------------------

    screen.blit(fishing_hut_bg, (0, 0))
    screen.blit(water_fish_1.surf, water_fish_1.rect)
    screen.blit(water_fish_3.surf, water_fish_3.rect)
    screen.blit(water_fish_4.surf, water_fish_4.rect)
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)
    screen.blit(fishing_spot_1.surf, fishing_spot_1.rect)
    screen.blit(fishing_spot_2.surf, fishing_spot_2.rect)
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

    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)
    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world)
    drawing_functions.draw_it(screen)
    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])

    if pygame.Rect.colliderect(player.rect, fishing_hut_rect):
        interaction_popup.update(847, 148, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("fishing hut"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (847, 148)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter hut."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            movement_able = False
            in_over_world = False
            in_hut = True

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
                    if item.name == "korlok bait":
                        fishing = True
                        interacted = False
                        fishing_timer = time.perf_counter()
                        player.items.remove(item)
                        previous_surf = player.surf
                        # to clear popup
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

            if interacted and in_over_world and fishing_unlocked:
                for item in player.items:
                    if item.name == "korlok bait":
                        fishing = True
                        interacted = False
                        fishing_timer = time.perf_counter()
                        player.items.remove(item)
                        previous_surf = player.surf
                        fish_caught = False
                        break

    # move player to seldon district when they approach nascent grove exit
    if player.x_coordinate < 50 and player.y_coordinate < 375:
        player.current_zone = "korlok"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 925
        player.y_coordinate = 545

    hut_return = {"over_world_song_set": over_world_song_set, "basic_fish_counter": basic_fish_counter,
                  "better_fish_counter": better_fish_counter, "even_better_fish_counter": even_better_fish_counter,
                  "best_fish_counter": best_fish_counter, "fish_caught": fish_caught, "movement_able": movement_able,
                  "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                  "info_text_4": info_text_4, "in_hut": in_hut, "fishing": fishing, "fishing_timer": fishing_timer,
                  "previous_surf": previous_surf, "interacted": interacted, "in_over_world": in_over_world}

    return hut_return
