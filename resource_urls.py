import os
import sys


# function for building executable with PyInstaller adding the data files needed (images, sounds)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# non sprite sheets ----------------------------------------------------------------------------------------------------
amuna_character_screen = resource_path('resources/art/screen_amuna_character_select.png')
nuldar_character_screen = resource_path('resources/art/screen_nuldar_character_select.png')
sorae_character_screen = resource_path('resources/art/screen_sorae_character_select.png')
nascent_grove_screen = resource_path('resources/art/bg_nascent_grove.png')
stardust_outpost_screen = resource_path('resources/art/bg_stardust_post.png')
seldon_bg_screen = resource_path('resources/art/bg_seldon_district.png')
korlok_bg_screen = resource_path('resources/art/bg_korlok_district.png')
seldon_battle_screen = resource_path('resources/art/bg_seldon_battle_screen.png')
seldon_shop_screen = resource_path('resources/art/bg_seldon_shop.png')
seldon_inn_screen = resource_path('resources/art/bg_seldon_inn.png')
seldon_academia_screen = resource_path('resources/art/bg_seldon_academia.png')
seldon_hearth_screen = resource_path('resources/art/screen_seldon_hearth.png')
game_over_screen = resource_path('resources/art/screen_game_over.png')
start_screen = resource_path('resources/art/screen_start.png')
nera_sleep_screen = resource_path('resources/art/screen_nera_sleep.png')
bar_backdrop = resource_path('resources/art/overlay_status_bar_backdrop.png')
enemy_status = resource_path('resources/art/overlay_enemy_status_backdrop.png')
enemy_bar_backdrop = resource_path('resources/art/overlay_enemy_status_bar.png')
buy_inventory = resource_path('resources/art/overlay_buy_inventory.png')
message_box = resource_path('resources/art/overlay_message_box.png')
nascent_gate_url = resource_path('resources/art/sprites_nascent_gate.png')
pine_tree = resource_path('resources/art/sprite_pine_tree.png')
hearth_stone = resource_path('resources/art/sprite_hearth_stone.png')
quest_logs = resource_path('resources/art/sprite_logs.png')
rohir_gate = resource_path('resources/art/overlay_rohir_gate.png')
lets_go_button = resource_path('resources/art/button_lets_go.png')
learn_button = resource_path('resources/art/overlay_learn.png')
skill_learn_button = resource_path('resources/art/overlay_skill_learn.png')
game_play_function_buttons_url = resource_path('resources/art/buttons_game_play_function.png')
nascent_gate_popup_url = resource_path('resources/art/popup_nascent_gate.png')
level_up = resource_path('resources/art/popup_level_up.png')
close_button = resource_path('resources/art/button_close.png')
knowledge_window = resource_path('resources/art/overlay_knowledge.png')
skill_bar = resource_path('resources/art/overlay_skill_bar.png')
start_button = resource_path('resources/art/button_start.png')
npc_name_plate = resource_path('resources/art/overlay_npc_name_plate.png')
character_select_overlay_url = resource_path('resources/art/overlay_character_select.png')
name_input_url = resource_path('resources/art/overlay_name_input.png')
race_select_overlays_url = resource_path('resources/art/overlays_race_select.png')

# create character screen character race selections
character_selections = resource_path('resources/art/overlay_character_selections.png')
# player no role amuna race --------------------------------------------------------------------------------------------
player_no_role_amuna_down_url = resource_path('resources/art/player_no_role_amuna_down.png')
player_no_role_amuna_up_url = resource_path('resources/art/player_no_role_amuna_up.png')
player_no_role_amuna_left_url = resource_path('resources/art/player_no_role_amuna_left.png')
player_no_role_amuna_right_url = resource_path('resources/art/player_no_role_amuna_right.png')
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
player_mage_amuna_down_url = resource_path('resources/art/player_mage_amuna_down.png')
player_mage_amuna_up_url = resource_path('resources/art/player_mage_amuna_up.png')
player_mage_amuna_left_url = resource_path('resources/art/player_mage_amuna_left.png')
player_mage_amuna_right_url = resource_path('resources/art/player_mage_amuna_right.png')
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
player_fighter_amuna_down_url = resource_path('resources/art/player_fighter_amuna_down.png')
player_fighter_amuna_up_url = resource_path('resources/art/player_fighter_amuna_up.png')
player_fighter_amuna_left_url = resource_path('resources/art/player_fighter_amuna_left.png')
player_fighter_amuna_right_url = resource_path('resources/art/player_fighter_amuna_right.png')
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
player_scout_amuna_down_url = resource_path('resources/art/player_scout_amuna_down.png')
player_scout_amuna_up_url = resource_path('resources/art/player_scout_amuna_up.png')
player_scout_amuna_left_url = resource_path('resources/art/player_scout_amuna_left.png')
player_scout_amuna_right_url = resource_path('resources/art/player_scout_amuna_right.png')
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
garan_url = resource_path('resources/art/sprites_garans.png')
# maurelle npc ---------------------------------------------------------------------------------------------------------
maurelle_url = resource_path('resources/art/sprites_maurelles.png')
# celeste npc ---------------------------------------------------------------------------------------------------------
celeste_url = resource_path('resources/art/sprites_celestes.png')
# guard npc ------------------------------------------------------------------------------------------------------------
guard_url = resource_path('resources/art/sprites_guards.png')
# torune npc -----------------------------------------------------------------------------------------------------------
torune_url = resource_path('resources/art/sprites_torune.png')
# npc interactions -----------------------------------------------------------------------------------------------------
npc_interactions_url = resource_path('resources/art/sprites_npc_interactions.png')
# enemies --------------------------------------------------------------------------------------------------------------
enemies_url = resource_path('resources/art/sprites_enemies.png')
# enemies battle -------------------------------------------------------------------------------------------------------
enemies_battle_url = resource_path('resources/art/sprites_enemies_battle.png')
# amuna buildings ------------------------------------------------------------------------------------------------------
amuna_buildings_url = resource_path('resources/art/sprites_amuna_buildings.png')
# role select overlay --------------------------------------------------------------------------------------------------
role_selection_overlay = resource_path('resources/art/overlay_role_select.png')
# role select buttons --------------------------------------------------------------------------------------------------
role_selection_buttons = resource_path('resources/art/buttons_select_role.png')
# star power -----------------------------------------------------------------------------------------------------------
star_power_url = resource_path('resources/art/overlay_star_power.png')
# items ----------------------------------------------------------------------------------------------------------------
items_url = resource_path('resources/art/overlay_items.png')
# items info -----------------------------------------------------------------------------------------------------------
items_info_url = resource_path('resources/art/overlay_info_items.png')
# player info windows --------------------------------------------------------------------------------------------------
player_info_url = resource_path('resources/art/overlay_info_sheets.png')
# books ----------------------------------------------------------------------------------------------------------------
books_url = resource_path('resources/art/overlay_role_books.png')
# sell items -----------------------------------------------------------------------------------------------------------
sell_items_url = resource_path('resources/art/overlay_sell_items.png')
# start screen buttons -------------------------------------------------------------------------------------------------
start_buttons_url = resource_path('resources/art/buttons_start_screen.png')
# race select buttons on character screen ------------------------------------------------------------------------------
race_select_buttons_url = resource_path('resources/art/buttons_race_select.png')
# buttons --------------------------------------------------------------------------------------------------------------
buttons_url = resource_path('resources/art/buttons_main.png')
# attack buttons -------------------------------------------------------------------------------------------------------
attack_buttons_url = resource_path('resources/art/overlay_attacks.png')
# skill buttons --------------------------------------------------------------------------------------------------------
skill_buttons_url = resource_path('resources/art/overlay_skills.png')
# quest windows --------------------------------------------------------------------------------------------------------
quest_windows_url = resource_path('resources/art/overlay_quest_sheets.png')
# quest stars ----------------------------------------------------------------------------------------------------------
quest_stars_url = resource_path('resources/art/overlay_quest_stars.png')
# pop up notifications -------------------------------------------------------------------------------------------------
popups_url = resource_path('resources/art/popups_main.png')
# heath bars -----------------------------------------------------------------------------------------------------------
hp_url = resource_path('resources/art/bars_health.png')
# energy bars ----------------------------------------------------------------------------------------------------------
en_url = resource_path('resources/art/bars_energy.png')
# energy bars ----------------------------------------------------------------------------------------------------------
xp_url = resource_path('resources/art/bars_xp.png')
