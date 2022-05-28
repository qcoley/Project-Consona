import random
import time
import pygame
from pygame.locals import *

import click_handlers
import gameplay_functions
import resource_urls
import drawing_functions
import combat_scenario
import character_creation
import shop_scenario

# global variables
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
velocity = 2


# class objects --------------------------------------------------------------------------------------------------------
class PlayerAmuna(pygame.sprite.Sprite):
    def __init__(self, name, race, role, items, p_equipment, current_quests, quest_progress, quest_status,
                 quest_complete, knowledge, skills_mage, skills_fighter, skills_scout, level, experience, health,
                 energy, alive_status, rupees, reputation, current_zone, defense, offense, star_power):
        super(PlayerAmuna, self).__init__()
        self.x_coordinate = 760
        self.y_coordinate = 510
        self.surf = resource_urls.player_no_role_amuna_down_1
        self.rect = self.surf.get_rect(midbottom=(self.x_coordinate, self.y_coordinate))
        self.name = name
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
        self.current_zone = current_zone
        self.defense = defense
        self.offense = offense
        self.star_power = star_power

    # move the player sprite based on input keys
    def update(self, pressed_key, current_zone, walk_timed):
        if player.role == "":  # ---------------------------------------------------------------------------------------
            # w key is pressed to move player up. set y value -
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_amuna_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_amuna_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_amuna_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_amuna_up_4
                self.y_coordinate -= velocity
            # s key is pressed to move player down. set y value +
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_amuna_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_amuna_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_amuna_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_amuna_down_4
                self.y_coordinate += velocity
            # a key is pressed to move player left. set x value -
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_amuna_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_amuna_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_amuna_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_amuna_left_4
                self.x_coordinate -= velocity
            # d key is pressed to move player right. set x value +
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_amuna_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_amuna_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_amuna_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_amuna_right_4
                self.x_coordinate += velocity
        if player.role == "mage":  # -----------------------------------------------------------------------------------
            # w key is pressed to move player up. set y value -
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_amuna_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_amuna_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_amuna_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_amuna_up_4
                self.y_coordinate -= velocity
            # s key is pressed to move player down. set y value +
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_amuna_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_amuna_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_amuna_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_amuna_down_4
                self.y_coordinate += velocity
            # a key is pressed to move player left. set x value -
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_amuna_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_amuna_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_amuna_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_amuna_left_4
                self.x_coordinate -= velocity
            # d key is pressed to move player right. set x value +
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_amuna_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_amuna_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_amuna_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_amuna_right_4
                self.x_coordinate += velocity
        if player.role == "fighter":  # --------------------------------------------------------------------------------
            # w key is pressed to move player up. set y value -
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_amuna_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_amuna_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_amuna_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_amuna_up_4
                self.y_coordinate -= velocity
            # s key is pressed to move player down. set y value +
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_amuna_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_amuna_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_amuna_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_amuna_down_4
                self.y_coordinate += velocity
            # a key is pressed to move player left. set x value -
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_amuna_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_amuna_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_amuna_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_amuna_left_4
                self.x_coordinate -= velocity
            # d key is pressed to move player right. set x value +
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_amuna_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_amuna_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_amuna_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_amuna_right_4
                self.x_coordinate += velocity
        if player.role == "scout":  # ----------------------------------------------------------------------------------
            # w key is pressed to move player up. set y value -
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_amuna_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_amuna_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_amuna_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_amuna_up_4
                self.y_coordinate -= velocity
            # s key is pressed to move player down. set y value +
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_amuna_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_amuna_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_amuna_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_amuna_down_4
                self.y_coordinate += velocity
            # a key is pressed to move player left. set x value -
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_amuna_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_amuna_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_amuna_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_amuna_left_4
                self.x_coordinate -= velocity
            # d key is pressed to move player right. set x value +
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_amuna_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_amuna_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_amuna_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_amuna_right_4
                self.x_coordinate += velocity
        # keep player on the screen, boundaries vary depending on current zone
        if current_zone == "nascent":
            if self.x_coordinate < 340:
                self.x_coordinate = 340
            elif self.x_coordinate > SCREEN_WIDTH - 325:
                self.x_coordinate = SCREEN_WIDTH - 325
            if self.y_coordinate <= 60:
                self.y_coordinate = 60
            elif self.y_coordinate >= SCREEN_HEIGHT - 50:
                self.y_coordinate = SCREEN_HEIGHT - 50
            # for wall/gate collision in nascent grove/starting area
            elif 315 >= self.y_coordinate >= 300:
                self.y_coordinate = 315
            elif 300 >= self.y_coordinate >= 230:
                self.y_coordinate = 230
        if current_zone == "seldon":
            if self.x_coordinate < 15:
                self.x_coordinate = 15
            elif self.x_coordinate > SCREEN_WIDTH - 355:
                self.x_coordinate = SCREEN_WIDTH - 355
            if self.y_coordinate <= 115:
                self.y_coordinate = 115
            elif self.y_coordinate >= SCREEN_HEIGHT - 5:
                self.y_coordinate = SCREEN_HEIGHT - 5
        if current_zone == "stardust":
            if self.x_coordinate < 225:
                self.x_coordinate = 225
            elif self.x_coordinate > SCREEN_WIDTH - 325:
                self.x_coordinate = SCREEN_WIDTH - 325
            if self.y_coordinate <= 80:
                self.y_coordinate = 80
            elif self.y_coordinate >= SCREEN_HEIGHT - 80:
                self.y_coordinate = SCREEN_HEIGHT - 80
            # for stardust outpost collision, bigger building
            elif 360 >= self.y_coordinate >= 300 and 641 >= self.x_coordinate >= 409:
                self.y_coordinate = 360
            elif 300 >= self.y_coordinate >= 230 and 641 >= self.x_coordinate >= 409:
                self.y_coordinate = 230
            elif 645 >= self.x_coordinate >= 500 and 358 >= self.y_coordinate >= 232:
                self.x_coordinate = 645
            elif 500 >= self.x_coordinate >= 395 and 358 >= self.y_coordinate >= 232:
                self.x_coordinate = 395
        if current_zone == "korlok":
            if self.x_coordinate < 25:
                self.x_coordinate = 25
            elif self.x_coordinate > SCREEN_WIDTH - 355:
                self.x_coordinate = SCREEN_WIDTH - 355
            if self.y_coordinate <= 115:
                self.y_coordinate = 115
            elif self.y_coordinate >= SCREEN_HEIGHT - 5:
                self.y_coordinate = SCREEN_HEIGHT - 5
        if current_zone == "seldon":
            collided = pygame.sprite.spritecollideany(player, environments, pygame.sprite.collide_rect_ratio(0.50))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        # update player position
        self.rect.midbottom = (self.x_coordinate, self.y_coordinate)


class PlayerNuldar(pygame.sprite.Sprite):
    def __init__(self, name, race, role, items, p_equipment, current_quests, quest_progress, quest_status,
                 quest_complete, knowledge, skills_mage, skills_fighter, skills_scout, level, experience, health,
                 energy, alive_status, rupees, reputation, current_zone, defense, offense, star_power):
        super(PlayerNuldar, self).__init__()
        self.x_coordinate = 760
        self.y_coordinate = 510
        self.surf = resource_urls.player_no_role_amuna_down_1
        self.rect = self.surf.get_rect(midbottom=(self.x_coordinate, self.y_coordinate))
        self.name = name
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
        self.current_zone = current_zone
        self.defense = defense
        self.offense = offense
        self.star_power = star_power

    def update(self, pressed_key, current_zone, walk_timed):
        if player.role == "":  # ---------------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_nuldar_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_nuldar_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_nuldar_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_nuldar_up_4
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_nuldar_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_nuldar_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_nuldar_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_nuldar_down_4
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_nuldar_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_nuldar_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_nuldar_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_nuldar_left_4
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_nuldar_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_nuldar_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_nuldar_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_nuldar_right_4
                self.x_coordinate += velocity
        if player.role == "mage":  # -----------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_nuldar_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_nuldar_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_nuldar_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_nuldar_up_4
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_nuldar_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_nuldar_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_nuldar_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_nuldar_down_4
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_nuldar_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_nuldar_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_nuldar_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_nuldar_left_4
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_nuldar_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_nuldar_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_nuldar_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_nuldar_right_4
                self.x_coordinate += velocity
        if player.role == "fighter":  # --------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_nuldar_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_nuldar_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_nuldar_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_nuldar_up_4
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_nuldar_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_nuldar_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_nuldar_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_nuldar_down_4
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_nuldar_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_nuldar_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_nuldar_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_nuldar_left_4
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_nuldar_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_nuldar_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_nuldar_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_nuldar_right_4
                self.x_coordinate += velocity
        if player.role == "scout":  # ----------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_nuldar_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_nuldar_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_nuldar_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_nuldar_up_4
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_nuldar_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_nuldar_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_nuldar_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_nuldar_down_4
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_nuldar_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_nuldar_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_nuldar_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_nuldar_left_4
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_nuldar_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_nuldar_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_nuldar_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_nuldar_right_4
                self.x_coordinate += velocity
        if current_zone == "nascent":
            if self.x_coordinate < 340:
                self.x_coordinate = 340
            elif self.x_coordinate > SCREEN_WIDTH - 325:
                self.x_coordinate = SCREEN_WIDTH - 325
            if self.y_coordinate <= 60:
                self.y_coordinate = 60
            elif self.y_coordinate >= SCREEN_HEIGHT - 50:
                self.y_coordinate = SCREEN_HEIGHT - 50
            elif 315 >= self.y_coordinate >= 300:
                self.y_coordinate = 315
            elif 300 >= self.y_coordinate >= 230:
                self.y_coordinate = 230
        if current_zone == "seldon":
            if self.x_coordinate < 15:
                self.x_coordinate = 15
            elif self.x_coordinate > SCREEN_WIDTH - 355:
                self.x_coordinate = SCREEN_WIDTH - 355
            if self.y_coordinate <= 115:
                self.y_coordinate = 115
            elif self.y_coordinate >= SCREEN_HEIGHT - 5:
                self.y_coordinate = SCREEN_HEIGHT - 5
        if current_zone == "stardust":
            if self.x_coordinate < 225:
                self.x_coordinate = 225
            elif self.x_coordinate > SCREEN_WIDTH - 325:
                self.x_coordinate = SCREEN_WIDTH - 325
            if self.y_coordinate <= 80:
                self.y_coordinate = 80
            elif self.y_coordinate >= SCREEN_HEIGHT - 80:
                self.y_coordinate = SCREEN_HEIGHT - 80
            elif 360 >= self.y_coordinate >= 300 and 641 >= self.x_coordinate >= 409:
                self.y_coordinate = 360
            elif 300 >= self.y_coordinate >= 230 and 641 >= self.x_coordinate >= 409:
                self.y_coordinate = 230
            elif 645 >= self.x_coordinate >= 500 and 358 >= self.y_coordinate >= 232:
                self.x_coordinate = 645
            elif 500 >= self.x_coordinate >= 395 and 358 >= self.y_coordinate >= 232:
                self.x_coordinate = 395
        if current_zone == "korlok":
            if self.x_coordinate < 25:
                self.x_coordinate = 25
            elif self.x_coordinate > SCREEN_WIDTH - 355:
                self.x_coordinate = SCREEN_WIDTH - 355
            if self.y_coordinate <= 115:
                self.y_coordinate = 115
            elif self.y_coordinate >= SCREEN_HEIGHT - 5:
                self.y_coordinate = SCREEN_HEIGHT - 5
        if current_zone == "seldon":
            collided = pygame.sprite.spritecollideany(player, environments, pygame.sprite.collide_rect_ratio(0.50))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        self.rect.midbottom = (self.x_coordinate, self.y_coordinate)


class PlayerSorae(pygame.sprite.Sprite):
    def __init__(self, name, race, role, items, p_equipment, current_quests, quest_progress, quest_status,
                 quest_complete, knowledge, skills_mage, skills_fighter, skills_scout, level, experience, health,
                 energy, alive_status, rupees, reputation, current_zone, defense, offense, star_power):
        super(PlayerSorae, self).__init__()
        self.x_coordinate = 760
        self.y_coordinate = 510
        self.surf = resource_urls.player_no_role_amuna_down_1
        self.rect = self.surf.get_rect(midbottom=(self.x_coordinate, self.y_coordinate))
        self.name = name
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
        self.current_zone = current_zone
        self.defense = defense
        self.offense = offense
        self.star_power = star_power

    def update(self, pressed_key, current_zone, walk_timed):
        if player.role == "":  # ---------------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_sorae_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_sorae_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_sorae_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_sorae_up_4
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_sorae_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_sorae_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_sorae_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_sorae_down_4
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_sorae_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_sorae_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_sorae_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_sorae_left_4
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_no_role_sorae_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_no_role_sorae_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_no_role_sorae_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_no_role_sorae_right_4
                self.x_coordinate += velocity
        if player.role == "mage":  # -----------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_sorae_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_sorae_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_sorae_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_sorae_up_4
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_sorae_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_sorae_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_sorae_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_sorae_down_4
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_sorae_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_sorae_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_sorae_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_sorae_left_4
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_mage_sorae_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_mage_sorae_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_mage_sorae_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_mage_sorae_right_4
                self.x_coordinate += velocity
        if player.role == "fighter":  # --------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_sorae_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_sorae_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_sorae_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_sorae_up_4
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_sorae_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_sorae_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_sorae_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_sorae_down_4
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_sorae_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_sorae_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_sorae_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_sorae_left_4
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_fighter_sorae_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_fighter_sorae_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_fighter_sorae_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_fighter_sorae_right_4
                self.x_coordinate += velocity
        if player.role == "scout":  # ----------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_sorae_up_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_sorae_up_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_sorae_up_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_sorae_up_4
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_sorae_down_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_sorae_down_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_sorae_down_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_sorae_down_4
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_sorae_left_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_sorae_left_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_sorae_left_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_sorae_left_4
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = resource_urls.player_scout_sorae_right_1
                if walk_timed > 0.2:
                    self.surf = resource_urls.player_scout_sorae_right_2
                if walk_timed > 0.4:
                    self.surf = resource_urls.player_scout_sorae_right_3
                if walk_timed > 0.6:
                    self.surf = resource_urls.player_scout_sorae_right_4
                self.x_coordinate += velocity
        if current_zone == "nascent":
            if self.x_coordinate < 340:
                self.x_coordinate = 340
            elif self.x_coordinate > SCREEN_WIDTH - 325:
                self.x_coordinate = SCREEN_WIDTH - 325
            if self.y_coordinate <= 60:
                self.y_coordinate = 60
            elif self.y_coordinate >= SCREEN_HEIGHT - 50:
                self.y_coordinate = SCREEN_HEIGHT - 50
            elif 315 >= self.y_coordinate >= 300:
                self.y_coordinate = 315
            elif 300 >= self.y_coordinate >= 230:
                self.y_coordinate = 230
        if current_zone == "seldon":
            if self.x_coordinate < 15:
                self.x_coordinate = 15
            elif self.x_coordinate > SCREEN_WIDTH - 355:
                self.x_coordinate = SCREEN_WIDTH - 355
            if self.y_coordinate <= 115:
                self.y_coordinate = 115
            elif self.y_coordinate >= SCREEN_HEIGHT - 5:
                self.y_coordinate = SCREEN_HEIGHT - 5
        if current_zone == "stardust":
            if self.x_coordinate < 225:
                self.x_coordinate = 225
            elif self.x_coordinate > SCREEN_WIDTH - 325:
                self.x_coordinate = SCREEN_WIDTH - 325
            if self.y_coordinate <= 80:
                self.y_coordinate = 80
            elif self.y_coordinate >= SCREEN_HEIGHT - 80:
                self.y_coordinate = SCREEN_HEIGHT - 80
            elif 360 >= self.y_coordinate >= 300 and 641 >= self.x_coordinate >= 409:
                self.y_coordinate = 360
            elif 300 >= self.y_coordinate >= 230 and 641 >= self.x_coordinate >= 409:
                self.y_coordinate = 230
            elif 645 >= self.x_coordinate >= 500 and 358 >= self.y_coordinate >= 232:
                self.x_coordinate = 645
            elif 500 >= self.x_coordinate >= 395 and 358 >= self.y_coordinate >= 232:
                self.x_coordinate = 395
        if current_zone == "korlok":
            if self.x_coordinate < 25:
                self.x_coordinate = 25
            elif self.x_coordinate > SCREEN_WIDTH - 355:
                self.x_coordinate = SCREEN_WIDTH - 355
            if self.y_coordinate <= 115:
                self.y_coordinate = 115
            elif self.y_coordinate >= SCREEN_HEIGHT - 5:
                self.y_coordinate = SCREEN_HEIGHT - 5
        if current_zone == "seldon":
            collided = pygame.sprite.spritecollideany(player, environments, pygame.sprite.collide_rect_ratio(0.50))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        self.rect.midbottom = (self.x_coordinate, self.y_coordinate)


# any in game npc. can have quests and also gifts to player upon initial interaction
class NPC(pygame.sprite.Sprite):
    def __init__(self, name, race, dialog, quest_to_give, quest_description, x_coordinate, y_coordinate,
                 alive_status, quest_complete, items, gift, image):
        super(NPC, self).__init__()
        self.name = name
        self.race = race
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


# shopkeeper class for assigning attributed items in shop
class Shopkeeper(pygame.sprite.Sprite):
    def __init__(self, name, race, items):
        super(Shopkeeper, self).__init__()
        self.name = name
        self.race = race
        self.items = items


# enemy class used for any enemy like snakes, ghouls etc
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

    # updates enemy image
    def update_image(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))

    # updates enemy map position
    def update_position(self, ranges_x, ranges_y, direction_x, direction_y):
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


# tree or tree-like sprites. collision checks
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


# building sprite. collision checks
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


# any UI element like buttons, bars, player status etc
class UiElement(pygame.sprite.Sprite):
    def __init__(self, name, x_coordinate, y_coordinate, image):
        super(UiElement, self).__init__()
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


# inventory class used for shop
class Inventory(pygame.sprite.Sprite):
    def __init__(self, name, contains, x_coordinate, y_coordinate, image):
        super(Inventory, self).__init__()
        self.name = name
        self.contains = contains
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# pop up notifications
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


# representation of character for battle screen or npc interaction
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


# any item or equipment
class Item(pygame.sprite.Sprite):
    def __init__(self, name, types, x_coordinate, y_coordinate, image):
        super(Item, self).__init__()
        self.name = name
        self.type = types
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# ----------------------------------------------------------------------------------------------------------------------
# function to respawn enemies if they are less than a specified amount active in game. spawns with random coord. and lvl
def enemy_respawn():
    snake_counter = 0
    ghoul_counter = 0
    # generate random coordinates and level for new enemy to spawn within boundaries and level range
    # if not scaled, coordinates set to default boundaries
    random_snake_x = random.randrange(150, 300)
    random_snake_y = random.randrange(150, 300)
    random_snake_level = random.randrange(1, 3)
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
        new_snake = Enemy("snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y, True,
                          Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_img), resource_urls.snake,
                          UiElement("snake hp bar", 700, 90, resource_urls.hp_100))
        snakes.add(new_snake)
        enemies.add(new_snake)
        most_sprites.add(new_snake)

    # if there are less than 3 ghouls in game, create another ghoul with random level and coordinates. add to groups
    if ghoul_counter < 3:
        new_ghoul = Enemy("ghoul", "ghoul", 100, 100, random_ghoul_level, random_ghoul_x, random_ghoul_y, True,
                          Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_img), resource_urls.ghoul,
                          UiElement("ghoul hp bar", 700, 90, resource_urls.hp_100))
        ghouls.add(new_ghoul)
        enemies.add(new_ghoul)
        most_sprites.add(new_ghoul)


# hearth button is clicked, sets fade transition for hearth screen and then back to district bg
def hearthstone_animation():
    resource_urls.screen.fill((0, 0, 0))
    for alphas in range(0, 200):
        seldon_hearth_screen.set_alpha(alphas)
        resource_urls.screen.blit(seldon_hearth_screen, (0, 0))
        pygame.display.flip()
    resource_urls.screen.fill((0, 0, 0))
    for alphas in range(0, 50):
        seldon_district_bg.set_alpha(alphas)
        resource_urls.screen.blit(seldon_district_bg, (0, 0))
        pygame.display.flip()
    seldon_district_bg.set_alpha(255)
    resource_urls.screen.blit(seldon_district_bg, (0, 0))
    pygame.display.flip()


# ----------------------------------------------------------------------------------------------------------------------
# pygame.mixer.init()
# initialize game, set clock for frame rate, set screen size

# background textures --------------------------------------------------------------------------------------------------
nascent_grove_bg = resource_urls.nascent_grove_screen
seldon_district_bg = resource_urls.seldon_bg_screen
seldon_district_battle = resource_urls.seldon_battle_screen
seldon_district_shop = resource_urls.seldon_shop_screen
seldon_district_inn = resource_urls.seldon_inn_screen
seldon_district_academia = resource_urls.seldon_academia_screen
stardust_outpost_bg = resource_urls.stardust_outpost_screen
seldon_hearth_screen = resource_urls.seldon_hearth_screen
game_over_screen = resource_urls.game_over_screen
start_screen = resource_urls.start_screen
nera_sleep_screen = resource_urls.nera_sleep_screen
korlok_district_bg = resource_urls.korlok_bg_screen
amuna_character_screen = resource_urls.a_char_screen
nuldar_character_screen = resource_urls.n_char_screen
sorae_character_screen = resource_urls.s_char_screen

# display notifications ------------------------------------------------------------------------------------------------
knowledge_academia = Notification("knowledge academia notification", False, 510, 365, resource_urls.knowledge_popup)
rest_recover = Notification("rest recover", False, 510, 365, resource_urls.health_popup)
shop_gear = Notification("shop gear", False, 510, 365, resource_urls.gear_popup)
save_check = Notification("save check", False, 510, 365, resource_urls.save_popup)
save_absent = Notification("save absent", False, 640, 574, resource_urls.save_not_found)
# inventory items
health_potion = Item("health potion", "potion", 200, 200, resource_urls.health_pot_img)
energy_potion = Item("energy potion", "potion", 200, 200, resource_urls.energy_pot_img)
shiny_rock = Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_img)
bone_dust = Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_img)
# starter equipment
basic_staff = Item("basic staff", "mage", 200, 200, resource_urls.basic_staff_img)
basic_sword = Item("basic sword", "fighter", 200, 200, resource_urls.basic_sword_img)
basic_bow = Item("basic bow", "scout", 200, 200, resource_urls.basic_bow_img)
basic_robes = Item("basic robes", "mage", 200, 200, resource_urls.basic_robes_img)
basic_armor = Item("basic armor", "fighter", 200, 200, resource_urls.basic_armor_img)
basic_tunic = Item("basic tunic", "scout", 200, 200, resource_urls.basic_tunic_img)
# character selection
amuna_character = UiElement("amuna character", 640, 360, resource_urls.amuna_character_img)
nuldar_character = UiElement("nuldar character", 640, 360, resource_urls.nuldar_character_img)
sorae_character = UiElement("sorae character", 640, 360, resource_urls.sorae_character_img)

# default player
player = PlayerAmuna("stan", "amuna", "",  # name, race, role
                     [health_potion, energy_potion],  # inventory
                     {"weapon": "", "chest": ""},  # equipment ('type', 'name')
                     {"sneaky snakes": "Speak to Garan to start this quest.",
                      "village repairs": "Speak to Maurelle to start this quest.",
                      "where's nede?": "Speak to Celeste to start this quest",
                      "ghouled again": "Speak to the gate Guard to start this quest.", "": ""},
                     {"sneaky snakes": 0, "village repairs": 0, "where's nede?": 0, "ghouled again": 0},
                     {"sneaky snakes": False, "village repairs": False, "where's nede?": False, "ghouled again": False},
                     {"sneaky snakes": False, "village repairs": False, "where's nede?": False, "ghouled again": False},
                     {"mage": 0, "fighter": 0, "scout": 0},  # role knowledge ('role', 'amount')
                     {"skill 2": "", "skill 3": "", "skill 4": ""},  # mage skills
                     {"skill 2": "", "skill 3": "", "skill 4": ""},  # fighter skills
                     {"skill 2": "", "skill 3": "", "skill 4": ""},  # scout skills
                     1, 0, 100, 100,  # lvl, exp, health, energy
                     True, 0, {"amuna": 0, "nuldar": 0, "sorae": 0},  # alive, rupees, reputation
                     "", 0, 0, 0)  # zone, defence, offense, image

# npcs: name, gender, race, role, dialog, quest, quest_description, x_coordinate, y_coordinate
#                  alive_status, quest_complete, items, gift, image
npc_garan = NPC("garan", "amuna", "It's dangerous to go alone.", "stupid snakes", "", 210, 432,
                True, False, ["Items"], False, resource_urls.garan_down)
npc_maurelle = NPC("maurelle", "amuna", "We need help!", "village repairs", "", 745, 615,
                   True, False, ["Items"], False, resource_urls.maurelle_down)
npc_celeste = NPC("celeste", "sorae", "My pet!", "where's nede?", "", 760, 415,
                  True, False, ["Items"], False, resource_urls.celeste_down)
npc_torune = NPC("torune", "nuldar", "Onur-oh.", "ghouled again", "", 430, 120,
                 True, False, ["Items"], False, resource_urls.torune_down)
npc_amuna_shopkeeper = Shopkeeper("amuna shopkeeper", "amuna", [
    Item("health potion", "potion", 200, 200, resource_urls.health_pot_img),
    Item("energy potion", "potion", 200, 200, resource_urls.energy_pot_img),
    Item("basic staff", "mage", 200, 200, resource_urls.basic_staff_img),
    Item("basic sword", "fighter", 200, 200, resource_urls.basic_sword_img),
    Item("basic bow", "scout", 200, 200, resource_urls.basic_bow_img),
    Item("basic robes", "mage", 200, 200, resource_urls.basic_robes_img),
    Item("basic armor", "fighter", 200, 200, resource_urls.basic_armor_img),
    Item("basic tunic", "scout", 200, 200, resource_urls.basic_tunic_img)])
npc_garan_interaction = UiElement("garan interaction", 647, 360, resource_urls.garan_interaction)
npc_maurelle_interaction = UiElement("maurelle interaction", 641, 360, resource_urls.maurelle_interaction)
npc_celeste_interaction = UiElement("celeste interaction", 639, 360, resource_urls.celeste_interaction)
npc_torune_interaction = UiElement("torune interaction", 635, 360, resource_urls.torune_interaction)

# enemies: kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image, color, health bar
snake_1 = Enemy("snake", "snake", 100, 100, 1, 100, 130, True,
                Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_img),
                resource_urls.snake, UiElement("snake hp bar", 700, 90, resource_urls.hp_100))
snake_2 = Enemy("snake", "snake", 100, 100, 2, 285, 150, True,
                Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_img),
                resource_urls.snake, UiElement("snake hp bar", 700, 90, resource_urls.hp_100))
snake_3 = Enemy("snake", "snake", 100, 100, 1, 100, 230, True,
                Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_img),
                resource_urls.snake, UiElement("snake hp bar", 700, 90, resource_urls.hp_100))
snake_4 = Enemy("snake", "snake", 100, 100, 2, 285, 250, True,
                Item("shiny rock", "rock", 200, 200, resource_urls.shiny_rock_img),
                resource_urls.snake, UiElement("snake hp bar", 700, 90, resource_urls.hp_100))
ghoul_low_1 = Enemy("ghoul", "ghoul", 100, 100, 4, 665, 180, True,
                    Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_img),
                    resource_urls.ghoul, UiElement("ghoul hp bar", 700, 90, resource_urls.hp_100))
ghoul_low_2 = Enemy("ghoul", "ghoul", 100, 100, 5, 800, 130, True,
                    Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_img),
                    resource_urls.ghoul, UiElement("ghoul hp bar", 700, 90, resource_urls.hp_100))
ghoul_low_3 = Enemy("ghoul", "ghoul", 100, 100, 3, 760, 240, True,
                    Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_img),
                    resource_urls.ghoul, UiElement("ghoul hp bar", 700, 90, resource_urls.hp_100))
ghoul_low_4 = Enemy("ghoul", "ghoul", 100, 100, 4, 890, 205, True,
                    Item("bone dust", "dust", 200, 200, resource_urls.bone_dust_img),
                    resource_urls.ghoul, UiElement("ghoul hp bar", 700, 90, resource_urls.hp_100))

pine_tree_1 = Tree("tree", "pine tree", 80, 445, False, resource_urls.pine_tree)
pine_tree_2 = Tree("tree", "pine tree", 260, 590, False, resource_urls.pine_tree)
pine_tree_3 = Tree("tree", "pine tree", 340, 400, False, resource_urls.pine_tree)
seldon_inn = Building("inn", "seldon inn", 635, 600, resource_urls.amuna_inn_building)
seldon_shop = Building("shop", "seldon shop", 665, 400, resource_urls.amuna_shop_building)
seldon_academia = Building("academia", "seldon academia", 875, 440, resource_urls.amuna_academia_building)
seldon_hearth = Building("hearth", "seldon hearth", 860, 595, resource_urls.hearth_stone)
rohir_gate = Building("gate", "rohir gate", 525, 50, resource_urls.rohir_gate)
nascent_gate = Building("gate", "nascent gate", 418, 262, resource_urls.nascent_gate_closed)

location_overlay = UiElement("location overlay", 915, 28, resource_urls.location_overlay)
character_select_overlay = UiElement("character select overlay", 640, 365, resource_urls.char_select_overlay)
amuna_select_overlay = UiElement("amuna select overlay", 1140, 305, resource_urls.amuna_overlay_img)
nuldar_select_overlay = UiElement("nuldar select overlay", 1140, 305, resource_urls.nuldar_overlay_img)
sorae_select_overlay = UiElement("sorae select overlay", 1140, 305, resource_urls.sorae_overlay_img)
name_input = UiElement("name input", 640, 585, resource_urls.name_input_img)

character_button = UiElement("character button", 860, 680, resource_urls.character_button_img)
journal_button = UiElement("journal button", 970, 680, resource_urls.journal_button_img)
new_game_button = UiElement("new game button", 640, 342, resource_urls.new_game_img)
continue_button = UiElement("continue button", 640, 425, resource_urls.continue_img)
amuna_button = UiElement("amuna button", 100, 255, resource_urls.amuna_button_img)
nuldar_button = UiElement("nuldar button", 100, 350, resource_urls.nuldar_button_img)
sorae_button = UiElement("sorae button", 100, 445, resource_urls.sorae_button_img)
start_button = UiElement("start button", 640, 660, resource_urls.start_button)
lets_go_button = UiElement("lets go button", 625, 575, resource_urls.lets_go_button)
buy_button = UiElement("buy button", 860, 680, resource_urls.buy_button_img)
leave_button = UiElement("leave button", 970, 680, resource_urls.leave_button_img)
rest_button = UiElement("rest button", 860, 680, resource_urls.rest_button_img)
mage_learn_button = UiElement("mage learn button", 650, 250, resource_urls.learn_button)
fighter_learn_button = UiElement("fighter learn button", 420, 330, resource_urls.learn_button)
scout_learn_button = UiElement("scout learn button", 560, 410, resource_urls.learn_button)
barrier_learn_button = UiElement("barrier learn button", 505, 300, resource_urls.skill_learn_button)
hard_strike_learn_button = UiElement("hard strike learn button", 505, 300, resource_urls.skill_learn_button)
sharp_sense_learn_button = UiElement("sharp sense learn button", 505, 300, resource_urls.skill_learn_button)
close_button = UiElement("close button", 975, 135, resource_urls.close_button)
quest_button = UiElement("quest button", 860, 680, resource_urls.quest_button_img)
accept_button = UiElement("accept button", 340, 670, resource_urls.accept_button_img)
decline_button = UiElement("decline button", 450, 670, resource_urls.decline_button_img)
hearth_button = UiElement("hearth button", 860, 60, resource_urls.hearth_button_img)
save_button = UiElement("save button", 970, 60, resource_urls.save_button_img)
yes_button = UiElement("yes button", 450, 394, resource_urls.yes_button_img)
no_button = UiElement("no button", 564, 394, resource_urls.no_button_img)
item_info_button = UiElement("item info button", 1153, 345, resource_urls.use_button_img)
mage_select_button = UiElement("role select overlay", 296, 566, resource_urls.mage_select_button_img)
fighter_select_button = UiElement("role select overlay", 550, 566, resource_urls.fighter_select_button_img)
scout_select_button = UiElement("role select overlay", 804, 566, resource_urls.scout_select_button_img)

no_role_attack_button = UiElement("no role attack button", 750, 642, resource_urls.no_role_attack_button_img)
mage_attack_button = UiElement("mage attack button", 750, 642, resource_urls.mage_attack_button_img)
fighter_attack_button = UiElement("fighter attack button", 750, 642, resource_urls.fighter_attack_button_img)
scout_attack_button = UiElement("scout attack button", 750, 642, resource_urls.scout_attack_button_img)
barrier_button = UiElement("barrier button", 820, 642, resource_urls.barrier_button_img)
hard_strike_button = UiElement("hard strike button", 820, 642, resource_urls.strike_button_img)
sharp_sense_button = UiElement("sharp sense button", 820, 642, resource_urls.sense_button_img)

skill_bar = UiElement("skill bar", 855, 636, resource_urls.skill_bar)
enemy_status = UiElement("enemy status", 855, 687, resource_urls.enemy_status)
hp_bar = UiElement("health bar", 165, 25, resource_urls.hp_100)
en_bar = UiElement("energy bar", 165, 45, resource_urls.en_100)
xp_bar = UiElement("xp bar", 165, 65, resource_urls.xp_100)
journal = UiElement("journal", 770, 380, resource_urls.journal_window_img)
level_up_win = UiElement("level up window", 165, 132, resource_urls.level_up)
character_sheet = UiElement("character sheet", 770, 380, resource_urls.character_window_img)
mage_book = UiElement("mage book", 670, 375, resource_urls.mage_book_img)
fighter_book = UiElement("fighter book", 670, 375, resource_urls.fighter_book_img)
scout_book = UiElement("scout book", 670, 375, resource_urls.scout_book_img)
quest_logs_1 = Item("pine logs", "quest", 60, 540, resource_urls.quest_logs)
quest_logs_2 = Item("pine logs", "quest", 315, 560, resource_urls.quest_logs)
quest_logs_3 = Item("pine logs", "quest", 415, 435, resource_urls.quest_logs)
quest_logs_4 = Item("pine logs", "quest", 100, 540, resource_urls.quest_logs)
nede = Item("nede", "quest", 450, 450, resource_urls.nede_left)
npc_name_plate = UiElement("npc name plate", 638, 192, resource_urls.npc_name_plate)
buy_inventory = Inventory("buy inventory", [], 900, 500, resource_urls.buy_inventory)
knowledge_window = UiElement("knowledge window", 635, 680, resource_urls.knowledge_window)
garan_quest_window = UiElement("garan quest window", 262, 442, resource_urls.garan_quest)
maurelle_quest_window = UiElement("maurelle quest window", 262, 442, resource_urls.maurelle_quest)
celeste_quest_window = UiElement("maurelle quest window", 262, 442, resource_urls.celeste_quest)
torune_quest_window = UiElement("torune quest window", 262, 442, resource_urls.torune_quest)
message_box = UiElement("message box", 173, 650, resource_urls.message_box)
bar_backdrop = UiElement("bar backdrop", 165, 45, resource_urls.bar_backdrop)
enemy_status_bar_back = UiElement("enemy bar backdrop", 700, 90, resource_urls.enemy_bar_backdrop)
quest_star_garan = UiElement("quest star garan", 210, 390, resource_urls.quest_start_star)
quest_star_maurelle = UiElement("quest star maurelle", 744, 575, resource_urls.quest_start_star)
quest_star_celeste = UiElement("quest star maurelle", 760, 373, resource_urls.quest_start_star)
quest_star_torune = UiElement("quest star torune", 430, 75, resource_urls.quest_start_star)
player_battle_sprite = BattleCharacter("stan battle", 320, 460, resource_urls.player_no_role_amuna_battle)
snake_battle_sprite = BattleCharacter("snake battle", 715, 250, resource_urls.snake_battle)
ghoul_battle_sprite = BattleCharacter("ghoul battle", 698, 280, resource_urls.ghoul_battle)
nascent_gate_popup = UiElement("nascent gate popup", 418, 200, resource_urls.nascent_gate_popup)
sell_items = UiElement("sell items", 1155, 270, resource_urls.s_health_pot_img)
info_items = UiElement("info items", 1155, 270, resource_urls.info_health_pot_img)
buy_items = UiElement("buy items", 900, 230, resource_urls.b_health_pot_img)
star_power_meter = UiElement("star power", 1210, 360, resource_urls.star_00)
role_select_overlay = UiElement("role select overlay", 550, 369, resource_urls.role_selection_overlay)
dealt_damage_overlay = UiElement("dealt damage overlay", 850, 225, resource_urls.dealt_damage_img)
received_damage_overlay = UiElement("recieved damage overlay", 125, 275, resource_urls.received_damage_img)
interaction_popup = UiElement("interaction popup", 125, 275, resource_urls.popup_interaction)
loot_popup = UiElement("loot popup", 171, 528, resource_urls.popup_loot)

font = pygame.font.SysFont('freesansbold.ttf', 22, bold=False, italic=False)
level_up_font = pygame.font.SysFont('freesansbold.ttf', 28, bold=True, italic=False)
name_input_font = pygame.font.SysFont('freesansbold.ttf', 32, bold=True, italic=False)

quest_items = pygame.sprite.Group()
npcs = pygame.sprite.Group()
enemies = pygame.sprite.Group()
trees = pygame.sprite.Group()
buildings = pygame.sprite.Group()
environments = pygame.sprite.Group()
user_interface = pygame.sprite.Group()
enemy_hp_bars = pygame.sprite.Group()
most_sprites = pygame.sprite.Group()
non_sprite_sheets = pygame.sprite.Group()
snakes = pygame.sprite.Group()
ghouls = pygame.sprite.Group()

snakes.add(snake_1, snake_2, snake_3, snake_4)
ghouls.add(ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)
npcs.add(npc_garan, npc_maurelle, npc_celeste, npc_torune)
enemies.add(snake_1, snake_2, snake_3, snake_4, ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)
trees.add(pine_tree_1, pine_tree_2, pine_tree_3)
buildings.add(seldon_inn, seldon_shop, seldon_academia)
environments.add(trees, buildings)
quest_items.add(quest_logs_1, quest_logs_2, quest_logs_3, quest_logs_4, rohir_gate)
most_sprites.add(npcs, trees, buildings, quest_items, enemies, seldon_hearth, rohir_gate)
user_interface.add(rest_button, buy_button, leave_button, character_button, journal_button, save_button, hearth_button,
                   message_box, location_overlay, star_power_meter)

# code related to sound effects that will be used later
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
amuna_race_selected = True
nuldar_race_selected = False
sorae_race_selected = False
name_input_selected = False
in_over_world = True
in_battle = False
in_shop = False
in_inn = False
in_academia = False
in_npc_interaction = False
interacted = False
movement_able = True
combat_cooldown = False
combat_happened = False
buy_clicked = False
rest_clicked = False
mage_learn_clicked = False
fighter_learn_clicked = False
scout_learn_clicked = False
character_button_clicked = False
journal_button_clicked = False
encounter_started = False
item_bought = False
rested = False
barrier_learned = False
hard_strike_learned = False
sharp_sense_learned = False
barrier_active = False
sharp_sense_active = False
faded_inn_screen = False
hard_strike = False
quest_clicked = False
knowledge_academia_show = False
knowledge_window_clicked = False
rest_recover_show = False
rest_window_clicked = False
saved = False
entered = False
mage_select = False
fighter_select = False
scout_select = False
loot_updated = True

buy_shop_elements = []
shopkeeper_items = []
skill_learn_items = []
books = []
knowledge_academia_window = []
rest_recover_window = []
save_check_window = []
save_data_window = []
nascent_gate_popup_container = []
sell_window = []
buy_window = []
loot_popup_container = []
loot_text_container = []

info_text_1 = ''
info_text_2 = ''
info_text_3 = ''
info_text_4 = ''
character_name_input = ''
current_buy_item = ''
current_sell_item = ''
current_info_item = ''

# default values for buttons updated in event loops
npc_button = ''
academia_button = ''
combat_button = ''
inn_button = ''
shop_button = ''
# default objects for event loops, updated when player interacts with new object
current_enemy_battling = snake_1
current_npc_interacting = npc_garan
current_building_entering = seldon_inn

battle_info_to_return_to_main_loop = {"experience": 0, "item dropped": "", "leveled_up": False, "knowledge": ""}

clock = pygame.time.Clock()
enemy_tic = time.perf_counter()
npc_tic = time.perf_counter()
walk_tic = time.perf_counter()

# main loop ------------------------------------------------------------------------------------------------------------
while game_running:

    if not new_game_chosen and not continue_game_chosen and not start_chosen:
        resource_urls.screen.blit(start_screen, (0, 0))
        resource_urls.screen.blit(new_game_button.surf, new_game_button.rect)
        resource_urls.screen.blit(continue_button.surf, continue_button.rect)

        if len(save_data_window) > 0:
            for element in save_data_window:
                resource_urls.screen.blit(element.surf, element.rect)

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
                # click to dismiss save absent popup if player tries to continue with no save file
                if save_absent.rect.collidepoint(pos):
                    save_data_window.clear()
            elif event.type == QUIT:
                exit()
        pygame.display.flip()

    # ------------------------------------------------------------------------------------------------------------------
    # character selection for new game ---------------------------------------------------------------------------------
    if new_game_chosen:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                # if enter key is pressed, de-select name box and proceed
                if event.key == K_RETURN:
                    name_input_selected = False
                    entered = True
                if event.key == K_BACKSPACE:
                    if name_input_selected:
                        character_name_input = character_name_input[:-1]
                else:
                    if name_input_selected:
                        if len(character_name_input) < 12:
                            character_name_input += event.unicode
            elif event.type == QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # player clicks on the box to type name
                if name_input.rect.collidepoint(pos):
                    if name_input_selected:
                        if len(character_name_input) < 1:
                            name_input.update(name_input.x_coordinate, name_input.y_coordinate,
                                              resource_urls.name_input_img)
                        name_input_selected = False
                    else:
                        name_input.update(name_input.x_coordinate, name_input.y_coordinate,
                                          resource_urls.name_input_empty_img)
                        name_input_selected = True

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

            # noinspection PyUnboundLocalVariable
            if start_button.rect.collidepoint(pos) or entered:
                if amuna_race_selected:
                    player = PlayerAmuna(player.name, player.race, player.role, player.items, player.equipment,
                                         player.current_quests, player.quest_progress, player.quest_status,
                                         player.quest_complete, player.knowledge, player.skills_mage,
                                         player.skills_fighter, player.skills_scout, player.level, player.experience,
                                         player.health, player.energy, player.alive_status, player.rupees,
                                         player.reputation, player.current_zone, player.defense, player.offense,
                                         player.star_power)
                    player.race = "amuna"
                    player.surf = resource_urls.player_no_role_amuna_down_1
                    player.current_zone = "nascent"
                    in_over_world = True
                    new_game_chosen = False
                    start_chosen = True
                if nuldar_race_selected:
                    player = PlayerNuldar(player.name, player.race, player.role, player.items, player.equipment,
                                          player.current_quests, player.quest_progress, player.quest_status,
                                          player.quest_complete, player.knowledge, player.skills_mage,
                                          player.skills_fighter, player.skills_scout, player.level, player.experience,
                                          player.health, player.energy, player.alive_status, player.rupees,
                                          player.reputation, player.current_zone, player.defense, player.offense,
                                          player.star_power)
                    player.race = "nuldar"
                    player.surf = resource_urls.player_no_role_nuldar_down_1
                    player.current_zone = "nascent"
                    in_over_world = True
                    new_game_chosen = False
                    start_chosen = True
                if sorae_race_selected:
                    player = PlayerSorae(player.name, player.race, player.role, player.items, player.equipment,
                                         player.current_quests, player.quest_progress, player.quest_status,
                                         player.quest_complete, player.knowledge, player.skills_mage,
                                         player.skills_fighter, player.skills_scout, player.level, player.experience,
                                         player.health, player.energy, player.alive_status, player.rupees,
                                         player.reputation, player.current_zone, player.defense, player.offense,
                                         player.star_power)
                    player.race = "sorae"
                    player.surf = resource_urls.player_no_role_sorae_down_1
                    player.current_zone = "nascent"
                    in_over_world = True
                    new_game_chosen = False
                    start_chosen = True

                if len(character_name_input) > 0:
                    player.name = str(character_name_input)
                else:
                    player.name = "default"

        # amuna race selected on character selection screen ------------------------------------------------------------
        if amuna_race_selected:
            character_creation.character_screen_draw("amuna", amuna_character_screen, nuldar_character_screen,
                                                     sorae_character_screen, character_select_overlay,
                                                     amuna_select_overlay, amuna_character, nuldar_select_overlay,
                                                     nuldar_character, sorae_select_overlay, sorae_character,
                                                     amuna_button, nuldar_button, sorae_button, start_button,
                                                     name_input, name_input_font, character_name_input, pygame)

        # nuldar race selected on character selection screen -----------------------------------------------------------
        if nuldar_race_selected:
            character_creation.character_screen_draw("nuldar", amuna_character_screen, nuldar_character_screen,
                                                     sorae_character_screen, character_select_overlay,
                                                     amuna_select_overlay, amuna_character, nuldar_select_overlay,
                                                     nuldar_character, sorae_select_overlay, sorae_character,
                                                     amuna_button, nuldar_button, sorae_button, start_button,
                                                     name_input, name_input_font, character_name_input, pygame)

        # sorae race selected on character selection screen ------------------------------------------------------------
        if sorae_race_selected:
            character_creation.character_screen_draw("sorae", amuna_character_screen, nuldar_character_screen,
                                                     sorae_character_screen, character_select_overlay,
                                                     amuna_select_overlay, amuna_character, nuldar_select_overlay,
                                                     nuldar_character, sorae_select_overlay, sorae_character,
                                                     amuna_button, nuldar_button, sorae_button, start_button,
                                                     name_input, name_input_font, character_name_input, pygame)

    # continue game selected on start screen. try to load player info from save_game file ------------------------------
    if continue_game_chosen:
        load_returned = gameplay_functions.load_game(player, Item)
        barrier_learned = load_returned["barrier learned"]
        hard_strike_learned = load_returned["strike learned"]
        sharp_sense_learned = load_returned["sense learned"]
        saved = load_returned["saved"]
        start_chosen = load_returned["start"]
        continue_game_chosen = load_returned["continue"]
        npc_garan.gift = load_returned["garan gift"]
        rest_recover_show = load_returned["rest popup"]
        knowledge_academia_show = load_returned["knowledge popup"]

        if player.race == "amuna":
            player = PlayerAmuna(player.name, player.race, player.role, player.items, player.equipment,
                                 player.current_quests, player.quest_progress, player.quest_status,
                                 player.quest_complete, player.knowledge, player.skills_mage,
                                 player.skills_fighter, player.skills_scout, player.level, player.experience,
                                 player.health, player.energy, player.alive_status, player.rupees,
                                 player.reputation, player.current_zone, player.defense, player.offense,
                                 player.star_power)
            if player.role == "":
                player.surf = resource_urls.player_no_role_amuna_down_1
            if player.role == "mage":
                player.surf = resource_urls.player_mage_amuna_down_1
            if player.role == "fighter":
                player.surf = resource_urls.player_fighter_amuna_down_1
            if player.role == "scout":
                player.surf = resource_urls.player_scout_amuna_down_1

        if player.race == "nuldar":
            player = PlayerNuldar(player.name, player.race, player.role, player.items, player.equipment,
                                  player.current_quests, player.quest_progress, player.quest_status,
                                  player.quest_complete, player.knowledge, player.skills_mage,
                                  player.skills_fighter, player.skills_scout, player.level, player.experience,
                                  player.health, player.energy, player.alive_status, player.rupees,
                                  player.reputation, player.current_zone, player.defense, player.offense,
                                  player.star_power)
            if player.role == "":
                player.surf = resource_urls.player_no_role_nuldar_down_1
            if player.role == "mage":
                player.surf = resource_urls.player_mage_nuldar_down_1
            if player.role == "fighter":
                player.surf = resource_urls.player_fighter_nuldar_down_1
            if player.role == "scout":
                player.surf = resource_urls.player_scout_nuldar_down_1

        if player.race == "sorae":
            player = PlayerSorae(player.name, player.race, player.role, player.items, player.equipment,
                                 player.current_quests, player.quest_progress, player.quest_status,
                                 player.quest_complete, player.knowledge, player.skills_mage,
                                 player.skills_fighter, player.skills_scout, player.level, player.experience,
                                 player.health, player.energy, player.alive_status, player.rupees,
                                 player.reputation, player.current_zone, player.defense, player.offense,
                                 player.star_power)
            if player.role == "":
                player.surf = resource_urls.player_no_role_sorae_down_1
            if player.role == "mage":
                player.surf = resource_urls.player_mage_sorae_down_1
            if player.role == "fighter":
                player.surf = resource_urls.player_fighter_sorae_down_1
            if player.role == "scout":
                player.surf = resource_urls.player_scout_sorae_down_1

        if player.quest_progress["where's nede?"] == 1:
            nede.update(809, 390, resource_urls.nede_left)

        if load_returned["not found"]:
            save_data_window.append(save_absent)

    # ------------------------------------------------------------------------------------------------------------------
    # player has chosen to start game ----------------------------------------------------------------------------------
    if start_chosen:
        if player.alive_status:

            # player information updates
            gameplay_functions.player_info_and_ui_updates(player, hp_bar, en_bar, xp_bar, star_power_meter)

            if in_over_world and not in_battle and not in_npc_interaction and not in_shop and not in_inn \
                    and not in_academia:

                pressed_keys = pygame.key.get_pressed()
                # player movement updates
                walking_return = gameplay_functions.walk_time(walk_tic)
                if walking_return["reset"]:
                    walk_tic = time.perf_counter()
                if movement_able and in_over_world:
                    if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                        player.update("right", player.current_zone, walking_return["total time"])
                    if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                        player.update("left", player.current_zone, walking_return["total time"])
                    if pressed_keys[K_w] or pressed_keys[K_UP]:
                        player.update("up", player.current_zone, walking_return["total time"])
                    if pressed_keys[K_s] or pressed_keys[K_DOWN]:
                        player.update("down", player.current_zone, walking_return["total time"])

                # main event loop
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        # escape key was pressed, exit game
                        if event.key == K_ESCAPE:
                            exit()
                        # "F" key for player interaction
                        if event.key == K_f:
                            interacted = True
                        # "C" hotkey for character sheet
                        if event.key == K_c:
                            if character_button_clicked:
                                character_button_clicked = False
                            else:
                                character_button_clicked = True
                        # "J" hotkey for journal sheet
                        if event.key == K_j:
                            if journal_button_clicked:
                                journal_button_clicked = False
                            else:
                                journal_button_clicked = True
                    elif event.type == QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        # click handlers
                        info_choice = click_handlers.item_info_button(event, item_info_button, pygame)
                        if info_choice == "yes":
                            inventory_event = click_handlers.inventory_click_handler(player, current_info_item)
                            if inventory_event["item message"] != "":
                                info_text_1 = inventory_event["item message"]
                                info_text_2 = ""
                            drawing_functions.item_info_window.clear()
                        if info_choice == "no":
                            drawing_functions.item_info_window.clear()
                        inventory_item_clicked = click_handlers.inventory_event_item(event, pygame)
                        if inventory_item_clicked["clicked"]:
                            current_info_item = drawing_functions.item_info_draw(inventory_item_clicked["element"],
                                                                                 info_items, item_info_button)
                        # function to handle equipment item clicks. apply item message to message box if not empty str.
                        equipment_event = click_handlers.equipment_click_handler(player, event, pygame)
                        if equipment_event["equipment message"] != "":
                            info_text_1 = equipment_event["equipment message"]
                            info_text_2 = ""
                        # hearth button was clicked, set animation and move player to stone
                        if hearth_button.rect.collidepoint(pos):
                            hearthstone_animation()
                            player.current_zone = "seldon"
                            player.x_coordinate = 850
                            player.y_coordinate = 650
                            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                            info_text_1 = "You recalled to the hearth stone."
                        # save button was clicked. Save player info in dictionary to be loaded later
                        if save_button.rect.collidepoint(pos):
                            yes_button.update(450, 394, resource_urls.yes_button_img)
                            # see if there already exists a save file by trying to read it
                            try:
                                with open("save_game", "rb") as f:
                                    saved = True
                            except FileNotFoundError:
                                saved = False
                                pass
                            if saved:
                                save_check_window.append(save_check)
                                save_check_window.append(yes_button)
                                save_check_window.append(no_button)
                            if not saved:
                                gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                             sharp_sense_learned, saved, npc_garan.gift,
                                                             rest_recover_show, knowledge_academia_show)
                                saved = True
                                info_text_1 = "You saved your game. "
                        if yes_button.rect.collidepoint(pos):
                            gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                         sharp_sense_learned, saved, npc_garan.gift,
                                                         rest_recover_show, knowledge_academia_show)
                            save_check_window.clear()
                            info_text_1 = "You saved your game. "
                        if no_button.rect.collidepoint(pos):
                            save_check_window.clear()

                        # character button clicked
                        if character_button.rect.collidepoint(pos):
                            if character_button_clicked:
                                character_button_clicked = False
                            else:
                                character_button_clicked = True
                        # journal button clicked
                        if journal_button.rect.collidepoint(pos):
                            if journal_button_clicked:
                                journal_button_clicked = False
                            else:
                                journal_button_clicked = True

                        # pop-up notifications, click to hide
                        if level_up_win.rect.collidepoint(pos):
                            drawing_functions.level_up_draw(level_up_win, player, font, False)
                        if knowledge_academia.rect.collidepoint(pos) and knowledge_academia_show:
                            knowledge_window_clicked = True
                        if rest_recover.rect.collidepoint(pos) and rest_recover_show:
                            rest_window_clicked = True
                        if loot_popup.rect.collidepoint(pos):
                            loot_popup_container.clear()
                            loot_text_container.clear()

                drawing_functions.character_sheet_info_draw(character_sheet, player, font, character_button_clicked)
                drawing_functions.journal_info_draw(journal, player, font, journal_button_clicked)

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in nascent grove (starting area) ------------------------------------------------------------
            if player.current_zone == "nascent" and in_over_world and not in_shop and not in_inn and not in_academia \
                    and not in_battle and not in_npc_interaction:
                resource_urls.screen.blit(nascent_grove_bg, (0, 0))
                resource_urls.screen.blit(nascent_gate.surf, nascent_gate.rect)
                resource_urls.screen.blit(player.surf, player.rect)

                if len(nascent_gate_popup_container) > 0:
                    for popup in nascent_gate_popup_container:
                        resource_urls.screen.blit(popup.surf, popup.rect)

                if pygame.sprite.collide_rect(player, nascent_gate):
                    nascent_gate_popup_container.append(nascent_gate_popup)
                    if interacted and in_over_world:
                        nascent_gate.update(nascent_gate.x_coordinate, nascent_gate.y_coordinate,
                                            resource_urls.nascent_gate_open)
                        if player.y_coordinate > 300:
                            player.y_coordinate = 215
                        else:
                            player.y_coordinate = 375
                        interacted = False
                else:
                    nascent_gate_popup_container.clear()
                    nascent_gate.update(nascent_gate.x_coordinate, nascent_gate.y_coordinate,
                                        resource_urls.nascent_gate_closed)

                # move player to seldon district when they approach nascent grove exit
                if player.x_coordinate > 700 and player.y_coordinate < 80:
                    player.current_zone = "seldon"
                    in_over_world = True
                    player.x_coordinate = 425
                    player.y_coordinate = 690

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in stardust outpost -------------------------------------------------------------------------
            if player.current_zone == "stardust" and in_over_world and not in_shop and not in_inn and not in_academia \
                    and not in_battle and not in_npc_interaction:
                resource_urls.screen.blit(stardust_outpost_bg, (0, 0))
                if player.quest_progress["where's nede?"] < 1:
                    resource_urls.screen.blit(nede.surf, nede.rect)
                resource_urls.screen.blit(player.surf, player.rect)
                for save_window in save_check_window:
                    resource_urls.screen.blit(save_window.surf, save_window.rect)
                for ui_elements in user_interface:
                    resource_urls.screen.blit(ui_elements.surf, ui_elements.rect)
                resource_urls.screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                resource_urls.screen.blit(hp_bar.surf, hp_bar.rect)
                resource_urls.screen.blit(en_bar.surf, en_bar.rect)
                resource_urls.screen.blit(xp_bar.surf, xp_bar.rect)
                # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                drawing_functions.text_info_draw(player, font,
                                                 info_text_1, info_text_2, info_text_3, info_text_4, in_over_world)
                drawing_functions.draw_it()

                # player encounters Nede for Celeste's quest
                if pygame.sprite.collide_rect(player, nede):
                    interaction_popup.update(nede.x_coordinate, nede.y_coordinate - 25,
                                             resource_urls.popup_interaction)
                    resource_urls.screen.blit(interaction_popup.surf, interaction_popup.rect)
                    interaction_info_surf = font.render(str("nede"), True, "black", "light yellow")
                    interaction_info_rect = interaction_info_surf.get_rect()
                    interaction_info_rect.center = (nede.x_coordinate, nede.y_coordinate - 25)
                    resource_urls.screen.blit(interaction_info_surf, interaction_info_rect)

                    if player.quest_status["where's nede?"]:
                        info_text_1 = f"Press 'F' key to pet Nede."
                        if interacted and in_over_world:
                            if player.quest_progress["where's nede?"] < 1:
                                player.quest_progress["where's nede?"] += 1
                                info_text_2 = "You pet Nede. He seems calm. "
                                info_text_3 = "Nede heads back towards Seldon. "
                                nede.update(809, 390, resource_urls.nede_left)
                                interacted = False
                            else:
                                info_text_1 = "Nede's already been found."
                                interacted = False
                    else:
                        info_text_1 = "What a nice dog!"

                # move player to seldon district when they approach nascent grove exit
                if player.x_coordinate > 925 and 175 < player.y_coordinate < 275:
                    player.current_zone = "seldon"
                    in_over_world = True
                    player.x_coordinate = 125
                    player.y_coordinate = 375

                # nede movement updates
                if player.quest_progress["where's nede?"] < 1:
                    face_direction = random.choice(["left", "right"])
                    if movement_able and in_over_world:
                        npc_toc = time.perf_counter()
                        if npc_toc - npc_tic > 2:
                            npc_tic = time.perf_counter()
                            if face_direction == "left":
                                nede.update(nede.x_coordinate, nede.y_coordinate, resource_urls.nede_left)
                            if face_direction == "right":
                                nede.update(nede.x_coordinate, nede.y_coordinate, resource_urls.nede_right)

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in korlok district --------------------------------------------------------------------------
            if player.current_zone == "korlok" and in_over_world and not in_shop and not in_inn \
                    and not in_academia and not in_battle and not in_npc_interaction:
                resource_urls.screen.blit(korlok_district_bg, (0, 0))
                resource_urls.screen.blit(rohir_gate.surf, rohir_gate.rect)
                resource_urls.screen.blit(player.surf, player.rect)
                for save_window in save_check_window:
                    resource_urls.screen.blit(save_window.surf, save_window.rect)
                for ui_elements in user_interface:
                    resource_urls.screen.blit(ui_elements.surf, ui_elements.rect)
                resource_urls.screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                resource_urls.screen.blit(hp_bar.surf, hp_bar.rect)
                resource_urls.screen.blit(en_bar.surf, en_bar.rect)
                resource_urls.screen.blit(xp_bar.surf, xp_bar.rect)
                # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                drawing_functions.text_info_draw(player, font, info_text_1, info_text_2, info_text_3,
                                                 info_text_4, in_over_world)
                drawing_functions.draw_it()

                quest_item = pygame.sprite.spritecollideany(player, quest_items)
                try:
                    interaction_popup.update(quest_item.x_coordinate, quest_item.y_coordinate - 25,
                                             resource_urls.popup_interaction)
                    resource_urls.screen.blit(interaction_popup.surf, interaction_popup.rect)
                    interaction_info_surf = font.render(str(quest_item.name), True, "black", "light yellow")
                    interaction_info_rect = interaction_info_surf.get_rect()
                    interaction_info_rect.center = (quest_item.x_coordinate, quest_item.y_coordinate - 25)
                    resource_urls.screen.blit(interaction_info_surf, interaction_info_rect)

                    if quest_item.model == "rohir gate":
                        if player.quest_complete["ghouled again"]:
                            info_text_1 = f"Press 'F' key to enter Seldon District."
                            if interacted:
                                player.current_zone = "seldon"
                                in_over_world = True
                                interacted = False
                                player.x_coordinate = 525
                                player.y_coordinate = 100
                                player.rect = player.surf.get_rect(
                                    midbottom=(player.x_coordinate, player.y_coordinate))
                                rohir_gate.update(525, 50, resource_urls.rohir_gate)

                except AttributeError:
                    pass

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in seldon district --------------------------------------------------------------------------
            if player.current_zone == "seldon" and in_over_world and not in_shop and not in_inn and not in_academia \
                    and not in_battle and not in_npc_interaction:

                resource_urls.screen.blit(seldon_district_bg, (0, 0))

                enemy_respawn()
                for entity in most_sprites:
                    resource_urls.screen.blit(entity.surf, entity.rect)
                for enemy_sprite in enemies:
                    resource_urls.screen.blit(enemy_sprite.surf, enemy_sprite.rect)
                if player.quest_progress["where's nede?"] == 1:
                    resource_urls.screen.blit(nede.surf, nede.rect)
                gameplay_functions.npc_quest_star_updates(player, quest_star_garan, quest_star_maurelle,
                                                          quest_star_celeste, quest_star_torune)
                resource_urls.screen.blit(player.surf, player.rect)

                for save_window in save_check_window:
                    resource_urls.screen.blit(save_window.surf, save_window.rect)
                for ui_elements in user_interface:
                    resource_urls.screen.blit(ui_elements.surf, ui_elements.rect)

                if len(loot_popup_container) > 0:
                    for popup in loot_popup_container:
                        resource_urls.screen.blit(popup.surf, popup.rect)
                if len(loot_text_container) > 0:
                    for loot_text in loot_text_container:
                        resource_urls.screen.blit(loot_text[0], loot_text[1])

                resource_urls.screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                resource_urls.screen.blit(hp_bar.surf, hp_bar.rect)
                resource_urls.screen.blit(en_bar.surf, en_bar.rect)
                resource_urls.screen.blit(xp_bar.surf, xp_bar.rect)

                # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                drawing_functions.text_info_draw(player, font, info_text_1, info_text_2, info_text_3,
                                                 info_text_4, in_over_world)
                drawing_functions.draw_it()

                # pop up notifications for situations like low health or first weapon acquire
                if not knowledge_academia_show:
                    if player.knowledge["mage"] == 50 or player.knowledge["fighter"] == 50 or \
                            player.knowledge["scout"] == 50:
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

                # draw pop up notifications on top of everything else
                if len(knowledge_academia_window) > 0:
                    for knowledge_window_notification in knowledge_academia_window:
                        resource_urls.screen.blit(knowledge_window_notification.surf,
                                                  knowledge_window_notification.rect)
                if len(rest_recover_window) > 0:
                    for rest_window in rest_recover_window:
                        resource_urls.screen.blit(rest_window.surf, rest_window.rect)

                # if battle happened, get battle info (item or experience gained) and apply to message box
                if not loot_updated:
                    loot_popup_container.append(loot_popup)
                    xp_info_surf = font.render(str(battle_info_to_return_to_main_loop["experience"]),
                                               True, "black", "light yellow")
                    xp_info_rect = xp_info_surf.get_rect()
                    xp_info_rect.center = (170, 492)
                    loot_text_container.append((xp_info_surf, xp_info_rect))
                    know_info_surf = font.render(str(battle_info_to_return_to_main_loop["knowledge"]),
                                                 True, "black", "light yellow")
                    know_info_rect = know_info_surf.get_rect()
                    know_info_rect.center = (205, 510)
                    loot_text_container.append((know_info_surf, know_info_rect))
                    loot_info_surf = font.render(str(battle_info_to_return_to_main_loop["item dropped"]),
                                                 True, "black", "light yellow")
                    loot_info_rect = loot_info_surf.get_rect()
                    loot_info_rect.center = (170, 565)
                    loot_text_container.append((loot_info_surf, loot_info_rect))
                    loot_updated = True

                if battle_info_to_return_to_main_loop["leveled_up"]:
                    drawing_functions.level_up_draw(level_up_win, player, font, True)

                # move player to nascent grove when they approach
                if 375 < player.x_coordinate < 475 and player.y_coordinate > 700:
                    player.current_zone = "nascent"
                    in_over_world = True
                    player.x_coordinate = 750
                    player.y_coordinate = 125
                # move player to stardust outpost when they approach
                if player.x_coordinate < 25 and 325 < player.y_coordinate < 400:
                    player.current_zone = "stardust"
                    in_over_world = True
                    player.x_coordinate = 925
                    player.y_coordinate = 275

                # player encounters a quest item. check progress and add to if interacted with
                quest_item = pygame.sprite.spritecollideany(player, quest_items)
                try:
                    interaction_popup.update(quest_item.x_coordinate, quest_item.y_coordinate - 25,
                                             resource_urls.popup_interaction)
                    resource_urls.screen.blit(interaction_popup.surf, interaction_popup.rect)
                    interaction_info_surf = font.render(str(quest_item.name), True, "black", "light yellow")
                    interaction_info_rect = interaction_info_surf.get_rect()
                    interaction_info_rect.center = (quest_item.x_coordinate, quest_item.y_coordinate - 25)
                    resource_urls.screen.blit(interaction_info_surf, interaction_info_rect)

                    if quest_item.name == "pine logs":
                        if not player.quest_complete["village repairs"]:
                            if player.quest_status["village repairs"]:
                                info_text_1 = "Press 'F' key to gather the pine log."
                                if interacted and in_over_world:
                                    if player.quest_progress["village repairs"] < 4:
                                        player.quest_progress["village repairs"] += 1
                                        info_text_1 = "You gathered 1 pine log."
                                        quest_item.kill()
                                        interacted = False
                                    else:
                                        info_text_1 = "You've already gathered these."
                                        interacted = False
                        else:
                            info_text_1 = "That's a nice pine log."

                    if quest_item.model == "rohir gate":
                        if player.quest_complete["ghouled again"]:
                            info_text_1 = "Press 'F' key to enter Korlok District."
                            if interacted and in_over_world:
                                player.x_coordinate = 525
                                player.y_coordinate = 650
                                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                                rohir_gate.update(525, 600, resource_urls.rohir_gate)
                                player.current_zone = "korlok"
                                interacted = False
                        else:
                            info_text_1 = "The gate seems to be locked shut."
                            info_text_2 = "Perhaps the nearby Guard knows why?"
                except AttributeError:
                    pass

                # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
                enemy = pygame.sprite.spritecollideany(player, enemies)
                if enemy:
                    interaction_popup.update(enemy.x_coordinate, enemy.y_coordinate - 40,
                                             resource_urls.popup_interaction)
                    resource_urls.screen.blit(interaction_popup.surf, interaction_popup.rect)
                    interaction_info_surf = font.render(str(enemy.name) + " lvl " +
                                                        str(enemy.level), True, "black", "light yellow")
                    interaction_info_rect = interaction_info_surf.get_rect()
                    interaction_info_rect.center = (enemy.x_coordinate, enemy.y_coordinate - 40)
                    resource_urls.screen.blit(interaction_info_surf, interaction_info_rect)

                    # lets player know if they are in range of enemy they can press f to attack it
                    info_text_1 = "Press 'F' key to attack enemy."
                    info_text_2 = ""

                    if interacted and in_over_world and not in_battle and not in_shop and not in_inn \
                            and not in_academia and not in_npc_interaction:
                        current_enemy_battling = enemy
                        in_over_world = False
                        in_battle = True
                        combat_scenario.resting_animation(player, enemy, player_battle_sprite,
                                                          snake_battle_sprite, ghoul_battle_sprite, barrier_active,
                                                          sharp_sense_active, in_battle, in_npc_interaction)

                # player collides with building, enters if chosen to interact and starts related scenario
                building = pygame.sprite.spritecollideany(player, buildings)
                if building and in_over_world and not in_battle and not in_shop and not in_inn and not in_academia \
                        and not in_npc_interaction:

                    interaction_popup.update(building.x_coordinate, building.y_coordinate - 50,
                                             resource_urls.popup_interaction)
                    resource_urls.screen.blit(interaction_popup.surf, interaction_popup.rect)
                    interaction_info_surf = font.render(str(building.name), True, "black", "light yellow")
                    interaction_info_rect = interaction_info_surf.get_rect()
                    interaction_info_rect.center = (building.x_coordinate, building.y_coordinate - 50)
                    resource_urls.screen.blit(interaction_info_surf, interaction_info_rect)

                    # lets player know if they are in range of building they can press f to enter it
                    info_text_1 = "Press 'F' key to enter building."
                    info_text_2 = ""

                    if interacted:
                        current_building_entering = building
                        movement_able = False
                        in_over_world = False
                        if building.name == "shop":
                            in_shop = True
                        if building.name == "inn":
                            in_inn = True
                        if building.name == "academia":
                            in_academia = True

                # if player collides with npc sprite and chooses to interact with it
                npc = pygame.sprite.spritecollideany(player, npcs)
                if npc:
                    interaction_popup.update(npc.x_coordinate, npc.y_coordinate - 50,
                                             resource_urls.popup_interaction)
                    resource_urls.screen.blit(interaction_popup.surf, interaction_popup.rect)
                    interaction_info_surf = font.render(str(npc.name), True, "black", "light yellow")
                    interaction_info_rect = interaction_info_surf.get_rect()
                    interaction_info_rect.center = (npc.x_coordinate, npc.y_coordinate - 50)
                    resource_urls.screen.blit(interaction_info_surf, interaction_info_rect)

                    info_text_1 = "Press 'F' key to talk to NPC."
                    info_text_2 = ""

                    if interacted and in_over_world and not in_battle and not in_shop and not in_inn \
                            and not in_academia and not in_npc_interaction:
                        current_npc_interacting = npc
                        in_over_world = False
                        in_npc_interaction = True
                        movement_able = False
                        combat_scenario.resting_animation(player, enemy, player_battle_sprite,
                                                          snake_battle_sprite, ghoul_battle_sprite,
                                                          barrier_active, sharp_sense_active, in_battle,
                                                          in_npc_interaction)

                # enemy movement updates
                direction_horizontal = random.choice(["left", "right"])
                direction_vertical = random.choice(["up", "down"])
                move_snake = random.choice(snakes.sprites())
                move_ghoul = random.choice(ghouls.sprites())
                if movement_able and in_over_world:
                    enemy_toc = time.perf_counter()
                    if enemy_toc - enemy_tic > 2:
                        enemy_tic = time.perf_counter()
                        move_snake.update_position([100, 300], [200, 300], direction_horizontal, direction_vertical)
                        move_ghoul.update_position([700, 900], [200, 300], direction_horizontal, direction_vertical)

                # npc movement updates
                face_direction = random.choice(["front", "back", "left", "right"])
                face_this_npc = random.choice(npcs.sprites())
                if movement_able and in_over_world:
                    npc_toc = time.perf_counter()
                    if npc_toc - npc_tic > 5:
                        npc_tic = time.perf_counter()
                        if face_direction == "front":
                            if face_this_npc.name == "garan":
                                npc_garan.update(resource_urls.garan_down)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(resource_urls.maurelle_down)
                            if face_this_npc.name == "celeste":
                                npc_celeste.update(resource_urls.celeste_down)
                            if face_this_npc.name == "torune":
                                npc_torune.update(resource_urls.torune_down)
                        if face_direction == "back":
                            if face_this_npc.name == "garan":
                                npc_garan.update(resource_urls.garan_up)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(resource_urls.maurelle_up)
                            if face_this_npc.name == "celeste":
                                npc_celeste.update(resource_urls.celeste_up)
                            if face_this_npc.name == "torune":
                                npc_torune.update(resource_urls.torune_up)
                        if face_direction == "left":
                            if face_this_npc.name == "garan":
                                npc_garan.update(resource_urls.garan_left)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(resource_urls.maurelle_left)
                            if face_this_npc.name == "celeste":
                                npc_celeste.update(resource_urls.celeste_left)
                            if face_this_npc.name == "torune":
                                npc_torune.update(resource_urls.torune_left)
                        if face_direction == "right":
                            if face_this_npc.name == "garan":
                                npc_garan.update(resource_urls.garan_right)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(resource_urls.maurelle_right)
                            if face_this_npc.name == "celeste":
                                npc_celeste.update(resource_urls.celeste_right)
                            if face_this_npc.name == "torune":
                                npc_torune.update(resource_urls.torune_right)

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in battle -----------------------------------------------------------------------------------
            if in_battle and not in_over_world and not in_shop and not in_inn and not in_academia \
                    and not in_npc_interaction:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                    elif event.type == QUIT:
                        exit()
                    # get which button player pressed during combat scenario
                    combat_button = click_handlers.combat_event_button(event, no_role_attack_button,
                                                                       mage_attack_button, fighter_attack_button,
                                                                       scout_attack_button, barrier_button,
                                                                       hard_strike_button, sharp_sense_button, pygame)
                    # click handlers
                    info_choice = click_handlers.item_info_button(event, item_info_button, pygame)
                    if info_choice == "yes":
                        inventory_event = click_handlers.inventory_click_handler(player, current_info_item)
                        if inventory_event["item message"] != "":
                            info_text_1 = inventory_event["item message"]
                            info_text_2 = ""
                        drawing_functions.item_info_window.clear()
                    if info_choice == "no":
                        drawing_functions.item_info_window.clear()

                    inventory_item_clicked = click_handlers.inventory_event_item(event, pygame)
                    if inventory_item_clicked["clicked"]:
                        current_info_item = drawing_functions.item_info_draw(inventory_item_clicked["element"],
                                                                             info_items, item_info_button)

                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = click_handlers.equipment_click_handler(player, event, pygame)
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""

                # outside of battle event loop -------------------------------------------------------------------------
                combat_scenario.enemy_health_bar(current_enemy_battling)
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

                        combat_keys = pygame.key.get_pressed()
                        if combat_button == "attack" or combat_keys[K_1]:
                            combat_button = ''
                            combat_scenario.combat_animation(player, current_enemy_battling,
                                                             player_battle_sprite, snake_battle_sprite,
                                                             ghoul_battle_sprite, barrier_active, sharp_sense_active,
                                                             hard_strike)

                            # combat event function that handles and returns damage and health
                            combat_events = combat_scenario.attack_scenario(current_enemy_battling, "attack", player,
                                                                            level_up_win, level_up_font,
                                                                            hard_strike_learned)
                            combat_happened = True

                            # add all combat scenario happenings from function to message box
                            if combat_events["damage done string"] == 0:
                                info_text_1 = ""
                            else:
                                info_text_1 = str(combat_events["damage done string"])
                            if combat_events["damage taken string"] == 0:
                                info_text_2 = ""
                            else:
                                info_text_2 = str(combat_events["damage taken string"])

                            # adds item dropped and experienced gained messages to box if enemy was defeated
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
                            if combat_events["enemy defeated"]:
                                # player will gain knowledge based on their current role
                                if player.role == "mage":
                                    player.knowledge["mage"] += 10
                                    battle_info_to_return_to_main_loop["knowledge"] = \
                                        "10 mage"
                                if player.role == "fighter":
                                    player.knowledge["fighter"] += 10
                                    battle_info_to_return_to_main_loop["knowledge"] = \
                                        "10 fighter"
                                if player.role == "scout":
                                    player.knowledge["scout"] += 10
                                    battle_info_to_return_to_main_loop["knowledge"] = \
                                        "10 scout"

                                # if barrier is active on enemy defeat, restore original defence and set off
                                if barrier_active:
                                    barrier_active = False
                                    # noinspection PyUnboundLocalVariable
                                    player.defense = original_defence
                                # if sharp sense is active on enemy defeat, restore original offense
                                if sharp_sense_active:
                                    sharp_sense_active = False
                                    # noinspection PyUnboundLocalVariable
                                    player.offense = original_offense

                                movement_able = True
                                combat_happened = False
                                interacted = False
                                encounter_started = False
                                in_battle = False
                                in_over_world = True
                                loot_updated = False

                        # (buffs) mage -> barrier [defence], scout -> sharp sense [offense]
                        elif combat_button == "skill 1" or combat_keys[K_2]:
                            combat_button = ''
                            # make sure player has enough energy to use the skill
                            if player.energy > 34:
                                # player is a mage and uses the barrier spell. Set barrier active to true
                                # save original defence value to be re applied upon enemy or player defeat
                                if player.role == "mage":
                                    if barrier_learned:
                                        if not barrier_active:
                                            original_defence = player.defense
                                            info_text_1 = "Barrier spell is active."
                                            info_text_2 = "You have gained 10 defence."
                                            barrier_active = True
                                            player.defense += 10
                                            player.energy -= 35
                                        else:
                                            info_text_1 = "Barrier spell is already active."
                                # player is a scout and uses sharp sense. Set sharp sense active to true
                                # save original offense value to be re applied upon enemy or player defeat
                                if player.role == "scout":
                                    if sharp_sense_learned:
                                        if not sharp_sense_active:
                                            original_offense = player.offense
                                            info_text_1 = "Sharp sense is active."
                                            info_text_2 = "You have gained 20 offense."
                                            sharp_sense_active = True
                                            player.offense += 20
                                            player.energy -= 35
                                        else:
                                            info_text_1 = "Sharp sense is already active."
                                # player is a fighter and uses hard strike
                                if player.role == "fighter":
                                    if hard_strike_learned:
                                        hard_strike = True
                                        combat_scenario.fighter_hard_strike_animation(player, player_battle_sprite,
                                                                                      current_enemy_battling,
                                                                                      snake_battle_sprite,
                                                                                      ghoul_battle_sprite)
                                        combat_events = combat_scenario.attack_scenario(current_enemy_battling,
                                                                                        "skill 1", player,
                                                                                        level_up_win, level_up_font,
                                                                                        hard_strike_learned)
                                        combat_happened = True
                                        player.energy -= 35
                                        if combat_events["damage done string"] == 0:
                                            info_text_1 = ""
                                        else:
                                            info_text_1 = str(combat_events["damage done string"])
                                        if combat_events["damage taken string"] == 0:
                                            info_text_2 = ""
                                        else:
                                            info_text_2 = str(combat_events["damage taken string"])
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
                                            encounter_started = False
                                            in_battle = False
                                            in_over_world = True
                                            loot_updated = False
                            else:
                                info_text_1 = "Not enough energy to use this skill."

                # battle scene and enemy are drawn to screen -----------------------------------------------------------
                try:
                    if player.current_zone == "seldon" and in_battle and not in_over_world and not in_shop \
                            and not in_inn and not in_academia and not in_npc_interaction:
                        resource_urls.screen.blit(seldon_district_battle, (0, 0))
                        resource_urls.screen.blit(skill_bar.surf, skill_bar.rect)
                        if player.role == "mage":
                            resource_urls.screen.blit(mage_attack_button.surf, mage_attack_button.rect)
                            if player.skills_mage["skill 2"] == "barrier":
                                resource_urls.screen.blit(barrier_button.surf, barrier_button.rect)
                        if player.role == "fighter":
                            resource_urls.screen.blit(fighter_attack_button.surf, fighter_attack_button.rect)
                            if player.skills_fighter["skill 2"] == "hard strike":
                                resource_urls.screen.blit(hard_strike_button.surf, hard_strike_button.rect)
                        if player.role == "scout":
                            resource_urls.screen.blit(scout_attack_button.surf, scout_attack_button.rect)
                            if player.skills_scout["skill 2"] == "sharp sense":
                                resource_urls.screen.blit(sharp_sense_button.surf, sharp_sense_button.rect)
                        if player.role == "":
                            resource_urls.screen.blit(no_role_attack_button.surf, no_role_attack_button.rect)
                        resource_urls.screen.blit(player_battle_sprite.surf, player_battle_sprite.rect)
                        if current_enemy_battling.name == "snake":
                            resource_urls.screen.blit(snake_battle_sprite.surf, snake_battle_sprite.rect)
                        if current_enemy_battling.name == "ghoul":
                            resource_urls.screen.blit(ghoul_battle_sprite.surf, ghoul_battle_sprite.rect)
                        resource_urls.screen.blit(enemy_status_bar_back.surf, enemy_status_bar_back.rect)
                        try:
                            resource_urls.screen.blit(current_enemy_battling.health_bar.surf,
                                                      current_enemy_battling.health_bar.rect)
                        except TypeError:
                            pass
                        resource_urls.screen.blit(star_power_meter.surf, star_power_meter.rect)
                        resource_urls.screen.blit(message_box.surf, message_box.rect)
                        # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                        drawing_functions.text_info_draw(player, font, info_text_1, info_text_2, info_text_3,
                                                         info_text_4, in_over_world)
                        drawing_functions.draw_it()
                        resource_urls.screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                        resource_urls.screen.blit(hp_bar.surf, hp_bar.rect)
                        resource_urls.screen.blit(en_bar.surf, en_bar.rect)
                        resource_urls.screen.blit(xp_bar.surf, xp_bar.rect)
                        resource_urls.screen.blit(enemy_status.surf, enemy_status.rect)
                        text_enemy_name_surf = font.render(str(current_enemy_battling.name), True, "black",
                                                           "light yellow")
                        text_enemy_name_rect = text_enemy_name_surf.get_rect()
                        text_enemy_name_rect.center = (805, 689)
                        resource_urls.screen.blit(text_enemy_name_surf, text_enemy_name_rect)
                        text_enemy_level_surf = font.render(str(current_enemy_battling.level), True, "black",
                                                            "light yellow")
                        text_enemy_level_rect = text_enemy_level_surf.get_rect()
                        text_enemy_level_rect.center = (915, 689)
                        resource_urls.screen.blit(text_enemy_level_surf, text_enemy_level_rect)

                        # popup damage overlays ------------------------------------------------------------------------
                        if combat_happened and combat_events["damage done"] != 0:
                            resource_urls.screen.blit(dealt_damage_overlay.surf, dealt_damage_overlay.rect)
                            damage_done_surf = level_up_font.render(str(combat_events["damage done"]),
                                                                    True, "black", "white")
                            damage_done_rect = damage_done_surf.get_rect()
                            damage_done_rect.center = (850, 225)
                            resource_urls.screen.blit(damage_done_surf, damage_done_rect)
                            pygame.display.flip()

                            if combat_events["damage taken"] != 0:
                                pygame.time.wait(250)
                                resource_urls.screen.blit(received_damage_overlay.surf, received_damage_overlay.rect)
                                damage_received_surf = level_up_font.render(str(combat_events["damage taken"]),
                                                                            True, "black", "white")
                                damage_received_rect = damage_received_surf.get_rect()
                                damage_received_rect.center = (125, 275)
                                resource_urls.screen.blit(damage_received_surf, damage_received_rect)
                                pygame.display.flip()

                except AttributeError:
                    pass

                # combat didn't happen this iteration, reset sprites to default surface image
                if not combat_happened:
                    combat_scenario.resting_animation(player, current_enemy_battling, player_battle_sprite,
                                                      snake_battle_sprite, ghoul_battle_sprite, barrier_active,
                                                      sharp_sense_active, in_battle, in_npc_interaction)
                    combat_cooldown = False

                # combat happened this turn, update sprites for attack and apply short cooldown to attack again
                if combat_happened:
                    combat_scenario.combat_animation(player, current_enemy_battling, player_battle_sprite,
                                                     snake_battle_sprite, ghoul_battle_sprite, barrier_active,
                                                     sharp_sense_active, hard_strike)
                    combat_cooldown = True
                    # when combat happens, apply a short cooldown so attack button can't be spammed
                    pygame.time.wait(750)
                    # reset combat animation and ability to click without delay on next iteration
                    combat_happened = False
                    # reset hard strike condition so regular fighter attack animation resumes
                    hard_strike = False

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in shop -------------------------------------------------------------------------------------
            if in_shop and not in_over_world and not in_battle and not in_inn and not in_academia \
                    and not in_npc_interaction:

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                    elif event.type == QUIT:
                        exit()

                    # get which button player pressed during shop scenario (buy or leave)
                    shop_button = click_handlers.shop_event_button(event, buy_button, leave_button, pygame)
                    if buy_clicked:
                        # if player clicks yes button to sell item, get current item and buy ---------------------------
                        buy_choice = click_handlers.shop_buy_button(event, yes_button, pygame)
                        buy_return = shop_scenario.buy_items(player, buy_choice, current_buy_item, Item)
                        if buy_return["info 1"] != "":
                            info_text_1 = buy_return["info 1"]
                        if buy_return["info 2"] != "":
                            info_text_1 = buy_return["info 2"]
                        item_bought = buy_return["bought"]
                        # draws buy info box for info and confirmation
                        buy_item = click_handlers.buy_event_item(event, shopkeeper_items, pygame)
                        if drawing_functions.buy_info_draw(buy_item, buy_items, yes_button) is not None:
                            current_buy_item = drawing_functions.buy_info_draw(buy_item, buy_items, yes_button)

                    if not buy_clicked:
                        # if player clicks yes button to sell item, get current item and sell --------------------------
                        sell_choice = click_handlers.shop_sell_button(event, yes_button, pygame)
                        sell_return = shop_scenario.sell_items(player, sell_choice, current_sell_item)
                        if sell_return["info 1"] != "":
                            info_text_1 = sell_return["info 1"]
                        if sell_return["info 2"] != "":
                            info_text_1 = sell_return["info 2"]
                        item_sold = sell_return["sold"]
                        # draws sell info box for info and confirmation
                        sell_item = click_handlers.sell_event_item(event, pygame)
                        if drawing_functions.sell_info_draw(sell_item, sell_items, yes_button) is not None:
                            current_sell_item = drawing_functions.sell_info_draw(sell_item, sell_items, yes_button)

                # outside of shop event loop ---------------------------------------------------------------------------
                # if player has just started shop scenario, clear message box
                if not encounter_started:
                    info_text_1 = "Click an inventory item to sell it."
                    info_text_2 = "Or, click buy button to buy an item."
                    info_text_3 = ""
                    info_text_4 = ""
                    encounter_started = True
                    # reset items bought condition on new shop encounter so that message is shown to player that
                    item_bought = False
                    item_sold = False

                shop_keys = pygame.key.get_pressed()
                if shop_button == "buy":
                    shop_button = ''
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
                    # user clicked buy button for the first time. show buy window
                    else:
                        buy_clicked = True
                        buy_shop_elements.insert(0, buy_inventory)
                        shop_scenario.shop_keeper_inventory_draw(npc_amuna_shopkeeper, shopkeeper_items)

                if shop_button == "leave" or shop_keys[K_l]:
                    shop_button = ''
                    if len(buy_shop_elements) > 0:
                        buy_shop_elements.pop(0)
                        shopkeeper_items.clear()

                    buy_clicked = False
                    movement_able = True
                    interacted = False
                    encounter_started = False
                    in_shop = False
                    in_over_world = True

                # draw objects to screen related to shop scenario ------------------------------------------------------
                if player.current_zone == "seldon" and in_shop and not in_over_world and not in_battle and not in_inn \
                        and not in_academia and not in_npc_interaction:
                    resource_urls.screen.blit(seldon_district_shop, (0, 0))
                    resource_urls.screen.blit(buy_button.surf, buy_button.rect)
                    resource_urls.screen.blit(leave_button.surf, leave_button.rect)
                    resource_urls.screen.blit(message_box.surf, message_box.rect)
                    resource_urls.screen.blit(star_power_meter.surf, star_power_meter.rect)
                    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                    drawing_functions.text_info_draw(player, font, info_text_1, info_text_2, info_text_3,
                                                     info_text_4, in_over_world)
                    drawing_functions.draw_it()
                    resource_urls.screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                    resource_urls.screen.blit(hp_bar.surf, hp_bar.rect)
                    resource_urls.screen.blit(en_bar.surf, en_bar.rect)
                    resource_urls.screen.blit(xp_bar.surf, xp_bar.rect)

                    if buy_clicked:
                        for window in buy_shop_elements:
                            resource_urls.screen.blit(window.surf, window.rect)
                        for shop_item in shopkeeper_items:
                            resource_urls.screen.blit(shop_item.surf, shop_item.rect)
                        if len(buy_window) > 0:
                            for element in buy_window:
                                resource_urls.screen.blit(element.surf, element.rect)
                    if len(sell_window) > 0:
                        for element in sell_window:
                            resource_urls.screen.blit(element.surf, element.rect)

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in inn --------------------------------------------------------------------------------------
            if in_inn and not in_over_world and not in_shop and not in_battle and not in_academia \
                    and not in_npc_interaction:

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                    elif event.type == QUIT:
                        exit()

                    # get which button player pressed during inn scenario (rest or leave)
                    inn_button = click_handlers.inn_event_button(event, rest_button, leave_button, pygame)

                    # click handlers
                    info_choice = click_handlers.item_info_button(event, item_info_button, pygame)
                    if info_choice == "yes":
                        inventory_event = click_handlers.inventory_click_handler(player, current_info_item)
                        if inventory_event["item message"] != "":
                            info_text_1 = inventory_event["item message"]
                            info_text_2 = ""
                        drawing_functions.item_info_window.clear()
                    if info_choice == "no":
                        drawing_functions.item_info_window.clear()

                    inventory_item_clicked = click_handlers.inventory_event_item(event, pygame)
                    if inventory_item_clicked["clicked"]:
                        current_info_item = drawing_functions.item_info_draw(inventory_item_clicked["element"],
                                                                             info_items, item_info_button)

                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = click_handlers.equipment_click_handler(player, event, pygame)
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""

                # outside of inn event loop ----------------------------------------------------------------------------
                # if player has just started inn scenario, clear message box
                inn_keys = pygame.key.get_pressed()
                if not encounter_started:
                    info_text_1 = "Click rest button to sleep."
                    info_text_2 = "Sleep regains health and energy."
                    info_text_3 = ""
                    info_text_4 = ""
                    encounter_started = True
                if inn_button == "rest" or inn_keys[K_r]:
                    inn_button = ''
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
                # noinspection PyUnboundLocalVariable
                if inn_button == "leave" or inn_keys[K_l]:
                    inn_button = ''
                    rest_clicked = False
                    movement_able = True
                    interacted = False
                    encounter_started = False
                    in_inn = False
                    in_over_world = True
                    rested = False
                    faded_inn_screen = False

                # draw objects to screen related to inn scenario -------------------------------------------------------
                if player.current_zone == "seldon" and in_inn and not in_over_world and not in_shop and not in_battle \
                        and not in_academia and not in_npc_interaction:
                    # if player has just rested, fade inn screen back in with alpha value loop
                    if rested:
                        if not faded_inn_screen:
                            for alpha in range(0, 50):
                                seldon_district_inn.set_alpha(alpha)
                                resource_urls.screen.blit(seldon_district_inn, (0, 0))
                                pygame.display.flip()
                            faded_inn_screen = True
                        else:
                            seldon_district_inn.set_alpha(255)
                            resource_urls.screen.blit(seldon_district_inn, (0, 0))
                    if not rested:
                        seldon_district_inn.set_alpha(255)
                        resource_urls.screen.blit(seldon_district_inn, (0, 0))
                resource_urls.screen.blit(rest_button.surf, rest_button.rect)
                resource_urls.screen.blit(leave_button.surf, leave_button.rect)
                resource_urls.screen.blit(star_power_meter.surf, star_power_meter.rect)
                resource_urls.screen.blit(message_box.surf, message_box.rect)
                # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                drawing_functions.text_info_draw(player, font, info_text_1, info_text_2, info_text_3,
                                                 info_text_4, in_over_world)
                drawing_functions.draw_it()
                resource_urls.screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                resource_urls.screen.blit(hp_bar.surf, hp_bar.rect)
                resource_urls.screen.blit(en_bar.surf, en_bar.rect)
                resource_urls.screen.blit(xp_bar.surf, xp_bar.rect)

                if rest_clicked:
                    if not rested:
                        # set sleep screen to fade in with alpha value loop. flip each iteration to show
                        for alpha in range(0, 255):
                            nera_sleep_screen.set_alpha(alpha)
                            resource_urls.screen.blit(nera_sleep_screen, (0, 0))
                            pygame.display.flip()
                        player.health = 100
                        player.energy = 100
                        rested = True

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in academia ---------------------------------------------------------------------------------
            if in_academia and not in_over_world and not in_shop and not in_inn and not in_npc_interaction \
                    and not in_battle:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                    elif event.type == QUIT:
                        exit()
                    # get which button player pressed during academia scenario (learn or leave)
                    academia_button = click_handlers.academia_event_button(event, mage_learn_button,
                                                                           fighter_learn_button, scout_learn_button,
                                                                           leave_button, pygame)
                    # click handlers
                    info_choice = click_handlers.item_info_button(event, item_info_button, pygame)
                    if info_choice == "yes":
                        inventory_event = click_handlers.inventory_click_handler(player, current_info_item)
                        if inventory_event["item message"] != "":
                            info_text_1 = inventory_event["item message"]
                            info_text_2 = ""
                        drawing_functions.item_info_window.clear()
                    if info_choice == "no":
                        drawing_functions.item_info_window.clear()

                    inventory_item_clicked = click_handlers.inventory_event_item(event, pygame)
                    if inventory_item_clicked["clicked"]:
                        current_info_item = drawing_functions.item_info_draw(inventory_item_clicked["element"],
                                                                             info_items, item_info_button)

                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = click_handlers.equipment_click_handler(player, event, pygame)
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""

                    # get which button player pressed during book skill open (skill or close)
                    book_button = click_handlers.skill_learn_event_item(event, skill_learn_items, pygame)
                    if mage_learn_clicked:
                        try:
                            if book_button.name == "barrier learn button":
                                if not barrier_learned:
                                    if player.knowledge["mage"] > 49:
                                        player.skills_mage["skill 2"] = "barrier"
                                        info_text_1 = "'Barrier' skill learned!"
                                        info_text_2 = "Skill added. 50 knowledge used."
                                        player.knowledge["mage"] -= 50
                                        barrier_learned = True
                                    else:
                                        info_text_1 = "50 mage knowledge required to learn."
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
                                    if player.knowledge["fighter"] > 49:
                                        player.skills_fighter["skill 2"] = "hard strike"
                                        info_text_1 = "'Hard Strike' skill learned!"
                                        info_text_2 = "Skill added. 50 knowledge used."
                                        player.knowledge["fighter"] -= 50
                                        hard_strike_learned = True
                                    else:
                                        info_text_1 = "50 fighter knowledge required to learn."
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
                                    if player.knowledge["scout"] > 49:
                                        player.skills_scout["skill 2"] = "sharp sense"
                                        info_text_1 = "'Sharp Sense' skill learned!"
                                        info_text_2 = "Skill added. 50 knowledge used."
                                        player.knowledge["scout"] -= 50
                                        sharp_sense_learned = True
                                    else:
                                        info_text_1 = "50 scout knowledge required to learn."
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
                academia_keys = pygame.key.get_pressed()
                if not encounter_started:
                    info_text_1 = "Click a book to view skills."
                    info_text_2 = "Then, click a skill to learn it."
                    info_text_3 = ""
                    info_text_4 = ""
                    encounter_started = True
                if academia_button == "mage learn":
                    academia_button = ''
                    mage_learn_clicked = True
                if academia_button == "fighter learn":
                    academia_button = ''
                    fighter_learn_clicked = True
                if academia_button == "scout learn":
                    academia_button = ''
                    scout_learn_clicked = True
                # noinspection PyUnboundLocalVariable
                if academia_button == "leave" or academia_keys[K_l]:
                    academia_button = ''
                    learn_clicked = False
                    movement_able = True
                    interacted = False
                    encounter_started = False
                    in_academia = False
                    in_over_world = True
                    mage_learn_clicked = False
                    fighter_learn_clicked = False
                    scout_learn_clicked = False
                    learned = False
                    books.clear()
                    skill_learn_items.clear()

                # draw objects to screen related to academia scenario --------------------------------------------------
                if in_academia and not in_over_world and not in_shop and not in_inn and not in_npc_interaction \
                        and not in_battle:
                    if player.current_zone == "seldon":
                        resource_urls.screen.blit(seldon_district_academia, (0, 0))
                    resource_urls.screen.blit(mage_learn_button.surf, mage_learn_button.rect)
                    resource_urls.screen.blit(fighter_learn_button.surf, fighter_learn_button.rect)
                    resource_urls.screen.blit(scout_learn_button.surf, scout_learn_button.rect)
                    resource_urls.screen.blit(leave_button.surf, leave_button.rect)
                    resource_urls.screen.blit(message_box.surf, message_box.rect)
                    resource_urls.screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                    resource_urls.screen.blit(hp_bar.surf, hp_bar.rect)
                    resource_urls.screen.blit(en_bar.surf, en_bar.rect)
                    resource_urls.screen.blit(xp_bar.surf, xp_bar.rect)
                    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                    drawing_functions.text_info_draw(player, font, info_text_1, info_text_2, info_text_3,
                                                     info_text_4, in_over_world)
                    drawing_functions.draw_it()
                    for book in books:
                        resource_urls.screen.blit(book.surf, book.rect)
                    for skill_item in skill_learn_items:
                        resource_urls.screen.blit(skill_item.surf, skill_item.rect)
                    resource_urls.screen.blit(knowledge_window.surf, knowledge_window.rect)
                    text_mage_knowledge_surf = font.render(str(player.knowledge["mage"]), True, "black",
                                                           "light yellow")
                    text_mage_knowledge_rect = text_mage_knowledge_surf.get_rect()
                    text_mage_knowledge_rect.center = (515, 680)
                    resource_urls.screen.blit(text_mage_knowledge_surf, text_mage_knowledge_rect)
                    text_fighter_know_surf = font.render(str(player.knowledge["fighter"]), True, "black",
                                                         "light yellow")
                    text_fighter_know_rect = text_fighter_know_surf.get_rect()
                    text_fighter_know_rect.center = (695, 680)
                    resource_urls.screen.blit(text_fighter_know_surf, text_fighter_know_rect)
                    text_scout_knowledge_surf = font.render(str(player.knowledge["scout"]), True, "black",
                                                            "light yellow")
                    text_scout_knowledge_rect = text_scout_knowledge_surf.get_rect()
                    text_scout_knowledge_rect.center = (865, 680)
                    resource_urls.screen.blit(text_scout_knowledge_surf, text_scout_knowledge_rect)
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
            if in_npc_interaction and not in_over_world and not in_shop and not in_inn and not in_academia \
                    and not in_battle:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                    elif event.type == QUIT:
                        exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if level_up_win.rect.collidepoint(pos):
                            drawing_functions.level_up_draw(level_up_win, player, font, False)
                        if mage_select_button.rect.collidepoint(pos):
                            if not npc_garan.gift:
                                player.items.append(Item("basic staff", "mage", 0, 0, resource_urls.basic_staff_img))
                                player.items.append(Item("basic robes", "mage", 0, 0, resource_urls.basic_robes_img))
                                npc_garan.gift = True
                        if fighter_select_button.rect.collidepoint(pos):
                            if not npc_garan.gift:
                                player.items.append(Item("basic sword", "fighter", 0, 0, resource_urls.basic_sword_img))
                                player.items.append(Item("basic armor", "fighter", 0, 0, resource_urls.basic_armor_img))
                                npc_garan.gift = True
                        if scout_select_button.rect.collidepoint(pos):
                            if not npc_garan.gift:
                                player.items.append(Item("basic bow", "scout", 0, 0, resource_urls.basic_bow_img))
                                player.items.append(Item("basic tunic", "scout", 0, 0, resource_urls.basic_tunic_img))
                                npc_garan.gift = True

                    # npc was interacted with, if quest button clicked get npc name and check quest progress
                    npc_button = click_handlers.npc_event_button(event, quest_button, leave_button, pygame)
                    # in quest window pop-up, if accept or decline buttons are clicked
                    quest_buttons = click_handlers.quest_event_button(event, accept_button, decline_button, pygame)
                    # options once quest window is open ----------------------------------------------------------------
                    if quest_buttons == "accept":
                        info_text_1 = "You've accepted the quest!"
                        if current_npc_interacting.name == "garan":
                            player.quest_status["sneaky snakes"] = True
                            player.current_quests["sneaky snakes"] = "Garan asked you to defeat snakes near the river."
                        if current_npc_interacting.name == "maurelle":
                            player.quest_status["village repairs"] = True
                            player.current_quests["village repairs"] = "Maurelle asked you to " \
                                                                       "gather lumber from nearby trees."
                        if current_npc_interacting.name == "celeste":
                            player.quest_status["where's nede?"] = True
                            player.current_quests["where's nede?"] = "Celeste asked you to find her pet dog Nede. "
                        if current_npc_interacting.name == "torune":
                            player.quest_status["ghouled again"] = True
                            player.current_quests["ghouled again"] = "Torune asked you to defeat " \
                                                                     "ghouls nearby the Castle wall."
                        quest_clicked = False
                        drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                         maurelle_quest_window, celeste_quest_window,
                                                         torune_quest_window, accept_button, decline_button)
                    # if player chooses to decline, just close the quest window
                    if quest_buttons == "decline":
                        info_text_1 = ""
                        quest_clicked = False
                        drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                         maurelle_quest_window, celeste_quest_window,
                                                         torune_quest_window, accept_button, decline_button)

                    # click handlers
                    info_choice = click_handlers.item_info_button(event, item_info_button, pygame)
                    if info_choice == "yes":
                        inventory_event = click_handlers.inventory_click_handler(player, current_info_item)
                        if inventory_event["item message"] != "":
                            info_text_1 = inventory_event["item message"]
                            info_text_2 = ""
                        drawing_functions.item_info_window.clear()
                    if info_choice == "no":
                        drawing_functions.item_info_window.clear()

                    inventory_item_clicked = click_handlers.inventory_event_item(event, pygame)
                    if inventory_item_clicked["clicked"]:
                        current_info_item = drawing_functions.item_info_draw(inventory_item_clicked["element"],
                                                                             info_items, item_info_button)

                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = click_handlers.equipment_click_handler(player, event, pygame)
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""

                # outside event loop -----------------------------------------------------------------------------------
                npc_keys = pygame.key.get_pressed()
                if not encounter_started:
                    info_text_1 = ""
                    info_text_2 = ""
                    info_text_3 = ""
                    info_text_4 = ""
                    encounter_started = True

                if npc_button == "quest":
                    npc_button = ''
                    # garan npc, check player's quest progress and reward if completed ---------------------------------
                    if current_npc_interacting.name == "garan":
                        if player.quest_progress["sneaky snakes"] == 4 and not player.quest_complete["sneaky snakes"]:
                            if len(player.items) < 16:
                                player.quest_complete["sneaky snakes"] = True
                                player.current_quests["sneaky snakes"] = "You completed this quest!"
                                info_text_1 = "You've completed Garan's quest!"
                                info_text_2 = "You've gained: "
                                info_text_3 = "1 health potion. "
                                info_text_4 = "1 star, 50 xp and 10 amuna rep. "
                                player.star_power += 1
                                player.experience += 50
                                if player.experience >= 100:
                                    gameplay_functions.level_up(player, level_up_win, level_up_font)
                                player.reputation["amuna"] += 10
                                player.items.append(Item("health potion", "potion", 200, 200,
                                                         resource_urls.health_pot_img))
                            else:
                                info_text_1 = "You completed the quest, but "
                                info_text_2 = "Your inventory is full!"
                        if not quest_clicked:
                            if not player.quest_complete["sneaky snakes"]:
                                drawing_functions.quest_box_draw(current_npc_interacting, True, garan_quest_window,
                                                                 maurelle_quest_window, celeste_quest_window,
                                                                 torune_quest_window, accept_button, decline_button)
                                quest_clicked = True
                            else:
                                info_text_1 = "You've completed this quest!"
                        else:
                            drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                             maurelle_quest_window, celeste_quest_window,
                                                             torune_quest_window, accept_button, decline_button)
                            quest_clicked = False

                    # celeste npc, check player's quest progress and reward if completed -------------------------------
                    if current_npc_interacting.name == "celeste":
                        if player.quest_progress["where's nede?"] == 1 and not player.quest_complete["where's nede?"]:
                            if len(player.items) < 16:
                                player.quest_complete["where's nede?"] = True
                                player.current_quests["where's nede?"] = "You completed this quest!"
                                info_text_1 = "You've completed Celeste's quest!"
                                info_text_2 = "You've gained: "
                                info_text_3 = "1 star, 50 xp and 10 amuna rep. "
                                player.star_power += 1
                                player.experience += 50
                                if player.experience >= 100:
                                    gameplay_functions.level_up(player, level_up_win, level_up_font)
                                player.reputation["sorae"] += 10
                            else:
                                info_text_1 = "You completed the quest, but "
                                info_text_2 = "Your inventory is full!"
                        if not quest_clicked:
                            if not player.quest_complete["where's nede?"]:
                                drawing_functions.quest_box_draw(current_npc_interacting, True, garan_quest_window,
                                                                 maurelle_quest_window, celeste_quest_window,
                                                                 torune_quest_window, accept_button, decline_button)
                                quest_clicked = True
                            else:
                                info_text_1 = "You've completed this quest!"
                        else:
                            drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                             maurelle_quest_window, celeste_quest_window,
                                                             torune_quest_window, accept_button, decline_button)
                            quest_clicked = False

                    # maurelle npc, check player's quest progress and reward if completed ------------------------------
                    if current_npc_interacting.name == "maurelle":
                        if player.quest_progress["village repairs"] == 4 and not \
                                player.quest_complete["village repairs"]:
                            if len(player.items) < 16:
                                player.quest_complete["village repairs"] = True
                                player.current_quests["village repairs"] = "You completed this quest!"
                                info_text_1 = "You've completed Maurelle's quest!"
                                info_text_2 = "You've gained: "
                                info_text_3 = "1 energy potion. "
                                info_text_4 = "1 star, 50 xp and 10 amuna rep. "
                                player.star_power += 1
                                player.experience += 50
                                if player.experience >= 100:
                                    gameplay_functions.level_up(player, level_up_win, level_up_font)
                                player.reputation["amuna"] += 10
                                player.items.append(Item("energy potion", "potion", 200, 200,
                                                         resource_urls.energy_pot_img))
                            else:
                                info_text_1 = "You completed the quest, but "
                                info_text_2 = "Your inventory is full!"
                        if not quest_clicked:
                            if not player.quest_complete["village repairs"]:
                                drawing_functions.quest_box_draw(current_npc_interacting, True, garan_quest_window,
                                                                 maurelle_quest_window, celeste_quest_window,
                                                                 torune_quest_window, accept_button, decline_button)
                                quest_clicked = True
                            else:
                                info_text_1 = "You've completed this quest!"
                        else:
                            drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                             maurelle_quest_window, celeste_quest_window,
                                                             torune_quest_window, accept_button, decline_button)
                            quest_clicked = False

                    # torune npc, check player's quest progress and reward if completed --------------------------------
                    if current_npc_interacting.name == "torune":
                        if player.quest_progress["ghouled again"] == 4 and not player.quest_complete["ghouled again"]:
                            if len(player.items) < 16:
                                player.quest_complete["ghouled again"] = True
                                player.current_quests["ghouled again"] = "You completed this quest!"
                                info_text_1 = "You've completed Guard's quest!"
                                info_text_2 = "You've gained: "
                                info_text_3 = "Rohir bridge gate access. "
                                info_text_4 = "1 star, 50 xp and 10 amuna rep. "
                                player.star_power += 1
                                player.experience += 50
                                if player.experience >= 100:
                                    gameplay_functions.level_up(player, level_up_win, level_up_font)
                                player.reputation["amuna"] += 10
                            else:
                                info_text_1 = "You completed the quest, but "
                                info_text_2 = "Your inventory is full!"
                        if not quest_clicked:
                            if not player.quest_complete["ghouled again"]:
                                drawing_functions.quest_box_draw(current_npc_interacting, True, garan_quest_window,
                                                                 maurelle_quest_window, celeste_quest_window,
                                                                 torune_quest_window, accept_button, decline_button)
                                quest_clicked = True
                            else:
                                info_text_1 = "You've completed this quest!"
                        else:
                            drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                             maurelle_quest_window, celeste_quest_window,
                                                             torune_quest_window, accept_button, decline_button)
                            quest_clicked = False

                if npc_button == "leave" or npc_keys[K_l]:
                    npc_button = ''
                    movement_able = True
                    interacted = False
                    encounter_started = False
                    in_npc_interaction = False
                    in_over_world = True
                    quest_clicked = False
                    drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                     maurelle_quest_window, celeste_quest_window,
                                                     torune_quest_window, accept_button, decline_button)

                # draw objects to screen related to npc interaction scenario -------------------------------------------
                if player.current_zone == "seldon" and in_npc_interaction and not in_over_world and not in_shop \
                        and not in_inn and not in_academia and not in_battle:
                    resource_urls.screen.blit(seldon_district_battle, (0, 0))
                    resource_urls.screen.blit(player_battle_sprite.surf, player_battle_sprite.rect)
                    resource_urls.screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                    resource_urls.screen.blit(hp_bar.surf, hp_bar.rect)
                    resource_urls.screen.blit(en_bar.surf, en_bar.rect)
                    resource_urls.screen.blit(xp_bar.surf, xp_bar.rect)
                    resource_urls.screen.blit(leave_button.surf, leave_button.rect)
                    resource_urls.screen.blit(quest_button.surf, quest_button.rect)
                    resource_urls.screen.blit(npc_name_plate.surf, npc_name_plate.rect)
                    # noinspection PyUnboundLocalVariable
                    if current_npc_interacting.name == "garan":
                        resource_urls.screen.blit(npc_garan_interaction.surf, npc_garan_interaction.rect)
                    if current_npc_interacting.name == "maurelle":
                        resource_urls.screen.blit(npc_maurelle_interaction.surf, npc_maurelle_interaction.rect)
                    if current_npc_interacting.name == "celeste":
                        resource_urls.screen.blit(npc_celeste_interaction.surf, npc_celeste_interaction.rect)
                    if current_npc_interacting.name == "torune":
                        resource_urls.screen.blit(npc_torune_interaction.surf, npc_torune_interaction.rect)
                    resource_urls.screen.blit(message_box.surf, message_box.rect)
                    resource_urls.screen.blit(star_power_meter.surf, star_power_meter.rect)
                    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                    drawing_functions.text_info_draw(player, font, info_text_1, info_text_2, info_text_3,
                                                     info_text_4, in_over_world)
                    drawing_functions.draw_it()
                    text_npc_name_surf = font.render(str(current_npc_interacting.name), True, "black", "light yellow")
                    text_npc_name_rect = text_npc_name_surf.get_rect()
                    text_npc_name_rect.center = (637, 192)
                    resource_urls.screen.blit(text_npc_name_surf, text_npc_name_rect)

                    if player.quest_status["sneaky snakes"]:
                        if not npc_garan.gift:
                            resource_urls.screen.blit(role_select_overlay.surf, role_select_overlay.rect)
                            resource_urls.screen.blit(mage_select_button.surf, mage_select_button.rect)
                            resource_urls.screen.blit(fighter_select_button.surf, fighter_select_button.rect)
                            resource_urls.screen.blit(scout_select_button.surf, scout_select_button.rect)

            # ----------------------------------------------------------------------------------------------------------
            # end of whole iteration -----------------------------------------------------------------------------------
            clock.tick(60)
            pygame.display.flip()

        # --------------------------------------------------------------------------------------------------------------
        # player has died, show game over and give continue option -----------------------------------------------------
        else:
            resource_urls.screen.blit(game_over_screen, (0, 0))
            resource_urls.screen.blit(lets_go_button.surf, lets_go_button.rect)
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
                        in_over_world = True
                        # turn off barrier and restore original defence if player mage was killed while active
                        if barrier_active:
                            barrier_active = False
                            # noinspection PyUnboundLocalVariable
                            player.defense = original_defence
                        # turn off barrier and restore original defence if player mage was killed while active
                        if sharp_sense_active:
                            sharp_sense_active = False
                            # noinspection PyUnboundLocalVariable
                            player.offense = original_offense

                        if player.current_zone == "nascent":
                            player.x_coordinate = 760
                            player.y_coordinate = 510
                        if player.current_zone == "seldon":
                            player.x_coordinate = 425
                            player.y_coordinate = 690
                        if player.current_zone == "korlok":
                            player.x_coordinate = 500
                            player.y_coordinate = 500
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

                        # player returns in a weakened state
                        player.health = 25
                        player.energy = 25
                        player.alive_status = True

                        # bring enemies back to full health
                        for enemy in enemies:
                            enemy.health = 100
                            # noinspection PyTypeChecker
                            combat_scenario.enemy_health_bar(enemy)

                elif event.type == QUIT:
                    exit()

            pygame.display.flip()

if __name__ == '__exit__':
    pygame.quit()
