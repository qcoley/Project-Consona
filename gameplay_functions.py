import random
import pickle
import time

import drawing_functions
import resource_urls


# quest stars for npcs that update based on player quest progress
def npc_quest_star_updates(player, star_garan, star_maurelle, star_celeste, star_torune):

    if not player.quest_complete["sneaky snakes"]:
        resource_urls.screen.blit(star_garan.surf, star_garan.rect)
    if player.quest_progress["sneaky snakes"] == 4:
        star_garan.update(210, 390, resource_urls.quest_complete_star)
    if player.quest_status["sneaky snakes"] and player.quest_progress["sneaky snakes"] != 4:
        star_garan.update(210, 390, resource_urls.quest_progress_star)

    if not player.quest_complete["where's nede?"]:
        resource_urls.screen.blit(star_celeste.surf, star_celeste.rect)
    if player.quest_progress["where's nede?"] == 1:
        star_celeste.update(760, 373, resource_urls.quest_complete_star)
    if player.quest_status["where's nede?"] and player.quest_progress["where's nede?"] != 1:
        star_celeste.update(760, 373, resource_urls.quest_progress_star)

    if not player.quest_complete["village repairs"]:
        resource_urls.screen.blit(star_maurelle.surf, star_maurelle.rect)
    if player.quest_progress["village repairs"] == 4:
        star_maurelle.update(744, 575, resource_urls.quest_complete_star)
    if player.quest_status["village repairs"] and player.quest_progress["village repairs"] != 4:
        star_maurelle.update(744, 575, resource_urls.quest_progress_star)

    if not player.quest_complete["ghouled again"]:
        resource_urls.screen.blit(star_torune.surf, star_torune.rect)
    if player.quest_progress["ghouled again"] == 4:
        star_torune.update(430, 75, resource_urls.quest_complete_star)
    if player.quest_status["ghouled again"] and player.quest_progress["ghouled again"] != 4:
        star_torune.update(430, 75, resource_urls.quest_progress_star)


def load_game(player, Item):
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
                    player.surf = resource_urls.player_mage_amuna_down_1
                if player.role == "fighter":
                    player.surf = resource_urls.player_fighter_amuna_down_1
                if player.role == "scout":
                    player.surf = resource_urls.player_scout_amuna_down_1
                else:
                    player.surf = resource_urls.player_no_role_amuna_down_1
            if player.race == "nuldar":
                if player.role == "mage":
                    player.surf = resource_urls.player_mage_nuldar_down_1
                if player.role == "fighter":
                    player.surf = resource_urls.player_fighter_nuldar_down_1
                if player.role == "scout":
                    player.surf = resource_urls.player_scout_nuldar_down_1
                else:
                    player.surf = resource_urls.player_no_role_nuldar_down_1
            if player.race == "sorae":
                if player.role == "mage":
                    player.surf = resource_urls.player_mage_sorae_down_1
                if player.role == "fighter":
                    player.surf = resource_urls.player_fighter_sorae_down_1
                if player.role == "scout":
                    player.surf = resource_urls.player_scout_sorae_down_1
                else:
                    player.surf = resource_urls.player_no_role_sorae_down_1

            # clear default starting items and load personal player items from save file
            player.items.clear()
            for item in player_load_info["inventory"]:
                if item == "health potion":
                    player.items.append(Item("health potion", "potion", 200, 200, resource_urls.health_pot_img))
                if item == "energy potion":
                    player.items.append(Item("energy potion", "potion", 200, 200, resource_urls.energy_pot_img))
                if item == "basic staff":
                    player.items.append(Item("basic staff", "mage", 200, 200, resource_urls.basic_staff_img))
                if item == "basic sword":
                    player.items.append(Item("basic sword", "fighter", 200, 200, resource_urls.basic_sword_img))
                if item == "basic bow":
                    player.items.append(Item("basic bow", "scout", 200, 200, resource_urls.basic_bow_img))
                if item == "basic robes":
                    player.items.append(Item("basic robes", "mage", 200, 200, resource_urls.basic_robes_img))
                if item == "basic armor":
                    player.items.append(Item("basic armor", "fighter", 200, 200, resource_urls.basic_armor_img))
                if item == "basic tunic":
                    player.items.append(Item("basic tunic", "scout", 200, 200, resource_urls.basic_tunic_img))
                if item == "shiny rock":
                    player.items.append(Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_img))
                if item == "bone dust":
                    player.items.append(Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_img))

            for equipped_item in player_load_info["equipment"]:
                if equipped_item == "basic staff":
                    player.equipment["weapon"] = Item("basic staff", "mage", 200, 200, resource_urls.basic_staff_img)
                if equipped_item == "basic sword":
                    player.equipment["weapon"] = Item("basic sword", "fighter", 200, 200, resource_urls.basic_sword_img)
                if equipped_item == "basic bow":
                    player.equipment["weapon"] = Item("basic bow", "scout", 200, 200, resource_urls.basic_bow_img)
                if equipped_item == "basic robes":
                    player.equipment["chest"] = Item("basic robes", "mage", 200, 200, resource_urls.basic_robes_img)
                if equipped_item == "basic armor":
                    player.equipment["chest"] = Item("basic armor", "fighter", 200, 200, resource_urls.basic_armor_img)
                if equipped_item == "basic tunic":
                    player.equipment["chest"] = Item("basic tunic", "scout", 200, 200, resource_urls.basic_tunic_img)

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
            load_return["rest popup"] = player_load_info["rest popup"]
            load_return["knowledge popup"] = player_load_info["knowledge popup"]
            load_return["start"] = True
            load_return["continue"] = False

    # no save file found, show a notification to player and reset condition
    except FileNotFoundError:
        load_return["continue"] = False
        load_return["not found"] = True
        pass

    return load_return


# save game function. stores player info in a dictionary that's serialized and saved to save_game file
def save_game(player, barrier_learned, hard_strike_learned, sharp_sense_learned, saved, garan_gift,
              rest_popup, knowledge_popup):
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
                        "learned":
                            {"barrier": barrier_learned, "strike": hard_strike_learned, "sense": sharp_sense_learned},
                        "rupees": int(player.rupees), "reputation": dict(player.reputation),
                        "zone": str(player.current_zone), "saved": saved,
                        "rest popup": rest_popup, "knowledge popup": knowledge_popup}
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
def player_info_and_ui_updates(player, hp_bar, en_bar, xp_bar, star_power_meter):
    # update players status bars
    hp_bar.update(hp_bar.x_coordinate, hp_bar.y_coordinate, health_bar_update(player))
    en_bar.update(en_bar.x_coordinate, en_bar.y_coordinate, energy_bar_update(player))
    xp_bar.update(xp_bar.x_coordinate, xp_bar.y_coordinate, xp_bar_update(player))

    if player.star_power == 0:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, resource_urls.star_00)
    if player.star_power == 1:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, resource_urls.star_01)
    if player.star_power == 2:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, resource_urls.star_02)
    if player.star_power == 3:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, resource_urls.star_03)
    if player.star_power == 4:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, resource_urls.star_04)

    # update players current equipment
    drawing_functions.equipment_updates(player)
    # update players current inventory
    drawing_functions.item_updates(player)


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
def health_bar_update(character):
    if character.health == 100:
        return resource_urls.hp_100
    if character.health == 99:
        return resource_urls.hp_99
    if character.health == 98:
        return resource_urls.hp_98
    if character.health == 97:
        return resource_urls.hp_97
    if character.health == 96:
        return resource_urls.hp_96
    if character.health == 95:
        return resource_urls.hp_95
    if character.health == 94:
        return resource_urls.hp_94
    if character.health == 93:
        return resource_urls.hp_93
    if character.health == 92:
        return resource_urls.hp_92
    if character.health == 91:
        return resource_urls.hp_91
    if character.health == 90:
        return resource_urls.hp_90
    if character.health == 89:
        return resource_urls.hp_89
    if character.health == 88:
        return resource_urls.hp_88
    if character.health == 87:
        return resource_urls.hp_87
    if character.health == 86:
        return resource_urls.hp_86
    if character.health == 85:
        return resource_urls.hp_85
    if character.health == 84:
        return resource_urls.hp_84
    if character.health == 83:
        return resource_urls.hp_83
    if character.health == 82:
        return resource_urls.hp_82
    if character.health == 81:
        return resource_urls.hp_81
    if character.health == 80:
        return resource_urls.hp_80
    if character.health == 79:
        return resource_urls.hp_79
    if character.health == 78:
        return resource_urls.hp_78
    if character.health == 77:
        return resource_urls.hp_77
    if character.health == 76:
        return resource_urls.hp_76
    if character.health == 75:
        return resource_urls.hp_75
    if character.health == 74:
        return resource_urls.hp_74
    if character.health == 73:
        return resource_urls.hp_73
    if character.health == 72:
        return resource_urls.hp_72
    if character.health == 71:
        return resource_urls.hp_71
    if character.health == 70:
        return resource_urls.hp_70
    if character.health == 69:
        return resource_urls.hp_69
    if character.health == 68:
        return resource_urls.hp_68
    if character.health == 67:
        return resource_urls.hp_67
    if character.health == 66:
        return resource_urls.hp_66
    if character.health == 65:
        return resource_urls.hp_65
    if character.health == 64:
        return resource_urls.hp_64
    if character.health == 63:
        return resource_urls.hp_63
    if character.health == 62:
        return resource_urls.hp_62
    if character.health == 61:
        return resource_urls.hp_61
    if character.health == 60:
        return resource_urls.hp_60
    if character.health == 59:
        return resource_urls.hp_59
    if character.health == 58:
        return resource_urls.hp_58
    if character.health == 57:
        return resource_urls.hp_57
    if character.health == 56:
        return resource_urls.hp_56
    if character.health == 55:
        return resource_urls.hp_55
    if character.health == 54:
        return resource_urls.hp_54
    if character.health == 53:
        return resource_urls.hp_53
    if character.health == 52:
        return resource_urls.hp_52
    if character.health == 51:
        return resource_urls.hp_51
    if character.health == 50:
        return resource_urls.hp_50
    if character.health == 49:
        return resource_urls.hp_49
    if character.health == 48:
        return resource_urls.hp_48
    if character.health == 47:
        return resource_urls.hp_47
    if character.health == 46:
        return resource_urls.hp_46
    if character.health == 45:
        return resource_urls.hp_45
    if character.health == 44:
        return resource_urls.hp_44
    if character.health == 43:
        return resource_urls.hp_43
    if character.health == 42:
        return resource_urls.hp_42
    if character.health == 41:
        return resource_urls.hp_41
    if character.health == 40:
        return resource_urls.hp_40
    if character.health == 39:
        return resource_urls.hp_39
    if character.health == 38:
        return resource_urls.hp_38
    if character.health == 37:
        return resource_urls.hp_37
    if character.health == 36:
        return resource_urls.hp_36
    if character.health == 35:
        return resource_urls.hp_35
    if character.health == 34:
        return resource_urls.hp_34
    if character.health == 33:
        return resource_urls.hp_33
    if character.health == 32:
        return resource_urls.hp_32
    if character.health == 31:
        return resource_urls.hp_31
    if character.health == 30:
        return resource_urls.hp_30
    if character.health == 29:
        return resource_urls.hp_29
    if character.health == 28:
        return resource_urls.hp_28
    if character.health == 27:
        return resource_urls.hp_27
    if character.health == 26:
        return resource_urls.hp_26
    if character.health == 25:
        return resource_urls.hp_25
    if character.health == 24:
        return resource_urls.hp_24
    if character.health == 23:
        return resource_urls.hp_23
    if character.health == 22:
        return resource_urls.hp_22
    if character.health == 21:
        return resource_urls.hp_21
    if character.health == 20:
        return resource_urls.hp_20
    if character.health == 19:
        return resource_urls.hp_19
    if character.health == 18:
        return resource_urls.hp_18
    if character.health == 17:
        return resource_urls.hp_17
    if character.health == 16:
        return resource_urls.hp_16
    if character.health == 15:
        return resource_urls.hp_15
    if character.health == 14:
        return resource_urls.hp_14
    if character.health == 13:
        return resource_urls.hp_13
    if character.health == 12:
        return resource_urls.hp_12
    if character.health == 11:
        return resource_urls.hp_11
    if character.health == 10:
        return resource_urls.hp_10
    if character.health == 9:
        return resource_urls.hp_9
    if character.health == 8:
        return resource_urls.hp_8
    if character.health == 7:
        return resource_urls.hp_7
    if character.health == 6:
        return resource_urls.hp_6
    if character.health == 5:
        return resource_urls.hp_5
    if character.health == 4:
        return resource_urls.hp_4
    if character.health == 3:
        return resource_urls.hp_3
    if character.health == 2:
        return resource_urls.hp_2
    if character.health == 1:
        return resource_urls.hp_1
    if character.health == 0:
        return resource_urls.hp_0


# player energy bar update function. return image representing amount
def energy_bar_update(character):
    if character.energy == 100:
        return resource_urls.en_100
    if character.energy == 99:
        return resource_urls.en_99
    if character.energy == 98:
        return resource_urls.en_98
    if character.energy == 97:
        return resource_urls.en_97
    if character.energy == 96:
        return resource_urls.en_96
    if character.energy == 95:
        return resource_urls.en_95
    if character.energy == 94:
        return resource_urls.en_94
    if character.energy == 93:
        return resource_urls.en_93
    if character.energy == 92:
        return resource_urls.en_92
    if character.energy == 91:
        return resource_urls.en_91
    if character.energy == 90:
        return resource_urls.en_90
    if character.energy == 89:
        return resource_urls.en_89
    if character.energy == 88:
        return resource_urls.en_88
    if character.energy == 87:
        return resource_urls.en_87
    if character.energy == 86:
        return resource_urls.en_86
    if character.energy == 85:
        return resource_urls.en_85
    if character.energy == 84:
        return resource_urls.en_84
    if character.energy == 83:
        return resource_urls.en_83
    if character.energy == 82:
        return resource_urls.en_82
    if character.energy == 81:
        return resource_urls.en_81
    if character.energy == 80:
        return resource_urls.en_80
    if character.energy == 79:
        return resource_urls.en_79
    if character.energy == 78:
        return resource_urls.en_78
    if character.energy == 77:
        return resource_urls.en_77
    if character.energy == 76:
        return resource_urls.en_76
    if character.energy == 75:
        return resource_urls.en_75
    if character.energy == 74:
        return resource_urls.en_74
    if character.energy == 73:
        return resource_urls.en_73
    if character.energy == 72:
        return resource_urls.en_72
    if character.energy == 71:
        return resource_urls.en_71
    if character.energy == 70:
        return resource_urls.en_70
    if character.energy == 69:
        return resource_urls.en_69
    if character.energy == 68:
        return resource_urls.en_68
    if character.energy == 67:
        return resource_urls.en_67
    if character.energy == 66:
        return resource_urls.en_66
    if character.energy == 65:
        return resource_urls.en_65
    if character.energy == 64:
        return resource_urls.en_64
    if character.energy == 63:
        return resource_urls.en_63
    if character.energy == 62:
        return resource_urls.en_62
    if character.energy == 61:
        return resource_urls.en_61
    if character.energy == 60:
        return resource_urls.en_60
    if character.energy == 59:
        return resource_urls.en_59
    if character.energy == 58:
        return resource_urls.en_58
    if character.energy == 57:
        return resource_urls.en_57
    if character.energy == 56:
        return resource_urls.en_56
    if character.energy == 55:
        return resource_urls.en_55
    if character.energy == 54:
        return resource_urls.en_54
    if character.energy == 53:
        return resource_urls.en_53
    if character.energy == 52:
        return resource_urls.en_52
    if character.energy == 51:
        return resource_urls.en_51
    if character.energy == 50:
        return resource_urls.en_50
    if character.energy == 49:
        return resource_urls.en_49
    if character.energy == 48:
        return resource_urls.en_48
    if character.energy == 47:
        return resource_urls.en_47
    if character.energy == 46:
        return resource_urls.en_46
    if character.energy == 45:
        return resource_urls.en_45
    if character.energy == 44:
        return resource_urls.en_44
    if character.energy == 43:
        return resource_urls.en_43
    if character.energy == 42:
        return resource_urls.en_42
    if character.energy == 41:
        return resource_urls.en_41
    if character.energy == 40:
        return resource_urls.en_40
    if character.energy == 39:
        return resource_urls.en_39
    if character.energy == 38:
        return resource_urls.en_38
    if character.energy == 37:
        return resource_urls.en_37
    if character.energy == 36:
        return resource_urls.en_36
    if character.energy == 35:
        return resource_urls.en_35
    if character.energy == 34:
        return resource_urls.en_34
    if character.energy == 33:
        return resource_urls.en_33
    if character.energy == 32:
        return resource_urls.en_32
    if character.energy == 31:
        return resource_urls.en_31
    if character.energy == 30:
        return resource_urls.en_30
    if character.energy == 29:
        return resource_urls.en_29
    if character.energy == 28:
        return resource_urls.en_28
    if character.energy == 27:
        return resource_urls.en_27
    if character.energy == 26:
        return resource_urls.en_26
    if character.energy == 25:
        return resource_urls.en_25
    if character.energy == 24:
        return resource_urls.en_24
    if character.energy == 23:
        return resource_urls.en_23
    if character.energy == 22:
        return resource_urls.en_22
    if character.energy == 21:
        return resource_urls.en_21
    if character.energy == 20:
        return resource_urls.en_20
    if character.energy == 19:
        return resource_urls.en_19
    if character.energy == 18:
        return resource_urls.en_18
    if character.energy == 17:
        return resource_urls.en_17
    if character.energy == 16:
        return resource_urls.en_16
    if character.energy == 15:
        return resource_urls.en_15
    if character.energy == 14:
        return resource_urls.en_14
    if character.energy == 13:
        return resource_urls.en_13
    if character.energy == 12:
        return resource_urls.en_12
    if character.energy == 11:
        return resource_urls.en_11
    if character.energy == 10:
        return resource_urls.en_10
    if character.energy == 9:
        return resource_urls.en_9
    if character.energy == 8:
        return resource_urls.en_8
    if character.energy == 7:
        return resource_urls.en_7
    if character.energy == 6:
        return resource_urls.en_6
    if character.energy == 5:
        return resource_urls.en_5
    if character.energy == 4:
        return resource_urls.en_4
    if character.energy == 3:
        return resource_urls.en_3
    if character.energy == 2:
        return resource_urls.en_2
    if character.energy == 1:
        return resource_urls.en_1
    if character.energy == 0:
        return resource_urls.en_0


# player xp bar update function. return image representing amount
def xp_bar_update(character):
    if character.experience == 100:
        return resource_urls.xp_100
    if character.experience == 99:
        return resource_urls.xp_99
    if character.experience == 98:
        return resource_urls.xp_98
    if character.experience == 97:
        return resource_urls.xp_97
    if character.experience == 96:
        return resource_urls.xp_96
    if character.experience == 95:
        return resource_urls.xp_95
    if character.experience == 94:
        return resource_urls.xp_94
    if character.experience == 93:
        return resource_urls.xp_93
    if character.experience == 92:
        return resource_urls.xp_92
    if character.experience == 91:
        return resource_urls.xp_91
    if character.experience == 90:
        return resource_urls.xp_90
    if character.experience == 89:
        return resource_urls.xp_89
    if character.experience == 88:
        return resource_urls.xp_88
    if character.experience == 87:
        return resource_urls.xp_87
    if character.experience == 86:
        return resource_urls.xp_86
    if character.experience == 85:
        return resource_urls.xp_85
    if character.experience == 84:
        return resource_urls.xp_84
    if character.experience == 83:
        return resource_urls.xp_83
    if character.experience == 82:
        return resource_urls.xp_82
    if character.experience == 81:
        return resource_urls.xp_81
    if character.experience == 80:
        return resource_urls.xp_80
    if character.experience == 79:
        return resource_urls.xp_79
    if character.experience == 78:
        return resource_urls.xp_78
    if character.experience == 77:
        return resource_urls.xp_77
    if character.experience == 76:
        return resource_urls.xp_76
    if character.experience == 75:
        return resource_urls.xp_75
    if character.experience == 74:
        return resource_urls.xp_74
    if character.experience == 73:
        return resource_urls.xp_73
    if character.experience == 72:
        return resource_urls.xp_72
    if character.experience == 71:
        return resource_urls.xp_71
    if character.experience == 70:
        return resource_urls.xp_70
    if character.experience == 69:
        return resource_urls.xp_69
    if character.experience == 68:
        return resource_urls.xp_68
    if character.experience == 67:
        return resource_urls.xp_67
    if character.experience == 66:
        return resource_urls.xp_66
    if character.experience == 65:
        return resource_urls.xp_65
    if character.experience == 64:
        return resource_urls.xp_64
    if character.experience == 63:
        return resource_urls.xp_63
    if character.experience == 62:
        return resource_urls.xp_62
    if character.experience == 61:
        return resource_urls.xp_61
    if character.experience == 60:
        return resource_urls.xp_60
    if character.experience == 59:
        return resource_urls.xp_59
    if character.experience == 58:
        return resource_urls.xp_58
    if character.experience == 57:
        return resource_urls.xp_57
    if character.experience == 56:
        return resource_urls.xp_56
    if character.experience == 55:
        return resource_urls.xp_55
    if character.experience == 54:
        return resource_urls.xp_54
    if character.experience == 53:
        return resource_urls.xp_53
    if character.experience == 52:
        return resource_urls.xp_52
    if character.experience == 51:
        return resource_urls.xp_51
    if character.experience == 50:
        return resource_urls.xp_50
    if character.experience == 49:
        return resource_urls.xp_49
    if character.experience == 48:
        return resource_urls.xp_48
    if character.experience == 47:
        return resource_urls.xp_47
    if character.experience == 46:
        return resource_urls.xp_46
    if character.experience == 45:
        return resource_urls.xp_45
    if character.experience == 44:
        return resource_urls.xp_44
    if character.experience == 43:
        return resource_urls.xp_43
    if character.experience == 42:
        return resource_urls.xp_42
    if character.experience == 41:
        return resource_urls.xp_41
    if character.experience == 40:
        return resource_urls.xp_40
    if character.experience == 39:
        return resource_urls.xp_39
    if character.experience == 38:
        return resource_urls.xp_38
    if character.experience == 37:
        return resource_urls.xp_37
    if character.experience == 36:
        return resource_urls.xp_36
    if character.experience == 35:
        return resource_urls.xp_35
    if character.experience == 34:
        return resource_urls.xp_34
    if character.experience == 33:
        return resource_urls.xp_33
    if character.experience == 32:
        return resource_urls.xp_32
    if character.experience == 31:
        return resource_urls.xp_31
    if character.experience == 30:
        return resource_urls.xp_30
    if character.experience == 29:
        return resource_urls.xp_29
    if character.experience == 28:
        return resource_urls.xp_28
    if character.experience == 27:
        return resource_urls.xp_27
    if character.experience == 26:
        return resource_urls.xp_26
    if character.experience == 25:
        return resource_urls.xp_25
    if character.experience == 24:
        return resource_urls.xp_24
    if character.experience == 23:
        return resource_urls.xp_23
    if character.experience == 22:
        return resource_urls.xp_22
    if character.experience == 21:
        return resource_urls.xp_21
    if character.experience == 20:
        return resource_urls.xp_20
    if character.experience == 19:
        return resource_urls.xp_19
    if character.experience == 18:
        return resource_urls.xp_18
    if character.experience == 17:
        return resource_urls.xp_17
    if character.experience == 16:
        return resource_urls.xp_16
    if character.experience == 15:
        return resource_urls.xp_15
    if character.experience == 14:
        return resource_urls.xp_14
    if character.experience == 13:
        return resource_urls.xp_13
    if character.experience == 12:
        return resource_urls.xp_12
    if character.experience == 11:
        return resource_urls.xp_11
    if character.experience == 10:
        return resource_urls.xp_10
    if character.experience == 9:
        return resource_urls.xp_9
    if character.experience == 8:
        return resource_urls.xp_8
    if character.experience == 7:
        return resource_urls.xp_7
    if character.experience == 6:
        return resource_urls.xp_6
    if character.experience == 5:
        return resource_urls.xp_5
    if character.experience == 4:
        return resource_urls.xp_4
    if character.experience == 3:
        return resource_urls.xp_3
    if character.experience == 2:
        return resource_urls.xp_2
    if character.experience == 1:
        return resource_urls.xp_1
    if character.experience == 0:
        return resource_urls.xp_0
