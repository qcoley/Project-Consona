character_sheet_text = []
character_sheet_window = []
journal_text = []
journal_window = []
level_up_text = []
level_up_window = []
quest_box = []


def draw_it(screen):

    for character_window in character_sheet_window:
        screen.blit(character_window.surf, character_window.rect)
    for character_text in character_sheet_text:
        screen.blit(character_text[0], character_text[1])
    for journals_window in journal_window:
        screen.blit(journals_window.surf, journals_window.rect)
    for journals_text in journal_text:
        screen.blit(journals_text[0], journals_text[1])
    for level_ups_window in level_up_window:
        screen.blit(level_ups_window.surf, level_ups_window.rect)
    for level_ups_text in level_up_text:
        screen.blit(level_ups_text[0], level_ups_text[1])
    for quest_element in quest_box:
        screen.blit(quest_element.surf, quest_element.rect)


def text_info_draw(scaled_1024, scaled_1280, scaled_1600, screen, player, font, info_text_1, info_text_2, info_text_3,
                   info_text_4):

    # get current player rupee count and create surf and rectangle to blit to screen------------------------------------
    text_rupee_surf = font.render(str(player.rupees), True, "black", "light yellow")
    text_rupee_rect = text_rupee_surf.get_rect()
    if scaled_1024:
        text_rupee_rect.center = (1120 * .80, 693 * .80)
    if scaled_1280:
        text_rupee_rect.center = (1120, 693)
    if scaled_1600:
        text_rupee_rect.center = (1120 / .80, 693 / .80)
    screen.blit(text_rupee_surf, text_rupee_rect)
    # get current player district and create surf and rectangle to blit to screen---------------------------------------
    text_zone_surf = font.render(str(player.current_zone), True, "black", "light yellow")
    text_zone_rect = text_zone_surf.get_rect()
    if scaled_1024:
        text_zone_rect.center = (1225 * .80, 693 * .80)
    if scaled_1280:
        text_zone_rect.center = (1225, 693)
    if scaled_1600:
        text_zone_rect.center = (1225 / .80, 693 / .80)
    screen.blit(text_zone_surf, text_zone_rect)
    # get current player district and create surf and rectangle to blit to screen---------------------------------------
    text_level_surf = font.render(str(player.level), True, "black", "light yellow")
    text_level_rect = text_level_surf.get_rect()
    if scaled_1024:
        text_level_rect.center = (1105 * .80, 362 * .80)
    if scaled_1280:
        text_level_rect.center = (1105, 362)
    if scaled_1600:
        text_level_rect.center = (1105 / .80, 362 / .80)
    screen.blit(text_level_surf, text_level_rect)
    # get current player role and create surf and rectangle to blit to screen-------------------------------------------
    text_role_surf = font.render(str(player.role), True, "black", "light yellow")
    text_role_rect = text_role_surf.get_rect()
    if scaled_1024:
        text_role_rect.center = (1220 * .80, 362 * .80)
    if scaled_1280:
        text_role_rect.center = (1220, 362)
    if scaled_1600:
        text_role_rect.center = (1220 / .80, 362 / .80)
    screen.blit(text_role_surf, text_role_rect)
    # get current player offense and create surf and rectangle to blit to screen----------------------------------------
    text_offense_surf = font.render(str(player.offense), True, "black", "light yellow")
    text_offense_rect = text_offense_surf.get_rect()
    if scaled_1024:
        text_offense_rect.center = (1135 * .80, 82 * .80)
    if scaled_1280:
        text_offense_rect.center = (1135, 82)
    if scaled_1600:
        text_offense_rect.center = (1135 / .80, 82 / .80)
    screen.blit(text_offense_surf, text_offense_rect)
    # get current player defence and create surf and rectangle to blit to screen----------------------------------------
    text_defence_surf = font.render(str(player.defence), True, "black", "light yellow")
    text_defence_rect = text_defence_surf.get_rect()
    if scaled_1024:
        text_defence_rect.center = (1135 * .80, 120 * .80)
    if scaled_1280:
        text_defence_rect.center = (1135, 120)
    if scaled_1600:
        text_defence_rect.center = (1135 / .80, 120 / .80)
    screen.blit(text_defence_surf, text_defence_rect)
    # current info text for message box in lower left corner of screen, first line--------------------------------------
    text_info_surf_1 = font.render(info_text_1, True, "black", "light yellow")
    text_info_rect_1 = text_info_surf_1.get_rect()
    if scaled_1024:
        text_info_rect_1.midleft = (30 * .80, 630 * .80)
    if scaled_1280:
        text_info_rect_1.midleft = (30, 630)
    if scaled_1600:
        text_info_rect_1.midleft = (30 / .80, 630 / .80)
    screen.blit(text_info_surf_1, text_info_rect_1)
    # current info text for message box in lower left corner of screen, second line-------------------------------------
    text_info_surf_2 = font.render(info_text_2, True, "black", "light yellow")
    text_info_rect_2 = text_info_surf_2.get_rect()
    if scaled_1024:
        text_info_rect_2.midleft = (30 * .80, 650 * .80)
    if scaled_1280:
        text_info_rect_2.midleft = (30, 650)
    if scaled_1600:
        text_info_rect_2.midleft = (30 / .80, 650 / .80)
    screen.blit(text_info_surf_2, text_info_rect_2)
    # current info text for message box in lower left corner of screen, third line--------------------------------------
    text_info_surf_3 = font.render(info_text_3, True, "black", "light yellow")
    text_info_rect_3 = text_info_surf_3.get_rect()
    if scaled_1024:
        text_info_rect_3.midleft = (30 * .80, 670 * .80)
    if scaled_1280:
        text_info_rect_3.midleft = (30, 670)
    if scaled_1600:
        text_info_rect_3.midleft = (30 / .80, 670 / .80)
    screen.blit(text_info_surf_3, text_info_rect_3)
    # current info text for message box in lower left corner of screen, fourth line-------------------------------------
    text_info_surf_4 = font.render(info_text_4, True, "black", "light yellow")
    text_info_rect_4 = text_info_surf_4.get_rect()
    if scaled_1024:
        text_info_rect_4.midleft = (30 * .80, 690 * .80)
    if scaled_1280:
        text_info_rect_4.midleft = (30, 690)
    if scaled_1600:
        text_info_rect_4.midleft = (30 / .80, 690 / .80)
    screen.blit(text_info_surf_4, text_info_rect_4)


def character_sheet_info_draw(character_sheet, scaled_1024, scaled_1280, scaled_1600, player, font, draw_condition):

    if not draw_condition:
        character_sheet_text.clear()
        character_sheet_window.clear()

    else:
        text_name_surf = font.render(str(player.name), True, "black", "light yellow")
        text_name_rect = text_name_surf.get_rect()
        if scaled_1024:
            text_name_rect.center = (650 * .80, 152 * .80)
        if scaled_1280:
            text_name_rect.center = (650, 152)
        if scaled_1600:
            text_name_rect.center = (650 / .80, 152 / .80 + 10)
        text_race_surf = font.render(str(player.race), True, "black", "light yellow")
        text_race_rect = text_race_surf.get_rect()
        if scaled_1024:
            text_race_rect.center = (642 * .80, 190 * .80)
        if scaled_1280:
            text_race_rect.center = (642, 190)
        if scaled_1600:
            text_race_rect.center = (642 / .80, 190 / .80 + 10)
        text_gender_surf = font.render(str(player.gender), True, "black", "light yellow")
        text_gender_rect = text_gender_surf.get_rect()
        if scaled_1024:
            text_gender_rect.center = (658 * .80, 228 * .80)
        if scaled_1280:
            text_gender_rect.center = (658, 228)
        if scaled_1600:
            text_gender_rect.center = (658 / .80, 228 / .80 + 10)
        text_rolled_surf = font.render(str(player.role), True, "black", "light yellow")
        text_rolled_rect = text_rolled_surf.get_rect()
        if scaled_1024:
            text_rolled_rect.center = (630 * .80, 267 * .80)
        if scaled_1280:
            text_rolled_rect.center = (630, 267)
        if scaled_1600:
            text_rolled_rect.center = (630 / .80, 267 / .80 + 5)
        text_health_surf = font.render(str(player.health), True, "black", "light yellow")
        text_health_rect = text_health_surf.get_rect()
        if scaled_1024:
            text_health_rect.center = (900 * .80, 151 * .80)
        if scaled_1280:
            text_health_rect.center = (900, 151)
        if scaled_1600:
            text_health_rect.center = (900 / .80, 151 / .80 + 10)
        text_energy_surf = font.render(str(player.energy), True, "black", "light yellow")
        text_energy_rect = text_energy_surf.get_rect()
        if scaled_1024:
            text_energy_rect.center = (900 * .80, 189 * .80)
        if scaled_1280:
            text_energy_rect.center = (900, 189)
        if scaled_1600:
            text_energy_rect.center = (900 / .80, 189 / .80 + 10)
        text_experience_surf = font.render(str(player.experience), True, "black", "light yellow")
        text_experience_rect = text_experience_surf.get_rect()
        if scaled_1024:
            text_experience_rect.center = (922 * .80, 229 * .80)
        if scaled_1280:
            text_experience_rect.center = (922, 229)
        if scaled_1600:
            text_experience_rect.center = (922 / .80, 229 / .80 + 10)
        text_leveled_surf = font.render(str(player.level), True, "black", "light yellow")
        text_leveled_rect = text_leveled_surf.get_rect()
        if scaled_1024:
            text_leveled_rect.center = (618 * .80, 328 * .80)
        if scaled_1280:
            text_leveled_rect.center = (618, 328)
        if scaled_1600:
            text_leveled_rect.center = (618 / .80 + 8, 328 / .80 + 2)
        text_mage_surf = font.render(str(player.knowledge["mage"]), True, "black", "light yellow")
        text_mage_rect = text_mage_surf.get_rect()
        if scaled_1024:
            text_mage_rect.center = (710 * .80, 366 * .80)
        if scaled_1280:
            text_mage_rect.center = (710, 366)
        if scaled_1600:
            text_mage_rect.center = (710 / .80, 366 / .80)
        text_fighter_surf = font.render(str(player.knowledge["fighter"]), True, "black", "light yellow")
        text_fighter_rect = text_fighter_surf.get_rect()
        if scaled_1024:
            text_fighter_rect.center = (718 * .80, 404 * .80)
        if scaled_1280:
            text_fighter_rect.center = (718, 404)
        if scaled_1600:
            text_fighter_rect.center = (718 / .80, 404 / .80)
        text_scout_surf = font.render(str(player.knowledge["scout"]), True, "black", "light yellow")
        text_scout_rect = text_scout_surf.get_rect()
        if scaled_1024:
            text_scout_rect.center = (710 * .80, 443 * .80)
        if scaled_1280:
            text_scout_rect.center = (710, 443)
        if scaled_1600:
            text_scout_rect.center = (710 / .80, 443 / .80)
        text_amuna_surf = font.render(str(player.reputation["amuna"]), True, "black", "light yellow")
        text_amuna_rect = text_amuna_surf.get_rect()
        if scaled_1024:
            text_amuna_rect.center = (720 * .80, 517 * .80)
        if scaled_1280:
            text_amuna_rect.center = (720, 517)
        if scaled_1600:
            text_amuna_rect.center = (720 / .80, 517 / .80 - 5)
        text_nuldar_surf = font.render(str(player.reputation["nuldar"]), True, "black", "light yellow")
        text_nuldar_rect = text_nuldar_surf.get_rect()
        if scaled_1024:
            text_nuldar_rect.center = (715 * .80, 556 * .80)
        if scaled_1280:
            text_nuldar_rect.center = (715, 556)
        if scaled_1600:
            text_nuldar_rect.center = (715 / .80, 556 / .80 - 10)
        text_sorae_surf = font.render(str(player.reputation["sorae"]), True, "black", "light yellow")
        text_sorae_rect = text_sorae_surf.get_rect()
        if scaled_1024:
            text_sorae_rect.center = (708 * .80, 594 * .80)
        if scaled_1280:
            text_sorae_rect.center = (708, 594)
        if scaled_1600:
            text_sorae_rect.center = (708 / .80, 594 / .80 - 10)
        text_mage_skills_surf = font.render(str(player.skills_mage["skill 2"]), True, "black", "light yellow")
        text_mage_skills_rect = text_mage_skills_surf.get_rect()
        if scaled_1024:
            text_mage_skills_rect.center = (935 * .80, 366 * .80)
        if scaled_1280:
            text_mage_skills_rect.center = (935, 366)
        if scaled_1600:
            text_mage_skills_rect.center = (935 / .80, 366 / .80 + 10)
        text_fighter_skills_surf = font.render(str(player.skills_fighter["skill 2"]), True, "black", "light yellow")
        text_fighter_skills_rect = text_fighter_skills_surf.get_rect()
        if scaled_1024:
            text_fighter_skills_rect.center = (955 * .80, 404 * .80)
        if scaled_1280:
            text_fighter_skills_rect.center = (955, 404)
        if scaled_1600:
            text_fighter_skills_rect.center = (955 / .80, 404 / .80 + 10)
        text_scout_skills_surf = font.render(str(player.skills_scout["skill 2"]), True, "black", "light yellow")
        text_scout_skills_rect = text_scout_skills_surf.get_rect()
        if scaled_1024:
            text_scout_skills_rect.center = (950 * .80, 443 * .80)
        if scaled_1280:
            text_scout_skills_rect.center = (950, 443)
        if scaled_1600:
            text_scout_skills_rect.center = (950 / .80, 443 / .80 + 10)

        character_sheet_text.append((text_name_surf, text_name_rect))
        character_sheet_text.append((text_race_surf, text_race_rect))
        character_sheet_text.append((text_gender_surf, text_gender_rect))
        character_sheet_text.append((text_rolled_surf, text_rolled_rect))
        character_sheet_text.append((text_health_surf, text_health_rect))
        character_sheet_text.append((text_energy_surf, text_energy_rect))
        character_sheet_text.append((text_experience_surf, text_experience_rect))
        character_sheet_text.append((text_leveled_surf, text_leveled_rect))
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


def journal_info_draw(journal, scaled_1024, scaled_1280, scaled_1600, player, font, draw_condition):

    if not draw_condition:
        journal_text.clear()
        journal_window.clear()

    else:
        text_quest1_surf = font.render(str(list(player.current_quests)[0]), True, "black", "light yellow")
        text_quest1_rect = text_quest1_surf.get_rect()
        if scaled_1024:
            text_quest1_rect.center = (650 * .80, 145 * .80)
        if scaled_1280:
            text_quest1_rect.center = (650, 145)
        if scaled_1600:
            text_quest1_rect.center = (650 / .80, 145 / .80 + 10)
        text_quest1_info_surf = font.render(str(list(player.current_quests.values())[0]), True, "black", "light yellow")
        text_quest1_info_rect = text_quest1_info_surf.get_rect()
        if scaled_1024:
            text_quest1_info_rect.center = (760 * .80 + 5, 190 * .80)
        if scaled_1280:
            text_quest1_info_rect.center = (760, 190)
        if scaled_1600:
            text_quest1_info_rect.center = (760 / .80 + 5, 190 / .80)
        text_quest2_surf = font.render(str(list(player.current_quests)[1]), True, "black", "light yellow")
        text_quest2_rect = text_quest2_surf.get_rect()
        if scaled_1024:
            text_quest2_rect.center = (650 * .80, 272 * .80)
        if scaled_1280:
            text_quest2_rect.center = (650, 272)
        if scaled_1600:
            text_quest2_rect.center = (650 / .80, 272 / .80 + 5)
        text_quest2_info_surf = font.render(str(list(player.current_quests.values())[1]), True, "black", "light yellow")
        text_quest2_info_rect = text_quest2_info_surf.get_rect()
        if scaled_1024:
            text_quest2_info_rect.center = (725 * .80 + 5, 320 * .80)
        if scaled_1280:
            text_quest2_info_rect.center = (725, 320)
        if scaled_1600:
            text_quest2_info_rect.center = (725 / .80, 320 / .80)
        text_quest3_surf = font.render(str(list(player.current_quests)[2]), True, "black", "light yellow")
        text_quest3_rect = text_quest3_surf.get_rect()
        if scaled_1024:
            text_quest3_rect.center = (650 * .80, 405 * .80)
        if scaled_1280:
            text_quest3_rect.center = (650, 405)
        if scaled_1600:
            text_quest3_rect.center = (650 / .80, 405 / .80 - 2)
        text_quest3_info_surf = font.render(str(list(player.current_quests.values())[2]), True, "black", "light yellow")
        text_quest3_info_rect = text_quest3_info_surf.get_rect()
        if scaled_1024:
            text_quest3_info_rect.center = (755 * .80 + 5, 755 * .80)
        if scaled_1280:
            text_quest3_info_rect.center = (755, 455)
        if scaled_1600:
            text_quest3_info_rect.center = (755 / .80, 755 / .80)
        text_quest4_surf = font.render(str(list(player.current_quests)[3]), True, "black", "light yellow")
        text_quest4_rect = text_quest4_surf.get_rect()
        if scaled_1024:
            text_quest4_rect.center = (660 * .80, 538 * .80)
        if scaled_1280:
            text_quest4_rect.center = (660, 538)
        if scaled_1600:
            text_quest4_rect.center = (660 / .80, 538 / .80 - 10)
        text_quest4_info_surf = font.render(str(list(player.current_quests.values())[3]), True, "black", "light yellow")
        text_quest4_info_rect = text_quest4_info_surf.get_rect()
        if scaled_1024:
            text_quest4_info_rect.center = (618 * .80 + 5, 585 * .80)
        if scaled_1280:
            text_quest4_info_rect.center = (618, 585)
        if scaled_1600:
            text_quest4_info_rect.center = (618 / .80, 585 / .80 - 10)
        journal_text.append((text_quest1_surf, text_quest1_rect))
        journal_text.append((text_quest1_info_surf, text_quest1_info_rect))
        journal_text.append((text_quest2_surf, text_quest2_rect))
        journal_text.append((text_quest2_info_surf, text_quest2_info_rect))
        journal_text.append((text_quest3_surf, text_quest3_rect))
        journal_text.append((text_quest3_info_surf, text_quest3_info_rect))
        journal_text.append((text_quest4_surf, text_quest4_rect))
        journal_text.append((text_quest4_info_surf, text_quest4_info_rect))
        journal_window.append(journal)


def level_up_draw(level_up_win, scaled_1024, scaled_1280, scaled_1600, player, level_up_font, draw_condition):

    if not draw_condition:
        level_up_text.clear()
        level_up_window.clear()

    else:
        text_leveled_up_surf = level_up_font.render(str(player.level), True, "black", "light yellow")
        text_leveled_up_rect = text_leveled_up_surf.get_rect()
        if scaled_1024:
            text_leveled_up_rect.center = (660 * .80, 398 * .80)
        if scaled_1280:
            text_leveled_up_rect.center = (660, 398)
        if scaled_1600:
            text_leveled_up_rect.center = (660 / .80, 398 / .80)
        level_up_text.append((text_leveled_up_surf, text_leveled_up_rect))
        level_up_window.append(level_up_win)


def quest_box_draw(quest_npc, draw_condition, garan_quest_window, maurelle_quest_window, guard_quest_window,
                   accept_button, decline_button):

    if not draw_condition:
        quest_box.clear()

    else:
        if quest_npc.name == "garan":
            quest_box.append(garan_quest_window)
        if quest_npc.name == "maurelle":
            quest_box.append(maurelle_quest_window)
        if quest_npc.name == "guard":
            quest_box.append(guard_quest_window)

        quest_box.append(accept_button)
        quest_box.append(decline_button)

