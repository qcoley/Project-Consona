import os
import random
import sys

import pygame
from pygame.locals import *

# ----------------------------------------------------------------------------------------------------------------------
# global variables -----------------------------------------------------------------------------------------------------

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

pygame.display.set_caption("Project Eterna")
vec = pygame.math.Vector2

# acceleration and friction
ACC = 0.20
FRIC = -0.20


# ----------------------------------------------------------------------------------------------------------------------
# class objects --------------------------------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):

    def __init__(self, name, gender, race, role, items, equipment, current_quest, quest_status, quest_dictionary,
                 statistics, skills, level, experience, health, energy, alive_status, rupees, reputation, mount,
                 current_zone):

        super(Player, self).__init__()
        self.surf = pygame.image.load(stan_down_url).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.pos = vec((435, 700))

        # velocity and acceleration vectors for movement physics
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.name = name
        self.gender = gender
        self.race = race
        self.role = role
        self.items = items
        self.equipment = equipment
        self.current_quest = current_quest
        self.quest_status = quest_status
        self.quest_dictionary = quest_dictionary
        self.statistics = statistics
        self.skills = skills
        self.level = level
        self.experience = experience
        self.health = health
        self.energy = energy
        self.alive_status = alive_status
        self.rupees = rupees
        self.reputation = reputation
        self.mount = mount
        self.current_zone = current_zone

    # move the character sprite based on key presses
    def update(self, pressed_keyes, current_zone):

        # setting acceleration vector on player update frame
        self.acc = vec(0, 0)

        # control acceleration based on user keys pressed from input parameter -----------------------------------------
        if pressed_keyes[K_w]:
            self.surf = pygame.image.load(stan_up_url).convert()

            if scaled_800:
                self.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() * .78,
                                                                       player.surf.get_height() * .78))
                self.rect = player.surf.get_rect(center=player.pos * .78)

            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.y = -ACC

            if scaled_800:
                self.acc.y *= .78

        if pressed_keyes[K_s]:
            self.surf = pygame.image.load(stan_down_url).convert()

            if scaled_800:
                self.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() * .78,
                                                                       player.surf.get_height() * .78))
                self.rect = player.surf.get_rect(center=player.pos * .78)

            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.y = ACC

            if scaled_800:
                self.acc.y *= .78

        if pressed_keyes[K_a]:
            self.surf = pygame.image.load(stan_left_url).convert()

            if scaled_800:
                self.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() * .78,
                                                                       player.surf.get_height() * .78))
                self.rect = player.surf.get_rect(center=player.pos * .78)

            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.x = -ACC

            if scaled_800:
                self.acc.x *= .78

        if pressed_keyes[K_d]:
            self.surf = pygame.image.load(stan_right_url).convert()

            if scaled_800:
                self.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() * .78,
                                                                       player.surf.get_height() * .78))
                self.rect = player.surf.get_rect(center=player.pos * .78)

            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.x = ACC

            if scaled_800:
                self.acc.x *= .78

        # Keep player on the screen, boundaries vary depending on current zone -----------------------------------------
        if current_zone == "seldon":
            if scaled_800:
                if self.pos.x < 25 * .78:
                    self.pos.x = 25 * .78

                elif self.pos.x > width - 115 * .78:
                    self.pos.x = width - 115 * .78

                if self.pos.y <= 115 * .78:
                    self.pos.y = 115 * .78

                elif self.pos.y >= height - 5 * .78:
                    self.pos.y = height - 5 * .78
            else:
                if self.pos.x < 25:
                    self.pos.x = 25

                elif self.pos.x > width - 115:
                    self.pos.x = width - 115

                if self.pos.y <= 115:
                    self.pos.y = 115

                elif self.pos.y >= height - 5:
                    self.pos.y = height - 5

        # equations and update player movement based on vectors --------------------------------------------------------
        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        if scaled_800:
            self.acc.x = self.acc.x * .78
            self.acc.y = self.acc.y * .78

        # collision detection with environment objects (trees, buildings, etc) -----------------------------------------
        if pygame.sprite.spritecollide(player, environment_objects, False, pygame.sprite.collide_rect_ratio(0.50)):

            if scaled_800:
                if pressed_keyes[K_w]:
                    player.vel.y = + .46 * .78

                if pressed_keyes[K_s]:
                    player.vel.y = - .46 * .78

                if pressed_keyes[K_a]:
                    player.vel.x = + .46 * .78

                if pressed_keyes[K_d]:
                    player.vel.x = - .46 * .78

            else:
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
                 alive_status, quest_complete, items, gift, image, color):
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
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, image):
        self.surf = pygame.image.load(image).convert()
        if scaled_800:
            self.surf = pygame.transform.smoothscale(self.surf,
                                                     (self.surf.get_width() * .78, self.surf.get_height() * .78))

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)


class Enemy(pygame.sprite.Sprite):

    def __init__(self, name, kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image,
                 color, health_bar):
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
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.speed = 1
        self.health_bar = health_bar

    def update(self, ranges_x, ranges_y, direction_x, direction_y):

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

    def __init__(self, name, model, x_coordinate, y_coordinate, gathered, image, color):
        super(Tree, self).__init__()

        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.gathered = gathered
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))


class Building(pygame.sprite.Sprite):

    def __init__(self, name, model, x_coordinate, y_coordinate, image, color):
        super(Building, self).__init__()

        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))


# any UI element like buttons, bars, status etc.
class UiElement(pygame.sprite.Sprite):

    def __init__(self, name, x_coordinate, y_coordinate, image, color, update_flag):
        super(UiElement, self).__init__()

        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.update_flag = update_flag

    def update(self, image):
        self.surf = pygame.image.load(image).convert()
        if scaled_800:
            self.surf = pygame.transform.smoothscale(self.surf,
                                                     (self.surf.get_width() * .78, self.surf.get_height() * .78))

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)


class Inventory(pygame.sprite.Sprite):

    def __init__(self, contains, x_coordinate, y_coordinate, image, color, update_flag):
        super(Inventory, self).__init__()

        self.contains = contains
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.update_flag = update_flag


# pop up notifications, like the welcome screen image when game starts
class Notification(pygame.sprite.Sprite):

    def __init__(self, name, shown, x_coordinate, y_coordinate, image, color):
        super(Notification, self).__init__()

        self.name = name
        self.shown = shown
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))


# to create a representation of character for battle screen
class BattleCharacter(pygame.sprite.Sprite):

    def __init__(self, name, x_coordinate, y_coordinate, image, color):
        super(BattleCharacter, self).__init__()
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, image):
        self.surf = pygame.image.load(image).convert()
        if scaled_800:
            self.surf = pygame.transform.smoothscale(self.surf,
                                                     (self.surf.get_width() * .78, self.surf.get_height() * .78))

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)


class Item(pygame.sprite.Sprite):

    def __init__(self, name, model, x_coordinate, y_coordinate, image, color):
        super(Item, self).__init__()

        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = pygame.image.load(image).convert()

        if scaled_800:
            self.surf = pygame.transform.smoothscale(self.surf,
                                                     (self.surf.get_width() * .78, self.surf.get_height() * .78))

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# ----------------------------------------------------------------------------------------------------------------------
# function for building executable with PyInstaller adding the data files needed (images, sounds)
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ----------------------------------------------------------------------------------------------------------------------
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
            health_bar_update_enemy(enemy_combating)

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

                # ------------------------------------------------------------------------------------------------------
                # quest checks -----------------------------------------------------------------------------------------
                # if player is on quest to kill snakes
                if enemy_combating.kind == "snake":
                    if player.current_quest == "Sneaky Snakes":
                        if player.quest_status < 4:
                            player.quest_status = player.quest_status + 1
                            quest_string = f"*** {player.quest_status}/4 snakes for [{player.current_quest}] quest ***"

                            # add to dictionary player quest updates if enemy was an objective of quest for player -
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill ghouls
                if enemy_combating.kind == "ghoul":
                    if player.current_quest == "Ghoulish Ghosts":
                        if player.quest_status < 4:
                            player.quest_status = player.quest_status + 1
                            quest_string = f"*** {player.quest_status}/4 ghouls for [{player.current_quest}] quest ***"

                            # add to dictionary player quest updates if enemy was an objective of quest for player -
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"
                # ------------------------------------------------------------------------------------------------------

                # ------------------------------------------------------------------------------------------------------
                # experienced gained by player from defeating enemy ----------------------------------------------------
                if player.level <= enemy_combating.level + 1:
                    experience = int((enemy_combating.level / player.level) * 25)
                    player.experience = player.experience + experience

                    enemy_experience = f"Gained {experience} experience."

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
                    level_up_info = level_up()
                    combat_event_dictionary["level up status"] = str(level_up_info["new level"])
                    combat_event_dictionary["level up attributes"] = str(level_up_info["player stats"])

                enemy_combating.alive_status = False
                enemy_combating.kill()

                # add to dictionary True if enemy has been defeated so scenario will end -------------------------------
                combat_event_dictionary["enemy defeated"] = True

                return combat_event_dictionary

        else:
            print("\nThis enemy appears to be dead already!")

    if combat_event == "run":

        # 50% chance of player escaping encounter
        escape_chance = random.randrange(0, 50)
        if escape_chance > 25:

            # add dialog for escape if successful. just overwrites first message in dictionary
            combat_event_dictionary["damage done"] = "You got away safely."
            # boolean to add to dictionary and return to main function if escape was successful
            combat_event_dictionary["escaped"] = True

            return combat_event_dictionary

        else:

            # add dialog for escape if not successful. just overwrites first message in dictionary
            combat_event_dictionary["damage done"] = f"{enemy_combating.name} blocked your escape."
            # boolean to add to dictionary and return to main function if escape was successful
            combat_event_dictionary["escaped"] = False

            return combat_event_dictionary


# ----------------------------------------------------------------------------------------------------------------------
# player attacks enemy, gets damage to enemy done based on player's role and equipment ---------------------------------
def attack_enemy(mob):
    # if player is lower level than mob, scale their damage based on the difference of their levels
    if player.level < mob.__getattribute__("level"):
        difference = mob.__getattribute__("level") - player.level

    # if player is equal level or higher level than mob, just return full damage value
    else:
        difference = 1

    # fighters do more damage with 2-handed weapons
    if player.role == "fighter":
        if player.equipment[0] == "2H":

            # do damage to enemy from 10-35 divided by level difference. ex. 20 dmg // 4 level = 5 overall dmg
            # level difference based on player and enemies level. player lvl 5, enemy lvl 10 = 5 difference
            damage = (random.randrange(10, 35) // difference)

            # includes player strength stat to scale overall damage
            # stat_scale = damage * player.statistics[5]

            return damage

        else:
            damage = (random.randrange(1, 10) // difference)

            return damage

    # mages do more damage with magic weapons
    if player.role == "mage":
        if player.equipment[0] == "magic":
            damage = (random.randrange(10, 35) // difference)

            # includes player wisdom stat to scale overall damage
            # stat_scale = (damage * player.statistics[7]) // 2

            return damage

        else:
            damage = (random.randrange(1, 10) // difference)

            return damage

    # rogues do more damage with 1-handed weapons
    if player.role == "rogue":
        if player.equipment[0] == "1H":
            damage = (random.randrange(10, 35) // difference)

            # includes player strength stat to scale overall damage (strength will be higher for rogues)
            # stat_scale = damage * player.statistics[5]

            return damage

        else:
            damage = (random.randrange(1, 10) // difference)

            return damage


# ----------------------------------------------------------------------------------------------------------------------
# enemy attacks player, gets damage to player done, subtract players defense level (gear) ------------------------------
def attack_player(mob):
    difference = mob.__getattribute__("level") - player.level
    base_damage = (random.randrange(10, 15))

    # add additional damage if enemy is a higher level than player. the higher the level difference, the more damage ---
    if difference >= 1:
        base_damage = base_damage + 3
    if difference >= 2:
        base_damage = base_damage + 5
    if difference >= 3:
        base_damage = base_damage + 8
    # ------------------------------------------------------------------------------------------------------------------

    # heavily armored character will take less damage
    if player.equipment[2] == "heavy":
        final_damage = base_damage - 10

        return final_damage

    # lightly armored character will take most damage
    elif player.equipment[2] == "light":
        final_damage = base_damage - 4

        return final_damage

    # medium armored character will take more damage
    elif player.equipment[2] == "medium":
        final_damage = base_damage - 7

        return final_damage

    # player is not wearing armor, return full damage
    else:
        return base_damage


# ----------------------------------------------------------------------------------------------------------------------
# player levels up, assign attributes based on player's role, return attributes and new level --------------------------
def level_up():
    level_up_dictionary = {"new level": 0, "player stats": []}

    if player.level < 20:
        if player.role == "fighter":
            player.statistics[1] = player.statistics[1] + 3  # vitality
            player.statistics[3] = player.statistics[3] + 1  # intellect
            player.statistics[5] = player.statistics[5] + 2  # strength
            player.statistics[7] = player.statistics[7] + 1  # wisdom
            player.level = player.level + 1

            # reset player health, energy and experience points
            player.health = 100
            player.energy = 100
            player.experience = 0

            level_up_dictionary["new level"] = "You are now level: " + f"{player.level}"
            level_up_dictionary["player stats"] = f"{player.statistics}"

            return level_up_dictionary

        if player.role == "mage":
            player.statistics[1] = player.statistics[1] + 1  # vitality
            player.statistics[3] = player.statistics[3] + 2  # intellect
            player.statistics[5] = player.statistics[5] + 1  # strength
            player.statistics[7] = player.statistics[7] + 3  # wisdom
            player.level = player.level + 1

            # reset player health, energy and experience points
            player.health = 100
            player.energy = 100
            player.experience = 0

            level_up_dictionary["new level"] = "You are now level: " + f"{player.level}"
            level_up_dictionary["player stats"] = f"{player.statistics}"

            return level_up_dictionary

        if player.role == "rogue":
            player.statistics[1] = player.statistics[1] + 2  # vitality
            player.statistics[3] = player.statistics[3] + 1  # intellect
            player.statistics[5] = player.statistics[5] + 3  # strength
            player.statistics[7] = player.statistics[7] + 1  # wisdom
            player.level = player.level + 1

            # reset player health, energy and experience points
            player.health = 100
            player.energy = 100
            player.experience = 0

            level_up_dictionary["new level"] = "You are now level: " + f"{player.level}"
            level_up_dictionary["player stats"] = f"{player.statistics}"

            return level_up_dictionary

    else:
        level_up_dictionary["new level"] = "You are already max level. "
        return level_up_dictionary


def npc_interaction_scenario(npc):
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

                npc_interaction_scenario(npc)

        if interaction_choice.strip().lower() == "quest" or interaction_choice.strip().lower() == "q":

            # if player has not done this NPCs quest yet
            if not npc.quest_complete:

                # if NPC has not given player their quest yet
                if player.quest != npc.quest_to_give:

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
                                    player.items.append("health potion")
                                    npc.gift = True
                                    print(
                                        "\n*** Garan has given you a weapon: [rusty sword] and gear: [damaged plate] "
                                        "***")
                                    print("\n*** Garan has also given you a: Health Potion ***")

                                if player.role == "mage":
                                    player.equipment[0] = "magic"
                                    player.equipment[1] = "broken staff"
                                    player.equipment[2] = "light"
                                    player.equipment[3] = "tattered robes"
                                    player.items.append("health potion")
                                    npc.gift = True
                                    print(
                                        "\n*** Garan has given you a weapon: [broken staff] and gear: [tattered robes] "
                                        "***")
                                    print("\n*** Garan has also given you a: Health Potion ***")

                                if player.role == "rogue":
                                    player.equipment[0] = "1H"
                                    player.equipment[1] = "dull dagger"
                                    player.equipment[2] = "medium"
                                    player.equipment[3] = "worn jerkin"
                                    player.items.append("health potion")
                                    npc.gift = True
                                    print(
                                        "\n*** Garan has given you a weapon: [dull dagger] and gear: [worn jerkin] ***")
                                    print("\n*** Garan has also given you a: Health Potion ***")

                        # if player doesn't already have an active quest (currently only can have one quest at a time)
                        if player.quest_status == 0:
                            print(f"\nYou chose to accept {npc.name}'s quest [{npc.quest_to_give}]. ")
                            player.quest = npc.quest_to_give
                            player.quest_status = 0

                            npc_interaction_scenario(npc)

                        else:
                            print(f"\nYou are already on a quest! [{player.quest}]")

                # if player has completed NPCs quest with 4 objectives, will give level and item reward
                # as well as additional dialog from NPC related to the narrative
                else:
                    if player.quest_status == 4:
                        npc.quest_complete = True
                        player.quest_status = 0
                        player.quest = ""
                        print(f"\n*** Quest [{npc.quest_to_give}] Complete! ***")

                        level_up()

                        player.rupees = player.rupees + 10
                        print(f"\n*** NPC {npc.name} has given you 10 rupees! ***")

                        player.items.append("health potion")
                        print("\n*** You have also gained a health potion! "
                              "This item has been added to your inventory. ***")

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

                            print("\n*** As you walk through the gates, you look over the side to the water below. "
                                  "***")

                            print("\n*** The Rohir River is deep and dark as it is wide. You note there are no "
                                  "other "
                                  "ways to cross. ***")

                            print("\n*** You emerge on the other side of the Bridge ***")

                            print("\n*** You are now within the Korlok District of the Consona Region World ***")

                            print("\n*** You feel the heat on your face and look around to notice the bright "
                                  "oranges "
                                  "and reds of the terrain, ***")

                            print("\n*** As well as snow-capped mountain peaks in the distance.. ***")

                            print("\n*** Where could the Vanguard Captain Adria be? ***")

                        npc_interaction_scenario(npc)

            # NPCs quest has already been completed by player
            else:
                print(f"\nYou have already completed {npc.name}'s quest [{npc.quest_to_give}]. ")

                npc_interaction_scenario(npc)

        # moves player away from NPC to return to regular action screen
        if interaction_choice.strip().lower() == "leave" or interaction_choice.strip().lower() == "l":
            print(f"\n*** You say goodbye to {npc.name} and head on your way ***")

            player.x_coordinate = player.x_coordinate + 1
            player.y_coordinate = player.y_coordinate + 1
            print(f"\n*** Your new coordinates are: {player.x_coordinate, player.y_coordinate} ***")

        # returns information based on the NPC being interacted with
        if interaction_choice.strip().lower() == "examine" or interaction_choice.strip().lower() == "exam" or \
                interaction_choice.strip().lower() == "e":
            print(f"\n*** NPC info: NPC name - {npc.name}, NPC gender - {npc.gender}, NPC race - {npc.race},"
                  f" NPC role - {npc.role} ***")

        npc_interaction_scenario(npc)

    return


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# gets current player health and updates hp bar image on screen according to the health value from 0-100
def health_bar_update(character):
    if character.health == 100:
        hp_bar.update(health_100_url)
    if character.health == 99:
        hp_bar.update(health_99_url)
    if character.health == 98:
        hp_bar.update(health_98_url)
    if character.health == 97:
        hp_bar.update(health_97_url)
    if character.health == 96:
        hp_bar.update(health_96_url)
    if character.health == 95:
        hp_bar.update(health_95_url)
    if character.health == 94:
        hp_bar.update(health_94_url)
    if character.health == 93:
        hp_bar.update(health_93_url)
    if character.health == 92:
        hp_bar.update(health_92_url)
    if character.health == 91:
        hp_bar.update(health_91_url)
    if character.health == 90:
        hp_bar.update(health_90_url)
    if character.health == 89:
        hp_bar.update(health_89_url)
    if character.health == 88:
        hp_bar.update(health_88_url)
    if character.health == 87:
        hp_bar.update(health_87_url)
    if character.health == 86:
        hp_bar.update(health_86_url)
    if character.health == 85:
        hp_bar.update(health_85_url)
    if character.health == 84:
        hp_bar.update(health_84_url)
    if character.health == 83:
        hp_bar.update(health_83_url)
    if character.health == 82:
        hp_bar.update(health_82_url)
    if character.health == 81:
        hp_bar.update(health_81_url)
    if character.health == 80:
        hp_bar.update(health_80_url)
    if character.health == 79:
        hp_bar.update(health_79_url)
    if character.health == 78:
        hp_bar.update(health_78_url)
    if character.health == 77:
        hp_bar.update(health_77_url)
    if character.health == 76:
        hp_bar.update(health_76_url)
    if character.health == 75:
        hp_bar.update(health_75_url)
    if character.health == 74:
        hp_bar.update(health_74_url)
    if character.health == 73:
        hp_bar.update(health_73_url)
    if character.health == 72:
        hp_bar.update(health_72_url)
    if character.health == 71:
        hp_bar.update(health_71_url)
    if character.health == 70:
        hp_bar.update(health_70_url)
    if character.health == 69:
        hp_bar.update(health_69_url)
    if character.health == 68:
        hp_bar.update(health_68_url)
    if character.health == 67:
        hp_bar.update(health_67_url)
    if character.health == 66:
        hp_bar.update(health_66_url)
    if character.health == 65:
        hp_bar.update(health_65_url)
    if character.health == 64:
        hp_bar.update(health_64_url)
    if character.health == 63:
        hp_bar.update(health_63_url)
    if character.health == 62:
        hp_bar.update(health_62_url)
    if character.health == 61:
        hp_bar.update(health_61_url)
    if character.health == 60:
        hp_bar.update(health_60_url)
    if character.health == 59:
        hp_bar.update(health_59_url)
    if character.health == 58:
        hp_bar.update(health_58_url)
    if character.health == 57:
        hp_bar.update(health_57_url)
    if character.health == 56:
        hp_bar.update(health_56_url)
    if character.health == 55:
        hp_bar.update(health_55_url)
    if character.health == 54:
        hp_bar.update(health_54_url)
    if character.health == 53:
        hp_bar.update(health_53_url)
    if character.health == 52:
        hp_bar.update(health_52_url)
    if character.health == 51:
        hp_bar.update(health_51_url)
    if character.health == 50:
        hp_bar.update(health_50_url)
    if character.health == 49:
        hp_bar.update(health_49_url)
    if character.health == 48:
        hp_bar.update(health_48_url)
    if character.health == 47:
        hp_bar.update(health_47_url)
    if character.health == 46:
        hp_bar.update(health_46_url)
    if character.health == 45:
        hp_bar.update(health_45_url)
    if character.health == 44:
        hp_bar.update(health_44_url)
    if character.health == 43:
        hp_bar.update(health_43_url)
    if character.health == 42:
        hp_bar.update(health_42_url)
    if character.health == 41:
        hp_bar.update(health_41_url)
    if character.health == 40:
        hp_bar.update(health_40_url)
    if character.health == 39:
        hp_bar.update(health_39_url)
    if character.health == 38:
        hp_bar.update(health_38_url)
    if character.health == 37:
        hp_bar.update(health_37_url)
    if character.health == 36:
        hp_bar.update(health_36_url)
    if character.health == 35:
        hp_bar.update(health_35_url)
    if character.health == 34:
        hp_bar.update(health_34_url)
    if character.health == 33:
        hp_bar.update(health_33_url)
    if character.health == 32:
        hp_bar.update(health_32_url)
    if character.health == 31:
        hp_bar.update(health_31_url)
    if character.health == 30:
        hp_bar.update(health_30_url)
    if character.health == 29:
        hp_bar.update(health_29_url)
    if character.health == 28:
        hp_bar.update(health_28_url)
    if character.health == 27:
        hp_bar.update(health_27_url)
    if character.health == 26:
        hp_bar.update(health_26_url)
    if character.health == 25:
        hp_bar.update(health_25_url)
    if character.health == 24:
        hp_bar.update(health_24_url)
    if character.health == 23:
        hp_bar.update(health_23_url)
    if character.health == 22:
        hp_bar.update(health_22_url)
    if character.health == 21:
        hp_bar.update(health_21_url)
    if character.health == 20:
        hp_bar.update(health_20_url)
    if character.health == 19:
        hp_bar.update(health_19_url)
    if character.health == 18:
        hp_bar.update(health_18_url)
    if character.health == 17:
        hp_bar.update(health_17_url)
    if character.health == 16:
        hp_bar.update(health_16_url)
    if character.health == 15:
        hp_bar.update(health_15_url)
    if character.health == 14:
        hp_bar.update(health_14_url)
    if character.health == 13:
        hp_bar.update(health_13_url)
    if character.health == 12:
        hp_bar.update(health_12_url)
    if character.health == 11:
        hp_bar.update(health_11_url)
    if character.health == 10:
        hp_bar.update(health_10_url)
    if character.health == 9:
        hp_bar.update(health_9_url)
    if character.health == 8:
        hp_bar.update(health_8_url)
    if character.health == 7:
        hp_bar.update(health_7_url)
    if character.health == 6:
        hp_bar.update(health_6_url)
    if character.health == 5:
        hp_bar.update(health_5_url)
    if character.health == 4:
        hp_bar.update(health_4_url)
    if character.health == 3:
        hp_bar.update(health_3_url)
    if character.health == 2:
        hp_bar.update(health_2_url)
    if character.health == 1:
        hp_bar.update(health_1_url)
    if character.health == 0:
        hp_bar.update(health_0_url)


# player energy bar update
def energy_bar_update(character):
    if character.energy == 100:
        en_bar.update(energy_100_url)
    if character.energy == 99:
        en_bar.update(energy_99_url)
    if character.energy == 98:
        en_bar.update(energy_98_url)
    if character.energy == 97:
        en_bar.update(energy_97_url)
    if character.energy == 96:
        en_bar.update(energy_96_url)
    if character.energy == 95:
        en_bar.update(energy_95_url)
    if character.energy == 94:
        en_bar.update(energy_94_url)
    if character.energy == 93:
        en_bar.update(energy_93_url)
    if character.energy == 92:
        en_bar.update(energy_92_url)
    if character.energy == 91:
        en_bar.update(energy_91_url)
    if character.energy == 90:
        en_bar.update(energy_90_url)
    if character.energy == 89:
        en_bar.update(energy_89_url)
    if character.energy == 88:
        en_bar.update(energy_88_url)
    if character.energy == 87:
        en_bar.update(energy_87_url)
    if character.energy == 86:
        en_bar.update(energy_86_url)
    if character.energy == 85:
        en_bar.update(energy_85_url)
    if character.energy == 84:
        en_bar.update(energy_84_url)
    if character.energy == 83:
        en_bar.update(energy_83_url)
    if character.energy == 82:
        en_bar.update(energy_82_url)
    if character.energy == 81:
        en_bar.update(energy_81_url)
    if character.energy == 80:
        en_bar.update(energy_80_url)
    if character.energy == 79:
        en_bar.update(energy_79_url)
    if character.energy == 78:
        en_bar.update(energy_78_url)
    if character.energy == 77:
        en_bar.update(energy_77_url)
    if character.energy == 76:
        en_bar.update(energy_76_url)
    if character.energy == 75:
        en_bar.update(energy_75_url)
    if character.energy == 74:
        en_bar.update(energy_74_url)
    if character.energy == 73:
        en_bar.update(energy_73_url)
    if character.energy == 72:
        en_bar.update(energy_72_url)
    if character.energy == 71:
        en_bar.update(energy_71_url)
    if character.energy == 70:
        en_bar.update(energy_70_url)
    if character.energy == 69:
        en_bar.update(energy_69_url)
    if character.energy == 68:
        en_bar.update(energy_68_url)
    if character.energy == 67:
        en_bar.update(energy_67_url)
    if character.energy == 66:
        en_bar.update(energy_66_url)
    if character.energy == 65:
        en_bar.update(energy_65_url)
    if character.energy == 64:
        en_bar.update(energy_64_url)
    if character.energy == 63:
        en_bar.update(energy_63_url)
    if character.energy == 62:
        en_bar.update(energy_62_url)
    if character.energy == 61:
        en_bar.update(energy_61_url)
    if character.energy == 60:
        en_bar.update(energy_60_url)
    if character.energy == 59:
        en_bar.update(energy_59_url)
    if character.energy == 58:
        en_bar.update(energy_58_url)
    if character.energy == 57:
        en_bar.update(energy_57_url)
    if character.energy == 56:
        en_bar.update(energy_56_url)
    if character.energy == 55:
        en_bar.update(energy_55_url)
    if character.energy == 54:
        en_bar.update(energy_54_url)
    if character.energy == 53:
        en_bar.update(energy_53_url)
    if character.energy == 52:
        en_bar.update(energy_52_url)
    if character.energy == 51:
        en_bar.update(energy_51_url)
    if character.energy == 50:
        en_bar.update(energy_50_url)
    if character.energy == 49:
        en_bar.update(energy_49_url)
    if character.energy == 48:
        en_bar.update(energy_48_url)
    if character.energy == 47:
        en_bar.update(energy_47_url)
    if character.energy == 46:
        en_bar.update(energy_46_url)
    if character.energy == 45:
        en_bar.update(energy_45_url)
    if character.energy == 44:
        en_bar.update(energy_44_url)
    if character.energy == 43:
        en_bar.update(energy_43_url)
    if character.energy == 42:
        en_bar.update(energy_42_url)
    if character.energy == 41:
        en_bar.update(energy_41_url)
    if character.energy == 40:
        en_bar.update(energy_40_url)
    if character.energy == 39:
        en_bar.update(energy_39_url)
    if character.energy == 38:
        en_bar.update(energy_38_url)
    if character.energy == 37:
        en_bar.update(energy_37_url)
    if character.energy == 36:
        en_bar.update(energy_36_url)
    if character.energy == 35:
        en_bar.update(energy_35_url)
    if character.energy == 34:
        en_bar.update(energy_34_url)
    if character.energy == 33:
        en_bar.update(energy_33_url)
    if character.energy == 32:
        en_bar.update(energy_32_url)
    if character.energy == 31:
        en_bar.update(energy_31_url)
    if character.energy == 30:
        en_bar.update(energy_30_url)
    if character.energy == 29:
        en_bar.update(energy_29_url)
    if character.energy == 28:
        en_bar.update(energy_28_url)
    if character.energy == 27:
        en_bar.update(energy_27_url)
    if character.energy == 26:
        en_bar.update(energy_26_url)
    if character.energy == 25:
        en_bar.update(energy_25_url)
    if character.energy == 24:
        en_bar.update(energy_24_url)
    if character.energy == 23:
        en_bar.update(energy_23_url)
    if character.energy == 22:
        en_bar.update(energy_22_url)
    if character.energy == 21:
        en_bar.update(energy_21_url)
    if character.energy == 20:
        en_bar.update(energy_20_url)
    if character.energy == 19:
        en_bar.update(energy_19_url)
    if character.energy == 18:
        en_bar.update(energy_18_url)
    if character.energy == 17:
        en_bar.update(energy_17_url)
    if character.energy == 16:
        en_bar.update(energy_16_url)
    if character.energy == 15:
        en_bar.update(energy_15_url)
    if character.energy == 14:
        en_bar.update(energy_14_url)
    if character.energy == 13:
        en_bar.update(energy_13_url)
    if character.energy == 12:
        en_bar.update(energy_12_url)
    if character.energy == 11:
        en_bar.update(energy_11_url)
    if character.energy == 10:
        en_bar.update(energy_10_url)
    if character.energy == 9:
        en_bar.update(energy_9_url)
    if character.energy == 8:
        en_bar.update(energy_8_url)
    if character.energy == 7:
        en_bar.update(energy_7_url)
    if character.energy == 6:
        en_bar.update(energy_6_url)
    if character.energy == 5:
        en_bar.update(energy_5_url)
    if character.energy == 4:
        en_bar.update(energy_4_url)
    if character.energy == 3:
        en_bar.update(energy_3_url)
    if character.energy == 2:
        en_bar.update(energy_2_url)
    if character.energy == 1:
        en_bar.update(energy_1_url)
    if character.energy == 0:
        en_bar.update(energy_0_url)


# player xp bar update
def xp_bar_update(character):
    if character.experience == 100:
        xp_bar.update(xp_100_url)
    if character.experience == 99:
        xp_bar.update(xp_99_url)
    if character.experience == 98:
        xp_bar.update(xp_98_url)
    if character.experience == 97:
        xp_bar.update(xp_97_url)
    if character.experience == 96:
        xp_bar.update(xp_96_url)
    if character.experience == 95:
        xp_bar.update(xp_95_url)
    if character.experience == 94:
        xp_bar.update(xp_94_url)
    if character.experience == 93:
        xp_bar.update(xp_93_url)
    if character.experience == 92:
        xp_bar.update(xp_92_url)
    if character.experience == 91:
        xp_bar.update(xp_91_url)
    if character.experience == 90:
        xp_bar.update(xp_90_url)
    if character.experience == 89:
        xp_bar.update(xp_89_url)
    if character.experience == 88:
        xp_bar.update(xp_88_url)
    if character.experience == 87:
        xp_bar.update(xp_87_url)
    if character.experience == 86:
        xp_bar.update(xp_86_url)
    if character.experience == 85:
        xp_bar.update(xp_85_url)
    if character.experience == 84:
        xp_bar.update(xp_84_url)
    if character.experience == 83:
        xp_bar.update(xp_83_url)
    if character.experience == 82:
        xp_bar.update(xp_82_url)
    if character.experience == 81:
        xp_bar.update(xp_81_url)
    if character.experience == 80:
        xp_bar.update(xp_80_url)
    if character.experience == 79:
        xp_bar.update(xp_79_url)
    if character.experience == 78:
        xp_bar.update(xp_78_url)
    if character.experience == 77:
        xp_bar.update(xp_77_url)
    if character.experience == 76:
        xp_bar.update(xp_76_url)
    if character.experience == 75:
        xp_bar.update(xp_75_url)
    if character.experience == 74:
        xp_bar.update(xp_74_url)
    if character.experience == 73:
        xp_bar.update(xp_73_url)
    if character.experience == 72:
        xp_bar.update(xp_72_url)
    if character.experience == 71:
        xp_bar.update(xp_71_url)
    if character.experience == 70:
        xp_bar.update(xp_70_url)
    if character.experience == 69:
        xp_bar.update(xp_69_url)
    if character.experience == 68:
        xp_bar.update(xp_68_url)
    if character.experience == 67:
        xp_bar.update(xp_67_url)
    if character.experience == 66:
        xp_bar.update(xp_66_url)
    if character.experience == 65:
        xp_bar.update(xp_65_url)
    if character.experience == 64:
        xp_bar.update(xp_64_url)
    if character.experience == 63:
        xp_bar.update(xp_63_url)
    if character.experience == 62:
        xp_bar.update(xp_62_url)
    if character.experience == 61:
        xp_bar.update(xp_61_url)
    if character.experience == 60:
        xp_bar.update(xp_60_url)
    if character.experience == 59:
        xp_bar.update(xp_59_url)
    if character.experience == 58:
        xp_bar.update(xp_58_url)
    if character.experience == 57:
        xp_bar.update(xp_57_url)
    if character.experience == 56:
        xp_bar.update(xp_56_url)
    if character.experience == 55:
        xp_bar.update(xp_55_url)
    if character.experience == 54:
        xp_bar.update(xp_54_url)
    if character.experience == 53:
        xp_bar.update(xp_53_url)
    if character.experience == 52:
        xp_bar.update(xp_52_url)
    if character.experience == 51:
        xp_bar.update(xp_51_url)
    if character.experience == 50:
        xp_bar.update(xp_50_url)
    if character.experience == 49:
        xp_bar.update(xp_49_url)
    if character.experience == 48:
        xp_bar.update(xp_48_url)
    if character.experience == 47:
        xp_bar.update(xp_47_url)
    if character.experience == 46:
        xp_bar.update(xp_46_url)
    if character.experience == 45:
        xp_bar.update(xp_45_url)
    if character.experience == 44:
        xp_bar.update(xp_44_url)
    if character.experience == 43:
        xp_bar.update(xp_43_url)
    if character.experience == 42:
        xp_bar.update(xp_42_url)
    if character.experience == 41:
        xp_bar.update(xp_41_url)
    if character.experience == 40:
        xp_bar.update(xp_40_url)
    if character.experience == 39:
        xp_bar.update(xp_39_url)
    if character.experience == 38:
        xp_bar.update(xp_38_url)
    if character.experience == 37:
        xp_bar.update(xp_37_url)
    if character.experience == 36:
        xp_bar.update(xp_36_url)
    if character.experience == 35:
        xp_bar.update(xp_35_url)
    if character.experience == 34:
        xp_bar.update(xp_34_url)
    if character.experience == 33:
        xp_bar.update(xp_33_url)
    if character.experience == 32:
        xp_bar.update(xp_32_url)
    if character.experience == 31:
        xp_bar.update(xp_31_url)
    if character.experience == 30:
        xp_bar.update(xp_30_url)
    if character.experience == 29:
        xp_bar.update(xp_29_url)
    if character.experience == 28:
        xp_bar.update(xp_28_url)
    if character.experience == 27:
        xp_bar.update(xp_27_url)
    if character.experience == 26:
        xp_bar.update(xp_26_url)
    if character.experience == 25:
        xp_bar.update(xp_25_url)
    if character.experience == 24:
        xp_bar.update(xp_24_url)
    if character.experience == 23:
        xp_bar.update(xp_23_url)
    if character.experience == 22:
        xp_bar.update(xp_22_url)
    if character.experience == 21:
        xp_bar.update(xp_21_url)
    if character.experience == 20:
        xp_bar.update(xp_20_url)
    if character.experience == 19:
        xp_bar.update(xp_19_url)
    if character.experience == 18:
        xp_bar.update(xp_18_url)
    if character.experience == 17:
        xp_bar.update(xp_17_url)
    if character.experience == 16:
        xp_bar.update(xp_16_url)
    if character.experience == 15:
        xp_bar.update(xp_15_url)
    if character.experience == 14:
        xp_bar.update(xp_14_url)
    if character.experience == 13:
        xp_bar.update(xp_13_url)
    if character.experience == 12:
        xp_bar.update(xp_12_url)
    if character.experience == 11:
        xp_bar.update(xp_11_url)
    if character.experience == 10:
        xp_bar.update(xp_10_url)
    if character.experience == 9:
        xp_bar.update(xp_9_url)
    if character.experience == 8:
        xp_bar.update(xp_8_url)
    if character.experience == 7:
        xp_bar.update(xp_7_url)
    if character.experience == 6:
        xp_bar.update(xp_6_url)
    if character.experience == 5:
        xp_bar.update(xp_5_url)
    if character.experience == 4:
        xp_bar.update(xp_4_url)
    if character.experience == 3:
        xp_bar.update(xp_3_url)
    if character.experience == 2:
        xp_bar.update(xp_2_url)
    if character.experience == 1:
        xp_bar.update(xp_1_url)
    if character.experience == 0:
        xp_bar.update(xp_0_url)


# enemy health bar update
def health_bar_update_enemy(character):
    if character.health == 100:
        character.health_bar.update(health_100_url)
    if character.health == 99:
        character.health_bar.update(health_99_url)
    if character.health == 98:
        character.health_bar.update(health_98_url)
    if character.health == 97:
        character.health_bar.update(health_97_url)
    if character.health == 96:
        character.health_bar.update(health_96_url)
    if character.health == 95:
        character.health_bar.update(health_95_url)
    if character.health == 94:
        character.health_bar.update(health_94_url)
    if character.health == 93:
        character.health_bar.update(health_93_url)
    if character.health == 92:
        character.health_bar.update(health_92_url)
    if character.health == 91:
        character.health_bar.update(health_91_url)
    if character.health == 90:
        character.health_bar.update(health_90_url)
    if character.health == 89:
        character.health_bar.update(health_89_url)
    if character.health == 88:
        character.health_bar.update(health_88_url)
    if character.health == 87:
        character.health_bar.update(health_87_url)
    if character.health == 86:
        character.health_bar.update(health_86_url)
    if character.health == 85:
        character.health_bar.update(health_85_url)
    if character.health == 84:
        character.health_bar.update(health_84_url)
    if character.health == 83:
        character.health_bar.update(health_83_url)
    if character.health == 82:
        character.health_bar.update(health_82_url)
    if character.health == 81:
        character.health_bar.update(health_81_url)
    if character.health == 80:
        character.health_bar.update(health_80_url)
    if character.health == 79:
        character.health_bar.update(health_79_url)
    if character.health == 78:
        character.health_bar.update(health_78_url)
    if character.health == 77:
        character.health_bar.update(health_77_url)
    if character.health == 76:
        character.health_bar.update(health_76_url)
    if character.health == 75:
        character.health_bar.update(health_75_url)
    if character.health == 74:
        character.health_bar.update(health_74_url)
    if character.health == 73:
        character.health_bar.update(health_73_url)
    if character.health == 72:
        character.health_bar.update(health_72_url)
    if character.health == 71:
        character.health_bar.update(health_71_url)
    if character.health == 70:
        character.health_bar.update(health_70_url)
    if character.health == 69:
        character.health_bar.update(health_69_url)
    if character.health == 68:
        character.health_bar.update(health_68_url)
    if character.health == 67:
        character.health_bar.update(health_67_url)
    if character.health == 66:
        character.health_bar.update(health_66_url)
    if character.health == 65:
        character.health_bar.update(health_65_url)
    if character.health == 64:
        character.health_bar.update(health_64_url)
    if character.health == 63:
        character.health_bar.update(health_63_url)
    if character.health == 62:
        character.health_bar.update(health_62_url)
    if character.health == 61:
        character.health_bar.update(health_61_url)
    if character.health == 60:
        character.health_bar.update(health_60_url)
    if character.health == 59:
        character.health_bar.update(health_59_url)
    if character.health == 58:
        character.health_bar.update(health_58_url)
    if character.health == 57:
        character.health_bar.update(health_57_url)
    if character.health == 56:
        character.health_bar.update(health_56_url)
    if character.health == 55:
        character.health_bar.update(health_55_url)
    if character.health == 54:
        character.health_bar.update(health_54_url)
    if character.health == 53:
        character.health_bar.update(health_53_url)
    if character.health == 52:
        character.health_bar.update(health_52_url)
    if character.health == 51:
        character.health_bar.update(health_51_url)
    if character.health == 50:
        character.health_bar.update(health_50_url)
    if character.health == 49:
        character.health_bar.update(health_49_url)
    if character.health == 48:
        character.health_bar.update(health_48_url)
    if character.health == 47:
        character.health_bar.update(health_47_url)
    if character.health == 46:
        character.health_bar.update(health_46_url)
    if character.health == 45:
        character.health_bar.update(health_45_url)
    if character.health == 44:
        character.health_bar.update(health_44_url)
    if character.health == 43:
        character.health_bar.update(health_43_url)
    if character.health == 42:
        character.health_bar.update(health_42_url)
    if character.health == 41:
        character.health_bar.update(health_41_url)
    if character.health == 40:
        character.health_bar.update(health_40_url)
    if character.health == 39:
        character.health_bar.update(health_39_url)
    if character.health == 38:
        character.health_bar.update(health_38_url)
    if character.health == 37:
        character.health_bar.update(health_37_url)
    if character.health == 36:
        character.health_bar.update(health_36_url)
    if character.health == 35:
        character.health_bar.update(health_35_url)
    if character.health == 34:
        character.health_bar.update(health_34_url)
    if character.health == 33:
        character.health_bar.update(health_33_url)
    if character.health == 32:
        character.health_bar.update(health_32_url)
    if character.health == 31:
        character.health_bar.update(health_31_url)
    if character.health == 30:
        character.health_bar.update(health_30_url)
    if character.health == 29:
        character.health_bar.update(health_29_url)
    if character.health == 28:
        character.health_bar.update(health_28_url)
    if character.health == 27:
        character.health_bar.update(health_27_url)
    if character.health == 26:
        character.health_bar.update(health_26_url)
    if character.health == 25:
        character.health_bar.update(health_25_url)
    if character.health == 24:
        character.health_bar.update(health_24_url)
    if character.health == 23:
        character.health_bar.update(health_23_url)
    if character.health == 22:
        character.health_bar.update(health_22_url)
    if character.health == 21:
        character.health_bar.update(health_21_url)
    if character.health == 20:
        character.health_bar.update(health_20_url)
    if character.health == 19:
        character.health_bar.update(health_19_url)
    if character.health == 18:
        character.health_bar.update(health_18_url)
    if character.health == 17:
        character.health_bar.update(health_17_url)
    if character.health == 16:
        character.health_bar.update(health_16_url)
    if character.health == 15:
        character.health_bar.update(health_15_url)
    if character.health == 14:
        character.health_bar.update(health_14_url)
    if character.health == 13:
        character.health_bar.update(health_13_url)
    if character.health == 12:
        character.health_bar.update(health_12_url)
    if character.health == 11:
        character.health_bar.update(health_11_url)
    if character.health == 10:
        character.health_bar.update(health_10_url)
    if character.health == 9:
        character.health_bar.update(health_9_url)
    if character.health == 8:
        character.health_bar.update(health_8_url)
    if character.health == 7:
        character.health_bar.update(health_7_url)
    if character.health == 6:
        character.health_bar.update(health_6_url)
    if character.health == 5:
        character.health_bar.update(health_5_url)
    if character.health == 4:
        character.health_bar.update(health_4_url)
    if character.health == 3:
        character.health_bar.update(health_3_url)
    if character.health == 2:
        character.health_bar.update(health_2_url)
    if character.health == 1:
        character.health_bar.update(health_1_url)
    if character.health == 0:
        character.health_bar.update(health_0_url)


# ----------------------------------------------------------------------------------------------------------------------
# getting event based on user click related to combat scenario (attack, skill and run buttons)
def combat_event_button(combat_event):
    if combat_event.type == pygame.MOUSEBUTTONUP:
        combat_mouse = pygame.mouse.get_pos()

        # if mouse rect collides with attack button, skill button or run button return string representing it
        if attack_button.rect.collidepoint(combat_mouse):
            return "attack"

        if skill_button.rect.collidepoint(combat_mouse):
            return "skill"

        if run_button.rect.collidepoint(combat_mouse):
            return "run"


# ----------------------------------------------------------------------------------------------------------------------
# getting event based on user click related to shop scenario (buy, sell and leave buttons)
def shop_event_button(shop_event):
    if shop_event.type == pygame.MOUSEBUTTONUP:
        shop_mouse = pygame.mouse.get_pos()

        # if mouse rect collides with buy button, sell button or leave button return string representing it
        if buy_button.rect.collidepoint(shop_mouse):
            return "buy"

        if sell_button.rect.collidepoint(shop_mouse):
            return "sell"

        if leave_button.rect.collidepoint(shop_mouse):
            return "leave"


# ----------------------------------------------------------------------------------------------------------------------
# getting event based on user click related to shop scenario (buy, sell and leave buttons)
def inn_event_button(inn_event):
    if inn_event.type == pygame.MOUSEBUTTONUP:
        inn_mouse = pygame.mouse.get_pos()

        # if mouse rect collides with buy button, sell button or leave button return string representing it
        if rest_button.rect.collidepoint(inn_mouse):
            return "rest"

        if leave_button.rect.collidepoint(inn_mouse):
            return "leave"


# ----------------------------------------------------------------------------------------------------------------------
# getting item player clicked based on it's name and return the corresponding item, for clicking on inventory items
def inventory_event_item(inventory_event):
    if inventory_event.type == pygame.MOUSEBUTTONUP:
        inventory_mouse = pygame.mouse.get_pos()

        # list of sprites that collided with mouse cursor rect
        clicked_element = [inventory_element for inventory_element in player_items
                           if inventory_element.rect.collidepoint(inventory_mouse)]

        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_element[0].__getattribute__("name") == "health potion":
                return clicked_element[0]

            if clicked_element[0].__getattribute__("name") == "energy potion":
                return clicked_element[0]

            if clicked_element[0].__getattribute__("name") == "shiny rock":
                return clicked_element[0]

            if clicked_element[0].__getattribute__("name") == "bone dust":
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
            if clicked_element[0].__getattribute__("name") == "health potion":
                return clicked_element[0]

            if clicked_element[0].__getattribute__("name") == "energy potion":
                return clicked_element[0]

            if clicked_element[0].__getattribute__("name") == "shiny rock":
                return clicked_element[0]

            if clicked_element[0].__getattribute__("name") == "bone dust":
                return clicked_element[0]

        except IndexError:
            pass


# ----------------------------------------------------------------------------------------------------------------------
# getting item player clicked based on it's name and return the corresponding item, for clicking on sell items
def sell_event_item(sell_event):
    if sell_event.type == pygame.MOUSEBUTTONUP:
        sell_mouse = pygame.mouse.get_pos()

        # list of sprites that collided with mouse cursor rect
        clicked_element = [sell_element for sell_element in sell_player_items if
                           sell_element.rect.collidepoint(sell_mouse)]

        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_element[0].__getattribute__("name") == "health potion":
                return clicked_element[0]

            if clicked_element[0].__getattribute__("name") == "energy potion":
                return clicked_element[0]

            if clicked_element[0].__getattribute__("name") == "shiny rock":
                return clicked_element[0]

            if clicked_element[0].__getattribute__("name") == "bone dust":
                return clicked_element[0]

        except IndexError:
            pass


# ----------------------------------------------------------------------------------------------------------------------
# function to respawn enemies if they are less than a specified amount active in game. spawns with random coord. and lvl
def enemy_respawn():
    snake_counter = 0
    ghoul_counter = 0

    # generate random coordinates and level for new enemy to spawn within boundaries and level range
    random_snake_x = random.randrange(150, 300)
    random_snake_y = random.randrange(150, 300)
    random_snake_level = random.randrange(1, 4)

    random_ghoul_x = random.randrange(650, 900)
    random_ghoul_y = random.randrange(150, 300)
    random_ghoul_level = random.randrange(3, 6)

    # count current enemies active in game
    for mob in enemies:
        if mob.__getattribute__("kind") == "snake":
            snake_counter += 1
        if mob.__getattribute__("kind") == "ghoul":
            ghoul_counter += 1

    # if there are less than 3 snakes in game, create another snake with random level and coordinates. add to groups
    if snake_counter < 3:
        new_snake = Enemy("Snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y, True,
                          Item("shiny rock", "rock", 200, 200, shiny_rock_url,
                               (255, 255, 255)), snake_url, (255, 255, 255),
                          UiElement("snake hp bar", 700, 90, health_100_url, (255, 255, 255), False))
        snakes.add(new_snake)
        enemies.add(new_snake)
        all_sprites.add(new_snake)

    # if there are less than 3 ghouls in game, create another ghoul with random level and coordinates. add to groups
    if ghoul_counter < 3:
        new_ghoul = Enemy("Ghoul", "ghoul", 100, 100, random_ghoul_level, random_ghoul_x, random_ghoul_y, True,
                          Item("bone dust", "dust", 200, 200, bone_dust_url, (255, 255, 255)),
                          ghoul_url, (255, 255, 255),
                          UiElement("ghoul hp bar", 700, 90, health_100_url, (255, 255, 255), False))
        ghouls.add(new_ghoul)
        enemies.add(new_ghoul)
        all_sprites.add(new_ghoul)


# leftover code from template to add moving clouds, can be used later for other scenery or critters --------------------
# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
# class Cloud(pygame.sprite.Sprite):
# def __init__(self):
# super(Cloud, self).__init__()
# self.surf = pygame.image.load("cloud.png").convert()
# self.surf.set_colorkey((0, 0, 0), RLEACCEL)
# The starting position is randomly generated
# self.rect = self.surf.get_rect(
# center=(
# random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
# random.randint(0, SCREEN_HEIGHT),
# )
# )

# Move the cloud based on a constant speed
# Remove it when it passes the left edge of the screen
# def update(self):
# self.rect.move_ip(-5, 0)
# if self.rect.right < 0:
# self.kill()
# ----------------------------------------------------------------------------------------------------------------------

# will be used for music later -----------------------------------------------------------------------------------------
# pygame.mixer.init()

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# asset urls -----------------------------------------------------------------------------------------------------------
stan_down_url = resource_path('resources/art/character_art/player_character/default/stan_down.png')
stan_left_url = resource_path('resources/art/character_art/player_character/default/stan_left.png')
stan_right_url = resource_path('resources/art/character_art/player_character/default/stan_right.png')
stan_up_url = resource_path('resources/art/character_art/player_character/default/stan_up.png')
stan_battle_url = resource_path('resources/art/character_art/player_character/default/battle/stan_battle.png')
stan_attack_url = resource_path('resources/art/character_art/player_character/default/battle/stan_battle_attacking.png')

amuna_shopkeeper_url = resource_path('resources/art/character_art/NPCs/shops/amuna_shopkeeper.png')
garan_url = resource_path('resources/art/character_art/NPCs/garan/garan.png')
garan_left_url = resource_path('resources/art/character_art/NPCs/garan/garan_left.png')
garan_right_url = resource_path('resources/art/character_art/NPCs/garan/garan_right.png')
garan_back_url = resource_path('resources/art/character_art/NPCs/garan/garan_back.png')

guard_url = resource_path('resources/art/character_art/NPCs/guards/guard.png')
guard_left_url = resource_path('resources/art/character_art/NPCs/guards/guard_left.png')
guard_right_url = resource_path('resources/art/character_art/NPCs/guards/guard_right.png')
guard_back_url = resource_path('resources/art/character_art/NPCs/guards/guard_back.png')

maurelle_url = resource_path('resources/art/character_art/NPCs/maurelle/maurelle.png')
maurelle_left_url = resource_path('resources/art/character_art/NPCs/maurelle/maurelle_left.png')
maurelle_right_url = resource_path('resources/art/character_art/NPCs/maurelle/maurelle_right.png')
maurelle_back_url = resource_path('resources/art/character_art/NPCs/maurelle/maurelle_back.png')

snake_url = resource_path('resources/art/enemy_art/snake.png')
ghoul_url = resource_path('resources/art/enemy_art/ghoul.png')
snake_battle_url = resource_path('resources/art/enemy_art/battle/snake_battle.png')
snake_attack_url = resource_path('resources/art/enemy_art/battle/snake_battle_attacking.png')
ghoul_battle_url = resource_path('resources/art/enemy_art/battle/ghoul_battle.png')
ghoul_attack_url = resource_path('resources/art/enemy_art/battle/ghoul_battle_attacking.png')

seldon_bg_url = resource_path('resources/art/environment_art/background_textures/seldon_district.png')
seldon_battle_url = resource_path('resources/art/environment_art/background_textures/seldon_battle_screen.png')
seldon_shop_screen_url = resource_path('resources/art/environment_art/background_textures/seldon_shop.png')
seldon_inn_screen_url = resource_path('resources/art/environment_art/background_textures/seldon_inn.png')

seldon_academia_url = resource_path('resources/art/environment_art/buildings/amuna_building_academia.png')
seldon_inn_url = resource_path('resources/art/environment_art/buildings/amuna_building_inn.png')
seldon_shop_url = resource_path('resources/art/environment_art/buildings/amuna_building_shop.png')

pine_tree_url = resource_path('resources/art/environment_art/pine_tree.png')
seldon_grass_url = resource_path('resources/art/environment_art/seldon_grass.png')
seldon_flower_url = resource_path('resources/art/environment_art/seldon_flower.png')

health_pot_url = resource_path('resources/art/item_art/health_potion.png')
energy_pot_url = resource_path('resources/art/item_art/energy_potion.png')
shiny_rock_url = resource_path('resources/art/item_art/shiny_rock.png')
bone_dust_url = resource_path('resources/art/item_art/bone_dust.png')
temp_item_url = resource_path('resources/art/item_art/temp_item.png')

game_over_screen_url = resource_path('resources/art/screens/game_over.png')
nera_sleep_screen_url = resource_path('resources/art/screens/nera_sleep_screen.png')

bar_backdrop_url = resource_path('resources/art/ui_elements/status_bar_backdrop.png')
enemy_bar_backdrop_url = resource_path('resources/art/ui_elements/enemy_status_bar_backdrop.png')
buy_inventory_url = resource_path('resources/art/ui_elements/buy_inventory.png')
sell_inventory_url = resource_path('resources/art/ui_elements/sell_inventory.png')
inventory_url = resource_path('resources/art/ui_elements/inventory.png')
message_box_url = resource_path('resources/art/ui_elements/message_box.png')
player_status_url = resource_path('resources/art/ui_elements/status/player.png')
enemy_status_url = resource_path('resources/art/ui_elements/status/enemy.png')
welcome_image_url = resource_path('resources/art/ui_elements/notifications/welcome.png')
character_button_url = resource_path('resources/art/ui_elements/buttons/character.png')
continue_button_url = resource_path('resources/art/ui_elements/buttons/continue_button.png')
interact_button_url = resource_path('resources/art/ui_elements/buttons/interact.png')
inventory_button_url = resource_path('resources/art/ui_elements/buttons/inventory.png')
journal_button_url = resource_path('resources/art/ui_elements/buttons/journal.png')
buy_button_url = resource_path('resources/art/ui_elements/buttons/shop/buy.png')
sell_button_url = resource_path('resources/art/ui_elements/buttons/shop/sell.png')
leave_button_url = resource_path('resources/art/ui_elements/buttons/shop/leave.png')
attack_button_url = resource_path('resources/art/ui_elements/buttons/battle_screen/attack.png')
skill_button_url = resource_path('resources/art/ui_elements/buttons/battle_screen/skill.png')
run_button_url = resource_path('resources/art/ui_elements/buttons/battle_screen/run.png')
rest_button_url = resource_path('resources/art/ui_elements/buttons/inn/rest.png')
screen_size_button_url = resource_path('resources/art/ui_elements/buttons/screen_size.png')
screen_size_window_url = resource_path('resources/art/ui_elements/resize_options.png')
s_1200x900_url = resource_path('resources/art/ui_elements/buttons/screen_size_buttons/1200.png')
s_1024x768_url = resource_path('resources/art/ui_elements/buttons/screen_size_buttons/1024.png')
s_800x600_url = resource_path('resources/art/ui_elements/buttons/screen_size_buttons/800.png')

health_100_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_100.png')
health_99_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_99.png')
health_98_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_98.png')
health_97_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_97.png')
health_96_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_96.png')
health_95_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_95.png')
health_94_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_94.png')
health_93_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_93.png')
health_92_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_92.png')
health_91_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_91.png')
health_90_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_90.png')
health_89_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_89.png')
health_88_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_88.png')
health_87_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_87.png')
health_86_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_86.png')
health_85_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_85.png')
health_84_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_84.png')
health_83_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_83.png')
health_82_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_82.png')
health_81_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_81.png')
health_80_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_80.png')
health_79_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_79.png')
health_78_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_78.png')
health_77_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_77.png')
health_76_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_76.png')
health_75_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_75.png')
health_74_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_74.png')
health_73_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_73.png')
health_72_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_72.png')
health_71_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_71.png')
health_70_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_70.png')
health_69_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_69.png')
health_68_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_68.png')
health_67_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_67.png')
health_66_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_66.png')
health_65_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_65.png')
health_64_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_64.png')
health_63_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_63.png')
health_62_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_62.png')
health_61_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_61.png')
health_60_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_60.png')
health_59_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_59.png')
health_58_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_58.png')
health_57_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_57.png')
health_56_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_56.png')
health_55_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_55.png')
health_54_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_54.png')
health_53_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_53.png')
health_52_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_52.png')
health_51_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_51.png')
health_50_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_50.png')
health_49_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_49.png')
health_48_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_48.png')
health_47_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_47.png')
health_46_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_46.png')
health_45_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_45.png')
health_44_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_44.png')
health_43_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_43.png')
health_42_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_42.png')
health_41_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_41.png')
health_40_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_40.png')
health_39_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_39.png')
health_38_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_38.png')
health_37_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_37.png')
health_36_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_36.png')
health_35_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_35.png')
health_34_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_34.png')
health_33_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_33.png')
health_32_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_32.png')
health_31_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_31.png')
health_30_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_30.png')
health_29_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_29.png')
health_28_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_28.png')
health_27_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_27.png')
health_26_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_26.png')
health_25_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_25.png')
health_24_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_24.png')
health_23_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_23.png')
health_22_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_22.png')
health_21_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_21.png')
health_20_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_20.png')
health_19_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_19.png')
health_18_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_18.png')
health_17_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_17.png')
health_16_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_16.png')
health_15_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_15.png')
health_14_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_14.png')
health_13_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_13.png')
health_12_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_12.png')
health_11_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_11.png')
health_10_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_10.png')
health_9_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_9.png')
health_8_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_8.png')
health_7_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_7.png')
health_6_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_6.png')
health_5_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_5.png')
health_4_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_4.png')
health_3_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_3.png')
health_2_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_2.png')
health_1_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_1.png')
health_0_url = resource_path('resources/art/ui_elements/bars/health/hp_bar_0.png')

energy_100_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_100.png')
energy_99_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_99.png')
energy_98_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_98.png')
energy_97_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_97.png')
energy_96_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_96.png')
energy_95_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_95.png')
energy_94_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_94.png')
energy_93_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_93.png')
energy_92_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_92.png')
energy_91_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_91.png')
energy_90_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_90.png')
energy_89_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_89.png')
energy_88_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_88.png')
energy_87_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_87.png')
energy_86_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_86.png')
energy_85_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_85.png')
energy_84_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_84.png')
energy_83_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_83.png')
energy_82_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_82.png')
energy_81_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_81.png')
energy_80_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_80.png')
energy_79_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_79.png')
energy_78_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_78.png')
energy_77_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_77.png')
energy_76_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_76.png')
energy_75_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_75.png')
energy_74_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_74.png')
energy_73_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_73.png')
energy_72_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_72.png')
energy_71_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_71.png')
energy_70_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_70.png')
energy_69_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_69.png')
energy_68_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_68.png')
energy_67_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_67.png')
energy_66_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_66.png')
energy_65_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_65.png')
energy_64_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_64.png')
energy_63_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_63.png')
energy_62_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_62.png')
energy_61_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_61.png')
energy_60_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_60.png')
energy_59_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_59.png')
energy_58_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_58.png')
energy_57_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_57.png')
energy_56_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_56.png')
energy_55_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_55.png')
energy_54_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_54.png')
energy_53_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_53.png')
energy_52_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_52.png')
energy_51_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_51.png')
energy_50_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_50.png')
energy_49_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_49.png')
energy_48_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_48.png')
energy_47_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_47.png')
energy_46_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_46.png')
energy_45_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_45.png')
energy_44_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_44.png')
energy_43_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_43.png')
energy_42_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_42.png')
energy_41_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_41.png')
energy_40_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_40.png')
energy_39_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_39.png')
energy_38_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_38.png')
energy_37_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_37.png')
energy_36_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_36.png')
energy_35_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_35.png')
energy_34_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_34.png')
energy_33_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_33.png')
energy_32_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_32.png')
energy_31_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_31.png')
energy_30_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_30.png')
energy_29_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_29.png')
energy_28_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_28.png')
energy_27_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_27.png')
energy_26_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_26.png')
energy_25_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_25.png')
energy_24_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_24.png')
energy_23_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_23.png')
energy_22_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_22.png')
energy_21_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_21.png')
energy_20_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_20.png')
energy_19_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_19.png')
energy_18_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_18.png')
energy_17_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_17.png')
energy_16_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_16.png')
energy_15_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_15.png')
energy_14_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_14.png')
energy_13_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_13.png')
energy_12_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_12.png')
energy_11_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_11.png')
energy_10_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_10.png')
energy_9_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_9.png')
energy_8_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_8.png')
energy_7_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_7.png')
energy_6_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_6.png')
energy_5_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_5.png')
energy_4_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_4.png')
energy_3_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_3.png')
energy_2_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_2.png')
energy_1_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_1.png')
energy_0_url = resource_path('resources/art/ui_elements/bars/energy/en_bar_0.png')

xp_100_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_100.png')
xp_99_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_99.png')
xp_98_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_98.png')
xp_97_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_97.png')
xp_96_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_96.png')
xp_95_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_95.png')
xp_94_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_94.png')
xp_93_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_93.png')
xp_92_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_92.png')
xp_91_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_91.png')
xp_90_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_90.png')
xp_89_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_89.png')
xp_88_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_88.png')
xp_87_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_87.png')
xp_86_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_86.png')
xp_85_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_85.png')
xp_84_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_84.png')
xp_83_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_83.png')
xp_82_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_82.png')
xp_81_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_81.png')
xp_80_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_80.png')
xp_79_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_79.png')
xp_78_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_78.png')
xp_77_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_77.png')
xp_76_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_76.png')
xp_75_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_75.png')
xp_74_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_74.png')
xp_73_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_73.png')
xp_72_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_72.png')
xp_71_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_71.png')
xp_70_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_70.png')
xp_69_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_69.png')
xp_68_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_68.png')
xp_67_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_67.png')
xp_66_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_66.png')
xp_65_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_65.png')
xp_64_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_64.png')
xp_63_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_63.png')
xp_62_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_62.png')
xp_61_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_61.png')
xp_60_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_60.png')
xp_59_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_59.png')
xp_58_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_58.png')
xp_57_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_57.png')
xp_56_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_56.png')
xp_55_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_55.png')
xp_54_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_54.png')
xp_53_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_53.png')
xp_52_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_52.png')
xp_51_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_51.png')
xp_50_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_50.png')
xp_49_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_49.png')
xp_48_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_48.png')
xp_47_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_47.png')
xp_46_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_46.png')
xp_45_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_45.png')
xp_44_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_44.png')
xp_43_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_43.png')
xp_42_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_42.png')
xp_41_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_41.png')
xp_40_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_40.png')
xp_39_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_39.png')
xp_38_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_38.png')
xp_37_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_37.png')
xp_36_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_36.png')
xp_35_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_35.png')
xp_34_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_34.png')
xp_33_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_33.png')
xp_32_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_32.png')
xp_31_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_31.png')
xp_30_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_30.png')
xp_29_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_29.png')
xp_28_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_28.png')
xp_27_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_27.png')
xp_26_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_26.png')
xp_25_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_25.png')
xp_24_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_24.png')
xp_23_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_23.png')
xp_22_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_22.png')
xp_21_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_21.png')
xp_20_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_20.png')
xp_19_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_19.png')
xp_18_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_18.png')
xp_17_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_17.png')
xp_16_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_16.png')
xp_15_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_15.png')
xp_14_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_14.png')
xp_13_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_13.png')
xp_12_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_12.png')
xp_11_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_11.png')
xp_10_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_10.png')
xp_9_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_9.png')
xp_8_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_8.png')
xp_7_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_7.png')
xp_6_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_6.png')
xp_5_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_5.png')
xp_4_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_4.png')
xp_3_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_3.png')
xp_2_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_2.png')
xp_1_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_1.png')
xp_0_url = resource_path('resources/art/ui_elements/bars/xp/xp_bar_0.png')

cat_url = resource_path('resources/art/critter_art/cat.png')

quest_logs_url = resource_path('resources/art/quest_items/logs.png')

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# initialize game, set clock for framerate, set screen size ------------------------------------------------------------
pygame.init()
clock = pygame.time.Clock()
width = 1024
height = 768
screen = pygame.display.set_mode((width, height))

# background textures --------------------------------------------------------------------------------------------------
seldon_district_bg = pygame.image.load(seldon_bg_url)
seldon_district_battle = pygame.image.load(seldon_battle_url)
seldon_district_shop = pygame.image.load(seldon_shop_screen_url)
seldon_district_inn = pygame.image.load(seldon_inn_screen_url)

game_over_screen = pygame.image.load(game_over_screen_url)
nera_sleep_screen = pygame.image.load(nera_sleep_screen_url)

# creating objects from defined classes --------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# display notifications to user (shown, x_coordinate, y_coordinate, image, color) --------------------------------------
greeting = Notification("greeting", False, 512, 384, welcome_image_url, (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# inventory items ------------------------------------------------------------------------------------------------------
health_potion = Item("health potion", "potion", 200, 200, health_pot_url, (255, 255, 255))
energy_potion = Item("energy potion", "potion", 200, 200, energy_pot_url, (255, 255, 255))
shiny_rock = Item("shiny rock", "rock", 200, 200, shiny_rock_url, (255, 255, 255))
bone_dust = Item("bone dust", "dust", 200, 200, bone_dust_url, (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# default player character ---------------------------------------------------------------------------------------------
player = Player("Stan", "male", "amuna", "mage",  # name, gender, race, role
                [health_potion, energy_potion],  # inventory
                ["magic", "basic staff", "medium", "green robes"],  # equipment ('type', 'name')
                # current quest, quest status (x/4), quest dictionary (quest: done)
                [""], 0, {"Sneaky Snakes": False, "Village Repairs": False, "Ghoulish Ghosts": False},
                ["vitality", 1, "intellect", 3, "strength", 1, "wisdom", 2],  # stats ('stat', 'amount')
                ["barrier"], 1, 5, 100, 100,  # skills, lvl, exp, health, energy
                True, 20, ["amuna", 10, "nuldar", 0, "sorae", 0], "", "")  # alive, rupees, reputation, mount, zone

# nps: name, gender, race, role, dialog, quest, quest_description, x_coordinate, y_coordinate --------------------------
#                  alive_status, quest_complete, items, gift, image, color
npc_garan = NPC("Garan", "male", "amuna", "rogue", "It's dangerous to go alone.", "Stupid Snakes",
                "Greetings! I don't believe I've seen you around here before. You must be a traveler, \nright? "
                "Or maybe the request for reinforcements has finally been answered! Well, either way, we're\n"
                "thankful for all the help we can get. \n\nLook, you seem pretty strong, but you're going to need "
                "a weapon to survive out here. \n\nI've got something you can have for now, but you'll need to find "
                "something better if you plan on \njourneying further into the Region. Here's a basic weapon and "
                "some gear. \n\nWhy don't you go and test it out? There's some snakes nearby that have been coming up "
                "from the \nriver. They've shown an unusual aggressiveness with larger numbers than I've seen "
                "before. \n\nMaybe you could take care of them for me? I'll be sure to give you something worth the "
                "trouble. ", 240, 480, True, False, ["Items to be added for steal"], False,
                garan_url, (255, 255, 255))

npc_maurelle = NPC("Maurelle", "female", "amuna", "mage", "We need help!", "Village Repairs",
                   "You there! I don't know who you are, or why you're here, but we could \nreally use your help!"
                   "\n\nThe beast Dreth has occupied our former capital Castle, on the other side of the walls "
                   "\nto the east, and our numbers have been spread thin trying to repel its minions and contain "
                   "the \ndamage they've inflicted. \n\nOur best fighters have been sent in a combined Vanguard with "
                   "the other districts to try and \nattack the beast directly, but its left us vulnerable here. "
                   "The most recent wave of attacks from\nthe castle has left several damages to our village, "
                   "and if you are able, please gather\nresources and bring them to me to distribute to the "
                   "villagers conducting the repairs and \nfortifications. \n\nYou can gather some lumber from the "
                   "trees just west of here. Nera bless you. ", 755, 515, True, False,
                   ["Items to be added for steal"], False,
                   maurelle_url, (255, 255, 255))

npc_guard = NPC("Guard", "male", "amuna", "fighter", "Another day.", "Ghoulish Glee",
                "You need to cross the bridge to get to the Korlok District, you say? \n\nOrdinarily"
                " I would have no issue granting you passage, however the gates are barred tight \n"
                "due to the recent wave of Ghoul Minions from across the wall. \n\nI cannot leave my post and"
                " leave the bridge unguarded, but if you could \ntake care of the remaining ghouls I"
                " will signal to unbar the gates and allow you passage \nto the other side. \n\nThe"
                " ghouls were last spotted just east of here, nearby the northern Castle wall ramparts! ", 475, 140,
                True,
                False, ["Items to be added for steal"], False,
                guard_url, (255, 255, 255))

npc_amuna_shopkeeper = NPC("Amuna Shopkeeper", "male", "amuna", "trader", "These ghoul attacks are bad for business!",
                           "", "", 700, 700, True, False, [
                               Item("health potion", "potion", 200, 200, health_pot_url,
                                    (255, 255, 255)),
                               Item("energy potion", "potion", 200, 200, energy_pot_url,
                                    (255, 255, 255)),
                               Item("bronze sword", "2H", 200, 200, temp_item_url,
                                    (255, 255, 255)),
                               Item("bronze armor", "heavy", 200, 200, temp_item_url,
                                    (255, 255, 255))
                           ], False, amuna_shopkeeper_url, (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# enemies: kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image, color, health bar ------
snake_1 = Enemy("Snake", "snake", 100, 100, 1, 100, 150, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_url, (255, 255, 255)),
                snake_url, (255, 255, 255),
                UiElement("snake hp bar", 700, 90, health_100_url, (255, 255, 255), False))
snake_2 = Enemy("Snake", "snake", 100, 100, 2, 260, 170, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_url, (255, 255, 255)),
                snake_url, (255, 255, 255),
                UiElement("snake hp bar", 700, 90, health_100_url, (255, 255, 255), False))
snake_3 = Enemy("Snake", "snake", 100, 100, 1, 100, 250, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_url, (255, 255, 255)),
                snake_url, (255, 255, 255),
                UiElement("snake hp bar", 700, 90, health_100_url, (255, 255, 255), False))
snake_4 = Enemy("Snake", "snake", 100, 100, 2, 260, 270, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_url, (255, 255, 255)),
                snake_url, (255, 255, 255),
                UiElement("snake hp bar", 700, 90, health_100_url, (255, 255, 255), False))

ghoul_low_1 = Enemy("Ghoul", "ghoul", 100, 100, 4, 675, 200, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_url, (255, 255, 255)),
                    ghoul_url, (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, health_100_url, (255, 255, 255), False))
ghoul_low_2 = Enemy("Ghoul", "ghoul", 100, 100, 5, 800, 150, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_url, (255, 255, 255)),
                    ghoul_url, (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, health_100_url, (255, 255, 255), False))
ghoul_low_3 = Enemy("Ghoul", "ghoul", 100, 100, 3, 760, 260, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_url, (255, 255, 255)),
                    ghoul_url, (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, health_100_url, (255, 255, 255), False))
ghoul_low_4 = Enemy("Ghoul", "ghoul", 100, 100, 4, 875, 225, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_url, (255, 255, 255)),
                    ghoul_url, (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, health_100_url, (255, 255, 255), False))

# environmental objects: name, model, x_coordinate, y_coordinate, gathered, image, color -------------------------------
pine_tree_1 = Tree("pine tree 1", "pine tree", 80, 475, False, pine_tree_url, (255, 255, 255))
pine_tree_2 = Tree("pine tree 4", "pine tree", 260, 660, False, pine_tree_url, (255, 255, 255))
pine_tree_3 = Tree("pine tree 5", "pine tree", 380, 400, False, pine_tree_url, (255, 255, 255))

seldon_grass_1 = Item("seldon grass", "grass", 380, 145, seldon_grass_url, (255, 255, 255))
seldon_grass_2 = Item("seldon grass", "grass", 290, 215, seldon_grass_url, (255, 255, 255))
seldon_grass_3 = Item("seldon grass", "grass", 425, 255, seldon_grass_url, (255, 255, 255))
seldon_grass_4 = Item("seldon grass", "grass", 175, 155, seldon_grass_url, (255, 255, 255))
seldon_grass_5 = Item("seldon grass", "grass", 160, 275, seldon_grass_url, (255, 255, 255))
seldon_grass_6 = Item("seldon grass", "grass", 50, 200, seldon_grass_url, (255, 255, 255))

seldon_flower_1 = Item("seldon flower", "flower", 580, 410, seldon_flower_url, (255, 255, 255))
seldon_flower_2 = Item("seldon flower", "flower", 700, 620, seldon_flower_url, (255, 255, 255))
seldon_flower_3 = Item("seldon flower", "flower", 800, 470, seldon_flower_url, (255, 255, 255))

# buildings: name, model, x_coordinate, y_coordinate, image, color -----------------------------------------------------
amuna_inn = Building("amuna inn", "inn", 625, 620, seldon_inn_url, (255, 255, 255))
amuna_shop = Building("amuna shop", "shop", 660, 400, seldon_shop_url, (255, 255, 255))
amuna_academia = Building("amuna academia", "academia", 875, 500, seldon_academia_url, (255, 255, 255))

# ui elements: name, x_coordinate, y_coordinate, image, color, update flag ---------------------------------------------
inventory_button = UiElement("inventory button", 960, 730, inventory_button_url, (255, 255, 255), False)
character_button = UiElement("character button", 850, 730, character_button_url, (255, 255, 255), False)
journal_button = UiElement("journal button", 740, 730, journal_button_url, (255, 255, 255), False)

attack_button = UiElement("attack button", 740, 670, attack_button_url, (255, 255, 255), False)
skill_button = UiElement("skill button", 850, 670, skill_button_url, (255, 255, 255), False)
run_button = UiElement("run button", 960, 670, run_button_url, (255, 255, 255), False)
continue_button = UiElement("continue button", 500, 600, continue_button_url, (255, 255, 255), False)
buy_button = UiElement("buy button", 740, 730, buy_button_url, (255, 255, 255), False)
sell_button = UiElement("sell button", 850, 730, sell_button_url, (255, 255, 255), False)
leave_button = UiElement("leave button", 960, 730, leave_button_url, (255, 255, 255), False)
rest_button = UiElement("rest button", 740, 730, rest_button_url, (255, 255, 255), False)
screen_button = UiElement("screen size button", 960, 25, screen_size_button_url, (255, 255, 255), False)
screen_resize_window = UiElement("screen resize window", 940, 113, screen_size_window_url, (255, 255, 255), False)

s_1200x900_button = UiElement("1200x900", 940, 85, s_1200x900_url, (255, 255, 255), False)
s_1024x768_button = UiElement("1024x768", 940, 110, s_1024x768_url, (255, 255, 255), False)
s_800x600_button = UiElement("800x600", 940, 135, s_800x600_url, (255, 255, 255), False)

player_status = UiElement("player status", 850, 670, player_status_url, (255, 255, 255), False)
enemy_status = UiElement("enemy status", 850, 730, enemy_status_url, (255, 255, 255), False)

hp_bar = UiElement("hp bar", 170, 25, health_100_url, (255, 255, 255), False)
en_bar = UiElement("en bar", 170, 45, energy_100_url, (255, 255, 255), False)
xp_bar = UiElement("xp bar", 170, 65, xp_100_url, (255, 255, 255), False)

inventory = Inventory([], 890, 515, inventory_url, (255, 255, 255), False)

quest_logs_1 = Item("pine logs", "quest", 65, 575, quest_logs_url, (255, 255, 255))
quest_logs_2 = Item("pine logs", "quest", 315, 615, quest_logs_url, (255, 255, 255))
quest_logs_3 = Item("pine logs", "quest", 432, 462, quest_logs_url, (255, 255, 255))
quest_logs_4 = Item("pine logs", "quest", 105, 575, quest_logs_url, (255, 255, 255))

# shop windows ---------------------------------------------------------------------------------------------------------
buy_inventory = Inventory([], 890, 490, buy_inventory_url, (255, 255, 255), False)
sell_inventory = Inventory([], 890, 490, sell_inventory_url, (255, 255, 255), False)
# ----------------------------------------------------------------------------------------------------------------------

message_box = UiElement("message box", 175, 700, message_box_url, (255, 255, 255), False)
status_bar_backdrop = UiElement("status bar backdrop", 165, 45, bar_backdrop_url, (255, 255, 255), False)
enemy_status_bar_backdrop = UiElement("enemy status bar backdrop", 695, 90, enemy_bar_backdrop_url, (255, 255, 255),
                                      False)

# ----------------------------------------------------------------------------------------------------------------------
# battle sprites -------------------------------------------------------------------------------------------------------
stan_battle_sprite = BattleCharacter("stan battle", 300, 460, stan_battle_url, (255, 255, 255))
snake_battle_sprite = BattleCharacter("snake battle", 700, 250, snake_battle_url, (255, 255, 255))
ghoul_battle_sprite = BattleCharacter("ghoul battle", 700, 250, ghoul_battle_url, (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# setting font and size for text to screen updates ---------------------------------------------------------------------
font = pygame.font.SysFont('freesansbold.ttf', 16, bold=True, italic=False)

# ----------------------------------------------------------------------------------------------------------------------
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
screen_resize_buttons = pygame.sprite.Group()
battle_elements = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
total_elements = pygame.sprite.Group()

# specific enemy groups for movement and respawn -----------------------------------------------------------------------
snakes = pygame.sprite.Group()
snakes.add(snake_1, snake_2, snake_3, snake_4)

ghouls = pygame.sprite.Group()
ghouls.add(ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)

# adding sprite objects to groups --------------------------------------------------------------------------------------
npcs.add(npc_garan, npc_maurelle, npc_guard)
enemies.add(snake_1, snake_2, snake_3, snake_4, ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)
trees.add(pine_tree_1, pine_tree_2, pine_tree_3)
grass.add(seldon_grass_1, seldon_grass_2, seldon_grass_3, seldon_grass_4, seldon_grass_5, seldon_grass_6)
flowers.add(seldon_flower_1, seldon_flower_2, seldon_flower_3)
buildings.add(amuna_inn, amuna_shop, amuna_academia)
screen_resize_buttons.add(s_1200x900_button, s_1024x768_button, s_800x600_button)

user_interface.add(rest_button, buy_button, sell_button, leave_button, character_button, journal_button,
                   inventory_button, screen_button, attack_button, skill_button, run_button, player_status, message_box,
                   status_bar_backdrop)

conditional_interface.add(inventory, buy_inventory, sell_inventory, screen_resize_window)

# all environment sprites for collision detection ----------------------------------------------------------------------
environment_objects.add(trees, buildings)

# quest item sprites for gathering -------------------------------------------------------------------------------------
quest_items.add(quest_logs_1, quest_logs_2, quest_logs_3, quest_logs_4)

# battle element sprites for combat scenario ---------------------------------------------------------------------------
battle_elements.add(stan_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, enemy_status_bar_backdrop)

# adding all sprites to game screen
all_sprites.add(npcs, enemies, trees, buildings, grass, flowers, quest_items)

total_elements.add(npcs, enemies, trees, buildings, grass, flowers, quest_items, battle_elements, environment_objects,
                   conditional_interface, user_interface, screen_resize_buttons)

# pygame.mixer.music.load("Electric_1.mp3")
# pygame.mixer.music.play(loops=-1)

# move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
# move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
# collision_sound = pygame.mixer.Sound("Collision.ogg")

# Set the base volume for all sounds
# move_up_sound.set_volume(0.5)
# move_down_sound.set_volume(0.5)
# collision_sound.set_volume(0.5)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# main loop variables --------------------------------------------------------------------------------------------------
game_running = True

# condition to check if player has chosen to interact with sprite
interacted = False
# condition to allow or block player movement (combat or npc interaction)
movement_able = True
# condition for battle sequences so that buttons can't be spam clicked
combat_cooldown = False
# condition to check if combat occurred on current game loop iteration to update sprites at end of loop
combat_happened = False
# condition to check if inventory button is clicked
inventory_clicked = False
# condition to check if buy button is clicked in shop
buy_clicked = False
# condition to check if sell button is clicked in shop
sell_clicked = False
# condition to check if rest button is clicked in inn
rest_clicked = False
# condition to check if screen resize button has been clicked
screen_clicked = False
# condition to check if enemy has just been defeated so that the message box doesn't instantly clear and shows updates
loot_update = False
# condition to check if player has started combat encounter with enemy to clear message box (before adding combat text)
encounter_started = False
# condition to check if player is in a shop building
in_shop = False
# condition to check if player is in an inn building
in_inn = False
# condition to check if player has bought an item from shop
item_bought = False
# condition to check if player has sold an item to shop
item_sold = False
# condition to check if player has rested in an inn
rest = False
# conditions to check current screen size scaling
scaled_800 = False
scaled_1024 = True
scaled_1200 = False

# what zone the player is in, used for player update and map boundaries
zone_seldon = True
zone_korlok = False
zone_eldream = False
zone_marrow = False

# list to contain clicked UI elements for display
display_elements = []
# list to contain current player items for display
player_items = []
# separate list based on same player inventory but used to populate sell window in shop
sell_player_items = []
# list to contain buy inventory window for display within shop
buy_shop_elements = []
# list to contain sell inventory window for display within shop
sell_shop_elements = []
# list to contain current shop items for display
shopkeeper_items = []
# list to contain screen size elements for display
screen_size_elements = []

# combat text strings to be updated on scenario, shown on UI message box
# initially set to these default strings but will be overwritten
info_text_1 = ""
info_text_2 = ""
info_text_3 = ""
info_text_4 = ""

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# main loop ------------------------------------------------------------------------------------------------------------
while game_running:

    # screen scaling ---------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    scale_w, scale_h = pygame.display.get_surface().get_size()

    # while player is alive --------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    if player.alive_status:

        # clear loot update after some time has passed (ab 3 seconds)
        # seems to be inconsistent currently
        if pygame.time.get_ticks() % 183 == 0:
            loot_update = False

        # if player is not currently in range of sprite, or using inventory, or recently defeated enemy for loot update,
        # clear message box
        sprite = pygame.sprite.spritecollideany(player, all_sprites)
        if not sprite:
            if not inventory_clicked:
                if not loot_update:
                    info_text_1 = ""
                    info_text_2 = ""
                    info_text_3 = ""
                    info_text_4 = ""

        if zone_seldon:
            player.current_zone = "Seldon"
        if zone_korlok:
            player.current_zone = "Korlok"
        if zone_eldream:
            player.current_zone = "Eldream"
        if zone_marrow:
            player.current_zone = "Marrow"

        # switches between 1 and 0 to select a left or right direction for enemy sprite to move
        enemy_switch = 1

        # gets defeated enemy count and will respawn a new enemy type if count is greater than specified
        # new enemy is added to sprite groups and will be random level and location in boundaries of type
        enemy_respawn()

        # used for backdrop to enemies health bar, so it's easier to see. will be updated in enemy encounter below
        screen.blit(enemy_status_bar_backdrop.surf, enemy_status_bar_backdrop.rect)

        # draw screen 1 background
        screen.blit(seldon_district_bg, (0, 0))

        # draw sprites -------------------------------------------------------------------------------------------------
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # draw player --------------------------------------------------------------------------------------------------
        screen.blit(player.surf, player.rect)

        # draw user interface elements ---------------------------------------------------------------------------------
        for ui_element in user_interface:
            screen.blit(ui_element.surf, ui_element.rect)

        # get ui windows from clicked display elements and draw
        for window in display_elements:
            screen.blit(window.surf, window.rect)

        # get item from current items based on players inventory and draw with inventory window
        for item in player_items:
            screen.blit(item.surf, item.rect)

        # get screen option elements and draw window
        for size_window in screen_size_elements:
            screen.blit(size_window.surf, size_window.rect)

        # if screen resize option button has been clicked, draw buttons for options with size window
        if screen_clicked:
            for size_button in screen_resize_buttons:
                screen.blit(size_button.surf, size_button.rect)

        # for shop encounter -------------------------------------------------------------------------------------------
        # get ui windows from clicked buy or sell buttons and draw here at the beginning of iteration
        # so that rest of the code can use its information. drawn again at end of iteration to ensure viewable
        if in_shop:
            for window in buy_shop_elements:
                screen.blit(window.surf, window.rect)
            for window in sell_shop_elements:
                screen.blit(window.surf, window.rect)

            # get item from current items based on shopkeeper's inventory and draw with buy window
            for shop_item in shopkeeper_items:
                screen.blit(shop_item.surf, shop_item.rect)

            # get item from current items based on player's inventory and draw with sell window
            for sell_item in sell_player_items:
                screen.blit(sell_item.surf, sell_item.rect)

        # update players status bars -----------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        health_bar_update(player)
        energy_bar_update(player)
        xp_bar_update(player)

        screen.blit(hp_bar.surf, hp_bar.rect)
        screen.blit(en_bar.surf, en_bar.rect)
        screen.blit(xp_bar.surf, xp_bar.rect)

        # text updates to screen for things like current zone, rupee count, combat text, etc. --------------------------
        # --------------------------------------------------------------------------------------------------------------
        # get current player rupee count and create surf and rectangle to blit to screen
        text_rupee_surf = font.render(str(player.rupees), True, "black", "light yellow")
        text_rupee_rect = text_rupee_surf.get_rect()
        if scaled_800:
            text_rupee_rect.center = (975 * .78, 672 * .78)
            screen.blit(text_rupee_surf, text_rupee_rect)
        else:
            text_rupee_rect.center = (975, 672)
            screen.blit(text_rupee_surf, text_rupee_rect)

        # get current player district and create surf and rectangle to blit to screen
        text_zone_surf = font.render(str(player.current_zone), True, "black", "light yellow")
        text_zone_rect = text_zone_surf.get_rect()
        if scaled_800:
            text_zone_rect.center = (865 * .78, 672 * .78)
            screen.blit(text_zone_surf, text_zone_rect)
        else:
            text_zone_rect.center = (865, 672)
            screen.blit(text_zone_surf, text_zone_rect)

        # get current player district and create surf and rectangle to blit to screen
        text_level_surf = font.render(str(player.level), True, "black", "light yellow")
        text_level_rect = text_level_surf.get_rect()
        if scaled_800:
            text_level_rect.center = (760 * .78, 672 * .78)
            screen.blit(text_level_surf, text_level_rect)
        else:
            text_level_rect.center = (760, 672)
            screen.blit(text_level_surf, text_level_rect)

        # current info text for message box in lower left corner of screen, first line
        text_info_surf_1 = font.render(info_text_1, True, "black", "light yellow")
        text_combat_info_rect_1 = text_info_surf_1.get_rect()
        if scaled_800:
            text_combat_info_rect_1.midleft = (30 * .78, 680 * .78)
            screen.blit(text_info_surf_1, text_combat_info_rect_1)
        else:
            text_combat_info_rect_1.midleft = (30, 680)
            screen.blit(text_info_surf_1, text_combat_info_rect_1)

        # current info text for message box in lower left corner of screen, second line
        text_info_surf_2 = font.render(info_text_2, True, "black", "light yellow")
        text_combat_info_rect_2 = text_info_surf_2.get_rect()
        if scaled_800:
            text_combat_info_rect_2.midleft = (30 * .78, 700 * .78)
            screen.blit(text_info_surf_2, text_combat_info_rect_2)
        else:
            text_combat_info_rect_2.midleft = (30, 700)
            screen.blit(text_info_surf_2, text_combat_info_rect_2)

        # current info text for message box in lower left corner of screen, third line
        text_info_surf_3 = font.render(info_text_3, True, "black", "light yellow")
        text_combat_info_rect_3 = text_info_surf_3.get_rect()
        if scaled_800:
            text_combat_info_rect_3.midleft = (30 * .78, 720 * .78)
            screen.blit(text_info_surf_3, text_combat_info_rect_3)
        else:
            text_combat_info_rect_3.midleft = (30, 720)
            screen.blit(text_info_surf_3, text_combat_info_rect_3)

        # current info text for message box in lower left corner of screen, fourth line
        text_info_surf_4 = font.render(info_text_4, True, "black", "light yellow")
        text_combat_info_rect_4 = text_info_surf_4.get_rect()
        if scaled_800:
            text_combat_info_rect_4.midleft = (30 * .78, 740 * .78)
            screen.blit(text_info_surf_4, text_combat_info_rect_4)
        else:
            text_combat_info_rect_4.midleft = (30, 740)
            screen.blit(text_info_surf_4, text_combat_info_rect_4)

        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # all user input events such as key presses or UI interaction
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                # escape key was pressed, exit game
                if event.key == K_ESCAPE:
                    exit()

                # "F" key for player interaction
                if event.key == K_f:
                    interacted = True

                if event.type == VIDEORESIZE:
                    screen = pygame.display.set_mode((event.width, event.height), pygame.RESIZABLE)

            # if something was clicked on screen by mouse cursor, get its position and see what sprite it collided with
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # if screen resize button is clicked and if one of the option buttons for sizes is clicked
                # set the current screen resolution to that size
                if screen_clicked:
                    if s_800x600_button.rect.collidepoint(pos):
                        width = 800
                        height = 600
                        screen = pygame.display.set_mode((width, height))

                    if s_1024x768_button.rect.collidepoint(pos):
                        width = 1024
                        height = 768
                        screen = pygame.display.set_mode((width, height))

                    if s_1200x900_button.rect.collidepoint(pos):
                        width = 1200
                        height = 900
                        screen = pygame.display.set_mode((width, height))

                # if mouse cursor collided with screen resize button when player clicked -------------------------------
                if screen_button.rect.collidepoint(pos):

                    if screen_clicked:
                        screen_clicked = False

                        if len(screen_size_elements) > 0:
                            screen_size_elements.pop(0)

                    # user clicked inventory button for the first time. show inventory window
                    else:
                        screen_clicked = True
                        screen_size_elements.insert(0, screen_resize_window)

                # ------------------------------------------------------------------------------------------------------
                # if mouse cursor collided with inventory button when player clicked -----------------------------------
                if inventory_button.rect.collidepoint(pos):

                    # don't show regular inventory window while combat or shop encounter is happening
                    if not encounter_started:

                        # if user clicks inventory button again, set condition to false which will hide inventory window
                        if inventory_clicked:
                            inventory_clicked = False

                            # remove inventory window from display and clear temporary list used to populate it
                            # temporary list was used because items need to be cleared for iteration when inventory
                            # window is removed from screen (can't just remove players actual items from their inv.)
                            # so that the items don't continue to draw on screen after inventory window has been closed.
                            if len(display_elements) > 0:
                                display_elements.pop(0)
                                player_items.clear()

                        # user clicked inventory button for the first time. show inventory window
                        else:
                            inventory_clicked = True
                            display_elements.insert(0, inventory)

                            # if player has items in their inventory
                            if len(player.items) > 0:
                                first_coord = 800
                                second_coord = 425

                                if scaled_800:
                                    first_coord = first_coord * .78
                                    second_coord = second_coord * .78

                                inventory_counter = 0
                                # go through player items and assign inventory slots (coordinates) to them
                                for item in player.items:
                                    if item.name == "health potion":
                                        item.update(first_coord, second_coord, health_pot_url)
                                        player_items.append(item)
                                        inventory_counter += 1
                                    if item.name == "energy potion":
                                        item.update(first_coord, second_coord, energy_pot_url)
                                        player_items.append(item)
                                        inventory_counter += 1
                                    if item.name == "shiny rock":
                                        item.update(first_coord, second_coord, shiny_rock_url)
                                        player_items.append(item)
                                        inventory_counter += 1
                                    if item.name == "bone dust":
                                        item.update(first_coord, second_coord, bone_dust_url)
                                        player_items.append(item)
                                        inventory_counter += 1

                                    # add 75 to the items x-coordinate value so the next item will be added to next slot
                                    first_coord += 60
                                    if scaled_800:
                                        first_coord = first_coord - 13.2

                                    # add 60 to items y coordinate value if the first row of (4) slots has been filled
                                    # reset first coordinate and counter to start in the leftmost slot again
                                    if inventory_counter > 3:
                                        second_coord += 60
                                        first_coord = 800
                                        inventory_counter = 0

                                        if scaled_800:
                                            first_coord = first_coord * .78
                                            second_coord = second_coord * .78

            elif event.type == QUIT:
                exit()

            # ----------------------------------------------------------------------------------------------------------
            # if item has been clicked and inventory window is open, get item within inventory window that was
            # clicked and use the item based on its name attribute. health potion heals, energy potion energizes, etc
            if inventory_clicked:
                # make sure that click to use items is separate from click to buy or sell by checking if in shop
                if not in_shop:

                    inventory_item = inventory_event_item(event)

                    try:
                        if inventory_item.__getattribute__("name") == "health potion":
                            if player.health == 100:
                                info_text_1 = "You're already at full health."
                                info_text_2 = ""

                            else:
                                player.health = player.health + 40
                                # if health potion heals over 100 hp, just set to 100 (max health)
                                if player.health > 100:
                                    player.health = 100
                                info_text_1 = "The potion heals you for 40 hp."
                                info_text_2 = ""

                                player_items.remove(inventory_item)
                                player.items.remove(inventory_item)

                        if inventory_item.__getattribute__("name") == "energy potion":
                            if player.energy == 100:
                                info_text_1 = "You're already at full energy."
                                info_text_2 = ""
                                energy_bar_update(player)

                            else:
                                player.energy = player.energy + 40
                                # if energy potion energizes over 100 hp, just set to 100 (max energy)
                                if player.energy > 100:
                                    player.energy = 100
                                info_text_1 = "The potion energizes you for 40 en."
                                player_items.remove(inventory_item)
                                player.items.remove(inventory_item)

                        if inventory_item.__getattribute__("name") == "shiny rock":
                            info_text_1 = "Oh, shiny. Maybe you can sell it?"
                            info_text_2 = ""

                        if inventory_item.__getattribute__("name") == "bone dust":
                            info_text_1 = "Eh, dusty. Maybe you can sell it?"
                            info_text_2 = ""

                    except AttributeError:
                        pass

            # ----------------------------------------------------------------------------------------------------------
            # if player collides with enemy sprite, doesn't have combat cooldown,
            # and chooses to interact with it then get event from button press and start combat encounter
            enemy = pygame.sprite.spritecollideany(player, enemies)
            if enemy:

                # update enemy health bar on each iteration
                health_bar_update_enemy(enemy)

                if not combat_cooldown:
                    if interacted:

                        # if player has just started combat, clear message box, change condition to True
                        # so that it doesn't continuously clear box after combat text is added
                        if not encounter_started:
                            info_text_1 = ""
                            info_text_2 = ""
                            info_text_3 = ""
                            info_text_4 = ""
                            encounter_started = True

                        # get which button player pressed during combat scenario (attack, skill or run)
                        combat_button = combat_event_button(event)

                        # Info returned from combat scenario function in form of dictionary ----------------------------
                        # "damage done": 0,
                        # "damage taken": 0,
                        # "item dropped": "",
                        # "experience gained": 0,
                        # "quest update": "",
                        # "enemy defeated": False,
                        # "escaped": False
                        # "level up status": "",
                        # "level up attributes": ""
                        # ----------------------------------------------------------------------------------------------

                        # enter combat scenario and attack enemy. attack_scenario will return all info in form of list
                        if combat_button == "attack":

                            # update player character sprite for combat animation
                            stan_battle_sprite.update(stan_attack_url)

                            # update to attacking sprite surface for combat animation
                            if enemy.kind == "snake":
                                snake_battle_sprite.update(snake_attack_url)

                            if enemy.kind == "ghoul":
                                ghoul_battle_sprite.update(ghoul_attack_url)

                            # combat event function that handles and returns damage and health
                            combat_events = attack_scenario(enemy, "attack")
                            combat_happened = True

                            # add all combat scenario happenings from function to message box
                            # if any of the values are currently zero, or no, return blank string to message box
                            if combat_events["damage done"] == 0:
                                info_text_1 = ""
                            else:
                                info_text_1 = str(combat_events["damage done"])
                            if combat_events["damage taken"] == 0:
                                info_text_2 = ""
                            else:
                                info_text_2 = str(combat_events["damage taken"])

                            # adds item dropped and experienced gained messages to box if enemy was defeated
                            if combat_events["enemy defeated"]:
                                if combat_events["item dropped"] != "No":
                                    info_text_1 = str(combat_events["item dropped"])
                                if combat_events["experience gained"] != 0:
                                    info_text_2 = str(combat_events["experience gained"])

                            # if enemy was defeated and player leveled up, add messages related to box
                            if combat_events["enemy defeated"]:
                                if combat_events["level up status"] != "":
                                    info_text_3 = str(combat_events["level up status"])
                                    info_text_4 = str(combat_events["level up attributes"])

                            # if player was successful in defeating enemy, combat scenario ends, movement is allowed
                            # set combat happened false, allowing iterations to continue without cooldown
                            # reset encounter_started condition so that next enemy will clear message box
                            if combat_events["enemy defeated"]:
                                movement_able = True
                                combat_happened = False
                                interacted = False
                                loot_update = True
                                encounter_started = False

                        if combat_button == "skill":
                            combat_events = attack_scenario(enemy, "skill")

                        # if player chooses run in combat
                        if combat_button == "run":

                            combat_events = attack_scenario(enemy, "run")

                            # if combat scenario returns true that player is able to escape enemy, move player to
                            # safe location to exit the encounter and re-enable movement for player character
                            # set loot update to true to allow escape message to show for a short time
                            if combat_events["escaped"]:
                                info_text_1 = str(combat_events["damage done"])
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""

                                movement_able = True
                                interacted = False
                                loot_update = True
                                encounter_started = False
                                player.pos = vec((500, 400))

                            else:
                                info_text_1 = str(combat_events["damage done"])
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""

            # ----------------------------------------------------------------------------------------------------------
            # player collides with building, enters if chosen to interact and starts related scenario (shop, inn etc) --
            building = pygame.sprite.spritecollideany(player, buildings)
            if building:
                if interacted:
                    if building.__getattribute__("model") == "shop":

                        # so that subsequent code which allows clicking on the items knows they are for buying or sell.
                        in_shop = True

                        # if player left regular inventory window open when they entered shop, remove it from display
                        # and set its condition to false, so it doesn't have to be double-clicked to view after
                        if len(display_elements) > 0:
                            display_elements.pop(0)
                            player_items.clear()
                        inventory_clicked = False

                        # if player has just started shop scenario, clear message box
                        if not encounter_started:
                            info_text_1 = ""
                            info_text_2 = ""
                            info_text_3 = ""
                            info_text_4 = ""
                            encounter_started = True

                            # reset items bought condition on new shop encounter so that message is shown to player
                            # that they can click to buy or sell items. The condition makes it to where this doesn't
                            # keep showing after they've bought or sold an item (they know at that point).
                            item_bought = False
                            item_sold = False

                        # get which button player pressed during shop scenario (buy, sell or leave)
                        shop_button = shop_event_button(event)

                        if shop_button == "buy":
                            # don't allow buy and sell windows to display at the same time
                            if not sell_clicked:

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

                                # user clicked buy button for the first time. show buy window --------------------------
                                else:
                                    buy_clicked = True
                                    buy_shop_elements.insert(0, buy_inventory)

                                    # if shopkeeper has items in their inventory (they should but condition will verify)
                                    if len(npc_amuna_shopkeeper.items) > 0:
                                        buy_first_coord = 800
                                        buy_second_coord = 425

                                        if scaled_800:
                                            buy_first_coord = buy_first_coord * .78
                                            buy_second_coord = buy_second_coord * .78

                                        # ------------------------------------------------------------------------------
                                        buy_inventory_counter = 0
                                        # go through shop items and assign inventory slots (coordinates) to them
                                        for shop_item in npc_amuna_shopkeeper.items:
                                            if shop_item.name == "health potion":
                                                shop_item.update(buy_first_coord, buy_second_coord, health_pot_url)
                                                shopkeeper_items.append(shop_item)
                                                buy_inventory_counter += 1
                                            if shop_item.name == "energy potion":
                                                shop_item.update(buy_first_coord, buy_second_coord, energy_pot_url)
                                                shopkeeper_items.append(shop_item)
                                                buy_inventory_counter += 1

                                            # add 75 to the items x-coordinate value, next item will be added to next
                                            # slot
                                            buy_first_coord += 60
                                            if scaled_800:
                                                buy_first_coord = buy_first_coord - 13.2

                                            # add 60 to items y coordinate value if first row of (4) slots has been
                                            # filled reset first coordinate and counter to start in the leftmost
                                            # slot again
                                            if buy_inventory_counter > 3:
                                                buy_second_coord += 60
                                                buy_first_coord = 800
                                                buy_inventory_counter = 0

                                                if scaled_800:
                                                    buy_first_coord = buy_first_coord * .78
                                                    buy_second_coord = buy_second_coord * .78

                        # ----------------------------------------------------------------------------------------------
                        if shop_button == "sell":
                            # don't allow buy and sell windows to display at the same time
                            if not buy_clicked:

                                # if player hasn't sold an item yet, show message that item can be clicked to sell
                                if not item_sold:
                                    info_text_1 = "Click an item to sell."
                                    info_text_2 = ""
                                    info_text_3 = ""
                                    info_text_4 = ""

                                # if user clicks sell button again, set condition to false which will hide sell window
                                if sell_clicked:
                                    sell_clicked = False

                                    # remove sell window from display and clear temporary list used to populate it
                                    if len(sell_player_items) > 0:
                                        sell_shop_elements.pop(0)
                                        sell_player_items.clear()

                                # user clicked sell button for the first time. show sell window
                                else:
                                    sell_clicked = True
                                    sell_shop_elements.insert(0, sell_inventory)

                                    # if player has items in their inventory to be sold
                                    if len(player.items) > 0:
                                        sell_first_coord = 800
                                        sell_second_coord = 425

                                        if scaled_800:
                                            sell_first_coord = sell_first_coord * .78
                                            sell_second_coord = sell_second_coord * .78

                                        # ------------------------------------------------------------------------------
                                        sell_inventory_counter = 0
                                        # go through player items and assign inventory slots (coordinates) to them
                                        for sell_item in player.items:
                                            if sell_item.name == "health potion":
                                                sell_item.update(sell_first_coord, sell_second_coord, health_pot_url)
                                                sell_player_items.append(sell_item)
                                                sell_inventory_counter += 1
                                            if sell_item.name == "energy potion":
                                                sell_item.update(sell_first_coord, sell_second_coord, energy_pot_url)
                                                sell_player_items.append(sell_item)
                                                sell_inventory_counter += 1
                                            if sell_item.name == "shiny rock":
                                                sell_item.update(sell_first_coord, sell_second_coord, shiny_rock_url)
                                                sell_player_items.append(sell_item)
                                                sell_inventory_counter += 1
                                            if sell_item.name == "bone dust":
                                                sell_item.update(sell_first_coord, sell_second_coord, bone_dust_url)
                                                sell_player_items.append(sell_item)
                                                sell_inventory_counter += 1

                                            # add 75 to the items x-coordinate value, next item will be added to next
                                            # slot
                                            sell_first_coord += 60
                                            if scaled_800:
                                                sell_first_coord = sell_first_coord - 13.2

                                            # add 60 to items y coordinate value if first row of (4) slots has been
                                            # filled reset first coordinate and counter to start in the leftmost slot
                                            # again
                                            if sell_inventory_counter > 3:
                                                sell_second_coord += 60
                                                sell_first_coord = 800
                                                sell_inventory_counter = 0

                                                if scaled_800:
                                                    sell_first_coord = sell_first_coord * .78
                                                    sell_second_coord = sell_second_coord * .78

                        # ----------------------------------------------------------------------------------------------
                        # if player chooses to leave shop, set conditions to allow normal gameplay loop
                        if shop_button == "leave":

                            # clear out sell and buy windows if left open ----------------------------------------------
                            if len(sell_player_items) > 0:
                                sell_shop_elements.pop(0)
                                sell_player_items.clear()

                            if len(buy_shop_elements) > 0:
                                buy_shop_elements.pop(0)
                                shopkeeper_items.clear()
                            # ------------------------------------------------------------------------------------------
                            buy_clicked = False
                            sell_clicked = False
                            movement_able = True
                            interacted = False
                            loot_update = True
                            encounter_started = False
                            in_shop = False

                    # --------------------------------------------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    if building.__getattribute__("model") == "inn":

                        # so that subsequent code which allows clicking on the items knows they are for buying or sell.
                        in_inn = True

                        # if player left regular inventory window open when they entered shop, remove it from display
                        # and set its condition to false, so it doesn't have to be double-clicked to view after
                        if len(display_elements) > 0:
                            display_elements.pop(0)
                            player_items.clear()
                        inventory_clicked = False

                        # if player has just started inn scenario, clear message box
                        if not encounter_started:
                            info_text_1 = ""
                            info_text_2 = ""
                            info_text_3 = ""
                            info_text_4 = ""
                            encounter_started = True

                        # get which button player pressed during shop scenario (buy, sell or leave)
                        inn_button = inn_event_button(event)

                        if inn_button == "rest":
                            pygame.time.wait(2000)
                            rest = True

                        # ----------------------------------------------------------------------------------------------
                        # if player chooses to leave shop, set conditions to allow normal gameplay loop
                        if inn_button == "leave":
                            buy_clicked = False
                            sell_clicked = False
                            rest_clicked = False
                            movement_able = True
                            interacted = False
                            loot_update = True
                            encounter_started = False
                            in_inn = False
                            rest = False

            # shop item click handlers ---------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # handles clicks in buy window, shop encounter -------------------------------------------------------------
            # if item has been clicked and buy window is open, get item within buy window that was clicked
            if buy_clicked:
                if in_shop:
                    buy_item = buy_event_item(event)

                    try:
                        # player has clicked health potion. If player has enough rupees it will buy item
                        # and add to their inventory. Also subtracts the price of item from current rupee count
                        if buy_item.__getattribute__("name") == "health potion":

                            if len(player.items) < 16:
                                if player.rupees > 9:
                                    info_text_1 = "Bought Health Potion for 10 rupees."
                                    info_text_2 = "Health Potion added to inventory."
                                    player.items.append(
                                        Item("health potion", "potion", 200, 200, health_pot_url, (255, 255, 255)))
                                    player.rupees = player.rupees - 10
                                    item_bought = True

                                else:
                                    info_text_1 = "You do not have enough rupees."
                                    info_text_2 = "Health Potion cost 10 rupees."
                            else:
                                info_text_1 = "Your inventory is full."
                                info_text_2 = ""

                        if buy_item.__getattribute__("name") == "energy potion":

                            if len(player.items) < 16:
                                if player.rupees > 9:
                                    info_text_1 = "Bought Energy Potion for 10 rupees."
                                    info_text_2 = "Energy Potion added to inventory."
                                    player.items.append(
                                        Item("energy potion", "potion", 200, 200, energy_pot_url, (255, 255, 255)))
                                    player.rupees = player.rupees - 10
                                    item_bought = True

                                else:
                                    info_text_1 = "You do not have enough rupees."
                                    info_text_2 = "Energy Potion cost 10 rupees."
                            else:
                                info_text_1 = "Your inventory is full."
                                info_text_2 = ""

                    except AttributeError:
                        pass

            # handle clicks in sell window, shop encounter ------------------------------------------------------------
            # if item has been clicked and sell window is open, get item within sell window that was clicked
            if sell_clicked:
                if in_shop:
                    sell_item = sell_event_item(event)

                    try:
                        # player has clicked health potion. This will sell the item, removing it from player's
                        # inventory and giving them "x" rupees to add to their current count
                        if sell_item.__getattribute__("name") == "health potion":
                            info_text_1 = "Sold Health Potion for 5 rupees."
                            info_text_2 = "Health Potion removed from inventory."
                            player.items.remove(sell_item)
                            sell_player_items.remove(sell_item)
                            player.rupees = player.rupees + 5
                            item_sold = True

                        if sell_item.__getattribute__("name") == "energy potion":
                            info_text_1 = "Sold Energy Potion for 5 rupees."
                            info_text_2 = "Energy Potion removed from inventory."
                            player.items.remove(sell_item)
                            sell_player_items.remove(sell_item)
                            player.rupees = player.rupees + 5
                            item_sold = True

                        if sell_item.__getattribute__("name") == "shiny rock":
                            info_text_1 = "Sold Shiny Rock for 20 rupees."
                            info_text_2 = "Shiny Rock removed from inventory."
                            player.items.remove(sell_item)
                            sell_player_items.remove(sell_item)
                            player.rupees = player.rupees + 20
                            item_sold = True

                        if sell_item.__getattribute__("name") == "bone dust":
                            info_text_1 = "Sold Bone Dust for 20 rupees."
                            info_text_2 = "Bone Dust removed from inventory."
                            player.items.remove(sell_item)
                            sell_player_items.remove(sell_item)
                            player.rupees = player.rupees + 20
                            item_sold = True

                    except AttributeError:
                        pass

        # outside of event loop ----------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # get current pressed keys from player and apply zone boundaries depending on current players current zone
        pressed_keys = pygame.key.get_pressed()

        # Apply pressed keys update to movement based on zone boundaries, defined in player.update()
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

        # if greeting message has not been shown yet, add it to display elements to be drawn
        if not greeting.shown:
            display_elements.append(greeting)
            greeting.shown = True

        # if greeting has been shown, after a few seconds remove it from screen
        if greeting.shown:
            if pygame.time.get_ticks() > 3000:
                for notification in display_elements:
                    try:
                        if notification.__getattribute__("name") == "greeting":
                            display_elements.remove(notification)
                    except AttributeError:
                        pass

        # enemy movement updates ---------------------------------------------------------------------------------------
        # choose random directions and random enemy to move that direction ---------------------------------------------
        direction_horizontal = random.choice(["left", "right"])
        direction_vertical = random.choice(["up", "down"])

        move_this_snake = random.choice(snakes.sprites())
        move_this_ghoul = random.choice(ghouls.sprites())

        # move snakes in random direction within boundaries
        if movement_able:
            if pygame.time.get_ticks() % 20 == 0:
                move_this_snake.update([50, 300], [200, 300], direction_horizontal, direction_vertical)
                move_this_ghoul.update([650, 900], [200, 300], direction_horizontal, direction_vertical)

        # npc movement updates -----------------------------------------------------------------------------------------
        # choose random facing direction and random npc to move face that direction ------------------------------------
        face_direction = random.choice(["front", "back", "left", "right"])
        face_this_npc = random.choice(npcs.sprites())

        if pygame.time.get_ticks() % 180 == 0:

            if face_direction == "front":
                if face_this_npc.name == "Garan":
                    npc_garan.update(garan_url)
                if face_this_npc.name == "Maurelle":
                    npc_maurelle.update(maurelle_url)
                if face_this_npc.name == "Guard":
                    npc_guard.update(guard_url)

            if face_direction == "back":
                if face_this_npc.name == "Garan":
                    npc_garan.update(garan_back_url)
                if face_this_npc.name == "Maurelle":
                    npc_maurelle.update(maurelle_back_url)
                if face_this_npc.name == "Guard":
                    npc_guard.update(guard_back_url)

            if face_direction == "left":
                if face_this_npc.name == "Garan":
                    npc_garan.update(garan_left_url)
                if face_this_npc.name == "Maurelle":
                    npc_maurelle.update(maurelle_left_url)
                if face_this_npc.name == "Guard":
                    npc_guard.update(guard_left_url)

            if face_direction == "right":
                if face_this_npc.name == "Garan":
                    npc_garan.update(garan_right_url)
                if face_this_npc.name == "Maurelle":
                    npc_maurelle.update(maurelle_right_url)
                if face_this_npc.name == "Guard":
                    npc_guard.update(guard_right_url)

        # --------------------------------------------------------------------------------------------------------------
        # the code in this next section draws scenario related graphics on top of every other graphic
        # at the end of iteration to ensure it is on top and viewable by player (if they are in the encounter
        # where those graphics are needed, like combat and shop scenarios etc.) checks by verifying current collision
        # --------------------------------------------------------------------------------------------------------------
        # player rect collides with an enemy rect ----------------------------------------------------------------------
        enemy = pygame.sprite.spritecollideany(player, enemies)
        if enemy:
            # player has pressed "F" key to interact with enemy (attack)
            if interacted:
                # don't allow player to move while in combat
                movement_able = False

                if zone_seldon:
                    # --------------------------------------------------------------------------------------------------
                    # if enemy is snake in seldon zone, chose snake sprite and seldon backdrop
                    if enemy.__getattribute__("kind") == "snake":
                        screen.blit(seldon_district_battle, (0, 0))
                        screen.blit(stan_battle_sprite.surf, stan_battle_sprite.rect)
                        screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(attack_button.surf, attack_button.rect)
                        screen.blit(skill_button.surf, skill_button.rect)
                        screen.blit(run_button.surf, run_button.rect)
                        screen.blit(snake_battle_sprite.surf, snake_battle_sprite.rect)
                        screen.blit(enemy_status_bar_backdrop.surf, enemy_status_bar_backdrop.rect)
                        screen.blit(enemy.health_bar.surf, enemy.health_bar.rect)
                        screen.blit(enemy_status.surf, enemy_status.rect)
                        screen.blit(message_box.surf, message_box.rect)

                        # get current enemy name and create surf and rectangle to draw to screen
                        text_enemy_name_surf = font.render(str(enemy.__getattribute__("name")), True, "black",
                                                           "light yellow")
                        text_enemy_name_rect = text_enemy_name_surf.get_rect()
                        text_enemy_name_rect.center = (800, 732)
                        screen.blit(text_enemy_name_surf, text_enemy_name_rect)

                        # get current enemy level and create surf and rectangle to draw to screen
                        text_enemy_level_surf = font.render(str(enemy.__getattribute__("level")), True, "black",
                                                            "light yellow")
                        text_enemy_level_rect = text_enemy_level_surf.get_rect()
                        text_enemy_level_rect.center = (910, 732)
                        screen.blit(text_enemy_level_surf, text_enemy_level_rect)

                        # draw message box text to screen, updated during combat scenario
                        screen.blit(text_info_surf_1, text_combat_info_rect_1)
                        screen.blit(text_info_surf_2, text_combat_info_rect_2)
                        screen.blit(text_info_surf_3, text_combat_info_rect_3)
                        screen.blit(text_info_surf_4, text_combat_info_rect_4)

                    # --------------------------------------------------------------------------------------------------
                    if enemy.__getattribute__("kind") == "ghoul":
                        screen.blit(seldon_district_battle, (0, 0))
                        screen.blit(stan_battle_sprite.surf, stan_battle_sprite.rect)
                        screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(attack_button.surf, attack_button.rect)
                        screen.blit(skill_button.surf, skill_button.rect)
                        screen.blit(run_button.surf, run_button.rect)
                        screen.blit(ghoul_battle_sprite.surf, ghoul_battle_sprite.rect)
                        screen.blit(enemy_status_bar_backdrop.surf, enemy_status_bar_backdrop.rect)
                        screen.blit(enemy.health_bar.surf, enemy.health_bar.rect)
                        screen.blit(enemy_status.surf, enemy_status.rect)
                        screen.blit(message_box.surf, message_box.rect)

                        text_enemy_name_surf = font.render(str(enemy.__getattribute__("name")), True, "black",
                                                           "light yellow")
                        text_enemy_name_rect = text_enemy_name_surf.get_rect()
                        text_enemy_name_rect.center = (805, 732)
                        screen.blit(text_enemy_name_surf, text_enemy_name_rect)

                        text_enemy_level_surf = font.render(str(enemy.__getattribute__("level")), True, "black",
                                                            "light yellow")
                        text_enemy_level_rect = text_enemy_level_surf.get_rect()
                        text_enemy_level_rect.center = (910, 732)
                        screen.blit(text_enemy_level_surf, text_enemy_level_rect)

                        screen.blit(text_info_surf_1, text_combat_info_rect_1)
                        screen.blit(text_info_surf_2, text_combat_info_rect_2)
                        screen.blit(text_info_surf_3, text_combat_info_rect_3)
                        screen.blit(text_info_surf_4, text_combat_info_rect_4)

            else:
                # don't show if player has recently defeated enemy, so that it doesn't overwrite loot and xp info
                if not loot_update:
                    # lets player know if they are in range of enemy they can press f to attack it
                    info_text_1 = "Press 'F' key to attack enemy."

        # --------------------------------------------------------------------------------------------------------------
        # player rect collides with a building rect --------------------------------------------------------------------
        building = pygame.sprite.spritecollideany(player, buildings)
        if building:
            # player has pressed "F" key to interact with building (enter building)
            if interacted:
                # don't allow player to move while in building
                movement_able = False

                if zone_seldon:
                    # --------------------------------------------------------------------------------------------------
                    # if building is a shop in the seldon zone
                    if building.__getattribute__("name") == "amuna shop":
                        screen.blit(seldon_district_shop, (0, 0))
                        screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)

                        screen.blit(buy_button.surf, buy_button.rect)
                        screen.blit(sell_button.surf, sell_button.rect)
                        screen.blit(leave_button.surf, leave_button.rect)

                        screen.blit(player_status.surf, player_status.rect)
                        screen.blit(text_level_surf, text_level_rect)
                        screen.blit(text_zone_surf, text_zone_rect)
                        screen.blit(text_rupee_surf, text_rupee_rect)

                        screen.blit(message_box.surf, message_box.rect)
                        # draw message box text to screen, updated during scenario
                        screen.blit(text_info_surf_1, text_combat_info_rect_1)
                        screen.blit(text_info_surf_2, text_combat_info_rect_2)
                        screen.blit(text_info_surf_3, text_combat_info_rect_3)
                        screen.blit(text_info_surf_4, text_combat_info_rect_4)

                        # ----------------------------------------------------------------------------------------------
                        if buy_clicked:
                            for window in buy_shop_elements:
                                screen.blit(window.surf, window.rect)

                            # get item from shopkeeper's inventory and draw with buy window
                            for shop_item in shopkeeper_items:
                                screen.blit(shop_item.surf, shop_item.rect)

                        # ----------------------------------------------------------------------------------------------
                        if sell_clicked:
                            for window in sell_shop_elements:
                                screen.blit(window.surf, window.rect)

                            # get item from player's inventory and draw with sell window
                            for sell_item in sell_player_items:
                                screen.blit(sell_item.surf, sell_item.rect)

                    # --------------------------------------------------------------------------------------------------
                    # if building is an inn in the seldon zone
                    if building.__getattribute__("name") == "amuna inn":
                        screen.blit(seldon_district_inn, (0, 0))
                        screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)

                        screen.blit(rest_button.surf, rest_button.rect)
                        screen.blit(leave_button.surf, leave_button.rect)

                        screen.blit(player_status.surf, player_status.rect)
                        screen.blit(text_level_surf, text_level_rect)
                        screen.blit(text_zone_surf, text_zone_rect)
                        screen.blit(text_rupee_surf, text_rupee_rect)

                        screen.blit(message_box.surf, message_box.rect)
                        # draw message box text to screen, updated during scenario
                        screen.blit(text_info_surf_1, text_combat_info_rect_1)
                        screen.blit(text_info_surf_2, text_combat_info_rect_2)
                        screen.blit(text_info_surf_3, text_combat_info_rect_3)
                        screen.blit(text_info_surf_4, text_combat_info_rect_4)

                        # ----------------------------------------------------------------------------------------------
                        if rest_clicked:
                            if not rest:
                                screen.blit(nera_sleep_screen, (0, 0))

            else:
                # don't show if player has recently defeated enemy, so that it doesn't overwrite loot and xp info
                if not loot_update:
                    # lets player know if they are in range of enemy they can press f to attack it
                    info_text_1 = "Press 'F' key to enter building."

        # combat didn't happen this iteration, reset sprites to default surface image
        if not combat_happened:
            combat_cooldown = False
            stan_battle_sprite.update(stan_battle_url)
            snake_battle_sprite.update(snake_battle_url)
            ghoul_battle_sprite.update(ghoul_battle_url)

            # ----------------------------------------------------------------------------------------------------------
            # if size of player's display resolution is less than what the default resolution scaling is set for
            # go through all sprites and make their image and rect attributes smaller
            # scales here at the end of iteration to ensure all sprites updated during iteration are also scaled -------
            if scale_w < 1024 or scale_h < 768:
                if not scaled_800:
                    for sprite in all_sprites:
                        sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                   (sprite.surf.get_width() * .78,
                                                                    sprite.surf.get_height() * .78))
                        sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") * .78,
                                                                   sprite.__getattribute__("y_coordinate") * .78))
                    for element in user_interface:
                        element.surf = pygame.transform.smoothscale(element.surf,
                                                                    (element.surf.get_width() * .78,
                                                                     element.surf.get_height() * .78))
                        element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") * .78,
                                                                     element.__getattribute__("y_coordinate") * .78))
                    for element in conditional_interface:
                        element.surf = pygame.transform.smoothscale(element.surf,
                                                                    (element.surf.get_width() * .78,
                                                                     element.surf.get_height() * .78))
                        element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") * .78,
                                                                     element.__getattribute__("y_coordinate") * .78))
                    for button in screen_resize_buttons:
                        button.surf = pygame.transform.smoothscale(button.surf,
                                                                   (button.surf.get_width() * .78,
                                                                    button.surf.get_height() * .78))
                        button.rect = button.surf.get_rect(center=(button.__getattribute__("x_coordinate") * .78,
                                                                   button.__getattribute__("y_coordinate") * .78))
                    for sprite in battle_elements:
                        sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                   (sprite.surf.get_width() * .78,
                                                                    sprite.surf.get_height() * .78))
                        sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") * .78,
                                                                   sprite.__getattribute__("y_coordinate") * .78))

                    seldon_district_bg = pygame.transform.scale(seldon_district_bg, (scale_w, scale_h))
                    seldon_district_shop = pygame.transform.scale(seldon_district_shop, (scale_w, scale_h))
                    seldon_district_inn = pygame.transform.scale(seldon_district_inn, (scale_w, scale_h))
                    seldon_district_battle = pygame.transform.scale(seldon_district_battle, (scale_w, scale_h))

                    player.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() * .78,
                                                                             player.surf.get_height() * .78))
                    player.rect = player.surf.get_rect(center=player.pos * .78)
                    player.pos *= .78

                    scaled_800 = True
                    scaled_1024 = False
                    scaled_1200 = False

            # ----------------------------------------------------------------------------------------------------------
            if scale_w == 1024 or scale_h == 768:
                if not scaled_1024:
                    if scaled_800:
                        for sprite in all_sprites:
                            sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                       (sprite.surf.get_width() / .78,
                                                                        sprite.surf.get_height() / .78))
                            sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") / .78,
                                                                       sprite.__getattribute__("y_coordinate") / .78))
                        for element in user_interface:
                            element.surf = pygame.transform.smoothscale(element.surf,
                                                                        (element.surf.get_width() / .78,
                                                                         element.surf.get_height() / .78))
                            element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") / .78,
                                                                         element.__getattribute__("y_coordinate")
                                                                         / .78))
                        for element in conditional_interface:
                            element.surf = pygame.transform.smoothscale(element.surf,
                                                                        (element.surf.get_width() / .78,
                                                                         element.surf.get_height() / .78))
                            element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") / .78,
                                                                         element.__getattribute__("y_coordinate")
                                                                         / .78))
                        for button in screen_resize_buttons:
                            button.surf = pygame.transform.smoothscale(button.surf,
                                                                       (button.surf.get_width() / .78,
                                                                        button.surf.get_height() / .78))
                            button.rect = button.surf.get_rect(center=(button.__getattribute__("x_coordinate") / .78,
                                                                       button.__getattribute__("y_coordinate") / .78))
                        for sprite in battle_elements:
                            sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                       (sprite.surf.get_width() / .78,
                                                                        sprite.surf.get_height() / .78))
                            sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") / .78,
                                                                       sprite.__getattribute__("y_coordinate") / .78))

                        seldon_district_bg = pygame.transform.scale(seldon_district_bg, (scale_w, scale_h))
                        seldon_district_shop = pygame.transform.scale(seldon_district_shop, (scale_w, scale_h))
                        seldon_district_inn = pygame.transform.scale(seldon_district_inn, (scale_w, scale_h))
                        seldon_district_battle = pygame.transform.scale(seldon_district_battle, (scale_w, scale_h))

                        player.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() / .78,
                                                                                 player.surf.get_height() / .78))
                        player.rect = player.surf.get_rect(center=player.pos / .78)
                        player.pos /= .78

                    if scaled_1200:
                        for sprite in all_sprites:
                            sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                       (sprite.surf.get_width() * .78,
                                                                        sprite.surf.get_height() * .78))
                            sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") * .78,
                                                                       sprite.__getattribute__("y_coordinate") * .78))
                        for element in user_interface:
                            element.surf = pygame.transform.smoothscale(element.surf,
                                                                        (element.surf.get_width() * .78,
                                                                         element.surf.get_height() * .78))
                            element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") * .78,
                                                                         element.__getattribute__(
                                                                             "y_coordinate") * .78))
                        for element in conditional_interface:
                            element.surf = pygame.transform.smoothscale(element.surf,
                                                                        (element.surf.get_width() * .78,
                                                                         element.surf.get_height() * .78))
                            element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") * .78,
                                                                         element.__getattribute__(
                                                                             "y_coordinate") * .78))
                        for button in screen_resize_buttons:
                            button.surf = pygame.transform.smoothscale(button.surf,
                                                                       (button.surf.get_width() * .78,
                                                                        button.surf.get_height() * .78))
                            button.rect = button.surf.get_rect(center=(button.__getattribute__("x_coordinate") * .78,
                                                                       button.__getattribute__("y_coordinate") * .78))
                        for sprite in battle_elements:
                            sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                       (sprite.surf.get_width() * .78,
                                                                        sprite.surf.get_height() * .78))
                            sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") * .78,
                                                                       sprite.__getattribute__("y_coordinate") * .78))

                        seldon_district_bg = pygame.transform.scale(seldon_district_bg, (scale_w, scale_h))
                        seldon_district_shop = pygame.transform.scale(seldon_district_shop, (scale_w, scale_h))
                        seldon_district_inn = pygame.transform.scale(seldon_district_inn, (scale_w, scale_h))
                        seldon_district_battle = pygame.transform.scale(seldon_district_battle, (scale_w, scale_h))

                        player.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() * .78,
                                                                                 player.surf.get_height() * .78))
                        player.rect = player.surf.get_rect(center=player.pos * .78)
                        player.pos *= .78

                    # conditions updated after scaling
                    scaled_800 = False
                    scaled_1024 = True
                    scaled_1200 = False

            # ----------------------------------------------------------------------------------------------------------
            if scale_w > 1024 or scale_h > 768:
                if not scaled_1200:
                    for sprite in all_sprites:
                        sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                   (sprite.surf.get_width() / .86,
                                                                    sprite.surf.get_height() / .86))
                        sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") / .86,
                                                                   sprite.__getattribute__("y_coordinate") / .86))
                    for element in user_interface:
                        element.surf = pygame.transform.smoothscale(element.surf,
                                                                    (element.surf.get_width() / .86,
                                                                     element.surf.get_height() / .86))
                        element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") / .86,
                                                                     element.__getattribute__("y_coordinate") / .86))
                    for element in conditional_interface:
                        element.surf = pygame.transform.smoothscale(element.surf,
                                                                    (element.surf.get_width() / .86,
                                                                     element.surf.get_height() / .86))
                        element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") / .86,
                                                                     element.__getattribute__("y_coordinate") / .86))
                    for button in screen_resize_buttons:
                        button.surf = pygame.transform.smoothscale(button.surf,
                                                                   (button.surf.get_width() / .86,
                                                                    button.surf.get_height() / .86))
                        button.rect = button.surf.get_rect(center=(button.__getattribute__("x_coordinate") / .86,
                                                                   button.__getattribute__("y_coordinate") / .86))
                    for sprite in battle_elements:
                        sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                   (sprite.surf.get_width() / .86,
                                                                    sprite.surf.get_height() / .86))
                        sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") / .86,
                                                                   sprite.__getattribute__("y_coordinate") / .86))

                    seldon_district_bg = pygame.transform.scale(seldon_district_bg, (scale_w, scale_h))
                    seldon_district_shop = pygame.transform.scale(seldon_district_shop, (scale_w, scale_h))
                    seldon_district_inn = pygame.transform.scale(seldon_district_inn, (scale_w, scale_h))
                    seldon_district_battle = pygame.transform.scale(seldon_district_battle, (scale_w, scale_h))

                    player.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() / .86,
                                                                             player.surf.get_height() / .86))
                    player.rect = player.surf.get_rect(center=player.pos / .86)
                    player.pos /= .86

                    # conditions updated after scaling
                    scaled_800 = False
                    scaled_1024 = False
                    scaled_1200 = True
            # ----------------------------------------------------------------------------------------------------------
            # flip to display ------------------------------------------------------------------------------------------
            pygame.display.flip()

            # ----------------------------------------------------------------------------------------------------------
            # 60 frames per second game rate
            clock.tick(60)

        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # combat happened this turn, update sprites for battle and apply short cooldown to attack again
        if combat_happened:
            combat_cooldown = True
            stan_battle_sprite.update(stan_attack_url)
            snake_battle_sprite.update(snake_attack_url)
            ghoul_battle_sprite.update(ghoul_attack_url)

            # sprite scaling at end of iteration to get updates --------------------------------------------------------
            if scale_w < 1024 or scale_h < 768:
                if not scaled_800:
                    for sprite in all_sprites:
                        sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                   (sprite.surf.get_width() * .78,
                                                                    sprite.surf.get_height() * .78))
                        sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") * .78,
                                                                   sprite.__getattribute__("y_coordinate") * .78))
                    for element in user_interface:
                        element.surf = pygame.transform.smoothscale(element.surf,
                                                                    (element.surf.get_width() * .78,
                                                                     element.surf.get_height() * .78))
                        element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") * .78,
                                                                     element.__getattribute__("y_coordinate") * .78))
                    for element in conditional_interface:
                        element.surf = pygame.transform.smoothscale(element.surf,
                                                                    (element.surf.get_width() * .78,
                                                                     element.surf.get_height() * .78))
                        element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") * .78,
                                                                     element.__getattribute__("y_coordinate") * .78))
                    for button in screen_resize_buttons:
                        button.surf = pygame.transform.smoothscale(button.surf,
                                                                   (button.surf.get_width() * .78,
                                                                    button.surf.get_height() * .78))
                        button.rect = button.surf.get_rect(center=(button.__getattribute__("x_coordinate") * .78,
                                                                   button.__getattribute__("y_coordinate") * .78))
                    for sprite in battle_elements:
                        sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                   (sprite.surf.get_width() * .78,
                                                                    sprite.surf.get_height() * .78))
                        sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") * .78,
                                                                   sprite.__getattribute__("y_coordinate") * .78))

                    seldon_district_bg = pygame.transform.scale(seldon_district_bg, (scale_w, scale_h))
                    seldon_district_shop = pygame.transform.scale(seldon_district_shop, (scale_w, scale_h))
                    seldon_district_inn = pygame.transform.scale(seldon_district_inn, (scale_w, scale_h))
                    seldon_district_battle = pygame.transform.scale(seldon_district_battle, (scale_w, scale_h))

                    player.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() * .78,
                                                                             player.surf.get_height() * .78))
                    player.rect = player.surf.get_rect(center=player.pos * .78)
                    player.pos *= .78

                    scaled_800 = True
                    scaled_1024 = False
                    scaled_1200 = False

            if scale_w == 1024 or scale_h == 768:
                if not scaled_1024:
                    if scaled_800:
                        for sprite in all_sprites:
                            sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                       (sprite.surf.get_width() / .78,
                                                                        sprite.surf.get_height() / .78))
                            sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") / .78,
                                                                       sprite.__getattribute__("y_coordinate") / .78))
                        for element in user_interface:
                            element.surf = pygame.transform.smoothscale(element.surf,
                                                                        (element.surf.get_width() / .78,
                                                                         element.surf.get_height() / .78))
                            element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") / .78,
                                                                         element.__getattribute__("y_coordinate")
                                                                         / .78))
                        for element in conditional_interface:
                            element.surf = pygame.transform.smoothscale(element.surf,
                                                                        (element.surf.get_width() / .78,
                                                                         element.surf.get_height() / .78))
                            element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") / .78,
                                                                         element.__getattribute__("y_coordinate")
                                                                         / .78))
                        for button in screen_resize_buttons:
                            button.surf = pygame.transform.smoothscale(button.surf,
                                                                       (button.surf.get_width() / .78,
                                                                        button.surf.get_height() / .78))
                            button.rect = button.surf.get_rect(center=(button.__getattribute__("x_coordinate") / .78,
                                                                       button.__getattribute__("y_coordinate") / .78))
                        for sprite in battle_elements:
                            sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                       (sprite.surf.get_width() / .78,
                                                                        sprite.surf.get_height() / .78))
                            sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") / .78,
                                                                       sprite.__getattribute__("y_coordinate") / .78))

                        seldon_district_bg = pygame.transform.scale(seldon_district_bg, (scale_w, scale_h))
                        seldon_district_shop = pygame.transform.scale(seldon_district_shop, (scale_w, scale_h))
                        seldon_district_inn = pygame.transform.scale(seldon_district_inn, (scale_w, scale_h))
                        seldon_district_battle = pygame.transform.scale(seldon_district_battle, (scale_w, scale_h))

                        player.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() / .78,
                                                                                 player.surf.get_height() / .78))
                        player.rect = player.surf.get_rect(center=player.pos / .78)
                        player.pos /= .78

                    if scaled_1200:
                        for sprite in all_sprites:
                            sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                       (sprite.surf.get_width() * .78,
                                                                        sprite.surf.get_height() * .78))
                            sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") * .78,
                                                                       sprite.__getattribute__("y_coordinate") * .78))
                        for element in user_interface:
                            element.surf = pygame.transform.smoothscale(element.surf,
                                                                        (element.surf.get_width() * .78,
                                                                         element.surf.get_height() * .78))
                            element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") * .78,
                                                                         element.__getattribute__(
                                                                             "y_coordinate") * .78))
                        for element in conditional_interface:
                            element.surf = pygame.transform.smoothscale(element.surf,
                                                                        (element.surf.get_width() * .78,
                                                                         element.surf.get_height() * .78))
                            element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") * .78,
                                                                         element.__getattribute__(
                                                                             "y_coordinate") * .78))
                        for button in screen_resize_buttons:
                            button.surf = pygame.transform.smoothscale(button.surf,
                                                                       (button.surf.get_width() * .78,
                                                                        button.surf.get_height() * .78))
                            button.rect = button.surf.get_rect(center=(button.__getattribute__("x_coordinate") * .78,
                                                                       button.__getattribute__("y_coordinate") * .78))
                        for sprite in battle_elements:
                            sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                       (sprite.surf.get_width() * .78,
                                                                        sprite.surf.get_height() * .78))
                            sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") * .78,
                                                                       sprite.__getattribute__("y_coordinate") * .78))

                        seldon_district_bg = pygame.transform.scale(seldon_district_bg, (scale_w, scale_h))
                        seldon_district_shop = pygame.transform.scale(seldon_district_shop, (scale_w, scale_h))
                        seldon_district_inn = pygame.transform.scale(seldon_district_inn, (scale_w, scale_h))
                        seldon_district_battle = pygame.transform.scale(seldon_district_battle, (scale_w, scale_h))

                        player.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() * .78,
                                                                                 player.surf.get_height() * .78))
                        player.rect = player.surf.get_rect(center=player.pos * .78)
                        player.pos *= .78

                    # conditions updated after scaling
                    scaled_800 = False
                    scaled_1024 = True
                    scaled_1200 = False

            # ----------------------------------------------------------------------------------------------------------
            if scale_w > 1024 or scale_h > 768:
                if not scaled_1200:
                    for sprite in all_sprites:
                        sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                   (sprite.surf.get_width() / .84,
                                                                    sprite.surf.get_height() / .84))
                        sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") / .84,
                                                                   sprite.__getattribute__("y_coordinate") / .84))
                    for element in user_interface:
                        element.surf = pygame.transform.smoothscale(element.surf,
                                                                    (element.surf.get_width() / .84,
                                                                     element.surf.get_height() / .84))
                        element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") / .84,
                                                                     element.__getattribute__("y_coordinate") / .84))
                    for element in conditional_interface:
                        element.surf = pygame.transform.smoothscale(element.surf,
                                                                    (element.surf.get_width() / .84,
                                                                     element.surf.get_height() / .84))
                        element.rect = element.surf.get_rect(center=(element.__getattribute__("x_coordinate") / .84,
                                                                     element.__getattribute__("y_coordinate") / .84))
                    for button in screen_resize_buttons:
                        button.surf = pygame.transform.smoothscale(button.surf,
                                                                   (button.surf.get_width() / .84,
                                                                    button.surf.get_height() / .84))
                        button.rect = button.surf.get_rect(center=(button.__getattribute__("x_coordinate") / .84,
                                                                   button.__getattribute__("y_coordinate") / .84))
                    for sprite in battle_elements:
                        sprite.surf = pygame.transform.smoothscale(sprite.surf,
                                                                   (sprite.surf.get_width() / .84,
                                                                    sprite.surf.get_height() / .84))
                        sprite.rect = sprite.surf.get_rect(center=(sprite.__getattribute__("x_coordinate") / .84,
                                                                   sprite.__getattribute__("y_coordinate") / .84))

                    seldon_district_bg = pygame.transform.scale(seldon_district_bg, (scale_w, scale_h))
                    seldon_district_shop = pygame.transform.scale(seldon_district_shop, (scale_w, scale_h))
                    seldon_district_inn = pygame.transform.scale(seldon_district_inn, (scale_w, scale_h))
                    seldon_district_battle = pygame.transform.scale(seldon_district_battle, (scale_w, scale_h))

                    player.surf = pygame.transform.smoothscale(player.surf, (player.surf.get_width() / .84,
                                                                             player.surf.get_height() / .84))
                    player.rect = player.surf.get_rect(center=player.pos / .84)
                    player.pos /= .84

                    # conditions updated after scaling
                    scaled_800 = False
                    scaled_1024 = False
                    scaled_1200 = True

            # ----------------------------------------------------------------------------------------------------------
            # flip (update) to display ---------------------------------------------------------------------------------
            pygame.display.flip()

            # when combat happens, wait after flipping display to allow animation time to show
            # 1000 milliseconds = 1 second
            pygame.time.wait(1000)

            # reset combat animation and ability to click on next iteration
            combat_happened = False

            # ----------------------------------------------------------------------------------------------------------
            # 60 frames per second game rate
            clock.tick(60)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # player has died, show game over and give continue option
    else:
        # draw game over screen and continue button
        screen.blit(game_over_screen, (0, 0))
        screen.blit(continue_button.surf, continue_button.rect)

        # --------------------------------------------------------------------------------------------------------------
        # user input events such as key presses or UI interaction
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # player chooses to continue, reset character experience and half health and energy on respawn
                if continue_button.rect.collidepoint(pos):
                    movement_able = True
                    # reset interaction, so it doesn't immediately interact again on subsequent sprite collisions
                    interacted = False
                    # make sure that windows haven't registered a click on reset for whatever reason
                    inventory_clicked = False
                    sell_clicked = False
                    buy_clicked = False
                    encounter_started = False

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
