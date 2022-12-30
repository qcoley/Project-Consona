import random
import time

import drawing_functions
import combat_scenario
import gameplay_functions


def terra_trail(pygame, screen, graphic_dict, player, mountain_trail_bg, korlok_overworld_music, over_world_song_set,
                   interaction_popup, font, save_check_window, user_interface, world_map_container, bar_backdrop,
                   hp_bar, en_bar, xp_bar, offense_upgraded, defense_upgraded, level_up_font, button_highlighted,
                   button_highlight, in_over_world, interacted, info_text_1, info_text_2, info_text_3, info_text_4,
                   npc_tic, in_npc_interaction, in_battle, movement_able, current_enemy_battling, interactables_seldon,
                   interactables_korlok, Item, UiElement, interactables_mines, quest_star_garan,
                   quest_star_maurelle, quest_star_celeste, quest_star_torune, star_voruke, star_zerah,
                   star_apothecary, terra_mountains, terra_cave):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(korlok_overworld_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(mountain_trail_bg, (0, 0))
    screen.blit(terra_mountains.surf, terra_mountains.rect)
    screen.blit(terra_cave.surf, terra_cave.rect)

    gameplay_functions.npc_quest_star_updates(screen, player, quest_star_garan, quest_star_maurelle, quest_star_celeste,
                                              quest_star_torune, graphic_dict["quest_progress_star"],
                                              graphic_dict["quest_complete_star"], star_voruke, star_zerah,
                                              star_apothecary)

    screen.blit(player.surf, player.rect)

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

    if player.x_coordinate < 75 and player.y_coordinate < 225:
        player.current_zone = "korlok"
        in_over_world = True
        player.x_coordinate = 900
        player.y_coordinate = 175
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    trail_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic, "info_text_1": info_text_1,
                    "info_text_2": info_text_2, "info_text_3": info_text_3, "info_text_4": info_text_4,
                    "interacted": interacted, "in_over_world": in_over_world, "in_battle": in_battle,
                    "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                    "current_enemy_battling": current_enemy_battling}

    return trail_return

