import time
import random
import drawing_functions
import gameplay_functions
import combat_scenario


def castle_one(pygame, screen, graphic_dict, player, castle_one_bg, over_world_song_set, castle_music,
               interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
               button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
               info_text_3, info_text_4, npc_tic, movement_able, equipment_screen, staff, sword, bow, npc_garan,
               offense_meter, defense_meter, weapon_select, pet_energy_window, artherian, player_battle_sprite,
               current_npc_interacting, in_npc_interaction, marrow_attuned, sfx_hearth,
               marrow_ghouls, enemy_tic, barrier_active, sharp_sense_active, ghoul_battle_sprite, in_battle,
               current_enemy_battling, Enemy, Item, UiElement, artherian_star, noren, boro, maydria, npcs,
               maydria_star, sub_marrow_ladder, sfx_ladder, vanished, vanish_overlay, basic_fish_counter,
               better_fish_counter, even_better_fish_counter, best_fish_counter, castle_bridge, prism_activate,
               prism_tic, sfx_chroma, castle_exit, chandelier, crate_1, crate_2, castle_crate_1_got,
               castle_crate_2_got, sfx_item_potion, dreth_laugh, dreth_taunt, dreth_taunt_popup, rope_phase,
               castle_one_roped_bg, castle_one_keyed_bg, key_got, castle_key, boss_door, sfx_item_key, jumanos,
               jumano_battle_sprite, apothis_gift, time_of_day, kasper_unlocked, torok_unlocked, iriana_unlocked,
               kasper_battle_sprite, torok_battle_sprite, iriana_battle_sprite, sfx_surprise):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(castle_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    if rope_phase != 2:
        screen.blit(castle_one_bg, (0, 0))
    if rope_phase == 2 and not key_got:
        screen.blit(castle_one_roped_bg, (0, 0))
    if key_got:
        screen.blit(castle_one_keyed_bg, (0, 0))

    if not castle_crate_1_got:
        screen.blit(crate_1.surf, crate_1.rect)
    if not castle_crate_2_got:
        screen.blit(crate_2.surf, crate_2.rect)

    if not dreth_taunt:
        dreth_taunt_popup.update(510, 365, graphic_dict["dreth_taunt_1"])
        drawing_functions.dreth_taunt_window.append(dreth_taunt_popup)
        pygame.mixer.find_channel(True).play(dreth_laugh)
        dreth_taunt = True

    respawned_dict = gameplay_functions.enemy_respawn(player, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, Enemy, Item, graphic_dict,
                                                      UiElement, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      jumanos, False, False, False, False, time_of_day)
    jumanos = respawned_dict["jumanos"]

    for jumano in jumanos:
        screen.blit(jumano.surf, jumano.rect)
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

    if rope_phase != 2:
        screen.blit(chandelier.surf, chandelier.rect)

    if pygame.sprite.collide_rect(player, crate_1):
        if not castle_crate_1_got:
            interaction_popup.update(crate_1.x_coordinate, crate_1.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_1.x_coordinate, crate_1.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not castle_crate_1_got:
                    if len(player.items) < 16:
                        castle_crate_1_got = True
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

    if pygame.sprite.collide_rect(player, crate_2):
        if not castle_crate_2_got:
            interaction_popup.update(crate_2.x_coordinate, crate_2.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_2.x_coordinate, crate_2.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not castle_crate_2_got:
                    if len(player.items) < 16:
                        castle_crate_2_got = True
                        pygame.mixer.find_channel(True).play(sfx_item_potion)
                        info_text_1 = "You found an energy potion!"
                        info_text_2 = ""
                        player.items.append(Item("small energy potion", "potion", 200, 200,
                                                 graphic_dict["energy_pot_img"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""

            interacted = False

    if pygame.Rect.colliderect(player.rect, castle_exit):
        interaction_popup.update(515, 25, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Marrow"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (515, 25)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to exit castle."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            over_world_song_set = False
            player.current_zone = "marrow"
            player.x_coordinate = 710
            player.y_coordinate = 525
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if not key_got and rope_phase == 2:
        if pygame.Rect.colliderect(player.rect, castle_key):
            interaction_popup.update(515, 260, graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Boss key"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (515, 260)
            screen.blit(interaction_info_surf, interaction_info_rect)

            info_text_1 = "Press 'F' to pickup key."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world:
                interacted = False
                pygame.mixer.find_channel(True).play(sfx_item_key)
                info_text_1 = "You found a golden key!"
                info_text_2 = ""
                player.items.append(Item("boss key", "key", 200, 200, graphic_dict["key_img"], 0))
                key_got = True

    if pygame.Rect.colliderect(player.rect, boss_door):
        interaction_popup.update(518, 525, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Dreth's lair"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (518, 525)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if key_got:
            info_text_1 = "Press 'F' key to enter."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world:
                for item in player.items:
                    if item.name == "boss key":
                        player.items.remove(item)
                interacted = False
                over_world_song_set = False
                player.current_zone = "castle lair"
                player.x_coordinate = 515
                player.y_coordinate = 150
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, jumanos, pygame.sprite.collide_rect_ratio(2.5))
    if enemy:
        interaction_popup.update(enemy.x_coordinate, enemy.y_coordinate - 40, graphic_dict["popup_interaction_red"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(enemy.name) + " lvl " + str(enemy.level), True, "black",
                                            (255, 204, 203))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (enemy.x_coordinate, enemy.y_coordinate - 40)
        screen.blit(interaction_info_surf, interaction_info_rect)
        enemy.surf = graphic_dict["jumano_red"]

        if interacted and in_over_world:
            current_enemy_battling = enemy
            in_over_world = False
            in_battle = True

            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                    sharp_sense_active, graphic_dict, kasper_unlocked,
                                                    torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                    torok_battle_sprite, iriana_battle_sprite)
            combat_scenario.battle_animation_enemy(current_enemy_battling, jumano_battle_sprite,
                                                   jumano_battle_sprite, jumano_battle_sprite, jumano_battle_sprite,
                                                   jumano_battle_sprite, jumano_battle_sprite, jumano_battle_sprite,
                                                   in_battle, in_npc_interaction, graphic_dict,
                                                   jumano_battle_sprite, jumano_battle_sprite, jumano_battle_sprite,
                                                   False, jumano_battle_sprite, 0, jumano_battle_sprite,
                                                   jumano_battle_sprite, jumano_battle_sprite, False, False,
                                                   time_of_day, True)

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, jumanos, pygame.sprite.collide_rect_ratio(1.5))
    if enemy and in_over_world:
        pygame.mixer.find_channel(True).play(sfx_surprise)
        current_enemy_battling = enemy
        in_over_world = False
        in_battle = True

        drawing_functions.loot_popup_container.clear()
        drawing_functions.loot_text_container.clear()
        combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                sharp_sense_active, graphic_dict, kasper_unlocked,
                                                torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                torok_battle_sprite, iriana_battle_sprite)
        combat_scenario.battle_animation_enemy(current_enemy_battling, jumano_battle_sprite,
                                               jumano_battle_sprite, jumano_battle_sprite, jumano_battle_sprite,
                                               jumano_battle_sprite, jumano_battle_sprite, jumano_battle_sprite,
                                               in_battle, in_npc_interaction, graphic_dict,
                                               jumano_battle_sprite, jumano_battle_sprite, jumano_battle_sprite,
                                               False, jumano_battle_sprite, 0, jumano_battle_sprite,
                                               jumano_battle_sprite, jumano_battle_sprite, False, False,
                                               time_of_day, True)

    # --------------------------------------------------------------------------------------------------
    direction_horizontal = random.choice(["left", "right"])
    direction_vertical = random.choice(["up", "down"])
    move_mon = random.choice(jumanos.sprites())
    if movement_able and in_over_world:
        enemy_toc = time.perf_counter()
        if enemy_toc - enemy_tic > 1:
            enemy_tic = time.perf_counter()
            move_mon.update_position([100, 800], [100, 500], direction_horizontal, direction_vertical)

    if player.x_coordinate < 35 and player.y_coordinate > 560:
        player.current_zone = "castle two"
        in_over_world = True
        player.x_coordinate = 860
        player.y_coordinate = 640
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if player.x_coordinate > 1005 and player.y_coordinate > 560:
        player.current_zone = "castle three"
        in_over_world = True
        player.x_coordinate = 150
        player.y_coordinate = 640
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    castle_one_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                         "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                         "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                         "movement_able": movement_able, "current_npc_interacting": current_npc_interacting,
                         "in_npc_interaction": in_npc_interaction, "marrow_attuned": marrow_attuned,
                         "enemy_tic": enemy_tic, "in_battle": in_battle, "current_enemy": current_enemy_battling,
                         "marrow_ghouls": marrow_ghouls, "prism_tic": prism_tic,
                         "castle_crate_1_got": castle_crate_1_got, "castle_crate_2_got": castle_crate_2_got,
                         "dreth_taunt": dreth_taunt, "has_key": key_got, "jumanos": jumanos}

    return castle_one_return


def castle_two(pygame, screen, graphic_dict, player, castle_two_bg, over_world_song_set, castle_music,
               interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
               in_over_world, interacted, info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able,
               equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select,
               pet_energy_window, player_battle_sprite, current_npc_interacting, in_npc_interaction, marrow_attuned,
               marrow_ghouls, enemy_tic, barrier_active, sharp_sense_active, ghoul_battle_sprite, in_battle,
               current_enemy_battling, vanished, vanish_overlay, basic_fish_counter, better_fish_counter,
               even_better_fish_counter, best_fish_counter, prism_tic, chandelier, rock_1, rock_2, sfx_rocks,
               dreth_laugh, dreth_taunt, dreth_taunt_popup, rope_wind, rope_phase, castle_two_roped_bg, sfx_rope,
               cell_1, cell_2, sfx_gate, mirage, mirage_updated, cell_popup, small_chest, mirage_saved, chest_1_got,
               sfx_rupee, sfx_atmon, atmon, atmon_battle_sprite, parts, parts_highlighted, sfx_item, apothis_gift,
               time_of_day, kasper_unlocked, torok_unlocked, iriana_unlocked, kasper_battle_sprite, torok_battle_sprite,
               iriana_battle_sprite, Item):
    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(castle_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    if not dreth_taunt:
        dreth_taunt_popup.update(510, 365, graphic_dict["dreth_taunt_2"])
        drawing_functions.dreth_taunt_window.append(dreth_taunt_popup)
        pygame.mixer.find_channel(True).play(dreth_laugh)
        dreth_taunt = True

    if mirage_saved:
        if atmon.alive_status:
            if time.perf_counter() - enemy_tic > 2:
                current_enemy_battling = atmon
                in_over_world = False
                in_battle = True
                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active, graphic_dict, kasper_unlocked,
                                                        torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                        torok_battle_sprite, iriana_battle_sprite)
                combat_scenario.battle_animation_enemy(current_enemy_battling, atmon_battle_sprite,
                                                       ghoul_battle_sprite, atmon_battle_sprite, atmon_battle_sprite,
                                                       atmon_battle_sprite, atmon_battle_sprite, atmon_battle_sprite,
                                                       in_battle, in_npc_interaction, graphic_dict, atmon_battle_sprite,
                                                       atmon_battle_sprite, atmon_battle_sprite, False,
                                                       atmon_battle_sprite, 0, atmon_battle_sprite, atmon_battle_sprite,
                                                       atmon_battle_sprite, False, False, time_of_day, True)

    if rope_phase == 0 or rope_phase == 11:
        screen.blit(castle_two_bg, (0, 0))
    if rope_phase == 10 or rope_phase == 2:
        screen.blit(castle_two_roped_bg, (0, 0))

    screen.blit(rock_1.surf, rock_1.rect)
    screen.blit(rock_2.surf, rock_2.rect)

    if player.quest_status["re recycling"] and not player.quest_complete["re recycling"]:
        if not parts_highlighted:
            for part in parts:
                part.update(part.x_coordinate, part.y_coordinate, graphic_dict["construct_part_high"])
            parts_highlighted = True

    if not player.quest_complete["re recycling"]:
        for part in parts:
            screen.blit(part.surf, part.rect)

    if not mirage_saved:
        if player.gender == "male":
            if not mirage_updated:
                mirage.update(415, 250, graphic_dict["mirage_female"])
                mirage_updated = True
        if player.gender == "female":
            if not mirage_updated:
                mirage.update(415, 250, graphic_dict["mirage_male"])
                mirage_updated = True
    if atmon.alive_status:
        screen.blit(mirage.surf, mirage.rect)
    if not chest_1_got:
        screen.blit(small_chest.surf, small_chest.rect)

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
                    if rock_1.y_coordinate == 275:
                        pygame.mixer.find_channel(True).play(sfx_rocks)
                        rock_1.update(rock_1.x_coordinate, rock_1.y_coordinate - 275, graphic_dict["rock"])
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
                    if rock_2.y_coordinate == 275:
                        pygame.mixer.find_channel(True).play(sfx_rocks)
                        rock_2.update(rock_2.x_coordinate, rock_2.y_coordinate - 275, graphic_dict["rock"])
                else:
                    info_text_1 = "The rock won't budge."
                    info_text_2 = ""
            except AttributeError:
                info_text_1 = "The rock won't budge."
                info_text_2 = ""
                pass
            interacted = False

    if pygame.Rect.colliderect(player.rect, rope_wind):
        interaction_popup.update(910, 250, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Rope"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (910, 250)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if rope_phase == 0 or rope_phase == 11:
            info_text_1 = "Press 'F' to release the rope."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_rope)
            info_text_1 = "The rope has been released!"
            info_text_2 = ""
            interacted = False
            if rope_phase == 0:
                chandelier.update(516, 285, graphic_dict["chandelier_right"])
                rope_phase = 10
            if rope_phase == 11:
                chandelier.update(516, 285, graphic_dict["chandelier_broken"])
                rope_phase = 2

    if pygame.Rect.colliderect(player.rect, cell_1):
        interaction_popup.update(420, 350, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Cell"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (420, 350)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' to open the cell gate."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            if not mirage_saved:
                enemy_tic = time.perf_counter()
                pygame.mixer.find_channel(True).play(sfx_gate)
                pygame.mixer.find_channel(True).play(sfx_atmon)
                interacted = False
                mirage_saved = True
                mirage.update(420, 255, graphic_dict["atmon"])

    if pygame.Rect.colliderect(player.rect, cell_2):
        interaction_popup.update(700, 350, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Cell"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (700, 350)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if not chest_1_got:
            info_text_1 = "Press 'F' to open the cell gate."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

        if interacted and in_over_world:
            if not chest_1_got:
                pygame.mixer.find_channel(True).play(sfx_gate)
                pygame.mixer.find_channel(True).play(sfx_rupee)
                interacted = False
                chest_1_got = True
                player.rupees += 50
                info_text_1 = "You found 50 Rupees. Wow!"
                info_text_2 = ""

    if not player.quest_complete["re recycling"]:
        part_pick = pygame.sprite.spritecollideany(player, parts)
        if part_pick:
            interaction_popup.update(part_pick.x_coordinate, part_pick.y_coordinate - 40,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str(part_pick.name), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (part_pick.x_coordinate, part_pick.y_coordinate - 40)
            screen.blit(interaction_info_surf, interaction_info_rect)
            if not player.quest_status["re recycling"]:
                info_text_1 = "It's some kind of construct."
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""
            if player.quest_status["re recycling"] and not player.quest_complete["re recycling"]:
                if len(player.items) < 16:
                    info_text_1 = "Press 'F' key to pick up the part."
                    info_text_2 = ""
                    info_text_3 = ""
                    info_text_4 = ""
                else:
                    info_text_1 = "Inventory is full. "
                    info_text_2 = ""
                    info_text_3 = ""
                    info_text_4 = ""
                if interacted and in_over_world and player.quest_progress["re recycling"] < 4:
                    if len(player.items) < 16:
                        pygame.mixer.find_channel(True).play(sfx_item)
                        player.quest_progress["re recycling"] += 1
                        player.items.append(Item("construct part", "part", 200, 200, graphic_dict["part"], 0))
                        part_pick.kill()
                    else:
                        info_text_1 = "Inventory is full."
                        info_text_2 = ""
                        info_text_3 = ""
                        info_text_4 = ""
                else:
                    if player.quest_progress["re recycling"] >= 4:
                        info_text_1 = "You've already gathered these."
                        info_text_2 = ""
                        info_text_3 = ""
                        info_text_4 = ""
            interacted = False

    # --------------------------------------------------------------------------------------------------
    if not mirage_saved:
        entrance_text_surf = font.render("Please.. help me.", True, "black", "light yellow")
        screen.blit(cell_popup.surf, cell_popup.rect)
        entrance_text_rect = entrance_text_surf.get_rect()
        entrance_text_rect.center = (cell_popup.x_coordinate, cell_popup.y_coordinate)
        screen.blit(entrance_text_surf, entrance_text_rect)

    if player.x_coordinate > 975 and player.y_coordinate > 560:
        player.current_zone = "castle one"
        in_over_world = True
        player.x_coordinate = 115
        player.y_coordinate = 600
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    castle_two_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                         "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                         "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                         "movement_able": movement_able, "current_npc_interacting": current_npc_interacting,
                         "in_npc_interaction": in_npc_interaction, "marrow_attuned": marrow_attuned,
                         "enemy_tic": enemy_tic, "in_battle": in_battle, "current_enemy": current_enemy_battling,
                         "marrow_ghouls": marrow_ghouls, "prism_tic": prism_tic, "dreth_taunt": dreth_taunt,
                         "rope_phase": rope_phase, "mirage_updated": mirage_updated, "mirage_saved": mirage_saved,
                         "castle_chest_1_got": chest_1_got, "parts_highlighted": parts_highlighted}

    return castle_two_return


def castle_three(pygame, screen, graphic_dict, player, castle_three_bg, over_world_song_set, castle_music,
                 interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                 in_over_world, interacted, info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able,
                 equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select,
                 pet_energy_window, player_battle_sprite, current_npc_interacting, in_npc_interaction, marrow_attuned,
                 marrow_ghouls, enemy_tic, barrier_active, sharp_sense_active, ghoul_battle_sprite, in_battle,
                 current_enemy_battling, vanished, vanish_overlay, basic_fish_counter, better_fish_counter,
                 even_better_fish_counter, best_fish_counter, prism_tic, chandelier, rock_1, rock_2, sfx_rocks,
                 dreth_laugh, dreth_taunt, dreth_taunt_popup, rope_wind, rope_phase, castle_three_roped_bg, sfx_rope,
                 cell_1, cell_2, sfx_gate, mirage, mirage_updated, cell_popup, small_chest, mirage_2_saved, chest_1_got,
                 sfx_rupee, sfx_atmon, atmon, atmon_battle_sprite, castle_ladder, sfx_ladder, jumano_hall, thanked,
                 up_move, jumano_battle_sprite, sfx_surprise, surprised, apothis_gift, parts, parts_highlighted,
                 sfx_item, apothis_upgrade, time_of_day, kasper_unlocked, torok_unlocked, iriana_unlocked,
                 kasper_battle_sprite, torok_battle_sprite, iriana_battle_sprite, Item):
    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(castle_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    if not dreth_taunt:
        dreth_taunt_popup.update(510, 365, graphic_dict["dreth_taunt_3"])
        drawing_functions.dreth_taunt_window.append(dreth_taunt_popup)
        pygame.mixer.find_channel(True).play(dreth_laugh)
        dreth_taunt = True

    if rope_phase == 0 or rope_phase == 10:
        screen.blit(castle_three_bg, (0, 0))
    if rope_phase == 11 or rope_phase == 2:
        screen.blit(castle_three_roped_bg, (0, 0))

    if jumano_hall.alive_status:
        if not surprised:
            if up_move:
                if jumano_hall.y_coordinate > 100:
                    jumano_hall.y_coordinate -= 1
                else:
                    jumano_hall.y_coordinate += 1
                    up_move = False
            else:
                if jumano_hall.y_coordinate < 600:
                    jumano_hall.y_coordinate += 1
                else:
                    jumano_hall.y_coordinate -= 1
                    up_move = True
            jumano_hall.rect = jumano_hall.surf.get_rect(center=(jumano_hall.x_coordinate, jumano_hall.y_coordinate))
        screen.blit(jumano_hall.surf, jumano_hall.rect)

    if player.quest_status["re recycling"] and not player.quest_complete["re recycling"]:
        if not parts_highlighted:
            for part in parts:
                part.update(part.x_coordinate, part.y_coordinate, graphic_dict["construct_part_high"])
            parts_highlighted = True

    if not player.quest_complete["re recycling"]:
        for part in parts:
            screen.blit(part.surf, part.rect)

    if not mirage_2_saved:
        if player.gender == "male":
            if not mirage_updated:
                mirage.update(608, 250, graphic_dict["mirage_female"])
                mirage_updated = True
        if player.gender == "female":
            if not mirage_updated:
                mirage.update(608, 250, graphic_dict["mirage_male"])
                mirage_updated = True
        screen.blit(mirage.surf, mirage.rect)

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

    if pygame.Rect.colliderect(player.rect, rope_wind):
        interaction_popup.update(120, 250, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Rope"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (120, 250)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if rope_phase == 0 or rope_phase == 10:
            info_text_1 = "Press 'F' to release the rope."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_rope)
            info_text_1 = "The rope has been released!"
            info_text_2 = ""
            interacted = False
            if rope_phase == 10:
                rope_phase = 2
                chandelier.update(516, 285, graphic_dict["chandelier_broken"])
            elif rope_phase == 0:
                rope_phase = 11
                chandelier.update(516, 285, graphic_dict["chandelier_left"])

    if pygame.Rect.colliderect(player.rect, cell_1):
        interaction_popup.update(610, 350, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Cell"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (610, 350)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if not mirage_2_saved:
            info_text_1 = "Press 'F' to open the cell gate."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

        if interacted and in_over_world:
            if not mirage_2_saved:
                mirage_2_saved = True
                enemy_tic = time.perf_counter()
                pygame.mixer.find_channel(True).play(sfx_gate)
                pygame.mixer.find_channel(True).play(sfx_rupee)
                interacted = False
                player.rupees += 50
                info_text_1 = "They gave you 50 Rupees. Wow!"
                info_text_2 = ""

    if pygame.Rect.colliderect(player.rect, castle_ladder):
        interaction_popup.update(332, 225, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Caldera"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (332, 225)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to climb down ladder."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_ladder)
            interacted = False
            over_world_song_set = False
            player.current_zone = "caldera"
            player.x_coordinate = 390
            player.y_coordinate = 315
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if jumano_hall.alive_status:
        if (jumano_hall.y_coordinate - 100 < player.y_coordinate < jumano_hall.y_coordinate + 100 and
                jumano_hall.x_coordinate - 100 < player.x_coordinate < jumano_hall.x_coordinate + 100):
            if not surprised:
                pygame.mixer.find_channel(True).play(sfx_surprise)
                jumano_hall.surf = graphic_dict["jumano_red"]
                surprised = True

            elif jumano_hall.y_coordinate > player.y_coordinate + 3:
                movement_able = False
                jumano_hall.y_coordinate -= 3
                if jumano_hall.x_coordinate > player.x_coordinate:
                    jumano_hall.x_coordinate -= 3
                elif jumano_hall.x_coordinate < player.x_coordinate:
                    jumano_hall.x_coordinate += 3
                jumano_hall.rect = jumano_hall.surf.get_rect(center=(jumano_hall.x_coordinate,
                                                                     jumano_hall.y_coordinate))
            elif jumano_hall.y_coordinate < player.y_coordinate - 3:
                movement_able = False
                jumano_hall.y_coordinate += 3
                if jumano_hall.x_coordinate > player.x_coordinate:
                    jumano_hall.x_coordinate -= 3
                elif jumano_hall.x_coordinate < player.x_coordinate:
                    jumano_hall.x_coordinate += 3
                jumano_hall.rect = jumano_hall.surf.get_rect(center=(jumano_hall.x_coordinate,
                                                                     jumano_hall.y_coordinate))
            else:
                current_enemy_battling = jumano_hall
                in_over_world = False
                movement_able = False
                in_battle = True
                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active, graphic_dict, kasper_unlocked,
                                                        torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                        torok_battle_sprite, iriana_battle_sprite)
                combat_scenario.battle_animation_enemy(current_enemy_battling, jumano_battle_sprite,
                                                       jumano_battle_sprite, jumano_battle_sprite, jumano_battle_sprite,
                                                       jumano_battle_sprite, jumano_battle_sprite,
                                                       jumano_battle_sprite, in_battle, jumano_battle_sprite,
                                                       graphic_dict, jumano_battle_sprite,
                                                       jumano_battle_sprite, jumano_battle_sprite,
                                                       False, jumano_battle_sprite, 0, jumano_battle_sprite,
                                                       jumano_battle_sprite, jumano_battle_sprite, apothis_gift, False,
                                                       time_of_day, True)

    if not player.quest_complete["re recycling"]:
        part_pick = pygame.sprite.spritecollideany(player, parts)
        if part_pick:
            interaction_popup.update(part_pick.x_coordinate, part_pick.y_coordinate - 40,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str(part_pick.name), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (part_pick.x_coordinate, part_pick.y_coordinate - 40)
            screen.blit(interaction_info_surf, interaction_info_rect)
            if not player.quest_status["re recycling"]:
                info_text_1 = "It's some kind of construct."
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""
            if player.quest_status["re recycling"] and not player.quest_complete["re recycling"]:
                if len(player.items) < 16:
                    info_text_1 = "Press 'F' key to pick up the part."
                    info_text_2 = ""
                    info_text_3 = ""
                    info_text_4 = ""
                else:
                    info_text_1 = "Inventory is full. "
                    info_text_2 = ""
                    info_text_3 = ""
                    info_text_4 = ""
                if interacted and in_over_world and player.quest_progress["re recycling"] < 4:
                    if len(player.items) < 16:
                        pygame.mixer.find_channel(True).play(sfx_item)
                        player.quest_progress["re recycling"] += 1
                        player.items.append(Item("construct part", "part", 200, 200, graphic_dict["part"], 0))
                        part_pick.kill()
                    else:
                        info_text_1 = "Inventory is full."
                        info_text_2 = ""
                        info_text_3 = ""
                        info_text_4 = ""
                else:
                    if player.quest_progress["re recycling"] >= 4:
                        info_text_1 = "You've already gathered these."
                        info_text_2 = ""
                        info_text_3 = ""
                        info_text_4 = ""
            interacted = False

    # --------------------------------------------------------------------------------------------------
    if not mirage_2_saved:
        entrance_text_surf = font.render("Please.. help me.", True, "black", "light yellow")
        screen.blit(cell_popup.surf, cell_popup.rect)
        entrance_text_rect = entrance_text_surf.get_rect()
        entrance_text_rect.center = (cell_popup.x_coordinate, cell_popup.y_coordinate)
        screen.blit(entrance_text_surf, entrance_text_rect)

    if mirage_2_saved and not thanked:
        if time.perf_counter() - enemy_tic < 2:
            entrance_text_surf = font.render("Thank you.", True, "black", "light yellow")
            screen.blit(cell_popup.surf, cell_popup.rect)
            entrance_text_rect = entrance_text_surf.get_rect()
            entrance_text_rect.center = (cell_popup.x_coordinate, cell_popup.y_coordinate)
            screen.blit(entrance_text_surf, entrance_text_rect)
            screen.blit(mirage.surf, mirage.rect)
            thanked = True

    if player.x_coordinate < 50 and player.y_coordinate > 560:
        player.current_zone = "castle one"
        in_over_world = True
        player.x_coordinate = 915
        player.y_coordinate = 600
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    castle_three_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                           "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                           "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                           "movement_able": movement_able, "current_npc_interacting": current_npc_interacting,
                           "in_npc_interaction": in_npc_interaction, "marrow_attuned": marrow_attuned,
                           "enemy_tic": enemy_tic, "in_battle": in_battle, "current_enemy": current_enemy_battling,
                           "marrow_ghouls": marrow_ghouls, "prism_tic": prism_tic, "dreth_taunt": dreth_taunt,
                           "rope_phase": rope_phase, "mirage_2_updated": mirage_updated,
                           "mirage_2_saved": mirage_2_saved, "castle_chest_1_got": chest_1_got, "thanked": thanked,
                           "critter_up_move": up_move, "surprised": surprised, "parts_highlighted": parts_highlighted}

    return castle_three_return


def castle_lair(pygame, screen, graphic_dict, player, castle_lair_zero_bg, over_world_song_set, lair_music,
                interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                in_over_world, interacted, info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able,
                equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select,
                pet_energy_window, player_battle_sprite, enemy_tic, barrier_active, sharp_sense_active, in_battle,
                current_enemy_battling, vanished, vanish_overlay, basic_fish_counter, better_fish_counter,
                even_better_fish_counter, best_fish_counter, dreth_laugh, dreth_taunt, dreth_taunt_popup, lair_exit,
                lights_switch, castle_lair_one_bg, castle_lair_two_bg, castle_lair_bg, dreth, dreth_battle_sprite,
                dreth_defeated, apothis_gift, time_of_day, kasper_unlocked, torok_unlocked, iriana_unlocked,
                kasper_battle_sprite, torok_battle_sprite, iriana_battle_sprite):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(lair_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    if not dreth_taunt:
        movement_able = False
        screen.blit(castle_lair_zero_bg, (0, 0))

    if not dreth_taunt:
        dreth_taunt_popup.update(510, 365, graphic_dict["dreth_taunt_4"])
        drawing_functions.dreth_taunt_window.append(dreth_taunt_popup)
        pygame.mixer.find_channel(True).play(dreth_laugh)
        lights_switch = time.perf_counter()
        dreth_taunt = True

    if dreth_taunt:
        if 5 > time.perf_counter() - lights_switch > 4:
            screen.blit(castle_lair_one_bg, (0, 0))
            movement_able = False
        elif 6 > time.perf_counter() - lights_switch > 5:
            screen.blit(castle_lair_two_bg, (0, 0))
            movement_able = False
        elif time.perf_counter() - lights_switch > 6:
            screen.blit(castle_lair_bg, (0, 0))
            movement_able = True
        else:
            screen.blit(castle_lair_zero_bg, (0, 0))
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

    if not dreth_defeated:
        screen.blit(dreth.surf, dreth.rect)

    if not dreth_defeated:
        if pygame.sprite.collide_rect(player, dreth):
            interaction_popup.update(dreth.x_coordinate - 5, dreth.y_coordinate - 150,
                                     graphic_dict["popup_interaction_red"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Dreth"), True, "black", (255, 204, 203))
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (dreth.x_coordinate - 5, dreth.y_coordinate - 150)
            screen.blit(interaction_info_surf, interaction_info_rect)

            # lets player know if they are in range of enemy they can press f to attack it
            info_text_1 = "Press 'F' key to attack enemy."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted:
                current_enemy_battling = dreth
                in_over_world = False
                in_battle = True

                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active, graphic_dict, kasper_unlocked,
                                                        torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                        torok_battle_sprite, iriana_battle_sprite)
                combat_scenario.battle_animation_enemy(current_enemy_battling, dreth_battle_sprite, dreth_battle_sprite,
                                                       dreth_battle_sprite, dreth_battle_sprite,
                                                       dreth_battle_sprite, dreth_battle_sprite,
                                                       dreth_battle_sprite, in_battle, False,
                                                       graphic_dict, dreth_battle_sprite,
                                                       dreth_battle_sprite, dreth_battle_sprite,
                                                       False, dreth_battle_sprite, 0, dreth_battle_sprite,
                                                       dreth_battle_sprite, dreth_battle_sprite, apothis_gift, False,
                                                       time_of_day, True)
    if pygame.Rect.colliderect(player.rect, lair_exit):
        interaction_popup.update(515, 25, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Castle"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (515, 25)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to exit lair."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            over_world_song_set = False
            player.current_zone = "castle one"
            player.x_coordinate = 515
            player.y_coordinate = 450
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # --------------------------------------------------------------------------------------------------
    castle_lair_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                          "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                          "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                          "movement_able": movement_able, "enemy_tic": enemy_tic, "in_battle": in_battle,
                          "current_enemy": current_enemy_battling,
                          "dreth_taunt": dreth_taunt, "light_switch": lights_switch}

    return castle_lair_return


def caldera(pygame, screen, graphic_dict, player, caldera_bg, over_world_song_set, castle_music,
            interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
            in_over_world, interacted, info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able,
            equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select,
            pet_energy_window, vanished, vanish_overlay, basic_fish_counter, better_fish_counter,
            even_better_fish_counter, best_fish_counter, caldera_ladder, sfx_ladder, fishing_spot, fishing, walk_tic,
            fishing_timer, fishing_level, fish_caught, previous_surf, fishing_unlocked, sfx_fishing_cast, cat,
            cats_pet, sfx_cat_meow, cat_rewarded, Item, item_block_10, item_block_10_got, sfx_item_block,
            kasper_unlocked, torok_unlocked, iriana_unlocked, apothis_gift):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(castle_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    # if player isn't currently fishing, periodically update spots for animation
    if not fishing:
        if walk_tic % 2 > 1.75:
            fishing_spot.update(710, 365, graphic_dict["fishing_spot_1"])
        else:
            fishing_spot.update(710, 365, graphic_dict["fishing_spot_2"])

    # if player is fishing
    else:
        fish_return = gameplay_functions.fishing_function(pygame, fishing_timer, player, player.current_zone,
                                                          graphic_dict["fishing_spot_3"],
                                                          graphic_dict["fishing_spot_4"],
                                                          fishing_spot, fishing_spot, fishing_level,
                                                          basic_fish_counter, better_fish_counter,
                                                          even_better_fish_counter, best_fish_counter, fishing,
                                                          fish_caught,
                                                          graphic_dict["amuna_m_fishing_right"],
                                                          graphic_dict["amuna_m_fishing_down"],
                                                          graphic_dict["amuna_m_fishing_right_2"],
                                                          graphic_dict["amuna_m_fishing_down_2"],
                                                          graphic_dict["amuna_m_fishing_right_3"],
                                                          graphic_dict["amuna_m_fishing_down_3"],
                                                          graphic_dict["amuna_f_fishing_right"],
                                                          graphic_dict["amuna_f_fishing_down"],
                                                          graphic_dict["amuna_f_fishing_right_2"],
                                                          graphic_dict["amuna_f_fishing_down_2"],
                                                          graphic_dict["amuna_f_fishing_right_3"],
                                                          graphic_dict["amuna_f_fishing_down_3"],
                                                          graphic_dict["nuldar_m_fishing_right"],
                                                          graphic_dict["nuldar_m_fishing_down"],
                                                          graphic_dict["nuldar_m_fishing_right_2"],
                                                          graphic_dict["nuldar_m_fishing_down_2"],
                                                          graphic_dict["nuldar_m_fishing_right_3"],
                                                          graphic_dict["nuldar_m_fishing_down_3"],
                                                          graphic_dict["nuldar_f_fishing_right"],
                                                          graphic_dict["nuldar_f_fishing_down"],
                                                          graphic_dict["nuldar_f_fishing_right_2"],
                                                          graphic_dict["nuldar_f_fishing_down_2"],
                                                          graphic_dict["nuldar_f_fishing_right_3"],
                                                          graphic_dict["nuldar_f_fishing_down_3"],
                                                          graphic_dict["sorae_a_fishing_right"],
                                                          graphic_dict["sorae_a_fishing_down"],
                                                          graphic_dict["sorae_a_fishing_right_2"],
                                                          graphic_dict["sorae_a_fishing_down_2"],
                                                          graphic_dict["sorae_a_fishing_right_3"],
                                                          graphic_dict["sorae_a_fishing_down_3"],
                                                          graphic_dict["sorae_b_fishing_right"],
                                                          graphic_dict["sorae_b_fishing_down"],
                                                          graphic_dict["sorae_b_fishing_right_2"],
                                                          graphic_dict["sorae_b_fishing_down_2"],
                                                          graphic_dict["sorae_b_fishing_right_3"],
                                                          graphic_dict["sorae_b_fishing_down_3"],
                                                          previous_surf, fishing_spot, fishing_spot,
                                                          fishing_spot, fishing_spot,
                                                          graphic_dict["sorae_a_fishing_up"],
                                                          graphic_dict["sorae_b_fishing_up"],
                                                          graphic_dict["sorae_a_fishing_up_2"],
                                                          graphic_dict["sorae_b_fishing_up_2"],
                                                          graphic_dict["sorae_a_fishing_up_3"],
                                                          graphic_dict["sorae_b_fishing_up_3"],
                                                          graphic_dict["amuna_m_fishing_up"],
                                                          graphic_dict["amuna_f_fishing_up"],
                                                          graphic_dict["amuna_m_fishing_up_2"],
                                                          graphic_dict["amuna_f_fishing_up_2"],
                                                          graphic_dict["amuna_m_fishing_up_3"],
                                                          graphic_dict["amuna_f_fishing_up_3"],
                                                          graphic_dict["nuldar_m_fishing_up"],
                                                          graphic_dict["nuldar_f_fishing_up"],
                                                          graphic_dict["nuldar_m_fishing_up_2"],
                                                          graphic_dict["nuldar_f_fishing_up_2"],
                                                          graphic_dict["nuldar_m_fishing_up_3"],
                                                          graphic_dict["nuldar_f_fishing_up_3"], fishing_spot)
        basic_fish_counter = fish_return["basic_fish_counter"]
        better_fish_counter = fish_return["better_fish_counter"]
        even_better_fish_counter = fish_return["even_better_fish_counter"]
        best_fish_counter = fish_return["best_fish_counter"]
        fish_caught = fish_return["fish_caught"]
        fishing = fish_return["fishing"]
        movement_able = fish_return["movement_able"]

    screen.blit(caldera_bg, (0, 0))
    screen.blit(fishing_spot.surf, fishing_spot.rect)
    if not item_block_10_got:
        screen.blit(item_block_10.surf, item_block_10.rect)
    screen.blit(cat.surf, cat.rect)

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

    if pygame.Rect.colliderect(player.rect, caldera_ladder):
        interaction_popup.update(340, 250, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Castle"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (340, 250)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to climb up ladder."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_ladder)
            interacted = False
            over_world_song_set = False
            player.current_zone = "castle three"
            player.x_coordinate = 333
            player.y_coordinate = 363
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.Rect.colliderect(player.rect, cat):
        interaction_popup.update(cat.x_coordinate - 10, cat.y_coordinate - 50, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Cat"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (cat.x_coordinate - 10, cat.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if not cats_pet["marrow"]:
            info_text_1 = "Press 'F' key to pet cat."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

        if interacted and in_over_world:
            cat.update(cat.x_coordinate, cat.y_coordinate, graphic_dict["marrow_cat_pet"])
            pygame.mixer.find_channel(True).play(sfx_cat_meow)
            cats_pet["marrow"] = True
            cat_count = 0
            for cat in cats_pet.values():
                if not cat:
                    break
                cat_count += 1
                if cat_count == 7 and not cat_rewarded:
                    if len(player.items) < 16:
                        cat_rewarded = True
                        player.items.append(Item("cat card", "card", 200, 200, graphic_dict["cat_card"], 0))
                    else:
                        info_text_1 = "Cats Reward but inventory is full."
                        info_text_2 = "Try freeing space and interact again."

            interacted = False

    if not fishing:
        if pygame.sprite.collide_rect(player, fishing_spot):
            interaction_popup.update(fishing_spot.x_coordinate, fishing_spot.y_coordinate - 50,
                                     graphic_dict["popup_interaction_blue"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Fishing spot"), True, "black", "light blue")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (fishing_spot.x_coordinate, fishing_spot.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if fishing_unlocked:
                info_text_1 = "Press 'F' key to fish."
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""
            else:
                info_text_1 = "You need to unlock fishing. "
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""

            # if player interacts with fishing spot and has it unlocked and has bait, use bait and start
            if interacted and in_over_world and fishing_unlocked:
                for item in player.items:
                    if item.name == "marrow bait":
                        pygame.mixer.find_channel(True).play(sfx_fishing_cast)
                        fishing = True
                        fishing_timer = time.perf_counter()
                        player.items.remove(item)
                        previous_surf = player.surf
                        fish_caught = False
                        break
            interacted = False

    if pygame.sprite.collide_rect(player, item_block_10):
        if not item_block_10_got:
            interaction_popup.update(item_block_10.x_coordinate, item_block_10.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Item Block"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (item_block_10.x_coordinate, item_block_10.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not item_block_10_got:
                    if len(player.items) < 16:
                        item = random.randint(1, 14)
                        item_block_10_got = True
                        pygame.mixer.find_channel(True).play(sfx_item_block)
                        if item == 1:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Big Health Potion!"
                            player.items.append(Item("big health potion", "potion", 200, 200,
                                                     graphic_dict["health_pot_img"], 0))
                        if item == 2:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Big Energy Potion!"
                            player.items.append(Item("big energy potion", "potion", 200, 200,
                                                     graphic_dict["energy_pot_img"], 0))
                        if item == 3:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "50 Rupees!"
                            player.rupees += 50
                        if item == 4:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "Marrow Bait!"
                            player.items.append(Item("marrow bait", "bait", 200, 200,
                                                     graphic_dict["marrow_bait"], 0))
                        if item == 5:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A Pet Snack!"
                            if kasper_unlocked:
                                player.items.append(Item("pet cookie", "cookie", 200, 200,
                                                         graphic_dict["pet_cookie_img"], 1))
                            elif torok_unlocked:
                                player.items.append(Item("pet candy", "candy", 200, 200,
                                                         graphic_dict["pet_candy_img"], 1))
                            elif iriana_unlocked:
                                player.items.append(Item("pet tart", "tart", 200, 200,
                                                         graphic_dict["pet_tart_img"], 1))
                            else:
                                player.items.append(Item("pet cookie", "cookie", 200, 200,
                                                         graphic_dict["pet_cookie_img"], 1))
                        if item == 6:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A mage book!"
                            player.items.append(Item("mage book", "book", 200, 200,
                                                     graphic_dict["mage_book"], 0))
                        if item == 7:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A fighter book!"
                            player.items.append(Item("fighter book", "book", 200, 200,
                                                     graphic_dict["fighter_book"], 0))
                        if item == 8:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A scout book!"
                            player.items.append(Item("scout book", "book", 200, 200,
                                                     graphic_dict["scout_book"], 0))
                        if item == 9:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A poison cure potion!"
                            player.items.append(Item("cure poison potion", "potion", 200, 200,
                                                     graphic_dict["poison_cure"], 0))
                        if item == 10:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A burn cure potion!"
                            player.items.append(Item("cure burn potion", "potion", 200, 200,
                                                     graphic_dict["burn_cure"], 0))
                        if item == 11:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A bandage wrap!"
                            player.items.append(Item("bandage wrap", "wrap", 200, 200,
                                                     graphic_dict["bandage_wrap"], 0))
                        if item == 12:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A big cure potion!"
                            player.items.append(Item("big cure potion", "potion", 200, 200,
                                                     graphic_dict["big_cure_potion"], 0))
                        if item == 13:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A reinforcing brace!"
                            player.items.append(Item("brace", "brace", 200, 200,
                                                     graphic_dict["brace"], 0))
                        if item == 14:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A big mend potion!"
                            player.items.append(Item("big mend potion", "potion", 200, 200,
                                                     graphic_dict["big_mend_potion"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""

            interacted = False

    # --------------------------------------------------------------------------------------------------
    caldera_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                      "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                      "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                      "movement_able": movement_able, "fish_caught": fish_caught, "fishing": fishing,
                      "fishing_timer": fishing_timer, "previous_surf": previous_surf,
                      "basic_fish_counter": basic_fish_counter, "better_fish_counter": better_fish_counter,
                      "even_better_fish_counter": even_better_fish_counter, "best_fish_counter": best_fish_counter,
                      "cats_pet": cats_pet, "cat_rewarded": cat_rewarded, "item_block_10_got": item_block_10_got}

    return caldera_return
