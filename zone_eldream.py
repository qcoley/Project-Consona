import random
import time

import drawing_functions
import combat_scenario
import gameplay_functions


def eldream_district(pygame, screen, graphic_dict, player, eldream_district_bg, eldream_overworld_music,
                     over_world_song_set, interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                     hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                     info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, in_npc_interaction, in_battle,
                     movement_able, current_enemy_battling, quest_star_garan, quest_star_maurelle, quest_star_celeste,
                     quest_star_torune, star_voruke, star_zerah, star_apothecary, terra_mountains, terra_cave,
                     npc_dionte, quest_star_dionte, enemy, player_battle_sprite, snake_battle_sprite,
                     ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite, magmon_battle_sprite,
                     bandile_battle_sprite, chinzilla_battle_sprite, barrier_active, sharp_sense_active,
                     current_npc_interacting, chinzilla, star_dionte, hearth_stone, equipment_screen, staff, sword, bow,
                     npc_garan, offense_meter, defense_meter, weapon_select, rock_7, rock_7_con, chinzilla_defeated,
                     eldream_gate_rect, eldream_attuned, in_shop, in_inn, current_building_entering, enemy_tic,
                     eldream_flowers, seldon_enemies, korlok_enemies, snakes, ghouls, magmons, bandiles,
                     interactables_seldon, interactables_korlok, interactables_mines, Enemy, Item, UiElement,
                     seldon_flowers, interactables_eldream):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(eldream_overworld_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(eldream_district_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    gameplay_functions.npc_quest_star_updates(screen, player, quest_star_garan, quest_star_maurelle, quest_star_celeste,
                                              quest_star_torune, graphic_dict["quest_progress_star"],
                                              graphic_dict["quest_complete_star"], star_voruke, star_zerah,
                                              star_apothecary, star_dionte)

    respawned_dict = gameplay_functions.enemy_respawn(player, seldon_enemies, korlok_enemies, snakes, ghouls, magmons,
                                                      bandiles, interactables_seldon, interactables_korlok,
                                                      interactables_mines, Enemy, Item, graphic_dict, UiElement,
                                                      seldon_flowers, eldream_flowers, interactables_eldream)

    eldream_flowers = respawned_dict["eldream_flowers"]
    interactables_eldream = respawned_dict["interactables_eldream"]

    for flower in eldream_flowers:
        screen.blit(flower.surf, flower.rect)

    screen.blit(player.surf, player.rect)

    # player collides with flower, if collected adds to player flower count
    flower = pygame.sprite.spritecollideany(player, eldream_flowers)
    if flower and in_over_world:
        flower.update(flower.x_coordinate, flower.y_coordinate, graphic_dict["flower_eldream_high"])
        if interacted:
            player.flowers_sorae += 1
            flower.kill()
            info_text_1 = "You collected the Eldream Flower."
            info_text_2 = ""
            interacted = False

    # resets flower surface to non-highlighted if not currently interacting
    for flow in eldream_flowers:
        if flow.surf == graphic_dict["flower_eldream_high"]:
            if flow != flower:
                flow.surf = graphic_dict["flower_eldream"]

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

    if player.x_coordinate < 100 and player.y_coordinate < 175:
        player.current_zone = "terra trail"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 555
        player.y_coordinate = 145
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    eldream_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic, "info_text_1": info_text_1,
                      "info_text_2": info_text_2, "info_text_3": info_text_3, "info_text_4": info_text_4,
                      "interacted": interacted, "in_over_world": in_over_world, "in_battle": in_battle,
                      "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                      "current_enemy_battling": current_enemy_battling,
                      "current_npc_interacting": current_npc_interacting, "eldream_attuned": eldream_attuned,
                      "in_shop": in_shop, "in_inn": in_inn, "current_building_entering": current_building_entering,
                      "enemy_tic": enemy_tic, "eldream_flowers": eldream_flowers,
                      "interactables_eldream": interactables_eldream}

    return eldream_return
