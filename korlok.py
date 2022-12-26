import random
import time

import drawing_functions
import combat_scenario
import gameplay_functions


def korlok_district(pygame, screen, graphic_dict, player, korlok_district_bg, korlok_overworld_music,
                    over_world_song_set, nuldar_buildings, rohir_gate, hearth_stone, mines_entrance, magmons,
                    interaction_popup, font, bridge_not_repaired, reservoir_enter, rock_1, rock_2, save_check_window,
                    user_interface, world_map_container, bar_backdrop, hp_bar, en_bar, xp_bar, offense_upgraded,
                    defense_upgraded, level_up_font, button_highlighted, button_highlight, in_over_world,
                    korlok_attuned, interacted, info_text_1, info_text_2, info_text_3, info_text_4, enemy_tic, npc_tic,
                    in_battle, in_shop, in_academia, in_inn, in_npc_interaction, movement_able, current_enemy_battling,
                    current_npc_interacting, current_building_entering, korlok_enemies, player_battle_sprite,
                    snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite,
                    barrier_active, sharp_sense_active, magmon_battle_sprite, bandile_battle_sprite, voruke, cerah,
                    npcs, seldon_enemies, snakes, ghouls, bandiles, interactables_seldon, interactables_korlok, Enemy,
                    Item, UiElement, interactables_mines, quest_star_garan, quest_star_maurelle,
                    quest_star_celeste, quest_star_torune, star_voruke, star_zerah):

    rohir_gate.update(525, 600, graphic_dict["rohir_gate"])
    hearth_stone.update(885, 230, graphic_dict["hearth_stone"])

    respawned_dict = gameplay_functions.enemy_respawn(player, seldon_enemies, korlok_enemies, snakes, ghouls, magmons,
                                                      bandiles, interactables_seldon, interactables_korlok,
                                                      interactables_mines, Enemy, Item, graphic_dict, UiElement)
    korlok_enemies = respawned_dict["korlok_enemies"]
    magmons = respawned_dict["magmons"]

    for enemy_sprite in magmons:  # update enemy sprite to a highlighted version
        if not player.quest_complete["elementary elementals"]:
            if player.quest_status["elementary elementals"]:
                enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                          graphic_dict["magmon_high"])
    for enemy_sprite in magmons:
        if player.quest_complete["elementary elementals"]:
            enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate, graphic_dict["magmon"])

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(korlok_overworld_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(korlok_district_bg, (0, 0))
    screen.blit(rohir_gate.surf, rohir_gate.rect)
    for building in nuldar_buildings:
        screen.blit(building.surf, building.rect)
    screen.blit(voruke.surf, voruke.rect)
    screen.blit(cerah.surf, cerah.rect)
    screen.blit(mines_entrance.surf, mines_entrance.rect)
    screen.blit(hearth_stone.surf, hearth_stone.rect)
    for magmon in magmons:
        screen.blit(magmon.surf, magmon.rect)

    gameplay_functions.npc_quest_star_updates(screen, player, quest_star_garan, quest_star_maurelle, quest_star_celeste,
                                              quest_star_torune, graphic_dict["quest_progress_star"],
                                              graphic_dict["quest_complete_star"], star_voruke, star_zerah)

    screen.blit(player.surf, player.rect)

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, korlok_enemies)
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
                                              magmon_battle_sprite, bandile_battle_sprite, barrier_active,
                                              sharp_sense_active, in_battle, in_npc_interaction, graphic_dict)

    # if player collides with npc sprite and chooses to interact with it
    npc = pygame.sprite.spritecollideany(player, npcs)
    if npc:
        interaction_popup.update(npc.x_coordinate, npc.y_coordinate - 50, graphic_dict["popup_interaction_purple"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(npc.name), True, "black", (203, 195, 227))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (npc.x_coordinate, npc.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to talk to NPC."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world and not in_battle and not in_shop and not in_inn \
                and not in_academia and not in_npc_interaction:
            interacted = False
            current_npc_interacting = npc
            in_over_world = False
            in_npc_interaction = True
            movement_able = False
            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.resting_animation(player, enemy, player_battle_sprite, snake_battle_sprite,
                                              ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite,
                                              magmon_battle_sprite, bandile_battle_sprite, barrier_active,
                                              sharp_sense_active, in_battle, in_npc_interaction, graphic_dict)

    if pygame.sprite.collide_rect(player, rohir_gate):
        interaction_popup.update(rohir_gate.x_coordinate, rohir_gate.y_coordinate, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(rohir_gate.name), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rohir_gate.x_coordinate, rohir_gate.y_coordinate)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if not bridge_not_repaired:
            info_text_1 = "Press 'F' key to enter Seldon District."

            if interacted:
                player.current_zone = "seldon"
                in_over_world = True
                interacted = False
                player.x_coordinate = 525
                player.y_coordinate = 100
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                rohir_gate.update(525, 50, graphic_dict["rohir_gate"])

    if pygame.sprite.collide_rect(player, reservoir_enter):
        interaction_popup.update(reservoir_enter.x_coordinate + 50, reservoir_enter.y_coordinate - 55,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("reservoir"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (reservoir_enter.x_coordinate + 50, reservoir_enter.y_coordinate - 55)
        screen.blit(interaction_info_surf, interaction_info_rect)
        info_text_1 = "Press 'F' key to enter the Reservoir."

        if interacted:
            player.current_zone = "reservoir c"
            in_over_world = True
            over_world_song_set = False
            interacted = False
            if rock_1.x_coordinate == 580:
                rock_1.update(rock_1.x_coordinate + 300, rock_1.y_coordinate, graphic_dict["rock_img"])
            if rock_2.x_coordinate == 580:
                rock_2.update(rock_2.x_coordinate + 300, rock_2.y_coordinate, graphic_dict["rock_img"])
            player.x_coordinate = 705
            player.y_coordinate = 175
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.sprite.collide_rect(player, mines_entrance):
        interaction_popup.update(mines_entrance.x_coordinate, mines_entrance.y_coordinate - 55,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("mines"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (mines_entrance.x_coordinate, mines_entrance.y_coordinate - 55)
        screen.blit(interaction_info_surf, interaction_info_rect)
        info_text_1 = "Press 'F' key to enter the Mines."

        if interacted:
            interacted = False
            player.current_zone = "mines"
            player.x_coordinate = 705
            player.y_coordinate = 600
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.sprite.collide_rect(player, hearth_stone):
        interaction_popup.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("hearth stone"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if not korlok_attuned:
            info_text_1 = "Press 'F' key to attune to stone."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world:
                hearth_stone.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate,
                                    graphic_dict["hearth_stone_lit"])
                korlok_attuned = True
                info_text_1 = "You have attuned to the stone."
                info_text_2 = "You may now fast travel here."
                interacted = False
    else:
        hearth_stone.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate, graphic_dict["hearth_stone"])

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
                                     in_over_world, offense_upgraded, defense_upgraded, level_up_font)
    drawing_functions.draw_it(screen)

    if button_highlighted:
        screen.blit(button_highlight.surf, button_highlight.rect)

    # enemy movement updates
    direction_horizontal = random.choice(["left", "right"])
    direction_vertical = random.choice(["up", "down"])
    move_mon = random.choice(magmons.sprites())
    if movement_able and in_over_world:
        enemy_toc = time.perf_counter()
        if enemy_toc - enemy_tic > 2:
            enemy_tic = time.perf_counter()
            move_mon.update_position([50, 500], [50, 250], direction_horizontal, direction_vertical)

    # info to return to main loop --------------------------------------------------------------------------------------
    korlok_return = {"over_world_song_set": over_world_song_set, "korlok_attuned": korlok_attuned,
                     "enemy_tic": enemy_tic, "npc_tic": npc_tic, "info_text_1": info_text_1,
                     "info_text_2": info_text_2, "info_text_3": info_text_3, "info_text_4": info_text_4,
                     "interacted": interacted, "in_over_world": in_over_world, "in_battle": in_battle,
                     "in_shop": in_shop, "in_academia": in_academia, "in_inn": in_inn,
                     "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                     "current_enemy_battling": current_enemy_battling,
                     "current_building_entering": current_building_entering,
                     "current_npc_interacting": current_npc_interacting}

    return korlok_return
