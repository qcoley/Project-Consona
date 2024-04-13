import random
import time

import drawing_functions
import combat_scenario
import gameplay_functions


def korlok_district(pygame, screen, graphic_dict, player, korlok_district_bg, korlok_overworld_music,
                    over_world_song_set, nuldar_buildings, rohir_gate, hearth_stone, mines_entrance, magmons,
                    interaction_popup, font, bridge_not_repaired, reservoir_enter, rock_1, rock_2, save_check_window,
                    user_interface, bar_backdrop, hp_bar, en_bar, xp_bar, button_highlighted, button_highlight,
                    in_over_world, korlok_attuned, interacted, info_text_1, info_text_2, info_text_3,
                    info_text_4, enemy_tic, npc_tic, in_battle, in_shop, in_academia, in_inn, in_npc_interaction,
                    movement_able, current_enemy_battling, current_npc_interacting, current_building_entering,
                    korlok_enemies, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite,
                    chorizon_battle_sprite, muchador_battle_sprite, barrier_active, sharp_sense_active,
                    magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite, voruke, zerah, npcs,
                    seldon_enemies, snakes, ghouls, bandiles, interactables_seldon, interactables_korlok, Enemy, Item,
                    UiElement, interactables_mines, star_voruke, star_zerah, korlok_mountains, in_apothecary,
                    equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter,
                    weapon_select, rock_4, rock_5, rock_6, rock_4_con, rock_5_con, rock_6_con, seldon_flowers,
                    eldream_flowers, interactables_eldream, pet_energy_window, ectrenos_front_enemies,
                    necrola_battle_sprite, osodark_battle_sprite, sfx_rupee, sfx_hearth, sfx_door, top_1, top_2, top_3,
                    worker, worker_tic, stelli_battle_sprite, vanished, vanish_overlay, worker_delay_tic,
                    bridge_gate, erebyth_defeated, repaired_bg, forge_entrance, basic_fish_counter, better_fish_counter,
                    even_better_fish_counter, best_fish_counter, sfx_paper, magmons_highlighted, magmons_reset,
                    nahun, star_nahun, apothis_gift, dawn, early_morning, morning, early_afternoon, afternoon,
                    dusk, night, time_of_day, snow_fall_tic, snow_fall_phase, cloaked, nede, kasper_unlocked,
                    torok_unlocked, iriana_unlocked, kasper_battle_sprite, torok_battle_sprite, iriana_battle_sprite,
                    night_music):

    respawned_dict = gameplay_functions.enemy_respawn(player, seldon_enemies, korlok_enemies, snakes, ghouls, magmons,
                                                      bandiles, interactables_seldon, interactables_korlok,
                                                      interactables_mines, Enemy, Item, graphic_dict, UiElement,
                                                      seldon_flowers, eldream_flowers, interactables_eldream,
                                                      ectrenos_front_enemies, ectrenos_front_enemies,
                                                      ectrenos_front_enemies, ectrenos_front_enemies,
                                                      ectrenos_front_enemies, False, False, False, False, time_of_day)
    magmons = respawned_dict["magmons"]

    if time_of_day == 0 or time_of_day == 7:
        if player.quest_status["elementary elementals"] and not player.quest_complete["elementary elementals"]:
            if not magmons_highlighted:
                for enemy_sprite in magmons:
                    if enemy_sprite.name == "Magmon":
                        enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                                  graphic_dict["magmon_high_night"])
                magmons_highlighted = True
        if player.quest_complete["elementary elementals"]:
            if not magmons_reset:
                for enemy_sprite in magmons:
                    if enemy_sprite.name == "Magmon":
                        enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                                  graphic_dict["magmon_night"])
                magmons_reset = True
    else:
        if player.quest_status["elementary elementals"] and not player.quest_complete["elementary elementals"]:
            if not magmons_highlighted:
                for enemy_sprite in magmons:
                    if enemy_sprite.name == "Magmon":
                        enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                                  graphic_dict["magmon_high"])
                magmons_highlighted = True
        if player.quest_complete["elementary elementals"]:
            if not magmons_reset:
                for enemy_sprite in magmons:
                    if enemy_sprite.name == "Magmon":
                        enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                                  graphic_dict["magmon"])
                magmons_reset = True

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            if time_of_day == 0 or time_of_day == 7:
                pygame.mixer.music.load(night_music)
            else:
                pygame.mixer.music.load(korlok_overworld_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    if not erebyth_defeated:
        screen.blit(korlok_district_bg, (0, 0))
    if erebyth_defeated:
        screen.blit(repaired_bg, (0, 0))
    screen.blit(rock_4.surf, rock_4.rect)
    screen.blit(rock_5.surf, rock_5.rect)
    screen.blit(rock_6.surf, rock_6.rect)
    screen.blit(rohir_gate.surf, rohir_gate.rect)
    for building in nuldar_buildings:
        screen.blit(building.surf, building.rect)
    screen.blit(voruke.surf, voruke.rect)
    screen.blit(zerah.surf, zerah.rect)
    screen.blit(nahun.surf, nahun.rect)
    screen.blit(mines_entrance.surf, mines_entrance.rect)
    screen.blit(hearth_stone.surf, hearth_stone.rect)
    for magmon in magmons:
        screen.blit(magmon.surf, magmon.rect)

    # ------------------------------------------------------------------------------------------------------------------
    if time_of_day != 0 and time_of_day != 7:
        if not erebyth_defeated:
            if 399 < worker.y_coordinate < 600:
                if not worker.gift:
                    worker.y_coordinate += 0.5
                if worker.gift:
                    worker.y_coordinate -= 0.5

                    worker_toc = time.perf_counter()
                    if worker_toc - worker_tic > 0.50:
                        worker_tic = time.perf_counter()
                        match worker.quest_complete:
                            case True:
                                worker.quest_complete = False
                                worker.update(graphic_dict["worker_2_back_a"])
                            case False:
                                worker.quest_complete = True
                                worker.update(graphic_dict["worker_2_back_b"])

                worker.rect = worker.surf.get_rect(midbottom=(worker.x_coordinate, worker.y_coordinate))

            worker_delay_toc = time.perf_counter()
            if worker_delay_toc - worker_delay_tic > 10:
                if worker.y_coordinate == 600:
                    worker.gift = True
                    worker.update(graphic_dict["worker_2_back_a"])
                    worker.y_coordinate -= 1
                    worker_delay_tic = time.perf_counter()

                if worker.y_coordinate == 399:
                    worker.gift = False
                    worker.update(graphic_dict["worker_2_full"])
                    worker.y_coordinate += 1
                    worker_delay_tic = time.perf_counter()

            screen.blit(worker.surf, worker.rect)
    # ------------------------------------------------------------------------------------------------------------------
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

    snow_fall_toc = time.perf_counter()
    if snow_fall_toc - snow_fall_tic > 2:
        match snow_fall_phase:
            case 0:
                korlok_mountains.update(241, 251, graphic_dict["korlok_mountains"])
                snow_fall_phase = 1
                snow_fall_tic = time.perf_counter()
            case 1:
                korlok_mountains.update(241, 251, graphic_dict["korlok_mountains_1"])
                snow_fall_phase = 2
                snow_fall_tic = time.perf_counter()
            case 2:
                korlok_mountains.update(241, 251, graphic_dict["korlok_mountains_2"])
                snow_fall_phase = 0
                snow_fall_tic = time.perf_counter()

    screen.blit(korlok_mountains.surf, korlok_mountains.rect)
    screen.blit(bridge_gate.surf, bridge_gate.rect)
    if len(drawing_functions.character_sheet_window) == 0 and len(drawing_functions.game_guide_container) == 0 \
            and len(drawing_functions.journal_window) == 0:
        screen.blit(top_1.surf, top_1.rect)
        screen.blit(top_2.surf, top_2.rect)
        screen.blit(top_3.surf, top_3.rect)

    if time_of_day == 0:
        screen.blit(dawn, (0, 0))
    if time_of_day == 1:
        screen.blit(early_morning, (0, 0))
    if time_of_day == 2:
        screen.blit(morning, (0, 0))
    if time_of_day == 4:
        screen.blit(early_afternoon, (0, 0))
    if time_of_day == 5:
        screen.blit(afternoon, (0, 0))
    if time_of_day == 6:
        screen.blit(dusk, (0, 0))
    if time_of_day == 7:
        screen.blit(night, (0, 0))

    if not player.quest_complete["band hammer"]:
        screen.blit(star_voruke.surf, star_voruke.rect)
    if not player.quest_complete["elementary elementals"]:
        screen.blit(star_zerah.surf, star_zerah.rect)
    if not player.quest_complete["disenchanted"]:
        screen.blit(star_nahun.surf, star_nahun.rect)

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, korlok_enemies, pygame.sprite.collide_rect_ratio(0.75))
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
                                                    sharp_sense_active, graphic_dict, kasper_unlocked,
                                                    torok_unlocked, iriana_unlocked,
                                                    kasper_battle_sprite, torok_battle_sprite,
                                                    iriana_battle_sprite)
            combat_scenario.battle_animation_enemy(current_enemy_battling, snake_battle_sprite,
                                                   ghoul_battle_sprite,
                                                   chorizon_battle_sprite, muchador_battle_sprite,
                                                   magmon_battle_sprite, bandile_battle_sprite,
                                                   chinzilla_battle_sprite, in_battle, in_npc_interaction,
                                                   graphic_dict, necrola_battle_sprite,
                                                   osodark_battle_sprite, stelli_battle_sprite,
                                                   False, stelli_battle_sprite, 0, stelli_battle_sprite,
                                                   stelli_battle_sprite, stelli_battle_sprite, False, cloaked,
                                                   time_of_day, True)

    # if player collides with npc sprite and chooses to interact with it
    npc = pygame.sprite.spritecollideany(player, npcs, pygame.sprite.collide_rect_ratio(0.75))
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
            combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                    sharp_sense_active, graphic_dict, kasper_unlocked,
                                                    torok_unlocked, iriana_unlocked,
                                                    kasper_battle_sprite, torok_battle_sprite,
                                                    iriana_battle_sprite)

    # player collides with building, enters if chosen to interact and starts related scenario
    building = pygame.sprite.spritecollideany(player, nuldar_buildings, pygame.sprite.collide_rect_ratio(0.75))
    if building and in_over_world and building != reservoir_enter:

        interaction_popup.update(building.x_coordinate, building.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(building.name), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (building.x_coordinate, building.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if building.name == "Shop":
            if time_of_day != 0 and time_of_day != 7:
                info_text_1 = "Press 'F' key to enter shop."
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""
            else:
                info_text_1 = "Shop only open during the day."
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""

        if building.name == "Apothecary":
            info_text_1 = "Press 'F' key to enter Apothecary."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

        if building.name == "Inn":
            info_text_1 = "Press 'F' key to enter inn."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

        if interacted:
            if building.name == "Shop":
                if time_of_day != 0 and time_of_day != 7:
                    in_shop = True
                    pygame.mixer.find_channel(True).play(sfx_door)
                    current_building_entering = building
                    movement_able = False
                    in_over_world = False
                    over_world_song_set = False
                    drawing_functions.loot_popup_container.clear()
                    drawing_functions.loot_text_container.clear()
            if building.name == "Inn":
                in_inn = True
                pygame.mixer.find_channel(True).play(sfx_door)
                current_building_entering = building
                movement_able = False
                in_over_world = False
                over_world_song_set = False
                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
            if building.name == "Apothecary":
                in_apothecary = True
                pygame.mixer.find_channel(True).play(sfx_door)
                current_building_entering = building
                movement_able = False
                in_over_world = False
                over_world_song_set = False
                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
            interacted = False

    if pygame.sprite.collide_rect(player, rohir_gate):
        interaction_popup.update(rohir_gate.x_coordinate, rohir_gate.y_coordinate, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render("Seldon", True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rohir_gate.x_coordinate, rohir_gate.y_coordinate)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if erebyth_defeated:
            info_text_1 = "Press 'F' key to enter Seldon District."

            if interacted:
                player.current_zone = "seldon"
                in_over_world = True
                interacted = False
                over_world_song_set = False
                player.x_coordinate = 545
                player.y_coordinate = 175
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                rohir_gate.update(525, 50, graphic_dict["rohir_gate"])

                if time_of_day == 0 or time_of_day == 7:
                    for snake in snakes:
                        if (player.quest_status["sneaky snakes"]
                                and not player.quest_complete["sneaky snakes"]):
                            snake.update_image(snake.x_coordinate, snake.y_coordinate,
                                               graphic_dict["snake_high_night"])
                        else:
                            snake.update_image(snake.x_coordinate, snake.y_coordinate,
                                               graphic_dict["snake_night"])
                    if player.quest_progress["where's nede?"] == 1:
                        nede.update(809, 390, graphic_dict["nede_sleep"])
                else:
                    for snake in snakes:
                        if (player.quest_status["sneaky snakes"]
                                and not player.quest_complete["sneaky snakes"]):
                            snake.update_image(snake.x_coordinate, snake.y_coordinate,
                                               graphic_dict["snake_high"])
                        else:
                            snake.update_image(snake.x_coordinate, snake.y_coordinate,
                                               graphic_dict["snake"])
                    if player.quest_progress["where's nede?"] == 1:
                        nede.update(809, 390, graphic_dict["nede_left"])

        if interacted:
            interacted = False

    if pygame.sprite.collide_rect(player, reservoir_enter):
        interaction_popup.update(reservoir_enter.x_coordinate + 50, reservoir_enter.y_coordinate - 55,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Reservoir"), True, "black", "light yellow")
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
                rock_1.update(rock_1.x_coordinate + 300, rock_1.y_coordinate, graphic_dict["rock"])
            if rock_2.x_coordinate == 580:
                rock_2.update(rock_2.x_coordinate + 300, rock_2.y_coordinate, graphic_dict["rock"])
            player.x_coordinate = 705
            player.y_coordinate = 175
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.sprite.collide_rect(player, mines_entrance):
        interaction_popup.update(mines_entrance.x_coordinate, mines_entrance.y_coordinate - 55,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Mines"), True, "black", "light yellow")
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
            if time_of_day == 0 or time_of_day == 7:
                for bandile in bandiles:
                    if (player.quest_status["band hammer"]
                            and not player.quest_complete["band hammer"]):
                        bandile.update_image(bandile.x_coordinate, bandile.y_coordinate,
                                             graphic_dict["bandile_high_night"])
                    else:
                        bandile.update_image(bandile.x_coordinate, bandile.y_coordinate,
                                             graphic_dict["bandile_night"])
            else:
                for bandile in bandiles:
                    if (player.quest_status["band hammer"]
                            and not player.quest_complete["band hammer"]):
                        bandile.update_image(bandile.x_coordinate, bandile.y_coordinate,
                                             graphic_dict["bandile_high"])
                    else:
                        bandile.update_image(bandile.x_coordinate, bandile.y_coordinate,
                                             graphic_dict["bandile"])

    if pygame.sprite.collide_rect(player, forge_entrance):
        interaction_popup.update(forge_entrance.x_coordinate + 5, forge_entrance.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Forge"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (forge_entrance.x_coordinate + 5, forge_entrance.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)
        info_text_1 = "Press 'F' key to enter the Forge."

        if interacted:
            interacted = False
            player.current_zone = "forge"
            player.x_coordinate = 515
            player.y_coordinate = 670
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.sprite.collide_rect(player, hearth_stone):
        interaction_popup.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Hearth stone"), True, "black", "light yellow")
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
                pygame.mixer.find_channel(True).play(sfx_hearth)
                info_text_1 = "You have attuned to the stone."
                info_text_2 = "You may now fast travel here."
                interacted = False

        if interacted:
            interacted = False
    else:
        hearth_stone.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate, graphic_dict["hearth_stone"])

    if pygame.sprite.collide_rect(player, rock_4):
        interaction_popup.update(rock_4.x_coordinate, rock_4.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Rock"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rock_4.x_coordinate, rock_4.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            try:
                if player.equipment["gloves"].name == "power gloves":
                    if rock_4.x_coordinate == 400:
                        rock_4.update(rock_4.x_coordinate - 90, rock_4.y_coordinate, graphic_dict["rock_small"])
                        if not rock_4_con:
                            pygame.mixer.find_channel(True).play(sfx_rupee)
                            player.rupees += 30
                            rock_4_con = True
                            info_text_1 = "You found 30 Rupees under the rock!"
                            info_text_2 = ""
                else:
                    info_text_1 = "The rock won't budge."
                    info_text_2 = ""
            except AttributeError:
                info_text_1 = "The rock won't budge."
                info_text_2 = ""
                pass
            interacted = False

    if pygame.sprite.collide_rect(player, rock_5):
        interaction_popup.update(rock_5.x_coordinate, rock_5.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Rock"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rock_5.x_coordinate, rock_5.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            try:
                if player.equipment["gloves"].name == "power gloves":
                    if rock_5.x_coordinate == 660:
                        rock_5.update(rock_5.x_coordinate + 90, rock_5.y_coordinate, graphic_dict["rock_small"])
                        if not rock_5_con:
                            pygame.mixer.find_channel(True).play(sfx_rupee)
                            player.rupees += 25
                            rock_5_con = True
                            info_text_1 = "You found 25 Rupees under the rock!"
                            info_text_2 = ""
                else:
                    info_text_1 = "The rock won't budge."
                    info_text_2 = ""
            except AttributeError:
                info_text_1 = "The rock won't budge."
                info_text_2 = ""
                pass
            interacted = False

    if pygame.sprite.collide_rect(player, rock_6):
        interaction_popup.update(rock_6.x_coordinate, rock_6.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Rock"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rock_6.x_coordinate, rock_6.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            try:
                if player.equipment["gloves"].name == "power gloves":
                    if rock_6.x_coordinate == 750:
                        rock_6.update(rock_6.x_coordinate + 110, rock_6.y_coordinate, graphic_dict["rock_small"])
                        if not rock_6_con:
                            pygame.mixer.find_channel(True).play(sfx_rupee)
                            player.rupees += 25
                            rock_6_con = True
                            info_text_1 = "You found 25 Rupees under the rock!"
                            info_text_2 = ""
                else:
                    info_text_1 = "The rock won't budge."
                    info_text_2 = ""
            except AttributeError:
                info_text_1 = "The rock won't budge."
                info_text_2 = ""
                pass
            interacted = False

    # --------------------------------------------------------------------------------------------------
    # enemy movement updates
    if time_of_day != 0 and time_of_day != 7:
        direction_horizontal = random.choice(["left", "right"])
        direction_vertical = random.choice(["up", "down"])
        move_mon = random.choice(magmons.sprites())
        if movement_able and in_over_world:
            enemy_toc = time.perf_counter()
            if enemy_toc - enemy_tic > 1:
                enemy_tic = time.perf_counter()
                move_mon.update_position([50, 500], [50, 250], direction_horizontal, direction_vertical)

    if player.x_coordinate > 950 and player.y_coordinate < 225:
        player.current_zone = "terra trail"
        in_over_world = True
        player.x_coordinate = 150
        player.y_coordinate = 150
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if player.x_coordinate > 975 and player.y_coordinate > 475:
        player.current_zone = "fishing hut"
        in_over_world = True
        if time_of_day != 0 and time_of_day != 7:
            over_world_song_set = False
        player.x_coordinate = 100
        player.y_coordinate = 285
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # npc movement updates
    face_direction = random.choice(["front", "back", "left", "right"])
    face_this_npc = random.choice(npcs.sprites())
    if movement_able and in_over_world:
        npc_toc = time.perf_counter()
        if npc_toc - npc_tic > 5:
            npc_tic = time.perf_counter()
            if face_direction == "front":
                if face_this_npc.name == "Nahun":
                    nahun.update(graphic_dict["nahun_down"])
                if face_this_npc.name == "Voruke":
                    voruke.update(graphic_dict["voruke_down"])
                if face_this_npc.name == "Zerah":
                    zerah.update(graphic_dict["zerah_down"])
            if face_direction == "back":
                if face_this_npc.name == "Nahun":
                    nahun.update(graphic_dict["nahun_up"])
                if face_this_npc.name == "Voruke":
                    voruke.update(graphic_dict["voruke_up"])
                if face_this_npc.name == "Zerah":
                    zerah.update(graphic_dict["zerah_up"])
            if face_direction == "left":
                if face_this_npc.name == "Nahun":
                    nahun.update(graphic_dict["nahun_left"])
                if face_this_npc.name == "Voruke":
                    voruke.update(graphic_dict["voruke_left"])
                if face_this_npc.name == "Zerah":
                    zerah.update(graphic_dict["zerah_left"])
            if face_direction == "right":
                if face_this_npc.name == "Nahun":
                    nahun.update(graphic_dict["nahun_right"])
                if face_this_npc.name == "Voruke":
                    voruke.update(graphic_dict["voruke_right"])
                if face_this_npc.name == "Zerah":
                    zerah.update(graphic_dict["zerah_right"])

    # info to return to main loop --------------------------------------------------------------------------------------
    korlok_return = {"over_world_song_set": over_world_song_set, "korlok_attuned": korlok_attuned,
                     "enemy_tic": enemy_tic, "npc_tic": npc_tic, "info_text_1": info_text_1,
                     "info_text_2": info_text_2, "info_text_3": info_text_3, "info_text_4": info_text_4,
                     "interacted": interacted, "in_over_world": in_over_world, "in_battle": in_battle,
                     "in_shop": in_shop, "in_academia": in_academia, "in_inn": in_inn,
                     "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                     "current_enemy_battling": current_enemy_battling,
                     "current_building_entering": current_building_entering,
                     "current_npc_interacting": current_npc_interacting,
                     "in_apothecary": in_apothecary, "rock_4_con": rock_4_con, "rock_5_con": rock_5_con,
                     "rock_6_con": rock_6_con, "worker_tic": worker_tic, "worker_delay_tic": worker_delay_tic,
                     "magmons_highlighted": magmons_highlighted, "magmons_reset": magmons_reset,
                     "snow_fall_tic": snow_fall_tic, "snow_fall_phase": snow_fall_phase}

    return korlok_return
