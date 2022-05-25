import drawing_functions
import random
import pickle
import time


# quest stars for npcs that update based on player quest progress
def npc_quest_star_updates(player, screen, quest_star_garan, quest_star_maurelle, quest_star_celeste, quest_star_torune,
                           quest_progress_star, quest_complete_star):
    if not player.quest_complete["sneaky snakes"]:
        screen.blit(quest_star_garan.surf, quest_star_garan.rect)
    if player.quest_progress["sneaky snakes"] == 4:
        quest_star_garan.update(210, 390, quest_complete_star)
    if player.quest_status["sneaky snakes"] and player.quest_progress["sneaky snakes"] != 4:
        quest_star_garan.update(210, 390, quest_progress_star)
    # ------------------------------------------------------------------------------------------------------------------
    if not player.quest_complete["where's nede?"]:
        screen.blit(quest_star_celeste.surf, quest_star_celeste.rect)
    if player.quest_progress["where's nede?"] == 1:
        quest_star_celeste.update(760, 373, quest_complete_star)
    if player.quest_status["where's nede?"] and player.quest_progress["where's nede?"] != 1:
        quest_star_celeste.update(760, 373, quest_progress_star)
    # ------------------------------------------------------------------------------------------------------------------
    if not player.quest_complete["village repairs"]:
        screen.blit(quest_star_maurelle.surf, quest_star_maurelle.rect)
    if player.quest_progress["village repairs"] == 4:
        quest_star_maurelle.update(744, 575, quest_complete_star)
    if player.quest_status["village repairs"] and player.quest_progress["village repairs"] != 4:
        quest_star_maurelle.update(744, 575, quest_progress_star)
    # ------------------------------------------------------------------------------------------------------------------
    if not player.quest_complete["ghouled again"]:
        screen.blit(quest_star_torune.surf, quest_star_torune.rect)
    if player.quest_progress["ghouled again"] == 4:
        quest_star_torune.update(430, 75, quest_complete_star)
    if player.quest_status["ghouled again"] and player.quest_progress["ghouled again"] != 4:
        quest_star_torune.update(430, 75, quest_progress_star)


def load_game(player, player_no_role_amuna_down_1, player_scout_amuna_down_1, player_fighter_amuna_down_1,
              player_mage_amuna_down_1, player_no_role_nuldar_down_1, player_scout_nuldar_down_1,
              player_fighter_nuldar_down_1, player_mage_nuldar_down_1, player_no_role_sorae_down_1,
              player_scout_sorae_down_1, player_fighter_sorae_down_1, player_mage_sorae_down_1, Item,
              health_pot_img, energy_pot_img, basic_staff_img, basic_sword_img, basic_bow_img, basic_robes_img,
              basic_armor_img, basic_tunic_img, shiny_rock_img, bone_dust_img):
    load_return = {"barrier learned": False, "strike learned": False, "sensed learned": False,
                   "saved": False, "start": False, "continue": False, "not found": False, "garan gift": False}
    try:
        with open("save_game", "rb") as f:
            player_load_info = pickle.load(f)
            player.name = player_load_info["name"]
            player.level = player_load_info["level"]
            player.health = player_load_info["hp"]
            player.energy = player_load_info["en"]
            player.offense = player_load_info["offense"]
            player.defense = player_load_info["defense"]
            player.experience = player_load_info["xp"]
            player.race = player_load_info["race"]
            player.role = player_load_info["role"]

            if player.race == "amuna":
                if player.role == "mage":
                    player.surf = player_mage_amuna_down_1
                if player.role == "fighter":
                    player.surf = player_fighter_amuna_down_1
                if player.role == "scout":
                    player.surf = player_scout_amuna_down_1
                else:
                    player.surf = player_no_role_amuna_down_1
            if player.race == "nuldar":
                if player.role == "mage":
                    player.surf = player_mage_nuldar_down_1
                if player.role == "fighter":
                    player.surf = player_fighter_nuldar_down_1
                if player.role == "scout":
                    player.surf = player_scout_nuldar_down_1
                else:
                    player.surf = player_no_role_nuldar_down_1
            if player.race == "sorae":
                if player.role == "mage":
                    player.surf = player_mage_sorae_down_1
                if player.role == "fighter":
                    player.surf = player_fighter_sorae_down_1
                if player.role == "scout":
                    player.surf = player_scout_sorae_down_1
                else:
                    player.surf = player_no_role_sorae_down_1

            # clear default starting items and load personal player items from save file
            player.items.clear()
            for item in player_load_info["inventory"]:
                if item == "health potion":
                    player.items.append(Item("health potion", "potion", 200, 200, health_pot_img))
                if item == "energy potion":
                    player.items.append(Item("energy potion", "potion", 200, 200, energy_pot_img))
                if item == "basic staff":
                    player.items.append(Item("basic staff", "mage", 200, 200, basic_staff_img))
                if item == "basic sword":
                    player.items.append(Item("basic sword", "fighter", 200, 200, basic_sword_img))
                if item == "basic bow":
                    player.items.append(Item("basic bow", "scout", 200, 200, basic_bow_img))
                if item == "basic robes":
                    player.items.append(Item("basic robes", "mage", 200, 200, basic_robes_img))
                if item == "basic armor":
                    player.items.append(Item("basic armor", "fighter", 200, 200, basic_armor_img))
                if item == "basic tunic":
                    player.items.append(Item("basic tunic", "scout", 200, 200, basic_tunic_img))
                if item == "shiny rock":
                    player.items.append(Item("shiny rock", "rock", 200, 200, shiny_rock_img))
                if item == "bone dust":
                    player.items.append(Item("bone dust", "dust", 200, 200, bone_dust_img))

            for equipped_item in player_load_info["equipment"]:
                if equipped_item == "basic staff":
                    player.equipment["weapon"] = Item("basic staff", "mage", 200, 200, basic_staff_img)
                if equipped_item == "basic sword":
                    player.equipment["weapon"] = Item("basic sword", "fighter", 200, 200, basic_sword_img)
                if equipped_item == "basic bow":
                    player.equipment["weapon"] = Item("basic bow", "scout", 200, 200, basic_bow_img)
                if equipped_item == "basic robes":
                    player.equipment["chest"] = Item("basic robes", "mage", 200, 200, basic_robes_img)
                if equipped_item == "basic armor":
                    player.equipment["chest"] = Item("basic armor", "fighter", 200, 200, basic_armor_img)
                if equipped_item == "basic tunic":
                    player.equipment["chest"] = Item("basic tunic", "scout", 200, 200, basic_tunic_img)

            player.current_quests = player_load_info["quests"]
            player.quest_progress = player_load_info["quest progress"]
            player.quest_status = player_load_info["quest status"]
            player.quest_complete = player_load_info["quest complete"]
            player.knowledge = player_load_info["knowledge"]
            player.skills_mage = player_load_info["mage skills"]
            player.skills_fighter = player_load_info["fighter skills"]
            player.skills_scout = player_load_info["scout skills"]
            load_return["barrier learned"] = player_load_info["learned"]["barrier"]
            load_return["strike learned"] = player_load_info["learned"]["strike"]
            load_return["sense learned"] = player_load_info["learned"]["sense"]
            player.rupees = player_load_info["rupees"]
            player.reputation = player_load_info["reputation"]
            player.current_zone = player_load_info["zone"]

            if player.current_zone == "nascent":
                player.x_coordinate = 760
                player.y_coordinate = 510
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
            if player.current_zone == "seldon":
                player.x_coordinate = 425
                player.y_coordinate = 690
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
            if player.current_zone == "korlok":
                player.x_coordinate = 500
                player.y_coordinate = 500
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

            load_return["saved"] = player_load_info["saved"]
            load_return["garan gift"] = player_load_info["garan gift"]
            load_return["start"] = True
            load_return["continue"] = False

    # no save file found, show a notification to player and reset condition
    except FileNotFoundError:
        load_return["continue"] = False
        load_return["not found"] = True
        pass

    return load_return


# save game function. stores player info in a dictionary that's serialized and saved to save_game file
def save_game(player, barrier_learned, hard_strike_learned, sharp_sense_learned, saved, garan_gift):
    inventory_save = []
    equipment_save = []
    # a sprite surface object cannot be serialized, so save the string item name instead
    try:
        for item_x in player.items:
            inventory_save.append(item_x.name)
        equipment_save.append(player.equipment["weapon"].name)
        equipment_save.append(player.equipment["chest"].name)
    except AttributeError:
        pass
    player_save_info = {"name": str(player.name), "race": str(player.race),
                        "level": int(player.level), "role": str(player.role),
                        "inventory": inventory_save, "equipment": equipment_save,
                        "hp": int(player.health), "en": int(player.energy), "xp": int(player.experience),
                        "offense": int(player.offense), "defense": int(player.defense),
                        "quests": dict(player.current_quests),
                        "garan gift": garan_gift,
                        "quest progress": dict(player.quest_progress),
                        "quest status": dict(player.quest_status),
                        "quest complete": dict(player.quest_complete),
                        "knowledge": dict(player.knowledge),
                        "mage skills": dict(player.skills_mage),
                        "fighter skills": dict(player.skills_fighter),
                        "scout skills": dict(player.skills_scout),
                        "learned": {"barrier": barrier_learned,
                                    "strike": hard_strike_learned,
                                    "sense": sharp_sense_learned},
                        "rupees": int(player.rupees), "reputation": dict(player.reputation),
                        "zone": str(player.current_zone), "saved": saved}
    # serialize dictionary and save to file ("save game") with python pickle (wb = write binary)
    with open("save_game", "wb") as ff:
        pickle.dump(player_save_info, ff)


# function to handle player walking animation with time values
def walk_time(tic):
    walk_dict = {"total time": 0, "reset": False}
    toc = time.perf_counter()
    walk_dict["total time"] = toc - tic
    if walk_dict["total time"] > 0.8:
        walk_dict["reset"] = True

    return walk_dict


# function that updates players info, status, role, inventory, equipment, etc
def player_info_and_ui_updates(player, screen, hp_bar, en_bar, xp_bar, in_over_world, status_bar_backdrop,
                               hp_100, hp_99, hp_98, hp_97, hp_96, hp_95, hp_94, hp_93, hp_92, hp_91,
                               hp_90, hp_89, hp_88, hp_87, hp_86, hp_85, hp_84, hp_83, hp_82, hp_81,
                               hp_80, hp_79, hp_78, hp_77, hp_76, hp_75, hp_74, hp_73, hp_72, hp_71,
                               hp_70, hp_69, hp_68, hp_67, hp_66, hp_65, hp_64, hp_63, hp_62, hp_61,
                               hp_60, hp_59, hp_58, hp_57, hp_56, hp_55, hp_54, hp_53, hp_52, hp_51,
                               hp_50, hp_49, hp_48, hp_47, hp_46, hp_45, hp_44, hp_43, hp_42, hp_41,
                               hp_40, hp_39, hp_38, hp_37, hp_36, hp_35, hp_34, hp_33, hp_32, hp_31,
                               hp_30, hp_29, hp_28, hp_27, hp_26, hp_25, hp_24, hp_23, hp_22, hp_21,
                               hp_20, hp_19, hp_18, hp_17, hp_16, hp_15, hp_14, hp_13, hp_12, hp_11,
                               hp_10, hp_9, hp_8, hp_7, hp_6, hp_5, hp_4, hp_3, hp_2, hp_1, hp_0,
                               en_100, en_99, en_98, en_97, en_96, en_95, en_94, en_93, en_92, en_91,
                               en_90, en_89, en_88, en_87, en_86, en_85, en_84, en_83, en_82, en_81,
                               en_80, en_79, en_78, en_77, en_76, en_75, en_74, en_73, en_72, en_71,
                               en_70, en_69, en_68, en_67, en_66, en_65, en_64, en_63, en_62, en_61,
                               en_60, en_59, en_58, en_57, en_56, en_55, en_54, en_53, en_52, en_51,
                               en_50, en_49, en_48, en_47, en_46, en_45, en_44, en_43, en_42, en_41,
                               en_40, en_39, en_38, en_37, en_36, en_35, en_34, en_33, en_32, en_31,
                               en_30, en_29, en_28, en_27, en_26, en_25, en_24, en_23, en_22, en_21,
                               en_20, en_19, en_18, en_17, en_16, en_15, en_14, en_13, en_12, en_11,
                               en_10, en_9, en_8, en_7, en_6, en_5, en_4, en_3, en_2, en_1, en_0,
                               xp_100, xp_99, xp_98, xp_97, xp_96, xp_95, xp_94, xp_93, xp_92, xp_91,
                               xp_90, xp_89, xp_88, xp_87, xp_86, xp_85, xp_84, xp_83, xp_82, xp_81,
                               xp_80, xp_79, xp_78, xp_77, xp_76, xp_75, xp_74, xp_73, xp_72, xp_71,
                               xp_70, xp_69, xp_68, xp_67, xp_66, xp_65, xp_64, xp_63, xp_62, xp_61,
                               xp_60, xp_59, xp_58, xp_57, xp_56, xp_55, xp_54, xp_53, xp_52, xp_51,
                               xp_50, xp_49, xp_48, xp_47, xp_46, xp_45, xp_44, xp_43, xp_42, xp_41,
                               xp_40, xp_39, xp_38, xp_37, xp_36, xp_35, xp_34, xp_33, xp_32, xp_31,
                               xp_30, xp_29, xp_28, xp_27, xp_26, xp_25, xp_24, xp_23, xp_22, xp_21,
                               xp_20, xp_19, xp_18, xp_17, xp_16, xp_15, xp_14, xp_13, xp_12, xp_11,
                               xp_10, xp_9, xp_8, xp_7, xp_6, xp_5, xp_4, xp_3, xp_2, xp_1, xp_0,
                               user_interface, save_check_window, font,
                               info_text_1, info_text_2, info_text_3, info_text_4,
                               health_pot_img, energy_pot_img, shiny_rock_img, bone_dust_img,
                               basic_staff_img, basic_sword_img, basic_bow_img,
                               basic_robes_img, basic_armor_img, basic_tunic_img, temp_img,
                               star_power_meter, star_00, star_01, star_02, star_03, star_04):

    screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
    try:
        screen.blit(hp_bar.surf, hp_bar.rect)
        screen.blit(en_bar.surf, en_bar.rect)
        screen.blit(xp_bar.surf, xp_bar.rect)
    except TypeError:
        pass

    # update players status bars
    hp_bar.update(hp_bar.x_coordinate, hp_bar.y_coordinate, health_bar_update(player,
                                                                              hp_100, hp_99, hp_98, hp_97, hp_96, hp_95,
                                                                              hp_94, hp_93, hp_92, hp_91, hp_90, hp_89,
                                                                              hp_88, hp_87, hp_86, hp_85, hp_84, hp_83,
                                                                              hp_82, hp_81, hp_80, hp_79, hp_78, hp_77,
                                                                              hp_76, hp_75, hp_74, hp_73, hp_72, hp_71,
                                                                              hp_70, hp_69, hp_68, hp_67, hp_66, hp_65,
                                                                              hp_64, hp_63, hp_62, hp_61, hp_60, hp_59,
                                                                              hp_58, hp_57, hp_56, hp_55, hp_54, hp_53,
                                                                              hp_52, hp_51, hp_50, hp_49, hp_48, hp_47,
                                                                              hp_46, hp_45, hp_44, hp_43, hp_42, hp_41,
                                                                              hp_40, hp_39, hp_38, hp_37, hp_36, hp_35,
                                                                              hp_34, hp_33, hp_32, hp_31, hp_30, hp_29,
                                                                              hp_28, hp_27, hp_26, hp_25, hp_24, hp_23,
                                                                              hp_22, hp_21, hp_20, hp_19, hp_18, hp_17,
                                                                              hp_16, hp_15, hp_14, hp_13, hp_12, hp_11,
                                                                              hp_10, hp_9, hp_8, hp_7, hp_6, hp_5, hp_4,
                                                                              hp_3, hp_2, hp_1, hp_0))

    en_bar.update(en_bar.x_coordinate, en_bar.y_coordinate, energy_bar_update(player,
                                                                              en_100, en_99, en_98, en_97, en_96, en_95,
                                                                              en_94, en_93, en_92, en_91, en_90, en_89,
                                                                              en_88, en_87, en_86, en_85, en_84, en_83,
                                                                              en_82, en_81, en_80, en_79, en_78, en_77,
                                                                              en_76, en_75, en_74, en_73, en_72, en_71,
                                                                              en_70, en_69, en_68, en_67, en_66, en_65,
                                                                              en_64, en_63, en_62, en_61, en_60, en_59,
                                                                              en_58, en_57, en_56, en_55, en_54, en_53,
                                                                              en_52, en_51, en_50, en_49, en_48, en_47,
                                                                              en_46, en_45, en_44, en_43, en_42, en_41,
                                                                              en_40, en_39, en_38, en_37, en_36, en_35,
                                                                              en_34, en_33, en_32, en_31, en_30, en_29,
                                                                              en_28, en_27, en_26, en_25, en_24, en_23,
                                                                              en_22, en_21, en_20, en_19, en_18, en_17,
                                                                              en_16, en_15, en_14, en_13, en_12, en_11,
                                                                              en_10, en_9, en_8, en_7, en_6, en_5, en_4,
                                                                              en_3, en_2, en_1, en_0))

    xp_bar.update(xp_bar.x_coordinate, xp_bar.y_coordinate, xp_bar_update(player,
                                                                          xp_100, xp_99, xp_98, xp_97, xp_96, xp_95,
                                                                          xp_94, xp_93, xp_92, xp_91, xp_90, xp_89,
                                                                          xp_88, xp_87, xp_86, xp_85, xp_84, xp_83,
                                                                          xp_82, xp_81, xp_80, xp_79, xp_78, xp_77,
                                                                          xp_76, xp_75, xp_74, xp_73, xp_72, xp_71,
                                                                          xp_70, xp_69, xp_68, xp_67, xp_66, xp_65,
                                                                          xp_64, xp_63, xp_62, xp_61, xp_60, xp_59,
                                                                          xp_58, xp_57, xp_56, xp_55, xp_54, xp_53,
                                                                          xp_52, xp_51, xp_50, xp_49, xp_48, xp_47,
                                                                          xp_46, xp_45, xp_44, xp_43, xp_42, xp_41,
                                                                          xp_40, xp_39, xp_38, xp_37, xp_36, xp_35,
                                                                          xp_34, xp_33, xp_32, xp_31, xp_30, xp_29,
                                                                          xp_28, xp_27, xp_26, xp_25, xp_24, xp_23,
                                                                          xp_22, xp_21, xp_20, xp_19, xp_18, xp_17,
                                                                          xp_16, xp_15, xp_14, xp_13, xp_12, xp_11,
                                                                          xp_10, xp_9, xp_8, xp_7, xp_6, xp_5, xp_4,
                                                                          xp_3, xp_2, xp_1, xp_0))

    if in_over_world:
        screen.blit(player.surf, player.rect)
        for save_window in save_check_window:
            screen.blit(save_window.surf, save_window.rect)
        for ui_elements in user_interface:
            screen.blit(ui_elements.surf, ui_elements.rect)

    if player.star_power == 0:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, star_00)
    if player.star_power == 1:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, star_01)
    if player.star_power == 2:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, star_02)
    if player.star_power == 3:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, star_03)
    if player.star_power == 4:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, star_04)

    screen.blit(star_power_meter.surf, star_power_meter.rect)

    # draw texts to the screen, like message box, player rupees and level
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4)
    # update players current equipment
    drawing_functions.equipment_updates(player, basic_staff_img, basic_sword_img, basic_bow_img,
                                        basic_robes_img, basic_armor_img, basic_tunic_img)
    # update players current inventory
    drawing_functions.item_updates(player, health_pot_img, energy_pot_img, shiny_rock_img, bone_dust_img,
                                   basic_staff_img, basic_sword_img, basic_bow_img,
                                   basic_robes_img, basic_armor_img, basic_tunic_img, temp_img)
    drawing_functions.draw_it(screen)


# player attacks enemy, gets damage to enemy done based on player's role and offense
def attack_enemy(player, mob):
    # if player is lower level than mob, scale their damage based on the difference of their levels
    if player.level < mob.level:
        difference = mob.level - player.level
    # if player is equal level or higher level than mob, just return full damage value
    else:
        difference = 1
    # scale damage based on player's offense stat and level difference
    if player.role == "mage":
        damage = (random.randrange(16, player.offense) // difference)
        return damage
    if player.role == "scout":
        damage = (random.randrange(12, player.offense) // difference)
        return damage
    if player.role == "fighter":
        damage = (random.randrange(8, player.offense) // difference)
        return damage
    if player.role == "":
        if player.offense != 0:
            damage = (random.randrange(1, player.offense) // difference)
            return damage
        else:
            return 1


# enemy attacks player, gets damage to player done, subtract players defense level
def attack_player(player, mob):
    base_damage = (random.randrange(12, 20))
    difference = mob.level - player.level
    # add additional damage if enemy is a higher level than player
    if difference >= 1:
        base_damage = base_damage + 3
    if difference >= 2:
        base_damage = base_damage + 5
    if difference >= 3:
        base_damage = base_damage + 8
    final_damage = base_damage - player.defense

    return final_damage


# level up function. increase player level by 1 if not at cap and return info in dictionary
def level_up(player, level_up_win, level_up_font):
    level_up_dictionary = {"new level": 0, "player stats": []}

    if player.level < 20:
        player.level = player.level + 1
        player.health = 100
        player.energy = 100
        player.experience = player.experience - 100
        drawing_functions.level_up_draw(level_up_win, player, level_up_font, True)
    else:
        level_up_dictionary["new level"] = "You are already max level. "
        return level_up_dictionary


# player health bar update function. return image representing amount
def health_bar_update(character, hp_100, hp_99, hp_98, hp_97, hp_96, hp_95, hp_94, hp_93, hp_92, hp_91, hp_90,
                      hp_89, hp_88, hp_87, hp_86, hp_85, hp_84, hp_83, hp_82, hp_81, hp_80,
                      hp_79, hp_78, hp_77, hp_76, hp_75, hp_74, hp_73, hp_72, hp_71, hp_70,
                      hp_69, hp_68, hp_67, hp_66, hp_65, hp_64, hp_63, hp_62, hp_61, hp_60,
                      hp_59, hp_58, hp_57, hp_56, hp_55, hp_54, hp_53, hp_52, hp_51, hp_50,
                      hp_49, hp_48, hp_47, hp_46, hp_45, hp_44, hp_43, hp_42, hp_41, hp_40,
                      hp_39, hp_38, hp_37, hp_36, hp_35, hp_34, hp_33, hp_32, hp_31, hp_30,
                      hp_29, hp_28, hp_27, hp_26, hp_25, hp_24, hp_23, hp_22, hp_21, hp_20,
                      hp_19, hp_18, hp_17, hp_16, hp_15, hp_14, hp_13, hp_12, hp_11, hp_10,
                      hp_9, hp_8, hp_7, hp_6, hp_5, hp_4, hp_3, hp_2, hp_1, hp_0):
    if character.health == 100:
        return hp_100
    if character.health == 99:
        return hp_99
    if character.health == 98:
        return hp_98
    if character.health == 97:
        return hp_97
    if character.health == 96:
        return hp_96
    if character.health == 95:
        return hp_95
    if character.health == 94:
        return hp_94
    if character.health == 93:
        return hp_93
    if character.health == 92:
        return hp_92
    if character.health == 91:
        return hp_91
    if character.health == 90:
        return hp_90
    if character.health == 89:
        return hp_89
    if character.health == 88:
        return hp_88
    if character.health == 87:
        return hp_87
    if character.health == 86:
        return hp_86
    if character.health == 85:
        return hp_85
    if character.health == 84:
        return hp_84
    if character.health == 83:
        return hp_83
    if character.health == 82:
        return hp_82
    if character.health == 81:
        return hp_81
    if character.health == 80:
        return hp_80
    if character.health == 79:
        return hp_79
    if character.health == 78:
        return hp_78
    if character.health == 77:
        return hp_77
    if character.health == 76:
        return hp_76
    if character.health == 75:
        return hp_75
    if character.health == 74:
        return hp_74
    if character.health == 73:
        return hp_73
    if character.health == 72:
        return hp_72
    if character.health == 71:
        return hp_71
    if character.health == 70:
        return hp_70
    if character.health == 69:
        return hp_69
    if character.health == 68:
        return hp_68
    if character.health == 67:
        return hp_67
    if character.health == 66:
        return hp_66
    if character.health == 65:
        return hp_65
    if character.health == 64:
        return hp_64
    if character.health == 63:
        return hp_63
    if character.health == 62:
        return hp_62
    if character.health == 61:
        return hp_61
    if character.health == 60:
        return hp_60
    if character.health == 59:
        return hp_59
    if character.health == 58:
        return hp_58
    if character.health == 57:
        return hp_57
    if character.health == 56:
        return hp_56
    if character.health == 55:
        return hp_55
    if character.health == 54:
        return hp_54
    if character.health == 53:
        return hp_53
    if character.health == 52:
        return hp_52
    if character.health == 51:
        return hp_51
    if character.health == 50:
        return hp_50
    if character.health == 49:
        return hp_49
    if character.health == 48:
        return hp_48
    if character.health == 47:
        return hp_47
    if character.health == 46:
        return hp_46
    if character.health == 45:
        return hp_45
    if character.health == 44:
        return hp_44
    if character.health == 43:
        return hp_43
    if character.health == 42:
        return hp_42
    if character.health == 41:
        return hp_41
    if character.health == 40:
        return hp_40
    if character.health == 39:
        return hp_39
    if character.health == 38:
        return hp_38
    if character.health == 37:
        return hp_37
    if character.health == 36:
        return hp_36
    if character.health == 35:
        return hp_35
    if character.health == 34:
        return hp_34
    if character.health == 33:
        return hp_33
    if character.health == 32:
        return hp_32
    if character.health == 31:
        return hp_31
    if character.health == 30:
        return hp_30
    if character.health == 29:
        return hp_29
    if character.health == 28:
        return hp_28
    if character.health == 27:
        return hp_27
    if character.health == 26:
        return hp_26
    if character.health == 25:
        return hp_25
    if character.health == 24:
        return hp_24
    if character.health == 23:
        return hp_23
    if character.health == 22:
        return hp_22
    if character.health == 21:
        return hp_21
    if character.health == 20:
        return hp_20
    if character.health == 19:
        return hp_19
    if character.health == 18:
        return hp_18
    if character.health == 17:
        return hp_17
    if character.health == 16:
        return hp_16
    if character.health == 15:
        return hp_15
    if character.health == 14:
        return hp_14
    if character.health == 13:
        return hp_13
    if character.health == 12:
        return hp_12
    if character.health == 11:
        return hp_11
    if character.health == 10:
        return hp_10
    if character.health == 9:
        return hp_9
    if character.health == 8:
        return hp_8
    if character.health == 7:
        return hp_7
    if character.health == 6:
        return hp_6
    if character.health == 5:
        return hp_5
    if character.health == 4:
        return hp_4
    if character.health == 3:
        return hp_3
    if character.health == 2:
        return hp_2
    if character.health == 1:
        return hp_1
    if character.health == 0:
        return hp_0


# player energy bar update function. return image representing amount
def energy_bar_update(character, en_100, en_99, en_98, en_97, en_96, en_95, en_94, en_93, en_92, en_91, en_90,
                      en_89, en_88, en_87, en_86, en_85, en_84, en_83, en_82, en_81, en_80,
                      en_79, en_78, en_77, en_76, en_75, en_74, en_73, en_72, en_71, en_70,
                      en_69, en_68, en_67, en_66, en_65, en_64, en_63, en_62, en_61, en_60,
                      en_59, en_58, en_57, en_56, en_55, en_54, en_53, en_52, en_51, en_50,
                      en_49, en_48, en_47, en_46, en_45, en_44, en_43, en_42, en_41, en_40,
                      en_39, en_38, en_37, en_36, en_35, en_34, en_33, en_32, en_31, en_30,
                      en_29, en_28, en_27, en_26, en_25, en_24, en_23, en_22, en_21, en_20,
                      en_19, en_18, en_17, en_16, en_15, en_14, en_13, en_12, en_11, en_10,
                      en_9, en_8, en_7, en_6, en_5, en_4, en_3, en_2, en_1, en_0):
    if character.energy == 100:
        return en_100
    if character.energy == 99:
        return en_99
    if character.energy == 98:
        return en_98
    if character.energy == 97:
        return en_97
    if character.energy == 96:
        return en_96
    if character.energy == 95:
        return en_95
    if character.energy == 94:
        return en_94
    if character.energy == 93:
        return en_93
    if character.energy == 92:
        return en_92
    if character.energy == 91:
        return en_91
    if character.energy == 90:
        return en_90
    if character.energy == 89:
        return en_89
    if character.energy == 88:
        return en_88
    if character.energy == 87:
        return en_87
    if character.energy == 86:
        return en_86
    if character.energy == 85:
        return en_85
    if character.energy == 84:
        return en_84
    if character.energy == 83:
        return en_83
    if character.energy == 82:
        return en_82
    if character.energy == 81:
        return en_81
    if character.energy == 80:
        return en_80
    if character.energy == 79:
        return en_79
    if character.energy == 78:
        return en_78
    if character.energy == 77:
        return en_77
    if character.energy == 76:
        return en_76
    if character.energy == 75:
        return en_75
    if character.energy == 74:
        return en_74
    if character.energy == 73:
        return en_73
    if character.energy == 72:
        return en_72
    if character.energy == 71:
        return en_71
    if character.energy == 70:
        return en_70
    if character.energy == 69:
        return en_69
    if character.energy == 68:
        return en_68
    if character.energy == 67:
        return en_67
    if character.energy == 66:
        return en_66
    if character.energy == 65:
        return en_65
    if character.energy == 64:
        return en_64
    if character.energy == 63:
        return en_63
    if character.energy == 62:
        return en_62
    if character.energy == 61:
        return en_61
    if character.energy == 60:
        return en_60
    if character.energy == 59:
        return en_59
    if character.energy == 58:
        return en_58
    if character.energy == 57:
        return en_57
    if character.energy == 56:
        return en_56
    if character.energy == 55:
        return en_55
    if character.energy == 54:
        return en_54
    if character.energy == 53:
        return en_53
    if character.energy == 52:
        return en_52
    if character.energy == 51:
        return en_51
    if character.energy == 50:
        return en_50
    if character.energy == 49:
        return en_49
    if character.energy == 48:
        return en_48
    if character.energy == 47:
        return en_47
    if character.energy == 46:
        return en_46
    if character.energy == 45:
        return en_45
    if character.energy == 44:
        return en_44
    if character.energy == 43:
        return en_43
    if character.energy == 42:
        return en_42
    if character.energy == 41:
        return en_41
    if character.energy == 40:
        return en_40
    if character.energy == 39:
        return en_39
    if character.energy == 38:
        return en_38
    if character.energy == 37:
        return en_37
    if character.energy == 36:
        return en_36
    if character.energy == 35:
        return en_35
    if character.energy == 34:
        return en_34
    if character.energy == 33:
        return en_33
    if character.energy == 32:
        return en_32
    if character.energy == 31:
        return en_31
    if character.energy == 30:
        return en_30
    if character.energy == 29:
        return en_29
    if character.energy == 28:
        return en_28
    if character.energy == 27:
        return en_27
    if character.energy == 26:
        return en_26
    if character.energy == 25:
        return en_25
    if character.energy == 24:
        return en_24
    if character.energy == 23:
        return en_23
    if character.energy == 22:
        return en_22
    if character.energy == 21:
        return en_21
    if character.energy == 20:
        return en_20
    if character.energy == 19:
        return en_19
    if character.energy == 18:
        return en_18
    if character.energy == 17:
        return en_17
    if character.energy == 16:
        return en_16
    if character.energy == 15:
        return en_15
    if character.energy == 14:
        return en_14
    if character.energy == 13:
        return en_13
    if character.energy == 12:
        return en_12
    if character.energy == 11:
        return en_11
    if character.energy == 10:
        return en_10
    if character.energy == 9:
        return en_9
    if character.energy == 8:
        return en_8
    if character.energy == 7:
        return en_7
    if character.energy == 6:
        return en_6
    if character.energy == 5:
        return en_5
    if character.energy == 4:
        return en_4
    if character.energy == 3:
        return en_3
    if character.energy == 2:
        return en_2
    if character.energy == 1:
        return en_1
    if character.energy == 0:
        return en_0


# player xp bar update function. return image representing amount
def xp_bar_update(character, xp_100, xp_99, xp_98, xp_97, xp_96, xp_95, xp_94, xp_93, xp_92, xp_91, xp_90,
                  xp_89, xp_88, xp_87, xp_86, xp_85, xp_84, xp_83, xp_82, xp_81, xp_80,
                  xp_79, xp_78, xp_77, xp_76, xp_75, xp_74, xp_73, xp_72, xp_71, xp_70,
                  xp_69, xp_68, xp_67, xp_66, xp_65, xp_64, xp_63, xp_62, xp_61, xp_60,
                  xp_59, xp_58, xp_57, xp_56, xp_55, xp_54, xp_53, xp_52, xp_51, xp_50,
                  xp_49, xp_48, xp_47, xp_46, xp_45, xp_44, xp_43, xp_42, xp_41, xp_40,
                  xp_39, xp_38, xp_37, xp_36, xp_35, xp_34, xp_33, xp_32, xp_31, xp_30,
                  xp_29, xp_28, xp_27, xp_26, xp_25, xp_24, xp_23, xp_22, xp_21, xp_20,
                  xp_19, xp_18, xp_17, xp_16, xp_15, xp_14, xp_13, xp_12, xp_11, xp_10,
                  xp_9, xp_8, xp_7, xp_6, xp_5, xp_4, xp_3, xp_2, xp_1, xp_0):
    if character.experience == 100:
        return xp_100
    if character.experience == 99:
        return xp_99
    if character.experience == 98:
        return xp_98
    if character.experience == 97:
        return xp_97
    if character.experience == 96:
        return xp_96
    if character.experience == 95:
        return xp_95
    if character.experience == 94:
        return xp_94
    if character.experience == 93:
        return xp_93
    if character.experience == 92:
        return xp_92
    if character.experience == 91:
        return xp_91
    if character.experience == 90:
        return xp_90
    if character.experience == 89:
        return xp_89
    if character.experience == 88:
        return xp_88
    if character.experience == 87:
        return xp_87
    if character.experience == 86:
        return xp_86
    if character.experience == 85:
        return xp_85
    if character.experience == 84:
        return xp_84
    if character.experience == 83:
        return xp_83
    if character.experience == 82:
        return xp_82
    if character.experience == 81:
        return xp_81
    if character.experience == 80:
        return xp_80
    if character.experience == 79:
        return xp_79
    if character.experience == 78:
        return xp_78
    if character.experience == 77:
        return xp_77
    if character.experience == 76:
        return xp_76
    if character.experience == 75:
        return xp_75
    if character.experience == 74:
        return xp_74
    if character.experience == 73:
        return xp_73
    if character.experience == 72:
        return xp_72
    if character.experience == 71:
        return xp_71
    if character.experience == 70:
        return xp_70
    if character.experience == 69:
        return xp_69
    if character.experience == 68:
        return xp_68
    if character.experience == 67:
        return xp_67
    if character.experience == 66:
        return xp_66
    if character.experience == 65:
        return xp_65
    if character.experience == 64:
        return xp_64
    if character.experience == 63:
        return xp_63
    if character.experience == 62:
        return xp_62
    if character.experience == 61:
        return xp_61
    if character.experience == 60:
        return xp_60
    if character.experience == 59:
        return xp_59
    if character.experience == 58:
        return xp_58
    if character.experience == 57:
        return xp_57
    if character.experience == 56:
        return xp_56
    if character.experience == 55:
        return xp_55
    if character.experience == 54:
        return xp_54
    if character.experience == 53:
        return xp_53
    if character.experience == 52:
        return xp_52
    if character.experience == 51:
        return xp_51
    if character.experience == 50:
        return xp_50
    if character.experience == 49:
        return xp_49
    if character.experience == 48:
        return xp_48
    if character.experience == 47:
        return xp_47
    if character.experience == 46:
        return xp_46
    if character.experience == 45:
        return xp_45
    if character.experience == 44:
        return xp_44
    if character.experience == 43:
        return xp_43
    if character.experience == 42:
        return xp_42
    if character.experience == 41:
        return xp_41
    if character.experience == 40:
        return xp_40
    if character.experience == 39:
        return xp_39
    if character.experience == 38:
        return xp_38
    if character.experience == 37:
        return xp_37
    if character.experience == 36:
        return xp_36
    if character.experience == 35:
        return xp_35
    if character.experience == 34:
        return xp_34
    if character.experience == 33:
        return xp_33
    if character.experience == 32:
        return xp_32
    if character.experience == 31:
        return xp_31
    if character.experience == 30:
        return xp_30
    if character.experience == 29:
        return xp_29
    if character.experience == 28:
        return xp_28
    if character.experience == 27:
        return xp_27
    if character.experience == 26:
        return xp_26
    if character.experience == 25:
        return xp_25
    if character.experience == 24:
        return xp_24
    if character.experience == 23:
        return xp_23
    if character.experience == 22:
        return xp_22
    if character.experience == 21:
        return xp_21
    if character.experience == 20:
        return xp_20
    if character.experience == 19:
        return xp_19
    if character.experience == 18:
        return xp_18
    if character.experience == 17:
        return xp_17
    if character.experience == 16:
        return xp_16
    if character.experience == 15:
        return xp_15
    if character.experience == 14:
        return xp_14
    if character.experience == 13:
        return xp_13
    if character.experience == 12:
        return xp_12
    if character.experience == 11:
        return xp_11
    if character.experience == 10:
        return xp_10
    if character.experience == 9:
        return xp_9
    if character.experience == 8:
        return xp_8
    if character.experience == 7:
        return xp_7
    if character.experience == 6:
        return xp_6
    if character.experience == 5:
        return xp_5
    if character.experience == 4:
        return xp_4
    if character.experience == 3:
        return xp_3
    if character.experience == 2:
        return xp_2
    if character.experience == 1:
        return xp_1
    if character.experience == 0:
        return xp_0
