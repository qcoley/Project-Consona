import time
import random

import gameplay_functions
import drawing_functions
import combat_scenario
import cutscenes


def seldon_district(pygame, player, screen, graphic_dict, rohir_gate, hearth_stone, over_world_song_set,
                    seldon_overworld_music, seldon_district_bg, seldon_enemies, korlok_enemies, snakes, ghouls,
                    magmons, bandiles, interactables_seldon, interactables_korlok, Enemy, Item, UiElement,
                    most_sprites, quest_items_seldon, log_sprite_reset, snake_sprite_reset, ghoul_sprite_reset,
                    nede, quest_star_garan, quest_star_maurelle, quest_star_celeste, quest_star_torune,
                    interaction_popup, font, interacted, in_over_world, bridge_not_repaired,
                    bridge_cutscenes_not_viewed, apothis_intro_music, apothis_scene_1, apothis_scene_2,
                    apothis_scene_3, apothis_scene_4, apothis_scene_5, apothis_scene_6, skip_button,
                    player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                    muchador_battle_sprite, barrier_active, sharp_sense_active, in_npc_interaction,
                    amuna_buildings, npcs, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                    button_highlighted, button_highlight, knowledge_academia_show, knowledge_academia,
                    rest_recover_show, rest_shown_before, rest_recover, quest_guide_shown, game_guide_overlay,
                    enemy_tic, npc_tic, npc_garan, npc_maurelle, npc_celeste, npc_torune, info_text_1, info_text_2,
                    info_text_3, info_text_4, in_battle, in_shop, in_academia, in_inn, movement_able,
                    current_enemy_battling, current_npc_interacting, current_building_entering,
                    magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite, interactables_mines,
                    equipment_screen, staff, sword, bow,
                    offense_meter, defense_meter, weapon_select, player_cutscene, player_cutscene_2, beyond_seldon,
                    flowers, eldream_flowers, interactables_eldream, pet_energy_window, ectrenos_front_enemies,
                    necrola_battle_sprite, osodark_battle_sprite, tree_top_1, tree_top_2, tree_top_3, building_top_1,
                    building_top_2, building_top_3, sfx_item_pickup, sfx_flower, sfx_door, worker_1, worker_tic,
                    worker_positions, worker_move_tic, log_pile, SCREEN_WIDTH, SCREEN_HEIGHT, game_window,
                    stelli_battle_sprite, vanished, vanish_overlay, erebyth_defeated, basic_fish_counter,
                    better_fish_counter, even_better_fish_counter, best_fish_counter, barrier_small, apothis_gift,
                    snakes_highlighted, ghouls_highlighted, quest_logs_highlighted, apothis_upgrade, dawn,
                    early_morning, morning, early_afternoon, afternoon, dusk, night, time_of_day, apothis_scene_1_night,
                    apothis_scene_2_night, apothis_scene_3_night, apothis_scene_4_night, apothis_scene_5_night,
                    apothis_scene_6_night, stardust_stelli, kasper_unlocked, torok_unlocked, iriana_unlocked,
                    kasper_battle_sprite, torok_battle_sprite, iriana_battle_sprite, night_music):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            if time_of_day == 0 or time_of_day == 7:
                pygame.mixer.music.load(night_music)
            else:
                pygame.mixer.music.load(seldon_overworld_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(seldon_district_bg, (0, 0))
    respawned_dict = gameplay_functions.enemy_respawn(player, seldon_enemies, korlok_enemies, snakes, ghouls, magmons,
                                                      bandiles, interactables_seldon, interactables_korlok,
                                                      interactables_mines, Enemy, Item, graphic_dict, UiElement,
                                                      flowers, eldream_flowers, interactables_eldream,
                                                      ectrenos_front_enemies, ectrenos_front_enemies,
                                                      ectrenos_front_enemies, ectrenos_front_enemies, snakes,
                                                      False, False, False, False, time_of_day)
    seldon_enemies = respawned_dict["seldon_enemies"]
    snakes = respawned_dict["snakes"]
    ghouls = respawned_dict["ghouls"]
    flowers = respawned_dict["seldon_flowers"]
    interactables_seldon = respawned_dict["interactables_seldon"]

    if player.quest_status["village repairs"] and not player.quest_complete["village repairs"]:
        if not quest_logs_highlighted:
            for quest_item in quest_items_seldon:
                if quest_item.name == "Pine logs":
                    quest_item.update(quest_item.x_coordinate, quest_item.y_coordinate,
                                      graphic_dict["pine_logs_high_img"])
            quest_logs_highlighted = True
    if player.quest_complete["village repairs"]:
        if not log_sprite_reset:
            for quest_item in quest_items_seldon:
                if quest_item.name == "Pine logs":
                    quest_item.update(quest_item.x_coordinate, quest_item.y_coordinate,
                                      graphic_dict["pine_logs_img"])
            if log_pile.level == 0:
                log_pile.update_level(log_pile.name, 1, graphic_dict["pine_logs_piled_img"])
            log_sprite_reset = True

    if player.quest_status["sneaky snakes"] and not player.quest_complete["sneaky snakes"]:
        if not snakes_highlighted:
            for enemy_sprite in seldon_enemies:
                if enemy_sprite.name == "Snake":
                    if time_of_day == 0 or time_of_day == 7:
                        enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                                  graphic_dict["snake_high_night"])
                    else:
                        enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                                  graphic_dict["snake_high"])
            snakes_highlighted = True
    if player.quest_complete["sneaky snakes"]:
        if not snake_sprite_reset:
            for enemy_sprite in seldon_enemies:
                if enemy_sprite.name == "Snake":
                    if time_of_day == 0 or time_of_day == 7:
                        enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                                  graphic_dict["snake_night"])
                    else:
                        enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                                  graphic_dict["snake"])
            snake_sprite_reset = True

    if player.quest_status["ghouled again"] and not player.quest_complete["ghouled again"]:
        if not ghouls_highlighted:
            for enemy_sprite in seldon_enemies:  # update enemy sprite to a highlighted version
                if enemy_sprite.name == "Ghoul":
                    enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                              graphic_dict["ghoul_high"])
            ghouls_highlighted = True
    if player.quest_complete["ghouled again"]:
        if not ghoul_sprite_reset:
            for enemy_sprite in seldon_enemies:
                if enemy_sprite.name == "Ghoul":
                    enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                              graphic_dict["ghoul"])
            ghoul_sprite_reset = True

    screen.blit(log_pile.surf, log_pile.rect)
    for entity in most_sprites:
        if entity.name == "Celeste":
            if time_of_day != 0 and time_of_day != 7:
                screen.blit(entity.surf, entity.rect)
            else:
                if not player.quest_complete["where's nede?"]:
                    screen.blit(entity.surf, entity.rect)
        else:
            screen.blit(entity.surf, entity.rect)
    for flower in flowers:
        screen.blit(flower.surf, flower.rect)
    if not player.quest_complete["village repairs"]:
        for quest_item in quest_items_seldon:
            screen.blit(quest_item.surf, quest_item.rect)
    for enemy_sprite in seldon_enemies:
        screen.blit(enemy_sprite.surf, enemy_sprite.rect)
    if player.quest_progress["where's nede?"] == 1:
        screen.blit(nede.surf, nede.rect)

    if time_of_day != 0 and time_of_day != 7:
        if not erebyth_defeated:
            screen.blit(worker_1.surf, worker_1.rect)

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

    screen.blit(tree_top_1.surf, tree_top_1.rect)
    screen.blit(tree_top_2.surf, tree_top_2.rect)
    screen.blit(tree_top_3.surf, tree_top_3.rect)
    if len(drawing_functions.character_sheet_window) == 0 and len(drawing_functions.game_guide_container) == 0 \
            and len(drawing_functions.journal_window) == 0:
        screen.blit(building_top_1.surf, building_top_1.rect)
        screen.blit(building_top_2.surf, building_top_2.rect)
        screen.blit(building_top_3.surf, building_top_3.rect)

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

    if not player.quest_complete["sneaky snakes"]:
        screen.blit(quest_star_garan.surf, quest_star_garan.rect)
    if not player.quest_complete["where's nede?"]:
        screen.blit(quest_star_celeste.surf, quest_star_celeste.rect)
    if not player.quest_complete["village repairs"]:
        screen.blit(quest_star_maurelle.surf, quest_star_maurelle.rect)
    if not player.quest_complete["ghouled again"]:
        screen.blit(quest_star_torune.surf, quest_star_torune.rect)

    # player encounters objects and draws popup information box --------------------------------------------------------
    # player encounters a quest item. check progress and add to if interacted with
    quest_item = pygame.sprite.spritecollideany(player, quest_items_seldon, pygame.sprite.collide_rect_ratio(0.75))
    try:
        interaction_popup.update(quest_item.x_coordinate, quest_item.y_coordinate - 25,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(quest_item.name), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (quest_item.x_coordinate, quest_item.y_coordinate - 25)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if quest_item.name == "Pine logs":
            if not player.quest_complete["village repairs"]:
                if player.quest_status["village repairs"]:
                    if player.quest_progress["village repairs"] < 4:
                        if len(player.items) < 16:
                            info_text_1 = "Press 'F' key to gather the pine log."
                            info_text_2 = ""
                            info_text_3 = ""
                            info_text_4 = ""
                        else:
                            info_text_1 = "Inventory is full. "
                            info_text_2 = ""
                            info_text_3 = ""
                            info_text_4 = ""

                    else:
                        info_text_1 = "You've already gathered these."
                        info_text_2 = ""
                        info_text_3 = ""
                        info_text_4 = ""

                    if interacted and in_over_world:
                        if player.quest_progress["village repairs"] < 4:
                            if len(player.items) < 16:
                                player.quest_progress["village repairs"] += 1
                                player.items.append(Item("pine log", "log", 200, 200, graphic_dict["log"], 0))
                                pygame.mixer.find_channel(True).play(sfx_item_pickup)
                                quest_item.kill()
                                interacted = False
                            else:
                                info_text_1 = "Inventory is full."
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                                interacted = False
                        else:
                            info_text_1 = "You've already gathered these."
                            info_text_2 = ""
                            info_text_3 = ""
                            info_text_4 = ""
                            interacted = False
                else:
                    info_text_1 = "That's some nice pine."
                    info_text_2 = ""
                    info_text_3 = ""
                    info_text_4 = ""
                    if interacted:
                        interacted = False

        if quest_item.model == "rohir gate":
            if player.quest_complete["ghouled again"]:
                info_text_1 = "Press 'F' key to enter Korlok District."

                if interacted and in_over_world:
                    if not erebyth_defeated:
                        if bridge_cutscenes_not_viewed:
                            if time_of_day == 0 or time_of_day == 7:
                                if player.race == "amuna":
                                    if player.gender == "male":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["amuna_cutscene_night"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["amuna_cutscene_2_night"])
                                    if player.gender == "female":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["amuna_cutscene_female_night"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["amuna_cutscene_2_female_night"])
                                if player.race == "nuldar":
                                    if player.gender == "male":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["nuldar_cutscene_night"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["nuldar_cutscene_2_night"])
                                    if player.gender == "female":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["nuldar_cutscene_female_night"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["nuldar_cutscene_2_female_night"])
                                if player.race == "sorae":
                                    if player.gender == "male":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["sorae_cutscene_night"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["sorae_cutscene_2_night"])
                                    if player.gender == "female":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["sorae_cutscene_beta_night"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["sorae_cutscene_2_beta_night"])
                            else:
                                if player.race == "amuna":
                                    if player.gender == "male":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["amuna_cutscene"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["amuna_cutscene_2"])
                                    if player.gender == "female":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["amuna_cutscene_female"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["amuna_cutscene_2_female"])
                                if player.race == "nuldar":
                                    if player.gender == "male":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["nuldar_cutscene"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["nuldar_cutscene_2"])
                                    if player.gender == "female":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["nuldar_cutscene_female"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["nuldar_cutscene_2_female"])
                                if player.race == "sorae":
                                    if player.gender == "male":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["sorae_cutscene"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["sorae_cutscene_2"])
                                    if player.gender == "female":
                                        player_cutscene.update(player_cutscene.x_coordinate,
                                                               player_cutscene.y_coordinate,
                                                               graphic_dict["sorae_cutscene_beta"])
                                        player_cutscene_2.update(player_cutscene_2.x_coordinate,
                                                                 player_cutscene_2.y_coordinate,
                                                                 graphic_dict["sorae_cutscene_2_beta"])
                            cutscene_tic = time.perf_counter()
                            cutscenes.cutscenes_apothis_bridge(pygame, apothis_intro_music, screen, apothis_scene_1,
                                                               apothis_scene_2, apothis_scene_3, apothis_scene_4,
                                                               apothis_scene_5, apothis_scene_6, cutscene_tic,
                                                               skip_button, player_cutscene, player_cutscene_2,
                                                               SCREEN_WIDTH, SCREEN_HEIGHT, game_window, time_of_day,
                                                               apothis_scene_1_night, apothis_scene_2_night,
                                                               apothis_scene_3_night, apothis_scene_4_night,
                                                               apothis_scene_5_night, apothis_scene_6_night)
                            bridge_cutscenes_not_viewed = False
                        player.x_coordinate = 900
                        player.y_coordinate = 400
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                        player.current_zone = "rohir"
                        interacted = False
                        over_world_song_set = False
                    else:
                        player.x_coordinate = 525
                        player.y_coordinate = 575
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                        rohir_gate.update(525, 600, graphic_dict["rohir_gate"])
                        player.current_zone = "korlok"
                        interacted = False
                        over_world_song_set = False

                        if time_of_day == 0 or time_of_day == 7:
                            for magmon in magmons:
                                if (player.quest_status["elementary elementals"]
                                        and not player.quest_complete["elementary elementals"]):
                                    magmon.update_image(magmon.x_coordinate, magmon.y_coordinate,
                                                        graphic_dict["magmon_high_night"])
                                else:
                                    magmon.update_image(magmon.x_coordinate, magmon.y_coordinate,
                                                        graphic_dict["magmon_night"])
                        else:
                            for magmon in magmons:
                                if (player.quest_status["elementary elementals"]
                                        and not player.quest_complete["elementary elementals"]):
                                    magmon.update_image(magmon.x_coordinate, magmon.y_coordinate,
                                                        graphic_dict["magmon_high"])
                                else:
                                    magmon.update_image(magmon.x_coordinate, magmon.y_coordinate,
                                                        graphic_dict["magmon"])
            else:
                info_text_1 = "The gate seems to be locked shut."
                info_text_2 = "Perhaps the nearby Guard knows why?"
                if interacted:
                    interacted = False

    except AttributeError:
        pass

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, seldon_enemies, pygame.sprite.collide_rect_ratio(0.75))
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

    # player collides with building, enters if chosen to interact and starts related scenario
    building = pygame.sprite.spritecollideany(player, amuna_buildings, pygame.sprite.collide_rect_ratio(0.75))
    if building and in_over_world:

        interaction_popup.update(building.x_coordinate, building.y_coordinate - 50, graphic_dict["popup_interaction"])
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
        if building.name == "Academia":
            info_text_1 = "Press 'F' key to enter Academia."
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
            if building.name == "Academia":
                in_academia = True
                pygame.mixer.find_channel(True).play(sfx_door)
                current_building_entering = building
                movement_able = False
                in_over_world = False
                over_world_song_set = False
                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
            interacted = False

    # player collides with flower, if collected adds to player flower count
    flower = pygame.sprite.spritecollideany(player, flowers, pygame.sprite.collide_rect_ratio(0.75))
    if flower and in_over_world:
        flower.update(flower.x_coordinate, flower.y_coordinate, graphic_dict["flower_seldon_high"])
        if interacted:
            pygame.mixer.find_channel(True).play(sfx_flower)
            player.flowers_amuna += 1
            flower.kill()
            info_text_1 = "You collected the Seldon Flower."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""
            interacted = False

    # resets flower surface to non-highlighted if not currently interacting
    for flow in flowers:
        if flow.surf == graphic_dict["flower_seldon_high"]:
            if flow != flower:
                flow.surf = graphic_dict["flower_seldon"]

    # if player collides with npc sprite and chooses to interact with it
    npc = pygame.sprite.spritecollideany(player, npcs, pygame.sprite.collide_rect_ratio(0.75))
    if npc:
        if npc.name == "Celeste":
            if time_of_day != 0 and time_of_day != 7:
                interaction_popup.update(npc.x_coordinate, npc.y_coordinate - 50,
                                         graphic_dict["popup_interaction_purple"])
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
                    current_npc_interacting = npc
                    in_over_world = False
                    in_npc_interaction = True
                    movement_able = False
                    drawing_functions.loot_popup_container.clear()
                    drawing_functions.loot_text_container.clear()
                    combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                            sharp_sense_active,
                                                            graphic_dict, kasper_unlocked, torok_unlocked,
                                                            iriana_unlocked,
                                                            kasper_battle_sprite, torok_battle_sprite,
                                                            iriana_battle_sprite)
            else:
                if not player.quest_complete["where's nede?"]:
                    interaction_popup.update(npc.x_coordinate, npc.y_coordinate - 50,
                                             graphic_dict["popup_interaction_purple"])
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
                        current_npc_interacting = npc
                        in_over_world = False
                        in_npc_interaction = True
                        movement_able = False
                        drawing_functions.loot_popup_container.clear()
                        drawing_functions.loot_text_container.clear()
                        combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                                sharp_sense_active,
                                                                graphic_dict, kasper_unlocked, torok_unlocked,
                                                                iriana_unlocked,
                                                                kasper_battle_sprite, torok_battle_sprite,
                                                                iriana_battle_sprite)
        else:
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
                current_npc_interacting = npc
                in_over_world = False
                in_npc_interaction = True
                movement_able = False
                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active,
                                                        graphic_dict, kasper_unlocked, torok_unlocked, iriana_unlocked,
                                                        kasper_battle_sprite, torok_battle_sprite, iriana_battle_sprite)

    if pygame.sprite.collide_rect(player, hearth_stone):
        interaction_popup.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Hearth stone"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25)
        screen.blit(interaction_info_surf, interaction_info_rect)
        if interacted:
            interacted = False

    if pygame.Rect.colliderect(player.rect, barrier_small):
        interaction_popup.update(970, 260,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Marrow"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (970, 260)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if apothis_gift:
            info_text_1 = "Press 'F' key to enter Marrow."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world:
                over_world_song_set = False
                interacted = False
                player.current_zone = "marrow"
                player.x_coordinate = 175
                player.y_coordinate = 335
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

        else:
            info_text_1 = "The barrier is held preventing entry."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""
            if interacted:
                interacted = False

    # --------------------------------------------------------------------------------------------------
    # pop up notifications for situations like low health or first weapon acquire
    if not knowledge_academia_show and not beyond_seldon:
        if player.race == "amuna":
            if player.mage_level == 2 or player.fighter_level == 2:
                drawing_functions.knowledge_academia_window.append(knowledge_academia)
                knowledge_academia_show = True
        if player.race == "nuldar":
            if player.mage_level == 2 or player.scout_level == 2:
                drawing_functions.knowledge_academia_window.append(knowledge_academia)
                knowledge_academia_show = True
        if player.race == "sorae":
            if player.fighter_level == 2 or player.scout_level == 2:
                drawing_functions.knowledge_academia_window.append(knowledge_academia)
                knowledge_academia_show = True
    if rest_recover_show:
        if not rest_shown_before and not beyond_seldon:
            drawing_functions.rest_recover_window.append(rest_recover)
            rest_recover_show = False
            rest_shown_before = True

    # draw pop up notifications on top of everything else
    if len(drawing_functions.knowledge_academia_window) > 0:
        for knowledge_window_notification in drawing_functions.knowledge_academia_window:
            screen.blit(knowledge_window_notification.surf,
                        knowledge_window_notification.rect)
    if len(drawing_functions.rest_recover_window) > 0:
        for rest_window in drawing_functions.rest_recover_window:
            screen.blit(rest_window.surf, rest_window.rect)
    if len(drawing_functions.first_quest_window) > 0:
        for quest_window in drawing_functions.first_quest_window:
            screen.blit(quest_window.surf, quest_window.rect)
    if len(drawing_functions.first_item_window) > 0:
        for item_window in drawing_functions.first_item_window:
            screen.blit(item_window.surf, item_window.rect)

    # move player to nascent grove when they approach
    if 375 < player.x_coordinate < 475 and player.y_coordinate > 700:
        player.current_zone = "nascent"
        in_over_world = True
        if time_of_day != 0 and time_of_day != 7:
            over_world_song_set = False
        player.x_coordinate = 750
        player.y_coordinate = 125
    # move player to stardust outpost when they approach
    if player.x_coordinate < 30 and 325 < player.y_coordinate < 400:
        player.current_zone = "stardust"
        if time_of_day != 0 and time_of_day != 7:
            over_world_song_set = False
        in_over_world = True
        player.x_coordinate = 925
        player.y_coordinate = 275

        if time_of_day == 0 or time_of_day == 7:
            for stelli in stardust_stelli:
                if stelli.name == "Stellia":
                    stelli.update_image(stelli.x_coordinate, stelli.y_coordinate,
                                        graphic_dict["stelli_a_night"])
                if stelli.name == "Stellib":
                    stelli.update_image(stelli.x_coordinate, stelli.y_coordinate,
                                        graphic_dict["stelli_b_night"])
                if stelli.name == "Stellic":
                    stelli.update_image(stelli.x_coordinate, stelli.y_coordinate,
                                        graphic_dict["stelli_c_night"])
        else:
            for stelli in stardust_stelli:
                if stelli.name == "Stellia":
                    stelli.update_image(stelli.x_coordinate, stelli.y_coordinate,
                                        graphic_dict["stelli_a"])
                if stelli.name == "Stellib":
                    stelli.update_image(stelli.x_coordinate, stelli.y_coordinate,
                                        graphic_dict["stelli_b"])
                if stelli.name == "Stellic":
                    stelli.update_image(stelli.x_coordinate, stelli.y_coordinate,
                                        graphic_dict["stelli_c"])

    # enemy movement updates
    direction_horizontal = random.choice(["left", "right"])
    direction_vertical = random.choice(["up", "down"])
    if time_of_day != 0 and time_of_day != 7:
        move_snake = random.choice(snakes.sprites())
    move_ghoul = random.choice(ghouls.sprites())
    if movement_able and in_over_world:
        enemy_toc = time.perf_counter()
        if enemy_toc - enemy_tic > 1:
            enemy_tic = time.perf_counter()
            if time_of_day != 0 and time_of_day != 7:
                move_snake.update_position([100, 300], [200, 300], direction_horizontal, direction_vertical)
            move_ghoul.update_position([700, 900], [200, 300], direction_horizontal, direction_vertical)

    # worker animation updates
    if time_of_day != 0 and time_of_day != 7:
        if movement_able and in_over_world and not erebyth_defeated:
            worker_toc = time.perf_counter()
            if worker_toc - worker_tic > 0.75:
                worker_tic = time.perf_counter()
                match worker_1.gift:
                    case True:
                        worker_1.gift = False
                        worker_1.update(graphic_dict["worker_1_a"])
                    case False:
                        worker_1.gift = True
                        worker_1.update(graphic_dict["worker_1_b"])

            worker_move_toc = time.perf_counter()
            if worker_move_toc - worker_move_tic > 20:
                worker_move_tic = time.perf_counter()
                worker_position = random.choice(worker_positions)
                worker_1.update_position(worker_position[0], worker_position[1])

    # npc movement updates
    face_direction = random.choice(["front", "back", "left", "right"])
    face_this_npc = random.choice(npcs.sprites())
    if movement_able and in_over_world:
        npc_toc = time.perf_counter()
        if npc_toc - npc_tic > 5:
            npc_tic = time.perf_counter()
            if face_direction == "front":
                if face_this_npc.name == "Garan":
                    npc_garan.update(graphic_dict["garan_down"])
                if face_this_npc.name == "Maurelle":
                    npc_maurelle.update(graphic_dict["maurelle_down"])
                if face_this_npc.name == "Celeste":
                    npc_celeste.update(graphic_dict["celeste_down"])
                if face_this_npc.name == "Torune":
                    npc_torune.update(graphic_dict["torune_down"])
            if face_direction == "back":
                if face_this_npc.name == "Garan":
                    npc_garan.update(graphic_dict["garan_up"])
                if face_this_npc.name == "Maurelle":
                    npc_maurelle.update(graphic_dict["maurelle_up"])
                if face_this_npc.name == "Celeste":
                    npc_celeste.update(graphic_dict["celeste_up"])
                if face_this_npc.name == "Torune":
                    npc_torune.update(graphic_dict["torune_up"])
            if face_direction == "left":
                if face_this_npc.name == "Garan":
                    npc_garan.update(graphic_dict["garan_left"])
                if face_this_npc.name == "Maurelle":
                    npc_maurelle.update(graphic_dict["maurelle_left"])
                if face_this_npc.name == "Celeste":
                    npc_celeste.update(graphic_dict["celeste_left"])
                if face_this_npc.name == "Torune":
                    npc_torune.update(graphic_dict["torune_left"])
            if face_direction == "right":
                if face_this_npc.name == "Garan":
                    npc_garan.update(graphic_dict["garan_right"])
                if face_this_npc.name == "Maurelle":
                    npc_maurelle.update(graphic_dict["maurelle_right"])
                if face_this_npc.name == "Celeste":
                    npc_celeste.update(graphic_dict["celeste_right"])
                if face_this_npc.name == "Torune":
                    npc_torune.update(graphic_dict["torune_right"])

    seldon_return = {"over_world_song_set": over_world_song_set, "interactables_seldon": interactables_seldon,
                     "interactables_korlok": interactables_korlok, "korlok_enemies": korlok_enemies, "magmons": magmons,
                     "bandiles": bandiles, "log_sprite_reset": log_sprite_reset,
                     "snake_sprite_reset": snake_sprite_reset, "ghoul_sprite_reset": ghoul_sprite_reset,
                     "bridge_cutscenes_not_viewed": bridge_cutscenes_not_viewed,
                     "current_enemy_battling": current_enemy_battling,
                     "current_building_entering": current_building_entering,
                     "current_npc_interacting": current_npc_interacting,
                     "knowledge_academia_show": knowledge_academia_show, "rest_recover_show": rest_recover_show,
                     "rest_shown_before": rest_shown_before, "quest_guide_shown": quest_guide_shown,
                     "enemy_tic": enemy_tic, "npc_tic": npc_tic,
                     "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                     "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                     "in_battle": in_battle, "in_shop": in_shop, "in_academia": in_academia, "in_inn": in_inn,
                     "in_npc_interaction": in_npc_interaction, "movement_able": movement_able,
                     "beyond_seldon": beyond_seldon, "worker_tic": worker_tic, "worker_move_tic": worker_move_tic,
                     "snakes_highlighted": snakes_highlighted, "ghouls_highlighted": ghouls_highlighted,
                     "quest_logs_highlighted": quest_logs_highlighted}

    return seldon_return
