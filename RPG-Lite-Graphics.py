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
        self.surf = pygame.image.load("stan.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(70, 700))

    # Move the sprite based on key presses
    def update(self, pressed_keyes):
        if pressed_keyes[K_w]:
            self.rect.move_ip(0, -2)
            # move_up_sound.play()
        if pressed_keyes[K_s]:
            self.rect.move_ip(0, 2)
            # move_down_sound.play()
        if pressed_keyes[K_a]:
            self.rect.move_ip(-2, 0)
        if pressed_keyes[K_d]:
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
seldon_district_bg = pygame.image.load("seldon_district.png")

pygame.mixer.init()
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

# Enemy: kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image, color

snake_1 = Enemy("snake", 100, 100, 1, 100, 150, True, "shiny rock", "snake.png", (255, 255, 255))
snake_2 = Enemy("snake", 100, 100, 1, 260, 170, True, "shiny rock", "snake.png", (255, 255, 255))
snake_3 = Enemy("snake", 100, 100, 1, 100, 250, True, "shiny rock", "snake.png", (255, 255, 255))
snake_4 = Enemy("snake", 100, 100, 1, 260, 270, True, "shiny rock", "snake.png", (255, 255, 255))

# Tree: name, model, x_coordinate, y_coordinate, gathered, image, color
pine_tree_1 = Tree("pine tree 1", "pine tree", 80, 570, False, "pine_tree.png", (255, 255, 255))
pine_tree_2 = Tree("pine tree 2", "pine tree", 180, 420, False, "pine_tree.png", (255, 255, 255))
pine_tree_4 = Tree("pine tree 4", "pine tree", 280, 660, False, "pine_tree.png", (255, 255, 255))
pine_tree_5 = Tree("pine tree 5", "pine tree", 380, 480, False, "pine_tree.png", (255, 255, 255))

# Water: name, model, x_coordinate, y_coordinate, image, color
rohir_river_1 = Water("rohir river 1", "rohir river", 75, 50, "rohir_river.png", (255, 255, 255))
rohir_river_2 = Water("rohir river 2", "rohir river", 225, 50, "rohir_river.png", (255, 255, 255))
rohir_river_3 = Water("rohir river 3", "rohir river", 375, 50, "rohir_river.png", (255, 255, 255))
rohir_river_4 = Water("rohir river 4", "rohir river", 675, 50, "rohir_river.png", (255, 255, 255))
rohir_river_5 = Water("rohir river 5", "rohir river", 825, 50, "rohir_river.png", (255, 255, 255))
rohir_river_6 = Water("rohir river 5", "rohir river", 975, 50, "rohir_river.png", (255, 255, 255))

# Buildings: name, model, x_coordinate, y_coordinate, image, color
rohir_river_gate = Building("rohir river gate", "river gate", 525, 50, "rohir_gate_bridge.png", (255, 255, 255))

castle_wall_1 = Building("castle wall 1", "castle wall", 975, 695, "castle_wall.png", (255, 255, 255))
castle_wall_2 = Building("castle wall 2", "castle wall", 975, 550, "castle_wall.png", (255, 255, 255))
castle_wall_3 = Building("castle wall 3", "castle wall", 975, 400, "castle_wall.png", (255, 255, 255))
castle_wall_4 = Building("castle wall 4", "castle wall", 975, 250, "castle_wall.png", (255, 255, 255))
castle_wall_5 = Building("castle wall 5", "castle wall", 975, 175, "castle_wall.png", (255, 255, 255))

amuna_inn = Building("amuna inn", "amuna building", 650, 675, "amuna_building.png", (255, 255, 255))
amuna_shop = Building("amuna shop", "amuna building", 720, 450, "amuna_building.png", (255, 255, 255))
amuna_academia = Building("amuna academia", "amuna building", 850, 595, "amuna_building.png", (255, 255, 255))

# groups for sprites
enemies = pygame.sprite.Group()
trees = pygame.sprite.Group()
water = pygame.sprite.Group()
buildings = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

# adding sprite objects to groups
enemies.add(snake_1, snake_2, snake_3, snake_4)
trees.add(pine_tree_1, pine_tree_2, pine_tree_4, pine_tree_5)
water.add(rohir_river_1, rohir_river_2, rohir_river_3, rohir_river_4, rohir_river_5, rohir_river_6)
buildings.add(rohir_river_gate, amuna_inn, castle_wall_1, castle_wall_2, castle_wall_3, castle_wall_4, castle_wall_5,
              amuna_shop, amuna_academia)

# adding all sprites to game screen
all_sprites.add(player, enemies, trees, water, buildings)

# pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
# pygame.mixer.music.play(loops=-1)

# move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
# move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
# collision_sound = pygame.mixer.Sound("Collision.ogg")

# Set the base volume for all sounds
# move_up_sound.set_volume(0.5)
# move_down_sound.set_volume(0.5)
# collision_sound.set_volume(0.5)

# Variable to keep our main loop running
running = True

# Our main loop
while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        # Should we add a new cloud?
        # elif event.type == ADDCLOUD:
        # Create the new cloud, and add it to our sprite groups
        # new_cloud = Cloud()
        # clouds.add(new_cloud)
        # all_sprites.add(new_cloud)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update the position of our enemies and clouds
    enemies.update()

    screen.blit(seldon_district_bg, (0, 0))

    # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        print("lol")

    # Flip everything to the display
    pygame.display.flip()

    # Ensure we maintain a 30 frames per second rate
    clock.tick(30)

# we can stop and quit the mixer
pygame.mixer.music.stop()
pygame.mixer.quit()
