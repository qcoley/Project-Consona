import drawing_functions
import combat_scenario


def reservoir_a(pygame, screen, SCREEN_HEIGHT, graphic_dict, player, reservoir_a_bg, reservoir_music,
                over_world_song_set, interaction_popup, font, save_check_window, user_interface, loot_popup_container,
                loot_text_container, bar_backdrop, hp_bar, en_bar, xp_bar, button_highlighted, button_highlight,
                in_over_world, interacted, info_text_1, info_text_2, info_text_3, info_text_4, switch_1,
                dungeon_switch_1, switch_2, dungeon_switch_2, switch_3, dungeon_switch_3, dungeon_walls, dungeon_items,
                dungeon_teleporter, mini_boss_1, dungeon_drop_wall, chorizon_1, mini_boss_2, chorizon_2, crate_1, Item,
                crate_2, crate_3, crate_4, mini_boss_1_defeated, mini_boss_2_defeated, boss_enemies,
                player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, chorizon_battle_sprite,
                muchador_battle_sprite, barrier_active, sharp_sense_active, in_npc_interaction, magmon_battle_sprite,
                bandile_battle_sprite, chinzilla_battle_sprite, equipment_screen, staff, sword, bow, npc_garan,
                offense_meter, defense_meter, weapon_select, pet_energy_window, necrola_battle_sprite,
                osodark_battle_sprite, sfx_item_rupee, sfx_item_key, sfx_item_potion, sfx_switch, sfx_teleporter,
                stelli_battle_sprite, chorizon_phase, vanished, vanish_overlay, basic_fish_counter, better_fish_counter,
                even_better_fish_counter, best_fish_counter, sfx_paper, apothis_gift, time_of_day, kasper_unlocked,
                torok_unlocked, iriana_unlocked, kasper_battle_sprite, torok_battle_sprite, iriana_battle_sprite):

    in_battle = False

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
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
                        pygame.mixer.find_channel(True).play(sfx_paper)
                        info_text_1 = "You found a book!"
                        info_text_2 = ""
                        player.items.append(Item("fighter book", "book", 200, 200, graphic_dict["fighter_book"], 0))
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
                        pygame.mixer.find_channel(True).play(sfx_item_key)
                        info_text_1 = "You found a golden key!"
                        info_text_2 = ""
                        player.items.append(Item("boss key", "key", 200, 200, graphic_dict["key_img"], 0))
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
                        pygame.mixer.find_channel(True).play(sfx_item_potion)
                        info_text_1 = "You found a health potion!"
                        info_text_2 = ""
                        player.items.append(Item("small health potion", "potion", 200, 200,
                                                 graphic_dict["health_pot_img"], 0))
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
                        pygame.mixer.find_channel(True).play(sfx_item_potion)
                        info_text_1 = "You found an energy potion!"
                        info_text_2 = ""
                        player.items.append(Item("small energy potion", "potion", 200, 200,
                                                 graphic_dict["energy_pot_img"], 0))
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
                    pygame.mixer.find_channel(True).play(sfx_switch)
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
                    pygame.mixer.find_channel(True).play(sfx_switch)
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
                    pygame.mixer.find_channel(True).play(sfx_switch)
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
            interaction_info_surf = font.render("Chorizon" + " lvl " + str(boss_enemy.level), True, "black",
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
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active, graphic_dict, kasper_unlocked,
                                                        torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                        torok_battle_sprite, iriana_battle_sprite)
                combat_scenario.battle_animation_enemy(current_enemy_battling, snake_battle_sprite,
                                                       ghoul_battle_sprite,
                                                       chorizon_battle_sprite, muchador_battle_sprite,
                                                       magmon_battle_sprite, bandile_battle_sprite,
                                                       chinzilla_battle_sprite, in_battle, in_npc_interaction,
                                                       graphic_dict, necrola_battle_sprite,
                                                       osodark_battle_sprite, stelli_battle_sprite,
                                                       False, stelli_battle_sprite, 0, stelli_battle_sprite,
                                                       stelli_battle_sprite, stelli_battle_sprite, apothis_gift, False,
                                                       time_of_day, True)

    # player defeats mini bosses and activates teleporter
    if pygame.sprite.collide_rect(player, dungeon_teleporter):
        interaction_popup.update(dungeon_teleporter.x_coordinate, dungeon_teleporter.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Teleporter"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (dungeon_teleporter.x_coordinate, dungeon_teleporter.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted:
            if switch_3:
                pygame.mixer.find_channel(True).play(sfx_teleporter)
                dungeon_teleporter.update(853, 540, graphic_dict["dungeon_teleporter"])
                player.current_zone = "reservoir b"
                in_over_world = True
                interacted = False
                player.x_coordinate = 852
                player.y_coordinate = 560
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

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
                in_npc_interaction, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar, button_highlighted,
                button_highlight, info_text_1, info_text_2, info_text_3, info_text_4, in_over_world,
                switch_1, switch_2, switch_3, has_key, magmon_battle_sprite, bandile_battle_sprite,
                chinzilla_battle_sprite, equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter,
                weapon_select, pet_energy_window, necrola_battle_sprite, osodark_battle_sprite, sfx_teleporter,
                sfx_rupee, sfx_gate, directional_arrow, stelli_battle_sprite, vanished, vanish_overlay,
                sfx_item_potion, Item, basic_fish_counter, better_fish_counter, even_better_fish_counter,
                best_fish_counter, apothis_gift, muchador_crate_1_top, muchador_crate_2_top, muchador_crate_3_top,
                muchador_crate_4_top, apothis_upgrade, time_of_day, kasper_unlocked, torok_unlocked, iriana_unlocked,
                kasper_battle_sprite, torok_battle_sprite, iriana_battle_sprite):

    in_battle = False

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(reservoir_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

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
        if muchador_lights_on:
            directional_arrow.update(350, 375, graphic_dict["arrow_left"])
            screen.blit(directional_arrow.surf, directional_arrow.rect)
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

    if muchador_lights_on:
        screen.blit(muchador_crate_1_top.surf, muchador_crate_1_top.rect)
        screen.blit(muchador_crate_2_top.surf, muchador_crate_2_top.rect)
        screen.blit(muchador_crate_3_top.surf, muchador_crate_3_top.rect)
        screen.blit(muchador_crate_4_top.surf, muchador_crate_4_top.rect)

    if pygame.sprite.collide_rect(player, dungeon_gate):
        interaction_popup.update(dungeon_gate.x_coordinate, dungeon_gate.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Gate"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (dungeon_gate.x_coordinate, dungeon_gate.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted:
            if player.x_coordinate > 705:
                for item in player.items:
                    if item.name == "boss key":
                        player.items.remove(item)
                        has_key = True
                if has_key or muchador_defeated:
                    if not muchador_lights_on:
                        muchador.update_image(350, 360, graphic_dict["muchador"])
                        muchador_lights_on = True
                    pygame.mixer.find_channel(True).play(sfx_gate)
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
        interaction_info_surf = font.render(str("Teleporter"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (dungeon_teleporter.x_coordinate, dungeon_teleporter.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted:
            pygame.mixer.find_channel(True).play(sfx_teleporter)
            dungeon_teleporter.update(519, 316, graphic_dict["dungeon_teleporter"])
            player.current_zone = "reservoir a"
            in_over_world = True
            interacted = False
            switch_1 = True
            switch_2 = True
            switch_3 = True
            player.x_coordinate = 519
            player.y_coordinate = 330
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.sprite.collide_rect(player, dungeon_crate_5):
        if not crate_5:
            interaction_popup.update(dungeon_crate_5.x_coordinate, dungeon_crate_5.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (dungeon_crate_5.x_coordinate, dungeon_crate_5.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not crate_5:
                    if len(player.items) < 16:
                        crate_5 = True
                        pygame.mixer.find_channel(True).play(sfx_item_potion)
                        info_text_1 = "You found a health potion!"
                        info_text_2 = ""
                        player.items.append(Item("small health potion", "potion", 200, 200,
                                                 graphic_dict["health_pot_img"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""

                interacted = False

    if pygame.sprite.collide_rect(player, reservoir_passage):
        if muchador_defeated:
            interaction_popup.update(reservoir_passage.x_coordinate + 45, reservoir_passage.y_coordinate - 75,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Passage"), True, "black", "light yellow")
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
                                     graphic_dict["popup_interaction_red"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Muchador"), True, "black", (255, 204, 203))
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
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active, graphic_dict, kasper_unlocked,
                                                        torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                        torok_battle_sprite, iriana_battle_sprite)
                combat_scenario.battle_animation_enemy(current_enemy_battling, snake_battle_sprite,
                                                       ghoul_battle_sprite,
                                                       chorizon_battle_sprite, muchador_battle_sprite,
                                                       magmon_battle_sprite, bandile_battle_sprite,
                                                       chinzilla_battle_sprite, in_battle, in_npc_interaction,
                                                       graphic_dict, necrola_battle_sprite,
                                                       osodark_battle_sprite, stelli_battle_sprite,
                                                       False, stelli_battle_sprite, 0, stelli_battle_sprite,
                                                       stelli_battle_sprite, stelli_battle_sprite, apothis_gift, False,
                                                       time_of_day, True)

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
                interacted, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar, button_highlighted,
                button_highlight, reservoir_c_bg, dungeon_chest, reservoir_exit, rock_1, rock_2, gloves_obtained,
                power_gloves, info_text_1, info_text_2, info_text_3, info_text_4, in_over_world, has_key,
                muchador_lights_on, equipment_screen, staff, sword, bow, npc_garan, offense_meter,
                defense_meter, weapon_select, pet_energy_window, sfx_chest, sfx_rocks, basic_fish_counter,
                better_fish_counter, even_better_fish_counter, best_fish_counter, rohir_gate, apothis_gift,
                dungeon_teleporter, time_of_day, magmons):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(reservoir_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(reservoir_c_bg, (0, 0))
    screen.blit(dungeon_chest.surf, dungeon_chest.rect)
    screen.blit(reservoir_exit.surf, reservoir_exit.rect)
    screen.blit(rock_1.surf, rock_1.rect)
    screen.blit(rock_2.surf, rock_2.rect)
    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)

    # move player back to reservoir b if they approach passage
    if 1000 > player.x_coordinate > 950 and 400 < player.y_coordinate:
        dungeon_teleporter.update(853, 540, graphic_dict["dungeon_teleporter"])
        player.current_zone = "reservoir b"
        in_over_world = True
        muchador_lights_on = True
        player.x_coordinate = 100
        player.y_coordinate = 375

    if pygame.sprite.collide_rect(player, dungeon_chest):
        interaction_popup.update(dungeon_chest.x_coordinate, dungeon_chest.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Chest"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (dungeon_chest.x_coordinate, dungeon_chest.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            if not gloves_obtained:
                if len(player.items) < 16:
                    dungeon_chest.update(dungeon_chest.x_coordinate, dungeon_chest.y_coordinate,
                                         graphic_dict["dungeon_chest_open"])
                    pygame.mixer.find_channel(True).play(sfx_chest)
                    info_text_1 = "You've obtained the power gloves!"
                    info_text_2 = ""
                    player.items.append(power_gloves)
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
        interaction_info_surf = font.render(str("Rock"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rock_1.x_coordinate, rock_1.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            try:
                if player.equipment["gloves"].name == "power gloves":
                    if rock_1.x_coordinate == 580:
                        pygame.mixer.find_channel(True).play(sfx_rocks)
                        rock_1.update(rock_1.x_coordinate + 300, rock_1.y_coordinate, graphic_dict["rock"])
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
        interaction_info_surf = font.render(str("Rock"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (rock_2.x_coordinate, rock_2.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            try:
                if player.equipment["gloves"].name == "power gloves":
                    if rock_2.x_coordinate == 580:
                        pygame.mixer.find_channel(True).play(sfx_rocks)
                        rock_2.update(rock_2.x_coordinate + 300, rock_2.y_coordinate, graphic_dict["rock"])
                else:
                    info_text_1 = "The rock won't budge."
                    info_text_2 = ""
            except AttributeError:
                info_text_1 = "The rock won't budge."
                info_text_2 = ""
                pass
            interacted = False

    if pygame.sprite.collide_rect(player, reservoir_exit):
        interaction_popup.update(reservoir_exit.x_coordinate - 14, reservoir_exit.y_coordinate - 6,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Exit"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (reservoir_exit.x_coordinate - 14, reservoir_exit.y_coordinate - 6)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            player.current_zone = "korlok"
            over_world_song_set = False
            in_over_world = True
            player.x_coordinate = 100
            player.y_coordinate = 550
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
            rohir_gate.update(525, 600, graphic_dict["rohir_gate"])
            interacted = False

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

    # info to return to main loop --------------------------------------------------------------------------------------
    reservoir_c_return = {"over_world_song_set": over_world_song_set, "interacted": interacted,
                          "muchador_lights_on": muchador_lights_on, "gloves_obtained": gloves_obtained,
                          "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                          "info_text_4": info_text_4, "has_key": has_key}

    return reservoir_c_return
