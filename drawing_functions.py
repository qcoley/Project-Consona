# functions for drawing certain text and images on screen
# lists for blitting elements/items to the screen that are contained within lists
character_sheet_text = []
character_sheet_window = []
journal_text = []
journal_window = []
level_up_text = []
level_up_window = []
quest_box = []
quest_complete_box = []
player_equipment = []
player_items = []
item_info_window = []
buy_info_window = []
sell_info_window = []


# draws elements on screen that have been appended to list by below functions
def draw_it(screen):
    if len(character_sheet_window) > 0:
        for character_window in character_sheet_window:
            screen.blit(character_window.surf, character_window.rect)
    if len(character_sheet_text) > 0:
        for character_text in character_sheet_text:
            screen.blit(character_text[0], character_text[1])
    if len(journal_window) > 0:
        for journals_window in journal_window:
            screen.blit(journals_window.surf, journals_window.rect)
    if len(journal_text) > 0:
        for journals_text in journal_text:
            screen.blit(journals_text[0], journals_text[1])
    if len(level_up_window) > 0:
        for level_ups_window in level_up_window:
            screen.blit(level_ups_window.surf, level_ups_window.rect)
    if len(level_up_text) > 0:
        for level_text in level_up_text:
            screen.blit(level_text[0], level_text[1])
    if len(character_sheet_text) > 0:
        for characters_text in character_sheet_text:
            screen.blit(characters_text[0], characters_text[1])
    if len(quest_box) > 0:
        for quest_element in quest_box:
            screen.blit(quest_element.surf, quest_element.rect)
    if len(quest_complete_box) > 0:
        for quest_complete_element in quest_complete_box:
            screen.blit(quest_complete_element.surf, quest_complete_element.rect)
    if len(player_equipment) > 0:
        for equipment_here in player_equipment:
            screen.blit(equipment_here.surf, equipment_here.rect)
    if len(player_items) > 0:
        for item_here in player_items:
            screen.blit(item_here.surf, item_here.rect)
    if len(item_info_window) > 0:
        for item_info in item_info_window:
            screen.blit(item_info.surf, item_info.rect)
    if len(buy_info_window) > 0:
        for buy_info in buy_info_window:
            screen.blit(buy_info.surf, buy_info.rect)
    if len(sell_info_window) > 0:
        for sell_info in sell_info_window:
            screen.blit(sell_info.surf, sell_info.rect)


def item_info_draw(inventory_item, info_items, item_info_button, graphic):
    if inventory_item:
        if inventory_item.name == "health potion":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_health_pot_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "energy potion":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_energy_pot_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "basic robes":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_basic_robes_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "basic armor":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_basic_armor_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "basic tunic":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_basic_tunic_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "basic staff":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_basic_staff_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "basic sword":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_basic_sword_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "basic bow":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_basic_bow_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "shiny rock":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_shiny_rock_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
        if inventory_item.name == "bone dust":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_bone_dust_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
        if inventory_item.name == "boss key":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_boss_key_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
        if inventory_item.name == "power gloves":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_gloves"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item


def buy_info_draw(buy_item, buy_items, yes_button, graphic):
    if buy_item:
        if buy_item.name == "health potion":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_health_pot_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "energy potion":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_energy_pot_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "basic robes":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_basic_robes_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "basic armor":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_basic_armor_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "basic tunic":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_basic_tunic_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "basic staff":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_basic_staff_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "basic sword":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_basic_sword_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "basic bow":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_basic_bow_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item


def sell_info_draw(sell_item, sell_items, yes_button, graphic):
    if sell_item:
        if sell_item.name == "health potion":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_health_pot_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "energy potion":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_energy_pot_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "basic robes":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_basic_robes_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "basic armor":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_basic_armor_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "basic tunic":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_basic_tunic_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "basic staff":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_basic_staff_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "basic sword":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_basic_sword_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "basic bow":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_basic_bow_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "shiny rock":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_shiny_rock_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "bone dust":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_bone_dust_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item


def text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4, in_over_world,
                   offense_upgraded, defense_upgraded, big_font):
    # get current player rupee count and create surf and rectangle to blit to screen------------------------------------
    text_rupee_surf = font.render(str(player.rupees), True, "black", "light blue")
    text_rupee_rect = text_rupee_surf.get_rect()
    text_rupee_rect.center = (1120, 693)
    screen.blit(text_rupee_surf, text_rupee_rect)
    # get current player level and create surf and rectangle to blit to screen------------------------------------------
    text_level_surf = font.render(str(player.level), True, "black", "light yellow")
    text_level_rect = text_level_surf.get_rect()
    text_level_rect.center = (1102, 360)
    screen.blit(text_level_surf, text_level_rect)
    # get current player role and create surf and rectangle to blit to screen-------------------------------------------
    text_role_surf = font.render(str(player.role), True, "black", "light gray")
    text_role_rect = text_role_surf.get_rect()
    text_role_rect.center = (1130, 81)
    screen.blit(text_role_surf, text_role_rect)
    # current player location for UI overlay ---------------------------------------------------------------------------
    if in_over_world:
        text_location = font.render(str(player.current_zone), True, "black", "light yellow")
        text_location_rect = text_location.get_rect()
        text_location_rect.midleft = (935, 29)
        screen.blit(text_location, text_location_rect)
    # get current player offense and create surf and rectangle to blit to screen----------------------------------------
    text_offense_surf = font.render(str(player.offense), True, "black", "light gray")
    text_offense_rect = text_offense_surf.get_rect()
    text_offense_rect.center = (1135, 117)
    screen.blit(text_offense_surf, text_offense_rect)
    # get current player defence and create surf and rectangle to blit to screen----------------------------------------
    text_defence_surf = font.render(str(player.defense), True, "black", "light gray")
    text_defence_rect = text_defence_surf.get_rect()
    text_defence_rect.center = (1233, 117)
    screen.blit(text_defence_surf, text_defence_rect)
    # current info text for message box in lower left corner of screen, first line--------------------------------------
    text_info_surf_1 = font.render(info_text_1, True, "black", "light yellow")
    text_info_rect_1 = text_info_surf_1.get_rect()
    text_info_rect_1.midleft = (30, 630)
    screen.blit(text_info_surf_1, text_info_rect_1)
    # current info text for message box in lower left corner of screen, second line-------------------------------------
    text_info_surf_2 = font.render(info_text_2, True, "black", "light yellow")
    text_info_rect_2 = text_info_surf_2.get_rect()
    text_info_rect_2.midleft = (30, 650)
    screen.blit(text_info_surf_2, text_info_rect_2)
    # current info text for message box in lower left corner of screen, third line--------------------------------------
    text_info_surf_3 = font.render(info_text_3, True, "black", "light yellow")
    text_info_rect_3 = text_info_surf_3.get_rect()
    text_info_rect_3.midleft = (30, 670)
    screen.blit(text_info_surf_3, text_info_rect_3)
    # current info text for message box in lower left corner of screen, fourth line-------------------------------------
    text_info_surf_4 = font.render(info_text_4, True, "black", "light yellow")
    text_info_rect_4 = text_info_surf_4.get_rect()
    text_info_rect_4.midleft = (30, 690)
    screen.blit(text_info_surf_4, text_info_rect_4)

    if offense_upgraded == 1:
        offense_up_surf = big_font.render(str("+"), True, "red", "light gray")
        offense_up_rect = offense_up_surf.get_rect()
        offense_up_rect.center = (1152, 114)
        screen.blit(offense_up_surf, offense_up_rect)
    if defense_upgraded == 1:
        defense_up_surf = big_font.render(str("+"), True, "red", "light gray")
        defense_up_rect = defense_up_surf.get_rect()
        defense_up_rect.center = (1248, 114)
        screen.blit(defense_up_surf, defense_up_rect)


def character_sheet_info_draw(character_sheet, player, font, draw_condition):

    if not draw_condition:
        character_sheet_text.clear()
        character_sheet_window.clear()
    else:
        text_name_surf = font.render(str(player.name), True, "black", "light yellow")
        text_name_rect = text_name_surf.get_rect()
        text_name_rect.midleft = (595, 152)
        text_race_surf = font.render(str(player.race), True, "black", "light yellow")
        text_race_rect = text_race_surf.get_rect()
        text_race_rect.midleft = (592, 190)
        text_rolled_surf = font.render(str(player.role), True, "black", "light yellow")
        text_rolled_rect = text_rolled_surf.get_rect()
        text_rolled_rect.midleft = (588, 228)
        text_health_surf = font.render(str(player.health), True, "black", "light yellow")
        text_health_rect = text_health_surf.get_rect()
        text_health_rect.midleft = (855, 151)
        text_energy_surf = font.render(str(player.energy), True, "black", "light yellow")
        text_energy_rect = text_energy_surf.get_rect()
        text_energy_rect.midleft = (855, 189)
        text_experience_surf = font.render(str(player.experience), True, "black", "light yellow")
        text_experience_rect = text_experience_surf.get_rect()
        text_experience_rect.midleft = (890, 229)
        text_mage_surf = font.render(str(player.knowledge["mage"]), True, "black", "light yellow")
        text_mage_rect = text_mage_surf.get_rect()
        text_mage_rect.midleft = (680, 310)
        text_fighter_surf = font.render(str(player.knowledge["fighter"]), True, "black", "light yellow")
        text_fighter_rect = text_fighter_surf.get_rect()
        text_fighter_rect.midleft = (688, 348)
        text_scout_surf = font.render(str(player.knowledge["scout"]), True, "black", "light yellow")
        text_scout_rect = text_scout_surf.get_rect()
        text_scout_rect.midleft = (680, 385)
        text_amuna_surf = font.render(str(player.reputation["amuna"]), True, "black", "light yellow")
        text_amuna_rect = text_amuna_surf.get_rect()
        text_amuna_rect.midleft = (940, 310)
        text_nuldar_surf = font.render(str(player.reputation["nuldar"]), True, "black", "light yellow")
        text_nuldar_rect = text_nuldar_surf.get_rect()
        text_nuldar_rect.midleft = (940, 348)
        text_sorae_surf = font.render(str(player.reputation["sorae"]), True, "black", "light yellow")
        text_sorae_rect = text_sorae_surf.get_rect()
        text_sorae_rect.midleft = (935, 385)
        text_mage_skills_surf = font.render(str(player.skills_mage["skill 2"]) +
                                                 (player.skills_mage["skill 3"]), True, "black", "light yellow")
        text_mage_skills_rect = text_mage_skills_surf.get_rect()
        text_mage_skills_rect.midleft = (650, 506)
        text_fighter_skills_surf = font.render(str(player.skills_fighter["skill 2"]) +
                                                 (player.skills_fighter["skill 3"]), True, "black", "light yellow")
        text_fighter_skills_rect = text_fighter_skills_surf.get_rect()
        text_fighter_skills_rect.midleft = (650, 543)
        text_scout_skills_surf = font.render(str(player.skills_scout["skill 2"]) +
                                                 (player.skills_scout["skill 3"]), True, "black", "light yellow")
        text_scout_skills_rect = text_scout_skills_surf.get_rect()
        text_scout_skills_rect.midleft = (650, 582)

        character_sheet_text.append((text_name_surf, text_name_rect))
        character_sheet_text.append((text_race_surf, text_race_rect))
        character_sheet_text.append((text_rolled_surf, text_rolled_rect))
        character_sheet_text.append((text_health_surf, text_health_rect))
        character_sheet_text.append((text_energy_surf, text_energy_rect))
        character_sheet_text.append((text_experience_surf, text_experience_rect))
        character_sheet_text.append((text_mage_surf, text_mage_rect))
        character_sheet_text.append((text_fighter_surf, text_fighter_rect))
        character_sheet_text.append((text_scout_surf, text_scout_rect))
        character_sheet_text.append((text_amuna_surf, text_amuna_rect))
        character_sheet_text.append((text_nuldar_surf, text_nuldar_rect))
        character_sheet_text.append((text_sorae_surf, text_sorae_rect))
        character_sheet_text.append((text_mage_skills_surf, text_mage_skills_rect))
        character_sheet_text.append((text_fighter_skills_surf, text_fighter_skills_rect))
        character_sheet_text.append((text_scout_skills_surf, text_scout_skills_rect))
        character_sheet_window.append(character_sheet)


def journal_info_draw(journal, player, font, draw_condition):

    if not draw_condition:
        journal_text.clear()
        journal_window.clear()
    else:
        text_quest1_surf = font.render(str(list(player.current_quests)[0]), True, "black", "light yellow")
        text_quest1_rect = text_quest1_surf.get_rect()
        text_quest1_rect.midleft = (600, 145)
        text_quest1_info_surf = font.render(str(list(player.current_quests.values())[0]), True, "black", "light yellow")
        text_quest1_info_rect = text_quest1_info_surf.get_rect()
        text_quest1_info_rect.midleft = (540, 190)
        text_quest1_prog_surf = font.render(str(player.quest_progress["sneaky snakes"]) + " /4",
                                            True, "black", "light yellow")
        text_quest1_prog_rect = text_quest1_prog_surf.get_rect()
        text_quest1_prog_rect.midleft = (950, 145)

        text_quest2_surf = font.render(str(list(player.current_quests)[1]), True, "black", "light yellow")
        text_quest2_rect = text_quest2_surf.get_rect()
        text_quest2_rect.midleft = (600, 272)
        text_quest2_info_surf = font.render(str(list(player.current_quests.values())[1]), True, "black", "light yellow")
        text_quest2_info_rect = text_quest2_info_surf.get_rect()
        text_quest2_info_rect.midleft = (540, 320)
        text_quest2_prog_surf = font.render(str(player.quest_progress["village repairs"]) + " /4",
                                            True, "black", "light yellow")
        text_quest2_prog_rect = text_quest2_prog_surf.get_rect()
        text_quest2_prog_rect.midleft = (950, 272)

        text_quest3_surf = font.render(str(list(player.current_quests)[2]), True, "black", "light yellow")
        text_quest3_rect = text_quest3_surf.get_rect()
        text_quest3_rect.midleft = (600, 405)
        text_quest3_info_surf = font.render(str(list(player.current_quests.values())[2]), True, "black", "light yellow")
        text_quest3_info_rect = text_quest3_info_surf.get_rect()
        text_quest3_info_rect.midleft = (540, 455)
        text_quest3_prog_surf = font.render(str(player.quest_progress["where's nede?"]) + " /1", True,
                                                "black", "light yellow")
        text_quest3_prog_rect = text_quest3_prog_surf.get_rect()
        text_quest3_prog_rect.midleft = (950, 405)

        text_quest4_surf = font.render(str(list(player.current_quests)[3]), True, "black", "light yellow")
        text_quest4_rect = text_quest4_surf.get_rect()
        text_quest4_rect.midleft = (600, 538)
        text_quest4_info_surf = font.render(str(list(player.current_quests.values())[3]), True, "black", "light yellow")
        text_quest4_info_rect = text_quest4_info_surf.get_rect()
        text_quest4_info_rect.midleft = (540, 585)
        text_quest4_prog_surf = font.render(str(player.quest_progress["ghouled again"]) + " /4", True,
                                            "black", "light yellow")
        text_quest4_prog_rect = text_quest4_prog_surf.get_rect()
        text_quest4_prog_rect.midleft = (950, 538)

        journal_text.append((text_quest1_surf, text_quest1_rect))
        journal_text.append((text_quest1_info_surf, text_quest1_info_rect))
        journal_text.append((text_quest1_prog_surf, text_quest1_prog_rect))
        journal_text.append((text_quest2_surf, text_quest2_rect))
        journal_text.append((text_quest2_info_surf, text_quest2_info_rect))
        journal_text.append((text_quest2_prog_surf, text_quest2_prog_rect))
        journal_text.append((text_quest3_surf, text_quest3_rect))
        journal_text.append((text_quest3_info_surf, text_quest3_info_rect))
        journal_text.append((text_quest3_prog_surf, text_quest3_prog_rect))
        journal_text.append((text_quest4_surf, text_quest4_rect))
        journal_text.append((text_quest4_info_surf, text_quest4_info_rect))
        journal_text.append((text_quest4_prog_surf, text_quest4_prog_rect))
        journal_window.append(journal)


def level_up_draw(level_up_win, player, level_up_font, draw_condition):

    if not draw_condition:
        level_up_text.clear()
        level_up_window.clear()

    else:
        text_leveled_up_surf = level_up_font.render(str(player.level), True, "black", "light yellow")
        text_leveled_up_rect = text_leveled_up_surf.get_rect()
        text_leveled_up_rect.center = (260, 146)

        level_up_text.append((text_leveled_up_surf, text_leveled_up_rect))
        level_up_window.append(level_up_win)


def quest_box_draw(quest_npc, draw_condition, garan_quest_window, maurelle_quest_window, celeste_quest_window,
                   torune_quest_window, accept_button, decline_button):

    if not draw_condition:
        quest_box.clear()
    else:
        if quest_npc.name == "garan":
            quest_box.append(garan_quest_window)
        if quest_npc.name == "maurelle":
            quest_box.append(maurelle_quest_window)
        if quest_npc.name == "celeste":
            quest_box.append(celeste_quest_window)
        if quest_npc.name == "torune":
            quest_box.append(torune_quest_window)

        quest_box.append(accept_button)
        quest_box.append(decline_button)


def quest_complete_draw(quest_npc, draw_condition, garan_quest_window, maurelle_quest_window, celeste_quest_window,
                        torune_quest_window):

    if not draw_condition:
        quest_complete_box.clear()
    else:
        if quest_npc.name == "garan":
            quest_complete_box.append(garan_quest_window)
        if quest_npc.name == "maurelle":
            quest_complete_box.append(maurelle_quest_window)
        if quest_npc.name == "celeste":
            quest_complete_box.append(celeste_quest_window)
        if quest_npc.name == "torune":
            quest_complete_box.append(torune_quest_window)


def equipment_updates(player, graphic):
    player_equipment.clear()
    try:
        if player.equipment["weapon"].name == "basic staff":
            player.equipment["weapon"].update(1078, 285, graphic["basic_staff_img"])
            player_equipment.append(player.equipment["weapon"])
        if player.equipment["weapon"].name == "basic sword":
            player.equipment["weapon"].update(1078, 285, graphic["basic_sword_img"])
            player_equipment.append(player.equipment["weapon"])
        if player.equipment["weapon"].name == "basic bow":
            player.equipment["weapon"].update(1078, 285, graphic["basic_bow_img"])
            player_equipment.append(player.equipment["weapon"])
        if player.equipment["torso"].name == "basic robes":
            player.equipment["torso"].update(1153, 197, graphic["basic_robes_img"])
            player_equipment.append(player.equipment["torso"])
        if player.equipment["torso"].name == "basic armor":
            player.equipment["torso"].update(1153, 197, graphic["basic_armor_img"])
            player_equipment.append(player.equipment["torso"])
        if player.equipment["torso"].name == "basic tunic":
            player.equipment["torso"].update(1153, 197, graphic["basic_tunic_img"])
            player_equipment.append(player.equipment["torso"])
        if player.equipment["gloves"].name == "power gloves":
            player.equipment["gloves"].update(1078, 197, graphic["gloves"])
            player_equipment.append(player.equipment["gloves"])
    except AttributeError:
        pass


def item_updates(player, graphic):
    player_items.clear()

    if len(player.items) > 0:
        first_coord = 1063
        second_coord = 462
        try:
            inventory_counter = 0

            for item_here in player.items:
                if item_here.name == "health potion":
                    item_here.update(first_coord, second_coord, graphic["health_pot_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "energy potion":
                    item_here.update(first_coord, second_coord, graphic["energy_pot_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "shiny rock":
                    item_here.update(first_coord, second_coord, graphic["shiny_rock_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "bone dust":
                    item_here.update(first_coord, second_coord, graphic["bone_dust_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic staff":
                    item_here.update(first_coord, second_coord, graphic["basic_staff_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic sword":
                    item_here.update(first_coord, second_coord, graphic["basic_sword_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic bow":
                    item_here.update(first_coord, second_coord, graphic["basic_bow_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic robes":
                    item_here.update(first_coord, second_coord, graphic["basic_robes_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic armor":
                    item_here.update(first_coord, second_coord, graphic["basic_armor_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic tunic":
                    item_here.update(first_coord, second_coord, graphic["basic_tunic_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "boss key":
                    item_here.update(first_coord, second_coord, graphic["key_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "power gloves":
                    item_here.update(first_coord, second_coord, graphic["gloves"])
                    player_items.append(item_here)
                    inventory_counter += 1

                first_coord += 60

                if inventory_counter > 3:
                    second_coord += 60
                    first_coord = 1063
                    inventory_counter = 0

        except AttributeError:
            pass
