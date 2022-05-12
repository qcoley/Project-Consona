import os
import sys


# function for building executable with PyInstaller adding the data files needed (images, sounds)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# non sprite sheets ----------------------------------------------------------------------------------------------------
amuna_character_screen = resource_path('resources/art/amuna_character_select.png')
nuldar_character_screen = resource_path('resources/art/nuldar_character_select.png')
sorae_character_screen = resource_path('resources/art/sorae_character_select.png')
seldon_bg_screen = resource_path('resources/art/seldon_district.png')
seldon_battle_screen = resource_path('resources/art/seldon_battle_screen.png')
seldon_shop_screen = resource_path('resources/art/seldon_shop.png')
seldon_inn_screen = resource_path('resources/art/seldon_inn.png')
seldon_academia_screen = resource_path('resources/art/seldon_academia.png')
seldon_hearth_screen = resource_path('resources/art/seldon_hearth_screen.png')
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
hearth_stone = resource_path('resources/art/hearth_stone.png')
rohir_gate = resource_path('resources/art/rohir_gate.png')
quest_logs = resource_path('resources/art/logs.png')
lets_go_button = resource_path('resources/art/lets_go_button.png')
learn_button = resource_path('resources/art/learn.png')
skill_learn_button = resource_path('resources/art/skill_learn.png')
game_play_function_buttons_url = resource_path('resources/art/game_play_function_buttons.png')

close_button = resource_path('resources/art/close.png')
knowledge_window = resource_path('resources/art/knowledge.png')
skill_bar = resource_path('resources/art/skill_bar.png')
start_button = resource_path('resources/art/start_button.png')
npc_name_plate = resource_path('resources/art/npc_name_plate.png')
character_select_overlay_url = resource_path('resources/art/character_select_overlay.png')
amuna_select_overlay_url = resource_path('resources/art/amuna_select_overlay.png')
nuldar_select_overlay_url = resource_path('resources/art/nuldar_select_overlay.png')
sorae_select_overlay_url = resource_path('resources/art/sorae_select_overlay.png')
name_input_url = resource_path('resources/art/name_input.png')

# create character screen character race selections
character_selections = resource_path('resources/art/character_selections.png')
# player no role amuna race --------------------------------------------------------------------------------------------
player_no_role_amuna_url = resource_path('resources/art/player_no_role_amuna.png')
# player no role sorae race --------------------------------------------------------------------------------------------
player_no_role_sorae_down_url = resource_path('resources/art/player_no_role_sorae_down.png')
player_no_role_sorae_up_url = resource_path('resources/art/player_no_role_sorae_up.png')
player_no_role_sorae_left_url = resource_path('resources/art/player_no_role_sorae_left.png')
player_no_role_sorae_right_url = resource_path('resources/art/player_no_role_sorae_right.png')
# player no role nuldar race -------------------------------------------------------------------------------------------
player_no_role_nuldar_down_url = resource_path('resources/art/player_no_role_nuldar_down.png')
player_no_role_nuldar_up_url = resource_path('resources/art/player_no_role_nuldar_up.png')
player_no_role_nuldar_left_url = resource_path('resources/art/player_no_role_nuldar_left.png')
player_no_role_nuldar_right_url = resource_path('resources/art/player_no_role_nuldar_right.png')
# player mage amuna race -----------------------------------------------------------------------------------------------
player_mage_amuna_url = resource_path('resources/art/player_mage_amuna.png')
# player mage nuldar race ----------------------------------------------------------------------------------------------
player_mage_nuldar_down_url = resource_path('resources/art/player_mage_nuldar_down.png')
player_mage_nuldar_up_url = resource_path('resources/art/player_mage_nuldar_up.png')
player_mage_nuldar_left_url = resource_path('resources/art/player_mage_nuldar_left.png')
player_mage_nuldar_right_url = resource_path('resources/art/player_mage_nuldar_right.png')
# player mage sorae race -----------------------------------------------------------------------------------------------
player_mage_sorae_down_url = resource_path('resources/art/player_mage_sorae_down.png')
player_mage_sorae_up_url = resource_path('resources/art/player_mage_sorae_up.png')
player_mage_sorae_left_url = resource_path('resources/art/player_mage_sorae_left.png')
player_mage_sorae_right_url = resource_path('resources/art/player_mage_sorae_right.png')
# player fighter amuna race --------------------------------------------------------------------------------------------
player_fighter_amuna_url = resource_path('resources/art/player_fighter_amuna.png')
# player fighter nuldar race -------------------------------------------------------------------------------------------
player_fighter_nuldar_down_url = resource_path('resources/art/player_fighter_nuldar_down.png')
player_fighter_nuldar_up_url = resource_path('resources/art/player_fighter_nuldar_up.png')
player_fighter_nuldar_left_url = resource_path('resources/art/player_fighter_nuldar_left.png')
player_fighter_nuldar_right_url = resource_path('resources/art/player_fighter_nuldar_right.png')
# player fighter sorae race --------------------------------------------------------------------------------------------
player_fighter_sorae_down_url = resource_path('resources/art/player_fighter_sorae_down.png')
player_fighter_sorae_up_url = resource_path('resources/art/player_fighter_sorae_up.png')
player_fighter_sorae_left_url = resource_path('resources/art/player_fighter_sorae_left.png')
player_fighter_sorae_right_url = resource_path('resources/art/player_fighter_sorae_right.png')
# player scout amuna race ----------------------------------------------------------------------------------------------
player_scout_amuna_url = resource_path('resources/art/player_scout_amuna.png')
# player scout nuldar race ---------------------------------------------------------------------------------------------
player_scout_nuldar_down_url = resource_path('resources/art/player_scout_nuldar_down.png')
player_scout_nuldar_up_url = resource_path('resources/art/player_scout_nuldar_up.png')
player_scout_nuldar_left_url = resource_path('resources/art/player_scout_nuldar_left.png')
player_scout_nuldar_right_url = resource_path('resources/art/player_scout_nuldar_right.png')
# player scout sorae race ----------------------------------------------------------------------------------------------
player_scout_sorae_down_url = resource_path('resources/art/player_scout_sorae_down.png')
player_scout_sorae_up_url = resource_path('resources/art/player_scout_sorae_up.png')
player_scout_sorae_left_url = resource_path('resources/art/player_scout_sorae_left.png')
player_scout_sorae_right_url = resource_path('resources/art/player_scout_sorae_right.png')
# player battle amuna race ---------------------------------------------------------------------------------------------
player_battle_amuna_url = resource_path('resources/art/player_battle_sprites_amuna.png')
# player skills amuna race ---------------------------------------------------------------------------------------------
player_skills_amuna_url = resource_path('resources/art/player_battle_sprites_skills_amuna.png')
# player battle sorae race ---------------------------------------------------------------------------------------------
player_battle_sorae_url = resource_path('resources/art/player_battle_sprites_sorae.png')
# player skills sorae race ---------------------------------------------------------------------------------------------
player_skills_sorae_url = resource_path('resources/art/player_battle_sprites_skills_sorae.png')
# player battle nuldar race --------------------------------------------------------------------------------------------
player_battle_nuldar_url = resource_path('resources/art/player_battle_sprites_nuldar.png')
# player skills sorae race ---------------------------------------------------------------------------------------------
player_skills_nuldar_url = resource_path('resources/art/player_battle_sprites_skills_nuldar.png')
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
start_buttons_url = resource_path('resources/art/start_buttons.png')
# race select buttons on character screen ------------------------------------------------------------------------------
race_select_buttons_url = resource_path('resources/art/race_select_buttons.png')
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
