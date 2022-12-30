import os
import sys
import pygame


# this file to load all images(graphics) into a dictionary and return to main file -------------------------------------

# function for building executable with PyInstaller adding the data files needed (images, sounds)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def sprite_sheet(size, file, posit=(0, 0)):
    len_sprt_x, len_sprt_y = size  # sprite size
    sprt_rect_x, sprt_rect_y = posit  # first sprite on sheet

    sheet = pygame.image.load(file).convert_alpha()  # Load the sheet
    sheet.set_colorkey((255, 255, 255))
    sheet_rect = sheet.get_rect()
    sprites = []

    for i in range(0, sheet_rect.height, size[1]):  # rows
        for j in range(0, sheet_rect.width, size[0]):  # columns
            sheet.set_clip(pygame.Rect(sprt_rect_x, sprt_rect_y, len_sprt_x, len_sprt_y))  # find sprite
            sprite = sheet.subsurface(sheet.get_clip())  # grab sprite
            sprites.append(sprite)
            sprt_rect_x += len_sprt_x

        sprt_rect_y += len_sprt_y
        sprt_rect_x = 0

    return sprites


def initialize_display():
    pygame.init()
    pygame.display.set_caption("Project Eterna")
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    return screen


def draw_loading_screen(screen):
    loading_screen = pygame.image.load(resource_path('resources/art/screen_loading.png')).convert_alpha()
    screen.blit(loading_screen, (0, 0))
    pygame.display.flip()


def load_graphics():

    loaded_dict = {"a_char_screen": "", "n_char_screen": "", "s_char_screen": "", "nascent_grove_screen": "",
                   "stardust_cove_screen": "", "stardust_post_screen": "", "seldon_bg_screen": "",
                   "korlok_bg_screen": "", "seldon_battle_screen": "", "seldon_shop_screen": "",
                   "seldon_inn_screen": "", "seldon_academia_screen": "", "seldon_hearth_screen": "",
                   "game_over_screen": "", "start_screen": "", "nera_sleep_screen": "", "bar_backdrop": "",
                   "enemy_status": "", "enemy_bar_backdrop": "", "buy_inventory": "", "message_box": "",
                   "pine_tree": "", "hearth_stone": "", "hearth_stone_lit": "", "rohir_gate": "", "lets_go_button": "",
                   "lets_go_button_high": "", "learn_button": "", "skill_learn_button": "", "nascent_gate_popup": "",
                   "level_up": "", "close_button": "", "knowledge_window": "", "skill_bar": "", "start_button": "",
                   "npc_name_plate": "", "char_select_overlay": "", "role_selection_overlay": "",
                   "location_overlay": "", "popup_interaction": "", "popup_interaction_red": "",
                   "popup_interaction_purple": "", "popup_loot": "", "stardust_entrance": "",
                   "upgrade_overlay": "", "cat_pet_button_overlay": "", "amuna_character_img": "",
                   "nuldar_character_img": "", "sorae_character_img": "", "amuna_overlay_img": "",
                   "nuldar_overlay_img": "", "sorae_overlay_img": "", "name_input_img": "", "name_input_empty_img": "",
                   "player_no_role_amuna_down_1": "", "player_no_role_amuna_down_2": "",
                   "player_no_role_amuna_down_3": "", "player_no_role_amuna_down_4": "",
                   "player_no_role_amuna_up_1": "", "player_no_role_amuna_up_2": "",
                   "player_no_role_amuna_up_3": "", "player_no_role_amuna_up_4": "",
                   "player_no_role_amuna_left_1": "", "player_no_role_amuna_left_2": "",
                   "player_no_role_amuna_left_3": "", "player_no_role_amuna_left_4": "",
                   "player_no_role_amuna_right_1": "", "player_no_role_amuna_right_2": "",
                   "player_no_role_amuna_right_3": "", "player_no_role_amuna_right_4": "",
                   "player_no_role_sorae_down_1": "", "player_no_role_sorae_down_2": "",
                   "player_no_role_sorae_down_3": "", "player_no_role_sorae_down_4": "",
                   "player_no_role_sorae_up_1": "", "player_no_role_sorae_up_2": "",
                   "player_no_role_sorae_up_3": "", "player_no_role_sorae_up_4": "",
                   "player_no_role_sorae_left_1": "", "player_no_role_sorae_left_2": "",
                   "player_no_role_sorae_left_3": "", "player_no_role_sorae_left_4": "",
                   "player_no_role_sorae_right_1": "", "player_no_role_sorae_right_2": "",
                   "player_no_role_sorae_right_3": "", "player_no_role_sorae_right_4": "",
                   "player_no_role_nuldar_down_1": "", "player_no_role_nuldar_down_2": "",
                   "player_no_role_nuldar_down_3": "", "player_no_role_nuldar_down_4": "",
                   "player_no_role_nuldar_up_1": "", "player_no_role_nuldar_up_2": "",
                   "player_no_role_nuldar_up_3": "", "player_no_role_nuldar_up_4": "",
                   "player_no_role_nuldar_left_1": "", "player_no_role_nuldar_left_2": "",
                   "player_no_role_nuldar_left_3": "", "player_no_role_nuldar_left_4": "",
                   "player_no_role_nuldar_right_1": "", "player_no_role_nuldar_right_2": "",
                   "player_no_role_nuldar_right_3": "", "player_no_role_nuldar_right_4": "",
                   "player_mage_amuna_down_1": "", "player_mage_amuna_down_2": "", "player_mage_amuna_down_3": "",
                   "player_mage_amuna_down_4": "", "player_mage_amuna_up_1": "", "player_mage_amuna_up_2": "",
                   "player_mage_amuna_up_3": "", "player_mage_amuna_up_4": "", "player_mage_amuna_left_1": "",
                   "player_mage_amuna_left_2": "", "player_mage_amuna_left_3": "",
                   "player_mage_amuna_left_4": "", "player_mage_amuna_right_1": "",
                   "player_mage_amuna_right_2": "", "player_mage_amuna_right_3": "",
                   "player_mage_amuna_right_4": "", "player_mage_sorae_down_1": "",
                   "player_mage_sorae_down_2": "", "player_mage_sorae_down_3": "",
                   "player_mage_sorae_down_4": "", "player_mage_sorae_up_1": "", "player_mage_sorae_up_2": "",
                   "player_mage_sorae_up_3": "", "player_mage_sorae_up_4": "", "player_mage_sorae_left_1": "",
                   "player_mage_sorae_left_2": "", "player_mage_sorae_left_3": "", "player_mage_sorae_left_4": "",
                   "player_mage_sorae_right_1": "", "player_mage_sorae_right_2": "",
                   "player_mage_sorae_right_3": "", "player_mage_sorae_right_4": "",
                   "player_mage_nuldar_down_1": "", "player_mage_nuldar_down_2": "",
                   "player_mage_nuldar_down_3": "", "player_mage_nuldar_down_4": "",
                   "player_mage_nuldar_up_1": "", "player_mage_nuldar_up_2": "", "player_mage_nuldar_up_3": "",
                   "player_mage_nuldar_up_4": "", "player_mage_nuldar_left_1": "",
                   "player_mage_nuldar_left_2": "", "player_mage_nuldar_left_3": "",
                   "player_mage_nuldar_left_4": "", "player_mage_nuldar_right_1": "",
                   "player_mage_nuldar_right_2": "", "player_mage_nuldar_right_3": "",
                   "player_mage_nuldar_right_4": "", "player_fighter_amuna_down_1": "",
                   "player_fighter_amuna_down_2": "", "player_fighter_amuna_down_3": "",
                   "player_fighter_amuna_down_4": "", "player_fighter_amuna_up_1": "",
                   "player_fighter_amuna_up_2": "", "player_fighter_amuna_up_3": "",
                   "player_fighter_amuna_up_4": "", "player_fighter_amuna_left_1": "",
                   "player_fighter_amuna_left_2": "", "player_fighter_amuna_left_3": "",
                   "player_fighter_amuna_left_4": "", "player_fighter_amuna_right_1": "",
                   "player_fighter_amuna_right_2": "", "player_fighter_amuna_right_3": "",
                   "player_fighter_amuna_right_4": "", "player_fighter_sorae_down_1": "",
                   "player_fighter_sorae_down_2": "", "player_fighter_sorae_down_3": "",
                   "player_fighter_sorae_down_4": "", "player_fighter_sorae_up_1": "",
                   "player_fighter_sorae_up_2": "", "player_fighter_sorae_up_3": "",
                   "player_fighter_sorae_up_4": "", "player_fighter_sorae_left_1": "",
                   "player_fighter_sorae_left_2": "", "player_fighter_sorae_left_3": "",
                   "player_fighter_sorae_left_4": "", "player_fighter_sorae_right_1": "",
                   "player_fighter_sorae_right_2": "", "player_fighter_sorae_right_3": "",
                   "player_fighter_sorae_right_4": "", "player_fighter_nuldar_down_1": "",
                   "player_fighter_nuldar_down_2": "", "player_fighter_nuldar_down_3": "",
                   "player_fighter_nuldar_down_4": "", "player_fighter_nuldar_up_1": "",
                   "player_fighter_nuldar_up_2": "", "player_fighter_nuldar_up_3": "",
                   "player_fighter_nuldar_up_4": "", "player_fighter_nuldar_left_1": "",
                   "player_fighter_nuldar_left_2": "", "player_fighter_nuldar_left_3": "",
                   "player_fighter_nuldar_left_4": "", "player_fighter_nuldar_right_1": "",
                   "player_fighter_nuldar_right_2": "", "player_fighter_nuldar_right_3": "",
                   "player_fighter_nuldar_right_4": "", "player_scout_amuna_down_1": "",
                   "player_scout_amuna_down_2": "", "player_scout_amuna_down_3": "",
                   "player_scout_amuna_down_4": "", "player_scout_amuna_up_1": "", "player_scout_amuna_up_2": "",
                   "player_scout_amuna_up_3": "", "player_scout_amuna_up_4": "", "player_scout_amuna_left_1": "",
                   "player_scout_amuna_left_2": "", "player_scout_amuna_left_3": "",
                   "player_scout_amuna_left_4": "", "player_scout_amuna_right_1": "",
                   "player_scout_amuna_right_2": "", "player_scout_amuna_right_3": "",
                   "player_scout_amuna_right_4": "", "player_scout_sorae_down_1": "",
                   "player_scout_sorae_down_2": "", "player_scout_sorae_down_3": "",
                   "player_scout_sorae_down_4": "", "player_scout_sorae_up_1": "", "player_scout_sorae_up_2": "",
                   "player_scout_sorae_up_3": "", "player_scout_sorae_up_4": "", "player_scout_sorae_left_1": "",
                   "player_scout_sorae_left_2": "", "player_scout_sorae_left_3": "",
                   "player_scout_sorae_left_4": "", "player_scout_sorae_right_1": "",
                   "player_scout_sorae_right_2": "", "player_scout_sorae_right_3": "",
                   "player_scout_sorae_right_4": "", "player_scout_nuldar_down_1": "",
                   "player_scout_nuldar_down_2": "", "player_scout_nuldar_down_3": "",
                   "player_scout_nuldar_down_4": "", "player_scout_nuldar_up_1": "",
                   "player_scout_nuldar_up_2": "", "player_scout_nuldar_up_3": "", "player_scout_nuldar_up_4": "",
                   "player_scout_nuldar_left_1": "", "player_scout_nuldar_left_2": "",
                   "player_scout_nuldar_left_3": "", "player_scout_nuldar_left_4": "",
                   "player_scout_nuldar_right_1": "", "player_scout_nuldar_right_2": "",
                   "player_scout_nuldar_right_3": "", "player_scout_nuldar_right_4": "",
                   "player_no_role_amuna_battle": "", "player_no_role_amuna_attack": "",
                   "player_mage_amuna_battle": "", "player_mage_amuna_attack": "",
                   "player_fighter_amuna_battle": "", "player_fighter_amuna_attack": "",
                   "player_scout_amuna_battle": "", "player_scout_amuna_attack": "",
                   "player_mage_barrier_amuna_battle": "", "player_mage_barrier_amuna_attack": "",
                   "player_scout_sense_amuna_battle": "", "player_scout_sense_amuna_attack": "",
                   "player_fighter_amuna_strike": "", "player_no_role_sorae_battle": "",
                   "player_no_role_sorae_attack": "", "player_mage_sorae_battle": "",
                   "player_mage_sorae_attack": "", "player_fighter_sorae_battle": "",
                   "player_fighter_sorae_attack": "", "player_scout_sorae_battle": "",
                   "player_scout_sorae_attack": "", "player_mage_barrier_sorae_battle": "",
                   "player_mage_barrier_sorae_attack": "", "player_scout_sense_sorae_battle": "",
                   "player_scout_sense_sorae_attack": "", "player_fighter_sorae_strike": "",
                   "garan_down": "", "garan_up": "", "garan_left": "", "garan_right": "", "maurelle_down": "",
                   "maurelle_up": "", "maurelle_left": "", "maurelle_right": "", "celeste_down": "",
                   "celeste_up": "", "celeste_left": "", "celeste_right": "", "voruke_down": "",
                   "voruke_up": "", "voruke_left": "", "voruke_right": "", "zerah_down": "",
                   "zerah_up": "", "zerah_left": "", "zerah_right": "", "nede_left": "", "nede_right": "",
                   "nede_high_left": "", "nede_high_right": "", "guard_down": "", "guard_up": "",
                   "guard_left": "", "guard_right": "", "torune_down": "", "torune_up": "", "torune_left": "",
                   "torune_right": "", "garan_interaction": "", "maurelle_interaction": "",
                   "celeste_interaction": "", "torune_interaction": "", "snake": "", "ghoul": "", "ghoul attacking": "",
                   "snake_high": "", "ghoul_high": "", "snake_battle": "", "snake_attack": "", "snake attacking": "",
                   "ghoul_battle": "", "ghoul_attack": "", "amuna_academia_building": "",
                   "amuna_inn_building": "", "amuna_shop_building": "", "nascent_gate_closed": "",
                   "nascent_gate_open": "", "health_pot_img": "", "energy_pot_img": "", "basic_robes_img": "",
                   "basic_armor_img": "", "basic_tunic_img": "", "basic_staff_img": "", "basic_sword_img": "",
                   "basic_bow_img": "", "bone_dust_img": "", "shiny_rock_img": "", "temp_img": "",
                   "info_health_pot_img": "", "info_energy_pot_img": "", "info_basic_robes_img": "",
                   "info_basic_armor_img": "", "info_basic_tunic_img": "", "info_basic_staff_img": "",
                   "info_basic_sword_img": "", "info_basic_bow_img": "", "info_bone_dust_img": "",
                   "info_shiny_rock_img": "", "b_health_pot_img": "", "b_energy_pot_img": "",
                   "b_basic_robes_img": "", "b_basic_armor_img": "", "b_basic_tunic_img": "",
                   "b_basic_staff_img": "", "b_basic_sword_img": "", "b_basic_bow_img": "",
                   "s_health_pot_img": "", "s_energy_pot_img": "", "s_basic_robes_img": "",
                   "s_basic_armor_img": "", "s_basic_tunic_img": "", "s_basic_staff_img": "",
                   "s_basic_sword_img": "", "s_basic_bow_img": "", "s_bone_dust_img": "", "s_shiny_rock_img": "",
                   "character_window_img": "", "journal_window_img": "", "mage_book_img": "",
                   "fighter_book_img": "", "scout_book_img": "", "new_game_img": "", "continue_img": "",
                   "main high": "", "skill high": "", "book high": "", "close high": "", "save hearth high": "",
                   "item high": "", "start high": "", "race high": "", "begin high": "", "role high": "",
                   "amuna_button_img": "", "nuldar_button_img": "", "sorae_button_img": "",
                   "character_button_img": "", "journal_button_img": "", "buy_button_img": "", "back_button_img": "",
                   "rest_button_img": "", "quest_button_img": "", "leave_button_img": "", "accept_button_img": "",
                   "decline_button_img": "", "yes_button_img": "", "no_button_img": "", "use_button_img": "",
                   "equip_button_img": "", "upgrade_button_img": "", "mage_attack_button_img": "",
                   "fighter_attack_button_img": "", "scout_attack_button_img": "", "ok_button_img": "",
                   "no_role_attack_button_img": "", "barrier_button_img": "", "strike_button_img": "",
                   "sense_button_img": "", "save_button_img": "", "map_button_img": "",
                   "mage_select_button_img": "", "fighter_select_button_img": "", "scout_select_button_img": "",
                   "offense_select_button_img": "", "defense_select_button_img": "", "garan_quest": "",
                   "maurelle_quest": "", "torune_quest": "", "celeste_quest": "", "garan_complete": "",
                   "maurelle_complete": "", "celeste_complete": "", "torune_complete": "", "quest_start_star": "",
                   "quest_progress_star": "", "quest_complete_star": "", "star_00": "", "star_01": "",
                   "star_02": "", "star_03": "", "star_04": "", "gear_popup": "", "health_popup": "",
                   "knowledge_popup": "", "save_popup": "", "quest_popup": "", "save_not_found": "",
                   "drop_popup": "", "pine_logs_img": "", "pine_logs_high_img": "", "guide_basics_quest_img": "",
                   "guide_basics_battle_img": "", "guide_basics_role_img": "", "guide_basics_upgrades_img": "",
                   "shop_cat_pet_img": "", "academia_cat_pet_img": "", "stardust_star_01": "", "stardust_star_02": "",
                   "stardust_star_03": "", "stardust_star_04": "", "hp_0": "", "hp_1": "", "hp_2": "", "hp_3": "",
                   "hp_4": "", "hp_5": "", "hp_6": "", "hp_7": "", "hp_8": "", "hp_9": "",
                   "hp_10": "", "hp_11": "", "hp_12": "", "hp_13": "", "hp_14": "", "hp_15": "",
                   "hp_16": "", "hp_17": "", "hp_18": "", "hp_19": "", "hp_20": "", "hp_21": "",
                   "hp_22": "", "hp_23": "", "hp_24": "", "hp_25": "", "hp_26": "", "hp_27": "",
                   "hp_28": "", "hp_29": "", "hp_30": "", "hp_31": "", "hp_32": "", "hp_33": "",
                   "hp_34": "", "hp_35": "", "hp_36": "", "hp_37": "", "hp_38": "", "hp_39": "",
                   "hp_40": "", "hp_41": "", "hp_42": "", "hp_43": "", "hp_44": "", "hp_45": "",
                   "hp_46": "", "hp_47": "", "hp_48": "", "hp_49": "", "hp_50": "", "hp_51": "",
                   "hp_52": "", "hp_53": "", "hp_54": "", "hp_55": "", "hp_56": "", "hp_57": "",
                   "hp_58": "", "hp_59": "", "hp_60": "", "hp_61": "", "hp_62": "", "hp_63": "",
                   "hp_64": "", "hp_65": "", "hp_66": "", "hp_67": "", "hp_68": "", "hp_69": "",
                   "hp_70": "", "hp_71": "", "hp_72": "", "hp_73": "", "hp_74": "", "hp_75": "",
                   "hp_76": "", "hp_77": "", "hp_78": "", "hp_79": "", "hp_80": "", "hp_81": "",
                   "hp_82": "", "hp_83": "", "hp_84": "", "hp_85": "", "hp_86": "", "hp_87": "",
                   "hp_88": "", "hp_89": "", "hp_90": "", "hp_91": "", "hp_92": "", "hp_93": "",
                   "hp_94": "", "hp_95": "", "hp_96": "", "hp_97": "", "hp_98": "", "hp_99": "",
                   "hp_100": "", "en_0": "", "en_1": "", "en_2": "", "en_3": "",
                   "en_4": "", "en_5": "", "en_6": "", "en_7": "", "en_8": "", "en_9": "",
                   "en_10": "", "en_11": "", "en_12": "", "en_13": "", "en_14": "", "en_15": "",
                   "en_16": "", "en_17": "", "en_18": "", "en_19": "", "en_20": "", "en_21": "",
                   "en_22": "", "en_23": "", "en_24": "", "en_25": "", "en_26": "", "en_27": "",
                   "en_28": "", "en_29": "", "en_30": "", "en_31": "", "en_32": "", "en_33": "",
                   "en_34": "", "en_35": "", "en_36": "", "en_37": "", "en_38": "", "en_39": "",
                   "en_40": "", "en_41": "", "en_42": "", "en_43": "", "en_44": "", "en_45": "",
                   "en_46": "", "en_47": "", "en_48": "", "en_49": "", "en_50": "", "en_51": "",
                   "en_52": "", "en_53": "", "en_54": "", "en_55": "", "en_56": "", "en_57": "",
                   "en_58": "", "en_59": "", "en_60": "", "en_61": "", "en_62": "", "en_63": "",
                   "en_64": "", "en_65": "", "en_66": "", "en_67": "", "en_68": "", "en_69": "",
                   "en_70": "", "en_71": "", "en_72": "", "en_73": "", "en_74": "", "en_75": "",
                   "en_76": "", "en_77": "", "en_78": "", "en_79": "", "en_80": "", "en_81": "",
                   "en_82": "", "en_83": "", "en_84": "", "en_85": "", "en_86": "", "en_87": "",
                   "en_88": "", "en_89": "", "en_90": "", "en_91": "", "en_92": "", "en_93": "",
                   "en_94": "", "en_95": "", "en_96": "", "en_97": "", "en_98": "", "en_99": "",
                   "en_100": "", "xp_0": "", "xp_1": "", "xp_2": "", "xp_3": "",
                   "xp_4": "", "xp_5": "", "xp_6": "", "xp_7": "", "xp_8": "", "xp_9": "",
                   "xp_10": "", "xp_11": "", "xp_12": "", "xp_13": "", "xp_14": "", "xp_15": "",
                   "xp_16": "", "xp_17": "", "xp_18": "", "xp_19": "", "xp_20": "", "xp_21": "",
                   "xp_22": "", "xp_23": "", "xp_24": "", "xp_25": "", "xp_26": "", "xp_27": "",
                   "xp_28": "", "xp_29": "", "xp_30": "", "xp_31": "", "xp_32": "", "xp_33": "",
                   "xp_34": "", "xp_35": "", "xp_36": "", "xp_37": "", "xp_38": "", "xp_39": "",
                   "xp_40": "", "xp_41": "", "xp_42": "", "xp_43": "", "xp_44": "", "xp_45": "",
                   "xp_46": "", "xp_47": "", "xp_48": "", "xp_49": "", "xp_50": "", "xp_51": "",
                   "xp_52": "", "xp_53": "", "xp_54": "", "xp_55": "", "xp_56": "", "xp_57": "",
                   "xp_58": "", "xp_59": "", "xp_60": "", "xp_61": "", "xp_62": "", "xp_63": "",
                   "xp_64": "", "xp_65": "", "xp_66": "", "xp_67": "", "xp_68": "", "xp_69": "",
                   "xp_70": "", "xp_71": "", "xp_72": "", "xp_73": "", "xp_74": "", "xp_75": "",
                   "xp_76": "", "xp_77": "", "xp_78": "", "xp_79": "", "xp_80": "", "xp_81": "",
                   "xp_82": "", "xp_83": "", "xp_84": "", "xp_85": "", "xp_86": "", "xp_87": "",
                   "xp_88": "", "xp_89": "", "xp_90": "", "xp_91": "", "xp_92": "", "xp_93": "",
                   "xp_94": "", "xp_95": "", "xp_96": "", "xp_97": "", "xp_98": "", "xp_99": "",
                   "xp_100": "", "arrow_up": "", "arrow_down": "", "arrow_right": "", "arrow_left": "",
                   "apothis_1": "", "apothis_2": "", "apothis_3": "", "apothis_4": "", "apothis_5": "",
                   "apothis_6": "", "rohir_river_screen": "", "water": "", "dungeon_entrance": "",
                   "world_map": "", "map_button": "", "map_button_high": "", "amuna_location": "",
                   "nuldar_location": "", "sorae_location": "", "stardust_battle": "", "ghoul attacking star": "",
                   "nede_big": "", "reservoir_a_screen": "", "reservoir_b_screen": "", "dungeon_wall_1": "",
                   "dungeon_wall_2": "", "dungeon_crate": "", "dungeon_switch_inactive": "", "dungeon_gate": "",
                   "dungeon_switch_active": "", "dungeon_switch_full": "", "dungeon_teleporter": "",
                   "dungeon_drop_wall": "", "chorizon": "", "muchador": "", "muchador_dark": "", "muchador_crate": "",
                   "reservoir_battle_screen": "", "chorizon_battle": "", "muchador_battle": "", "muchador_arena": "",
                   "chorizon_attack": "", "muchador_attack": "", "key image": "", "info_boss_key_img": "",
                   "skip_button_img": "", "reservoir_passage": "", "reservoir_c_screen": "", "dungeon_chest": "",
                   "dungeon_chest_open": "", "gloves": "", "info_gloves": "", "rock_img": "", "reservoir_exit": "",
                   "nuldar_herb_building": "", "nuldar_inn_building": "", "nuldar_shop_building": "",
                   "reservoir_enter": "", "korlok_hearth_screen": "", "magmon": "", "bandile": "", "mines_entrance": "",
                   "korlok_battle_screen": "", "magmon_battle": "", "magmon_attack": "", "bandile_battle": "",
                   "bandile_attack": "", "korlok_mines": "", "mines_wall": "", "mines_light": "",
                   "mines_battle_screen": "", "voruke_interaction": "", "zerah_interaction": "", "voruke_quest": "",
                   "voruke_complete": "", "zerah_quest": "", "zerah_complete": "", "ember": "", "band": "", "flow": "",
                   "magmon_high": "", "bandile_high": "", "info_ember": "", "info_band": "", "info_flow": "",
                   "s_ember_img": "", "s_band_img": "", "korlok_shop_screen": "", "korlok_inn_screen": "",
                   "korlok_mountains": "", "korlok_apothecary": "", "building_npc_star_available": "",
                   "building_npc_star_progress": "", "building_npc_star_complete": "", "sprite_ore_img": "",
                   "mountain_trail_bg": "", "terra_mountains": "", "terra_cave": ""}

    # non sprite sheets ------------------------------------------------------------------------------------------------
    a_char_screen = pygame.image.load(resource_path('resources/art/screen_amuna_character_select.png')).convert_alpha()
    n_char_screen = pygame.image.load(resource_path('resources/art/screen_nuldar_character_select.png')).convert_alpha()
    s_char_screen = pygame.image.load(resource_path('resources/art/screen_sorae_character_select.png')).convert_alpha()
    nascent_grove_screen = pygame.image.load(resource_path('resources/art/bg_nascent_grove.png')).convert_alpha()
    stardust_cove_screen = pygame.image.load(resource_path('resources/art/bg_stardust_post.png')).convert_alpha()
    stardust_post_screen = pygame.image.load(resource_path('resources/art/bg_stardust_inn.png')).convert_alpha()
    star_battle_screen = pygame.image.load(resource_path('resources/art/bg_stardust_battle_screen.png')).convert_alpha()
    seldon_bg_screen = pygame.image.load(resource_path('resources/art/bg_seldon_district.png')).convert_alpha()
    korlok_bg_screen = pygame.image.load(resource_path('resources/art/bg_korlok_district.png')).convert_alpha()
    korlok_mines_screen = pygame.image.load(resource_path('resources/art/bg_korlok_mines.png')).convert_alpha()
    korlok_battle_screen = pygame.image.load(resource_path('resources/art/bg_korlok_battle_screen.png')).convert_alpha()
    korlok_shop_screen = pygame.image.load(resource_path('resources/art/bg_korlok_shop.png')).convert_alpha()
    korlok_inn_screen = pygame.image.load(resource_path('resources/art/bg_korlok_inn.png')).convert_alpha()
    korlok_apothecary = pygame.image.load(resource_path('resources/art/bg_korlok_apothecary.png')).convert_alpha()
    mountain_trail_bg = pygame.image.load(resource_path('resources/art/bg_mountain_trail.png')).convert_alpha()
    mines_battle_screen = pygame.image.load(resource_path('resources/art/bg_mines_battle.png')).convert_alpha()
    rohir_river_screen = pygame.image.load(resource_path('resources/art/bg_rohir_river.png')).convert_alpha()
    reservoir_a_screen = pygame.image.load(resource_path('resources/art/bg_reservoir_a.png')).convert_alpha()
    reservoir_b_screen = pygame.image.load(resource_path('resources/art/bg_reservoir_b.png')).convert_alpha()
    reservoir_c_screen = pygame.image.load(resource_path('resources/art/bg_reservoir_c.png')).convert_alpha()
    reservoir_battle = pygame.image.load(resource_path('resources/art/bg_reservoir_battle_screen.png')).convert_alpha()
    seldon_battle_screen = pygame.image.load(resource_path('resources/art/bg_seldon_battle_screen.png')).convert_alpha()
    seldon_shop_screen = pygame.image.load(resource_path('resources/art/bg_seldon_shop.png')).convert_alpha()
    seldon_inn_screen = pygame.image.load(resource_path('resources/art/bg_seldon_inn.png')).convert_alpha()
    seldon_academia_screen = pygame.image.load(resource_path('resources/art/bg_seldon_academia.png')).convert_alpha()
    seldon_hearth_screen = pygame.image.load(resource_path('resources/art/screen_seldon_hearth.png')).convert_alpha()
    korlok_hearth_screen = pygame.image.load(resource_path('resources/art/screen_korlok_hearth.png')).convert_alpha()
    game_over_screen = pygame.image.load(resource_path('resources/art/screen_game_over.png')).convert_alpha()
    start_screen = pygame.image.load(resource_path('resources/art/screen_start.png')).convert_alpha()
    nera_sleep_screen = pygame.image.load(resource_path('resources/art/screen_nera_sleep.png')).convert_alpha()
    bar_backdrop = pygame.image.load(resource_path('resources/art/overlay_status_bar_backdrop.png')).convert_alpha()
    enemy_status = pygame.image.load(resource_path('resources/art/overlay_enemy_status_backdrop.png')).convert_alpha()
    enemy_bar_backdrop = pygame.image.load(resource_path('resources/art/overlay_enemy_status_bar.png')).convert_alpha()
    buy_inventory = pygame.image.load(resource_path('resources/art/overlay_buy_inventory.png')).convert_alpha()
    message_box = pygame.image.load(resource_path('resources/art/overlay_message_box.png')).convert_alpha()
    pine_tree = pygame.image.load(resource_path('resources/art/sprite_pine_tree.png')).convert_alpha()
    rohir_gate = pygame.image.load(resource_path('resources/art/overlay_rohir_gate.png')).convert_alpha()
    lets_go_button = pygame.image.load(resource_path('resources/art/button_lets_go.png')).convert_alpha()
    learn_button = pygame.image.load(resource_path('resources/art/overlay_learn.png')).convert_alpha()
    skill_learn_button = pygame.image.load(resource_path('resources/art/overlay_skill_learn.png')).convert_alpha()
    nascent_gate_popup = pygame.image.load(resource_path('resources/art/popup_nascent_gate.png')).convert_alpha()
    level_up = pygame.image.load(resource_path('resources/art/popup_level_up.png')).convert_alpha()
    close_button = pygame.image.load(resource_path('resources/art/button_close.png')).convert_alpha()
    knowledge_window = pygame.image.load(resource_path('resources/art/overlay_knowledge.png')).convert_alpha()
    skill_bar = pygame.image.load(resource_path('resources/art/overlay_skill_bar.png')).convert_alpha()
    start_button = pygame.image.load(resource_path('resources/art/button_start.png')).convert_alpha()
    npc_name_plate = pygame.image.load(resource_path('resources/art/overlay_npc_name_plate.png')).convert_alpha()
    char_select_overlay = pygame.image.load(resource_path('resources/art/overlay_character_select.png')).convert_alpha()
    role_selection_overlay = pygame.image.load(resource_path('resources/art/overlay_role_select.png')).convert_alpha()
    location_overlay = pygame.image.load(resource_path('resources/art/overlay_location.png')).convert_alpha()
    popup_loot = pygame.image.load(resource_path('resources/art/popup_loot.png')).convert_alpha()
    stardust_entrance = pygame.image.load(resource_path('resources/art/overlay_stardust_entrance.png')).convert_alpha()
    upgrade_overlay = pygame.image.load(resource_path('resources/art/overlay_upgrade_select.png')).convert_alpha()
    cat_pet_button_overlay = pygame.image.load(resource_path('resources/art/overlay_cat_pet.png')).convert_alpha()
    book_high = pygame.image.load(resource_path('resources/art/book_button_highlight.png')).convert_alpha()
    save_hearth_high = pygame.image.load(resource_path('resources/art/buttons_small_high.png')).convert_alpha()
    lets_go_high = pygame.image.load(resource_path('resources/art/button_lets_go_highlight.png')).convert_alpha()
    water = pygame.image.load(resource_path('resources/art/overlay_water.png')).convert_alpha()
    dungeon_entrance = pygame.image.load(resource_path('resources/art/overlay_dungeon_entrance.png')).convert_alpha()
    world_map = pygame.image.load(resource_path('resources/art/consona_region_map.png')).convert_alpha()
    world_map_button = pygame.image.load(resource_path('resources/art/button_map.png')).convert_alpha()
    world_map_button_high = pygame.image.load(resource_path('resources/art/button_map_highlight.png')).convert_alpha()
    nede_big = pygame.image.load(resource_path('resources/art/sprites_nede_big.png')).convert_alpha()
    dungeon_wall_1 = pygame.image.load(resource_path('resources/art/overlay_dungeon_wall_1.png')).convert_alpha()
    dungeon_wall_2 = pygame.image.load(resource_path('resources/art/overlay_dungeon_wall_2.png')).convert_alpha()
    dungeon_teleport = pygame.image.load(resource_path('resources/art/overlay_dungeon_teleporter.png')).convert_alpha()
    dungeon_drop_wall = pygame.image.load(resource_path('resources/art/overlay_dungeon_drop_wall.png')).convert_alpha()
    dungeon_gate = pygame.image.load(resource_path('resources/art/overlay_dungeon_gate.png')).convert_alpha()
    muchador_arena = pygame.image.load(resource_path('resources/art/overlay_muchador_arena.png')).convert_alpha()
    muchador_crate = pygame.image.load(resource_path('resources/art/overlay_muchador_crate.png')).convert_alpha()
    reservoir_passage = pygame.image.load(resource_path('resources/art/overlay_reservoir_passage.png')).convert_alpha()
    rock_img = pygame.image.load(resource_path('resources/art/sprite_rock.png')).convert_alpha()
    reservoir_exit = pygame.image.load(resource_path('resources/art/overlay_reservoir_exit.png')).convert_alpha()
    reservoir_enter = pygame.image.load(resource_path('resources/art/overlay_reservoir_enter.png')).convert_alpha()
    mines_entrance = pygame.image.load(resource_path('resources/art/overlay_mines_entrance.png')).convert_alpha()
    mines_wall = pygame.image.load(resource_path('resources/art/overlay_mines_wall.png')).convert_alpha()
    mines_light = pygame.image.load(resource_path('resources/art/overlay_mines_light.png')).convert_alpha()
    korlok_mountains = pygame.image.load(resource_path('resources/art/overlay_korlok_mountains.png')).convert_alpha()
    terra_mountains = pygame.image.load(resource_path('resources/art/'
                                                      'overlay_terra_trail_mountains.png')).convert_alpha()
    terra_cave = pygame.image.load(resource_path('resources/art/overlay_trail_cave.png')).convert_alpha()

    apothis_scene_1 = pygame.image.load(resource_path('resources/art/cutscene_apothis_1.png')).convert_alpha()
    apothis_scene_2 = pygame.image.load(resource_path('resources/art/cutscene_apothis_2.png')).convert_alpha()
    apothis_scene_3 = pygame.image.load(resource_path('resources/art/cutscene_apothis_3.png')).convert_alpha()
    apothis_scene_4 = pygame.image.load(resource_path('resources/art/cutscene_apothis_4.png')).convert_alpha()
    apothis_scene_5 = pygame.image.load(resource_path('resources/art/cutscene_apothis_5.png')).convert_alpha()
    apothis_scene_6 = pygame.image.load(resource_path('resources/art/cutscene_apothis_6.png')).convert_alpha()

    color_keys = [bar_backdrop, enemy_status, enemy_bar_backdrop, buy_inventory, message_box, pine_tree,
                  rohir_gate, lets_go_button, learn_button, skill_learn_button, nascent_gate_popup, level_up,
                  close_button, knowledge_window, skill_bar, start_button, npc_name_plate, char_select_overlay,
                  role_selection_overlay, location_overlay, popup_loot, stardust_entrance, book_high,
                  upgrade_overlay, cat_pet_button_overlay, save_hearth_high, lets_go_high, dungeon_entrance,
                  world_map_button, world_map_button_high, nede_big, dungeon_wall_1, dungeon_wall_2, dungeon_gate,
                  muchador_crate, reservoir_passage, rock_img, reservoir_exit, reservoir_enter, mines_entrance,
                  mines_wall, mines_light, korlok_mountains, terra_mountains, terra_cave]
    for image in color_keys:
        image.set_colorkey((255, 255, 255))

    loaded_dict["a_char_screen"] = a_char_screen
    loaded_dict["n_char_screen"] = n_char_screen
    loaded_dict["s_char_screen"] = s_char_screen
    loaded_dict["nascent_grove_screen"] = nascent_grove_screen
    loaded_dict["stardust_cove_screen"] = stardust_cove_screen
    loaded_dict["stardust_post_screen"] = stardust_post_screen
    loaded_dict["star_battle_screen"] = star_battle_screen
    loaded_dict["seldon_bg_screen"] = seldon_bg_screen
    loaded_dict["korlok_bg_screen"] = korlok_bg_screen
    loaded_dict["rohir_river_screen"] = rohir_river_screen
    loaded_dict["reservoir_a_screen"] = reservoir_a_screen
    loaded_dict["reservoir_b_screen"] = reservoir_b_screen
    loaded_dict["reservoir_c_screen"] = reservoir_c_screen
    loaded_dict["reservoir_battle_screen"] = reservoir_battle
    loaded_dict["seldon_battle_screen"] = seldon_battle_screen
    loaded_dict["korlok_battle_screen"] = korlok_battle_screen
    loaded_dict["mines_battle_screen"] = mines_battle_screen
    loaded_dict["seldon_shop_screen"] = seldon_shop_screen
    loaded_dict["korlok_shop_screen"] = korlok_shop_screen
    loaded_dict["seldon_inn_screen"] = seldon_inn_screen
    loaded_dict["korlok_inn_screen"] = korlok_inn_screen
    loaded_dict["mountain_trail_bg"] = mountain_trail_bg
    loaded_dict["seldon_academia_screen"] = seldon_academia_screen
    loaded_dict["seldon_hearth_screen"] = seldon_hearth_screen
    loaded_dict["game_over_screen"] = game_over_screen
    loaded_dict["start_screen"] = start_screen
    loaded_dict["nera_sleep_screen"] = nera_sleep_screen
    loaded_dict["bar_backdrop"] = bar_backdrop
    loaded_dict["enemy_status"] = enemy_status
    loaded_dict["enemy_bar_backdrop"] = enemy_bar_backdrop
    loaded_dict["buy_inventory"] = buy_inventory
    loaded_dict["message_box"] = message_box
    loaded_dict["pine_tree"] = pine_tree
    loaded_dict["rohir_gate"] = rohir_gate
    loaded_dict["lets_go_button"] = lets_go_button
    loaded_dict["learn_button"] = learn_button
    loaded_dict["skill_learn_button"] = skill_learn_button
    loaded_dict["nascent_gate_popup"] = nascent_gate_popup
    loaded_dict["level_up"] = level_up
    loaded_dict["close_button"] = close_button
    loaded_dict["knowledge_window"] = knowledge_window
    loaded_dict["skill_bar"] = skill_bar
    loaded_dict["start_button"] = start_button
    loaded_dict["npc_name_plate"] = npc_name_plate
    loaded_dict["char_select_overlay"] = char_select_overlay
    loaded_dict["role_selection_overlay"] = role_selection_overlay
    loaded_dict["location_overlay"] = location_overlay
    loaded_dict["popup_loot"] = popup_loot
    loaded_dict["stardust_entrance"] = stardust_entrance
    loaded_dict["upgrade_overlay"] = upgrade_overlay
    loaded_dict["cat_pet_button_overlay"] = cat_pet_button_overlay
    loaded_dict["book_high"] = book_high
    loaded_dict["save hearth high"] = save_hearth_high
    loaded_dict["lets_go_button_high"] = lets_go_high
    loaded_dict["apothis_1"] = apothis_scene_1
    loaded_dict["apothis_2"] = apothis_scene_2
    loaded_dict["apothis_3"] = apothis_scene_3
    loaded_dict["apothis_4"] = apothis_scene_4
    loaded_dict["apothis_5"] = apothis_scene_5
    loaded_dict["apothis_6"] = apothis_scene_6
    loaded_dict["water"] = water
    loaded_dict["dungeon_entrance"] = dungeon_entrance
    loaded_dict["world_map"] = world_map
    loaded_dict["map_button"] = world_map_button
    loaded_dict["map_button_high"] = world_map_button_high
    loaded_dict["nede_big"] = nede_big
    loaded_dict["dungeon_wall_1"] = dungeon_wall_1
    loaded_dict["dungeon_wall_2"] = dungeon_wall_2
    loaded_dict["dungeon_teleporter"] = dungeon_teleport
    loaded_dict["dungeon_drop_wall"] = dungeon_drop_wall
    loaded_dict["dungeon_gate"] = dungeon_gate
    loaded_dict["muchador_arena"] = muchador_arena
    loaded_dict["muchador_crate"] = muchador_crate
    loaded_dict["reservoir_passage"] = reservoir_passage
    loaded_dict["rock_img"] = rock_img
    loaded_dict["reservoir_exit"] = reservoir_exit
    loaded_dict["reservoir_enter"] = reservoir_enter
    loaded_dict["korlok_hearth_screen"] = korlok_hearth_screen
    loaded_dict["mines_entrance"] = mines_entrance
    loaded_dict["korlok_mines"] = korlok_mines_screen
    loaded_dict["mines_wall"] = mines_wall
    loaded_dict["mines_light"] = mines_light
    loaded_dict["korlok_mountains"] = korlok_mountains
    loaded_dict["korlok_apothecary"] = korlok_apothecary
    loaded_dict["terra_mountains"] = terra_mountains
    loaded_dict["terra_cave"] = terra_cave

    # sprite sheets ----------------------------------------------------------------------------------------------------
    # create character screen character race selections ----------------------------------------------------------------
    character_selections_url = resource_path('resources/art/overlay_character_selections.png')
    character_selections_sheet = sprite_sheet((250, 350), character_selections_url)
    loaded_dict["amuna_character_img"] = character_selections_sheet[0]
    loaded_dict["nuldar_character_img"] = character_selections_sheet[1]
    loaded_dict["sorae_character_img"] = character_selections_sheet[2]
    # race selection lore overlays -------------------------------------------------------------------------------------
    race_lore_url = resource_path('resources/art/overlays_race_select.png')
    race_lore_sheet = sprite_sheet((278, 372), race_lore_url)
    loaded_dict["amuna_overlay_img"] = race_lore_sheet[0]
    loaded_dict["nuldar_overlay_img"] = race_lore_sheet[1]
    loaded_dict["sorae_overlay_img"] = race_lore_sheet[2]
    # character name input box -----------------------------------------------------------------------------------------
    name_input_url = resource_path('resources/art/overlay_name_input.png')
    name_input_sheet = sprite_sheet((300, 50), name_input_url)
    loaded_dict["name_input_img"] = name_input_sheet[0]
    loaded_dict["name_input_empty_img"] = name_input_sheet[1]
    # player no role amuna race ----------------------------------------------------------------------------------------
    player_no_role_amuna_down_url = resource_path('resources/art/player_no_role_amuna_down.png')
    player_no_role_amuna_down_sheet = sprite_sheet((50, 75), player_no_role_amuna_down_url)
    loaded_dict["player_no_role_amuna_down_1"] = player_no_role_amuna_down_sheet[0]
    loaded_dict["player_no_role_amuna_down_2"] = player_no_role_amuna_down_sheet[1]
    loaded_dict["player_no_role_amuna_down_3"] = player_no_role_amuna_down_sheet[2]
    loaded_dict["player_no_role_amuna_down_4"] = player_no_role_amuna_down_sheet[3]
    player_no_role_amuna_up_url = resource_path('resources/art/player_no_role_amuna_up.png')
    player_no_role_amuna_up_sheet = sprite_sheet((50, 75), player_no_role_amuna_up_url)
    loaded_dict["player_no_role_amuna_up_1"] = player_no_role_amuna_up_sheet[0]
    loaded_dict["player_no_role_amuna_up_2"] = player_no_role_amuna_up_sheet[1]
    loaded_dict["player_no_role_amuna_up_3"] = player_no_role_amuna_up_sheet[2]
    loaded_dict["player_no_role_amuna_up_4"] = player_no_role_amuna_up_sheet[3]
    player_no_role_amuna_left_url = resource_path('resources/art/player_no_role_amuna_left.png')
    player_no_role_amuna_left_sheet = sprite_sheet((50, 75), player_no_role_amuna_left_url)
    loaded_dict["player_no_role_amuna_left_1"] = player_no_role_amuna_left_sheet[0]
    loaded_dict["player_no_role_amuna_left_2"] = player_no_role_amuna_left_sheet[1]
    loaded_dict["player_no_role_amuna_left_3"] = player_no_role_amuna_left_sheet[2]
    loaded_dict["player_no_role_amuna_left_4"] = player_no_role_amuna_left_sheet[3]
    player_no_role_amuna_right_url = resource_path('resources/art/player_no_role_amuna_right.png')
    player_no_role_amuna_right_sheet = sprite_sheet((50, 75), player_no_role_amuna_right_url)
    loaded_dict["player_no_role_amuna_right_1"] = player_no_role_amuna_right_sheet[0]
    loaded_dict["player_no_role_amuna_right_2"] = player_no_role_amuna_right_sheet[1]
    loaded_dict["player_no_role_amuna_right_3"] = player_no_role_amuna_right_sheet[2]
    loaded_dict["player_no_role_amuna_right_4"] = player_no_role_amuna_right_sheet[3]
    # player no role sorae race ----------------------------------------------------------------------------------------
    player_no_role_sorae_down_url = resource_path('resources/art/player_no_role_sorae_down.png')
    player_no_role_sorae_down_sheet = sprite_sheet((50, 75), player_no_role_sorae_down_url)
    loaded_dict["player_no_role_sorae_down_1"] = player_no_role_sorae_down_sheet[0]
    loaded_dict["player_no_role_sorae_down_2"] = player_no_role_sorae_down_sheet[1]
    loaded_dict["player_no_role_sorae_down_3"] = player_no_role_sorae_down_sheet[2]
    loaded_dict["player_no_role_sorae_down_4"] = player_no_role_sorae_down_sheet[3]
    player_no_role_sorae_up_url = resource_path('resources/art/player_no_role_sorae_up.png')
    player_no_role_sorae_up_sheet = sprite_sheet((50, 75), player_no_role_sorae_up_url)
    loaded_dict["player_no_role_sorae_up_1"] = player_no_role_sorae_up_sheet[0]
    loaded_dict["player_no_role_sorae_up_2"] = player_no_role_sorae_up_sheet[1]
    loaded_dict["player_no_role_sorae_up_3"] = player_no_role_sorae_up_sheet[2]
    loaded_dict["player_no_role_sorae_up_4"] = player_no_role_sorae_up_sheet[3]
    player_no_role_sorae_left_url = resource_path('resources/art/player_no_role_sorae_left.png')
    player_no_role_sorae_left_sheet = sprite_sheet((50, 75), player_no_role_sorae_left_url)
    loaded_dict["player_no_role_sorae_left_1"] = player_no_role_sorae_left_sheet[0]
    loaded_dict["player_no_role_sorae_left_2"] = player_no_role_sorae_left_sheet[1]
    loaded_dict["player_no_role_sorae_left_3"] = player_no_role_sorae_left_sheet[2]
    loaded_dict["player_no_role_sorae_left_4"] = player_no_role_sorae_left_sheet[3]
    player_no_role_sorae_right_url = resource_path('resources/art/player_no_role_sorae_right.png')
    player_no_role_sorae_right_sheet = sprite_sheet((50, 75), player_no_role_sorae_right_url)
    loaded_dict["player_no_role_sorae_right_1"] = player_no_role_sorae_right_sheet[0]
    loaded_dict["player_no_role_sorae_right_2"] = player_no_role_sorae_right_sheet[1]
    loaded_dict["player_no_role_sorae_right_3"] = player_no_role_sorae_right_sheet[2]
    loaded_dict["player_no_role_sorae_right_4"] = player_no_role_sorae_right_sheet[3]
    # player no role nuldar race ---------------------------------------------------------------------------------------
    player_no_role_nuldar_down_url = resource_path('resources/art/player_no_role_nuldar_down.png')
    player_no_role_nuldar_down_sheet = sprite_sheet((50, 75), player_no_role_nuldar_down_url)
    loaded_dict["player_no_role_nuldar_down_1"] = player_no_role_nuldar_down_sheet[0]
    loaded_dict["player_no_role_nuldar_down_2"] = player_no_role_nuldar_down_sheet[1]
    loaded_dict["player_no_role_nuldar_down_3"] = player_no_role_nuldar_down_sheet[2]
    loaded_dict["player_no_role_nuldar_down_4"] = player_no_role_nuldar_down_sheet[3]
    player_no_role_nuldar_up_url = resource_path('resources/art/player_no_role_nuldar_up.png')
    player_no_role_nuldar_up_sheet = sprite_sheet((50, 75), player_no_role_nuldar_up_url)
    loaded_dict["player_no_role_nuldar_up_1"] = player_no_role_nuldar_up_sheet[0]
    loaded_dict["player_no_role_nuldar_up_2"] = player_no_role_nuldar_up_sheet[1]
    loaded_dict["player_no_role_nuldar_up_3"] = player_no_role_nuldar_up_sheet[2]
    loaded_dict["player_no_role_nuldar_up_4"] = player_no_role_nuldar_up_sheet[3]
    player_no_role_nuldar_left_url = resource_path('resources/art/player_no_role_nuldar_left.png')
    player_no_role_nuldar_left_sheet = sprite_sheet((50, 75), player_no_role_nuldar_left_url)
    loaded_dict["player_no_role_nuldar_left_1"] = player_no_role_nuldar_left_sheet[0]
    loaded_dict["player_no_role_nuldar_left_2"] = player_no_role_nuldar_left_sheet[1]
    loaded_dict["player_no_role_nuldar_left_3"] = player_no_role_nuldar_left_sheet[2]
    loaded_dict["player_no_role_nuldar_left_4"] = player_no_role_nuldar_left_sheet[3]
    player_no_role_nuldar_right_url = resource_path('resources/art/player_no_role_nuldar_right.png')
    player_no_role_nuldar_right_sheet = sprite_sheet((50, 75), player_no_role_nuldar_right_url)
    loaded_dict["player_no_role_nuldar_right_1"] = player_no_role_nuldar_right_sheet[0]
    loaded_dict["player_no_role_nuldar_right_2"] = player_no_role_nuldar_right_sheet[1]
    loaded_dict["player_no_role_nuldar_right_3"] = player_no_role_nuldar_right_sheet[2]
    loaded_dict["player_no_role_nuldar_right_4"] = player_no_role_nuldar_right_sheet[3]
    # player mage amuna race -------------------------------------------------------------------------------------------
    player_mage_amuna_down_url = resource_path('resources/art/player_mage_amuna_down.png')
    player_mage_amuna_down_sheet = sprite_sheet((50, 75), player_mage_amuna_down_url)
    loaded_dict["player_mage_amuna_down_1"] = player_mage_amuna_down_sheet[0]
    loaded_dict["player_mage_amuna_down_2"] = player_mage_amuna_down_sheet[1]
    loaded_dict["player_mage_amuna_down_3"] = player_mage_amuna_down_sheet[2]
    loaded_dict["player_mage_amuna_down_4"] = player_mage_amuna_down_sheet[3]
    player_mage_amuna_up_url = resource_path('resources/art/player_mage_amuna_up.png')
    player_mage_amuna_up_sheet = sprite_sheet((50, 75), player_mage_amuna_up_url)
    loaded_dict["player_mage_amuna_up_1"] = player_mage_amuna_up_sheet[0]
    loaded_dict["player_mage_amuna_up_2"] = player_mage_amuna_up_sheet[1]
    loaded_dict["player_mage_amuna_up_3"] = player_mage_amuna_up_sheet[2]
    loaded_dict["player_mage_amuna_up_4"] = player_mage_amuna_up_sheet[3]
    player_mage_amuna_left_url = resource_path('resources/art/player_mage_amuna_left.png')
    player_mage_amuna_left_sheet = sprite_sheet((50, 75), player_mage_amuna_left_url)
    loaded_dict["player_mage_amuna_left_1"] = player_mage_amuna_left_sheet[0]
    loaded_dict["player_mage_amuna_left_2"] = player_mage_amuna_left_sheet[1]
    loaded_dict["player_mage_amuna_left_3"] = player_mage_amuna_left_sheet[2]
    loaded_dict["player_mage_amuna_left_4"] = player_mage_amuna_left_sheet[3]
    player_mage_amuna_right_url = resource_path('resources/art/player_mage_amuna_right.png')
    player_mage_amuna_right_sheet = sprite_sheet((50, 75), player_mage_amuna_right_url)
    loaded_dict["player_mage_amuna_right_1"] = player_mage_amuna_right_sheet[0]
    loaded_dict["player_mage_amuna_right_2"] = player_mage_amuna_right_sheet[1]
    loaded_dict["player_mage_amuna_right_3"] = player_mage_amuna_right_sheet[2]
    loaded_dict["player_mage_amuna_right_4"] = player_mage_amuna_right_sheet[3]
    # player mage nuldar race ------------------------------------------------------------------------------------------
    player_mage_nuldar_down_url = resource_path('resources/art/player_mage_nuldar_down.png')
    player_mage_nuldar_down_sheet = sprite_sheet((50, 75), player_mage_nuldar_down_url)
    loaded_dict["player_mage_nuldar_down_1"] = player_mage_nuldar_down_sheet[0]
    loaded_dict["player_mage_nuldar_down_2"] = player_mage_nuldar_down_sheet[1]
    loaded_dict["player_mage_nuldar_down_3"] = player_mage_nuldar_down_sheet[2]
    loaded_dict["player_mage_nuldar_down_4"] = player_mage_nuldar_down_sheet[3]
    player_mage_nuldar_up_url = resource_path('resources/art/player_mage_nuldar_up.png')
    player_mage_nuldar_up_sheet = sprite_sheet((50, 75), player_mage_nuldar_up_url)
    loaded_dict["player_mage_nuldar_up_1"] = player_mage_nuldar_up_sheet[0]
    loaded_dict["player_mage_nuldar_up_2"] = player_mage_nuldar_up_sheet[1]
    loaded_dict["player_mage_nuldar_up_3"] = player_mage_nuldar_up_sheet[2]
    loaded_dict["player_mage_nuldar_up_4"] = player_mage_nuldar_up_sheet[3]
    player_mage_nuldar_left_url = resource_path('resources/art/player_mage_nuldar_left.png')
    player_mage_nuldar_left_sheet = sprite_sheet((50, 75), player_mage_nuldar_left_url)
    loaded_dict["player_mage_nuldar_left_1"] = player_mage_nuldar_left_sheet[0]
    loaded_dict["player_mage_nuldar_left_2"] = player_mage_nuldar_left_sheet[1]
    loaded_dict["player_mage_nuldar_left_3"] = player_mage_nuldar_left_sheet[2]
    loaded_dict["player_mage_nuldar_left_4"] = player_mage_nuldar_left_sheet[3]
    player_mage_nuldar_right_url = resource_path('resources/art/player_mage_nuldar_right.png')
    player_mage_nuldar_right_sheet = sprite_sheet((50, 75), player_mage_nuldar_right_url)
    loaded_dict["player_mage_nuldar_right_1"] = player_mage_nuldar_right_sheet[0]
    loaded_dict["player_mage_nuldar_right_2"] = player_mage_nuldar_right_sheet[1]
    loaded_dict["player_mage_nuldar_right_3"] = player_mage_nuldar_right_sheet[2]
    loaded_dict["player_mage_nuldar_right_4"] = player_mage_nuldar_right_sheet[3]
    # player mage sorae race -------------------------------------------------------------------------------------------
    player_mage_sorae_down_url = resource_path('resources/art/player_mage_sorae_down.png')
    player_mage_sorae_down_sheet = sprite_sheet((50, 75), player_mage_sorae_down_url)
    loaded_dict["player_mage_sorae_down_1"] = player_mage_sorae_down_sheet[0]
    loaded_dict["player_mage_sorae_down_2"] = player_mage_sorae_down_sheet[1]
    loaded_dict["player_mage_sorae_down_3"] = player_mage_sorae_down_sheet[2]
    loaded_dict["player_mage_sorae_down_4"] = player_mage_sorae_down_sheet[3]
    player_mage_sorae_up_url = resource_path('resources/art/player_mage_sorae_up.png')
    player_mage_sorae_up_sheet = sprite_sheet((50, 75), player_mage_sorae_up_url)
    loaded_dict["player_mage_sorae_up_1"] = player_mage_sorae_up_sheet[0]
    loaded_dict["player_mage_sorae_up_2"] = player_mage_sorae_up_sheet[1]
    loaded_dict["player_mage_sorae_up_3"] = player_mage_sorae_up_sheet[2]
    loaded_dict["player_mage_sorae_up_4"] = player_mage_sorae_up_sheet[3]
    player_mage_sorae_left_url = resource_path('resources/art/player_mage_sorae_left.png')
    player_mage_sorae_left_sheet = sprite_sheet((50, 75), player_mage_sorae_left_url)
    loaded_dict["player_mage_sorae_left_1"] = player_mage_sorae_left_sheet[0]
    loaded_dict["player_mage_sorae_left_2"] = player_mage_sorae_left_sheet[1]
    loaded_dict["player_mage_sorae_left_3"] = player_mage_sorae_left_sheet[2]
    loaded_dict["player_mage_sorae_left_4"] = player_mage_sorae_left_sheet[3]
    player_mage_sorae_right_url = resource_path('resources/art/player_mage_sorae_right.png')
    player_mage_sorae_right_sheet = sprite_sheet((50, 75), player_mage_sorae_right_url)
    loaded_dict["player_mage_sorae_right_1"] = player_mage_sorae_right_sheet[0]
    loaded_dict["player_mage_sorae_right_2"] = player_mage_sorae_right_sheet[1]
    loaded_dict["player_mage_sorae_right_3"] = player_mage_sorae_right_sheet[2]
    loaded_dict["player_mage_sorae_right_4"] = player_mage_sorae_right_sheet[3]
    # player fighter amuna race ----------------------------------------------------------------------------------------
    player_fighter_amuna_down_url = resource_path('resources/art/player_fighter_amuna_down.png')
    player_fighter_amuna_down_sheet = sprite_sheet((50, 75), player_fighter_amuna_down_url)
    loaded_dict["player_fighter_amuna_down_1"] = player_fighter_amuna_down_sheet[0]
    loaded_dict["player_fighter_amuna_down_2"] = player_fighter_amuna_down_sheet[1]
    loaded_dict["player_fighter_amuna_down_3"] = player_fighter_amuna_down_sheet[2]
    loaded_dict["player_fighter_amuna_down_4"] = player_fighter_amuna_down_sheet[3]
    player_fighter_amuna_up_url = resource_path('resources/art/player_fighter_amuna_up.png')
    player_fighter_amuna_up_sheet = sprite_sheet((50, 75), player_fighter_amuna_up_url)
    loaded_dict["player_fighter_amuna_up_1"] = player_fighter_amuna_up_sheet[0]
    loaded_dict["player_fighter_amuna_up_2"] = player_fighter_amuna_up_sheet[1]
    loaded_dict["player_fighter_amuna_up_3"] = player_fighter_amuna_up_sheet[2]
    loaded_dict["player_fighter_amuna_up_4"] = player_fighter_amuna_up_sheet[3]
    player_fighter_amuna_left_url = resource_path('resources/art/player_fighter_amuna_left.png')
    player_fighter_amuna_left_sheet = sprite_sheet((50, 75), player_fighter_amuna_left_url)
    loaded_dict["player_fighter_amuna_left_1"] = player_fighter_amuna_left_sheet[0]
    loaded_dict["player_fighter_amuna_left_2"] = player_fighter_amuna_left_sheet[1]
    loaded_dict["player_fighter_amuna_left_3"] = player_fighter_amuna_left_sheet[2]
    loaded_dict["player_fighter_amuna_left_4"] = player_fighter_amuna_left_sheet[3]
    player_fighter_amuna_right_url = resource_path('resources/art/player_fighter_amuna_right.png')
    player_fighter_amuna_right_sheet = sprite_sheet((50, 75), player_fighter_amuna_right_url)
    loaded_dict["player_fighter_amuna_right_1"] = player_fighter_amuna_right_sheet[0]
    loaded_dict["player_fighter_amuna_right_2"] = player_fighter_amuna_right_sheet[1]
    loaded_dict["player_fighter_amuna_right_3"] = player_fighter_amuna_right_sheet[2]
    loaded_dict["player_fighter_amuna_right_4"] = player_fighter_amuna_right_sheet[3]
    # player fighter nuldar race ---------------------------------------------------------------------------------------
    player_fighter_nuldar_down_url = resource_path('resources/art/player_fighter_nuldar_down.png')
    player_fighter_nuldar_down_sheet = sprite_sheet((50, 75), player_fighter_nuldar_down_url)
    loaded_dict["player_fighter_nuldar_down_1"] = player_fighter_nuldar_down_sheet[0]
    loaded_dict["player_fighter_nuldar_down_2"] = player_fighter_nuldar_down_sheet[1]
    loaded_dict["player_fighter_nuldar_down_3"] = player_fighter_nuldar_down_sheet[2]
    loaded_dict["player_fighter_nuldar_down_4"] = player_fighter_nuldar_down_sheet[3]
    player_fighter_nuldar_up_url = resource_path('resources/art/player_fighter_nuldar_up.png')
    player_fighter_nuldar_up_sheet = sprite_sheet((50, 75), player_fighter_nuldar_up_url)
    loaded_dict["player_fighter_nuldar_up_1"] = player_fighter_nuldar_up_sheet[0]
    loaded_dict["player_fighter_nuldar_up_2"] = player_fighter_nuldar_up_sheet[1]
    loaded_dict["player_fighter_nuldar_up_3"] = player_fighter_nuldar_up_sheet[2]
    loaded_dict["player_fighter_nuldar_up_4"] = player_fighter_nuldar_up_sheet[3]
    player_fighter_nuldar_left_url = resource_path('resources/art/player_fighter_nuldar_left.png')
    player_fighter_nuldar_left_sheet = sprite_sheet((50, 75), player_fighter_nuldar_left_url)
    loaded_dict["player_fighter_nuldar_left_1"] = player_fighter_nuldar_left_sheet[0]
    loaded_dict["player_fighter_nuldar_left_2"] = player_fighter_nuldar_left_sheet[1]
    loaded_dict["player_fighter_nuldar_left_3"] = player_fighter_nuldar_left_sheet[2]
    loaded_dict["player_fighter_nuldar_left_4"] = player_fighter_nuldar_left_sheet[3]
    player_fighter_nuldar_right_url = resource_path('resources/art/player_fighter_nuldar_right.png')
    player_fighter_nuldar_right_sheet = sprite_sheet((50, 75), player_fighter_nuldar_right_url)
    loaded_dict["player_fighter_nuldar_right_1"] = player_fighter_nuldar_right_sheet[0]
    loaded_dict["player_fighter_nuldar_right_2"] = player_fighter_nuldar_right_sheet[1]
    loaded_dict["player_fighter_nuldar_right_3"] = player_fighter_nuldar_right_sheet[2]
    loaded_dict["player_fighter_nuldar_right_4"] = player_fighter_nuldar_right_sheet[3]
    # player fighter sorae race ----------------------------------------------------------------------------------------
    player_fighter_sorae_down_url = resource_path('resources/art/player_fighter_sorae_down.png')
    player_fighter_sorae_down_sheet = sprite_sheet((50, 75), player_fighter_sorae_down_url)
    loaded_dict["player_fighter_sorae_down_1"] = player_fighter_sorae_down_sheet[0]
    loaded_dict["player_fighter_sorae_down_2"] = player_fighter_sorae_down_sheet[1]
    loaded_dict["player_fighter_sorae_down_3"] = player_fighter_sorae_down_sheet[2]
    loaded_dict["player_fighter_sorae_down_4"] = player_fighter_sorae_down_sheet[3]
    player_fighter_sorae_up_url = resource_path('resources/art/player_fighter_sorae_up.png')
    player_fighter_sorae_up_sheet = sprite_sheet((50, 75), player_fighter_sorae_up_url)
    loaded_dict["player_fighter_sorae_up_1"] = player_fighter_sorae_up_sheet[0]
    loaded_dict["player_fighter_sorae_up_2"] = player_fighter_sorae_up_sheet[1]
    loaded_dict["player_fighter_sorae_up_3"] = player_fighter_sorae_up_sheet[2]
    loaded_dict["player_fighter_sorae_up_4"] = player_fighter_sorae_up_sheet[3]
    player_fighter_sorae_left_url = resource_path('resources/art/player_fighter_sorae_left.png')
    player_fighter_sorae_left_sheet = sprite_sheet((50, 75), player_fighter_sorae_left_url)
    loaded_dict["player_fighter_sorae_left_1"] = player_fighter_sorae_left_sheet[0]
    loaded_dict["player_fighter_sorae_left_2"] = player_fighter_sorae_left_sheet[1]
    loaded_dict["player_fighter_sorae_left_3"] = player_fighter_sorae_left_sheet[2]
    loaded_dict["player_fighter_sorae_left_4"] = player_fighter_sorae_left_sheet[3]
    player_fighter_sorae_right_url = resource_path('resources/art/player_fighter_sorae_right.png')
    player_fighter_sorae_right_sheet = sprite_sheet((50, 75), player_fighter_sorae_right_url)
    loaded_dict["player_fighter_sorae_right_1"] = player_fighter_sorae_right_sheet[0]
    loaded_dict["player_fighter_sorae_right_2"] = player_fighter_sorae_right_sheet[1]
    loaded_dict["player_fighter_sorae_right_3"] = player_fighter_sorae_right_sheet[2]
    loaded_dict["player_fighter_sorae_right_4"] = player_fighter_sorae_right_sheet[3]
    # player scout amuna race ------------------------------------------------------------------------------------------
    player_scout_amuna_down_url = resource_path('resources/art/player_scout_amuna_down.png')
    player_scout_amuna_down_sheet = sprite_sheet((50, 75), player_scout_amuna_down_url)
    loaded_dict["player_scout_amuna_down_1"] = player_scout_amuna_down_sheet[0]
    loaded_dict["player_scout_amuna_down_2"] = player_scout_amuna_down_sheet[1]
    loaded_dict["player_scout_amuna_down_3"] = player_scout_amuna_down_sheet[2]
    loaded_dict["player_scout_amuna_down_4"] = player_scout_amuna_down_sheet[3]
    player_scout_amuna_up_url = resource_path('resources/art/player_scout_amuna_up.png')
    player_scout_amuna_up_sheet = sprite_sheet((50, 75), player_scout_amuna_up_url)
    loaded_dict["player_scout_amuna_up_1"] = player_scout_amuna_up_sheet[0]
    loaded_dict["player_scout_amuna_up_2"] = player_scout_amuna_up_sheet[1]
    loaded_dict["player_scout_amuna_up_3"] = player_scout_amuna_up_sheet[2]
    loaded_dict["player_scout_amuna_up_4"] = player_scout_amuna_up_sheet[3]
    player_scout_amuna_left_url = resource_path('resources/art/player_scout_amuna_left.png')
    player_scout_amuna_left_sheet = sprite_sheet((50, 75), player_scout_amuna_left_url)
    loaded_dict["player_scout_amuna_left_1"] = player_scout_amuna_left_sheet[0]
    loaded_dict["player_scout_amuna_left_2"] = player_scout_amuna_left_sheet[1]
    loaded_dict["player_scout_amuna_left_3"] = player_scout_amuna_left_sheet[2]
    loaded_dict["player_scout_amuna_left_4"] = player_scout_amuna_left_sheet[3]
    player_scout_amuna_right_url = resource_path('resources/art/player_scout_amuna_right.png')
    player_scout_amuna_right_sheet = sprite_sheet((50, 75), player_scout_amuna_right_url)
    loaded_dict["player_scout_amuna_right_1"] = player_scout_amuna_right_sheet[0]
    loaded_dict["player_scout_amuna_right_2"] = player_scout_amuna_right_sheet[1]
    loaded_dict["player_scout_amuna_right_3"] = player_scout_amuna_right_sheet[2]
    loaded_dict["player_scout_amuna_right_4"] = player_scout_amuna_right_sheet[3]
    # player scout nuldar race -----------------------------------------------------------------------------------------
    player_scout_nuldar_down_url = resource_path('resources/art/player_scout_nuldar_down.png')
    player_scout_nuldar_down_sheet = sprite_sheet((50, 75), player_scout_nuldar_down_url)
    loaded_dict["player_scout_nuldar_down_1"] = player_scout_nuldar_down_sheet[0]
    loaded_dict["player_scout_nuldar_down_2"] = player_scout_nuldar_down_sheet[1]
    loaded_dict["player_scout_nuldar_down_3"] = player_scout_nuldar_down_sheet[2]
    loaded_dict["player_scout_nuldar_down_4"] = player_scout_nuldar_down_sheet[3]
    player_scout_nuldar_up_url = resource_path('resources/art/player_scout_nuldar_up.png')
    player_scout_nuldar_up_sheet = sprite_sheet((50, 75), player_scout_nuldar_up_url)
    loaded_dict["player_scout_nuldar_up_1"] = player_scout_nuldar_up_sheet[0]
    loaded_dict["player_scout_nuldar_up_2"] = player_scout_nuldar_up_sheet[1]
    loaded_dict["player_scout_nuldar_up_3"] = player_scout_nuldar_up_sheet[2]
    loaded_dict["player_scout_nuldar_up_4"] = player_scout_nuldar_up_sheet[3]
    player_scout_nuldar_left_url = resource_path('resources/art/player_scout_nuldar_left.png')
    player_scout_nuldar_left_sheet = sprite_sheet((50, 75), player_scout_nuldar_left_url)
    loaded_dict["player_scout_nuldar_left_1"] = player_scout_nuldar_left_sheet[0]
    loaded_dict["player_scout_nuldar_left_2"] = player_scout_nuldar_left_sheet[1]
    loaded_dict["player_scout_nuldar_left_3"] = player_scout_nuldar_left_sheet[2]
    loaded_dict["player_scout_nuldar_left_4"] = player_scout_nuldar_left_sheet[3]
    player_scout_nuldar_right_url = resource_path('resources/art/player_scout_nuldar_right.png')
    player_scout_nuldar_right_sheet = sprite_sheet((50, 75), player_scout_nuldar_right_url)
    loaded_dict["player_scout_nuldar_right_1"] = player_scout_nuldar_right_sheet[0]
    loaded_dict["player_scout_nuldar_right_2"] = player_scout_nuldar_right_sheet[1]
    loaded_dict["player_scout_nuldar_right_3"] = player_scout_nuldar_right_sheet[2]
    loaded_dict["player_scout_nuldar_right_4"] = player_scout_nuldar_right_sheet[3]
    # player scout sorae race ------------------------------------------------------------------------------------------
    player_scout_sorae_down_url = resource_path('resources/art/player_scout_sorae_down.png')
    player_scout_sorae_down_sheet = sprite_sheet((50, 75), player_scout_sorae_down_url)
    loaded_dict["player_scout_sorae_down_1"] = player_scout_sorae_down_sheet[0]
    loaded_dict["player_scout_sorae_down_2"] = player_scout_sorae_down_sheet[1]
    loaded_dict["player_scout_sorae_down_3"] = player_scout_sorae_down_sheet[2]
    loaded_dict["player_scout_sorae_down_4"] = player_scout_sorae_down_sheet[3]
    player_scout_sorae_up_url = resource_path('resources/art/player_scout_sorae_up.png')
    player_scout_sorae_up_sheet = sprite_sheet((50, 75), player_scout_sorae_up_url)
    loaded_dict["player_scout_sorae_up_1"] = player_scout_sorae_up_sheet[0]
    loaded_dict["player_scout_sorae_up_2"] = player_scout_sorae_up_sheet[1]
    loaded_dict["player_scout_sorae_up_3"] = player_scout_sorae_up_sheet[2]
    loaded_dict["player_scout_sorae_up_4"] = player_scout_sorae_up_sheet[3]
    player_scout_sorae_left_url = resource_path('resources/art/player_scout_sorae_left.png')
    player_scout_sorae_left_sheet = sprite_sheet((50, 75), player_scout_sorae_left_url)
    loaded_dict["player_scout_sorae_left_1"] = player_scout_sorae_left_sheet[0]
    loaded_dict["player_scout_sorae_left_2"] = player_scout_sorae_left_sheet[1]
    loaded_dict["player_scout_sorae_left_3"] = player_scout_sorae_left_sheet[2]
    loaded_dict["player_scout_sorae_left_4"] = player_scout_sorae_left_sheet[3]
    player_scout_sorae_right_url = resource_path('resources/art/player_scout_sorae_right.png')
    player_scout_sorae_right_sheet = sprite_sheet((50, 75), player_scout_sorae_right_url)
    loaded_dict["player_scout_sorae_right_1"] = player_scout_sorae_right_sheet[0]
    loaded_dict["player_scout_sorae_right_2"] = player_scout_sorae_right_sheet[1]
    loaded_dict["player_scout_sorae_right_3"] = player_scout_sorae_right_sheet[2]
    loaded_dict["player_scout_sorae_right_4"] = player_scout_sorae_right_sheet[3]
    # player battle amuna race -----------------------------------------------------------------------------------------
    player_battle_amuna_url = resource_path('resources/art/player_battle_sprites_amuna.png')
    player_battle_amuna_sheet = sprite_sheet((750, 624), player_battle_amuna_url)
    loaded_dict["player_no_role_amuna_battle"] = player_battle_amuna_sheet[0]
    loaded_dict["player_no_role_amuna_attack"] = player_battle_amuna_sheet[1]
    loaded_dict["player_mage_amuna_battle"] = player_battle_amuna_sheet[2]
    loaded_dict["player_mage_amuna_attack"] = player_battle_amuna_sheet[3]
    loaded_dict["player_fighter_amuna_battle"] = player_battle_amuna_sheet[4]
    loaded_dict["player_fighter_amuna_attack"] = player_battle_amuna_sheet[5]
    loaded_dict["player_scout_amuna_battle"] = player_battle_amuna_sheet[6]
    loaded_dict["player_scout_amuna_attack"] = player_battle_amuna_sheet[7]
    # player skills amuna race -----------------------------------------------------------------------------------------
    player_skills_amuna_url = resource_path('resources/art/player_battle_sprites_skills_amuna.png')
    player_skills_amuna_sheet = sprite_sheet((750, 624), player_skills_amuna_url)
    loaded_dict["player_mage_barrier_amuna_battle"] = player_skills_amuna_sheet[0]
    loaded_dict["player_mage_barrier_amuna_attack"] = player_skills_amuna_sheet[1]
    loaded_dict["player_scout_sense_amuna_battle"] = player_skills_amuna_sheet[2]
    loaded_dict["player_scout_sense_amuna_attack"] = player_skills_amuna_sheet[3]
    loaded_dict["player_fighter_amuna_strike"] = player_skills_amuna_sheet[4]
    # player battle sorae race -----------------------------------------------------------------------------------------
    player_battle_sorae_url = resource_path('resources/art/player_battle_sprites_sorae.png')
    player_battle_sorae_sheet = sprite_sheet((750, 624), player_battle_sorae_url)
    loaded_dict["player_no_role_sorae_battle"] = player_battle_sorae_sheet[0]
    loaded_dict["player_no_role_sorae_attack"] = player_battle_sorae_sheet[1]
    loaded_dict["player_mage_sorae_battle"] = player_battle_sorae_sheet[2]
    loaded_dict["player_mage_sorae_attack"] = player_battle_sorae_sheet[3]
    loaded_dict["player_fighter_sorae_battle"] = player_battle_sorae_sheet[4]
    loaded_dict["player_fighter_sorae_attack"] = player_battle_sorae_sheet[5]
    loaded_dict["player_scout_sorae_battle"] = player_battle_sorae_sheet[6]
    loaded_dict["player_scout_sorae_attack"] = player_battle_sorae_sheet[7]
    # player skills sorae race -----------------------------------------------------------------------------------------
    player_skills_sorae_url = resource_path('resources/art/player_battle_sprites_skills_sorae.png')
    player_skills_sorae_sheet = sprite_sheet((750, 624), player_skills_sorae_url)
    loaded_dict["player_mage_barrier_sorae_battle"] = player_skills_sorae_sheet[0]
    loaded_dict["player_mage_barrier_sorae_attack"] = player_skills_sorae_sheet[1]
    loaded_dict["player_scout_sense_sorae_battle"] = player_skills_sorae_sheet[2]
    loaded_dict["player_scout_sense_sorae_attack"] = player_skills_sorae_sheet[3]
    loaded_dict["player_fighter_sorae_strike"] = player_skills_sorae_sheet[4]
    # player battle nuldar race ----------------------------------------------------------------------------------------
    player_battle_nuldar_url = resource_path('resources/art/player_battle_sprites_nuldar.png')
    player_battle_nuldar_sheet = sprite_sheet((750, 624), player_battle_nuldar_url)
    loaded_dict["player_no_role_nuldar_battle"] = player_battle_nuldar_sheet[0]
    loaded_dict["player_no_role_nuldar_attack"] = player_battle_nuldar_sheet[1]
    loaded_dict["player_mage_nuldar_battle"] = player_battle_nuldar_sheet[2]
    loaded_dict["player_mage_nuldar_attack"] = player_battle_nuldar_sheet[3]
    loaded_dict["player_fighter_nuldar_battle"] = player_battle_nuldar_sheet[4]
    loaded_dict["player_fighter_nuldar_attack"] = player_battle_nuldar_sheet[5]
    loaded_dict["player_scout_nuldar_battle"] = player_battle_nuldar_sheet[6]
    loaded_dict["player_scout_nuldar_attack"] = player_battle_nuldar_sheet[7]
    # player skills nuldar race ----------------------------------------------------------------------------------------
    player_skills_nuldar_url = resource_path('resources/art/player_battle_sprites_skills_nuldar.png')
    player_skills_nuldar_sheet = sprite_sheet((750, 624), player_skills_nuldar_url)
    loaded_dict["player_mage_barrier_nuldar_battle"] = player_skills_nuldar_sheet[0]
    loaded_dict["player_mage_barrier_nuldar_attack"] = player_skills_nuldar_sheet[1]
    loaded_dict["player_scout_sense_nuldar_battle"] = player_skills_nuldar_sheet[2]
    loaded_dict["player_scout_sense_nuldar_attack"] = player_skills_nuldar_sheet[3]
    loaded_dict["player_fighter_nuldar_strike"] = player_skills_nuldar_sheet[4]
    # damage overlays --------------------------------------------------------------------------------------------------
    damage_overlays_url = resource_path('resources/art/overlays_damage.png')
    damage_overlays_sheet = sprite_sheet((150, 150), damage_overlays_url)
    loaded_dict["dealt_damage_img"] = damage_overlays_sheet[0]
    loaded_dict["received_damage_img"] = damage_overlays_sheet[1]
    # garan npc --------------------------------------------------------------------------------------------------------
    garan_url = resource_path('resources/art/sprites_garans.png')
    garan_sheet = sprite_sheet((40, 62), garan_url)
    loaded_dict["garan_down"] = garan_sheet[0]
    loaded_dict["garan_up"] = garan_sheet[1]
    loaded_dict["garan_left"] = garan_sheet[2]
    loaded_dict["garan_right"] = garan_sheet[3]
    # maurelle npc -----------------------------------------------------------------------------------------------------
    maurelle_url = resource_path('resources/art/sprites_maurelles.png')
    maurelle_sheet = sprite_sheet((40, 62), maurelle_url)
    loaded_dict["maurelle_down"] = maurelle_sheet[0]
    loaded_dict["maurelle_up"] = maurelle_sheet[1]
    loaded_dict["maurelle_left"] = maurelle_sheet[2]
    loaded_dict["maurelle_right"] = maurelle_sheet[3]
    # celeste npc ------------------------------------------------------------------------------------------------------
    celeste_url = resource_path('resources/art/sprites_celestes.png')
    celeste_sheet = sprite_sheet((45, 62), celeste_url)
    loaded_dict["celeste_down"] = celeste_sheet[0]
    loaded_dict["celeste_up"] = celeste_sheet[1]
    loaded_dict["celeste_left"] = celeste_sheet[2]
    loaded_dict["celeste_right"] = celeste_sheet[3]
    # nede sprite ------------------------------------------------------------------------------------------------------
    nede_url = resource_path('resources/art/sprites_nede.png')
    nede_sheet = sprite_sheet((60, 60), nede_url)
    loaded_dict["nede_left"] = nede_sheet[0]
    loaded_dict["nede_right"] = nede_sheet[1]
    loaded_dict["nede_high_left"] = nede_sheet[2]
    loaded_dict["nede_high_right"] = nede_sheet[3]
    # guard npc --------------------------------------------------------------------------------------------------------
    guard_url = resource_path('resources/art/sprites_guards.png')
    guard_sheet = sprite_sheet((50, 62), guard_url)
    loaded_dict["guard_down"] = guard_sheet[0]
    loaded_dict["guard_up"] = guard_sheet[1]
    loaded_dict["guard_left"] = guard_sheet[2]
    loaded_dict["guard_right"] = guard_sheet[3]
    # torune npc -------------------------------------------------------------------------------------------------------
    torune_url = resource_path('resources/art/sprites_torune.png')
    torune_sheet = sprite_sheet((50, 62), torune_url)
    loaded_dict["torune_down"] = torune_sheet[0]
    loaded_dict["torune_up"] = torune_sheet[1]
    loaded_dict["torune_left"] = torune_sheet[2]
    loaded_dict["torune_right"] = torune_sheet[3]
    # voruke npc -------------------------------------------------------------------------------------------------------
    voruke_url = resource_path('resources/art/sprites_voruke.png')
    voruke_sheet = sprite_sheet((45, 62), voruke_url)
    loaded_dict["voruke_down"] = voruke_sheet[0]
    loaded_dict["voruke_up"] = voruke_sheet[1]
    loaded_dict["voruke_left"] = voruke_sheet[2]
    loaded_dict["voruke_right"] = voruke_sheet[3]
    # zerah npc -------------------------------------------------------------------------------------------------------
    zerah_url = resource_path('resources/art/sprites_zerah.png')
    zerah_sheet = sprite_sheet((45, 62), zerah_url)
    loaded_dict["zerah_down"] = zerah_sheet[0]
    loaded_dict["zerah_up"] = zerah_sheet[1]
    loaded_dict["zerah_left"] = zerah_sheet[2]
    loaded_dict["zerah_right"] = zerah_sheet[3]
    # npc interactions -------------------------------------------------------------------------------------------------
    npc_interactions_url = resource_path('resources/art/sprites_npc_interactions.png')
    npc_interactions_sheet = sprite_sheet((220, 300), npc_interactions_url)
    loaded_dict["garan_interaction"] = npc_interactions_sheet[0]
    loaded_dict["maurelle_interaction"] = npc_interactions_sheet[1]
    loaded_dict["celeste_interaction"] = npc_interactions_sheet[2]
    loaded_dict["torune_interaction"] = npc_interactions_sheet[3]
    loaded_dict["voruke_interaction"] = npc_interactions_sheet[4]
    loaded_dict["zerah_interaction"] = npc_interactions_sheet[5]
    # interaction popup ------------------------------------------------------------------------------------------------
    interaction_popup_url = resource_path('resources/art/popup_interaction.png')
    interaction_popup_sheet = sprite_sheet((125, 25), interaction_popup_url)
    loaded_dict["popup_interaction"] = interaction_popup_sheet[0]
    loaded_dict["popup_interaction_red"] = interaction_popup_sheet[1]
    loaded_dict["popup_interaction_purple"] = interaction_popup_sheet[2]
    # enemies ----------------------------------------------------------------------------------------------------------
    enemies_url = resource_path('resources/art/sprites_enemies.png')
    enemies_sheet = sprite_sheet((50, 50), enemies_url)
    loaded_dict["snake"] = enemies_sheet[0]
    loaded_dict["ghoul"] = enemies_sheet[1]
    loaded_dict["magmon"] = enemies_sheet[2]
    loaded_dict["bandile"] = enemies_sheet[3]
    # boss enemies -----------------------------------------------------------------------------------------------------
    boss_enemies_url = resource_path('resources/art/sprites_bosses.png')
    boss_enemies_sheet = sprite_sheet((125, 125), boss_enemies_url)
    loaded_dict["chorizon"] = boss_enemies_sheet[0]
    loaded_dict["muchador"] = boss_enemies_sheet[1]
    loaded_dict["muchador_dark"] = boss_enemies_sheet[2]
    # enemies highlighted ----------------------------------------------------------------------------------------------
    enemies_high_url = resource_path('resources/art/sprites_enemies_highlighted.png')
    enemies_high_sheet = sprite_sheet((50, 75), enemies_high_url)
    loaded_dict["snake_high"] = enemies_high_sheet[0]
    loaded_dict["ghoul_high"] = enemies_high_sheet[1]
    loaded_dict["magmon_high"] = enemies_high_sheet[2]
    loaded_dict["bandile_high"] = enemies_high_sheet[3]
    # enemies battle ---------------------------------------------------------------------------------------------------
    enemies_battle_url = resource_path('resources/art/sprites_enemies_battle.png')
    enemies_battle_sheet = sprite_sheet((300, 280), enemies_battle_url)
    loaded_dict["snake_battle"] = enemies_battle_sheet[0]
    loaded_dict["snake_attack"] = enemies_battle_sheet[1]
    loaded_dict["ghoul_battle"] = enemies_battle_sheet[2]
    loaded_dict["ghoul_attack"] = enemies_battle_sheet[3]
    loaded_dict["magmon_battle"] = enemies_battle_sheet[4]
    loaded_dict["magmon_attack"] = enemies_battle_sheet[5]
    loaded_dict["bandile_battle"] = enemies_battle_sheet[6]
    loaded_dict["bandile_attack"] = enemies_battle_sheet[7]
    # boss enemies battle ----------------------------------------------------------------------------------------------
    boss_enemies_battle_url = resource_path('resources/art/sprites_bosses_battle.png')
    boss_enemies_battle_sheet = sprite_sheet((500, 500), boss_enemies_battle_url)
    loaded_dict["chorizon_battle"] = boss_enemies_battle_sheet[0]
    loaded_dict["muchador_battle"] = boss_enemies_battle_sheet[1]
    # enemies attacking ------------------------------------------------------------------------------------------------
    enemies_attack_url = resource_path('resources/art/sprites_enemies_attacking.png')
    enemies_attack_sheet = sprite_sheet((400, 300), enemies_attack_url)
    loaded_dict["snake attacking"] = enemies_attack_sheet[0]
    loaded_dict["ghoul attacking"] = enemies_attack_sheet[1]
    loaded_dict["ghoul attacking star"] = enemies_attack_sheet[2]
    # boss enemies attack ----------------------------------------------------------------------------------------------
    boss_enemies_battle_url = resource_path('resources/art/sprites_bosses_attack.png')
    boss_enemies_battle_sheet = sprite_sheet((500, 500), boss_enemies_battle_url)
    loaded_dict["chorizon_attack"] = boss_enemies_battle_sheet[0]
    loaded_dict["muchador_attack"] = boss_enemies_battle_sheet[1]
    # amuna buildings --------------------------------------------------------------------------------------------------
    amuna_buildings_url = resource_path('resources/art/sprites_amuna_buildings.png')
    amuna_buildings_sheet = sprite_sheet((100, 100), amuna_buildings_url)
    loaded_dict["amuna_academia_building"] = amuna_buildings_sheet[0]
    loaded_dict["amuna_inn_building"] = amuna_buildings_sheet[1]
    loaded_dict["amuna_shop_building"] = amuna_buildings_sheet[2]
    # nuldar buildings -------------------------------------------------------------------------------------------------
    nuldar_buildings_url = resource_path('resources/art/sprites_nuldar_buildings.png')
    nuldar_buildings_sheet = sprite_sheet((140, 110), nuldar_buildings_url)
    loaded_dict["nuldar_herb_building"] = nuldar_buildings_sheet[0]
    loaded_dict["nuldar_inn_building"] = nuldar_buildings_sheet[1]
    loaded_dict["nuldar_shop_building"] = nuldar_buildings_sheet[2]
    # nascent gate -----------------------------------------------------------------------------------------------------
    nascent_gate_url = resource_path('resources/art/sprites_nascent_gate.png')
    nascent_gate_sheet = sprite_sheet((178, 120), nascent_gate_url)
    loaded_dict["nascent_gate_closed"] = nascent_gate_sheet[0]
    loaded_dict["nascent_gate_open"] = nascent_gate_sheet[1]
    # items ------------------------------------------------------------------------------------------------------------
    items_url = resource_path('resources/art/overlay_items.png')
    items_sheet = sprite_sheet((50, 50), items_url)
    loaded_dict["health_pot_img"] = items_sheet[0]
    loaded_dict["energy_pot_img"] = items_sheet[1]
    loaded_dict["basic_robes_img"] = items_sheet[2]
    loaded_dict["basic_armor_img"] = items_sheet[3]
    loaded_dict["basic_tunic_img"] = items_sheet[4]
    loaded_dict["basic_staff_img"] = items_sheet[5]
    loaded_dict["basic_sword_img"] = items_sheet[6]
    loaded_dict["basic_bow_img"] = items_sheet[7]
    loaded_dict["bone_dust_img"] = items_sheet[8]
    loaded_dict["shiny_rock_img"] = items_sheet[9]
    loaded_dict["key_img"] = items_sheet[10]
    loaded_dict["gloves"] = items_sheet[11]
    loaded_dict["ember"] = items_sheet[12]
    loaded_dict["band"] = items_sheet[13]
    loaded_dict["flowe"] = items_sheet[14]
    # items info -------------------------------------------------------------------------------------------------------
    items_info_url = resource_path('resources/art/overlay_info_items.png')
    items_info_sheet = sprite_sheet((246, 240), items_info_url)
    loaded_dict["info_health_pot_img"] = items_info_sheet[0]
    loaded_dict["info_energy_pot_img"] = items_info_sheet[1]
    loaded_dict["info_basic_robes_img"] = items_info_sheet[2]
    loaded_dict["info_basic_armor_img"] = items_info_sheet[3]
    loaded_dict["info_basic_tunic_img"] = items_info_sheet[4]
    loaded_dict["info_basic_staff_img"] = items_info_sheet[5]
    loaded_dict["info_basic_sword_img"] = items_info_sheet[6]
    loaded_dict["info_basic_bow_img"] = items_info_sheet[7]
    loaded_dict["info_bone_dust_img"] = items_info_sheet[8]
    loaded_dict["info_shiny_rock_img"] = items_info_sheet[9]
    loaded_dict["info_boss_key_img"] = items_info_sheet[10]
    loaded_dict["info_gloves"] = items_info_sheet[11]
    loaded_dict["info_ember"] = items_info_sheet[12]
    loaded_dict["info_band"] = items_info_sheet[13]
    loaded_dict["info_flowe"] = items_info_sheet[14]
    # buy items info ---------------------------------------------------------------------------------------------------
    buy_items_url = resource_path('resources/art/overlay_buy_items.png')
    buy_items_sheet = sprite_sheet((246, 240), buy_items_url)
    loaded_dict["b_health_pot_img"] = buy_items_sheet[0]
    loaded_dict["b_energy_pot_img"] = buy_items_sheet[1]
    loaded_dict["b_basic_robes_img"] = buy_items_sheet[2]
    loaded_dict["b_basic_armor_img"] = buy_items_sheet[3]
    loaded_dict["b_basic_tunic_img"] = buy_items_sheet[4]
    loaded_dict["b_basic_staff_img"] = buy_items_sheet[5]
    loaded_dict["b_basic_sword_img"] = buy_items_sheet[6]
    loaded_dict["b_basic_bow_img"] = buy_items_sheet[7]
    # sell items -------------------------------------------------------------------------------------------------------
    sell_items_url = resource_path('resources/art/overlay_sell_items.png')
    sell_items_sheet = sprite_sheet((246, 240), sell_items_url)
    loaded_dict["s_health_pot_img"] = sell_items_sheet[0]
    loaded_dict["s_energy_pot_img"] = sell_items_sheet[1]
    loaded_dict["s_basic_robes_img"] = sell_items_sheet[2]
    loaded_dict["s_basic_armor_img"] = sell_items_sheet[3]
    loaded_dict["s_basic_tunic_img"] = sell_items_sheet[4]
    loaded_dict["s_basic_staff_img"] = sell_items_sheet[5]
    loaded_dict["s_basic_sword_img"] = sell_items_sheet[6]
    loaded_dict["s_basic_bow_img"] = sell_items_sheet[7]
    loaded_dict["s_bone_dust_img"] = sell_items_sheet[8]
    loaded_dict["s_shiny_rock_img"] = sell_items_sheet[9]
    loaded_dict["s_ember_img"] = sell_items_sheet[10]
    loaded_dict["s_band_img"] = sell_items_sheet[11]
    # player info windows ----------------------------------------------------------------------------------------------
    player_info_url = resource_path('resources/art/overlay_info_sheets.png')
    player_info_sheet = sprite_sheet((500, 525), player_info_url)
    loaded_dict["character_window_img"] = player_info_sheet[0]
    loaded_dict["journal_window_img"] = player_info_sheet[1]
    # books ------------------------------------------------------------------------------------------------------------
    books_url = resource_path('resources/art/overlay_role_books.png')
    books_sheet = sprite_sheet((700, 525), books_url)
    loaded_dict["mage_book_img"] = books_sheet[0]
    loaded_dict["fighter_book_img"] = books_sheet[1]
    loaded_dict["scout_book_img"] = books_sheet[2]
    # buttons highlight ------------------------------------------------------------------------------------------------
    buttons_high_url = resource_path('resources/art/buttons_highlight.png')
    buttons_high_sheet = sprite_sheet((100, 65), buttons_high_url)
    loaded_dict["main high"] = buttons_high_sheet[0]
    loaded_dict["skill high"] = buttons_high_sheet[1]
    loaded_dict["close high"] = buttons_high_sheet[2]
    loaded_dict["item high"] = buttons_high_sheet[3]
    # start screen buttons ---------------------------------------------------------------------------------------------
    start_buttons_url = resource_path('resources/art/buttons_start_screen.png')
    start_buttons_sheet = sprite_sheet((385, 75), start_buttons_url)
    loaded_dict["new_game_img"] = start_buttons_sheet[0]
    loaded_dict["continue_img"] = start_buttons_sheet[1]
    # start screen and race select buttons highlight -------------------------------------------------------------------
    start_buttons_high_url = resource_path('resources/art/buttons_start_highlight.png')
    start_buttons_high_sheet = sprite_sheet((405, 75), start_buttons_high_url)
    loaded_dict["start high"] = start_buttons_high_sheet[0]
    loaded_dict["race high"] = start_buttons_high_sheet[1]
    loaded_dict["begin high"] = start_buttons_high_sheet[2]
    # race select buttons on character screen --------------------------------------------------------------------------
    race_select_buttons_url = resource_path('resources/art/buttons_race_select.png')
    race_select_buttons_sheet = sprite_sheet((384, 75), race_select_buttons_url)
    loaded_dict["amuna_button_img"] = race_select_buttons_sheet[0]
    loaded_dict["nuldar_button_img"] = race_select_buttons_sheet[1]
    loaded_dict["sorae_button_img"] = race_select_buttons_sheet[2]
    # race select buttons on character screen --------------------------------------------------------------------------
    role_select_buttons_high_url = resource_path('resources/art/buttons_misc_high.png')
    role_select_buttons_high_sheet = sprite_sheet((200, 42), role_select_buttons_high_url)
    loaded_dict["role_high"] = role_select_buttons_high_sheet[0]
    # buttons ----------------------------------------------------------------------------------------------------------
    buttons_url = resource_path('resources/art/buttons_main.png')
    buttons_sheet = sprite_sheet((100, 50), buttons_url)
    loaded_dict["character_button_img"] = buttons_sheet[0]
    loaded_dict["journal_button_img"] = buttons_sheet[1]
    loaded_dict["buy_button_img"] = buttons_sheet[2]
    loaded_dict["rest_button_img"] = buttons_sheet[3]
    loaded_dict["quest_button_img"] = buttons_sheet[4]
    loaded_dict["leave_button_img"] = buttons_sheet[5]
    loaded_dict["accept_button_img"] = buttons_sheet[6]
    loaded_dict["decline_button_img"] = buttons_sheet[7]
    loaded_dict["yes_button_img"] = buttons_sheet[8]
    loaded_dict["no_button_img"] = buttons_sheet[9]
    loaded_dict["use_button_img"] = buttons_sheet[10]
    loaded_dict["equip_button_img"] = buttons_sheet[11]
    loaded_dict["upgrade_button_img"] = buttons_sheet[12]
    loaded_dict["back_button_img"] = buttons_sheet[13]
    loaded_dict["ok_button_img"] = buttons_sheet[14]
    loaded_dict["skip_button_img"] = buttons_sheet[15]
    # attack buttons ---------------------------------------------------------------------------------------------------
    attack_buttons_url = resource_path('resources/art/overlay_attacks.png')
    attack_buttons_sheet = sprite_sheet((60, 60), attack_buttons_url)
    loaded_dict["mage_attack_button_img"] = attack_buttons_sheet[0]
    loaded_dict["fighter_attack_button_img"] = attack_buttons_sheet[1]
    loaded_dict["scout_attack_button_img"] = attack_buttons_sheet[2]
    loaded_dict["no_role_attack_button_img"] = attack_buttons_sheet[3]
    # skill buttons ----------------------------------------------------------------------------------------------------
    skill_buttons_url = resource_path('resources/art/overlay_skills.png')
    skill_buttons_sheet = sprite_sheet((60, 60), skill_buttons_url)
    loaded_dict["barrier_button_img"] = skill_buttons_sheet[0]
    loaded_dict["strike_button_img"] = skill_buttons_sheet[1]
    loaded_dict["sense_button_img"] = skill_buttons_sheet[2]
    # function buttons -------------------------------------------------------------------------------------------------
    game_play_function_buttons_url = resource_path('resources/art/buttons_game_play_function.png')
    game_play_function_buttons_sheet = sprite_sheet((100, 25), game_play_function_buttons_url)
    loaded_dict["save_button_img"] = game_play_function_buttons_sheet[0]
    loaded_dict["map_button_img"] = game_play_function_buttons_sheet[1]
    # select buttons --------------------------------------------------------------------------------------------------
    selection_buttons_url = resource_path('resources/art/buttons_select_role.png')
    selection_buttons_sheet = sprite_sheet((184, 42), selection_buttons_url)
    loaded_dict["mage_select_button_img"] = selection_buttons_sheet[0]
    loaded_dict["fighter_select_button_img"] = selection_buttons_sheet[1]
    loaded_dict["scout_select_button_img"] = selection_buttons_sheet[2]
    loaded_dict["offense_select_button_img"] = selection_buttons_sheet[3]
    loaded_dict["defense_select_button_img"] = selection_buttons_sheet[4]
    # quest windows ----------------------------------------------------------------------------------------------------
    quest_windows_url = resource_path('resources/art/overlay_quest_sheets.png')
    quest_windows_sheet = sprite_sheet((500, 525), quest_windows_url)
    loaded_dict["garan_quest"] = quest_windows_sheet[0]
    loaded_dict["maurelle_quest"] = quest_windows_sheet[1]
    loaded_dict["torune_quest"] = quest_windows_sheet[2]
    loaded_dict["celeste_quest"] = quest_windows_sheet[3]
    loaded_dict["voruke_quest"] = quest_windows_sheet[4]
    loaded_dict["zerah_quest"] = quest_windows_sheet[5]
    loaded_dict["kirean_quest"] = quest_windows_sheet[6]
    loaded_dict["dionte_quest"] = quest_windows_sheet[7]
    # quest complete popups --------------------------------------------------------------------------------------------
    quest_popups_url = resource_path('resources/art/overlay_quest_completes.png')
    quest_popups_sheet = sprite_sheet((500, 250), quest_popups_url)
    loaded_dict["garan_complete"] = quest_popups_sheet[0]
    loaded_dict["maurelle_complete"] = quest_popups_sheet[1]
    loaded_dict["celeste_complete"] = quest_popups_sheet[2]
    loaded_dict["torune_complete"] = quest_popups_sheet[3]
    loaded_dict["voruke_complete"] = quest_popups_sheet[4]
    loaded_dict["zerah_complete"] = quest_popups_sheet[5]
    loaded_dict["kirean_complete"] = quest_popups_sheet[6]
    loaded_dict["dionte_complete"] = quest_popups_sheet[7]
    # quest stars ------------------------------------------------------------------------------------------------------
    quest_stars_url = resource_path('resources/art/overlay_quest_stars.png')
    quest_stars_sheet = sprite_sheet((50, 50), quest_stars_url)
    loaded_dict["quest_start_star"] = quest_stars_sheet[0]
    loaded_dict["quest_progress_star"] = quest_stars_sheet[1]
    loaded_dict["quest_complete_star"] = quest_stars_sheet[2]
    # quest stars ------------------------------------------------------------------------------------------------------
    building_quest_stars_url = resource_path('resources/art/overlay_building_npc_stars.png')
    building_quest_stars_sheet = sprite_sheet((125, 125), building_quest_stars_url)
    loaded_dict["building_npc_star_available"] = building_quest_stars_sheet[0]
    loaded_dict["building_npc_star_progress"] = building_quest_stars_sheet[1]
    loaded_dict["building_npc_star_complete"] = building_quest_stars_sheet[2]
    # star power -------------------------------------------------------------------------------------------------------
    star_power_url = resource_path('resources/art/overlay_star_power.png')
    star_power_sheet = sprite_sheet((150, 50), star_power_url)
    loaded_dict["star_00"] = star_power_sheet[0]
    loaded_dict["star_01"] = star_power_sheet[1]
    loaded_dict["star_02"] = star_power_sheet[2]
    loaded_dict["star_03"] = star_power_sheet[3]
    loaded_dict["star_04"] = star_power_sheet[4]
    # pop up notifications ---------------------------------------------------------------------------------------------
    popups_url = resource_path('resources/art/popups_main.png')
    popups_sheet = sprite_sheet((400, 200), popups_url)
    loaded_dict["gear_popup"] = popups_sheet[0]
    loaded_dict["health_popup"] = popups_sheet[1]
    loaded_dict["knowledge_popup"] = popups_sheet[2]
    loaded_dict["save_popup"] = popups_sheet[3]
    loaded_dict["save_not_found"] = popups_sheet[4]
    loaded_dict["quest_popup"] = popups_sheet[5]
    loaded_dict["drop_popup"] = popups_sheet[6]
    # quest pine logs --------------------------------------------------------------------------------------------------
    quest_logs_url = resource_path('resources/art/sprite_logs.png')
    quest_logs_sheet = sprite_sheet((40, 50), quest_logs_url)
    loaded_dict["pine_logs_img"] = quest_logs_sheet[0]
    loaded_dict["pine_logs_high_img"] = quest_logs_sheet[1]
    # quest pine logs --------------------------------------------------------------------------------------------------
    sprite_ore_url = resource_path('resources/art/sprite_ore.png')
    sprite_ore_sheet = sprite_sheet((75, 50), sprite_ore_url)
    loaded_dict["sprite_ore_img"] = sprite_ore_sheet[0]
    loaded_dict["sprite_ore_high_img"] = sprite_ore_sheet[1]
    # game guide overlays ----------------------------------------------------------------------------------------------
    game_guide_url = resource_path('resources/art/overlay_game_guide.png')
    game_guide_sheet = sprite_sheet((488, 480), game_guide_url)
    loaded_dict["guide_basics_quest_img"] = game_guide_sheet[0]
    loaded_dict["guide_basics_battle_img"] = game_guide_sheet[1]
    loaded_dict["guide_basics_role_img"] = game_guide_sheet[2]
    loaded_dict["guide_basics_upgrades_img"] = game_guide_sheet[3]
    # cat petting animation sprites ------------------------------------------------------------------------------------
    cat_pet_url = resource_path('resources/art/sprites_cat_pet.png')
    cat_pet_sheet = sprite_sheet((90, 100), cat_pet_url)
    loaded_dict["shop_cat_pet_img"] = cat_pet_sheet[0]
    loaded_dict["academia_cat_pet_img"] = cat_pet_sheet[1]
    # cat petting animation sprites ------------------------------------------------------------------------------------
    stardust_stars_url = resource_path('resources/art/overlays_stardust_stars.png')
    stardust_stars_sheet = sprite_sheet((271, 105), stardust_stars_url)
    loaded_dict["stardust_star_01"] = stardust_stars_sheet[0]
    loaded_dict["stardust_star_02"] = stardust_stars_sheet[1]
    loaded_dict["stardust_star_03"] = stardust_stars_sheet[2]
    loaded_dict["stardust_star_04"] = stardust_stars_sheet[3]
    # hearth stone sprites ---------------------------------------------------------------------------------------------
    hearth_stones_url = resource_path('resources/art/sprite_hearth_stone.png')
    hearth_stones_sheet = sprite_sheet((100, 100), hearth_stones_url)
    loaded_dict["hearth_stone"] = hearth_stones_sheet[0]
    loaded_dict["hearth_stone_lit"] = hearth_stones_sheet[1]
    # directional arrow sprites ----------------------------------------------------------------------------------------
    arrows_url = resource_path('resources/art/overlay_arrows.png')
    arrows_sheet = sprite_sheet((100, 100), arrows_url)
    loaded_dict["arrow_up"] = arrows_sheet[0]
    loaded_dict["arrow_down"] = arrows_sheet[1]
    loaded_dict["arrow_left"] = arrows_sheet[2]
    loaded_dict["arrow_right"] = arrows_sheet[3]
    # character current location overlay -------------------------------------------------------------------------------
    character_selections_url = resource_path('resources/art/overlay_character_location.png')
    character_selections_sheet = sprite_sheet((62, 75), character_selections_url)
    loaded_dict["amuna_location"] = character_selections_sheet[0]
    loaded_dict["nuldar_location"] = character_selections_sheet[1]
    loaded_dict["sorae_location"] = character_selections_sheet[2]
    # dungeon items ----------------------------------------------------------------------------------------------------
    dungeon_items_url = resource_path('resources/art/sprites_dungeon_items.png')
    dungeon_items_sheet = sprite_sheet((75, 100), dungeon_items_url)
    loaded_dict["dungeon_crate"] = dungeon_items_sheet[0]
    loaded_dict["dungeon_switch_inactive"] = dungeon_items_sheet[1]
    loaded_dict["dungeon_switch_active"] = dungeon_items_sheet[2]
    loaded_dict["dungeon_switch_full"] = dungeon_items_sheet[3]
    # dungeon chest closed and open ------------------------------------------------------------------------------------
    dungeon_chest_url = resource_path('resources/art/sprite_dungeon_chest.png')
    dungeon_chest_sheet = sprite_sheet((175, 150), dungeon_chest_url)
    loaded_dict["dungeon_chest"] = dungeon_chest_sheet[0]
    loaded_dict["dungeon_chest_open"] = dungeon_chest_sheet[1]
    # heath bars -------------------------------------------------------------------------------------------------------
    hp_url = resource_path('resources/art/bars_health.png')
    hp_sheet = sprite_sheet((305, 19), hp_url)
    loaded_dict["hp_0"] = hp_sheet[0]
    loaded_dict["hp_1"] = hp_sheet[1]
    loaded_dict["hp_2"] = hp_sheet[2]
    loaded_dict["hp_3"] = hp_sheet[3]
    loaded_dict["hp_4"] = hp_sheet[4]
    loaded_dict["hp_5"] = hp_sheet[5]
    loaded_dict["hp_6"] = hp_sheet[6]
    loaded_dict["hp_7"] = hp_sheet[7]
    loaded_dict["hp_8"] = hp_sheet[8]
    loaded_dict["hp_9"] = hp_sheet[9]
    loaded_dict["hp_10"] = hp_sheet[10]
    loaded_dict["hp_11"] = hp_sheet[11]
    loaded_dict["hp_12"] = hp_sheet[12]
    loaded_dict["hp_13"] = hp_sheet[13]
    loaded_dict["hp_14"] = hp_sheet[14]
    loaded_dict["hp_15"] = hp_sheet[15]
    loaded_dict["hp_16"] = hp_sheet[16]
    loaded_dict["hp_17"] = hp_sheet[17]
    loaded_dict["hp_18"] = hp_sheet[18]
    loaded_dict["hp_19"] = hp_sheet[19]
    loaded_dict["hp_20"] = hp_sheet[20]
    loaded_dict["hp_21"] = hp_sheet[21]
    loaded_dict["hp_22"] = hp_sheet[22]
    loaded_dict["hp_23"] = hp_sheet[23]
    loaded_dict["hp_24"] = hp_sheet[24]
    loaded_dict["hp_25"] = hp_sheet[25]
    loaded_dict["hp_26"] = hp_sheet[26]
    loaded_dict["hp_27"] = hp_sheet[27]
    loaded_dict["hp_28"] = hp_sheet[28]
    loaded_dict["hp_29"] = hp_sheet[29]
    loaded_dict["hp_30"] = hp_sheet[30]
    loaded_dict["hp_31"] = hp_sheet[31]
    loaded_dict["hp_32"] = hp_sheet[32]
    loaded_dict["hp_33"] = hp_sheet[33]
    loaded_dict["hp_34"] = hp_sheet[34]
    loaded_dict["hp_35"] = hp_sheet[35]
    loaded_dict["hp_36"] = hp_sheet[36]
    loaded_dict["hp_37"] = hp_sheet[37]
    loaded_dict["hp_38"] = hp_sheet[38]
    loaded_dict["hp_39"] = hp_sheet[39]
    loaded_dict["hp_40"] = hp_sheet[40]
    loaded_dict["hp_41"] = hp_sheet[41]
    loaded_dict["hp_42"] = hp_sheet[42]
    loaded_dict["hp_43"] = hp_sheet[43]
    loaded_dict["hp_44"] = hp_sheet[44]
    loaded_dict["hp_45"] = hp_sheet[45]
    loaded_dict["hp_46"] = hp_sheet[46]
    loaded_dict["hp_47"] = hp_sheet[47]
    loaded_dict["hp_48"] = hp_sheet[48]
    loaded_dict["hp_49"] = hp_sheet[49]
    loaded_dict["hp_50"] = hp_sheet[50]
    loaded_dict["hp_51"] = hp_sheet[51]
    loaded_dict["hp_52"] = hp_sheet[52]
    loaded_dict["hp_53"] = hp_sheet[53]
    loaded_dict["hp_54"] = hp_sheet[54]
    loaded_dict["hp_55"] = hp_sheet[55]
    loaded_dict["hp_56"] = hp_sheet[56]
    loaded_dict["hp_57"] = hp_sheet[57]
    loaded_dict["hp_58"] = hp_sheet[58]
    loaded_dict["hp_59"] = hp_sheet[59]
    loaded_dict["hp_60"] = hp_sheet[60]
    loaded_dict["hp_61"] = hp_sheet[61]
    loaded_dict["hp_62"] = hp_sheet[62]
    loaded_dict["hp_63"] = hp_sheet[63]
    loaded_dict["hp_64"] = hp_sheet[64]
    loaded_dict["hp_65"] = hp_sheet[65]
    loaded_dict["hp_66"] = hp_sheet[66]
    loaded_dict["hp_67"] = hp_sheet[67]
    loaded_dict["hp_68"] = hp_sheet[68]
    loaded_dict["hp_69"] = hp_sheet[69]
    loaded_dict["hp_70"] = hp_sheet[70]
    loaded_dict["hp_71"] = hp_sheet[71]
    loaded_dict["hp_72"] = hp_sheet[72]
    loaded_dict["hp_73"] = hp_sheet[73]
    loaded_dict["hp_74"] = hp_sheet[74]
    loaded_dict["hp_75"] = hp_sheet[75]
    loaded_dict["hp_76"] = hp_sheet[76]
    loaded_dict["hp_77"] = hp_sheet[77]
    loaded_dict["hp_78"] = hp_sheet[78]
    loaded_dict["hp_79"] = hp_sheet[79]
    loaded_dict["hp_80"] = hp_sheet[80]
    loaded_dict["hp_81"] = hp_sheet[81]
    loaded_dict["hp_82"] = hp_sheet[82]
    loaded_dict["hp_83"] = hp_sheet[83]
    loaded_dict["hp_84"] = hp_sheet[84]
    loaded_dict["hp_85"] = hp_sheet[85]
    loaded_dict["hp_86"] = hp_sheet[86]
    loaded_dict["hp_87"] = hp_sheet[87]
    loaded_dict["hp_88"] = hp_sheet[88]
    loaded_dict["hp_89"] = hp_sheet[89]
    loaded_dict["hp_90"] = hp_sheet[90]
    loaded_dict["hp_91"] = hp_sheet[91]
    loaded_dict["hp_92"] = hp_sheet[92]
    loaded_dict["hp_93"] = hp_sheet[93]
    loaded_dict["hp_94"] = hp_sheet[94]
    loaded_dict["hp_95"] = hp_sheet[95]
    loaded_dict["hp_96"] = hp_sheet[96]
    loaded_dict["hp_97"] = hp_sheet[97]
    loaded_dict["hp_98"] = hp_sheet[98]
    loaded_dict["hp_99"] = hp_sheet[99]
    loaded_dict["hp_100"] = hp_sheet[100]
    # energy bars ------------------------------------------------------------------------------------------------------
    en_url = resource_path('resources/art/bars_energy.png')
    en_sheet = sprite_sheet((305, 19), en_url)
    loaded_dict["en_0"] = en_sheet[0]
    loaded_dict["en_1"] = en_sheet[1]
    loaded_dict["en_2"] = en_sheet[2]
    loaded_dict["en_3"] = en_sheet[3]
    loaded_dict["en_4"] = en_sheet[4]
    loaded_dict["en_5"] = en_sheet[5]
    loaded_dict["en_6"] = en_sheet[6]
    loaded_dict["en_7"] = en_sheet[7]
    loaded_dict["en_8"] = en_sheet[8]
    loaded_dict["en_9"] = en_sheet[9]
    loaded_dict["en_10"] = en_sheet[10]
    loaded_dict["en_11"] = en_sheet[11]
    loaded_dict["en_12"] = en_sheet[12]
    loaded_dict["en_13"] = en_sheet[13]
    loaded_dict["en_14"] = en_sheet[14]
    loaded_dict["en_15"] = en_sheet[15]
    loaded_dict["en_16"] = en_sheet[16]
    loaded_dict["en_17"] = en_sheet[17]
    loaded_dict["en_18"] = en_sheet[18]
    loaded_dict["en_19"] = en_sheet[19]
    loaded_dict["en_20"] = en_sheet[20]
    loaded_dict["en_21"] = en_sheet[21]
    loaded_dict["en_22"] = en_sheet[22]
    loaded_dict["en_23"] = en_sheet[23]
    loaded_dict["en_24"] = en_sheet[24]
    loaded_dict["en_25"] = en_sheet[25]
    loaded_dict["en_26"] = en_sheet[26]
    loaded_dict["en_27"] = en_sheet[27]
    loaded_dict["en_28"] = en_sheet[28]
    loaded_dict["en_29"] = en_sheet[29]
    loaded_dict["en_30"] = en_sheet[30]
    loaded_dict["en_31"] = en_sheet[31]
    loaded_dict["en_32"] = en_sheet[32]
    loaded_dict["en_33"] = en_sheet[33]
    loaded_dict["en_34"] = en_sheet[34]
    loaded_dict["en_35"] = en_sheet[35]
    loaded_dict["en_36"] = en_sheet[36]
    loaded_dict["en_37"] = en_sheet[37]
    loaded_dict["en_38"] = en_sheet[38]
    loaded_dict["en_39"] = en_sheet[39]
    loaded_dict["en_40"] = en_sheet[40]
    loaded_dict["en_41"] = en_sheet[41]
    loaded_dict["en_42"] = en_sheet[42]
    loaded_dict["en_43"] = en_sheet[43]
    loaded_dict["en_44"] = en_sheet[44]
    loaded_dict["en_45"] = en_sheet[45]
    loaded_dict["en_46"] = en_sheet[46]
    loaded_dict["en_47"] = en_sheet[47]
    loaded_dict["en_48"] = en_sheet[48]
    loaded_dict["en_49"] = en_sheet[49]
    loaded_dict["en_50"] = en_sheet[50]
    loaded_dict["en_51"] = en_sheet[51]
    loaded_dict["en_52"] = en_sheet[52]
    loaded_dict["en_53"] = en_sheet[53]
    loaded_dict["en_54"] = en_sheet[54]
    loaded_dict["en_55"] = en_sheet[55]
    loaded_dict["en_56"] = en_sheet[56]
    loaded_dict["en_57"] = en_sheet[57]
    loaded_dict["en_58"] = en_sheet[58]
    loaded_dict["en_59"] = en_sheet[59]
    loaded_dict["en_60"] = en_sheet[60]
    loaded_dict["en_61"] = en_sheet[61]
    loaded_dict["en_62"] = en_sheet[62]
    loaded_dict["en_63"] = en_sheet[63]
    loaded_dict["en_64"] = en_sheet[64]
    loaded_dict["en_65"] = en_sheet[65]
    loaded_dict["en_66"] = en_sheet[66]
    loaded_dict["en_67"] = en_sheet[67]
    loaded_dict["en_68"] = en_sheet[68]
    loaded_dict["en_69"] = en_sheet[69]
    loaded_dict["en_70"] = en_sheet[70]
    loaded_dict["en_71"] = en_sheet[71]
    loaded_dict["en_72"] = en_sheet[72]
    loaded_dict["en_73"] = en_sheet[73]
    loaded_dict["en_74"] = en_sheet[74]
    loaded_dict["en_75"] = en_sheet[75]
    loaded_dict["en_76"] = en_sheet[76]
    loaded_dict["en_77"] = en_sheet[77]
    loaded_dict["en_78"] = en_sheet[78]
    loaded_dict["en_79"] = en_sheet[79]
    loaded_dict["en_80"] = en_sheet[80]
    loaded_dict["en_81"] = en_sheet[81]
    loaded_dict["en_82"] = en_sheet[82]
    loaded_dict["en_83"] = en_sheet[83]
    loaded_dict["en_84"] = en_sheet[84]
    loaded_dict["en_85"] = en_sheet[85]
    loaded_dict["en_86"] = en_sheet[86]
    loaded_dict["en_87"] = en_sheet[87]
    loaded_dict["en_88"] = en_sheet[88]
    loaded_dict["en_89"] = en_sheet[89]
    loaded_dict["en_90"] = en_sheet[90]
    loaded_dict["en_91"] = en_sheet[91]
    loaded_dict["en_92"] = en_sheet[92]
    loaded_dict["en_93"] = en_sheet[93]
    loaded_dict["en_94"] = en_sheet[94]
    loaded_dict["en_95"] = en_sheet[95]
    loaded_dict["en_96"] = en_sheet[96]
    loaded_dict["en_97"] = en_sheet[97]
    loaded_dict["en_98"] = en_sheet[98]
    loaded_dict["en_99"] = en_sheet[99]
    loaded_dict["en_100"] = en_sheet[100]
    # experience bars --------------------------------------------------------------------------------------------------
    xp_url = resource_path('resources/art/bars_xp.png')
    xp_sheet = sprite_sheet((305, 19), xp_url)
    loaded_dict["xp_0"] = xp_sheet[0]
    loaded_dict["xp_1"] = xp_sheet[1]
    loaded_dict["xp_2"] = xp_sheet[2]
    loaded_dict["xp_3"] = xp_sheet[3]
    loaded_dict["xp_4"] = xp_sheet[4]
    loaded_dict["xp_5"] = xp_sheet[5]
    loaded_dict["xp_6"] = xp_sheet[6]
    loaded_dict["xp_7"] = xp_sheet[7]
    loaded_dict["xp_8"] = xp_sheet[8]
    loaded_dict["xp_9"] = xp_sheet[9]
    loaded_dict["xp_10"] = xp_sheet[10]
    loaded_dict["xp_11"] = xp_sheet[11]
    loaded_dict["xp_12"] = xp_sheet[12]
    loaded_dict["xp_13"] = xp_sheet[13]
    loaded_dict["xp_14"] = xp_sheet[14]
    loaded_dict["xp_15"] = xp_sheet[15]
    loaded_dict["xp_16"] = xp_sheet[16]
    loaded_dict["xp_17"] = xp_sheet[17]
    loaded_dict["xp_18"] = xp_sheet[18]
    loaded_dict["xp_19"] = xp_sheet[19]
    loaded_dict["xp_20"] = xp_sheet[20]
    loaded_dict["xp_21"] = xp_sheet[21]
    loaded_dict["xp_22"] = xp_sheet[22]
    loaded_dict["xp_23"] = xp_sheet[23]
    loaded_dict["xp_24"] = xp_sheet[24]
    loaded_dict["xp_25"] = xp_sheet[25]
    loaded_dict["xp_26"] = xp_sheet[26]
    loaded_dict["xp_27"] = xp_sheet[27]
    loaded_dict["xp_28"] = xp_sheet[28]
    loaded_dict["xp_29"] = xp_sheet[29]
    loaded_dict["xp_30"] = xp_sheet[30]
    loaded_dict["xp_31"] = xp_sheet[31]
    loaded_dict["xp_32"] = xp_sheet[32]
    loaded_dict["xp_33"] = xp_sheet[33]
    loaded_dict["xp_34"] = xp_sheet[34]
    loaded_dict["xp_35"] = xp_sheet[35]
    loaded_dict["xp_36"] = xp_sheet[36]
    loaded_dict["xp_37"] = xp_sheet[37]
    loaded_dict["xp_38"] = xp_sheet[38]
    loaded_dict["xp_39"] = xp_sheet[39]
    loaded_dict["xp_40"] = xp_sheet[40]
    loaded_dict["xp_41"] = xp_sheet[41]
    loaded_dict["xp_42"] = xp_sheet[42]
    loaded_dict["xp_43"] = xp_sheet[43]
    loaded_dict["xp_44"] = xp_sheet[44]
    loaded_dict["xp_45"] = xp_sheet[45]
    loaded_dict["xp_46"] = xp_sheet[46]
    loaded_dict["xp_47"] = xp_sheet[47]
    loaded_dict["xp_48"] = xp_sheet[48]
    loaded_dict["xp_49"] = xp_sheet[49]
    loaded_dict["xp_50"] = xp_sheet[50]
    loaded_dict["xp_51"] = xp_sheet[51]
    loaded_dict["xp_52"] = xp_sheet[52]
    loaded_dict["xp_53"] = xp_sheet[53]
    loaded_dict["xp_54"] = xp_sheet[54]
    loaded_dict["xp_55"] = xp_sheet[55]
    loaded_dict["xp_56"] = xp_sheet[56]
    loaded_dict["xp_57"] = xp_sheet[57]
    loaded_dict["xp_58"] = xp_sheet[58]
    loaded_dict["xp_59"] = xp_sheet[59]
    loaded_dict["xp_60"] = xp_sheet[60]
    loaded_dict["xp_61"] = xp_sheet[61]
    loaded_dict["xp_62"] = xp_sheet[62]
    loaded_dict["xp_63"] = xp_sheet[63]
    loaded_dict["xp_64"] = xp_sheet[64]
    loaded_dict["xp_65"] = xp_sheet[65]
    loaded_dict["xp_66"] = xp_sheet[66]
    loaded_dict["xp_67"] = xp_sheet[67]
    loaded_dict["xp_68"] = xp_sheet[68]
    loaded_dict["xp_69"] = xp_sheet[69]
    loaded_dict["xp_70"] = xp_sheet[70]
    loaded_dict["xp_71"] = xp_sheet[71]
    loaded_dict["xp_72"] = xp_sheet[72]
    loaded_dict["xp_73"] = xp_sheet[73]
    loaded_dict["xp_74"] = xp_sheet[74]
    loaded_dict["xp_75"] = xp_sheet[75]
    loaded_dict["xp_76"] = xp_sheet[76]
    loaded_dict["xp_77"] = xp_sheet[77]
    loaded_dict["xp_78"] = xp_sheet[78]
    loaded_dict["xp_79"] = xp_sheet[79]
    loaded_dict["xp_80"] = xp_sheet[80]
    loaded_dict["xp_81"] = xp_sheet[81]
    loaded_dict["xp_82"] = xp_sheet[82]
    loaded_dict["xp_83"] = xp_sheet[83]
    loaded_dict["xp_84"] = xp_sheet[84]
    loaded_dict["xp_85"] = xp_sheet[85]
    loaded_dict["xp_86"] = xp_sheet[86]
    loaded_dict["xp_87"] = xp_sheet[87]
    loaded_dict["xp_88"] = xp_sheet[88]
    loaded_dict["xp_89"] = xp_sheet[89]
    loaded_dict["xp_90"] = xp_sheet[90]
    loaded_dict["xp_91"] = xp_sheet[91]
    loaded_dict["xp_92"] = xp_sheet[92]
    loaded_dict["xp_93"] = xp_sheet[93]
    loaded_dict["xp_94"] = xp_sheet[94]
    loaded_dict["xp_95"] = xp_sheet[95]
    loaded_dict["xp_96"] = xp_sheet[96]
    loaded_dict["xp_97"] = xp_sheet[97]
    loaded_dict["xp_98"] = xp_sheet[98]
    loaded_dict["xp_99"] = xp_sheet[99]
    loaded_dict["xp_100"] = xp_sheet[100]

    return loaded_dict
