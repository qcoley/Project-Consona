# RPG-Lite Concept Scratch Code
# Intrinsic Q


# npc classes ----------------------------------------------------------------------------------------------------------
import random
import time


class Player:

    def __init__(self, name, gender, race, role, inventory, equipment, quest_items, statistics, skills, level,
                 experience, health, energy, x_coordinate, y_coordinate, alive_status):
        self.name = name
        self.gender = gender
        self.race = race
        self.role = role
        self.inventory = inventory
        self.equipment = equipment
        self.quest_items = quest_items
        self.statistics = statistics
        self.skills = skills
        self.level = level
        self.experience = experience
        self.health = health
        self.energy = energy

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self.alive_status = alive_status


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

    def __init__(self, name, gender, race, role, dialog, quest, x_coordinate, y_coordinate, alive_status,
                 quest_complete, items):
        self.name = name
        self.gender = gender
        self.race = race
        self.role = role
        self.dialog = dialog
        self.quest = quest

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self.alive_status = alive_status
        self.quest_complete = quest_complete

        self.items = items


class Welcome:

    def __init__(self, message, shown):
        self.message = message
        self.shown = shown


class Tree:

    def __init__(self, name, model, x_coordinate, y_coordinate):
        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


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


# ----------------------------------------------------------------------------------------------------------------------
# character creator ----------------------------------------------------------------------------------------------------
# default character
default_character = Player("Intrinsic", "male", "sorae", "mage",  # name, gender, race, role
                           ["doritos", "health potion", "energy potion"],  # inventory
                           ["magic", "staff", "light", "fancy robes"],  # equipment ('type', 'name')
                           ["none"],  # quest items
                           ["vitality", 1, "intellect", 3, "strength", 1, "wisdom", 2],  # stats ('stat', 'amount')
                           ["beat boxing", "fire ball", "polymorph"], 1, 0, 100, 100,
                           # skills, lvl, exp, health, energy
                           1, 1, True)  # x-coordinate, y-coordinate, alive status

character_list = [default_character]

# enemies --------------------------------------------------------------------------------------------------------------
# basic enemy (kind, health, energy, level, x-coordinate, y-coordinate, alive status, inventory)
snake_1 = Enemy("snake", 100, 100, 1, 3, 12, True, "shiny rock")
snake_2 = Enemy("snake", 100, 100, 2, 4, 11, True, "shiny rock")
snake_3 = Enemy("snake", 100, 100, 3, 2, 10, True, "shiny rock")
snake_4 = Enemy("snake", 100, 100, 1, 3, 9, True, "shiny rock")

ghoul_low_1 = Enemy("ghoul", 100, 100, 3, 16, 14, True, "bone dust")
ghoul_low_2 = Enemy("ghoul", 100, 100, 4, 17, 12, True, "bone dust")
ghoul_low_3 = Enemy("ghoul", 100, 100, 5, 17, 15, True, "bone dust")
ghoul_low_4 = Enemy("ghoul", 100, 100, 3, 16, 11, True, "bone dust")

all_enemies = [snake_1, snake_2, snake_3, snake_4, ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4]

# npcs -----------------------------------------------------------------------------------------------------------------
# basic npc (name, gender, race, role, dialog, quest, x-coordinate, y-coordinate, alive status, quest complete)
npc_1 = NPC("Garon", "male", "nuldar", "rogue", "It's dangerous to go alone.", "Take This", 4, 4, True, False,
            ["Items to be added for thief steal"])
npc_2 = NPC("Celeste", "female", "sorae", "mage", "Please help Nede... ", "My Companion", 32, 34, True, False,
            ["Items to be added for thief steal"])
npc_3 = NPC("Artherian", "male", "amuna", "fighter", "By the light!", "Draconic Dreads", 28, 18, True, False,
            ["Items to be added for thief steal"])

guard_1 = NPC("Amuna Guard", "male", "amuna", "fighter", "Another day", "ID Check", 12, 17, True, False,
              ["Items to be added for thief steal"])
guard_2 = NPC("Amuna Guard", "male", "amuna", "fighter", "Another day", "ID Check", 13, 17, True, False,
              ["Items to be added for thief steal"])

all_npcs = [npc_1, npc_2, npc_3, guard_1, guard_2]

# trees ----------------------------------------------------------------------------------------------------------------
# any tree (name, model, x-coordinate, y-coordinate)
tree_1 = Tree("Pine tree", "tree", 4, 6)
tree_2 = Tree("Pine tree", "tree", 5, 2)
rock_1 = Tree("Pine tree", "tree", 2, 4)

all_trees = [tree_1, tree_2, rock_1]

# water ----------------------------------------------------------------------------------------------------------------
# water filler (name, model, x-coordinate, y-coordinate)
water_1 = Water("River", "water", 1, 18)
water_2 = Water("River", "water", 2, 18)
water_3 = Water("River", "water", 3, 18)
water_4 = Water("River", "water", 4, 18)
water_5 = Water("River", "water", 5, 18)
water_6 = Water("River", "water", 6, 18)
water_7 = Water("River", "water", 7, 18)
water_8 = Water("River", "water", 8, 18)
water_9 = Water("River", "water", 9, 18)
water_10 = Water("River", "water", 10, 18)
water_11 = Water("River", "water", 11, 18)
water_12 = Water("River", "water", 14, 18)
water_13 = Water("River", "water", 15, 18)
water_14 = Water("River", "water", 16, 18)
water_15 = Water("River", "water", 17, 18)
water_16 = Water("River", "water", 18, 18)
water_17 = Water("River", "water", 19, 18)
water_18 = Water("River", "water", 20, 18)

all_water = [water_1, water_2, water_3, water_4, water_5, water_6, water_7, water_8, water_9, water_10, water_11,
             water_12, water_13, water_14, water_15, water_16, water_17, water_18]

# buildings ------------------------------------------------------------------------------------------------------------
# any tree (name, model, x-coordinate, y-coordinate)
building_1 = Building("Amuna Shop", "Shop", 16, 5)
building_2 = Building("Amuna Home", "House", 13, 4)
building_3 = Building("Amuna Home", "House", 14, 7)

tower_1 = Building("Amuna Tower", "Tower", 6, 16)
tower_2 = Building("Amuna Tower", "Tower", 9, 15)

wall_1 = Building("Castle Wall", "Wall", 19, 1)
wall_2 = Building("Castle Wall", "Wall", 19, 2)
wall_3 = Building("Castle Wall", "Wall", 19, 3)
wall_4 = Building("Castle Wall", "Wall", 19, 4)
wall_5 = Building("Castle Wall", "Wall", 19, 5)
wall_6 = Building("Castle Wall", "Wall", 19, 6)
wall_7 = Building("Castle Wall", "Wall", 19, 7)
wall_8 = Building("Castle Wall", "Wall", 19, 8)
wall_9 = Building("Castle Wall", "Wall", 19, 9)
wall_10 = Building("Castle Wall", "Wall", 19, 10)
wall_11 = Building("Castle Wall", "Wall", 19, 11)
wall_12 = Building("Castle Wall", "Wall", 19, 12)
wall_13 = Building("Castle Wall", "Wall", 19, 13)
wall_14 = Building("Castle Wall", "Wall", 19, 14)
wall_15 = Building("Castle Wall", "Wall", 19, 15)
wall_16 = Building("Castle Wall", "Wall", 19, 16)
wall_17 = Building("Castle Wall", "Wall", 19, 17)
wall_18 = Building("Castle Wall", "Wall", 19, 18)

all_buildings = [building_1, building_2, building_3, tower_1, tower_2, wall_1, wall_2, wall_3, wall_4, wall_5,
                 wall_6, wall_7, wall_8, wall_9, wall_10, wall_11, wall_12, wall_13, wall_14, wall_15, wall_16,
                 wall_17, wall_18]

# welcome message ------------------------------------------------------------------------------------------------------
# False = hasn't been shown to the player yet. Once true it will not continue to show
greeting = Welcome("\n\n*** Welcome to RPG-Lite! [Version 0.1A] ***", False)


# ----------------------------------------------------------------------------------------------------------------------
# gameplay functions ---------------------------------------------------------------------------------------------------
def create_a_character():
    print("\n\n\n*** Character creator ***")

    # allows the player to create their own character. Stats and skills assigned based on chosen role.
    created_character = Player("name", "gender", "race", "role", "inventory", "equipment", "quest item", "stats",
                               "skills", "level", "xp", "health", "energy", "x-coordinate", "y-coordinate", True)

    my_name = input("\nWhat would you like your character's name to be? (Type a name): ")
    created_character.name = my_name.strip()

    my_gender = input("\nWhat would you like your character's gender to be? (Type a gender): ")
    created_character.gender = my_gender.strip().lower()

    # chosen_race = False means player has not chosen race yet and will continue to offer option until
    # race has been chosen, then it will set to true and continue with the creator tool
    chosen_race = False
    while not chosen_race:
        my_race = input(
            "\nWhat would you like your character's race to be? (Type a race, or, type info for race lore): ")
        if my_race.strip().lower() == "information" or my_race.strip().lower() == "info" or my_race.strip().lower() == "lore":

            print(
                "\n---------------------------------------- Race Lore ------------------------------------------------")
            print("\nAmuna: A well-rounded people. The Amuna seek knowledge and wish to grow, but most use this to "
                  "\nsatisfy their own needs. A becoming race, proven to be strong and able to adapt well to their "
                  "\nsurroundings. They often bicker amongst themselves, for the years of curiosity and exploring "
                  "\nthe outer reaches of their world have grown them to be large and diverse. It is for this reason \n"
                  "that a new generation has started a trend of bringing their peoples together, so that they may\ncontinue "
                  "to thrive amongst the coming chaos. * Associated with the element of water for their \nvast potential "
                  "as limitless as the oceans surrounding their world. However, the Amuna also \nhave the "
                  "tendency to change much like the shifting of the tides. This can be a boon if the\nsituation warrants, "
                  "but this instability can also put them in harm's way. The Amuna’s\ncohesiveness has proven to be "
                  "their greatest strength if they can come together to realize\nand grasp their shared fate. "
                  "\n\nSorae: Mysterious and wise, the Sorae are not well understood by most other races. But this "
                  "is \nfine with them. As an Eldar race, they view themselves as caretakers and shepherds, "
                  "guiding\nthe new races of the realm or any beings they may see as troubled. Although, this "
                  "quality\nwhile inherently good in nature can also lead to a sense of arrogance and "
                  "condescension amongst\nthem. The Sorae must be cautious to not allow this to hinder them, as there "
                  "is much they can\nstill learn from others. * The Sorae are associated with the element of earth "
                  "and all the nature\nof which inhabits it. They can be very self-sufficient, much as the plant "
                  "life surrounding their\nworld can produce its own source of energy. But when "
                  "combined with others they can be much \nstronger for it. "
                  "\n\nNuldar: A hearty race, strong and fierce. The Nuldar do not seek to pass time idle thinking "
                  "of \nthings, for they would rather act and make a difference that they can see and feel. They \nare "
                  "well grounded in their beliefs and hold fast to their strong bonds with family and friends. \nThis "
                  "can cause issues to arise, as they are resistant to change even if it could prove beneficial. "
                  "\nThey are quick to judge and slow to trust, a result of the hardships they have endured in the "
                  "\nred world of Rohir. * The Nuldar are associated with the element of fire. They burn bright and\nhave "
                  "forged themselves as diamonds in the flames of their often-difficult lives. "
                  "They must take \ncare not to allow their flames to be extinguished by keeping their hearts close "
                  "and \nwell guarded by their tough spirits. ")
            print(
                "\n---------------------------------------------------------------------------------------------------")

        # player did not choose to read race lore or has read it and made a choice. sets chosen_race to true
        else:
            if my_race.strip().lower() == "amuna" or my_race.strip().lower() == "amu":
                created_character.race = "amuna"
                chosen_race = True

            if my_race.strip().lower() == "sorae" or my_race.strip().lower() == "sor":
                created_character.race = "sorae"
                chosen_race = True

            if my_race.strip().lower() == "nuldar" or my_race.strip().lower() == "nul":
                created_character.race = "nuldar"
                chosen_race = True

    # chosen_role = False means player has not chosen role yet and will continue to offer option until
    # role has been chosen, then it will set to true and continue with the creator tool
    chosen_role = False
    while not chosen_role:
        my_role = input(
            "\nWhat would you like your character's role to be? (Type a role, or, type info for role lore): ")
        if my_role.strip().lower() == "information" or my_role.strip().lower() == "info" or my_role.strip().lower() == "lore":

            print(
                "\n---------------------------------------- Role Lore ------------------------------------------------")
            print("\nFighter: The warrior type role. Fighters have more vitality than the other roles, making them "
                  "\nsignificantly tankier. However, they have less intelligence than the mage role and less strength\n"
                  "than the rogue role. Fighters work best with a 2-handed weapon equipped. "
                  "\n\nMage: The magic type role. Mages have more intellect and wisdom than other roles, making them"
                  "\nhave higher energy pools. However, they have less vitality than the fighter role and less strength "
                  "\nthan the rogue role. Mages work best with a magic type weapon equipped. "
                  "\n\nRogue: The thief type role. Rogues have a high strength stat and will do more damage than other"
                  "\nroles in melee combat. However, they have less vitality than the fighter role and"
                  " less intellect\nthan the mage role. Rogues work best with a 1-handed weapon equipped. ")
            print(
                "\n---------------------------------------------------------------------------------------------------")

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
            created_character.equipment = ["2H", "", "heavy", ""]
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
            created_character.equipment = ["magic", "", "light", ""]
            created_character.statistics = ["vitality", 1, "intellect", 3, "strength", 1, "wisdom", 2]
            created_character.skills = ["fireball", ""]  # polymorph 2nd
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
            created_character.equipment = ["1H", "", "medium", ""]
            created_character.statistics = ["vitality", 2, "intellect", 1, "strength", 3, "wisdom", 1]
            created_character.skills = ["back stab", ""]  # steal 2nd
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
    if player.level < 11:
        if player.role == "fighter":
            player.statistics[1] = player.statistics[1] + 3  # vitality
            player.statistics[3] = player.statistics[3] + 1  # intellect
            player.statistics[5] = player.statistics[5] + 2  # strength
            player.statistics[7] = player.statistics[7] + 1  # wisdom
            player.level = player.level + 1

            # vitality increases player health
            player.health = player.health + player.statistics[1]
            # intellect increases player energy
            player.energy = player.energy + player.statistics[3]

            print(f"\n*** Congrats, you leveled up! You are now level: {player.level} ***")
            print("*** In addition, as a fighter, your stats have been increased to: ***")
            print(f"*** {player.statistics} ***")

            return player.level

        if player.role == "mage":
            player.statistics[1] = player.statistics[1] + 1  # vitality
            player.statistics[3] = player.statistics[3] + 2  # intellect
            player.statistics[5] = player.statistics[5] + 1  # strength
            player.statistics[7] = player.statistics[7] + 3  # wisdom
            player.level = player.level + 1

            # vitality increases player health
            player.health = player.health + player.statistics[1]
            # intellect increases player energy
            player.energy = player.energy + player.statistics[3]

            print(f"\n*** Congrats, you leveled up! You are now level: {player.level} ***")
            print("*** In addition, as a mage, your stats have been increased to: ***")
            print(f"*** {player.statistics} ***")

            return player.level

        if player.role == "rogue":
            player.statistics[1] = player.statistics[1] + 2  # vitality
            player.statistics[3] = player.statistics[3] + 1  # intellect
            player.statistics[5] = player.statistics[5] + 3  # strength
            player.statistics[7] = player.statistics[7] + 1  # wisdom
            player.level = player.level + 1

            # vitality increases player health
            player.health = player.health + player.statistics[1]
            # intellect increases player energy
            player.energy = player.energy + player.statistics[3]

            print(f"\n*** Congrats, you leveled up! You are now level: {player.level} ***")
            print("*** In addition, as a rogue, your stats have been increased to: ***")
            print(f"*** {player.statistics} ***")

            return player.level

    else:
        print("\n You're already at max level! (Level 10)")
        return player.level


def attack_enemy(player, enemy):
    # fighters do more damage with 2-handed weapons -------------------------
    if player.role == "fighter":
        if player.equipment[0] == "2H":
            damage = (random.randrange(25, 50) // enemy.level)

            # includes player strength stat to scale overall damage
            stat_scale = damage * player.statistics[5]

            return stat_scale

        else:
            damage = (random.randrange(0, 5) // enemy.level)
            print("\n*** You may have an incorrect weapon type equipped! ***")

            return damage

    # mages do more damage with magic weapons --------------------------------
    if player.role == "mage":
        if player.equipment[0] == "magic":
            damage = (random.randrange(25, 50) // enemy.level)

            # includes player wisdom stat to scale overall damage
            stat_scale = (damage * player.statistics[7]) // 2

            return stat_scale

        else:
            damage = (random.randrange(0, 5) // enemy.level)
            print("\n*** You may have an incorrect weapon type equipped! ***")

            return damage

    # rogues do more damage with 1-handed weapons ----------------------------
    if player.role == "rogue":
        if player.equipment[0] == "1H":
            damage = (random.randrange(25, 50) // enemy.level)

            # includes player strength stat to scale overall damage (strength will be higher for rogues)
            stat_scale = damage * player.statistics[5]

            return stat_scale

        else:
            damage = (random.randrange(0, 5) // enemy.level)
            print("\n*** You may have an incorrect weapon type equipped! ***")

            return damage


def attack_player(enemy, player):
    if enemy.kind == "snake":
        base_damage = (random.randrange(10, 30) // player.level)

        if player.equipment[2] == "heavy":
            final_damage = base_damage - 15

            return final_damage

        if player.equipment[2] == "light":
            final_damage = base_damage - 5

            return final_damage

        if player.equipment[2] == "medium":
            final_damage = base_damage - 10

            return final_damage

    if enemy.kind == "ghoul":
        base_damage = (random.randrange(20, 30) // player.level)

        if player.equipment[2] == "heavy":
            final_damage = base_damage - 15

            return final_damage

        if player.equipment[2] == "light":
            final_damage = base_damage - 5

            return final_damage

        if player.equipment[2] == "medium":
            final_damage = base_damage - 10

            return final_damage


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
                else:
                    print("\n*** There appears to be a tree here blocking your way.. ***")
                    print(f"\n*** The tree is: {tree_found.name} ***")
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
                else:
                    print("\n*** There appears to be a tree here blocking your way.. ***")
                    print(f"\n*** The tree is: {tree_found.name} ***")
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
                else:
                    print("\n*** There appears to be a tree here blocking your way.. ***")
                    print(f"\n*** The tree is: {tree_found.name} ***")
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
                else:
                    print("\n*** There appears to be a tree here blocking your way.. ***")
                    print(f"\n*** The tree is: {tree_found.name} ***")
            else:
                print("\n*** There appears to be a body of water blocking your way.. maybe "
                      "there's a way around it? ***")
                print(f"\n*** The tree is: {water_found.name} ***")
        else:
            print("\n*** You can't move any further right! ***")


def draw_map(player, enemy_list, npc_list, tree_list, water_list, building_list):
    print("\n")
    current_map = []

    # player is in screen one, set boundaries to draw screen one -------------------------------------------------------
    if player.x_coordinate < 20 and player.y_coordinate < 20:

        for y in range(20):  # draw screen one -------------------------------------------------------------------------

            current_row = []
            current_map.append(current_row)

            for x in range(20):
                current_row.append("_")

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
                current_row.append("=")

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
    current_map.reverse()
    for i in range(1, len(current_map) - 1):
        print(current_map[i])

    print("\n*** Map guide: O = player, X = enemy, N = npc, T = tree, W = water, B = building, '_' = ground ***")
    time.sleep(1)
    return


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# scenarios ------------------------------------------------------------------------------------------------------------

def attack_scenario(player, enemy):

    # Verifies player is still in range of enemy
    if player.x_coordinate == enemy.x_coordinate and player.y_coordinate == enemy.y_coordinate:

        print("\n-----------------------------------------------------------------------------------------------------")
        combat_choice = input("What do you want to do? (Attack or Run): ")

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
                    attacked_player = attack_player(enemy, player)
                    if attacked_player is not None and attacked_player > 0:
                        print(f'\nOuch! The {enemy.kind} retaliates and damages you for {attacked_player}.')
                        player.health = player.health - attacked_player
                        time.sleep(1)

                        if player.health > 0:
                            print(f"\nYour health is now: {player.health}/100.")
                            time.sleep(1)
                            attack_scenario(player, enemy)

                        else:  # your health is zero and you're dead
                            print("\n*** Oh dear, you are dead... ***")
                            player.alive_status = False
                            time.sleep(1)
                            print("\n\n-----------------------------------------"
                                  "------------------------------------------------------------")
                            print("-------------------------------------- Game over, try again! "
                                  "----------------------------------------")
                            print("-----------------------------------------"
                                  "------------------------------------------------------------")
                            time.sleep(1)
                            exit()

                    else:
                        print(f'\nThe {enemy.kind} attempted to retaliate, but missed and did no damage!')
                        time.sleep(1)
                        attack_scenario(player, enemy)

                # enemy has been defeated, will return an amount of xp based on current levels
                else:
                    experience = int((enemy.level / player.level) * 10)
                    player.experience = player.experience + experience
                    print(f"\nYou killed the {enemy.kind} and gained {experience} experience!\n")
                    print(f"Your current experience is {player.experience}/100")
                    time.sleep(1)

                    # player will level up (see level up method)
                    if player.experience > 100:
                        level_up(player)

                    enemy.alive_status = False
                    time.sleep(1)

            else:
                print("\nThis enemy appears to be dead already!")

        if combat_choice.strip().lower() == "run" or combat_choice.strip().lower() == "r":

            escape_chance = random.randrange(35, 75)
            if escape_chance > 50:

                print("\nYou escaped safely, nice!")
                player.x_coordinate = player.x_coordinate + 1
                player.y_coordinate = player.y_coordinate + 1
                print(f"\nYour new position coordinates are {player.x_coordinate, player.y_coordinate}")
                attack_scenario(player, enemy)

            else:
                print(f"\nThe {enemy.kind} blocked your escape!")
                time.sleep(1)
                attack_scenario(player, enemy)

        else:
            if enemy.alive_status:
                attack_scenario(player, enemy)

    else:
        return


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# run stuff ------------------------------------------------------------------------------------------------------------

# basic game run command, can take any player, enemy and npc as parameters
def game_run(player, enemies, npcs, trees, water, buildings):
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
                        print(f'\n\n*** You encounter an enemy {enemy.kind}, level {enemy.level} ***')
                        attack_scenario(player, enemy)

        # if player is in range of npc (to do create dialog/quest from npc in the scenarios section)
        for npc in npcs:
            if player.x_coordinate == npc.x_coordinate:
                if player.y_coordinate == npc.y_coordinate:

                    if npc.alive_status:
                        print(f'\n\n*** You meet an npc {npc.name} ***')
                        # npc_scenario(player, npc)

        print("\n\n---------------------------------------------------------------------------------------------------")
        print("Actions: Check Status, Check Inventory, Check Equipment, Check Skills, Check Location, Check Quests")
        print("         Move, Draw Map, Use item, Use skill, Hotkeys, How to Play, Exit Game")
        print("---------------------------------------------------------------------------------------------------")
        player_choice = input("\nWhat would you like to do? (Type an action): ")

        if player_choice.strip().lower() == "how to play" or player_choice.strip().lower() == "how" or \
                player_choice.strip().lower() == "play" or player_choice.strip().lower() == "help":
            print("\nYour character is on an adventure! The world is open to you to explore freely, so look"
                  " around and \nsee what you can find. Currently all actions are based on text input from"
                  " the user entered into \nthe console. \n\nUpon reaching the action screen, just type the command"
                  " corresponding to the action\nyou would like your character to perform next. For example, to move"
                  " up on the map, type 'move'\nand hit enter. Once in the move menu type 'up' to go up. Following this"
                  " action you will be returned \nto the main action screen where you can perform more character commands."
                  "\n\nTo see where your character is currently located in the world, type 'draw map' or 'draw' and "
                  "\nthe game will print out a current rendition of the game world to the console, including nearby"
                  "\nenemies and npcs. Pay attention to the map guide to see what each symbol on the map stands for. "
                  "\n\nTry talking to some nearby NPCs and see if they have any information or quests to give you! \nOr,"
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

        if player_choice.strip().lower() == "move" or player_choice.strip().lower() == "m":

            player_direction = input("\nWhich direction would you like to move in? (Type up, down, left or right): ")

            # allow player to move if not in range of enemy (combat check)
            if player.x_coordinate != [enemy.x_coordinate for enemy in enemies] or \
                    player.y_coordinate != [enemy.y_coordinate for enemy in enemies]:
                player_move(player, player_direction, water, trees, buildings)

        if player_choice.strip().lower() == "draw map" or player_choice.strip().lower() == "draw" or \
                player_choice.strip().lower() == "d":
            draw_map(player, enemies, npcs, trees, water, buildings)

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

                        print("\n*** You drink the health potion and heal for 25 hp! ***")
                        time.sleep(1)
                        break

        if player_choice.strip().lower() == "check status" or player_choice.strip().lower() == "status" or \
                player_choice.strip().lower() == "s":
            print(f"\nYour current status: "
                  f"name: {player.name}, race: {player.race}, gender: {player.gender}, role: {player.role}"
                  f"\nhealth: {player.health}, energy: {player.energy}, "
                  f"level: {player.level}, experience: {player.experience}")
            time.sleep(1)

        if player_choice.strip().lower() == "exit game" or player_choice.strip().lower() == "exit":
            print(f"\n\n*** Thanks for playing! ***\n\n")
            exit()

    return


# ----------------------------------------------------------------------------------------------------------------------
# current game start ---------------------------------------------------------------------------------------------------

# my_character = create_character()
# create an enemy and npc list for multiple situations (currently only supports 1 enemy and 1 npc)

game_run(default_character, all_enemies, all_npcs, all_trees, all_water, all_buildings)


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
