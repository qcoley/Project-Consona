import time
import random
import drawing_functions
import gameplay_functions
import combat_scenario


def castle_one(pygame, screen, graphic_dict, player, marrow_bg, over_world_song_set, marrow_music,
               interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
               button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
               info_text_3, info_text_4, npc_tic, movement_able, equipment_screen, staff, sword, bow, npc_garan,
               offense_meter, defense_meter, weapon_select, pet_energy_window, artherian, player_battle_sprite,
               current_npc_interacting, in_npc_interaction, hearth_stone, marrow_attuned, sfx_hearth,
               marrow_ghouls, enemy_tic, barrier_active, sharp_sense_active, ghoul_battle_sprite, in_battle,
               current_enemy_battling, Enemy, Item, UiElement, artherian_star, noren, boro, maydria, npcs,
               maydria_star, sub_marrow_ladder, sfx_ladder, vanished, vanish_overlay, basic_fish_counter,
               better_fish_counter, even_better_fish_counter, best_fish_counter, castle_bridge, prism_activate,
               prism_tic, sfx_chroma):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(marrow_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(marrow_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)
    screen.blit(artherian.surf, artherian.rect)
    screen.blit(noren.surf, noren.rect)
    screen.blit(boro.surf, boro.rect)
    screen.blit(maydria.surf, maydria.rect)

    if noren.quest_complete or boro.quest_complete:
        screen.blit(castle_bridge.surf, castle_bridge.rect)

    if noren.quest_complete or boro.quest_complete:
        prism_toc = time.perf_counter()
        if prism_toc - prism_tic < 1.5:
            screen.blit(prism_activate.surf, prism_activate.rect)
            if noren.quest_complete:
                noren.surf = graphic_dict["noren_prism"]
            if boro.quest_complete:
                boro.surf = graphic_dict["boro_prism"]

    if not artherian.quest_complete:
        screen.blit(artherian_star.surf, artherian_star.rect)
    if not maydria.quest_complete:
        screen.blit(maydria_star.surf, maydria_star.rect)

    screen.blit(hearth_stone.surf, hearth_stone.rect)

    respawned_dict = gameplay_functions.enemy_respawn(player, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, Enemy, Item, graphic_dict,
                                                      UiElement, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, marrow_ghouls, marrow_ghouls)
    marrow_ghouls = respawned_dict["marrow_ghouls"]

    for ghoul in marrow_ghouls:
        screen.blit(ghoul.surf, ghoul.rect)
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

    if pygame.sprite.collide_rect(player, artherian):
        interaction_popup.update(artherian.x_coordinate, artherian.y_coordinate - 50,
                                 graphic_dict["popup_interaction_purple"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(artherian.name), True, "black", (203, 195, 227))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (artherian.x_coordinate, artherian.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to talk to NPC."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            current_npc_interacting = artherian
            in_over_world = False
            in_npc_interaction = True
            movement_able = False
            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, False,
                                                    False, graphic_dict)

    if pygame.sprite.collide_rect(player, noren):
        interaction_popup.update(noren.x_coordinate, noren.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(noren.name), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (noren.x_coordinate, noren.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = ""
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            if not noren.quest_complete:
                for item in player.items:
                    if item.name == "prism":
                        pygame.mixer.find_channel(True).play(sfx_chroma)
                        prism_tic = time.perf_counter()
                        noren.quest_complete = True
                        if boro.quest_complete:
                            castle_bridge.update(castle_bridge.x_coordinate, castle_bridge.y_coordinate,
                                                 graphic_dict["castle_bridge_finished"])
                        player.items.remove(item)
                        break
            interacted = False

    if pygame.sprite.collide_rect(player, boro):
        interaction_popup.update(boro.x_coordinate, boro.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(boro.name), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (boro.x_coordinate, boro.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = ""
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            if not boro.quest_complete:
                for item in player.items:
                    if item.name == "prism":
                        pygame.mixer.find_channel(True).play(sfx_chroma)
                        prism_tic = time.perf_counter()
                        boro.quest_complete = True
                        if noren.quest_complete:
                            castle_bridge.update(castle_bridge.x_coordinate, castle_bridge.y_coordinate,
                                                 graphic_dict["castle_bridge_finished"])
                        player.items.remove(item)
                        break
            interacted = False

    if pygame.sprite.collide_rect(player, maydria):
        interaction_popup.update(maydria.x_coordinate, maydria.y_coordinate - 50,
                                 graphic_dict["popup_interaction_purple"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(maydria.name), True, "black", (203, 195, 227))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (maydria.x_coordinate, maydria.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to talk to NPC."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            current_npc_interacting = maydria
            in_over_world = False
            in_npc_interaction = True
            movement_able = False
            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, False,
                                                    False, graphic_dict)

    if pygame.sprite.collide_rect(player, hearth_stone):
        interaction_popup.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("hearth stone"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if not marrow_attuned:
            info_text_1 = "Press 'F' key to attune to stone."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world:
                pygame.mixer.find_channel(True).play(sfx_hearth)
                hearth_stone.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate,
                                    graphic_dict["hearth_stone_lit"])
                marrow_attuned = True
                info_text_1 = "You have attuned to the stone."
                info_text_2 = "You may now fast travel here."
                interacted = False
    else:
        hearth_stone.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate, graphic_dict["hearth_stone"])

    if pygame.Rect.colliderect(player.rect, sub_marrow_ladder):
        interaction_popup.update(365, 575, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Subterranean"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (365, 575)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to climb down ladder."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_ladder)
            interacted = False
            player.current_zone = "sub marrow"
            player.x_coordinate = 425
            player.y_coordinate = 650
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

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, marrow_ghouls)
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
            combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                    sharp_sense_active, graphic_dict)
            combat_scenario.battle_animation_enemy(current_enemy_battling, ghoul_battle_sprite,
                                                   ghoul_battle_sprite, ghoul_battle_sprite, ghoul_battle_sprite,
                                                   ghoul_battle_sprite, ghoul_battle_sprite, ghoul_battle_sprite,
                                                   in_battle, in_npc_interaction, graphic_dict, ghoul_battle_sprite,
                                                   ghoul_battle_sprite, ghoul_battle_sprite, False, ghoul_battle_sprite,
                                                   0, ghoul_battle_sprite)

    # npc movement updates
    face_direction = random.choice(["front", "back", "left", "right"])
    face_this_npc = random.choice(npcs.sprites())
    if movement_able and in_over_world:
        npc_toc = time.perf_counter()
        if npc_toc - npc_tic > 5:
            npc_tic = time.perf_counter()
            if face_direction == "front":
                if face_this_npc.name == "adria":
                    face_this_npc.update(graphic_dict["adria_down"])
                if face_this_npc.name == "noren":
                    face_this_npc.update(graphic_dict["noren_down"])
                if face_this_npc.name == "boro":
                    face_this_npc.update(graphic_dict["boro_down"])
                if face_this_npc.name == "artherian":
                    face_this_npc.update(graphic_dict["artherian_down"])
            if face_direction == "back":
                if face_this_npc.name == "adria":
                    face_this_npc.update(graphic_dict["adria_up"])
                if face_this_npc.name == "noren":
                    face_this_npc.update(graphic_dict["noren_up"])
                if face_this_npc.name == "boro":
                    face_this_npc.update(graphic_dict["boro_up"])
                if face_this_npc.name == "artherian":
                    face_this_npc.update(graphic_dict["artherian_up"])
            if face_direction == "left":
                if face_this_npc.name == "adria":
                    face_this_npc.update(graphic_dict["adria_left"])
                if face_this_npc.name == "noren":
                    face_this_npc.update(graphic_dict["noren_left"])
                if face_this_npc.name == "boro":
                    face_this_npc.update(graphic_dict["boro_left"])
                if face_this_npc.name == "artherian":
                    face_this_npc.update(graphic_dict["artherian_left"])
            if face_direction == "right":
                if face_this_npc.name == "adria":
                    face_this_npc.update(graphic_dict["adria_right"])
                if face_this_npc.name == "noren":
                    face_this_npc.update(graphic_dict["noren_right"])
                if face_this_npc.name == "boro":
                    face_this_npc.update(graphic_dict["boro_right"])
                if face_this_npc.name == "artherian":
                    face_this_npc.update(graphic_dict["artherian_right"])

    # enemy movement updates
    direction_horizontal = random.choice(["left", "right"])
    direction_vertical = random.choice(["up", "down"])
    move_mon = random.choice(marrow_ghouls.sprites())
    if movement_able and in_over_world:
        enemy_toc = time.perf_counter()
        if enemy_toc - enemy_tic > 2:
            enemy_tic = time.perf_counter()
            move_mon.update_position([125, 600], [100, 300], direction_horizontal, direction_vertical)

    if player.y_coordinate <= 50:
        player.current_zone = "marrow entrance"
        over_world_song_set = False
        in_over_world = True
        player.x_coordinate = 465
        player.y_coordinate = 675
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if player.x_coordinate > 660 and player.y_coordinate > 565:
        player.current_zone = "marrow castle"
        over_world_song_set = False
        in_over_world = True
        player.x_coordinate = 465
        player.y_coordinate = 675
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    castle_one_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                         "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                         "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                         "movement_able": movement_able, "current_npc_interacting": current_npc_interacting,
                         "in_npc_interaction": in_npc_interaction, "marrow_attuned": marrow_attuned,
                         "enemy_tic": enemy_tic, "in_battle": in_battle, "current_enemy": current_enemy_battling,
                         "marrow_ghouls": marrow_ghouls, "prism_tic": prism_tic}

    return castle_one_return
