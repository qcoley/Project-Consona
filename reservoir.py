import drawing_functions
import combat_scenario


def reservoir_a(pygame, screen, SCREEN_HEIGHT, graphic_dict, player, reservoir_a_bg, reservoir_music,
                over_world_song_set, interaction_popup, font, save_check_window, user_interface, world_map_container,
                loot_popup_container, loot_text_container, bar_backdrop, hp_bar, en_bar, xp_bar,
                button_highlighted, button_highlight, in_over_world, interacted,
                info_text_1, info_text_2, info_text_3, info_text_4, switch_1, dungeon_switch_1, switch_2,
                dungeon_switch_2, switch_3, dungeon_switch_3, dungeon_walls, dungeon_items, dungeon_teleporter,
                mini_boss_1, dungeon_drop_wall, chorizon_1, mini_boss_2, chorizon_2, crate_1, Item, crate_2, crate_3,
                crate_4, mini_boss_1_defeated, mini_boss_2_defeated, boss_enemies, player_battle_sprite,
                snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite,
                barrier_active, sharp_sense_active, in_npc_interaction, magmon_battle_sprite, bandile_battle_sprite,
                chinzilla_battle_sprite):

    in_battle = False

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(reservoir_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    # set switches to active graphics, or inactive, depending on their current condition
    if switch_1:
        dungeon_switch_1.update(dungeon_switch_1.x_coordinate, dungeon_switch_1.y_coordinate,
                                graphic_dict["dungeon_switch_active"])
    if not switch_1:
        dungeon_switch_1.update(dungeon_switch_1.x_coordinate, dungeon_switch_1.y_coordinate,
                                graphic_dict["dungeon_switch_inactive"])
    if switch_2:
        dungeon_switch_2.update(dungeon_switch_2.x_coordinate, dungeon_switch_2.y_coordinate,
                                graphic_dict["dungeon_switch_active"])
    if not switch_2:
        dungeon_switch_2.update(dungeon_switch_2.x_coordinate, dungeon_switch_2.y_coordinate,
                                graphic_dict["dungeon_switch_inactive"])
    if switch_3:
        dungeon_switch_1.update(dungeon_switch_1.x_coordinate, dungeon_switch_1.y_coordinate,
                                graphic_dict["dungeon_switch_full"])
        dungeon_switch_2.update(dungeon_switch_2.x_coordinate, dungeon_switch_2.y_coordinate,
                                graphic_dict["dungeon_switch_full"])
        dungeon_switch_3.update(dungeon_switch_3.x_coordinate, dungeon_switch_3.y_coordinate,
                                graphic_dict["dungeon_switch_full"])

    screen.blit(reservoir_a_bg, (0, 0))
    for wall in dungeon_walls:
        screen.blit(wall.surf, wall.rect)
    for item in dungeon_items:
        screen.blit(item.surf, item.rect)
    dungeon_teleporter.update(519, 316, graphic_dict["dungeon_teleporter"])
    if switch_3:
        screen.blit(dungeon_teleporter.surf, dungeon_teleporter.rect)
    if mini_boss_1:
        dungeon_drop_wall.update(310, 224, graphic_dict["dungeon_drop_wall"])
        screen.blit(dungeon_drop_wall.surf, dungeon_drop_wall.rect)
        screen.blit(chorizon_1.surf, chorizon_1.rect)
    if mini_boss_2:
        dungeon_drop_wall.update(722, 224, graphic_dict["dungeon_drop_wall"])
        screen.blit(dungeon_drop_wall.surf, dungeon_drop_wall.rect)
        screen.blit(chorizon_2.surf, chorizon_2.rect)
    screen.blit(player.surf, player.rect)

    # move player back to rohir if they approach dungeon exit
    if 680 > player.x_coordinate > 365 and SCREEN_HEIGHT - 25 < player.y_coordinate:
        player.current_zone = "rohir"
        over_world_song_set = False
        in_over_world = True
        player.x_coordinate = 100
        player.y_coordinate = 375

    item = pygame.sprite.spritecollideany(player, dungeon_items)
    if item:
        interaction_popup.update(item.x_coordinate, item.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(item.type), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (item.x_coordinate, item.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted:
            if item.name == "dungeon crate 1":
                if not crate_1:
                    if len(player.items) < 16:
                        info_text_1 = "You found a health potion!"
                        info_text_2 = ""
                        player.items.append(Item("health potion", "potion", 200, 200,
                                                 graphic_dict["health_pot_img"]))
                        crate_1 = True
                        item.kill()
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""
            if item.name == "dungeon crate 2":
                if not crate_2:
                    if len(player.items) < 16:
                        info_text_1 = "You found a golden key!"
                        info_text_2 = ""
                        player.items.append(Item("boss key", "key", 200, 200,
                                                 graphic_dict["key_img"]))
                        crate_2 = True
                        item.kill()
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""
            if item.name == "dungeon crate 3":
                if not crate_3:
                    if len(player.items) < 16:
                        info_text_1 = "You found a health potion!"
                        info_text_2 = ""
                        player.items.append(Item("health potion", "potion", 200, 200,
                                                 graphic_dict["health_pot_img"]))
                        crate_3 = True
                        item.kill()
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""
            if item.name == "dungeon crate 4":
                if not crate_4:
                    if len(player.items) < 16:
                        info_text_1 = "You found an energy potion!"
                        info_text_2 = ""
                        player.items.append(Item("energy potion", "potion", 200, 200,
                                                 graphic_dict["energy_pot_img"]))
                        crate_4 = True
                        item.kill()
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""
            if item.name == "dungeon switch 1":
                if not switch_1:
                    info_text_1 = "You activated the first switch!"
                    if not mini_boss_1_defeated:
                        info_text_2 = "It seems your path is blocked."
                    switch_1 = True
                    if not mini_boss_1_defeated:
                        mini_boss_1 = True
                else:
                    info_text_1 = "This switch appears active."
                    info_text_2 = ""
            if item.name == "dungeon switch 2":
                if not switch_2:
                    info_text_1 = "You activated the second switch!"
                    if not mini_boss_2_defeated:
                        info_text_2 = "It seems your path is blocked."
                    switch_2 = True
                    if not mini_boss_2_defeated:
                        mini_boss_2 = True
                else:
                    info_text_1 = "This switch appears active."
                    info_text_2 = ""
            if item.name == "dungeon switch 3":
                if switch_1 and switch_2:
                    info_text_1 = "You activated the final switch!"
                    info_text_2 = "Use the teleporter to proceed."
                    switch_3 = True
                else:
                    info_text_1 = "Requires activation sequence."
                    info_text_2 = ""
            interacted = False

    if mini_boss_1 or mini_boss_2:
        boss_enemy = pygame.sprite.spritecollideany(player, boss_enemies)
        if boss_enemy:
            interaction_popup.update(boss_enemy.x_coordinate, boss_enemy.y_coordinate - 40,
                                     graphic_dict["popup_interaction_red"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str(boss_enemy.kind) + " lvl " + str(boss_enemy.level), True, "black",
                                                (255, 204, 203))
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (boss_enemy.x_coordinate, boss_enemy.y_coordinate - 40)
            screen.blit(interaction_info_surf, interaction_info_rect)

            # lets player know if they are in range of enemy they can press f to attack it
            info_text_1 = "Press 'F' key to attack enemy."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world:
                current_enemy_battling = boss_enemy
                in_over_world = False
                in_battle = True

                loot_popup_container.clear()
                loot_text_container.clear()
                combat_scenario.resting_animation(player, current_enemy_battling, player_battle_sprite,
                                                  snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                                                  muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite,
                                                  chinzilla_battle_sprite, barrier_active, sharp_sense_active,
                                                  in_battle, in_npc_interaction, graphic_dict)

    # player defeats mini bosses and activates teleporter
    if pygame.sprite.collide_rect(player, dungeon_teleporter):
        interaction_popup.update(dungeon_teleporter.x_coordinate, dungeon_teleporter.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("teleporter"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (dungeon_teleporter.x_coordinate, dungeon_teleporter.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted:
            if switch_3:
                dungeon_teleporter.update(880, 525, graphic_dict["dungeon_teleporter"])
                player.current_zone = "reservoir b"
                in_over_world = True
                interacted = False
                player.x_coordinate = 880
                player.y_coordinate = 560
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        screen.blit(ui_elements.surf, ui_elements.rect)
    for maps in world_map_container:
        screen.blit(maps.surf, maps.rect)

    if len(loot_popup_container) > 0:
        for popup in loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(loot_text_container) > 0:
        for loot_text in loot_text_container:
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

    # info to return to main loop --------------------------------------------------------------------------------------
    reservoir_a_return = {"over_world_song_set": over_world_song_set, "interacted": interacted, "crate_1": crate_1,
                          "crate_2": crate_2, "crate_3": crate_3, "crate_4": crate_4, "switch_1": switch_1,
                          "switch_2": switch_2, "switch_3": switch_3, "mini_boss_1": mini_boss_1,
                          "mini_boss_2": mini_boss_2, "current_enemy_battling": "current_enemy_battling",
                          "in_over_world": in_over_world, "in_battle": in_battle, "info_text_1": info_text_1,
                          "info_text_2": info_text_2}
    if in_battle:
        reservoir_a_return["current_enemy_battling"] = current_enemy_battling

    return reservoir_a_return


def reservoir_b(pygame, player, screen, graphic_dict, over_world_song_set, reservoir_music, dungeon_teleporter,
                reservoir_b_bg, dungeon_gate, crate_5, dungeon_crate_5, muchador_lights_on, muchador_arena,
                muchador_defeated, muchador, muchador_crate_1, muchador_crate_2, muchador_crate_3,
                muchador_crate_4, reservoir_passage, interaction_popup, font, interacted, SCREEN_WIDTH,
                save_check_window, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite,
                chorizon_battle_sprite, muchador_battle_sprite, barrier_active, sharp_sense_active,
                in_npc_interaction, user_interface, world_map_container, bar_backdrop, hp_bar, en_bar, xp_bar,
                button_highlighted, button_highlight, info_text_1, info_text_2, info_text_3, info_text_4, in_over_world,
                switch_1, switch_2, switch_3, has_key, magmon_battle_sprite, bandile_battle_sprite,
                chinzilla_battle_sprite):

    in_battle = False

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(reservoir_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    dungeon_teleporter.update(880, 525, graphic_dict["dungeon_teleporter"])

    screen.blit(reservoir_b_bg, (0, 0))
    screen.blit(dungeon_gate.surf, dungeon_gate.rect)
    if not crate_5:
        screen.blit(dungeon_crate_5.surf, dungeon_crate_5.rect)
    if muchador_lights_on:
        screen.blit(muchador_arena.surf, muchador_arena.rect)
    if not muchador_defeated:
        screen.blit(muchador.surf, muchador.rect)
    if muchador_lights_on:
        screen.blit(muchador_crate_1.surf, muchador_crate_1.rect)
        screen.blit(muchador_crate_2.surf, muchador_crate_2.rect)
        screen.blit(muchador_crate_3.surf, muchador_crate_3.rect)
        screen.blit(muchador_crate_4.surf, muchador_crate_4.rect)
    if muchador_defeated:
        screen.blit(reservoir_passage.surf, reservoir_passage.rect)
    screen.blit(player.surf, player.rect)

    if pygame.sprite.collide_rect(player, dungeon_gate):
        interaction_popup.update(dungeon_gate.x_coordinate, dungeon_gate.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("gate"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (dungeon_gate.x_coordinate, dungeon_gate.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted:
            if player.x_coordinate > SCREEN_WIDTH - 575:
                for item in player.items:
                    if item.name == "boss key":
                        player.items.remove(item)
                        has_key = True
                if has_key:
                    if not muchador_lights_on:
                        muchador.update_image(350, 360, graphic_dict["muchador"])
                        muchador_lights_on = True
                    info_text_1 = "You used the key to open the gate."
                    info_text_2 = ""
                    player.x_coordinate = 625
                    player.y_coordinate = 200
                    player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                    interacted = False
                else:
                    info_text_1 = "This gate requires a key "
                    info_text_2 = "Located somewhere in this dungeon. "
                    interacted = False
            else:
                player.x_coordinate = 775
                player.y_coordinate = 200
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                interacted = False

    if pygame.sprite.collide_rect(player, dungeon_teleporter):
        interaction_popup.update(dungeon_teleporter.x_coordinate, dungeon_teleporter.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("teleporter"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (dungeon_teleporter.x_coordinate, dungeon_teleporter.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted:
            dungeon_teleporter.update(519, 316, graphic_dict["dungeon_teleporter"])
            player.current_zone = "reservoir a"
            in_over_world = True
            interacted = False
            switch_1 = True
            switch_2 = True
            switch_3 = True
            player.x_coordinate = 519
            player.y_coordinate = 315
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.sprite.collide_rect(player, dungeon_crate_5):
        if not crate_5:
            interaction_popup.update(dungeon_crate_5.x_coordinate, dungeon_crate_5.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (dungeon_crate_5.x_coordinate, dungeon_crate_5.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not crate_5:
                    info_text_1 = "You found 10 Rupees!"
                    info_text_2 = ""
                    player.rupees += 10
                    crate_5 = True
                    interacted = False
                    dungeon_crate_5.kill()

    if pygame.sprite.collide_rect(player, reservoir_passage):
        if muchador_defeated:
            interaction_popup.update(reservoir_passage.x_coordinate + 45, reservoir_passage.y_coordinate - 75,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("passage"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (reservoir_passage.x_coordinate + 45, reservoir_passage.y_coordinate - 75)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                player.current_zone = "reservoir c"
                in_over_world = True
                interacted = False
                player.x_coordinate = 900
                player.y_coordinate = 545
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if not muchador_defeated:
        if pygame.sprite.collide_rect(player, muchador):
            interaction_popup.update(muchador.x_coordinate, muchador.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("muchador"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (muchador.x_coordinate, muchador.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            # lets player know if they are in range of enemy they can press f to attack it
            info_text_1 = "Press 'F' key to attack enemy."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted:
                current_enemy_battling = muchador
                in_over_world = False
                in_battle = True

                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
                combat_scenario.resting_animation(player, muchador, player_battle_sprite, snake_battle_sprite,
                                                  ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite,
                                                  magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite,
                                                  barrier_active, sharp_sense_active, in_battle, in_npc_interaction,
                                                  graphic_dict)

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
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if button_highlighted:
        screen.blit(button_highlight.surf, button_highlight.rect)

    # info to return to main loop --------------------------------------------------------------------------------------
    reservoir_b_return = {"over_world_song_set": over_world_song_set, "interacted": interacted, "muchador_lights_on":
                          muchador_lights_on, "switch_1": switch_1, "switch_2": switch_2, "switch_3": switch_3,
                          "crate_5": crate_5, "current_enemy_battling": "current_enemy_battling",
                          "in_over_world": in_over_world, "in_battle": in_battle, "info_text_1": info_text_1,
                          "info_text_2": info_text_2, "has_key": has_key}
    if in_battle:
        reservoir_b_return["current_enemy_battling"] = current_enemy_battling

    return reservoir_b_return


def reservoir_c(pygame, player, screen, graphic_dict, over_world_song_set, reservoir_music, interaction_popup, font,
                interacted, save_check_window, user_interface, world_map_container, bar_backdrop, hp_bar, en_bar,
                xp_bar, button_highlighted, button_highlight, reservoir_c_bg, dungeon_chest, reservoir_exit,
                rock_1, rock_2, gloves_obtained, Item, info_text_1, info_text_2, info_text_3, info_text_4,
                in_over_world, has_key, muchador_lights_on, hearth_stone):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(reservoir_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    screen.blit(reservoir_c_bg, (0, 0))
    screen.blit(dungeon_chest.surf, dungeon_chest.rect)
    screen.blit(reservoir_exit.surf, reservoir_exit.rect)
    screen.blit(rock_1.surf, rock_1.rect)
    screen.blit(rock_2.surf, rock_2.rect)
    screen.blit(player.surf, player.rect)

    # move player back to reservoir b if they approach passage
    if 1000 > player.x_coordinate > 950 and 400 < player.y_coordinate:
        player.current_zone = "reservoir b"
        over_world_song_set = False
        in_over_world = True
        muchador_lights_on = True
        player.x_coordinate = 100
        player.y_coordinate = 375

    if pygame.sprite.collide_rect(player, dungeon_chest):
        interaction_popup.update(dungeon_chest.x_coordinate, dungeon_chest.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("chest"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (dungeon_chest.x_coordinate, dungeon_chest.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            if not gloves_obtained:
                if len(player.items) < 16:
                    dungeon_chest.update(dungeon_chest.x_coordinate, dungeon_chest.y_coordinate,
                                         graphic_dict["dungeon_chest_open"])
                    info_text_1 = "You've obtained the power gloves!"
                    info_text_2 = ""
                    player.items.append(Item("power gloves", "gloves", 0, 0, graphic_dict["gloves"]))
                    gloves_obtained = True
                else:
                    info_text_1 = "You're inventory is full."
                    info_text_2 = ""
            else:
                info_text_1 = "You've already obtained this item."
                info_text_2 = ""
            interacted = False

    if pygame.sprite.collide_rect(player, rock_1):
        interaction_popup.update(rock_1.x_coordinate, rock_1.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("rock"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rock_1.x_coordinate, rock_1.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            try:
                if player.equipment["gloves"].name == "power gloves":
                    if rock_1.x_coordinate == 580:
                        rock_1.update(rock_1.x_coordinate + 300, rock_1.y_coordinate, graphic_dict["rock_img"])
                else:
                    info_text_1 = "The rock won't budge."
                    info_text_2 = ""
            except AttributeError:
                info_text_1 = "The rock won't budge."
                info_text_2 = ""
                pass
            interacted = False

    if pygame.sprite.collide_rect(player, rock_2):
        interaction_popup.update(rock_2.x_coordinate, rock_2.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("rock"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rock_2.x_coordinate, rock_2.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            try:
                if player.equipment["gloves"].name == "power gloves":
                    if rock_2.x_coordinate == 580:
                        rock_2.update(rock_2.x_coordinate + 300, rock_2.y_coordinate, graphic_dict["rock_img"])
                else:
                    info_text_1 = "The rock won't budge."
                    info_text_2 = ""
            except AttributeError:
                info_text_1 = "The rock won't budge."
                info_text_2 = ""
                pass
            interacted = False

    if pygame.sprite.collide_rect(player, reservoir_exit):
        interaction_popup.update(reservoir_exit.x_coordinate - 15, reservoir_exit.y_coordinate,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("exit"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (reservoir_exit.x_coordinate - 15, reservoir_exit.y_coordinate)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            player.current_zone = "korlok"
            over_world_song_set = False
            in_over_world = True
            player.x_coordinate = 100
            player.y_coordinate = 550
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
            hearth_stone.update(885, 230, graphic_dict["hearth_stone"])
            interacted = False

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
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if button_highlighted:
        screen.blit(button_highlight.surf, button_highlight.rect)

    # info to return to main loop --------------------------------------------------------------------------------------
    reservoir_c_return = {"over_world_song_set": over_world_song_set, "interacted": interacted,
                          "muchador_lights_on": muchador_lights_on, "gloves_obtained": gloves_obtained,
                          "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                          "info_text_4": info_text_4, "has_key": has_key}

    return reservoir_c_return
