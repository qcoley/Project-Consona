import drawing_functions
import time
import random


def korlok_forge(pygame, screen, graphic_dict, player, korlok_mines_bg, korlok_overworld_music,
                 over_world_song_set, interaction_popup, font, save_check_window, user_interface,
                 bar_backdrop, hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                 info_text_1, info_text_2, info_text_3, info_text_4, enemy_tic, npc_tic, in_battle, in_npc_interaction,
                 movement_able, equipment_screen, staff, sword, bow, npc_garan, offense_meter,
                 defense_meter, weapon_select, pet_energy_window, vanished, vanish_overlay,
                 chroma_forge, forge_rect, Item, sfx_smelting, overlay_smelting, using_forge, smelted_casing,
                 basic_fish_counter, better_fish_counter, even_better_fish_counter, best_fish_counter, item_block_11,
                 item_block_11_got, sfx_item_block, kasper_unlocked, torok_unlocked, iriana_unlocked, apothis_gift,
                 time_of_day, magmons):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(korlok_overworld_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(korlok_mines_bg, (0, 0))
    screen.blit(chroma_forge.surf, chroma_forge.rect)

    if not item_block_11_got:
        screen.blit(item_block_11.surf, item_block_11.rect)

    if using_forge and not smelted_casing:
        npc_toc = time.perf_counter()
        if not npc_toc - npc_tic > 2:
            screen.blit(overlay_smelting.surf, overlay_smelting.rect)
        else:
            smelted_casing = True
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

    if pygame.Rect.colliderect(player.rect, forge_rect):
        interaction_popup.update(515, 100,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Forge"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (515, 100)
        screen.blit(interaction_info_surf, interaction_info_rect)
        info_text_1 = "Press 'F' key to use the Forge."
        info_text_2 = ""

        if interacted:
            npc_tic = time.perf_counter()
            interacted = False
            if not smelted_casing:
                pygame.mixer.find_channel(True).play(sfx_smelting)
                for item in player.items:
                    if item.name == "casing":
                        player.items.remove(item)
                        player.items.append(Item("smelted casing", "casing", 200, 200, graphic_dict["smelted_casing"],
                                                 0))
                        using_forge = True

    if pygame.sprite.collide_rect(player, item_block_11):
        if not item_block_11_got:
            interaction_popup.update(item_block_11.x_coordinate, item_block_11.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Item Block"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (item_block_11.x_coordinate, item_block_11.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not item_block_11_got:
                    if len(player.items) < 16:
                        item = random.randint(1, 12)
                        item_block_11_got = True
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
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""

            interacted = False

    if 700 < player.y_coordinate:
        using_forge = False
        player.current_zone = "korlok"
        in_over_world = True
        player.x_coordinate = 540
        player.y_coordinate = 225

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
    forge_return = {"over_world_song_set": over_world_song_set, "enemy_tic": enemy_tic, "npc_tic": npc_tic,
                    "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                    "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                    "movement_able": movement_able, "using_forge": using_forge, "smelted_casing": smelted_casing,
                    "item_block_11_got": item_block_11_got}

    return forge_return
