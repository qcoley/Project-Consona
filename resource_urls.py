import sys
import os
import pygame

pygame.init()
pygame.display.set_caption("Project Eterna")
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)


class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, x, y, width, height):
        sprite_image = pygame.Surface([width, height], pygame.SRCALPHA)
        sprite_image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return sprite_image


# ----------------------------------------------------------------------------------------------------------------------
# function for building executable with PyInstaller adding the data files needed (images, sounds)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# non sprite sheets ----------------------------------------------------------------------------------------------------
seldon_bg_screen = resource_path('resources/art/seldon_district.png')
seldon_battle_screen = resource_path('resources/art/seldon_battle_screen.png')
seldon_shop_screen = resource_path('resources/art/seldon_shop.png')
seldon_inn_screen = resource_path('resources/art/seldon_inn.png')
seldon_academia_screen = resource_path('resources/art/seldon_academia.png')
korlok_bg_screen = resource_path('resources/art/korlok_district.png')
game_over_screen = resource_path('resources/art/game_over.png')
start_screen = resource_path('resources/art/start_screen.png')
nera_sleep_screen = resource_path('resources/art/nera_sleep_screen.png')
level_up = resource_path('resources/art/level_up.png')
bar_backdrop = resource_path('resources/art/status_bar_backdrop.png')
enemy_bar_backdrop = resource_path('resources/art/enemy_status_bar_backdrop.png')
enemy_status = resource_path('resources/art/enemy_status_backdrop.png')
buy_inventory = resource_path('resources/art/buy_inventory.png')
inventory = resource_path('resources/art/inventory.png')
message_box = resource_path('resources/art/message_box.png')
pine_tree = resource_path('resources/art/pine_tree.png')
seldon_grass = resource_path('resources/art/seldon_grass.png')
seldon_flower = resource_path('resources/art/seldon_flower.png')
rohir_gate = resource_path('resources/art/rohir_gate.png')
quest_logs = resource_path('resources/art/logs.png')
continue_button = resource_path('resources/art/continue_button.png')
learn_button = resource_path('resources/art/learn.png')
skill_learn_button = resource_path('resources/art/skill_learn.png')
hearth_button = resource_path('resources/art/hearth.png')
close_button = resource_path('resources/art/close.png')
knowledge_window = resource_path('resources/art/knowledge.png')
skill_bar = resource_path('resources/art/skill_bar.png')
start_button = resource_path('resources/art/start_button.png')
npc_name_plate = resource_path('resources/art/npc_name_plate.png')

# sprite sheets --------------------------------------------------------------------------------------------------------
# player no role -------------------------------------------------------------------------------------------------------
player_no_role_url = resource_path('resources/art/player_no_role.png')
player_no_role_sheet = SpriteSheet(player_no_role_url)
player_no_role_down = player_no_role_sheet.get_image(0, 0, 50, 75)
player_no_role_up = player_no_role_sheet.get_image(51, 0, 50, 75)
player_no_role_left = player_no_role_sheet.get_image(101, 0, 50, 75)
player_no_role_right = player_no_role_sheet.get_image(151, 0, 50, 75)

# player mage ----------------------------------------------------------------------------------------------------------
player_mage_url = resource_path('resources/art/player_mage.png')
player_mage_sheet = SpriteSheet(player_mage_url)
player_mage_down = player_mage_sheet.get_image(0, 0, 50, 75)
player_mage_up = player_mage_sheet.get_image(51, 0, 50, 75)
player_mage_left = player_mage_sheet.get_image(101, 0, 50, 75)
player_mage_right = player_mage_sheet.get_image(151, 0, 50, 75)

# player fighter -------------------------------------------------------------------------------------------------------
player_fighter_url = resource_path('resources/art/player_fighter.png')
player_fighter_sheet = SpriteSheet(player_fighter_url)
player_fighter_down = player_fighter_sheet.get_image(0, 0, 50, 75)
player_fighter_up = player_fighter_sheet.get_image(51, 0, 50, 75)
player_fighter_left = player_fighter_sheet.get_image(101, 0, 50, 75)
player_fighter_right = player_fighter_sheet.get_image(151, 0, 50, 75)

# player scout ---------------------------------------------------------------------------------------------------------
player_scout_url = resource_path('resources/art/player_scout.png')
player_scout_sheet = SpriteSheet(player_scout_url)
player_scout_down = player_scout_sheet.get_image(0, 0, 50, 75)
player_scout_up = player_scout_sheet.get_image(51, 0, 50, 75)
player_scout_left = player_scout_sheet.get_image(101, 0, 50, 75)
player_scout_right = player_scout_sheet.get_image(151, 0, 50, 75)

# player battle --------------------------------------------------------------------------------------------------------
player_battle_url = resource_path('resources/art/player_battle_sprites.png')
player_battle_sheet = SpriteSheet(player_battle_url)
player_no_role_battle = player_battle_sheet.get_image(0, 0, 750, 624)
player_no_role_attack = player_battle_sheet.get_image(751, 0, 750, 624)
player_mage_battle = player_battle_sheet.get_image(1501, 0, 750, 624)
player_mage_attack = player_battle_sheet.get_image(2251, 0, 750, 624)
player_fighter_battle = player_battle_sheet.get_image(3001, 0, 750, 624)
player_fighter_attack = player_battle_sheet.get_image(3751, 0, 750, 624)
player_scout_battle = player_battle_sheet.get_image(4501, 0, 750, 624)
player_scout_attack = player_battle_sheet.get_image(5251, 0, 750, 624)

# player skills --------------------------------------------------------------------------------------------------------
player_skills_url = resource_path('resources/art/player_battle_sprites_skills.png')
player_skills_sheet = SpriteSheet(player_skills_url)
player_mage_barrier_battle = player_skills_sheet.get_image(0, 0, 750, 624)
player_mage_barrier_attack = player_skills_sheet.get_image(751, 0, 750, 624)
player_scout_sense_battle = player_skills_sheet.get_image(1501, 0, 750, 624)
player_scout_sense_attack = player_skills_sheet.get_image(2251, 0, 750, 624)
player_fighter_strike = player_skills_sheet.get_image(3001, 0, 750, 624)

# garan npc ------------------------------------------------------------------------------------------------------------
garan_url = resource_path('resources/art/garans.png')
garan_sheet = SpriteSheet(garan_url)
garan_down = garan_sheet.get_image(0, 0, 50, 75)
garan_up = garan_sheet.get_image(51, 0, 50, 75)
garan_left = garan_sheet.get_image(101, 0, 50, 75)
garan_right = garan_sheet.get_image(151, 0, 50, 75)

# maurelle npc ---------------------------------------------------------------------------------------------------------
maurelle_url = resource_path('resources/art/maurelles.png')
maurelle_sheet = SpriteSheet(maurelle_url)
maurelle_down = maurelle_sheet.get_image(0, 0, 50, 75)
maurelle_up = maurelle_sheet.get_image(51, 0, 50, 75)
maurelle_left = maurelle_sheet.get_image(101, 0, 50, 75)
maurelle_right = maurelle_sheet.get_image(151, 0, 50, 75)

# guard npc ------------------------------------------------------------------------------------------------------------
guard_url = resource_path('resources/art/guards.png')
guard_sheet = SpriteSheet(guard_url)
guard_down = guard_sheet.get_image(0, 0, 50, 75)
guard_up = guard_sheet.get_image(51, 0, 50, 75)
guard_left = guard_sheet.get_image(101, 0, 50, 75)
guard_right = guard_sheet.get_image(151, 0, 50, 75)

# npc interactions -----------------------------------------------------------------------------------------------------
npc_interactions_url = resource_path('resources/art/npc_interactions.png')
npc_interactions_sheet = SpriteSheet(npc_interactions_url)
garan_interaction = npc_interactions_sheet.get_image(0, 0, 200, 260)
maurelle_interaction = npc_interactions_sheet.get_image(201, 0, 200, 260)
guard_interaction = npc_interactions_sheet.get_image(401, 0, 200, 260)

# enemies --------------------------------------------------------------------------------------------------------------
enemies_url = resource_path('resources/art/enemies.png')
enemies_sheet = SpriteSheet(enemies_url)
snake = enemies_sheet.get_image(0, 0, 50, 50)
ghoul = enemies_sheet.get_image(51, 0, 50, 50)

# enemies battle -------------------------------------------------------------------------------------------------------
enemies_battle_url = resource_path('resources/art/enemies_battle.png')
enemies_battle_sheet = SpriteSheet(enemies_battle_url)
snake_battle = enemies_battle_sheet.get_image(0, 0, 300, 250)
snake_attack = enemies_battle_sheet.get_image(301, 0, 300, 250)
ghoul_battle = enemies_battle_sheet.get_image(601, 0, 300, 250)
ghoul_attack = enemies_battle_sheet.get_image(901, 0, 300, 250)

# amuna buildings ------------------------------------------------------------------------------------------------------
amuna_buildings_url = resource_path('resources/art/amuna_buildings.png')
amuna_buildings_sheet = SpriteSheet(amuna_buildings_url)
amuna_academia_building = amuna_buildings_sheet.get_image(0, 0, 100, 100)
amuna_inn_building = amuna_buildings_sheet.get_image(101, 0, 100, 100)
amuna_shop_building = amuna_buildings_sheet.get_image(201, 0, 100, 100)

# items ----------------------------------------------------------------------------------------------------------------
items_url = resource_path('resources/art/items.png')
items_sheet = SpriteSheet(items_url)
health_pot = items_sheet.get_image(0, 0, 50, 50)
energy_pot = items_sheet.get_image(51, 0, 50, 50)
basic_robes = items_sheet.get_image(101, 0, 50, 50)
basic_armor = items_sheet.get_image(151, 0, 50, 50)
basic_tunic = items_sheet.get_image(201, 0, 50, 50)
basic_staff = items_sheet.get_image(251, 0, 50, 50)
basic_sword = items_sheet.get_image(301, 0, 50, 50)
basic_bow = items_sheet.get_image(351, 0, 50, 50)
bone_dust = items_sheet.get_image(401, 0, 50, 50)
shiny_rock = items_sheet.get_image(451, 0, 50, 50)
temp = items_sheet.get_image(501, 0, 50, 50)

# player info windows --------------------------------------------------------------------------------------------------
player_info_url = resource_path('resources/art/info_sheets.png')
player_info_sheet = SpriteSheet(player_info_url)
character_window = player_info_sheet.get_image(0, 0, 500, 525)
journal_window = player_info_sheet.get_image(501, 0, 500, 525)

# books ----------------------------------------------------------------------------------------------------------------
books_url = resource_path('resources/art/role_books.png')
books_sheet = SpriteSheet(books_url)
mage_book = books_sheet.get_image(0, 0, 700, 525)
fighter_book = books_sheet.get_image(701, 0, 700, 525)
scout_book = books_sheet.get_image(1401, 0, 700, 525)

# start screen buttons -------------------------------------------------------------------------------------------------
start_buttons_url = resource_path('resources/art/start_screen_buttons.png')
start_buttons_sheet = SpriteSheet(start_buttons_url)
s1024_button = start_buttons_sheet.get_image(0, 0, 385, 60)
s1280_button = start_buttons_sheet.get_image(386, 0, 385, 60)
s1600_button = start_buttons_sheet.get_image(769, 0, 385, 60)

# buttons --------------------------------------------------------------------------------------------------------------
buttons_url = resource_path('resources/art/main_buttons.png')
buttons_sheet = SpriteSheet(buttons_url)
character_button = buttons_sheet.get_image(0, 0, 100, 50)
journal_button = buttons_sheet.get_image(101, 0, 100, 50)
buy_button = buttons_sheet.get_image(201, 0, 100, 50)
rest_button = buttons_sheet.get_image(301, 0, 100, 50)
quest_button = buttons_sheet.get_image(401, 0, 100, 50)
leave_button = buttons_sheet.get_image(501, 0, 100, 50)
accept_button = buttons_sheet.get_image(601, 0, 100, 50)
decline_button = buttons_sheet.get_image(701, 0, 100, 50)

# attack buttons -------------------------------------------------------------------------------------------------------
attack_buttons_url = resource_path('resources/art/attacks.png')
attack_buttons_sheet = SpriteSheet(attack_buttons_url)
mage_attack_button = attack_buttons_sheet.get_image(0, 0, 60, 60)
fighter_attack_button = attack_buttons_sheet.get_image(61, 0, 60, 60)
scout_attack_button = attack_buttons_sheet.get_image(121, 0, 60, 60)
no_role_attack_button = attack_buttons_sheet.get_image(181, 0, 60, 60)

# skill buttons --------------------------------------------------------------------------------------------------------
skill_buttons_url = resource_path('resources/art/skills.png')
skill_buttons_sheet = SpriteSheet(skill_buttons_url)
barrier_button = attack_buttons_sheet.get_image(0, 0, 60, 60)
strike_button = attack_buttons_sheet.get_image(61, 0, 60, 60)
sense_button = attack_buttons_sheet.get_image(121, 0, 60, 60)

# quest windows --------------------------------------------------------------------------------------------------------
quest_windows_url = resource_path('resources/art/quest_sheets.png')
quest_windows_sheet = SpriteSheet(quest_windows_url)
garan_quest = quest_windows_sheet.get_image(0, 0, 500, 525)
maurelle_quest = quest_windows_sheet.get_image(501, 0, 500, 525)
guard_quest = quest_windows_sheet.get_image(1001, 0, 500, 525)

# quest stars ----------------------------------------------------------------------------------------------------------
quest_stars_url = resource_path('resources/art/quest_stars.png')
quest_stars_sheet = SpriteSheet(quest_stars_url)
quest_start_star = quest_stars_sheet.get_image(0, 0, 50, 50)
quest_progress_star = quest_stars_sheet.get_image(51, 0, 50, 50)
quest_complete_star = quest_stars_sheet.get_image(101, 0, 50, 50)

# pop up notifications -------------------------------------------------------------------------------------------------
popups_url = resource_path('resources/art/pop_ups.png')
popups_sheet = SpriteSheet(popups_url)
gear_popup = popups_sheet.get_image(0, 0, 400, 200)
health_popup = popups_sheet.get_image(401, 0, 400, 200)
knowledge_popup = popups_sheet.get_image(801, 0, 400, 200)

# heath bars -----------------------------------------------------------------------------------------------------------
hp_url = resource_path('resources/art/health_bars.png')
hp_sheet = SpriteSheet(hp_url)
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
en_url = resource_path('resources/art/energy_bars.png')
en_sheet = SpriteSheet(en_url)
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
xp_url = resource_path('resources/art/xp_bars.png')
xp_sheet = SpriteSheet(xp_url)
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
