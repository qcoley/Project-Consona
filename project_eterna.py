import os
import random
import sys
import time

import pygame
from pygame.locals import *

import resource_urls
import bar_updates
import screen_scaling


# global variables -----------------------------------------------------------------------------------------------------
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
ACC = 0.20  # acceleration
FRIC = -0.20  # friction

pygame.display.set_caption("Project Eterna")
vec = pygame.math.Vector2


# ----------------------------------------------------------------------------------------------------------------------
# class objects --------------------------------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):

    def __init__(self, name, gender, race, role, items, equipment, current_quest, quest_status, quest_dictionary,
                 statistics, skills, level, experience, health, energy, alive_status, rupees, reputation, mount,
                 current_zone):

        super(Player, self).__init__()
        self.surf = pygame.image.load(resource_urls.stan_down_url).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
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
            self.surf = pygame.image.load(resource_urls.stan_up_url).convert()

            # when player animation changes to face current walking direction, also apply current resolution scale
            if scaled_1024:
                self.surf = pygame.image.load(resource_urls.stan_up_url_1024).convert()
                self.rect = player.surf.get_rect(center=player.pos * .80)
            if scaled_1600:
                self.surf = pygame.image.load(resource_urls.stan_up_url_1600).convert()
                self.rect = player.surf.get_rect(center=player.pos / .80)
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.y = -ACC

            # set acceleration value based on current resolution scale
            if scaled_1024:
                self.acc.y *= .60
            if scaled_1600:
                self.acc.y /= .60

        if pressed_keyes[K_s]:
            self.surf = pygame.image.load(resource_urls.stan_down_url).convert()

            # when player animation changes to face current walking direction, also apply current resolution scale
            if scaled_1024:
                self.surf = pygame.image.load(resource_urls.stan_down_url_1024).convert()
                self.rect = player.surf.get_rect(center=player.pos * .80)
            if scaled_1600:
                self.surf = pygame.image.load(resource_urls.stan_down_url_1600).convert()
                self.rect = player.surf.get_rect(center=player.pos / .80)
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.y = ACC

            # set acceleration value based on current resolution scale
            if scaled_1024:
                self.acc.y *= .60
            if scaled_1600:
                self.acc.y /= .60

        if pressed_keyes[K_a]:
            self.surf = pygame.image.load(resource_urls.stan_left_url).convert()

            # when player animation changes to face current walking direction, also apply current resolution scale
            if scaled_1024:
                self.surf = pygame.image.load(resource_urls.stan_left_url_1024).convert()
                self.rect = player.surf.get_rect(center=player.pos * .80)
            if scaled_1600:
                self.surf = pygame.image.load(resource_urls.stan_left_url_1600).convert()
                self.rect = player.surf.get_rect(center=player.pos / .80)
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.x = -ACC

            # set acceleration value based on current resolution scale
            if scaled_1024:
                self.acc.x *= .60
            if scaled_1600:
                self.acc.x /= .60

        if pressed_keyes[K_d]:
            self.surf = pygame.image.load(resource_urls.stan_right_url).convert()

            # when player animation changes to face current walking direction, also apply current resolution scale
            if scaled_1024:
                self.surf = pygame.image.load(resource_urls.stan_right_url_1024).convert()
                self.rect = player.surf.get_rect(center=player.pos * .80)
            if scaled_1600:
                self.surf = pygame.image.load(resource_urls.stan_right_url_1600).convert()
                self.rect = player.surf.get_rect(center=player.pos / .80)
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.x = ACC

            # set acceleration value based on current resolution scale
            if scaled_1024:
                self.acc.x *= .60
            if scaled_1600:
                self.acc.x /= .60

        # --------------------------------------------------------------------------------------------------------------
        # Keep player on the screen, boundaries vary depending on current zone -----------------------------------------
        if current_zone == "seldon":

            # set boundaries scaled to current resolution for 1024x576
            if scaled_1024:
                if self.pos.x < 25 * .80:
                    self.pos.x = 25 * .80
                elif self.pos.x > width - 115 * .80:
                    self.pos.x = width - 115 * .80
                if self.pos.y <= 115 * .78:
                    self.pos.y = 115 * .78
                elif self.pos.y >= height - 5 * .80:
                    self.pos.y = height - 5 * .80
            # set boundaries scaled to current resolution for 1280x720
            if scaled_1280:
                if self.pos.x < 25:
                    self.pos.x = 25
                elif self.pos.x > width - 355:
                    self.pos.x = width - 355
                if self.pos.y <= 115:
                    self.pos.y = 115
                elif self.pos.y >= height - 5:
                    self.pos.y = height - 5
            # set boundaries scaled to current resolution for 1600x900
            if scaled_1600:
                if self.pos.x < 25 / .80:
                    self.pos.x = 25 / .80
                elif self.pos.x > width - 115 / .80:
                    self.pos.x = width - 115 / .80
                if self.pos.y <= 115 / .80:
                    self.pos.y = 115 / .80
                elif self.pos.y >= height - 5 / .80:
                    self.pos.y = height - 5 / .80

        # equations and update player movement based on vectors --------------------------------------------------------
        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        # collision detection with environment objects (trees, buildings, etc) -----------------------------------------
        if pygame.sprite.spritecollide(player, environment_objects, False, pygame.sprite.collide_rect_ratio(0.50)):

            # scale current player velocity based on smaller resolution screen (800x600)
            if scaled_1024:
                if pressed_keyes[K_w]:
                    player.vel.y = + .46 * .60
                if pressed_keyes[K_s]:
                    player.vel.y = - .46 * .60
                if pressed_keyes[K_a]:
                    player.vel.x = + .46 * .60
                if pressed_keyes[K_d]:
                    player.vel.x = - .46 * .60
            if scaled_1280:
                # create normal force by applying velocity opposite direction player is trying to move on colliding
                if pressed_keyes[K_w]:
                    player.vel.y = + .46
                if pressed_keyes[K_s]:
                    player.vel.y = - .46
                if pressed_keyes[K_a]:
                    player.vel.x = + .46
                if pressed_keyes[K_d]:
                    player.vel.x = - .46
            # scale current player velocity based on larger resolution screen (1200x900)
            if scaled_1600:
                if pressed_keyes[K_w]:
                    player.vel.y = + .46 / .60
                if pressed_keyes[K_s]:
                    player.vel.y = - .46 / .60
                if pressed_keyes[K_a]:
                    player.vel.x = + .46 / .60
                if pressed_keyes[K_d]:
                    player.vel.x = - .46 / .60


class NPC(pygame.sprite.Sprite):

    def __init__(self, name, gender, race, role, dialog, quest_to_give, quest_description, x_coordinate, y_coordinate,
                 alive_status, quest_complete, items, gift, image, color, image_size):
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
        self.image_size = image_size

    def update(self, image):
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)


class Enemy(pygame.sprite.Sprite):

    def __init__(self, name, kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image,
                 color, health_bar, image_size):
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
        self.image_size = image_size

    # update separate into 2 functions to handle image updates and position updates
    # so that they both don't need the same parameters to change one or the other in main interation
    def update_image(self, x_coord, y_coord, image):

        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

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

    def __init__(self, name, model, x_coordinate, y_coordinate, gathered, image, color, image_size):
        super(Tree, self).__init__()

        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.gathered = gathered
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.image_size = image_size

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        if scaled_1024:
            self.rect = self.surf.get_rect(center=(x_coord * .80, y_coord * .80))
        if scaled_1600:
            self.rect = self.surf.get_rect(center=(x_coord / .80, y_coord / .80))
        else:
            self.rect = self.surf.get_rect(center=(x_coord, y_coord))


class Building(pygame.sprite.Sprite):

    def __init__(self, name, model, x_coordinate, y_coordinate, image, color, image_size):
        super(Building, self).__init__()

        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.image_size = image_size

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        if scaled_1024:
            self.rect = self.surf.get_rect(center=(x_coord * .80, y_coord * .80))
        if scaled_1600:
            self.rect = self.surf.get_rect(center=(x_coord / .80, y_coord / .80))
        else:
            self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# any UI element like buttons, bars, status etc.
class UiElement(pygame.sprite.Sprite):

    def __init__(self, name, x_coordinate, y_coordinate, image, color, update_flag, image_size):
        super(UiElement, self).__init__()

        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.update_flag = update_flag
        self.image_size = image_size

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        if scaled_1024:
            self.rect = self.surf.get_rect(center=(x_coord * .80, y_coord * .80))
        if scaled_1600:
            self.rect = self.surf.get_rect(center=(x_coord / .80, y_coord / .80))
        else:
            self.rect = self.surf.get_rect(center=(x_coord, y_coord))


class Inventory(pygame.sprite.Sprite):

    def __init__(self, name, contains, x_coordinate, y_coordinate, image, color, update_flag, image_size):
        super(Inventory, self).__init__()

        self.name = name
        self.contains = contains
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.update_flag = update_flag
        self.image_size = image_size

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        if scaled_1024:
            self.rect = self.surf.get_rect(center=(x_coord * .80, y_coord * .80))
        if scaled_1600:
            self.rect = self.surf.get_rect(center=(x_coord / .80, y_coord / .80))
        else:
            self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# pop up notifications, like the welcome screen image when game starts
class Notification(pygame.sprite.Sprite):

    def __init__(self, name, shown, x_coordinate, y_coordinate, image, color, image_size):
        super(Notification, self).__init__()

        self.name = name
        self.shown = shown
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.image_size = image_size

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        if scaled_1024:
            self.rect = self.surf.get_rect(center=(x_coord * .80, y_coord * .80))
        if scaled_1600:
            self.rect = self.surf.get_rect(center=(x_coord / .80, y_coord / .80))
        else:
            self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# to create a representation of character for battle screen
class BattleCharacter(pygame.sprite.Sprite):

    def __init__(self, name, x_coordinate, y_coordinate, image, color, image_size):
        super(BattleCharacter, self).__init__()
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.image_size = image_size

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        if scaled_1024:
            self.rect = self.surf.get_rect(center=(x_coord * .80, y_coord * .80))
        if scaled_1280:
            self.rect = self.surf.get_rect(center=(x_coord, y_coord))
        if scaled_1600:
            self.rect = self.surf.get_rect(center=(x_coord / .80, y_coord / .80))


class Item(pygame.sprite.Sprite):

    def __init__(self, name, model, x_coordinate, y_coordinate, image, color, image_size):
        super(Item, self).__init__()

        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.image_size = image_size

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        if scaled_1024:
            self.rect = self.surf.get_rect(center=(x_coord * .80, y_coord * .80))
        if scaled_1600:
            self.rect = self.surf.get_rect(center=(x_coord / .80, y_coord / .80))
        else:
            self.rect = self.surf.get_rect(center=(x_coord, y_coord))


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
    print(npc)
    # npc dialog and quest system will be here
    return


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# gets current player health and updates hp bar image on screen according to the health value from 0-100
def health_bar_update(character):
    hp_bar.update(hp_bar.x_coordinate, hp_bar.y_coordinate, bar_updates.health_bar_update(character))


# player energy bar update
def energy_bar_update(character):
    en_bar.update(en_bar.x_coordinate, en_bar.y_coordinate, bar_updates.energy_bar_update(character))


# player xp bar update
def xp_bar_update(character):
    xp_bar.update(xp_bar.x_coordinate, xp_bar.y_coordinate, bar_updates.xp_bar_update(character))


# enemy health bar update
def health_bar_update_enemy(character):
    character.health_bar.update(character.health_bar.x_coordinate, character.health_bar.y_coordinate,
                                bar_updates.health_bar_update(character))


# ----------------------------------------------------------------------------------------------------------------------
# getting event based on user click related to combat scenario (attack, skill and run buttons)
def combat_event_button(combat_event):
    if combat_event.type == pygame.MOUSEBUTTONUP:
        combat_mouse = pygame.mouse.get_pos()

        # if mouse rect collides with attack button, skill button or run button return string representing it
        if attack_button.rect.collidepoint(combat_mouse):
            return "attack"
        # if skill_button.rect.collidepoint(combat_mouse):
        # return "skill"


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

        except IndexError:
            pass


# ----------------------------------------------------------------------------------------------------------------------
# function to respawn enemies if they are less than a specified amount active in game. spawns with random coord. and lvl
def enemy_respawn():
    snake_counter = 0
    ghoul_counter = 0

    # generate random coordinates and level for new enemy to spawn within boundaries and level range
    if scaled_1024:
        random_snake_x = random.randrange(120, 240)
        random_snake_y = random.randrange(120, 240)
        random_snake_level = random.randrange(1, 4)
        random_ghoul_x = random.randrange(520, 720)
        random_ghoul_y = random.randrange(120, 240)
        random_ghoul_level = random.randrange(3, 6)
    if scaled_1280:
        random_snake_x = random.randrange(150, 300)
        random_snake_y = random.randrange(150, 300)
        random_snake_level = random.randrange(1, 4)
        random_ghoul_x = random.randrange(650, 900)
        random_ghoul_y = random.randrange(150, 300)
        random_ghoul_level = random.randrange(3, 6)
    if scaled_1600:
        random_snake_x = random.randrange(188, 375)
        random_snake_y = random.randrange(188, 375)
        random_snake_level = random.randrange(1, 4)
        random_ghoul_x = random.randrange(812, 1125)
        random_ghoul_y = random.randrange(188, 375)
        random_ghoul_level = random.randrange(3, 6)

    # count current enemies active in game
    for mob in enemies:
        if mob.name == "snake":
            snake_counter += 1
        if mob.name == "ghoul":
            ghoul_counter += 1

    # if there are less than 3 snakes in game, create another snake with random level and coordinates. add to groups
    if snake_counter < 3:
        if scaled_1024:
            new_snake = Enemy("snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y, True,
                              Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_url_1024,
                                   (255, 255, 255), "1024"), resource_urls.snake_url_1024, (255, 255, 255),
                              UiElement("snake hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255),
                                        False, "1024"),
                              "1024")
        if scaled_1280:
            new_snake = Enemy("snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y, True,
                              Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_url,
                                   (255, 255, 255), "1280"), resource_urls.snake_url, (255, 255, 255),
                              UiElement("snake hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255), False,
                                        "1280"),
                              "1280")
        if scaled_1600:
            new_snake = Enemy("snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y, True,
                              Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_url_1600,
                                   (255, 255, 255), "1600"), resource_urls.snake_url_1600, (255, 255, 255),
                              UiElement("snake hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255),
                                        False, "1600"),
                              "1600")
        snakes.add(new_snake)
        enemies.add(new_snake)
        most_sprites.add(new_snake)

    # if there are less than 3 ghouls in game, create another ghoul with random level and coordinates. add to groups
    if ghoul_counter < 3:
        if scaled_1024:
            new_ghoul = Enemy("ghoul", "ghoul", 100, 100, random_ghoul_level, random_ghoul_x, random_ghoul_y, True,
                              Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_url_1024,
                                   (255, 255, 255), "1024"), resource_urls.ghoul_url_1024, (255, 255, 255),
                              UiElement("ghoul hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255),
                                        False, "1024"),
                              "1024")
        if scaled_1280:
            new_ghoul = Enemy("ghoul", "ghoul", 100, 100, random_ghoul_level, random_ghoul_x, random_ghoul_y, True,
                              Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_url,
                                   (255, 255, 255), "1280"), resource_urls.ghoul_url, (255, 255, 255),
                              UiElement("ghoul hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255), False,
                                        "1280"),
                              "1280")
        if scaled_1600:
            new_ghoul = Enemy("ghoul", "ghoul", 100, 100, random_ghoul_level, random_ghoul_x, random_ghoul_y, True,
                              Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_url_1600,
                                   (255, 255, 255), "1600"), resource_urls.ghoul_url_1600, (255, 255, 255),
                              UiElement("ghoul hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255),
                                        False, "1600"),
                              "1600")
        ghouls.add(new_ghoul)
        enemies.add(new_ghoul)
        most_sprites.add(new_ghoul)


def status_and_inventory_updates():
    # update players status bars -----------------------------------------------------------------------
    health_bar_update(player)
    energy_bar_update(player)
    xp_bar_update(player)

    # update function will reset coordinates so fix scaling here for 1600x900 (temp. solution maybe)
    if scaled_1600:
        status_bar_backdrop.rect = status_bar_backdrop.surf.get_rect(
            center=(status_bar_backdrop.x_coordinate / .80, status_bar_backdrop.y_coordinate / .80))
        hp_bar.rect = hp_bar.surf.get_rect(
            center=(hp_bar.x_coordinate / .80 - 1, hp_bar.y_coordinate / .80 + 5))
        en_bar.rect = en_bar.surf.get_rect(
            center=(en_bar.x_coordinate / .80 - 1, en_bar.y_coordinate / .80))
        xp_bar.rect = xp_bar.surf.get_rect(
            center=(xp_bar.x_coordinate / .80 - 1, xp_bar.y_coordinate / .80 - 5))

    # clear list used for drawing player items to screen before going through inventory and drawing
    # this removes items that may have been used and left in list from previous iterations,
    # so they are not re-drawn after being used.
    player_items.clear()

    # create inventory window items ------------------------------------------------------------------------------------
    # if player has items in their inventory ---------------------------------------------------------------------------
    if len(player.items) > 0:
        first_coord = 1063
        second_coord = 462

        if scaled_1024:
            first_coord = first_coord * .80
            second_coord = second_coord * .80
        if scaled_1600:
            first_coord = first_coord - 2
            second_coord = second_coord - 2

        inventory_counter = 0
        # go through player items and assign inventory slots (coordinates) to them
        for item_here in player.items:
            if scaled_1024:
                if item_here.name == "health potion":
                    item_here.update(first_coord, second_coord, resource_urls.health_pot_url_1024)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "energy potion":
                    item_here.update(first_coord, second_coord, resource_urls.energy_pot_url_1024)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "shiny rock":
                    item_here.update(first_coord, second_coord, resource_urls.shiny_rock_url_1024)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "bone dust":
                    item_here.update(first_coord, second_coord, resource_urls.bone_dust_url_1024)
                    player_items.append(item_here)
                    inventory_counter += 1
            if scaled_1280:
                if item_here.name == "health potion":
                    item_here.update(first_coord, second_coord, resource_urls.health_pot_url)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "energy potion":
                    item_here.update(first_coord, second_coord, resource_urls.energy_pot_url)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "shiny rock":
                    item_here.update(first_coord, second_coord, resource_urls.shiny_rock_url)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "bone dust":
                    item_here.update(first_coord, second_coord, resource_urls.bone_dust_url)
                    player_items.append(item_here)
                    inventory_counter += 1
            if scaled_1600:
                if item_here.name == "health potion":
                    item_here.update(first_coord, second_coord, resource_urls.health_pot_url_1600)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "energy potion":
                    item_here.update(first_coord, second_coord, resource_urls.energy_pot_url_1600)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "shiny rock":
                    item_here.update(first_coord, second_coord, resource_urls.shiny_rock_url_1600)
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "bone dust":
                    item_here.update(first_coord, second_coord, resource_urls.bone_dust_url_1600)
                    player_items.append(item_here)
                    inventory_counter += 1

            # add 75 to the items x-coordinate value so the next item will be added to next slot
            first_coord += 60
            if scaled_1024:
                first_coord = first_coord - 13.2
            if scaled_1600:
                first_coord = first_coord + 2

            # add 60 to items y coordinate value if the first row of (4) slots has been filled
            # reset first coordinate and counter to start in the leftmost slot again
            if inventory_counter > 3:
                second_coord += 60
                first_coord = 1063
                inventory_counter = 0
                if scaled_1024:
                    first_coord = first_coord * .80
                    second_coord = second_coord * .80 + 80

        # updates players inventory items if item is used in combat scenario (ex. health pot.)
        for item_here in player_items:
            screen.blit(item_here.surf, item_here.rect)


def inventory_click_handler():
    return_dict = {"item message": ""}
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
    except AttributeError:
        pass

    return return_dict


def text_info_draw():
    # get current player rupee count and create surf and rectangle to blit to screen------------------------------------
    text_rupee_surf = font.render(str(player.rupees), True, "black", "light yellow")
    text_rupee_rect = text_rupee_surf.get_rect()
    if scaled_1024:
        text_rupee_rect.center = (1225 * .80, 362 * .80)
    if scaled_1280:
        text_rupee_rect.center = (1225, 362)
    if scaled_1600:
        text_rupee_rect.center = (1225 / .80, 362 / .80)
    screen.blit(text_rupee_surf, text_rupee_rect)
    # get current player district and create surf and rectangle to blit to screen---------------------------------------
    text_zone_surf = font.render(str(player.current_zone), True, "black", "light yellow")
    text_zone_rect = text_zone_surf.get_rect()
    if scaled_1024:
        text_zone_rect.center = (1120 * .80, 693 * .80)
    if scaled_1280:
        text_zone_rect.center = (1120, 693)
    if scaled_1600:
        text_zone_rect.center = (1120 / .80, 693 / .80)
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


# will be used for music later -----------------------------------------------------------------------------------------
# pygame.mixer.init()
# initialize game, set clock for framerate, set screen size ------------------------------------------------------------
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# background textures --------------------------------------------------------------------------------------------------
seldon_district_bg = pygame.image.load(resource_urls.seldon_bg_screen_url)
seldon_district_battle = pygame.image.load(resource_urls.seldon_battle_screen_url)
seldon_district_shop = pygame.image.load(resource_urls.seldon_shop_screen_url)
seldon_district_inn = pygame.image.load(resource_urls.seldon_inn_screen_url)
seldon_district_academia = pygame.image.load(resource_urls.seldon_academia_screen_url)

game_over_screen = pygame.image.load(resource_urls.game_over_screen_url)
start_screen = pygame.image.load(resource_urls.start_screen_url)
nera_sleep_screen = pygame.image.load(resource_urls.nera_sleep_screen_url)

# creating objects from defined classes --------------------------------------------------------------------------------

# display notifications to user (shown, x_coordinate, y_coordinate, image, color) --------------------------------------
greeting = Notification("greeting", False, 510, 365, resource_urls.welcome_image_url, (255, 255, 255), "1280")

# inventory items ------------------------------------------------------------------------------------------------------
health_potion = Item("health potion", "potion", 200, 200, resource_urls.health_pot_url, (255, 255, 255), "1280")
energy_potion = Item("energy potion", "potion", 200, 200, resource_urls.energy_pot_url, (255, 255, 255), "1280")
shiny_rock = Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_url, (255, 255, 255), "1280")
bone_dust = Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_url, (255, 255, 255), "1280")

# default player character ---------------------------------------------------------------------------------------------
player = Player("player", "male", "amuna", "mage",  # name, gender, race, role
                [health_potion, energy_potion, shiny_rock, bone_dust],  # inventory
                ["magic", "basic staff", "medium", "green robes"],  # equipment ('type', 'name')
                # current quest, quest status (x/4), quest dictionary (quest: done)
                [""], 0, {"Sneaky Snakes": False, "Village Repairs": False, "Ghoulish Ghosts": False},
                ["vitality", 1, "intellect", 3, "strength", 1, "wisdom", 2],  # stats ('stat', 'amount')
                ["barrier"], 1, 5, 100, 100,  # skills, lvl, exp, health, energy
                True, 20, ["amuna", 10, "nuldar", 0, "sorae", 0], "", "")  # alive, rupees, reputation, mount, zone

# nps: name, gender, race, role, dialog, quest, quest_description, x_coordinate, y_coordinate --------------------------
#                  alive_status, quest_complete, items, gift, image, color
npc_garan = NPC("garan", "male", "amuna", "rogue", "It's dangerous to go alone.", "Stupid Snakes",
                "Greetings! I don't believe I've seen you around here before. You must be a traveler, \nright? "
                "Or maybe the request for reinforcements has finally been answered! Well, either way, we're\n"
                "thankful for all the help we can get. \n\nLook, you seem pretty strong, but you're going to need "
                "a weapon to survive out here. \n\nI've got something you can have for now, but you'll need to find "
                "something better if you plan on \njourneying further into the Region. Here's a basic weapon and "
                "some gear. \n\nWhy don't you go and test it out? There's some snakes nearby that have been coming up "
                "from the \nriver. They've shown an unusual aggressiveness with larger numbers than I've seen "
                "before. \n\nMaybe you could take care of them for me? I'll be sure to give you something worth the "
                "trouble. ", 210, 430, True, False, ["Items to be added for steal"], False,
                resource_urls.garan_url, (255, 255, 255), "1280")
npc_maurelle = NPC("maurelle", "female", "amuna", "mage", "We need help!", "Village Repairs",
                   "You there! I don't know who you are, or why you're here, but we could \nreally use your help!"
                   "\n\nThe beast Dreth has occupied our former capital Castle, on the other side of the walls "
                   "\nto the east, and our numbers have been spread thin trying to repel its minions and contain "
                   "the \ndamage they've inflicted. \n\nOur best fighters have been sent in a combined Vanguard with "
                   "the other districts to try and \nattack the beast directly, but its left us vulnerable here. "
                   "The most recent wave of attacks from\nthe castle has left several damages to our village, "
                   "and if you are able, please gather\nresources and bring them to me to distribute to the "
                   "villagers conducting the repairs and \nfortifications. \n\nYou can gather some lumber from the "
                   "trees just west of here. Nera bless you. ", 760, 520, True, False,
                   ["Items to be added for steal"], False,
                   resource_urls.maurelle_url, (255, 255, 255), "1280")
npc_guard = NPC("guard", "male", "amuna", "fighter", "Another day.", "Ghoulish Glee",
                "You need to cross the bridge to get to the Korlok District, you say? \n\nOrdinarily"
                " I would have no issue granting you passage, however the gates are barred tight \n"
                "due to the recent wave of Ghoul Minions from across the wall. \n\nI cannot leave my post and"
                " leave the bridge unguarded, but if you could \ntake care of the remaining ghouls I"
                " will signal to unbar the gates and allow you passage \nto the other side. \n\nThe"
                " ghouls were last spotted just east of here, nearby the northern Castle wall ramparts! ", 460, 120,
                True,
                False, ["Items to be added for steal"], False,
                resource_urls.guard_url, (255, 255, 255), "1280")
npc_amuna_shopkeeper = NPC("amuna shopkeeper", "male", "amuna", "trader", "These ghoul attacks are bad for business!",
                           "", "", 700, 700, True, False, [
                               Item("health potion", "potion", 200, 200, resource_urls.health_pot_url,
                                    (255, 255, 255), "1280"),
                               Item("energy potion", "potion", 200, 200, resource_urls.energy_pot_url,
                                    (255, 255, 255), "1280"),
                               Item("bronze sword", "2H", 200, 200, resource_urls.temp_item_url,
                                    (255, 255, 255), "1280"),
                               Item("bronze armor", "heavy", 200, 200, resource_urls.temp_item_url,
                                    (255, 255, 255), "1280")
                           ], False, resource_urls.amuna_shopkeeper_url, (255, 255, 255), "1280")

# ----------------------------------------------------------------------------------------------------------------------
# enemies: kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image, color, health bar ------
snake_1 = Enemy("snake", "snake", 100, 100, 1, 80, 130, True,
                Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_url, (255, 255, 255), "1280"),
                resource_urls.snake_url, (255, 255, 255),
                UiElement("snake hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255), False, "1280"),
                "1280")
snake_2 = Enemy("snake", "snake", 100, 100, 2, 285, 150, True,
                Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_url, (255, 255, 255), "1280"),
                resource_urls.snake_url, (255, 255, 255),
                UiElement("snake hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255), False, "1280"),
                "1280")
snake_3 = Enemy("snake", "snake", 100, 100, 1, 80, 230, True,
                Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_url, (255, 255, 255), "1280"),
                resource_urls.snake_url, (255, 255, 255),
                UiElement("snake hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255), False, "1280"),
                "1280")
snake_4 = Enemy("snake", "snake", 100, 100, 2, 285, 250, True,
                Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_url, (255, 255, 255), "1280"),
                resource_urls.snake_url, (255, 255, 255),
                UiElement("snake hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255), False, "1280"),
                "1280")
ghoul_low_1 = Enemy("ghoul", "ghoul", 100, 100, 4, 665, 180, True,
                    Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_url, (255, 255, 255), "1280"),
                    resource_urls.ghoul_url, (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255), False, "1280"),
                    "1280")
ghoul_low_2 = Enemy("ghoul", "ghoul", 100, 100, 5, 800, 130, True,
                    Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_url, (255, 255, 255), "1280"),
                    resource_urls.ghoul_url, (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255), False, "1280"),
                    "1280")
ghoul_low_3 = Enemy("ghoul", "ghoul", 100, 100, 3, 760, 240, True,
                    Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_url, (255, 255, 255), "1280"),
                    resource_urls.ghoul_url, (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255), False, "1280"),
                    "1280")
ghoul_low_4 = Enemy("ghoul", "ghoul", 100, 100, 4, 890, 205, True,
                    Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_url, (255, 255, 255), "1280"),
                    resource_urls.ghoul_url, (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, resource_urls.health_100_url, (255, 255, 255), False, "1280"),
                    "1280")

# environmental objects: name, model, x_coordinate, y_coordinate, gathered, image, color -------------------------------
pine_tree_1 = Tree("tree", "pine tree", 80, 445, False, resource_urls.pine_tree_url, (255, 255, 255), "1280")
pine_tree_2 = Tree("tree", "pine tree", 260, 590, False, resource_urls.pine_tree_url, (255, 255, 255), "1280")
pine_tree_3 = Tree("tree", "pine tree", 340, 400, False, resource_urls.pine_tree_url, (255, 255, 255), "1280")
seldon_grass_1 = Item("grass", "seldon grass", 360, 125, resource_urls.seldon_grass_url, (255, 255, 255), "1280")
seldon_grass_2 = Item("grass", "seldon grass", 270, 195, resource_urls.seldon_grass_url, (255, 255, 255), "1280")
seldon_grass_3 = Item("grass", "seldon grass", 405, 235, resource_urls.seldon_grass_url, (255, 255, 255), "1280")
seldon_grass_4 = Item("grass", "seldon grass", 165, 135, resource_urls.seldon_grass_url, (255, 255, 255), "1280")
seldon_grass_5 = Item("grass", "seldon grass", 150, 255, resource_urls.seldon_grass_url, (255, 255, 255), "1280")
seldon_grass_6 = Item("grass", "seldon grass", 50, 180, resource_urls.seldon_grass_url, (255, 255, 255), "1280")
seldon_flower_1 = Item("flower", "seldon flower", 590, 410, resource_urls.seldon_flower_url, (255, 255, 255), "1280")
seldon_flower_2 = Item("flower", "seldon flower", 705, 600, resource_urls.seldon_flower_url, (255, 255, 255), "1280")
seldon_flower_3 = Item("flower", "seldon flower", 800, 440, resource_urls.seldon_flower_url, (255, 255, 255), "1280")

# buildings: name, model, x_coordinate, y_coordinate, image, color -----------------------------------------------------
seldon_inn = Building("inn", "seldon inn", 635, 600, resource_urls.seldon_inn_url, (255, 255, 255), "1280")
seldon_shop = Building("shop", "seldon shop", 665, 400, resource_urls.seldon_shop_url, (255, 255, 255), "1280")
seldon_academia = Building("academia", "seldon academia", 875, 440, resource_urls.seldon_academia_url, (255, 255, 255),
                           "1280")

# ui elements: name, x_coordinate, y_coordinate, image, color, update flag ---------------------------------------------
character_button = UiElement("character button", 860, 680, resource_urls.character_button_url, (255, 255, 255), False,
                             "1280")
journal_button = UiElement("journal button", 970, 680, resource_urls.journal_button_url, (255, 255, 255), False,
                           "1280")

# start screen elements: -----------------------------------------------------------------------------------------------
start_button = UiElement("start button", 640, 274, resource_urls.start_button_url, (255, 255, 255), False, "1280")
s1024_x_576_button = UiElement("s1024x576 button", 640, 402, resource_urls.s1024_x_576_button_url, (255, 255, 255),
                               False, "1280")
s1280_x_720_button = UiElement("s1280x720 button", 640, 472, resource_urls.s1280_x_720_button_url, (255, 255, 255),
                               False, "1280")
s1600_x_900_button = UiElement("s1280x720 button", 640, 542, resource_urls.s1600_x_900_button_url, (255, 255, 255),
                               False, "1280")

# ----------------------------------------------------------------------------------------------------------------------
continue_button = UiElement("continue button", 625, 575, resource_urls.continue_button_url, (255, 255, 255), False,
                            "1280")
buy_button = UiElement("buy button", 860, 680, resource_urls.buy_button_url, (255, 255, 255), False,
                       "1280")
leave_button = UiElement("leave button", 970, 680, resource_urls.leave_button_url, (255, 255, 255), False,
                         "1280")
rest_button = UiElement("rest button", 860, 680, resource_urls.rest_button_url, (255, 255, 255), False,
                        "1280")
learn_button = UiElement("learn button", 860, 680, resource_urls.learn_button_url, (255, 255, 255), False,
                         "1280")
unstuck_button = UiElement("unstuck button", 970, 25, resource_urls.unstuck_button_url, (255, 255, 255), False,
                           "1280")
skill_bar = UiElement("skill bar", 855, 627, resource_urls.skill_bar_url, (255, 255, 255), False,
                      "1280")
attack_button = UiElement("attack button", 750, 627, resource_urls.mage_attack_button_url, (255, 255, 255), False,
                          "1280")
enemy_status = UiElement("enemy status", 855, 680, resource_urls.enemy_status_url, (255, 255, 255), False,
                         "1280")
hp_bar = UiElement("health bar", 170, 25, resource_urls.health_100_url, (255, 255, 255), False,
                   "1280")
en_bar = UiElement("energy bar", 170, 45, resource_urls.energy_100_url, (255, 255, 255), False,
                   "1280")
xp_bar = UiElement("xp bar", 170, 65, resource_urls.xp_100_url, (255, 255, 255), False,
                   "1280")

inventory = Inventory("inventory", [], 890, 515, resource_urls.inventory_url, (255, 255, 255), False, "1280")

quest_logs_1 = Item("quest", "quest logs", 60, 540, resource_urls.quest_logs_url, (255, 255, 255), "1280")
quest_logs_2 = Item("quest", "quest logs", 315, 560, resource_urls.quest_logs_url, (255, 255, 255), "1280")
quest_logs_3 = Item("quest", "quest logs", 415, 435, resource_urls.quest_logs_url, (255, 255, 255), "1280")
quest_logs_4 = Item("quest", "quest logs", 100, 540, resource_urls.quest_logs_url, (255, 255, 255), "1280")

# shop window ---------------------------------------------------------------------------------------------------------
buy_inventory = Inventory("buy inventory", [], 900, 500, resource_urls.buy_inventory_url, (255, 255, 255), False,
                          "1280")

# ----------------------------------------------------------------------------------------------------------------------
message_box = UiElement("message box", 173, 650, resource_urls.message_box_url, (255, 255, 255), False, "1280")
status_bar_backdrop = UiElement("bar backdrop", 165, 45, resource_urls.bar_backdrop_url, (255, 255, 255), False, "1280")
enemy_status_bar_backdrop = UiElement("enemy bar backdrop", 695, 90, resource_urls.enemy_bar_backdrop_url,
                                      (255, 255, 255),
                                      False, "1280")

# battle sprites -------------------------------------------------------------------------------------------------------
stan_battle_sprite = BattleCharacter("stan battle", 320, 460, resource_urls.stan_battle_url, (255, 255, 255), "1280")
snake_battle_sprite = BattleCharacter("snake battle", 700, 250, resource_urls.snake_battle_url, (255, 255, 255), "1280")
ghoul_battle_sprite = BattleCharacter("ghoul battle", 700, 250, resource_urls.ghoul_battle_url, (255, 255, 255), "1280")

# setting font and size for text to screen updates ---------------------------------------------------------------------
font = pygame.font.SysFont('freesansbold.ttf', 16, bold=True, italic=False)

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
scaling_sprites = pygame.sprite.Group()
start_screen_sprites = pygame.sprite.Group()
game_over_screen_sprites = pygame.sprite.Group()

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
user_interface.add(rest_button, buy_button, leave_button, character_button, journal_button, unstuck_button, message_box)
conditional_interface.add(buy_inventory)
start_screen_sprites.add(s1024_x_576_button, s1280_x_720_button, s1600_x_900_button, start_button)
game_over_screen_sprites.add(continue_button)
# all environment sprites for collision detection ----------------------------------------------------------------------
environment_objects.add(trees, buildings)
# quest item sprites for gathering -------------------------------------------------------------------------------------
quest_items.add(quest_logs_1, quest_logs_2, quest_logs_3, quest_logs_4)
# battle element sprites for combat scenario ---------------------------------------------------------------------------
battle_elements.add(stan_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, enemy_status, skill_bar,
                    attack_button)
# adding most sprites to this group for drawing and related functions
most_sprites.add(npcs, trees, buildings, grass, flowers, quest_items, enemies)
# adding these sprites to a scaling sprite group which is used to reference sprites that should be scaled
scaling_sprites.add(most_sprites, user_interface, enemies, battle_elements, conditional_interface, start_screen_sprites,
                    game_over_screen_sprites, greeting)

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
start_chosen = False
player_created = True
in_battle = False
in_shop = False
in_inn = False
in_academia = False
in_district_over_world = True
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
learn_clicked = False
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
# conditions to check current screen size scaling
scaled_1024 = False
scaled_1280 = True
scaled_1600 = False
# condition to check if initial player position has been set to current resolution scale
player_initial_pos_set = False
# condition that checks if inn screen has been faded when player rests
faded_inn_screen = False
# what zone the player is in, used for player update and map boundaries
zone_seldon = True
zone_korlok = False
zone_eldream = False
zone_marrow = False

# list to contain current player items for display
player_items = []
# list to contain buy inventory window for display within shop
buy_shop_elements = []
# list to contain current shop items for display
shopkeeper_items = []
# list to contain screen size elements for display
display_elements = []

# combat text strings to be updated on scenario, shown on UI message box
# initially set to these default strings but will be overwritten
info_text_1 = ""
info_text_2 = ""
info_text_3 = ""
info_text_4 = ""
# text updates from battle instance to apply to main over-world message box
battle_info_to_return_to_main_loop = {"experience": 0, "item dropped": "", "leveled_up": False}

# ----------------------------------------------------------------------------------------------------------------------
# main loop ------------------------------------------------------------------------------------------------------------
while game_running:

    if not start_chosen:
        screen.blit(start_screen, (0, 0))
        screen.blit(start_button.surf, start_button.rect)
        screen.blit(s1024_x_576_button.surf, s1024_x_576_button.rect)
        screen.blit(s1280_x_720_button.surf, s1280_x_720_button.rect)
        screen.blit(s1600_x_900_button.surf, s1600_x_900_button.rect)

        # ---------------------------------------------------------------------------------------------------------------
        # user input events such as key presses or UI interaction
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # player chooses to continue, reset character experience and half health and energy on respawn
                if start_button.rect.collidepoint(pos):
                    start_chosen = True
                    # start timer for greeting message when button is clicked
                    tic = time.perf_counter()

                # 1024 x 576 (down-scale) resolution -------------------------------------------------------------------
                if s1024_x_576_button.rect.collidepoint(pos):
                    if not scaled_1024:
                        width = 1024
                        height = 576
                        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

                        start_screen = pygame.image.load(resource_urls.start_screen_url_1024)
                        seldon_district_bg = pygame.image.load(resource_urls.seldon_bg_screen_url_1024)
                        seldon_district_shop = pygame.image.load(resource_urls.seldon_shop_screen_url_1024)
                        seldon_district_inn = pygame.image.load(resource_urls.seldon_inn_screen_url_1024)
                        seldon_district_academia = pygame.image.load(resource_urls.seldon_academia_screen_url_1024)
                        seldon_district_battle = pygame.image.load(resource_urls.seldon_battle_screen_url_1024)
                        nera_sleep_screen = pygame.image.load(resource_urls.nera_sleep_screen_url_1024)
                        game_over_screen = pygame.image.load(resource_urls.game_over_screen_url_1024)

                        for sprite_to_scale in scaling_sprites:
                            sprite_to_scale.image_size = "1024"
                            sprite_to_scale.surf = pygame.image.load(
                                screen_scaling.screen_scaling(sprite_to_scale)).convert()
                            sprite_to_scale.surf.set_colorkey((255, 255, 255), RLEACCEL)
                            sprite_to_scale.rect = sprite_to_scale.surf.get_rect(
                                center=(sprite_to_scale.x_coordinate * .80, sprite_to_scale.y_coordinate * .80))

                        player.image_size = "1024"
                        player.surf = pygame.image.load(
                            screen_scaling.screen_scaling(player)).convert()
                        player.surf.set_colorkey((255, 255, 255), RLEACCEL)

                        scaled_1024 = True
                        scaled_1280 = False
                        scaled_1600 = False

                # 1280 x 720 (original) resolution ---------------------------------------------------------------------
                if s1280_x_720_button.rect.collidepoint(pos):
                    if not scaled_1280:
                        width = 1280
                        height = 720
                        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

                        start_screen = pygame.image.load(resource_urls.start_screen_url)
                        seldon_district_bg = pygame.image.load(resource_urls.seldon_bg_screen_url)
                        seldon_district_shop = pygame.image.load(resource_urls.seldon_shop_screen_url)
                        seldon_district_inn = pygame.image.load(resource_urls.seldon_inn_screen_url)
                        seldon_district_academia = pygame.image.load(resource_urls.seldon_academia_screen_url)
                        seldon_district_battle = pygame.image.load(resource_urls.seldon_battle_screen_url)
                        nera_sleep_screen = pygame.image.load(resource_urls.nera_sleep_screen_url)
                        game_over_screen = pygame.image.load(resource_urls.game_over_screen_url)

                        for sprite_to_scale in scaling_sprites:
                            sprite_to_scale.image_size = "1280"
                            sprite_to_scale.surf = pygame.image.load(
                                screen_scaling.screen_scaling(sprite_to_scale)).convert()
                            sprite_to_scale.surf.set_colorkey((255, 255, 255), RLEACCEL)
                            sprite_to_scale.rect = sprite_to_scale.surf.get_rect(
                                center=(sprite_to_scale.x_coordinate, sprite_to_scale.y_coordinate))

                        player.image_size = "1280"
                        player.surf = pygame.image.load(
                            screen_scaling.screen_scaling(player)).convert()
                        player.surf.set_colorkey((255, 255, 255), RLEACCEL)

                        scaled_1024 = False
                        scaled_1280 = True
                        scaled_1600 = False

                # 1600 x 900 (up-scale) resolution ---------------------------------------------------------------------
                if s1600_x_900_button.rect.collidepoint(pos):
                    if not scaled_1600:
                        width = 1600
                        height = 900
                        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

                        start_screen = pygame.image.load(resource_urls.start_screen_url_1600)
                        seldon_district_bg = pygame.image.load(resource_urls.seldon_bg_screen_url_1600)
                        seldon_district_shop = pygame.image.load(resource_urls.seldon_shop_screen_url_1600)
                        seldon_district_inn = pygame.image.load(resource_urls.seldon_inn_screen_url_1600)
                        seldon_district_academia = pygame.image.load(resource_urls.seldon_academia_screen_url_1600)
                        seldon_district_battle = pygame.image.load(resource_urls.seldon_battle_screen_url_1600)
                        nera_sleep_screen = pygame.image.load(resource_urls.nera_sleep_screen_url_1600)
                        game_over_screen = pygame.image.load(resource_urls.game_over_screen_url_1600)

                        for sprite_to_scale in scaling_sprites:
                            sprite_to_scale.image_size = "1600"
                            sprite_to_scale.surf = pygame.image.load(
                                screen_scaling.screen_scaling(sprite_to_scale)).convert()
                            sprite_to_scale.surf.set_colorkey((255, 255, 255), RLEACCEL)
                            sprite_to_scale.rect = sprite_to_scale.surf.get_rect(
                                center=(sprite_to_scale.x_coordinate / .80, sprite_to_scale.y_coordinate / .80))

                        player.image_size = "1600"
                        player.surf = pygame.image.load(
                            screen_scaling.screen_scaling(player)).convert()
                        player.surf.set_colorkey((255, 255, 255), RLEACCEL)

                        scaled_1024 = False
                        scaled_1280 = False
                        scaled_1600 = True

            elif event.type == QUIT:
                exit()

            pygame.display.flip()

    # if player has chosen to start game -------------------------------------------------------------------------------
    if start_chosen:
        # start game clock
        clock = pygame.time.Clock()

        # update initial player position based on chosen resolution scaling at start screen
        # set condition to true after position is set, so it doesn't keep applying
        if not player_initial_pos_set:
            if scaled_1024:
                player.pos = player.pos * .80
                player_initial_pos_set = True
            if scaled_1600:
                player.pos = player.pos / .80
                player_initial_pos_set = True

        # scale font size to current screen resolution
        if scaled_1024:
            font = pygame.font.SysFont('freesansbold.ttf', 16, bold=True, italic=False)
        if scaled_1280:
            font = pygame.font.SysFont('freesansbold.ttf', 20, bold=True, italic=False)
        if scaled_1600:
            font = pygame.font.SysFont('freesansbold.ttf', 24, bold=True, italic=False)

        # if player has created character or chosen default
        if player_created:
            # if player is currently alive
            if player.alive_status:
                # if player is in over world
                if in_district_over_world:

                    # clear info update after some time has passed
                    if pygame.time.get_ticks() % 287 == 0:
                        info_update = False
                    # clear loot update after some time has passed
                    if pygame.time.get_ticks() % 347 == 0:
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
                    enemy_respawn()
                    # create blank background to be drawn on top of for each iteration
                    screen.fill((255, 255, 255))  # (255, 255, 255) RGB value for WHITE
                    # draw screen 1 background
                    screen.blit(seldon_district_bg, (0, 0))

                    # draw sprites
                    for entity in most_sprites:
                        screen.blit(entity.surf, entity.rect)
                    # draw enemies
                    for enemy_sprite in enemies:
                        screen.blit(enemy_sprite.surf, enemy_sprite.rect)
                    # draw player
                    screen.blit(player.surf, player.rect)
                    # draw user interface elements
                    for ui_element in user_interface:
                        screen.blit(ui_element.surf, ui_element.rect)
                    # get screen option elements and draw window
                    for window in display_elements:
                        screen.blit(window.surf, window.rect)

                    # corrects position of player status bars and backdrop if scaled to 1600x900 resolution
                    if scaled_1600:
                        status_bar_backdrop.rect = status_bar_backdrop.surf.get_rect(
                            center=(status_bar_backdrop.x_coordinate / .80, status_bar_backdrop.y_coordinate / .80))
                        hp_bar.rect = hp_bar.surf.get_rect(
                            center=(hp_bar.x_coordinate / .80 - 1, hp_bar.y_coordinate / .80 + 5))
                        en_bar.rect = en_bar.surf.get_rect(
                            center=(en_bar.x_coordinate / .80 - 1, en_bar.y_coordinate / .80))
                        xp_bar.rect = xp_bar.surf.get_rect(
                            center=(xp_bar.x_coordinate / .80 - 1, xp_bar.y_coordinate / .80 - 5))

                    screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                    screen.blit(hp_bar.surf, hp_bar.rect)
                    screen.blit(en_bar.surf, en_bar.rect)
                    screen.blit(xp_bar.surf, xp_bar.rect)

                    # draw texts to the screen, like message box, player rupees and level
                    text_info_draw()
                    # update players current inventory and status
                    status_and_inventory_updates()

                    # if battle happened, get battle info (item or experience gained) and apply to message box
                    if battle_info_to_return_to_main_loop["item dropped"] != "":
                        if loot_update:
                            info_text_3 = str(battle_info_to_return_to_main_loop["item dropped"])
                            info_text_4 = str(battle_info_to_return_to_main_loop["experience"])

                    # --------------------------------------------------------------------------------------------------
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
                            if unstuck_button.rect.collidepoint(pos):
                                if scaled_1024:
                                    player.pos = vec((850 * .80, 650 * .80))
                                if scaled_1280:
                                    player.pos = vec((850, 650))
                                if scaled_1600:
                                    player.pos = vec((850 / .80, 650 / .80))

                        elif event.type == QUIT:
                            exit()

                        # ----------------------------------------------------------------------------------------------
                        # if player collides with enemy sprite, doesn't have combat cooldown,
                        # and chooses to interact with it then get event from button press and start combat encounter
                        enemy = pygame.sprite.spritecollideany(player, enemies)
                        if enemy:
                            # lets player know if they are in range of enemy they can press f to attack it
                            info_text_1 = f"Press 'F' key to attack {enemy.name}."
                            info_text_2 = f"{enemy.name} level: {enemy.level}"
                            if interacted:
                                in_district_over_world = False
                                in_battle = True

                        # ----------------------------------------------------------------------------------------------
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

                        # function to handle inventory item clicks. apply item message to message box if not empty str.
                        inventory_event = inventory_click_handler()
                        if inventory_event["item message"] != "":
                            info_text_1 = inventory_event["item message"]
                            info_text_2 = ""
                            info_update = True

                    # outside of main event loop -----------------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    # get current pressed keys from player and apply zone boundaries depending on current zone
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

                    # get time elapsed since player started game
                    toc = time.perf_counter()

                    # if greeting has been shown, and time has elapsed, hide greeting window from screen
                    if greeting.shown:
                        # if time elapsed has been greater than 5 seconds, hide the greeting window
                        if toc - tic > 2.5:
                            for notification in display_elements:
                                try:
                                    if notification.name == "greeting":
                                        display_elements.remove(notification)
                                except AttributeError:
                                    pass

                    # enemy movement updates ---------------------------------------------------------------------------
                    # choose random directions and random enemy to move that direction ---------------------------------
                    direction_horizontal = random.choice(["left", "right"])
                    direction_vertical = random.choice(["up", "down"])
                    move_this_snake = random.choice(snakes.sprites())
                    move_this_ghoul = random.choice(ghouls.sprites())

                    # move snakes in random direction within boundaries
                    if movement_able:
                        if pygame.time.get_ticks() % 20 == 0:
                            if scaled_1024:
                                move_this_snake.update_position([30 * .80, 400 * .80], [150 * .80, 350 * .80],
                                                                direction_horizontal, direction_vertical)
                                move_this_ghoul.update_position([650 * .80, 920 * .80], [150 * .80, 350 * .80],
                                                                direction_horizontal, direction_vertical)
                            if scaled_1280:
                                move_this_snake.update_position([30, 400], [150, 350],
                                                                direction_horizontal, direction_vertical)
                                move_this_ghoul.update_position([650, 920], [150, 350],
                                                                direction_horizontal, direction_vertical)
                            if scaled_1600:
                                move_this_snake.update_position([30 / .80, 400 / .80], [150 / .80, 350 / .80],
                                                                direction_horizontal, direction_vertical)
                                move_this_ghoul.update_position([650 / .80, 920 / .80], [150 / .80, 350 / .80],
                                                                direction_horizontal, direction_vertical)

                    # npc movement updates -----------------------------------------------------------------------------
                    # choose random facing direction and random npc to move face that direction ------------------------
                    face_direction = random.choice(["front", "back", "left", "right"])
                    face_this_npc = random.choice(npcs.sprites())

                    if pygame.time.get_ticks() % 180 == 0:
                        if face_direction == "front":
                            if scaled_1024:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_url_1024)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_url_1024)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_url_1024)
                            if scaled_1280:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_url)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_url)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_url)
                            if scaled_1600:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_url_1600)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_url_1600)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_url_1600)
                        if face_direction == "back":
                            if scaled_1024:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_back_url_1024)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_back_url_1024)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_back_url_1024)
                            if scaled_1280:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_back_url)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_back_url)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_back_url)
                            if scaled_1600:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_back_url_1600)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_back_url_1600)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_back_url_1600)
                        if face_direction == "left":
                            if scaled_1024:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_left_url_1024)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_left_url_1024)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_left_url_1024)
                            if scaled_1280:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_left_url)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_left_url)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_left_url)
                            if scaled_1600:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_left_url_1600)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_left_url_1600)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_left_url_1600)
                        if face_direction == "right":
                            if scaled_1024:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_right_url_1024)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_right_url_1024)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_right_url_1024)
                            if scaled_1280:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_right_url)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_right_url)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_right_url)
                            if scaled_1600:
                                if face_this_npc.name == "garan":
                                    npc_garan.update(resource_urls.garan_right_url_1600)
                                if face_this_npc.name == "maurelle":
                                    npc_maurelle.update(resource_urls.maurelle_right_url_1600)
                                if face_this_npc.name == "guard":
                                    npc_guard.update(resource_urls.guard_right_url_1600)

                # ------------------------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if player is in battle -------------------------------------------------------------------------------
                if in_battle:

                    # update players current inventory and status
                    status_and_inventory_updates()

                    # battle scenario event loop
                    # --------------------------------------------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                exit()

                        elif event.type == QUIT:
                            exit()

                        # function to handle inventory item clicks. apply item message to message box if not empty str.
                        inventory_event = inventory_click_handler()
                        if inventory_event["item message"] != "":
                            info_text_1 = inventory_event["item message"]
                            info_text_2 = ""
                            info_update = True

                        enemy = pygame.sprite.spritecollideany(player, enemies)
                        if enemy:

                            # update enemy health bar on each iteration
                            health_bar_update_enemy(enemy)

                            # don't let player attack again immediately by spam clicking button
                            # the combat cooldown at the end of battle sequence has a time delay which prevents this
                            # but an additional check is used here so the button click won't register for
                            # multiple attacks to happen after the delay is over
                            if not combat_cooldown:
                                # if interact key 'f' has been pressed
                                if interacted:
                                    # don't allow player to move while in combat
                                    movement_able = False

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

                                    # Info returned from combat scenario function in form of dictionary ----------------
                                    # "damage done": 0,
                                    # "damage taken": 0,
                                    # "item dropped": "",
                                    # "experience gained": 0,
                                    # "quest update": "",
                                    # "enemy defeated": False,
                                    # "escaped": False
                                    # "level up status": "",
                                    # "level up attributes": ""

                                    # enter combat scenario and attack enemy. attack_scenario will return all info in
                                    # form of list
                                    if combat_button == "attack":

                                        if scaled_1024:
                                            # update player character sprite for combat animation
                                            stan_battle_sprite.update(stan_battle_sprite.x_coordinate,
                                                                      stan_battle_sprite.y_coordinate,
                                                                      resource_urls.stan_attack_url_1024)
                                            # update to attacking sprite surface for combat animation
                                            if enemy.kind == "snake":
                                                snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                                           snake_battle_sprite.y_coordinate,
                                                                           resource_urls.snake_attack_url_1024)
                                            if enemy.kind == "ghoul":
                                                ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                                           ghoul_battle_sprite.y_coordinate,
                                                                           resource_urls.ghoul_attack_url_1024)
                                        if scaled_1280:
                                            # update player character sprite for combat animation
                                            stan_battle_sprite.update(stan_battle_sprite.x_coordinate,
                                                                      stan_battle_sprite.y_coordinate,
                                                                      resource_urls.stan_attack_url)
                                            # update to attacking sprite surface for combat animation
                                            if enemy.kind == "snake":
                                                snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                                           snake_battle_sprite.y_coordinate,
                                                                           resource_urls.snake_attack_url)
                                            if enemy.kind == "ghoul":
                                                ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                                           ghoul_battle_sprite.y_coordinate,
                                                                           resource_urls.ghoul_attack_url)
                                        if scaled_1600:
                                            # update player character sprite for combat animation
                                            stan_battle_sprite.update(stan_battle_sprite.x_coordinate,
                                                                      stan_battle_sprite.y_coordinate,
                                                                      resource_urls.stan_attack_url_1600)
                                            # update to attacking sprite surface for combat animation
                                            if enemy.kind == "snake":
                                                snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                                           snake_battle_sprite.y_coordinate,
                                                                           resource_urls.snake_attack_url_1600)
                                            if enemy.kind == "ghoul":
                                                ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                                           ghoul_battle_sprite.y_coordinate,
                                                                           resource_urls.ghoul_attack_url_1600)

                                        # ------------------------------------------------------------------------------
                                        # ------------------------------------------------------------------------------
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
                                            movement_able = True
                                            combat_happened = False
                                            interacted = False
                                            loot_update = True
                                            encounter_started = False
                                            in_battle = False
                                            in_district_over_world = True

                    # outside of battle event loop ---------------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    # battle scene and enemy are drawn to screen -------------------------------------------------------
                    try:
                        if zone_seldon:
                            screen.blit(seldon_district_battle, (0, 0))
                            screen.blit(stan_battle_sprite.surf, stan_battle_sprite.rect)
                            screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                            screen.blit(hp_bar.surf, hp_bar.rect)
                            screen.blit(en_bar.surf, en_bar.rect)
                            screen.blit(xp_bar.surf, xp_bar.rect)
                            screen.blit(skill_bar.surf, skill_bar.rect)
                            screen.blit(attack_button.surf, attack_button.rect)
                            if enemy.name == "snake":
                                screen.blit(snake_battle_sprite.surf, snake_battle_sprite.rect)
                            if enemy.name == "ghoul":
                                screen.blit(ghoul_battle_sprite.surf, ghoul_battle_sprite.rect)
                            if scaled_1024:
                                enemy_status_bar_backdrop.rect = enemy_status_bar_backdrop.surf.get_rect(
                                    center=(enemy_status_bar_backdrop.x_coordinate * .80,
                                            enemy_status_bar_backdrop.y_coordinate * .80))
                                enemy.health_bar.rect = enemy.health_bar.surf.get_rect(
                                    center=(enemy.health_bar.x_coordinate * .80,
                                            enemy.health_bar.y_coordinate * .80))
                            if scaled_1600:
                                enemy_status_bar_backdrop.rect = enemy_status_bar_backdrop.surf.get_rect(
                                    center=(enemy_status_bar_backdrop.x_coordinate / .80,
                                            enemy_status_bar_backdrop.y_coordinate / .80))
                                enemy.health_bar.rect = enemy.health_bar.surf.get_rect(
                                    center=(enemy.health_bar.x_coordinate / .80,
                                            enemy.health_bar.y_coordinate / .80))
                            screen.blit(enemy_status_bar_backdrop.surf, enemy_status_bar_backdrop.rect)
                            screen.blit(enemy.health_bar.surf, enemy.health_bar.rect)
                            screen.blit(enemy_status.surf, enemy_status.rect)
                            screen.blit(message_box.surf, message_box.rect)
                            screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                            screen.blit(hp_bar.surf, hp_bar.rect)
                            screen.blit(en_bar.surf, en_bar.rect)
                            screen.blit(xp_bar.surf, xp_bar.rect)

                            # updates players inventory items if item is used in combat scenario (ex. health pot.)
                            for item in player_items:
                                screen.blit(item.surf, item.rect)

                            text_info_draw()

                            # get current enemy name and create surf and rectangle to draw to screen
                            text_enemy_name_surf = font.render(str(enemy.name), True, "black", "light yellow")
                            text_enemy_name_rect = text_enemy_name_surf.get_rect()
                            if scaled_1024:
                                text_enemy_name_rect.center = (800 * .80, 680 * .80)
                            if scaled_1280:
                                text_enemy_name_rect.center = (800, 680)
                            if scaled_1600:
                                text_enemy_name_rect.center = (800 / .80, 680 / .80)
                            screen.blit(text_enemy_name_surf, text_enemy_name_rect)
                            # get current enemy level and create surf and rectangle to draw to screen
                            text_enemy_level_surf = font.render(str(enemy.level), True, "black", "light yellow")
                            text_enemy_level_rect = text_enemy_level_surf.get_rect()
                            if scaled_1024:
                                text_enemy_level_rect.center = (915 * .80, 680 * .80)
                            if scaled_1280:
                                text_enemy_level_rect.center = (915, 680)
                            if scaled_1600:
                                text_enemy_level_rect.center = (915 / .80, 680 / .80)
                            screen.blit(text_enemy_level_surf, text_enemy_level_rect)

                    # after enemy is defeated, it may return a none type for collision. in this case, just ignore error
                    except AttributeError:
                        pass

                    # --------------------------------------------------------------------------------------------------
                    # combat didn't happen this iteration, reset sprites to default surface image
                    if not combat_happened:

                        if scaled_1024:
                            stan_battle_sprite.update(stan_battle_sprite.x_coordinate,
                                                      stan_battle_sprite.y_coordinate,
                                                      resource_urls.stan_battle_url_1024)
                            snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                       snake_battle_sprite.y_coordinate,
                                                       resource_urls.snake_battle_url_1024)
                            ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                       ghoul_battle_sprite.y_coordinate,
                                                       resource_urls.ghoul_battle_url_1024)
                        if scaled_1280:
                            stan_battle_sprite.update(stan_battle_sprite.x_coordinate,
                                                      stan_battle_sprite.y_coordinate,
                                                      resource_urls.stan_battle_url)
                            snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                       snake_battle_sprite.y_coordinate,
                                                       resource_urls.snake_battle_url)
                            ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                       ghoul_battle_sprite.y_coordinate,
                                                       resource_urls.ghoul_battle_url)
                        if scaled_1600:
                            stan_battle_sprite.update(stan_battle_sprite.x_coordinate,
                                                      stan_battle_sprite.y_coordinate,
                                                      resource_urls.stan_battle_url_1600)
                            snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                       snake_battle_sprite.y_coordinate,
                                                       resource_urls.snake_battle_url_1600)
                            ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                       ghoul_battle_sprite.y_coordinate,
                                                       resource_urls.ghoul_battle_url_1600)
                        combat_cooldown = False

                    # combat happened this turn, update sprites for battle and apply short cooldown to attack again
                    if combat_happened:

                        if scaled_1024:
                            stan_battle_sprite.update(stan_battle_sprite.x_coordinate,
                                                      stan_battle_sprite.y_coordinate,
                                                      resource_urls.stan_attack_url_1024)
                            snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                       snake_battle_sprite.y_coordinate,
                                                       resource_urls.snake_attack_url_1024)
                            ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                       ghoul_battle_sprite.y_coordinate,
                                                       resource_urls.ghoul_attack_url_1024)
                        if scaled_1280:
                            stan_battle_sprite.update(stan_battle_sprite.x_coordinate,
                                                      stan_battle_sprite.y_coordinate,
                                                      resource_urls.stan_attack_url)
                            snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                       snake_battle_sprite.y_coordinate,
                                                       resource_urls.snake_attack_url)
                            ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                       ghoul_battle_sprite.y_coordinate,
                                                       resource_urls.ghoul_attack_url)
                        if scaled_1600:
                            stan_battle_sprite.update(stan_battle_sprite.x_coordinate,
                                                      stan_battle_sprite.y_coordinate,
                                                      resource_urls.stan_attack_url_1600)
                            snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                       snake_battle_sprite.y_coordinate,
                                                       resource_urls.snake_attack_url_1600)
                            ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                       ghoul_battle_sprite.y_coordinate,
                                                       resource_urls.ghoul_attack_url_1600)
                        # flip to display ------------------------------------------------------------------------------
                        # needs to flip here to show the new attacking sprites for the 1-second duration
                        pygame.display.flip()

                        combat_cooldown = True

                        # when combat happens, wait after flipping display to allow animation time to show
                        # 1000 milliseconds = 1 second
                        pygame.time.wait(1000)

                        # reset combat animation and ability to click without delay on next iteration
                        combat_happened = False

                # ------------------------------------------------------------------------------------------------------
                # if player is in shop ---------------------------------------------------------------------------------
                if in_shop:

                    status_and_inventory_updates()

                    # shop scenario event loop
                    # --------------------------------------------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                exit()

                        elif event.type == QUIT:
                            exit()

                        # ----------------------------------------------------------------------------------------------
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

                            # get which button player pressed during shop scenario (buy or leave)-------------------
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

                                # user clicked buy button for the first time. show buy window ----------------------
                                else:
                                    buy_clicked = True
                                    buy_shop_elements.insert(0, buy_inventory)

                                    # if shopkeeper has items in their inventory
                                    if len(npc_amuna_shopkeeper.items) > 0:
                                        buy_first_coord = 810
                                        buy_second_coord = 435

                                        if scaled_1024:
                                            buy_first_coord = buy_first_coord * .80
                                            buy_second_coord = buy_second_coord * .80
                                        if scaled_1600:
                                            buy_first_coord = buy_first_coord - 2
                                            buy_second_coord = buy_second_coord - 2

                                        # --------------------------------------------------------------------------
                                        buy_inventory_counter = 0
                                        # go through shop items and assign inventory slots (coordinates) to them
                                        for shop_item in npc_amuna_shopkeeper.items:
                                            if shop_item.name == "health potion":
                                                if scaled_1024:
                                                    shop_item.update(buy_first_coord, buy_second_coord,
                                                                     resource_urls.health_pot_url_1024)
                                                if scaled_1280:
                                                    shop_item.update(buy_first_coord, buy_second_coord,
                                                                     resource_urls.health_pot_url)
                                                if scaled_1600:
                                                    shop_item.update(buy_first_coord, buy_second_coord,
                                                                     resource_urls.health_pot_url_1600)
                                                shopkeeper_items.append(shop_item)
                                                buy_inventory_counter += 1

                                            if shop_item.name == "energy potion":
                                                if scaled_1024:
                                                    shop_item.update(buy_first_coord, buy_second_coord,
                                                                     resource_urls.energy_pot_url_1024)
                                                if scaled_1280:
                                                    shop_item.update(buy_first_coord, buy_second_coord,
                                                                     resource_urls.energy_pot_url)
                                                if scaled_1600:
                                                    shop_item.update(buy_first_coord, buy_second_coord,
                                                                     resource_urls.energy_pot_url_1600)
                                                shopkeeper_items.append(shop_item)
                                                buy_inventory_counter += 1

                                            buy_first_coord += 60
                                            if scaled_1024:
                                                buy_first_coord = buy_first_coord - 13.2
                                            if scaled_1600:
                                                buy_first_coord = buy_first_coord + 2
                                            if buy_inventory_counter > 3:
                                                buy_second_coord += 60
                                                buy_first_coord = 1063
                                                buy_inventory_counter = 0
                                                if scaled_1024:
                                                    buy_first_coord = buy_first_coord * .80
                                                    buy_second_coord = buy_second_coord * .80 + 80

                            # ------------------------------------------------------------------------------------------
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

                            # ------------------------------------------------------------------------------------------
                            # shop click handlers ----------------------------------------------------------------------
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

                                                if scaled_1024:
                                                    player.items.append(
                                                        Item("health potion", "potion", 200, 200,
                                                             resource_urls.health_pot_url_1024,
                                                             (255, 255, 255), "1024"))
                                                if scaled_1280:
                                                    player.items.append(
                                                        Item("health potion", "potion", 200, 200,
                                                             resource_urls.health_pot_url,
                                                             (255, 255, 255), "1280"))
                                                if scaled_1600:
                                                    player.items.append(
                                                        Item("health potion", "potion", 200, 200,
                                                             resource_urls.health_pot_url_1600,
                                                             (255, 255, 255), "1600"))
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

                                                if scaled_1024:
                                                    player.items.append(
                                                        Item("energy potion", "potion", 200, 200,
                                                             resource_urls.energy_pot_url_1024,
                                                             (255, 255, 255), "1024"))
                                                if scaled_1280:
                                                    player.items.append(
                                                        Item("energy potion", "potion", 200, 200,
                                                             resource_urls.energy_pot_url,
                                                             (255, 255, 255), "1280"))
                                                if scaled_1600:
                                                    player.items.append(
                                                        Item("energy potion", "potion", 200, 200,
                                                             resource_urls.energy_pot_url_1600,
                                                             (255, 255, 255), "1600"))
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

                            # handles sell item clicks -----------------------------------------------------------------
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

                            except AttributeError:
                                pass

                    # outside of shop event loop -----------------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
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

                        text_info_draw()

                        # ----------------------------------------------------------------------------------------------
                        if buy_clicked:
                            for window in buy_shop_elements:
                                screen.blit(window.surf, window.rect)

                            # get item from shopkeeper's inventory and draw with buy window
                            for shop_item in shopkeeper_items:
                                screen.blit(shop_item.surf, shop_item.rect)

                # ------------------------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if player is in inn
                if in_inn:

                    # update players current inventory and status
                    status_and_inventory_updates()

                    # inn scenario event loop
                    # --------------------------------------------------------------------------------------------------
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                exit()

                        # function to handle inventory item clicks. apply item message to message box if not empty str.
                        inventory_event = inventory_click_handler()
                        if inventory_event["item message"] != "":
                            info_text_1 = inventory_event["item message"]
                            info_text_2 = ""
                            info_update = True

                        elif event.type == QUIT:
                            exit()

                        # ----------------------------------------------------------------------------------------------
                        inn = pygame.sprite.spritecollideany(player, buildings)
                        if building.name == "inn":
                            # if player has just started inn scenario, clear message box
                            if not encounter_started:
                                info_text_1 = "Click rest button to sleep."
                                info_text_2 = "Sleep regains health and energy."
                                info_text_3 = ""
                                info_text_4 = ""
                                encounter_started = True

                            # get which button player pressed during inn scenario (rest or leave)-----------------------
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

                        # ----------------------------------------------------------------------------------------------
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

                    # outside of inn event loop ------------------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    # if building is an inn in the seldon zone
                    if building.name == "inn":

                        # if player has just rested, fade inn screen back in with alpha value loop
                        if rested:
                            # so this only happens once and not each iteration
                            if not faded_inn_screen:
                                for alpha in range(0, 50):
                                    seldon_district_inn.set_alpha(alpha)
                                    screen.blit(seldon_district_inn, (0, 0))
                                    # flip sleep screen to display -----------------------------------------------------
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

                        # updates players inventory items if item is used in scenario (ex. health pot.)
                        for item in player_items:
                            screen.blit(item.surf, item.rect)

                        text_info_draw()

                        # ----------------------------------------------------------------------------------------------
                        if rest_clicked:
                            if not rested:

                                # set sleep screen to fade in with alpha value loop. Flip each iteration to show
                                for alpha in range(0, 255):
                                    nera_sleep_screen.set_alpha(alpha)
                                    screen.blit(nera_sleep_screen, (0, 0))

                                    # flip sleep screen to display each iteration to show fade -------------------------
                                    pygame.display.flip()

                                # when rest happens, wait after flipping display to allow rest time
                                # 1000 milliseconds = 1 second

                                pygame.time.delay(2500)

                                player.health = 100
                                player.energy = 100
                                rested = True

                # ------------------------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if player is in academia
                if in_academia:

                    # update players current inventory and status
                    status_and_inventory_updates()

                    # inn scenario event loop
                    # --------------------------------------------------------------------------------------------------
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                exit()

                        # function to handle inventory item clicks. apply item message to message box if not empty str.
                        inventory_event = inventory_click_handler()
                        if inventory_event["item message"] != "":
                            info_text_1 = inventory_event["item message"]
                            info_text_2 = ""
                            info_update = True

                        elif event.type == QUIT:
                            exit()

                        # ----------------------------------------------------------------------------------------------
                        academia = pygame.sprite.spritecollideany(player, buildings)
                        if building.name == "academia":
                            # if player has just started inn scenario, clear message box
                            if not encounter_started:
                                info_text_1 = ""
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                                encounter_started = True

                            # get which button player pressed during inn scenario (rest or leave)-----------------------
                            academia_button = inn_event_button(event)
                            if academia_button == "learn":
                                # if player has not yet rested this instance
                                if not learned:
                                    rest_clicked = True
                                    info_text_1 = "You feel well rested."
                                    info_text_2 = ""
                                    info_text_3 = ""
                                    info_text_4 = ""

                        # ----------------------------------------------------------------------------------------------
                        # if player chooses to leave shop, set conditions to allow normal gameplay loop
                        if academia_button == "leave":
                            learn_clicked = False
                            movement_able = True
                            interacted = False
                            info_update = True
                            encounter_started = False
                            in_academia = False
                            in_district_over_world = True

                    # outside of inn event loop ------------------------------------------------------------------------
                    # --------------------------------------------------------------------------------------------------
                    # if building is an inn in the seldon zone
                    if building.name == "academia":
                        screen.blit(seldon_district_academia, (0, 0))
                        screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(learn_button.surf, learn_button.rect)
                        screen.blit(leave_button.surf, leave_button.rect)
                        screen.blit(message_box.surf, message_box.rect)

                        # updates players inventory items if item is used in scenario (ex. health pot.)
                        for item in player_items:
                            screen.blit(item.surf, item.rect)

                        text_info_draw()

                        # ----------------------------------------------------------------------------------------------
                        if learn_clicked:
                            print("learn the things")

                # end of iteration -------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # flip to display --------------------------------------------------------------------------------------
                pygame.display.flip()

                # 60 frames per second game rate -----------------------------------------------------------------------
                clock.tick(60)

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # player has died, show game over and give continue option
            else:
                # draw game over screen and continue button
                screen.blit(game_over_screen, (0, 0))
                screen.blit(continue_button.surf, continue_button.rect)

                # ------------------------------------------------------------------------------------------------------
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
                            # reset interaction, so it doesn't immediately interact again on subsequent sprite
                            # collisions
                            interacted = False
                            # make sure that windows haven't registered a click on reset for whatever reason
                            inventory_clicked = False
                            sell_clicked = False
                            buy_clicked = False
                            encounter_started = False
                            in_battle = False
                            in_district_over_world = True

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
