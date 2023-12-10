import drawing_functions
import time
import random


def korlok_forge(pygame, screen, graphic_dict, player, korlok_mines_bg, korlok_overworld_music,
                 over_world_song_set, interaction_popup, font, save_check_window, user_interface,
                 bar_backdrop, hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                 info_text_1, info_text_2, info_text_3, info_text_4, enemy_tic, npc_tic, in_battle, in_npc_interaction,
                 movement_able, equipment_screen, staff, sword, bow, npc_garan, offense_meter,
                 defense_meter, weapon_select, pet_energy_window, vanished, vanish_overlay, hearth_stone,
                 chroma_forge, forge_rect, Item, sfx_smelting, overlay_smelting, using_forge, smelted_casing,
                 basic_fish_counter, better_fish_counter, even_better_fish_counter, best_fish_counter, item_block_11,
                 item_block_11_got, sfx_item_block, kasper_unlocked, torok_unlocked, iriana_unlocked):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(korlok_overworld_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(korlok_mines_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    screen.blit(chroma_forge.surf, chroma_forge.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

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
    drawing_functions.draw_level_up(screen, in_over_world)
    try:
        for pet in player.pet:
            if pet.active:
                pet_energy_surf = font.render(str(pet.energy) + " /100", True, "dark green", "light yellow")
                pet_energy_rect = pet_energy_surf.get_rect()
                pet_energy_rect.midleft = (345, 57)
                screen.blit(pet_energy_window.surf, pet_energy_window.rect)
                screen.blit(pet_energy_surf, pet_energy_rect)
    except AttributeError:
        pass

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
                        item = random.randint(1, 8)
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
        hearth_stone.update(885, 230, graphic_dict["hearth_stone"])

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)

    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world, basic_fish_counter, better_fish_counter, even_better_fish_counter,
                                     best_fish_counter)
    drawing_functions.draw_it(screen)

    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])

    # info to return to main loop --------------------------------------------------------------------------------------
    forge_return = {"over_world_song_set": over_world_song_set, "enemy_tic": enemy_tic, "npc_tic": npc_tic,
                    "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                    "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                    "movement_able": movement_able, "using_forge": using_forge, "smelted_casing": smelted_casing,
                    "item_block_11_got": item_block_11_got}

    return forge_return
