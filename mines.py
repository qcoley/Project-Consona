import random
import time

import drawing_functions
import combat_scenario


def korlok_mines(pygame, screen, graphic_dict, player, korlok_mines_bg, korlok_overworld_music,
                 over_world_song_set, bandiles, interaction_popup, font, save_check_window, user_interface,
                 world_map_container, bar_backdrop, hp_bar, en_bar, xp_bar, offense_upgraded, defense_upgraded,
                 level_up_font, button_highlighted, button_highlight, in_over_world, interacted, info_text_1,
                 info_text_2, info_text_3, info_text_4, enemy_tic, npc_tic, in_battle, in_npc_interaction,
                 movement_able, current_enemy_battling, mine_enemies, player_battle_sprite, snake_battle_sprite,
                 ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite, barrier_active,
                 sharp_sense_active, magmon_battle_sprite, bandile_battle_sprite, mines_wall, mines_light):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(korlok_overworld_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(korlok_mines_bg, (0, 0))
    for bandile in bandiles:
        screen.blit(bandile.surf, bandile.rect)
    screen.blit(player.surf, player.rect)

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, mine_enemies)
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

    if player.x_coordinate > 660 and 685 < player.y_coordinate:
        player.current_zone = "korlok"
        over_world_song_set = False
        in_over_world = True
        player.x_coordinate = 430
        player.y_coordinate = 430

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
    move_mon = random.choice(bandiles.sprites())
    if movement_able and in_over_world:
        enemy_toc = time.perf_counter()
        if enemy_toc - enemy_tic > 2:
            enemy_tic = time.perf_counter()
            move_mon.update_position([50, 500], [50, 250], direction_horizontal, direction_vertical)

    # info to return to main loop --------------------------------------------------------------------------------------
    mines_return = {"over_world_song_set": over_world_song_set, "enemy_tic": enemy_tic, "npc_tic": npc_tic,
                    "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                    "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                    "in_battle": in_battle, "movement_able": movement_able,
                    "current_enemy_battling": current_enemy_battling}

    return mines_return
