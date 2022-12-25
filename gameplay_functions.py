import os
import random
import pickle
import time

import drawing_functions


# quest stars for npcs that update based on player quest progress
def npc_quest_star_updates(screen, player, star_garan, star_maurelle, star_celeste, star_torune,
                           quest_progress_star, quest_complete_star):
    if not player.quest_complete["sneaky snakes"]:
        screen.blit(star_garan.surf, star_garan.rect)
    if player.quest_progress["sneaky snakes"] == 4:
        star_garan.update(210, 390, quest_complete_star)
    if player.quest_status["sneaky snakes"] and player.quest_progress["sneaky snakes"] != 4:
        star_garan.update(210, 390, quest_progress_star)

    if not player.quest_complete["where's nede?"]:
        screen.blit(star_celeste.surf, star_celeste.rect)
    if player.quest_progress["where's nede?"] == 1:
        star_celeste.update(760, 373, quest_complete_star)
    if player.quest_status["where's nede?"] and player.quest_progress["where's nede?"] != 1:
        star_celeste.update(760, 373, quest_progress_star)

    if not player.quest_complete["village repairs"]:
        screen.blit(star_maurelle.surf, star_maurelle.rect)
    if player.quest_progress["village repairs"] == 4:
        star_maurelle.update(744, 575, quest_complete_star)
    if player.quest_status["village repairs"] and player.quest_progress["village repairs"] != 4:
        star_maurelle.update(744, 575, quest_progress_star)

    if not player.quest_complete["ghouled again"]:
        screen.blit(star_torune.surf, star_torune.rect)
    if player.quest_progress["ghouled again"] == 4:
        star_torune.update(430, 75, quest_complete_star)
    if player.quest_status["ghouled again"] and player.quest_progress["ghouled again"] != 4:
        star_torune.update(430, 75, quest_progress_star)


def load_game(player, Item, graphics):
    load_return = {"barrier learned": False, "strike learned": False, "sensed learned": False,
                   "saved": False, "start": False, "continue": False, "not found": False, "garan gift": False,
                   "offense upgrade": 0, "defense upgrade": 0}
    try:
        directory = os.getcwd()
        with open(directory + "/saves/save_game", "rb") as ff:
            player_load_info = pickle.load(ff)
            player.name = player_load_info["name"]
            player.level = player_load_info["level"]
            player.health = player_load_info["hp"]
            player.energy = player_load_info["en"]
            player.offense = player_load_info["offense"]
            player.defense = player_load_info["defense"]
            player.experience = player_load_info["xp"]
            player.race = player_load_info["race"]
            player.role = player_load_info["role"]
            player.star_power = player_load_info["star power"]

            if player.race == "amuna":
                if player.role == "mage":
                    player.surf = graphics["player_mage_amuna_down_1"]
                if player.role == "fighter":
                    player.surf = graphics["player_fighter_amuna_down_1"]
                if player.role == "scout":
                    player.surf = graphics["player_scout_amuna_down_1"]
                else:
                    player.surf = graphics["player_no_role_amuna_down_1"]
            if player.race == "nuldar":
                if player.role == "mage":
                    player.surf = graphics["player_mage_nuldar_down_1"]
                if player.role == "fighter":
                    player.surf = graphics["player_fighter_nuldar_down_1"]
                if player.role == "scout":
                    player.surf = graphics["player_scout_nuldar_down_1"]
                else:
                    player.surf = graphics["player_no_role_nuldar_down_1"]
            if player.race == "sorae":
                if player.role == "mage":
                    player.surf = graphics["player_mage_sorae_down_1"]
                if player.role == "fighter":
                    player.surf = graphics["player_fighter_sorae_down_1"]
                if player.role == "scout":
                    player.surf = graphics["player_scout_sorae_down_1"]
                else:
                    player.surf = graphics["player_no_role_sorae_down_1"]

            # clear default starting items and load personal player items from save file
            player.items.clear()
            for item in player_load_info["inventory"]:
                if item == "health potion":
                    player.items.append(Item("health potion", "potion", 200, 200, graphics["health_pot_img"]))
                if item == "energy potion":
                    player.items.append(Item("energy potion", "potion", 200, 200, graphics["energy_pot_img"]))
                if item == "basic staff":
                    player.items.append(Item("basic staff", "mage", 200, 200, graphics["basic_staff_img"]))
                if item == "basic sword":
                    player.items.append(Item("basic sword", "fighter", 200, 200, graphics["basic_sword_img"]))
                if item == "basic bow":
                    player.items.append(Item("basic bow", "scout", 200, 200, graphics["basic_bow_img"]))
                if item == "basic robes":
                    player.items.append(Item("basic robes", "mage", 200, 200, graphics["basic_robes_img"]))
                if item == "basic armor":
                    player.items.append(Item("basic armor", "fighter", 200, 200, graphics["basic_armor_img"]))
                if item == "basic tunic":
                    player.items.append(Item("basic tunic", "scout", 200, 200, graphics["basic_tunic_img"]))
                if item == "shiny rock":
                    player.items.append(Item("shiny rock", "rock", 200, 200, graphics["shiny_rock_img"]))
                if item == "bone dust":
                    player.items.append(Item("bone dust", "dust", 200, 200, graphics["bone_dust_img"]))
                if item == "boss key":
                    player.items.append(Item("boss key", "key", 200, 200, graphics["key_img"]))
                if item == "power gloves":
                    player.items.append(Item("power gloves", "gloves", 200, 200, graphics["gloves"]))

            for equipped_item in player_load_info["equipment"]:
                if equipped_item == "basic staff":
                    player.equipment["weapon"] = Item("basic staff", "mage", 200, 200, graphics["basic_staff_img"])
                if equipped_item == "basic sword":
                    player.equipment["weapon"] = Item("basic sword", "fighter", 200, 200, graphics["basic_sword_img"])
                if equipped_item == "basic bow":
                    player.equipment["weapon"] = Item("basic bow", "scout", 200, 200, graphics["basic_bow_img"])
                if equipped_item == "basic robes":
                    player.equipment["torso"] = Item("basic robes", "mage", 200, 200, graphics["basic_robes_img"])
                if equipped_item == "basic armor":
                    player.equipment["torso"] = Item("basic armor", "fighter", 200, 200, graphics["basic_armor_img"])
                if equipped_item == "basic tunic":
                    player.equipment["torso"] = Item("basic tunic", "scout", 200, 200, graphics["basic_tunic_img"])
                if equipped_item == "power gloves":
                    player.equipment["gloves"] = Item("power gloves", "gloves", 200, 200, graphics["gloves"])

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
            load_return["offense upgrade"] = player_load_info["offense upgrade"]
            load_return["defense upgrade"] = player_load_info["defense upgrade"]
            load_return["quest guide"] = player_load_info["quest guide"]
            load_return["battle guide"] = player_load_info["battle guide"]
            load_return["role guide"] = player_load_info["role guide"]
            load_return["upgrade guide"] = player_load_info["upgrade guide"]
            load_return["rest shown before"] = player_load_info["rest shown before"]
            load_return["quest highlight popup"] = player_load_info["quest highlight popup"]
            load_return["first drop popup"] = player_load_info["first drop popup"]
            load_return["bridge not repaired"] = player_load_info["bridge not repaired"]
            load_return["nede ghoul defeated"] = player_load_info["nede ghoul defeated"]
            load_return["bridge_cutscenes_not_viewed"] = player_load_info["bridge_cutscenes_not_viewed"]
            load_return["crate_1"] = player_load_info["crate_1"]
            load_return["crate_2"] = player_load_info["crate_2"]
            load_return["crate_3"] = player_load_info["crate_3"]
            load_return["crate_4"] = player_load_info["crate_4"]
            load_return["crate_5"] = player_load_info["crate_5"]
            load_return["switch_1"] = player_load_info["switch_1"]
            load_return["switch_2"] = player_load_info["switch_2"]
            load_return["switch_3"] = player_load_info["switch_3"]
            load_return["muchador_defeated"] = player_load_info["muchador_defeated"]
            load_return["mini_boss_1_defeated"] = player_load_info["mini_boss_1_defeated"]
            load_return["mini_boss_2_defeated"] = player_load_info["mini_boss_2_defeated"]
            load_return["has_key"] = player_load_info["has_key"]
            load_return["gloves_obtained"] = player_load_info["gloves_obtained"]
            load_return["korlok_attuned"] = player_load_info["korlok_attuned"]
            load_return["eldream_attuned"] = player_load_info["eldream_attuned"]
            load_return["start"] = True
            load_return["continue"] = False

    # no save file found, show a notification to player and reset condition
    except FileNotFoundError:
        load_return["continue"] = False
        load_return["not found"] = True

    return load_return


# save game function. stores player info in a dictionary that's serialized and saved to save_game file
def save_game(player, barrier_learned, hard_strike_learned, sharp_sense_learned, saved, garan_gift,
              rest_popup, knowledge_popup, offense_upgraded, defense_upgraded,
              quest_guide_shown, battle_guide_shown, role_guide_shown, upgrade_guide_shown, rest_shown_before,
              quest_highlight_popup, first_drop_popup, bridge_not_repaired, nede_ghoul_defeated,
              bridge_cutscenes_not_viewed, crate_1, crate_2, crate_3, crate_4, crate_5, switch_1, switch_2, switch_3,
              muchador_defeated, has_key, mini_boss_1_defeated, mini_boss_2_defeated, gloves_obtained, korlok_attuned,
              eldream_attuned):
    inventory_save = []
    equipment_save = []
    # a sprite surface object cannot be serialized, so save the string item name instead
    try:
        for item_x in player.items:
            inventory_save.append(item_x.name)
        equipment_save.append(player.equipment["weapon"].name)
        equipment_save.append(player.equipment["torso"].name)
        equipment_save.append(player.equipment["gloves"].name)
    except AttributeError:
        pass
    player_save_info = {"name": str(player.name), "race": str(player.race), "level": int(player.level),
                        "role": str(player.role), "inventory": inventory_save, "equipment": equipment_save,
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
                        "rest popup": rest_popup, "knowledge popup": knowledge_popup,
                        "star power": int(player.star_power),
                        "offense upgrade": int(offense_upgraded), "defense upgrade": int(defense_upgraded),
                        "quest guide": quest_guide_shown, "battle guide": battle_guide_shown,
                        "role guide": role_guide_shown, "upgrade guide": upgrade_guide_shown,
                        "rest shown before": rest_shown_before, "quest highlight popup": quest_highlight_popup,
                        "first drop popup": first_drop_popup, "bridge not repaired": bridge_not_repaired,
                        "nede ghoul defeated": nede_ghoul_defeated,
                        "bridge_cutscenes_not_viewed": bridge_cutscenes_not_viewed,
                        "crate_1": crate_1, "crate_2": crate_2, "crate_3": crate_3, "crate_4": crate_4,
                        "crate_5": crate_5, "switch_1": switch_1, "switch_2": switch_2, "switch_3": switch_3,
                        "muchador_defeated": muchador_defeated, "has_key": has_key,
                        "mini_boss_1_defeated": mini_boss_1_defeated, "mini_boss_2_defeated": mini_boss_2_defeated,
                        "gloves_obtained": gloves_obtained, "korlok_attuned": korlok_attuned,
                        "eldream_attuned": eldream_attuned}
    try:
        # serialize dictionary and save to file ("save game") with python pickle (wb = write binary)
        directory = os.getcwd()
        save_directory = directory + "/saves/save_game"
        assert os.path.isfile(save_directory)
        with open(save_directory, "wb") as ff:
            pickle.dump(player_save_info, ff)

    # create the directory with save data if it doesn't exist
    except FileNotFoundError and AssertionError:
        directory = os.getcwd()
        os.mkdir(directory + "/saves")
        with open(directory + "/saves/save_game", "wb") as ff:
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
def player_info_and_ui_updates(player, hp_bar, en_bar, xp_bar, star_power_meter, graphics):

    # update players status bars
    hp_bar.update(hp_bar.x_coordinate, hp_bar.y_coordinate, health_bar_update(player, graphics))
    en_bar.update(en_bar.x_coordinate, en_bar.y_coordinate, energy_bar_update(player, graphics))
    xp_bar.update(xp_bar.x_coordinate, xp_bar.y_coordinate, xp_bar_update(player, graphics))

    if player.star_power == 0:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, graphics["star_00"])
    if player.star_power == 1:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, graphics["star_01"])
    if player.star_power == 2:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, graphics["star_02"])
    if player.star_power == 3:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, graphics["star_03"])
    if player.star_power == 4:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, graphics["star_04"])

    # update players current equipment
    drawing_functions.equipment_updates(player, graphics)
    # update players current inventory
    drawing_functions.item_updates(player, graphics)


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
        base_damage = base_damage + 2
    if difference >= 2:
        base_damage = base_damage + 4
    if difference >= 3:
        base_damage = base_damage + 6
    if difference >= 4:
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


# function to respawn enemies if they are less than a specified amount active in game. spawns with random coord. and lvl
def enemy_respawn(player, seldon_enemies, korlok_enemies, snakes, ghouls, magmons, bandiles, interactables_seldon,
                  interactables_korlok, interactables_mines, Enemy, Item, graphic_dict, UiElement):

    if player.current_zone == "seldon":
        snake_counter = 0
        ghoul_counter = 0
        # generate random coordinates and level for new enemy to spawn within boundaries and level range
        # if not scaled, coordinates set to default boundaries
        random_snake_x = random.randrange(150, 300)
        random_snake_y = random.randrange(150, 300)
        random_snake_level = random.randrange(1, 4)
        random_ghoul_x = random.randrange(650, 900)
        random_ghoul_y = random.randrange(150, 300)
        random_ghoul_level = random.randrange(4, 7)

        # count current enemies active in game
        for mob in seldon_enemies:
            if mob.name == "snake":
                snake_counter += 1
            if mob.name == "ghoul":
                ghoul_counter += 1

        # if there are less than 3 snakes in game, create another snake with random level and coordinates. add to groups
        if snake_counter < 3:
            new_snake = Enemy("snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y, True,
                              Item("shiny rock", "rock", 200, 200, graphic_dict["shiny_rock_img"]), graphic_dict["snake"],
                              UiElement("snake hp bar", 700, 90, graphic_dict["hp_100"]))
            snakes.add(new_snake)
            seldon_enemies.add(new_snake)
            interactables_seldon.add(new_snake)
        # if there are less than 3 ghouls in game, create another ghoul with random level and coordinates. add to groups
        if ghoul_counter < 3:
            new_ghoul = Enemy("ghoul", "ghoul", 100, 100, random_ghoul_level, random_ghoul_x, random_ghoul_y, True,
                              Item("bone dust", "dust", 200, 200, graphic_dict["bone_dust_img"]), graphic_dict["ghoul"],
                              UiElement("ghoul hp bar", 700, 90, graphic_dict["hp_100"]))
            ghouls.add(new_ghoul)
            seldon_enemies.add(new_ghoul)
            interactables_seldon.add(new_ghoul)

    if player.current_zone == "korlok":
        magmon_counter = 0
        # generate random coordinates and level for new enemy to spawn within boundaries and level range
        # if not scaled, coordinates set to default boundaries
        random_magmon_x = random.randrange(100, 375)
        random_magmon_y = random.randrange(125, 225)
        random_magmon_level = random.randrange(6, 9)

        # count current enemies active in game
        for mob in magmons:
            if mob.name == "magmon":
                magmon_counter += 1

        # if there are less than 3 snakes in game, create another snake with random level and coordinates. add to groups
        if magmon_counter < 3:
            new_magmon = Enemy("magmon", "magmon", 100, 100, random_magmon_level, random_magmon_x, random_magmon_y,
                               True, Item("cracked ember", "ember", 200, 200, graphic_dict["ember"]),
                               graphic_dict["magmon"], UiElement("magmon hp bar", 700, 90, graphic_dict["hp_100"]))
            magmons.add(new_magmon)
            korlok_enemies.add(new_magmon)
            interactables_korlok.add(new_magmon)

    if player.current_zone == "mines":
        bandile_counter = 0
        # generate random coordinates and level for new enemy to spawn within boundaries and level range
        # if not scaled, coordinates set to default boundaries
        random_bandile_x = random.randrange(655, 880)
        random_bandile_y = random.randrange(165, 335)
        random_bandile_level = random.randrange(8, 12)

        # count current enemies active in game
        for mob in bandiles:
            if mob.name == "bandile":
                bandile_counter += 1

        # if there are less than 3 snakes in game, create another snake with random level and coordinates. add to groups
        if bandile_counter < 3:
            new_bandile = Enemy("bandile", "bandile", 100, 100, random_bandile_level, random_bandile_x,
                                random_bandile_y, True, Item("broken band", "band", 200, 200, graphic_dict["band"]),
                                graphic_dict["bandile"], UiElement("bandile hp bar", 700, 90, graphic_dict["hp_100"]))
            bandiles.add(new_bandile)
            interactables_mines.add(new_bandile)

    respawn_dict = {"seldon_enemies": seldon_enemies, "snakes": snakes, "ghouls": ghouls,
                    "interactables_seldon": interactables_seldon, "interactables_korlok": interactables_korlok,
                    "korlok_enemies": korlok_enemies, "magmons": magmons, "bandiles": bandiles}

    return respawn_dict


# player bar update functions. return image representing amount
def health_bar_update(character, graphics):
    if character.health == 100:
        return graphics["hp_100"]
    if character.health == 99:
        return graphics["hp_99"]
    if character.health == 98:
        return graphics["hp_98"]
    if character.health == 97:
        return graphics["hp_97"]
    if character.health == 96:
        return graphics["hp_96"]
    if character.health == 95:
        return graphics["hp_95"]
    if character.health == 94:
        return graphics["hp_94"]
    if character.health == 93:
        return graphics["hp_93"]
    if character.health == 92:
        return graphics["hp_92"]
    if character.health == 91:
        return graphics["hp_91"]
    if character.health == 90:
        return graphics["hp_90"]
    if character.health == 89:
        return graphics["hp_89"]
    if character.health == 88:
        return graphics["hp_88"]
    if character.health == 87:
        return graphics["hp_87"]
    if character.health == 86:
        return graphics["hp_86"]
    if character.health == 85:
        return graphics["hp_85"]
    if character.health == 84:
        return graphics["hp_84"]
    if character.health == 83:
        return graphics["hp_83"]
    if character.health == 82:
        return graphics["hp_82"]
    if character.health == 81:
        return graphics["hp_81"]
    if character.health == 80:
        return graphics["hp_80"]
    if character.health == 79:
        return graphics["hp_79"]
    if character.health == 78:
        return graphics["hp_78"]
    if character.health == 77:
        return graphics["hp_77"]
    if character.health == 76:
        return graphics["hp_76"]
    if character.health == 75:
        return graphics["hp_75"]
    if character.health == 74:
        return graphics["hp_74"]
    if character.health == 73:
        return graphics["hp_73"]
    if character.health == 72:
        return graphics["hp_72"]
    if character.health == 71:
        return graphics["hp_71"]
    if character.health == 70:
        return graphics["hp_70"]
    if character.health == 69:
        return graphics["hp_69"]
    if character.health == 68:
        return graphics["hp_68"]
    if character.health == 67:
        return graphics["hp_67"]
    if character.health == 66:
        return graphics["hp_66"]
    if character.health == 65:
        return graphics["hp_65"]
    if character.health == 64:
        return graphics["hp_64"]
    if character.health == 63:
        return graphics["hp_63"]
    if character.health == 62:
        return graphics["hp_62"]
    if character.health == 61:
        return graphics["hp_61"]
    if character.health == 60:
        return graphics["hp_60"]
    if character.health == 59:
        return graphics["hp_59"]
    if character.health == 58:
        return graphics["hp_58"]
    if character.health == 57:
        return graphics["hp_57"]
    if character.health == 56:
        return graphics["hp_56"]
    if character.health == 55:
        return graphics["hp_55"]
    if character.health == 54:
        return graphics["hp_54"]
    if character.health == 53:
        return graphics["hp_53"]
    if character.health == 52:
        return graphics["hp_52"]
    if character.health == 51:
        return graphics["hp_51"]
    if character.health == 50:
        return graphics["hp_50"]
    if character.health == 49:
        return graphics["hp_49"]
    if character.health == 48:
        return graphics["hp_48"]
    if character.health == 47:
        return graphics["hp_47"]
    if character.health == 46:
        return graphics["hp_46"]
    if character.health == 45:
        return graphics["hp_45"]
    if character.health == 44:
        return graphics["hp_44"]
    if character.health == 43:
        return graphics["hp_43"]
    if character.health == 42:
        return graphics["hp_42"]
    if character.health == 41:
        return graphics["hp_41"]
    if character.health == 40:
        return graphics["hp_40"]
    if character.health == 39:
        return graphics["hp_39"]
    if character.health == 38:
        return graphics["hp_38"]
    if character.health == 37:
        return graphics["hp_37"]
    if character.health == 36:
        return graphics["hp_36"]
    if character.health == 35:
        return graphics["hp_35"]
    if character.health == 34:
        return graphics["hp_34"]
    if character.health == 33:
        return graphics["hp_33"]
    if character.health == 32:
        return graphics["hp_32"]
    if character.health == 31:
        return graphics["hp_31"]
    if character.health == 30:
        return graphics["hp_30"]
    if character.health == 29:
        return graphics["hp_29"]
    if character.health == 28:
        return graphics["hp_28"]
    if character.health == 27:
        return graphics["hp_27"]
    if character.health == 26:
        return graphics["hp_26"]
    if character.health == 25:
        return graphics["hp_25"]
    if character.health == 24:
        return graphics["hp_24"]
    if character.health == 23:
        return graphics["hp_23"]
    if character.health == 22:
        return graphics["hp_22"]
    if character.health == 21:
        return graphics["hp_21"]
    if character.health == 20:
        return graphics["hp_20"]
    if character.health == 19:
        return graphics["hp_19"]
    if character.health == 18:
        return graphics["hp_18"]
    if character.health == 17:
        return graphics["hp_17"]
    if character.health == 16:
        return graphics["hp_16"]
    if character.health == 15:
        return graphics["hp_15"]
    if character.health == 14:
        return graphics["hp_14"]
    if character.health == 13:
        return graphics["hp_13"]
    if character.health == 12:
        return graphics["hp_12"]
    if character.health == 11:
        return graphics["hp_11"]
    if character.health == 10:
        return graphics["hp_10"]
    if character.health == 9:
        return graphics["hp_9"]
    if character.health == 8:
        return graphics["hp_8"]
    if character.health == 7:
        return graphics["hp_7"]
    if character.health == 6:
        return graphics["hp_6"]
    if character.health == 5:
        return graphics["hp_5"]
    if character.health == 4:
        return graphics["hp_4"]
    if character.health == 3:
        return graphics["hp_3"]
    if character.health == 2:
        return graphics["hp_2"]
    if character.health == 1:
        return graphics["hp_1"]
    if character.health == 0:
        return graphics["hp_0"]


def energy_bar_update(character, graphics):
    if character.energy == 100:
        return graphics["en_100"]
    if character.energy == 99:
        return graphics["en_99"]
    if character.energy == 98:
        return graphics["en_98"]
    if character.energy == 97:
        return graphics["en_97"]
    if character.energy == 96:
        return graphics["en_96"]
    if character.energy == 95:
        return graphics["en_95"]
    if character.energy == 94:
        return graphics["en_94"]
    if character.energy == 93:
        return graphics["en_93"]
    if character.energy == 92:
        return graphics["en_92"]
    if character.energy == 91:
        return graphics["en_91"]
    if character.energy == 90:
        return graphics["en_90"]
    if character.energy == 89:
        return graphics["en_89"]
    if character.energy == 88:
        return graphics["en_88"]
    if character.energy == 87:
        return graphics["en_87"]
    if character.energy == 86:
        return graphics["en_86"]
    if character.energy == 85:
        return graphics["en_85"]
    if character.energy == 84:
        return graphics["en_84"]
    if character.energy == 83:
        return graphics["en_83"]
    if character.energy == 82:
        return graphics["en_82"]
    if character.energy == 81:
        return graphics["en_81"]
    if character.energy == 80:
        return graphics["en_80"]
    if character.energy == 79:
        return graphics["en_79"]
    if character.energy == 78:
        return graphics["en_78"]
    if character.energy == 77:
        return graphics["en_77"]
    if character.energy == 76:
        return graphics["en_76"]
    if character.energy == 75:
        return graphics["en_75"]
    if character.energy == 74:
        return graphics["en_74"]
    if character.energy == 73:
        return graphics["en_73"]
    if character.energy == 72:
        return graphics["en_72"]
    if character.energy == 71:
        return graphics["en_71"]
    if character.energy == 70:
        return graphics["en_70"]
    if character.energy == 69:
        return graphics["en_69"]
    if character.energy == 68:
        return graphics["en_68"]
    if character.energy == 67:
        return graphics["en_67"]
    if character.energy == 66:
        return graphics["en_66"]
    if character.energy == 65:
        return graphics["en_65"]
    if character.energy == 64:
        return graphics["en_64"]
    if character.energy == 63:
        return graphics["en_63"]
    if character.energy == 62:
        return graphics["en_62"]
    if character.energy == 61:
        return graphics["en_61"]
    if character.energy == 60:
        return graphics["en_60"]
    if character.energy == 59:
        return graphics["en_59"]
    if character.energy == 58:
        return graphics["en_58"]
    if character.energy == 57:
        return graphics["en_57"]
    if character.energy == 56:
        return graphics["en_56"]
    if character.energy == 55:
        return graphics["en_55"]
    if character.energy == 54:
        return graphics["en_54"]
    if character.energy == 53:
        return graphics["en_53"]
    if character.energy == 52:
        return graphics["en_52"]
    if character.energy == 51:
        return graphics["en_51"]
    if character.energy == 50:
        return graphics["en_50"]
    if character.energy == 49:
        return graphics["en_49"]
    if character.energy == 48:
        return graphics["en_48"]
    if character.energy == 47:
        return graphics["en_47"]
    if character.energy == 46:
        return graphics["en_46"]
    if character.energy == 45:
        return graphics["en_45"]
    if character.energy == 44:
        return graphics["en_44"]
    if character.energy == 43:
        return graphics["en_43"]
    if character.energy == 42:
        return graphics["en_42"]
    if character.energy == 41:
        return graphics["en_41"]
    if character.energy == 40:
        return graphics["en_40"]
    if character.energy == 39:
        return graphics["en_39"]
    if character.energy == 38:
        return graphics["en_38"]
    if character.energy == 37:
        return graphics["en_37"]
    if character.energy == 36:
        return graphics["en_36"]
    if character.energy == 35:
        return graphics["en_35"]
    if character.energy == 34:
        return graphics["en_34"]
    if character.energy == 33:
        return graphics["en_33"]
    if character.energy == 32:
        return graphics["en_32"]
    if character.energy == 31:
        return graphics["en_31"]
    if character.energy == 30:
        return graphics["en_30"]
    if character.energy == 29:
        return graphics["en_29"]
    if character.energy == 28:
        return graphics["en_28"]
    if character.energy == 27:
        return graphics["en_27"]
    if character.energy == 26:
        return graphics["en_26"]
    if character.energy == 25:
        return graphics["en_25"]
    if character.energy == 24:
        return graphics["en_24"]
    if character.energy == 23:
        return graphics["en_23"]
    if character.energy == 22:
        return graphics["en_22"]
    if character.energy == 21:
        return graphics["en_21"]
    if character.energy == 20:
        return graphics["en_20"]
    if character.energy == 19:
        return graphics["en_19"]
    if character.energy == 18:
        return graphics["en_18"]
    if character.energy == 17:
        return graphics["en_17"]
    if character.energy == 16:
        return graphics["en_16"]
    if character.energy == 15:
        return graphics["en_15"]
    if character.energy == 14:
        return graphics["en_14"]
    if character.energy == 13:
        return graphics["en_13"]
    if character.energy == 12:
        return graphics["en_12"]
    if character.energy == 11:
        return graphics["en_11"]
    if character.energy == 10:
        return graphics["en_10"]
    if character.energy == 9:
        return graphics["en_9"]
    if character.energy == 8:
        return graphics["en_8"]
    if character.energy == 7:
        return graphics["en_7"]
    if character.energy == 6:
        return graphics["en_6"]
    if character.energy == 5:
        return graphics["en_5"]
    if character.energy == 4:
        return graphics["en_4"]
    if character.energy == 3:
        return graphics["en_3"]
    if character.energy == 2:
        return graphics["en_2"]
    if character.energy == 1:
        return graphics["en_1"]
    if character.energy == 0:
        return graphics["en_0"]


def xp_bar_update(character, graphics):
    if character.experience >= 100:
        return graphics["xp_100"]
    if character.experience == 99:
        return graphics["xp_99"]
    if character.experience == 98:
        return graphics["xp_98"]
    if character.experience == 97:
        return graphics["xp_97"]
    if character.experience == 96:
        return graphics["xp_96"]
    if character.experience == 95:
        return graphics["xp_95"]
    if character.experience == 94:
        return graphics["xp_94"]
    if character.experience == 93:
        return graphics["xp_93"]
    if character.experience == 92:
        return graphics["xp_92"]
    if character.experience == 91:
        return graphics["xp_91"]
    if character.experience == 90:
        return graphics["xp_90"]
    if character.experience == 89:
        return graphics["xp_89"]
    if character.experience == 88:
        return graphics["xp_88"]
    if character.experience == 87:
        return graphics["xp_87"]
    if character.experience == 86:
        return graphics["xp_86"]
    if character.experience == 85:
        return graphics["xp_85"]
    if character.experience == 84:
        return graphics["xp_84"]
    if character.experience == 83:
        return graphics["xp_83"]
    if character.experience == 82:
        return graphics["xp_82"]
    if character.experience == 81:
        return graphics["xp_81"]
    if character.experience == 80:
        return graphics["xp_80"]
    if character.experience == 79:
        return graphics["xp_79"]
    if character.experience == 78:
        return graphics["xp_78"]
    if character.experience == 77:
        return graphics["xp_77"]
    if character.experience == 76:
        return graphics["xp_76"]
    if character.experience == 75:
        return graphics["xp_75"]
    if character.experience == 74:
        return graphics["xp_74"]
    if character.experience == 73:
        return graphics["xp_73"]
    if character.experience == 72:
        return graphics["xp_72"]
    if character.experience == 71:
        return graphics["xp_71"]
    if character.experience == 70:
        return graphics["xp_70"]
    if character.experience == 69:
        return graphics["xp_69"]
    if character.experience == 68:
        return graphics["xp_68"]
    if character.experience == 67:
        return graphics["xp_67"]
    if character.experience == 66:
        return graphics["xp_66"]
    if character.experience == 65:
        return graphics["xp_65"]
    if character.experience == 64:
        return graphics["xp_64"]
    if character.experience == 63:
        return graphics["xp_63"]
    if character.experience == 62:
        return graphics["xp_62"]
    if character.experience == 61:
        return graphics["xp_61"]
    if character.experience == 60:
        return graphics["xp_60"]
    if character.experience == 59:
        return graphics["xp_59"]
    if character.experience == 58:
        return graphics["xp_58"]
    if character.experience == 57:
        return graphics["xp_57"]
    if character.experience == 56:
        return graphics["xp_56"]
    if character.experience == 55:
        return graphics["xp_55"]
    if character.experience == 54:
        return graphics["xp_54"]
    if character.experience == 53:
        return graphics["xp_53"]
    if character.experience == 52:
        return graphics["xp_52"]
    if character.experience == 51:
        return graphics["xp_51"]
    if character.experience == 50:
        return graphics["xp_50"]
    if character.experience == 49:
        return graphics["xp_49"]
    if character.experience == 48:
        return graphics["xp_48"]
    if character.experience == 47:
        return graphics["xp_47"]
    if character.experience == 46:
        return graphics["xp_46"]
    if character.experience == 45:
        return graphics["xp_45"]
    if character.experience == 44:
        return graphics["xp_44"]
    if character.experience == 43:
        return graphics["xp_43"]
    if character.experience == 42:
        return graphics["xp_42"]
    if character.experience == 41:
        return graphics["xp_41"]
    if character.experience == 40:
        return graphics["xp_40"]
    if character.experience == 39:
        return graphics["xp_39"]
    if character.experience == 38:
        return graphics["xp_38"]
    if character.experience == 37:
        return graphics["xp_37"]
    if character.experience == 36:
        return graphics["xp_36"]
    if character.experience == 35:
        return graphics["xp_35"]
    if character.experience == 34:
        return graphics["xp_34"]
    if character.experience == 33:
        return graphics["xp_33"]
    if character.experience == 32:
        return graphics["xp_32"]
    if character.experience == 31:
        return graphics["xp_31"]
    if character.experience == 30:
        return graphics["xp_30"]
    if character.experience == 29:
        return graphics["xp_29"]
    if character.experience == 28:
        return graphics["xp_28"]
    if character.experience == 27:
        return graphics["xp_27"]
    if character.experience == 26:
        return graphics["xp_26"]
    if character.experience == 25:
        return graphics["xp_25"]
    if character.experience == 24:
        return graphics["xp_24"]
    if character.experience == 23:
        return graphics["xp_23"]
    if character.experience == 22:
        return graphics["xp_22"]
    if character.experience == 21:
        return graphics["xp_21"]
    if character.experience == 20:
        return graphics["xp_20"]
    if character.experience == 19:
        return graphics["xp_19"]
    if character.experience == 18:
        return graphics["xp_18"]
    if character.experience == 17:
        return graphics["xp_17"]
    if character.experience == 16:
        return graphics["xp_16"]
    if character.experience == 15:
        return graphics["xp_15"]
    if character.experience == 14:
        return graphics["xp_14"]
    if character.experience == 13:
        return graphics["xp_13"]
    if character.experience == 12:
        return graphics["xp_12"]
    if character.experience == 11:
        return graphics["xp_11"]
    if character.experience == 10:
        return graphics["xp_10"]
    if character.experience == 9:
        return graphics["xp_9"]
    if character.experience == 8:
        return graphics["xp_8"]
    if character.experience == 7:
        return graphics["xp_7"]
    if character.experience == 6:
        return graphics["xp_6"]
    if character.experience == 5:
        return graphics["xp_5"]
    if character.experience == 4:
        return graphics["xp_4"]
    if character.experience == 3:
        return graphics["xp_3"]
    if character.experience == 2:
        return graphics["xp_2"]
    if character.experience == 1:
        return graphics["xp_1"]
    if character.experience <= 0:
        return graphics["xp_0"]

    else:
        return graphics["xp_0"]
