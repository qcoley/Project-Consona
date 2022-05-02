import random
import time
import pygame
from pygame.locals import *

import resource_urls
import drawing_functions

# global variables -----------------------------------------------------------------------------------------------------
ACC = 0.20  # acceleration
FRIC = -0.20  # friction
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
vec = pygame.math.Vector2


# ----------------------------------------------------------------------------------------------------------------------
# class objects --------------------------------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, name, gender, race, role, items, p_equipment, current_quests, quest_progress, quest_status,
                 quest_complete, knowledge, skills_mage, skills_fighter, skills_scout, level, experience, health,
                 energy, alive_status, rupees, reputation, mount, current_zone, defence, offense, image):
        super(Player, self).__init__()
        self.surf = image
        self.rect = self.surf.get_rect()
        self.pos = vec((450, 650))
        # velocity and acceleration vectors for movement physics
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.name = name
        self.gender = gender
        self.race = race
        self.role = role
        self.items = items
        self.equipment = p_equipment
        self.current_quests = current_quests
        self.quest_progress = quest_progress
        self.quest_status = quest_status
        self.quest_complete = quest_complete
        self.knowledge = knowledge
        self.skills_mage = skills_mage
        self.skills_fighter = skills_fighter
        self.skills_scout = skills_scout
        self.level = level
        self.experience = experience
        self.health = health
        self.energy = energy
        self.alive_status = alive_status
        self.rupees = rupees
        self.reputation = reputation
        self.mount = mount
        self.current_zone = current_zone
        self.defence = defence
        self.offense = offense

    # move the character sprite based on key presses
    def update(self, pressed_keyes, current_zone):
        # setting acceleration vector on player update frame
        self.acc = vec(0, 0)
        # control acceleration based on user keys pressed from input parameter -----------------------------------------
        if pressed_keyes[K_w]:
            if player.race == "amuna":
                if player.role == "mage":
                    self.surf = player_mage_up
                if player.role == "fighter":
                    self.surf = player_fighter_up
                if player.role == "scout":
                    self.surf = player_scout_up
                if player.role == "":
                    self.surf = player_no_role_amuna_up
            if player.race == "sorae":
                if player.role == "mage":
                    self.surf = player_mage_up
                if player.role == "fighter":
                    self.surf = player_fighter_up
                if player.role == "scout":
                    self.surf = player_scout_up
                if player.role == "":
                    self.surf = player_no_role_sorae_up

            self.acc.y = -ACC

        if pressed_keyes[K_s]:
            if player.race == "amuna":
                if player.role == "mage":
                    self.surf = player_mage_down
                if player.role == "fighter":
                    self.surf = player_fighter_down
                if player.role == "scout":
                    self.surf = player_scout_down
                if player.role == "":
                    self.surf = player_no_role_amuna_down
            if player.race == "sorae":
                if player.role == "mage":
                    self.surf = player_mage_down
                if player.role == "fighter":
                    self.surf = player_fighter_down
                if player.role == "scout":
                    self.surf = player_scout_down
                if player.role == "":
                    self.surf = player_no_role_sorae_down

            self.acc.y = ACC

        if pressed_keyes[K_a]:
            if player.race == "amuna":
                if player.role == "mage":
                    self.surf = player_mage_left
                if player.role == "fighter":
                    self.surf = player_fighter_left
                if player.role == "scout":
                    self.surf = player_scout_left
                if player.role == "":
                    self.surf = player_no_role_amuna_left
            if player.race == "sorae":
                if player.role == "mage":
                    self.surf = player_mage_left
                if player.role == "fighter":
                    self.surf = player_fighter_left
                if player.role == "scout":
                    self.surf = player_scout_left
                if player.role == "":
                    self.surf = player_no_role_sorae_left

            self.acc.x = -ACC

        if pressed_keyes[K_d]:
            if player.race == "amuna":
                if player.role == "mage":
                    self.surf = player_mage_right
                if player.role == "fighter":
                    self.surf = player_fighter_right
                if player.role == "scout":
                    self.surf = player_scout_right
                if player.role == "":
                    self.surf = player_no_role_amuna_right
            if player.race == "sorae":
                if player.role == "mage":
                    self.surf = player_mage_right
                if player.role == "fighter":
                    self.surf = player_fighter_right
                if player.role == "scout":
                    self.surf = player_scout_right
                if player.role == "":
                    self.surf = player_no_role_sorae_right
            self.acc.x = ACC

        # --------------------------------------------------------------------------------------------------------------
        # Keep player on the screen, boundaries vary depending on current zone -----------------------------------------
        if current_zone == "seldon" or current_zone == "korlok":
            if self.pos.x < 25:
                self.pos.x = 25
            elif self.pos.x > SCREEN_WIDTH - 355:
                self.pos.x = SCREEN_WIDTH - 355
            if self.pos.y <= 115:
                self.pos.y = 115
            elif self.pos.y >= SCREEN_HEIGHT - 5:
                self.pos.y = SCREEN_HEIGHT - 5

        # equations and update player movement based on vectors --------------------------------------------------------
        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        # collision detection with environment objects (trees, buildings, etc) -----------------------------------------
        if pygame.sprite.spritecollide(player, environment_objects, False, pygame.sprite.collide_rect_ratio(0.50)):
            # create normal force by applying velocity opposite direction player is trying to move on colliding
            if pressed_keyes[K_w]:
                player.vel.y = + .46
            if pressed_keyes[K_s]:
                player.vel.y = - .46
            if pressed_keyes[K_a]:
                player.vel.x = + .46
            if pressed_keyes[K_d]:
                player.vel.x = - .46


class NPC(pygame.sprite.Sprite):
    def __init__(self, name, gender, race, role, dialog, quest_to_give, quest_description, x_coordinate, y_coordinate,
                 alive_status, quest_complete, items, gift, image):
        super(NPC, self).__init__()
        self.name = name
        self.gender = gender
        self.race = race
        self.role = role
        self.dialog = dialog
        self.quest_to_give = quest_to_give
        self.quest_description = quest_description
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.alive_status = alive_status
        self.quest_complete = quest_complete
        self.items = items
        self.gift = gift
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, image):
        self.surf = image


class Shopkeeper(pygame.sprite.Sprite):
    def __init__(self, name, race, items):
        super(Shopkeeper, self).__init__()
        self.name = name
        self.race = race
        self.items = items


class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image,
                 health_bar):
        super(Enemy, self).__init__()
        self.name = name
        self.kind = kind
        self.health = health
        self.energy = energy
        self.level = level
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.alive_status = alive_status
        self.items = items
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.speed = 1
        self.health_bar = health_bar

    # update separate into 2 functions to handle image updates and position updates
    # so that they both don't need the same parameters to change one or the other in main interation
    def update_image(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))

    # update separate into 2 functions to handle image updates and position updates
    # so that they both don't need the same parameters to change one or the other in main interation
    def update_position(self, ranges_x, ranges_y, direction_x, direction_y):
        # movement on map ----------------------------------------------------------------------------------------------
        if ranges_x[0] < self.rect.x < ranges_x[1]:
            if direction_x == "left":
                self.rect.move_ip(-1, 0)
            if direction_x == "right":
                self.rect.move_ip(1, 0)
        else:
            if direction_x == "left":
                self.rect.move_ip(1, 0)
            if direction_x == "right":
                self.rect.move_ip(-1, 0)
        if ranges_y[0] < self.rect.x < ranges_y[1]:
            if direction_y == "down":
                self.rect.move_ip(0, -1)
            if direction_y == "up":
                self.rect.move_ip(0, 1)
        else:
            if direction_y == "down":
                self.rect.move_ip(0, 1)
            if direction_y == "up":
                self.rect.move_ip(0, -1)


class Tree(pygame.sprite.Sprite):
    def __init__(self, name, model, x_coordinate, y_coordinate, gathered, image):
        super(Tree, self).__init__()
        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.gathered = gathered
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


class Building(pygame.sprite.Sprite):
    def __init__(self, name, model, x_coordinate, y_coordinate, image):
        super(Building, self).__init__()
        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# any UI element like buttons, bars, status etc.
class UiElement(pygame.sprite.Sprite):
    def __init__(self, name, x_coordinate, y_coordinate, image, update_flag):
        super(UiElement, self).__init__()
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.update_flag = update_flag

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


class Inventory(pygame.sprite.Sprite):
    def __init__(self, name, contains, x_coordinate, y_coordinate, image, update_flag):
        super(Inventory, self).__init__()
        self.name = name
        self.contains = contains
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.update_flag = update_flag

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# pop up notifications, like the welcome screen image when game starts
class Notification(pygame.sprite.Sprite):
    def __init__(self, name, shown, x_coordinate, y_coordinate, image):
        super(Notification, self).__init__()
        self.name = name
        self.shown = shown
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# to create a representation of character for battle screen
class BattleCharacter(pygame.sprite.Sprite):
    def __init__(self, name, x_coordinate, y_coordinate, image):
        super(BattleCharacter, self).__init__()
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


class Item(pygame.sprite.Sprite):
    def __init__(self, name, type, x_coordinate, y_coordinate, image):
        super(Item, self).__init__()
        self.name = name
        self.type = type
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
        self.sprite_sheet.set_colorkey((255, 255, 255), RLEACCEL)

    def get_image(self, x, y, width, height):
        sprite_image = pygame.Surface([width, height], pygame.SRCALPHA)
        sprite_image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return sprite_image


# gameplay functions ---------------------------------------------------------------------------------------------------
def attack_scenario(enemy_combating, combat_event):
    # get the all the stuff that happened in this scenario and return it to main loop via dictionary keys and values
    combat_event_dictionary = {
        "damage done": 0,
        "damage taken": 0,
        "item dropped": "",
        "experience gained": 0,
        "quest update": "",
        "enemy defeated": False,
        "escaped": False,
        "level up status": "",
        "level up attributes": ""
    }
    if combat_event == "attack":
        if enemy_combating.alive_status:
            # returns players damage to the enemy based on level and equipment
            attacked_enemy_health = attack_enemy(enemy_combating)
            enemy_combating.health = enemy_combating.health - attacked_enemy_health
            try:
                enemy_combating.health_bar.update(enemy_combating.health_bar.x_coordinate,
                                                  enemy_combating.health_bar.y_coordinate,
                                                  health_bar_update(enemy_combating))
            except AttributeError:
                pass

            # if enemy is not dead yet
            if enemy_combating.health > 0:
                attacked_enemy_string = f" You did {attacked_enemy_health} damage to {enemy_combating.name}."
                # add damage to enemy to event dictionary to be returned to main loop ----------------------------------
                combat_event_dictionary["damage done"] = attacked_enemy_string
                # returns total damage output from enemy as attacked_player_health value
                attacked_player_health = attack_player(enemy_combating)
                if attacked_player_health > 0:
                    attacked_player_string = f"You take {attacked_player_health} damage from {enemy_combating.name}."
                    player.health = player.health - attacked_player_health
                    # add damage done to player from enemy to dictionary -----------------------------------------------
                    combat_event_dictionary["damage taken"] = attacked_player_string

                    # enemy has defeated player, game over
                    if player.health <= 0:
                        player.alive_status = False
                    return combat_event_dictionary
                else:
                    enemy_miss_string = f'{enemy_combating.name} missed.'
                    # add to dictionary that enemy did no damage to player ---------------------------------------------
                    combat_event_dictionary["damage taken"] = enemy_miss_string
                    return combat_event_dictionary

            # ----------------------------------------------------------------------------------------------------------
            # enemy has been defeated, will return an amount of xp based on current levels -----------------------------
            else:
                # quest checks -----------------------------------------------------------------------------------------
                # if player is on quest to kill snakes
                if enemy_combating.kind == "snake":
                    if player.quest_status["sneaky snakes"]:
                        if player.quest_progress["sneaky snakes"] < 4:
                            player.quest_progress["sneaky snakes"] = player.quest_progress["sneaky snakes"] + 1
                            quest_string = f"{player.quest_progress['sneaky snakes']}/4 snakes"
                            # add to dictionary player quest updates if enemy was an objective of quest for player -
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill ghouls
                if enemy_combating.kind == "ghoul":
                    if player.quest_status["ghouled again"]:
                        if player.quest_progress["ghouled again"] < 4:
                            player.quest_progress["ghouled again"] = player.quest_progress["ghouled again"] + 1
                            quest_string = f"{player.quest_status['ghouled again']}/4 ghouls"
                            # add to dictionary player quest updates if enemy was an objective of quest for player -
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # ------------------------------------------------------------------------------------------------------
                # experienced gained by player from defeating enemy ----------------------------------------------------
                if player.level <= enemy_combating.level + 1:
                    experience = int((enemy_combating.level / player.level) * 25)
                    player.experience = player.experience + experience
                    enemy_experience = f"{experience} xp "
                    # add to dictionary experience given from defeating enemy ------------------------------------------
                    combat_event_dictionary["experience gained"] = enemy_experience

                drop_chance = random.randrange(1, 10)
                # ------------------------------------------------------------------------------------------------------
                # 80% chance to drop merchant item sellable by player for rupees at shops ------------------------------
                if drop_chance > 2:

                    # doesn't give item to player if their inventory is full
                    if len(player.items) < 16:
                        player.items.append(enemy_combating.items)
                        enemy_dropped_this = f"{enemy_combating.name} dropped [{enemy_combating.items.name}]."
                        # add to dictionary anything dropped from enemy upon their defeat ------------------------------
                        combat_event_dictionary["item dropped"] = enemy_dropped_this
                    else:
                        combat_event_dictionary["item dropped"] = "Item, but your inventory is full."
                else:
                    combat_event_dictionary["item dropped"] = "No"

                # player will level up (see level up method) -----------------------------------------------------------
                if player.experience >= 100:
                    level_up()

                enemy_combating.alive_status = False
                enemy_combating.kill()

                # add to dictionary True if enemy has been defeated so scenario will end -------------------------------
                combat_event_dictionary["enemy defeated"] = True
                return combat_event_dictionary
        else:
            print("\nThis enemy appears to be dead already!")

    # active combat skill, if player is fighter and has learned hard strike from the academia
    if combat_event == "skill 1":
        if player.role == "fighter":
            if hard_strike_learned:
                if enemy_combating.alive_status:
                    # returns players damage to the enemy based on level and equipment
                    striked = random.randrange(20, 40)  # hard strike damage
                    enemy_combating.health = enemy_combating.health - striked
                    try:
                        enemy_combating.health_bar.update(enemy_combating.health_bar.x_coordinate,
                                                          enemy_combating.health_bar.y_coordinate,
                                                          health_bar_update(enemy_combating))
                    except AttributeError:
                        pass

                    # if enemy is not dead yet
                    if enemy_combating.health > 0:
                        attacked_enemy_string = f"Hard strike did {striked} damage!"
                        # add damage to enemy to event dictionary to be returned to main loop --------------------------
                        combat_event_dictionary["damage done"] = attacked_enemy_string
                        # returns total damage output from enemy as attacked_player_health value
                        attacked_player_health = attack_player(enemy_combating)
                        if attacked_player_health > 0:
                            attacked_player_string = f"You take {attacked_player_health} damage from " \
                                                     f"{enemy_combating.name}."
                            player.health = player.health - attacked_player_health
                            # add damage done to player from enemy to dictionary ---------------------------------------
                            combat_event_dictionary["damage taken"] = attacked_player_string

                            # enemy has defeated player, game over
                            if player.health <= 0:
                                player.alive_status = False
                            return combat_event_dictionary
                        else:
                            enemy_miss_string = f'{enemy_combating.name} missed.'
                            # add to dictionary that enemy did no damage to player -------------------------------------
                            combat_event_dictionary["damage taken"] = enemy_miss_string
                            return combat_event_dictionary

                    # --------------------------------------------------------------------------------------------------
                    # enemy has been defeated, will return an amount of xp based on current levels ---------------------
                    else:
                        # ----------------------------------------------------------------------------------------------
                        # quest checks ---------------------------------------------------------------------------------
                        # if player is on quest to kill snakes
                        if enemy_combating.kind == "snake":
                            if player.quest_status["sneaky snakes"]:
                                if player.quest_progress["sneaky snakes"] < 4:
                                    player.quest_progress["sneaky snakes"] = player.quest_progress["sneaky snakes"] + 1
                                    quest_string = f"{player.quest_progress['sneaky snakes']}/4 snakes"
                                    # add to dictionary player quest updates if enemy was an objective of quest
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"

                        # if player is on quest to kill ghouls
                        if enemy_combating.kind == "ghoul":
                            if player.quest_status["ghouled again"]:
                                if player.quest_progress["ghouled again"] < 4:
                                    player.quest_progress["ghouled again"] = player.quest_progress["ghouled again"] + 1
                                    quest_string = f"{player.quest_status['ghouled again']}/4 ghouls"
                                    # add to dictionary player quest updates if enemy was an objective of quest
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"

                        # ----------------------------------------------------------------------------------------------
                        # experienced gained by player from defeating enemy --------------------------------------------
                        if player.level <= enemy_combating.level + 1:
                            experience = int((enemy_combating.level / player.level) * 35)
                            player.experience = player.experience + experience
                            enemy_experience = f"{experience} xp "
                            # add to dictionary experience given from defeating enemy ----------------------------------
                            combat_event_dictionary["experience gained"] = enemy_experience

                        drop_chance = random.randrange(1, 10)
                        # ----------------------------------------------------------------------------------------------
                        # 80% chance to drop merchant item sellable by player for rupees at shops ----------------------
                        if drop_chance > 2:

                            # doesn't give item to player if their inventory is full
                            if len(player.items) < 16:
                                player.items.append(enemy_combating.items)
                                enemy_dropped_this = f"{enemy_combating.name} dropped [{enemy_combating.items.name}]."
                                # add to dictionary anything dropped from enemy upon their defeat ----------------------
                                combat_event_dictionary["item dropped"] = enemy_dropped_this
                            else:
                                combat_event_dictionary["item dropped"] = "Item, but your inventory is full."
                        else:
                            combat_event_dictionary["item dropped"] = "No"

                        # player will level up (see level up method) ---------------------------------------------------
                        if player.experience >= 100:
                            level_up()

                        enemy_combating.alive_status = False
                        enemy_combating.kill()

                        # add to dictionary True if enemy has been defeated so scenario will end -----------------------
                        combat_event_dictionary["enemy defeated"] = True
                        return combat_event_dictionary
                else:
                    print("\nThis enemy appears to be dead already!")


# ----------------------------------------------------------------------------------------------------------------------
# player attacks enemy, gets damage to enemy done based on player's role and equipment ---------------------------------
def attack_enemy(mob):
    # if player is lower level than mob, scale their damage based on the difference of their levels
    if player.level < mob.level:
        difference = mob.level - player.level
    # if player is equal level or higher level than mob, just return full damage value
    else:
        difference = 1

    # scale damage based on player's offense stat and level difference
    if player.role == "mage":
        damage = (random.randrange(17, player.offense) // difference)
    if player.role == "scout":
        damage = (random.randrange(12, player.offense) // difference)
    if player.role == "fighter":
        damage = (random.randrange(7, player.offense) // difference)
    if player.role == "":
        damage = (random.randrange(1, 7) // difference)

    return damage


# ----------------------------------------------------------------------------------------------------------------------
# enemy attacks player, gets damage to player done, subtract players defense level (gear) ------------------------------
def attack_player(mob):
    difference = mob.level - player.level
    base_damage = (random.randrange(10, 18))

    # add additional damage if enemy is a higher level than player. the higher the level difference, the more damage ---
    if difference >= 1:
        base_damage = base_damage + 3
    if difference >= 2:
        base_damage = base_damage + 5
    if difference >= 3:
        base_damage = base_damage + 8

    final_damage = base_damage - player.defence

    return final_damage


# ----------------------------------------------------------------------------------------------------------------------
# player levels up, assign attributes based on player's role, return attributes and new level --------------------------
def level_up():
    level_up_dictionary = {"new level": 0, "player stats": []}

    if player.level < 20:
        player.level = player.level + 1
        # reset player health, energy and experience points
        player.health = 100
        player.energy = 100
        player.experience = 0
        drawing_functions.level_up_draw(level_up_win, player, level_up_font, True)
    else:
        level_up_dictionary["new level"] = "You are already max level. "
        return level_up_dictionary


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# gets current player health and updates hp bar image on screen according to the health value from 0-100
# ----------------------------------------------------------------------------------------------------------------------
# gets current player health and updates hp bar image on screen according to the health value from 0-100
def health_bar_update(character):
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


# player energy bar update
def energy_bar_update(character):
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


# player xp bar update
def xp_bar_update(character):
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
        return rxp_89
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


# ----------------------------------------------------------------------------------------------------------------------
# getting event based on user click related to combat scenario (attack, skill and run buttons)
def combat_event_button(combat_event):
    if combat_event.type == pygame.MOUSEBUTTONUP:
        combat_mouse = pygame.mouse.get_pos()
        # if mouse rect collides with attack button, skill button or run button return string representing it
        if no_role_attack_button.rect.collidepoint(combat_mouse):
            return "attack"
        if mage_attack_button.rect.collidepoint(combat_mouse):
            return "attack"
        if fighter_attack_button.rect.collidepoint(combat_mouse):
            return "attack"
        if scout_attack_button.rect.collidepoint(combat_mouse):
            return "attack"
        if barrier_button.rect.collidepoint(combat_mouse):
            return "skill 1"
        if hard_strike_button.rect.collidepoint(combat_mouse):
            return "skill 1"
        if sharp_sense_button.rect.collidepoint(combat_mouse):
            return "skill 1"


# ----------------------------------------------------------------------------------------------------------------------
def npc_event_button(npc_event):
    if npc_event.type == pygame.MOUSEBUTTONUP:
        npc_mouse = pygame.mouse.get_pos()
        if quest_button.rect.collidepoint(npc_mouse):
            return "quest"
        if leave_button.rect.collidepoint(npc_mouse):
            return "leave"


# ----------------------------------------------------------------------------------------------------------------------
def quest_event_button(quest_event):
    if quest_event.type == pygame.MOUSEBUTTONUP:
        quest_mouse = pygame.mouse.get_pos()
        if accept_button.rect.collidepoint(quest_mouse):
            return "accept"
        if decline_button.rect.collidepoint(quest_mouse):
            return "decline"


# ----------------------------------------------------------------------------------------------------------------------
# getting event based on user click related to shop scenario (buy, sell and leave buttons)
def shop_event_button(shop_event):
    if shop_event.type == pygame.MOUSEBUTTONUP:
        shop_mouse = pygame.mouse.get_pos()
        # if mouse rect collides with buy button, sell button or leave button return string representing it
        if buy_button.rect.collidepoint(shop_mouse):
            return "buy"
        if leave_button.rect.collidepoint(shop_mouse):
            return "leave"


# ----------------------------------------------------------------------------------------------------------------------
# getting event based on user click related to inn scenario
def inn_event_button(inn_event):
    if inn_event.type == pygame.MOUSEBUTTONUP:
        inn_mouse = pygame.mouse.get_pos()
        if rest_button.rect.collidepoint(inn_mouse):
            return "rest"
        if leave_button.rect.collidepoint(inn_mouse):
            return "leave"


# ----------------------------------------------------------------------------------------------------------------------
# getting event based on user click related to academia scenario
def academia_event_button(academia_event):
    if academia_event.type == pygame.MOUSEBUTTONUP:
        academia_mouse = pygame.mouse.get_pos()

        if mage_learn_button.rect.collidepoint(academia_mouse):
            return "mage learn"
        if fighter_learn_button.rect.collidepoint(academia_mouse):
            return "fighter learn"
        if scout_learn_button.rect.collidepoint(academia_mouse):
            return "scout learn"
        if leave_button.rect.collidepoint(academia_mouse):
            return "leave"


# ----------------------------------------------------------------------------------------------------------------------
# getting item player clicked based on it's name and return the corresponding item, for clicking on inventory items
def inventory_event_item(inventory_event_here):
    if inventory_event_here.type == pygame.MOUSEBUTTONUP:
        inventory_mouse = pygame.mouse.get_pos()
        # list of sprites that collided with mouse cursor rect
        clicked_element = [inventory_element for inventory_element in player_items
                           if inventory_element.rect.collidepoint(inventory_mouse)]
        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_element[0].name == "health potion":
                return clicked_element[0]
            if clicked_element[0].name == "energy potion":
                return clicked_element[0]
            if clicked_element[0].name == "shiny rock":
                return clicked_element[0]
            if clicked_element[0].name == "bone dust":
                return clicked_element[0]
            if clicked_element[0].name == "basic staff":
                return clicked_element[0]
            if clicked_element[0].name == "basic sword":
                return clicked_element[0]
            if clicked_element[0].name == "basic bow":
                return clicked_element[0]
            if clicked_element[0].name == "basic robes":
                return clicked_element[0]
            if clicked_element[0].name == "basic armor":
                return clicked_element[0]
            if clicked_element[0].name == "basic tunic":
                return clicked_element[0]
            if clicked_element[0].name == "temporary item":
                return clicked_element[0]
        except IndexError:
            pass


# ----------------------------------------------------------------------------------------------------------------------
# getting item player clicked based on it's name and return the corresponding item, for clicking on inventory items
def equipment_event_item(equipment_event_here):
    if equipment_event_here.type == pygame.MOUSEBUTTONUP:
        equipment_mouse = pygame.mouse.get_pos()
        # list of sprites that collided with mouse cursor rect
        clicked_element = [equipment_element for equipment_element in player_equipment
                           if equipment_element.rect.collidepoint(equipment_mouse)]
        # try to get equipment item player clicked based on it's name and return it
        try:
            if clicked_element[0].name == "basic staff":
                return clicked_element[0]
            if clicked_element[0].name == "basic sword":
                return clicked_element[0]
            if clicked_element[0].name == "basic bow":
                return clicked_element[0]
            if clicked_element[0].name == "basic robes":
                return clicked_element[0]
            if clicked_element[0].name == "basic armor":
                return clicked_element[0]
            if clicked_element[0].name == "basic tunic":
                return clicked_element[0]
        except IndexError:
            pass


# ----------------------------------------------------------------------------------------------------------------------
# getting item player clicked based on it's name and return the corresponding item, for clicking on buy items
def buy_event_item(buy_event):
    if buy_event.type == pygame.MOUSEBUTTONUP:
        buy_mouse = pygame.mouse.get_pos()
        # list of sprites that collided with mouse cursor rect
        clicked_element = [buy_element for buy_element in shopkeeper_items if buy_element.rect.collidepoint(buy_mouse)]
        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_element[0].name == "health potion":
                return clicked_element[0]
            if clicked_element[0].name == "energy potion":
                return clicked_element[0]
            if clicked_element[0].name == "shiny rock":
                return clicked_element[0]
            if clicked_element[0].name == "bone dust":
                return clicked_element[0]
            if clicked_element[0].name == "basic staff":
                return clicked_element[0]
            if clicked_element[0].name == "basic sword":
                return clicked_element[0]
            if clicked_element[0].name == "basic bow":
                return clicked_element[0]
            if clicked_element[0].name == "basic robes":
                return clicked_element[0]
            if clicked_element[0].name == "basic armor":
                return clicked_element[0]
            if clicked_element[0].name == "basic tunic":
                return clicked_element[0]
        except IndexError:
            pass


# ----------------------------------------------------------------------------------------------------------------------
# getting item player clicked based on it's name and return the corresponding item, for clicking on sell items
def sell_event_item(sell_event):
    if sell_event.type == pygame.MOUSEBUTTONUP:
        sell_mouse = pygame.mouse.get_pos()
        # list of sprites that collided with mouse cursor rect
        clicked_element = [sell_element for sell_element in player_items if
                           sell_element.rect.collidepoint(sell_mouse)]
        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_element[0].name == "health potion":
                return clicked_element[0]
            if clicked_element[0].name == "energy potion":
                return clicked_element[0]
            if clicked_element[0].name == "shiny rock":
                return clicked_element[0]
            if clicked_element[0].name == "bone dust":
                return clicked_element[0]
            if clicked_element[0].name == "basic staff":
                return clicked_element[0]
            if clicked_element[0].name == "basic sword":
                return clicked_element[0]
            if clicked_element[0].name == "basic bow":
                return clicked_element[0]
            if clicked_element[0].name == "basic robes":
                return clicked_element[0]
            if clicked_element[0].name == "basic armor":
                return clicked_element[0]
            if clicked_element[0].name == "basic tunic":
                return clicked_element[0]
            if clicked_element[0].name == "temporary item":
                return clicked_element[0]
        except IndexError:
            pass


# ----------------------------------------------------------------------------------------------------------------------
# getting item player clicked based on it's name and return the corresponding item, for clicking on sell items
def skill_learn_event_item(skill_learn_event):
    if skill_learn_event.type == pygame.MOUSEBUTTONUP:
        skill_learn_mouse = pygame.mouse.get_pos()
        # list of sprites that collided with mouse cursor rect
        skill_learn_element = [skill_learn_element for skill_learn_element in skill_learn_items if
                               skill_learn_element.rect.collidepoint(skill_learn_mouse)]

        # try to get skill player clicked based on it's name and return it
        try:
            if skill_learn_element[0].name == "barrier learn button":
                return skill_learn_element[0]
            if skill_learn_element[0].name == "hard strike learn button":
                return skill_learn_element[0]
            if skill_learn_element[0].name == "sharp sense learn button":
                return skill_learn_element[0]
            if skill_learn_element[0].name == "close button":
                return skill_learn_element[0]
        except IndexError:
            pass


# ----------------------------------------------------------------------------------------------------------------------
# function to respawn enemies if they are less than a specified amount active in game. spawns with random coord. and lvl
def enemy_respawn():
    snake_counter = 0
    ghoul_counter = 0
    # generate random coordinates and level for new enemy to spawn within boundaries and level range
    # if not scaled, coordinates set to default boundaries
    random_snake_x = random.randrange(150, 300)
    random_snake_y = random.randrange(150, 300)
    random_snake_level = random.randrange(1, 4)
    random_ghoul_x = random.randrange(650, 900)
    random_ghoul_y = random.randrange(150, 300)
    random_ghoul_level = random.randrange(3, 6)

    # count current enemies active in game
    for mob in enemies:
        if mob.name == "snake":
            snake_counter += 1
        if mob.name == "ghoul":
            ghoul_counter += 1

    # if there are less than 3 snakes in game, create another snake with random level and coordinates. add to groups
    if snake_counter < 3:
        # if not scaled, set images attributed to enemy with default values
        new_snake = Enemy("snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y, True,
                          Item("shiny rock", "rock", 200, 200, shiny_rock_img), snake,
                          UiElement("snake hp bar", 700, 90, hp_100, False))
        snakes.add(new_snake)
        enemies.add(new_snake)
        most_sprites.add(new_snake)

    # if there are less than 3 ghouls in game, create another ghoul with random level and coordinates. add to groups
    if ghoul_counter < 3:
        new_ghoul = Enemy("ghoul", "ghoul", 100, 100, random_ghoul_level, random_ghoul_x, random_ghoul_y, True,
                          Item("bone dust", "dust", 200, 200, bone_dust_img), ghoul,
                          UiElement("ghoul hp bar", 700, 90, hp_100, False))
        ghouls.add(new_ghoul)
        enemies.add(new_ghoul)
        most_sprites.add(new_ghoul)


def status_and_inventory_updates():
    # update players status bars ---------------------------------------------------------------------------------------
    hp_bar.update(hp_bar.x_coordinate, hp_bar.y_coordinate, health_bar_update(player))
    en_bar.update(en_bar.x_coordinate, en_bar.y_coordinate, energy_bar_update(player))
    xp_bar.update(xp_bar.x_coordinate, xp_bar.y_coordinate, xp_bar_update(player))

    # set player's current role based on the type of weapon they have equipped -----------------------------------------
    if player.equipment["weapon"] != "":
        if player.equipment["weapon"].type == "mage":
            player.role = "mage"
            if player.race == "amuna":
                # update player sprite based on their current role and facing direction
                if current_direction == "up":
                    player.surf = player_mage_up
                if current_direction == "down":
                    player.surf = player_mage_down
                if current_direction == "left":
                    player.surf = player_mage_left
                if current_direction == "right":
                    player.surf = player_mage_right

        if player.equipment["weapon"].type == "fighter":
            player.role = "fighter"
            if player.race == "amuna":
                if current_direction == "up":
                    player.surf = player_fighter_up
                if current_direction == "down":
                    player.surf = player_fighter_down
                if current_direction == "left":
                    player.surf = player_fighter_left
                if current_direction == "right":
                    player.surf = player_fighter_right

        if player.equipment["weapon"].type == "scout":
            player.role = "scout"
            if player.race == "amuna":
                if current_direction == "up":
                    player.surf = player_scout_up
                if current_direction == "down":
                    player.surf = player_scout_down
                if current_direction == "left":
                    player.surf = player_scout_left
                if current_direction == "right":
                    player.surf = player_scout_right

    # player doesn't have a role without a weapon equipped
    else:
        player.role = ""
        if player.race == "amuna":
            if current_direction == "up":
                player.surf = player_no_role_amuna_up
            if current_direction == "down":
                player.surf = player_no_role_amuna_down
            if current_direction == "left":
                player.surf = player_no_role_amuna_left
            if current_direction == "right":
                player.surf = player_no_role_amuna_right
        if player.race == "sorae":
            if current_direction == "up":
                player.surf = player_no_role_sorae_up
            if current_direction == "down":
                player.surf = player_no_role_sorae_down
            if current_direction == "left":
                player.surf = player_no_role_sorae_left
            if current_direction == "right":
                player.surf = player_no_role_sorae_right

    # ------------------------------------------------------------------------------------------------------------------
    # clear list used for drawing player items to screen before going through inventory and drawing
    # this removes items that may have been used and left in list from previous iterations,
    # so they are not re-drawn after being used.
    player_items.clear()

    # create inventory window items ------------------------------------------------------------------------------------
    # if player has items in their inventory ---------------------------------------------------------------------------
    if len(player.items) > 0:
        first_coord = 1063
        second_coord = 462

        try:
            inventory_counter = 0
            # go through player items and assign inventory slots (coordinates) to them
            for item_here in player.items:
                if item_here.name == "health potion":
                    item_here.update(first_coord, second_coord, health_pot_img)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "energy potion":
                    item_here.update(first_coord, second_coord, energy_pot_img)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "shiny rock":
                    item_here.update(first_coord, second_coord, shiny_rock_img)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "bone dust":
                    item_here.update(first_coord, second_coord, bone_dust_img)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic staff":
                    item_here.update(first_coord, second_coord, basic_staff_img)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic sword":
                    item_here.update(first_coord, second_coord, basic_sword_img)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic bow":
                    item_here.update(first_coord, second_coord, basic_bow_img)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic robes":
                    item_here.update(first_coord, second_coord, basic_robes_img)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic armor":
                    item_here.update(first_coord, second_coord, basic_armor_img)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic tunic":
                    item_here.update(first_coord, second_coord, basic_tunic_img)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "temporary item":
                    item_here.update(first_coord, second_coord, temp_img)
                    player_items.append(item_here)
                    inventory_counter += 1

                # add 75 to the items x-coordinate value so the next item will be added to next slot
                first_coord += 60

                # add 60 to items y coordinate value if the first row of (4) slots has been filled
                # reset first coordinate and counter to start in the leftmost slot again
                if inventory_counter > 3:
                    second_coord += 60
                    first_coord = 1063
                    inventory_counter = 0

        except AttributeError:
            pass
        # updates players inventory items if item is used in combat scenario (ex. health pot.)
        for item_here in player_items:
            screen.blit(item_here.surf, item_here.rect)


def inventory_click_handler():
    return_dict = {"item message": "", "gear checked": True, "weapon checked": True}
    # inventory click handler ------------------------------------------------------------------------------------------
    inventory_item = inventory_event_item(event)

    try:
        if inventory_item.name == "health potion":
            if player.health == 100:
                return_dict["item message"] = "You're already at full health."
            else:
                player.health = player.health + 40
                # if health potion heals over 100 hp, just set to 100 (max health)
                if player.health > 100:
                    player.health = 100
                player_items.remove(inventory_item)
                player.items.remove(inventory_item)
                return_dict["item message"] = "The potion heals you for 40 hp."
        elif inventory_item.name == "energy potion":
            if player.energy == 100:
                return_dict["item message"] = "You're already at full energy."
            else:
                player.energy = player.energy + 40
                # if energy potion energizes over 100 hp, just set to 100 (max energy)
                if player.energy > 100:
                    player.energy = 100
                player_items.remove(inventory_item)
                player.items.remove(inventory_item)
                return_dict["item message"] = "The potion energizes you for 40 en."
        elif inventory_item.name == "shiny rock":
            return_dict["item message"] = "Oh, shiny. Maybe you can sell it?"
        elif inventory_item.name == "bone dust":
            return_dict["item message"] = "Eh, dusty. Maybe you can sell it?"
        elif inventory_item.name == "temporary item":
            return_dict["item message"] = "Tell my designer to finish me!"

        # if player clicks an equitable item, equip it and set gear checked to false so main loop will check stats
        elif inventory_item.name == "basic staff":
            if player.equipment["weapon"] == "":
                player.equipment["weapon"] = inventory_item
                player_items.remove(inventory_item)
                player.items.remove(inventory_item)
                return_dict["item message"] = "Basic Staff weapon equipped"
                return_dict["weapon checked"] = False
            else:
                return_dict["item message"] = "Un-equip your current weapon first."
        elif inventory_item.name == "basic sword":
            if player.equipment["weapon"] == "":
                player.equipment["weapon"] = inventory_item
                player_items.remove(inventory_item)
                player.items.remove(inventory_item)
                return_dict["item message"] = "Basic Sword weapon equipped"
                return_dict["weapon checked"] = False
            else:
                return_dict["item message"] = "Un-equip your current weapon first."
        elif inventory_item.name == "basic bow":
            if player.equipment["weapon"] == "":
                player.equipment["weapon"] = inventory_item
                player_items.remove(inventory_item)
                player.items.remove(inventory_item)
                return_dict["item message"] = "Basic Bow weapon equipped"
                return_dict["weapon checked"] = False
            else:
                return_dict["item message"] = "Un-equip your current weapon first."
        elif inventory_item.name == "basic robes":
            if player.equipment["chest"] == "":
                if player.role == "mage":
                    player.equipment["chest"] = inventory_item
                    player_items.remove(inventory_item)
                    player.items.remove(inventory_item)
                    return_dict["item message"] = "Basic Robes chest equipped"
                    return_dict["gear checked"] = False
                else:
                    return_dict["item message"] = "Only mages wear light armor."
            else:
                return_dict["item message"] = "Un-equip your current gear first."
        elif inventory_item.name == "basic armor":
            if player.equipment["chest"] == "":
                if player.role == "fighter":
                    player.equipment["chest"] = inventory_item
                    player_items.remove(inventory_item)
                    player.items.remove(inventory_item)
                    return_dict["item message"] = "Basic Armor chest equipped"
                    return_dict["gear checked"] = False
                else:
                    return_dict["item message"] = "Only fighters wear heavy armor."
            else:
                return_dict["item message"] = "Un-equip your current gear first."
        elif inventory_item.name == "basic tunic":
            if player.equipment["chest"] == "":
                if player.role == "scout":
                    player.equipment["chest"] = inventory_item
                    player_items.remove(inventory_item)
                    player.items.remove(inventory_item)
                    return_dict["item message"] = "Basic Tunic chest equipped"
                    return_dict["gear checked"] = False
                else:
                    return_dict["item message"] = "Only scouts wear medium armor."
            else:
                return_dict["item message"] = "Un-equip your current gear first."
    except AttributeError:
        pass

    return return_dict


def equipment_updates():
    player_equipment.clear()
    try:
        if player.equipment["weapon"].name == "basic staff":
            player.equipment["weapon"].update(1078, 285, basic_staff_img)
            player_equipment.append(player.equipment["weapon"])
        if player.equipment["weapon"].name == "basic sword":
            player.equipment["weapon"].update(1078, 285, basic_sword_img)
            player_equipment.append(player.equipment["weapon"])
        if player.equipment["weapon"].name == "basic bow":
            player.equipment["weapon"].update(1078, 285, basic_bow_img)
            player_equipment.append(player.equipment["weapon"])
        if player.equipment["chest"].name == "basic robes":
            player.equipment["chest"].update(1153, 197, basic_robes_img)
            player_equipment.append(player.equipment["chest"])
        if player.equipment["chest"].name == "basic armor":
            player.equipment["chest"].update(1153, 197, basic_armor_img)
            player_equipment.append(player.equipment["chest"])
        if player.equipment["chest"].name == "basic tunic":
            player.equipment["chest"].update(1153, 197, basic_tunic_img)
            player_equipment.append(player.equipment["chest"])
    except AttributeError:
        pass

    # updates players inventory items if item is used in combat scenario (ex. health pot.)
    for equipment_here in player_equipment:
        screen.blit(equipment_here.surf, equipment_here.rect)


def equipment_click_handler():
    return_dict = {"equipment message": "", "gear checked": True, "weapon checked": True}
    equipment_item = equipment_event_item(event)

    # if player clicks item in equipment sub-screen, un-equip the item and place in inventory, if inventory isn't full
    try:
        if equipment_item.name == "basic staff":
            if len(player.items) < 15:
                player.items.append(equipment_item)
                player.equipment["weapon"] = ""
                # remove gear along with weapon when weapon is clicked. Add both to inventory
                if player.equipment["chest"] != "":
                    player.items.append(player.equipment["chest"])
                    player.equipment["chest"] = ""
                return_dict["equipment message"] = "Basic Staff weapon un-equipped."
                return_dict["gear checked"] = False
                return_dict["weapon checked"] = False
            else:
                return_dict["equipment message"] = "Your inventory is full."
        if equipment_item.name == "basic sword":
            if len(player.items) < 15:
                player.items.append(equipment_item)
                player.equipment["weapon"] = ""
                if player.equipment["chest"] != "":
                    player.items.append(player.equipment["chest"])
                    player.equipment["chest"] = ""
                return_dict["equipment message"] = "Basic Sword weapon un-equipped."
                return_dict["gear checked"] = False
                return_dict["weapon checked"] = False
            else:
                return_dict["equipment message"] = "Your inventory is full."
        if equipment_item.name == "basic bow":
            if len(player.items) < 15:
                player.items.append(equipment_item)
                player.equipment["weapon"] = ""
                if player.equipment["chest"] != "":
                    player.items.append(player.equipment["chest"])
                    player.equipment["chest"] = ""
                return_dict["equipment message"] = "Basic Bow weapon un-equipped."
                return_dict["gear checked"] = False
                return_dict["weapon checked"] = False
            else:
                return_dict["equipment message"] = "Your inventory is full."
        if equipment_item.name == "basic robes":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["chest"] = ""
                return_dict["equipment message"] = "Basic Robes chest un-equipped."
                return_dict["gear checked"] = False
            else:
                return_dict["equipment message"] = "Your inventory is full."
        if equipment_item.name == "basic armor":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["chest"] = ""
                return_dict["equipment message"] = "Basic Armor chest un-equipped."
                return_dict["gear checked"] = False
            else:
                return_dict["equipment message"] = "Your inventory is full."
        if equipment_item.name == "basic tunic":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["chest"] = ""
                return_dict["equipment message"] = "Basic Tunic chest un-equipped."
                return_dict["gear checked"] = False
            else:
                return_dict["equipment message"] = "Your inventory is full."
    except AttributeError:
        pass

    return return_dict


def gear_check():
    # check players current gear type. return true after checked so the defense stat doesn't keep adding every iteration
    try:
        if player.equipment["chest"].type == "fighter":
            player.defence += 12
        if player.equipment["chest"].type == "scout":
            player.defence += 8
        if player.equipment["chest"].type == "mage":
            player.defence += 4
    # if exception is raised, player isn't wearing anything because the .type doesn't exist, so set defence to 0
    except AttributeError:
        player.defence = 0
        pass
    return True


def weapon_check():
    # same as above function for equipment just checks weapon and applies to offense instead
    try:
        if player.equipment["weapon"].type == "mage":
            player.offense += 35
        if player.equipment["weapon"].type == "scout":
            player.offense += 25
        if player.equipment["weapon"].type == "fighter":
            player.offense += 15
    except AttributeError:
        player.offense = 0
        pass
    return True


# will be used for music later -----------------------------------------------------------------------------------------
# pygame.mixer.init()
# initialize game, set clock for framerate, set screen size ------------------------------------------------------------
pygame.init()
pygame.display.set_caption("Project Eterna")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# background textures --------------------------------------------------------------------------------------------------
seldon_district_bg = pygame.image.load(resource_urls.seldon_bg_screen)
seldon_district_battle = pygame.image.load(resource_urls.seldon_battle_screen)
seldon_district_shop = pygame.image.load(resource_urls.seldon_shop_screen)
seldon_district_inn = pygame.image.load(resource_urls.seldon_inn_screen)
seldon_district_academia = pygame.image.load(resource_urls.seldon_academia_screen)
seldon_hearth_screen = pygame.image.load(resource_urls.seldon_hearth_screen)
game_over_screen = pygame.image.load(resource_urls.game_over_screen)
start_screen = pygame.image.load(resource_urls.start_screen)
nera_sleep_screen = pygame.image.load(resource_urls.nera_sleep_screen)
korlok_district_bg = pygame.image.load(resource_urls.korlok_bg_screen)
amuna_character_screen = pygame.image.load(resource_urls.amuna_character_screen)
nuldar_character_screen = pygame.image.load(resource_urls.nuldar_character_screen)
sorae_character_screen = pygame.image.load(resource_urls.sorae_character_screen)

# sprite sheets --------------------------------------------------------------------------------------------------------
# character selections -------------------------------------------------------------------------------------------------
character_select_sheet = SpriteSheet(resource_urls.character_selections)
amuna_character_img = character_select_sheet.get_image(0, 0, 250, 350)
nuldar_character_img = character_select_sheet.get_image(250, 0, 250, 350)
sorae_character_img = character_select_sheet.get_image(500, 0, 250, 350)
# name text box --------------------------------------------------------------------------------------------------------
name_input_sheet = SpriteSheet(resource_urls.name_input_url)
name_input_img = name_input_sheet.get_image(0, 0, 300, 50)
name_input_empty_img = name_input_sheet.get_image(300, 0, 300, 50)
# player no role amuna race --------------------------------------------------------------------------------------------
player_no_role_amuna_sheet = SpriteSheet(resource_urls.player_no_role_amuna_url)
player_no_role_amuna_down = player_no_role_amuna_sheet.get_image(0, 0, 50, 75)
player_no_role_amuna_up = player_no_role_amuna_sheet.get_image(50, 0, 50, 75)
player_no_role_amuna_left = player_no_role_amuna_sheet.get_image(100, 0, 50, 75)
player_no_role_amuna_right = player_no_role_amuna_sheet.get_image(150, 0, 50, 75)
# player no role amuna race --------------------------------------------------------------------------------------------
player_no_role_sorae_sheet = SpriteSheet(resource_urls.player_no_role_sorae_url)
player_no_role_sorae_down = player_no_role_sorae_sheet.get_image(0, 0, 50, 75)
player_no_role_sorae_up = player_no_role_sorae_sheet.get_image(50, 0, 50, 75)
player_no_role_sorae_left = player_no_role_sorae_sheet.get_image(100, 0, 50, 75)
player_no_role_sorae_right = player_no_role_sorae_sheet.get_image(150, 0, 50, 75)
# player mage ----------------------------------------------------------------------------------------------------------
player_mage_sheet = SpriteSheet(resource_urls.player_mage_url)
player_mage_down = player_mage_sheet.get_image(0, 0, 50, 75)
player_mage_up = player_mage_sheet.get_image(50, 0, 50, 75)
player_mage_left = player_mage_sheet.get_image(100, 0, 50, 75)
player_mage_right = player_mage_sheet.get_image(150, 0, 50, 75)
# player fighter -------------------------------------------------------------------------------------------------------
player_fighter_sheet = SpriteSheet(resource_urls.player_fighter_url)
player_fighter_down = player_fighter_sheet.get_image(0, 0, 50, 75)
player_fighter_up = player_fighter_sheet.get_image(50, 0, 50, 75)
player_fighter_left = player_fighter_sheet.get_image(100, 0, 50, 75)
player_fighter_right = player_fighter_sheet.get_image(150, 0, 50, 75)
# player scout ---------------------------------------------------------------------------------------------------------
player_scout_sheet = SpriteSheet(resource_urls.player_scout_url)
player_scout_down = player_scout_sheet.get_image(0, 0, 50, 75)
player_scout_up = player_scout_sheet.get_image(50, 0, 50, 75)
player_scout_left = player_scout_sheet.get_image(100, 0, 50, 75)
player_scout_right = player_scout_sheet.get_image(150, 0, 50, 75)
# player battle --------------------------------------------------------------------------------------------------------
player_battle_sheet = SpriteSheet(resource_urls.player_battle_url)
player_no_role_battle = player_battle_sheet.get_image(0, 0, 750, 624)
player_no_role_attack = player_battle_sheet.get_image(750, 0, 750, 624)
player_mage_battle = player_battle_sheet.get_image(1500, 0, 750, 624)
player_mage_attack = player_battle_sheet.get_image(2250, 0, 750, 624)
player_fighter_battle = player_battle_sheet.get_image(3000, 0, 750, 624)
player_fighter_attack = player_battle_sheet.get_image(3750, 0, 750, 624)
player_scout_battle = player_battle_sheet.get_image(4500, 0, 750, 624)
player_scout_attack = player_battle_sheet.get_image(5250, 0, 750, 624)
# player skills --------------------------------------------------------------------------------------------------------
player_skills_sheet = SpriteSheet(resource_urls.player_skills_url)
player_mage_barrier_battle = player_skills_sheet.get_image(0, 0, 750, 624)
player_mage_barrier_attack = player_skills_sheet.get_image(750, 0, 750, 624)
player_scout_sense_battle = player_skills_sheet.get_image(1500, 0, 750, 624)
player_scout_sense_attack = player_skills_sheet.get_image(2250, 0, 750, 624)
player_fighter_strike = player_skills_sheet.get_image(3000, 0, 750, 624)
# garan npc ------------------------------------------------------------------------------------------------------------
garan_sheet = SpriteSheet(resource_urls.garan_url)
garan_down = garan_sheet.get_image(0, 0, 40, 62)
garan_up = garan_sheet.get_image(40, 0, 40, 62)
garan_left = garan_sheet.get_image(80, 0, 40, 62)
garan_right = garan_sheet.get_image(120, 0, 40, 62)
# maurelle npc ---------------------------------------------------------------------------------------------------------
maurelle_sheet = SpriteSheet(resource_urls.maurelle_url)
maurelle_down = maurelle_sheet.get_image(0, 0, 40, 62)
maurelle_up = maurelle_sheet.get_image(40, 0, 40, 62)
maurelle_left = maurelle_sheet.get_image(80, 0, 40, 62)
maurelle_right = maurelle_sheet.get_image(120, 0, 40, 62)
# guard npc ------------------------------------------------------------------------------------------------------------
guard_sheet = SpriteSheet(resource_urls.guard_url)
guard_down = guard_sheet.get_image(0, 0, 50, 75)
guard_up = guard_sheet.get_image(50, 0, 50, 75)
guard_left = guard_sheet.get_image(100, 0, 50, 75)
guard_right = guard_sheet.get_image(150, 0, 50, 75)
# npc interactions -----------------------------------------------------------------------------------------------------
npc_interactions_sheet = SpriteSheet(resource_urls.npc_interactions_url)
garan_interaction = npc_interactions_sheet.get_image(0, 0, 200, 260)
maurelle_interaction = npc_interactions_sheet.get_image(200, 0, 200, 260)
guard_interaction = npc_interactions_sheet.get_image(400, 0, 200, 260)
# enemies --------------------------------------------------------------------------------------------------------------
enemies_sheet = SpriteSheet(resource_urls.enemies_url)
snake = enemies_sheet.get_image(0, 0, 50, 50)
ghoul = enemies_sheet.get_image(50, 0, 50, 50)
# enemies battle -------------------------------------------------------------------------------------------------------
enemies_battle_sheet = SpriteSheet(resource_urls.enemies_battle_url)
snake_battle = enemies_battle_sheet.get_image(0, 0, 300, 250)
snake_attack = enemies_battle_sheet.get_image(300, 0, 300, 250)
ghoul_battle = enemies_battle_sheet.get_image(600, 0, 300, 250)
ghoul_attack = enemies_battle_sheet.get_image(900, 0, 300, 250)
# amuna buildings ------------------------------------------------------------------------------------------------------
amuna_buildings_sheet = SpriteSheet(resource_urls.amuna_buildings_url)
amuna_academia_building = amuna_buildings_sheet.get_image(0, 0, 100, 100)
amuna_inn_building = amuna_buildings_sheet.get_image(100, 0, 100, 100)
amuna_shop_building = amuna_buildings_sheet.get_image(200, 0, 100, 100)
# items ----------------------------------------------------------------------------------------------------------------
items_sheet = SpriteSheet(resource_urls.items_url)
health_pot_img = items_sheet.get_image(0, 0, 50, 50)
energy_pot_img = items_sheet.get_image(50, 0, 50, 50)
basic_robes_img = items_sheet.get_image(100, 0, 50, 50)
basic_armor_img = items_sheet.get_image(150, 0, 50, 50)
basic_tunic_img = items_sheet.get_image(200, 0, 50, 50)
basic_staff_img = items_sheet.get_image(250, 0, 50, 50)
basic_sword_img = items_sheet.get_image(300, 0, 50, 50)
basic_bow_img = items_sheet.get_image(350, 0, 50, 50)
bone_dust_img = items_sheet.get_image(400, 0, 50, 50)
shiny_rock_img = items_sheet.get_image(450, 0, 50, 50)
temp_img = items_sheet.get_image(500, 0, 50, 50)
# player info windows --------------------------------------------------------------------------------------------------
player_info_sheet = SpriteSheet(resource_urls.player_info_url)
character_window_img = player_info_sheet.get_image(0, 0, 500, 525)
journal_window_img = player_info_sheet.get_image(500, 0, 500, 525)
# books ----------------------------------------------------------------------------------------------------------------
books_sheet = SpriteSheet(resource_urls.books_url)
mage_book_img = books_sheet.get_image(0, 0, 700, 525)
fighter_book_img = books_sheet.get_image(700, 0, 700, 525)
scout_book_img = books_sheet.get_image(1400, 0, 700, 525)
# start screen buttons -------------------------------------------------------------------------------------------------
start_button_sheet = SpriteSheet(resource_urls.start_buttons_url)
new_game_img = start_button_sheet.get_image(0, 0, 384, 75)
continue_img = start_button_sheet.get_image(385, 0, 384, 75)
# race select buttons --------------------------------------------------------------------------------------------------
race_select_button_sheet = SpriteSheet(resource_urls.race_select_buttons_url)
amuna_button_img = race_select_button_sheet.get_image(0, 0, 384, 75)
nuldar_button_img = race_select_button_sheet.get_image(385, 0, 384, 75)
sorae_button_img = race_select_button_sheet.get_image(770, 0, 384, 75)
# main buttons ---------------------------------------------------------------------------------------------------------
buttons_sheet = SpriteSheet(resource_urls.buttons_url)
character_button_img = buttons_sheet.get_image(0, 0, 100, 50)
journal_button_img = buttons_sheet.get_image(100, 0, 100, 50)
buy_button_img = buttons_sheet.get_image(200, 0, 100, 50)
rest_button_img = buttons_sheet.get_image(300, 0, 100, 50)
quest_button_img = buttons_sheet.get_image(400, 0, 100, 50)
leave_button_img = buttons_sheet.get_image(500, 0, 100, 50)
accept_button_img = buttons_sheet.get_image(600, 0, 100, 50)
decline_button_img = buttons_sheet.get_image(700, 0, 100, 50)
# attack buttons -------------------------------------------------------------------------------------------------------
attack_buttons_sheet = SpriteSheet(resource_urls.attack_buttons_url)
mage_attack_button_img = attack_buttons_sheet.get_image(0, 0, 60, 60)
fighter_attack_button_img = attack_buttons_sheet.get_image(60, 0, 60, 60)
scout_attack_button_img = attack_buttons_sheet.get_image(120, 0, 60, 60)
no_role_attack_button_img = attack_buttons_sheet.get_image(180, 0, 60, 60)
# skill buttons --------------------------------------------------------------------------------------------------------
skill_buttons_sheet = SpriteSheet(resource_urls.skill_buttons_url)
barrier_button_img = skill_buttons_sheet.get_image(0, 0, 60, 60)
strike_button_img = skill_buttons_sheet.get_image(60, 0, 60, 60)
sense_button_img = skill_buttons_sheet.get_image(120, 0, 60, 60)
# quest windows --------------------------------------------------------------------------------------------------------
quest_windows_sheet = SpriteSheet(resource_urls.quest_windows_url)
garan_quest = quest_windows_sheet.get_image(0, 0, 500, 525)
maurelle_quest = quest_windows_sheet.get_image(500, 0, 500, 525)
guard_quest = quest_windows_sheet.get_image(1000, 0, 500, 525)
# quest stars ----------------------------------------------------------------------------------------------------------
quest_stars_sheet = SpriteSheet(resource_urls.quest_stars_url)
quest_start_star = quest_stars_sheet.get_image(0, 0, 50, 50)
quest_progress_star = quest_stars_sheet.get_image(50, 0, 50, 50)
quest_complete_star = quest_stars_sheet.get_image(100, 0, 50, 50)
# pop up notifications -------------------------------------------------------------------------------------------------
popups_sheet = SpriteSheet(resource_urls.popups_url)
gear_popup = popups_sheet.get_image(0, 0, 400, 200)
health_popup = popups_sheet.get_image(400, 0, 400, 200)
knowledge_popup = popups_sheet.get_image(800, 0, 400, 200)
# heath bars -----------------------------------------------------------------------------------------------------------
hp_sheet = SpriteSheet(resource_urls.hp_url)
hp_0 = hp_sheet.get_image(0, 0, 305, 19)
hp_1 = hp_sheet.get_image(305, 0, 305, 19)
hp_2 = hp_sheet.get_image(610, 0, 305, 19)
hp_3 = hp_sheet.get_image(915, 0, 305, 19)
hp_4 = hp_sheet.get_image(1220, 0, 305, 19)
hp_5 = hp_sheet.get_image(1525, 0, 305, 19)
hp_6 = hp_sheet.get_image(1830, 0, 305, 19)
hp_7 = hp_sheet.get_image(2135, 0, 305, 19)
hp_8 = hp_sheet.get_image(2440, 0, 305, 19)
hp_9 = hp_sheet.get_image(2745, 0, 305, 19)
hp_10 = hp_sheet.get_image(0, 19, 305, 19)
hp_11 = hp_sheet.get_image(305, 19, 305, 19)
hp_12 = hp_sheet.get_image(610, 19, 305, 19)
hp_13 = hp_sheet.get_image(915, 19, 305, 19)
hp_14 = hp_sheet.get_image(1220, 19, 305, 19)
hp_15 = hp_sheet.get_image(1525, 19, 305, 19)
hp_16 = hp_sheet.get_image(1830, 19, 305, 19)
hp_17 = hp_sheet.get_image(2135, 19, 305, 19)
hp_18 = hp_sheet.get_image(2440, 19, 305, 19)
hp_19 = hp_sheet.get_image(2745, 19, 305, 19)
hp_20 = hp_sheet.get_image(0, 38, 305, 19)
hp_21 = hp_sheet.get_image(305, 38, 305, 19)
hp_22 = hp_sheet.get_image(610, 38, 305, 19)
hp_23 = hp_sheet.get_image(915, 38, 305, 19)
hp_24 = hp_sheet.get_image(1220, 38, 305, 19)
hp_25 = hp_sheet.get_image(1525, 38, 305, 19)
hp_26 = hp_sheet.get_image(1830, 38, 305, 19)
hp_27 = hp_sheet.get_image(2135, 38, 305, 19)
hp_28 = hp_sheet.get_image(2440, 38, 305, 19)
hp_29 = hp_sheet.get_image(2745, 38, 305, 19)
hp_30 = hp_sheet.get_image(0, 57, 305, 19)
hp_31 = hp_sheet.get_image(305, 57, 305, 19)
hp_32 = hp_sheet.get_image(610, 57, 305, 19)
hp_33 = hp_sheet.get_image(915, 57, 305, 19)
hp_34 = hp_sheet.get_image(1220, 57, 305, 19)
hp_35 = hp_sheet.get_image(1525, 57, 305, 19)
hp_36 = hp_sheet.get_image(1830, 57, 305, 19)
hp_37 = hp_sheet.get_image(2135, 57, 305, 19)
hp_38 = hp_sheet.get_image(2440, 57, 305, 19)
hp_39 = hp_sheet.get_image(2745, 57, 305, 19)
hp_40 = hp_sheet.get_image(0, 76, 305, 19)
hp_41 = hp_sheet.get_image(305, 76, 305, 19)
hp_42 = hp_sheet.get_image(610, 76, 305, 19)
hp_43 = hp_sheet.get_image(915, 76, 305, 19)
hp_44 = hp_sheet.get_image(1220, 76, 305, 19)
hp_45 = hp_sheet.get_image(1525, 76, 305, 19)
hp_46 = hp_sheet.get_image(1830, 76, 305, 19)
hp_47 = hp_sheet.get_image(2135, 76, 305, 19)
hp_48 = hp_sheet.get_image(2440, 76, 305, 19)
hp_49 = hp_sheet.get_image(2745, 76, 305, 19)
hp_50 = hp_sheet.get_image(0, 95, 305, 19)
hp_51 = hp_sheet.get_image(305, 95, 305, 19)
hp_52 = hp_sheet.get_image(610, 95, 305, 19)
hp_53 = hp_sheet.get_image(915, 95, 305, 19)
hp_54 = hp_sheet.get_image(1220, 95, 305, 19)
hp_55 = hp_sheet.get_image(1525, 95, 305, 19)
hp_56 = hp_sheet.get_image(1830, 95, 305, 19)
hp_57 = hp_sheet.get_image(2135, 95, 305, 19)
hp_58 = hp_sheet.get_image(2440, 95, 305, 19)
hp_59 = hp_sheet.get_image(2745, 95, 305, 19)
hp_60 = hp_sheet.get_image(0, 114, 305, 19)
hp_61 = hp_sheet.get_image(305, 114, 305, 19)
hp_62 = hp_sheet.get_image(610, 114, 305, 19)
hp_63 = hp_sheet.get_image(915, 114, 305, 19)
hp_64 = hp_sheet.get_image(1220, 114, 305, 19)
hp_65 = hp_sheet.get_image(1525, 114, 305, 19)
hp_66 = hp_sheet.get_image(1830, 114, 305, 19)
hp_67 = hp_sheet.get_image(2135, 114, 305, 19)
hp_68 = hp_sheet.get_image(2440, 114, 305, 19)
hp_69 = hp_sheet.get_image(2745, 114, 305, 19)
hp_70 = hp_sheet.get_image(0, 133, 305, 19)
hp_71 = hp_sheet.get_image(305, 133, 305, 19)
hp_72 = hp_sheet.get_image(610, 133, 305, 19)
hp_73 = hp_sheet.get_image(915, 133, 305, 19)
hp_74 = hp_sheet.get_image(1220, 133, 305, 19)
hp_75 = hp_sheet.get_image(1525, 133, 305, 19)
hp_76 = hp_sheet.get_image(1830, 133, 305, 19)
hp_77 = hp_sheet.get_image(2135, 133, 305, 19)
hp_78 = hp_sheet.get_image(2440, 133, 305, 19)
hp_79 = hp_sheet.get_image(2745, 133, 305, 19)
hp_80 = hp_sheet.get_image(0, 152, 305, 19)
hp_81 = hp_sheet.get_image(305, 152, 305, 19)
hp_82 = hp_sheet.get_image(610, 152, 305, 19)
hp_83 = hp_sheet.get_image(915, 152, 305, 19)
hp_84 = hp_sheet.get_image(1220, 152, 305, 19)
hp_85 = hp_sheet.get_image(1525, 152, 305, 19)
hp_86 = hp_sheet.get_image(1830, 152, 305, 19)
hp_87 = hp_sheet.get_image(2135, 152, 305, 19)
hp_88 = hp_sheet.get_image(2440, 152, 305, 19)
hp_89 = hp_sheet.get_image(2745, 152, 305, 19)
hp_90 = hp_sheet.get_image(0, 171, 305, 19)
hp_91 = hp_sheet.get_image(305, 171, 305, 19)
hp_92 = hp_sheet.get_image(610, 171, 305, 19)
hp_93 = hp_sheet.get_image(915, 171, 305, 19)
hp_94 = hp_sheet.get_image(1220, 171, 305, 19)
hp_95 = hp_sheet.get_image(1525, 171, 305, 19)
hp_96 = hp_sheet.get_image(1830, 171, 305, 19)
hp_97 = hp_sheet.get_image(2135, 171, 305, 19)
hp_98 = hp_sheet.get_image(2440, 171, 305, 19)
hp_99 = hp_sheet.get_image(2745, 171, 305, 19)
hp_100 = hp_sheet.get_image(0, 190, 305, 19)
# energy bars ----------------------------------------------------------------------------------------------------------
en_sheet = SpriteSheet(resource_urls.en_url)
en_0 = en_sheet.get_image(0, 0, 305, 19)
en_1 = en_sheet.get_image(305, 0, 305, 19)
en_2 = en_sheet.get_image(610, 0, 305, 19)
en_3 = en_sheet.get_image(915, 0, 305, 19)
en_4 = en_sheet.get_image(1220, 0, 305, 19)
en_5 = en_sheet.get_image(1525, 0, 305, 19)
en_6 = en_sheet.get_image(1830, 0, 305, 19)
en_7 = en_sheet.get_image(2135, 0, 305, 19)
en_8 = en_sheet.get_image(2440, 0, 305, 19)
en_9 = en_sheet.get_image(2745, 0, 305, 19)
en_10 = en_sheet.get_image(0, 19, 305, 19)
en_11 = en_sheet.get_image(305, 19, 305, 19)
en_12 = en_sheet.get_image(610, 19, 305, 19)
en_13 = en_sheet.get_image(915, 19, 305, 19)
en_14 = en_sheet.get_image(1220, 19, 305, 19)
en_15 = en_sheet.get_image(1525, 19, 305, 19)
en_16 = en_sheet.get_image(1830, 19, 305, 19)
en_17 = en_sheet.get_image(2135, 19, 305, 19)
en_18 = en_sheet.get_image(2440, 19, 305, 19)
en_19 = en_sheet.get_image(2745, 19, 305, 19)
en_20 = en_sheet.get_image(0, 38, 305, 19)
en_21 = en_sheet.get_image(305, 38, 305, 19)
en_22 = en_sheet.get_image(610, 38, 305, 19)
en_23 = en_sheet.get_image(915, 38, 305, 19)
en_24 = en_sheet.get_image(1220, 38, 305, 19)
en_25 = en_sheet.get_image(1525, 38, 305, 19)
en_26 = en_sheet.get_image(1830, 38, 305, 19)
en_27 = en_sheet.get_image(2135, 38, 305, 19)
en_28 = en_sheet.get_image(2440, 38, 305, 19)
en_29 = en_sheet.get_image(2745, 38, 305, 19)
en_30 = en_sheet.get_image(0, 57, 305, 19)
en_31 = en_sheet.get_image(305, 57, 305, 19)
en_32 = en_sheet.get_image(610, 57, 305, 19)
en_33 = en_sheet.get_image(915, 57, 305, 19)
en_34 = en_sheet.get_image(1220, 57, 305, 19)
en_35 = en_sheet.get_image(1525, 57, 305, 19)
en_36 = en_sheet.get_image(1830, 57, 305, 19)
en_37 = en_sheet.get_image(2135, 57, 305, 19)
en_38 = en_sheet.get_image(2440, 57, 305, 19)
en_39 = en_sheet.get_image(2745, 57, 305, 19)
en_40 = en_sheet.get_image(0, 76, 305, 19)
en_41 = en_sheet.get_image(305, 76, 305, 19)
en_42 = en_sheet.get_image(610, 76, 305, 19)
en_43 = en_sheet.get_image(915, 76, 305, 19)
en_44 = en_sheet.get_image(1220, 76, 305, 19)
en_45 = en_sheet.get_image(1525, 76, 305, 19)
en_46 = en_sheet.get_image(1830, 76, 305, 19)
en_47 = en_sheet.get_image(2135, 76, 305, 19)
en_48 = en_sheet.get_image(2440, 76, 305, 19)
en_49 = en_sheet.get_image(2745, 76, 305, 19)
en_50 = en_sheet.get_image(0, 95, 305, 19)
en_51 = en_sheet.get_image(305, 95, 305, 19)
en_52 = en_sheet.get_image(610, 95, 305, 19)
en_53 = en_sheet.get_image(915, 95, 305, 19)
en_54 = en_sheet.get_image(1220, 95, 305, 19)
en_55 = en_sheet.get_image(1525, 95, 305, 19)
en_56 = en_sheet.get_image(1830, 95, 305, 19)
en_57 = en_sheet.get_image(2135, 95, 305, 19)
en_58 = en_sheet.get_image(2440, 95, 305, 19)
en_59 = en_sheet.get_image(2745, 95, 305, 19)
en_60 = en_sheet.get_image(0, 114, 305, 19)
en_61 = en_sheet.get_image(305, 114, 305, 19)
en_62 = en_sheet.get_image(610, 114, 305, 19)
en_63 = en_sheet.get_image(915, 114, 305, 19)
en_64 = en_sheet.get_image(1220, 114, 305, 19)
en_65 = en_sheet.get_image(1525, 114, 305, 19)
en_66 = en_sheet.get_image(1830, 114, 305, 19)
en_67 = en_sheet.get_image(2135, 114, 305, 19)
en_68 = en_sheet.get_image(2440, 114, 305, 19)
en_69 = en_sheet.get_image(2745, 114, 305, 19)
en_70 = en_sheet.get_image(0, 133, 305, 19)
en_71 = en_sheet.get_image(305, 133, 305, 19)
en_72 = en_sheet.get_image(610, 133, 305, 19)
en_73 = en_sheet.get_image(915, 133, 305, 19)
en_74 = en_sheet.get_image(1220, 133, 305, 19)
en_75 = en_sheet.get_image(1525, 133, 305, 19)
en_76 = en_sheet.get_image(1830, 133, 305, 19)
en_77 = en_sheet.get_image(2135, 133, 305, 19)
en_78 = en_sheet.get_image(2440, 133, 305, 19)
en_79 = en_sheet.get_image(2745, 133, 305, 19)
en_80 = en_sheet.get_image(0, 152, 305, 19)
en_81 = en_sheet.get_image(305, 152, 305, 19)
en_82 = en_sheet.get_image(610, 152, 305, 19)
en_83 = en_sheet.get_image(915, 152, 305, 19)
en_84 = en_sheet.get_image(1220, 152, 305, 19)
en_85 = en_sheet.get_image(1525, 152, 305, 19)
en_86 = en_sheet.get_image(1830, 152, 305, 19)
en_87 = en_sheet.get_image(2135, 152, 305, 19)
en_88 = en_sheet.get_image(2440, 152, 305, 19)
en_89 = en_sheet.get_image(2745, 152, 305, 19)
en_90 = en_sheet.get_image(0, 171, 305, 19)
en_91 = en_sheet.get_image(305, 171, 305, 19)
en_92 = en_sheet.get_image(610, 171, 305, 19)
en_93 = en_sheet.get_image(915, 171, 305, 19)
en_94 = en_sheet.get_image(1220, 171, 305, 19)
en_95 = en_sheet.get_image(1525, 171, 305, 19)
en_96 = en_sheet.get_image(1830, 171, 305, 19)
en_97 = en_sheet.get_image(2135, 171, 305, 19)
en_98 = en_sheet.get_image(2440, 171, 305, 19)
en_99 = en_sheet.get_image(2745, 171, 305, 19)
en_100 = en_sheet.get_image(0, 190, 305, 19)
# energy bars ----------------------------------------------------------------------------------------------------------
xp_sheet = SpriteSheet(resource_urls.xp_url)
xp_0 = xp_sheet.get_image(0, 0, 305, 19)
xp_1 = xp_sheet.get_image(305, 0, 305, 19)
xp_2 = xp_sheet.get_image(610, 0, 305, 19)
xp_3 = xp_sheet.get_image(915, 0, 305, 19)
xp_4 = xp_sheet.get_image(1220, 0, 305, 19)
xp_5 = xp_sheet.get_image(1525, 0, 305, 19)
xp_6 = xp_sheet.get_image(1830, 0, 305, 19)
xp_7 = xp_sheet.get_image(2135, 0, 305, 19)
xp_8 = xp_sheet.get_image(2440, 0, 305, 19)
xp_9 = xp_sheet.get_image(2745, 0, 305, 19)
xp_10 = xp_sheet.get_image(0, 19, 305, 19)
xp_11 = xp_sheet.get_image(305, 19, 305, 19)
xp_12 = xp_sheet.get_image(610, 19, 305, 19)
xp_13 = xp_sheet.get_image(915, 19, 305, 19)
xp_14 = xp_sheet.get_image(1220, 19, 305, 19)
xp_15 = xp_sheet.get_image(1525, 19, 305, 19)
xp_16 = xp_sheet.get_image(1830, 19, 305, 19)
xp_17 = xp_sheet.get_image(2135, 19, 305, 19)
xp_18 = xp_sheet.get_image(2440, 19, 305, 19)
xp_19 = xp_sheet.get_image(2745, 19, 305, 19)
xp_20 = xp_sheet.get_image(0, 38, 305, 19)
xp_21 = xp_sheet.get_image(305, 38, 305, 19)
xp_22 = xp_sheet.get_image(610, 38, 305, 19)
xp_23 = xp_sheet.get_image(915, 38, 305, 19)
xp_24 = xp_sheet.get_image(1220, 38, 305, 19)
xp_25 = xp_sheet.get_image(1525, 38, 305, 19)
xp_26 = xp_sheet.get_image(1830, 38, 305, 19)
xp_27 = xp_sheet.get_image(2135, 38, 305, 19)
xp_28 = xp_sheet.get_image(2440, 38, 305, 19)
xp_29 = xp_sheet.get_image(2745, 38, 305, 19)
xp_30 = xp_sheet.get_image(0, 57, 305, 19)
xp_31 = xp_sheet.get_image(305, 57, 305, 19)
xp_32 = xp_sheet.get_image(610, 57, 305, 19)
xp_33 = xp_sheet.get_image(915, 57, 305, 19)
xp_34 = xp_sheet.get_image(1220, 57, 305, 19)
xp_35 = xp_sheet.get_image(1525, 57, 305, 19)
xp_36 = xp_sheet.get_image(1830, 57, 305, 19)
xp_37 = xp_sheet.get_image(2135, 57, 305, 19)
xp_38 = xp_sheet.get_image(2440, 57, 305, 19)
xp_39 = xp_sheet.get_image(2745, 57, 305, 19)
xp_40 = xp_sheet.get_image(0, 76, 305, 19)
xp_41 = xp_sheet.get_image(305, 76, 305, 19)
xp_42 = xp_sheet.get_image(610, 76, 305, 19)
xp_43 = xp_sheet.get_image(915, 76, 305, 19)
xp_44 = xp_sheet.get_image(1220, 76, 305, 19)
xp_45 = xp_sheet.get_image(1525, 76, 305, 19)
xp_46 = xp_sheet.get_image(1830, 76, 305, 19)
xp_47 = xp_sheet.get_image(2135, 76, 305, 19)
xp_48 = xp_sheet.get_image(2440, 76, 305, 19)
xp_49 = xp_sheet.get_image(2745, 76, 305, 19)
xp_50 = xp_sheet.get_image(0, 95, 305, 19)
xp_51 = xp_sheet.get_image(305, 95, 305, 19)
xp_52 = xp_sheet.get_image(610, 95, 305, 19)
xp_53 = xp_sheet.get_image(915, 95, 305, 19)
xp_54 = xp_sheet.get_image(1220, 95, 305, 19)
xp_55 = xp_sheet.get_image(1525, 95, 305, 19)
xp_56 = xp_sheet.get_image(1830, 95, 305, 19)
xp_57 = xp_sheet.get_image(2135, 95, 305, 19)
xp_58 = xp_sheet.get_image(2440, 95, 305, 19)
xp_59 = xp_sheet.get_image(2745, 95, 305, 19)
xp_60 = xp_sheet.get_image(0, 114, 305, 19)
xp_61 = xp_sheet.get_image(305, 114, 305, 19)
xp_62 = xp_sheet.get_image(610, 114, 305, 19)
xp_63 = xp_sheet.get_image(915, 114, 305, 19)
xp_64 = xp_sheet.get_image(1220, 114, 305, 19)
xp_65 = xp_sheet.get_image(1525, 114, 305, 19)
xp_66 = xp_sheet.get_image(1830, 114, 305, 19)
xp_67 = xp_sheet.get_image(2135, 114, 305, 19)
xp_68 = xp_sheet.get_image(2440, 114, 305, 19)
xp_69 = xp_sheet.get_image(2745, 114, 305, 19)
xp_70 = xp_sheet.get_image(0, 133, 305, 19)
xp_71 = xp_sheet.get_image(305, 133, 305, 19)
xp_72 = xp_sheet.get_image(610, 133, 305, 19)
xp_73 = xp_sheet.get_image(915, 133, 305, 19)
xp_74 = xp_sheet.get_image(1220, 133, 305, 19)
xp_75 = xp_sheet.get_image(1525, 133, 305, 19)
xp_76 = xp_sheet.get_image(1830, 133, 305, 19)
xp_77 = xp_sheet.get_image(2135, 133, 305, 19)
xp_78 = xp_sheet.get_image(2440, 133, 305, 19)
xp_79 = xp_sheet.get_image(2745, 133, 305, 19)
xp_80 = xp_sheet.get_image(0, 152, 305, 19)
xp_81 = xp_sheet.get_image(305, 152, 305, 19)
xp_82 = xp_sheet.get_image(610, 152, 305, 19)
xp_83 = xp_sheet.get_image(915, 152, 305, 19)
xp_84 = xp_sheet.get_image(1220, 152, 305, 19)
xp_85 = xp_sheet.get_image(1525, 152, 305, 19)
xp_86 = xp_sheet.get_image(1830, 152, 305, 19)
xp_87 = xp_sheet.get_image(2135, 152, 305, 19)
xp_88 = xp_sheet.get_image(2440, 152, 305, 19)
xp_89 = xp_sheet.get_image(2745, 152, 305, 19)
xp_90 = xp_sheet.get_image(0, 171, 305, 19)
xp_91 = xp_sheet.get_image(305, 171, 305, 19)
xp_92 = xp_sheet.get_image(610, 171, 305, 19)
xp_93 = xp_sheet.get_image(915, 171, 305, 19)
xp_94 = xp_sheet.get_image(1220, 171, 305, 19)
xp_95 = xp_sheet.get_image(1525, 171, 305, 19)
xp_96 = xp_sheet.get_image(1830, 171, 305, 19)
xp_97 = xp_sheet.get_image(2135, 171, 305, 19)
xp_98 = xp_sheet.get_image(2440, 171, 305, 19)
xp_99 = xp_sheet.get_image(2745, 171, 305, 19)
xp_100 = xp_sheet.get_image(0, 190, 305, 19)

# creating objects from defined classes --------------------------------------------------------------------------------
# display notifications to user (shown, x_coordinate, y_coordinate, image, color) --------------------------------------
knowledge_academia = Notification("knowledge academia notification", False, 510, 365, knowledge_popup)
rest_recover = Notification("rest recover", False, 510, 365, health_popup)
shop_gear = Notification("shop gear", False, 510, 365, gear_popup)
# inventory items ------------------------------------------------------------------------------------------------------
health_potion = Item("health potion", "potion", 200, 200, health_pot_img)
energy_potion = Item("energy potion", "potion", 200, 200, energy_pot_img)
shiny_rock = Item("shiny rock", "rock", 200, 200, shiny_rock_img)
bone_dust = Item("bone dust", "dust", 200, 200, bone_dust_img)
# starter equipment ----------------------------------------------------------------------------------------------------
basic_staff = Item("basic staff", "mage", 200, 200, basic_staff_img)
basic_sword = Item("basic sword", "fighter", 200, 200, basic_sword_img)
basic_bow = Item("basic bow", "scout", 200, 200, basic_bow_img)
basic_robes = Item("basic robes", "mage", 200, 200, basic_robes_img)
basic_armor = Item("basic armor", "fighter", 200, 200, basic_armor_img)
basic_tunic = Item("basic tunic", "scout", 200, 200, basic_tunic_img)

# character selection screen display characters ------------------------------------------------------------------------
amuna_character = UiElement("amuna character", 640, 360, amuna_character_img, False)
nuldar_character = UiElement("nuldar character", 640, 360, nuldar_character_img, False)
sorae_character = UiElement("sorae character", 640, 360, sorae_character_img, False)

# default player character ---------------------------------------------------------------------------------------------
player = Player("stane", "male", "amuna", "",  # name, gender, race, role
                [health_potion, energy_potion],  # inventory
                {"weapon": "", "chest": ""},  # equipment ('type', 'name')
                # current quests, quest progress (x/4), quest status (quest: done)
                {"sneaky snakes": "Speak to Garan to start this quest.",
                 "village repairs": "Speak to Maurelle to start this quest.",
                 "ghouled again": "Speak to the gate Guard to start this quest.",
                 "": ""},
                {"sneaky snakes": 0, "village repairs": 0, "ghouled again": 0},  # quest progress (x/4)
                {"sneaky snakes": False, "village repairs": False, "ghouled again": False},  # quest status
                {"sneaky snakes": False, "village repairs": False, "ghouled again": False},  # quest complete
                {"mage": 60, "fighter": 60, "scout": 60},  # role knowledge ('role', 'amount')
                {"skill 2": "", "skill 3": "", "skill 4": ""},  # mage skills
                {"skill 2": "", "skill 3": "", "skill 4": ""},  # fighter skills
                {"skill 2": "", "skill 3": "", "skill 4": ""},  # scout skills
                1, 0, 100, 100,  # lvl, exp, health, energy
                True, 20, {"amuna": 0, "nuldar": 0, "sorae": 0},  # alive, rupees, reputation
                "", "", 0, 0, player_no_role_amuna_down)  # mount, zone, defence, offense, image

# nps: name, gender, race, role, dialog, quest, quest_description, x_coordinate, y_coordinate --------------------------
#                  alive_status, quest_complete, items, gift, image, color
npc_garan = NPC("garan", "male", "amuna", "rogue", "It's dangerous to go alone.", "Stupid Snakes", "", 210, 430,
                True, False, ["Items"], False, garan_down)
npc_maurelle = NPC("maurelle", "female", "amuna", "mage", "We need help!", "Village Repairs", "", 760, 520,
                   True, False, ["Items"], False, maurelle_down)
npc_guard = NPC("guard", "male", "amuna", "fighter", "Another day.", "Ghouled Again", "", 430, 120,
                True, False, ["Items"], False, guard_down)
npc_amuna_shopkeeper = Shopkeeper("amuna shopkeeper", "amuna", [
    Item("health potion", "potion", 200, 200, health_pot_img),
    Item("energy potion", "potion", 200, 200, energy_pot_img),
    Item("basic staff", "mage", 200, 200, basic_staff_img),
    Item("basic sword", "fighter", 200, 200, basic_sword_img),
    Item("basic bow", "scout", 200, 200, basic_bow_img),
    Item("basic robes", "mage", 200, 200, basic_robes_img),
    Item("basic armor", "fighter", 200, 200, basic_armor_img),
    Item("basic tunic", "scout", 200, 200, basic_tunic_img)])
npc_garan_interaction = UiElement("garan interaction", 650, 350, garan_interaction, False)
npc_maurelle_interaction = UiElement("maurelle interaction", 650, 350, maurelle_interaction, False)
npc_guard_interaction = UiElement("guard interaction", 650, 350, guard_interaction, False)
# ----------------------------------------------------------------------------------------------------------------------
# enemies: kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image, color, health bar ------
snake_1 = Enemy("snake", "snake", 100, 100, 1, 80, 130, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_img), snake,
                UiElement("snake hp bar", 700, 90, hp_100, False))
snake_2 = Enemy("snake", "snake", 100, 100, 2, 285, 150, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_img), snake,
                UiElement("snake hp bar", 700, 90, hp_100, False))
snake_3 = Enemy("snake", "snake", 100, 100, 1, 80, 230, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_img), snake,
                UiElement("snake hp bar", 700, 90, hp_100, False))
snake_4 = Enemy("snake", "snake", 100, 100, 2, 285, 250, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_img), snake,
                UiElement("snake hp bar", 700, 90, hp_100, False))
ghoul_low_1 = Enemy("ghoul", "ghoul", 100, 100, 4, 665, 180, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_img), ghoul,
                    UiElement("ghoul hp bar", 700, 90, hp_100, False))
ghoul_low_2 = Enemy("ghoul", "ghoul", 100, 100, 5, 800, 130, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_img), ghoul,
                    UiElement("ghoul hp bar", 700, 90, hp_100, False))
ghoul_low_3 = Enemy("ghoul", "ghoul", 100, 100, 3, 760, 240, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_img), ghoul,
                    UiElement("ghoul hp bar", 700, 90, hp_100, False))
ghoul_low_4 = Enemy("ghoul", "ghoul", 100, 100, 4, 890, 205, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_img), ghoul,
                    UiElement("ghoul hp bar", 700, 90, hp_100, False))
# environmental objects: name, model, x_coordinate, y_coordinate, gathered, image --------------------------------------
pine_tree_1 = Tree("tree", "pine tree", 80, 445, False, pygame.image.load(resource_urls.pine_tree).convert())
pine_tree_2 = Tree("tree", "pine tree", 260, 590, False, pygame.image.load(resource_urls.pine_tree).convert())
pine_tree_3 = Tree("tree", "pine tree", 340, 400, False, pygame.image.load(resource_urls.pine_tree).convert())
seldon_grass_1 = Item("grass", "seldon grass", 360, 125, pygame.image.load(resource_urls.seldon_grass).convert())
seldon_grass_2 = Item("grass", "seldon grass", 270, 195, pygame.image.load(resource_urls.seldon_grass).convert())
seldon_grass_3 = Item("grass", "seldon grass", 405, 235, pygame.image.load(resource_urls.seldon_grass).convert())
seldon_grass_4 = Item("grass", "seldon grass", 165, 135, pygame.image.load(resource_urls.seldon_grass).convert())
seldon_grass_5 = Item("grass", "seldon grass", 150, 255, pygame.image.load(resource_urls.seldon_grass).convert())
seldon_grass_6 = Item("grass", "seldon grass", 50, 180, pygame.image.load(resource_urls.seldon_grass).convert())
seldon_flower_1 = Item("flower", "seldon flower", 590, 410,
                       pygame.image.load(resource_urls.seldon_flower).convert())
seldon_flower_2 = Item("flower", "seldon flower", 705, 600,
                       pygame.image.load(resource_urls.seldon_flower).convert())
seldon_flower_3 = Item("flower", "seldon flower", 800, 440,
                       pygame.image.load(resource_urls.seldon_flower).convert())
# buildings: name, model, x_coordinate, y_coordinate, image, color -----------------------------------------------------
seldon_inn = Building("inn", "seldon inn", 635, 600, amuna_inn_building)
seldon_shop = Building("shop", "seldon shop", 665, 400, amuna_shop_building)
seldon_academia = Building("academia", "seldon academia", 875, 440, amuna_academia_building)
seldon_hearth = Building("hearth", "seldon hearth", 860, 595, pygame.image.load(resource_urls.hearth_stone).convert())
rohir_gate = UiElement("rohir gate", 525, 40, pygame.image.load(resource_urls.rohir_gate).convert(), False)
# ui elements: name, x_coordinate, y_coordinate, image, color, update flag ---------------------------------------------
character_button = UiElement("character button", 860, 680, character_button_img, False)
journal_button = UiElement("journal button", 970, 680, journal_button_img, False)
# start screen elements ------------------------------------------------------------------------------------------------
new_game_button = UiElement("new game button", 640, 342, new_game_img, False)
continue_button = UiElement("continue button", 640, 425, continue_img, False)
amuna_button = UiElement("amuna button", 100, 255, amuna_button_img, False)
nuldar_button = UiElement("nuldar button", 100, 350, nuldar_button_img, False)
sorae_button = UiElement("sorae button", 100, 445, sorae_button_img, False)
character_select_overlay = UiElement("character select overlay", 640, 365,
                                     pygame.image.load(resource_urls.character_select_overlay_url).convert(), False)
amuna_select_overlay = UiElement("amuna select overlay", 1140, 305,
                                     pygame.image.load(resource_urls.amuna_select_overlay_url).convert(), False)
nuldar_select_overlay = UiElement("nuldar select overlay", 1140, 305,
                                     pygame.image.load(resource_urls.nuldar_select_overlay_url).convert(), False)
sorae_select_overlay = UiElement("sorae select overlay", 1140, 305,
                                     pygame.image.load(resource_urls.sorae_select_overlay_url).convert(), False)
start_button = UiElement("start button", 640, 660, pygame.image.load(resource_urls.start_button).convert(), False)
name_input = UiElement("name input", 640, 585, name_input_img, False)
# ----------------------------------------------------------------------------------------------------------------------
lets_go_button = UiElement("lets go button", 625, 575,
                           pygame.image.load(resource_urls.lets_go_button).convert(), False)
buy_button = UiElement("buy button", 860, 680, buy_button_img, False)
leave_button = UiElement("leave button", 970, 680, leave_button_img, False)
rest_button = UiElement("rest button", 860, 680, rest_button_img, False)
mage_learn_button = UiElement("mage learn button", 650, 250,
                              pygame.image.load(resource_urls.learn_button).convert(), False)
fighter_learn_button = UiElement("fighter learn button", 420, 330,
                                 pygame.image.load(resource_urls.learn_button).convert(), False)
scout_learn_button = UiElement("scout learn button", 560, 410,
                               pygame.image.load(resource_urls.learn_button).convert(), False)
barrier_learn_button = UiElement("barrier learn button", 505, 300,
                                 pygame.image.load(resource_urls.skill_learn_button).convert(), False)
hard_strike_learn_button = UiElement("hard strike learn button", 505, 300,
                                     pygame.image.load(resource_urls.skill_learn_button).convert(), False)
sharp_sense_learn_button = UiElement("sharp sense learn button", 505, 300,
                                     pygame.image.load(resource_urls.skill_learn_button).convert(), False)
hearth_button = UiElement("hearth button", 970, 25, pygame.image.load(resource_urls.hearth_button).convert(), False)
close_button = UiElement("close button", 975, 135, pygame.image.load(resource_urls.close_button).convert(), False)
quest_button = UiElement("quest button", 860, 680, quest_button_img, False)
accept_button = UiElement("accept button", 340, 670, accept_button_img, False)
decline_button = UiElement("decline button", 450, 670, decline_button_img, False)
# ----------------------------------------------------------------------------------------------------------------------
skill_bar = UiElement("skill bar", 855, 615, pygame.image.load(resource_urls.skill_bar).convert(), False)
no_role_attack_button = UiElement("no role attack button", 750, 627, no_role_attack_button_img, False)
mage_attack_button = UiElement("mage attack button", 750, 627, mage_attack_button_img, False)
fighter_attack_button = UiElement("fighter attack button", 750, 627, fighter_attack_button_img, False)
scout_attack_button = UiElement("scout attack button", 750, 627, scout_attack_button_img, False)
barrier_button = UiElement("barrier button", 820, 627, barrier_button_img, False)
hard_strike_button = UiElement("hard strike button", 820, 627, strike_button_img, False)
sharp_sense_button = UiElement("sharp sense button", 820, 627, sense_button_img, False)
# ----------------------------------------------------------------------------------------------------------------------
enemy_status = UiElement("enemy status", 855, 680, pygame.image.load(resource_urls.enemy_status).convert(), False)
hp_bar = UiElement("health bar", 165, 25, hp_100, False)
en_bar = UiElement("energy bar", 165, 45, en_100, False)
xp_bar = UiElement("xp bar", 165, 65, xp_100, False)
inventory = Inventory("inventory", [], 890, 515, pygame.image.load(resource_urls.inventory).convert(), False)
journal = UiElement("journal", 770, 380, journal_window_img, False)
level_up_win = UiElement("level up window", 520, 375, pygame.image.load(resource_urls.level_up).convert(), False)
character_sheet = UiElement("character sheet", 770, 380, character_window_img, False)
mage_book = UiElement("mage book", 670, 375, mage_book_img, False)
fighter_book = UiElement("fighter book", 670, 375, fighter_book_img, False)
scout_book = UiElement("scout book", 670, 375, scout_book_img, False)
quest_logs_1 = Item("quest logs", "quest", 60, 540, pygame.image.load(resource_urls.quest_logs).convert())
quest_logs_2 = Item("quest logs", "quest", 315, 560, pygame.image.load(resource_urls.quest_logs).convert())
quest_logs_3 = Item("quest logs", "quest", 415, 435, pygame.image.load(resource_urls.quest_logs).convert())
quest_logs_4 = Item("quest logs", "quest", 100, 540, pygame.image.load(resource_urls.quest_logs).convert())
npc_name_plate = UiElement("npc name plate", 640, 192, pygame.image.load(resource_urls.npc_name_plate).convert(), False)
# instance windows -----------------------------------------------------------------------------------------------------
buy_inventory = Inventory("buy inventory", [], 900, 500, pygame.image.load(resource_urls.buy_inventory).convert(),
                          False)
knowledge_window = UiElement("knowledge window", 635, 680, pygame.image.load(resource_urls.knowledge_window).convert(),
                             False)
garan_quest_window = UiElement("garan quest window", 262, 442, garan_quest, False)
maurelle_quest_window = UiElement("maurelle quest window", 262, 442, maurelle_quest, False)
guard_quest_window = UiElement("guard quest window", 262, 442, guard_quest, False)
# ----------------------------------------------------------------------------------------------------------------------
message_box = UiElement("message box", 173, 650, pygame.image.load(resource_urls.message_box), False)
status_bar_backdrop = UiElement("bar backdrop", 165, 45, pygame.image.load(resource_urls.bar_backdrop), False)
enemy_status_bar_backdrop = UiElement("enemy bar backdrop", 700, 90,
                                      pygame.image.load(resource_urls.enemy_bar_backdrop), False)
quest_star_garan = UiElement("quest star garan", 210, 390, quest_start_star, False)
quest_star_maurelle = UiElement("quest star maurelle", 760, 480, quest_start_star, False)
quest_star_guard = UiElement("quest star guard", 430, 75, quest_start_star, False)
# battle sprites -------------------------------------------------------------------------------------------------------
player_battle_sprite = BattleCharacter("stan battle", 320, 460, player_no_role_battle)
snake_battle_sprite = BattleCharacter("snake battle", 715, 250, snake_battle)
ghoul_battle_sprite = BattleCharacter("ghoul battle", 700, 250, ghoul_battle)

# setting font and size for text to screen updates ---------------------------------------------------------------------
font = pygame.font.SysFont('freesansbold.ttf', 16, bold=True, italic=False)
name_input_font = pygame.font.SysFont('freesansbold.ttf', 32, bold=True, italic=False)

# groups for sprites ---------------------------------------------------------------------------------------------------
quest_items = pygame.sprite.Group()
npcs = pygame.sprite.Group()
enemies = pygame.sprite.Group()
trees = pygame.sprite.Group()
grass = pygame.sprite.Group()
flowers = pygame.sprite.Group()
buildings = pygame.sprite.Group()
environment_objects = pygame.sprite.Group()
user_interface = pygame.sprite.Group()
conditional_interface = pygame.sprite.Group()
battle_elements = pygame.sprite.Group()
enemy_hp_bars = pygame.sprite.Group()
most_sprites = pygame.sprite.Group()
game_over_screen_sprites = pygame.sprite.Group()
non_sprite_sheets = pygame.sprite.Group()
# specific enemy groups for movement and respawn -----------------------------------------------------------------------
snakes = pygame.sprite.Group()
snakes.add(snake_1, snake_2, snake_3, snake_4)
ghouls = pygame.sprite.Group()
ghouls.add(ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)
# adding most sprite objects to groups ---------------------------------------------------------------------------------
npcs.add(npc_garan, npc_maurelle, npc_guard)
enemies.add(snake_1, snake_2, snake_3, snake_4, ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)
trees.add(pine_tree_1, pine_tree_2, pine_tree_3)
grass.add(seldon_grass_1, seldon_grass_2, seldon_grass_3, seldon_grass_4, seldon_grass_5, seldon_grass_6)
flowers.add(seldon_flower_1, seldon_flower_2, seldon_flower_3)
buildings.add(seldon_inn, seldon_shop, seldon_academia)
user_interface.add(rest_button, buy_button, leave_button, character_button, journal_button, hearth_button, message_box)
conditional_interface.add(buy_inventory, character_sheet, journal, level_up_win, mage_book, fighter_book, scout_book,
                          mage_learn_button, fighter_learn_button, scout_learn_button, barrier_learn_button,
                          hard_strike_learn_button, sharp_sense_learn_button, close_button)
game_over_screen_sprites.add(lets_go_button)
# all environment sprites for collision detection ----------------------------------------------------------------------
environment_objects.add(trees, buildings)
# quest item sprites for gathering -------------------------------------------------------------------------------------
quest_items.add(quest_logs_1, quest_logs_2, quest_logs_3, quest_logs_4, rohir_gate)
# battle element sprites for combat scenario ---------------------------------------------------------------------------
battle_elements.add(player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, enemy_status, skill_bar,
                    mage_attack_button, scout_attack_button, fighter_attack_button, barrier_button, hard_strike_button,
                    sharp_sense_button)
# adding most sprites to this group for drawing and related functions
most_sprites.add(npcs, trees, buildings, grass, flowers, quest_items, enemies, seldon_hearth)
# group to set transparency to sprites that don't have it set in the spritesheet class constructor
non_sprite_sheets.add(trees, grass, flowers, seldon_hearth, quest_items, skill_bar, lets_go_button,
                      mage_learn_button, fighter_learn_button, scout_learn_button,
                      barrier_learn_button, hard_strike_learn_button, sharp_sense_learn_button,
                      character_select_overlay, amuna_select_overlay, nuldar_select_overlay, sorae_select_overlay,
                      start_button)
for non_sprite_sheet_sprite in non_sprite_sheets:
    non_sprite_sheet_sprite.surf.set_colorkey((255, 255, 255), RLEACCEL)


# code related to sound effects that will be used later ----------------------------------------------------------------
# pygame.mixer.music.load("Electric_1.mp3")
# pygame.mixer.music.play(loops=-1)
# move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
# move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
# collision_sound = pygame.mixer.Sound("Collision.ogg")
# Set the base volume for all sounds
# move_up_sound.set_volume(0.5)
# move_down_sound.set_volume(0.5)
# collision_sound.set_volume(0.5)

# main loop variables --------------------------------------------------------------------------------------------------
game_running = True
new_game_chosen = False
continue_game_chosen = False
start_chosen = False
player_created = True
# conditions for character selection screen to switch screens
amuna_race_selected = True
nuldar_race_selected = False
sorae_race_selected = False
# condition to check if player has clicked on the name input text box
name_input_selected = False
# main iteration condition checks for player position
in_battle = False
in_shop = False
in_inn = False
in_academia = False
in_district_over_world = True
in_npc_interaction = False
in_korlok = False
# condition to check if player has chosen to interact with sprite
interacted = False
# condition to allow or block player movement (combat or npc interaction)
movement_able = True
# condition for battle sequences so that buttons can't be spam clicked
combat_cooldown = False
# condition to check if combat occurred on current game loop iteration to update sprites at end of loop
combat_happened = False
# condition to check if buy button is clicked in shop
buy_clicked = False
# condition to check if sell button is clicked in shop
sell_clicked = False
# condition to check if rest button is clicked in inn
rest_clicked = False
# condition to check if screen resize button has been clicked
screen_clicked = False
# conditions to check if role books have been clicked in academia
mage_learn_clicked = False
fighter_learn_clicked = False
scout_learn_clicked = False
# condition to check if the character button has been clicked
character_button_clicked = False
# condition to check if the journal button has been clicked
journal_button_clicked = False
# condition to check if window close button has been clicked
close_button_clicked = False
# condition to check if hearth button has been clicked to move player and set fade animation
hearth_clicked = False
# condition to check if player has hearthed
hearthed = False
# condition to keep message box text for amount of time, so it's not cleared when player is not in range of sprite
info_update = False
# condition to keep loot text for amount of time, so it's not cleared when player is not in range of sprite
loot_update = False
# condition to check if player has started combat encounter with enemy to clear message box (before adding combat text)
encounter_started = False
# condition to check if player has bought an item from shop
item_bought = False
# condition to check if player has sold an item to shop
item_sold = False
# condition to check if player has rested in an inn
rested = False
# conditions to check if player has a learned these skills from the academia
barrier_learned = False
hard_strike_learned = False
sharp_sense_learned = False
# condition to check if player gear has been checked for stat bonus
gear_checked = False
# condition to check if player weapon has been checked for stat bonus
weapon_checked = False
# conditions to check whether these role skills are active in loop
barrier_active = False
sharp_sense_active = False
# condition to check if initial player position has been set to current resolution scale
player_initial_pos_set = False
# condition that checks if inn screen has been faded when player rests
faded_inn_screen = False
# what zone the player is in, used for player update and map boundaries
zone_seldon = True
zone_korlok = False
zone_eldream = False
zone_marrow = False
# condition to check if fighter skill hard strike has been used for applying the animation
hard_strike = False
# condition to check if quest button has been clicked in npc interation
quest_clicked = False
# condition to check if garan has given player basic weapons when starting his quest
garan_gifted = False
# condition to check if knowledge notification has been shown to player
knowledge_academia_show = False
# condition to check if player has clicked on knowledge notification to hide it
knowledge_window_clicked = False
# condition to check if rest notification has been shown to player
rest_recover_show = False
# condition to check if player has clicked on rest notification to hide it
rest_window_clicked = False
# condition to check if gear notification has been shown to player
shop_gear_show = False
# condition to check if player has clicked on gear notification to hide it
shop_window_clicked = False
# string to store players current direction on key press for correctly displaying orientation on sprite update
# when changing gear/role etc.
current_direction = ""
# list to contain current player items for display
player_items = []
# list to contain current player equipment for display
player_equipment = []
# list to contain buy inventory window for display within shop
buy_shop_elements = []
# list to contain current shop items for display
shopkeeper_items = []
# list to contain screen size elements for display
display_elements = []
# list to contain character sheet text information
character_sheet_text = []
# list to contain character sheet window
character_sheet_window = []
# list to contain journal text information (quests)
journal_text = []
# list to contain journal window
journal_window = []
# list to contain level up text information
level_up_text = []
# list to contain level up window
level_up_window = []
# list to contain skill learn items for the academia instance
skill_learn_items = []
# list to contain books in academia instance for displaying
books = []
# list to contain quest related images and text for drawing in npc interaction
quest_box = []
# list to contain knowledge notification when player knowledge is 40
knowledge_academia_window = []
# list to contain rest notification when player health is less than 50
rest_recover_window = []
# list to contain gear notification when player gets weapon
shop_gear_window = []
# combat text strings to be updated on scenario, shown on UI message box
# initially set to these default strings but will be overwritten
info_text_1 = ""
info_text_2 = ""
info_text_3 = ""
info_text_4 = ""
# string to get character name input from user when selecting a character
character_name_input = ''
# text updates from battle instance to apply to main over-world message box
battle_info_to_return_to_main_loop = {"experience": 0, "item dropped": "", "leveled_up": False, "knowledge": ""}

enemy_tic = time.perf_counter()
npc_tic = time.perf_counter()
info_tic = time.perf_counter()
loot_tic = time.perf_counter()

# ----------------------------------------------------------------------------------------------------------------------
# main loop ------------------------------------------------------------------------------------------------------------
while game_running:
    if not new_game_chosen and not continue_game_chosen and not start_chosen:
        screen.blit(start_screen, (0, 0))
        screen.blit(new_game_button.surf, new_game_button.rect)
        screen.blit(continue_button.surf, continue_button.rect)

        # ---------------------------------------------------------------------------------------------------------------
        # user input events such as key presses or UI interaction
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # player chooses to start a new game or continue from previous
                if new_game_button.rect.collidepoint(pos):
                    new_game_chosen = True
                if continue_button.rect.collidepoint(pos):
                    continue_game_chosen = True
            elif event.type == QUIT:
                exit()
        pygame.display.flip()

    # ------------------------------------------------------------------------------------------------------------------
    # character selection for new game ---------------------------------------------------------------------------------
    if new_game_chosen:
        if amuna_race_selected:
            screen.blit(amuna_character_screen, (0, 0))
            screen.blit(character_select_overlay.surf, character_select_overlay.rect)
            screen.blit(amuna_button.surf, amuna_button.rect)
            screen.blit(nuldar_button.surf, nuldar_button.rect)
            screen.blit(sorae_button.surf, sorae_button.rect)
            screen.blit(amuna_select_overlay.surf, amuna_select_overlay.rect)
            screen.blit(amuna_character.surf, amuna_character.rect)
            screen.blit(start_button.surf, start_button.rect)
            screen.blit(name_input.surf, name_input.rect)
            character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
            screen.blit(character_name_surface, (605, 575))

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
                    if event.key == K_BACKSPACE:
                        if name_input_selected:
                            character_name_input = character_name_input[:-1]
                    else:
                        if name_input_selected:
                            if len(character_name_input) < 12:
                                character_name_input += event.unicode

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    # player amuna race selection, set conditions to go to amuna select screen
                    if amuna_button.rect.collidepoint(pos):
                        amuna_race_selected = True
                        nuldar_race_selected = False
                        sorae_race_selected = False
                    # player amuna race selection, set conditions to go to amuna select screen
                    if nuldar_button.rect.collidepoint(pos):
                        amuna_race_selected = False
                        nuldar_race_selected = True
                        sorae_race_selected = False
                    # player amuna race selection, set conditions to go to amuna select screen
                    if sorae_button.rect.collidepoint(pos):
                        amuna_race_selected = False
                        nuldar_race_selected = False
                        sorae_race_selected = True
                    # player clicks on the box to type name
                    if name_input.rect.collidepoint(pos):
                        if name_input_selected:
                            if len(character_name_input) < 1:
                                name_input.update(name_input.x_coordinate, name_input.y_coordinate, name_input_img)
                            name_input_selected = False
                        else:
                            name_input.update(name_input.x_coordinate, name_input.y_coordinate, name_input_empty_img)
                            name_input_selected = True
                    # get whatever the player typed in name box and chosen race and start game
                    if start_button.rect.collidepoint(pos):
                        if len(character_name_input) > 0:
                            player.name = str(character_name_input)
                        else:
                            player.name = "default"
                        player.race = "amuna"
                        player.surf = player_no_role_amuna_down
                        new_game_chosen = False
                        start_chosen = True

                elif event.type == QUIT:
                    exit()
            pygame.display.flip()

        if sorae_race_selected:
            screen.blit(sorae_character_screen, (0, 0))
            screen.blit(character_select_overlay.surf, character_select_overlay.rect)
            screen.blit(amuna_button.surf, amuna_button.rect)
            screen.blit(nuldar_button.surf, nuldar_button.rect)
            screen.blit(sorae_button.surf, sorae_button.rect)
            screen.blit(sorae_select_overlay.surf, sorae_select_overlay.rect)
            screen.blit(sorae_character.surf, sorae_character.rect)
            screen.blit(start_button.surf, start_button.rect)
            screen.blit(name_input.surf, name_input.rect)
            character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
            screen.blit(character_name_surface, (605, 575))

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
                    if event.key == K_BACKSPACE:
                        if name_input_selected:
                            character_name_input = character_name_input[:-1]
                    else:
                        if name_input_selected:
                            if len(character_name_input) < 12:
                                character_name_input += event.unicode

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    # player amuna race selection, set conditions to go to amuna select screen
                    if amuna_button.rect.collidepoint(pos):
                        amuna_race_selected = True
                        nuldar_race_selected = False
                        sorae_race_selected = False
                    # player amuna race selection, set conditions to go to amuna select screen
                    if nuldar_button.rect.collidepoint(pos):
                        amuna_race_selected = False
                        nuldar_race_selected = True
                        sorae_race_selected = False
                    # player amuna race selection, set conditions to go to amuna select screen
                    if sorae_button.rect.collidepoint(pos):
                        amuna_race_selected = False
                        nuldar_race_selected = False
                        sorae_race_selected = True
                    # player clicks on the box to type name
                    if name_input.rect.collidepoint(pos):
                        if name_input_selected:
                            if len(character_name_input) < 1:
                                name_input.update(name_input.x_coordinate, name_input.y_coordinate, name_input_img)
                            name_input_selected = False
                        else:
                            name_input.update(name_input.x_coordinate, name_input.y_coordinate,
                                              name_input_empty_img)
                            name_input_selected = True
                    # get whatever the player typed in name box and chosen race and start game
                    if start_button.rect.collidepoint(pos):
                        if len(character_name_input) > 0:
                            player.name = str(character_name_input)
                        else:
                            player.name = "default"
                        player.race = "sorae"
                        player.surf = player_no_role_sorae_down
                        new_game_chosen = False
                        start_chosen = True

                elif event.type == QUIT:
                    exit()
            pygame.display.flip()

        if nuldar_race_selected:
            screen.blit(nuldar_character_screen, (0, 0))
            screen.blit(character_select_overlay.surf, character_select_overlay.rect)
            screen.blit(amuna_button.surf, amuna_button.rect)
            screen.blit(nuldar_button.surf, nuldar_button.rect)
            screen.blit(sorae_button.surf, sorae_button.rect)
            screen.blit(nuldar_select_overlay.surf, nuldar_select_overlay.rect)
            screen.blit(nuldar_character.surf, nuldar_character.rect)
            screen.blit(start_button.surf, start_button.rect)
            screen.blit(name_input.surf, name_input.rect)
            character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
            screen.blit(character_name_surface, (605, 575))

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
                    if event.key == K_BACKSPACE:
                        if name_input_selected:
                            character_name_input = character_name_input[:-1]
                    else:
                        if name_input_selected:
                            if len(character_name_input) < 12:
                                character_name_input += event.unicode

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    # player amuna race selection, set conditions to go to amuna select screen
                    if amuna_button.rect.collidepoint(pos):
                        amuna_race_selected = True
                        nuldar_race_selected = False
                        sorae_race_selected = False
                    # player amuna race selection, set conditions to go to amuna select screen
                    if nuldar_button.rect.collidepoint(pos):
                        amuna_race_selected = False
                        nuldar_race_selected = True
                        sorae_race_selected = False
                    # player amuna race selection, set conditions to go to amuna select screen
                    if sorae_button.rect.collidepoint(pos):
                        amuna_race_selected = False
                        nuldar_race_selected = False
                        sorae_race_selected = True
                    # player clicks on the box to type name
                    if name_input.rect.collidepoint(pos):
                        if name_input_selected:
                            if len(character_name_input) < 1:
                                name_input.update(name_input.x_coordinate, name_input.y_coordinate, name_input_img)
                            name_input_selected = False
                        else:
                            name_input.update(name_input.x_coordinate, name_input.y_coordinate,
                                              name_input_empty_img)
                            name_input_selected = True
                    # get whatever the player typed in name box and chosen race and start game
                    if start_button.rect.collidepoint(pos):
                        if len(character_name_input) > 0:
                            player.name = str(character_name_input)
                        else:
                            player.name = "default"
                        player.race = "nuldar"
                        player.surf = player_no_role_sorae_down
                        new_game_chosen = False
                        start_chosen = True

                elif event.type == QUIT:
                    exit()
            pygame.display.flip()

    # if player has chosen to start game -------------------------------------------------------------------------------
    if start_chosen:
        # start game clock
        clock = pygame.time.Clock()
        font = pygame.font.SysFont('freesansbold.ttf', 22, bold=False, italic=False)
        level_up_font = pygame.font.SysFont('freesansbold.ttf', 35, bold=True, italic=False)

        # if player is currently alive
        if player.alive_status:
            # if player is in over world
            if in_district_over_world:
                screen.blit(seldon_district_bg, (0, 0))

                # ------------------------------------------------------------------------------------------------------
                # hearth button is clicked, sets fade transition for hearth screen and then back to district bg
                if hearth_clicked:
                    screen.fill((0, 0, 0))
                    for alpha in range(0, 200):
                        seldon_hearth_screen.set_alpha(alpha)
                        screen.blit(seldon_hearth_screen, (0, 0))
                        # flip sleep screen to display each iteration to show fade -------------------------------------
                        pygame.display.flip()
                    hearth_clicked = False
                    hearthed = True
                if hearthed:
                    screen.fill((0, 0, 0))
                    for alpha in range(0, 50):
                        seldon_district_bg.set_alpha(alpha)
                        screen.blit(seldon_district_bg, (0, 0))
                        # flip sleep screen to display each iteration to show fade -------------------------------------
                        pygame.display.flip()
                    seldon_district_bg.set_alpha(255)
                    screen.blit(seldon_district_bg, (0, 0))
                    pygame.display.flip()
                    hearthed = False
                    info_text_1 = "You recalled to the hearth stone."
                    info_update = True

                # ------------------------------------------------------------------------------------------------------
                info_toc = time.perf_counter()
                # clear info update after some time has passed
                if info_toc - info_tic > 2:
                    info_tic = time.perf_counter()
                    info_update = False
                loot_toc = time.perf_counter()
                # clear loot update after some time has passed
                if loot_toc - loot_tic > 4:
                    loot_tic = time.perf_counter()
                    loot_update = False

                # if player is not currently in range of sprite and there is not an active info update,
                # clear message box
                sprite = pygame.sprite.spritecollideany(player, most_sprites)
                if not sprite:
                    if not info_update:
                        info_text_1 = ""
                        info_text_2 = ""
                    if not loot_update:
                        info_text_3 = ""
                        info_text_4 = ""

                if zone_seldon:
                    player.current_zone = "seldon"
                if zone_korlok:
                    player.current_zone = "korlok"
                if zone_eldream:
                    player.current_zone = "eldream"
                if zone_marrow:
                    player.current_zone = "marrow"

                # switches between 1 and 0 to select a left or right direction for enemy sprite to move
                enemy_switch = 1
                # gets defeated enemy count and will respawn a new enemy type if count is greater than specified
                enemy_respawn()

                try:
                    for entity in most_sprites:
                        screen.blit(entity.surf, entity.rect)
                    for enemy_sprite in enemies:
                        screen.blit(enemy_sprite.surf, enemy_sprite.rect)
                    for ui_element in user_interface:
                        screen.blit(ui_element.surf, ui_element.rect)
                    for window in display_elements:
                        screen.blit(window.surf, window.rect)
                    for knowledge_window_notification in knowledge_academia_window:
                        screen.blit(knowledge_window_notification.surf, knowledge_window_notification.rect)
                    for rest_window in rest_recover_window:
                        screen.blit(rest_window.surf, rest_window.rect)
                    for gear_window in shop_gear_window:
                        screen.blit(gear_window.surf, gear_window.rect)
                    screen.blit(rohir_gate.surf, rohir_gate.rect)
                except TypeError:
                    pass

                # pop up notifications for situation stuff like low health or first weapon acquire ---------------------
                if not knowledge_academia_show:
                    if player.knowledge["mage"] == 40 or player.knowledge["fighter"] == 40 or \
                            player.knowledge["scout"] == 40:
                        knowledge_academia_window.append(knowledge_academia)
                        knowledge_academia_show = True
                if knowledge_academia_show:
                    if knowledge_window_clicked:
                        knowledge_academia_window.clear()
                if not rest_recover_show:
                    if player.health < 50:
                        rest_recover_window.append(rest_recover)
                        rest_recover_show = True
                if rest_recover_show:
                    if rest_window_clicked:
                        rest_recover_window.clear()
                if not shop_gear_show:
                    if player.quest_status["sneaky snakes"]:
                        shop_gear_window.append(shop_gear)
                        shop_gear_show = True
                if shop_gear_show:
                    if shop_window_clicked:
                        shop_gear_window.clear()

                # quest stars for npcs that update based on player quest progress
                # ------------------------------------------------------------------------------------------------------
                if not player.quest_complete["sneaky snakes"]:
                    screen.blit(quest_star_garan.surf, quest_star_garan.rect)
                if player.quest_progress["sneaky snakes"] == 4:
                    quest_star_garan.update(210, 390, quest_complete_star)
                if player.quest_status["sneaky snakes"] and player.quest_progress["sneaky snakes"] != 4:
                    quest_star_garan.update(210, 390, quest_progress_star)
                if not player.quest_complete["village repairs"]:
                    screen.blit(quest_star_maurelle.surf, quest_star_maurelle.rect)
                if player.quest_progress["village repairs"] == 4:
                    quest_star_maurelle.update(760, 480, quest_complete_star)
                if player.quest_status["village repairs"] and player.quest_progress["village repairs"] != 4:
                    quest_star_maurelle.update(760, 480, quest_progress_star)
                if not player.quest_complete["ghouled again"]:
                    screen.blit(quest_star_guard.surf, quest_star_guard.rect)
                if player.quest_progress["ghouled again"] == 4:
                    quest_star_guard.update(462, 80, quest_complete_star)
                if player.quest_status["ghouled again"] and player.quest_progress["ghouled again"] != 4:
                    quest_star_guard.update(462, 80, quest_progress_star)
                # ------------------------------------------------------------------------------------------------------

                # draw player and status bars
                screen.blit(player.surf, player.rect)
                screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                screen.blit(hp_bar.surf, hp_bar.rect)
                screen.blit(en_bar.surf, en_bar.rect)
                screen.blit(xp_bar.surf, xp_bar.rect)
                # draw texts to the screen, like message box, player rupees and level
                drawing_functions.text_info_draw(screen, player, font,
                                                 info_text_1, info_text_2, info_text_3, info_text_4)
                drawing_functions.draw_it(screen)
                # update players current inventory and status
                status_and_inventory_updates()
                # update players current equipment
                equipment_updates()
                # if players gear hasn't been checked, due to initial iteration or if equipment was updated
                # elsewhere, then check their current gear and apply stat bonus based on item equipped
                if not gear_checked:
                    gear_checked = gear_check()
                if not weapon_checked:
                    weapon_checked = weapon_check()
                # if battle happened, get battle info (item or experience gained) and apply to message box
                if battle_info_to_return_to_main_loop["item dropped"] != "":
                    if loot_update:
                        info_text_3 = str(battle_info_to_return_to_main_loop["item dropped"])
                        info_text_4 = str(battle_info_to_return_to_main_loop["experience"]) + "and " + \
                                      str(battle_info_to_return_to_main_loop["knowledge"])
                if battle_info_to_return_to_main_loop["leveled_up"]:
                    drawing_functions.level_up_draw(level_up_win, player, font, True)

                # ------------------------------------------------------------------------------------------------------
                # all in-game events such as key presses or UI interaction
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        # escape key was pressed, exit game
                        if event.key == K_ESCAPE:
                            exit()
                        # "F" key for player interaction
                        if event.key == K_f:
                            if pygame.sprite.spritecollideany(player, most_sprites):
                                interacted = True
                    # if the unstuck button was clicked, move the player to bottom right corner of screen
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if hearth_button.rect.collidepoint(pos):
                            hearth_clicked = True
                            player.pos = vec((850, 650))
                        # if character button is clicked, call draw function and show elements. second click hides
                        if character_button.rect.collidepoint(pos):
                            if character_button_clicked:
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, False)
                                character_button_clicked = False
                            else:
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, True)
                                character_button_clicked = True
                        # if journal button is clicked, call draw function and show elements. second click hides
                        if journal_button.rect.collidepoint(pos):
                            if journal_button_clicked:
                                drawing_functions.journal_info_draw(journal, player, font, False)
                                journal_button_clicked = False
                            else:
                                drawing_functions.journal_info_draw(journal, player, font, True)
                                journal_button_clicked = True
                        # when player levels up, this lets them click to dismiss the window pop-up
                        if level_up_win.rect.collidepoint(pos):
                            drawing_functions.level_up_draw(level_up_win, player, font, False)
                        if knowledge_academia.rect.collidepoint(pos) and knowledge_academia_show:
                            knowledge_window_clicked = True
                        if rest_recover.rect.collidepoint(pos) and rest_recover_show:
                            rest_window_clicked = True
                        if shop_gear.rect.collidepoint(pos) and shop_gear_show:
                            shop_window_clicked = True
                    elif event.type == QUIT:
                        exit()

                    # --------------------------------------------------------------------------------------------------
                    quest_item = pygame.sprite.spritecollideany(player, quest_items)
                    try:
                        if quest_item.name == "quest logs":
                            if player.quest_status["village repairs"]:
                                info_text_1 = f"Press 'F' key to gather the pine logs."
                                if interacted:
                                    if player.quest_progress["village repairs"] < 4:
                                        player.quest_progress["village repairs"] += 1
                                        info_text_1 = f"You gathered 1 pine log."
                                        quest_item.kill()
                                        interacted = False
                                        loot_update = True
                        if quest_item.name == "rohir gate":
                            if player.quest_complete["ghouled again"]:
                                info_text_1 = f"Press 'F' key to enter Korlok District."
                                if interacted:
                                    player.current_zone = "korlok"
                                    zone_korlok = True
                                    zone_seldon = False
                                    in_district_over_world = False
                                    in_korlok = True
                                    interacted = False
                            if not player.quest_complete["ghouled again"]:
                                info_text_1 = f"The gate seems to be locked shut."
                                info_text_2 = f"Perhaps the nearby Guard knows why?"
                    except AttributeError:
                        pass

                    # --------------------------------------------------------------------------------------------------
                    # if player collides with enemy sprite, doesn't have combat cooldown,
                    # and chooses to interact with it then get event from button press and start combat encounter
                    enemy = pygame.sprite.spritecollideany(player, enemies)
                    if enemy:
                        # lets player know if they are in range of enemy they can press f to attack it
                        info_text_1 = f"Press 'F' key to attack {enemy.name}."
                        info_text_2 = f"{enemy.name} level: {enemy.level}"
                        if interacted:
                            if player.role == "mage":
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_battle)
                            if player.role == "fighter":
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_fighter_battle)
                            if player.role == "scout":
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_battle)
                            if player.role == "":
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_no_role_battle)
                            in_district_over_world = False
                            in_battle = True

                    # --------------------------------------------------------------------------------------------------
                    # player collides with building, enters if chosen to interact and starts related scenario
                    building = pygame.sprite.spritecollideany(player, buildings)
                    if building:
                        # lets player know if they are in range of building they can press f to enter it
                        info_text_1 = f"Press 'F' key to enter {building.name}."
                        info_text_2 = ""
                        if interacted:
                            if building.name == "shop":
                                in_district_over_world = False
                                in_shop = True
                            if building.name == "inn":
                                in_district_over_world = False
                                in_inn = True
                            if building.name == "academia":
                                in_district_over_world = False
                                in_academia = True

                    # --------------------------------------------------------------------------------------------------
                    # if player collides with enemy sprite, doesn't have combat cooldown,
                    # and chooses to interact with it then get event from button press and start combat encounter
                    npc = pygame.sprite.spritecollideany(player, npcs)
                    if npc:
                        info_text_1 = f"Press 'F' key to talk to {npc.name}."
                        if interacted:
                            if player.role == "mage":
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_battle)
                            if player.role == "fighter":
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_fighter_battle)
                            if player.role == "scout":
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_battle)
                            if player.role == "":
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_no_role_battle)
                            in_district_over_world = False
                            in_npc_interaction = True

                    # click handlers for main event loop ---------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    # function to handle inventory item clicks. apply item message to message box if not empty str.
                    inventory_event = inventory_click_handler()
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                        info_update = True
                    # if click handler returns that an equitable item has been updated, set gear_checked to false
                    if not inventory_event["gear checked"]:
                        gear_checked = False
                    if not inventory_event["weapon checked"]:
                        weapon_checked = False
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = equipment_click_handler()
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""
                        info_update = True
                    # same as above but for when an equipment item is un-equipped
                    if not equipment_event["gear checked"]:
                        gear_checked = False
                    if not equipment_event["weapon checked"]:
                        weapon_checked = False

                # outside of main event loop ---------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # get current pressed keys from player and apply zone boundaries depending on current zone
                pressed_keys = pygame.key.get_pressed()
                # Apply pressed keys update to movement based on zone boundaries, defined in player.update()

                # apply direction to current_direction based on current input user keys
                # this will be applied when player sprite is updated with new gear
                if pressed_keys[K_d]:
                    current_direction = "right"
                if pressed_keys[K_a]:
                    current_direction = "left"
                if pressed_keys[K_w]:
                    current_direction = "up"
                if pressed_keys[K_s]:
                    current_direction = "down"
                if zone_seldon:
                    if movement_able:
                        player.update(pressed_keys, "seldon")
                if zone_korlok:
                    if movement_able:
                        player.update(pressed_keys, "korlok")
                if zone_eldream:
                    if movement_able:
                        player.update(pressed_keys, "eldream")
                if zone_marrow:
                    if movement_able:
                        player.update(pressed_keys, "marrow")

                # enemy movement updates -------------------------------------------------------------------------------
                # choose random directions and random enemy to move that direction -------------------------------------
                direction_horizontal = random.choice(["left", "right"])
                direction_vertical = random.choice(["up", "down"])
                move_this_snake = random.choice(snakes.sprites())
                move_this_ghoul = random.choice(ghouls.sprites())
                # move snakes in random direction within boundaries
                if movement_able:
                    enemy_toc = time.perf_counter()
                    if enemy_toc - enemy_tic > 1:
                        enemy_tic = time.perf_counter()
                        move_this_snake.update_position([100, 300], [200, 300],
                                                        direction_horizontal, direction_vertical)
                        move_this_ghoul.update_position([700, 900], [200, 300],
                                                        direction_horizontal, direction_vertical)

                # npc movement updates ---------------------------------------------------------------------------------
                # choose random facing direction and random npc to move face that direction ----------------------------
                face_direction = random.choice(["front", "back", "left", "right"])
                face_this_npc = random.choice(npcs.sprites())
                if movement_able:
                    npc_toc = time.perf_counter()
                    if npc_toc - npc_tic > 2:
                        npc_tic = time.perf_counter()
                        if face_direction == "front":
                            if face_this_npc.name == "garan":
                                npc_garan.update(garan_down)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(maurelle_down)
                            if face_this_npc.name == "guard":
                                npc_guard.update(guard_down)
                        if face_direction == "back":
                            if face_this_npc.name == "garan":
                                npc_garan.update(garan_up)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(maurelle_up)
                            if face_this_npc.name == "guard":
                                npc_guard.update(guard_up)
                        if face_direction == "left":
                            if face_this_npc.name == "garan":
                                npc_garan.update(garan_left)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(maurelle_left)
                            if face_this_npc.name == "guard":
                                npc_guard.update(guard_left)
                        if face_direction == "right":
                            if face_this_npc.name == "garan":
                                npc_garan.update(garan_right)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(maurelle_right)
                            if face_this_npc.name == "guard":
                                npc_guard.update(guard_right)

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in battle -----------------------------------------------------------------------------------
            if in_battle:
                # update players current inventory and status
                status_and_inventory_updates()
                # update players current equipment
                equipment_updates()
                if not gear_checked:
                    gear_checked = gear_check()
                if not weapon_checked:
                    weapon_checked = weapon_check()

                # battle scenario event loop
                # ------------------------------------------------------------------------------------------------------
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()

                    # click handlers for main event loop ---------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    # function to handle inventory item clicks. apply item message to message box if not empty str.
                    inventory_event = inventory_click_handler()
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                        info_update = True
                    # if click handler returns that an equitable item has been updated, set gear_checked to false
                    # so that gear check function will run and get players current stats with new item equipped
                    if not inventory_event["gear checked"]:
                        gear_checked = False
                    if not inventory_event["weapon checked"]:
                        weapon_checked = False
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = equipment_click_handler()
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""
                        info_update = True
                    # same as above but for when an equipment item is un-equipped
                    if not equipment_event["gear checked"]:
                        gear_checked = False
                    if not equipment_event["weapon checked"]:
                        weapon_checked = False
                    elif event.type == QUIT:
                        exit()

                    enemy = pygame.sprite.spritecollideany(player, enemies)
                    if enemy:
                        # update enemy health bar on each iteration
                        enemy.health_bar.update(enemy.health_bar.x_coordinate,
                                                enemy.health_bar.y_coordinate,
                                                health_bar_update(enemy))
                        # don't let player attack again immediately by spam clicking button
                        if not combat_cooldown:
                            # if interact key 'f' has been pressed
                            if interacted:
                                # don't allow player to move while in combat
                                movement_able = False
                                # if player has just started combat, clear message box, change condition to True
                                if not encounter_started:
                                    info_text_1 = ""
                                    info_text_2 = ""
                                    info_text_3 = ""
                                    info_text_4 = ""
                                    encounter_started = True
                                # get which button player pressed during combat scenario (attack, skill or run)
                                combat_button = combat_event_button(event)

                                if combat_button == "attack":
                                    # update player character sprite for combat animation
                                    if player.role == "mage":
                                        if barrier_active:
                                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                        player_battle_sprite.y_coordinate,
                                                                        player_mage_barrier_attack)
                                        else:
                                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                        player_battle_sprite.y_coordinate,
                                                                        player_mage_attack)
                                    if player.role == "fighter":
                                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                    player_battle_sprite.y_coordinate,
                                                                    player_fighter_attack)
                                    if player.role == "scout":
                                        if sharp_sense_active:
                                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                        player_battle_sprite.y_coordinate,
                                                                        player_scout_sense_attack)
                                        else:
                                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                        player_battle_sprite.y_coordinate,
                                                                        player_scout_attack)
                                    if player.role == "":
                                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                    player_battle_sprite.y_coordinate,
                                                                    player_no_role_attack)
                                    # update to attacking sprite surface for combat animation
                                    if enemy.kind == "snake":
                                        snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                                   snake_battle_sprite.y_coordinate,
                                                                   snake_attack)
                                    if enemy.kind == "ghoul":
                                        ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                                   ghoul_battle_sprite.y_coordinate,
                                                                   ghoul_attack)

                                    # ----------------------------------------------------------------------------------
                                    # combat event function that handles and returns damage and health
                                    combat_events = attack_scenario(enemy, "attack")
                                    combat_happened = True
                                    # add all combat scenario happenings from function to message box
                                    # if any of the values are currently zero, or no, return blank string
                                    if combat_events["damage done"] == 0:
                                        info_text_1 = ""
                                    else:
                                        info_text_1 = str(combat_events["damage done"])
                                    if combat_events["damage taken"] == 0:
                                        info_text_2 = ""
                                    else:
                                        info_text_2 = str(combat_events["damage taken"])

                                    # adds item dropped and experienced gained messages to box if enemy was defeated
                                    # appends to dictionary to return to main loop outside of battle
                                    if combat_events["enemy defeated"]:
                                        if combat_events["item dropped"] != "No":
                                            battle_info_to_return_to_main_loop["item dropped"] = \
                                                str(combat_events["item dropped"])
                                        if combat_events["experience gained"] != 0:
                                            battle_info_to_return_to_main_loop["experience"] = \
                                                str(combat_events["experience gained"])
                                    # if enemy was defeated and player leveled up, add messages related to box
                                    if combat_events["enemy defeated"]:
                                        if combat_events["level up status"] != "":
                                            battle_info_to_return_to_main_loop["leveled_up"] = True

                                    # if player was successful in defeating enemy, combat ends, movement is allowed
                                    # set combat happened false, allowing iterations to continue without cooldown
                                    # reset encounter_started condition so that next enemy will clear message box
                                    if combat_events["enemy defeated"]:
                                        # player will gain knowledge based on their current role
                                        if player.role == "mage":
                                            player.knowledge["mage"] += 10
                                            battle_info_to_return_to_main_loop["knowledge"] = \
                                                "10 mage knowledge gained."
                                        if player.role == "fighter":
                                            player.knowledge["fighter"] += 10
                                            battle_info_to_return_to_main_loop["knowledge"] = \
                                                "10 fighter knowledge gained."
                                        if player.role == "scout":
                                            player.knowledge["scout"] += 10
                                            battle_info_to_return_to_main_loop["knowledge"] = \
                                                "10 scout knowledge gained."
                                        # if barrier is active on enemy defeat, restore original defence and set off
                                        if barrier_active:
                                            barrier_active = False
                                            player.defence = original_defence
                                        # if sharp sense is active on enemy defeat, restore original offense
                                        if sharp_sense_active:
                                            sharp_sense_active = False
                                            player.offense = original_offense
                                        movement_able = True
                                        combat_happened = False
                                        interacted = False
                                        loot_update = True
                                        encounter_started = False
                                        in_battle = False
                                        in_district_over_world = True

                                # first skill, or second skill bar slot is clicked
                                # (buffs) mage -> barrier [defence], scout -> sharp sense [offense]
                                if combat_button == "skill 1":
                                    # make sure player has enough energy to use the skill
                                    if player.energy > 34:
                                        # player is a mage and uses the barrier spell. Set barrier active to true
                                        # giving them 20 additional defence and subtract 35 energy
                                        # save original defence value to be re applied upon enemy or player defeat
                                        if player.role == "mage":
                                            if barrier_learned:
                                                if not barrier_active:
                                                    info_text_1 = "Barrier spell is active."
                                                    info_text_2 = "You have gained 10 defence."
                                                    barrier_active = True
                                                    original_defence = player.defence
                                                    player.defence += 10
                                                    player.energy -= 35
                                                else:
                                                    info_text_1 = "Barrier spell is already active."

                                        # player is a scout and uses sharp sense. Set sharp sense active to true
                                        # giving them 20 additional offense and subtract 35 energy
                                        # save original offense value to be re applied upon enemy or player defeat
                                        if player.role == "scout":
                                            if sharp_sense_learned:
                                                if not sharp_sense_active:
                                                    info_text_1 = "Sharp sense is active."
                                                    info_text_2 = "You have gained 20 offense."
                                                    sharp_sense_active = True
                                                    original_offense = player.offense
                                                    player.offense += 20
                                                    player.energy -= 35
                                                else:
                                                    info_text_1 = "Sharp sense is already active."

                                        # player is a fighter and uses hard strike. This uses the standard "attack"
                                        # scenario from above, with the input being changed to the skill instead of
                                        # attack to trigger a different damage value within the attack function
                                        if player.role == "fighter":
                                            if hard_strike_learned:
                                                hard_strike = True

                                                # update animations for hard strike attack -----------------------------
                                                if player.role == "fighter":
                                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                                player_battle_sprite.y_coordinate,
                                                                                player_fighter_strike)
                                                if enemy.kind == "snake":
                                                    snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                                               snake_battle_sprite.y_coordinate,
                                                                               snake_attack)
                                                if enemy.kind == "ghoul":
                                                    ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                                               ghoul_battle_sprite.y_coordinate,
                                                                               ghoul_attack)
                                                # ----------------------------------------------------------------------

                                                combat_events = attack_scenario(enemy, "skill 1")
                                                combat_happened = True
                                                player.energy -= 35
                                                if combat_events["damage done"] == 0:
                                                    info_text_1 = ""
                                                else:
                                                    info_text_1 = str(combat_events["damage done"])
                                                if combat_events["damage taken"] == 0:
                                                    info_text_2 = ""
                                                else:
                                                    info_text_2 = str(combat_events["damage taken"])
                                                if combat_events["enemy defeated"]:
                                                    if combat_events["item dropped"] != "No":
                                                        battle_info_to_return_to_main_loop["item dropped"] = \
                                                            str(combat_events["item dropped"])
                                                    if combat_events["experience gained"] != 0:
                                                        battle_info_to_return_to_main_loop["experience"] = \
                                                            str(combat_events["experience gained"])
                                                if combat_events["enemy defeated"]:
                                                    if combat_events["level up status"] != "":
                                                        battle_info_to_return_to_main_loop["leveled_up"] = True
                                                if combat_events["enemy defeated"]:
                                                    if player.role == "fighter":
                                                        player.knowledge["fighter"] += 10
                                                        battle_info_to_return_to_main_loop["knowledge"] = \
                                                            "10 fighter knowledge gained."
                                                    movement_able = True
                                                    combat_happened = False
                                                    interacted = False
                                                    loot_update = True
                                                    encounter_started = False
                                                    in_battle = False
                                                    in_district_over_world = True
                                    else:
                                        info_text_1 = "Not enough energy to use this skill."

                # outside of battle event loop -------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # battle scene and enemy are drawn to screen -----------------------------------------------------------
                try:
                    if zone_seldon:
                        # create blank background to be drawn on top of each iteration
                        screen.fill((255, 255, 255))  # (255, 255, 255) RGB value for WHITE
                        screen.blit(seldon_district_battle, (0, 0))
                        screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(skill_bar.surf, skill_bar.rect)

                        if player.role == "mage":
                            screen.blit(mage_attack_button.surf, mage_attack_button.rect)
                            if player.skills_mage["skill 2"] == "barrier":
                                screen.blit(barrier_button.surf, barrier_button.rect)
                        if player.role == "fighter":
                            screen.blit(fighter_attack_button.surf, fighter_attack_button.rect)
                            if player.skills_fighter["skill 2"] == "hard strike":
                                screen.blit(hard_strike_button.surf, hard_strike_button.rect)
                        if player.role == "scout":
                            screen.blit(scout_attack_button.surf, scout_attack_button.rect)
                            if player.skills_scout["skill 2"] == "sharp sense":
                                screen.blit(sharp_sense_button.surf, sharp_sense_button.rect)
                        if player.role == "":
                            screen.blit(no_role_attack_button.surf, no_role_attack_button.rect)

                        if enemy.name == "snake":
                            screen.blit(snake_battle_sprite.surf, snake_battle_sprite.rect)
                        if enemy.name == "ghoul":
                            screen.blit(ghoul_battle_sprite.surf, ghoul_battle_sprite.rect)

                        # draw player after enemy to show animations on top of enemy and not under
                        screen.blit(player_battle_sprite.surf, player_battle_sprite.rect)
                        screen.blit(enemy_status_bar_backdrop.surf, enemy_status_bar_backdrop.rect)
                        try:
                            screen.blit(enemy.health_bar.surf, enemy.health_bar.rect)
                        except TypeError:
                            pass
                        screen.blit(enemy_status.surf, enemy_status.rect)
                        screen.blit(message_box.surf, message_box.rect)
                        screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)

                        # updates players inventory items if item is used in combat scenario (ex. health pot.)
                        for item in player_items:
                            screen.blit(item.surf, item.rect)
                        for equipment in player_equipment:
                            screen.blit(equipment.surf, equipment.rect)

                        drawing_functions.text_info_draw(screen, player, font,
                                                         info_text_1, info_text_2, info_text_3, info_text_4)

                        # get current enemy name and create surf and rectangle to draw to screen
                        text_enemy_name_surf = font.render(str(enemy.name), True, "black", "light yellow")
                        text_enemy_name_rect = text_enemy_name_surf.get_rect()
                        text_enemy_name_rect.center = (800, 680)
                        screen.blit(text_enemy_name_surf, text_enemy_name_rect)
                        # get current enemy level and create surf and rectangle to draw to screen
                        text_enemy_level_surf = font.render(str(enemy.level), True, "black", "light yellow")
                        text_enemy_level_rect = text_enemy_level_surf.get_rect()
                        text_enemy_level_rect.center = (915, 680)
                        screen.blit(text_enemy_level_surf, text_enemy_level_rect)

                # after enemy is defeated, it may return a none type for collision. in this case, just ignore error
                except AttributeError:
                    pass

                # ------------------------------------------------------------------------------------------------------
                # combat didn't happen this iteration, reset sprites to default surface image
                if not combat_happened:
                    if player.role == "mage":
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_mage_barrier_battle)
                        else:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_mage_battle)
                    if player.role == "fighter":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    player_fighter_battle)
                    if player.role == "scout":
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_scout_sense_battle)
                        else:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_scout_battle)
                    if player.role == "":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    player_no_role_battle)

                    snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                               snake_battle_sprite.y_coordinate,
                                               snake_battle)
                    ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                               ghoul_battle_sprite.y_coordinate,
                                               ghoul_battle)
                    pygame.display.flip()
                    combat_cooldown = False

                # combat happened this turn, update sprites for battle and apply short cooldown to attack again
                if combat_happened:
                    if player.role == "mage":
                        if barrier_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_mage_barrier_attack)
                        else:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_mage_attack)
                    if not hard_strike:
                        if player.role == "fighter":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_fighter_attack)
                    if player.role == "scout":
                        if sharp_sense_active:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_scout_sense_attack)
                        else:
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_scout_attack)
                    if player.role == "":
                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                    player_battle_sprite.y_coordinate,
                                                    player_no_role_attack)

                    snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                               snake_battle_sprite.y_coordinate,
                                               snake_attack)
                    ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                               ghoul_battle_sprite.y_coordinate,
                                               ghoul_attack)
                    # flip to display ----------------------------------------------------------------------------------
                    # needs to flip here to show the new attacking sprites for the 1-second duration
                    pygame.display.flip()
                    combat_cooldown = True
                    # when combat happens, wait after flipping display to allow animation time to show
                    # 1000 milliseconds = 1 second
                    pygame.time.wait(1000)
                    # reset combat animation and ability to click without delay on next iteration
                    combat_happened = False
                    # reset hard strike condition so regular fighter attack animation resumes
                    hard_strike = False

            # ----------------------------------------------------------------------------------------------------------
            # if player is in shop -------------------------------------------------------------------------------------
            if in_shop:
                status_and_inventory_updates()
                equipment_updates()

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                    elif event.type == QUIT:
                        exit()

                    # --------------------------------------------------------------------------------------------------
                    shop = pygame.sprite.spritecollideany(player, buildings)
                    if building.name == "shop":
                        # if player has just started shop scenario, clear message box
                        if not encounter_started:
                            info_text_1 = "Click an inventory item to sell it."
                            info_text_2 = "Or, click buy button to buy an item."
                            info_text_3 = ""
                            info_text_4 = ""
                            encounter_started = True
                            # reset items bought condition on new shop encounter so that message is shown to
                            # player that they can click to buy or sell items.
                            item_bought = False
                            item_sold = False
                        # get which button player pressed during shop scenario (buy or leave)---------------------------
                        shop_button = shop_event_button(event)
                        if shop_button == "buy":
                            # if player hasn't bought an item yet, show message that item can be clicked to buy
                            if not item_bought:
                                info_text_1 = "Click an item to buy."
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                            # if user clicks buy button again, set condition to false which will hide buy window
                            if buy_clicked:
                                buy_clicked = False
                                # remove buy window from display and clear temporary list used to populate it
                                if len(buy_shop_elements) > 0:
                                    buy_shop_elements.pop(0)
                                    shopkeeper_items.clear()

                            # user clicked buy button for the first time. show buy window ------------------------------
                            else:
                                buy_clicked = True
                                buy_shop_elements.insert(0, buy_inventory)
                                # if shopkeeper has items in their inventory
                                if len(npc_amuna_shopkeeper.items) > 0:
                                    buy_first_coord = 810
                                    buy_second_coord = 435

                                    # ----------------------------------------------------------------------------------
                                    buy_inventory_counter = 0
                                    # go through shop items and assign inventory slots (coordinates) to them
                                    for shop_item in npc_amuna_shopkeeper.items:
                                        if shop_item.name == "health potion":
                                            shop_item.update(buy_first_coord, buy_second_coord, health_pot_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "energy potion":
                                            shop_item.update(buy_first_coord, buy_second_coord, energy_pot_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic staff":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_staff_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic sword":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_sword_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic bow":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_bow_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic robes":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_robes_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic armor":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_armor_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic tunic":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_tunic_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1

                                        buy_first_coord += 60
                                        if buy_inventory_counter > 3:
                                            buy_second_coord += 60
                                            buy_first_coord = 810
                                            buy_inventory_counter = 0
                        # ----------------------------------------------------------------------------------------------
                        # if player chooses to leave shop, set conditions to allow normal gameplay loop
                        if shop_button == "leave":
                            if len(buy_shop_elements) > 0:
                                buy_shop_elements.pop(0)
                                shopkeeper_items.clear()

                            buy_clicked = False
                            movement_able = True
                            interacted = False
                            info_update = True
                            encounter_started = False
                            in_shop = False
                            in_district_over_world = True

                        # ----------------------------------------------------------------------------------------------
                        # shop click handlers --------------------------------------------------------------------------
                        if buy_clicked:
                            buy_item = buy_event_item(event)
                            try:
                                # player has clicked health potion. If player has enough rupees it will buy item
                                # and add to their inventory. Also subtracts the price from current rupee count
                                if buy_item.name == "health potion":
                                    if len(player.items) < 16:
                                        if player.rupees > 9:
                                            info_text_1 = "You Bought Health Potion for 10 rupees."
                                            info_text_2 = "Health Potion added to inventory."
                                            player.items.append(Item("health potion", "potion", 200, 200,
                                                                     health_pot_img))
                                            player.rupees = player.rupees - 10
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Health Potion cost 10 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""

                                if buy_item.name == "energy potion":
                                    if len(player.items) < 16:
                                        if player.rupees > 9:
                                            info_text_1 = "Bought Energy Potion for 10 rupees."
                                            info_text_2 = "Energy Potion added to inventory."
                                            player.items.append(Item("energy potion", "potion", 200, 200,
                                                                     energy_pot_img))
                                            player.rupees = player.rupees - 10
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Energy Potion cost 10 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""

                                if buy_item.name == "basic staff":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Staff for 20 rupees."
                                            info_text_2 = "Basic Staff added to inventory."
                                            player.items.append(Item("basic staff", "mage", 200, 200,
                                                                     basic_staff_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Staff cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""

                                if buy_item.name == "basic sword":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Sword for 20 rupees."
                                            info_text_2 = "Basic Sword added to inventory."
                                            player.items.append(Item("basic sword", "fighter", 200, 200,
                                                                     basic_sword_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Sword cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""

                                if buy_item.name == "basic bow":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Bow for 20 rupees."
                                            info_text_2 = "Basic Bow added to inventory."
                                            player.items.append(Item("basic bow", "scout", 200, 200,
                                                                     basic_bow_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Bow cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""

                                if buy_item.name == "basic robes":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Robes for 20 rupees."
                                            info_text_2 = "Basic Robes added to inventory."
                                            player.items.append(Item("basic robes", "mage", 200, 200,
                                                                     basic_robes_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Robes cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""

                                if buy_item.name == "basic armor":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Armor for 20 rupees."
                                            info_text_2 = "Basic Armor added to inventory."
                                            player.items.append(Item("basic armor", "fighter", 200, 200,
                                                                     basic_armor_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Armor cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""

                                if buy_item.name == "basic tunic":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Tunic for 20 rupees."
                                            info_text_2 = "Basic Tunic added to inventory."
                                            player.items.append(Item("basic tunic", "scout", 200, 200,
                                                                     basic_tunic_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Tunic cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""
                            except AttributeError:
                                pass

                        # handles sell item clicks ---------------------------------------------------------------------
                        sell_item = sell_event_item(event)
                        try:
                            # player has clicked health potion. This will sell the item, removing it from
                            # inventory and giving them "x" rupees to add to their current count
                            if sell_item.name == "health potion":
                                info_text_1 = "Sold Health Potion for 5 rupees."
                                info_text_2 = "Health Potion removed from inventory."
                                player.items.remove(sell_item)
                                player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "energy potion":
                                info_text_1 = "Sold Energy Potion for 5 rupees."
                                info_text_2 = "Energy Potion removed from inventory."
                                player.items.remove(sell_item)
                                player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "shiny rock":
                                info_text_1 = "Sold Shiny Rock for 5 rupees."
                                info_text_2 = "Shiny Rock removed from inventory."
                                player.items.remove(sell_item)
                                player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "bone dust":
                                info_text_1 = "Sold Bone Dust for 10 rupees."
                                info_text_2 = "Bone Dust removed from inventory."
                                player.items.remove(sell_item)
                                player_items.remove(sell_item)
                                player.rupees = player.rupees + 10
                                item_sold = True
                            if sell_item.name == "basic staff":
                                info_text_1 = "Sold Basic Staff for 5 rupees."
                                info_text_2 = "Basic Staff removed from inventory."
                                player.items.remove(sell_item)
                                player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "basic sword":
                                info_text_1 = "Sold Basic Sword for 5 rupees."
                                info_text_2 = "Basic Sword removed from inventory."
                                player.items.remove(sell_item)
                                player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "basic bow":
                                info_text_1 = "Sold Basic Bow for 5 rupees."
                                info_text_2 = "Basic Bow removed from inventory."
                                player.items.remove(sell_item)
                                player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "basic robes":
                                info_text_1 = "Sold Basic Robes for 5 rupees."
                                info_text_2 = "Basic Robes removed from inventory."
                                player.items.remove(sell_item)
                                player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "basic armor":
                                info_text_1 = "Sold Basic Armor for 5 rupees."
                                info_text_2 = "Basic Armor removed from inventory."
                                player.items.remove(sell_item)
                                player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "basic tunic":
                                info_text_1 = "Sold Basic Tunic for 5 rupees."
                                info_text_2 = "Basic Tunic removed from inventory."
                                player.items.remove(sell_item)
                                player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "temporary item":
                                info_text_1 = "Sold Temporary Item for 0 rupees."
                                info_text_2 = "Temporary Item removed from inventory."
                                player.items.remove(sell_item)
                                player_items.remove(sell_item)
                                item_sold = True
                        except AttributeError:
                            pass

                # outside of shop event loop ---------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if building is a shop in the seldon zone
                if building.name == "shop":
                    screen.blit(seldon_district_shop, (0, 0))
                    screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                    screen.blit(hp_bar.surf, hp_bar.rect)
                    screen.blit(en_bar.surf, en_bar.rect)
                    screen.blit(xp_bar.surf, xp_bar.rect)
                    screen.blit(buy_button.surf, buy_button.rect)
                    screen.blit(leave_button.surf, leave_button.rect)
                    screen.blit(message_box.surf, message_box.rect)
                    for item in player_items:
                        screen.blit(item.surf, item.rect)
                    for equipment in player_equipment:
                        screen.blit(equipment.surf, equipment.rect)
                    drawing_functions.text_info_draw(screen, player, font,
                                                     info_text_1, info_text_2, info_text_3, info_text_4)
                    # --------------------------------------------------------------------------------------------------
                    if buy_clicked:
                        for window in buy_shop_elements:
                            screen.blit(window.surf, window.rect)
                        # get item from shopkeeper's inventory and draw with buy window
                        for shop_item in shopkeeper_items:
                            screen.blit(shop_item.surf, shop_item.rect)

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in inn
            if in_inn:
                status_and_inventory_updates()
                equipment_updates()
                if not gear_checked:
                    gear_checked = gear_check()
                if not weapon_checked:
                    weapon_checked = weapon_check()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()

                    # click handlers for inn event loop ----------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    # function to handle inventory item clicks. apply item message to message box if not empty str.
                    inventory_event = inventory_click_handler()
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                        info_update = True
                    # if click handler returns that an equitable item has been updated, set gear_checked to false
                    # so that gear check function will run and get players current stats with new item equipped
                    if not inventory_event["gear checked"]:
                        gear_checked = False
                    if not inventory_event["weapon checked"]:
                        weapon_checked = False
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = equipment_click_handler()
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""
                        info_update = True
                    # same as above but for when an equipment item is un-equipped
                    if not equipment_event["gear checked"]:
                        gear_checked = False
                    if not equipment_event["weapon checked"]:
                        weapon_checked = False
                    elif event.type == QUIT:
                        exit()

                    # --------------------------------------------------------------------------------------------------
                    inn = pygame.sprite.spritecollideany(player, buildings)
                    if building.name == "inn":
                        # if player has just started inn scenario, clear message box
                        if not encounter_started:
                            info_text_1 = "Click rest button to sleep."
                            info_text_2 = "Sleep regains health and energy."
                            info_text_3 = ""
                            info_text_4 = ""
                            encounter_started = True
                        # get which button player pressed during inn scenario (rest or leave)---------------------------
                        inn_button = inn_event_button(event)
                        if inn_button == "rest":
                            # if player has not yet rested this instance
                            if not rested:
                                rest_clicked = True
                                info_text_1 = "You feel well rested."
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                            # if player has already rested this instance
                            else:
                                info_text_1 = "You've already rested."
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                    # --------------------------------------------------------------------------------------------------
                    # if player chooses to leave shop, set conditions to allow normal gameplay loop
                    if inn_button == "leave":
                        rest_clicked = False
                        movement_able = True
                        interacted = False
                        info_update = True
                        encounter_started = False
                        in_inn = False
                        in_district_over_world = True
                        # reset rest condition and screen fade effect so next instance player can rest again
                        rested = False
                        faded_inn_screen = False

                # outside of inn event loop ----------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if building is an inn in the seldon zone
                if building.name == "inn":
                    # if player has just rested, fade inn screen back in with alpha value loop
                    if rested:
                        # so this only happens once and not each iteration
                        if not faded_inn_screen:
                            for alpha in range(0, 50):
                                seldon_district_inn.set_alpha(alpha)
                                screen.blit(seldon_district_inn, (0, 0))
                                # flip sleep screen to display ---------------------------------------------------------
                                pygame.display.flip()
                            faded_inn_screen = True
                        else:
                            seldon_district_inn.set_alpha(255)
                            screen.blit(seldon_district_inn, (0, 0))
                    if not rested:
                        seldon_district_inn.set_alpha(255)
                        screen.blit(seldon_district_inn, (0, 0))
                    screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                    screen.blit(hp_bar.surf, hp_bar.rect)
                    screen.blit(en_bar.surf, en_bar.rect)
                    screen.blit(xp_bar.surf, xp_bar.rect)
                    screen.blit(rest_button.surf, rest_button.rect)
                    screen.blit(leave_button.surf, leave_button.rect)
                    screen.blit(message_box.surf, message_box.rect)
                    for item in player_items:
                        screen.blit(item.surf, item.rect)
                    for equipment in player_equipment:
                        screen.blit(equipment.surf, equipment.rect)
                    drawing_functions.text_info_draw(screen, player, font,
                                                     info_text_1, info_text_2, info_text_3, info_text_4)

                    # --------------------------------------------------------------------------------------------------
                    if rest_clicked:
                        if not rested:
                            # set sleep screen to fade in with alpha value loop. Flip each iteration to show
                            for alpha in range(0, 255):
                                nera_sleep_screen.set_alpha(alpha)
                                screen.blit(nera_sleep_screen, (0, 0))
                                # flip sleep screen to display each iteration to show fade -----------------------------
                                pygame.display.flip()
                            player.health = 100
                            player.energy = 100
                            rested = True

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in academia
            if in_academia:
                status_and_inventory_updates()
                equipment_updates()
                if not gear_checked:
                    gear_checked = gear_check()
                if not weapon_checked:
                    weapon_checked = weapon_check()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()

                    # click handlers -----------------------------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    # function to handle inventory item clicks. apply item message to message box if not empty str.
                    inventory_event = inventory_click_handler()
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                        info_update = True
                    # if click handler returns that an equitable item has been updated, set gear_checked to false
                    # so that gear check function will run and get players current stats with new item equipped
                    if not inventory_event["gear checked"]:
                        gear_checked = False
                    if not inventory_event["weapon checked"]:
                        weapon_checked = False
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = equipment_click_handler()
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""
                        info_update = True
                    # same as above but for when an equipment item is un-equipped
                    if not equipment_event["gear checked"]:
                        gear_checked = False
                    if not equipment_event["weapon checked"]:
                        weapon_checked = False
                    elif event.type == QUIT:
                        exit()

                    # --------------------------------------------------------------------------------------------------
                    academia = pygame.sprite.spritecollideany(player, buildings)
                    if building.name == "academia":
                        if not encounter_started:
                            info_text_1 = "Click a book to view skills."
                            info_text_2 = "Then, click a skill to learn it."
                            info_text_3 = ""
                            info_text_4 = ""
                            encounter_started = True
                        # get which button player pressed during academia scenario (learn or leave)---------------------
                        academia_button = academia_event_button(event)
                        if academia_button == "mage learn":
                            mage_learn_clicked = True
                        if academia_button == "fighter learn":
                            fighter_learn_clicked = True
                        if academia_button == "scout learn":
                            scout_learn_clicked = True

                    # --------------------------------------------------------------------------------------------------
                    # if player chooses to leave academia, set conditions to allow normal gameplay loop
                    if academia_button == "leave":
                        learn_clicked = False
                        movement_able = True
                        interacted = False
                        info_update = True
                        encounter_started = False
                        in_academia = False
                        in_district_over_world = True
                        mage_learn_clicked = False
                        fighter_learn_clicked = False
                        scout_learn_clicked = False
                        learned = False
                        books.clear()
                        skill_learn_items.clear()

                    # get which button player pressed during book skill open (skill or close)---------------------------
                    book_button = skill_learn_event_item(event)
                    if mage_learn_clicked:
                        try:
                            if book_button.name == "barrier learn button":
                                if not barrier_learned:
                                    if player.knowledge["mage"] > 39:
                                        player.skills_mage["skill 2"] = "barrier"
                                        info_text_1 = "'Barrier' skill learned!"
                                        info_text_2 = "Skill added. 40 knowledge used."
                                        player.knowledge["mage"] -= 40
                                        barrier_learned = True
                                    else:
                                        info_text_1 = "40 mage knowledge required to learn."
                                else:
                                    info_text_1 = "You've already learned 'Barrier'."
                                    info_text_2 = ""
                            if book_button.name == "close button":
                                mage_learn_clicked = False
                                books.clear()
                                skill_learn_items.clear()
                        except AttributeError:
                            pass
                    if fighter_learn_clicked:
                        try:
                            if book_button.name == "hard strike learn button":
                                if not hard_strike_learned:
                                    if player.knowledge["fighter"] > 39:
                                        player.skills_fighter["skill 2"] = "hard strike"
                                        info_text_1 = "'Hard Strike' skill learned!"
                                        info_text_2 = "Skill added. 40 knowledge used."
                                        player.knowledge["fighter"] -= 40
                                        hard_strike_learned = True
                                    else:
                                        info_text_1 = "40 fighter knowledge required to learn."
                                else:
                                    info_text_1 = "You've already learned 'Hard Strike'."
                                    info_text_2 = ""
                            if book_button.name == "close button":
                                fighter_learn_clicked = False
                                books.clear()
                                skill_learn_items.clear()
                        except AttributeError:
                            pass
                    if scout_learn_clicked:
                        try:
                            if book_button.name == "sharp sense learn button":
                                if not sharp_sense_learned:
                                    if player.knowledge["scout"] > 39:
                                        player.skills_scout["skill 2"] = "sharp sense"
                                        info_text_1 = "'Sharp Sense' skill learned!"
                                        info_text_2 = "Skill added. 40 knowledge used."
                                        player.knowledge["scout"] -= 40
                                        sharp_sense_learned = True
                                    else:
                                        info_text_1 = "40 scout knowledge required to learn."
                                else:
                                    info_text_1 = "You've already learned 'Sharp Sense'."
                                    info_text_2 = ""
                            if book_button.name == "close button":
                                scout_learn_clicked = False
                                books.clear()
                                skill_learn_items.clear()
                        except AttributeError:
                            pass

                # outside of inn event loop ----------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if building is an inn in the seldon zone
                if building.name == "academia":
                    screen.blit(seldon_district_academia, (0, 0))
                    screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                    screen.blit(hp_bar.surf, hp_bar.rect)
                    screen.blit(en_bar.surf, en_bar.rect)
                    screen.blit(xp_bar.surf, xp_bar.rect)
                    screen.blit(mage_learn_button.surf, mage_learn_button.rect)
                    screen.blit(fighter_learn_button.surf, fighter_learn_button.rect)
                    screen.blit(scout_learn_button.surf, scout_learn_button.rect)
                    screen.blit(leave_button.surf, leave_button.rect)
                    screen.blit(message_box.surf, message_box.rect)
                    for item in player_items:
                        screen.blit(item.surf, item.rect)
                    for equipment in player_equipment:
                        screen.blit(equipment.surf, equipment.rect)
                    for book in books:
                        screen.blit(book.surf, book.rect)
                    for skill_item in skill_learn_items:
                        screen.blit(skill_item.surf, skill_item.rect)
                    drawing_functions.text_info_draw(screen, player, font,
                                                     info_text_1, info_text_2, info_text_3, info_text_4)
                    screen.blit(knowledge_window.surf, knowledge_window.rect)
                    text_mage_knowledge_surf = font.render(str(player.knowledge["mage"]), True, "black",
                                                           "light yellow")
                    text_mage_knowledge_rect = text_mage_knowledge_surf.get_rect()
                    text_mage_knowledge_rect.center = (515, 680)
                    screen.blit(text_mage_knowledge_surf, text_mage_knowledge_rect)
                    text_fighter_knowledge_surf = font.render(str(player.knowledge["fighter"]), True, "black",
                                                              "light yellow")
                    text_fighter_knowledge_rect = text_fighter_knowledge_surf.get_rect()
                    text_fighter_knowledge_rect.center = (695, 680)
                    screen.blit(text_fighter_knowledge_surf, text_fighter_knowledge_rect)
                    text_scout_knowledge_surf = font.render(str(player.knowledge["scout"]), True, "black",
                                                            "light yellow")
                    text_scout_knowledge_rect = text_scout_knowledge_surf.get_rect()
                    text_scout_knowledge_rect.center = (865, 680)
                    screen.blit(text_scout_knowledge_surf, text_scout_knowledge_rect)

                    # --------------------------------------------------------------------------------------------------
                    if mage_learn_clicked and fighter_learn_clicked is False and scout_learn_clicked is False:
                        books.append(mage_book)
                        skill_learn_items.append(barrier_learn_button)
                        skill_learn_items.append(close_button)
                    if fighter_learn_clicked and mage_learn_clicked is False and scout_learn_clicked is False:
                        books.append(fighter_book)
                        skill_learn_items.append(hard_strike_learn_button)
                        skill_learn_items.append(close_button)
                    if scout_learn_clicked and fighter_learn_clicked is False and mage_learn_clicked is False:
                        books.append(scout_book)
                        skill_learn_items.append(sharp_sense_learn_button)
                        skill_learn_items.append(close_button)

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player interacting with an npc (quest) ----------------------------------------------------------------
            if in_npc_interaction:
                # update players current inventory and status
                status_and_inventory_updates()
                # update players current equipment
                equipment_updates()
                if not gear_checked:
                    gear_checked = gear_check()
                if not weapon_checked:
                    weapon_checked = weapon_check()

                # npc scenario event loop
                # ------------------------------------------------------------------------------------------------------
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()

                    # click handlers for npc event loop ----------------------------------------------------------------
                    inventory_event = inventory_click_handler()
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                        info_update = True
                    if not inventory_event["gear checked"]:
                        gear_checked = False
                    if not inventory_event["weapon checked"]:
                        weapon_checked = False
                    equipment_event = equipment_click_handler()
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""
                        info_update = True
                    if not equipment_event["gear checked"]:
                        gear_checked = False
                    if not equipment_event["weapon checked"]:
                        weapon_checked = False
                    elif event.type == QUIT:
                        exit()

                    # when player levels up, this lets them click to dismiss the window pop-up
                    if level_up_win.rect.collidepoint(pos):
                        drawing_functions.level_up_draw(level_up_win, player, font, False)

                    # --------------------------------------------------------------------------------------------------
                    npc = pygame.sprite.spritecollideany(player, npcs)
                    if npc:
                        if interacted:
                            movement_able = False
                            if not encounter_started:
                                info_text_1 = ""
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                                encounter_started = True

                            npc_button = npc_event_button(event)
                            if npc_button == "quest":
                                if npc.name == "garan":
                                    if player.quest_progress["sneaky snakes"] == 4 and not \
                                            player.quest_complete["sneaky snakes"]:

                                        if len(player.items) < 16:
                                            player.quest_complete["sneaky snakes"] = True
                                            player.current_quests["sneaky snakes"] = "You completed this quest!"
                                            info_text_1 = "You've completed Garan's quest!"
                                            info_text_2 = "You've gained: "
                                            info_text_3 = "2 health and energy potions. "
                                            info_text_4 = "50 xp and 10 amuna rep. "
                                            player.experience += 50
                                            if player.experience >= 100:
                                                level_up()
                                            player.reputation["amuna"] += 10
                                            player.items.append(Item("health potion", "potion", 200, 200,
                                                                     health_pot_img))
                                            player.items.append(Item("health potion", "potion", 200, 200,
                                                                     health_pot_img))
                                            player.items.append(Item("energy potion", "potion", 200, 200,
                                                                     energy_pot_img))
                                            player.items.append(Item("energy potion", "potion", 200, 200,
                                                                     energy_pot_img))
                                        else:
                                            info_text_1 = "You completed the quest, but "
                                            info_text_2 = "Your inventory is full!"

                                    if not quest_clicked:
                                        if not player.quest_complete["sneaky snakes"]:
                                            drawing_functions.quest_box_draw(npc, True, garan_quest_window,
                                                                             maurelle_quest_window,
                                                                             guard_quest_window,
                                                                             accept_button, decline_button)
                                            quest_clicked = True
                                        else:
                                            info_text_1 = "You've completed this quest!"
                                    else:
                                        drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                         maurelle_quest_window, guard_quest_window,
                                                                         accept_button, decline_button)
                                        quest_clicked = False

                                if npc.name == "maurelle":
                                    if player.quest_progress["village repairs"] == 4 and not \
                                            player.quest_complete["village repairs"]:

                                        if len(player.items) < 16:
                                            player.quest_complete["village repairs"] = True
                                            player.current_quests["village repairs"] = "You completed this quest!"
                                            info_text_1 = "You've completed Maurelle's quest!"
                                            info_text_2 = "You've gained: "
                                            info_text_3 = "Nera's blessing (Trinket). "
                                            info_text_4 = "50 xp and 10 amuna rep. "
                                            player.experience += 50
                                            if player.experience >= 100:
                                                level_up()
                                            player.reputation["amuna"] += 10
                                            player.items.append(Item("temporary item", "trinket", 200, 200, temp_img))
                                        else:
                                            info_text_1 = "You completed the quest, but "
                                            info_text_2 = "Your inventory is full!"

                                    if not quest_clicked:
                                        if not player.quest_complete["village repairs"]:
                                            drawing_functions.quest_box_draw(npc, True, garan_quest_window,
                                                                             maurelle_quest_window,
                                                                             guard_quest_window,
                                                                             accept_button, decline_button)
                                            quest_clicked = True
                                        else:
                                            info_text_1 = "You've completed this quest!"
                                    else:
                                        drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                         maurelle_quest_window, guard_quest_window,
                                                                         accept_button, decline_button)
                                        quest_clicked = False

                                if npc.name == "guard":
                                    if player.quest_progress["ghouled again"] == 4 and not \
                                            player.quest_complete["ghouled again"]:

                                        if len(player.items) < 16:
                                            player.quest_complete["ghouled again"] = True
                                            player.current_quests["ghouled again"] = "You completed this quest!"
                                            info_text_1 = "You've completed Guard's quest!"
                                            info_text_2 = "You've gained: "
                                            info_text_3 = "Rohir bridge gate access. "
                                            info_text_4 = "50 xp and 10 amuna rep. "
                                            player.experience += 50
                                            if player.experience >= 100:
                                                level_up()
                                            player.reputation["amuna"] += 10
                                        else:
                                            info_text_1 = "You completed the quest, but "
                                            info_text_2 = "Your inventory is full!"

                                    if not quest_clicked:
                                        if not player.quest_complete["ghouled again"]:
                                            drawing_functions.quest_box_draw(npc, True, garan_quest_window,
                                                                             maurelle_quest_window,
                                                                             guard_quest_window,
                                                                             accept_button, decline_button)
                                            quest_clicked = True
                                        else:
                                            info_text_1 = "You've completed this quest!"
                                    else:
                                        drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                         maurelle_quest_window, guard_quest_window,
                                                                         accept_button, decline_button)
                                        quest_clicked = False

                            quest_buttons = quest_event_button(event)
                            if quest_buttons == "accept":
                                info_text_1 = "You've accepted the quest!"
                                if npc.name == "garan":
                                    # when players first accept garan's quest he will give them a basic weapon
                                    if not garan_gifted:
                                        player.items.append(Item("basic staff", "mage", 200, 200,
                                                                 basic_staff_img))
                                        player.items.append(Item("basic sword", "fighter", 200, 200,
                                                                 basic_sword_img))
                                        player.items.append(Item("basic bow", "scout", 200, 200,
                                                                 basic_bow_img))
                                        player.rupees += 20
                                        info_text_2 = "garan has given you:"
                                        info_text_3 = "Basic Staff, Basic Sword, Basic Bow"
                                        info_text_4 = "And 20 rupees!"
                                        garan_gifted = True

                                    player.quest_status["sneaky snakes"] = True
                                    player.current_quests["sneaky snakes"] = "Garan asked you to defeat" \
                                                                             " snakes near the river."
                                if npc.name == "maurelle":
                                    player.quest_status["village repairs"] = True
                                    player.current_quests["village repairs"] = "Maurelle asked you to " \
                                                                               "gather lumber from nearby trees."
                                if npc.name == "guard":
                                    player.quest_status["ghouled again"] = True
                                    player.current_quests["ghouled again"] = "The Guard asked you to defeat" \
                                                                             " ghouls nearby the Castle wall."
                                quest_clicked = False
                                drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                 maurelle_quest_window, guard_quest_window,
                                                                 accept_button, decline_button)
                            if quest_buttons == "decline":
                                info_text_1 = ""
                                quest_clicked = False
                                drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                 maurelle_quest_window, guard_quest_window,
                                                                 accept_button, decline_button)
                            if npc_button == "leave":
                                movement_able = True
                                interacted = False
                                info_update = True
                                encounter_started = False
                                in_npc_interaction = False
                                in_district_over_world = True
                                quest_clicked = False
                                drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                 maurelle_quest_window, guard_quest_window,
                                                                 accept_button, decline_button)

                # outside npc interaction event loop -------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # battle scene and enemy are drawn to screen -----------------------------------------------------------
                if zone_seldon:
                    # create blank background to be drawn on top of each iteration
                    screen.fill((255, 255, 255))  # (255, 255, 255) RGB value for WHITE
                    screen.blit(seldon_district_battle, (0, 0))
                    screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                    screen.blit(hp_bar.surf, hp_bar.rect)
                    screen.blit(en_bar.surf, en_bar.rect)
                    screen.blit(xp_bar.surf, xp_bar.rect)
                    screen.blit(player_battle_sprite.surf, player_battle_sprite.rect)
                    screen.blit(message_box.surf, message_box.rect)
                    screen.blit(leave_button.surf, leave_button.rect)
                    screen.blit(quest_button.surf, quest_button.rect)
                    screen.blit(npc_name_plate.surf, npc_name_plate.rect)

                    if npc.name == "garan":
                        screen.blit(npc_garan_interaction.surf, npc_garan_interaction.rect)
                    if npc.name == "maurelle":
                        screen.blit(npc_maurelle_interaction.surf, npc_maurelle_interaction.rect)
                    if npc.name == "guard":
                        screen.blit(npc_guard_interaction.surf, npc_guard_interaction.rect)

                    # updates players inventory items if item is used in combat scenario (ex. health pot.)
                    for item in player_items:
                        screen.blit(item.surf, item.rect)
                    for equipment in player_equipment:
                        screen.blit(equipment.surf, equipment.rect)
                    drawing_functions.text_info_draw(screen, player, font,
                                                     info_text_1, info_text_2, info_text_3, info_text_4)
                    # get current npc name and create surf and rectangle to draw to screen
                    text_npc_name_surf = font.render(str(npc.name), True, "black", "light yellow")
                    text_npc_name_rect = text_npc_name_surf.get_rect()
                    text_npc_name_rect.center = (640, 192)
                    screen.blit(text_npc_name_surf, text_npc_name_rect)

                    drawing_functions.draw_it(screen)

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in korlok over world
            if in_korlok:
                # clear info update after some time has passed
                if pygame.time.get_ticks() % 287 == 0:
                    info_update = False
                # clear loot update after some time has passed
                if pygame.time.get_ticks() % 517 == 0:
                    loot_update = False
                # if player is not currently in range of sprite and there is not an active info update,
                # clear message box
                sprite = pygame.sprite.spritecollideany(player, most_sprites)
                if not sprite:
                    if not info_update:
                        info_text_1 = ""
                        info_text_2 = ""
                    if not loot_update:
                        info_text_3 = ""
                        info_text_4 = ""

                # create blank background to be drawn on top of for each iteration
                screen.fill((255, 255, 255))  # (255, 255, 255) RGB value for WHITE
                # draw screen 1 background
                screen.blit(korlok_district_bg, (0, 0))

                # draw user interface elements
                for ui_element in user_interface:
                    screen.blit(ui_element.surf, ui_element.rect)
                # get screen option elements and draw window
                for window in display_elements:
                    screen.blit(window.surf, window.rect)

                rohir_gate.update(525, 600, pygame.image.load(resource_urls.rohir_gate).convert())
                screen.blit(rohir_gate.surf, rohir_gate.rect)

                # draw player
                screen.blit(player.surf, player.rect)

                # handles drawing most text based elements to the screen, such as level, rupees, etc
                drawing_functions.draw_it(screen)

                screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                screen.blit(hp_bar.surf, hp_bar.rect)
                screen.blit(en_bar.surf, en_bar.rect)
                screen.blit(xp_bar.surf, xp_bar.rect)

                # draw texts to the screen, like message box, player rupees and level
                drawing_functions.text_info_draw(screen, player, font,
                                                 info_text_1, info_text_2, info_text_3, info_text_4)
                # update players current inventory and status
                status_and_inventory_updates()
                # update players current equipment
                equipment_updates()
                # if players gear hasn't been checked, due to initial iteration or if equipment was updated
                # elsewhere, then check their current gear and apply stat bonus based on item equipped
                if not gear_checked:
                    gear_checked = gear_check()
                if not weapon_checked:
                    weapon_checked = weapon_check()

                # ------------------------------------------------------------------------------------------------------
                # all in-game events such as key presses or UI interaction
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        # escape key was pressed, exit game
                        if event.key == K_ESCAPE:
                            exit()
                        # "F" key for player interaction
                        if event.key == K_f:
                            interacted = True
                    # if the unstuck button was clicked, move the player to bottom right corner of screen
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if hearth_button.rect.collidepoint(pos):
                            player.pos = vec((850, 650))

                        # if character button is clicked, call draw function and show elements. second click hides
                        if character_button.rect.collidepoint(pos):
                            if character_button_clicked:
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, False)
                                character_button_clicked = False
                            else:
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, True)
                                character_button_clicked = True

                        # if journal button is clicked, call draw function and show elements. second click hides
                        if journal_button.rect.collidepoint(pos):
                            if journal_button_clicked:
                                drawing_functions.journal_info_draw(journal, player, font, False)
                                journal_button_clicked = False
                            else:
                                drawing_functions.journal_info_draw(journal, player, font, True)
                                journal_button_clicked = True

                        # when player levels up, this lets them click to dismiss the window pop-up
                        if level_up_win.rect.collidepoint(pos):
                            drawing_functions.level_up_draw(level_up_win, player, font, False)

                        if knowledge_academia.rect.collidepoint(pos) and knowledge_academia_show:
                            knowledge_window_clicked = True
                        if rest_recover.rect.collidepoint(pos) and rest_recover_show:
                            rest_window_clicked = True
                        if shop_gear.rect.collidepoint(pos) and shop_gear_show:
                            shop_window_clicked = True

                    elif event.type == QUIT:
                        exit()

                    # --------------------------------------------------------------------------------------------------
                    quest_item = pygame.sprite.spritecollideany(player, quest_items)
                    try:
                        if quest_item.name == "rohir gate":
                            if player.quest_complete["ghouled again"]:
                                info_text_1 = f"Press 'F' key to enter Seldon District."
                                if interacted:
                                    player.current_zone = "seldon"
                                    zone_korlok = False
                                    zone_seldon = True
                                    in_district_over_world = True
                                    in_korlok = False
                                    interacted = False
                                    rohir_gate.update(525, 40,
                                                      pygame.image.load(resource_urls.rohir_gate).convert())

                    except AttributeError:
                        pass

                    # click handlers for main event loop ---------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    # function to handle inventory item clicks. apply item message to message box if not empty str.
                    inventory_event = inventory_click_handler()
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                        info_update = True
                    # if click handler returns that an equitable item has been updated, set gear_checked to false
                    # so that gear check function will run and get players current stats with new item equipped
                    if not inventory_event["gear checked"]:
                        gear_checked = False
                    if not inventory_event["weapon checked"]:
                        weapon_checked = False
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = equipment_click_handler()
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""
                        info_update = True
                    # same as above but for when an equipment item is un-equipped
                    if not equipment_event["gear checked"]:
                        gear_checked = False
                    if not equipment_event["weapon checked"]:
                        weapon_checked = False

                # outside of main event loop ---------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # get current pressed keys from player and apply zone boundaries depending on current zone
                pressed_keys = pygame.key.get_pressed()
                # Apply pressed keys update to movement based on zone boundaries, defined in player.update()

                # apply direction to current_direction based on current input user keys
                # this will be applied when player sprite is updated with new gear
                if pressed_keys[K_d]:
                    current_direction = "right"
                if pressed_keys[K_a]:
                    current_direction = "left"
                if pressed_keys[K_w]:
                    current_direction = "up"
                if pressed_keys[K_s]:
                    current_direction = "down"

                if zone_korlok:
                    if movement_able:
                        player.update(pressed_keys, "korlok")

            # end of whole iteration -----------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # flip to display ------------------------------------------------------------------------------------------
            pygame.display.flip()
            # 60 frames per second game rate ---------------------------------------------------------------------------
            clock.tick(60)

        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # player has died, show game over and give continue option
        else:
            # draw game over screen and continue button
            screen.blit(game_over_screen, (0, 0))
            screen.blit(lets_go_button.surf, lets_go_button.rect)

            # ----------------------------------------------------------------------------------------------------------
            # user input events such as key presses or UI interaction
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    # player chooses to continue, reset character experience and half health and energy on respawn
                    if lets_go_button.rect.collidepoint(pos):
                        movement_able = True
                        # reset interaction, so it doesn't immediately interact again on subsequent collisions
                        interacted = False
                        # make sure that windows haven't registered a click on reset for whatever reason
                        inventory_clicked = False
                        sell_clicked = False
                        buy_clicked = False
                        encounter_started = False
                        in_battle = False
                        in_district_over_world = True

                        # turn off barrier and restore original defence if player mage was killed while active
                        if barrier_active:
                            barrier_active = False
                            player.defence = original_defence

                        # turn off barrier and restore original defence if player mage was killed while active
                        if sharp_sense_active:
                            sharp_sense_active = False
                            player.offense = original_offense

                        player.pos = vec((435, 700))
                        player.health = 50
                        player.energy = 50
                        player.experience = 0
                        # bring enemies back to full health
                        for enemy in enemies:
                            enemy.health = 100
                        player.alive_status = True

                elif event.type == QUIT:
                    exit()

            pygame.display.flip()

# related to music - implement later
# we can stop and quit the mixer
# pygame.mixer.music.stop()
# pygame.mixer.quit()
