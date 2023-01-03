import os
import random
import sys
import time
import pygame
from pygame.locals import *

import click_handlers
import gameplay_functions
import graphics
import drawing_functions
import combat_scenario
import character_creation
import shop_scenario
import korlok
import reservoir
import rohir
import stardust
import seldon
import mines
import trail

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
        self.surf = graphic_dict["player_no_role_amuna_down_1"]
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

            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_no_role_amuna_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_amuna_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_amuna_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_amuna_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_no_role_amuna_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_amuna_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_amuna_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_amuna_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_no_role_amuna_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_amuna_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_amuna_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_amuna_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_no_role_amuna_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_amuna_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_amuna_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_amuna_right_4"]
                self.x_coordinate += velocity
        if player.role == "mage":  # -----------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_amuna_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_amuna_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_amuna_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_amuna_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_amuna_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_amuna_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_amuna_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_amuna_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_amuna_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_amuna_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_amuna_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_amuna_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_amuna_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_amuna_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_amuna_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_amuna_right_4"]
                self.x_coordinate += velocity
        if player.role == "fighter":  # --------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_amuna_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_amuna_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_amuna_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_amuna_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_amuna_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_amuna_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_amuna_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_amuna_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_amuna_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_amuna_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_amuna_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_amuna_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_amuna_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_amuna_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_amuna_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_amuna_right_4"]
                self.x_coordinate += velocity
        if player.role == "scout":  # ----------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_amuna_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_amuna_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_amuna_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_amuna_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_amuna_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_amuna_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_amuna_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_amuna_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_amuna_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_amuna_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_amuna_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_amuna_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_amuna_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_amuna_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_amuna_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_amuna_right_4"]
                self.x_coordinate += velocity
        if current_zone == "rohir":
            if self.x_coordinate < 50:
                self.x_coordinate = 50
            elif self.x_coordinate > SCREEN_WIDTH - 350:
                self.x_coordinate = SCREEN_WIDTH - 350
            if self.y_coordinate <= 140:
                self.y_coordinate = 140
            elif self.y_coordinate >= SCREEN_HEIGHT - 130:
                self.y_coordinate = SCREEN_HEIGHT - 130
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
        if current_zone == "reservoir a":
            if self.x_coordinate < 50:
                self.x_coordinate = 50
            elif self.x_coordinate > SCREEN_WIDTH - 300:
                self.x_coordinate = SCREEN_WIDTH - 300
            elif self.x_coordinate < 365:
                if self.y_coordinate > 350:
                    if self.x_coordinate > 360:
                        self.x_coordinate = 365
            elif self.x_coordinate > 680:
                if self.y_coordinate > 350:
                    if self.x_coordinate < 685:
                        self.x_coordinate = 680
            if self.y_coordinate <= 125:
                self.y_coordinate = 125
            elif self.x_coordinate < 360 or self.x_coordinate > 725:
                if self.y_coordinate >= SCREEN_HEIGHT - 200:
                    self.y_coordinate = SCREEN_HEIGHT - 200
            elif self.x_coordinate > 300 or self.x_coordinate < 725:
                if self.y_coordinate >= SCREEN_HEIGHT:
                    self.y_coordinate = SCREEN_HEIGHT
        if current_zone == "reservoir b":
            if self.x_coordinate < 60:
                self.x_coordinate = 60
            elif self.x_coordinate < SCREEN_WIDTH - 535:
                if self.x_coordinate > SCREEN_WIDTH - 575:
                    self.x_coordinate = SCREEN_WIDTH - 535
            if self.x_coordinate < SCREEN_WIDTH - 575:
                if self.x_coordinate > SCREEN_WIDTH - 625:
                    self.x_coordinate = SCREEN_WIDTH - 625
            elif self.x_coordinate > SCREEN_WIDTH - 275:
                self.x_coordinate = SCREEN_WIDTH - 275
            if self.y_coordinate <= 75:
                self.y_coordinate = 75
            elif self.x_coordinate > SCREEN_WIDTH - 575:
                if self.y_coordinate >= SCREEN_HEIGHT:
                    self.y_coordinate = SCREEN_HEIGHT
            else:
                if self.y_coordinate >= SCREEN_HEIGHT - 50:
                    self.y_coordinate = SCREEN_HEIGHT - 50
        if current_zone == "reservoir c":
            if self.x_coordinate < 90:
                self.x_coordinate = 90
            if self.x_coordinate > SCREEN_WIDTH - 275:
                self.x_coordinate = SCREEN_WIDTH - 275
            if self.y_coordinate >= SCREEN_HEIGHT - 82:
                self.y_coordinate = SCREEN_HEIGHT - 82
            if self.x_coordinate > 510:
                if self.y_coordinate < 400:
                    if self.y_coordinate <= 100:
                        self.y_coordinate = 100
                    if self.y_coordinate > 320:
                        self.y_coordinate = 320
                if self.y_coordinate > 400:
                    if self.y_coordinate <= 425:
                        self.y_coordinate = 425
            else:
                if self.y_coordinate <= 100:
                    self.y_coordinate = 100
                if 425 > self.y_coordinate > 320:
                    if self.x_coordinate > 505:
                        self.x_coordinate = 505
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
            elif self.x_coordinate > SCREEN_WIDTH - 275:
                self.x_coordinate = SCREEN_WIDTH - 275
            elif self.x_coordinate < 490 and 325 < self.y_coordinate < 400:
                self.y_coordinate = 400
            elif self.x_coordinate < 490 and 400 > self.y_coordinate > 300:
                self.y_coordinate = 300
            elif self.x_coordinate < 492 and 325 < self.y_coordinate < 400:
                self.x_coordinate = 492
            if self.y_coordinate <= 50:
                self.y_coordinate = 50
            elif self.y_coordinate >= SCREEN_HEIGHT - 93:
                self.y_coordinate = SCREEN_HEIGHT - 93
        if current_zone == "mines":
            if self.x_coordinate < 72:
                self.x_coordinate = 72
            elif self.x_coordinate > SCREEN_WIDTH - 315:
                self.x_coordinate = SCREEN_WIDTH - 315
            if self.y_coordinate <= 115:
                self.y_coordinate = 115
            elif self.x_coordinate < 660:
                if self.y_coordinate >= SCREEN_HEIGHT - 75:
                    self.y_coordinate = SCREEN_HEIGHT - 75
            elif self.x_coordinate > 660:
                if self.y_coordinate >= SCREEN_HEIGHT:
                    self.y_coordinate = SCREEN_HEIGHT
        if current_zone == "terra trail":
            if self.x_coordinate < 50:
                self.x_coordinate = 50
            elif self.x_coordinate > SCREEN_WIDTH - 550:
                self.x_coordinate = SCREEN_WIDTH - 550

            if self.y_coordinate <= 70:
                self.y_coordinate = 70
            elif self.y_coordinate >= SCREEN_HEIGHT - 130:
                self.y_coordinate = SCREEN_HEIGHT - 130

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
        if current_zone == "korlok":
            collided = pygame.sprite.spritecollideany(player, nuldar_buildings, pygame.sprite.collide_rect_ratio(0.50))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "mines":
            if pygame.sprite.collide_rect(player, mines_wall):
                if player.x_coordinate < mines_wall.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > mines_wall.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < mines_wall.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > mines_wall.y_coordinate:
                    self.y_coordinate += velocity
            if pygame.sprite.collide_rect(player, mines_light):
                if player.x_coordinate < mines_light.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > mines_light.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < mines_light.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > mines_light.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "reservoir a":
            if mini_boss_1 or mini_boss_2:
                if pygame.sprite.collide_rect(player, dungeon_drop_wall):
                    if player.x_coordinate < dungeon_drop_wall.x_coordinate:
                        self.x_coordinate -= velocity
                    if player.x_coordinate > dungeon_drop_wall.x_coordinate:
                        self.x_coordinate += velocity
                    if player.y_coordinate < dungeon_drop_wall.y_coordinate:
                        self.y_coordinate -= velocity
                    if player.y_coordinate > dungeon_drop_wall.y_coordinate:
                        self.y_coordinate += velocity
            collided = pygame.sprite.spritecollideany(player, dungeon_walls, pygame.sprite.collide_rect_ratio(0.75))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "reservoir b":
            collided = pygame.sprite.spritecollideany(player, muchador_crates, pygame.sprite.collide_rect_ratio(0.75))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "reservoir c":
            collided = pygame.sprite.spritecollideany(player, dungeon_rocks, pygame.sprite.collide_rect_ratio(0.90))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
            if pygame.Rect.colliderect(player.rect, dungeon_chest_rect):
                if player.x_coordinate < dungeon_chest_rect.x:
                    self.x_coordinate -= velocity
                if player.x_coordinate > dungeon_chest_rect.x:
                    self.x_coordinate += velocity
                if player.y_coordinate < dungeon_chest_rect.y:
                    self.y_coordinate -= velocity
                if player.y_coordinate > dungeon_chest_rect.y:
                    self.y_coordinate += velocity
        if current_zone == "terra trail":
            if pygame.sprite.collide_rect(player, terra_mountains):
                if player.x_coordinate < terra_mountains.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > terra_mountains.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < terra_mountains.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > terra_mountains.y_coordinate:
                    self.y_coordinate += velocity
            if pygame.sprite.collide_rect(player, terra_cave):
                if player.x_coordinate < terra_cave.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > terra_cave.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < terra_cave.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > terra_cave.y_coordinate:
                    self.y_coordinate += velocity

        self.rect.midbottom = (self.x_coordinate, self.y_coordinate)


class PlayerNuldar(pygame.sprite.Sprite):
    def __init__(self, name, race, role, items, p_equipment, current_quests, quest_progress, quest_status,
                 quest_complete, knowledge, skills_mage, skills_fighter, skills_scout, level, experience, health,
                 energy, alive_status, rupees, reputation, current_zone, defense, offense, star_power):
        super(PlayerNuldar, self).__init__()
        self.x_coordinate = 760
        self.y_coordinate = 510
        self.surf = graphic_dict["player_no_role_amuna_down_1"]
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
                    self.surf = graphic_dict["player_no_role_nuldar_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_nuldar_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_nuldar_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_nuldar_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_no_role_nuldar_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_nuldar_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_nuldar_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_nuldar_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_no_role_nuldar_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_nuldar_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_nuldar_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_nuldar_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_no_role_nuldar_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_nuldar_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_nuldar_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_nuldar_right_4"]
                self.x_coordinate += velocity
        if player.role == "mage":  # -----------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_nuldar_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_nuldar_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_nuldar_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_nuldar_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_nuldar_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_nuldar_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_nuldar_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_nuldar_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_nuldar_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_nuldar_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_nuldar_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_nuldar_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_nuldar_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_nuldar_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_nuldar_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_nuldar_right_4"]
                self.x_coordinate += velocity
        if player.role == "fighter":  # --------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_nuldar_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_nuldar_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_nuldar_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_nuldar_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_nuldar_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_nuldar_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_nuldar_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_nuldar_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_nuldar_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_nuldar_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_nuldar_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_nuldar_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_nuldar_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_nuldar_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_nuldar_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_nuldar_right_4"]
                self.x_coordinate += velocity
        if player.role == "scout":  # ----------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_nuldar_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_nuldar_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_nuldar_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_nuldar_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_nuldar_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_nuldar_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_nuldar_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_nuldar_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_nuldar_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_nuldar_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_nuldar_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_nuldar_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_nuldar_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_nuldar_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_nuldar_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_nuldar_right_4"]
                self.x_coordinate += velocity
        if current_zone == "rohir":
            if self.x_coordinate < 50:
                self.x_coordinate = 50
            elif self.x_coordinate > SCREEN_WIDTH - 350:
                self.x_coordinate = SCREEN_WIDTH - 350
            if self.y_coordinate <= 140:
                self.y_coordinate = 140
            elif self.y_coordinate >= SCREEN_HEIGHT - 130:
                self.y_coordinate = SCREEN_HEIGHT - 130
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
        if current_zone == "reservoir a":
            if self.x_coordinate < 50:
                self.x_coordinate = 50
            elif self.x_coordinate > SCREEN_WIDTH - 300:
                self.x_coordinate = SCREEN_WIDTH - 300
            elif self.x_coordinate < 365:
                if self.y_coordinate > 350:
                    if self.x_coordinate > 360:
                        self.x_coordinate = 365
            elif self.x_coordinate > 680:
                if self.y_coordinate > 350:
                    if self.x_coordinate < 685:
                        self.x_coordinate = 680
            if self.y_coordinate <= 125:
                self.y_coordinate = 125
            elif self.x_coordinate < 360 or self.x_coordinate > 725:
                if self.y_coordinate >= SCREEN_HEIGHT - 200:
                    self.y_coordinate = SCREEN_HEIGHT - 200
            elif self.x_coordinate > 300 or self.x_coordinate < 725:
                if self.y_coordinate >= SCREEN_HEIGHT:
                    self.y_coordinate = SCREEN_HEIGHT
        if current_zone == "reservoir b":
            if self.x_coordinate < 60:
                self.x_coordinate = 60
            elif self.x_coordinate < SCREEN_WIDTH - 535:
                if self.x_coordinate > SCREEN_WIDTH - 575:
                    self.x_coordinate = SCREEN_WIDTH - 535
            if self.x_coordinate < SCREEN_WIDTH - 575:
                if self.x_coordinate > SCREEN_WIDTH - 625:
                    self.x_coordinate = SCREEN_WIDTH - 625
            elif self.x_coordinate > SCREEN_WIDTH - 275:
                self.x_coordinate = SCREEN_WIDTH - 275
            if self.y_coordinate <= 75:
                self.y_coordinate = 75
            elif self.x_coordinate > SCREEN_WIDTH - 575:
                if self.y_coordinate >= SCREEN_HEIGHT:
                    self.y_coordinate = SCREEN_HEIGHT
            else:
                if self.y_coordinate >= SCREEN_HEIGHT - 50:
                    self.y_coordinate = SCREEN_HEIGHT - 50
        if current_zone == "reservoir c":
            if self.x_coordinate < 90:
                self.x_coordinate = 90
            if self.x_coordinate > SCREEN_WIDTH - 275:
                self.x_coordinate = SCREEN_WIDTH - 275
            if self.y_coordinate >= SCREEN_HEIGHT - 82:
                self.y_coordinate = SCREEN_HEIGHT - 82
            if self.x_coordinate > 510:
                if self.y_coordinate < 400:
                    if self.y_coordinate <= 100:
                        self.y_coordinate = 100
                    if self.y_coordinate > 320:
                        self.y_coordinate = 320
                if self.y_coordinate > 400:
                    if self.y_coordinate <= 425:
                        self.y_coordinate = 425
            else:
                if self.y_coordinate <= 100:
                    self.y_coordinate = 100
                if 425 > self.y_coordinate > 320:
                    if self.x_coordinate > 505:
                        self.x_coordinate = 505
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
            elif self.x_coordinate > SCREEN_WIDTH - 275:
                self.x_coordinate = SCREEN_WIDTH - 275
            elif self.x_coordinate < 490 and 325 < self.y_coordinate < 400:
                self.y_coordinate = 400
            elif self.x_coordinate < 490 and 400 > self.y_coordinate > 300:
                self.y_coordinate = 300
            elif self.x_coordinate < 492 and 325 < self.y_coordinate < 400:
                self.x_coordinate = 492
            if self.y_coordinate <= 50:
                self.y_coordinate = 50
            elif self.y_coordinate >= SCREEN_HEIGHT - 93:
                self.y_coordinate = SCREEN_HEIGHT - 93
        if current_zone == "mines":
            if self.x_coordinate < 72:
                self.x_coordinate = 72
            elif self.x_coordinate > SCREEN_WIDTH - 315:
                self.x_coordinate = SCREEN_WIDTH - 315
            if self.y_coordinate <= 115:
                self.y_coordinate = 115
            elif self.x_coordinate < 660:
                if self.y_coordinate >= SCREEN_HEIGHT - 75:
                    self.y_coordinate = SCREEN_HEIGHT - 75
            elif self.x_coordinate > 660:
                if self.y_coordinate >= SCREEN_HEIGHT:
                    self.y_coordinate = SCREEN_HEIGHT
        if current_zone == "terra trail":
            if self.x_coordinate < 50:
                self.x_coordinate = 50
            elif self.x_coordinate > SCREEN_WIDTH - 550:
                self.x_coordinate = SCREEN_WIDTH - 550

            if self.y_coordinate <= 70:
                self.y_coordinate = 70
            elif self.y_coordinate >= SCREEN_HEIGHT - 130:
                self.y_coordinate = SCREEN_HEIGHT - 130

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
        if current_zone == "korlok":
            collided = pygame.sprite.spritecollideany(player, nuldar_buildings, pygame.sprite.collide_rect_ratio(0.50))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "mines":
            if pygame.sprite.collide_rect(player, mines_wall):
                if player.x_coordinate < mines_wall.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > mines_wall.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < mines_wall.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > mines_wall.y_coordinate:
                    self.y_coordinate += velocity
            if pygame.sprite.collide_rect(player, mines_light):
                if player.x_coordinate < mines_light.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > mines_light.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < mines_light.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > mines_light.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "reservoir a":
            if mini_boss_1 or mini_boss_2:
                if pygame.sprite.collide_rect(player, dungeon_drop_wall):
                    if player.x_coordinate < dungeon_drop_wall.x_coordinate:
                        self.x_coordinate -= velocity
                    if player.x_coordinate > dungeon_drop_wall.x_coordinate:
                        self.x_coordinate += velocity
                    if player.y_coordinate < dungeon_drop_wall.y_coordinate:
                        self.y_coordinate -= velocity
                    if player.y_coordinate > dungeon_drop_wall.y_coordinate:
                        self.y_coordinate += velocity
            collided = pygame.sprite.spritecollideany(player, dungeon_walls, pygame.sprite.collide_rect_ratio(0.75))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "reservoir b":
            collided = pygame.sprite.spritecollideany(player, muchador_crates, pygame.sprite.collide_rect_ratio(0.75))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "reservoir c":
            collided = pygame.sprite.spritecollideany(player, dungeon_rocks, pygame.sprite.collide_rect_ratio(0.90))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
            if pygame.Rect.colliderect(player.rect, dungeon_chest_rect):
                if player.x_coordinate < dungeon_chest_rect.x:
                    self.x_coordinate -= velocity
                if player.x_coordinate > dungeon_chest_rect.x:
                    self.x_coordinate += velocity
                if player.y_coordinate < dungeon_chest_rect.y:
                    self.y_coordinate -= velocity
                if player.y_coordinate > dungeon_chest_rect.y:
                    self.y_coordinate += velocity
        if current_zone == "terra trail":
            if pygame.sprite.collide_rect(player, terra_mountains):
                if player.x_coordinate < terra_mountains.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > terra_mountains.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < terra_mountains.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > terra_mountains.y_coordinate:
                    self.y_coordinate += velocity
            if pygame.sprite.collide_rect(player, terra_cave):
                if player.x_coordinate < terra_cave.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > terra_cave.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < terra_cave.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > terra_cave.y_coordinate:
                    self.y_coordinate += velocity

        self.rect.midbottom = (self.x_coordinate, self.y_coordinate)


class PlayerSorae(pygame.sprite.Sprite):
    def __init__(self, name, race, role, items, p_equipment, current_quests, quest_progress, quest_status,
                 quest_complete, knowledge, skills_mage, skills_fighter, skills_scout, level, experience, health,
                 energy, alive_status, rupees, reputation, current_zone, defense, offense, star_power):
        super(PlayerSorae, self).__init__()
        self.x_coordinate = 760
        self.y_coordinate = 510
        self.surf = graphic_dict["player_no_role_amuna_down_1"]
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
                    self.surf = graphic_dict["player_no_role_sorae_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_sorae_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_sorae_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_sorae_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_no_role_sorae_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_sorae_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_sorae_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_sorae_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_no_role_sorae_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_sorae_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_sorae_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_sorae_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_no_role_sorae_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_no_role_sorae_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_no_role_sorae_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_no_role_sorae_right_4"]
                self.x_coordinate += velocity
        if player.role == "mage":  # -----------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_sorae_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_sorae_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_sorae_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_sorae_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_sorae_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_sorae_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_sorae_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_sorae_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_sorae_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_sorae_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_sorae_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_sorae_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_mage_sorae_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_mage_sorae_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_mage_sorae_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_mage_sorae_right_4"]
                self.x_coordinate += velocity
        if player.role == "fighter":  # --------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_sorae_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_sorae_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_sorae_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_sorae_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_sorae_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_sorae_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_sorae_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_sorae_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_sorae_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_sorae_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_sorae_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_sorae_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_fighter_sorae_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_fighter_sorae_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_fighter_sorae_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_fighter_sorae_right_4"]
                self.x_coordinate += velocity
        if player.role == "scout":  # ----------------------------------------------------------------------------------
            if pressed_key == "up":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_sorae_up_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_sorae_up_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_sorae_up_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_sorae_up_4"]
                self.y_coordinate -= velocity
            if pressed_key == "down":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_sorae_down_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_sorae_down_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_sorae_down_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_sorae_down_4"]
                self.y_coordinate += velocity
            if pressed_key == "left":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_sorae_left_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_sorae_left_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_sorae_left_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_sorae_left_4"]
                self.x_coordinate -= velocity
            if pressed_key == "right":
                if walk_timed < 0.2:
                    self.surf = graphic_dict["player_scout_sorae_right_1"]
                if walk_timed > 0.2:
                    self.surf = graphic_dict["player_scout_sorae_right_2"]
                if walk_timed > 0.4:
                    self.surf = graphic_dict["player_scout_sorae_right_3"]
                if walk_timed > 0.6:
                    self.surf = graphic_dict["player_scout_sorae_right_4"]
                self.x_coordinate += velocity
        if current_zone == "rohir":
            if self.x_coordinate < 50:
                self.x_coordinate = 50
            elif self.x_coordinate > SCREEN_WIDTH - 350:
                self.x_coordinate = SCREEN_WIDTH - 350
            if self.y_coordinate <= 140:
                self.y_coordinate = 140
            elif self.y_coordinate >= SCREEN_HEIGHT - 130:
                self.y_coordinate = SCREEN_HEIGHT - 130
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
        if current_zone == "reservoir a":
            if self.x_coordinate < 50:
                self.x_coordinate = 50
            elif self.x_coordinate > SCREEN_WIDTH - 300:
                self.x_coordinate = SCREEN_WIDTH - 300
            elif self.x_coordinate < 365:
                if self.y_coordinate > 350:
                    if self.x_coordinate > 360:
                        self.x_coordinate = 365
            elif self.x_coordinate > 680:
                if self.y_coordinate > 350:
                    if self.x_coordinate < 685:
                        self.x_coordinate = 680
            if self.y_coordinate <= 125:
                self.y_coordinate = 125
            elif self.x_coordinate < 360 or self.x_coordinate > 725:
                if self.y_coordinate >= SCREEN_HEIGHT - 200:
                    self.y_coordinate = SCREEN_HEIGHT - 200
            elif self.x_coordinate > 300 or self.x_coordinate < 725:
                if self.y_coordinate >= SCREEN_HEIGHT:
                    self.y_coordinate = SCREEN_HEIGHT
        if current_zone == "reservoir b":
            if self.x_coordinate < 60:
                self.x_coordinate = 60
            elif self.x_coordinate < SCREEN_WIDTH - 535:
                if self.x_coordinate > SCREEN_WIDTH - 575:
                    self.x_coordinate = SCREEN_WIDTH - 535
            if self.x_coordinate < SCREEN_WIDTH - 575:
                if self.x_coordinate > SCREEN_WIDTH - 625:
                    self.x_coordinate = SCREEN_WIDTH - 625
            elif self.x_coordinate > SCREEN_WIDTH - 275:
                self.x_coordinate = SCREEN_WIDTH - 275
            if self.y_coordinate <= 75:
                self.y_coordinate = 75
            elif self.x_coordinate > SCREEN_WIDTH - 575:
                if self.y_coordinate >= SCREEN_HEIGHT:
                    self.y_coordinate = SCREEN_HEIGHT
            else:
                if self.y_coordinate >= SCREEN_HEIGHT - 50:
                    self.y_coordinate = SCREEN_HEIGHT - 50
        if current_zone == "reservoir c":
            if self.x_coordinate < 90:
                self.x_coordinate = 90
            if self.x_coordinate > SCREEN_WIDTH - 275:
                self.x_coordinate = SCREEN_WIDTH - 275
            if self.y_coordinate >= SCREEN_HEIGHT - 82:
                self.y_coordinate = SCREEN_HEIGHT - 82
            if self.x_coordinate > 510:
                if self.y_coordinate < 400:
                    if self.y_coordinate <= 100:
                        self.y_coordinate = 100
                    if self.y_coordinate > 320:
                        self.y_coordinate = 320
                if self.y_coordinate > 400:
                    if self.y_coordinate <= 425:
                        self.y_coordinate = 425
            else:
                if self.y_coordinate <= 100:
                    self.y_coordinate = 100
                if 425 > self.y_coordinate > 320:
                    if self.x_coordinate > 505:
                        self.x_coordinate = 505
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
            elif self.x_coordinate > SCREEN_WIDTH - 275:
                self.x_coordinate = SCREEN_WIDTH - 275
            elif self.x_coordinate < 490 and 325 < self.y_coordinate < 400:
                self.y_coordinate = 400
            elif self.x_coordinate < 490 and 400 > self.y_coordinate > 300:
                self.y_coordinate = 300
            elif self.x_coordinate < 492 and 325 < self.y_coordinate < 400:
                self.x_coordinate = 492
            if self.y_coordinate <= 50:
                self.y_coordinate = 50
            elif self.y_coordinate >= SCREEN_HEIGHT - 93:
                self.y_coordinate = SCREEN_HEIGHT - 93
        if current_zone == "mines":
            if self.x_coordinate < 72:
                self.x_coordinate = 72
            elif self.x_coordinate > SCREEN_WIDTH - 315:
                self.x_coordinate = SCREEN_WIDTH - 315
            if self.y_coordinate <= 115:
                self.y_coordinate = 115
            elif self.x_coordinate < 660:
                if self.y_coordinate >= SCREEN_HEIGHT - 75:
                    self.y_coordinate = SCREEN_HEIGHT - 75
            elif self.x_coordinate > 660:
                if self.y_coordinate >= SCREEN_HEIGHT:
                    self.y_coordinate = SCREEN_HEIGHT
        if current_zone == "terra trail":
            if self.x_coordinate < 50:
                self.x_coordinate = 50
            elif self.x_coordinate > SCREEN_WIDTH - 550:
                self.x_coordinate = SCREEN_WIDTH - 550

            if self.y_coordinate <= 70:
                self.y_coordinate = 70
            elif self.y_coordinate >= SCREEN_HEIGHT - 130:
                self.y_coordinate = SCREEN_HEIGHT - 130

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
        if current_zone == "korlok":
            collided = pygame.sprite.spritecollideany(player, nuldar_buildings, pygame.sprite.collide_rect_ratio(0.50))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "mines":
            if pygame.sprite.collide_rect(player, mines_wall):
                if player.x_coordinate < mines_wall.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > mines_wall.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < mines_wall.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > mines_wall.y_coordinate:
                    self.y_coordinate += velocity
            if pygame.sprite.collide_rect(player, mines_light):
                if player.x_coordinate < mines_light.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > mines_light.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < mines_light.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > mines_light.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "reservoir a":
            if mini_boss_1 or mini_boss_2:
                if pygame.sprite.collide_rect(player, dungeon_drop_wall):
                    if player.x_coordinate < dungeon_drop_wall.x_coordinate:
                        self.x_coordinate -= velocity
                    if player.x_coordinate > dungeon_drop_wall.x_coordinate:
                        self.x_coordinate += velocity
                    if player.y_coordinate < dungeon_drop_wall.y_coordinate:
                        self.y_coordinate -= velocity
                    if player.y_coordinate > dungeon_drop_wall.y_coordinate:
                        self.y_coordinate += velocity
            collided = pygame.sprite.spritecollideany(player, dungeon_walls, pygame.sprite.collide_rect_ratio(0.75))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "reservoir b":
            collided = pygame.sprite.spritecollideany(player, muchador_crates, pygame.sprite.collide_rect_ratio(0.75))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
        if current_zone == "reservoir c":
            collided = pygame.sprite.spritecollideany(player, dungeon_rocks, pygame.sprite.collide_rect_ratio(0.90))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity
            if pygame.Rect.colliderect(player.rect, dungeon_chest_rect):
                if player.x_coordinate < dungeon_chest_rect.x:
                    self.x_coordinate -= velocity
                if player.x_coordinate > dungeon_chest_rect.x:
                    self.x_coordinate += velocity
                if player.y_coordinate < dungeon_chest_rect.y:
                    self.y_coordinate -= velocity
                if player.y_coordinate > dungeon_chest_rect.y:
                    self.y_coordinate += velocity
        if current_zone == "terra trail":
            if pygame.sprite.collide_rect(player, terra_mountains):
                if player.x_coordinate < terra_mountains.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > terra_mountains.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < terra_mountains.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > terra_mountains.y_coordinate:
                    self.y_coordinate += velocity
            if pygame.sprite.collide_rect(player, terra_cave):
                if player.x_coordinate < terra_cave.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > terra_cave.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < terra_cave.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > terra_cave.y_coordinate:
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
                 health_bar, type):
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
        self.type = type

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
                self.x_coordinate -= 1
            if direction_x == "right":
                self.x_coordinate += 1
        else:
            if direction_x == "left":
                self.x_coordinate += 1
            if direction_x == "right":
                self.x_coordinate -= 1
        if ranges_y[0] < self.rect.x < ranges_y[1]:
            if direction_y == "down":
                self.y_coordinate -= 1
            if direction_y == "up":
                self.y_coordinate += 1
        else:
            if direction_y == "down":
                self.y_coordinate += 1
            if direction_y == "up":
                self.y_coordinate -= 1

        self.rect = self.surf.get_rect(center=(self.x_coordinate, self.y_coordinate))


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
    def __init__(self, name, types, x_coordinate, y_coordinate, image, level):
        super(Item, self).__init__()
        self.name = name
        self.type = types
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.level = level

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))

    def update_level(self, name, level, image):
        self.name = name
        self.level = level
        self.image = image


# ----------------------------------------------------------------------------------------------------------------------
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def button_highlighter(posit):
    button_highlighters = drawing_functions.button_highlights(pygame, player, start_chosen, new_game_chosen,
                                                              new_game_button, posit, button_highlight, graphic_dict,
                                                              continue_button, start_button, back_button, amuna_button,
                                                              nuldar_button, sorae_button, save_check_window,
                                                              yes_button, no_button, item_info_button, rest_button,
                                                              leave_button, buy_button, in_inn, in_shop, buy_clicked,
                                                              offense_select_button, in_battle,
                                                              mage_attack_button, fighter_attack_button,
                                                              scout_attack_button, no_role_attack_button,
                                                              barrier_button, sharp_sense_button, hard_strike_button,
                                                              in_over_world, seldon_map_button, korlok_map_button,
                                                              eldream_map_button, marrow_map_button, character_button,
                                                              quests_button, save_button, map_button,
                                                              in_npc_interaction, quest_button, quest_clicked,
                                                              accept_button, decline_button, in_apothecary, staff,
                                                              sword, bow)
    return button_highlighters


if __name__ == '__main__':
    # ------------------------------------------------------------------------------------------------------------------
    # initialize the screen in graphics file, return here. draw loading screen, then load from graphics file into dict
    screen = graphics.initialize_display()
    graphics.draw_loading_screen(screen)
    # dictionary contains all graphical resources
    graphic_dict = graphics.load_graphics()
    # pygame.mixer.init()

    # background textures ----------------------------------------------------------------------------------------------
    nascent_grove_bg = graphic_dict["nascent_grove_screen"]
    rohir_river_bg = graphic_dict["rohir_river_screen"]
    seldon_district_bg = graphic_dict["seldon_bg_screen"]
    seldon_district_battle = graphic_dict["seldon_battle_screen"]
    korlok_district_battle = graphic_dict["korlok_battle_screen"]
    mines_battle = graphic_dict["mines_battle_screen"]
    seldon_district_shop = graphic_dict["seldon_shop_screen"]
    korlok_district_shop = graphic_dict["korlok_shop_screen"]
    seldon_district_inn = graphic_dict["seldon_inn_screen"]
    korlok_district_inn = graphic_dict["korlok_inn_screen"]
    seldon_district_academia = graphic_dict["seldon_academia_screen"]
    korlok_district_apothecary = graphic_dict["korlok_apothecary"]
    stardust_cove_bg = graphic_dict["stardust_cove_screen"]
    stardust_post_bg = graphic_dict["stardust_post_screen"]
    stardust_battle = graphic_dict["star_battle_screen"]
    seldon_hearth_screen = graphic_dict["seldon_hearth_screen"]
    korlok_hearth_screen = graphic_dict["korlok_hearth_screen"]
    game_over_screen = graphic_dict["game_over_screen"]
    start_screen = graphic_dict["start_screen"]
    nera_sleep_screen = graphic_dict["nera_sleep_screen"]
    korlok_district_bg = graphic_dict["korlok_bg_screen"]
    korlok_mines_bg = graphic_dict["korlok_mines"]
    amuna_character_screen = graphic_dict["a_char_screen"]
    nuldar_character_screen = graphic_dict["n_char_screen"]
    sorae_character_screen = graphic_dict["s_char_screen"]
    reservoir_a_bg = graphic_dict["reservoir_a_screen"]
    reservoir_b_bg = graphic_dict["reservoir_b_screen"]
    reservoir_c_bg = graphic_dict["reservoir_c_screen"]
    reservoir_battle = graphic_dict["reservoir_battle_screen"]
    mountain_trail_bg = graphic_dict["mountain_trail_bg"]
    terra_trail_screen = graphic_dict["terra_trail_screen"]
    caves_battle_screen = graphic_dict["caves_battle_screen"]

    # cutscenes --------------------------------------------------------------------------------------------------------
    apothis_scene_1 = graphic_dict["apothis_1"]
    apothis_scene_2 = graphic_dict["apothis_2"]
    apothis_scene_3 = graphic_dict["apothis_3"]
    apothis_scene_4 = graphic_dict["apothis_4"]
    apothis_scene_5 = graphic_dict["apothis_5"]
    apothis_scene_6 = graphic_dict["apothis_6"]

    # display notifications --------------------------------------------------------------------------------------------
    knowledge_academia = Notification("knowledge academia notification", False, 510, 365,
                                      graphic_dict["knowledge_popup"])
    rest_recover = Notification("rest recover", False, 510, 365, graphic_dict["health_popup"])
    shop_gear = Notification("shop gear", False, 510, 365, graphic_dict["gear_popup"])
    save_check = Notification("save check", False, 510, 365, graphic_dict["save_popup"])
    save_absent = Notification("save absent", False, 640, 574, graphic_dict["save_not_found"])
    first_quest = Notification("first quest", False, 510, 365, graphic_dict["quest_popup"])
    # inventory items
    health_potion = Item("health potion", "potion", 200, 200, graphic_dict["health_pot_img"], 0)
    energy_potion = Item("energy potion", "potion", 200, 200, graphic_dict["energy_pot_img"], 0)
    shiny_rock = Item("shiny rock", "rock", 200, 200, graphic_dict["shiny_rock_img"], 0)
    bone_dust = Item("bone dust", "dust", 200, 200, graphic_dict["bone_dust_img"], 0)
    # weapons
    staff = UiElement("staff", 1077, 283, graphic_dict["staff_1"])
    sword = UiElement("sword", 1155, 283, graphic_dict["sword_1"])
    bow = UiElement("bow", 1230, 283, graphic_dict["bow_1"])
    # armor
    basic_armor = Item("basic armor", "armor", 1078, 197, graphic_dict["basic_armor"], 1)
    forged_armor = Item("forged armor", "armor", 1078, 197, graphic_dict["forged_armor"], 2)
    mythical_armor = Item("mythical armor", "armor", 1078, 197, graphic_dict["mythical_armor"], 3)
    legendary_armor = Item("legendary armor", "armor", 1078, 197, graphic_dict["legendary_armor"], 4)
    # equipment items
    power_gloves = Item("power gloves", "gloves", 1153, 197, graphic_dict["gloves"], 0)
    # character selection
    amuna_character = UiElement("amuna character", 640, 360, graphic_dict["amuna_character_img"])
    nuldar_character = UiElement("nuldar character", 640, 360, graphic_dict["nuldar_character_img"])
    sorae_character = UiElement("sorae character", 640, 360, graphic_dict["sorae_character_img"])

    # default player
    player = PlayerAmuna("stan", "amuna", "",  # name, race, role
                         [],  # inventory
                         {"weapon": "", "armor": "", "gloves": "", "boots": ""},
                         {"sneaky snakes": "Speak to Garan to start this quest.",
                          "village repairs": "Speak to Maurelle to start this quest.",
                          "where's nede?": "Speak to Celeste to start this quest",
                          "ghouled again": "Speak to the gate Guard to start this quest.",
                          "band hammer": "Speak to Voruke to start this quest.",
                          "elementary elementals": "Speak to Zerah to start this quest.",
                          "can't apothecary it": "Speak to the apothecary owner to start this quest.",
                          "it's dangerous to go alone": "Speak to Dionte to start this quest"},
                         {"sneaky snakes": 0, "village repairs": 0, "where's nede?": 0, "ghouled again": 0,
                          "band hammer": 0, "elementary elementals": 0, "can't apothecary it": 0,
                          "it's dangerous to go alone": 0},
                         {"sneaky snakes": False, "village repairs": False, "where's nede?": False,
                          "ghouled again": False, "band hammer": False, "elementary elementals": False,
                          "can't apothecary it": False, "it's dangerous to go alone": False},
                         {"sneaky snakes": False, "village repairs": False, "where's nede?": False,
                          "ghouled again": False, "band hammer": False, "elementary elementals": False,
                          "can't apothecary it": False, "it's dangerous to go alone": False},
                         {"mage": 0, "fighter": 0, "scout": 0},  # role knowledge ('role', 'amount')
                         {"skill 2": "", "skill 3": "", "skill 4": ""},  # mage skills
                         {"skill 2": "", "skill 3": "", "skill 4": ""},  # fighter skills
                         {"skill 2": "", "skill 3": "", "skill 4": ""},  # scout skills
                         1, 0, 100, 100,  # lvl, exp, health, energy
                         True, 0, {"amuna": 0, "nuldar": 0, "sorae": 0},  # alive, rupees, reputation
                         "", 0, 1, 0)  # zone, defence, offense, image

    # npcs: name, gender, race, role, dialog, quest, quest_description, x_coordinate, y_coordinate
    #                  alive_status, quest_complete, items, gift, image
    npc_garan = NPC("garan", "amuna", "It's dangerous to go alone.", "stupid snakes", "", 210, 432,
                    True, False, ["Items"], False, graphic_dict["garan_down"])
    npc_maurelle = NPC("maurelle", "amuna", "We need help!", "village repairs", "", 745, 615,
                       True, False, ["Items"], False, graphic_dict["maurelle_down"])
    npc_celeste = NPC("celeste", "sorae", "My pet!", "where's nede?", "", 760, 415,
                      True, False, ["Items"], False, graphic_dict["celeste_down"])
    npc_torune = NPC("torune", "nuldar", "Onur-oh.", "ghouled again", "", 430, 120,
                     True, False, ["Items"], False, graphic_dict["torune_down"])

    npc_voruke = NPC("voruke", "nuldar", "Onur-oh.", "band hammer", "", 262, 425,
                     True, False, ["Items"], False, graphic_dict["voruke_down"])
    npc_zerah = NPC("zerah", "nuldar", "Onur-oh.", "elementary elementals", "", 652, 90,
                    True, False, ["Items"], False, graphic_dict["zerah_down"])
    npc_dionte = NPC("dionte", "amuna", "It's dangerous to go alone.", "It's dangerous to go alone", "", 625, 110,
                     True, False, ["Items"], False, graphic_dict["dionte_down"])

    npc_amuna_shopkeeper = Shopkeeper("amuna shopkeeper", "amuna", [
        Item("basic armor", "armor", 1078, 197, graphic_dict["basic_armor"], 1),
        Item("health potion", "potion", 200, 200, graphic_dict["health_pot_img"], 0),
        Item("energy potion", "potion", 200, 200, graphic_dict["energy_pot_img"], 0)])

    npc_nuldar_shopkeeper = Shopkeeper("nuldar shopkeeper", "amuna", [
        Item("forged armor", "armor", 1078, 197, graphic_dict["forged_armor"], 2),
        Item("health potion", "potion", 200, 200, graphic_dict["health_pot_img"], 0),
        Item("energy potion", "potion", 200, 200, graphic_dict["energy_pot_img"], 0)])

    npc_garan_interaction = UiElement("garan interaction", 647, 360, graphic_dict["garan_interaction"])
    npc_maurelle_interaction = UiElement("maurelle interaction", 641, 360, graphic_dict["maurelle_interaction"])
    npc_celeste_interaction = UiElement("celeste interaction", 639, 360, graphic_dict["celeste_interaction"])
    npc_torune_interaction = UiElement("torune interaction", 635, 360, graphic_dict["torune_interaction"])

    npc_voruke_interaction = UiElement("voruke interaction", 640, 360, graphic_dict["voruke_interaction"])
    npc_zerah_interaction = UiElement("zerah interaction", 640, 360, graphic_dict["zerah_interaction"])
    npc_dionte_interaction = UiElement("dionte interaction", 647, 360, graphic_dict["dionte_interaction"])

    # enemies: kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image, color, health bar
    # seldon enemies ---------------------------------------------------------------------------------------------------
    snake_1 = Enemy("snake", "snake", 100, 100, 1, 100, 130, True,
                    Item("shiny rock", "rock", 200, 200, graphic_dict["shiny_rock_img"], 0),
                    graphic_dict["snake"], UiElement("snake hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
    snake_2 = Enemy("snake", "snake", 100, 100, 2, 285, 150, True,
                    Item("shiny rock", "rock", 200, 200, graphic_dict["shiny_rock_img"], 0),
                    graphic_dict["snake"], UiElement("snake hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
    snake_3 = Enemy("snake", "snake", 100, 100, 1, 100, 230, True,
                    Item("shiny rock", "rock", 200, 200, graphic_dict["shiny_rock_img"], 0),
                    graphic_dict["snake"], UiElement("snake hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
    snake_4 = Enemy("snake", "snake", 100, 100, 2, 285, 250, True,
                    Item("shiny rock", "rock", 200, 200, graphic_dict["shiny_rock_img"], 0),
                    graphic_dict["snake"], UiElement("snake hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
    ghoul_low_1 = Enemy("ghoul", "ghoul", 100, 100, 4, 665, 180, True,
                        Item("bone dust", "dust", 200, 200, graphic_dict["bone_dust_img"], 0),
                        graphic_dict["ghoul"], UiElement("ghoul hp bar", 700, 90, graphic_dict["hp_100"]), "scout")
    ghoul_low_2 = Enemy("ghoul", "ghoul", 100, 100, 5, 800, 130, True,
                        Item("bone dust", "dust", 200, 200, graphic_dict["bone_dust_img"], 0),
                        graphic_dict["ghoul"], UiElement("ghoul hp bar", 700, 90, graphic_dict["hp_100"]), "scout")
    ghoul_low_3 = Enemy("ghoul", "ghoul", 100, 100, 3, 760, 240, True,
                        Item("bone dust", "dust", 200, 200, graphic_dict["bone_dust_img"], 0),
                        graphic_dict["ghoul"], UiElement("ghoul hp bar", 700, 90, graphic_dict["hp_100"]), "scout")
    ghoul_low_4 = Enemy("ghoul", "ghoul", 100, 100, 4, 890, 205, True,
                        Item("bone dust", "dust", 200, 200, graphic_dict["bone_dust_img"], 0),
                        graphic_dict["ghoul"], UiElement("ghoul hp bar", 700, 90, graphic_dict["hp_100"]), "scout")
    ghoul_nede = Enemy("nede ghoul", "ghoul", 100, 100, 3, 450, 455, True,
                        Item("bone dust", "dust", 200, 200, graphic_dict["bone_dust_img"], 0),
                        graphic_dict["ghoul"], UiElement("ghoul hp bar", 700, 90, graphic_dict["hp_100"]), "scout")
    # reservoir enemies ------------------------------------------------------------------------------------------------
    chorizon_1 = Enemy("chorizon_1", "chorizon", 100, 100, 7, 150, 230, True, "item", graphic_dict["chorizon"],
                       UiElement("chorizon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
    chorizon_2 = Enemy("chorizon_2", "chorizon", 100, 100, 7, 870, 230, True, "item", graphic_dict["chorizon"],
                       UiElement("chorizon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
    muchador = Enemy("muchador", "muchador", 100, 100, 8, 350, 360, True, "item", graphic_dict["muchador_dark"],
                     UiElement("muchador hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
    # korlok enemies ---------------------------------------------------------------------------------------------------
    magmon_1 = Enemy("magmon", "magmon", 100, 100, 9, 125, 135, True,
                     Item("cracked ember", "ember", 200, 200, graphic_dict["ember"], 0),
                     graphic_dict["magmon"], UiElement("magmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
    magmon_2 = Enemy("magmon", "magmon", 100, 100, 11, 375, 125, True,
                     Item("cracked ember", "ember", 200, 200, graphic_dict["ember"], 0),
                     graphic_dict["magmon"], UiElement("magmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
    magmon_3 = Enemy("magmon", "magmon", 100, 100, 10, 200, 197, True,
                     Item("cracked ember", "ember", 200, 200, graphic_dict["ember"], 0),
                     graphic_dict["magmon"], UiElement("magmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
    magmon_4 = Enemy("magmon", "magmon", 100, 100, 9, 320, 197, True,
                     Item("cracked ember", "ember", 200, 200, graphic_dict["ember"], 0),
                     graphic_dict["magmon"], UiElement("magmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
    bandile_1 = Enemy("bandile", "bandile", 100, 100, 8, 655, 245, True,
                        Item("broken band", "band", 200, 200, graphic_dict["band"], 0),
                        graphic_dict["bandile"], UiElement("bandile hp bar", 700, 90, graphic_dict["hp_100"]),
                      "fighter")
    bandile_2 = Enemy("bandile", "bandile", 100, 100, 9, 765, 165, True,
                        Item("broken band", "band", 200, 200, graphic_dict["band"], 0),
                        graphic_dict["bandile"], UiElement("bandile hp bar", 700, 90, graphic_dict["hp_100"]),
                      "fighter")
    bandile_3 = Enemy("bandile", "bandile", 100, 100, 7, 765, 335, True,
                        Item("broken band", "band", 200, 200, graphic_dict["band"], 0),
                        graphic_dict["bandile"], UiElement("bandile hp bar", 700, 90, graphic_dict["hp_100"]),
                      "fighter")
    bandile_4 = Enemy("bandile", "bandile", 100, 100, 8, 880, 245, True,
                        Item("broken band", "band", 200, 200, graphic_dict["band"], 0),
                        graphic_dict["bandile"], UiElement("bandile hp bar", 700, 90, graphic_dict["hp_100"]),
                      "fighter")
    # terra cave enemy -------------------------------------------------------------------------------------------------
    chinzilla = Enemy("chinzilla", "chinzilla", 100, 100, 14, 350, 360, True, "item", graphic_dict["chinzilla"],
                      UiElement("chinzilla hp bar", 700, 90, graphic_dict["hp_100"]), "scout")

    pine_tree_1 = Tree("tree", "pine tree", 80, 445, False, graphic_dict["pine_tree"])
    pine_tree_2 = Tree("tree", "pine tree", 260, 590, False, graphic_dict["pine_tree"])
    pine_tree_3 = Tree("tree", "pine tree", 340, 400, False, graphic_dict["pine_tree"])
    seldon_inn = Building("inn", "seldon inn", 635, 600, graphic_dict["amuna_inn_building"])
    seldon_shop = Building("shop", "seldon shop", 665, 400, graphic_dict["amuna_shop_building"])
    seldon_academia = Building("academia", "seldon academia", 875, 440, graphic_dict["amuna_academia_building"])

    korlok_inn = Building("inn", "korlok inn", 895, 365, graphic_dict["nuldar_inn_building"])
    korlok_shop = Building("shop", "korlok shop", 675, 390, graphic_dict["nuldar_shop_building"])
    korlok_herb = Building("apothecary", "korlok apothecary", 745, 240, graphic_dict["nuldar_herb_building"])
    mines_entrance = Building("entrance", "mines entrance", 430, 375, graphic_dict["mines_entrance"])

    mines_ore_1 = Item("mines ore", "ore", 125, 230, graphic_dict["sprite_ore_img"], 0)
    mines_ore_2 = Item("mines ore", "ore", 200, 230, graphic_dict["sprite_ore_img"], 0)
    mines_ore_3 = Item("mines ore", "ore", 275, 230, graphic_dict["sprite_ore_img"], 0)
    mines_ore_4 = Item("mines ore", "ore", 275, 150, graphic_dict["sprite_ore_img"], 0)

    hearth_stone = Building("hearth", "seldon hearth", 860, 595, graphic_dict["hearth_stone"])

    stardust_entrance = Building("shop", "stardust post", 530, 325, graphic_dict["stardust_entrance"])
    rohir_gate = Building("gate", "rohir gate", 525, 50, graphic_dict["rohir_gate"])
    nascent_gate = Building("gate", "nascent gate", 418, 262, graphic_dict["nascent_gate_closed"])

    dungeon_entrance = Building("entrance", "dungeon entrance", 35, 350, graphic_dict["dungeon_entrance"])
    dungeon_wall_1 = Building("wall", "dungeon wall 1", 347, 472, graphic_dict["dungeon_wall_1"])
    dungeon_wall_2 = Building("wall", "dungeon wall 2", 308, 384, graphic_dict["dungeon_wall_2"])
    dungeon_wall_3 = Building("wall", "dungeon wall 3", 682, 472, graphic_dict["dungeon_wall_1"])
    dungeon_wall_4 = Building("wall", "dungeon wall 4", 720, 384, graphic_dict["dungeon_wall_2"])

    location_overlay = UiElement("location overlay", 915, 28, graphic_dict["location_overlay"])
    character_select_overlay = UiElement("character select overlay", 640, 365, graphic_dict["char_select_overlay"])
    amuna_select_overlay = UiElement("amuna select overlay", 1140, 305, graphic_dict["amuna_overlay_img"])
    nuldar_select_overlay = UiElement("nuldar select overlay", 1140, 305, graphic_dict["nuldar_overlay_img"])
    sorae_select_overlay = UiElement("sorae select overlay", 1140, 305, graphic_dict["sorae_overlay_img"])
    name_input = UiElement("name input", 640, 585, graphic_dict["name_input_img"])

    equipment_screen = UiElement("equipment screen", 1155, 360, graphic_dict["equipment_screen"])
    offense_meter = UiElement("offense meter", 1200, 81, graphic_dict["offense_defense_0"])
    defense_meter = UiElement("defense meter", 1200, 117, graphic_dict["offense_defense_0"])
    weapon_select = UiElement("weapon select", 1079, 284, graphic_dict["weapon_select"])

    character_button = UiElement("character button", 860, 680, graphic_dict["character_button_img"])
    quests_button = UiElement("quests button", 970, 680, graphic_dict["journal_button_img"])
    new_game_button = UiElement("new game button", 640, 342, graphic_dict["new_game_img"])
    continue_button = UiElement("continue button", 640, 425, graphic_dict["continue_img"])
    amuna_button = UiElement("amuna button", 100, 255, graphic_dict["amuna_button_img"])
    nuldar_button = UiElement("nuldar button", 99, 350, graphic_dict["nuldar_button_img"])
    sorae_button = UiElement("sorae button", 98, 445, graphic_dict["sorae_button_img"])
    start_button = UiElement("start button", 640, 660, graphic_dict["start_button"])
    lets_go_button = UiElement("lets go button", 625, 575, graphic_dict["lets_go_button"])
    buy_button = UiElement("buy button", 860, 680, graphic_dict["buy_button_img"])
    upgrade_button = UiElement("upgrade button", 860, 680, graphic_dict["upgrade_button_img"])
    leave_button = UiElement("leave button", 970, 680, graphic_dict["leave_button_img"])
    rest_button = UiElement("rest button", 860, 680, graphic_dict["rest_button_img"])
    mage_learn_button = UiElement("mage learn button", 763, 250, graphic_dict["learn_button"])
    fighter_learn_button = UiElement("fighter learn button", 303, 330, graphic_dict["learn_button"])
    scout_learn_button = UiElement("scout learn button", 560, 410, graphic_dict["learn_button"])
    barrier_learn_button = UiElement("barrier learn button", 505, 300, graphic_dict["skill_learn_button"])
    hard_strike_learn_button = UiElement("hard strike learn button", 505, 300, graphic_dict["skill_learn_button"])
    sharp_sense_learn_button = UiElement("sharp sense learn button", 505, 300, graphic_dict["skill_learn_button"])
    close_button = UiElement("close button", 975, 135, graphic_dict["close_button"])
    quest_button = UiElement("quest button", 860, 680, graphic_dict["quest_button_img"])
    accept_button = UiElement("accept button", 340, 670, graphic_dict["accept_button_img"])
    decline_button = UiElement("decline button", 450, 670, graphic_dict["decline_button_img"])
    map_button = UiElement("map button", 860, 60, graphic_dict["map_button_img"])
    save_button = UiElement("save button", 970, 60, graphic_dict["save_button_img"])
    yes_button = UiElement("yes button", 450, 394, graphic_dict["yes_button_img"])
    no_button = UiElement("no button", 564, 394, graphic_dict["no_button_img"])
    back_button = UiElement("back button", 75, 665, graphic_dict["back_button_img"])
    item_info_button = UiElement("item info button", 1153, 345, graphic_dict["use_button_img"])
    offense_select_button = UiElement("offense select", 764, 586, graphic_dict["offense_select_button_img"])
    skip_button = UiElement("skip button", 1212, 680, graphic_dict["skip_button_img"])

    no_role_attack_button = UiElement("no role attack button", 750, 642, graphic_dict["no_role_attack_button_img"])
    mage_attack_button = UiElement("mage attack button", 750, 642, graphic_dict["mage_attack_button_img"])
    fighter_attack_button = UiElement("fighter attack button", 750, 642, graphic_dict["fighter_attack_button_img"])
    scout_attack_button = UiElement("scout attack button", 750, 642, graphic_dict["scout_attack_button_img"])
    barrier_button = UiElement("barrier button", 820, 642, graphic_dict["barrier_button_img"])
    hard_strike_button = UiElement("hard strike button", 820, 642, graphic_dict["strike_button_img"])
    sharp_sense_button = UiElement("sharp sense button", 820, 642, graphic_dict["sense_button_img"])

    type_advantage_overlay = UiElement("type advantage overlay", 580, 48, graphic_dict["mage_type_overlay"])

    skill_bar = UiElement("skill bar", 855, 636, graphic_dict["skill_bar"])
    enemy_status = UiElement("enemy status", 855, 687, graphic_dict["enemy_status"])
    hp_bar = UiElement("health bar", 165, 25, graphic_dict["hp_100"])
    en_bar = UiElement("energy bar", 165, 45, graphic_dict["en_100"])
    xp_bar = UiElement("xp bar", 165, 65, graphic_dict["xp_100"])
    journal = UiElement("journal", 770, 380, graphic_dict["journal_window_img"])
    level_up_win = UiElement("level up window", 165, 132, graphic_dict["level_up"])
    character_sheet = UiElement("character sheet", 770, 380, graphic_dict["character_window_img"])
    mage_book = UiElement("mage book", 670, 375, graphic_dict["mage_book_img"])
    fighter_book = UiElement("fighter book", 670, 375, graphic_dict["fighter_book_img"])
    scout_book = UiElement("scout book", 670, 375, graphic_dict["scout_book_img"])
    quest_logs_1 = Item("pine logs", "quest", 60, 540, graphic_dict["pine_logs_img"], 0)
    quest_logs_2 = Item("pine logs", "quest", 315, 560, graphic_dict["pine_logs_img"], 0)
    quest_logs_3 = Item("pine logs", "quest", 415, 435, graphic_dict["pine_logs_img"], 0)
    quest_logs_4 = Item("pine logs", "quest", 100, 540, graphic_dict["pine_logs_img"], 0)
    nede = Item("nede", "quest", 650, 450, graphic_dict["nede_left"], 0)
    nede_big = UiElement("big nede", 840, 270, graphic_dict["nede_big"])
    npc_name_plate = UiElement("npc name plate", 638, 192, graphic_dict["npc_name_plate"])
    buy_inventory = Inventory("buy inventory", [], 900, 500, graphic_dict["buy_inventory"])
    knowledge_window = UiElement("knowledge window", 635, 680, graphic_dict["knowledge_window"])

    garan_quest_window = UiElement("garan quest window", 262, 443, graphic_dict["garan_quest"])
    garan_complete_quest_window = UiElement("garan quest complete window", 550, 350, graphic_dict["garan_complete"])
    maurelle_quest_window = UiElement("maurelle quest window", 262, 443, graphic_dict["maurelle_quest"])
    maurelle_complete_quest_window = UiElement("maurelle quest complete window", 550, 350,
                                               graphic_dict["maurelle_complete"])
    celeste_quest_window = UiElement("maurelle quest window", 262, 443, graphic_dict["celeste_quest"])
    celeste_complete_quest_window = UiElement("celeste quest complete window", 550, 350,
                                              graphic_dict["celeste_complete"])
    torune_quest_window = UiElement("torune quest window", 262, 443, graphic_dict["torune_quest"])
    torune_complete_quest_window = UiElement("torune quest complete window", 550, 350, graphic_dict["torune_complete"])
    voruke_quest_window = UiElement("voruke quest window", 262, 443, graphic_dict["voruke_quest"])
    voruke_complete_quest_window = UiElement("voruke quest complete window", 550, 350, graphic_dict["voruke_complete"])
    zerah_quest_window = UiElement("zerah quest window", 262, 443, graphic_dict["zerah_quest"])
    zerah_complete_quest_window = UiElement("zerah quest complete window", 550, 350, graphic_dict["zerah_complete"])
    kirean_quest_window = UiElement("kirean quest window", 262, 443, graphic_dict["kirean_quest"])
    kirean_complete_quest_window = UiElement("kirean quest complete window", 550, 350, graphic_dict["kirean_complete"])
    dionte_quest_window = UiElement("dionte quest window", 262, 443, graphic_dict["dionte_quest"])
    dionte_complete_quest_window = UiElement("dionte quest complete window", 550, 350, graphic_dict["dionte_complete"])

    message_box = UiElement("message box", 173, 650, graphic_dict["message_box"])
    bar_backdrop = UiElement("bar backdrop", 165, 45, graphic_dict["bar_backdrop"])
    enemy_status_bar_back = UiElement("enemy bar backdrop", 700, 90, graphic_dict["enemy_bar_backdrop"])

    quest_star_garan = UiElement("quest star garan", 210, 390, graphic_dict["quest_start_star"])
    quest_star_maurelle = UiElement("quest star maurelle", 744, 575, graphic_dict["quest_start_star"])
    quest_star_celeste = UiElement("quest star maurelle", 760, 373, graphic_dict["quest_start_star"])
    quest_star_torune = UiElement("quest star torune", 430, 75, graphic_dict["quest_start_star"])

    quest_star_voruke = UiElement("quest star voruke", 262, 385, graphic_dict["quest_start_star"])
    quest_star_zerah = UiElement("quest star zerah", 651, 50, graphic_dict["quest_start_star"])
    quest_star_kirean = UiElement("quest star kirean", 746, 225, graphic_dict["quest_start_star"])
    quest_star_dionte = UiElement("quest star dionte", 625, 65, graphic_dict["quest_start_star"])

    quest_star_apothecary = UiElement("quest star apothecary", 796, 85, graphic_dict["building_npc_star_available"])

    player_battle_sprite = BattleCharacter("stan battle", 320, 460, graphic_dict["player_no_role_amuna_battle"])
    snake_battle_sprite = BattleCharacter("snake battle", 715, 250, graphic_dict["snake_battle"])
    ghoul_battle_sprite = BattleCharacter("ghoul battle", 698, 280, graphic_dict["ghoul_battle"])
    chorizon_battle_sprite = BattleCharacter("chorizon battle", 720, 325, graphic_dict["chorizon_battle"])
    muchador_battle_sprite = BattleCharacter("muchador battle", 705, 290, graphic_dict["muchador_battle"])
    magmon_battle_sprite = BattleCharacter("magmon battle", 705, 286, graphic_dict["magmon_battle"])
    bandile_battle_sprite = BattleCharacter("bandile battle", 695, 300, graphic_dict["bandile_battle"])
    chinzilla_battle_sprite = BattleCharacter("chinzilla battle", 715, 300, graphic_dict["chinzilla_battle"])

    nascent_gate_popup = UiElement("nascent gate popup", 418, 200, graphic_dict["nascent_gate_popup"])
    sell_items = UiElement("sell items", 1155, 270, graphic_dict["s_health_pot_img"])
    info_items = UiElement("info items", 1155, 270, graphic_dict["info_health_pot_img"])
    buy_items = UiElement("buy items", 900, 230, graphic_dict["b_health_pot_img"])
    star_power_meter = UiElement("star power", 1195, 360, graphic_dict["star_00"])
    role_select_overlay = UiElement("role select overlay", 710, 263, graphic_dict["role_selection_overlay"])
    game_guide_overlay = UiElement("game guide overlay", 776, 256, graphic_dict["guide_basics_quest_img"])
    cat_pet_button_overlay = UiElement("cat pet button", 505, 235, graphic_dict["cat_pet_button_overlay"])
    cat_pet_animation_overlay = UiElement("cat pet animation", 507, 242, graphic_dict["shop_cat_pet_img"])
    stardust_star_overlay = UiElement("stardust stars", 236, 185, graphic_dict["stardust_star_01"])
    stardust_star_overlay_korlok = UiElement("stardust stars korlok", 236, 295, graphic_dict["stardust_star_01_korlok"])
    directional_arrow = UiElement("directional arrow", 855, 620, graphic_dict["arrow_down"])

    water_player = UiElement("water", 855, 620, graphic_dict["water"])
    water_1 = UiElement("water", 855, 525, graphic_dict["water"])
    water_2 = UiElement("water", 855, 200, graphic_dict["water"])
    water_3 = UiElement("water", 500, 500, graphic_dict["water"])
    water_4 = UiElement("water", 575, 250, graphic_dict["water"])
    water_5 = UiElement("water", 650, 575, graphic_dict["water"])
    korlok_mountains = UiElement("korlok mountains", 241, 251, graphic_dict["korlok_mountains"])

    upgrade_overlay = UiElement("upgrade overlay", 764, 380, graphic_dict["upgrade_overlay"])
    dealt_damage_overlay = UiElement("dealt damage overlay", 850, 225, graphic_dict["dealt_damage_img"])
    received_damage_overlay = UiElement("recieved damage overlay", 125, 275, graphic_dict["received_damage_img"])
    interaction_popup = UiElement("interaction popup", 125, 275, graphic_dict["popup_interaction"])
    loot_popup = UiElement("loot popup", 171, 528, graphic_dict["popup_loot"])
    button_highlight = UiElement("button_highlight", 200, 200, graphic_dict["main high"])

    world_map = UiElement("world map", 769, 332, graphic_dict["world_map"])
    korlok_map_button = UiElement("seldon map button", 663, 238, graphic_dict["map_button"])
    eldream_map_button = UiElement("korlok map button", 874, 238, graphic_dict["map_button"])
    seldon_map_button = UiElement("eldream map button", 663, 448, graphic_dict["map_button"])
    marrow_map_button = UiElement("marrow map button", 874, 448, graphic_dict["map_button"])

    amuna_location = UiElement("amuna character location", 663, 238, graphic_dict["amuna_location"])
    nuldar_location = UiElement("nuldar character location", 663, 238, graphic_dict["nuldar_location"])
    sorae_location = UiElement("sorae character location", 663, 238, graphic_dict["sorae_location"])

    dungeon_teleporter = UiElement("dungeon teleporter", 519, 316, graphic_dict["dungeon_teleporter"])
    dungeon_drop_wall = UiElement("dungeon drop wall", 310, 224, graphic_dict["dungeon_drop_wall"])
    dungeon_gate = UiElement("dungeon gate", 705, 180, graphic_dict["dungeon_gate"])
    reservoir_passage = UiElement("reservoir passage", 27, 365, graphic_dict["reservoir_passage"])
    reservoir_exit = UiElement("reservoir exit", 724, 40, graphic_dict["reservoir_exit"])
    reservoir_enter = UiElement("reservoir enter", 30, 500, graphic_dict["reservoir_enter"])
    muchador_arena = UiElement("muchador arena", 365, 363, graphic_dict["muchador_arena"])
    muchador_crate_1 = UiElement("muchador crate 1", 200, 200, graphic_dict["muchador_crate"])
    muchador_crate_2 = UiElement("muchador crate 2", 500, 200, graphic_dict["muchador_crate"])
    muchador_crate_3 = UiElement("muchador crate 3", 200, 530, graphic_dict["muchador_crate"])
    muchador_crate_4 = UiElement("muchador crate 4", 500, 530, graphic_dict["muchador_crate"])

    dungeon_crate_1 = Item("dungeon crate 1", "crate", 75, 150, graphic_dict["dungeon_crate"], 0)
    dungeon_crate_2 = Item("dungeon crate 2", "crate", 960, 150, graphic_dict["dungeon_crate"], 0)
    dungeon_crate_3 = Item("dungeon crate 3", "crate", 388, 575, graphic_dict["dungeon_crate"], 0)
    dungeon_crate_4 = Item("dungeon crate 4", "crate", 650, 575, graphic_dict["dungeon_crate"], 0)
    dungeon_crate_5 = Item("dungeon crate 5", "crate", 970, 150, graphic_dict["dungeon_crate"], 0)
    dungeon_switch_1 = Item("dungeon switch 1", "switch", 158, 430, graphic_dict["dungeon_switch_inactive"], 0)
    dungeon_switch_2 = Item("dungeon switch 2", "switch", 874, 430, graphic_dict["dungeon_switch_inactive"], 0)
    dungeon_switch_3 = Item("dungeon switch 3", "switch", 519, 165, graphic_dict["dungeon_switch_inactive"], 0)
    dungeon_chest = Item("dungeon chest", "chest", 297, 355, graphic_dict["dungeon_chest"], 0)
    dungeon_chest_rect = pygame.Rect((245, 310,), (90, 10))

    mines_wall = UiElement("mines wall", 780, 430, graphic_dict["mines_wall"])
    mines_light = UiElement("mines light", 322, 325, graphic_dict["mines_light"])

    terra_mountains = UiElement("terra mountains", 250, 270, graphic_dict["terra_mountains"])
    terra_cave = UiElement("terra cave", 100, 400, graphic_dict["terra_cave"])

    rock_1 = Item("rock 1", "rock", 580, 145, graphic_dict["rock_img"], 0)
    rock_2 = Item("rock 2", "rock", 580, 255, graphic_dict["rock_img"], 0)

    font = pygame.font.SysFont('freesansbold.ttf', 22, bold=False, italic=False)
    level_up_font = pygame.font.SysFont('freesansbold.ttf', 28, bold=True, italic=False)
    name_input_font = pygame.font.SysFont('freesansbold.ttf', 32, bold=True, italic=False)

    quest_items_seldon = pygame.sprite.Group()
    npcs_seldon = pygame.sprite.Group()
    npcs_korlok = pygame.sprite.Group()
    seldon_enemies = pygame.sprite.Group()
    korlok_enemies = pygame.sprite.Group()
    mine_enemies = pygame.sprite.Group()
    mine_walls = pygame.sprite.Group()
    boss_enemies = pygame.sprite.Group()
    trees = pygame.sprite.Group()
    ores = pygame.sprite.Group()
    dungeon_rocks = pygame.sprite.Group()
    amuna_buildings = pygame.sprite.Group()
    nuldar_buildings = pygame.sprite.Group()
    dungeon_walls = pygame.sprite.Group()
    dungeon_items = pygame.sprite.Group()
    muchador_crates = pygame.sprite.Group()
    environments = pygame.sprite.Group()
    user_interface = pygame.sprite.Group()
    enemy_hp_bars = pygame.sprite.Group()
    most_sprites = pygame.sprite.Group()
    non_sprite_sheets = pygame.sprite.Group()
    snakes = pygame.sprite.Group()
    ghouls = pygame.sprite.Group()
    magmons = pygame.sprite.Group()
    bandiles = pygame.sprite.Group()
    interactables_nascent = pygame.sprite.Group()
    interactables_seldon = pygame.sprite.Group()
    interactables_stardust = pygame.sprite.Group()
    interactables_korlok = pygame.sprite.Group()
    interactables_mines = pygame.sprite.Group()
    interactables_terra_trail = pygame.sprite.Group()
    interactables_reservoir_a = pygame.sprite.Group()
    interactables_reservoir_b = pygame.sprite.Group()
    interactables_reservoir_c = pygame.sprite.Group()

    snakes.add(snake_1, snake_2, snake_3, snake_4)
    ghouls.add(ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)
    magmons.add(magmon_1, magmon_2, magmon_3, magmon_4)
    bandiles.add(bandile_1, bandile_2, bandile_3, bandile_4)
    npcs_seldon.add(npc_garan, npc_maurelle, npc_celeste, npc_torune)
    npcs_korlok.add(npc_voruke, npc_zerah)
    seldon_enemies.add(snake_1, snake_2, snake_3, snake_4, ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)
    korlok_enemies.add(magmon_1, magmon_2, magmon_3, magmon_4)
    mine_enemies.add(bandile_1, bandile_2, bandile_3, bandile_4)
    mine_walls.add(mines_wall, mines_light)
    boss_enemies.add(chorizon_1, chorizon_2)
    trees.add(pine_tree_1, pine_tree_2, pine_tree_3)
    ores.add(mines_ore_1, mines_ore_2, mines_ore_3, mines_ore_4)
    dungeon_rocks.add(rock_1, rock_2)
    amuna_buildings.add(seldon_inn, seldon_shop, seldon_academia)
    nuldar_buildings.add(korlok_inn, korlok_shop, korlok_herb, reservoir_enter)
    dungeon_walls.add(dungeon_wall_1, dungeon_wall_2, dungeon_wall_3, dungeon_wall_4)
    dungeon_items.add(dungeon_crate_1, dungeon_crate_2, dungeon_crate_3, dungeon_crate_4, dungeon_switch_1,
                      dungeon_switch_2, dungeon_switch_3)
    muchador_crates.add(muchador_crate_1, muchador_crate_2, muchador_crate_3, muchador_crate_4)
    environments.add(trees, amuna_buildings)
    quest_items_seldon.add(quest_logs_1, quest_logs_2, quest_logs_3, quest_logs_4, rohir_gate)
    most_sprites.add(npcs_seldon, trees, amuna_buildings, quest_items_seldon, seldon_enemies, hearth_stone, rohir_gate)
    user_interface.add(rest_button, buy_button, leave_button, character_button, quests_button, save_button,
                       map_button, message_box, location_overlay, star_power_meter)
    interactables_nascent.add(nascent_gate)
    interactables_seldon.add(npcs_seldon, seldon_enemies, amuna_buildings, hearth_stone, quest_items_seldon)
    interactables_stardust.add(stardust_entrance, nede, ghoul_nede)
    interactables_korlok.add(nuldar_buildings, reservoir_enter, rohir_gate, hearth_stone, korlok_enemies,
                             mines_entrance, npc_voruke, npc_zerah)
    interactables_reservoir_a.add(dungeon_items, chorizon_1, chorizon_2, dungeon_teleporter)
    interactables_reservoir_b.add(dungeon_gate, dungeon_teleporter, dungeon_crate_5, muchador, reservoir_passage)
    interactables_reservoir_c.add(dungeon_chest, rock_1, rock_2, reservoir_exit)
    interactables_mines.add(bandiles, mines_ore_1, mines_ore_2, mines_ore_3, mines_ore_4)
    interactables_terra_trail.add(npc_dionte, terra_cave)

    # music tracks
    start_screen_music = resource_path("resources/music/eterna_title.mp3")
    seldon_overworld_music = resource_path("resources/music/eterna_seldon.mp3")
    seldon_building_music = resource_path("resources/music/eterna_building.mp3")
    stardust_outpost_music = resource_path("resources/music/eterna_stardust.mp3")
    apothis_intro_music = resource_path("resources/music/eterna_apothis.mp3")
    rohir_river_music = resource_path("resources/music/eterna_rohir.mp3")
    reservoir_music = resource_path("resources/music/eterna_dungeon.mp3")
    korlok_overworld_music = resource_path("resources/music/eterna_korlok.mp3")
    korlok_building_music = resource_path("resources/music/eterna_building_korlok.mp3")

    pygame.mixer.music.set_volume(0.75)
    pygame.mixer.music.load(start_screen_music)
    pygame.mixer.music.play(loops=-1)

    # move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
    # move_up_sound.set_volume(0.5)

    # main loop variables ----------------------------------------------------------------------------------------------
    game_running = True
    saving = False
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
    in_apothecary = False
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
    map_button_clicked = False
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
    loot_info = False
    garan_complete_shown = False
    maurelle_complete_shown = False
    celeste_complete_shown = False
    torune_complete_shown = False
    voruke_complete_shown = False
    zerah_complete_shown = False
    kirean_complete_shown = False
    dionte_complete_shown = False
    snake_sprite_reset = False
    ghoul_sprite_reset = False
    log_sprite_reset = False
    nede_sprite_reset = False
    quest_guide_shown = False
    battle_guide_shown = False
    quest_highlight_popup = True
    shop_cat_pet = False
    academia_cat_pet = False
    rest_shown_before = False
    leveled = False
    button_highlighted = False
    book_appended = False
    first_npc_cond = True
    first_shop_cond = True
    first_inn_cond = True
    first_academy_cond = True
    first_battle_cond = True
    bridge_not_repaired = True
    nede_ghoul_defeated = False
    bridge_cutscenes_not_viewed = True
    has_key = False
    muchador_lights_on = False
    muchador_relocate = False
    muchador_defeated = False
    mini_boss_1_defeated = False
    mini_boss_2_defeated = False
    gloves_obtained = False
    rock_1_moved = False
    rock_2_moved = False
    korlok_attuned = False
    eldream_attuned = False
    apothecary_access = False

    over_world_song_set = False
    battle_song_set = False
    stardust_song_set = False
    building_song_set = False

    attack_hotkey = False
    skill_1_hotkey = False

    # reservoir dungeon conditions
    crate_1 = False
    crate_2 = False
    crate_3 = False
    crate_4 = False
    crate_5 = False
    switch_1 = False
    switch_2 = False
    switch_3 = False

    mini_boss_1 = False
    mini_boss_2 = False

    buy_shop_elements = []
    stardust_upgrade_elements = []
    shopkeeper_items = []
    skill_learn_items = []
    books = []
    knowledge_academia_window = []
    rest_recover_window = []
    save_check_window = []
    save_data_window = []
    first_quest_window = []
    sell_window = []
    buy_window = []
    loot_popup_container = []
    loot_text_container = []
    game_guide_container = []
    world_map_container = []

    info_text_1 = ''
    info_text_2 = ''
    info_text_3 = ''
    info_text_4 = ''
    character_name_input = ''
    current_buy_item = ''
    current_sell_item = ''
    current_info_item = ''

    # default objects for event loops, updated when player interacts with new object
    current_enemy_battling = snake_1
    current_npc_interacting = npc_garan
    current_building_entering = seldon_inn

    battle_info_to_return_to_main_loop = {"experience": 0, "item dropped": "", "leveled_up": False, "knowledge": ""}

    clock = pygame.time.Clock()
    enemy_tic = time.perf_counter()
    npc_tic = time.perf_counter()
    walk_tic = time.perf_counter()
    loot_level_tic = time.perf_counter()

    # main loop --------------------------------------------------------------------------------------------------------
    while game_running:

        if not new_game_chosen and not continue_game_chosen and not start_chosen:
            screen.blit(start_screen, (0, 0))
            screen.blit(new_game_button.surf, new_game_button.rect)
            screen.blit(continue_button.surf, continue_button.rect)

            if len(save_data_window) > 0:
                for element in save_data_window:
                    screen.blit(element.surf, element.rect)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        if len(save_data_window) > 0:
                            for element in save_data_window:
                                save_data_window.clear()

                pos = pygame.mouse.get_pos()
                button_highlighted = button_highlighter(pos)

                if event.type == pygame.MOUSEBUTTONUP:
                    # player chooses to start a new game or continue from previous
                    if new_game_button.rect.collidepoint(pos):
                        new_game_chosen = True
                        button_highlighted = False
                        save_data_window.clear()
                    if continue_button.rect.collidepoint(pos):
                        continue_game_chosen = True
                        button_highlighted = False
                    # click to dismiss save absent popup if player tries to continue with no save file
                    if save_absent.rect.collidepoint(pos):
                        save_data_window.clear()
                elif event.type == QUIT:
                    sys.exit()

            if button_highlighted:
                screen.blit(button_highlight.surf, button_highlight.rect)

            pygame.display.flip()

        # --------------------------------------------------------------------------------------------------------------
        # character selection for new game -----------------------------------------------------------------------------
        if new_game_chosen:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        new_game_chosen = False
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
                    pygame.mixer.quit()
                    sys.exit()

                pos = pygame.mouse.get_pos()
                button_highlighted = button_highlighter(pos)

                if event.type == pygame.MOUSEBUTTONUP:

                    # player clicks on the box to type name
                    if name_input.rect.collidepoint(pos):
                        if name_input_selected:
                            if len(character_name_input) < 1:
                                name_input.update(name_input.x_coordinate, name_input.y_coordinate,
                                                  graphic_dict["name_input_img"])
                            name_input_selected = False
                        else:
                            name_input.update(name_input.x_coordinate, name_input.y_coordinate,
                                              graphic_dict["name_input_empty_img"])
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
                                                 player.skills_fighter, player.skills_scout, player.level,
                                                 player.experience, player.health, player.energy, player.alive_status,
                                                 player.rupees, player.reputation, player.current_zone, player.defense,
                                                 player.offense, player.star_power)
                            player.race = "amuna"
                            player.surf = graphic_dict["player_no_role_amuna_down_1"]
                            player.current_zone = "nascent"
                            in_over_world = True
                            new_game_chosen = False
                            start_chosen = True
                        if nuldar_race_selected:
                            player = PlayerNuldar(player.name, player.race, player.role, player.items, player.equipment,
                                                  player.current_quests, player.quest_progress, player.quest_status,
                                                  player.quest_complete, player.knowledge, player.skills_mage,
                                                  player.skills_fighter, player.skills_scout, player.level,
                                                  player.experience, player.health, player.energy, player.alive_status,
                                                  player.rupees, player.reputation, player.current_zone, player.defense,
                                                  player.offense, player.star_power)
                            player.race = "nuldar"
                            player.surf = graphic_dict["player_no_role_nuldar_down_1"]
                            player.current_zone = "nascent"
                            in_over_world = True
                            new_game_chosen = False
                            start_chosen = True
                        if sorae_race_selected:
                            player = PlayerSorae(player.name, player.race, player.role, player.items, player.equipment,
                                                 player.current_quests, player.quest_progress, player.quest_status,
                                                 player.quest_complete, player.knowledge, player.skills_mage,
                                                 player.skills_fighter, player.skills_scout, player.level,
                                                 player.experience, player.health, player.energy, player.alive_status,
                                                 player.rupees, player.reputation, player.current_zone, player.defense,
                                                 player.offense, player.star_power)
                            player.race = "sorae"
                            player.surf = graphic_dict["player_no_role_sorae_down_1"]
                            player.current_zone = "nascent"
                            in_over_world = True
                            new_game_chosen = False
                            start_chosen = True

                        if len(character_name_input) > 0:
                            player.name = str(character_name_input)
                        else:
                            player.name = "default"

                    if back_button.rect.collidepoint(pos):
                        button_highlighted = False
                        new_game_chosen = False

            # amuna race selected on character selection screen --------------------------------------------------------
            if amuna_race_selected:
                character_creation.character_screen_draw(screen, "amuna", amuna_character_screen,
                                                         nuldar_character_screen, sorae_character_screen,
                                                         character_select_overlay, amuna_select_overlay,
                                                         amuna_character, nuldar_select_overlay, nuldar_character,
                                                         sorae_select_overlay, sorae_character, amuna_button,
                                                         nuldar_button, sorae_button, start_button, back_button,
                                                         name_input, name_input_font, character_name_input, pygame)
                if button_highlighted:
                    screen.blit(button_highlight.surf, button_highlight.rect)
                pygame.display.flip()

            # nuldar race selected on character selection screen -------------------------------------------------------
            if nuldar_race_selected:
                character_creation.character_screen_draw(screen, "nuldar", amuna_character_screen,
                                                         nuldar_character_screen, sorae_character_screen,
                                                         character_select_overlay, amuna_select_overlay,
                                                         amuna_character, nuldar_select_overlay, nuldar_character,
                                                         sorae_select_overlay, sorae_character, amuna_button,
                                                         nuldar_button, sorae_button, start_button, back_button,
                                                         name_input, name_input_font, character_name_input, pygame)
                if button_highlighted:
                    screen.blit(button_highlight.surf, button_highlight.rect)
                pygame.display.flip()

            # sorae race selected on character selection screen --------------------------------------------------------
            if sorae_race_selected:
                character_creation.character_screen_draw(screen, "sorae", amuna_character_screen,
                                                         nuldar_character_screen, sorae_character_screen,
                                                         character_select_overlay, amuna_select_overlay,
                                                         amuna_character, nuldar_select_overlay, nuldar_character,
                                                         sorae_select_overlay, sorae_character, amuna_button,
                                                         nuldar_button, sorae_button, start_button, back_button,
                                                         name_input, name_input_font, character_name_input, pygame)
                if button_highlighted:
                    screen.blit(button_highlight.surf, button_highlight.rect)
                pygame.display.flip()

        # continue game selected on start screen. try to load player info from save_game file --------------------------
        if continue_game_chosen:
            directory = os.getcwd()
            try:
                load_returned = gameplay_functions.load_game(player, Item, graphic_dict)
                try:
                    if load_returned["not found"]:
                        save_data_window.append(save_absent)
                    continue_game_chosen = load_returned["continue"]
                    barrier_learned = load_returned["barrier learned"]
                    hard_strike_learned = load_returned["strike learned"]
                    sharp_sense_learned = load_returned["sense learned"]
                    saved = load_returned["saved"]
                    start_chosen = load_returned["start"]
                    npc_garan.gift = load_returned["garan gift"]
                    rest_recover_show = load_returned["rest popup"]
                    knowledge_academia_show = load_returned["knowledge popup"]
                    quest_guide_shown = load_returned["quest guide"]
                    battle_guide_shown = load_returned["battle guide"]
                    rest_shown_before = load_returned["rest shown before"]
                    quest_highlight_popup = load_returned["quest highlight popup"]
                    bridge_not_repaired = load_returned["bridge not repaired"]
                    nede_ghoul_defeated = load_returned["nede ghoul defeated"]
                    bridge_cutscenes_not_viewed = load_returned["bridge_cutscenes_not_viewed"]
                    crate_1 = load_returned["crate_1"]
                    crate_2 = load_returned["crate_2"]
                    crate_3 = load_returned["crate_3"]
                    crate_4 = load_returned["crate_4"]
                    crate_5 = load_returned["crate_5"]
                    switch_1 = load_returned["switch_1"]
                    switch_2 = load_returned["switch_2"]
                    switch_3 = load_returned["switch_3"]
                    muchador_defeated = load_returned["muchador_defeated"]
                    has_key = load_returned["has_key"]
                    gloves_obtained = load_returned["gloves_obtained"]
                    korlok_attuned = load_returned["korlok_attuned"]
                    eldream_attuned = load_returned["eldream_attuned"]

                    if player.race == "amuna":
                        player = PlayerAmuna(player.name, player.race, player.role, player.items, player.equipment,
                                             player.current_quests, player.quest_progress, player.quest_status,
                                             player.quest_complete, player.knowledge, player.skills_mage,
                                             player.skills_fighter, player.skills_scout, player.level,
                                             player.experience, player.health, player.energy, player.alive_status,
                                             player.rupees, player.reputation, player.current_zone, player.defense,
                                             player.offense, player.star_power)
                        if player.role == "":
                            player.surf = graphic_dict["player_no_role_amuna_down_1"]
                        if player.role == "mage":
                            player.surf = graphic_dict["player_mage_amuna_down_1"]
                        if player.role == "fighter":
                            player.surf = graphic_dict["player_fighter_amuna_down_1"]
                        if player.role == "scout":
                            player.surf = graphic_dict["player_scout_amuna_down_1"]

                    if player.race == "nuldar":
                        player = PlayerNuldar(player.name, player.race, player.role, player.items, player.equipment,
                                              player.current_quests, player.quest_progress, player.quest_status,
                                              player.quest_complete, player.knowledge, player.skills_mage,
                                              player.skills_fighter, player.skills_scout, player.level,
                                              player.experience, player.health, player.energy, player.alive_status,
                                              player.rupees, player.reputation, player.current_zone, player.defense,
                                              player.offense, player.star_power)
                        if player.role == "":
                            player.surf = graphic_dict["player_no_role_nuldar_down_1"]
                        if player.role == "mage":
                            player.surf = graphic_dict["player_mage_nuldar_down_1"]
                        if player.role == "fighter":
                            player.surf = graphic_dict["player_fighter_nuldar_down_1"]
                        if player.role == "scout":
                            player.surf = graphic_dict["player_scout_nuldar_down_1"]

                    if player.race == "sorae":
                        player = PlayerSorae(player.name, player.race, player.role, player.items, player.equipment,
                                             player.current_quests, player.quest_progress, player.quest_status,
                                             player.quest_complete, player.knowledge, player.skills_mage,
                                             player.skills_fighter, player.skills_scout, player.level,
                                             player.experience, player.health, player.energy, player.alive_status,
                                             player.rupees, player.reputation, player.current_zone, player.defense,
                                             player.offense, player.star_power)
                        if player.role == "":
                            player.surf = graphic_dict["player_no_role_sorae_down_1"]
                        if player.role == "mage":
                            player.surf = graphic_dict["player_mage_sorae_down_1"]
                        if player.role == "fighter":
                            player.surf = graphic_dict["player_fighter_sorae_down_1"]
                        if player.role == "scout":
                            player.surf = graphic_dict["player_scout_sorae_down_1"]

                    if player.quest_progress["where's nede?"] == 1:
                        nede.update(809, 390, graphic_dict["nede_left"])

                    if player.current_zone == "seldon":
                        player.x_coordinate = 860
                        player.y_coordinate = 655
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                    if player.current_zone == "stardust":
                        player.x_coordinate = 925
                        player.y_coordinate = 275
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                    if player.current_zone == "korlok":
                        player.x_coordinate = 882
                        player.y_coordinate = 290
                        hearth_stone.update(885, 230, graphic_dict["hearth_stone"])
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                    if player.current_zone == "mines":
                        player.x_coordinate = 815
                        player.y_coordinate = 600
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                    if player.current_zone == "rohir":
                        player.x_coordinate = 900
                        player.y_coordinate = 400
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                    if player.current_zone == "reservoir a":
                        player.x_coordinate = 525
                        player.y_coordinate = 650
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                    if player.current_zone == "reservoir b":
                        player.x_coordinate = 880
                        player.y_coordinate = 560
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                        dungeon_teleporter.update(880, 525, graphic_dict["dungeon_teleporter"])
                    if player.current_zone == "reservoir c":
                        player.x_coordinate = 900
                        player.y_coordinate = 545
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                    if player.current_zone == "terra trail":
                        player.x_coordinate = 150
                        player.y_coordinate = 150
                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                except TypeError:
                    pass
            except KeyError:
                pass

        # --------------------------------------------------------------------------------------------------------------
        # player has chosen to start game ------------------------------------------------------------------------------
        if start_chosen:
            if player.alive_status:

                loot_level_toc = time.perf_counter()
                # after battle, clear loot popup after about 3 seconds
                if loot_info:
                    if loot_level_toc - loot_level_tic > 3:
                        drawing_functions.loot_popup_container.clear()
                        drawing_functions.loot_text_container.clear()
                # if player leveled, clear level up popup after about 3 seconds
                if leveled:
                    if loot_level_toc - loot_level_tic > 3:
                        drawing_functions.level_up_draw(level_up_win, player, font, False)
                        leveled = False

                # player information updates
                gameplay_functions.player_info_and_ui_updates(player, hp_bar, en_bar, xp_bar, star_power_meter,
                                                              offense_meter, defense_meter, graphic_dict, basic_armor,
                                                              forged_armor, mythical_armor, legendary_armor,
                                                              power_gloves)

                if in_over_world and not in_battle and not in_npc_interaction and not in_shop and not in_inn \
                        and not in_academia:

                    # checks if player has started any quest to show the quest popup info window for highlights
                    if player.quest_status["sneaky snakes"]:
                        if quest_highlight_popup:
                            drawing_functions.first_quest_window.append(first_quest)
                            quest_highlight_popup = False
                    elif player.quest_status["village repairs"]:
                        if quest_highlight_popup:
                            drawing_functions.first_quest_window.append(first_quest)
                            quest_highlight_popup = False
                    elif player.quest_status["where's nede?"]:
                        if quest_highlight_popup:
                            drawing_functions.first_quest_window.append(first_quest)
                            quest_highlight_popup = False
                    elif player.quest_status["ghouled again"]:
                        if quest_highlight_popup:
                            drawing_functions.first_quest_window.append(first_quest)
                            quest_highlight_popup = False

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
                            # escape key was pressed, clear any element on top of screen
                            if event.key == K_ESCAPE:
                                # clear popups
                                if len(drawing_functions.knowledge_academia_window) > 0:
                                    drawing_functions.knowledge_academia_window.clear()
                                if len(drawing_functions.rest_recover_window) > 0:
                                    drawing_functions.rest_recover_window.clear()
                                if len(drawing_functions.game_guide_container) > 0:
                                    drawing_functions.game_guide_container.clear()
                                if len(save_check_window) > 0:
                                    save_check_window.clear()
                                if len(drawing_functions.first_quest_window) > 0:
                                    drawing_functions.first_quest_window.clear()
                                if len(world_map_container) > 0:
                                    world_map_container.clear()
                                # clear character or journal sheet
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, False)
                                drawing_functions.journal_info_draw(journal, player, font, False)

                            # "F" key for player interaction
                            if event.key == K_f:
                                if player.current_zone == "nascent":
                                    if pygame.sprite.spritecollideany(player, interactables_nascent):
                                        interacted = True
                                if player.current_zone == "seldon":
                                    if pygame.sprite.spritecollideany(player, interactables_seldon):
                                        interacted = True
                                if player.current_zone == "stardust":
                                    if pygame.sprite.spritecollideany(player, interactables_stardust):
                                        interacted = True
                                if player.current_zone == "rohir":
                                    if pygame.sprite.collide_rect(player, dungeon_entrance):
                                        interacted = True
                                if player.current_zone == "reservoir a":
                                    if pygame.sprite.spritecollideany(player, dungeon_items):
                                        interacted = True
                                    if mini_boss_1:
                                        if pygame.sprite.collide_rect(player, chorizon_1):
                                            interacted = True
                                    if mini_boss_2:
                                        if pygame.sprite.collide_rect(player, chorizon_2):
                                            interacted = True
                                    if switch_3:
                                        if pygame.sprite.collide_rect(player, dungeon_teleporter):
                                            interacted = True
                                if player.current_zone == "reservoir b":
                                    if pygame.sprite.spritecollideany(player, interactables_reservoir_b):
                                        interacted = True
                                if player.current_zone == "reservoir c":
                                    if pygame.sprite.spritecollideany(player, interactables_reservoir_c):
                                        interacted = True
                                if player.current_zone == "korlok":
                                    if pygame.sprite.spritecollideany(player, interactables_korlok):
                                        interacted = True
                                if player.current_zone == "mines":
                                    if pygame.sprite.spritecollideany(player, interactables_mines):
                                        interacted = True
                                if player.current_zone == "terra trail":
                                    if pygame.sprite.spritecollideany(player, interactables_terra_trail):
                                        interacted = True
                        elif event.type == QUIT:
                            pygame.mixer.quit()
                            sys.exit()

                        # getting mouse position and highlighting buttons if they collide
                        pos = pygame.mouse.get_pos()
                        button_highlighted = button_highlighter(pos)

                        # continuing to use mouse position for clicking buttons
                        if event.type == pygame.MOUSEBUTTONUP:

                            gameplay_functions.role_swap(player, pos, graphic_dict, staff, sword, bow, pressed_keys)

                            # click handlers
                            info_choice = click_handlers.item_info_button(event, item_info_button, pygame, info_items)
                            if info_choice == "yes":
                                inventory_event = click_handlers.inventory(player, current_info_item)
                                if inventory_event["item message"] != "":
                                    info_text_1 = inventory_event["item message"]
                                    info_text_2 = ""
                                drawing_functions.item_info_window.clear()
                                button_highlighted = False
                            if info_choice == "no":
                                drawing_functions.item_info_window.clear()
                                button_highlighted = False

                            inventory_item_clicked = click_handlers.inventory_event_item(event, pygame)
                            if inventory_item_clicked["clicked"]:
                                current_info_item = drawing_functions.item_info_draw(inventory_item_clicked["element"],
                                                                                     info_items, item_info_button,
                                                                                     graphic_dict)

                            if len(drawing_functions.item_info_window) == 0:
                                equipment_event = click_handlers.equipment(player, event, pygame, basic_armor,
                                                                           forged_armor, mythical_armor,
                                                                           legendary_armor, power_gloves)
                                if equipment_event["equipment message"] != "":
                                    button_highlighted = False
                                    info_text_1 = equipment_event["equipment message"]
                                    info_text_2 = ""

                            # map button was clicked, set animation and move player to stone
                            if map_button.rect.collidepoint(pos):
                                # clears other windows first, if they were open
                                drawing_functions.journal_info_draw(journal, player, font, False)
                                journal_button_clicked = False
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, False)
                                character_button_clicked = False
                                save_check_window.clear()
                                saving = False
                                button_highlighted = False

                                if map_button_clicked:
                                    drawing_functions.world_map_container.clear()
                                    map_button_clicked = False
                                else:
                                    map_button_clicked = True
                                    info_text_1 = "Click an area to travel there. "
                                    info_text_2 = ""
                                    info_text_3 = ""
                                    info_text_4 = ""

                                    drawing_functions.mini_map(player, graphic_dict, world_map, seldon_map_button,
                                                               korlok_map_button, eldream_map_button, marrow_map_button,
                                                               amuna_location, nuldar_location, sorae_location)

                            # save button was clicked. Save player info in dictionary to be loaded later
                            if save_button.rect.collidepoint(pos):
                                try:
                                    # clears other windows first, if they were open
                                    drawing_functions.character_sheet_info_draw(character_sheet, player, font, False)
                                    character_button_clicked = False
                                    drawing_functions.journal_info_draw(journal, player, font, False)
                                    journal_button_clicked = False
                                    world_map_container.clear()
                                    map_button_clicked = False

                                    saving = True
                                    yes_button.update(450, 394, graphic_dict["yes_button_img"])
                                    # see if there already exists a save file by trying to read it
                                    try:
                                        directory = os.getcwd()
                                        save_directory = directory + "/saves/save_game"
                                        assert os.path.isfile(save_directory)
                                        with open(save_directory, "rb") as f:
                                            saved = True
                                    except FileNotFoundError and AssertionError:
                                        saved = False
                                        pass
                                    if saved:
                                        save_check_window.append(save_check)
                                        save_check_window.append(yes_button)
                                        save_check_window.append(no_button)
                                    if not saved:
                                        gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                                     sharp_sense_learned, saved, npc_garan.gift,
                                                                     rest_recover_show, knowledge_academia_show,
                                                                     quest_guide_shown, battle_guide_shown,
                                                                     rest_shown_before, quest_highlight_popup,
                                                                     bridge_not_repaired, nede_ghoul_defeated,
                                                                     bridge_cutscenes_not_viewed, crate_1, crate_2,
                                                                     crate_3, crate_4, crate_5, switch_1, switch_2,
                                                                     switch_3, muchador_defeated, has_key,
                                                                     mini_boss_1_defeated, mini_boss_2_defeated,
                                                                     gloves_obtained, korlok_attuned, eldream_attuned)
                                        saved = True
                                        saving = False
                                        info_text_1 = "You saved your game. "
                                except PermissionError:
                                    pass
                            if yes_button.rect.collidepoint(pos) and saving:
                                gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                             sharp_sense_learned, saved, npc_garan.gift,
                                                             rest_recover_show, knowledge_academia_show,
                                                             quest_guide_shown, battle_guide_shown, rest_shown_before,
                                                             quest_highlight_popup, bridge_not_repaired,
                                                             nede_ghoul_defeated, bridge_cutscenes_not_viewed, crate_1,
                                                             crate_2, crate_3, crate_4, crate_5, switch_1, switch_2,
                                                             switch_3, muchador_defeated, has_key, mini_boss_1_defeated,
                                                             mini_boss_2_defeated, gloves_obtained, korlok_attuned,
                                                             eldream_attuned)
                                save_check_window.clear()
                                button_highlighted = False
                                saving = False
                                info_text_1 = "You saved your game. "
                            if no_button.rect.collidepoint(pos) and saving:
                                save_check_window.clear()
                                saving = False
                                button_highlighted = False

                            if character_button.rect.collidepoint(pos):
                                # clears other open windows first, if they were open
                                drawing_functions.journal_info_draw(journal, player, font, False)
                                journal_button_clicked = False
                                world_map_container.clear()
                                map_button_clicked = False
                                save_check_window.clear()
                                saving = False
                                button_highlighted = False

                                if character_button_clicked:
                                    drawing_functions.character_sheet_info_draw(character_sheet, player, font, False)
                                    character_button_clicked = False
                                else:
                                    drawing_functions.character_sheet_info_draw(character_sheet, player, font, True)
                                    character_button_clicked = True

                            if quests_button.rect.collidepoint(pos):
                                # clears other windows first, if they were open
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, False)
                                character_button_clicked = False
                                world_map_container.clear()
                                map_button_clicked = False
                                save_check_window.clear()
                                saving = False
                                button_highlighted = False

                                if journal_button_clicked:
                                    drawing_functions.journal_info_draw(journal, player, font, False)
                                    journal_button_clicked = False
                                else:
                                    drawing_functions.journal_info_draw(journal, player, font, True)
                                    journal_button_clicked = True

                            # for clicking map buttons, when the map is open
                            if len(drawing_functions.world_map_container) > 0:
                                if seldon_map_button.rect.collidepoint(pos):
                                    player.current_zone = "seldon"
                                    drawing_functions.hearthstone_animation(pygame, screen, player,
                                                                            seldon_hearth_screen, seldon_district_bg,
                                                                            korlok_hearth_screen, korlok_district_bg)
                                    player.x_coordinate = 860
                                    player.y_coordinate = 655
                                    player.rect = player.surf.get_rect(midbottom=(player.x_coordinate,
                                                                                  player.y_coordinate))
                                    hearth_stone.update(860, 595, graphic_dict["hearth_stone"])
                                    info_text_1 = "You recalled to the seldon stone."
                                    over_world_song_set = False
                                    stardust_song_set = False
                                    drawing_functions.world_map_container.clear()
                                    map_button_clicked = False
                                if korlok_map_button.rect.collidepoint(pos):
                                    if korlok_attuned:
                                        player.current_zone = "korlok"
                                        drawing_functions.hearthstone_animation(pygame, screen, player,
                                                                                seldon_hearth_screen,
                                                                                seldon_district_bg,
                                                                                korlok_hearth_screen,
                                                                                korlok_district_bg)
                                        player.x_coordinate = 895
                                        player.y_coordinate = 325
                                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate,
                                                                                      player.y_coordinate))
                                        hearth_stone.update(885, 230, graphic_dict["hearth_stone"])
                                        info_text_1 = "You recalled to the korlok stone."
                                        over_world_song_set = False
                                        stardust_song_set = False
                                        drawing_functions.world_map_container.clear()
                                        map_button_clicked = False
                                    else:
                                        info_text_1 = "You have not yet attuned there. "
                                        info_text_2 = ""
                                if eldream_map_button.rect.collidepoint(pos):
                                    if eldream_attuned:
                                        player.current_zone = "eldream"
                                        drawing_functions.hearthstone_animation(pygame, screen, player,
                                                                                seldon_hearth_screen,
                                                                                seldon_district_bg,
                                                                                korlok_hearth_screen,
                                                                                korlok_district_bg)
                                        player.x_coordinate = hearth_stone.x_coordinate
                                        player.y_coordinate = hearth_stone.y_coordinate + 50
                                        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate,
                                                                                      player.y_coordinate))
                                        info_text_1 = "You recalled to the eldream stone."
                                        over_world_song_set = False
                                        stardust_song_set = False
                                        drawing_functions.world_map_container.clear()
                                        map_button_clicked = False
                                    else:
                                        info_text_1 = "You have not yet attuned there. "
                                        info_text_2 = ""
                                if marrow_map_button.rect.collidepoint(pos):
                                    info_text_1 = "You have not yet attuned there. "
                                    info_text_2 = ""

                            # pop-up notifications, click to hide
                            if knowledge_academia.rect.collidepoint(pos):
                                drawing_functions.knowledge_academia_window.clear()
                            if rest_recover.rect.collidepoint(pos):
                                drawing_functions.rest_recover_window.clear()
                            if loot_popup.rect.collidepoint(pos):
                                drawing_functions.loot_popup_container.clear()
                                drawing_functions.loot_text_container.clear()
                            if first_quest.rect.collidepoint(pos):
                                drawing_functions.first_quest_window.clear()
                            if game_guide_overlay.rect.collidepoint(pos):
                                drawing_functions.game_guide_container.clear()
                            if level_up_win.rect.collidepoint(pos):
                                drawing_functions.level_up_draw(level_up_win, player, font, False)

                # ------------------------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if player is in nascent grove (starting area) --------------------------------------------------------
                if player.current_zone == "nascent" and in_over_world and not in_shop and not in_inn \
                        and not in_academia and not in_battle and not in_npc_interaction:

                    pygame.mixer.music.fadeout(3000)
                    screen.blit(nascent_grove_bg, (0, 0))
                    screen.blit(equipment_screen.surf, equipment_screen.rect)
                    screen.blit(nascent_gate.surf, nascent_gate.rect)
                    screen.blit(player.surf, player.rect)

                    if pygame.sprite.collide_rect(player, nascent_gate):
                        screen.blit(nascent_gate_popup.surf, nascent_gate_popup.rect)
                        if interacted and in_over_world:
                            nascent_gate.update(nascent_gate.x_coordinate, nascent_gate.y_coordinate,
                                                graphic_dict["nascent_gate_open"])
                            if player.y_coordinate > 300:
                                player.y_coordinate = 215
                            else:
                                player.y_coordinate = 375
                            interacted = False
                    else:
                        nascent_gate.update(nascent_gate.x_coordinate, nascent_gate.y_coordinate,
                                            graphic_dict["nascent_gate_closed"])

                    # move player to seldon district when they approach nascent grove exit
                    if player.x_coordinate > 700 and player.y_coordinate < 80:
                        player.current_zone = "seldon"
                        in_over_world = True
                        player.x_coordinate = 425
                        player.y_coordinate = 690

                # ------------------------------------------------------------------------------------------------------
                # if player is in seldon district ----------------------------------------------------------------------
                if player.current_zone == "seldon" and in_over_world and not in_shop and not in_inn \
                        and not in_academia and not in_battle and not in_npc_interaction:

                    seldon_returned = seldon.seldon_district(pygame, player, screen, graphic_dict, rohir_gate,
                                                             hearth_stone, over_world_song_set, seldon_overworld_music,
                                                             seldon_district_bg, seldon_enemies, korlok_enemies, snakes,
                                                             ghouls, magmons, bandiles, interactables_seldon,
                                                             interactables_korlok, Enemy, Item, UiElement, most_sprites,
                                                             quest_items_seldon, log_sprite_reset, snake_sprite_reset,
                                                             ghoul_sprite_reset, nede, quest_star_garan,
                                                             quest_star_maurelle, quest_star_celeste, quest_star_torune,
                                                             interaction_popup, font, interacted, in_over_world,
                                                             bridge_not_repaired, bridge_cutscenes_not_viewed,
                                                             apothis_intro_music, apothis_scene_1, apothis_scene_2,
                                                             apothis_scene_3, apothis_scene_4, apothis_scene_5,
                                                             apothis_scene_6, skip_button, player_battle_sprite,
                                                             snake_battle_sprite, ghoul_battle_sprite,
                                                             chorizon_battle_sprite, muchador_battle_sprite,
                                                             barrier_active, sharp_sense_active, in_npc_interaction,
                                                             amuna_buildings, npcs_seldon, save_check_window,
                                                             user_interface, world_map_container, bar_backdrop, hp_bar,
                                                             en_bar, xp_bar, button_highlighted, button_highlight,
                                                             knowledge_academia_show, knowledge_academia,
                                                             rest_recover_show, rest_shown_before, rest_recover,
                                                             quest_guide_shown, game_guide_overlay, enemy_tic, npc_tic,
                                                             npc_garan, npc_maurelle, npc_celeste,
                                                             npc_torune, info_text_1, info_text_2, info_text_3,
                                                             info_text_4, in_battle, in_shop, in_academia, in_inn,
                                                             movement_able, current_enemy_battling,
                                                             current_npc_interacting, current_building_entering,
                                                             magmon_battle_sprite, bandile_battle_sprite,
                                                             chinzilla_battle_sprite, interactables_mines,
                                                             quest_star_voruke, quest_star_zerah, quest_star_kirean,
                                                             quest_star_dionte, equipment_screen, staff, sword, bow,
                                                             offense_meter, defense_meter, weapon_select)

                    over_world_song_set = seldon_returned["over_world_song_set"]
                    interactables_seldon = seldon_returned["interactables_seldon"]
                    interactables_korlok = seldon_returned["interactables_korlok"]
                    korlok_enemies = seldon_returned["korlok_enemies"]
                    magmons = seldon_returned["magmons"]
                    bandiles = seldon_returned["bandiles"]
                    log_sprite_reset = seldon_returned["log_sprite_reset"]
                    snake_sprite_reset = seldon_returned["snake_sprite_reset"]
                    ghoul_sprite_reset = seldon_returned["ghoul_sprite_reset"]
                    bridge_cutscenes_not_viewed = seldon_returned["bridge_cutscenes_not_viewed"]
                    current_enemy_battling = seldon_returned["current_enemy_battling"]
                    current_building_entering = seldon_returned["current_building_entering"]
                    current_npc_interacting = seldon_returned["current_npc_interacting"]
                    knowledge_academia_show = seldon_returned["knowledge_academia_show"]
                    rest_recover_show = seldon_returned["rest_recover_show"]
                    rest_shown_before = seldon_returned["rest_shown_before"]
                    quest_guide_shown = seldon_returned["quest_guide_shown"]
                    enemy_tic = seldon_returned["enemy_tic"]
                    npc_tic = seldon_returned["npc_tic"]
                    info_text_1 = seldon_returned["info_text_1"]
                    info_text_2 = seldon_returned["info_text_2"]
                    info_text_3 = seldon_returned["info_text_3"]
                    info_text_4 = seldon_returned["info_text_4"]
                    interacted = seldon_returned["interacted"]
                    in_over_world = seldon_returned["in_over_world"]
                    in_battle = seldon_returned["in_battle"]
                    in_shop = seldon_returned["in_shop"]
                    in_academia = seldon_returned["in_academia"]
                    in_inn = seldon_returned["in_inn"]
                    in_npc_interaction = seldon_returned["in_npc_interaction"]
                    movement_able = seldon_returned["movement_able"]

                    loot_popup_returned = drawing_functions.loot_popups(time, loot_updated, font, loot_popup,
                                                                        battle_info_to_return_to_main_loop, leveled)
                    try:
                        loot_updated = loot_popup_returned["loot_updated"]
                        loot_level_tic = loot_popup_returned["loot_level_tic"]
                        loot_info = loot_popup_returned["loot_info"]
                        leveled = loot_popup_returned["leveled"]
                    except TypeError:
                        pass

                # ------------------------------------------------------------------------------------------------------
                # if player is in korlok district ----------------------------------------------------------------------
                if player.current_zone == "korlok" and in_over_world and not in_shop and not in_inn \
                        and not in_academia and not in_battle and not in_npc_interaction:

                    korlok_returned = korlok.korlok_district(pygame, screen, graphic_dict, player, korlok_district_bg,
                                                             korlok_overworld_music, over_world_song_set,
                                                             nuldar_buildings, rohir_gate, hearth_stone, mines_entrance,
                                                             magmons, interaction_popup, font, bridge_not_repaired,
                                                             reservoir_enter, rock_1, rock_2, save_check_window,
                                                             user_interface, world_map_container, bar_backdrop, hp_bar,
                                                             en_bar, xp_bar, button_highlighted, button_highlight,
                                                             in_over_world, korlok_attuned, interacted, info_text_1,
                                                             info_text_2, info_text_3, info_text_4, enemy_tic, npc_tic,
                                                             in_battle, in_shop, in_academia, in_inn,
                                                             in_npc_interaction, movement_able, current_enemy_battling,
                                                             current_npc_interacting, current_building_entering,
                                                             korlok_enemies, player_battle_sprite, snake_battle_sprite,
                                                             ghoul_battle_sprite, chorizon_battle_sprite,
                                                             muchador_battle_sprite, barrier_active, sharp_sense_active,
                                                             magmon_battle_sprite, bandile_battle_sprite,
                                                             chinzilla_battle_sprite, npc_voruke,
                                                             npc_zerah, npcs_korlok, seldon_enemies, snakes, ghouls,
                                                             bandiles, interactables_seldon, interactables_korlok,
                                                             Enemy, Item, UiElement, interactables_mines,
                                                             quest_star_garan, quest_star_maurelle, quest_star_celeste,
                                                             quest_star_torune, quest_star_voruke, quest_star_zerah,
                                                             korlok_mountains, in_apothecary, quest_star_kirean,
                                                             quest_star_dionte, equipment_screen, staff, sword, bow,
                                                             npc_garan, offense_meter, defense_meter, weapon_select)

                    over_world_song_set = korlok_returned["over_world_song_set"]
                    korlok_attuned = korlok_returned["korlok_attuned"]
                    interacted = korlok_returned["interacted"]
                    in_over_world = korlok_returned["in_over_world"]
                    in_battle = korlok_returned["in_battle"]
                    in_shop = korlok_returned["in_shop"]
                    in_academia = korlok_returned["in_academia"]
                    in_apothecary = korlok_returned["in_apothecary"]
                    in_inn = korlok_returned["in_inn"]
                    in_npc_interaction = korlok_returned["in_npc_interaction"]
                    movement_able = korlok_returned["movement_able"]
                    current_enemy_battling = korlok_returned["current_enemy_battling"]
                    current_building_entering = korlok_returned["current_building_entering"]
                    current_npc_interacting = korlok_returned["current_npc_interacting"]
                    enemy_tic = korlok_returned["enemy_tic"]
                    npc_tic = korlok_returned["npc_tic"]
                    info_text_1 = korlok_returned["info_text_1"]
                    info_text_2 = korlok_returned["info_text_2"]
                    info_text_3 = korlok_returned["info_text_3"]
                    info_text_4 = korlok_returned["info_text_4"]

                    loot_popup_returned = drawing_functions.loot_popups(time, loot_updated, font, loot_popup,
                                                                        battle_info_to_return_to_main_loop, leveled)
                    try:
                        loot_updated = loot_popup_returned["loot_updated"]
                        loot_level_tic = loot_popup_returned["loot_level_tic"]
                        loot_info = loot_popup_returned["loot_info"]
                        leveled = loot_popup_returned["leveled"]
                    except TypeError:
                        pass

                # ------------------------------------------------------------------------------------------------------
                # if player is in korlok district ----------------------------------------------------------------------
                if player.current_zone == "mines" and in_over_world and not in_shop and not in_inn \
                        and not in_academia and not in_battle and not in_npc_interaction:

                    mines_returned = mines.korlok_mines(pygame, screen, graphic_dict, player, korlok_mines_bg,
                                                        korlok_overworld_music, over_world_song_set, bandiles,
                                                        interaction_popup, font, save_check_window, user_interface,
                                                        world_map_container, bar_backdrop, hp_bar, en_bar, xp_bar,
                                                        button_highlighted, button_highlight, in_over_world,
                                                        interacted, info_text_1, info_text_2, info_text_3, info_text_4,
                                                        enemy_tic, npc_tic, in_battle, in_npc_interaction,
                                                        movement_able, current_enemy_battling, player_battle_sprite,
                                                        snake_battle_sprite, ghoul_battle_sprite,
                                                        chorizon_battle_sprite, muchador_battle_sprite,
                                                        chinzilla_battle_sprite, barrier_active,
                                                        sharp_sense_active, magmon_battle_sprite, bandile_battle_sprite,
                                                        seldon_enemies, korlok_enemies, snakes, ghouls, magmons,
                                                        interactables_seldon, interactables_korlok, Enemy, Item,
                                                        UiElement, interactables_mines, ores, equipment_screen, staff,
                                                        sword, bow, npc_garan, offense_meter, defense_meter,
                                                        weapon_select)

                    over_world_song_set = mines_returned["over_world_song_set"]
                    interacted = mines_returned["interacted"]
                    in_over_world = mines_returned["in_over_world"]
                    in_battle = mines_returned["in_battle"]
                    movement_able = mines_returned["movement_able"]
                    current_enemy_battling = mines_returned["current_enemy_battling"]
                    enemy_tic = mines_returned["enemy_tic"]
                    npc_tic = mines_returned["npc_tic"]
                    info_text_1 = mines_returned["info_text_1"]
                    info_text_2 = mines_returned["info_text_2"]
                    info_text_3 = mines_returned["info_text_3"]
                    info_text_4 = mines_returned["info_text_4"]

                    loot_popup_returned = drawing_functions.loot_popups(time, loot_updated, font, loot_popup,
                                                                        battle_info_to_return_to_main_loop, leveled)
                    try:
                        loot_updated = loot_popup_returned["loot_updated"]
                        loot_level_tic = loot_popup_returned["loot_level_tic"]
                        loot_info = loot_popup_returned["loot_info"]
                        leveled = loot_popup_returned["leveled"]
                    except TypeError:
                        pass

                # ------------------------------------------------------------------------------------------------------
                # if player is in korlok district ----------------------------------------------------------------------
                if player.current_zone == "terra trail" and in_over_world and not in_shop and not in_inn \
                        and not in_academia and not in_battle and not in_npc_interaction:

                    trail_returned = trail.terra_trail(pygame, screen, graphic_dict, player, mountain_trail_bg,
                                                       korlok_overworld_music, over_world_song_set,
                                                       interaction_popup, font, save_check_window, user_interface,
                                                       world_map_container, bar_backdrop, hp_bar, en_bar, xp_bar,
                                                       button_highlighted, button_highlight, in_over_world, interacted,
                                                       info_text_1, info_text_2, info_text_3, info_text_4, npc_tic,
                                                       in_npc_interaction, in_battle, movement_able,
                                                       current_enemy_battling, quest_star_garan, quest_star_maurelle,
                                                       quest_star_celeste, quest_star_torune, quest_star_voruke,
                                                       quest_star_zerah, quest_star_apothecary, terra_mountains,
                                                       terra_cave, npc_dionte, quest_star_dionte, Enemy,
                                                       player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite,
                                                       chorizon_battle_sprite, muchador_battle_sprite,
                                                       magmon_battle_sprite, bandile_battle_sprite,
                                                       chinzilla_battle_sprite, barrier_active, sharp_sense_active,
                                                       current_npc_interacting, chinzilla, quest_star_dionte,
                                                       hearth_stone, equipment_screen, staff, sword, bow, npc_garan,
                                                       offense_meter, defense_meter, weapon_select)

                    over_world_song_set = trail_returned["over_world_song_set"]
                    interacted = trail_returned["interacted"]
                    in_over_world = trail_returned["in_over_world"]
                    in_battle = trail_returned["in_battle"]
                    in_npc_interaction = trail_returned["in_npc_interaction"]
                    current_enemy_battling = trail_returned["current_enemy_battling"]
                    current_npc_interacting = trail_returned["current_npc_interacting"]
                    movement_able = trail_returned["movement_able"]
                    npc_tic = trail_returned["npc_tic"]
                    info_text_1 = trail_returned["info_text_1"]
                    info_text_2 = trail_returned["info_text_2"]
                    info_text_3 = trail_returned["info_text_3"]
                    info_text_4 = trail_returned["info_text_4"]

                    loot_popup_returned = drawing_functions.loot_popups(time, loot_updated, font, loot_popup,
                                                                        battle_info_to_return_to_main_loop, leveled)
                    try:
                        loot_updated = loot_popup_returned["loot_updated"]
                        loot_level_tic = loot_popup_returned["loot_level_tic"]
                        loot_info = loot_popup_returned["loot_info"]
                        leveled = loot_popup_returned["leveled"]
                    except TypeError:
                        pass

                # ------------------------------------------------------------------------------------------------------
                # if player is in stardust outpost ---------------------------------------------------------------------
                if player.current_zone == "stardust" and in_over_world and not in_shop and not in_inn \
                        and not in_academia and not in_battle and not in_npc_interaction:

                    stardust_returned = stardust.stardust_outpost(pygame, player, screen, stardust_song_set,
                                                                  stardust_outpost_music, stardust_cove_bg,
                                                                  nede_sprite_reset, nede, graphic_dict, ghoul_nede,
                                                                  nede_ghoul_defeated, interaction_popup, font,
                                                                  interacted, in_over_world, player_battle_sprite,
                                                                  snake_battle_sprite, ghoul_battle_sprite,
                                                                  chorizon_battle_sprite, muchador_battle_sprite,
                                                                  barrier_active, sharp_sense_active,
                                                                  in_npc_interaction, stardust_entrance,
                                                                  save_check_window, user_interface,
                                                                  world_map_container, bar_backdrop, hp_bar, en_bar,
                                                                  xp_bar, button_highlighted, button_highlight,
                                                                  npc_tic, info_text_1, info_text_2, info_text_3,
                                                                  info_text_4, current_enemy_battling,
                                                                  current_building_entering, in_battle, movement_able,
                                                                  in_shop, magmon_battle_sprite, bandile_battle_sprite,
                                                                  chinzilla_battle_sprite, equipment_screen, staff,
                                                                  sword, bow, npc_garan, offense_meter, defense_meter,
                                                                  weapon_select)

                    stardust_song_set = stardust_returned["stardust_song_set"]
                    nede_sprite_reset = stardust_returned["nede_sprite_reset"]
                    current_enemy_battling = stardust_returned["current_enemy_battling"]
                    in_battle = stardust_returned["in_battle"]
                    in_over_world = stardust_returned["in_over_world"]
                    info_text_1 = stardust_returned["info_text_1"]
                    info_text_2 = stardust_returned["info_text_2"]
                    info_text_3 = stardust_returned["info_text_3"]
                    info_text_4 = stardust_returned["info_text_4"]
                    movement_able = stardust_returned["movement_able"]
                    current_building_entering = stardust_returned["current_building_entering"]
                    in_shop = stardust_returned["in_shop"]
                    interacted = stardust_returned["interacted"]
                    npc_tic = stardust_returned["npc_tic"]

                    loot_popup_returned = drawing_functions.loot_popups(time, loot_updated, font, loot_popup,
                                                                        battle_info_to_return_to_main_loop, leveled)
                    try:
                        loot_updated = loot_popup_returned["loot_updated"]
                        loot_level_tic = loot_popup_returned["loot_level_tic"]
                        loot_info = loot_popup_returned["loot_info"]
                        leveled = loot_popup_returned["leveled"]
                    except TypeError:
                        pass

                # ------------------------------------------------------------------------------------------------------
                # if player is in rohir river (after apothis cutscene) -------------------------------------------------
                if player.current_zone == "rohir" and in_over_world and not in_shop and not in_inn \
                        and not in_academia and not in_battle and not in_npc_interaction:

                    rohir_returned = rohir.rohir_river(pygame, screen, player, over_world_song_set, rohir_river_bg,
                                                       dungeon_entrance, water_1, water_2, water_3, water_4, water_5,
                                                       water_player, graphic_dict, save_check_window, user_interface,
                                                       world_map_container, bar_backdrop, hp_bar, en_bar, xp_bar, font,
                                                       info_text_1, info_text_2, info_text_3, info_text_4,
                                                       in_over_world, button_highlighted, button_highlight,
                                                       rohir_river_music, interaction_popup, interacted,
                                                       equipment_screen, staff, sword, bow, npc_garan, offense_meter,
                                                       defense_meter, weapon_select)

                    over_world_song_set = rohir_returned["over_world_song_set"]
                    info_text_1 = rohir_returned["info_text_1"]
                    info_text_2 = rohir_returned["info_text_2"]
                    info_text_3 = rohir_returned["info_text_3"]
                    info_text_4 = rohir_returned["info_text_4"]
                    in_over_world = rohir_returned["in_over_world"]
                    interacted = rohir_returned["interacted"]

                    loot_popup_returned = drawing_functions.loot_popups(time, loot_updated, font, loot_popup,
                                                                        battle_info_to_return_to_main_loop, leveled)
                    try:
                        loot_updated = loot_popup_returned["loot_updated"]
                        loot_level_tic = loot_popup_returned["loot_level_tic"]
                        loot_info = loot_popup_returned["loot_info"]
                        leveled = loot_popup_returned["leveled"]
                    except TypeError:
                        pass

                # ------------------------------------------------------------------------------------------------------
                # if player is in first dungeon, first floor -----------------------------------------------------------
                if player.current_zone == "reservoir a" and in_over_world and not in_shop and not in_inn \
                        and not in_academia and not in_battle and not in_npc_interaction:

                    reservoir_a_returned = reservoir.reservoir_a(pygame, screen, SCREEN_HEIGHT, graphic_dict, player,
                                                                 reservoir_a_bg, reservoir_music, over_world_song_set,
                                                                 interaction_popup, font, save_check_window,
                                                                 user_interface, world_map_container,
                                                                 loot_popup_container, loot_text_container,
                                                                 bar_backdrop, hp_bar, en_bar, xp_bar,
                                                                 button_highlighted, button_highlight, in_over_world,
                                                                 interacted, info_text_1, info_text_2, info_text_3,
                                                                 info_text_4, switch_1, dungeon_switch_1, switch_2,
                                                                 dungeon_switch_2, switch_3, dungeon_switch_3,
                                                                 dungeon_walls, dungeon_items, dungeon_teleporter,
                                                                 mini_boss_1, dungeon_drop_wall, chorizon_1,
                                                                 mini_boss_2, chorizon_2, crate_1, Item, crate_2,
                                                                 crate_3, crate_4, mini_boss_1_defeated,
                                                                 mini_boss_2_defeated, boss_enemies,
                                                                 player_battle_sprite, snake_battle_sprite,
                                                                 ghoul_battle_sprite, chorizon_battle_sprite,
                                                                 muchador_battle_sprite, barrier_active,
                                                                 sharp_sense_active, in_npc_interaction,
                                                                 magmon_battle_sprite, bandile_battle_sprite,
                                                                 chinzilla_battle_sprite, equipment_screen, staff,
                                                                 sword, bow, npc_garan, offense_meter, defense_meter,
                                                                 weapon_select)

                    over_world_song_set = reservoir_a_returned["over_world_song_set"]
                    interacted = reservoir_a_returned["interacted"]
                    info_text_1 = reservoir_a_returned["info_text_1"]
                    info_text_2 = reservoir_a_returned["info_text_2"]
                    crate_1 = reservoir_a_returned["crate_1"]
                    crate_2 = reservoir_a_returned["crate_2"]
                    crate_3 = reservoir_a_returned["crate_3"]
                    crate_4 = reservoir_a_returned["crate_4"]
                    switch_1 = reservoir_a_returned["switch_1"]
                    switch_2 = reservoir_a_returned["switch_2"]
                    switch_3 = reservoir_a_returned["switch_3"]
                    mini_boss_1 = reservoir_a_returned["mini_boss_1"]
                    mini_boss_2 = reservoir_a_returned["mini_boss_2"]
                    current_enemy_battling = reservoir_a_returned["current_enemy_battling"]
                    in_over_world = reservoir_a_returned["in_over_world"]
                    in_battle = reservoir_a_returned["in_battle"]

                    loot_popup_returned = drawing_functions.loot_popups(time, loot_updated, font, loot_popup,
                                                                        battle_info_to_return_to_main_loop, leveled)
                    try:
                        loot_updated = loot_popup_returned["loot_updated"]
                        loot_level_tic = loot_popup_returned["loot_level_tic"]
                        loot_info = loot_popup_returned["loot_info"]
                        leveled = loot_popup_returned["leveled"]
                    except TypeError:
                        pass

                # ------------------------------------------------------------------------------------------------------
                # if player is in first dungeon, second floor ----------------------------------------------------------
                if player.current_zone == "reservoir b" and in_over_world and not in_shop and not in_inn \
                        and not in_academia and not in_battle and not in_npc_interaction:

                    reservoir_b_returned = reservoir.reservoir_b(pygame, player, screen, graphic_dict,
                                                                 over_world_song_set, reservoir_music,
                                                                 dungeon_teleporter, reservoir_b_bg, dungeon_gate,
                                                                 crate_5, dungeon_crate_5, muchador_lights_on,
                                                                 muchador_arena, muchador_defeated, muchador,
                                                                 muchador_crate_1, muchador_crate_2, muchador_crate_3,
                                                                 muchador_crate_4, reservoir_passage, interaction_popup,
                                                                 font, interacted, SCREEN_WIDTH, save_check_window,
                                                                 player_battle_sprite, snake_battle_sprite,
                                                                 ghoul_battle_sprite, chorizon_battle_sprite,
                                                                 muchador_battle_sprite, barrier_active,
                                                                 sharp_sense_active, in_npc_interaction, user_interface,
                                                                 world_map_container, bar_backdrop, hp_bar, en_bar,
                                                                 xp_bar, button_highlighted, button_highlight,
                                                                 info_text_1, info_text_2, info_text_3, info_text_4,
                                                                 in_over_world, switch_1, switch_2, switch_3, has_key,
                                                                 magmon_battle_sprite, bandile_battle_sprite,
                                                                 chinzilla_battle_sprite, equipment_screen, staff,
                                                                 sword, bow, npc_garan, offense_meter, defense_meter,
                                                                 weapon_select)

                    over_world_song_set = reservoir_b_returned["over_world_song_set"]
                    interacted = reservoir_b_returned["interacted"]
                    info_text_1 = reservoir_b_returned["info_text_1"]
                    info_text_2 = reservoir_b_returned["info_text_2"]
                    muchador_lights_on = reservoir_b_returned["muchador_lights_on"]
                    switch_1 = reservoir_b_returned["switch_1"]
                    switch_2 = reservoir_b_returned["switch_2"]
                    switch_3 = reservoir_b_returned["switch_3"]
                    crate_5 = reservoir_b_returned["crate_5"]
                    current_enemy_battling = reservoir_b_returned["current_enemy_battling"]
                    in_over_world = reservoir_b_returned["in_over_world"]
                    in_battle = reservoir_b_returned["in_battle"]
                    has_key = reservoir_b_returned["has_key"]

                    loot_popup_returned = drawing_functions.loot_popups(time, loot_updated, font, loot_popup,
                                                                        battle_info_to_return_to_main_loop, leveled)
                    try:
                        loot_updated = loot_popup_returned["loot_updated"]
                        loot_level_tic = loot_popup_returned["loot_level_tic"]
                        loot_info = loot_popup_returned["loot_info"]
                        leveled = loot_popup_returned["leveled"]
                    except TypeError:
                        pass

                # ------------------------------------------------------------------------------------------------------
                # if player is in first dungeon, third floor -----------------------------------------------------------
                if player.current_zone == "reservoir c" and in_over_world and not in_shop and not in_inn \
                        and not in_academia and not in_battle and not in_npc_interaction:

                    reservoir_c_returned = reservoir.reservoir_c(pygame, player, screen, graphic_dict,
                                                                 over_world_song_set, reservoir_music,
                                                                 interaction_popup, font, interacted, save_check_window,
                                                                 user_interface, world_map_container, bar_backdrop,
                                                                 hp_bar, en_bar, xp_bar, button_highlighted,
                                                                 button_highlight, reservoir_c_bg, dungeon_chest,
                                                                 reservoir_exit, rock_1, rock_2, gloves_obtained,
                                                                 power_gloves, info_text_1, info_text_2, info_text_3,
                                                                 info_text_4, in_over_world, has_key,
                                                                 muchador_lights_on, hearth_stone, equipment_screen,
                                                                 staff, sword, bow, npc_garan, offense_meter,
                                                                 defense_meter, weapon_select)

                    over_world_song_set = reservoir_c_returned["over_world_song_set"]
                    interacted = reservoir_c_returned["interacted"]
                    muchador_lights_on = reservoir_c_returned["muchador_lights_on"]
                    gloves_obtained = reservoir_c_returned["gloves_obtained"]
                    has_key = reservoir_c_returned["has_key"]
                    info_text_1 = reservoir_c_returned["info_text_1"]
                    info_text_2 = reservoir_c_returned["info_text_2"]
                    info_text_3 = reservoir_c_returned["info_text_3"]
                    info_text_4 = reservoir_c_returned["info_text_4"]

                    loot_popup_returned = drawing_functions.loot_popups(time, loot_updated, font, loot_popup,
                                                                        battle_info_to_return_to_main_loop, leveled)
                    try:
                        loot_updated = loot_popup_returned["loot_updated"]
                        loot_level_tic = loot_popup_returned["loot_level_tic"]
                        loot_info = loot_popup_returned["loot_info"]
                        leveled = loot_popup_returned["leveled"]
                    except TypeError:
                        pass

                # ------------------------------------------------------------------------------------------------------
                # if player is in battle -------------------------------------------------------------------------------
                if in_battle and not in_over_world and not in_shop and not in_inn and not in_academia \
                        and not in_npc_interaction:

                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_1:
                                attack_hotkey = True
                            if event.key == K_2:
                                skill_1_hotkey = True
                        elif event.type == QUIT:
                            pygame.mixer.quit()
                            sys.exit()

                        # getting mouse position and highlighting buttons if they collide
                        pos = pygame.mouse.get_pos()
                        button_highlighted = button_highlighter(pos)

                        if event.type == pygame.MOUSEBUTTONUP:

                            gameplay_functions.role_swap(player, pos, graphic_dict, staff, sword, bow, pressed_keys)

                            if game_guide_overlay.rect.collidepoint(pos):
                                game_guide_container.clear()

                        # get which button player pressed during combat scenario
                        combat_button = click_handlers.combat_event_button(event, no_role_attack_button,
                                                                           mage_attack_button, fighter_attack_button,
                                                                           scout_attack_button, barrier_button,
                                                                           hard_strike_button, sharp_sense_button,
                                                                           pygame)
                        # click handlers

                        info_choice = click_handlers.item_info_button(event, item_info_button, pygame, info_items)
                        if info_choice == "yes":
                            inventory_event = click_handlers.inventory(player, current_info_item)
                            if inventory_event["item message"] != "":
                                info_text_1 = inventory_event["item message"]
                                info_text_2 = ""
                            drawing_functions.item_info_window.clear()
                            button_highlighted = False
                        if info_choice == "no":
                            drawing_functions.item_info_window.clear()
                            button_highlighted = False

                        inventory_item_clicked = click_handlers.inventory_event_item(event, pygame)
                        if inventory_item_clicked["clicked"]:
                            current_info_item = drawing_functions.item_info_draw(inventory_item_clicked["element"],
                                                                                 info_items, item_info_button,
                                                                                 graphic_dict)

                        # function to handle equipment item clicks. apply item message to message box if not empty str.
                        if len(drawing_functions.item_info_window) == 0:
                            equipment_event = click_handlers.equipment(player, event, pygame, basic_armor, forged_armor,
                                                                       mythical_armor, legendary_armor, power_gloves)
                            if equipment_event["equipment message"] != "":
                                info_text_1 = equipment_event["equipment message"]
                                info_text_2 = ""

                        if combat_button == "attack" or attack_hotkey:
                            first_battle_cond = False
                            game_guide_container.clear()
                            if not combat_cooldown:
                                attack_hotkey = False
                                combat_scenario.combat_animation(player, current_enemy_battling, player_battle_sprite,
                                                                 snake_battle_sprite, ghoul_battle_sprite,
                                                                 chorizon_battle_sprite, muchador_battle_sprite,
                                                                 magmon_battle_sprite, bandile_battle_sprite,
                                                                 chinzilla_battle_sprite, barrier_active,
                                                                 sharp_sense_active, hard_strike, graphic_dict)

                                # combat event function that handles and returns damage and health
                                combat_events = combat_scenario.attack_scenario(current_enemy_battling, "attack",
                                                                                player, hard_strike_learned,
                                                                                level_up_win, level_up_font,
                                                                                graphic_dict)
                                combat_happened = True

                                # add all combat scenario happenings from function to message box
                                try:
                                    if combat_events["damage done string"] == 0:
                                        info_text_1 = ""
                                    else:
                                        info_text_1 = str(combat_events["damage done string"])
                                    if combat_events["damage taken string"] == 0:
                                        info_text_2 = ""
                                    else:
                                        info_text_2 = str(combat_events["damage taken string"])
                                except TypeError:
                                    pass

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
                                    if combat_events["leveled"]:
                                        battle_info_to_return_to_main_loop["leveled_up"] = True

                                # if player was successful in defeating enemy, combat ends, movement is allowed
                                if combat_events["enemy defeated"]:
                                    # player will gain knowledge based on their current role
                                    if player.role == "mage":
                                        player.knowledge["mage"] += 10
                                        battle_info_to_return_to_main_loop["knowledge"] = "+10 mage"
                                    if player.role == "fighter":
                                        player.knowledge["fighter"] += 10
                                        battle_info_to_return_to_main_loop["knowledge"] = "+10 fighter"
                                    if player.role == "scout":
                                        player.knowledge["scout"] += 10
                                        battle_info_to_return_to_main_loop["knowledge"] = "+10 scout"

                                    if current_enemy_battling.name == "nede ghoul":
                                        nede_ghoul_defeated = True
                                        ghoul_nede.kill()
                                    if current_enemy_battling.name == "chorizon_1":
                                        mini_boss_1_defeated = True
                                        mini_boss_1 = False
                                        chorizon_1.kill()
                                    if current_enemy_battling.name == "chorizon_2":
                                        mini_boss_2_defeated = True
                                        mini_boss_2 = False
                                        chorizon_2.kill()
                                    if current_enemy_battling.name == "muchador":
                                        muchador_defeated = True
                                        muchador.kill()

                                    # if barrier is active on enemy defeat, restore original defence and set off
                                    if barrier_active:
                                        barrier_active = False
                                        # noinspection PyUnboundLocalVariable

                                    # if sharp sense is active on enemy defeat, restore original offense
                                    if sharp_sense_active:
                                        sharp_sense_active = False
                                        # noinspection PyUnboundLocalVariable

                                    movement_able = True
                                    combat_happened = False
                                    interacted = False
                                    encounter_started = False
                                    in_battle = False
                                    in_over_world = True
                                    loot_updated = False

                        # (buffs) mage -> barrier [defence], scout -> sharp sense [offense]
                        elif combat_button == "skill 1" or skill_1_hotkey:
                            if not combat_cooldown:
                                skill_1_hotkey = False
                                # make sure player has enough energy to use the skill
                                if player.energy > 34:
                                    # player is a mage and uses the barrier spell. Set barrier active to true
                                    # save original defence value to be re applied upon enemy or player defeat
                                    if player.role == "mage":
                                        if barrier_learned:
                                            if not barrier_active:
                                                original_defence = player.defense
                                                info_text_1 = "Barrier spell is active."
                                                barrier_active = True
                                                player.energy -= 35
                                            else:
                                                info_text_1 = "Barrier spell is already active."
                                    # player is a scout and uses sharp sense. Set sharp sense active to true
                                    # save original offense value to be re applied upon enemy or player defeat
                                    if player.role == "scout":
                                        if sharp_sense_learned:
                                            if not sharp_sense_active:
                                                info_text_1 = "Sharp sense is active."
                                                sharp_sense_active = True
                                                player.energy -= 35
                                            else:
                                                info_text_1 = "Sharp sense is already active."
                                    # player is a fighter and uses hard strike
                                    if player.role == "fighter":
                                        if hard_strike_learned:
                                            hard_strike = True
                                            combat_scenario.fighter(player, player_battle_sprite,
                                                                    current_enemy_battling,
                                                                    snake_battle_sprite, ghoul_battle_sprite,
                                                                    chorizon_battle_sprite, muchador_battle_sprite,
                                                                    magmon_battle_sprite, bandile_battle_sprite,
                                                                    chinzilla_battle_sprite,
                                                                    graphic_dict["player_fighter_amuna_strike"],
                                                                    graphic_dict["player_fighter_sorae_strike"],
                                                                    graphic_dict["player_fighter_nuldar_strike"],
                                                                    graphic_dict["snake_battle"],
                                                                    graphic_dict["ghoul_battle"],
                                                                    graphic_dict["chorizon_battle"],
                                                                    graphic_dict["muchador_battle"],
                                                                    graphic_dict["magmon_battle"],
                                                                    graphic_dict["bandile_battle"],
                                                                    graphic_dict["chinzilla_battle"])

                                            combat_events = combat_scenario.attack_scenario(current_enemy_battling,
                                                                                            "skill 1", player,
                                                                                            hard_strike_learned,
                                                                                            level_up_win, level_up_font,
                                                                                            graphic_dict)
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
                                                if player.role == "fighter":
                                                    player.knowledge["fighter"] += 10
                                                    battle_info_to_return_to_main_loop["knowledge"] = \
                                                        "10 fighter knowledge gained."
                                                if current_enemy_battling.name == "nede ghoul":
                                                    nede_ghoul_defeated = True
                                                    ghoul_nede.kill()
                                                if current_enemy_battling.name == "chorizon_1":
                                                    mini_boss_1 = False
                                                    mini_boss_1_defeated = True
                                                    chorizon_1.kill()
                                                if current_enemy_battling.name == "chorizon_2":
                                                    mini_boss_2 = False
                                                    mini_boss_2_defeated = True
                                                    chorizon_2.kill()
                                                if current_enemy_battling.name == "muchador":
                                                    muchador_defeated = True
                                                    muchador.kill()
                                                movement_able = True
                                                combat_happened = False
                                                interacted = False
                                                encounter_started = False
                                                in_battle = False
                                                in_over_world = True
                                                loot_updated = False
                                else:
                                    info_text_1 = "Not enough energy to use this skill."

                    # outside of battle event loop ---------------------------------------------------------------------
                    combat_scenario.enemy_health_bar(current_enemy_battling, graphic_dict)
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

                    # battle scene and enemy are drawn to screen -------------------------------------------------------
                    try:
                        if in_battle and not in_over_world and not in_shop \
                                and not in_inn and not in_academia and not in_npc_interaction:
                            if player.current_zone == "seldon":
                                screen.blit(seldon_district_battle, (0, 0))
                            if player.current_zone == "korlok":
                                screen.blit(korlok_district_battle, (0, 0))
                            if player.current_zone == "mines":
                                screen.blit(mines_battle, (0, 0))
                            if player.current_zone == "stardust":
                                screen.blit(stardust_battle, (0, 0))
                            if player.current_zone == "reservoir a" or player.current_zone == "reservoir b":
                                screen.blit(reservoir_battle, (0, 0))
                            if player.current_zone == "terra trail":
                                screen.blit(caves_battle_screen, (0, 0))
                            screen.blit(equipment_screen.surf, equipment_screen.rect)
                            screen.blit(offense_meter.surf, offense_meter.rect)
                            screen.blit(defense_meter.surf, defense_meter.rect)
                            drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan,
                                                          weapon_select)
                            screen.blit(skill_bar.surf, skill_bar.rect)
                            screen.blit(enemy_status_bar_back.surf, enemy_status_bar_back.rect)
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
                            try:
                                screen.blit(current_enemy_battling.health_bar.surf,
                                            current_enemy_battling.health_bar.rect)
                            except TypeError:
                                pass
                            screen.blit(star_power_meter.surf, star_power_meter.rect)

                            if not combat_cooldown:
                                if button_highlighted:
                                    screen.blit(button_highlight.surf, button_highlight.rect)

                            screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                            screen.blit(hp_bar.surf, hp_bar.rect)
                            screen.blit(en_bar.surf, en_bar.rect)
                            screen.blit(xp_bar.surf, xp_bar.rect)
                            screen.blit(enemy_status.surf, enemy_status.rect)
                            text_enemy_name_surf = font.render(str(current_enemy_battling.kind), True, "black",
                                                               (255, 204, 203))
                            text_enemy_name_rect = text_enemy_name_surf.get_rect()
                            text_enemy_name_rect.center = (805, 689)
                            screen.blit(text_enemy_name_surf, text_enemy_name_rect)
                            text_enemy_level_surf = font.render(str(current_enemy_battling.level), True, "black",
                                                                (255, 204, 203))
                            text_enemy_level_rect = text_enemy_level_surf.get_rect()
                            text_enemy_level_rect.center = (915, 689)
                            screen.blit(text_enemy_level_surf, text_enemy_level_rect)

                            if current_enemy_battling.type == "mage":
                                type_advantage_overlay.update(580, 50, graphic_dict["mage_type_overlay"])
                            if current_enemy_battling.type == "fighter":
                                type_advantage_overlay.update(580, 50, graphic_dict["fighter_type_overlay"])
                            if current_enemy_battling.type == "scout":
                                type_advantage_overlay.update(580, 50, graphic_dict["scout_type_overlay"])
                            screen.blit(type_advantage_overlay.surf, type_advantage_overlay.rect)

                            # game guide popups
                            if not battle_guide_shown:
                                game_guide_overlay.update(game_guide_overlay.x_coordinate,
                                                          game_guide_overlay.y_coordinate,
                                                          graphic_dict["guide_basics_battle_img"])
                                game_guide_container.append(game_guide_overlay)
                                battle_guide_shown = True

                            if first_battle_cond:
                                directional_arrow.update(745, 565, graphic_dict["arrow_down"])
                                screen.blit(directional_arrow.surf, directional_arrow.rect)

                    except AttributeError:
                        pass

                    # combat didn't happen this iteration, reset sprites to default surface image
                    if not combat_happened:
                        combat_scenario.resting_animation(player, current_enemy_battling, player_battle_sprite,
                                                          snake_battle_sprite, ghoul_battle_sprite,
                                                          chorizon_battle_sprite, muchador_battle_sprite,
                                                          magmon_battle_sprite, bandile_battle_sprite,
                                                          chinzilla_battle_sprite, barrier_active,
                                                          sharp_sense_active, in_battle, in_npc_interaction,
                                                          graphic_dict)
                        if current_enemy_battling.name == "snake":
                            screen.blit(snake_battle_sprite.surf, snake_battle_sprite.rect)
                        if current_enemy_battling.kind == "ghoul":
                            screen.blit(ghoul_battle_sprite.surf, ghoul_battle_sprite.rect)
                        if current_enemy_battling.kind == "chorizon":
                            screen.blit(chorizon_battle_sprite.surf, chorizon_battle_sprite.rect)
                        if current_enemy_battling.kind == "muchador":
                            screen.blit(muchador_battle_sprite.surf, muchador_battle_sprite.rect)
                        if current_enemy_battling.kind == "magmon":
                            screen.blit(magmon_battle_sprite.surf, magmon_battle_sprite.rect)
                        if current_enemy_battling.kind == "bandile":
                            screen.blit(bandile_battle_sprite.surf, bandile_battle_sprite.rect)
                        if current_enemy_battling.kind == "chinzilla":
                            screen.blit(chinzilla_battle_sprite.surf, chinzilla_battle_sprite.rect)
                        screen.blit(player_battle_sprite.surf, player_battle_sprite.rect)
                        screen.blit(message_box.surf, message_box.rect)
                        # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                        drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2,
                                                         info_text_3, info_text_4, in_over_world)
                        drawing_functions.draw_it(screen)

                        if len(game_guide_container) > 0:
                            for guide_overlay in game_guide_container:
                                screen.blit(guide_overlay.surf, guide_overlay.rect)

                        pygame.display.flip()
                        combat_cooldown = False

                    # combat happened this turn, update sprites for attack and apply short cooldown to attack again
                    if combat_happened:
                        # disengage player when fighting muchador boss after it's health gets low
                        # muchador picks a random crate and hides in it
                        if current_enemy_battling.name == "muchador":
                            if not muchador_relocate:
                                if current_enemy_battling.health < 60:
                                    muchador_crates_list = [muchador_crate_1, muchador_crate_2,
                                                            muchador_crate_3, muchador_crate_4]
                                    info_text_1 = "The muchador attempts to escape!"
                                    info_text_2 = "Maybe it's hiding? "
                                    movement_able = True
                                    combat_happened = False
                                    interacted = False
                                    encounter_started = False
                                    in_battle = False
                                    in_over_world = True
                                    muchador_relocate = True
                                    random_crate = random.choice(muchador_crates_list)
                                    muchador.update_image(random_crate.x_coordinate, random_crate.y_coordinate,
                                                          graphic_dict["muchador"])

                        combat_scenario.combat_animation(player, current_enemy_battling, player_battle_sprite,
                                                         snake_battle_sprite, ghoul_battle_sprite,
                                                         chorizon_battle_sprite, muchador_battle_sprite,
                                                         magmon_battle_sprite, bandile_battle_sprite,
                                                         chinzilla_battle_sprite, barrier_active,
                                                         sharp_sense_active, hard_strike, graphic_dict)
                        if current_enemy_battling.name == "snake":
                            screen.blit(snake_battle_sprite.surf, snake_battle_sprite.rect)
                        if current_enemy_battling.kind == "ghoul":
                            screen.blit(ghoul_battle_sprite.surf, ghoul_battle_sprite.rect)
                        if current_enemy_battling.kind == "chorizon":
                            screen.blit(chorizon_battle_sprite.surf, chorizon_battle_sprite.rect)
                        if current_enemy_battling.kind == "muchador":
                            screen.blit(muchador_battle_sprite.surf, muchador_battle_sprite.rect)
                        if current_enemy_battling.kind == "magmon":
                            screen.blit(magmon_battle_sprite.surf, magmon_battle_sprite.rect)
                        if current_enemy_battling.kind == "bandile":
                            screen.blit(bandile_battle_sprite.surf, bandile_battle_sprite.rect)
                        if current_enemy_battling.kind == "chinzilla":
                            screen.blit(chinzilla_battle_sprite.surf, chinzilla_battle_sprite.rect)
                        screen.blit(player_battle_sprite.surf, player_battle_sprite.rect)
                        screen.blit(message_box.surf, message_box.rect)
                        # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                        drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2,
                                                         info_text_3, info_text_4, in_over_world)
                        drawing_functions.draw_it(screen)

                        # damage overlays, updated depending on if damage was in effective range
                        if combat_events["damage done"] != 0:
                            dealt_damage_overlay.update(850, 225, graphic_dict["dealt_damage_img"])
                            if combat_events["non effective player"]:
                                dealt_damage_overlay.update(850, 225, graphic_dict["non_effective_dealt_damage_img"])
                            if combat_events["effective player"]:
                                dealt_damage_overlay.update(850, 225, graphic_dict["effective_dealt_damage_img"])

                            screen.blit(dealt_damage_overlay.surf, dealt_damage_overlay.rect)
                            damage_done_surf = level_up_font.render(str(combat_events["damage done"]),
                                                                    True, "black", "white")
                            damage_done_rect = damage_done_surf.get_rect()
                            damage_done_rect.center = (850, 225)
                            screen.blit(damage_done_surf, damage_done_rect)

                        if combat_events["damage taken"] != 0:
                            received_damage_overlay.update(125, 275, graphic_dict["received_damage_img"])
                            if combat_events["non effective enemy"]:
                                received_damage_overlay.update(125, 275, graphic_dict["non_effective_dealt_damage_img"])
                            if combat_events["effective enemy"]:
                                received_damage_overlay.update(125, 275, graphic_dict["effective_received_damage_img"])

                            screen.blit(received_damage_overlay.surf, received_damage_overlay.rect)
                            damage_received_surf = level_up_font.render(str(combat_events["damage taken"]),
                                                                        True, "black", "white")
                            damage_received_rect = damage_received_surf.get_rect()
                            damage_received_rect.center = (125, 275)
                            screen.blit(damage_received_surf, damage_received_rect)

                        if len(game_guide_container) > 0:
                            for guide_overlay in game_guide_container:
                                screen.blit(guide_overlay.surf, guide_overlay.rect)

                        pygame.display.flip()
                        combat_cooldown = True
                        # when combat happens, apply a short cooldown so attack button can't be spammed
                        pygame.time.wait(750)
                        # reset combat animation and ability to click without delay on next iteration
                        combat_happened = False
                        # reset hard strike condition so regular fighter attack animation resumes
                        hard_strike = False

                # ------------------------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if player is in shop ---------------------------------------------------------------------------------
                if in_shop and not in_over_world and not in_battle and not in_inn and not in_academia \
                        and not in_npc_interaction:

                    if player.current_zone == "seldon":
                        if not building_song_set:
                            pygame.mixer.music.fadeout(50)
                            pygame.mixer.music.load(seldon_building_music)
                            pygame.mixer.music.play(loops=-1)
                            building_song_set = True

                    if player.current_zone == "korlok":
                        if not building_song_set:
                            pygame.mixer.music.fadeout(50)
                            pygame.mixer.music.load(korlok_building_music)
                            pygame.mixer.music.play(loops=-1)
                            building_song_set = True

                    for event in pygame.event.get():
                        if buy_clicked:
                            if player.current_zone == "stardust":
                                upgrade_event = click_handlers.stardust_upgrade_event(event, offense_select_button,
                                                                                      pygame)
                                # if player is in stardust post and chooses to upgrade +10 offense, consume 4 stars
                                if len(stardust_upgrade_elements) > 0:
                                    if upgrade_event == "offense":
                                        if player.star_power >= 4:
                                            buy_clicked = False
                                            button_highlighted = False
                                            player.offense += 1
                                            player.star_power -= 4
                                            info_text_1 = "You consumed 4 stars,"
                                            info_text_2 = "Upgrading your weapon to level 2."
                                            stardust_upgrade_elements.clear()
                                        else:
                                            info_text_1 = "4 stars are required to upgrade."
                                            info_text_2 = ""

                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                shop_button = ''
                                if len(buy_shop_elements) > 0:
                                    buy_shop_elements.pop(0)
                                    shopkeeper_items.clear()
                                if len(drawing_functions.buy_info_window) > 0:
                                    drawing_functions.buy_info_window.clear()
                                if len(drawing_functions.sell_info_window) > 0:
                                    drawing_functions.sell_info_window.clear()

                                buy_clicked = False
                                movement_able = True
                                interacted = False
                                encounter_started = False
                                in_shop = False
                                in_over_world = True
                                shop_cat_pet = False
                                building_song_set = False
                        elif event.type == QUIT:
                            pygame.mixer.quit()
                            sys.exit()

                        # getting mouse position and highlighting buttons if they collide
                        pos = pygame.mouse.get_pos()
                        button_highlighted = button_highlighter(pos)

                        if event.type == pygame.MOUSEBUTTONUP:
                            gameplay_functions.role_swap(player, pos, graphic_dict, staff, sword, bow, pressed_keys)
                            if game_guide_overlay.rect.collidepoint(pos):
                                game_guide_container.clear()
                            if cat_pet_button_overlay.rect.collidepoint(pos):
                                shop_cat_pet = True

                        shop_button = click_handlers.shop_event_button(event, buy_button, leave_button, pygame)

                        # get which button player pressed during shop scenario (buy or leave)
                        if buy_clicked:
                            # if player clicks yes button to sell item, get current item and buy -------------------
                            buy_choice = click_handlers.shop_buy_button(event, yes_button, pygame)
                            buy_return = shop_scenario.buy_items(player, buy_choice, current_buy_item, Item,
                                                                 graphic_dict["health_pot_img"],
                                                                 graphic_dict["energy_pot_img"],
                                                                 graphic_dict["basic_armor"],
                                                                 graphic_dict["forged_armor"],
                                                                 graphic_dict["mythical_armor"])
                            if buy_return["info 1"] != "":
                                button_highlighted = False
                                info_text_1 = buy_return["info 1"]
                            if buy_return["info 2"] != "":
                                info_text_1 = buy_return["info 2"]
                            item_bought = buy_return["bought"]
                            # draws buy info box for info and confirmation
                            buy_item = click_handlers.buy_event_item(event, shopkeeper_items, pygame)
                            if drawing_functions.buy_info_draw(buy_item, buy_items, yes_button,
                                                               graphic_dict) is not None:
                                current_buy_item = drawing_functions.buy_info_draw(buy_item, buy_items, yes_button,
                                                                                   graphic_dict)
                        if not buy_clicked:
                            if player.current_zone != "stardust":
                                # if player clicks yes button to sell item, get current item and sell ------------------
                                sell_choice = click_handlers.shop_sell_button(event, yes_button, pygame, sell_items)
                                sell_return = shop_scenario.sell_items(player, sell_choice, current_sell_item)
                                if sell_return["info 1"] != "":
                                    button_highlighted = False
                                    info_text_1 = sell_return["info 1"]
                                if sell_return["info 2"] != "":
                                    info_text_1 = sell_return["info 2"]
                                item_sold = sell_return["sold"]
                                # draws sell info box for info and confirmation
                                sell_item = click_handlers.sell_event_item(event, pygame)
                                if drawing_functions.sell_info_draw(sell_item, sell_items, yes_button,
                                                                    graphic_dict) is not None:
                                    current_sell_item = drawing_functions.sell_info_draw(sell_item, sell_items,
                                                                                         yes_button, graphic_dict)

                        if player.current_zone == "stardust":
                            if shop_button == "buy":
                                first_shop_cond = False
                                shop_button = ''
                                # if player hasn't bought an item yet, show message that item can be clicked to buy
                                if not item_bought:
                                    info_text_1 = "Select an upgrade."
                                    info_text_2 = ""
                                    info_text_3 = ""
                                    info_text_4 = ""
                                # if user clicks buy button again, set condition to false which will hide buy window
                                if buy_clicked:
                                    buy_clicked = False
                                    # remove buy window from display and clear temporary list used to populate it
                                    if len(stardust_upgrade_elements) > 0:
                                        stardust_upgrade_elements.clear()
                                # user clicked buy button for the first time. show buy window
                                else:
                                    buy_clicked = True
                                    stardust_upgrade_elements.append(upgrade_overlay)
                                    stardust_upgrade_elements.append(offense_select_button)

                        shop_keys = pygame.key.get_pressed()
                        # outside of shop event loop -------------------------------------------------------------------
                        if player.current_zone != "stardust":
                            # if player has just started shop scenario, clear message box
                            if not encounter_started:
                                info_text_1 = "Click an inventory item to sell it."
                                info_text_2 = "Or, click buy button to buy an item."
                                info_text_3 = ""
                                info_text_4 = ""
                                encounter_started = True
                                # reset items bought condition on new shop encounter so that message is shown to player
                                item_bought = False
                                item_sold = False
                            if shop_button == "buy":
                                first_shop_cond = False
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
                                    if player.current_zone == "seldon":
                                        shop_scenario.shop_keeper_inventory_draw(npc_amuna_shopkeeper, shopkeeper_items,
                                                                                 graphic_dict["health_pot_img"],
                                                                                 graphic_dict["energy_pot_img"],
                                                                                 graphic_dict["basic_armor"],
                                                                                 graphic_dict["forged_armor"],
                                                                                 graphic_dict["mythical_armor"])
                                    if player.current_zone == "korlok":
                                        shop_scenario.shop_keeper_inventory_draw(npc_nuldar_shopkeeper,
                                                                                 shopkeeper_items,
                                                                                 graphic_dict["health_pot_img"],
                                                                                 graphic_dict["energy_pot_img"],
                                                                                 graphic_dict["basic_armor"],
                                                                                 graphic_dict["forged_armor"],
                                                                                 graphic_dict["mythical_armor"])

                        if shop_button == "leave":
                            shop_button = ''
                            if len(buy_shop_elements) > 0:
                                buy_shop_elements.pop(0)
                                shopkeeper_items.clear()
                            if len(drawing_functions.buy_info_window) > 0:
                                drawing_functions.buy_info_window.clear()
                            if len(drawing_functions.sell_info_window) > 0:
                                drawing_functions.sell_info_window.clear()

                            buy_clicked = False
                            movement_able = True
                            interacted = False
                            encounter_started = False
                            in_shop = False
                            in_over_world = True
                            shop_cat_pet = False
                            building_song_set = False

                    # draw objects to screen related to shop scenario --------------------------------------------------
                    if player.current_zone == "seldon" and in_shop and not in_over_world and not in_battle \
                            and not in_inn and not in_academia and not in_npc_interaction:
                        screen.blit(seldon_district_shop, (0, 0))
                        screen.blit(equipment_screen.surf, equipment_screen.rect)
                        screen.blit(offense_meter.surf, offense_meter.rect)
                        screen.blit(defense_meter.surf, defense_meter.rect)
                        drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)
                        screen.blit(buy_button.surf, buy_button.rect)
                        screen.blit(leave_button.surf, leave_button.rect)
                        screen.blit(message_box.surf, message_box.rect)
                        screen.blit(star_power_meter.surf, star_power_meter.rect)
                        # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                        drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3,
                                                         info_text_4, in_over_world)
                        drawing_functions.draw_it(screen)

                        screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        cat_pet_button_overlay.update(505, 235, graphic_dict["cat_pet_button_overlay"])
                        screen.blit(cat_pet_button_overlay.surf, cat_pet_button_overlay.rect)
                        if shop_cat_pet:
                            cat_pet_animation_overlay.update(507, 242, graphic_dict["shop_cat_pet_img"])
                            screen.blit(cat_pet_animation_overlay.surf, cat_pet_animation_overlay.rect)

                        if buy_clicked:
                            for window in buy_shop_elements:
                                screen.blit(window.surf, window.rect)
                            for shop_item in shopkeeper_items:
                                screen.blit(shop_item.surf, shop_item.rect)
                            if len(buy_window) > 0:
                                for element in buy_window:
                                    screen.blit(element.surf, element.rect)
                        if len(sell_window) > 0:
                            for element in sell_window:
                                screen.blit(element.surf, element.rect)

                        if first_shop_cond:
                            directional_arrow.update(855, 620, graphic_dict["arrow_down"])
                            screen.blit(directional_arrow.surf, directional_arrow.rect)

                        if button_highlighted:
                            screen.blit(button_highlight.surf, button_highlight.rect)

                    # draw objects to screen related to shop scenario --------------------------------------------------
                    if player.current_zone == "korlok" and in_shop and not in_over_world and not in_battle \
                            and not in_inn and not in_academia and not in_npc_interaction:
                        screen.blit(korlok_district_shop, (0, 0))
                        screen.blit(equipment_screen.surf, equipment_screen.rect)
                        screen.blit(offense_meter.surf, offense_meter.rect)
                        screen.blit(defense_meter.surf, defense_meter.rect)
                        drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)
                        screen.blit(buy_button.surf, buy_button.rect)
                        screen.blit(leave_button.surf, leave_button.rect)
                        screen.blit(message_box.surf, message_box.rect)
                        screen.blit(star_power_meter.surf, star_power_meter.rect)
                        # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                        drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2,
                                                         info_text_3, info_text_4, in_over_world)
                        drawing_functions.draw_it(screen)

                        screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        cat_pet_button_overlay.update(505, 235, graphic_dict["cat_pet_button_overlay"])
                        screen.blit(cat_pet_button_overlay.surf, cat_pet_button_overlay.rect)
                        if shop_cat_pet:
                            cat_pet_animation_overlay.update(507, 242, graphic_dict["shop_cat_pet_img"])
                            screen.blit(cat_pet_animation_overlay.surf, cat_pet_animation_overlay.rect)

                        if buy_clicked:
                            for window in buy_shop_elements:
                                screen.blit(window.surf, window.rect)
                            for shop_item in shopkeeper_items:
                                screen.blit(shop_item.surf, shop_item.rect)
                            if len(buy_window) > 0:
                                for element in buy_window:
                                    screen.blit(element.surf, element.rect)
                        if len(sell_window) > 0:
                            for element in sell_window:
                                screen.blit(element.surf, element.rect)

                        if first_shop_cond:
                            directional_arrow.update(855, 620, graphic_dict["arrow_down"])
                            screen.blit(directional_arrow.surf, directional_arrow.rect)

                        if button_highlighted:
                            screen.blit(button_highlight.surf, button_highlight.rect)

                    # draw objects to screen related to shop scenario --------------------------------------------------
                    if player.current_zone == "stardust" and in_shop and not in_over_world and not in_battle \
                            and not in_inn and not in_academia and not in_npc_interaction:
                        screen.blit(stardust_post_bg, (0, 0))
                        screen.blit(equipment_screen.surf, equipment_screen.rect)
                        screen.blit(offense_meter.surf, offense_meter.rect)
                        screen.blit(defense_meter.surf, defense_meter.rect)
                        drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)
                        screen.blit(upgrade_button.surf, upgrade_button.rect)
                        screen.blit(leave_button.surf, leave_button.rect)
                        screen.blit(message_box.surf, message_box.rect)
                        screen.blit(star_power_meter.surf, star_power_meter.rect)
                        # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                        drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3,
                                                         info_text_4, in_over_world)
                        drawing_functions.draw_it(screen)

                        screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)

                        if buy_clicked:
                            for element in stardust_upgrade_elements:
                                screen.blit(element.surf, element.rect)

                        # stardust outpost stars on the wall representing player progress in each zone
                        if player.quest_complete["sneaky snakes"]:
                            stardust_star_overlay.update(236, 185, graphic_dict["stardust_star_01"])
                            screen.blit(stardust_star_overlay.surf, stardust_star_overlay.rect)
                        if player.quest_complete["village repairs"]:
                            stardust_star_overlay.update(236, 185, graphic_dict["stardust_star_02"])
                            screen.blit(stardust_star_overlay.surf, stardust_star_overlay.rect)
                        if player.quest_complete["where's nede?"]:
                            stardust_star_overlay.update(236, 185, graphic_dict["stardust_star_03"])
                            screen.blit(stardust_star_overlay.surf, stardust_star_overlay.rect)
                        if player.quest_complete["ghouled again"]:
                            stardust_star_overlay.update(236, 185, graphic_dict["stardust_star_04"])
                            screen.blit(stardust_star_overlay.surf, stardust_star_overlay.rect)

                        if player.quest_complete["band hammer"]:
                            stardust_star_overlay_korlok.update(236, 295, graphic_dict["stardust_star_01_korlok"])
                            screen.blit(stardust_star_overlay_korlok.surf, stardust_star_overlay_korlok.rect)
                        if player.quest_complete["can't apothecary it"]:
                            stardust_star_overlay_korlok.update(236, 295, graphic_dict["stardust_star_02_korlok"])
                            screen.blit(stardust_star_overlay_korlok.surf, stardust_star_overlay_korlok.rect)
                        if player.quest_complete["elementary elementals"]:
                            stardust_star_overlay_korlok.update(236, 295, graphic_dict["stardust_star_03_korlok"])
                            screen.blit(stardust_star_overlay_korlok.surf, stardust_star_overlay_korlok.rect)
                        if player.quest_complete["it's dangerous to go alone"]:
                            stardust_star_overlay_korlok.update(236, 295, graphic_dict["stardust_star_04_korlok"])
                            screen.blit(stardust_star_overlay_korlok.surf, stardust_star_overlay_korlok.rect)

                        if len(game_guide_container) > 0:
                            for guide_overlay in game_guide_container:
                                screen.blit(guide_overlay.surf, guide_overlay.rect)

                        if first_shop_cond:
                            directional_arrow.update(855, 620, graphic_dict["arrow_down"])
                            screen.blit(directional_arrow.surf, directional_arrow.rect)

                        if button_highlighted:
                            screen.blit(button_highlight.surf, button_highlight.rect)

                # ------------------------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if player is in inn ----------------------------------------------------------------------------------
                if in_inn and not in_over_world and not in_shop and not in_battle and not in_academia \
                        and not in_npc_interaction:

                    if player.current_zone == "seldon":
                        if not building_song_set:
                            pygame.mixer.music.fadeout(50)
                            pygame.mixer.music.load(seldon_building_music)
                            pygame.mixer.music.play(loops=-1)
                            building_song_set = True

                    if player.current_zone == "korlok":
                        if not building_song_set:
                            pygame.mixer.music.fadeout(50)
                            pygame.mixer.music.load(korlok_building_music)
                            pygame.mixer.music.play(loops=-1)
                            building_song_set = True

                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                inn_button = ''
                                rest_clicked = False
                                movement_able = True
                                interacted = False
                                encounter_started = False
                                in_inn = False
                                in_over_world = True
                                rested = False
                                faded_inn_screen = False
                                building_song_set = False
                        elif event.type == QUIT:
                            pygame.mixer.quit()
                            sys.exit()

                        # getting mouse position and highlighting buttons if they collide
                        pos = pygame.mouse.get_pos()
                        button_highlighted = button_highlighter(pos)

                        gameplay_functions.role_swap(player, pos, graphic_dict, staff, sword, bow, pressed_keys)

                        # get which button player pressed during inn scenario (rest or leave)
                        inn_button = click_handlers.inn_event_button(event, rest_button, leave_button, pygame)

                        # click handlers
                        info_choice = click_handlers.item_info_button(event, item_info_button, pygame, info_items)
                        if info_choice == "yes":
                            inventory_event = click_handlers.inventory(player, current_info_item)
                            if inventory_event["item message"] != "":
                                info_text_1 = inventory_event["item message"]
                                info_text_2 = ""
                            drawing_functions.item_info_window.clear()
                        if info_choice == "no":
                            drawing_functions.item_info_window.clear()
                        inventory_item_clicked = click_handlers.inventory_event_item(event, pygame)
                        if inventory_item_clicked["clicked"]:
                            current_info_item = drawing_functions.item_info_draw(inventory_item_clicked["element"],
                                                                                 info_items, item_info_button,
                                                                                 graphic_dict)
                        # function to handle equipment item clicks. apply item message to message box if not empty str.
                        if len(drawing_functions.item_info_window) == 0:
                            equipment_event = click_handlers.equipment(player, event, pygame, basic_armor, forged_armor,
                                                                       mythical_armor, legendary_armor, power_gloves)
                            if equipment_event["equipment message"] != "":
                                info_text_1 = equipment_event["equipment message"]
                                info_text_2 = ""

                        if inn_button == "rest":
                            first_inn_cond = False
                            # if player has not yet rested this instance
                            if not rested:
                                rest_clicked = True
                                info_text_1 = "You feel well rested."
                                info_text_2 = "Your health is restored."
                                info_text_3 = "Your energy is restored."
                                info_text_4 = ""
                            # if player has already rested this instance
                            else:
                                info_text_1 = "You've already rested."
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""

                        if inn_button == "leave":
                            inn_button = ''
                            rest_clicked = False
                            movement_able = True
                            interacted = False
                            encounter_started = False
                            in_inn = False
                            in_over_world = True
                            rested = False
                            faded_inn_screen = False
                            building_song_set = False

                    # outside of inn event loop ------------------------------------------------------------------------
                    # if player has just started inn scenario, clear message box
                    if not encounter_started:
                        info_text_1 = "Click rest button to sleep."
                        info_text_2 = "Sleep regains health and energy."
                        info_text_3 = ""
                        info_text_4 = ""
                        encounter_started = True

                    # draw objects to screen related to inn scenario ---------------------------------------------------
                    if in_inn and not in_over_world and not in_shop and not \
                            in_battle and not in_academia and not in_npc_interaction:

                        if player.current_zone == "seldon":
                            # if player has just rested, fade inn screen back in with alpha value loop
                            if rested:
                                if not faded_inn_screen:
                                    for alpha in range(0, 50):
                                        seldon_district_inn.set_alpha(alpha)
                                        screen.blit(seldon_district_inn, (0, 0))
                                        screen.blit(equipment_screen.surf, equipment_screen.rect)
                                        pygame.display.flip()
                                    faded_inn_screen = True
                                else:
                                    seldon_district_inn.set_alpha(255)
                                    screen.blit(seldon_district_inn, (0, 0))
                                    screen.blit(equipment_screen.surf, equipment_screen.rect)
                            if not rested:
                                seldon_district_inn.set_alpha(255)
                                screen.blit(seldon_district_inn, (0, 0))
                                screen.blit(equipment_screen.surf, equipment_screen.rect)

                        if player.current_zone == "korlok":
                            # if player has just rested, fade inn screen back in with alpha value loop
                            if rested:
                                if not faded_inn_screen:
                                    for alpha in range(0, 50):
                                        korlok_district_inn.set_alpha(alpha)
                                        screen.blit(korlok_district_inn, (0, 0))
                                        screen.blit(equipment_screen.surf, equipment_screen.rect)
                                        pygame.display.flip()
                                    faded_inn_screen = True
                                else:
                                    korlok_district_inn.set_alpha(255)
                                    screen.blit(korlok_district_inn, (0, 0))
                                    screen.blit(equipment_screen.surf, equipment_screen.rect)
                            if not rested:
                                korlok_district_inn.set_alpha(255)
                                screen.blit(korlok_district_inn, (0, 0))
                                screen.blit(equipment_screen.surf, equipment_screen.rect)

                    screen.blit(rest_button.surf, rest_button.rect)
                    screen.blit(leave_button.surf, leave_button.rect)
                    screen.blit(star_power_meter.surf, star_power_meter.rect)
                    screen.blit(message_box.surf, message_box.rect)
                    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3,
                                                     info_text_4, in_over_world)
                    drawing_functions.draw_it(screen)
                    if button_highlighted:
                        screen.blit(button_highlight.surf, button_highlight.rect)
                    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                    screen.blit(hp_bar.surf, hp_bar.rect)
                    screen.blit(en_bar.surf, en_bar.rect)
                    screen.blit(xp_bar.surf, xp_bar.rect)

                    if rest_clicked:
                        if not rested:
                            # set sleep screen to fade in with alpha value loop. flip each iteration to show
                            for alpha in range(0, 255):
                                nera_sleep_screen.set_alpha(alpha)
                                screen.blit(nera_sleep_screen, (0, 0))
                                pygame.display.flip()
                            player.health = 100
                            player.energy = 100
                            rested = True

                    if first_inn_cond:
                        directional_arrow.update(855, 620, graphic_dict["arrow_down"])
                        screen.blit(directional_arrow.surf, directional_arrow.rect)

                # ------------------------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if player is in academia -----------------------------------------------------------------------------
                if in_academia and not in_over_world and not in_shop and not in_inn and not in_npc_interaction \
                        and not in_battle:

                    if not building_song_set:
                        pygame.mixer.music.fadeout(50)
                        pygame.mixer.music.load(seldon_building_music)
                        pygame.mixer.music.play(loops=-1)
                        building_song_set = True

                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                book_appended = False
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
                                academia_cat_pet = False
                                building_song_set = False
                                books.clear()
                                skill_learn_items.clear()
                        elif event.type == QUIT:
                            pygame.mixer.quit()
                            sys.exit()

                        # getting mouse position and highlighting buttons if they collide
                        pos = pygame.mouse.get_pos()
                        # highlighting books once moused over
                        if not mage_learn_clicked and not fighter_learn_clicked and not scout_learn_clicked:
                            if mage_learn_button.rect.collidepoint(pos):
                                button_highlight.update(mage_learn_button.x_coordinate - 7,
                                                        mage_learn_button.y_coordinate + 12,
                                                        graphic_dict["skill high"])
                                button_highlighted = True
                            elif fighter_learn_button.rect.collidepoint(pos):
                                button_highlight.update(fighter_learn_button.x_coordinate - 1,
                                                        fighter_learn_button.y_coordinate + 12,
                                                        graphic_dict["skill high"])
                                button_highlighted = True
                            elif scout_learn_button.rect.collidepoint(pos):
                                button_highlight.update(scout_learn_button.x_coordinate - 2,
                                                        scout_learn_button.y_coordinate + 12,
                                                        graphic_dict["skill high"])
                                button_highlighted = True
                            elif leave_button.rect.collidepoint(pos):
                                button_highlight.update(leave_button.x_coordinate, leave_button.y_coordinate + 7,
                                                        graphic_dict["main high"])
                                button_highlighted = True
                            else:
                                button_highlighted = False
                        # highlighting skill learn buttons inside of books once moused over
                        else:
                            if barrier_learn_button.rect.collidepoint(pos):
                                button_highlight.update(barrier_learn_button.x_coordinate + 2,
                                                        barrier_learn_button.y_coordinate + 3,
                                                        graphic_dict["book_high"])
                                button_highlighted = True
                            elif close_button.rect.collidepoint(pos):
                                button_highlight.update(close_button.x_coordinate - 3, close_button.y_coordinate + 3,
                                                        graphic_dict["close high"])
                                button_highlighted = True
                            elif leave_button.rect.collidepoint(pos):
                                button_highlight.update(leave_button.x_coordinate, leave_button.y_coordinate + 7,
                                                        graphic_dict["main high"])
                                button_highlighted = True
                            else:
                                button_highlighted = False

                        if event.type == pygame.MOUSEBUTTONUP:
                            gameplay_functions.role_swap(player, pos, graphic_dict, staff, sword, bow, pressed_keys)
                            if cat_pet_button_overlay.rect.collidepoint(pos):
                                academia_cat_pet = True
                        # get which button player pressed during academia scenario (learn or leave)
                        academia_button = click_handlers.academia_event_button(event, mage_learn_button,
                                                                               fighter_learn_button, scout_learn_button,
                                                                               leave_button, pygame)
                        # click handlers
                        info_choice = click_handlers.item_info_button(event, item_info_button, pygame, info_items)
                        if info_choice == "yes":
                            inventory_event = click_handlers.inventory(player, current_info_item)
                            if inventory_event["item message"] != "":
                                info_text_1 = inventory_event["item message"]
                                info_text_2 = ""
                            drawing_functions.item_info_window.clear()
                        if info_choice == "no":
                            drawing_functions.item_info_window.clear()
                        inventory_item_clicked = click_handlers.inventory_event_item(event, pygame)
                        if inventory_item_clicked["clicked"]:
                            current_info_item = drawing_functions.item_info_draw(inventory_item_clicked["element"],
                                                                                 info_items, item_info_button,
                                                                                 graphic_dict)
                        # function to handle equipment item clicks. apply item message to message box if not empty str.
                        if len(drawing_functions.item_info_window) == 0:
                            equipment_event = click_handlers.equipment(player, event, pygame, basic_armor, forged_armor,
                                                                       mythical_armor, legendary_armor, power_gloves)
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
                                            button_highlighted = False
                                            mage_learn_clicked = False
                                            book_appended = False
                                            books.clear()
                                            skill_learn_items.clear()
                                        else:
                                            info_text_1 = "50 mage knowledge required to learn."
                                    else:
                                        info_text_1 = "You've already learned 'Barrier'."
                                        info_text_2 = ""
                                if book_button.name == "close button":
                                    mage_learn_clicked = False
                                    book_appended = False
                                    button_highlighted = False
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
                                            fighter_learn_clicked = False
                                            book_appended = False
                                            button_highlighted = False
                                            books.clear()
                                            skill_learn_items.clear()
                                        else:
                                            info_text_1 = "50 fighter knowledge required to learn."
                                    else:
                                        info_text_1 = "You've already learned 'Hard Strike'."
                                        info_text_2 = ""
                                if book_button.name == "close button":
                                    fighter_learn_clicked = False
                                    book_appended = False
                                    button_highlighted = False
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
                                            button_highlighted = False
                                            scout_learn_clicked = False
                                            book_appended = False
                                            books.clear()
                                            skill_learn_items.clear()
                                        else:
                                            info_text_1 = "50 scout knowledge required to learn."
                                    else:
                                        info_text_1 = "You've already learned 'Sharp Sense'."
                                        info_text_2 = ""
                                if book_button.name == "close button":
                                    scout_learn_clicked = False
                                    book_appended = False
                                    button_highlighted = False
                                    books.clear()
                                    skill_learn_items.clear()
                            except AttributeError:
                                pass

                        if len(skill_learn_items) == 0 and len(books) == 0:
                            if academia_button == "mage learn":
                                mage_learn_clicked = True
                                button_highlighted = False
                                first_academy_cond = False
                            if academia_button == "fighter learn":
                                fighter_learn_clicked = True
                                button_highlighted = False
                                first_academy_cond = False
                            if academia_button == "scout learn":
                                scout_learn_clicked = True
                                button_highlighted = False
                                first_academy_cond = False

                        if academia_button == "leave":
                            book_appended = False
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
                            academia_cat_pet = False
                            building_song_set = False
                            books.clear()
                            skill_learn_items.clear()

                    # outside of inn event loop ------------------------------------------------------------------------
                    if not encounter_started:
                        info_text_1 = "Click a book to view skills."
                        info_text_2 = "Then, click a skill to learn it."
                        info_text_3 = ""
                        info_text_4 = ""
                        encounter_started = True

                    # draw objects to screen related to academia scenario ----------------------------------------------
                    if in_academia and not in_over_world and not in_shop and not in_inn and not in_npc_interaction \
                            and not in_battle:

                        screen.blit(seldon_district_academia, (0, 0))
                        screen.blit(equipment_screen.surf, equipment_screen.rect)
                        screen.blit(offense_meter.surf, offense_meter.rect)
                        screen.blit(defense_meter.surf, defense_meter.rect)
                        drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)
                        screen.blit(mage_learn_button.surf, mage_learn_button.rect)
                        screen.blit(fighter_learn_button.surf, fighter_learn_button.rect)
                        screen.blit(scout_learn_button.surf, scout_learn_button.rect)
                        screen.blit(leave_button.surf, leave_button.rect)
                        screen.blit(message_box.surf, message_box.rect)
                        screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(star_power_meter.surf, star_power_meter.rect)
                        cat_pet_button_overlay.update(125, 500, graphic_dict["cat_pet_button_overlay"])
                        screen.blit(cat_pet_button_overlay.surf, cat_pet_button_overlay.rect)
                        if academia_cat_pet:
                            cat_pet_animation_overlay.update(130, 500, graphic_dict["academia_cat_pet_img"])
                            screen.blit(cat_pet_animation_overlay.surf, cat_pet_animation_overlay.rect)
                        # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                        drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3,
                                                         info_text_4, in_over_world)
                        drawing_functions.draw_it(screen)

                        if len(books) > 0:
                            for book in books:
                                screen.blit(book.surf, book.rect)
                        if len(skill_learn_items) > 0:
                            for skill_item in skill_learn_items:
                                screen.blit(skill_item.surf, skill_item.rect)
                        if button_highlighted:
                            screen.blit(button_highlight.surf, button_highlight.rect)

                        screen.blit(knowledge_window.surf, knowledge_window.rect)
                        text_mage_knowledge_surf = font.render(str(player.knowledge["mage"]), True, "black",
                                                               "light yellow")
                        text_mage_knowledge_rect = text_mage_knowledge_surf.get_rect()
                        text_mage_knowledge_rect.center = (515, 680)
                        screen.blit(text_mage_knowledge_surf, text_mage_knowledge_rect)
                        text_fighter_know_surf = font.render(str(player.knowledge["fighter"]), True, "black",
                                                             "light yellow")
                        text_fighter_know_rect = text_fighter_know_surf.get_rect()
                        text_fighter_know_rect.center = (695, 680)
                        screen.blit(text_fighter_know_surf, text_fighter_know_rect)
                        text_scout_knowledge_surf = font.render(str(player.knowledge["scout"]), True, "black",
                                                                "light yellow")
                        text_scout_knowledge_rect = text_scout_knowledge_surf.get_rect()
                        text_scout_knowledge_rect.center = (865, 680)
                        screen.blit(text_scout_knowledge_surf, text_scout_knowledge_rect)

                        if not book_appended:
                            if mage_learn_clicked and fighter_learn_clicked is False and scout_learn_clicked is False:
                                books.append(mage_book)
                                skill_learn_items.append(barrier_learn_button)
                                skill_learn_items.append(close_button)
                                book_appended = True
                            if fighter_learn_clicked and mage_learn_clicked is False and scout_learn_clicked is False:
                                books.append(fighter_book)
                                skill_learn_items.append(hard_strike_learn_button)
                                skill_learn_items.append(close_button)
                                book_appended = True
                            if scout_learn_clicked and fighter_learn_clicked is False and mage_learn_clicked is False:
                                books.append(scout_book)
                                skill_learn_items.append(sharp_sense_learn_button)
                                skill_learn_items.append(close_button)
                                book_appended = True

                        # the first time player enters academy, show an arrow pointing to their book button
                        if first_academy_cond:
                            if player.role == "mage":
                                directional_arrow.update(753, 195, graphic_dict["arrow_down"])
                                screen.blit(directional_arrow.surf, directional_arrow.rect)
                            if player.role == "fighter":
                                directional_arrow.update(298, 280, graphic_dict["arrow_down"])
                                screen.blit(directional_arrow.surf, directional_arrow.rect)
                            if player.role == "scout":
                                directional_arrow.update(555, 360, graphic_dict["arrow_down"])
                                screen.blit(directional_arrow.surf, directional_arrow.rect)

                # ------------------------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if player is in apothecary ---------------------------------------------------------------------------
                if in_apothecary and not in_over_world and not in_shop and not in_inn and not in_npc_interaction \
                        and not in_battle:

                    if not building_song_set:
                        pygame.mixer.music.fadeout(50)
                        pygame.mixer.music.load(korlok_building_music)
                        pygame.mixer.music.play(loops=-1)
                        building_song_set = True

                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                npc_button = ''
                                movement_able = True
                                interacted = False
                                encounter_started = False
                                in_apothecary = False
                                in_over_world = True
                                building_song_set = False
                                quest_clicked = False
                                drawing_functions.quest_complete_box.clear()
                                drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                                 maurelle_quest_window, celeste_quest_window,
                                                                 torune_quest_window, voruke_quest_window,
                                                                 zerah_quest_window, kirean_quest_window,
                                                                 dionte_quest_window, accept_button, decline_button)
                        elif event.type == QUIT:
                            pygame.mixer.quit()
                            sys.exit()

                        pos = pygame.mouse.get_pos()
                        button_highlighted = button_highlighter(pos)

                        if event.type == pygame.MOUSEBUTTONUP:
                            gameplay_functions.role_swap(player, pos, graphic_dict, staff, sword, bow, pressed_keys)
                            if kirean_complete_quest_window.rect.collidepoint(pos):
                                drawing_functions.quest_complete_box.clear()

                        # npc was interacted with, if quest button clicked get npc name and check quest progress
                        npc_button = click_handlers.npc_event_button(event, quest_button, leave_button, pygame)
                        # in quest window pop-up, if accept or decline buttons are clicked
                        quest_buttons = click_handlers.quest_event_button(event, accept_button, decline_button, pygame)

                        # click handlers
                        info_choice = click_handlers.item_info_button(event, item_info_button, pygame, info_items)
                        if info_choice == "yes":
                            inventory_event = click_handlers.inventory(player, current_info_item)
                            if inventory_event["item message"] != "":
                                info_text_1 = inventory_event["item message"]
                                info_text_2 = ""
                            drawing_functions.item_info_window.clear()
                        if info_choice == "no":
                            drawing_functions.item_info_window.clear()
                        inventory_item_clicked = click_handlers.inventory_event_item(event, pygame)
                        if inventory_item_clicked["clicked"]:
                            current_info_item = drawing_functions.item_info_draw(
                                inventory_item_clicked["element"],
                                info_items, item_info_button,
                                graphic_dict)
                        # function to handle equipment item clicks. apply item message to message box if not empty str.
                        if len(drawing_functions.item_info_window) == 0:
                            equipment_event = click_handlers.equipment(player, event, pygame, basic_armor, forged_armor,
                                                                       mythical_armor, legendary_armor, power_gloves)
                            if equipment_event["equipment message"] != "":
                                info_text_1 = equipment_event["equipment message"]
                                info_text_2 = ""

                        if npc_button == "quest":
                            if player.quest_progress["can't apothecary it"] == 4 and not \
                                    player.quest_complete["can't apothecary it"]:
                                if len(player.items) < 16:
                                    player.quest_complete["can't apothecary it"] = True
                                    player.current_quests["can't apothecary it"] = "You completed this quest!"
                                    info_text_1 = "You've completed Kirean's quest!"
                                    info_text_2 = "Your game has been saved. "
                                    info_text_3 = ""
                                    info_text_4 = ""
                                    player.star_power += 1
                                    player.experience += 50
                                    apothecary_access = True
                                    if player.experience >= 100:
                                        gameplay_functions.level_up(player, level_up_win, level_up_font)
                                        leveled = True
                                        loot_level_tic = time.perf_counter()
                                    player.reputation["sorae"] += 10
                                    # autosave on quest complete
                                    try:
                                        gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                                     sharp_sense_learned, saved, npc_garan.gift,
                                                                     rest_recover_show, knowledge_academia_show,
                                                                     quest_guide_shown, battle_guide_shown,
                                                                     rest_shown_before, quest_highlight_popup,
                                                                     bridge_not_repaired, nede_ghoul_defeated,
                                                                     bridge_cutscenes_not_viewed, crate_1, crate_2,
                                                                     crate_3, crate_4, crate_5, switch_1, switch_2,
                                                                     switch_3, muchador_defeated, has_key,
                                                                     mini_boss_1_defeated, mini_boss_2_defeated,
                                                                     gloves_obtained, korlok_attuned, eldream_attuned)
                                    except PermissionError:
                                        pass

                            if not quest_clicked:
                                if not player.quest_complete["can't apothecary it"]:
                                    drawing_functions.quest_box_draw("kirean", True, garan_quest_window,
                                                                     maurelle_quest_window, celeste_quest_window,
                                                                     torune_quest_window, voruke_quest_window,
                                                                     zerah_quest_window, kirean_quest_window,
                                                                     dionte_quest_window, accept_button, decline_button)
                                    quest_clicked = True
                                else:  # quest complete popup
                                    if not kirean_complete_shown:
                                        drawing_functions.quest_complete_draw("kirean", True,
                                                                              garan_complete_quest_window,
                                                                              maurelle_complete_quest_window,
                                                                              celeste_complete_quest_window,
                                                                              torune_complete_quest_window,
                                                                              voruke_complete_quest_window,
                                                                              zerah_complete_quest_window,
                                                                              kirean_complete_quest_window,
                                                                              dionte_complete_quest_window)
                                        kirean_complete_shown = True
                                        quest_clicked = True
                            else:
                                drawing_functions.quest_box_draw("kirean", False, garan_quest_window,
                                                                 maurelle_quest_window, celeste_quest_window,
                                                                 torune_quest_window, voruke_quest_window,
                                                                 zerah_quest_window, kirean_quest_window,
                                                                 dionte_quest_window, accept_button, decline_button)
                                quest_clicked = False

                        # options once quest window is open ------------------------------------------------------------
                        if quest_buttons == "accept":
                            info_text_1 = "You've accepted the quest!"
                            button_highlighted = False
                            player.quest_status["can't apothecary it"] = True
                            player.current_quests["can't apothecary it"] = "Kirean asked you to gather ore."
                            quest_clicked = False
                            drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                             maurelle_quest_window, celeste_quest_window,
                                                             torune_quest_window, voruke_quest_window,
                                                             zerah_quest_window, kirean_quest_window,
                                                             dionte_quest_window, accept_button, decline_button)

                        # if player chooses to decline, just close the quest window
                        if quest_buttons == "decline":
                            info_text_1 = ""
                            quest_clicked = False
                            button_highlighted = False
                            drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                             maurelle_quest_window, celeste_quest_window,
                                                             torune_quest_window, voruke_quest_window,
                                                             zerah_quest_window, kirean_quest_window,
                                                             dionte_quest_window, accept_button, decline_button)
                        if npc_button == "leave":
                            movement_able = True
                            interacted = False
                            encounter_started = False
                            in_apothecary = False
                            in_over_world = True
                            building_song_set = False

                    # outside of inn event loop ------------------------------------------------------------------------
                    if not encounter_started:
                        info_text_1 = ""
                        info_text_2 = ""
                        info_text_3 = ""
                        info_text_4 = ""
                        encounter_started = True

                    # draw objects to screen related to academia scenario ----------------------------------------------
                    if in_apothecary and not in_over_world and not in_shop and not in_inn and not in_npc_interaction \
                            and not in_battle:

                        screen.blit(korlok_district_apothecary, (0, 0))
                        screen.blit(equipment_screen.surf, equipment_screen.rect)
                        screen.blit(offense_meter.surf, offense_meter.rect)
                        screen.blit(defense_meter.surf, defense_meter.rect)
                        drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)
                        screen.blit(leave_button.surf, leave_button.rect)
                        screen.blit(message_box.surf, message_box.rect)
                        screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(quest_button.surf, quest_button.rect)
                        screen.blit(star_power_meter.surf, star_power_meter.rect)
                        if not player.quest_complete["can't apothecary it"]:
                            if not player.quest_status["can't apothecary it"]:
                                screen.blit(quest_star_apothecary.surf, quest_star_apothecary.rect)
                            if player.quest_status["can't apothecary it"]:
                                quest_star_apothecary.update(quest_star_apothecary.x_coordinate,
                                                             quest_star_apothecary.y_coordinate,
                                                             graphic_dict["building_npc_star_progress"])
                                screen.blit(quest_star_apothecary.surf, quest_star_apothecary.rect)
                            if player.quest_progress["can't apothecary it"] == 4:
                                quest_star_apothecary.update(quest_star_apothecary.x_coordinate,
                                                             quest_star_apothecary.y_coordinate,
                                                             graphic_dict["building_npc_star_complete"])
                                screen.blit(quest_star_apothecary.surf, quest_star_apothecary.rect)
                        # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                        drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3,
                                                         info_text_4, in_over_world)
                        drawing_functions.draw_it(screen)

                        if button_highlighted:
                            screen.blit(button_highlight.surf, button_highlight.rect)

                # ------------------------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # if player interacting with an npc (quest) ------------------------------------------------------------
                if in_npc_interaction and not in_over_world and not in_shop and not in_inn and not in_academia \
                        and not in_battle:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                npc_button = ''
                                movement_able = True
                                interacted = False
                                encounter_started = False
                                in_npc_interaction = False
                                in_over_world = True
                                quest_clicked = False
                                drawing_functions.quest_complete_box.clear()
                                drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                                 maurelle_quest_window, celeste_quest_window,
                                                                 torune_quest_window, voruke_quest_window,
                                                                 zerah_quest_window, kirean_quest_window,
                                                                 dionte_quest_window, accept_button, decline_button)
                                drawing_functions.type_advantage_window.clear()
                        elif event.type == QUIT:
                            pygame.mixer.quit()
                            sys.exit()

                        pos = pygame.mouse.get_pos()
                        button_highlighted = button_highlighter(pos)

                        if event.type == pygame.MOUSEBUTTONUP:
                            gameplay_functions.role_swap(player, pos, graphic_dict, staff, sword, bow, pressed_keys)
                            if garan_complete_quest_window.rect.collidepoint(pos):
                                drawing_functions.quest_complete_box.clear()
                            if maurelle_complete_quest_window.rect.collidepoint(pos):
                                drawing_functions.quest_complete_box.clear()
                            if celeste_complete_quest_window.rect.collidepoint(pos):
                                drawing_functions.quest_complete_box.clear()
                            if torune_complete_quest_window.rect.collidepoint(pos):
                                drawing_functions.quest_complete_box.clear()
                            if voruke_complete_quest_window.rect.collidepoint(pos):
                                drawing_functions.quest_complete_box.clear()
                            if zerah_complete_quest_window.rect.collidepoint(pos):
                                drawing_functions.quest_complete_box.clear()
                            if dionte_complete_quest_window.rect.collidepoint(pos):
                                drawing_functions.quest_complete_box.clear()
                            if level_up_win.rect.collidepoint(pos):
                                drawing_functions.level_up_draw(level_up_win, player, font, False)
                            if role_select_overlay.rect.collidepoint(pos):
                                drawing_functions.type_advantage_window.clear()

                        # npc was interacted with, if quest button clicked get npc name and check quest progress
                        npc_button = click_handlers.npc_event_button(event, quest_button, leave_button, pygame)
                        # in quest window pop-up, if accept or decline buttons are clicked
                        quest_buttons = click_handlers.quest_event_button(event, accept_button, decline_button, pygame)
                        # options once quest window is open ------------------------------------------------------------
                        if quest_buttons == "accept":
                            info_text_1 = "You've accepted the quest!"
                            button_highlighted = False
                            if current_npc_interacting.name == "garan":
                                player.quest_status["sneaky snakes"] = True
                                player.current_quests["sneaky snakes"] = \
                                    "Garan asked you to defeat snakes near the river."
                                if not npc_garan.gift:
                                    npc_garan.gift = True
                                    drawing_functions.type_advantage_window.append(role_select_overlay)
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
                            if current_npc_interacting.name == "voruke":
                                player.quest_status["band hammer"] = True
                                player.current_quests["band hammer"] = "Voruke asked you to defeat bandiles in the " \
                                                                       "mines. "
                            if current_npc_interacting.name == "zerah":
                                player.quest_status["elementary elementals"] = True
                                player.current_quests["elementary elementals"] = "Zerah asked you to defeat magmons" \
                                                                                 " near the lava pool. "
                            if current_npc_interacting.name == "dionte":
                                player.quest_status["it's dangerous to go alone"] = True
                                player.current_quests["it's dangerous to go alone"] = "Dionte asked you to face the" \
                                        " monster in the cave."
                            quest_clicked = False
                            drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                             maurelle_quest_window, celeste_quest_window,
                                                             torune_quest_window, voruke_quest_window,
                                                             zerah_quest_window, kirean_quest_window,
                                                             dionte_quest_window, accept_button, decline_button)
                        # if player chooses to decline, just close the quest window
                        if quest_buttons == "decline":
                            info_text_1 = ""
                            quest_clicked = False
                            button_highlighted = False
                            drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                             maurelle_quest_window, celeste_quest_window,
                                                             torune_quest_window, voruke_quest_window,
                                                             zerah_quest_window, kirean_quest_window,
                                                             dionte_quest_window, accept_button, decline_button)

                        # click handlers
                        info_choice = click_handlers.item_info_button(event, item_info_button, pygame, info_items)
                        if info_choice == "yes":
                            inventory_event = click_handlers.inventory(player, current_info_item)
                            if inventory_event["item message"] != "":
                                info_text_1 = inventory_event["item message"]
                                info_text_2 = ""
                            drawing_functions.item_info_window.clear()
                            button_highlighted = False
                        if info_choice == "no":
                            drawing_functions.item_info_window.clear()
                            button_highlighted = False
                        inventory_item_clicked = click_handlers.inventory_event_item(event, pygame)
                        if inventory_item_clicked["clicked"]:
                            current_info_item = drawing_functions.item_info_draw(inventory_item_clicked["element"],
                                                                                 info_items, item_info_button,
                                                                                 graphic_dict)
                        # function to handle equipment item clicks. apply item message to message box if not empty str.
                        if len(drawing_functions.item_info_window) == 0:
                            equipment_event = click_handlers.equipment(player, event, pygame, basic_armor, forged_armor,
                                                                       mythical_armor, legendary_armor, power_gloves)
                            if equipment_event["equipment message"] != "":
                                button_highlighted = False
                                info_text_1 = equipment_event["equipment message"]
                                info_text_2 = ""

                        if npc_button == "quest":
                            if first_npc_cond:
                                first_npc_cond = False
                            # garan npc, check player's quest progress and reward if completed -------------------------
                            if current_npc_interacting.name == "garan":
                                if player.quest_progress["sneaky snakes"] == 4 and not \
                                        player.quest_complete["sneaky snakes"]:
                                    if len(player.items) < 16:
                                        player.quest_complete["sneaky snakes"] = True
                                        player.current_quests["sneaky snakes"] = "You completed this quest!"
                                        info_text_1 = "You've completed Garan's quest!"
                                        info_text_2 = "Your game has been saved. "
                                        info_text_3 = ""
                                        info_text_4 = ""
                                        player.star_power += 1
                                        player.experience += 50
                                        if player.experience >= 100:
                                            gameplay_functions.level_up(player, level_up_win, level_up_font)
                                            leveled = True
                                            loot_level_tic = time.perf_counter()
                                        player.reputation["amuna"] += 10
                                        # autosave on quest complete
                                        try:
                                            gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                                         sharp_sense_learned, saved, npc_garan.gift,
                                                                         rest_recover_show, knowledge_academia_show,
                                                                         quest_guide_shown, battle_guide_shown,
                                                                         rest_shown_before, quest_highlight_popup,
                                                                         bridge_not_repaired, nede_ghoul_defeated,
                                                                         bridge_cutscenes_not_viewed, crate_1, crate_2,
                                                                         crate_3, crate_4, crate_5, switch_1, switch_2,
                                                                         switch_3, muchador_defeated, has_key,
                                                                         mini_boss_1_defeated, mini_boss_2_defeated,
                                                                         gloves_obtained, korlok_attuned,
                                                                         eldream_attuned)
                                        except PermissionError:
                                            pass
                                    else:
                                        info_text_1 = "You completed the quest, but "
                                        info_text_2 = "Your inventory is full!"
                                if not quest_clicked:
                                    if not player.quest_complete["sneaky snakes"]:
                                        drawing_functions.quest_box_draw(current_npc_interacting, True,
                                                                         garan_quest_window,
                                                                         maurelle_quest_window, celeste_quest_window,
                                                                         torune_quest_window, voruke_quest_window,
                                                                         zerah_quest_window, kirean_quest_window,
                                                                         dionte_quest_window, accept_button,
                                                                         decline_button)
                                        quest_clicked = True
                                    else:  # quest complete popup
                                        if not garan_complete_shown:
                                            drawing_functions.quest_complete_draw(current_npc_interacting, True,
                                                                                  garan_complete_quest_window,
                                                                                  maurelle_complete_quest_window,
                                                                                  celeste_complete_quest_window,
                                                                                  torune_complete_quest_window,
                                                                                  voruke_complete_quest_window,
                                                                                  zerah_complete_quest_window,
                                                                                  kirean_complete_quest_window,
                                                                                  dionte_complete_quest_window)
                                            garan_complete_shown = True
                                            quest_clicked = True
                                else:
                                    drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                                     maurelle_quest_window, celeste_quest_window,
                                                                     torune_quest_window, voruke_quest_window,
                                                                     zerah_quest_window, kirean_quest_window,
                                                                     dionte_quest_window, accept_button, decline_button)
                                    quest_clicked = False

                            # celeste npc, check player's quest progress and reward if completed -----------------------
                            if current_npc_interacting.name == "celeste":
                                if player.quest_progress["where's nede?"] == 1 and not \
                                        player.quest_complete["where's nede?"]:
                                    if len(player.items) < 16:
                                        nede.update(nede.x_coordinate, nede.y_coordinate, graphic_dict["nede_left"])
                                        player.quest_complete["where's nede?"] = True
                                        player.current_quests["where's nede?"] = "You completed this quest!"
                                        info_text_1 = "You've completed Celeste's quest!"
                                        info_text_2 = "Your game has been saved. "
                                        info_text_3 = ""
                                        info_text_4 = ""
                                        player.star_power += 1
                                        player.experience += 50
                                        if player.experience >= 100:
                                            gameplay_functions.level_up(player, level_up_win, level_up_font)
                                            leveled = True
                                            loot_level_tic = time.perf_counter()
                                        player.reputation["sorae"] += 10
                                        # autosave on quest complete
                                        try:
                                            gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                                         sharp_sense_learned, saved, npc_garan.gift,
                                                                         rest_recover_show, knowledge_academia_show,
                                                                         quest_guide_shown, battle_guide_shown,
                                                                         rest_shown_before, quest_highlight_popup,
                                                                         bridge_not_repaired, nede_ghoul_defeated,
                                                                         bridge_cutscenes_not_viewed, crate_1, crate_2,
                                                                         crate_3, crate_4, crate_5, switch_1, switch_2,
                                                                         switch_3, muchador_defeated, has_key,
                                                                         mini_boss_1_defeated, mini_boss_2_defeated,
                                                                         gloves_obtained, korlok_attuned,
                                                                         eldream_attuned)
                                        except PermissionError:
                                            pass
                                    else:
                                        info_text_1 = "You completed the quest, but "
                                        info_text_2 = "Your inventory is full!"
                                if not quest_clicked:
                                    if not player.quest_complete["where's nede?"]:
                                        drawing_functions.quest_box_draw(current_npc_interacting, True,
                                                                         garan_quest_window,
                                                                         maurelle_quest_window, celeste_quest_window,
                                                                         torune_quest_window, voruke_quest_window,
                                                                         zerah_quest_window, kirean_quest_window,
                                                                         dionte_quest_window, accept_button,
                                                                         decline_button)
                                        quest_clicked = True
                                    else:  # quest complete popup
                                        if not celeste_complete_shown:
                                            drawing_functions.quest_complete_draw(current_npc_interacting, True,
                                                                                  garan_complete_quest_window,
                                                                                  maurelle_complete_quest_window,
                                                                                  celeste_complete_quest_window,
                                                                                  torune_complete_quest_window,
                                                                                  voruke_complete_quest_window,
                                                                                  zerah_complete_quest_window,
                                                                                  kirean_complete_quest_window,
                                                                                  dionte_complete_quest_window)
                                            celeste_complete_shown = True
                                            quest_clicked = True
                                else:
                                    drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                                     maurelle_quest_window, celeste_quest_window,
                                                                     torune_quest_window, voruke_quest_window,
                                                                     zerah_quest_window, kirean_quest_window,
                                                                     dionte_quest_window, accept_button, decline_button)
                                    quest_clicked = False

                            # maurelle npc, check player's quest progress and reward if completed ----------------------
                            if current_npc_interacting.name == "maurelle":
                                if player.quest_progress["village repairs"] == 4 and not \
                                        player.quest_complete["village repairs"]:
                                    if len(player.items) < 16:
                                        player.quest_complete["village repairs"] = True
                                        player.current_quests["village repairs"] = "You completed this quest!"
                                        info_text_1 = "You've completed Maurelle's quest!"
                                        info_text_2 = "Your game has been saved. "
                                        info_text_3 = ""
                                        info_text_4 = ""
                                        player.star_power += 1
                                        player.experience += 50
                                        if player.experience >= 100:
                                            gameplay_functions.level_up(player, level_up_win, level_up_font)
                                            leveled = True
                                            loot_level_tic = time.perf_counter()
                                        player.reputation["amuna"] += 10
                                        # autosave on quest complete
                                        try:
                                            gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                                         sharp_sense_learned, saved, npc_garan.gift,
                                                                         rest_recover_show, knowledge_academia_show,
                                                                         quest_guide_shown, battle_guide_shown,
                                                                         rest_shown_before, quest_highlight_popup,
                                                                         bridge_not_repaired, nede_ghoul_defeated,
                                                                         bridge_cutscenes_not_viewed, crate_1, crate_2,
                                                                         crate_3, crate_4, crate_5, switch_1, switch_2,
                                                                         switch_3, muchador_defeated, has_key,
                                                                         mini_boss_1_defeated, mini_boss_2_defeated,
                                                                         gloves_obtained, korlok_attuned,
                                                                         eldream_attuned)
                                        except PermissionError:
                                            pass
                                    else:
                                        info_text_1 = "You completed the quest, but "
                                        info_text_2 = "Your inventory is full!"
                                if not quest_clicked:
                                    if not player.quest_complete["village repairs"]:
                                        drawing_functions.quest_box_draw(current_npc_interacting, True,
                                                                         garan_quest_window,
                                                                         maurelle_quest_window, celeste_quest_window,
                                                                         torune_quest_window, voruke_quest_window,
                                                                         zerah_quest_window, kirean_quest_window,
                                                                         dionte_quest_window, accept_button,
                                                                         decline_button)
                                        quest_clicked = True
                                    else:  # quest complete popup
                                        if not maurelle_complete_shown:
                                            drawing_functions.quest_complete_draw(current_npc_interacting, True,
                                                                                  garan_complete_quest_window,
                                                                                  maurelle_complete_quest_window,
                                                                                  celeste_complete_quest_window,
                                                                                  torune_complete_quest_window,
                                                                                  voruke_complete_quest_window,
                                                                                  zerah_complete_quest_window,
                                                                                  kirean_complete_quest_window,
                                                                                  dionte_complete_quest_window)
                                            maurelle_complete_shown = True
                                            quest_clicked = True
                                else:
                                    drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                                     maurelle_quest_window, celeste_quest_window,
                                                                     torune_quest_window, voruke_quest_window,
                                                                     zerah_quest_window, kirean_quest_window,
                                                                     dionte_quest_window, accept_button, decline_button)
                                    quest_clicked = False

                            # torune npc, check player's quest progress and reward if completed ------------------------
                            if current_npc_interacting.name == "torune":
                                if player.quest_progress["ghouled again"] == 4 and not \
                                        player.quest_complete["ghouled again"]:
                                    if len(player.items) < 16:
                                        player.quest_complete["ghouled again"] = True
                                        player.current_quests["ghouled again"] = "You completed this quest!"
                                        info_text_1 = "You've completed Torune's quest!"
                                        info_text_2 = "Your game has been saved. "
                                        info_text_3 = ""
                                        info_text_4 = ""
                                        player.star_power += 1
                                        player.experience += 50
                                        if player.experience >= 100:
                                            gameplay_functions.level_up(player, level_up_win, level_up_font)
                                            leveled = True
                                            loot_level_tic = time.perf_counter()
                                        player.reputation["nuldar"] += 10
                                        # autosave on quest complete
                                        try:
                                            gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                                         sharp_sense_learned, saved, npc_garan.gift,
                                                                         rest_recover_show, knowledge_academia_show,
                                                                         quest_guide_shown, battle_guide_shown,
                                                                         rest_shown_before, quest_highlight_popup,
                                                                         bridge_not_repaired, nede_ghoul_defeated,
                                                                         bridge_cutscenes_not_viewed, crate_1, crate_2,
                                                                         crate_3, crate_4, crate_5, switch_1, switch_2,
                                                                         switch_3, muchador_defeated, has_key,
                                                                         mini_boss_1_defeated, mini_boss_2_defeated,
                                                                         gloves_obtained, korlok_attuned,
                                                                         eldream_attuned)
                                        except PermissionError:
                                            pass
                                    else:
                                        info_text_1 = "You completed the quest, but "
                                        info_text_2 = "Your inventory is full!"
                                if not quest_clicked:
                                    if not player.quest_complete["ghouled again"]:
                                        drawing_functions.quest_box_draw(current_npc_interacting, True,
                                                                         garan_quest_window,
                                                                         maurelle_quest_window, celeste_quest_window,
                                                                         torune_quest_window, voruke_quest_window,
                                                                         zerah_quest_window, kirean_quest_window,
                                                                         dionte_quest_window, accept_button,
                                                                         decline_button)
                                        quest_clicked = True
                                    else:  # quest complete popup
                                        if not torune_complete_shown:
                                            drawing_functions.quest_complete_draw(current_npc_interacting, True,
                                                                                  garan_complete_quest_window,
                                                                                  maurelle_complete_quest_window,
                                                                                  celeste_complete_quest_window,
                                                                                  torune_complete_quest_window,
                                                                                  voruke_complete_quest_window,
                                                                                  zerah_complete_quest_window,
                                                                                  kirean_complete_quest_window,
                                                                                  dionte_complete_quest_window)
                                            torune_complete_shown = True
                                            quest_clicked = True
                                else:
                                    drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                                     maurelle_quest_window, celeste_quest_window,
                                                                     torune_quest_window, voruke_quest_window,
                                                                     zerah_quest_window, kirean_quest_window,
                                                                     dionte_quest_window, accept_button, decline_button)
                                    quest_clicked = False

                            # voruke npc, check player's quest progress and reward if completed ------------------------
                            if current_npc_interacting.name == "voruke":
                                if player.quest_progress["band hammer"] == 4 and not \
                                        player.quest_complete["band hammer"]:
                                    if len(player.items) < 16:
                                        player.quest_complete["band hammer"] = True
                                        player.current_quests["band hammer"] = "You completed this quest!"
                                        info_text_1 = "You've completed Voruke's quest!"
                                        info_text_2 = "Your game has been saved. "
                                        info_text_3 = ""
                                        info_text_4 = ""
                                        player.star_power += 1
                                        player.experience += 50
                                        if player.experience >= 100:
                                            gameplay_functions.level_up(player, level_up_win, level_up_font)
                                            leveled = True
                                            loot_level_tic = time.perf_counter()
                                        player.reputation["nuldar"] += 10
                                        # autosave on quest complete
                                        try:
                                            gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                                         sharp_sense_learned, saved, npc_garan.gift,
                                                                         rest_recover_show, knowledge_academia_show,
                                                                         quest_guide_shown, battle_guide_shown,
                                                                         rest_shown_before, quest_highlight_popup,
                                                                         bridge_not_repaired, nede_ghoul_defeated,
                                                                         bridge_cutscenes_not_viewed, crate_1, crate_2,
                                                                         crate_3, crate_4, crate_5, switch_1, switch_2,
                                                                         switch_3, muchador_defeated, has_key,
                                                                         mini_boss_1_defeated, mini_boss_2_defeated,
                                                                         gloves_obtained, korlok_attuned,
                                                                         eldream_attuned)
                                        except PermissionError:
                                            pass
                                    else:
                                        info_text_1 = "You completed the quest, but "
                                        info_text_2 = "Your inventory is full!"
                                if not quest_clicked:
                                    if not player.quest_complete["band hammer"]:
                                        drawing_functions.quest_box_draw(current_npc_interacting, True,
                                                                         garan_quest_window,
                                                                         maurelle_quest_window,
                                                                         celeste_quest_window,
                                                                         torune_quest_window, voruke_quest_window,
                                                                         zerah_quest_window, kirean_quest_window,
                                                                         dionte_quest_window, accept_button,
                                                                         decline_button)
                                        quest_clicked = True
                                    else:  # quest complete popup
                                        if not voruke_complete_shown:
                                            drawing_functions.quest_complete_draw(current_npc_interacting, True,
                                                                                  garan_complete_quest_window,
                                                                                  maurelle_complete_quest_window,
                                                                                  celeste_complete_quest_window,
                                                                                  torune_complete_quest_window,
                                                                                  voruke_complete_quest_window,
                                                                                  zerah_complete_quest_window,
                                                                                  kirean_complete_quest_window,
                                                                                  dionte_complete_quest_window)
                                            voruke_complete_shown = True
                                            quest_clicked = True
                                else:
                                    drawing_functions.quest_box_draw(current_npc_interacting, False,
                                                                     garan_quest_window, maurelle_quest_window,
                                                                     celeste_quest_window, torune_quest_window,
                                                                     voruke_quest_window, zerah_quest_window,
                                                                     kirean_quest_window, dionte_quest_window,
                                                                     accept_button, decline_button)
                                    quest_clicked = False

                            # voruke npc, check player's quest progress and reward if completed ------------------------
                            if current_npc_interacting.name == "zerah":
                                if player.quest_progress["elementary elementals"] == 4 and not \
                                        player.quest_complete["elementary elementals"]:
                                    if len(player.items) < 16:
                                        player.quest_complete["elementary elementals"] = True
                                        player.current_quests["elementary elementals"] = "You completed this quest!"
                                        info_text_1 = "You've completed Zerah's quest!"
                                        info_text_2 = "Your game has been saved. "
                                        info_text_3 = ""
                                        info_text_4 = ""
                                        player.star_power += 1
                                        player.experience += 50
                                        if player.experience >= 100:
                                            gameplay_functions.level_up(player, level_up_win, level_up_font)
                                            leveled = True
                                            loot_level_tic = time.perf_counter()
                                        player.reputation["nuldar"] += 10
                                        # autosave on quest complete
                                        try:
                                            gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                                         sharp_sense_learned, saved, npc_garan.gift,
                                                                         rest_recover_show, knowledge_academia_show,
                                                                         quest_guide_shown, battle_guide_shown,
                                                                         rest_shown_before, quest_highlight_popup,
                                                                         bridge_not_repaired, nede_ghoul_defeated,
                                                                         bridge_cutscenes_not_viewed, crate_1, crate_2,
                                                                         crate_3, crate_4, crate_5, switch_1, switch_2,
                                                                         switch_3, muchador_defeated, has_key,
                                                                         mini_boss_1_defeated, mini_boss_2_defeated,
                                                                         gloves_obtained, korlok_attuned,
                                                                         eldream_attuned)
                                        except PermissionError:
                                            pass
                                    else:
                                        info_text_1 = "You completed the quest, but "
                                        info_text_2 = "Your inventory is full!"
                                if not quest_clicked:
                                    if not player.quest_complete["elementary elementals"]:
                                        drawing_functions.quest_box_draw(current_npc_interacting, True,
                                                                         garan_quest_window, maurelle_quest_window,
                                                                         celeste_quest_window, torune_quest_window,
                                                                         voruke_quest_window, zerah_quest_window,
                                                                         kirean_quest_window, dionte_quest_window,
                                                                         accept_button, decline_button)
                                        quest_clicked = True
                                    else:  # quest complete popup
                                        if not zerah_complete_shown:
                                            drawing_functions.quest_complete_draw(current_npc_interacting, True,
                                                                                  garan_complete_quest_window,
                                                                                  maurelle_complete_quest_window,
                                                                                  celeste_complete_quest_window,
                                                                                  torune_complete_quest_window,
                                                                                  voruke_complete_quest_window,
                                                                                  zerah_complete_quest_window,
                                                                                  kirean_complete_quest_window,
                                                                                  dionte_complete_quest_window)
                                            zerah_complete_shown = True
                                            quest_clicked = True
                                else:
                                    drawing_functions.quest_box_draw(current_npc_interacting, False,
                                                                     garan_quest_window, maurelle_quest_window,
                                                                     celeste_quest_window, torune_quest_window,
                                                                     voruke_quest_window, zerah_quest_window,
                                                                     kirean_quest_window, dionte_quest_window,
                                                                     accept_button, decline_button)
                                    quest_clicked = False

                            # dionte npc, check player's quest progress and reward if completed ------------------------
                            if current_npc_interacting.name == "dionte":
                                if player.quest_progress["it's dangerous to go alone"] == 1 and not \
                                        player.quest_complete["it's dangerous to go alone"]:
                                    if len(player.items) < 16:
                                        player.quest_complete["it's dangerous to go alone"] = True
                                        player.current_quests["it's dangerous to go alone"] = "You completed this" \
                                                "quest!"
                                        info_text_1 = "You've completed Dionte's quest!"
                                        info_text_2 = "Your game has been saved. "
                                        info_text_3 = ""
                                        info_text_4 = ""
                                        player.star_power += 1
                                        player.experience += 50
                                        if player.experience >= 100:
                                            gameplay_functions.level_up(player, level_up_win, level_up_font)
                                            leveled = True
                                            loot_level_tic = time.perf_counter()
                                        player.reputation["amuna"] += 10
                                        # autosave on quest complete
                                        try:
                                            gameplay_functions.save_game(player, barrier_learned, hard_strike_learned,
                                                                         sharp_sense_learned, saved, npc_garan.gift,
                                                                         rest_recover_show, knowledge_academia_show,
                                                                         quest_guide_shown, battle_guide_shown,
                                                                         rest_shown_before, quest_highlight_popup,
                                                                         bridge_not_repaired, nede_ghoul_defeated,
                                                                         bridge_cutscenes_not_viewed, crate_1, crate_2,
                                                                         crate_3, crate_4, crate_5, switch_1, switch_2,
                                                                         switch_3, muchador_defeated, has_key,
                                                                         mini_boss_1_defeated, mini_boss_2_defeated,
                                                                         gloves_obtained, korlok_attuned,
                                                                         eldream_attuned)
                                        except PermissionError:
                                            pass
                                    else:
                                        info_text_1 = "You completed the quest, but "
                                        info_text_2 = "Your inventory is full!"
                                if not quest_clicked:
                                    if not player.quest_complete["it's dangerous to go alone"]:
                                        drawing_functions.quest_box_draw(current_npc_interacting, True,
                                                                         garan_quest_window, maurelle_quest_window,
                                                                         celeste_quest_window, torune_quest_window,
                                                                         voruke_quest_window, zerah_quest_window,
                                                                         kirean_quest_window, dionte_quest_window,
                                                                         accept_button, decline_button)
                                        quest_clicked = True
                                    else:  # quest complete popup
                                        if not dionte_complete_shown:
                                            drawing_functions.quest_complete_draw(current_npc_interacting, True,
                                                                                  garan_complete_quest_window,
                                                                                  maurelle_complete_quest_window,
                                                                                  celeste_complete_quest_window,
                                                                                  torune_complete_quest_window,
                                                                                  voruke_complete_quest_window,
                                                                                  zerah_complete_quest_window,
                                                                                  kirean_complete_quest_window,
                                                                                  dionte_complete_quest_window)
                                            dionte_complete_shown = True
                                            quest_clicked = True
                                else:
                                    drawing_functions.quest_box_draw(current_npc_interacting, False,
                                                                     garan_quest_window, maurelle_quest_window,
                                                                     celeste_quest_window, torune_quest_window,
                                                                     voruke_quest_window, zerah_quest_window,
                                                                     kirean_quest_window, dionte_quest_window,
                                                                     accept_button, decline_button)
                                    quest_clicked = False

                        if npc_button == "leave":
                            npc_button = ''
                            movement_able = True
                            interacted = False
                            encounter_started = False
                            in_npc_interaction = False
                            in_over_world = True
                            quest_clicked = False
                            drawing_functions.quest_complete_box.clear()
                            drawing_functions.quest_box_draw(current_npc_interacting, False, garan_quest_window,
                                                             maurelle_quest_window, celeste_quest_window,
                                                             torune_quest_window, voruke_quest_window,
                                                             zerah_quest_window, kirean_quest_window,
                                                             dionte_quest_window, accept_button, decline_button)
                            drawing_functions.type_advantage_window.clear()

                    # outside event loop -------------------------------------------------------------------------------
                    if not encounter_started:
                        info_text_1 = ""
                        info_text_2 = ""
                        info_text_3 = ""
                        info_text_4 = ""
                        encounter_started = True

                    # draw objects to screen related to npc interaction scenario ---------------------------------------
                    if in_npc_interaction and not in_over_world and not in_shop and not in_inn and not \
                            in_academia and not in_battle:
                        if player.current_zone == "seldon":
                            screen.blit(seldon_district_battle, (0, 0))
                        if player.current_zone == "korlok":
                            screen.blit(korlok_district_battle, (0, 0))
                        if player.current_zone == "terra trail":
                            screen.blit(terra_trail_screen, (0, 0))
                        screen.blit(equipment_screen.surf, equipment_screen.rect)
                        screen.blit(offense_meter.surf, offense_meter.rect)
                        screen.blit(defense_meter.surf, defense_meter.rect)
                        drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)
                        combat_scenario.resting_animation(player, current_enemy_battling, player_battle_sprite,
                                                          snake_battle_sprite, ghoul_battle_sprite,
                                                          chorizon_battle_sprite, muchador_battle_sprite,
                                                          magmon_battle_sprite, bandile_battle_sprite,
                                                          chinzilla_battle_sprite, barrier_active,
                                                          sharp_sense_active, in_battle, in_npc_interaction,
                                                          graphic_dict)
                        screen.blit(player_battle_sprite.surf, player_battle_sprite.rect)
                        screen.blit(bar_backdrop.surf, bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(leave_button.surf, leave_button.rect)
                        screen.blit(quest_button.surf, quest_button.rect)
                        # noinspection PyUnboundLocalVariable
                        if current_npc_interacting.name == "garan":
                            screen.blit(npc_garan_interaction.surf, npc_garan_interaction.rect)
                        if current_npc_interacting.name == "maurelle":
                            screen.blit(npc_maurelle_interaction.surf, npc_maurelle_interaction.rect)
                        if current_npc_interacting.name == "celeste":
                            if player.quest_progress["where's nede?"] == 1:
                                screen.blit(nede_big.surf, nede_big.rect)
                            screen.blit(npc_celeste_interaction.surf, npc_celeste_interaction.rect)
                        if current_npc_interacting.name == "torune":
                            screen.blit(npc_torune_interaction.surf, npc_torune_interaction.rect)
                        if current_npc_interacting.name == "voruke":
                            screen.blit(npc_voruke_interaction.surf, npc_voruke_interaction.rect)
                        if current_npc_interacting.name == "zerah":
                            screen.blit(npc_zerah_interaction.surf, npc_zerah_interaction.rect)
                        if current_npc_interacting.name == "dionte":
                            screen.blit(npc_dionte_interaction.surf, npc_dionte_interaction.rect)
                        screen.blit(npc_name_plate.surf, npc_name_plate.rect)
                        screen.blit(message_box.surf, message_box.rect)
                        screen.blit(star_power_meter.surf, star_power_meter.rect)
                        # draw texts to the screen, like message box, player rupees and level, inv and equ updates
                        drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3,
                                                         info_text_4, in_over_world)
                        text_npc_name_surf = font.render(str(current_npc_interacting.name), True, "black",
                                                         (203, 195, 227))
                        text_npc_name_rect = text_npc_name_surf.get_rect()
                        text_npc_name_rect.center = (637, 192)
                        screen.blit(text_npc_name_surf, text_npc_name_rect)
                        drawing_functions.draw_it(screen)

                        if button_highlighted:
                            screen.blit(button_highlight.surf, button_highlight.rect)

                        if first_npc_cond:
                            directional_arrow.update(855, 620, graphic_dict["arrow_down"])
                            screen.blit(directional_arrow.surf, directional_arrow.rect)

                # ------------------------------------------------------------------------------------------------------
                # end of whole iteration -------------------------------------------------------------------------------
                clock.tick(60)
                pygame.display.flip()

            # ----------------------------------------------------------------------------------------------------------
            # player has died, show game over and give continue option -------------------------------------------------
            else:
                button_highlight.update(lets_go_button.x_coordinate, lets_go_button.y_coordinate,
                                        graphic_dict["lets_go_button_high"])
                screen.blit(game_over_screen, (0, 0))
                screen.blit(lets_go_button.surf, lets_go_button.rect)
                for event in pygame.event.get():
                    pos = pygame.mouse.get_pos()
                    if lets_go_button.rect.collidepoint(pos):
                        button_highlighted = True
                    else:
                        button_highlighted = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        # player chooses to continue, reset character experience and half health and energy on respawn
                        if lets_go_button.rect.collidepoint(pos):
                            info_text_1 = ""
                            info_text_2 = ""
                            info_text_3 = ""
                            info_text_4 = ""
                            button_highlighted = False
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
                            over_world_song_set = False
                            if mini_boss_1:
                                mini_boss_1 = False
                            if mini_boss_2:
                                mini_boss_2 = False
                            if not switch_3:
                                switch_1 = False
                                switch_2 = False
                            # turn off barrier and restore original defence if player mage was killed while active
                            if barrier_active:
                                barrier_active = False

                            # turn off barrier and restore original defence if player mage was killed while active
                            if sharp_sense_active:
                                sharp_sense_active = False

                            if player.current_zone == "korlok" or player.current_zone == "mines" or \
                                    player.current_zone == "terra trail":
                                player.current_zone = "korlok"
                                player.x_coordinate = 882
                                player.y_coordinate = 290
                                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
                            else:
                                player.current_zone = "seldon"
                                player.x_coordinate = 860
                                player.y_coordinate = 655
                                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

                            # player returns in a weakened state
                            player.health = 25
                            player.energy = 25
                            player.alive_status = True
                            rest_recover_show = True

                            # bring enemies back to full health
                            for enemy in seldon_enemies:
                                enemy.health = 100
                                # noinspection PyTypeChecker
                                combat_scenario.enemy_health_bar(enemy, graphic_dict)
                            for enemy in korlok_enemies:
                                enemy.health = 100
                                # noinspection PyTypeChecker
                                combat_scenario.enemy_health_bar(enemy, graphic_dict)
                            for enemy in bandiles:
                                enemy.health = 100
                                # noinspection PyTypeChecker
                                combat_scenario.enemy_health_bar(enemy, graphic_dict)

                            muchador.health = 100
                            chinzilla.health = 100
                            combat_scenario.enemy_health_bar(muchador, graphic_dict)

                    elif event.type == QUIT:
                        pygame.mixer.quit()
                        sys.exit()

                if button_highlighted:
                    screen.blit(button_highlight.surf, button_highlight.rect)

                pygame.display.flip()
