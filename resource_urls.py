import os
import sys


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

# player no role -------------------------------------------------------------------------------------------------------
player_no_role_url = resource_path('resources/art/player_no_role.png')
# player mage ----------------------------------------------------------------------------------------------------------
player_mage_url = resource_path('resources/art/player_mage.png')
# player fighter -------------------------------------------------------------------------------------------------------
player_fighter_url = resource_path('resources/art/player_fighter.png')
# player scout ---------------------------------------------------------------------------------------------------------
player_scout_url = resource_path('resources/art/player_scout.png')
# player battle --------------------------------------------------------------------------------------------------------
player_battle_url = resource_path('resources/art/player_battle_sprites.png')
# player skills --------------------------------------------------------------------------------------------------------
player_skills_url = resource_path('resources/art/player_battle_sprites_skills.png')
# garan npc ------------------------------------------------------------------------------------------------------------
garan_url = resource_path('resources/art/garans.png')
# maurelle npc ---------------------------------------------------------------------------------------------------------
maurelle_url = resource_path('resources/art/maurelles.png')
# guard npc ------------------------------------------------------------------------------------------------------------
guard_url = resource_path('resources/art/guards.png')
# npc interactions -----------------------------------------------------------------------------------------------------
npc_interactions_url = resource_path('resources/art/npc_interactions.png')
# enemies --------------------------------------------------------------------------------------------------------------
enemies_url = resource_path('resources/art/enemies.png')
# enemies battle -------------------------------------------------------------------------------------------------------
enemies_battle_url = resource_path('resources/art/enemies_battle.png')
# amuna buildings ------------------------------------------------------------------------------------------------------
amuna_buildings_url = resource_path('resources/art/amuna_buildings.png')
# items ----------------------------------------------------------------------------------------------------------------
items_url = resource_path('resources/art/items.png')
# player info windows --------------------------------------------------------------------------------------------------
player_info_url = resource_path('resources/art/info_sheets.png')
# books ----------------------------------------------------------------------------------------------------------------
books_url = resource_path('resources/art/role_books.png')
# start screen buttons -------------------------------------------------------------------------------------------------
start_buttons_url = resource_path('resources/art/start_screen_buttons.png')
# buttons --------------------------------------------------------------------------------------------------------------
buttons_url = resource_path('resources/art/main_buttons.png')
# attack buttons -------------------------------------------------------------------------------------------------------
attack_buttons_url = resource_path('resources/art/attacks.png')
# skill buttons --------------------------------------------------------------------------------------------------------
skill_buttons_url = resource_path('resources/art/skills.png')
# quest windows --------------------------------------------------------------------------------------------------------
quest_windows_url = resource_path('resources/art/quest_sheets.png')
# quest stars ----------------------------------------------------------------------------------------------------------
quest_stars_url = resource_path('resources/art/quest_stars.png')
# pop up notifications -------------------------------------------------------------------------------------------------
popups_url = resource_path('resources/art/pop_ups.png')
# heath bars -----------------------------------------------------------------------------------------------------------
hp_url = resource_path('resources/art/health_bars.png')
# energy bars ----------------------------------------------------------------------------------------------------------
en_url = resource_path('resources/art/energy_bars.png')
# energy bars ----------------------------------------------------------------------------------------------------------
xp_url = resource_path('resources/art/xp_bars.png')
