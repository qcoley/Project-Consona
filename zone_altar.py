import time
import random
import drawing_functions


def eldream_altar(pygame, screen, graphic_dict, player, eldream_altar_bg, ectrenos_music,
                  over_world_song_set, interaction_popup, font, save_check_window, user_interface,
                  bar_backdrop, hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                  info_text_1, info_text_2, info_text_3, info_text_4, enemy_tic, npc_tic, in_battle, in_npc_interaction,
                  movement_able, equipment_screen, staff, sword, bow, npc_garan, offense_meter,
                  defense_meter, weapon_select, pet_energy_window, vanished, vanish_overlay,
                  chroma_forge, forge_rect, Item, sfx_enchanting, overlay_smelting, using_forge, enchanted_casing,
                  artherian_2, task_star_artherian, basic_fish_counter, better_fish_counter,
                  even_better_fish_counter, best_fish_counter, item_block_12, item_block_12_got, sfx_item_block,
                  kasper_unlocked, torok_unlocked, iriana_unlocked, apothis_gift, smelted_casing):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(ectrenos_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(eldream_altar_bg, (0, 0))
    screen.blit(chroma_forge.surf, chroma_forge.rect)

    if not item_block_12_got:
        screen.blit(item_block_12.surf, item_block_12.rect)

    if using_forge and not enchanted_casing:
        npc_toc = time.perf_counter()
        if not npc_toc - npc_tic > 2:
            screen.blit(overlay_smelting.surf, overlay_smelting.rect)
        else:
            enchanted_casing = True
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
        interaction_popup.update(515, 100, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Altar"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (515, 100)
        screen.blit(interaction_info_surf, interaction_info_rect)
        if smelted_casing:
            info_text_1 = "Press 'F' key to use the Altar."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""
        else:
            info_text_1 = "First go to the Forge in Korlok."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

        if interacted:
            npc_tic = time.perf_counter()
            interacted = False
            if not enchanted_casing:
                if smelted_casing:
                    pygame.mixer.find_channel(True).play(sfx_enchanting)
                    for item in player.items:
                        if item.name == "smelted casing":
                            player.items.remove(item)
                            player.items.append(Item("enchanted casing", "casing", 200, 200,
                                                     graphic_dict["enchanted_casing"], 0))
                            artherian_2 = True
                            using_forge = True
                            task_star_artherian.update(210, 400, graphic_dict["artherian_complete_star"])

    if pygame.sprite.collide_rect(player, item_block_12):
        if not item_block_12_got:
            interaction_popup.update(item_block_12.x_coordinate, item_block_12.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Item Block"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (item_block_12.x_coordinate, item_block_12.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not item_block_12_got:
                    if len(player.items) < 16:
                        item = random.randint(1, 12)
                        item_block_12_got = True
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
        player.current_zone = "ectrenos left"
        in_over_world = True
        player.x_coordinate = 150
        player.y_coordinate = 475
        over_world_song_set = False

    # info to return to main loop --------------------------------------------------------------------------------------
    altar_return = {"over_world_song_set": over_world_song_set, "enemy_tic": enemy_tic, "npc_tic": npc_tic,
                    "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                    "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                    "movement_able": movement_able, "using_forge": using_forge, "enchanted_casing": enchanted_casing,
                    "artherian_2": artherian_2, "item_block_12_got": item_block_12_got}

    return altar_return
