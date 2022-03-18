import random
import pygame
from pygame import K_f
from pygame.locals import (RLEACCEL, K_w, K_s, K_a, K_d, K_ESCAPE, KEYDOWN, QUIT)

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
        self.surf = pygame.image.load("art/character_art/player_character/default/stan_down.png").convert()
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
            self.surf = pygame.image.load("art/character_art/player_character/default/stan_up.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.y = ACC
            self.acc.y = -ACC

        if pressed_keyes[K_s]:
            self.surf = pygame.image.load("art/character_art/player_character/default/stan_down.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.y = ACC

        if pressed_keyes[K_a]:
            self.surf = pygame.image.load("art/character_art/player_character/default/stan_left.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.x = -ACC

        if pressed_keyes[K_d]:
            self.surf = pygame.image.load("art/character_art/player_character/default/stan_right.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.acc.x = ACC

        # Keep player on the screen, boundaries vary depending on current zone -----------------------------------------
        if current_zone == "seldon":
            if self.pos.x < 25:
                self.pos.x = 25

            elif self.pos.x > SCREEN_WIDTH - 115:
                self.pos.x = SCREEN_WIDTH - 115

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
        if pygame.sprite.spritecollide(player, environment_objects, False, pygame.sprite.collide_rect_ratio(0.75)):

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
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


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
        "escaped": False
    }

    if combat_event == "attack":

        if enemy_combating.alive_status:

            # returns players damage to the enemy based on level and equipment
            attacked_enemy = attack_enemy(enemy_combating)

            enemy_combating.health = enemy_combating.health - attacked_enemy
            health_bar_update_enemy(enemy_combating)

            # if enemy is not dead yet
            if enemy_combating.health > 0:

                attacked_enemy_string = f" You did {attacked_enemy} damage to {enemy_combating.name}."

                # add damage to enemy to event dictionary to be returned to main loop ------------------------------
                combat_event_dictionary["damage done"] = attacked_enemy_string

                # returns total damage output from enemy as attacked_player value
                attacked_player = attack_player()
                if attacked_player > 0:
                    attacked_player_string = f"You take {attacked_player} damage from {enemy_combating.name}."
                    player.health = player.health - attacked_player

                    # add damage done to player from enemy to dictionary -------------------------------------------
                    combat_event_dictionary["damage taken"] = attacked_player_string

                    # enemy has defeated player, game over
                    if player.health < 0:
                        player.alive_status = False

                    return combat_event_dictionary

                else:
                    enemy_miss_string = f'{enemy_combating.name} missed.'

                    # add to dictionary that enemy did no damage to player -----------------------------------------
                    combat_event_dictionary["damage taken"] = enemy_miss_string

                    return combat_event_dictionary

            # enemy has been defeated, will return an amount of xp based on current levels
            else:

                # if player is on quest to kill snakes from Garan
                if enemy_combating.kind == "snake":
                    if player.current_quest == "Sneaky Snakes":
                        if player.quest_status < 4:
                            player.quest_status = player.quest_status + 1
                            quest_string = f"*** {player.quest_status}/4 snakes for [{player.current_quest}] quest ***"

                            # add to dictionary player quest updates if enemy was an objective of quest for player -
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No quest"

                # if player is on quest to kill snakes from Garan
                if enemy_combating.kind == "ghoul":
                    if player.current_quest == "Ghoulish Ghosts":
                        if player.quest_status < 4:
                            player.quest_status = player.quest_status + 1
                            quest_string = f"*** {player.quest_status}/4 ghouls for [{player.current_quest}] quest ***"

                            # add to dictionary player quest updates if enemy was an objective of quest for player -
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # only gain experience from enemies equal or higher level
                if player.level <= enemy_combating.level:
                    experience = int((enemy_combating.level / player.level) * 5)
                    player.experience = player.experience + experience

                    enemy_experience = f"Gained {experience} experience."

                    # add to dictionary experience given from defeating enemy --------------------------------------
                    combat_event_dictionary["experience gained"] = enemy_experience

                drop_chance = random.randrange(1, 10)

                # 70% chance to drop merchant item
                if drop_chance > 3:
                    player.items.append(enemy_combating.items)

                    enemy_dropped_this = f"{enemy_combating.name} dropped [{enemy_combating.items.name}]. "

                    # add to dictionary anything dropped from enemy upon their defeat ------------------------------
                    combat_event_dictionary["item dropped"] = enemy_dropped_this

                else:
                    combat_event_dictionary["item dropped"] = "No"

                # player will level up (see level up method)
                if player.experience > 100:
                    level_up()

                enemy_combating.alive_status = False
                enemy_combating.kill()

                # add to dictionary True if enemy has been defeated so scenario will end ---------------------------
                combat_event_dictionary["enemy defeated"] = True

                return combat_event_dictionary

        else:
            print("\nThis enemy appears to be dead already!")

    if combat_event == "run":

        escape_chance = random.randrange(35, 75)
        if escape_chance > 50:

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


def attack_enemy(enemy_attacked):
    # fighters do more damage with 2-handed weapons -------------------------
    if player.role == "fighter":
        if player.equipment[0] == "2H":
            damage = (random.randrange(10, 40) // enemy_attacked.level)

            # includes player strength stat to scale overall damage
            stat_scale = damage * player.statistics[5]

            return stat_scale

        else:
            damage = (random.randrange(1, 10) // enemy_attacked.level)
            print("\n*** You may have an incorrect weapon type equipped! ***")

            return damage

    # mages do more damage with magic weapons --------------------------------
    if player.role == "mage":
        if player.equipment[0] == "magic":
            damage = (random.randrange(10, 40) // enemy_attacked.level)

            # includes player wisdom stat to scale overall damage
            stat_scale = (damage * player.statistics[7]) // 2

            return stat_scale

        else:
            damage = (random.randrange(1, 10) // enemy_attacked.level)
            print("\n*** You may have an incorrect weapon type equipped! ***")

            return damage

    # rogues do more damage with 1-handed weapons ----------------------------
    if player.role == "rogue":
        if player.equipment[0] == "1H":
            damage = (random.randrange(10, 40) // enemy_attacked.level)

            # includes player strength stat to scale overall damage (strength will be higher for rogues)
            stat_scale = damage * player.statistics[5]

            return stat_scale

        else:
            damage = (random.randrange(1, 10) // enemy_attacked.level)
            print("\n*** You may have an incorrect weapon type equipped! ***")

            return damage


def attack_player():
    base_damage = (random.randrange(5, 15) // player.level)

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


def level_up():
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


# ----------------------------------------------------------------------------------------------------------------------
# gets current player health and updates hp bar image on screen according to the health value from 0-100
def health_bar_update(character):
    for i in range(0, 100):
        if character.health == i:
            hp_bar.update("art/ui_elements/bars/health/hp_bar_" + str(i) + ".png")


# player energy bar update
def energy_bar_update(character):
    for i in range(0, 100):
        if character.energy == i:
            en_bar.update("art/ui_elements/bars/energy/en_bar_" + str(i) + ".png")


# player xp bar update
def xp_bar_update(character):
    for i in range(0, 100):
        if character.experience == i:
            xp_bar.update("art/ui_elements/bars/xp/xp_bar_" + str(i) + ".png")


# enemy health bar update
def health_bar_update_enemy(character):
    for i in range(0, 100):
        if character.health == i:
            character.health_bar.update("art/ui_elements/bars/health/hp_bar_" + str(i) + ".png")


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
# getting event based on user click related to combat scenario (attack, skill and run buttons).
def inventory_event_item(inventory_event):
    if inventory_event.type == pygame.MOUSEBUTTONUP:
        inventory_mouse = pygame.mouse.get_pos()

        # list of sprites that collided with mouse cursor rect
        clicked_combat_element = [element for element in player_items if element.rect.collidepoint(inventory_mouse)]

        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_combat_element[0].__getattribute__("name") == "health potion":
                return clicked_combat_element[0]

            if clicked_combat_element[0].__getattribute__("name") == "energy potion":
                return clicked_combat_element[0]

            if clicked_combat_element[0].__getattribute__("name") == "shiny rock":
                return clicked_combat_element[0]

            if clicked_combat_element[0].__getattribute__("name") == "bone dust":
                return clicked_combat_element[0]

        except IndexError:
            pass


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
# pygame.mixer.init()

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 1024 x 768

# background textures --------------------------------------------------------------------------------------------------
seldon_district_bg = pygame.image.load("art/environment_art/background_textures/seldon_district.png")
seldon_district_battle = pygame.image.load("art/environment_art/background_textures/seldon_battle_screen.png")
seldon_district_shop = pygame.image.load("art/environment_art/background_textures/seldon_shop.png")

game_over_screen = pygame.image.load("art/screens/game_over.png")

# creating objects from defined classes --------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# display notifications to user (shown, x_coordinate, y_coordinate, image, color) --------------------------------------
greeting = Notification("greeting", False, 512, 384, "art/ui_elements/notifications/welcome.png", (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# inventory items ------------------------------------------------------------------------------------------------------
health_potion = Item("health potion", "potion", 200, 200, "art/item_art/health_potion.png", (255, 255, 255))
energy_potion = Item("energy potion", "potion", 200, 200, "art/item_art/energy_potion.png", (255, 255, 255))
shiny_rock = Item("shiny rock", "rock", 200, 200, "art/item_art/shiny_rock.png", (255, 255, 255))
bone_dust = Item("bone dust", "dust", 200, 200, "art/item_art/bone_dust.png", (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# default player character ---------------------------------------------------------------------------------------------
player = Player("Player", "male", "amuna", "mage",  # name, gender, race, role
                [health_potion, energy_potion, shiny_rock, bone_dust],  # inventory
                ["magic", "basic staff", "light", "green robes"],  # equipment ('type', 'name')
                # current quest, quest status (x/4), quest dictionary (quest: done)
                [""], 0, {"Sneaky Snakes": False, "Village Repairs": False, "Ghoulish Ghosts": False},
                ["vitality", 1, "intellect", 3, "strength", 1, "wisdom", 2],  # stats ('stat', 'amount')
                ["barrier"], 1, 0, 100, 100,  # skills, lvl, exp, health, energy
                True, 0, ["amuna", 10, "nuldar", 0, "sorae", 0], "", "")  # alive, rupees, reputation, mount, zone

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
                "trouble. ", 240, 480, True, False, ["Items to be added for thief steal"], False,
                "art/character_art/NPCs/garan.png", (255, 255, 255))

npc_maurelle = NPC("Village Matron Maurelle", "female", "amuna", "mage", "We need help!", "Village Repairs",
                   "You there! I don't know who you are, or why you're here, but we could \nreally use your help!"
                   "\n\nThe beast Dreth has occupied our former capital Castle, on the other side of the walls "
                   "\nto the east, and our numbers have been spread thin trying to repel its minions and contain "
                   "the \ndamage they've inflicted. \n\nOur best fighters have been sent in a combined Vanguard with "
                   "the other districts to try and \nattack the beast directly, but its left us vulnerable here. "
                   "The most recent wave of attacks from\nthe castle has left several damages to our village, "
                   "and if you are able, please gather\nresources and bring them to me to distribute to the "
                   "villagers conducting the repairs and \nfortifications. \n\nYou can gather some lumber from the "
                   "trees just west of here. Nera bless you. ", 755, 515, True, False,
                   ["Items to be added for thief steal"], False,
                   "art/character_art/NPCs/maurelle.png", (255, 255, 255))

npc_guard = NPC("Guard", "male", "amuna", "fighter", "Another day.", "Ghoulish Glee",
                "You need to cross the bridge to get to the Korlok District, you say? \n\nOrdinarily"
                " I would have no issue granting you passage, however the gates are barred tight \n"
                "due to the recent wave of Ghoul Minions from across the wall. \n\nI cannot leave my post and"
                " leave the bridge unguarded, but if you could \ntake care of the remaining ghouls I"
                " will signal to unbar the gates and allow you passage \nto the other side. \n\nThe"
                " ghouls were last spotted just east of here, nearby the northern Castle wall ramparts! ", 475, 140,
                True,
                False, ["Items to be added for thief steal"], False,
                "art/character_art/NPCs/guard.png", (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# enemies: kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image, color, health bar ------
snake_1 = Enemy("Snake", "snake", 100, 100, 1, 100, 150, True,
                Item("shiny rock", "rock", 200, 200, "art/item_art/shiny_rock.png", (255, 255, 255)),
                "art/enemy_art/snake.png", (255, 255, 255),
                UiElement("snake hp bar", 700, 90, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255),
                          False))
snake_2 = Enemy("Snake", "snake", 100, 100, 2, 260, 170, True,
                Item("shiny rock", "rock", 200, 200, "art/item_art/shiny_rock.png", (255, 255, 255)),
                "art/enemy_art/snake.png", (255, 255, 255),
                UiElement("snake hp bar", 700, 90, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255),
                          False))
snake_3 = Enemy("Snake", "snake", 100, 100, 1, 100, 250, True,
                Item("shiny rock", "rock", 200, 200, "art/item_art/shiny_rock.png", (255, 255, 255)),
                "art/enemy_art/snake.png", (255, 255, 255),
                UiElement("snake hp bar", 700, 90, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255),
                          False))
snake_4 = Enemy("Snake", "snake", 100, 100, 2, 260, 270, True,
                Item("shiny rock", "rock", 200, 200, "art/item_art/shiny_rock.png", (255, 255, 255)),
                "art/enemy_art/snake.png", (255, 255, 255),
                UiElement("snake hp bar", 700, 90, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255),
                          False))

ghoul_low_1 = Enemy("Ghoul", "ghoul", 100, 100, 4, 675, 200, True,
                    Item("bone dust", "dust", 200, 200, "art/item_art/bone_dust.png", (255, 255, 255)),
                    "art/enemy_art/ghoul.png", (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255),
                              False))
ghoul_low_2 = Enemy("Ghoul", "ghoul", 100, 100, 5, 800, 150, True,
                    Item("bone dust", "dust", 200, 200, "art/item_art/bone_dust.png", (255, 255, 255)),
                    "art/enemy_art/ghoul.png", (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255),
                              False))
ghoul_low_3 = Enemy("Ghoul", "ghoul", 100, 100, 3, 760, 260, True,
                    Item("bone dust", "dust", 200, 200, "art/item_art/bone_dust.png", (255, 255, 255)),
                    "art/enemy_art/ghoul.png", (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255),
                              False))
ghoul_low_4 = Enemy("Ghoul", "ghoul", 100, 100, 4, 875, 225, True,
                    Item("bone dust", "dust", 200, 200, "art/item_art/bone_dust.png", (255, 255, 255)),
                    "art/enemy_art/ghoul.png", (255, 255, 255),
                    UiElement("ghoul hp bar", 700, 90, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255),
                              False))

# trees: name, model, x_coordinate, y_coordinate, gathered, image, color -----------------------------------------------
pine_tree_1 = Tree("pine tree 1", "pine tree", 80, 475, False, "art/environment_art/pine_tree.png", (255, 255, 255))
pine_tree_2 = Tree("pine tree 4", "pine tree", 260, 660, False, "art/environment_art/pine_tree.png", (255, 255, 255))
pine_tree_3 = Tree("pine tree 5", "pine tree", 380, 400, False, "art/environment_art/pine_tree.png", (255, 255, 255))

# buildings: name, model, x_coordinate, y_coordinate, image, color -----------------------------------------------------
amuna_inn = Building("amuna inn", "amuna building", 600, 600,
                     "art/environment_art/buildings/amuna_building_inn.png",
                     (255, 255, 255))
amuna_shop = Building("amuna shop", "amuna building", 650, 400,
                      "art/environment_art/buildings/amuna_building_shop.png",
                      (255, 255, 255))
amuna_academia = Building("amuna academia", "amuna building", 875, 500,
                          "art/environment_art/buildings/amuna_building_academia.png",
                          (255, 255, 255))

# ui elements: name, x_coordinate, y_coordinate, image, color, update flag ---------------------------------------------
inventory_button = UiElement("inventory button", 960, 730, "art/ui_elements/buttons/inventory.png",
                             (255, 255, 255), False)
character_button = UiElement("character button", 850, 730, "art/ui_elements/buttons/character.png",
                             (255, 255, 255), False)
journal_button = UiElement("journal button", 740, 730, "art/ui_elements/buttons/journal.png",
                           (255, 255, 255), False)

attack_button = UiElement("attack button", 740, 670, "art/ui_elements/buttons/battle_screen/attack.png",
                          (255, 255, 255), False)
skill_button = UiElement("skill button", 850, 670, "art/ui_elements/buttons/battle_screen/skill.png",
                         (255, 255, 255), False)
run_button = UiElement("run button", 960, 670, "art/ui_elements/buttons/battle_screen/run.png",
                       (255, 255, 255), False)
continue_button = UiElement("continue button", 500, 600, "art/ui_elements/buttons/continue_button.png",
                            (255, 255, 255), False)
buy_button = UiElement("buy button", 740, 730, "art/ui_elements/buttons/shop/buy.png",
                       (255, 255, 255), False)
sell_button = UiElement("sell button", 850, 730, "art/ui_elements/buttons/shop/sell.png",
                        (255, 255, 255), False)
leave_button = UiElement("leave button", 960, 730, "art/ui_elements/buttons/shop/leave.png",
                         (255, 255, 255), False)

player_status = UiElement("player status", 850, 670, "art/ui_elements/status/player.png", (255, 255, 255), False)
enemy_status = UiElement("enemy status", 850, 730, "art/ui_elements/status/enemy.png", (255, 255, 255), False)

hp_bar = UiElement("hp bar", 170, 25, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255), False)
en_bar = UiElement("en bar", 170, 45, "art/ui_elements/bars/energy/en_bar_full.png", (255, 255, 255), False)
xp_bar = UiElement("xp bar", 170, 65, "art/ui_elements/bars/xp/xp_bar_full.png", (255, 255, 255), False)

enemy_hp_bar = UiElement("enemy hp bar", 700, 90, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255), False)

inventory = Inventory([], 890, 515, "art/ui_elements/inventory.png", (255, 255, 255), False)

message_box = UiElement("message box", 175, 700, "art/ui_elements/message_box.png", (255, 255, 255), False)

status_bar_backdrop = UiElement("status bar backdrop", 165, 45, "art/ui_elements/status_bar_backdrop.png",
                                (255, 255, 255), False)

# ----------------------------------------------------------------------------------------------------------------------
# battle sprites -------------------------------------------------------------------------------------------------------
stan_battle_sprite = BattleCharacter("stan battle", 300, 460,
                                     "art/character_art/player_character/default/battle/stan_battle.png",
                                     (255, 255, 255))

snake_battle_sprite = BattleCharacter("snake battle", 700, 250,
                                      "art/enemy_art/battle/snake_battle.png",
                                      (255, 255, 255))

ghoul_battle_sprite = BattleCharacter("ghoul battle", 700, 250,
                                      "art/enemy_art/battle/ghoul_battle.png",
                                      (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# setting font and size for text to screen updates ---------------------------------------------------------------------
font = pygame.font.SysFont('calibri', 16, bold=True, italic=False)

# ----------------------------------------------------------------------------------------------------------------------
# groups for sprites ---------------------------------------------------------------------------------------------------
npcs = pygame.sprite.Group()
enemies = pygame.sprite.Group()
trees = pygame.sprite.Group()
water = pygame.sprite.Group()
buildings = pygame.sprite.Group()
environment_objects = pygame.sprite.Group()
user_interface = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# adding sprite objects to groups --------------------------------------------------------------------------------------
npcs.add(npc_garan, npc_maurelle, npc_guard)
enemies.add(snake_1, snake_2, snake_3, snake_4, ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)
trees.add(pine_tree_1, pine_tree_2, pine_tree_3)
buildings.add(amuna_inn, amuna_shop, amuna_academia)

user_interface.add(buy_button, sell_button, leave_button, character_button, journal_button, inventory_button,
                   attack_button, skill_button, run_button, player_status, message_box, status_bar_backdrop)

# all environment sprites for collision detection ----------------------------------------------------------------------
environment_objects.add(trees, buildings)

# adding all sprites to game screen
all_sprites.add(npcs, enemies, trees, buildings)

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
# condition to check if enemy has just been defeated so that the message box doesn't instantly clear and shows updates
loot_update = False
# condition to check if player has started combat encounter with enemy to clear message box (before adding combat text)
encounter_started = False

# what zone the player is in, used for player update and map boundaries
zone_seldon = True
zone_korlok = False
zone_eldream = False
zone_marrow = False

# list to contain clicked UI elements for display
display_elements = []
# list to contain current player items for display
player_items = []

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

    if player.alive_status:

        # clear loot update after some time has passed (ab 3 seconds)
        if pygame.time.get_ticks() % 180 == 0:
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
        text_rupee_rect.center = (975, 672)
        screen.blit(text_rupee_surf, text_rupee_rect)

        # get current player district and create surf and rectangle to blit to screen
        text_zone_surf = font.render(str(player.current_zone), True, "black", "light yellow")
        text_zone_rect = text_zone_surf.get_rect()
        text_zone_rect.center = (865, 672)
        screen.blit(text_zone_surf, text_zone_rect)

        # get current player district and create surf and rectangle to blit to screen
        text_level_surf = font.render(str(player.level), True, "black", "light yellow")
        text_level_rect = text_level_surf.get_rect()
        text_level_rect.center = (760, 672)
        screen.blit(text_level_surf, text_level_rect)

        # current info text, first line
        text_info_surf_1 = font.render(info_text_1, True, "black", "light yellow")
        text_combat_info_rect_1 = text_info_surf_1.get_rect()
        text_combat_info_rect_1.center = (145, 690)
        screen.blit(text_info_surf_1, text_combat_info_rect_1)

        # current info text, second line
        text_info_surf_2 = font.render(info_text_2, True, "black", "light yellow")
        text_combat_info_rect_2 = text_info_surf_2.get_rect()
        text_combat_info_rect_2.center = (145, 710)
        screen.blit(text_info_surf_2, text_combat_info_rect_2)

        # current info text, third line
        text_info_surf_3 = font.render(info_text_3, True, "black", "light yellow")
        text_combat_info_rect_3 = text_info_surf_3.get_rect()
        text_combat_info_rect_3.center = (145, 730)
        screen.blit(text_info_surf_3, text_combat_info_rect_3)

        # current info text, fourth line
        text_info_surf_4 = font.render(info_text_4, True, "black", "light yellow")
        text_combat_info_rect_4 = text_info_surf_4.get_rect()
        text_combat_info_rect_4.center = (145, 750)
        screen.blit(text_info_surf_4, text_combat_info_rect_4)

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

            # if something was clicked on screen by mouse cursor, get its position and see what sprite it collided with
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # if mouse cursor collided with inventory button when player clicked
                if inventory_button.rect.collidepoint(pos):

                    if not encounter_started:

                        # if user clicks inventory button again, set condition to false which will hide inventory window
                        if inventory_clicked:
                            inventory_clicked = False

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

                                inventory_counter = 0
                                # go through player items and assign inventory slots (coordinates) to them
                                for item in player.items:
                                    if item.name == "shiny rock":
                                        item.update(first_coord, second_coord, "art/item_art/shiny_rock.png")
                                        player_items.append(item)
                                        inventory_counter += 1
                                    if item.name == "bone dust":
                                        item.update(first_coord, second_coord, "art/item_art/bone_dust.png")
                                        player_items.append(item)
                                        inventory_counter += 1
                                    if item.name == "health potion":
                                        item.update(first_coord, second_coord, "art/item_art/health_potion.png")
                                        player_items.append(item)
                                        inventory_counter += 1
                                    if item.name == "energy potion":
                                        item.update(first_coord, second_coord, "art/item_art/energy_potion.png")
                                        player_items.append(item)
                                        inventory_counter += 1

                                    # add 75 to the items x-coordinate value so the next item will be added to next slot
                                    first_coord += 60

                                    # add 60 to items y coordinate value if the first row of (4) slots has been filled
                                    # reset first coordinate and counter to start in the leftmost slot again
                                    if inventory_counter > 3:
                                        second_coord += 60
                                        first_coord = 800
                                        inventory_counter = 0

            elif event.type == QUIT:
                exit()

            # ----------------------------------------------------------------------------------------------------------
            # if inventory has been clicked and inventory window is open, get item within inventory window that was
            # clicked and use the item based on its name attribute. health potion heals, energy potion energizes, etc
            if inventory_clicked:
                inventory_item = inventory_event_item(event)

                try:
                    if inventory_item.__getattribute__("name") == "health potion":
                        if player.health == 100:
                            info_text_1 = "You're already at full health."
                            info_text_2 = ""

                        else:
                            player.health = player.health + 25
                            # if health potion heals over 100 hp, just set to 100 (max health)
                            if player.health > 100:
                                player.health = 100
                            info_text_1 = "The potion heals you for 25 hp."
                            info_text_2 = ""

                            player_items.remove(inventory_item)
                            player.items.remove(inventory_item)

                    if inventory_item.__getattribute__("name") == "energy potion":
                        if player.energy == 100:
                            info_text_1 = "You're already at full energy."
                            info_text_2 = ""

                        else:
                            player.energy = player.energy + 25
                            # if energy potion energizes over 100 hp, just set to 100 (max energy)
                            if player.energy > 100:
                                player.energy = 100
                            info_text_1 = "The potion energizes you for 25 en."
                            player_items.remove(inventory_item)
                            player.items.remove(inventory_item)

                    if inventory_item.__getattribute__("name") == "shiny rock":
                        info_text_1 = "Oh shiny. Maybe you can sell it?"
                        info_text_2 = ""

                    if inventory_item.__getattribute__("name") == "bone dust":
                        info_text_1 = "Dusty. Maybe you can sell it?"
                        info_text_2 = ""

                except AttributeError:
                    pass

            # ----------------------------------------------------------------------------------------------------------
            # if player collides with enemy sprite, doesn't have combat cooldown,
            # and chooses to interact with it then get event from button press and perform action
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
                        # ----------------------------------------------------------------------------------------------

                        # enter combat scenario and attack enemy. attack_scenario will return all info in form of list
                        if combat_button == "attack":

                            # update player character sprite for combat animation
                            stan_battle_sprite.update("art/character_art/player_character/default/battle/"
                                                      "stan_battle_attacking.png")

                            # update to attacking sprite surface for combat animation
                            if enemy.kind == "snake":
                                snake_battle_sprite.update("art/enemy_art/battle/snake_battle_attacking.png")

                            if enemy.kind == "ghoul":
                                ghoul_battle_sprite.update("art/enemy_art/battle/ghoul_battle_attacking.png")

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

                            if combat_events["item dropped"] != "No" and combat_events["enemy defeated"]:
                                info_text_1 = str(combat_events["item dropped"])

                            if combat_events["experience gained"] != 0 and combat_events["enemy defeated"]:
                                info_text_2 = str(combat_events["experience gained"])

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
            # ----------------------------------------------------------------------------------------------------------
            building = pygame.sprite.spritecollideany(player, buildings)
            if building:
                if interacted:

                    # if player has just started shop scenario, clear message box
                    if not encounter_started:
                        info_text_1 = ""
                        info_text_2 = ""
                        info_text_3 = ""
                        info_text_4 = ""
                        encounter_started = True

                    # get which button player pressed during shop scenario (buy, sell or leave)
                    shop_button = shop_event_button(event)

                    if shop_button == "buy":
                        print("you clicked buy.")

                    if shop_button == "sell":
                        print("you clicked sell.")

                    # if player chooses to leave shop, set conditions to allow normal gameplay loop
                    if shop_button == "leave":
                        movement_able = True
                        interacted = False
                        loot_update = True
                        encounter_started = False

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
        move_this_snake = random.choice([snake_1, snake_2, snake_3, snake_4])
        move_this_ghoul = random.choice([ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4])

        # move snakes in random direction within boundaries every 20 fps
        if movement_able:
            if pygame.time.get_ticks() % 20 == 0:
                move_this_snake.update([50, 300], [200, 300], direction_horizontal, direction_vertical)
                move_this_ghoul.update([650, 900], [200, 300], direction_horizontal, direction_vertical)

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
                    info_text_2 = ""
                    info_text_3 = ""
                    info_text_4 = ""

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
                    # if enemy is snake in seldon zone, chose snake sprite and seldon backdrop
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
                        # draw message box text to screen, updated during combat scenario
                        screen.blit(text_info_surf_1, text_combat_info_rect_1)
                        screen.blit(text_info_surf_2, text_combat_info_rect_2)
                        screen.blit(text_info_surf_3, text_combat_info_rect_3)
                        screen.blit(text_info_surf_4, text_combat_info_rect_4)

            else:
                # don't show if player has recently defeated enemy, so that it doesn't overwrite loot and xp info
                if not loot_update:
                    # lets player know if they are in range of enemy they can press f to attack it
                    info_text_1 = "Press 'F' key to enter building."
                    info_text_2 = ""
                    info_text_3 = ""
                    info_text_4 = ""

        # combat didn't happen this iteration, reset sprites to default surface image
        if not combat_happened:
            combat_cooldown = False
            stan_battle_sprite.update("art/character_art/player_character/default/battle/stan_battle.png")
            snake_battle_sprite.update("art/enemy_art/battle/snake_battle.png")
            ghoul_battle_sprite.update("art/enemy_art/battle/ghoul_battle.png")

            # flip to display ------------------------------------------------------------------------------------------
            pygame.display.flip()

            # ----------------------------------------------------------------------------------------------------------
            # 60 frames per second game rate
            clock.tick(60)

        # combat happened this turn, update sprites for battle and apply short cooldown to attack again
        if combat_happened:
            combat_cooldown = True
            stan_battle_sprite.update("art/character_art/player_character/default/battle/stan_battle_attacking.png")
            snake_battle_sprite.update("art/enemy_art/battle/snake_battle_attacking.png")
            ghoul_battle_sprite.update("art/enemy_art/battle/ghoul_battle_attacking.png")

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
                    player.pos = vec((435, 700))
                    player.health = 50
                    player.energy = 50
                    player.experience = 0
                    for enemy in enemies:
                        enemy.health = 100
                    player.alive_status = True

            elif event.type == QUIT:
                exit()

        pygame.display.flip()

# we can stop and quit the mixer
# pygame.mixer.music.stop()
# pygame.mixer.quit()
