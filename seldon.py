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
                    amuna_buildings, npcs, save_check_window, user_interface, world_map_container, bar_backdrop,
                    hp_bar, en_bar, xp_bar, offense_upgraded, defense_upgraded, level_up_font, button_highlighted,
                    button_highlight, knowledge_academia_show, knowledge_academia, rest_recover_show,
                    rest_shown_before, rest_recover, quest_guide_shown, game_guide_overlay, role_guide_shown,
                    enemy_tic, npc_tic, npc_garan, npc_maurelle, npc_celeste, npc_torune, info_text_1, info_text_2,
                    info_text_3, info_text_4, in_battle, in_shop, in_academia, in_inn, movement_able,
                    current_enemy_battling, current_npc_interacting, current_building_entering,
                    magmon_battle_sprite, bandile_battle_sprite):

    rohir_gate.update(525, 50, graphic_dict["rohir_gate"])
    hearth_stone.update(860, 595, graphic_dict["hearth_stone"])

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(seldon_overworld_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(seldon_district_bg, (0, 0))
    respawned_dict = gameplay_functions.enemy_respawn(seldon_enemies, korlok_enemies, snakes, ghouls, magmons, bandiles,
                                                      interactables_seldon, interactables_korlok, Enemy, Item,
                                                      graphic_dict, UiElement)
    seldon_enemies = respawned_dict["seldon_enemies"]
    snakes = respawned_dict["snakes"]
    ghouls = respawned_dict["ghouls"]
    interactables_seldon = respawned_dict["interactables_seldon"]

    for entity in most_sprites:
        screen.blit(entity.surf, entity.rect)

    for quest_item in quest_items_seldon:
        if not player.quest_complete["village repairs"]:
            if player.quest_status["village repairs"]:
                if quest_item.name == "pine logs":
                    quest_item.update(quest_item.x_coordinate, quest_item.y_coordinate,
                                      graphic_dict["pine_logs_high_img"])
        else:
            if not log_sprite_reset:
                if quest_item.name == "pine logs":
                    quest_item.update(quest_item.x_coordinate, quest_item.y_coordinate,
                                      graphic_dict["pine_logs_img"])

    # condition to check if sprites have been reverted to original img after quest complete
    if player.quest_complete["village repairs"]:
        log_sprite_reset = True

    for enemy_sprite in seldon_enemies:  # update enemy sprite to a highlighted version
        if not player.quest_complete["sneaky snakes"]:
            if player.quest_status["sneaky snakes"]:
                if enemy_sprite.name == "snake":
                    enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                              graphic_dict["snake_high"])
        else:  # revert to original snake sprite
            if not snake_sprite_reset:
                if enemy_sprite.name == "snake":
                    enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                              graphic_dict["snake"])
        if not player.quest_complete["ghouled again"]:
            if player.quest_status["ghouled again"]:
                if enemy_sprite.name == "ghoul":
                    enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                              graphic_dict["ghoul_high"])
        else:  # revert to original ghoul sprite
            if not ghoul_sprite_reset:
                if enemy_sprite.name == "ghoul":
                    enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                              graphic_dict["ghoul"])
        screen.blit(enemy_sprite.surf, enemy_sprite.rect)

    # condition to check if sprites have been reverted to original img after quest complete
    if player.quest_complete["sneaky snakes"]:
        snake_sprite_reset = True
    if player.quest_complete["ghouled again"]:
        ghoul_sprite_reset = True
    if player.quest_progress["where's nede?"] == 1:
        screen.blit(nede.surf, nede.rect)

    gameplay_functions.npc_quest_star_updates(screen, player, quest_star_garan, quest_star_maurelle, quest_star_celeste,
                                              quest_star_torune, graphic_dict["quest_progress_star"],
                                              graphic_dict["quest_complete_star"])
    screen.blit(player.surf, player.rect)

    # player encounters objects and draws popup information box ----------------------------------------
    # player encounters a quest item. check progress and add to if interacted with
    quest_item = pygame.sprite.spritecollideany(player, quest_items_seldon)
    try:
        interaction_popup.update(quest_item.x_coordinate, quest_item.y_coordinate - 25,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(quest_item.name), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (quest_item.x_coordinate, quest_item.y_coordinate - 25)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if quest_item.name == "pine logs":
            if not player.quest_complete["village repairs"]:
                if player.quest_status["village repairs"]:
                    info_text_1 = "Press 'F' key to gather the pine log."

                    if interacted and in_over_world:
                        if player.quest_progress["village repairs"] < 4:
                            player.quest_progress["village repairs"] += 1
                            info_text_1 = "You gathered 1 pine log."
                            quest_item.kill()
                            interacted = False
                        else:
                            info_text_1 = "You've already gathered these."
                            interacted = False
            else:
                info_text_1 = "That's a nice pine log."

        if quest_item.model == "rohir gate":
            if player.quest_complete["ghouled again"]:
                info_text_1 = "Press 'F' key to enter Korlok District."

                if interacted and in_over_world:
                    if bridge_not_repaired:
                        if bridge_cutscenes_not_viewed:
                            cutscene_tic = time.perf_counter()
                            cutscenes.cutscenes_apothis_bridge(pygame, apothis_intro_music, screen, apothis_scene_1,
                                                               apothis_scene_2, apothis_scene_3, apothis_scene_4,
                                                               apothis_scene_5, apothis_scene_6, cutscene_tic,
                                                               skip_button)
                            bridge_cutscenes_not_viewed = False
                        player.x_coordinate = 900
                        player.y_coordinate = 400
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                        player.current_zone = "rohir"
                        interacted = False
                        over_world_song_set = False
                    else:
                        player.x_coordinate = 525
                        player.y_coordinate = 650
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                        rohir_gate.update(525, 600, graphic_dict["rohir_gate"])
                        player.current_zone = "korlok"
                        interacted = False
                        over_world_song_set = False
            else:
                info_text_1 = "The gate seems to be locked shut."
                info_text_2 = "Perhaps the nearby Guard knows why?"

    except AttributeError:
        pass

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, seldon_enemies)
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

    # player collides with building, enters if chosen to interact and starts related scenario
    building = pygame.sprite.spritecollideany(player, amuna_buildings)
    if building and in_over_world:

        interaction_popup.update(building.x_coordinate, building.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(building.name), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (building.x_coordinate, building.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        # lets player know if they are in range of building they can press f to enter it
        info_text_1 = "Press 'F' key to enter building."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted:
            current_building_entering = building
            movement_able = False
            in_over_world = False
            over_world_song_set = False
            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()

            if building.name == "shop":
                in_shop = True
            if building.name == "inn":
                in_inn = True
            if building.name == "academia":
                in_academia = True

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

    if pygame.sprite.collide_rect(player, hearth_stone):
        interaction_popup.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("hearth stone"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25)
        screen.blit(interaction_info_surf, interaction_info_rect)

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

    # pop up notifications for situations like low health or first weapon acquire
    if not knowledge_academia_show:
        if player.knowledge["mage"] == 50 or player.knowledge["fighter"] == 50 or \
                player.knowledge["scout"] == 50:
            drawing_functions.knowledge_academia_window.append(knowledge_academia)
            knowledge_academia_show = True
    if rest_recover_show:
        if not rest_shown_before:
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
        over_world_song_set = False
        player.x_coordinate = 750
        player.y_coordinate = 125
    # move player to stardust outpost when they approach
    if player.x_coordinate < 25 and 325 < player.y_coordinate < 400:
        player.current_zone = "stardust"
        over_world_song_set = False
        in_over_world = True
        player.x_coordinate = 925
        player.y_coordinate = 275

    # game guide popups
    if not quest_guide_shown:
        drawing_functions.game_guide_container.append(game_guide_overlay)
        quest_guide_shown = True
    if not role_guide_shown:
        if player.role == "mage" or player.role == "fighter" or player.role == "scout":
            game_guide_overlay.update(game_guide_overlay.x_coordinate, game_guide_overlay.y_coordinate,
                                      graphic_dict["guide_basics_role_img"])
            drawing_functions.game_guide_container.append(game_guide_overlay)
            role_guide_shown = True

    # enemy movement updates
    direction_horizontal = random.choice(["left", "right"])
    direction_vertical = random.choice(["up", "down"])
    move_snake = random.choice(snakes.sprites())
    move_ghoul = random.choice(ghouls.sprites())
    if movement_able and in_over_world:
        enemy_toc = time.perf_counter()
        if enemy_toc - enemy_tic > 2:
            enemy_tic = time.perf_counter()
            move_snake.update_position([100, 300], [200, 300], direction_horizontal, direction_vertical)
            move_ghoul.update_position([700, 900], [200, 300], direction_horizontal, direction_vertical)

    # npc movement updates
    face_direction = random.choice(["front", "back", "left", "right"])
    face_this_npc = random.choice(npcs.sprites())
    if movement_able and in_over_world:
        npc_toc = time.perf_counter()
        if npc_toc - npc_tic > 5:
            npc_tic = time.perf_counter()
            if face_direction == "front":
                if face_this_npc.name == "garan":
                    npc_garan.update(graphic_dict["garan_down"])
                if face_this_npc.name == "maurelle":
                    npc_maurelle.update(graphic_dict["maurelle_down"])
                if face_this_npc.name == "celeste":
                    npc_celeste.update(graphic_dict["celeste_down"])
                if face_this_npc.name == "torune":
                    npc_torune.update(graphic_dict["torune_down"])
            if face_direction == "back":
                if face_this_npc.name == "garan":
                    npc_garan.update(graphic_dict["garan_up"])
                if face_this_npc.name == "maurelle":
                    npc_maurelle.update(graphic_dict["maurelle_up"])
                if face_this_npc.name == "celeste":
                    npc_celeste.update(graphic_dict["celeste_up"])
                if face_this_npc.name == "torune":
                    npc_torune.update(graphic_dict["torune_up"])
            if face_direction == "left":
                if face_this_npc.name == "garan":
                    npc_garan.update(graphic_dict["garan_left"])
                if face_this_npc.name == "maurelle":
                    npc_maurelle.update(graphic_dict["maurelle_left"])
                if face_this_npc.name == "celeste":
                    npc_celeste.update(graphic_dict["celeste_left"])
                if face_this_npc.name == "torune":
                    npc_torune.update(graphic_dict["torune_left"])
            if face_direction == "right":
                if face_this_npc.name == "garan":
                    npc_garan.update(graphic_dict["garan_right"])
                if face_this_npc.name == "maurelle":
                    npc_maurelle.update(graphic_dict["maurelle_right"])
                if face_this_npc.name == "celeste":
                    npc_celeste.update(graphic_dict["celeste_right"])
                if face_this_npc.name == "torune":
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
                     "role_guide_shown": role_guide_shown, "enemy_tic": enemy_tic, "npc_tic": npc_tic,
                     "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                     "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                     "in_battle": in_battle, "in_shop": in_shop, "in_academia": in_academia, "in_inn": in_inn,
                     "in_npc_interaction": in_npc_interaction, "movement_able": movement_able}

    return seldon_return
