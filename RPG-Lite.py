# RPG-Lite Code
# Intrinsic Q


# npc classes ----------------------------------------------------------------------------------------------------------
import random
import time


class Player:

    def __init__(self, name, gender, race, role, inventory, equipment, quest, quest_status, statistics, skills, level,
                 experience, health, energy, x_coordinate, y_coordinate, alive_status, rupees, reputation, mount):
        self.name = name
        self.gender = gender
        self.race = race
        self.role = role
        self.inventory = inventory
        self.equipment = equipment
        self.quest = quest
        self.quest_status = quest_status
        self.statistics = statistics
        self.skills = skills
        self.level = level
        self.experience = experience
        self.health = health
        self.energy = energy

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self.alive_status = alive_status

        self.rupees = rupees
        self.reputation = reputation

        self.mount = mount


class Enemy:

    def __init__(self, kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items):
        self.kind = kind
        self.health = health
        self.energy = energy
        self.level = level

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self.alive_status = alive_status

        self.items = items


class NPC:

    def __init__(self, name, gender, race, role, dialog, quest, quest_description, x_coordinate, y_coordinate,
                 alive_status, quest_complete, items, gift):
        self.name = name
        self.gender = gender
        self.race = race
        self.role = role
        self.dialog = dialog
        self.quest = quest
        self.quest_description = quest_description

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self.alive_status = alive_status
        self.quest_complete = quest_complete

        self.items = items
        self.gift = gift


class Welcome:

    def __init__(self, message, shown):
        self.message = message
        self.shown = shown


class Tree:

    def __init__(self, name, model, x_coordinate, y_coordinate, gathered):
        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.gathered = gathered


class Building:

    def __init__(self, name, model, x_coordinate, y_coordinate):
        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


class Water:

    def __init__(self, name, model, x_coordinate, y_coordinate):
        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


class Path:

    def __init__(self, name, model, x_coordinate, y_coordinate):
        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


class Shopkeeper:

    def __init__(self, name, location, inventory, dialog):
        self.name = name
        self.location = location
        self.inventory = inventory
        self.dialog = dialog


class Trainer:

    def __init__(self, name, location, skills, dialog):
        self.name = name
        self.location = location
        self.skills = skills
        self.dialog = dialog


# ----------------------------------------------------------------------------------------------------------------------
# character creator ----------------------------------------------------------------------------------------------------
# default character
default_character = Player("Player", "female", "amuna", "fighter",  # name, gender, race, role
                           ["health potion", "energy potion"],  # inventory
                           ["", "", "", ""],  # equipment ('type', 'name')
                           [""], 0,  # quest, # quest status
                           ["vitality", 3, "intellect", 1, "strength", 2, "wisdom", 1],  # stats ('stat', 'amount')
                           ["heavy swing"], 1, 0, 100, 100,  # skills, lvl, exp, health, energy
                           1, 1, True, 0, ["amuna", 10, "nuldar", 0, "sorae", 0], "none")
# x-coordinate, y-coordinate, alive status, rupees, reputation, mount

character_list = [default_character]

# enemies --------------------------------------------------------------------------------------------------------------
# basic enemy (kind, health, energy, level, x-coordinate, y-coordinate, alive status, inventory)
snake_1 = Enemy("snake", 100, 100, 1, 3, 13, True, "shiny rock")
snake_2 = Enemy("snake", 100, 100, 2, 4, 12, True, "shiny rock")
snake_3 = Enemy("snake", 100, 100, 3, 2, 11, True, "shiny rock")
snake_4 = Enemy("snake", 100, 100, 2, 3, 10, True, "shiny rock")
snake_5 = Enemy("snake", 100, 100, 3, 2, 14, True, "shiny rock")
snake_6 = Enemy("snake", 100, 100, 1, 4, 15, True, "shiny rock")

ghoul_low_1 = Enemy("ghoul", 100, 100, 4, 16, 13, True, "bone dust")
ghoul_low_2 = Enemy("ghoul", 100, 100, 5, 17, 11, True, "bone dust")
ghoul_low_3 = Enemy("ghoul", 100, 100, 3, 17, 14, True, "bone dust")
ghoul_low_4 = Enemy("ghoul", 100, 100, 4, 15, 12, True, "bone dust")

all_enemies = [snake_1, snake_2, snake_3, snake_4, snake_5, snake_6, ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4]

# npcs -----------------------------------------------------------------------------------------------------------------
# basic npc (name, gender, race, role, dialog, quest, quest description x-coordinate, y-coordinate, alive status,
# quest complete, items, gift status)
npc_garan = NPC("Garan", "male", "amuna", "rogue", "It's dangerous to go alone.", "Stupid Snakes",
                "Greetings! I don't believe I've seen you around here before. You must be a traveler, \nright? "
                "Or maybe the request for reinforcements has finally been answered! Well, either way, we're\n"
                "thankful for all the help we can get. \n\nLook, you seem pretty strong, but you're going to need "
                "a weapon to survive out here. \n\nI've got something you can have for now, but you'll need to find "
                "something better if you plan on \njourneying further into the Region. Here's a basic weapon and "
                "some gear. \n\nWhy don't you go and test it out? There's some snakes nearby that have been coming up "
                "from the \nriver. They've shown an unusual aggressiveness with larger numbers than I've seen "
                "before. \n\nMaybe you could take care of them for me? I'll be sure to give you something worth the "
                "trouble. ", 4, 4, True, False, ["Items to be added for thief steal"], False)

npc_celeste = NPC("Celeste", "female", "sorae", "mage", "Please help Nede... ", "My Companion",
                  "quest description placeholder", 32, 34, True, False,
                  ["Items to be added for thief steal"], False)

npc_artherian = NPC("Artherian", "male", "amuna", "fighter", "We must hold!", "Draconian Dreads",
                    "quest description placeholder", 28, 18, True, False,
                    ["Items to be added for thief steal"], False)

guard = NPC("Guard", "male", "amuna", "fighter", "Another day.", "Ghoulish Glee",
            "You need to cross the bridge to get to the Korlok District, you say? \n\nOrdinarily"
            " I would have no issue granting you passage, however the gates are barred tight \n"
            "due to the recent wave of Ghoul Minions from across the wall. \n\nI cannot leave my post and"
            " leave the bridge unguarded, but if you could \ntake care of the remaining ghouls I"
            " will signal to unbar the gates and allow you passage \nto the other side. \n\nThe"
            " ghouls were last spotted just east of here, nearby the northern Castle wall ramparts! ", 11, 15, True,
            False, ["Items to be added for thief steal"], False)

village_matron = NPC("Village Matron Maurelle", "female", "amuna", "mage", "We need help!", "Village Repairs",
                     "You there! I don't know who you are, or why you're here, but we could \nreally use your help!"
                     "\n\nThe beast Dreth has occupied our former capital Castle, on the other side of the walls "
                     "\nto the east, and our numbers have been spread thin trying to repel its minions and contain "
                     "the \ndamage they've inflicted. \n\nOur best fighters have been sent in a combined Vanguard with "
                     "the other districts to try and \nattack the beast directly, but its left us vulnerable here. "
                     "The most recent wave of attacks from\nthe castle has left several damages to our village, "
                     "and if you are able, please gather\nresources and bring them to me to distribute to the "
                     "villagers conducting the repairs and \nfortifications. \n\nYou can gather some lumber from the "
                     "trees just west of here. Nera bless you. ", 13, 6, True, False,
                     ["Items to be added for thief steal"], False)

vanguard_captain_adria = NPC("Vanguard Captain Adria", "female", "amuna", "fighter", "We will prevail.",
                             "Quacking Questions", "Placeholder quest text", 32, 32, True, False,
                             ["Items to be added for thief steal"], False)

all_npcs = [npc_garan, npc_celeste, npc_artherian, guard, village_matron]

# shop keepers ---------------------------------------------------------------------------------------------------------
# (name, location, inventory, dialog)

amuna_shop_keeper = Shopkeeper("Amuna Shopkeeper Beetle", "Seldon District", ["health potion", "energy potion",
                                                                              "bronze sword", "bronze armor",
                                                                              "oaken staff", "woven robes",
                                                                              "sharpened dirks", "padded jerkin",
                                                                              "chestnut horse"],
                               "These Ghoul Minion attacks are bad for business!")

nuldar_shop_keeper = Shopkeeper("Nuldar Shopkeeper Darunia", "Korlok District", ["hearty health potion",
                                                                                 "extra energy potion",
                                                                                 "iron forged sword",
                                                                                 "iron forged armor",
                                                                                 "smooth metal staff", "fire robes",
                                                                                 "dark iron daggers",
                                                                                 "resistant jerkin",
                                                                                 "aren's mighty gloves"],
                                "Welcome, Onurok.")

# skill trainers -------------------------------------------------------------------------------------------------------
# (name, location, skills, dialog)

amuna_fighter_trainer = Trainer("Amuna Fighter Trainer Raron", "Seldon District", ["Protection"],
                                "Hail, fellow fighter. What can I teach you today?")
amuna_mage_trainer = Trainer("Amuna Mage Trainer Kepora", "Seldon District", ["Chillshot"],
                             "Hail, fellow mage. What can I teach you today?")
amuna_rogue_trainer = Trainer("Amuna Rogue Trainer Drago", "Seldon District", ["Evasion Tactics"],
                              "Hail, fellow rogue. What can I teach you today?")

nuldar_fighter_trainer = Trainer("Nuldar Fighter Trainer Dongo", "Korlok District", ["Aren's Flame"],
                                 "Kunkoro, big-sword. What may I teach?")
nuldar_mage_trainer = Trainer("Nuldar Mage Trainer Kepora", "Korlok District", ["Thermal Manipulation"],
                              "Kunkoro, bright-mind. What may I teach?")
nuldar_rogue_trainer = Trainer("Nuldar Rogue Trainer Drago", "Korlok District", ["Molten Blades"],
                               "Kunkoro, silence-seeker. What may I teach?")

# trees ----------------------------------------------------------------------------------------------------------------
# any tree (name, model, x-coordinate, y-coordinate)
tree_1 = Tree("Pine tree", "tree", 7, 5, False)
tree_2 = Tree("Pine tree", "tree", 6, 2, False)
tree_3 = Tree("Pine tree", "tree", 2, 4, False)
tree_4 = Tree("Pine tree", "tree", 3, 6, False)
tree_5 = Tree("Pine tree", "tree", 8, 3, False)
tree_6 = Tree("Pine tree", "tree", 5, 7, False)

all_trees = [tree_1, tree_2, tree_3, tree_4, tree_5, tree_6]

# water ----------------------------------------------------------------------------------------------------------------
# water filler (name, model, x-coordinate, y-coordinate)
water_1 = Water("Rohir River", "water", 1, 18)
water_2 = Water("Rohir River", "water", 2, 18)
water_3 = Water("Rohir River", "water", 3, 18)
water_4 = Water("Rohir River", "water", 4, 18)
water_5 = Water("Rohir River", "water", 5, 18)
water_6 = Water("Rohir River", "water", 6, 18)
water_7 = Water("Rohir River", "water", 7, 18)
water_8 = Water("Rohir River", "water", 8, 18)
water_9 = Water("Rohir River", "water", 9, 18)
water_10 = Water("Rohir River", "water", 10, 18)
water_11 = Water("Rohir River", "water", 11, 18)
water_12 = Water("Rohir River", "water", 14, 18)
water_13 = Water("Rohir River", "water", 15, 18)
water_14 = Water("Rohir River", "water", 16, 18)
water_15 = Water("Rohir River", "water", 17, 18)
water_16 = Water("Rohir River", "water", 18, 18)
water_17 = Water("Rohir River", "water", 19, 18)
water_18 = Water("Rohir River", "water", 20, 18)
water_19 = Water("Rohir River", "water", 1, 17)
water_20 = Water("Rohir River", "water", 2, 17)
water_21 = Water("Rohir River", "water", 3, 17)
water_22 = Water("Rohir River", "water", 4, 17)
water_23 = Water("Rohir River", "water", 5, 17)
water_24 = Water("Rohir River", "water", 6, 17)
water_25 = Water("Rohir River", "water", 7, 17)
water_26 = Water("Rohir River", "water", 8, 17)
water_27 = Water("Rohir River", "water", 9, 17)
water_28 = Water("Rohir River", "water", 10, 17)
water_29 = Water("Rohir River", "water", 11, 17)
water_30 = Water("Rohir River", "water", 14, 17)
water_31 = Water("Rohir River", "water", 15, 17)
water_32 = Water("Rohir River", "water", 16, 17)
water_33 = Water("Rohir River", "water", 17, 17)
water_34 = Water("Rohir River", "water", 18, 17)

all_water = [water_1, water_2, water_3, water_4, water_5, water_6, water_7, water_8, water_9, water_10, water_11,
             water_12, water_13, water_14, water_15, water_16, water_17, water_18, water_19, water_20, water_21,
             water_22, water_23, water_24, water_25, water_26, water_27, water_28, water_29, water_30,
             water_31, water_32, water_33, water_34]

# buildings ------------------------------------------------------------------------------------------------------------
# any tree (name, model, x-coordinate, y-coordinate)
building_1 = Building("Amuna Shop", "shop", 17, 4)
building_2 = Building("Amuna Academia", "academia", 14, 3)
building_3 = Building("Amuna Inn", "inn", 15, 7)

farm_1 = Building("Amuna Farm", "farm", 6, 15)
farm_2 = Building("Amuna Farm", "farm", 9, 14)

wall_1 = Building("Castle Wall", "wall", 19, 1)
wall_2 = Building("Castle Wall", "wall", 19, 2)
wall_3 = Building("Castle Wall", "wall", 19, 3)
wall_4 = Building("Castle Wall", "wall", 19, 4)
wall_5 = Building("Castle Wall", "wall", 19, 5)
wall_6 = Building("Castle Wall", "wall", 19, 6)
wall_7 = Building("Castle Wall", "wall", 19, 7)
wall_8 = Building("Castle Wall", "wall", 19, 8)
wall_9 = Building("Castle Wall", "wall", 19, 9)
wall_10 = Building("Castle Wall", "wall", 19, 10)
wall_11 = Building("Castle Wall", "wall", 19, 11)
wall_12 = Building("Castle Wall", "wall", 19, 12)
wall_13 = Building("Castle Wall", "wall", 19, 13)
wall_14 = Building("Castle Wall", "wall", 19, 14)
wall_15 = Building("Castle Wall", "wall", 19, 15)
wall_16 = Building("Castle Wall", "wall", 19, 16)
wall_17 = Building("Castle Wall", "wall", 19, 17)
wall_18 = Building("Castle Wall", "wall", 19, 18)

bridge_1 = Building("Rohir River Bridge", "bridge", 12, 18)
bridge_2 = Building("Rohir River Bridge", "bridge", 13, 18)
bridge_gate_1 = Building("Rohir River Bridge Gate", "bridge", 12, 17)
bridge_gate_2 = Building("Rohir River Bridge Gate", "bridge", 13, 17)

all_buildings = [building_1, building_2, building_3, farm_1, farm_2, wall_1, wall_2, wall_3, wall_4, wall_5,
                 wall_6, wall_7, wall_8, wall_9, wall_10, wall_11, wall_12, wall_13, wall_14, wall_15, wall_16,
                 wall_17, wall_18, bridge_1, bridge_2, bridge_gate_1, bridge_gate_2]

# path ways ------------------------------------------------------------------------------------------------------------
# any path (name, model, x-coordinate, y-coordinate)

dirt_path_1 = Path("Dirt Path", "dirt", 10, 1)
dirt_path_3 = Path("Dirt Path", "dirt", 10, 2)
dirt_path_5 = Path("Dirt Path", "dirt", 10, 3)
dirt_path_7 = Path("Dirt Path", "dirt", 10, 4)
dirt_path_9 = Path("Dirt Path", "dirt", 10, 5)
dirt_path_11 = Path("Dirt Path", "dirt", 10, 6)
dirt_path_13 = Path("Dirt Path", "dirt", 10, 7)
dirt_path_15 = Path("Dirt Path", "dirt", 10, 8)
dirt_path_17 = Path("Dirt Path", "dirt", 10, 9)
dirt_path_19 = Path("Dirt Path", "dirt", 11, 10)
dirt_path_21 = Path("Dirt Path", "dirt", 12, 11)
dirt_path_23 = Path("Dirt Path", "dirt", 12, 12)
dirt_path_25 = Path("Dirt Path", "dirt", 12, 13)
dirt_path_27 = Path("Dirt Path", "dirt", 12, 14)
dirt_path_29 = Path("Dirt Path", "dirt", 12, 15)
dirt_path_31 = Path("Dirt Path", "dirt", 12, 16)
dirt_path_33 = Path("Dirt Path", "dirt", 12, 17)

all_paths = [dirt_path_1, dirt_path_3, dirt_path_5, dirt_path_7, dirt_path_9, dirt_path_11, dirt_path_13, dirt_path_15,
             dirt_path_17, dirt_path_19, dirt_path_21, dirt_path_23, dirt_path_25, dirt_path_27, dirt_path_29,
             dirt_path_31, dirt_path_33]

# system messages ------------------------------------------------------------------------------------------------------
# False = hasn't been shown to the player yet. Once true it will not continue to show
greeting = Welcome("\n\n-----------------------------------------------------------------------------------------------"
                   "-------"
                   "  \n| * Welcome to RPG-Lite! [Version 0.1A]                                                        "
                   "      |"
                   "  \n-----------------------------------------------------------------------------------------------"
                   "-------", False)

game_start = Welcome("\n-----------------------------------------------------------------------------------------------"
                     "-------"
                     "\n| * Your character has entered into the Seldon District within the Consona World Region.       "
                     "      |"
                     "\n| * Try drawing your map (by typing 'draw' or 'd' at the action screen)                        "
                     "      |"
                     "\n| * And look for nearby NPCs. They may have important information or items for you!            "
                     "      |"
                     "\n-----------------------------------------------------------------------------------------------"
                     "-------", False)

game_hint = Welcome("\n### Hint: Most actions can be utilized with the first letter of the action name. "
                    "\n### To see a complete list of hotkeys, type 'hotkeys' or 'h' at the action prompt. ",
                    False)


# ----------------------------------------------------------------------------------------------------------------------
# gameplay functions ---------------------------------------------------------------------------------------------------

def shop_instance(player, shop, district):
    if district == "seldon district":
        if player.x_coordinate == shop.x_coordinate:
            print(f"\n{amuna_shop_keeper.name} says: {amuna_shop_keeper.dialog}")
            time.sleep(1)

            print("\n-------------------------------------------------------------------------------------------------"
                  "-----")
            trade_choice = input(f"What would you like to do? (Type Buy, Sell, Check Prices or Leave): ")
            if trade_choice.strip().lower() == "buy" or trade_choice.strip().lower() == "b":
                print(f"\n{amuna_shop_keeper.inventory}")
                buy_choice = input("\nWhat would you like to buy? (type an item): ")

                if buy_choice.strip().lower() == "health potion" or buy_choice.strip().lower() == "health":
                    if player.rupees > 9:
                        print("\n*** You have chosen to buy the health potion ***")
                        player.inventory.append("health potion")
                        print("\n*** This item has been added to your inventory ***")
                        time.sleep(1)
                        print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                    else:
                        print("\n*** You do not have enough Rupees to buy this item! ***")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                if buy_choice.strip().lower() == "energy potion" or buy_choice.strip().lower() == "energy":
                    if player.rupees > 9:
                        print("\n*** You have chosen to buy the energy potion ***")
                        player.inventory.append("energy potion")
                        print("\n*** This item has been added to your inventory ***")
                        time.sleep(1)
                        print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                    else:
                        print("\n*** You do not have enough Rupees to buy this item! ***")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                if buy_choice.strip().lower() == "bronze sword" or buy_choice.strip().lower() == "sword":
                    if player.rupees > 49:
                        print("\n*** You have chosen to buy the bronze sword ***")
                        player.equipment[0] = "2H"
                        player.equipment[1] = "bronze sword"
                        print("\n*** This item has been added to your equipment ***")
                        time.sleep(1)
                        print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                    else:
                        print("\n*** You do not have enough Rupees to buy this item! ***")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                if buy_choice.strip().lower() == "bronze armor" or buy_choice.strip().lower() == "armor":
                    if player.rupees > 49:
                        print("\n*** You have chosen to buy the bronze armor ***")
                        player.equipment[2] = "heavy"
                        player.equipment[3] = "bronze armor"
                        print("\n*** This item has been added to your equipment ***")
                        time.sleep(1)
                        print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                    else:
                        print("\n*** You do not have enough Rupees to buy this item! ***")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                if buy_choice.strip().lower() == "oaken staff" or buy_choice.strip().lower() == "staff":
                    if player.rupees > 49:
                        print("\n*** You have chosen to buy the oaken staff ***")
                        player.equipment[0] = "magic"
                        player.equipment[1] = "oaken staff"
                        print("\n*** This item has been added to your equipment ***")
                        time.sleep(1)
                        print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                    else:
                        print("\n*** You do not have enough Rupees to buy this item! ***")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                if buy_choice.strip().lower() == "woven robes" or buy_choice.strip().lower() == "robes" \
                        or buy_choice.strip().lower() == "robe":
                    if player.rupees > 49:
                        print("\n*** You have chosen to buy the woven robes ***")
                        player.equipment[2] = "light"
                        player.equipment[3] = "woven robes"
                        print("\n*** This item has been added to your equipment ***")
                        time.sleep(1)
                        print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                        time.sleep(1)
                        shop_instance(player, shop, district)
                    else:
                        print("\n*** You do not have enough Rupees to buy this item! ***")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                if buy_choice.strip().lower() == "sharpened dirks" or buy_choice.strip().lower() == "dirks":
                    if player.rupees > 49:
                        print("\n*** You have chosen to buy the sharpened dirks ***")
                        player.equipment[0] = "1H"
                        player.equipment[1] = "sharpened dirks"
                        print("\n*** This item has been added to your equipment ***")
                        time.sleep(1)
                        print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                        time.sleep(1)
                        shop_instance(player, shop, district)
                    else:
                        print("\n*** You do not have enough Rupees to buy this item! ***")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                if buy_choice.strip().lower() == "padded jerkin" or buy_choice.strip().lower() == "jerkin":
                    if player.rupees > 49:
                        print("\n*** You have chosen to buy the padded jerkin ***")
                        player.equipment[2] = "medium"
                        player.equipment[3] = "padded jerkin"
                        print("\n*** This item has been added to your equipment ***")
                        time.sleep(1)
                        print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                    else:
                        print("\n*** You do not have enough Rupees to buy this item! ***")
                        time.sleep(1)
                        shop_instance(player, shop, district)

                if buy_choice.strip().lower() == "chestnut horse" or buy_choice == "horse" or \
                        buy_choice.strip().lower() == "chestnut":

                    if player.rupees > 500:
                        if player.reputation[1] > 100:
                            print("\n*** You have chosen to buy the chestnut horse ***")
                            player.mount = "chestnut horse"
                            print("\n*** This item has been added to your mount slot ***")
                            time.sleep(1)
                            print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                            time.sleep(1)
                            shop_instance(player, shop, district)

                        else:
                            print(f"\n*** Your current reputation with the Amuna is not high enough to buy this. "
                                  f"***")
                            time.sleep(1)
                            print(f"\n*** Your reputation: {player.reputation} ***")
                            time.sleep(1)
                    else:
                        print("\n*** You do not have enough Rupees to buy this item! ***")
                        time.sleep(1)
                        shop_instance(player, shop, district)

            if trade_choice.strip().lower() == "sell" or trade_choice.strip().lower() == "s":
                print(f"\n{player.inventory}")
                sell_choice = input("\nWhat would you like to sell? (type an item): ")

                if sell_choice.strip().lower() == "health potion" or sell_choice.strip().lower() == "health":
                    print("\n*** You have chosen to sell the health potion ***")
                    player.rupees += 5
                    print("\n*** You have gained 5 Rupees ***")
                    player.inventory.remove("health potion")
                    time.sleep(1)
                    print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                    time.sleep(1)
                    shop_instance(player, shop, district)

                if sell_choice.strip().lower() == "energy potion" or sell_choice.strip().lower() == "energy":
                    print("\n*** You have chosen to sell the energy potion ***")
                    player.rupees += 5
                    print("\n*** You have gained 5 Rupees ***")
                    player.inventory.remove("energy potion")
                    time.sleep(1)
                    print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                    time.sleep(1)
                    shop_instance(player, shop, district)

                if sell_choice.strip().lower() == "shiny rock" or sell_choice.strip().lower() == "shiny" or \
                        sell_choice.strip().lower() == "rock":
                    print("\n*** You have chosen to sell the shiny rock ***")
                    player.rupees += 10
                    print("\n*** You have gained 10 Rupees ***")
                    player.inventory.remove("shiny rock")
                    time.sleep(1)
                    print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                    time.sleep(1)
                    shop_instance(player, shop, district)

                if sell_choice.strip().lower() == "bone dust" or sell_choice.strip().lower() == "bone" or \
                        sell_choice.strip().lower() == "dust":
                    print("\n*** You have chosen to sell the bone dust ***")
                    player.rupees += 10
                    print("\n*** You have gained 10 Rupees ***")
                    player.inventory.remove("bone dust")
                    time.sleep(1)
                    print(f"\nShopkeeper {amuna_shop_keeper.name} says: Thank you!\n")
                    time.sleep(1)
                    shop_instance(player, shop, district)

                shop_instance(player, shop, district)

            if trade_choice.strip().lower() == "leave" or trade_choice.strip().lower() == "l":
                print(f"\n*** You say goodbye to the shop keeper {amuna_shop_keeper.name} and head on your way. ***")
                player.x_coordinate -= 1
                time.sleep(1)

            if trade_choice.strip().lower() == "check prices" or trade_choice.strip().lower() == "check" \
                    or trade_choice.strip().lower() == "c":

                print(f"\n*** Current shop prices: ***")
                for item in amuna_shop_keeper.inventory:
                    if item == "health potion":
                        print("\nHealth potion: 10 Rupees")
                    if item == "energy potion":
                        print("\nEnergy potion: 10 Rupees")
                    if item == "bronze sword":
                        print("\nBronze Sword: 50 Rupees")
                    if item == "bronze armor":
                        print("\nBronze Armor: 50 Rupees")
                    if item == "oaken staff":
                        print("\nOaken Staff: 50 Rupees")
                    if item == "woven robes":
                        print("\nWoven Robes: 50 Rupees")
                    if item == "sharpened dirks":
                        print("\nSharpened Dirks: 50 Rupees")
                    if item == "padded jerkin":
                        print("\nPadded Jerkin: 50 Rupees")
                    if item == "chestnut horse":
                        print("\nChestnut Horse: 500 Rupees and 100+ Amuna Reputation")
                print(f"\n*** Your current Rupees: {player.rupees}\n")
                shop_instance(player, shop, district)

    return


def academia_instance(player, academia, district):
    # to check if player has already learned an ability
    skill_flag = False

    if district == "seldon district":
        if player.x_coordinate == academia.x_coordinate:
            if player.role == "fighter":
                print(f"\n{amuna_fighter_trainer.name} says: {amuna_fighter_trainer.dialog}")
                time.sleep(1)

                print("\n----------------------------------------------------------------------------------------------"
                      "--------")
                train_choice = input(f"What would you like to do? (Type Train, Check Skills or Leave): ")
                if train_choice.strip().lower() == "train" or train_choice.strip().lower() == "t":
                    print(f"\n{amuna_fighter_trainer.skills}")
                    skill_learn_choice = input("\nWhat would you like to train? (Type a Skill): ")

                    if skill_learn_choice.strip().lower() == "protection" or skill_learn_choice.strip().lower() == "p":
                        for x in player.skills:
                            if x == "protection":
                                print("\n*** You have already learned this skill! ***")
                                skill_flag = True

                        # if skill has not already been learned by player character
                        if not skill_flag:
                            if player.level > 3:
                                print("\n*** You have chosen to learn 'Protection' ***")
                                player.skills.append("protection")
                                print("\n*** This ability has been added to your skills ***")
                                time.sleep(1)
                                print(f"\nTrainer {amuna_fighter_trainer.name} says: Use it wisely.\n")
                                time.sleep(1)
                                academia_instance(player, academia, district)

                            else:
                                print("\n*** You need to be a higher level to learn this skill! ***")
                                print("\n*** Required level: 4 ***")
                                print(f"\n*** Current level: {player.level} ***")
                                time.sleep(1)
                                academia_instance(player, academia, district)

                if train_choice.strip().lower() == "check skills" or train_choice.strip().lower() == "check" or \
                        train_choice.strip().lower() == "c":
                    print(f"\nYour skills: {player.skills}")
                    print(f"\nTrainer skills: Protection - Grants additional armor for fight duration.")

                    academia_instance(player, academia, district)

                if train_choice.strip().lower() == "leave" or train_choice.strip().lower() == "l":
                    print(f"\n*** You say goodbye to the trainer {amuna_fighter_trainer.name} "
                          f"and head on your way. ***")
                    player.x_coordinate -= 1
                    time.sleep(1)

                else:
                    time.sleep(1)
                    academia_instance(player, academia, district)

            if player.role == "mage":
                print(f"\n{amuna_mage_trainer.name} says: {amuna_mage_trainer.dialog}")
                time.sleep(1)

                print("\n----------------------------------------------------------------------------------------------"
                      "--------")
                train_choice = input(f"What would you like to do? (Type Train, Check Skills or Leave): ")
                if train_choice.strip().lower() == "train" or train_choice.strip().lower() == "t":
                    print(f"\n{amuna_mage_trainer.skills}")
                    skill_learn_choice = input("\nWhat would you like to train? (Type a Skill): ")

                    if skill_learn_choice.strip().lower() == "chillshot" or skill_learn_choice.strip().lower() == "c":
                        for x in player.skills:
                            if x == "chillshot":
                                print("\n*** You have already learned this skill! ***")
                                skill_flag = True

                        # if skill has not already been learned by player character
                        if not skill_flag:
                            if player.level > 3:
                                print("\n*** You have chosen to learn 'Chillshot' ***")
                                player.skills.append("chillshot")
                                print("\n*** This ability has been added to your skills ***")
                                time.sleep(1)
                                print(f"\nTrainer {amuna_mage_trainer.name} says: Use it wisely.\n")
                                time.sleep(1)
                                academia_instance(player, academia, district)

                            else:
                                print("\n*** You need to be a higher level to learn this skill! ***")
                                print("\n*** Required level: 4 ***")
                                print(f"\n*** Current level: {player.level} ***")
                                time.sleep(1)
                                academia_instance(player, academia, district)

                if train_choice.strip().lower() == "check skills" or train_choice.strip().lower() == "check" or \
                        train_choice.strip().lower() == "c":
                    print(f"\nYour skills: {player.skills}")
                    print(f"\nTrainer skills: Chillshot - Fires a quick shot of ice at target enemy.")

                    academia_instance(player, academia, district)

                if train_choice.strip().lower() == "leave" or train_choice.strip().lower() == "l":
                    print(f"\n*** You say goodbye to the trainer {amuna_mage_trainer.name} "
                          f"and head on your way. ***")
                    player.x_coordinate -= 1
                    time.sleep(1)

                else:
                    time.sleep(1)
                    academia_instance(player, academia, district)

            if player.role == "rogue":
                print(f"\n{amuna_rogue_trainer.name} says: {amuna_rogue_trainer.dialog}")
                time.sleep(1)

                print("\n----------------------------------------------------------------------------------------------"
                      "--------")
                train_choice = input(f"What would you like to do? (Type Train, Check Skills or Leave): ")
                if train_choice.strip().lower() == "train" or train_choice.strip().lower() == "t":
                    print(f"\n{amuna_rogue_trainer.skills}")
                    skill_learn_choice = input("\nWhat would you like to train? (Type a Skill): ")

                    if skill_learn_choice.strip().lower() == "evasion tactics" or \
                            skill_learn_choice.strip().lower() == "evasion" \
                            or skill_learn_choice.strip().lower() == "e":
                        for x in player.skills:
                            if x == "evasion tactics":
                                print("\n*** You have already learned this skill! ***")
                                skill_flag = True

                        # if skill has not already been learned by player character
                        if not skill_flag:
                            if player.level > 3:
                                print("\n*** You have chosen to learn 'Evasion Tactics' ***")
                                player.skills.append("evasion tactics")
                                print("\n*** This ability has been added to your skills ***")
                                time.sleep(1)
                                print(f"\nTrainer {amuna_rogue_trainer.name} says: Use it wisely.\n")
                                time.sleep(1)
                                academia_instance(player, academia, district)

                            else:
                                print("\n*** You need to be a higher level to learn this skill! ***")
                                print("\n*** Required level: 4 ***")
                                print(f"\n*** Current level: {player.level} ***")
                                time.sleep(1)
                                academia_instance(player, academia, district)

                if train_choice.strip().lower() == "check skills" or train_choice.strip().lower() == "check" or \
                        train_choice.strip().lower() == "c":
                    print(f"\nYour skills: {player.skills}")
                    print(f"\nTrainer skills: Evasion Tactics - Allows you to dodge some enemy attacks.")

                    academia_instance(player, academia, district)

                if train_choice.strip().lower() == "leave" or train_choice.strip().lower() == "l":
                    print(f"\n*** You say goodbye to the trainer {amuna_rogue_trainer.name} "
                          f"and head on your way. ***")
                    player.x_coordinate -= 1
                    time.sleep(1)

                else:
                    time.sleep(1)
                    academia_instance(player, academia, district)

    return


def inn_instance(player, inn, district):
    if district == "seldon district":
        if player.x_coordinate == inn.x_coordinate:

            print(f"\nWelcome to the Seldon District Inn, {player.role}")
            print("\n----------------------------------------------------------------------------------------------"
                  "--------")
            train_choice = input(f"What would you like to do? (Type Rest or Leave): ")
            if train_choice.strip().lower() == "rest" or train_choice.strip().lower() == "r":
                print("\nYou have chosen to rest. You head up to the upper floor of the inn and find your room. ")
                time.sleep(2)
                print("\nYou find a bed next to a small table holding a candle. You lie down and close your eyes... ")
                time.sleep(2)
                print("\n...")
                time.sleep(1)
                print("\n...")
                time.sleep(1)
                print("\n...")
                time.sleep(1)
                print("\n*** You have slept through the night. Your stats have been fully recovered! ***")
                player.health = 100
                player.energy = 100
                time.sleep(1)
                inn_instance(player, inn, district)

            if train_choice.strip().lower() == "leave" or train_choice.strip().lower() == "l":
                print(f"\n*** You say leave {inn.name} and head on your way. ***")
                player.x_coordinate -= 1
                time.sleep(1)

            else:
                time.sleep(1)
                inn_instance(player, inn, district)

    return


def enemy_respawn(enemies):
    for enemy_snake in enemies:
        if enemy_snake.kind == "snake":
            enemy_snake.alive_status = True
            enemy_snake.health = 100
            enemy_snake.energy = 100

    for enemy_ghoul in enemies:
        if enemy_ghoul.kind == "ghoul":
            enemy_ghoul.alive_status = True
            enemy_ghoul.health = 100
            enemy_ghoul.energy = 100


def enemy_respawn_counter(enemies):
    snake_respawn_counter = 0
    ghoul_respawn_counter = 0
    snakes = []
    ghouls = []
    # ------------------------------------------------------------------------------------------------------------------
    # creates a counter that checks the status of enemies. Add to counter for each dead
    # if more than 3 are dead, respawn enemies

    for enemy in enemies:

        if enemy.kind == "snake":
            snakes.append(enemy)
            if not enemy.alive_status:
                snake_respawn_counter += 1

        if enemy.kind == "ghoul":
            ghouls.append(enemy)
            if not enemy.alive_status:
                ghoul_respawn_counter += 1

    # ------------------------------------------------------------------------------------------------------------------

    if snake_respawn_counter > 3:
        enemy_respawn(snakes)

    if ghoul_respawn_counter > 2:
        enemy_respawn(ghouls)


def create_a_character():
    print("\n\n------------------------------------------------------------------------------------------------------"
          "\n| * Character Creator                                                                                |"
          "\n------------------------------------------------------------------------------------------------------")

    # allows the player to create their own character. Stats and skills assigned based on chosen role.
    created_character = Player("name", "gender", "race", "role", "inventory", "equipment", "quest", 0, "stats",
                               "skills", "level", "xp", "health", "energy", "x-coordinate", "y-coordinate", True, 0,
                               ["amuna", 0, "nuldar", 0, "sorae", 0], "none")

    my_name = input("\nWhat would you like your character's name to be? (Type a name): ")
    created_character.name = my_name.strip()

    chosen_gender = False
    while not chosen_gender:

        my_gender = input("\nWhat would you like your character's gender to be? (Type a gender): ")
        if my_gender.strip().lower() == "male" or my_gender.strip().lower() == "m":
            created_character.gender = "male"
            chosen_gender = True

        if my_gender.strip().lower() == "female" or my_gender.strip().lower() == "f":
            created_character.gender = "female"
            chosen_gender = True

    # chosen_race = False means player has not chosen race yet and will continue to offer option until
    # race has been chosen, then it will set to true and continue with the creator tool
    chosen_race = False
    while not chosen_race:
        my_race = input(
            "\nWhat would you like your character's race to be? (Type a race, or, type info for race lore): ")
        if my_race.strip().lower() == "information" or my_race.strip().lower() == "info" or my_race.strip().lower() == \
                "lore":

            print(
                "\n------------------------------------------- Race Lore ----------------------------------------------"
                "--")
            print("\nAmuna: A well-rounded people. The Amuna seek knowledge and wish to grow, but most use this to "
                  "\nsatisfy their own needs. A becoming race, proven to be strong and able to adapt well to their "
                  "\nsurroundings. They often bicker amongst themselves, for the years of curiosity and exploring "
                  "\nthe outer reaches of their world have grown them to be large and diverse. It is for this reason \n"
                  "that a new generation has started a trend of bringing their peoples together, so that they may"
                  "\ncontinue to thrive amongst the coming chaos. * Associated with the element of water for their "
                  "\nvast potential as limitless as the oceans surrounding their world. However, the Amuna also \nhave "
                  "the tendency to change much like the shifting of the tides. This can be a boon if the\nsituation "
                  "warrants, but this instability can also put them in harm's way. The Amuna’s\ncohesiveness has "
                  "proven "
                  "to be their greatest strength if they can come together to realize\nand grasp their shared fate. "
                  "\n\nSorae: Mysterious and wise, the Sorae are not well understood by most other races. But this "
                  "is \nfine with them. As an Eldar race, they view themselves as caretakers and shepherds, "
                  "guiding\nthe new races of the realm or any beings they may see as troubled. Although, this "
                  "quality\nwhile inherently good in nature can also lead to a sense of arrogance and "
                  "condescension amongst\nthem. The Sorae must be cautious to not allow this to hinder them, as there "
                  "is much they can\nstill learn from others. * The Sorae are associated with the element of earth "
                  "and all the nature\nof which inhabits it. They can be very self-sufficient, much as the plant "
                  "life surrounding their\nworld can produce its own source of energy. But when "
                  "cooperative with others they can be much \nstronger for it. "
                  "\n\nNuldar: A hearty race, strong and fierce. The Nuldar do not seek to pass time idle thinking "
                  "of \nthings, for they would rather act and make a difference that they can see and feel. They \nare "
                  "well grounded in their beliefs and hold fast to their strong bonds with family and friends. \nThis "
                  "can cause issues to arise, as they are resistant to change even if it could prove beneficial. "
                  "\nThey are quick to judge and slow to trust, a result of the hardships they have endured in the "
                  "\nred world of Rodin. * The Nuldar are associated with the element of fire. They burn bright and"
                  "\nhave forged themselves as diamonds in the flames of their often-difficult lives. "
                  "They must take \ncare not to allow their flames to be extinguished by keeping their hearts close "
                  "and \nwell guarded by their tough spirits. ")
            print(
                "\n----------------------------------------------------------------------------------------------------"
                "--")

        # player did not choose to read race lore or has read it and made a choice. sets chosen_race to true
        else:
            if my_race.strip().lower() == "amuna" or my_race.strip().lower() == "amu":
                created_character.race = "amuna"
                chosen_race = True
                created_character.reputation[1] = 10

            if my_race.strip().lower() == "sorae" or my_race.strip().lower() == "sor":
                created_character.race = "sorae"
                chosen_race = True
                created_character.reputation[5] = 10

            if my_race.strip().lower() == "nuldar" or my_race.strip().lower() == "nul":
                created_character.race = "nuldar"
                chosen_race = True
                created_character.reputation[3] = 10

    # chosen_role = False means player has not chosen role yet and will continue to offer option until
    # role has been chosen, then it will set to true and continue with the creator tool
    chosen_role = False
    while not chosen_role:
        my_role = input(
            "\nWhat would you like your character's role to be? (Type a role, or, type info for role lore): ")
        if my_role.strip().lower() == "information" or my_role.strip().lower() == "info" or my_role.strip().lower() == \
                "lore":

            print(
                "\n------------------------------------------- Role Lore ----------------------------------------------"
                "--")
            print("\nFighter: The warrior type role. Fighters have more vitality than the other roles, making them "
                  "\nsignificantly tankier. However, they have less intelligence than the mage role and less strength\n"
                  "than the rogue role. Fighters work best with a 2-handed weapon equipped. "
                  "\n\nMage: The magic type role. Mages have more intellect and wisdom than other roles, making them"
                  "\nhave higher energy pools. However, they have less vitality than the fighter role and less "
                  "strength "
                  "\nthan the rogue role. Mages work best with a magic type weapon equipped. "
                  "\n\nRogue: The thief type role. Rogues have a high strength stat and will do more damage than other"
                  "\nroles in melee combat. However, they have less vitality than the fighter role and"
                  " less intellect\nthan the mage role. Rogues work best with a 1-handed weapon equipped. ")
            print(
                "\n----------------------------------------------------------------------------------------------------"
                "--")

        # player did not choose to read role lore or has read it and made a choice. sets chosen_role to true
        else:
            if my_role.strip().lower() == "fighter" or my_role.strip().lower() == "fig":
                created_character.role = "fighter"
                chosen_role = True

            if my_role.strip().lower() == "mage" or my_role.strip().lower() == "mag":
                created_character.role = "mage"
                chosen_role = True

            if my_role.strip().lower() == "rogue" or my_role.strip().lower() == "rog":
                created_character.role = "rogue"
                chosen_role = True

    # player has chosen race and role and inventory, equipment, stats and skills will be assigned based on choice
    # returns created character
    if chosen_race is True and chosen_role is True:
        if created_character.role == "fighter":
            created_character.inventory = ["health potion", "energy potion", "character lore sheet"]
            created_character.equipment = ["", "", "", ""]
            created_character.statistics = ["vitality", 3, "intellect", 1, "strength", 2, "wisdom", 1]
            created_character.skills = ["heavy swing", ""]  # defender 2nd
            created_character.level = 1
            created_character.experience = 0
            created_character.health = 100
            created_character.energy = 100
            created_character.x_coordinate = 1
            created_character.y_coordinate = 1

            print(f"\n*** Your created character: name: {created_character.name}, gender: {created_character.gender},"
                  f" race: {created_character.race}, role: {created_character.role} ***")
            time.sleep(1)
            print("\n*** You are entering the world... ***\n")
            time.sleep(1)

            # adds player created character to list, which the game checks at start to see if one has been created
            # or if it's only the default character, in which case game will start with default
            character_list.append(created_character)
            return created_character

        if created_character.role == "mage":
            created_character.inventory = ["health potion", "energy potion", "character lore sheet"]
            created_character.equipment = ["", "", "", ""]
            created_character.statistics = ["vitality", 1, "intellect", 3, "strength", 1, "wisdom", 2]
            created_character.skills = ["barrier", ""]  # fireball 2nd?
            created_character.level = 1
            created_character.experience = 0
            created_character.health = 100
            created_character.energy = 100
            created_character.x_coordinate = 1
            created_character.y_coordinate = 1

            print(f"\n*** Your created character: name: {created_character.name}, gender: {created_character.gender},"
                  f" race: {created_character.race}, role: {created_character.role} ***")
            time.sleep(1)
            print("\n*** You are entering the world... ***\n")
            time.sleep(1)

            # adds player created character to list, which the game checks at start to see if one has been created
            # or if it's only the default character, in which case game will start with default
            character_list.append(created_character)
            return created_character

        if created_character.role == "rogue":
            created_character.inventory = ["health potion", "energy potion", "character lore sheet"]
            created_character.equipment = ["", "", "", ""]
            created_character.statistics = ["vitality", 2, "intellect", 1, "strength", 3, "wisdom", 1]
            created_character.skills = ["swift strike", ""]  # steal 2nd
            created_character.level = 1
            created_character.experience = 0
            created_character.health = 100
            created_character.energy = 100
            created_character.x_coordinate = 1
            created_character.y_coordinate = 1

            print(f"\n*** Your created character: name: {created_character.name}, gender: {created_character.gender},"
                  f" race: {created_character.race}, role: {created_character.role} ***")
            time.sleep(1)
            print("\n*** You are entering the world... ***\n")
            time.sleep(1)

            # adds player created character to list, which the game checks at start to see if one has been created
            # or if it's only the default character, in which case game will start with default
            character_list.append(created_character)
            return created_character


def level_up(player):
    if player.level < 10:
        if player.role == "fighter":
            player.statistics[1] = player.statistics[1] + 3  # vitality
            player.statistics[3] = player.statistics[3] + 1  # intellect
            player.statistics[5] = player.statistics[5] + 2  # strength
            player.statistics[7] = player.statistics[7] + 1  # wisdom
            player.level = player.level + 1

            player.health = 100
            player.energy = 100

            print("\n----------------------------------------------------------------------")
            print(
                f"| * Congrats, you leveled up! You are now level: {player.level}                   |")
            print("| * In addition, as a fighter, your stats have been increased to:    |")
            print(f"| * {player.statistics}      |")
            print("----------------------------------------------------------------------")

            player.experience = 0
            return player.level

        if player.role == "mage":
            player.statistics[1] = player.statistics[1] + 1  # vitality
            player.statistics[3] = player.statistics[3] + 2  # intellect
            player.statistics[5] = player.statistics[5] + 1  # strength
            player.statistics[7] = player.statistics[7] + 3  # wisdom
            player.level = player.level + 1

            player.health = 100
            player.energy = 100

            print("\n----------------------------------------------------------------------")
            print(
                f"| * Congrats, you leveled up! You are now level: {player.level}                   |")
            print("| * In addition, as a mage, your stats have been increased to:       |")
            print(f"| * {player.statistics}      |")
            print("----------------------------------------------------------------------")

            player.experience = 0
            return player.level

        if player.role == "rogue":
            player.statistics[1] = player.statistics[1] + 2  # vitality
            player.statistics[3] = player.statistics[3] + 1  # intellect
            player.statistics[5] = player.statistics[5] + 3  # strength
            player.statistics[7] = player.statistics[7] + 1  # wisdom
            player.level = player.level + 1

            player.health = 100
            player.energy = 100

            print("\n----------------------------------------------------------------------")
            print(
                f"| * Congrats, you leveled up! You are now level: {player.level}                   |")
            print("| * In addition, as a rogue, your stats have been increased to:      |")
            print(f"| * {player.statistics}      |")
            print("----------------------------------------------------------------------")

            player.experience = 0
            return player.level

    else:
        print("\n*** You're already at max level! (Level 10) *** ")
        return player.level


def attack_enemy(player, enemy):
    # fighters do more damage with 2-handed weapons -------------------------
    if player.role == "fighter":
        if player.equipment[0] == "2H":
            damage = (random.randrange(10, 30) // enemy.level)

            # includes player strength stat to scale overall damage
            stat_scale = damage * player.statistics[5]

            return stat_scale

        else:
            damage = (random.randrange(10, 30) // enemy.level)
            print("\n*** You may have an incorrect weapon type equipped! ***")

            return damage

    # mages do more damage with magic weapons --------------------------------
    if player.role == "mage":
        if player.equipment[0] == "magic":
            damage = (random.randrange(10, 30) // enemy.level)

            # includes player wisdom stat to scale overall damage
            stat_scale = (damage * player.statistics[7]) // 2

            return stat_scale

        else:
            damage = (random.randrange(1, 10) // enemy.level)
            print("\n*** You may have an incorrect weapon type equipped! ***")

            return damage

    # rogues do more damage with 1-handed weapons ----------------------------
    if player.role == "rogue":
        if player.equipment[0] == "1H":
            damage = (random.randrange(10, 30) // enemy.level)

            # includes player strength stat to scale overall damage (strength will be higher for rogues)
            stat_scale = damage * player.statistics[5]

            return stat_scale

        else:
            damage = (random.randrange(1, 10) // enemy.level)
            print("\n*** You may have an incorrect weapon type equipped! ***")

            return damage


def attack_player(player):
    base_damage = (random.randrange(15, 30) // player.level)

    # heavily armored character will take less damage
    if player.equipment[2] == "heavy":
        final_damage = base_damage - 10

        return final_damage

    # lightly armored character will take most damage
    elif player.equipment[2] == "light":
        final_damage = base_damage - 2

        return final_damage

    # medium armored character will take more damage
    elif player.equipment[2] == "medium":
        final_damage = base_damage - 5

        return final_damage

    else:
        print("\n*** You're not wearing any armor! ***")
        return base_damage


def player_move(player, player_direction, water, trees, buildings):
    # size of the game world
    world_boundaries_x_max = 40
    world_boundaries_x_min = 0
    world_boundaries_y_max = 40
    world_boundaries_y_min = 0

    # Flags set to true if this object is detected in collision detection loops
    water_flag = False
    tree_flag = False
    building_flag = False

    # Objects found when flag is set
    water_found = "water"
    tree_found = "tree"
    building_found = "building"

    # ------------------------------------------------------------------------------------------------------------------
    # player chooses up and is still within the upper-y game world boundary --------------------------------------------
    if player_direction == "up" or player_direction == "u":
        if player.y_coordinate < world_boundaries_y_max:

            # water collision detection
            for water_body in water:
                if water_body.y_coordinate - 1 == player.y_coordinate:
                    if water_body.x_coordinate == player.x_coordinate:
                        water_flag = True
                        water_found = water_body
                        break

            # tree collision detection
            for tree in trees:
                if tree.y_coordinate - 1 == player.y_coordinate:
                    if tree.x_coordinate == player.x_coordinate:
                        tree_flag = True
                        tree_found = tree
                        break

            # building collision detection
            for building in buildings:
                if building.y_coordinate - 1 == player.y_coordinate:
                    if building.x_coordinate == player.x_coordinate:
                        building_flag = True
                        building_found = building
                        break

            # if nothing was detected that would block player from moving
            if not water_flag:
                if not tree_flag:
                    if not building_flag:
                        player.y_coordinate = player.y_coordinate + 1
                        print(f"\nYou moved up! Your current position is now: "
                              f"{player.x_coordinate, player.y_coordinate}")

                    else:
                        print("\n*** There appears to be a building here blocking your way.. ***")
                        print(f"\n*** The building is: {building_found.name} ***")

                        if building_found.model == "shop":
                            shop_choice = input(f"\nWould you like to enter the shop? (yes or no): ")
                            if shop_choice.strip().lower() == "yes" or shop_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    # put player in shop, so the shop function can move player when finished and exit
                                    player.x_coordinate = building_found.x_coordinate

                                    shop_instance(player, building_found, "seldon district")

                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    shop_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    shop_instance(player, building_found, "eldream district")

                        if building_found.model == "academia":
                            academia_choice = input(f"\nWould you like to enter the academia? (yes or no): ")
                            if academia_choice.strip().lower() == "yes" or academia_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "seldon district")
                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "eldream district")

                        if building_found.model == "inn":
                            inn_choice = input(f"\nWould you like to enter the inn? (yes or no): ")
                            if inn_choice.strip().lower() == "yes" or inn_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "seldon district")
                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "eldream district")

                else:
                    print("\n*** There appears to be a tree here blocking your way.. ***")
                    print(f"\n*** The tree is: {tree_found.name} ***")

                    if player.quest == "Village Repairs":
                        if not tree_found.gathered:
                            if player.quest_status < 4:
                                print("\nIt appears you can gather some lumber from a large branch that has fallen "
                                      "near the tree.")

                                lumber_choice = input("\nDo you wish to gather the lumber? (Yes or no): ")
                                if lumber_choice == "Yes" or lumber_choice == "y":
                                    if player.quest_status < 4:
                                        player.quest_status = player.quest_status + 1
                                        tree_found.gathered = True
                                        print(f"\n*** You gather the lumber, {player.quest_status}/4 for "
                                              f"[{player.quest}] ***")
                        else:
                            print("\nYou've already gathered lumber from this tree!")
            else:
                print("\n*** There appears to be a body of water blocking your way.. maybe "
                      "there's a way around it? ***")
                print(f"\n*** The water is: {water_found.name} ***")
        else:
            print("\n*** You can't move any further up! ***")

    # ------------------------------------------------------------------------------------------------------------------
    # player chooses up and is still within the upper-y game world boundary --------------------------------------------
    if player_direction == "down" or player_direction == "d":
        if player.y_coordinate > world_boundaries_y_min:

            # water collision detection
            for water_body in water:
                if water_body.y_coordinate + 1 == player.y_coordinate:
                    if water_body.x_coordinate == player.x_coordinate:
                        water_flag = True
                        water_found = water_body
                        break

            # tree collision detection
            for tree in trees:
                if tree.y_coordinate + 1 == player.y_coordinate:
                    if tree.x_coordinate == player.x_coordinate:
                        tree_flag = True
                        tree_found = tree
                        break

            # building collision detection
            for building in buildings:
                if building.y_coordinate + 1 == player.y_coordinate:
                    if building.x_coordinate == player.x_coordinate:
                        building_flag = True
                        building_found = building
                        break

            # if nothing was detected that would block player from moving
            if not water_flag:
                if not tree_flag:
                    if not building_flag:
                        player.y_coordinate = player.y_coordinate - 1
                        print(f"\nYou moved down! Your current position is now: "
                              f"{player.x_coordinate, player.y_coordinate}")

                    else:
                        print("\n*** There appears to be a building here blocking your way.. ***")
                        print(f"\n*** The building is: {building_found.name} ***")

                        if building_found.model == "shop":
                            shop_choice = input(f"\nWould you like to enter the shop? (yes or no): ")
                            if shop_choice.strip().lower() == "yes" or shop_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    shop_instance(player, building_found, "seldon district")
                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    shop_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    shop_instance(player, building_found, "eldream district")

                        if building_found.model == "academia":
                            academia_choice = input(f"\nWould you like to enter the academia? (yes or no): ")
                            if academia_choice.strip().lower() == "yes" or academia_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "seldon district")
                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "eldream district")

                        if building_found.model == "inn":
                            inn_choice = input(f"\nWould you like to enter the inn? (yes or no): ")
                            if inn_choice.strip().lower() == "yes" or inn_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "seldon district")
                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "eldream district")

                else:
                    print("\n*** There appears to be a tree here blocking your way.. ***")
                    print(f"\n*** The tree is: {tree_found.name} ***")

                    if player.quest == "Village Repairs":
                        if not tree_found.gathered:
                            if player.quest_status < 4:
                                print("\nIt appears you can gather some lumber from a large branch that has fallen "
                                      "near the tree.")

                                lumber_choice = input("\nDo you wish to gather the lumber? (Yes or no): ")
                                if lumber_choice == "Yes" or lumber_choice == "y":
                                    if player.quest_status < 4:
                                        player.quest_status = player.quest_status + 1
                                        tree_found.gathered = True
                                        print(f"\n*** You gather the lumber, {player.quest_status}/4 for "
                                              f"[{player.quest}] ***")
                        else:
                            print("\nYou've already gathered lumber from this tree!")
            else:
                print("\n*** There appears to be a body of water blocking your way.. maybe "
                      "there's a way around it? ***")
                print(f"\n*** The water is: {water_found.name} ***")
        else:
            print("\n*** You can't move any further down! ***")

    # ------------------------------------------------------------------------------------------------------------------
    # player chooses up and is still within the upper-y game world boundary --------------------------------------------
    if player_direction == "left" or player_direction == "l":
        if player.x_coordinate > world_boundaries_x_min:

            # water collision detection
            for water_body in water:
                if water_body.x_coordinate + 1 == player.x_coordinate:
                    if water_body.y_coordinate == player.y_coordinate:
                        water_flag = True
                        water_found = water_body
                        break

            # tree collision detection
            for tree in trees:
                if tree.x_coordinate + 1 == player.x_coordinate:
                    if tree.y_coordinate == player.y_coordinate:
                        tree_flag = True
                        tree_found = tree
                        break

            # building collision detection
            for building in buildings:
                if building.x_coordinate + 1 == player.x_coordinate:
                    if building.y_coordinate == player.y_coordinate:
                        building_flag = True
                        building_found = building
                        break

            # if nothing was detected that would block player from moving
            if not water_flag:
                if not tree_flag:
                    if not building_flag:
                        player.x_coordinate = player.x_coordinate - 1
                        print(f"\nYou moved left! Your current position is now: "
                              f"{player.x_coordinate, player.y_coordinate}")

                    else:
                        print("\n*** There appears to be a building here blocking your way.. ***")
                        print(f"\n*** The building is: {building_found.name} ***")

                        if building_found.model == "shop":
                            shop_choice = input(f"\nWould you like to enter the shop? (yes or no): ")
                            if shop_choice.strip().lower() == "yes" or shop_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    shop_instance(player, building_found, "seldon district")
                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    shop_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    shop_instance(player, building_found, "eldream district")

                        if building_found.model == "academia":
                            academia_choice = input(f"\nWould you like to enter the academia? (yes or no): ")
                            if academia_choice.strip().lower() == "yes" or academia_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "seldon district")
                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "eldream district")

                        if building_found.model == "inn":
                            inn_choice = input(f"\nWould you like to enter the inn? (yes or no): ")
                            if inn_choice.strip().lower() == "yes" or inn_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "seldon district")
                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "eldream district")

                else:
                    print("\n*** There appears to be a tree here blocking your way.. ***")
                    print(f"\n*** The tree is: {tree_found.name} ***")

                    if player.quest == "Village Repairs":
                        if not tree_found.gathered:
                            if player.quest_status < 4:
                                print("\nIt appears you can gather some lumber from a large branch that has fallen "
                                      "near the tree.")

                                lumber_choice = input("\nDo you wish to gather the lumber? (Yes or no): ")
                                if lumber_choice == "Yes" or lumber_choice == "y":
                                    if player.quest_status < 4:
                                        player.quest_status = player.quest_status + 1
                                        tree_found.gathered = True
                                        print(f"\n*** You gather the lumber, {player.quest_status}/4 for "
                                              f"[{player.quest}] ***")
                        else:
                            print("\nYou've already gathered lumber from this tree!")
            else:
                print("\n*** There appears to be a body of water blocking your way.. maybe "
                      "there's a way around it? ***")
                print(f"\n*** The water is: {water_found.name} ***")
        else:
            print("\n*** You can't move any further left! ***")

    # ------------------------------------------------------------------------------------------------------------------
    # player chooses up and is still within the upper-y game world boundary --------------------------------------------
    if player_direction == "right" or player_direction == "r":
        if player.x_coordinate < world_boundaries_x_max:

            # water collision detection
            for water_body in water:
                if water_body.x_coordinate - 1 == player.x_coordinate:
                    if water_body.y_coordinate == player.y_coordinate:
                        water_flag = True
                        water_found = water_body
                        break

            # tree collision detection
            for tree in trees:
                if tree.x_coordinate - 1 == player.x_coordinate:
                    if tree.y_coordinate == player.y_coordinate:
                        tree_flag = True
                        tree_found = tree
                        break

            # building collision detection
            for building in buildings:
                if building.x_coordinate - 1 == player.x_coordinate:
                    if building.y_coordinate == player.y_coordinate:
                        building_flag = True
                        building_found = building
                        break

            # if nothing was detected that would block player from moving
            if not water_flag:
                if not tree_flag:
                    if not building_flag:
                        player.x_coordinate = player.x_coordinate + 1
                        print(f"\nYou moved right! Your current position is now: "
                              f"{player.x_coordinate, player.y_coordinate}")

                    else:
                        print("\n*** There appears to be a building here blocking your way.. ***")
                        print(f"\n*** The building is: {building_found.name} ***")

                        if building_found.model == "shop":
                            shop_choice = input(f"\nWould you like to enter the shop? (yes or no): ")
                            if shop_choice.strip().lower() == "yes" or shop_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    shop_instance(player, building_found, "seldon district")
                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    shop_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    shop_instance(player, building_found, "eldream district")

                        if building_found.model == "academia":
                            academia_choice = input(f"\nWould you like to enter the academia? (yes or no): ")
                            if academia_choice.strip().lower() == "yes" or academia_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "seldon district")
                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    academia_instance(player, building_found, "eldream district")

                        if building_found.model == "inn":
                            inn_choice = input(f"\nWould you like to enter the inn? (yes or no): ")
                            if inn_choice.strip().lower() == "yes" or inn_choice.strip().lower() == "y":
                                if player.x_coordinate < 20 and player.y_coordinate < 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "seldon district")
                                if player.x_coordinate < 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "korlok district")
                                if player.x_coordinate > 20 and player.y_coordinate > 20:
                                    print(f"\n\n*** You have entered the {building_found.name}. "
                                          f"You see someone nearby. ***")
                                    time.sleep(1)
                                    player.x_coordinate = building_found.x_coordinate
                                    inn_instance(player, building_found, "eldream district")

                else:
                    print("\n*** There appears to be a tree here blocking your way.. ***")
                    print(f"\n*** The tree is: {tree_found.name} ***")

                    # if player is on quest to gather lumber for Maurelle
                    if player.quest == "Village Repairs":
                        if not tree_found.gathered:
                            if player.quest_status < 4:
                                print("\nIt appears you can gather some lumber from a large branch that has fallen "
                                      "near the tree.")

                                lumber_choice = input("\nDo you wish to gather the lumber? (Yes or no): ")
                                if lumber_choice == "Yes" or lumber_choice == "y":
                                    if player.quest_status < 4:
                                        player.quest_status = player.quest_status + 1
                                        tree_found.gathered = True
                                        print(f"\n*** You gather the lumber, {player.quest_status}/4 for "
                                              f"[{player.quest}] ***")
                        else:
                            print("\nYou've already gathered lumber from this tree!")
            else:
                print("\n*** There appears to be a body of water blocking your way.. maybe "
                      "there's a way around it? ***")
                print(f"\n*** The tree is: {water_found.name} ***")
        else:
            print("\n*** You can't move any further right! ***")


def draw_map(player, enemy_list, npc_list, tree_list, water_list, building_list, path_list):
    print("\n")
    current_map = []

    # player is in screen one, set boundaries to draw screen one -------------------------------------------------------
    if player.x_coordinate < 20 and player.y_coordinate < 20:

        for y in range(20):  # draw screen one -------------------------------------------------------------------------

            current_row = []
            current_map.append(current_row)

            for x in range(20):
                current_row.append("_")

                # if path is at current drawing space
                for path in path_list:
                    if y == path.y_coordinate:
                        if x == path.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "#")

                # if enemy is alive and at current drawing space
                for enemy in enemy_list:
                    if enemy.alive_status:
                        if y == enemy.y_coordinate:
                            if x == enemy.x_coordinate:
                                current_row.pop(x)
                                current_row.insert(x, "X")

                # if npc is alive and at current drawing space
                for npc in npc_list:
                    if npc.alive_status:
                        if y == npc.y_coordinate:
                            if x == npc.x_coordinate:
                                current_row.pop(x)
                                current_row.insert(x, "N")

                # if tree is at current drawing space
                for tree in tree_list:
                    if y == tree.y_coordinate:
                        if x == tree.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "T")

                # if tree is at current drawing space
                for water in water_list:
                    if y == water.y_coordinate:
                        if x == water.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "W")

                # if tree is at current drawing space
                for building in building_list:
                    if y == building.y_coordinate:
                        if x == building.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "B")

                # if player is at current drawing space
                if y == player.y_coordinate:
                    if x == player.x_coordinate:
                        current_row.pop(x)
                        current_row.insert(x, "O")

    # player is in screen two, set boundaries to draw screen two -------------------------------------------------------
    if player.x_coordinate < 20 and player.y_coordinate > 20:

        for y in range(20):  # draw screen two -------------------------------------------------------------------------

            current_row = []
            current_map.append(current_row)

            for x in range(20):
                current_row.append("_")

                # if path is at current drawing space
                for path in path_list:
                    if y + 20 == path.y_coordinate:
                        if x == path.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "#")

                # if enemy is alive and at current drawing space
                for enemy in enemy_list:
                    if enemy.alive_status:
                        if y + 20 == enemy.y_coordinate:
                            if x == enemy.x_coordinate:
                                current_row.pop(x)
                                current_row.insert(x, "X")

                # if npc is alive and at current drawing space
                for npc in npc_list:
                    if npc.alive_status:
                        if y + 20 == npc.y_coordinate:
                            if x == npc.x_coordinate:
                                current_row.pop(x)
                                current_row.insert(x, "N")

                # if tree is at current drawing space
                for tree in tree_list:
                    if y + 20 == tree.y_coordinate:
                        if x == tree.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "T")

                # if tree is at current drawing space
                for water in water_list:
                    if y + 20 == water.y_coordinate:
                        if x == water.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "W")

                # if tree is at current drawing space
                for building in building_list:
                    if y + 20 == building.y_coordinate:
                        if x == building.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "B")

                # if player is at current drawing space
                if y + 20 == player.y_coordinate:
                    if x == player.x_coordinate:
                        current_row.pop(x)
                        current_row.insert(x, "O")

    # player is in screen three, set boundaries to draw screen three ---------------------------------------------------
    if player.x_coordinate > 20 and player.y_coordinate > 20:

        for y in range(20):  # draw screen 3  --------------------------------------------------------------------------

            current_row = []
            current_map.append(current_row)

            for x in range(20):
                current_row.append("_")

                # if path is at current drawing space
                for path in path_list:
                    if y + 20 == path.y_coordinate:
                        if x + 20 == path.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "#")

                # if enemy is alive and at current drawing space
                for enemy in enemy_list:
                    if enemy.alive_status:
                        if y + 20 == enemy.y_coordinate:
                            if x + 20 == enemy.x_coordinate:
                                current_row.pop(x)
                                current_row.insert(x, "X")

                # if npc is alive and at current drawing space
                for npc in npc_list:
                    if npc.alive_status:
                        if y + 20 == npc.y_coordinate:
                            if x + 20 == npc.x_coordinate:
                                current_row.pop(x)
                                current_row.insert(x, "N")

                # if tree is at current drawing space
                for tree in tree_list:
                    if y + 20 == tree.y_coordinate:
                        if x + 20 == tree.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "T")

                # if tree is at current drawing space
                for water in water_list:
                    if y + 20 == water.y_coordinate:
                        if x + 20 == water.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "W")

                # if tree is at current drawing space
                for building in building_list:
                    if y + 20 == building.y_coordinate:
                        if x + 20 == building.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "B")

                # if player is at current drawing space
                if y + 20 == player.y_coordinate:
                    if x + 20 == player.x_coordinate:
                        current_row.pop(x)
                        current_row.insert(x, "O")

    # player is in screen four, set boundaries to draw screen four -----------------------------------------------------
    if player.x_coordinate > 20 and player.y_coordinate < 20:

        for y in range(20):  # draw screen four --------------------------------------------------------------

            current_row = []
            current_map.append(current_row)

            for x in range(20):
                current_row.append("_")

                # if path is at current drawing space
                for path in path_list:
                    if y == path.y_coordinate:
                        if x + 20 == path.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "#")

                # if enemy is alive and at current drawing space
                for enemy in enemy_list:
                    if enemy.alive_status:
                        if y == enemy.y_coordinate:
                            if x + 20 == enemy.x_coordinate:
                                current_row.pop(x)
                                current_row.insert(x, "X")

                # if npc is alive and at current drawing space
                for npc in npc_list:
                    if npc.alive_status:
                        if y == npc.y_coordinate:
                            if x + 20 == npc.x_coordinate:
                                current_row.pop(x)
                                current_row.insert(x, "N")

                # if tree is at current drawing space
                for tree in tree_list:
                    if y == tree.y_coordinate:
                        if x + 20 == tree.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "T")

                # if tree is at current drawing space
                for water in water_list:
                    if y == water.y_coordinate:
                        if x + 20 == water.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "W")

                # if tree is at current drawing space
                for building in building_list:
                    if y == building.y_coordinate:
                        if x + 20 == building.x_coordinate:
                            current_row.pop(x)
                            current_row.insert(x, "B")

                # if player is at current drawing space
                if y == player.y_coordinate:
                    if x + 20 == player.x_coordinate:
                        current_row.pop(x)
                        current_row.insert(x, "O")

    for row in current_map:
        row.remove(row[0])

    # get map rows from current map list (list of lists) and print
    # starts from 1 to avoid printing empty row
    # reverse is for flipping map to make it read from bottom left (vs. top left) to top right

    print("------------------------------------------------------------------------------------------------------")
    current_map.reverse()
    for i in range(1, len(current_map) - 1):
        print("|-", current_map[i], "--|")

    print("------------------------------------------------------------------------------------------------------")
    print("| * Map guide: O = player, X = enemy, N = npc, T = tree, W = water, B = building, '_' = ground       |")
    print("| *            # = pathway, M = mountain                                                             |")
    print("------------------------------------------------------------------------------------------------------")

    time.sleep(1)
    return


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# scenarios ------------------------------------------------------------------------------------------------------------

def attack_scenario(player, enemy):
    # Verifies player is still in range of enemy
    if player.x_coordinate == enemy.x_coordinate and player.y_coordinate == enemy.y_coordinate:

        # doesn't work correctly atm, for barrier skill
        # original_player_gear_type = player.equipment[2]

        print("\n-----------------------------------------------------------------------------------------------------"
              "-")
        combat_choice = input("What do you want to do? (Type Attack, Use Skill, Character Status or Run): ")

        if combat_choice.strip().lower() == "attack" or combat_choice.strip().lower() == "a":

            if enemy.alive_status and player.x_coordinate == enemy.x_coordinate:
                # returns players damage to the enemy based on level and equipment
                attacked_enemy = attack_enemy(player, enemy)

                enemy.health = enemy.health - attacked_enemy

                # if enemy is not dead yet
                if enemy.health > 0:

                    print(f"\nYou did {attacked_enemy} damage to the {enemy.kind}, "
                          f"who's health is now {enemy.health}/100.")
                    time.sleep(1)

                    # returns total damage output from enemy as attacked_player value
                    attacked_player = attack_player(player)
                    if attacked_player > 0:
                        print(f'\nOuch! The {enemy.kind} retaliates and damages you for {attacked_player}.')
                        player.health = player.health - attacked_player
                        time.sleep(1)

                        if player.health > 0:
                            print(f"\nYour health is now: {player.health}/100.")
                            time.sleep(1)
                            attack_scenario(player, enemy)

                        else:  # your health is zero and you're dead
                            print("\n*** You've suffered a fatality ***")
                            player.alive_status = False
                            time.sleep(1)
                            print("\n\n"
                                  "------------------------------------------------------------------------------------"
                                  "------------------")
                            print(
                                f"| * Oh dear, you are dead! Try again.                                               "
                                f"                 |")
                            print(
                                "--------------------------------------------------------------------------------------"
                                "----------------\n\n")
                            exit()

                    else:
                        print(f'\nThe {enemy.kind} attempted to retaliate, but missed and did no damage!')
                        time.sleep(1)
                        attack_scenario(player, enemy)

                # enemy has been defeated, will return an amount of xp based on current levels
                else:

                    # if player is on quest to kill snakes from Garan
                    if enemy.kind == "snake":
                        if player.quest == "Stupid Snakes":
                            if player.quest_status < 4:
                                player.quest_status = player.quest_status + 1
                                print(f"\n*** {player.quest_status}/4 snakes for [{player.quest}] quest ***")
                                time.sleep(1)

                    # if player is on quest to kill snakes from Garan
                    if enemy.kind == "ghoul":
                        if player.quest == "Ghoulish Glee":
                            if player.quest_status < 4:
                                player.quest_status = player.quest_status + 1
                                print(f"\n*** {player.quest_status}/4 ghouls for [{player.quest}] quest ***")
                                time.sleep(1)

                    # only gain experience from enemies equal or higher level
                    if player.level <= enemy.level:
                        experience = int((enemy.level / player.level) * 5)
                        player.experience = player.experience + experience
                        print(f"\nYou killed the {enemy.kind} and gained {experience} experience!\n")
                        print(f"Your current experience is {player.experience}/100")

                    drop_chance = random.randrange(1, 10)

                    # 70% chance to drop merchant item
                    if drop_chance > 3:
                        player.inventory.append(enemy.items)
                        print(f"\nThe {enemy.kind} dropped a [{enemy.items}], which has been added to your "
                              f"inventory. \n")

                    time.sleep(1)

                    # player will level up (see level up method)
                    if player.experience > 100:
                        level_up(player)

                    # doesn't work correctly atm
                    # player.equipment[2] = original_player_gear_type

                    enemy.alive_status = False
                    time.sleep(1)

            else:
                print("\nThis enemy appears to be dead already!")

        if combat_choice.strip().lower() == "use skill" or combat_choice.strip().lower() == "skill" \
                or combat_choice.strip().lower() == "use" or combat_choice.strip().lower() == "k" \
                or combat_choice.strip().lower() == "u":

            print(f"\nYour skills: {player.skills}")
            skill_choice = input("\nWhich skill would you like to use? (type a skill): ")

            if player.role == "fighter":
                if skill_choice.strip().lower() == "heavy swing" or skill_choice.strip().lower() == "heavy" \
                        or skill_choice.strip().lower() == "swing" or skill_choice.strip().lower() == "h":
                    print(f"\nYou use prepare to use Heavy Swing on {enemy.kind}. ")
                    time.sleep(1)
                    print(f"\nYou whack the {enemy.kind} for 20 damage!")
                    time.sleep(1)
                    enemy.health = enemy.health - 20
                    print(f"\nThe {enemy.kind}'s health is now {enemy.health}/100.")
                    time.sleep(1)
                    print("\n*** Using this skill has consumed some of your energy! ***")
                    time.sleep(1)
                    player.energy = player.energy - 25
                    print(f"\nYour energy level is now {player.energy}/100.")

                    # if player skill kills the enemy
                    if enemy.health <= 0:

                        # if player is on quest to kill snakes from Garan
                        if enemy.kind == "snake":
                            if player.quest == "Stupid Snakes":
                                if player.quest_status < 4:
                                    player.quest_status = player.quest_status + 1
                                    print(f"\n*** {player.quest_status}/4 snakes for [{player.quest}] quest ***")
                                    time.sleep(1)

                        # if player is on quest to kill snakes from Garan
                        if enemy.kind == "ghoul":
                            if player.quest == "Ghoulish Glee":
                                if player.quest_status < 4:
                                    player.quest_status = player.quest_status + 1
                                    print(f"\n*** {player.quest_status}/4 ghouls for [{player.quest}] quest ***")
                                    time.sleep(1)

                        # only gain experience from enemies equal or higher level
                        if player.level <= enemy.level:
                            experience = int((enemy.level / player.level) * 5)
                            player.experience = player.experience + experience
                            print(f"\nYou killed the {enemy.kind} and gained {experience} experience!\n")
                            print(f"Your current experience is {player.experience}/100")

                        drop_chance = random.randrange(1, 10)

                        # 70% chance to drop merchant item
                        if drop_chance > 3:
                            player.inventory.append(enemy.items)
                            print(f"\nThe {enemy.kind} dropped a [{enemy.items}], which has been added to your "
                                  f"inventory. \n")

                        time.sleep(1)

                        # player will level up (see level up method)
                        if player.experience > 100:
                            level_up(player)

                        # doesn't work correctly atm
                        # player.equipment[2] = original_player_gear_type

                        enemy.alive_status = False
                        time.sleep(1)
                        player.x_coordinate -= 1

                    time.sleep(1)
                    attack_scenario(player, enemy)

                if skill_choice.strip().lower() == "protection" or skill_choice.strip().lower() == "p":

                    # verify player has learned the ability
                    for x in player.skills:
                        if x == "protection":
                            print("\nYou grit your teeth and dig your feet in. You feel ready for anything! ")
                            print("\n*** Using Protection has given you +10 armor protection! ***")
                            time.sleep(1)
                            print("\n*** This effect will last the duration of the fight. ***")
                            time.sleep(1)
                            print("\n*** Using this skill has consumed some of your energy! ***")
                            time.sleep(1)
                            player.energy = player.energy - 25
                            print(f"\nYour energy level is now {player.energy}/100.")
                            time.sleep(1)
                            attack_scenario(player, enemy)

            if player.role == "mage":
                if skill_choice.strip().lower() == "barrier" or skill_choice.strip().lower() == "b":
                    print(f"\nYou use Barrier on self. ")
                    player.equipment[2] = "heavy"
                    print("\n*** Using Barrier has given you +10 armor protection! ***")
                    time.sleep(1)
                    print("\n*** This effect will last the duration of the fight. ***")
                    time.sleep(1)
                    print("\n*** Using this skill has consumed some of your energy! ***")
                    time.sleep(1)
                    player.energy = player.energy - 25
                    print(f"\nYour energy level is now {player.energy}/100.")
                    time.sleep(1)
                    attack_scenario(player, enemy)

                if skill_choice.strip().lower() == "chillshot" or skill_choice.strip().lower() == "c":
                    # verify player has learned the ability
                    for x in player.skills:
                        if x == "chillshot":
                            print(f"\nYou use prepare to use Chillshot on {enemy.kind}. ")
                            time.sleep(1)
                            print(f"\nYou slice the air and feel the cold rush forth to the {enemy.kind}!")
                            time.sleep(1)
                            print(f"\n{enemy.kind} has taken 20 damage!")
                            enemy.health = enemy.health - 20
                            print(f"\nThe {enemy.kind}'s health is now {enemy.health}/100.")
                            time.sleep(1)
                            print("\n*** Using this skill has consumed some of your energy! ***")
                            time.sleep(1)
                            player.energy = player.energy - 25
                            print(f"\nYour energy level is now {player.energy}/100.")

                            # if player skill kills the enemy
                            if enemy.health <= 0:

                                # if player is on quest to kill snakes from Garan
                                if enemy.kind == "snake":
                                    if player.quest == "Stupid Snakes":
                                        if player.quest_status < 4:
                                            player.quest_status = player.quest_status + 1
                                            print(
                                                f"\n*** {player.quest_status}/4 snakes for [{player.quest}] quest ***")
                                            time.sleep(1)

                                # if player is on quest to kill snakes from Garan
                                if enemy.kind == "ghoul":
                                    if player.quest == "Ghoulish Glee":
                                        if player.quest_status < 4:
                                            player.quest_status = player.quest_status + 1
                                            print(
                                                f"\n*** {player.quest_status}/4 ghouls for [{player.quest}] quest ***")
                                            time.sleep(1)

                                # only gain experience from enemies equal or higher level
                                if player.level <= enemy.level:
                                    experience = int((enemy.level / player.level) * 5)
                                    player.experience = player.experience + experience
                                    print(f"\nYou killed the {enemy.kind} and gained {experience} experience!\n")
                                    print(f"Your current experience is {player.experience}/100")

                                drop_chance = random.randrange(1, 10)

                                # 70% chance to drop merchant item
                                if drop_chance > 3:
                                    player.inventory.append(enemy.items)
                                    print(f"\nThe {enemy.kind} dropped a [{enemy.items}], which has been added to your "
                                          f"inventory. \n")

                                time.sleep(1)

                                # player will level up (see level up method)
                                if player.experience > 100:
                                    level_up(player)

                                # doesn't work correctly atm
                                # player.equipment[2] = original_player_gear_type

                                enemy.alive_status = False
                                time.sleep(1)
                                player.x_coordinate -= 1

                            time.sleep(1)
                            attack_scenario(player, enemy)

            if player.role == "rogue":
                if skill_choice.strip().lower() == "swift strike" or skill_choice.strip().lower() == "swift" \
                        or skill_choice.strip().lower() == "strike" or skill_choice.strip().lower() == "s":
                    print(f"\nYou use prepare to use Swift Strike on {enemy.kind}.")
                    time.sleep(1)
                    print(f"\nYou quickly slash the {enemy.kind} for 30 damage!")
                    time.sleep(1)
                    enemy.health = enemy.health - 30
                    print(f"\nThe {enemy.kind}'s health is now {enemy.health}/100.")
                    time.sleep(1)
                    print("\n*** Using this skill has consumed some of your energy! ***")
                    time.sleep(1)
                    player.energy = player.energy - 25
                    print(f"\nYour energy level is now {player.energy}/100.")

                    # if player skill kills the enemy
                    if enemy.health <= 0:

                        # if player is on quest to kill snakes from Garan
                        if enemy.kind == "snake":
                            if player.quest == "Stupid Snakes":
                                if player.quest_status < 4:
                                    player.quest_status = player.quest_status + 1
                                    print(f"\n*** {player.quest_status}/4 snakes for [{player.quest}] quest ***")
                                    time.sleep(1)

                        # if player is on quest to kill snakes from Garan
                        if enemy.kind == "ghoul":
                            if player.quest == "Ghoulish Glee":
                                if player.quest_status < 4:
                                    player.quest_status = player.quest_status + 1
                                    print(f"\n*** {player.quest_status}/4 ghouls for [{player.quest}] quest ***")
                                    time.sleep(1)

                        # only gain experience from enemies equal or higher level
                        if player.level <= enemy.level:
                            experience = int((enemy.level / player.level) * 5)
                            player.experience = player.experience + experience
                            print(f"\nYou killed the {enemy.kind} and gained {experience} experience!\n")
                            print(f"Your current experience is {player.experience}/100")

                        drop_chance = random.randrange(1, 10)

                        # 70% chance to drop merchant item
                        if drop_chance > 3:
                            player.inventory.append(enemy.items)
                            print(f"\nThe {enemy.kind} dropped a [{enemy.items}], which has been added to your "
                                  f"inventory. \n")

                        time.sleep(1)

                        # player will level up (see level up method)
                        if player.experience > 100:
                            level_up(player)

                        # doesn't work correctly atm
                        # player.equipment[2] = original_player_gear_type

                        enemy.alive_status = False
                        time.sleep(1)
                        player.x_coordinate -= 1

                    time.sleep(1)
                    attack_scenario(player, enemy)

                if skill_choice.strip().lower() == "evasion tactics" or skill_choice.strip().lower() == "evasion" \
                        or skill_choice.strip().lower() == "e":
                    # verify player has learned the ability
                    for x in player.skills:
                        if x == "evasion tactics":
                            print(f"\nYou use Evasion Tactics on self. ")
                            player.equipment[2] = "heavy"
                            print("\n*** Using Evade has given you additional protection! ***")
                            time.sleep(1)
                            print("\n*** This effect will last the duration of the fight. ***")
                            time.sleep(1)
                            print("\n*** Using this skill has consumed some of your energy! ***")
                            time.sleep(1)
                            player.energy = player.energy - 25
                            print(f"\nYour energy level is now {player.energy}/100.")
                            time.sleep(1)
                            attack_scenario(player, enemy)

        if combat_choice.strip().lower() == "run" or combat_choice.strip().lower() == "r":

            escape_chance = random.randrange(35, 75)
            if escape_chance > 50:

                print("\nYou escaped safely!")
                time.sleep(1)
                player.x_coordinate = player.x_coordinate - 1
                attack_scenario(player, enemy)

            else:
                print(f"\nThe {enemy.kind} blocked your escape!")
                time.sleep(1)
                attack_scenario(player, enemy)

        if combat_choice.strip().lower() == "character status" or combat_choice.strip().lower() == "status" \
                or combat_choice.strip().lower() == "s" or combat_choice.strip().lower() == "c":

            print(f"\n*** Your current status: health: {player.health}, energy: {player.energy} ***")
            print(f"\n*** Your current equipment: {player.equipment} ***")

            time.sleep(1)
            attack_scenario(player, enemy)

        else:
            if enemy.alive_status:
                attack_scenario(player, enemy)

    else:
        return


def npc_interaction_scenario(player, npc):
    # Verifies player is still in range of npc
    if player.x_coordinate == npc.x_coordinate and player.y_coordinate == npc.y_coordinate:

        print(f"\n{npc.name} says: '{npc.dialog}'")
        print("\n-----------------------------------------------------------------------------------------------------")

        interaction_choice = input("What do you want to say? (Information, Quest, Examine or Leave): ")

        if interaction_choice.strip().lower() == "information" or interaction_choice.strip().lower() == "info" \
                or interaction_choice.strip().lower() == "i":

            if npc.race == "amuna":
                print(f"\n{npc.name} says: You're currently in the Amuna district of Seldon. \n\nWe're one part of a "
                      f"new Region named Consona inhabited by all three known races in an effort \nto build better "
                      f"relations amongst "
                      f"our peoples. \n\nIt's a quiet District for the most part, however with the recent takeover of "
                      f"our "
                      f"capital castle by the \nbeast 'Dreth' and his minions, we've had to wall off the most "
                      f"eastern region to protect \nthe local settlement. \n\nAlthough, even with these precautions in "
                      f"place some ghouls have still managed to creep through. \nPlease be careful if you go to that "
                      f"area of the district! \n\nIf you're looking for a shop to buy and sell items, check the Village"
                      f"\non the eastern side of the District. \n\nIf you're looking for a trainer to teach you new"
                      f"skills,\nyou can also find them in the Village as well as an inn to rest!")

                time.sleep(1)

                npc_interaction_scenario(player, npc)

        if interaction_choice.strip().lower() == "quest" or interaction_choice.strip().lower() == "q":

            # if player has not done this NPCs quest yet
            if not npc.quest_complete:

                # if NPC has not given player their quest yet
                if player.quest != npc.quest:

                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          "~~~~~~~~~~~~")
                    print(f"{npc.name} says: {npc.quest_description}")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          "~~~~~~~~~~")

                    quest_choice = input("\nDo you wish to accept this quest? (Type yes or no): ")
                    if quest_choice == "yes" or quest_choice == "y":

                        # when player talks to garan for the first time, he will give them a basic item for their role
                        if npc.name == "Garan":
                            if not npc.gift:
                                if player.role == "fighter":
                                    player.equipment[0] = "2H"
                                    player.equipment[1] = "rusty sword"
                                    player.equipment[2] = "heavy"
                                    player.equipment[3] = "damaged plate"
                                    player.inventory.append("health potion")
                                    npc.gift = True
                                    print(
                                        "\n*** Garan has given you a weapon: [rusty sword] and gear: [damaged plate] "
                                        "***")
                                    print("\n*** Garan has also given you a: Health Potion ***")
                                    time.sleep(2)

                                if player.role == "mage":
                                    player.equipment[0] = "magic"
                                    player.equipment[1] = "broken staff"
                                    player.equipment[2] = "light"
                                    player.equipment[3] = "tattered robes"
                                    player.inventory.append("health potion")
                                    npc.gift = True
                                    print(
                                        "\n*** Garan has given you a weapon: [broken staff] and gear: [tattered robes] "
                                        "***")
                                    print("\n*** Garan has also given you a: Health Potion ***")
                                    time.sleep(2)

                                if player.role == "rogue":
                                    player.equipment[0] = "1H"
                                    player.equipment[1] = "dull dagger"
                                    player.equipment[2] = "medium"
                                    player.equipment[3] = "worn jerkin"
                                    player.inventory.append("health potion")
                                    npc.gift = True
                                    print(
                                        "\n*** Garan has given you a weapon: [dull dagger] and gear: [worn jerkin] ***")
                                    print("\n*** Garan has also given you a: Health Potion ***")
                                    time.sleep(2)

                        # if player doesn't already have an active quest (currently only can have one quest at a time)
                        if player.quest_status == 0:
                            print(f"\nYou chose to accept {npc.name}'s quest [{npc.quest}]. ")
                            player.quest = npc.quest
                            player.quest_status = 0
                            time.sleep(1)
                            npc_interaction_scenario(player, npc)

                        else:
                            print(f"\nYou are already on a quest! [{player.quest}]")

                # if player has completed NPCs quest with 4 objectives, will give level and item reward
                # as well as additional dialog from NPC related to the narrative
                else:
                    if player.quest_status == 4:
                        npc.quest_complete = True
                        player.quest_status = 0
                        player.quest = ""
                        print(f"\n*** Quest [{npc.quest}] Complete! ***")
                        time.sleep(2)
                        level_up(player)
                        time.sleep(2)

                        player.rupees = player.rupees + 10
                        print(f"\n*** NPC {npc.name} has given you 10 rupees! ***")
                        time.sleep(2)

                        player.inventory.append("health potion")
                        print("\n*** You have also gained a health potion! "
                              "This item has been added to your inventory. ***")
                        time.sleep(2)

                        if npc.name == "Garan":
                            print(
                                "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                                "~~~~~~~~~~~~~~~~~")
                            print(f"{npc.name} says: Thanks for taking care of those snakes! You're clearly a capable"
                                  f" {player.role}. \n\nWe could use someone like you in the resistance Vanguard. "
                                  f"Please,"
                                  f" head east to the nearby Village\nand see if they need any assistance. They were"
                                  f" attacked recently by a wave of Ghoul Minions. \n\nWe've been out"
                                  f" picking off the rest of the stragglers, but there will be more work to be done."
                                  f"\n\nNera bless you, {player.name}.")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                                  "~~~~~~~~~~~~~~~~~")

                            continue_choice = input("\n*** Press Enter key when ready to continue: ***")

                            # purpose is to give input a way to continue and not get stuck so that player
                            # only needs to press enter to continue
                            if continue_choice == "lol":
                                print("Why you do this")

                        if npc.name == "Village Matron Maurelle":
                            print(
                                "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                                "~~~~~~~~~~~~~~~~~")
                            print(f"{npc.name} says: Thank you for assisting us in our hour of need,"
                                  f" {player.name}. \nI fear this isn't the last time we will need to recover from such"
                                  f" an attack.. \nWe can only beseech the goddess Nera to deliver us from these "
                                  f"difficult times. \n\nAre you planning on journeying north? If so, you will cross "
                                  f"into"
                                  f" the District of Korlok. \nThe Vanguard Captain Adria headed there recently to "
                                  f"coordinate efforts with the Nuldar \nand our people to forge new"
                                  f" materials. I don't understand much of the details myself, \nhowever Adria has been"
                                  f" gone for some time. \n\nI've begun to worry, and she must know of the recent wave "
                                  f"of "
                                  f"attacks, as well as the damage we've \nsustained. Please, find Adria in the Korlok"
                                  f" District to the north and \nrelay my concerns to her!")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                                  "~~~~~~~~~~~~~~~~~")

                            continue_choice = input("\n*** Press Enter key when ready to continue: ***")

                            # purpose is to give input a way to continue and not get stuck so that player
                            # only needs to press enter to continue
                            if continue_choice == "lol":
                                print("Why you do this")

                        if npc.name == "Guard":
                            print(
                                "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                                "~~~~~~~~~~~~~~~~~")
                            print(f"{npc.name} says: The Ghoul Minions have been taken care of, then? \nNera's grace"
                                  f", we may finally gain a moment of respite. \n\nI will signal the other Bridge"
                                  f" Guards to unbar the gates and allow you to cross.\n\nBe careful, {player.name},"
                                  f" these are unforgiving times. ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                                  "~~~~~~~~~~~~~~~~~")

                            continue_choice = input("\n*** Press Enter key when ready to continue: ***")

                            # purpose is to give input a way to continue and not get stuck so that player
                            # only needs to press enter to continue
                            if continue_choice == "lol":
                                print("Why you do this")

                            player.x_coordinate = 32
                            player.y_coordinate = 22

                            print("\n\n*** The Bridge Guards have allowed you passage. ")
                            time.sleep(3)
                            print("\n*** As you walk through the gates, you look over the side to the water below. "
                                  "***")
                            time.sleep(3)
                            print("\n*** The Rohir River is deep and dark as it is wide. You note there are no "
                                  "other "
                                  "ways to cross. ***")
                            time.sleep(4)
                            print("\n*** You emerge on the other side of the Bridge ***")
                            time.sleep(3)
                            print("\n*** You are now within the Korlok District of the Consona Region World ***")
                            time.sleep(3)
                            print("\n*** You feel the heat on your face and look around to notice the bright "
                                  "oranges "
                                  "and reds of the terrain, ***")
                            time.sleep(4)
                            print("\n*** As well as snow-capped mountain peaks in the distance.. ***")
                            time.sleep(3)
                            print("\n*** Where could the Vanguard Captain Adria be? ***")
                            time.sleep(3)

                        time.sleep(1)
                        npc_interaction_scenario(player, npc)

            # NPCs quest has already been completed by player
            else:
                print(f"\nYou have already completed {npc.name}'s quest [{npc.quest}]. ")
                time.sleep(1)
                npc_interaction_scenario(player, npc)

        # moves player away from NPC to return to regular action screen
        if interaction_choice.strip().lower() == "leave" or interaction_choice.strip().lower() == "l":
            print(f"\n*** You say goodbye to {npc.name} and head on your way ***")
            time.sleep(1)
            player.x_coordinate = player.x_coordinate + 1
            player.y_coordinate = player.y_coordinate + 1
            print(f"\n*** Your new coordinates are: {player.x_coordinate, player.y_coordinate} ***")
            time.sleep(1)

        # returns information based on the NPC being interacted with
        if interaction_choice.strip().lower() == "examine" or interaction_choice.strip().lower() == "exam" or \
                interaction_choice.strip().lower() == "e":
            print(f"\n*** NPC info: NPC name - {npc.name}, NPC gender - {npc.gender}, NPC race - {npc.race},"
                  f" NPC role - {npc.role} ***")

        npc_interaction_scenario(player, npc)

    return


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# run stuff ------------------------------------------------------------------------------------------------------------

# basic game run command, can take any player, enemy and npc as parameters
def game_run(player, enemies, npcs, trees, water, buildings, paths):
    chosen = False

    while player.alive_status:

        if not greeting.shown:
            print(greeting.message)
            greeting.shown = True

        if len(character_list) < 2:
            if not chosen:

                create_choice = input("\n\nWould you like to create a character? (Type yes or no): ")

                if create_choice == "yes" or create_choice == "y":
                    chosen = True

                    # starts character creator tool and returns created character to set to current player
                    player = create_a_character()

                # developer mode character for testing game features
                elif create_choice == "dev mode":
                    chosen = True   # name           gender   race     role    inventory
                    player = Player("Intrinsic Dev", "male", "sorae", "mage", ["health potion", "health potion",
                                                                               "energy potion", "energy potion",
                                                                               "shiny rock", "shiny rock",
                                                                               "bone dust", "bone dust"],
                                    # equipment
                                    ["magic", "omega staff", "light", "omega robes"], "", 0,
                                    # stats
                                    ["vitality", 10, "intellect", 10, "strength", 10, "wisdom", 10],
                                    # skills, level, experience, health, energy
                                    ["heavy swing", "barrier", "swift strike"], 4, 0, 100, 100,
                                    # x-coordinate, y-coordinate, alive status, rupees, reputation, mount
                                    1, 1, True, 1000, ["amuna", 105, "nuldar", 105, "sorae", 105], "lamb of god")

                else:
                    chosen = True
                    # continues to use default character
                    player = player

                    print("\n*** Starting game with default character build... ***")
                    print("\n*** You are entering the world... ***\n")
                    time.sleep(1)

        # if player is in range of enemy
        for enemy in enemies:
            if player.x_coordinate == enemy.x_coordinate:
                if player.y_coordinate == enemy.y_coordinate:

                    if enemy.alive_status:
                        # check to see how many enemies are alive, if number of dead enemies is large some
                        # will be respawned based on the enemy kind and location
                        enemy_respawn_counter(enemies)

                        # store player gear type for use in replacing after enemy combat encounter
                        # ex. if player is mage and uses barrier to temporarily gain heavy armor
                        player_gear_type = player.equipment[2]

                        print(f'\n\n*** You encounter an enemy {enemy.kind}, level {enemy.level} ***')
                        attack_scenario(player, enemy)

                        # restores player equipment type after battle
                        player.equipment[2] = player_gear_type

        # if player is in range of npc (to do create dialog/quest from npc in the scenarios section)
        for npc in npcs:
            if player.x_coordinate == npc.x_coordinate:
                if player.y_coordinate == npc.y_coordinate:

                    if npc.alive_status:
                        print(f'\n\n*** You meet an npc {npc.name} ***')
                        npc_interaction_scenario(player, npc)

        # Player introduction to Seldon, the starting location.
        if not game_start.shown:
            print(game_start.message)
            time.sleep(2)
            game_start.shown = True

        print("\n\n"
              "------------------------------------------------------------------------------------------------------")
        print("| Actions: Check Status, Check Inventory, Check Equipment, Check Skills, Check Location, Check Quest |")
        print("|          Move Character, Draw Map, Use item, Use skill, Hotkeys, How to Play, Exit Game            |")
        print("------------------------------------------------------------------------------------------------------")

        # Hint for player for action hotkeys, should only show once at action screen
        if not game_hint.shown:
            print(game_hint.message)
            time.sleep(2)
            game_hint.shown = True

        player_choice = input("\nWhat would you like to do? (Type an action): ")

        if player_choice.strip().lower() == "how to play" or player_choice.strip().lower() == "how" or \
                player_choice.strip().lower() == "play" or player_choice.strip().lower() == "help":
            print("\nYour character is on an adventure! The world is open to you to explore, so look"
                  " around and \nsee what you can find. Currently all actions are based on text input from"
                  " the user entered into \nthe console. \n\nUpon reaching the action screen, just type the command"
                  " corresponding to the action\nyou would like your character to perform next. For example, to move"
                  " up on the map, type 'move'\nand hit enter. Once in the move menu type 'up' to go up. Following this"
                  "action you will be returned \nto the main action screen where you can perform more character "
                  "commands. "
                  "\n\nTo see where your character is currently located in the world, type 'draw map' or 'draw' and "
                  "\nthe game will print out a current rendition of the game world to the console, including nearby"
                  "\nenemies and npcs. Pay attention to the map guide to see what each symbol on the map stands for. "
                  "\n\nTry talking to some nearby NPCs and see if they have any information or quests to give you! "
                  "\nOr, "
                  " you can try to fight nearby enemies. Just be careful, higher level enemies will do more damage \nto"
                  " you and you can end up dead! At this point the game will end and you can restart. "
                  "\n\nTo talk to an NPC, just move your character to the location you see the NPC printed on the map "
                  "\n(see this by typing 'draw map' or 'draw' at the action screen). Once you are nearby the NPC, "
                  "you will \nhave the option to talk to them."
                  "\n\nFighting enemies works in the same way you talk to NPCs. Just move close to where the enemy is"
                  "\nlocated on the map and a battle sequence will start. Here you can choose to attack the enemy or to"
                  "\ntry and escape. If you escape you will have a chance to recover by drinking a health potion \n(if"
                  " you've got one!)"
                  "\n\nYou can buy potions and other items from some NPCs nearby buildings. \nSometimes you can also"
                  " sell items dropped from enemies to them, so be sure to check the local shop!")
            time.sleep(1)
            time.sleep(1)

        if player_choice.strip().lower() == "hotkeys" or player_choice.strip().lower() == "hot" or \
                player_choice.strip().lower() == "h":
            print("\nSome useful choice shortcuts to navigate menu: ")
            print("\nstatus = s")
            print("\ninventory = i")
            print("\nequipment = e")
            print("\nskills = k")
            print("\nlocation = l")
            print("\nquests = q")
            print("\nmove = m, right = r, left = l, up = u, down = d")
            print("\ndraw map = d")
            time.sleep(1)

        if player_choice.strip().lower() == "move character" or player_choice.strip().lower() == "move" \
                or player_choice.strip().lower() == "m":

            player_direction = input("\nWhich direction would you like to move in? (Type up, down, left or right): ")

            # allow player to move if not in range of enemy (combat check)
            if player.x_coordinate != [enemy.x_coordinate for enemy in enemies] or \
                    player.y_coordinate != [enemy.y_coordinate for enemy in enemies]:
                player_move(player, player_direction, water, trees, buildings)

        if player_choice.strip().lower() == "draw map" or player_choice.strip().lower() == "draw" or \
                player_choice.strip().lower() == "d":
            draw_map(player, enemies, npcs, trees, water, buildings, paths)

        if player_choice.strip().lower() == "check inventory" or player_choice.strip().lower() == "inventory" or \
                player_choice.strip().lower() == "i":
            print(f"\nYour current inventory: {player.inventory}")
            time.sleep(1)

        if player_choice.strip().lower() == "check equipment" or player_choice.strip().lower() == "equipment" or \
                player_choice.strip().lower() == "e":

            # skip equipment category and just print the actual equipment from equipment list
            equipment = []
            for x in range(1, len(player.equipment), 2):
                equipment.append(player.equipment[x])
            print(f"\nYour current equipment: {equipment}")
            time.sleep(1)

        if player_choice.strip().lower() == "equipment extra" or player_choice.strip().lower() == "e e":
            print(f"\nYour current equipment: {player.equipment}")
            time.sleep(1)

        if player_choice.strip().lower() == "check skills" or player_choice.strip().lower() == "skills" or \
                player_choice.strip().lower() == "k":
            print(f"\nYour current skills: {player.skills}")
            time.sleep(1)

        if player_choice.strip().lower() == "check location" or player_choice.strip().lower() == "location" or \
                player_choice.strip().lower() == "l":
            print(f"\nYour current location: {player.x_coordinate, player.y_coordinate}")
            time.sleep(1)

        if player_choice.strip().lower() == "use item" or player_choice.strip().lower() == "item":
            print(f"\nYour current inventory: {player.inventory}")
            item_choice = input("\nWhat item would you like to use? (Type an item from your inventory): ")

            if item_choice.strip().lower() == "health potion" or item_choice.strip().lower() == "health":
                for item in player.inventory:
                    if item == "health potion":
                        player.inventory.remove(item)
                        player.health = player.health + 25

                        # player cannot heal over max health
                        if player.health > 100:
                            player.health = 100

                        print("\nYou drink the health potion and heal for 25 hp.")
                        time.sleep(1)
                        break

            if item_choice.strip().lower() == "energy potion" or item_choice.strip().lower() == "energy":
                for item in player.inventory:
                    if item == "energy potion":
                        player.inventory.remove(item)
                        player.energy = player.energy + 25

                        # player cannot energize over max energy
                        if player.energy > 100:
                            player.energy = 100

                        print("\nYou drink the energy potion and energy for 25 ep.")
                        time.sleep(1)
                        break

        if player_choice.strip().lower() == "check status" or player_choice.strip().lower() == "status" or \
                player_choice.strip().lower() == "s":
            print(f"\nYour current status: "
                  f"name: {player.name}, race: {player.race}, gender: {player.gender}, role: {player.role}"
                  f"\nhealth: {player.health}, energy: {player.energy}, "
                  f"level: {player.level}, experience: {player.experience}, rupees: {player.rupees}")
            time.sleep(1)

        if player_choice.strip().lower() == "exit game" or player_choice.strip().lower() == "exit":
            print("\n\n\n\n"
                  "---------------------------------------------------------------------------------------------------"
                  "---")
            print(f"| * Thanks for playing!                                                                           "
                  f"   |")
            print("---------------------------------------------------------------------------------------------------"
                  "---\n\n\n\n")
            exit()

        if player_choice.strip().lower() == "check quest" or player_choice.strip().lower() == "quest" or \
                player_choice.strip().lower() == "q":
            print(f"\nYour current quest: [{player.quest}] status: [{player.quest_status} / 4]")
            time.sleep(1)

    return


# ----------------------------------------------------------------------------------------------------------------------
# current game start ---------------------------------------------------------------------------------------------------


game_run(default_character, all_enemies, all_npcs, all_trees, all_water, all_buildings, all_paths)


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# object checks --------------------------------------------------------------------------------------------------------

def list_all_objects():
    for x in all_enemies:
        print(x)

    for x in all_npcs:
        print(x)

    for x in all_trees:
        print(x)

    return
