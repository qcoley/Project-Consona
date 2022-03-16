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
                 color):
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
    # get the all the stuff that happened in combat and return it to main loop via dictionary keys and values
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


# gets current player health and updates hp bar image on screen according to the health value from 0-100
def health_bar_update(character):
    if character.health == 100:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_full.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 99:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_99.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 98:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_98.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 97:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_97.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 96:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_96.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 95:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_95.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 94:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_94.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 93:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_93.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 92:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_92.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 91:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_91.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 90:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_90.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 89:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_89.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 88:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_88.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 87:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_87.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 86:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_86.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 85:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_85.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 84:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_84.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 83:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_83.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 82:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_82.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 81:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_81.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 80:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_80.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 79:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_79.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 78:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_78.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 77:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_77.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 76:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_76.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 75:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_75.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 74:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_74.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 73:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_73.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 72:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_72.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 71:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_71.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 70:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_70.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 69:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_69.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 68:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_68.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 67:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_67.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 66:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_66.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 65:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_65.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 64:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_64.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 63:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_63.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 62:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_62.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 61:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_61.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 60:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_60.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 59:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_59.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 58:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_58.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 57:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_57.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 56:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_56.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 55:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_55.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 54:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_54.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 53:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_53.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 52:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_52.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 51:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_51.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 50:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_50.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 49:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_49.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 48:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_48.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 47:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_47.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 46:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_46.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 45:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_45.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 44:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_44.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 43:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_43.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 42:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_42.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 41:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_41.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 40:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_40.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 39:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_39.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 38:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_38.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 37:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_37.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 36:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_36.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 35:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_35.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 34:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_34.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 33:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_33.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 32:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_32.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 31:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_31.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 30:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_30.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 29:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_29.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 28:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_28.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 27:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_27.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 26:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_26.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 25:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_25.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 24:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_24.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 23:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_23.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 22:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_22.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 21:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_21.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 20:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_20.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 19:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_19.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 18:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_18.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 17:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_17.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 16:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_16.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 15:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_15.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 14:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_14.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 13:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_13.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 12:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_12.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 11:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_11.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 10:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_10.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 9:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_9.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 8:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_8.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 7:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_7.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 6:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_6.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 5:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_5.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 4:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_4.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 3:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_3.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 2:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_2.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 1:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_1.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 0:
        hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_0.png").convert()
        hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)


def energy_bar_update(character):
    if character.energy == 100:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_full.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 99:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_99.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 98:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_98.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 97:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_97.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 96:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_96.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 95:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_95.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 94:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_94.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 93:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_93.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 92:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_92.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 91:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_91.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 90:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_90.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 89:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_89.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 88:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_88.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 87:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_87.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 86:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_86.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 85:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_85.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 84:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_84.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 83:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_83.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 82:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_82.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 81:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_81.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 80:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_80.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 79:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_79.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 78:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_78.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 77:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_77.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 76:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_76.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 75:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_75.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 74:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_74.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 73:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_73.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 72:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_72.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 71:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_71.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 70:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_70.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 69:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_69.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 68:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_68.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 67:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_67.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 66:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_66.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 65:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_65.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 64:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_64.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 63:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_63.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 62:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_62.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 61:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_61.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 60:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_60.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 59:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_59.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 58:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_58.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 57:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_57.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 56:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_56.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 55:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_55.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 54:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_54.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 53:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_53.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 52:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_52.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 51:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_51.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 50:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_50.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 49:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_49.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 48:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_48.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 47:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_47.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 46:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_46.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 45:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_45.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 44:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_44.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 43:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_43.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 42:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_42.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 41:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_41.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 40:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_40.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 39:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_39.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 38:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_38.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 37:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_37.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 36:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_36.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 35:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_35.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 34:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_34.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 33:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_33.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 32:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_32.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 31:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_31.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 30:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_30.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 29:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_29.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 28:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_28.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 27:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_27.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 26:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_26.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 25:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_25.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 24:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_24.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 23:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_23.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 22:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_22.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 21:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_21.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 20:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_20.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 19:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_19.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 18:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_18.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 17:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_17.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 16:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_16.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 15:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_15.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 14:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_14.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 13:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_13.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 12:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_12.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 11:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_11.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 10:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_10.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 9:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_9.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 8:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_8.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 7:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_7.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 6:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_6.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 5:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_5.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 4:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_4.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 3:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_3.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 2:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_2.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 1:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_1.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.energy == 0:
        en_bar.surf = pygame.image.load("art/ui_elements/bars/energy/en_bar_0.png").convert()
        en_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)


def experience_bar_update(character):
    if character.experience == 100:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_full.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 99:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_99.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 98:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_98.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 97:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_97.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 96:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_96.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 95:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_95.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 94:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_94.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 93:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_93.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 92:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_92.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 91:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_91.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 90:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_90.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 89:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_89.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 88:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_88.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 87:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_87.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 86:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_86.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 85:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_85.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 84:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_84.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 83:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_83.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 82:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_82.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 81:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_81.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 80:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_80.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 79:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_79.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 78:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_78.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 77:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_77.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 76:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_76.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 75:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_75.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 74:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_74.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 73:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_73.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 72:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_72.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 71:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_71.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 70:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_70.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 69:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_69.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 68:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_68.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 67:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_67.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 66:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_66.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 65:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_65.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 64:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_64.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 63:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_63.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 62:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_62.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 61:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_61.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 60:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_60.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 59:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_59.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 58:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_58.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 57:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_57.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 56:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_56.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 55:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_55.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 54:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_54.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 53:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_53.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 52:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_52.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 51:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_51.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 50:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_50.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 49:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_49.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 48:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_48.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 47:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_47.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 46:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_46.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 45:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_45.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 44:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_44.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 43:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_43.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 42:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_42.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 41:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_41.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 40:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_40.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 39:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_39.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 38:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_38.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 37:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_37.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 36:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_36.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 35:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_35.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 34:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_34.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 33:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_33.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 32:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_32.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 31:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_31.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 30:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_30.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 29:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_29.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 28:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_28.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 27:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_27.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 26:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_26.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 25:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_25.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 24:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_24.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 23:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_23.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 22:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_22.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 21:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_21.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 20:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_20.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 19:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_19.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 18:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_18.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 17:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_17.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 16:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_16.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 15:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_15.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 14:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_14.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 13:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_13.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 12:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_12.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 11:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_11.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 10:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_10.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 9:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_9.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 8:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_8.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 7:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_7.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 6:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_6.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 5:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_5.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 4:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_4.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 3:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_3.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 2:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_2.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 1:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_1.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.experience == 0:
        xp_bar.surf = pygame.image.load("art/ui_elements/bars/xp/xp_bar_0.png").convert()
        xp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)


def health_bar_update_enemy(character):
    if character.health == 100:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_full.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 99:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_99.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 98:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_98.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 97:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_97.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 96:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_96.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 95:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_95.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 94:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_94.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 93:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_93.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 92:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_92.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 91:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_91.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 90:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_90.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 89:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_89.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 88:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_88.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 87:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_87.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 86:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_86.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 85:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_85.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 84:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_84.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 83:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_83.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 82:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_82.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 81:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_81.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 80:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_80.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 79:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_79.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 78:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_78.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 77:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_77.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 76:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_76.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 75:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_75.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 74:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_74.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 73:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_73.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 72:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_72.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 71:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_71.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 70:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_70.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 69:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_69.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 68:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_68.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 67:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_67.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 66:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_66.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 65:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_65.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 64:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_64.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 63:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_63.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 62:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_62.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 61:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_61.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 60:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_60.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 59:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_59.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 58:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_58.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 57:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_57.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 56:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_56.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 55:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_55.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 54:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_54.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 53:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_53.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 52:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_52.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 51:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_51.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 50:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_50.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 49:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_49.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 48:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_48.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 47:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_47.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 46:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_46.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 45:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_45.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 44:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_44.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 43:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_43.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 42:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_42.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 41:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_41.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 40:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_40.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 39:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_39.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 38:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_38.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 37:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_37.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 36:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_36.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 35:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_35.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 34:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_34.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 33:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_33.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 32:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_32.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 31:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_31.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 30:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_30.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 29:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_29.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 28:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_28.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 27:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_27.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 26:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_26.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 25:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_25.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 24:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_24.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 23:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_23.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 22:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_22.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 21:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_21.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 20:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_20.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 19:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_19.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 18:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_18.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 17:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_17.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 16:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_16.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 15:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_15.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 14:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_14.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 13:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_13.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 12:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_12.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 11:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_11.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 10:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_10.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 9:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_9.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 8:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_8.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 7:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_7.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 6:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_6.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 5:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_5.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 4:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_4.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 3:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_3.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 2:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_2.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 1:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_1.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)
    if character.health == 0:
        enemy_hp_bar.surf = pygame.image.load("art/ui_elements/bars/health/hp_bar_0.png").convert()
        enemy_hp_bar.surf.set_colorkey((255, 255, 255), RLEACCEL)


# ----------------------------------------------------------------------------------------------------------------------
# getting event based on user click related to combat scenario (attack, skill and run buttons).
def combat_event_button(combat_event):
    if combat_event.type == pygame.MOUSEBUTTONUP:
        mouse_pos = pygame.mouse.get_pos()

        # get a list of all sprites that are under the mouse cursor
        clicked_combat_element = [element for element in user_interface if element.rect.collidepoint(mouse_pos)]

        # try to get UI element user clicked on and set condition to True if corresponding button is clicked
        try:
            if clicked_combat_element[0].__getattribute__("name") == "attack button":
                return "attack"

            if clicked_combat_element[0].__getattribute__("name") == "skill button":
                return "skill"

            if clicked_combat_element[0].__getattribute__("name") == "run button":
                return "run"

        except IndexError:
            pass


# ----------------------------------------------------------------------------------------------------------------------
# getting event based on user click related to combat scenario (attack, skill and run buttons).
def inventory_event_item(inventory_event):
    if inventory_event.type == pygame.MOUSEBUTTONUP:
        mouse_pos = pygame.mouse.get_pos()

        # get a list of all sprites that are under the mouse cursor
        clicked_combat_element = [element for element in player_items if element.rect.collidepoint(mouse_pos)]

        # try to get UI element user clicked on and set condition to True if corresponding button is clicked
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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# background textures --------------------------------------------------------------------------------------------------
seldon_district_bg = pygame.image.load("art/environment_art/background_textures/seldon_district.png")
seldon_district_battle = pygame.image.load("art/environment_art/background_textures/seldon_battle_screen.png")
seldon_district_shop = pygame.image.load("art/environment_art/background_textures/seldon_shop.png")
game_over_screen = pygame.image.load("art/screens/game_over.png")

# creating objects from defined classes --------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# display notifications to user (shown, x_coordinate, y_coordinate, image, color) --------------------------------------
greeting = Notification("greeting", False, 500, 325, "art/ui_elements/notifications/welcome.png", (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# inventory items ------------------------------------------------------------------------------------------------------
health_potion = Item("health potion", "potion", 200, 200, "art/item_art/health_potion.png", (255, 255, 255))
energy_potion = Item("energy potion", "potion", 200, 200, "art/item_art/energy_potion.png", (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# default player character ---------------------------------------------------------------------------------------------
player = Player("Player", "male", "amuna", "mage",  # name, gender, race, role
                [health_potion, energy_potion],  # inventory
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
                "trouble. ", 230, 470, True, False, ["Items to be added for thief steal"], False,
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
                   "trees just west of here. Nera bless you. ", 755, 525, True, False,
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
# enemies: kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image, color ------------------
snake_1 = Enemy("Snake", "snake", 100, 100, 1, 100, 150, True, Item("shiny rock", "rock", 200, 200,
                                                                    "art/item_art/shiny_rock.png", (255, 255, 255)),
                "art/enemy_art/snake.png", (255, 255, 255))
snake_2 = Enemy("Snake", "snake", 100, 100, 2, 260, 170, True, Item("shiny rock", "rock", 200, 200,
                                                                    "art/item_art/shiny_rock.png", (255, 255, 255)),
                "art/enemy_art/snake.png", (255, 255, 255))
snake_3 = Enemy("Snake", "snake", 100, 100, 1, 100, 250, True, Item("shiny rock", "rock", 200, 200,
                                                                    "art/item_art/shiny_rock.png", (255, 255, 255)),
                "art/enemy_art/snake.png", (255, 255, 255))
snake_4 = Enemy("Snake", "snake", 100, 100, 2, 260, 270, True, Item("shiny rock", "rock", 200, 200,
                                                                    "art/item_art/shiny_rock.png", (255, 255, 255)),
                "art/enemy_art/snake.png", (255, 255, 255))

ghoul_low_1 = Enemy("Ghoul", "ghoul", 100, 100, 4, 675, 200, True, Item("bone dust", "dust", 200, 200,
                                                                        "art/item_art/bone_dust.png", (255, 255, 255)),
                    "art/enemy_art/ghoul.png", (255, 255, 255))
ghoul_low_2 = Enemy("Ghoul", "ghoul", 100, 100, 5, 800, 150, True, Item("bone dust", "dust", 200, 200,
                                                                        "art/item_art/bone_dust.png", (255, 255, 255)),
                    "art/enemy_art/ghoul.png", (255, 255, 255))
ghoul_low_3 = Enemy("Ghoul", "ghoul", 100, 100, 3, 760, 260, True, Item("bone dust", "dust", 200, 200,
                                                                        "art/item_art/bone_dust.png", (255, 255, 255)),
                    "art/enemy_art/ghoul.png", (255, 255, 255))
ghoul_low_4 = Enemy("Ghoul", "ghoul", 100, 100, 4, 875, 225, True, Item("bone dust", "dust", 200, 200,
                                                                        "art/item_art/bone_dust.png", (255, 255, 255)),
                    "art/enemy_art/ghoul.png", (255, 255, 255))

# trees: name, model, x_coordinate, y_coordinate, gathered, image, color -----------------------------------------------
pine_tree_1 = Tree("pine tree 1", "pine tree", 80, 475, False, "art/environment_art/pine_tree.png", (255, 255, 255))
pine_tree_2 = Tree("pine tree 4", "pine tree", 260, 660, False, "art/environment_art/pine_tree.png", (255, 255, 255))
pine_tree_3 = Tree("pine tree 5", "pine tree", 380, 400, False, "art/environment_art/pine_tree.png", (255, 255, 255))

# buildings: name, model, x_coordinate, y_coordinate, image, color -----------------------------------------------------
amuna_inn = Building("inn", "amuna building", 600, 625,
                     "art/environment_art/buildings/amuna_building_inn.png",
                     (255, 255, 255))
amuna_shop = Building("shop", "amuna building", 700, 400,
                      "art/environment_art/buildings/amuna_building_shop.png",
                      (255, 255, 255))
amuna_academia = Building("academia", "amuna building", 875, 545,
                          "art/environment_art/buildings/amuna_building_academia.png",
                          (255, 255, 255))

# ui elements: name, x_coordinate, y_coordinate, image, color, update flag ---------------------------------------------
inventory_button = UiElement("inventory button", 960, 730, "art/ui_elements/buttons/inventory.png",
                             (255, 255, 255), False)
character_button = UiElement("character button", 850, 730, "art/ui_elements/buttons/character.png",
                             (255, 255, 255), False)
journal_button = UiElement("journal button", 740, 730, "art/ui_elements/buttons/journal.png",
                           (255, 255, 255), False)

attack_button = UiElement("attack button", 740, 675, "art/ui_elements/buttons/battle_screen/attack.png",
                          (255, 255, 255), False)
skill_button = UiElement("skill button", 850, 675, "art/ui_elements/buttons/battle_screen/skill.png",
                         (255, 255, 255), False)
run_button = UiElement("run button", 960, 675, "art/ui_elements/buttons/battle_screen/run.png",
                       (255, 255, 255), False)

continue_button = UiElement("continue button", 500, 600, "art/ui_elements/buttons/continue_button.png",
                            (255, 255, 255), False)

buy_button = UiElement("buy button", 740, 675, "art/ui_elements/buttons/shop/buy.png",
                       (255, 255, 255), False)
sell_button = UiElement("sell button", 850, 675, "art/ui_elements/buttons/shop/sell.png",
                        (255, 255, 255), False)
leave_button = UiElement("leave button", 960, 675, "art/ui_elements/buttons/shop/leave.png",
                         (255, 255, 255), False)

player_status = UiElement("player status", 850, 675, "art/ui_elements/status/player.png", (255, 255, 255), False)
enemy_status = UiElement("enemy status", 850, 730, "art/ui_elements/status/enemy.png", (255, 255, 255), False)

hp_bar = UiElement("hp bar", 170, 25, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255), False)
en_bar = UiElement("en bar", 170, 45, "art/ui_elements/bars/energy/en_bar_full.png", (255, 255, 255), False)
xp_bar = UiElement("xp bar", 170, 65, "art/ui_elements/bars/xp/xp_bar_full.png", (255, 255, 255), False)

enemy_hp_bar = UiElement("enemy hp bar", 700, 90, "art/ui_elements/bars/health/hp_bar_full.png", (255, 255, 255), False)

inventory = Inventory([], 890, 525, "art/ui_elements/inventory.png", (255, 255, 255), False)

message_box = UiElement("message_box", 175, 705, "art/ui_elements/message_box.png", (255, 255, 255), False)

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
user_interface.add(inventory_button, character_button, journal_button, attack_button, skill_button, run_button,
                   player_status, message_box)

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

# condition to allow or block player movement (combat or npc interaction)
movement_able = True

# condition for battle sequences so that buttons can't be spam clicked
click_able = True

# condition to check if combat occurred on current game loop iteration to update sprites at end of loop
combat_happened = False

# condition to check if inventory button is clicked
inventory_clicked = False

# condition to check if a player has chosen to interact with a collided sprite
interacted = False

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

        # update player health, energy and experience bar on each iteration of main loop -------------------------------
        health_bar_update(player)
        energy_bar_update(player)
        experience_bar_update(player)
        screen.blit(hp_bar.surf, hp_bar.rect)
        screen.blit(en_bar.surf, en_bar.rect)
        screen.blit(xp_bar.surf, xp_bar.rect)

        # text updates to screen for things like current zone, rupee count, combat text, etc. --------------------------
        # --------------------------------------------------------------------------------------------------------------
        # get current player rupee count and create surf and rectangle to blit to screen
        text_rupee_surf = font.render(str(player.rupees), True, "black", "light yellow")
        text_rupee_rect = text_rupee_surf.get_rect()
        text_rupee_rect.center = (975, 677)
        screen.blit(text_rupee_surf, text_rupee_rect)

        # get current player district and create surf and rectangle to blit to screen
        text_zone_surf = font.render(str(player.current_zone), True, "black", "light yellow")
        text_zone_rect = text_zone_surf.get_rect()
        text_zone_rect.center = (865, 677)
        screen.blit(text_zone_surf, text_zone_rect)

        # get current player district and create surf and rectangle to blit to screen
        text_level_surf = font.render(str(player.level), True, "black", "light yellow")
        text_level_rect = text_level_surf.get_rect()
        text_level_rect.center = (760, 677)
        screen.blit(text_level_surf, text_level_rect)

        # current combat text, first line
        text_combat_info_surf_1 = font.render(info_text_1, True, "black", "light yellow")
        text_combat_info_rect_1 = text_combat_info_surf_1.get_rect()
        text_combat_info_rect_1.center = (140, 680)
        screen.blit(text_combat_info_surf_1, text_combat_info_rect_1)

        # current combat text, second line
        text_combat_info_surf_2 = font.render(info_text_2, True, "black", "light yellow")
        text_combat_info_rect_2 = text_combat_info_surf_2.get_rect()
        text_combat_info_rect_2.center = (140, 700)
        screen.blit(text_combat_info_surf_2, text_combat_info_rect_2)

        # current combat text, third line
        text_combat_info_surf_3 = font.render(info_text_3, True, "black", "light yellow")
        text_combat_info_rect_3 = text_combat_info_surf_3.get_rect()
        text_combat_info_rect_3.center = (140, 720)
        screen.blit(text_combat_info_surf_3, text_combat_info_rect_3)

        # current combat text, fourth line
        text_combat_info_surf_4 = font.render(info_text_4, True, "black", "light yellow")
        text_combat_info_rect_4 = text_combat_info_surf_4.get_rect()
        text_combat_info_rect_4.center = (140, 740)
        screen.blit(text_combat_info_surf_4, text_combat_info_rect_4)

        # --------------------------------------------------------------------------------------------------------------
        # user input events such as key presses or UI interaction
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_f:
                    interacted = True

                if event.key == K_ESCAPE:
                    exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # get a list of all sprites that are under the mouse cursor
                clicked_element = [element for element in user_interface if element.rect.collidepoint(pos)]

                # try to get UI element user clicked on and set condition to True if corresponding button is clicked
                try:
                    if clicked_element[0].__getattribute__("name") == "inventory button":

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
                                second_coord = 440

                                inventory_counter = 0
                                # go through player items and assign inventory slots (coordinates) to them
                                for item in player.items:
                                    if item.name == "shiny rock":
                                        item.update(first_coord, second_coord, "art/item_art/shiny_rock.png")
                                        player_items.append(item)
                                    if item.name == "bone dust":
                                        item.update(first_coord, second_coord, "art/item_art/bone_dust.png")
                                        player_items.append(item)
                                    if item.name == "health potion":
                                        item.update(first_coord, second_coord, "art/item_art/health_potion.png")
                                        player_items.append(item)
                                    if item.name == "energy potion":
                                        item.update(first_coord, second_coord, "art/item_art/energy_potion.png")
                                        player_items.append(item)

                                    # add 75 to the items x-coordinate value so the next item will be added to next slot
                                    first_coord += 60

                                    # add 100 to items y coordinate value if the first row of (4) slots has been filled
                                    inventory_counter += 1
                                    if inventory_counter % 4 == 0:
                                        second_coord += 100

                except IndexError:
                    pass

            elif event.type == QUIT:
                exit()

            # ----------------------------------------------------------------------------------------------------------
            # if inventory has been clicked and inventory window is open, get item within inventory window that was
            # clicked
            if inventory_clicked:
                inventory_item = inventory_event_item(event)

                try:
                    if inventory_item.__getattribute__("name") == "health potion":
                        if player.health == 100:
                            info_text_1 = "You're already at full health."

                        else:
                            player.health = player.health + 25
                            info_text_1 = "The potion heals you for 25 hp."
                            player_items.remove(inventory_item)
                            player.items.remove(inventory_item)

                    if inventory_item.__getattribute__("name") == "energy potion":
                        if player.energy == 100:
                            info_text_1 = "You're already at full energy."

                        else:
                            player.energy = player.energy + 25
                            info_text_1 = "The potion energizes you for 25 ep."
                            player_items.remove(inventory_item)
                            player.items.remove(inventory_item)

                    if inventory_item.__getattribute__("name") == "shiny rock":
                        info_text_1 = "Oh shiny. Maybe you can sell it?"
                        info_text_2 = ""

                    if inventory_item.__getattribute__("name") == "bone dust":
                        info_text_1 = "Dusty. Maybe someone would buy it?"
                        info_text_2 = ""

                except AttributeError:
                    pass

            # ----------------------------------------------------------------------------------------------------------
            # if player is able to perform combat action this turn, get event from button press and perform action
            if click_able:
                combat_button = combat_event_button(event)

                # Info returned from combat scenario function in form of dictionary ------------------------------------
                # "damage done": 0,
                # "damage taken": 0,
                # "item dropped": "",
                # "experience gained": 0,
                # "quest update": "",
                # "enemy defeated": False,
                # "escaped": False
                # ------------------------------------------------------------------------------------------------------

                # enter combat scenario and attack enemy. attack_scenario will return all combat info in form of list
                if combat_button == "attack":
                    stan_battle_sprite.update("art/character_art/player_character/default/battle/"
                                              "stan_battle_attacking.png")

                    enemy = pygame.sprite.spritecollideany(player, enemies)
                    if enemy:

                        if enemy.kind == "snake":
                            snake_battle_sprite.update("art/enemy_art/battle/snake_battle_attacking.png")

                        if enemy.kind == "ghoul":
                            ghoul_battle_sprite.update("art/enemy_art/battle/ghoul_battle_attacking.png")

                        combat_events = attack_scenario(enemy, "attack")
                        combat_happened = True

                        # add all combat scenario happenings from function to message box
                        # if any of the values are currently zero, or no, just return a blank string to message box
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

                        # if player was successful in defeating enemy, combat scenario ends and movement is allowed
                        # set combat happened to false, allowing iteration to continue without delay from combat
                        # animation
                        if combat_events["enemy defeated"]:
                            movement_able = True
                            combat_happened = False
                            interacted = False

                if combat_button == "skill":

                    enemy = pygame.sprite.spritecollideany(player, enemies)
                    if enemy:
                        combat_events = attack_scenario(enemy, "skill")

                        # commented out until skill functions added to prevent game crash
                        """
                        # add all combat scenario happenings from function to message box
                        # if any of the values are currently zero, or no, just return a blank string to message box
                        if combat_events["damage done"] == 0:
                            info_text_1 = ""
                        else:
                            info_text_1 = str(combat_events["damage done"])
    
                        if combat_events["damage taken"] == 0:
                            info_text_2 = ""
                        else:
                            info_text_2 = str(combat_events["damage taken"])
    
                        if combat_events["item dropped"] == "No":
                            info_text_1 = ""
                        else:
                            info_text_1 = str(combat_events["item dropped"])
    
                        if combat_events["experience gained"] == 0:
                            info_text_2 = ""
                        else:
                            info_text_2 = str(combat_events["experience gained"])
    
                        # if player was successful in defeating enemy, combat scenario ends and movement is allowed
                        if combat_events["enemy defeated"]:
                            movement_able = True
                            combat_happened = False
                        """

                # if player chooses run in combat, set their position to determined location which will disengage them
                # from combat scenario and allow them to move again
                if combat_button == "run":

                    enemy = pygame.sprite.spritecollideany(player, enemies)
                    if enemy:
                        combat_events = attack_scenario(enemy, "run")

                        # if combat scenario returns true that player is able to escape enemy, move player to
                        # safe location
                        # to exit the encounter and re-enable movement
                        if combat_events["escaped"]:
                            info_text_1 = str(combat_events["damage done"])
                            movement_able = True
                            interacted = False
                            player.pos = vec((500, 400))

                        else:
                            info_text_1 = str(combat_events["damage done"])

        # get current pressed keys from user and apply zone boundaries depending on current players zone
        pressed_keys = pygame.key.get_pressed()

        # get players current zone status and apply the keys update to movement based on zone boundaries
        # defined in update()
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

        # if greeting message has not been shown yet, add it to display elements to be blit to screen
        if not greeting.shown:
            display_elements.append(greeting)
            greeting.shown = True

        # if greeting has been shown, after a few seconds (based on framerate) remove it from screen
        if greeting.shown:
            if pygame.time.get_ticks() > 3000:
                for notification in display_elements:
                    try:
                        if notification.__getattribute__("name") == "greeting":
                            display_elements.remove(notification)
                    except AttributeError:
                        pass

        # choose random directions and random enemy to move that direction ---------------------------------------------
        direction_horizontal = random.choice(["left", "right"])
        direction_vertical = random.choice(["up", "down"])
        move_this_snake = random.choice([snake_1, snake_2, snake_3, snake_4])
        move_this_ghoul = random.choice([ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4])

        # move snakes in random direction within boundaries every 20 fps
        if movement_able:
            if pygame.time.get_ticks() % 20 == 0:
                move_this_snake.update([50, 250], [200, 300], direction_horizontal, direction_vertical)
                move_this_ghoul.update([650, 850], [200, 300], direction_horizontal, direction_vertical)

        # --------------------------------------------------------------------------------------------------------------
        # player rect collides with an enemy rect ----------------------------------------------------------------------
        enemy = pygame.sprite.spritecollideany(player, enemies)
        if enemy:

            # if player has collided with an enemy but has not yet attacked it
            # doesn't continue to show if interaction has occurred
            if not interacted:
                info_text_1 = "Press 'f' key to attack enemy."

            if interacted:

                # clear press f to attack message once encounter begins
                if info_text_1 == "Press 'f' key to attack enemy.":
                    info_text_1 = ""
                    info_text_2 = ""

                # doesn't allow player to move while in combat
                movement_able = False

                # update enemies health before displaying (blit) combat screen elements
                health_bar_update_enemy(enemy)

                if zone_seldon:

                    # if enemy is snake in seldon zone, push everything to top layer of screen for battle
                    if enemy.__getattribute__("kind") == "snake":
                        screen.blit(seldon_district_battle, (0, 0))
                        screen.blit(stan_battle_sprite.surf, stan_battle_sprite.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(attack_button.surf, attack_button.rect)
                        screen.blit(skill_button.surf, skill_button.rect)
                        screen.blit(run_button.surf, run_button.rect)
                        screen.blit(snake_battle_sprite.surf, snake_battle_sprite.rect)
                        screen.blit(enemy_hp_bar.surf, enemy_hp_bar.rect)
                        screen.blit(enemy_status.surf, enemy_status.rect)
                        screen.blit(message_box.surf, message_box.rect)

                        # get current enemy name and create surf and rectangle to blit to screen
                        text_enemy_name_surf = font.render(str(enemy.__getattribute__("name")), True, "black",
                                                           "light yellow")
                        text_enemy_name_rect = text_enemy_name_surf.get_rect()
                        text_enemy_name_rect.center = (800, 732)
                        screen.blit(text_enemy_name_surf, text_enemy_name_rect)

                        # get current enemy level and create surf and rectangle to blit to screen
                        text_enemy_level_surf = font.render(str(enemy.__getattribute__("level")), True, "black",
                                                            "light yellow")
                        text_enemy_level_rect = text_enemy_level_surf.get_rect()
                        text_enemy_level_rect.center = (910, 732)
                        screen.blit(text_enemy_level_surf, text_enemy_level_rect)

                        # combat info text for message box. initially blank and updated during combat scenario
                        screen.blit(text_combat_info_surf_1, text_combat_info_rect_1)
                        screen.blit(text_combat_info_surf_2, text_combat_info_rect_2)
                        screen.blit(text_combat_info_surf_3, text_combat_info_rect_3)
                        screen.blit(text_combat_info_surf_4, text_combat_info_rect_4)

                    if enemy.__getattribute__("kind") == "ghoul":
                        screen.blit(seldon_district_battle, (0, 0))
                        screen.blit(stan_battle_sprite.surf, stan_battle_sprite.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(attack_button.surf, attack_button.rect)
                        screen.blit(skill_button.surf, skill_button.rect)
                        screen.blit(run_button.surf, run_button.rect)
                        screen.blit(ghoul_battle_sprite.surf, ghoul_battle_sprite.rect)
                        screen.blit(enemy_hp_bar.surf, enemy_hp_bar.rect)
                        screen.blit(enemy_status.surf, enemy_status.rect)
                        screen.blit(message_box.surf, message_box.rect)

                        # get current enemy name and create surf and rectangle to blit to screen
                        text_enemy_name_surf = font.render(str(enemy.__getattribute__("name")), True, "black",
                                                           "light yellow")
                        text_enemy_name_rect = text_enemy_name_surf.get_rect()
                        text_enemy_name_rect.center = (805, 732)
                        screen.blit(text_enemy_name_surf, text_enemy_name_rect)

                        # get current enemy level and create surf and rectangle to blit to screen
                        text_enemy_level_surf = font.render(str(enemy.__getattribute__("level")), True, "black",
                                                            "light yellow")
                        text_enemy_level_rect = text_enemy_level_surf.get_rect()
                        text_enemy_level_rect.center = (910, 732)
                        screen.blit(text_enemy_level_surf, text_enemy_level_rect)

                        # combat info text for message box. initially blank and updated during combat scenario
                        screen.blit(text_combat_info_surf_1, text_combat_info_rect_1)
                        screen.blit(text_combat_info_surf_2, text_combat_info_rect_2)
                        screen.blit(text_combat_info_surf_3, text_combat_info_rect_3)
                        screen.blit(text_combat_info_surf_4, text_combat_info_rect_4)

        # --------------------------------------------------------------------------------------------------------------
        # player rect collides with an enemy rect ----------------------------------------------------------------------
        building = pygame.sprite.spritecollideany(player, buildings)
        if building:

            # if player has collided with a building but has not yet interacted with it
            # doesn't continue to show if interaction has occurred
            if not interacted:
                info_text_1 = "Press 'f' key to enter building."

            if zone_seldon:

                if interacted:

                    # if enemy is snake in seldon zone, push everything to top layer of screen for battle
                    if building.__getattribute__("name") == "shop":
                        # add shop related stuff
                        screen.blit(seldon_district_shop, (0, 0))
                        screen.blit(buy_button.surf, buy_button.rect)
                        screen.blit(sell_button.surf, sell_button.rect)
                        screen.blit(leave_button.surf, leave_button.rect)

                        # reset interacted switch
                        # interacted = False

                    if building.__getattribute__("name") == "inn":
                        # add inn related stuff
                        print("inn")

                        # reset interacted switch
                        interacted = False

        # --------------------------------------------------------------------------------------------------------------
        # if player is not currently in range of a sprite that can be interacted with, clear message box ---------------
        sprite = pygame.sprite.spritecollideany(player, all_sprites)
        if not sprite:
            info_text_1 = ""
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # allow player to click and update sprite to resting when combat didn't happen this turn
        if not combat_happened:
            click_able = True
            stan_battle_sprite.update("art/character_art/player_character/default/battle/stan_battle.png")
            snake_battle_sprite.update("art/enemy_art/battle/snake_battle.png")
            ghoul_battle_sprite.update("art/enemy_art/battle/ghoul_battle.png")

            # flip to display ------------------------------------------------------------------------------------------
            pygame.display.flip()

            # ----------------------------------------------------------------------------------------------------------
            # 60 frames per second game rate
            clock.tick(60)

        # if combat happened this turn, don't allow player to click again immediately and update battle sprite to attack
        if combat_happened:
            click_able = False
            stan_battle_sprite.update("art/character_art/player_character/default/battle/stan_battle_attacking.png")
            snake_battle_sprite.update("art/enemy_art/battle/snake_battle_attacking.png")
            ghoul_battle_sprite.update("art/enemy_art/battle/ghoul_battle_attacking.png")

            # flip to display ------------------------------------------------------------------------------------------
            pygame.display.flip()

            # when combat happens, wait after flipping (updating) display to allow animation time to show
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
        # draw game over screen
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

                # player chooses to continue, reset character experience and half health and energy
                if continue_button.rect.collidepoint(pos):

                    # reset enemy health when player continues
                    for enemy in enemies:
                        enemy.health = 100
                        enemy.energy = 100

                    movement_able = True
                    player.pos = vec((435, 700))
                    player.health = 50
                    player.energy = 50
                    player.experience = 0

                    player.alive_status = True

            elif event.type == QUIT:
                exit()

        pygame.display.flip()

# we can stop and quit the mixer
# pygame.mixer.music.stop()
# pygame.mixer.quit()
