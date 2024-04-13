import random
import time

import drawing_functions
import combat_scenario
import gameplay_functions


def korlok_mines(pygame, screen, graphic_dict, player, korlok_mines_bg, korlok_overworld_music,
                 over_world_song_set, bandiles, interaction_popup, font, save_check_window, user_interface,
                 bar_backdrop, hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                 info_text_1, info_text_2, info_text_3, info_text_4, enemy_tic, npc_tic, in_battle, in_npc_interaction,
                 movement_able, current_enemy_battling, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite,
                 chorizon_battle_sprite, muchador_battle_sprite, chinzilla_battle_sprite, barrier_active,
                 sharp_sense_active, magmon_battle_sprite, bandile_battle_sprite, seldon_enemies, korlok_enemies,
                 snakes, ghouls, magmons, interactables_seldon, interactables_korlok, Enemy, Item, UiElement,
                 interactables_mines, ores, equipment_screen, staff, sword, bow, npc_garan, offense_meter,
                 defense_meter, weapon_select, npc_prime, npc_jez, prime_popup, jez_popup, prime_1,
                 prime_2, prime_3, jez_1, jez_2, jez_3, seldon_flowers, eldream_flowers, interactables_eldream,
                 pet_energy_window, ectrenos_front_enemies, necrola_battle_sprite, osodark_battle_sprite, sfx_item,
                 sfx_talk, talk_start, stelli_battle_sprite, vanished, vanish_overlay, basic_fish_counter,
                 better_fish_counter, even_better_fish_counter, best_fish_counter, apothis_gift, bandiles_highlighted,
                 bandiles_reset, ore_highlighted, apothis_upgrade, time_of_day, kasper_unlocked, torok_unlocked,
                 iriana_unlocked, kasper_battle_sprite, torok_battle_sprite, iriana_battle_sprite):

    if time_of_day != 0 and time_of_day != 7:
        if not talk_start:
            pygame.mixer.find_channel(True).play(sfx_talk)
            talk_start = True

    respawned_dict = gameplay_functions.enemy_respawn(player, seldon_enemies, korlok_enemies, snakes, ghouls, magmons,
                                                      bandiles, interactables_seldon, interactables_korlok,
                                                      interactables_mines, Enemy, Item, graphic_dict, UiElement,
                                                      seldon_flowers, eldream_flowers, interactables_eldream,
                                                      ectrenos_front_enemies, ectrenos_front_enemies,
                                                      ectrenos_front_enemies, ectrenos_front_enemies,
                                                      ectrenos_front_enemies, False, False, False, False, time_of_day)
    bandiles = respawned_dict["bandiles"]

    if player.quest_status["band hammer"] and not player.quest_complete["band hammer"]:
        if not bandiles_highlighted:
            for enemy_sprite in bandiles:
                if enemy_sprite.name == "Bandile":
                    enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                              graphic_dict["bandile_high"])
            bandiles_highlighted = True
    if player.quest_complete["band hammer"]:
        if not bandiles_reset:
            for enemy_sprite in bandiles:
                if enemy_sprite.name == "Bandile":
                    enemy_sprite.update_image(enemy_sprite.x_coordinate, enemy_sprite.y_coordinate,
                                              graphic_dict["bandile"])
            bandiles_reset = True

    if player.quest_status["can't apothecary it"] and not player.quest_complete["can't apothecary it"]:
        if not ore_highlighted:
            for ore_sprite in ores:
                ore_sprite.update(ore_sprite.x_coordinate, ore_sprite.y_coordinate, graphic_dict["sprite_ore_high_img"])
            ore_highlighted = True

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(korlok_overworld_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(korlok_mines_bg, (0, 0))

    for bandile in bandiles:
        screen.blit(bandile.surf, bandile.rect)
    if not player.quest_complete["can't apothecary it"]:
        for ore in ores:
            screen.blit(ore.surf, ore.rect)
    if time_of_day != 0 and time_of_day != 7:
        screen.blit(npc_prime.surf, npc_prime.rect)
        screen.blit(npc_jez.surf, npc_jez.rect)
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

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, bandiles)
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
                                                    torok_unlocked, iriana_unlocked, kasper_battle_sprite,
                                                    torok_battle_sprite, iriana_battle_sprite)
            combat_scenario.battle_animation_enemy(current_enemy_battling, snake_battle_sprite,
                                                   ghoul_battle_sprite,
                                                   chorizon_battle_sprite, muchador_battle_sprite,
                                                   magmon_battle_sprite, bandile_battle_sprite,
                                                   chinzilla_battle_sprite, in_battle, in_npc_interaction,
                                                   graphic_dict, necrola_battle_sprite,
                                                   osodark_battle_sprite, stelli_battle_sprite,
                                                   False, stelli_battle_sprite, 0, ectrenos_front_enemies,
                                                   stelli_battle_sprite, stelli_battle_sprite, apothis_gift, False,
                                                   time_of_day, True)

    if player.x_coordinate > 660 and 685 < player.y_coordinate:
        player.current_zone = "korlok"
        in_over_world = True
        talk_start = False
        pygame.mixer.Sound.stop(sfx_talk)
        player.x_coordinate = 430
        player.y_coordinate = 430

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

    if not player.quest_complete["can't apothecary it"]:
        ore_pick = pygame.sprite.spritecollideany(player, ores)
        if ore_pick:
            interaction_popup.update(ore_pick.x_coordinate, ore_pick.y_coordinate - 40,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str(ore_pick.name), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (ore_pick.x_coordinate, ore_pick.y_coordinate - 40)
            screen.blit(interaction_info_surf, interaction_info_rect)
            if not player.quest_status["can't apothecary it"]:
                info_text_1 = "It's some kind of ore."
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""
            if player.quest_status["can't apothecary it"] and not player.quest_complete["can't apothecary it"]:
                if len(player.items) < 16:
                    if player.quest_progress["can't apothecary it"] < 4:
                        info_text_1 = "Press 'F' key to gather the ore."
                        info_text_2 = ""
                        info_text_3 = ""
                        info_text_4 = ""
                    else:
                        info_text_1 = "You've already gathered these."
                        info_text_2 = ""
                        info_text_3 = ""
                        info_text_4 = ""
                else:
                    info_text_1 = "Inventory is full."
                    info_text_2 = ""
                    info_text_3 = ""
                    info_text_4 = ""
                if interacted and in_over_world and player.quest_progress["can't apothecary it"] < 4:
                    if len(player.items) < 16:
                        pygame.mixer.find_channel(True).play(sfx_item)
                        player.quest_progress["can't apothecary it"] += 1
                        player.items.append(Item("korlok ore", "ore", 200, 200, graphic_dict["ore"], 0))
                        ore_pick.kill()
                        interacted = False
                    else:
                        info_text_1 = "Inventory is full."
                        info_text_2 = ""
                        info_text_3 = ""
                        info_text_4 = ""
                        interacted = False

            if interacted:
                interacted = False

    # ------------------------------------------------------------------------------------------------------------------
    # enemy movement updates
    if time_of_day != 0 and time_of_day != 7:
        direction_horizontal = random.choice(["left", "right"])
        direction_vertical = random.choice(["up", "down"])
        move_mon = random.choice(bandiles.sprites())
        if movement_able and in_over_world:
            enemy_toc = time.perf_counter()
            if enemy_toc - enemy_tic > 1:
                enemy_tic = time.perf_counter()
                move_mon.update_position([50, 500], [50, 250], direction_horizontal, direction_vertical)

    if time_of_day != 0 and time_of_day != 7:
        face_direction = random.choice(["left_p", "right_p", "left_j", "right_j"])
        if movement_able and in_over_world:
            npc_toc = time.perf_counter()
            if npc_toc - npc_tic > 7:
                npc_tic = time.perf_counter()
                if prime_2:
                    prime_3 = True
                if jez_2:
                    jez_3 = True
                if prime_1:
                    prime_1 = False
                    prime_2 = True
                if jez_1:
                    jez_1 = False
                    jez_2 = True
                if face_direction == "left_p":
                    npc_prime.update(graphic_dict["prime"])
                if face_direction == "right_p":
                    npc_prime.update(graphic_dict["prime_flip"])
                if face_direction == "left_j":
                    npc_jez.update(graphic_dict["jez"])
                if face_direction == "right_j":
                    npc_jez.update(graphic_dict["jez_flip"])
        if prime_1:
            prime_text_surf = font.render("What?", True, "black", "light yellow")
        if prime_2:
            prime_text_surf = font.render("I ate rock.", True, "black", "light yellow")
        if prime_3:
            prime_text_surf = font.render("I watch de-lava.", True, "black", "light yellow")
        if jez_1:
            jez_text_surf = font.render("You're not.", True, "black", "light yellow")
        if jez_2:
            jez_text_surf = font.render("Only like 3%.", True, "black", "light yellow")
        if jez_3:
            jez_text_surf = font.render("Don't matter.", True, "black", "light yellow")

        screen.blit(prime_popup.surf, prime_popup.rect)
        prime_text_rect = prime_text_surf.get_rect()
        prime_text_rect.center = (prime_popup.x_coordinate, prime_popup.y_coordinate)
        screen.blit(prime_text_surf, prime_text_rect)
        screen.blit(jez_popup.surf, jez_popup.rect)
        jez_text_rect = jez_text_surf.get_rect()
        jez_text_rect.center = (jez_popup.x_coordinate, jez_popup.y_coordinate)
        screen.blit(jez_text_surf, jez_text_rect)

    # info to return to main loop --------------------------------------------------------------------------------------
    mines_return = {"over_world_song_set": over_world_song_set, "enemy_tic": enemy_tic, "npc_tic": npc_tic,
                    "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                    "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                    "in_battle": in_battle, "movement_able": movement_able,
                    "current_enemy_battling": current_enemy_battling, "prime_1": prime_1, "prime_2": prime_2,
                    "prime_3": prime_3, "jez_1": jez_1, "jez_2": jez_2, "jez_3": jez_3, "talk_start": talk_start,
                    "bandiles_highlighted": bandiles_highlighted, "bandiles_reset": bandiles_reset,
                    "ore_highlighted": ore_highlighted}

    return mines_return
