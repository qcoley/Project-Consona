import pygame
import random

from pygame.locals import (RLEACCEL, K_w, K_s, K_a, K_d, K_ESCAPE, KEYDOWN, QUIT, )

# Define constants for the screen width and height
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

pygame.display.set_caption("RPG-Lite")


# Define the Player object extending pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("character_art/stan.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(70, 700))

    # move the character sprite based on key presses
    def update(self, pressed_keyes):

        if pressed_keys[K_w]:
            if pygame.sprite.spritecollideany(player, environment_objects):
                self.rect.move_ip(0, 10)

            self.rect.move_ip(0, -2)

        if pressed_keys[K_s]:
            if pygame.sprite.spritecollideany(player, environment_objects):
                self.rect.move_ip(0, -2)

            self.rect.move_ip(0, 2)

        if pressed_keys[K_a]:
            if pygame.sprite.spritecollideany(player, environment_objects):
                self.rect.move_ip(4, 0)

            self.rect.move_ip(-2, 0)

        if pressed_keys[K_d]:
            if pygame.sprite.spritecollideany(player, environment_objects):
                self.rect.move_ip(-4, 0)

            self.rect.move_ip(2, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0

        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class NPC(pygame.sprite.Sprite):

    def __init__(self, name, gender, race, role, dialog, quest, quest_description, x_coordinate, y_coordinate,
                 alive_status, quest_complete, items, gift, image, color):
        super(NPC, self).__init__()

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

        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(color, RLEACCEL)

        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))


# Define the enemy object extending pygame.sprite.Sprite
class Enemy(pygame.sprite.Sprite):

    def __init__(self, kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image, color):
        super(Enemy, self).__init__()

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


class Water(pygame.sprite.Sprite):

    def __init__(self, name, model, x_coordinate, y_coordinate, image, color):
        super(Water, self).__init__()

        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

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


# ----------------------------------------------------------------------------------------------------------------------
# gameplay functions ---------------------------------------------------------------------------------------------------


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
seldon_district_bg = pygame.image.load("background_textures/seldon_district.png")

pygame.mixer.init()
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

# NPC: name, gender, race, role, dialog, quest, quest_description, x_coordinate, y_coordinate,
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
                "trouble. ", 225, 550, True, False, ["Items to be added for thief steal"], False,
                "character_art/NPCs/garan.png", (255, 255, 255))

npc_maurelle = NPC("Village Matron Maurelle", "female", "amuna", "mage", "We need help!", "Village Repairs",
                   "You there! I don't know who you are, or why you're here, but we could \nreally use your help!"
                   "\n\nThe beast Dreth has occupied our former capital Castle, on the other side of the walls "
                   "\nto the east, and our numbers have been spread thin trying to repel its minions and contain "
                   "the \ndamage they've inflicted. \n\nOur best fighters have been sent in a combined Vanguard with "
                   "the other districts to try and \nattack the beast directly, but its left us vulnerable here. "
                   "The most recent wave of attacks from\nthe castle has left several damages to our village, "
                   "and if you are able, please gather\nresources and bring them to me to distribute to the "
                   "villagers conducting the repairs and \nfortifications. \n\nYou can gather some lumber from the "
                   "trees just west of here. Nera bless you. ", 625, 500, True, False,
                   ["Items to be added for thief steal"], False,
                   "character_art/NPCs/maurelle.png", (255, 255, 255))

npc_guard = NPC("Guard", "male", "amuna", "fighter", "Another day.", "Ghoulish Glee",
                "You need to cross the bridge to get to the Korlok District, you say? \n\nOrdinarily"
                " I would have no issue granting you passage, however the gates are barred tight \n"
                "due to the recent wave of Ghoul Minions from across the wall. \n\nI cannot leave my post and"
                " leave the bridge unguarded, but if you could \ntake care of the remaining ghouls I"
                " will signal to unbar the gates and allow you passage \nto the other side. \n\nThe"
                " ghouls were last spotted just east of here, nearby the northern Castle wall ramparts! ", 475, 140,
                True,
                False, ["Items to be added for thief steal"], False,
                "character_art/NPCs/guard.png", (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# Enemy: kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image, color --------------------
snake_1 = Enemy("snake", 100, 100, 1, 100, 150, True, "shiny rock", "enemy_art/snake.png", (255, 255, 255))
snake_2 = Enemy("snake", 100, 100, 1, 260, 170, True, "shiny rock", "enemy_art/snake.png", (255, 255, 255))
snake_3 = Enemy("snake", 100, 100, 1, 100, 250, True, "shiny rock", "enemy_art/snake.png", (255, 255, 255))
snake_4 = Enemy("snake", 100, 100, 1, 260, 270, True, "shiny rock", "enemy_art/snake.png", (255, 255, 255))

ghoul_low_1 = Enemy("ghoul", 100, 100, 4, 675, 200, True, "bone dust", "enemy_art/ghoul.png", (255, 255, 255))
ghoul_low_2 = Enemy("ghoul", 100, 100, 5, 800, 150, True, "bone dust", "enemy_art/ghoul.png", (255, 255, 255))
ghoul_low_3 = Enemy("ghoul", 100, 100, 3, 760, 260, True, "bone dust", "enemy_art/ghoul.png", (255, 255, 255))
ghoul_low_4 = Enemy("ghoul", 100, 100, 4, 875, 225, True, "bone dust", "enemy_art/ghoul.png", (255, 255, 255))

# Tree: name, model, x_coordinate, y_coordinate, gathered, image, color ------------------------------------------------
pine_tree_1 = Tree("pine tree 1", "pine tree", 80, 570, False, "environment_art/pine_tree.png", (255, 255, 255))
pine_tree_2 = Tree("pine tree 2", "pine tree", 180, 420, False, "environment_art/pine_tree.png", (255, 255, 255))
pine_tree_4 = Tree("pine tree 4", "pine tree", 280, 660, False, "environment_art/pine_tree.png", (255, 255, 255))
pine_tree_5 = Tree("pine tree 5", "pine tree", 380, 480, False, "environment_art/pine_tree.png", (255, 255, 255))

# Water: name, model, x_coordinate, y_coordinate, image, color ---------------------------------------------------------
rohir_river_1 = Water("rohir river 1", "rohir river", 75, 50, "environment_art/rohir_river.png", (255, 255, 255))
rohir_river_2 = Water("rohir river 2", "rohir river", 225, 50, "environment_art/rohir_river.png", (255, 255, 255))
rohir_river_3 = Water("rohir river 3", "rohir river", 375, 50, "environment_art/rohir_river.png", (255, 255, 255))
rohir_river_4 = Water("rohir river 4", "rohir river", 675, 50, "environment_art/rohir_river.png", (255, 255, 255))
rohir_river_5 = Water("rohir river 5", "rohir river", 825, 50, "environment_art/rohir_river.png", (255, 255, 255))
rohir_river_6 = Water("rohir river 5", "rohir river", 975, 50, "environment_art/rohir_river.png", (255, 255, 255))

# Buildings: name, model, x_coordinate, y_coordinate, image, color -----------------------------------------------------
rohir_river_gate = Building("rohir river gate", "river gate", 525, 50, "environment_art/rohir_gate_bridge.png",
                            (255, 255, 255))

castle_wall_1 = Building("castle wall 1", "castle wall", 975, 695, "environment_art/castle_wall.png", (255, 255, 255))
castle_wall_2 = Building("castle wall 2", "castle wall", 975, 550, "environment_art/castle_wall.png", (255, 255, 255))
castle_wall_3 = Building("castle wall 3", "castle wall", 975, 400, "environment_art/castle_wall.png", (255, 255, 255))
castle_wall_4 = Building("castle wall 4", "castle wall", 975, 250, "environment_art/castle_wall.png", (255, 255, 255))
castle_wall_5 = Building("castle wall 5", "castle wall", 975, 175, "environment_art/castle_wall.png", (255, 255, 255))

amuna_inn = Building("amuna inn", "amuna building", 650, 675, "environment_art/amuna_building.png", (255, 255, 255))
amuna_shop = Building("amuna shop", "amuna building", 720, 450, "environment_art/amuna_building.png", (255, 255, 255))
amuna_academia = Building("amuna academia", "amuna building", 850, 595, "environment_art/amuna_building.png",
                          (255, 255, 255))

# ----------------------------------------------------------------------------------------------------------------------
# groups for sprites ---------------------------------------------------------------------------------------------------
npcs = pygame.sprite.Group()
enemies = pygame.sprite.Group()
trees = pygame.sprite.Group()
water = pygame.sprite.Group()
buildings = pygame.sprite.Group()
environment_objects = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# adding sprite objects to groups
npcs.add(npc_garan, npc_maurelle, npc_guard)
enemies.add(snake_1, snake_2, snake_3, snake_4, ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)
trees.add(pine_tree_1, pine_tree_2, pine_tree_4, pine_tree_5)
water.add(rohir_river_1, rohir_river_2, rohir_river_3, rohir_river_4, rohir_river_5, rohir_river_6)
buildings.add(rohir_river_gate, amuna_inn, castle_wall_1, castle_wall_2, castle_wall_3, castle_wall_4, castle_wall_5,
              amuna_shop, amuna_academia)

# all environment sprites for collision detection
environment_objects.add(trees, water, buildings)

# adding all sprites to game screen
all_sprites.add(player, npcs, enemies, trees, water, buildings)

# pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
# pygame.mixer.music.play(loops=-1)

# move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
# move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
# collision_sound = pygame.mixer.Sound("Collision.ogg")

# Set the base volume for all sounds
# move_up_sound.set_volume(0.5)
# move_down_sound.set_volume(0.5)
# collision_sound.set_volume(0.5)


# ----------------------------------------------------------------------------------------------------------------------
# Variable to keep our main loop running -------------------------------------------------------------------------------
running = True

# Our main loop
while running:

    enemy_switch = 1

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # choose random directions and random enemy to move that direction
    direction_horizontal = random.choice(["left", "right"])
    direction_vertical = random.choice(["up", "down"])
    move_this_snake = random.choice([snake_1, snake_2, snake_3, snake_4])
    move_this_ghoul = random.choice([ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4])

    # move snakes in random direction within boundaries every 8 fps
    if pygame.time.get_ticks() % 8 == 0:
        move_this_snake.update([50, 300], [150, 300], direction_horizontal, direction_vertical)
        move_this_ghoul.update([650, 900], [150, 300], direction_horizontal, direction_vertical)

    # draw screen 1 background
    screen.blit(seldon_district_bg, (0, 0))

    # draw sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # check enemy collision with the player
    if pygame.sprite.spritecollideany(player, enemies):
        print("lol")

    # flip to display
    pygame.display.flip()

    # 30 frames per second game rate
    clock.tick(30)

# we can stop and quit the mixer
pygame.mixer.music.stop()
pygame.mixer.quit()
