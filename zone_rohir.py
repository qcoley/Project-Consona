import drawing_functions
import random


def rohir_river(pygame, screen, player, over_world_song_set, rohir_river_bg, dungeon_entrance, water_1, water_2,
                water_3, water_4, water_5, water_player, graphic_dict, save_check_window, user_interface,
                bar_backdrop, hp_bar, en_bar, xp_bar, font, info_text_1, info_text_2, info_text_3, info_text_4,
                in_over_world, button_highlighted, button_highlight, rohir_river_music, interaction_popup, interacted,
                equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select,
                beyond_seldon, pet_energy_window, basic_fish_counter, better_fish_counter, even_better_fish_counter,
                best_fish_counter, item_block, item_block_got, Item, sfx_item_block, dungeon_teleporter,
                apothis_gift, dawn, early_morning, morning, early_afternoon, afternoon, dusk, night, time_of_day):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(100)

    screen.blit(rohir_river_bg, (0, 0))
    screen.blit(dungeon_entrance.surf, dungeon_entrance.rect)
    screen.blit(water_1.surf, water_1.rect)
    screen.blit(water_2.surf, water_2.rect)
    screen.blit(water_3.surf, water_3.rect)
    screen.blit(water_4.surf, water_4.rect)
    screen.blit(water_5.surf, water_5.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)

    if 1000 > player.x_coordinate > 270:
        player.x_coordinate -= 1
        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)

        if player.x_coordinate > 285:
            water_player.update(player.x_coordinate, player.y_coordinate - 5, graphic_dict["water_player"])
            screen.blit(water_player.surf, water_player.rect)

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

    if not item_block_got:
        screen.blit(item_block.surf, item_block.rect)

    # water movement animation -------------------------------------------------------------------------
    if 1000 > water_1.x_coordinate > 294:
        water_1.x_coordinate -= 1
        water_1.rect.midbottom = (water_1.x_coordinate, water_1.y_coordinate)
    else:
        water_1.update(900, water_1.y_coordinate, graphic_dict["water"])
    if 1000 > water_2.x_coordinate > 294:
        water_2.x_coordinate -= 1
        water_2.rect.midbottom = (water_2.x_coordinate, water_2.y_coordinate)
    else:
        water_2.update(900, water_2.y_coordinate, graphic_dict["water"])
    if 1000 > water_3.x_coordinate > 294:
        water_3.x_coordinate -= 1
        water_3.rect.midbottom = (water_3.x_coordinate, water_3.y_coordinate)
    else:
        water_3.update(900, water_3.y_coordinate, graphic_dict["water"])
    if 1000 > water_4.x_coordinate > 294:
        water_4.x_coordinate -= 1
        water_4.rect.midbottom = (water_4.x_coordinate, water_4.y_coordinate)
    else:
        water_4.update(900, water_4.y_coordinate, graphic_dict["water"])
    if 1000 > water_5.x_coordinate > 294:
        water_5.x_coordinate -= 1
        water_5.rect.midbottom = (water_5.x_coordinate, water_5.y_coordinate)
    else:
        water_5.update(900, water_5.y_coordinate, graphic_dict["water"])
    # --------------------------------------------------------------------------------------------------

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.load(rohir_river_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    if pygame.sprite.collide_rect(player, dungeon_entrance):
        interaction_popup.update(dungeon_entrance.x_coordinate + 40,
                                 dungeon_entrance.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(dungeon_entrance.name), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (dungeon_entrance.x_coordinate + 40,
                                        dungeon_entrance.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        # lets player know if they are in range of building they can press f to enter it
        info_text_1 = "Press 'F' key to enter dungeon.."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            dungeon_teleporter.update(519, 316, graphic_dict["dungeon_teleporter"])
            player.current_zone = "reservoir a"
            in_over_world = True
            over_world_song_set = False
            player.x_coordinate = 525
            player.y_coordinate = 650
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate,
                                                          player.y_coordinate))
            interacted = False
            beyond_seldon = True

    if pygame.sprite.collide_rect(player, item_block):
        if not item_block_got:
            interaction_popup.update(item_block.x_coordinate, item_block.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("Item Block"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (item_block.x_coordinate, item_block.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not item_block_got:
                    if len(player.items) < 16:
                        item = random.randint(1, 12)
                        item_block_got = True
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
                            info_text_2 = "A mage book!"
                            player.items.append(Item("mage book", "book", 200, 200,
                                                     graphic_dict["mage_book"], 0))
                        if item == 5:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A fighter book!"
                            player.items.append(Item("fighter book", "book", 200, 200,
                                                     graphic_dict["fighter_book"], 0))
                        if item == 6:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A scout book!"
                            player.items.append(Item("scout book", "book", 200, 200,
                                                     graphic_dict["scout_book"], 0))
                        if item == 7:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A poison cure potion!"
                            player.items.append(Item("cure poison potion", "potion", 200, 200,
                                                     graphic_dict["poison_cure"], 0))
                        if item == 8:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A burn cure potion!"
                            player.items.append(Item("cure burn potion", "potion", 200, 200,
                                                     graphic_dict["burn_cure"], 0))
                        if item == 9:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A bandage wrap!"
                            player.items.append(Item("bandage wrap", "wrap", 200, 200,
                                                     graphic_dict["bandage_wrap"], 0))
                        if item == 10:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A big cure potion!"
                            player.items.append(Item("big cure potion", "potion", 200, 200,
                                                     graphic_dict["big_cure_potion"], 0))
                        if item == 11:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A reinforcing brace!"
                            player.items.append(Item("brace", "brace", 200, 200,
                                                     graphic_dict["brace"], 0))
                        if item == 12:
                            info_text_1 = "From the random item block you got:"
                            info_text_2 = "A big mend potion!"
                            player.items.append(Item("big mend potion", "potion", 200, 200,
                                                     graphic_dict["big_mend_potion"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""

            interacted = False

    rohir_return = {"over_world_song_set": over_world_song_set, "info_text_1": info_text_1, "info_text_2": info_text_2,
                    "info_text_3": info_text_3, "info_text_4": info_text_4, "in_over_world": in_over_world,
                    "interacted": interacted, "beyond seldon": beyond_seldon, "item_block_1_got": item_block_got}

    return rohir_return
